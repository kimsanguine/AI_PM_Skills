#!/usr/bin/env python3
"""context_quality_scorer.py — Context Quality Score (CQS) for hplan.

Scores the richness and reliability of PM research context BEFORE
the evidence rubric runs. Analogous to RAGAS context recall: measures
whether the input context is trustworthy enough to produce meaningful
rubric scores.

Usage:
    python3 hplan/scripts/context_quality_scorer.py harness/context-intake.md
    python3 hplan/scripts/context_quality_scorer.py --json harness/context-intake.md

Output:
    Human-readable report (default) or JSON (--json flag).

CQS dimensions (100 pts total):
    1. Interview Volume     25 pts  — how many direct interviews
    2. Segment Diversity    20 pts  — how many ICP segments covered
    3. Evidence Recency     20 pts  — age of most recent direct evidence
    4. Source Independence  15 pts  — variety of evidence source types
    5. Competitor Coverage  10 pts  — depth of competitive context
    6. Workaround Specificity 10 pts — quality of workaround evidence

Gate verdicts:
    CQS >= 75  → HIGH confidence  ✅
    55 <= CQS < 75 → MODERATE confidence ⚠️
    30 <= CQS < 55 → LOW confidence ⚠️  (proceed with caution)
    CQS < 30   → INSUFFICIENT — gate run blocked
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Scoring tables
# ---------------------------------------------------------------------------

def score_interview_volume(count: int) -> tuple[int, str]:
    """25 pts. Based on YC/Torres: 5+ interviews = pattern convergence."""
    if count == 0:
        return 0, "0 interviews — LLM will speculate on customer evidence"
    if count <= 2:
        return 5, f"{count} interview(s) — very limited signal"
    if count <= 4:
        return 12, f"{count} interviews — some signal, below convergence threshold (5)"
    if count <= 9:
        return 20, f"{count} interviews — pattern convergence likely"
    return 25, f"{count} interviews — strong sample"


def score_segment_diversity(icp_segment: str, icp_anti: str) -> tuple[int, str]:
    """20 pts. Penalizes demographic-only ICPs and single-segment research."""
    if not icp_segment or icp_segment.strip() in ("", '""'):
        return 0, "ICP not defined"
    # Weak signal: purely demographic language
    demographic_terms = ["나이", "직종", "국가", "성별", "age", "job title", "country"]
    if any(t in icp_segment.lower() for t in demographic_terms):
        return 4, "ICP appears demographic-only — behavioral description required"
    # Good signal: behavioral language
    behavioral_terms = ["weekly", "monthly", "매주", "매월", "반복", "건", "회"]
    has_behavioral = any(t in icp_segment.lower() for t in behavioral_terms)
    has_anti = bool(icp_anti and icp_anti.strip() not in ("", '""'))
    if has_behavioral and has_anti:
        return 20, "Behavioral ICP with anti-ICP defined — strong"
    if has_behavioral:
        return 15, "Behavioral ICP defined — add anti-ICP for full score"
    return 8, "ICP exists but behavioral context unclear"


def score_evidence_recency(event_recency: str) -> tuple[int, str]:
    """20 pts. Recent painful events are stronger buying signals."""
    mapping = {
        "within_7d": (20, "within 7 days — very fresh signal"),
        "within_30d": (20, "within 30 days — fresh signal"),
        "within_90d": (17, "within 90 days — acceptable"),
        "older": (5, "older than 90 days — signal may have decayed"),
        "": (0, "recency not specified"),
    }
    key = (event_recency or "").strip().lower().strip('"')
    return mapping.get(key, (0, f"unrecognized recency value: {event_recency!r}"))


def score_source_independence(
    interview_notes: str,
    workaround_tool: str,
    direct_competitors: str,
) -> tuple[int, str]:
    """15 pts. +5 per evidence type: interview / public review / market data."""
    types_found = []

    # Type 1: interview / direct observation
    if interview_notes and len(interview_notes.strip().strip('"')) > 20:
        types_found.append("interviews")

    # Type 2: public reviews / community signals (look for platform names)
    review_signals = ["G2", "Reddit", "Hacker News", "ProductHunt", "리뷰", "커뮤니티"]
    if any(s in (workaround_tool + direct_competitors) for s in review_signals):
        types_found.append("public reviews")

    # Type 3: market data / competitor reports
    market_signals = ["리포트", "report", "ARR", "revenue", "users", "사용자 수", "%"]
    combined = (direct_competitors or "") + (workaround_tool or "")
    if any(s in combined for s in market_signals):
        types_found.append("market data")

    pts = min(len(types_found) * 5, 15)
    if types_found:
        return pts, f"Sources: {', '.join(types_found)}"
    return 0, "Single source type — corroboration needed"


def score_competitor_coverage(direct_competitors: str) -> tuple[int, str]:
    """10 pts. Rewards depth of competitive context."""
    if not direct_competitors or direct_competitors.strip() in ("", '""', "없음", "none"):
        return 0, "No competitor analysis — market validation missing"
    # Check for depth signals
    depth_signals = ["pricing_tier", "primary_segment", "$", "ARR", "users", "세그먼트"]
    has_depth = any(s in direct_competitors for s in depth_signals)
    if has_depth:
        return 10, "Competitor analysis with pricing/segment detail"
    return 4, "Competitors mentioned but without pricing/segment analysis"


def score_workaround_specificity(workaround_tool: str, workaround_pain: str) -> tuple[int, str]:
    """10 pts. Rewards specific tool + pain pairing over generic descriptions."""
    if not workaround_tool or workaround_tool.strip() in ("", '""'):
        return 0, "No workaround documented — demand signal missing"
    # Generic signals
    generic = ["그냥 참", "없음", "none", "모름"]
    if any(g in workaround_tool.lower() for g in generic):
        return 0, "Workaround = 'nothing' — suggests no demand"
    # Specific tool
    has_tool = len(workaround_tool.strip()) > 5
    # Specific pain (quoted speech or numbers)
    has_pain_quote = bool(
        workaround_pain and (
            any(c in workaround_pain for c in ['"', "'", "분", "min", "건"])
        )
    )
    if has_tool and has_pain_quote:
        return 10, "Specific tool + quantified pain — strong workaround evidence"
    if has_tool:
        return 5, "Tool identified — add quantified pain for full score"
    return 2, "Workaround mentioned but vague"


# ---------------------------------------------------------------------------
# YAML-lite parser (no external deps)
# ---------------------------------------------------------------------------

def extract_field(text: str, key: str) -> str:
    """Extract first occurrence of 'key: value' from text.

    Handles:
      key: ""                  → ""  (empty)
      key: "" # comment        → ""  (empty, comment stripped)
      key: "actual value"      → "actual value"
      key: bare value # note   → "bare value"
    """
    pattern = rf'^{re.escape(key)}:\s*(.+)$'
    m = re.search(pattern, text, re.MULTILINE)
    if not m:
        return ""
    val = m.group(1).strip()

    # Empty quoted string (possibly followed by comment): "", '' , "" # ...
    if re.match(r'^(["\'])\1\s*(#.*)?$', val):
        return ""

    # Quoted string with content: "value" or 'value'
    quoted = re.match(r'^(["\'])(.*)\1\s*(#.*)?$', val)
    if quoted:
        inner = quoted.group(2)
        return inner if inner not in ('""', "''") else ""

    # Unquoted: strip trailing comment
    val = re.sub(r'\s+#.*$', '', val).strip()
    return val


def extract_int_field(text: str, key: str) -> int:
    val = extract_field(text, key)
    try:
        return int(val)
    except (ValueError, TypeError):
        return 0


def extract_block(text: str, key: str) -> str:
    """Extract multi-line block after 'key: |' marker, stripping comment lines."""
    pattern = rf'^{re.escape(key)}:\s*\|(.+?)(?=^\S|\Z)'
    m = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if not m:
        return ""
    lines = [
        ln for ln in m.group(1).splitlines()
        if ln.strip() and not ln.strip().startswith("#")
    ]
    return "\n".join(lines).strip()


# ---------------------------------------------------------------------------
# Main scorer
# ---------------------------------------------------------------------------

class CQSResult:
    def __init__(self, scores: dict[str, tuple[int, str]], total: int):
        self.scores = scores
        self.total = total

    @property
    def verdict(self) -> str:
        if self.total >= 75:
            return "HIGH"
        if self.total >= 55:
            return "MODERATE"
        if self.total >= 30:
            return "LOW"
        return "INSUFFICIENT"

    @property
    def badge(self) -> str:
        return {
            "HIGH":         "✅ High confidence — proceed to evidence rubric",
            "MODERATE":     "⚠️  Moderate confidence — rubric results less reliable",
            "LOW":          "⚠️  Low confidence — consider more interviews first",
            "INSUFFICIENT": "🚫 Insufficient context — gate blocked until CQS ≥ 30",
        }[self.verdict]

    def to_dict(self) -> dict:
        return {
            "cqs_total": self.total,
            "verdict": self.verdict,
            "scores": {k: {"pts": v[0], "note": v[1]} for k, v in self.scores.items()},
        }

    def print_report(self, idea: str = "") -> None:
        print(f"\nhplan Context Quality Score (CQS)")
        if idea:
            print(f"Idea: {idea}")
        print(f"{'─' * 52}")
        max_pts = {
            "interview_volume": 25,
            "segment_diversity": 20,
            "evidence_recency": 20,
            "source_independence": 15,
            "competitor_coverage": 10,
            "workaround_specificity": 10,
        }
        for key, (pts, note) in self.scores.items():
            bar = "█" * pts + "░" * (max_pts[key] - pts)
            print(f"  {key:<26} {pts:>3}/{max_pts[key]:>2}  {note}")
        print(f"{'─' * 52}")
        print(f"  TOTAL                      {self.total:>3}/100")
        print(f"\n  {self.badge}\n")
        if self.verdict == "INSUFFICIENT":
            print("  Minimum to proceed: CQS ≥ 30")
            print("  Fastest path: add 1 interview (5 pt) + recent event (20 pt)")
            print("  → interview_count: 1, event_recency: within_30d\n")


def score_file(path: Path) -> CQSResult:
    text = path.read_text(encoding="utf-8")

    idea                = extract_field(text, "idea")
    icp_segment         = extract_field(text, "icp_segment")
    icp_anti            = extract_field(text, "icp_anti")
    event_recency       = extract_field(text, "event_recency")
    workaround_tool     = extract_field(text, "workaround_tool")
    workaround_pain     = extract_field(text, "workaround_pain")
    direct_competitors  = extract_field(text, "direct_competitors")
    interview_notes     = extract_block(text, "interview_notes")
    interview_count     = extract_int_field(text, "interview_count")

    s_iv,  n_iv  = score_interview_volume(interview_count)
    s_sd,  n_sd  = score_segment_diversity(icp_segment, icp_anti)
    s_er,  n_er  = score_evidence_recency(event_recency)
    s_si,  n_si  = score_source_independence(interview_notes, workaround_tool, direct_competitors)
    s_cc,  n_cc  = score_competitor_coverage(direct_competitors)
    s_ws,  n_ws  = score_workaround_specificity(workaround_tool, workaround_pain)

    scores = {
        "interview_volume":       (s_iv, n_iv),
        "segment_diversity":      (s_sd, n_sd),
        "evidence_recency":       (s_er, n_er),
        "source_independence":    (s_si, n_si),
        "competitor_coverage":    (s_cc, n_cc),
        "workaround_specificity": (s_ws, n_ws),
    }
    total = sum(v[0] for v in scores.values())
    result = CQSResult(scores, total)
    result._idea = idea  # type: ignore[attr-defined]
    return result


def main() -> int:
    as_json = "--json" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]

    if not args:
        print("Usage: python3 context_quality_scorer.py [--json] <context-intake.md>")
        return 1

    path = Path(args[0])
    if not path.exists():
        print(f"Error: {path} not found", file=sys.stderr)
        return 1

    result = score_file(path)

    if as_json:
        print(json.dumps(result.to_dict(), ensure_ascii=False, indent=2))
    else:
        idea = getattr(result, "_idea", "")
        result.print_report(idea=idea)

    return 0 if result.verdict != "INSUFFICIENT" else 2


if __name__ == "__main__":
    sys.exit(main())
