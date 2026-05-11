---
description: "Export the Build Gate brief to your downstream coding ecosystem — Spec-Kit, Kiro, GStack, Claude Code, or all four at once."
argument-hint: "[brief.json] [--target spec-kit|kiro|gstack|claude|all]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-handoff

Export an approved Build Gate brief to one or more downstream coding ecosystems.

## Prerequisites

- `/hplan-build` returned `build` or `CONDITIONAL_GO`
- `harness/build-gate/checkpoint.json` has `status: "approved"` (if PreToolUse hook active)
- Brief JSON with at minimum: `product_name`, `problem`, `icp`, `jtbd`, `cogs_ceiling`, `decision`

## Run

```bash
python3 hplan/scripts/export_handoff.py brief.json --target all
```

Or per-ecosystem:

```bash
python3 hplan/scripts/export_handoff.py brief.json --target spec-kit
python3 hplan/scripts/export_handoff.py brief.json --target kiro
python3 hplan/scripts/export_handoff.py brief.json --target gstack
python3 hplan/scripts/export_handoff.py brief.json --target claude
```

## Output paths

| Target | Path | Format |
|---|---|---|
| spec-kit | `harness/exports/spec-kit/specs/NNN-slug/` | GitHub Spec-Kit `{spec, plan, tasks}.md` |
| kiro | `harness/exports/kiro/.kiro/specs/<slug>/` | Kiro `{requirements, design, tasks}.md` |
| gstack | `harness/exports/gstack/office-hours-brief.md` | GStack `/office-hours` first-message brief |
| claude | `harness/exports/claude/AGENTS.md` + `CLAUDE.md` | Codex + Claude Code project memory |

## After handoff

- Copy or symlink generated files into the actual project directory
- For spec-kit: `cp -r harness/exports/spec-kit/specs <repo-root>/specs`
- For kiro: `cp -r harness/exports/kiro/.kiro <repo-root>/`
- For gstack: paste the brief into `/office-hours` directly
- For claude: place AGENTS.md + CLAUDE.md at repo root

## Boundary

Handoff is the **last step** in the hplan lifecycle. Do not skip Evidence + Product + Build Gates to reach handoff faster — the brief will be hollow.
