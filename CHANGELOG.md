# Changelog

All notable changes to AI_PM_Skills are documented here.

---

## [0.7.2] — 2026-05-16

### Added — Context Engineering Layer (3 new artifacts)

**Problem**: hplan ran evidence-rubric scoring even when the context fed to it was garbage — no way to know if a 45/100 score reflected a weak idea or weak research.

**Solution**: a full Context Engineering layer that gates on *input quality* before running rubrics.

#### `hplan/scripts/context_quality_scorer.py` — Context Quality Score (CQS)

RAGAS-inspired 100-point scorer measuring PM research richness *before* the evidence rubric runs. 6 dimensions (100 pts total):

| Dimension | Max | Signal |
|-----------|-----|--------|
| Interview volume | 25 | Torres convergence threshold: 5+ = pattern likely |
| Segment diversity | 20 | Behavioral ICP > demographic ICP |
| Evidence recency | 20 | within_30d = fresh signal; older = decayed |
| Source independence | 15 | +5 per type (interviews / public reviews / market data) |
| Competitor coverage | 10 | pricing + segment depth required |
| Workaround specificity | 10 | tool + quantified pain = strong demand |

Gate verdicts: CQS ≥ 75 = HIGH ✅ / 55-74 = MODERATE ⚠️ / 30-54 = LOW ⚠️ / < 30 = INSUFFICIENT 🚫 (blocks gate).

No external dependencies (pure stdlib). `--json` flag for CI integration.

```bash
python3 hplan/scripts/context_quality_scorer.py harness/context-intake.md
python3 hplan/scripts/context_quality_scorer.py --json harness/context-intake.md
```

#### `hplan/references/competitor-context.md` — Competitive Gate Template

5-Block structure extracting GO/HOLD signals from competitive analysis:

- **Block A**: Market existence — direct + indirect competitors
- **Block B**: Segment gap — what incumbent neglects + your wedge
- **Block C**: Business model conflict — copy cost for incumbent (counterposition test)
- **Block D**: Hard blockers — 3 boolean fields; any `true` = immediate HOLD
- **Block E**: Entry rationale — `why_now` + `unfair_advantage` (both required)

Copy template to `harness/competitor-context.md` per project.

#### `hplan/commands/hplan.md` — Step 0 Context Intake Check added

`/hplan` orchestrator now runs a pre-flight before Step 1 (exclusions):
1. Reads `harness/context-intake.md` if present → runs CQS scorer → blocks if CQS < 30
2. Reads `harness/competitor-context.md` if present → any `blocker == true` → immediate HOLD

### Added — Freshness Enforcement + Dual-Defense Hook (Phase 1, shipped 2026-05-14)

**`hplan/hooks/gate_guard.py`** extended with `check_freshness()`:
- Reads `context_dates` from `harness/build-gate/checkpoint.json`
- Per-field thresholds: `customer_interviews` warn 60d/block 90d; `competitive_analysis` warn 45d/block 90d; `provider_pricing` warn 30d/block 60d; `market_size` warn 90d/block 180d
- Backward compatible: absent `context_dates` → silently passes

**`scripts/install-hooks.sh`** — git pre-commit hook installer (second defense layer):
- `gate_guard.py` = soft UX warning when Claude attempts the write
- `git pre-commit` = deterministic hard block before the commit lands
- `CLAUDE_HPLAN_BYPASS=1` env var for authorized bypass

**`hplan/references/context-intake.md`** — 9-section structured intake template with ✅/❌ inline examples for every field. Eliminates LLM inference dependency on GIGO inputs.

### Fixed — Pre-commit hook reads staged index, not working tree (security)

**Reported by**: Codex adversarial review.

**Bug**: `scripts/install-hooks.sh` read `harness/build-gate/checkpoint.json` from the working tree via `open(path)`. Git commits the index, not the working tree — a user could leave an approved checkpoint unstaged while staging guarded PRD/spec files; the hook would pass, but the resulting commit contained no approved checkpoint.

**Fix**: Replace `open(checkpoint)` with `git show :harness/build-gate/checkpoint.json` to read the index blob. Also run `context_dates` freshness threshold check against the staged blob (was: only gate_guard.py soft warning; now hard-blocks stale evidence at commit time).

Bypass: `CLAUDE_HPLAN_BYPASS=1` still available for authorized use.

