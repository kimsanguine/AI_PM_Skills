#!/usr/bin/env python3
"""
validate-mermaid.py — PRD의 두 mermaid 다이어그램(workflow/userflow) 정합성 검증.

사용자 노하우(2026-02-16 메모리)를 결정론화:
  mermaid workflow(시스템 관점) + mermaid userflow(유저 관점) 두 다이어그램의
  노드 매핑·요구사항 누락 여부를 LLM 추정 없이 파싱·검증한다.

이 스크립트는 hplan의 cogs-sentinel과 같은 가족이다:
  → 사람/모델이 "맞춰봤다"고 말하는 검증을 Python으로 결정론화.

사용:
  python scripts/validate-mermaid.py path/to/PRD.md
  python scripts/validate-mermaid.py path/to/PRD.md --strict   # orphan 0건 강제
종료 코드:
  0  통과
  1  정합성 위반 (orphan / missing 발견)
  2  파싱 불가 (다이어그램 또는 요구사항 섹션 없음)
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

# --- mermaid 노드 파서 ----------------------------------------------------

# 매칭: A[Label], A(Label), A{Label}, A((Label)), A>Label]
NODE_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\s*[\[\(\{>]+([^\]\)\}\n]+?)[\]\)\}]")
EDGE_ID_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*-->|--\s*([A-Za-z_][A-Za-z0-9_]*)")


STOPWORDS = {
    # 영어
    "a", "an", "the", "of", "to", "and", "or", "for", "in", "on", "at",
    "by", "is", "are", "be", "user", "users", "see", "view", "open",
    "trigger", "start", "end", "step", "optional",
    # 한국어 (잡음 토큰)
    "및", "또는", "수", "에", "을", "를", "이", "가", "은", "는", "의", "로",
    "후", "시", "측", "관점", "기본", "처리", "수행", "확인", "전송", "감지",
}


def _tokens(text: str) -> set[str]:
    """라벨/요구사항을 의미 토큰 셋으로 정규화."""
    # 한글/영문/숫자 외 문자는 공백으로
    norm = re.sub(r"[^0-9A-Za-z가-힣]+", " ", text.lower())
    raw = norm.split()
    # 짧은 단어 + 스톱워드 제거
    return {w for w in raw if len(w) >= 2 and w not in STOPWORDS}


@dataclass(frozen=True)
class Node:
    nid: str
    label: str

    @property
    def normalized(self) -> str:
        s = self.label.lower()
        return re.sub(r"[\s\-_/().·,]+", "", s)

    @property
    def token_set(self) -> frozenset[str]:
        return frozenset(_tokens(self.label))


def extract_mermaid_blocks(md: str) -> dict[str, str]:
    """fenced ```mermaid 블록을 찾고, 가장 가까운 직전 헤딩으로 종류를 추정한다."""
    blocks: dict[str, str] = {}
    fence_re = re.compile(r"```mermaid\s*\n(?P<body>.*?)\n```", re.DOTALL)
    heading_re = re.compile(r"^#{1,6}\s+(.+)$", re.MULTILINE)
    for m in fence_re.finditer(md):
        body = m.group("body")
        # 직전 헤딩을 fence 시작점 앞에서 역탐색
        prefix = md[: m.start()]
        last_heading = ""
        for h in heading_re.finditer(prefix):
            last_heading = h.group(1)
        kind = _classify(last_heading, body)
        # 같은 종류가 여러 번 나오면 첫 블록만 채택 (정합성 검증의 기준)
        blocks.setdefault(kind, body)
    return blocks


def _classify(heading: str, body: str) -> str:
    """헤딩만으로 분류한다. 본문에 우연히 들어간 키워드는 무시."""
    h = heading.lower()
    if "userflow" in h or "user flow" in h or "유저" in h or "사용자" in h:
        return "userflow"
    if "workflow" in h or "system" in h or "시스템" in h or "sequence" in h:
        return "workflow"
    # 헤딩에 단서가 없으면 본문 키워드를 fallback으로 사용
    b = body.lower()
    if "userflow" in b:
        return "userflow"
    return "workflow"


def parse_nodes(body: str) -> list[Node]:
    seen: dict[str, Node] = {}
    for m in NODE_RE.finditer(body):
        nid, label = m.group(1), m.group(2).strip()
        seen.setdefault(nid, Node(nid=nid, label=label))
    return list(seen.values())


# --- 요구사항 섹션 파서 ---------------------------------------------------

REQ_SECTION_RE = re.compile(
    r"(?:^|\n)#{1,6}\s*(?:requirements?|요구\s*사항|기능\s*요구|핵심\s*요구).*?\n(.*?)(?=\n#{1,6}\s|\Z)",
    re.IGNORECASE | re.DOTALL,
)
REQ_LINE_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(.+?)\s*$", re.MULTILINE)


def parse_requirements(md: str) -> list[str]:
    section = REQ_SECTION_RE.search(md)
    if not section:
        return []
    body = section.group(1)
    return [line.strip() for line in REQ_LINE_RE.findall(body) if line.strip()]


# --- 정합성 검증 ----------------------------------------------------------

MATCH_THRESHOLD = 0.34  # 의미 토큰 중 1/3 이상 겹치면 매핑된 것으로 간주


def _overlaps(a: set[str] | frozenset[str], b: set[str] | frozenset[str]) -> bool:
    if not a or not b:
        return False
    inter = a & b
    if not inter:
        return False
    # 한쪽 기준으로 1/3 이상 겹치면 매칭
    return len(inter) / max(1, min(len(a), len(b))) >= MATCH_THRESHOLD


def find_orphans(workflow: list[Node], userflow: list[Node]) -> tuple[list[Node], list[Node]]:
    """workflow에만 있는 노드 vs userflow에만 있는 노드 (토큰 셋 매칭)."""
    workflow_only = [n for n in workflow if not any(_overlaps(n.token_set, m.token_set) for m in userflow)]
    userflow_only = [n for n in userflow if not any(_overlaps(n.token_set, m.token_set) for m in workflow)]
    return workflow_only, userflow_only


def find_missing_requirements(reqs: list[str], all_nodes: list[Node]) -> list[str]:
    """workflow ∪ userflow의 어느 노드에도 매핑되지 않은 요구사항."""
    missing: list[str] = []
    for req in reqs:
        rt = set(_tokens(req))
        if not any(_overlaps(rt, n.token_set) for n in all_nodes):
            missing.append(req)
    return missing


# --- 메인 ----------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description="Validate PRD mermaid diagram consistency.")
    ap.add_argument("prd", type=Path, help="PRD 마크다운 파일 경로")
    ap.add_argument("--strict", action="store_true", help="orphan 1건이라도 있으면 실패")
    args = ap.parse_args()

    if not args.prd.exists():
        print(f"❌ PRD 파일 없음: {args.prd}", file=sys.stderr)
        return 2

    md = args.prd.read_text(encoding="utf-8")
    blocks = extract_mermaid_blocks(md)

    if "workflow" not in blocks or "userflow" not in blocks:
        print("❌ workflow + userflow 두 mermaid 다이어그램이 모두 필요합니다.")
        print(f"   감지된 블록: {sorted(blocks.keys()) or '없음'}")
        return 2

    wf_nodes = parse_nodes(blocks["workflow"])
    uf_nodes = parse_nodes(blocks["userflow"])
    reqs = parse_requirements(md)

    workflow_only, userflow_only = find_orphans(wf_nodes, uf_nodes)
    missing_reqs = find_missing_requirements(reqs, wf_nodes + uf_nodes) if reqs else []

    print(f"📊 PRD 정합성 검증: {args.prd}")
    print(f"   workflow 노드 {len(wf_nodes)}개 · userflow 노드 {len(uf_nodes)}개 · requirements {len(reqs)}개")

    issues = 0
    if workflow_only:
        issues += 1
        print(f"⚠️  workflow에만 있는 노드 ({len(workflow_only)}):")
        for n in workflow_only:
            print(f"     - {n.nid}: {n.label}")
    if userflow_only:
        issues += 1
        print(f"⚠️  userflow에만 있는 노드 ({len(userflow_only)}):")
        for n in userflow_only:
            print(f"     - {n.nid}: {n.label}")
    if missing_reqs:
        issues += 1
        print(f"❌ 다이어그램에 매핑되지 않은 요구사항 ({len(missing_reqs)}):")
        for r in missing_reqs:
            print(f"     - {r}")

    if issues == 0:
        print("✅ 정합성 통과: workflow ↔ userflow ↔ requirements 매핑 일관")
        return 0

    # strict 모드: orphan/missing 모두 실패
    if args.strict:
        return 1
    # 기본: missing requirement만 실패 (orphan은 경고)
    return 1 if missing_reqs else 0


if __name__ == "__main__":
    raise SystemExit(main())
