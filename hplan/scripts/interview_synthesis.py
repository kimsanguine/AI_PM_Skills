#!/usr/bin/env python3
"""Interview Synthesis Adapter — import AI-clustered interview output, force human tagging.

Why:
- 2026 reality: 78% of PM teams use AI for interview synthesis (BuildBetter,
  Perspective AI, and similar tools). Forbidding AI synthesis is anti-modern.
- hplan's rule still stands: evidence strength tagging is a human act. AI
  extracts quotes; humans assign weak/medium/strong + Push/Pull/Habit/Anxiety.

Workflow:
1. AI synthesis tool (BuildBetter MCP, Perspective AI, ...) exports JSON of
   themes + verbatim quotes per interview.
2. `interview_synthesis.py import <ai_export.json>` ingests it into
   `harness/evidence/snapshots.jsonl` with status="awaiting_human_tag".
3. Operator runs `interview_synthesis.py tag <quote_id> --strength strong
   --axes push,anxiety` to commit human judgment.
4. `interview_synthesis.py audit` returns the 5-vs-3 repeated-Push check
   from SKILL.md ("5 interviews can reveal a repeated pattern, not prove
   PMF. If 3 of 5 interviews repeat a strong Push signal, proceed.").

Expected AI export JSON shape:

  {
    "source": "buildbetter",
    "interviews": [
      {
        "person": "ICP candidate 1",
        "date": "2026-05-09",
        "quotes": [
          {"text": "지난주에 또 30분 날렸어요...", "theme": "manual workaround"},
          {"text": "이거 안 되면 영업 못 따요", "theme": "economic pain"}
        ]
      }
    ]
  }
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


VALID_STRENGTHS = {"strong", "medium", "weak"}
VALID_AXES = {"push", "pull", "habit", "anxiety", "workaround", "trigger"}


def snapshots_path(root: Path) -> Path:
    return root / "harness" / "evidence" / "snapshots.jsonl"


def import_ai_export(root: Path, export_path: Path) -> dict:
    data = json.loads(export_path.read_text(encoding="utf-8"))
    out_path = snapshots_path(root)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    imported = 0
    with out_path.open("a", encoding="utf-8") as f:
        for interview in data.get("interviews", []):
            person = interview.get("person", "anonymous")
            int_date = interview.get("date", datetime.now(timezone.utc).date().isoformat())
            for quote in interview.get("quotes", []):
                qhash = hashlib.sha1(
                    f"{person}{int_date}{quote.get('text','')}".encode("utf-8")
                ).hexdigest()[:8]
                payload = {
                    "id": f"q-{qhash}",
                    "person": person,
                    "date": int_date,
                    "theme": quote.get("theme"),
                    "quote": quote.get("text", ""),
                    "source": data.get("source", "ai-export"),
                    "status": "awaiting_human_tag",
                    "strength": None,
                    "axes": [],
                }
                f.write(json.dumps(payload, ensure_ascii=False) + "\n")
                imported += 1
    return {"imported": imported, "path": str(out_path)}


def read_all(root: Path) -> list[dict]:
    p = snapshots_path(root)
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def tag(root: Path, quote_id: str, strength: str, axes: list[str]) -> dict:
    if strength not in VALID_STRENGTHS:
        raise SystemExit(f"invalid strength: {strength}")
    for a in axes:
        if a not in VALID_AXES:
            raise SystemExit(f"invalid axis: {a}")
    entries = read_all(root)
    found = None
    for e in entries:
        if e["id"] == quote_id:
            e["strength"] = strength
            e["axes"] = axes
            e["status"] = "tagged"
            e["tagged_at"] = datetime.now(timezone.utc).isoformat()
            found = e
            break
    if not found:
        raise SystemExit(f"quote id not found: {quote_id}")
    snapshots_path(root).write_text(
        "\n".join(json.dumps(e, ensure_ascii=False) for e in entries) + "\n",
        encoding="utf-8",
    )
    return found


def audit(root: Path) -> dict:
    entries = read_all(root)
    by_person = defaultdict(list)
    for e in entries:
        by_person[e["person"]].append(e)

    untagged = [e for e in entries if e["status"] == "awaiting_human_tag"]
    tagged = [e for e in entries if e["status"] == "tagged"]
    by_strength = Counter(e["strength"] for e in tagged if e["strength"])
    push_signals = [e for e in tagged if "push" in (e.get("axes") or []) and e.get("strength") == "strong"]
    persons_with_strong_push = sorted({e["person"] for e in push_signals})

    # SKILL.md rule: "If 3 of 5 interviews repeat a strong Push signal, proceed."
    interview_count = len(by_person)
    proceed = interview_count >= 5 and len(persons_with_strong_push) >= 3

    verdict = "PROCEED_TO_PRODUCT_GATE" if proceed else "INTERVIEW_OR_HOLD"

    return {
        "interviews": interview_count,
        "tagged_quotes": len(tagged),
        "untagged_quotes": len(untagged),
        "by_strength": dict(by_strength),
        "persons_with_strong_push": persons_with_strong_push,
        "verdict": verdict,
        "guidance": _audit_guidance(verdict, interview_count, persons_with_strong_push, untagged),
    }


def _audit_guidance(verdict, interview_count, persons_push, untagged) -> list[str]:
    out = []
    if untagged:
        out.append(f"{len(untagged)} untagged quote(s) — AI synthesis is not evidence until a human assigns strength/axes.")
    if interview_count < 5:
        out.append(f"Only {interview_count} interview(s). Reach 5 before drawing pattern conclusions.")
    if interview_count >= 5 and len(persons_push) < 3:
        out.append(f"5+ interviews but only {len(persons_push)} repeated strong Push. Re-interview ICP variants or pivot.")
    if verdict == "PROCEED_TO_PRODUCT_GATE":
        out.append("Repeated Push pattern confirmed across 3+ of 5+ interviews. Product Gate may begin.")
    return out


def parse_args():
    p = argparse.ArgumentParser(description="hplan interview synthesis adapter")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_imp = sub.add_parser("import", help="Import an AI synthesis export JSON")
    p_imp.add_argument("export_path")
    p_imp.add_argument("--root", default=".")

    p_tag = sub.add_parser("tag", help="Human-tag a quote with strength + axes")
    p_tag.add_argument("quote_id")
    p_tag.add_argument("--strength", required=True, choices=sorted(VALID_STRENGTHS))
    p_tag.add_argument("--axes", default="", help="Comma-separated axes: push,pull,habit,anxiety,workaround,trigger")
    p_tag.add_argument("--root", default=".")

    p_audit = sub.add_parser("audit", help="Run the 5-vs-3 repeated Push check")
    p_audit.add_argument("--root", default=".")

    p_list = sub.add_parser("list", help="List all snapshots")
    p_list.add_argument("--root", default=".")
    p_list.add_argument("--untagged", action="store_true")

    return p.parse_args()


def main():
    args = parse_args()
    root = Path(args.root).resolve()
    if args.cmd == "import":
        print(json.dumps(import_ai_export(root, Path(args.export_path)), ensure_ascii=False, indent=2))
    elif args.cmd == "tag":
        axes = [a.strip() for a in args.axes.split(",") if a.strip()]
        print(json.dumps(tag(root, args.quote_id, args.strength, axes), ensure_ascii=False, indent=2))
    elif args.cmd == "audit":
        print(json.dumps(audit(root), ensure_ascii=False, indent=2))
    elif args.cmd == "list":
        for e in read_all(root):
            if args.untagged and e["status"] != "awaiting_human_tag":
                continue
            print(json.dumps(e, ensure_ascii=False))


if __name__ == "__main__":
    main()