---

### Added — Dovetail artifact rule + Netflix density penalty in CQS interview scoring

Two design weaknesses identified via adversarial review + market research (Guest et al. 2006, Dovetail, Netflix DORA):

**약점 2 — self-report unverifiable (Dovetail artifact rule)**
- New field: `interview_artifact` — link to Zoom recording / transcript / Dovetail board / note file. One artifact required.
- `score_interview_volume()` caps at 12/25 when `interview_count > 0` but no artifact is present.
- Prevents zero-evidence interview count claims from scoring as HIGH.

**약점 3 — gamification incentive (Netflix density penalty)**
- New field: `unique_insights` — number of distinct insights discovered across interviews.
- Density = `unique_insights / interview_count`; if < 0.5 → −3 pts applied.
- Discourages bulk low-quality interviews that inflate count without discovery.

**Evidence**: gaming scenario (10 interviews, no artifact, 1 insight) → 9/25. Honest scenario (10 interviews, artifact linked, 7 insights) → 25/25. The 16-point gap crosses the MODERATE ↔ HIGH boundary.

**약점 1 note — threshold calibration**: CQS thresholds (30/55/75) remain as **v0.7.2 hypotheses** — empirically derived only from Guest, Bunce & Johnson (2006) saturation research and Stage-Gate risk calibration patterns. Real calibration requires outcome tracking: collect 20+ hplan-gated project results (6-month retention, COGS accuracy) and back-calculate from pass/fail distributions. Planned for a future release once usage data accumulates.

---

## [0.7.1] — 2026-05-14

### Changed — `deliver/skills/prd` expanded to **Unified PRD 14-section**

Previously the `prd` skill was Agent-PRD-only (7-section: Overview / Instruction / Tools / Memory / Trigger / Output / Failure). This expansion unifies it with the customer-facing product PRD format so PMs maintain a **single source of truth** for both the product and the LLM agents inside it.

**Why unify:**
- In 2026, virtually every SaaS contains an LLM agent. The product PRD vs agent PRD split was artificial.
- One PRD = one cognitive entry point for PMs and solo builders.
- Solo-builder 60-day cycle teams maintain a single PRD they re-version (v0.1 → v0.3) instead of juggling two documents.

**New 14-section structure:**

Top (1-6) — People / Problem / Decisions
1. ICP & personas (via `discover/agent-gtm` beachhead 5-criteria)
2. JTBD with Switch 4 Forces
3. Core problem + 10x value (quantified)
4. Decision options matrix (`discover/build-or-buy` + `architect/orchestration` + `discover/hitl`)
5. Out-of-scope (min 5, via `hplan/exclusions`)
6. Now/Next/Later + cogs p50/p90 (via `discover/cost-sim`)

Middle (7-11) — Agent / Execution Spec
7. Role + Primary Goal + Anti-Goals (≥ 3) — `deliver/instruction` for detail
8. Tools & Integrations + call limits mandatory
9. Memory & Context (3-tier: Working / Long-term / Procedural)
10. Trigger & Execution Flow (Cron/Event/Manual/Pipeline)
11. Output Specification + sample

Bottom (12-14) — Metrics / Hypotheses / Failure
12. Dual-axis OKR (North Star + Business + Operational + Anti-Metric; cost KR mandatory) — `measure/north-star` + `deliver/okr`
13. Top-3 hypotheses (Value/Feasibility/Reliability/Ethics) + 2-day experiment — `discover/assumptions`
14. Failure modes (≥ 4) + Human-in-the-loop triggers

**Migration from v0.6 → v0.7 PRD:**

| v0.6 (Agent PRD 7-section) | v0.7 (Unified 14-section) |
|---|---|
| Section 1 Overview | Section 1 (페르소나) + Section 3 (문제) |
| Section 2 Instruction Design | Section 7 (Role + Anti-Goals) |
| Section 3 Tools & Integrations | Section 8 (same) |
| Section 4 Memory Strategy | Section 9 (same) |
| Section 5 Trigger & Execution | Section 10 (same) |
| Section 6 Output Specification | Section 11 (same) |
| Section 7 Failure + Success Metrics | Section 12 (success) + Section 14 (failure) split |

New sections to fill in for migration: 1·3·4·5·6·13 (people / decisions / hypotheses).

