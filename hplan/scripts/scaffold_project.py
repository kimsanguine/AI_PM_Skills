#!/usr/bin/env python3
"""Create an hplan project scaffold.

The script is intentionally conservative:
- it does not create real secrets
- it does not overwrite existing files unless --force is passed
- it separates planning scaffolds from build-ready scaffolds
"""

import argparse
from datetime import date
from pathlib import Path


LEAN_PLANNING_DOCS = [
    "README.md",
    "PRODUCT_BRIEF.md",
    "OPPORTUNITY_TREE.md",
    "HITL_FLOW.md",
    "DESIGN.md",
    "UNIT_ECONOMICS.md",
    "RISK_POLICY.md",
    "DECISION_LOG.md",
]

FULL_PLANNING_DOCS = [
    "README.md",
    "PRODUCT_BRIEF.md",
    "MARKET_RESEARCH.md",
    "COMPETITIVE_RESEARCH.md",
    "ICP_JTBD.md",
    "USER_INTERVIEWS.md",
    "PROBLEM_BRIEF.md",
    "USER_JOURNEY_MAP.md",
    "SITEMAP.md",
    "HYPOTHESIS_TREE.md",
    "OPPORTUNITY_TREE.md",
    "HITL_FLOW.md",
    "DESIGN.md",
    "UNIT_ECONOMICS.md",
    "RISK_POLICY.md",
    "DECISION_LOG.md",
]

LEAN_BUILD_DOCS = [
    "PRD.md",
    "ARCHITECTURE.md",
    "METRICS.md",
    "IMPLEMENTATION_READINESS.md",
]

FULL_BUILD_DOCS = [
    "PRD.md",
    "ARCHITECTURE.md",
    "PERFORMANCE_BENCHMARK.md",
    "METRICS.md",
    "LAUNCH_EXPERIMENT.md",
    "IMPLEMENTATION_READINESS.md",
]

HARNESS_DIRS = [
    "harness/evidence",
    "harness/product-gate",
    "harness/build-gate",
    "harness/exports",
    "harness/reports",
]

BUILD_READY_DIRS = [
    "review",
    "scripts",
    ".agents/skills",
    ".codex/hooks",
    ".claude/hooks",
    ".claude/skills",
    ".claude/agents",
]

IMPLEMENTATION_DIRS = [
    "apps",
    "services",
    "packages",
    "tests",
    "infra",
]


def render(text, project_name, mode, profile):
    return (
        text.replace("{{PROJECT_NAME}}", project_name)
        .replace("{{DATE}}", date.today().isoformat())
        .replace("{{MODE}}", mode)
        .replace("{{PROFILE}}", profile)
    )


