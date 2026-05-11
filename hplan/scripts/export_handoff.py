#!/usr/bin/env python3
"""Export an hplan Build Gate brief to downstream agent ecosystems.

Reads a single JSON brief (the accepted Product Brief + Build Gate) and writes
ecosystem-specific handoff folders under `harness/exports/`:

- spec-kit: GitHub Spec-Kit `specs/<NNN>-<slug>/{spec,plan,tasks}.md`
- kiro:     Kiro `.kiro/specs/<slug>/{requirements,design,tasks}.md`
- gstack:   GStack `/office-hours` first-input brief
- claude:   AGENTS.md + CLAUDE.md mirrors for Codex/Claude Code projects

The intent is to make hplan the upstream evidence gate that *feeds* every
spec-driven coding agent, not just Claude Code.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


TARGETS = ("spec-kit", "kiro", "gstack", "claude", "all")


def slugify(value: str) -> str:
    value = (value or "hplan-product").strip().lower()
    value = re.sub(r"[^a-z0-9가-힣]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "hplan-product"


def next_spec_number(specs_root: Path) -> str:
    if not specs_root.exists():
        return "001"
    nums = []
    for child in specs_root.iterdir():
        m = re.match(r"^(\d{3})-", child.name)
        if m:
            nums.append(int(m.group(1)))
    return f"{(max(nums) + 1) if nums else 1:03d}"


def render_spec_kit_spec(brief: dict) -> str:
    return f"""# Feature Specification — {brief.get('product_name', '')}

Generated: {date.today().isoformat()}
Source: hplan Build Gate (evidence-backed)

## Problem
{brief.get('problem', '-')}

## Target User
{brief.get('icp', '-')}

## JTBD
{brief.get('jtbd', '-')}

## Functional Requirements
{format_list(brief.get('functional_requirements', []))}

## Acceptance Criteria
{format_list(brief.get('acceptance_criteria', []))}

## Non-Goals
{format_list(brief.get('non_goals', []))}

## Evidence
- Interview strong signals: {brief.get('strong_signals', '-')}
- Current workarounds: {brief.get('workarounds', '-')}
- Competitor gap: {brief.get('competitor_gap', '-')}

## Constraints
- COGS ceiling per paid user: {brief.get('cogs_ceiling', 'TBD')}
- Latency budget: {brief.get('latency_budget', 'TBD')}
- Data policy: {brief.get('risk_policy', 'see RISK_POLICY.md')}
"""


def render_spec_kit_plan(brief: dict) -> str:
    return f"""# Implementation Plan — {brief.get('product_name', '')}

## System Boundary
{brief.get('architecture_boundary', '-')}

## Job States
- queued / running / succeeded / failed / blocked / review_required

## Core Flows
{format_list(brief.get('core_flows', []))}

## Providers / Models
{format_list(brief.get('providers', []))}

## Latency Budget
{brief.get('latency_budget', 'TBD')}

## Verification Strategy
- Test matrix in `tasks.md`
- COGS sentinel must pass before merge to main
"""


def render_spec_kit_tasks(brief: dict) -> str:
    tasks = brief.get("tasks") or default_tasks(brief)
    body = "\n".join(f"- [ ] T{idx:03d} — {task}" for idx, task in enumerate(tasks, start=1))
    return f"""# Tasks — {brief.get('product_name', '')}

Order follows hplan implementation-readiness rules: pipeline proof, schema, usage enforcement, billing/webhook tests, COGS measurement, alpha loop, then polish.

{body}

## Definition Of Done
- [ ] All tasks pass acceptance criteria from spec.md
- [ ] COGS sentinel green
- [ ] Human Build Checkpoint approved
"""


def default_tasks(brief: dict) -> list[str]:
    return [
        "Scaffold project repo from hplan build-ready scaffold",
        "Implement core pipeline thin-slice (one happy path)",
        "Add schema validation at all external boundaries",
        "Enforce usage caps and free-user abuse limits",
        "Wire payment provider with webhook tests",
        "Measure p50/p90 COGS against sentinel target",
        "Run alpha loop with first 5 users tagged from interview kit",
        "Polish empty/loading/failed/blocked/paid/review states",
    ]


def render_kiro_requirements(brief: dict) -> str:
    return f"""# Requirements

Source: hplan Build Gate

## User Stories
{format_list(brief.get('user_stories', []) or [
    f"As {brief.get('icp', 'the target user')}, I want to {brief.get('primary_outcome', 'achieve the primary outcome')} so that {brief.get('value', 'I get the proven value')}."
])}

## Acceptance Criteria (EARS-style)
{format_list(brief.get('acceptance_criteria_ears', []) or [
    "WHEN the user completes the core flow, THE SYSTEM SHALL produce a verifiable outcome.",
    "IF the COGS ceiling is exceeded, THE SYSTEM SHALL throttle or downgrade the provider.",
])}
"""


def render_kiro_design(brief: dict) -> str:
    return f"""# Design

## Architecture
{brief.get('architecture_boundary', '-')}

## Data Model
{format_list(brief.get('data_model', []))}

## Provider Routing
{format_list(brief.get('providers', []))}

## Failure Modes
- Provider timeout → fallback per `PERFORMANCE_BENCHMARK.md`
- Cost spike → throttle per `UNIT_ECONOMICS.md`
- Policy violation → block per `RISK_POLICY.md`
"""


def render_kiro_tasks(brief: dict) -> str:
    tasks = brief.get("tasks") or default_tasks(brief)
    body = "\n".join(f"- [ ] {idx}. {task}" for idx, task in enumerate(tasks, start=1))
    return f"""# Tasks