**Pure-agent use case (internal LLM agents)**:
Section 1·3 personas = internal users. Section 2 JTBD = internal workflow. Section 7-11 stays detailed.

**Pure-SaaS use case (no LLM agent)**:
Section 7-11 may be marked "N/A — no AI feature" with a single line, leaving placeholders for future AI additions.

**Quality Gate**: `scripts/validate-prd.sh` updated to check all 14 sections (was 7). 17 quality gate items total (14 sections + consistency + TK citations + Y/N coverage).

### Updated

- `deliver/skills/prd/SKILL.md` (449 lines) — 14-section template + Trigger Gate + Quality Gate + Phase 1-5 instructions
- `deliver/commands/write-prd.md` (123 lines) — 5-phase chain with 2 user checkpoints
- `deliver/skills/prd/examples/good-01.md` — 1인 변호사 한국 판례 RAG SaaS (full 14-section example)
- `deliver/skills/prd/examples/bad-01.md` — anti-pattern with 14-section diagnostic table
- `deliver/skills/prd/references/test-cases.md` — 17 Quality Gate items + interview validation
- `deliver/skills/prd/references/troubleshooting.md` — 10 FAQs (general SaaS vs agent-heavy SaaS, etc.)
- `deliver/skills/prd/context/domain.md` — 60-day cycle + domain notes + v0.6 → v0.7 migration table
- `scripts/validate-prd.sh` — 14-section keyword check
- `README.md` / `README-ko.md` — `prd` skill description updated to "Unified PRD 14-section"

### Not breaking — backward compatible

- Existing v0.6 Agent PRDs remain valid; missing sections (1·3·4·5·6·13) show as "TBD" in validate-prd.sh warnings but don't block.
- `/write-prd` command preserved (no rename); chain extended.

---

## [0.7.0] — 2026-05-14

운영 노하우 4영역(실행 통합 / PRD 검증 깊이 / 에이전트 생태계 / PPTX 생산성)을 hplan에 흡수.

### Added — new plugin

- **operate** — 에이전트 포트폴리오 운영. 단일 에이전트 KPI(measure)를 넘어서 5+ 에이전트 운영을 다룬다.
  - `agent-portfolio` — T1~T5 티어링 + 인시던트 가중치
  - `scorecard-5axis` — Accuracy/Reliability/Cost/Velocity/Satisfaction 5축 가중 점수
  - `weekly-rollup` — 주차별 평균·Δ·Top 이동자·이상치 자동 요약
  - `cross-team-routing` — capability + 부하 + 티어 + handoff cost 기반 단일 라우팅 결정

### Added — deliver 확장 (실행 통합도)

- `deliver/harness-design` — 4명+ 빌드 팀 + Ralph Loop + 백업 + dry-run + pending_inputs 배치
- `deliver/parallel-team` — 독립 태스크 ≥2 시 worktree 격리 병렬 디스패치
- `deliver/build-loop` — 발견→리서치→설계→PRD→분해→구현 한 루프 (`/build`)

### Added — PRD mermaid 정합성 게이트 (결정론 검증)

- `scripts/validate-mermaid.py` — workflow ↔ userflow ↔ requirements 차분 검증 Python 스크립트
- `scripts/validate-prd.sh`가 mermaid 검증을 자동 호출
- `deliver/skills/prd/SKILL.md`에 게이트 섹션 + 두 다이어그램 의무화
- `deliver/skills/prd/examples/good-02-mermaid-consistency.md`, `bad-02-mermaid-orphan.md` 예시
- `cogs-sentinel`과 같은 결정론 게이트 가족

### Changed — pptx 4엔진 라우터

- `deliver/skills/pptx-ai-slide`가 단일 흐름에서 **4엔진 라우터**로 재정의
  - mckinsey (30+장, 강의 시리즈)
  - hifidelity (≤10장, 이미지 자동 생성)
  - html-qa (5~25장, 디폴트, 자동 QA)
  - video (영상 입력 전처리, 후속 엔진 체이닝 필수)
- `references/engine-comparison.md`, `examples/good-02-engine-routing.md`, `bad-02-engine-misroute.md` 추가
- description을 라우터 문법으로 갱신

### Added — profiles/ 패턴

