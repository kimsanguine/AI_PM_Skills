# Changelog

All notable changes to AI_PM_Skills are documented here.

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
