#!/usr/bin/env python3
"""
skill-uplift.py — Skill uplift evaluator for hplan.

각 스킬에 대해 (skill-on / skill-off) 두 모드로 trigger eval을 실행하여
uplift = on_pass_rate - off_pass_rate 를 측정한다. ETH 취리히 -3%p 함정
(스킬 추가가 base Claude 의 라우팅을 오히려 깎는 현상) 을 자동 감지하고,
uplift < threshold 인 스킬을 quarantine 후보로 표시한다.

사용:
    export ANTHROPIC_API_KEY=...
    python3 evals/skill-uplift.py --skill velocity-baseline
    python3 evals/skill-uplift.py --all
    python3 evals/skill-uplift.py --dry-run                  # API 호출 없이 카탈로그 검증만
    python3 evals/skill-uplift.py --all --threshold 0.05     # uplift +5pp 미만 시 quarantine

산출물:
    evals/uplift-results-<version>.json
    quarantine 후보 리스트 (stdout)

비결정성:
    --runs-per-query 3 같이 다회 권장. 단 비용은 (on+off) 2배.

Rule 5 준수:
    LLM 응답은 1줄 라우팅 결정만 (분류). uplift 계산·judge·quarantine 결정은
    100% 결정론. complexity·routing·retry 정책에 LLM 호출 0.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGINS = ["hplan", "discover", "architect", "deliver", "measure", "learn", "operate", "track", "craft"]


def load_skill_catalog() -> dict[str, str]:
    catalog: dict[str, str] = {}
    for plugin in PLUGINS:
        skills_dir = REPO_ROOT / plugin / "skills"
        if not skills_dir.exists():
            continue
        for skill_md in skills_dir.glob("*/SKILL.md"):
            text = skill_md.read_text(encoding="utf-8")
            name_m = re.search(r"^name:\s*(\S+)", text, re.MULTILINE)
            desc_m = re.search(r"^description:\s*\"(.+?)\"\s*$", text, re.MULTILINE | re.DOTALL)
            if name_m and desc_m:
                catalog[name_m.group(1)] = desc_m.group(1).replace("\n", " ").strip()
    return catalog


PROMPT_TEMPLATE = """You are simulating the Claude Code skill auto-loading mechanism.

Given a user query and a catalog of available skills, decide WHICH SKILL (if any) should be auto-loaded to handle the query.

Available skills (name → description):
{catalog}

User query:
{query}

Reply with exactly ONE line in this format:
SKILL: <skill_name>

If no skill matches, reply:
SKILL: none