def write_file(path, content, force=False, executable=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    existed = path.exists()
    if path.exists() and not force:
        return "skipped"
    path.write_text(content, encoding="utf-8")
    if executable:
        path.chmod(0o755)
    return "written" if existed else "created"


def touch_keep(path):
    keep = path / ".gitkeep"
    if not keep.exists():
        keep.write_text("", encoding="utf-8")


def docs_readme():
    return """# {{PROJECT_NAME}} Docs

This folder is the product source of truth.

## Gate Order

1. Evidence Gate: market, competitors, ICP/JTBD, interviews
2. Product Gate: problem brief, journey map, sitemap, design, hypothesis tree
3. Build Gate: PRD, architecture, COGS, benchmarks, metrics, launch plan

Do not treat `PRD.md` as implementation-ready until Evidence Gate and Product Gate are credible and the human checkpoints in `HITL_FLOW.md` are approved.

## Scaffold Profile

Profile: `{{PROFILE}}`

- `lean`: keeps one consolidated `PRODUCT_BRIEF.md` plus only the core build blockers.
- `full`: expands the same decisions into separate audit docs for evidence, product, cost, metrics, launch, and benchmark review.
"""


def doc_templates():
    return {
        "PRODUCT_BRIEF.md": """# Product Brief

Status: working source of truth
Last updated: {{DATE}}

This lean brief consolidates Evidence Gate and Product Gate decisions. Split sections into dedicated docs only when the project needs audit depth or the scaffold is regenerated with `--profile full`.

## Market Diagnosis

- What is already abundant:
- What users still cannot do well:
- Market vacuum:
- Counter position:
- What not to build:

## Competitor / Alternative Summary

| Name | Type | Core job | Strength | Gap | Our wedge |
|---|---|---|---|---|---|
|  | Direct competitor |  |  |  |  |
|  | Alternative/workaround |  |  |  |  |

## ICP / Persona / JTBD

- ICP:
- Situation:
- Push:
- Pull:
- Habit:
- Anxiety:
- Current workaround:
- Buying trigger:
- Priority JTBD:

## Interview Evidence

- Recruiting plan:
- Strong evidence:
- Medium evidence:
- Weak evidence:
- Missing evidence:

## Problem Brief

For ___, when ___ happens, they currently ___, which causes ___.

## User Journey Map

| Stage | User goal | Current behavior | Product response | Success signal |
|---|---|---|---|---|
| Discover |  |  |  |  |
| Start |  |  |  |  |
| Core job |  |  |  |  |
| Review |  |  |  |  |
| Pay/continue |  |  |  |  |

## Sitemap

```text
/
├── Home / positioning
├── Core workflow
├── Result / output
├── Pricing or upgrade path
└── Account / support / policy if needed
```

## Hypothesis Tree

| Hypothesis | Evidence | Experiment | Metric | Decision rule |
|---|---|---|---|---|
| Market |  |  |  |  |
| Product |  |  |  |  |
| Revenue |  |  |  |  |
| Operations |  |  |  |  |

## Human Checkpoint

- Decision needed:
- Recommended decision:
- Options:
- Evidence:
- Main risk:
""",
        "MARKET_RESEARCH.md": """# Market Research

Status: draft
Last updated: {{DATE}}

## Market Vacuum

- What is already abundant:
- What users still cannot do well:
- What current tools make expensive, slow, risky, or fragmented:

## What Not To Build

- 

## Counter Position Options

| Option | Against whom | Wedge | Why now | Risk |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

## Evidence Needed

- 
""",
        "COMPETITIVE_RESEARCH.md": """# Competitive Research

Status: required
Last updated: {{DATE}}

## Competitors And Alternatives

| Name | Type | Target user | Core job | Pricing | Strength | Gap | Our wedge |
|---|---|---|---|---|---|---|---|
|  | Direct competitor |  |  |  |  |  |  |
|  | Alternative/workaround |  |  |  |  |  |  |

## Switching Conditions

- Users would switch if:
- Users would not switch if:

## Research Notes

- 
""",
        "ICP_JTBD.md": """# ICP / Persona / JTBD

Status: draft

## ICP Candidates

| ICP | Situation | Repeated behavior | Current workaround | Buying trigger | Priority |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

## Persona Card

- Situation:
- Push:
- Pull:
- Habit:
- Anxiety:
- Current workaround:
- Buying trigger:

## JTBD

When ___, I want to ___, so I can ___.
""",
        "USER_INTERVIEWS.md": """# User Interviews

Status: required before build

## Recruiting Plan

- Minimum interview count: 5
- Target ICP:
- Where to recruit:

## Interview Questions

- Tell me about the last time this happened.
- What did you use instead?
- How much time, money, or opportunity did it cost?
- What made the workaround painful enough to change?
- What would need to be true for you to switch?

## Interview Snapshots

| Person | Date | Situation | Current workaround | Pain strength | Switch trigger | Evidence |
|---|---|---|---|---|---|---|
|  |  |  |  | Strong/Medium/Weak |  |  |
""",
        "PROBLEM_BRIEF.md": """# Problem Brief

Status: draft

## Problem

For ___, when ___ happens, they currently ___, which causes ___.

## Evidence

- Strong:
- Medium:
- Weak:

## Scope

- In:
- Out:

## Decision

Build / Interview / Pivot / Hold:
""",
        "USER_JOURNEY_MAP.md": """# User Journey Map

Status: required before implementation

| Stage | User goal | Current behavior | Pain | Product opportunity | Success signal |
|---|---|---|---|---|---|
| Discover |  |  |  |  |  |
| Start |  |  |  |  |  |
| Core job |  |  |  |  |  |
| Review |  |  |  |  |  |
| Pay/continue |  |  |  |  |  |
""",
        "SITEMAP.md": """# Sitemap

Status: required before implementation

## Public Routes

- `/`
- `/pricing`
- `/login`

## App Routes

- `/app`

## Admin / Operations Routes

- 

## Empty, Error, Blocked, Paid, And Review States

- 
""",
        "OPPORTUNITY_TREE.md": """# Opportunity Solution Tree

Status: required Product Gate artifact (Teresa Torres OST)

Outcome: (one measurable outcome, not output)

## Tree

```mermaid
flowchart TD
  outcome["Outcome\\n(set outcome)"]
  O1["Opportunity 1\\n(evidence: 0)"]
  outcome --> O1
  S1_1(["Solution 1"])
  O1 --> S1_1
  E1_1[/"experiment: TBD"/]
  S1_1 --> E1_1
```

## Opportunities → Solutions → Experiments

| # | Opportunity | Evidence | Solution | Experiment | Decision rule |
|---|---|---|---|---|---|
| 1.1 |  | 0 |  |  | TBD |

## Rules

- Opportunities are unmet user needs from interview evidence — not solutions.
- Every solution points to one opportunity and one experiment with a decision rule.
- Drop opportunities backed by fewer than 3 strong-Push interviews unless deliberately parked.
- Regenerate with `scripts/ost_generator.py <input.json> --out docs/OPPORTUNITY_TREE.md` whenever evidence changes.
""",
        "HYPOTHESIS_TREE.md": """# Hypothesis Tree

Status: draft

## Objective

- 

## Opportunities

- 

## Solution Hypotheses

| Hypothesis | Evidence | Experiment | Metric | Decision rule |
|---|---|---|---|---|
|  |  |  |  |  |
""",
        "HITL_FLOW.md": """# Human In The Loop Flow

Status: required gate control

## Principle

AI can search, summarize, cluster, draft, score, and propose. The human approves the interpretation before the next gate.

## Gate Checkpoints

| Gate | Human decision | Status | Date | Notes |
|---|---|---|---|---|
| Intake | Confirm assumptions and constraints | WAITING_FOR_HUMAN |  |  |
| Evidence | Approve competitor set, market vacuum, interview ICP, and evidence table | WAITING_FOR_HUMAN |  |  |
| Product | Approve Problem Brief, ICP/JTBD, MPO, journey map, sitemap, and design direction | WAITING_FOR_HUMAN |  |  |
| Build | Approve COGS, policy, architecture boundary, PRD seed, and build status | WAITING_FOR_HUMAN |  |  |
| Launch | Review first users, metrics, cost, quality, and proceed/pivot/hold | WAITING_FOR_HUMAN |  |  |

## Interview Rule

- [ ] At least 5 real interviews are planned or equivalent strong behavior evidence exists.
- [ ] The human has reviewed salient quotes.
- [ ] AI summaries were checked against source notes or transcripts.
- [ ] Evidence is tagged Strong / Medium / Weak.

## Spec Approval Flow

```text
Problem Brief
  -> review-problem
PRD seed / Spec
  -> review-spec
Plan / Architecture
  -> review-plan
Tasks
  -> review-tasks
Implementation
  -> review-implementation
Launch
  -> review-metrics
```

## Current Smallest Decision Needed

- Decision:
- Options:
- Recommended option:
- Evidence:
- Risk:
""",
        "DESIGN.md": """# Design Guidelines

Status: required before UI implementation

## Product Mood

- 

## Screen Hierarchy

- Primary job:
- Secondary actions:
- Avoid:

## Visual Principles

- Layout:
- Typography:
- Color:
- Motion:
- Density:

## Component Rules

- Buttons:
- Forms:
- Tables/lists:
- Cards:
- Modals:

## State Rules

- Empty:
- Loading:
- Success:
- Failed:
- Blocked:
- Paid/usage limit:
- Review required:

## Mobile Verification Checklist

- Text fits without overlap.
- Primary action remains visible.
- Navigation works without hidden critical routes.
- Long words and translated strings do not break containers.
""",
        "UNIT_ECONOMICS.md": """# Unit Economics / COGS

Status: build blocker

## Revenue

- Price:
- Billing period:
- Payment fee:
- Net revenue:

## Cost Units

| Unit | Provider | Cost formula | Expected usage | Worst case | Cap |
|---|---|---|---|---|---|
| Model call |  |  |  |  |  |
| Analysis run |  |  |  |  |  |
| Export/render |  |  |  |  |  |
| Storage |  |  |  |  |  |

## Margin Guardrail

- Target gross margin:
- Allowed COGS per paid user:
- Free-user abuse scenario:
- Decision: GO / CONDITIONAL_GO / HOLD
""",
        "RISK_POLICY.md": """# Risk Policy

Status: required before handling user data

## Data Classes

- Synthetic:
- Owned:
- Approved third-party:
- Private/sensitive:

## User Confirmation

- What requires visible confirmation:
- What is blocked by default:

## Retention / Deletion / Takedown

- Retention:
- Deletion:
- Takedown:

## AI Output Safety

- Review-required outputs:
- Disallowed outputs:
""",
        "DECISION_LOG.md": """# Decision Log

| Date | Decision | Reason | Evidence | Revisit trigger |
|---|---|---|---|---|
| {{DATE}} | Scaffold created | {{MODE}} mode | hplan |  |
""",
        "PRD.md": """# PRD

Status: locked until Evidence Gate and Product Gate are credible

## Problem

- 

## Target User

- 

## JTBD

- 

## MVP Scope

- In:
- Out:

## User Stories

| Story | Acceptance criteria | Priority |
|---|---|---|
|  |  |  |

## Non-Goals

- 

## Risks

- 
""",
        "ARCHITECTURE.md": """# Architecture

Status: draft after Build Gate

## System Boundary

- Client:
- Server:
- Data:
- External providers:

## Core Flows

- 

## Job States

- queued
- running
- succeeded
- failed
- blocked
- review_required

## APIs / Events

| Name | Input | Output | Failure state |
|---|---|---|---|
|  |  |  |  |

## Security / Privacy

- 
""",
        "PERFORMANCE_BENCHMARK.md": """# Performance Benchmark

Status: required if speed, quality, or provider choice is part of the promise

## Latency Budget

| Flow | P50 | P95 | Timeout | Fallback |
|---|---|---|---|---|
|  |  |  |  |  |

## Provider Matrix

| Provider | Cost | Speed | Quality | Failure rate | Notes |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
""",
        "METRICS.md": """# Metrics

Status: required before launch

## 5-Layer Metrics

| Layer | Metric | Event/source | Decision rule |
|---|---|---|---|
| Outcome |  |  |  |
| Quality |  |  |  |
| Friction |  |  |  |
| Revenue |  |  |  |
| Cost |  |  |  |
""",
        "LAUNCH_EXPERIMENT.md": """# Launch Experiment

Status: draft

## Target Segment

- 

## Experiment

- Offer:
- Channel:
- Timebox:
- Success:
- Pivot/Kill:

## Paid Signal

- 
""",
        "IMPLEMENTATION_READINESS.md": """# Implementation Readiness

Status: final Build Gate checklist

## Required Before Build

- [ ] Competitor research completed
- [ ] 5+ interviews or strong behavior evidence
- [ ] Problem brief accepted
- [ ] ICP/JTBD narrowed
- [ ] HITL checkpoints approved through Product Gate
- [ ] User journey map exists
- [ ] Sitemap exists
- [ ] DESIGN.md exists
- [ ] COGS and margin guardrails calculated
- [ ] Risk policy exists
- [ ] Metrics and launch experiment defined

## Decision

Build / Conditional Go / Interview / Pivot / Hold:
""",
    }


def root_templates():
    return {
        "README.md": """# {{PROJECT_NAME}}

This repository was initialized with the hplan Product Build Gate scaffold.

Scaffold profile: `{{PROFILE}}`

## Source Of Truth

- `docs/` contains accepted product planning documents. In lean profile, `docs/PRODUCT_BRIEF.md` consolidates market, competitor, ICP/JTBD, interview, problem, journey, sitemap, and hypothesis notes.
- `harness/` contains hplan-generated working artifacts and reports.
- `review/` contains human and agent review checklists after the build-ready scaffold is generated.
- `.codex/` contains Codex project configuration and hooks after the build-ready scaffold is generated.
- `.claude/` contains Claude Code project settings and hooks after the build-ready scaffold is generated.
- `.agents/skills/` is reserved for optional repo-local Codex skills.

Do not start implementation from `PRD.md` alone. When present, confirm Evidence Gate, Product Gate, and Build Gate status in `docs/PRODUCT_BRIEF.md`, `docs/HITL_FLOW.md`, and `docs/IMPLEMENTATION_READINESS.md`.
""",
        "AGENTS.md": """# AGENTS.md

Guidance for Codex and other coding agents in this repository.

## Source Of Truth

- Read `docs/PRODUCT_BRIEF.md`, `docs/DESIGN.md`, and `docs/UNIT_ECONOMICS.md` before implementation.
- If this repo uses the full profile, also read `docs/PROBLEM_BRIEF.md`, `docs/USER_JOURNEY_MAP.md`, and `docs/SITEMAP.md`.
- Treat `harness/` as generated working output. Promote only accepted decisions into `docs/`.

## Build Gates

- Do not implement UI before `docs/DESIGN.md`, `docs/USER_JOURNEY_MAP.md`, and `docs/SITEMAP.md` are credible.
- Do not add paid or variable-cost features before `docs/UNIT_ECONOMICS.md` defines caps and margin guardrails.
- Do not process user data before `docs/RISK_POLICY.md` defines permissions, retention, deletion, and takedown rules.
- Do not create or commit real secrets. Use `.env.example`; keep `.env` ignored.

## Verification

Run project-specific checks from `scripts/run_checks.sh` once the stack is known.

## Codex Configuration

- Project config lives in `.codex/config.toml`.
- Project hooks live in `.codex/hooks.json` and may call scripts under `.codex/hooks/`.
- Optional repo-local skills live under `.agents/skills/`.
""",
        "CLAUDE.md": """# CLAUDE.md

Project memory for Claude Code.

## Planning Discipline

Use the hplan gate order:

1. Evidence Gate
2. Product Gate
3. Build Gate

Do not jump from idea to PRD without competitor research, user interview evidence, problem definition, journey map, sitemap, design guidelines, and COGS.

## Shared Source Of Truth

- Product docs: `docs/`
- Generated hplan outputs: `harness/`
- Reviews: `review/`
- Claude settings: `.claude/settings.json`
- Claude hooks: `.claude/hooks/`
- Claude project skills: `.claude/skills/`
""",
        ".codex/config.toml": """# Codex project configuration.
# Personal defaults live in ~/.codex/config.toml. Keep repo-shared settings conservative.

[features]
codex_hooks = true

# Optional project defaults after the stack is known:
# model = "gpt-5.5"
# approval_policy = "on-request"
# sandbox_mode = "workspace-write"
""",
        ".codex/hooks.json": """{
  "hooks": {}
}
""",
        ".codex/hooks/README.md": """# Codex Hooks

Codex discovers project hooks from `.codex/hooks.json` after the project is trusted.

Keep hook commands deterministic, fast, and safe to run from the repository root. Put hook scripts in this folder when they are Codex-specific; use `scripts/` for general project commands.
""",
        ".claude/settings.json": """{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "hooks": {}
}
""",
        ".claude/hooks/README.md": """# Claude Hooks

Claude Code project hooks are configured in `.claude/settings.json`.

Use this folder for hook scripts referenced from settings, for example with `$CLAUDE_PROJECT_DIR/.claude/hooks/check-style.sh`.
""",
        ".claude/skills/README.md": """# Claude Project Skills

Add Claude Code project skills here as subdirectories with `SKILL.md`.

Use this only for project-specific workflows. Reusable hplan itself should stay installed as a normal skill or plugin.
""",
        ".gitignore": """.env
.env.*
!.env.example
.claude/settings.local.json
.codex/log/
.codex/tmp/
node_modules/
.next/
dist/
build/
__pycache__/
.pytest_cache/
.DS_Store
output/
tmp/
*.log
""",
        ".env.example": """# Never commit real secrets.

# OPENAI_API_KEY=
# ANTHROPIC_API_KEY=
# DATABASE_URL=
# PAYMENT_PROVIDER_SECRET=
""",
    }


def review_templates():
    return {
        "review/design-review.md": """# Design Review

- [ ] DESIGN.md exists and matches the product mood.
- [ ] Journey map and sitemap are reflected in screens.
- [ ] Empty, loading, failed, blocked, paid, and review states exist.
- [ ] Mobile layout has been checked.
""",
        "review/security-privacy-review.md": """# Security / Privacy Review

- [ ] RISK_POLICY.md defines data classes.
- [ ] User confirmation exists for private or third-party content.
- [ ] Retention, deletion, and takedown rules are explicit.
""",
        "review/cost-review.md": """# Cost Review

- [ ] UNIT_ECONOMICS.md defines cost units.
- [ ] Free-user abuse scenario is calculated.
- [ ] Usage caps and payment boundaries are implemented.
""",
        "review/launch-review.md": """# Launch Review

- [ ] Launch experiment has a target segment and decision rule.
- [ ] Metrics include outcome, quality, friction, revenue, and cost.
- [ ] Paid signal is defined.
""",
        "review/qa-checklist.md": """# QA Checklist

- [ ] Core job succeeds.
- [ ] Failure states are visible.
- [ ] Billing and usage boundaries are tested.
- [ ] Public trust pages are review-ready when needed.
""",
    }


def hook_and_script_templates():
    return {
        "scripts/README.md": """# Scripts

Project-local scripts live here.

- `validate_docs.sh`: checks that required hplan docs exist
- `run_checks.sh`: placeholder for stack-specific checks
""",
        "scripts/validate_docs.sh": """#!/usr/bin/env bash
set -euo pipefail

required=(
  "docs/PRODUCT_BRIEF.md"
  "docs/HITL_FLOW.md"
  "docs/DESIGN.md"
  "docs/UNIT_ECONOMICS.md"
)

missing=0
for file in "${required[@]}"; do
  if [ ! -f "$file" ]; then
    echo "missing: $file"
    missing=1
  fi
done

if [ -f "docs/PRD.md" ]; then
  build_required=(
    "docs/ARCHITECTURE.md"
    "docs/IMPLEMENTATION_READINESS.md"
  )
  for file in "${build_required[@]}"; do
    if [ ! -f "$file" ]; then
      echo "missing: $file"
      missing=1
    fi
  done
fi

exit "$missing"
""",
        "scripts/run_checks.sh": """#!/usr/bin/env bash
set -euo pipefail

echo "No stack-specific checks configured yet."
echo "Update this script after choosing the project stack."
""",
    }


def create_scaffold(root, project_name, mode, profile, force):
    root.mkdir(parents=True, exist_ok=True)

    dirs = ["docs", *HARNESS_DIRS]
    docs = list(LEAN_PLANNING_DOCS if profile == "lean" else FULL_PLANNING_DOCS)
    files = {}

    if mode in {"build-ready", "implementation"}:
        dirs.extend(BUILD_READY_DIRS)
        docs.extend(LEAN_BUILD_DOCS if profile == "lean" else FULL_BUILD_DOCS)
        files.update(root_templates())
        files.update(review_templates())
        files.update(hook_and_script_templates())
    else:
        files["README.md"] = root_templates()["README.md"]
        files[".gitignore"] = root_templates()[".gitignore"]

    if mode == "implementation":
        dirs.extend(IMPLEMENTATION_DIRS)

    for directory in dirs:
        path = root / directory
        path.mkdir(parents=True, exist_ok=True)
        if directory.startswith(
            (
                "harness/",
                "apps",
                "services",
                "packages",
                "tests",
                "infra",
                ".agents/skills",
                ".claude/agents",
            )
        ):
            touch_keep(path)

    templates = doc_templates()
    for doc in docs:
        files[f"docs/{doc}"] = templates[doc] if doc != "README.md" else docs_readme()

    created = []
    skipped = []
    for relative_path, content in sorted(files.items()):
        target = root / relative_path
        rendered = render(content, project_name, mode, profile)
        executable = relative_path.endswith(".sh")
        status = write_file(target, rendered, force=force, executable=executable)
        if status == "skipped":
            skipped.append(relative_path)
        else:
            created.append(relative_path)

    return created, skipped


def parse_args():
    parser = argparse.ArgumentParser(description="Create an hplan project scaffold.")
    parser.add_argument("target", help="Target project directory")
    parser.add_argument("--project-name", default=None, help="Project name for templates")
    parser.add_argument(
        "--mode",
        choices=["planning", "build-ready", "implementation"],
        default="planning",
        help="Scaffold depth. Use build-ready after gates are credible.",
    )
    parser.add_argument(
        "--profile",
        choices=["lean", "full"],
        default="lean",
        help="Artifact profile. lean consolidates planning docs; full expands audit docs.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    return parser.parse_args()


def main():
    args = parse_args()
    root = Path(args.target).expanduser().resolve()
    project_name = args.project_name or root.name
    created, skipped = create_scaffold(root, project_name, args.mode, args.profile, args.force)

    print(f"hplan scaffold: {root}")
    print(f"mode: {args.mode}")
    print(f"profile: {args.profile}")
    print(f"created/written: {len(created)}")
    print(f"skipped existing: {len(skipped)}")
    if created:
        print("\ncreated:")
        for item in created:
            print(f"- {item}")
    if skipped:
        print("\nskipped:")
        for item in skipped:
            print(f"- {item}")


if __name__ == "__main__":
    main()
