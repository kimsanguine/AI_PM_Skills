#!/usr/bin/env python3
"""Opportunity Solution Tree generator — Teresa Torres OST as first-class artifact.

Why first-class:
- OST is the de-facto continuous-discovery framework PMs use in 2026.
- hplan currently mentions OST only in passing inside product-planning.md.
- Adding `docs/OPPORTUNITY_TREE.md` + auto-generated Mermaid as a Product Gate
  deliverable lets product-talk-fluent PMs adopt hplan without rewriting their
  vocabulary.

Input JSON (typically curated after interview tagging):

  {
    "outcome": "Sales-qualified meetings → closed-won rate +25% within 90 days",
    "opportunities": [
      {
        "name": "솔로 PM이 미팅 직후 결과물을 못 만든다",
        "evidence_count": 3,
        "solutions": [
          {"name": "60초 액션 아이템 초안", "experiment": "Concierge for 5 ICP"},
          {"name": "후속 메일 1-click", "experiment": "Manual draft compare"}
        ]
      },
      {
        "name": "다음 미팅 준비가 늦어 동일 안건 반복",
        "evidence_count": 2,
        "solutions": [...]
      }
    ]
  }

Output: docs/OPPORTUNITY_TREE.md with Mermaid diagram + opportunity/solution table.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


def render_mermaid(data: dict) -> str:
    lines = ["```mermaid", "flowchart TD", "  outcome[\"Outcome\\n" + data.get("outcome", "(set outcome)") + "\"]"]
    for i, opp in enumerate(data.get("opportunities", []), start=1):
        oid = f"O{i}"
        ev = opp.get("evidence_count", 0)
        label = f"{opp.get('name','?')}\\n(evidence: {ev})"
        lines.append(f'  {oid}["{label}"]')
        lines.append(f"  outcome --> {oid}")
        for j, sol in enumerate(opp.get("solutions", []), start=1):
            sid = f"S{i}_{j}"
            lines.append(f'  {sid}(["{sol.get("name","?")}"])')
            lines.append(f"  {oid} --> {sid}")
            exp = sol.get("experiment")
            if exp:
                eid = f"E{i}_{j}"
                lines.append(f'  {eid}[/"experiment: {exp}"/]')
                lines.append(f"  {sid} --> {eid}")
    lines.append("```")
    return "\n".join(lines)


def render_markdown(data: dict) -> str:
    today = date.today().isoformat()
    sections = [
        "# Opportunity Solution Tree",
        "",
        f"Generated: {today}",
        f"Outcome: **{data.get('outcome', '(set outcome)')}**",
        "",
        "## Tree",
        "",
        render_mermaid(data),
        "",
        "## Opportunities → Solutions → Experiments",
        "",
        "| # | Opportunity | Evidence | Solution | Experiment | Decision rule |",
        "|---|---|---|---|---|---|",
    ]
    for i, opp in enumerate(data.get("opportunities", []), start=1):
        sols = opp.get("solutions") or [{}]
        for j, sol in enumerate(sols):
            row = (
                f"| {i}.{j+1} "
                f"| {opp.get('name','-')} "
                f"| {opp.get('evidence_count', 0)} "
                f"| {sol.get('name','-')} "
                f"| {sol.get('experiment','-')} "
                f"| {sol.get('decision_rule','TBD')} |"
            )
            sections.append(row)
    sections += [
        "",
        "## Rules",
        "",
        "- Opportunities ≠ solutions. An opportunity is an unmet need from interview evidence.",
        "- Every solution must point upward to one opportunity and downward to one experiment.",
        "- Drop opportunities that have < 3 strong-Push interviews unless deliberately kept as parking-lot.",
        "- Mark experiments as `decision_rule` = the metric threshold that promotes/kills them.",
        "",
        "## Source Of Evidence",
        "",
        "Strong-Push interviews from `harness/evidence/snapshots.jsonl` should back each opportunity's evidence count.",
    ]
    return "\n".join(sections)


def parse_args():
    p = argparse.ArgumentParser(description="Generate OPPORTUNITY_TREE.md from JSON.")
    p.add_argument("input", help="Path to OST JSON")
    p.add_argument("--out", default="docs/OPPORTUNITY_TREE.md")
    return p.parse_args()


def main():
    args = parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    md = render_markdown(data)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8")
    print(f"wrote: {out}")


if __name__ == "__main__":
    main()