Do not explain. Just one line."""


def catalog_block(catalog: dict[str, str], exclude: str | None = None) -> str:
    items = sorted((n, d) for n, d in catalog.items() if n != exclude)
    return "\n".join(f"- {n}: {d}" for n, d in items)


def call_claude(client, model: str, query: str, block: str) -> str:
    msg = client.messages.create(
        model=model,
        max_tokens=64,
        messages=[{"role": "user", "content": PROMPT_TEMPLATE.format(catalog=block, query=query)}],
    )
    raw = msg.content[0].text.strip()
    m = re.search(r"SKILL:\s*([A-Za-z0-9_\-]+)", raw)
    return m.group(1) if m else "none"


def judge(predicted: str, expected_skill: str, should_trigger: bool, mode: str) -> bool:
    """결정론 라우팅 정답 판정.

    on-mode (skill in catalog):
      - should_trigger=True  → predicted must equal expected_skill (target hit)
      - should_trigger=False → predicted must NOT equal expected_skill (false positive 회피)

    off-mode (skill removed from catalog):
      - should_trigger=True  → predicted must be "none" (정답 fallback when intended skill 부재)
      - should_trigger=False → predicted must NOT equal expected_skill (same as on-mode false case)

    uplift = on_pass_rate - off_pass_rate 가 실제 의미를 가지려면:
      - on-mode 가 정확히 라우팅 (target hit) + off-mode 가 "none" 으로 fallback 못 함 → uplift 양수
      - on-mode 가 정확 + off-mode 도 "none" 잘 fallback → uplift ≈ 0 (스킬 추가 가치 약함)
      - on-mode 가 false positive 증가 (ETH 취리히 -3pp 함정) → uplift 음수 (quarantine)
    """
    if mode == "on":
        if should_trigger:
            return predicted == expected_skill
        return predicted != expected_skill
    # off-mode
    if should_trigger:
        return predicted == "none"
    return predicted != expected_skill


def evaluate_skill(client, model, catalog, skill_name: str, queries: list[dict], mode: str, runs: int) -> dict:
    block = catalog_block(catalog, exclude=None if mode == "on" else skill_name)
    passed = 0
    detail = []
    for q in queries:
        triggers = 0
        for _ in range(runs):
            predicted = call_claude(client, model, q["query"], block)
            if judge(predicted, skill_name, q["should_trigger"], mode):
                triggers += 1
        rate = triggers / runs
        ok = rate >= 0.5
        passed += int(ok)
        detail.append({"query": q["query"], "rate": rate, "pass": ok})
    return {"mode": mode, "pass": passed, "total": len(queries), "pass_rate": passed / max(1, len(queries)), "detail": detail}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="claude-haiku-4-5-20251001")
    ap.add_argument("--input", default=str(REPO_ROOT / "evals" / "trigger-evals.json"))
    ap.add_argument("--output", default=str(REPO_ROOT / "evals" / "uplift-results.json"))
    ap.add_argument("--skill", help="단일 스킬 평가")
    ap.add_argument("--all", action="store_true", help="모든 신규 스킬 평가")
    ap.add_argument("--runs-per-query", type=int, default=1)
    ap.add_argument("--threshold", type=float, default=0.05, help="quarantine 임계치 (기본 +5pp)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    catalog = load_skill_catalog()
    print(f"📚 Loaded {len(catalog)} skill descriptions", file=sys.stderr)

    if not args.skill and not args.all:
        print("❌ --skill <name> 또는 --all 필요", file=sys.stderr)
        return 2

    eval_data = json.loads(Path(args.input).read_text())
    targets = [args.skill] if args.skill else [s["skill"] for s in eval_data]
    eval_by_skill = {s["skill"]: s["queries"] for s in eval_data}

    if args.dry_run:
        for t in targets:
            present = "✅" if t in catalog else "❌ NOT IN CATALOG"
            queries = len(eval_by_skill.get(t, []))
            print(f"  {t}: {present}  queries={queries}")
        return 0

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("❌ ANTHROPIC_API_KEY 환경 변수 필요", file=sys.stderr)
        return 2
    try:
        import anthropic
    except ImportError:
        print("❌ pip install anthropic", file=sys.stderr)
        return 2

    client = anthropic.Anthropic()
    t0 = time.time()
    results = []
    quarantine = []

    for skill_name in targets:
        if skill_name not in eval_by_skill:
            print(f"⚠️  {skill_name}: trigger-evals.json 에 시드 없음 — skip", file=sys.stderr)
            continue
        if skill_name not in catalog:
            print(f"⚠️  {skill_name}: SKILL.md 카탈로그에 없음 — skip", file=sys.stderr)
            continue

        queries = eval_by_skill[skill_name]
        on = evaluate_skill(client, args.model, catalog, skill_name, queries, "on", args.runs_per_query)
        off = evaluate_skill(client, args.model, catalog, skill_name, queries, "off", args.runs_per_query)
        uplift = on["pass_rate"] - off["pass_rate"]
        verdict = "promote" if uplift >= args.threshold else "quarantine"
        if verdict == "quarantine":
            quarantine.append(skill_name)

        print(f"  {skill_name}: on={on['pass']}/{on['total']} off={off['pass']}/{off['total']} uplift={uplift:+.2%} → {verdict}")
        results.append({
            "skill": skill_name,
            "on": on,
            "off": off,
            "uplift": uplift,
            "verdict": verdict,
        })

    elapsed = time.time() - t0
    out = {
        "summary": {
            "threshold": args.threshold,
            "model": args.model,
            "runs_per_query": args.runs_per_query,
            "evaluated": len(results),
            "quarantine_count": len(quarantine),
            "quarantine_skills": quarantine,
            "elapsed_seconds": round(elapsed, 1),
        },
        "results": results,
    }
    Path(args.output).write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(f"\n📊 evaluated={len(results)}  quarantine={len(quarantine)}  → {args.output}")
    if quarantine:
        print(f"⚠️  Quarantine 후보: {', '.join(quarantine)}")
    return 0 if not quarantine else 1


if __name__ == "__main__":
    raise SystemExit(main())