- `profiles/_template/` — 새 운영자가 복사해서 시작할 yaml 4종
  - `agent-fleet.yaml`, `scorecard-weights.yaml`, `pptx-engines.yaml`, `ralph-loop.yaml`
- `.gitignore`에 `profiles/*` + `!profiles/_template/` + `!profiles/README.md` 추가
- 공개 스킬 ↔ 개인 운영 데이터 레이어 분리

### Added — pm-engine starter TK 4종

- `learn/skills/pm-engine/examples/PM-ENGINE-MEMORY-STARTER.md`에 TK-006~TK-009 추가
- TK-006: 독립 태스크 ≥2 → worktree + 4명+ 팀
- TK-007: PRD는 workflow + userflow 두 다이어그램 정합성 검증
- TK-008: 5+ 에이전트 → 5축 가중 ScoreCard
- TK-009: PPTX는 4엔진 라우팅 결정으로 시작

### Added — 메타 데모 시드

- `tools/intro-video/scenes/v0.7-meta-demo-script.md` — "hplan으로 hplan을 짠다" 70초 자기참조 영상 스크립트

### Infra

- `validate_plugins.py`의 PLUGINS에 `operate` 추가
- 총 7 플러그인 / 50 스킬 / 18 커맨드
- `evals/trigger-evals.json`에 신규 7개 스킬(harness-design, parallel-team, build-loop, agent-portfolio, scorecard-5axis, weekly-rollup, cross-team-routing) 시드 추가 — 스킬당 should_trigger 2건 + should_not 2건. 총 31 스킬 / 124 쿼리. **실제 회귀 평가는 v0.7.x patch에서 진행 예정** (96→124 쿼리 확장 측정 포함).

---

## [0.6.0] — 2026-05-11

### Breaking — 5 plugins renamed to PM standard vocabulary

The original Greek-mythology names (oracle / atlas / forge / argus / muse) were chosen for memorability in v0.3 but caused two problems:
- New users had to learn what each mythology name meant
- They didn't match the vocabulary PMs actually use (Double Diamond, Lean Startup, Teresa Torres CDH)

v0.6 renames each plugin to a PM lifecycle word everyone recognizes:

| Old | New | Why |
|---|---|---|
| `oracle` | `discover` | Continuous discovery / Double Diamond's first D |
| `atlas` | `architect` | System architecture, not UI design (avoids "design = UI" confusion) |
| `forge` | `deliver` | Double Diamond's Deliver phase |
| `argus` | `measure` | Lean Startup's Build–Measure–Learn |
| `muse` | `learn` | Lean Startup's Build–Measure–Learn |

`hplan` (Gate) is unchanged — it's an English brand acronym for **H**arness **Plan**ning and intentionally distinct from the lifecycle stage names.

New lifecycle: `hplan → discover → architect → deliver → measure → learn`

### Changed

- Plugin directories renamed (5 × `git mv`)
- All 6 `plugin.json` `name` fields updated; version bumped to 0.6.0
- `.claude-plugin/marketplace.json` plugin entries renamed + descriptions refreshed
- README.md / README-ko.md / GUIDE-ko.md / CONTRIBUTING.md — every reference to the old plugin names updated
- Plugin lifecycle SVG (`docs/images/plugin-lifecycle.svg`) — box labels + lifecycle phase labels (Execution → Delivery, Monitoring → Measurement, Knowledge → Learning)
- How-it-works SVG (`docs/images/how-it-works.svg`) — plugin pills relabeled
- All SKILL.md "Route to Other Skills When" cross-references updated
- `validate_plugins.py` PLUGINS list updated

### Migration for existing users

Old install commands like `/plugin install oracle@kimsanguine-hplan` now become `/plugin install discover@kimsanguine-hplan`. GitHub auto-redirect handles old paths; users with installed plugins should re-install under the new name.

### Preserved (intentional)

- The Greek tier-name **`Atlas`** inside `architect/skills/3-tier/SKILL.md` — refers to the Prometheus → Atlas → Worker pattern, which is the *content* of the skill, not the plugin name. Mythology tier name remains.
- All historical CHANGELOG entries and `.archive/` work logs.

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
- Added `Route to hplan when ...` lines to 7 existing skills: `discover/cost-sim`, `discover/opp-tree`, `discover/hitl`, `discover/assumptions`, `discover/build-or-buy`, `deliver/prd`, `measure/burn-rate`
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