{body}
"""


def render_gstack_brief(brief: dict) -> str:
    return f"""# /office-hours Input — {brief.get('product_name', '')}

This brief was produced by hplan after Evidence Gate + Product Gate + Build Gate passed.
Run `/office-hours` with this as the first message, then `/plan-ceo-review` and `/plan-eng-review`.

## Problem
{brief.get('problem', '-')}

## Target User (behavior, not demographics)
{brief.get('icp', '-')}

## Wedge / Counter Position
{brief.get('counter_position', '-')}

## What We Will Not Build (and why)
{format_list(brief.get('not_build', []))}

## Strong Evidence
{format_list(brief.get('strong_signals_list', []))}

## Economic Guardrails
- COGS ceiling: {brief.get('cogs_ceiling', 'TBD')}
- Target gross margin: {brief.get('gross_margin_target', 'TBD')}
- Free-user abuse cap: {brief.get('abuse_cap', 'TBD')}

## First Build Slice (one paid outcome / one agent job)
{brief.get('mvp_slice', '-')}

## Next GStack Steps
1. `/office-hours` — challenge wedge against this brief
2. `/plan-ceo-review` — confirm scope and money story
3. `/plan-eng-review` — architecture boundary and test matrix
4. `/plan-design-review` — UI states from `DESIGN.md`
5. `/qa` and `/review` per branch
6. `/ship`
"""


def render_claude_agents(brief: dict, kind: str) -> str:
    header = "AGENTS.md" if kind == "agents" else "CLAUDE.md"
    return f"""# {header}

Source of truth: produced by hplan Build Gate handoff on {date.today().isoformat()}.

## Source Docs (read before any change)
- `docs/PRODUCT_BRIEF.md`
- `docs/DESIGN.md`
- `docs/UNIT_ECONOMICS.md`
- `docs/RISK_POLICY.md`
- `harness/build-gate/decision.json`

## Build Gates
- Do not implement UI before `docs/DESIGN.md` + journey + sitemap are credible.
- Do not add paid or variable-cost features before COGS sentinel passes.
- Do not process user data before `docs/RISK_POLICY.md` rules exist.

## hplan Handoff Summary
- Product: {brief.get('product_name', '-')}
- Decision: {brief.get('decision', 'build')}
- COGS ceiling per paid user: {brief.get('cogs_ceiling', 'TBD')}
- Latency budget: {brief.get('latency_budget', 'TBD')}

## Verification
- `scripts/cogs_sentinel.py` must stay green.
- `scripts/validate_docs.sh` must pass.
"""


def format_list(items) -> str:
    if not items:
        return "- -"
    if isinstance(items, str):
        return f"- {items}"
    return "\n".join(f"- {item}" for item in items)


def write(path: Path, content: str, force: bool) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        return "skipped"
    path.write_text(content, encoding="utf-8")
    return "written"


def export(brief: dict, root: Path, targets: list[str], force: bool) -> dict:
    written = []
    skipped = []

    slug = slugify(brief.get("product_name", "hplan-product"))
    base = root / "harness" / "exports"

    if "spec-kit" in targets or "all" in targets:
        specs_root = base / "spec-kit" / "specs"
        spec_num = next_spec_number(specs_root)
        spec_dir = specs_root / f"{spec_num}-{slug}"
        for fname, renderer in (
            ("spec.md", render_spec_kit_spec),
            ("plan.md", render_spec_kit_plan),
            ("tasks.md", render_spec_kit_tasks),
        ):
            status = write(spec_dir / fname, renderer(brief), force)
            (written if status == "written" else skipped).append(str(spec_dir / fname))

    if "kiro" in targets or "all" in targets:
        kiro_dir = base / "kiro" / ".kiro" / "specs" / slug
        for fname, renderer in (
            ("requirements.md", render_kiro_requirements),
            ("design.md", render_kiro_design),
            ("tasks.md", render_kiro_tasks),
        ):
            status = write(kiro_dir / fname, renderer(brief), force)
            (written if status == "written" else skipped).append(str(kiro_dir / fname))

    if "gstack" in targets or "all" in targets:
        target = base / "gstack" / "office-hours-brief.md"
        status = write(target, render_gstack_brief(brief), force)
        (written if status == "written" else skipped).append(str(target))

    if "claude" in targets or "all" in targets:
        for fname, kind in (("AGENTS.md", "agents"), ("CLAUDE.md", "claude")):
            target = base / "claude" / fname
            status = write(target, render_claude_agents(brief, kind), force)
            (written if status == "written" else skipped).append(str(target))

    return {"written": written, "skipped": skipped}


def parse_args():
    p = argparse.ArgumentParser(description="Export hplan Build Gate brief to downstream agent ecosystems.")
    p.add_argument("brief", help="Path to JSON brief")
    p.add_argument("--root", default=".", help="Project root (defaults to cwd)")
    p.add_argument(
        "--target",
        action="append",
        choices=TARGETS,
        help="Target ecosystem(s). Repeat or use --target all.",
    )
    p.add_argument("--force", action="store_true")
    return p.parse_args()


def main():
    args = parse_args()
    brief = json.loads(Path(args.brief).read_text(encoding="utf-8"))
    targets = args.target or ["all"]
    result = export(brief, Path(args.root).resolve(), targets, args.force)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
