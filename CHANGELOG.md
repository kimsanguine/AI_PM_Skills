# Changelog

All notable changes to AI_PM_Skills are documented here.

---

## [0.5.0] — 2026-05-11

### Added — `hplan` plugin (6th plugin, lifecycle Stage 0)

A new plugin that runs BEFORE oracle's discovery — the **Evidence + COGS + Decision gate** that decides whether the product deserves to be built at all.

**New skills (7) under `hplan/skills/`:**

| Skill | What it does |
|---|---|
| `evidence-rubric` | Score idea against 100-point evidence rubric (ICP / recent painful event / workaround / repetition / economic pain / switching trigger / MVP narrowness / acquisition path) |
| `interview-synthesis` | Import AI-clustered interview output (BuildBetter / Perspective / Granola / Otter), force human strength + Push/Pull/Habit/Anxiety axes tagging, audit 5/3 strong-Push rule |
| `exclusions` | Append-only Do-Not-Build registry with Korean-aware char-bigram fuzzy match + reopen_trigger |
| `cogs-sentinel` | Executable COGS gate — p50/p90 monthly margin via lognormal sampling, free-user abuse blend, GREEN/CONDITIONAL_GO/RED decision |
| `ost` | Generate Teresa Torres-style Opportunity Solution Tree with Mermaid + `docs/OPPORTUNITY_TREE.md` |
| `decision-log` | Append-only build/interview/pivot/hold log + 3-6 month self-eval audit (hit_rate, false_holds, missed_builds) |
| `handoff` | Multi-target Build Gate brief → Spec-Kit `specs/NNN-slug/`, Kiro `.kiro/specs/`, GStack `/office-hours`, Claude Code `AGENTS.md` + `CLAUDE.md` |

**New commands (6):**

- `/hplan-evidence`, `/hplan-product`, `/hplan-build`, `/hplan-cogs`, `/hplan-exclude`, `/hplan-handoff`

**Cross-cutting infrastructure:**

- `hplan/hplan_mcp/server.py` — MCP server exposing 6 hplan tools to Cursor / Windsurf / Kiro / Codex / Goose
- `hplan/hooks/gate_guard.py` — Claude Code PreToolUse hook blocking writes to PRD.md / spec.md / `specs/` / `.kiro/specs/` until `harness/build-gate/checkpoint.json` has `status: "approved"`
- `hplan/agents/` — 4 role-locked reviewer agents (evidence / product / economics / build)
- `hplan/references/` — 14 playbooks + `provider_pricing.json` (2026-05-11 snapshot)
- `hplan/scripts/` — 9 deterministic Python scripts

### Changed

- Lifecycle reordered: `hplan → oracle → atlas → forge → argus → muse`
- Marketplace version 0.4.0 → 0.5.0
- "36 skills, 5 plugins" → "43 skills, 6 plugins"
- Added `Route to hplan when ...` lines to 7 existing skills: `oracle/cost-sim`, `oracle/opp-tree`, `oracle/hitl`, `oracle/assumptions`, `oracle/build-or-buy`, `forge/prd`, `argus/burn-rate`
- README.md + README-ko.md top sections updated with hplan callout + 6-stage lifecycle table

### Fixed

- Removed accidentally committed `.git_broken/` directory (hundreds of git internals)
- Removed stale `EVAL_QUICK_REFERENCE.txt` (2026-03 internal note)

### Moved

- `todolist.md` → `.archive/2026-03-todolist.md`
- `progress.md` → `.archive/2026-03-progress.md`
- `eval_metrics.json` → `evals/pm-framework-baseline.json`
- `eval-workspace/` → `evals/workspace/`

---

## [1.0.0] — 2026-03-07

### v1.0 Structural Upgrade

Every skill now follows a consistent v1.0 structure that adds production-grade rigor on top of the original educational content.

**New sections in every SKILL.md:**

- **Core Goal** — 1-2 sentence purpose statement
- **Trigger Gate** — Use / Route / Boundary for accurate skill selection
- **Failure Handling** — table of failure → detection → fallback
- **Quality Gate** — self-check checklist before delivery
- **Examples** — good/bad output signals

### New Skills (3)

| Skill | Plugin | What it does |
|-------|--------|-------------|
| `infographic-gif-creator` | forge | Animated infographic GIF/MP4 for agent architecture visualization |
| `pptx-ai-slide` | forge | Agent project presentation deck (pitch, review, investor) |
| `agent-demo-video` | forge | Remotion-based demo video for stakeholders |

### Stats

- **35 skills** (was 32), **12 commands**, **5 plugins**
- Trigger accuracy: 97.9% (94/96)
- Quality eval: with-skill 100% vs without-skill 88% (+12%)
- All 35 skills validated via `validate_plugins.py` — 0 errors, 0 warnings

### Documentation

- README.md / README-ko.md updated (badges, status, forge details, file structure, skill origin)
- CONTRIBUTING.md updated with v1.0 SKILL.md format guide
- GUIDE-ko.md updated (forge 11 skills, total 35)
- "What Makes This Different" — added section 6: v1.0 Structural Rigor
- CHANGELOG.md created (this file)

---

## [0.4.0] — 2026-03-06

### Phase 3 Complete — Eval Framework

- Quality eval: 10 tests, 54 assertions — with-skill 100% vs without-skill 88%
- Trigger eval: 96 queries, 97.9% accuracy
- eval-review.html viewer (237KB self-contained)
- benchmark.json structured results

### Phase 2 Complete — Description Optimization

- All 24 skills → 200+ char descriptions with "Use when..." trigger patterns
- `opp-tree` description expanded (307→646 chars)
- `run_eval.py` baseline: 94/96 passed

### Phase 1 Complete — Structure Migration

- Plugin manifests: PLUGIN.md → `.claude-plugin/plugin.json` (×5)
- Command frontmatter: removed unofficial `skills:` field (×12)
- All skills: added `argument-hint` frontmatter (×24)

---

## [0.3.0] — 2026-03-06

### Initial Content Release

- 5 plugins: oracle, atlas, forge, argus, muse
- 24 skills with Korean concepts + English instructions
- 12 commands (multi-skill chaining workflows)
- Greek mythology naming: Oracle / Atlas / Forge / Argus / Muse
- README.md (EN) + README-ko.md (KO)
- CONTRIBUTING.md + GUIDE-ko.md
