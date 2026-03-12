# AI_PM_Skills

> 36 skills for PMs who build AI agents as products — not just use AI as a tool

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-36-blue?style=flat-square)]()
[![Plugins](https://img.shields.io/badge/plugins-5-purple?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![한국어](https://img.shields.io/badge/lang-한국어-blue?style=flat-square)](README-ko.md)

> ⭐ **If you're a PM building AI agents, star this repo** — it's the only skillset designed for the full agent product lifecycle.

<p align="center">
  <img src="docs/images/demo-terminal.svg" alt="AI_PM_Skills Demo — opp-tree skill auto-triggered" width="800"/>
</p>

---

## The Problem

In 2026, PMs are being asked to "build an agent" — but existing PM skills don't prepare you for that.

General PM skills teach you to **use AI as a tool** — write PRDs faster, generate OKRs, analyze competitors. But when you're **building agents as products**, the questions are fundamentally different:

- "What would it cost to run this agent at 1,000 users/day?"
- "How does an agent recover from hallucination?"
- "How do I orchestrate multiple agents together?"
- "How do I encode 3 months of operational judgment into the agent's instructions?"

This project turns those questions into **36 production-grade skills** across the full agent lifecycle.

---

## Quick Start (30 seconds)

```bash
# 1. Install the plugin
/plugin marketplace add kimsanguine/AI_PM_Skills
/plugin install oracle@kimsanguine-AI_PM_Skills

# 2. Just describe your task — the right skill loads automatically
"We handle 500 support tickets/day. Which parts should an agent handle?"
# → opp-tree skill auto-loads → opportunity mapping starts
```

---

## The Agent PM Journey — 5 Stages

This isn't a random collection of skills. It's a **complete lifecycle** — the same path every agent PM walks.

```
발견(Discover) → 설계(Architect) → 실행(Ship) → 운영(Operate) → 학습(Learn)
   oracle            atlas            forge          argus          muse
  6 skills          7 skills        12 skills       8 skills       3 skills
     ↑                                                               │
     └──────────── Accumulated TK feeds back into next agent ────────┘
```

| Stage | Plugin | The Question | Key Skills |
|-------|--------|-------------|------------|
| **Discover** | `oracle` | "What agent should we build?" | opp-tree · assumptions · build-or-buy · cost-sim · hitl · agent-gtm |
| **Architect** | `atlas` | "How should we structure it?" | 3-tier · orchestration · router · memory-arch · moat · growth-loop · biz-model |
| **Ship** | `forge` | "How to spec and ship it?" | claude-md · prd · instruction · prompt · ctx-budget · okr · stakeholder-map · agent-plan-review + 4 comms tools |
| **Operate** | `argus` | "How to measure and improve?" | kpi · reliability · premortem · burn-rate · north-star · agent-ab-test · cohort · incident |
| **Learn** | `muse` ⭐ | "How to make agents smarter over time?" | pm-framework · pm-decision · pm-engine |

Each skill **auto-loads from natural language** — describe your task and the right skill fires. Skills also **route across plugins**: burn-rate (argus) detects a cost spike → suggests router (atlas) for model change → triggers cost-sim (oracle) for re-simulation.

---

## Why This Is Different — 6 Things No Other Skillset Does

### ① Complete Agent Lifecycle, Not Random Tools

36 skills map to 5 stages of agent product development. This isn't "AI tools for PMs" — it's **a structured methodology for building agents as products**, from discovery to self-improving agents.

### ② Two-Layer Architecture — Platform and Content Separation

We separate **how Claude finds skills** (Platform Layer — Skills 2.0 spec) from **what goes inside each skill** (Content Layer). The Content Layer defines the Trigger Gate (Use/Route/Boundary) pattern that prevents skill collisions, plus domain-specific context in each skill's `context/domain.md`. Result: **97.9% trigger accuracy** across 96 test queries.

```
┌─ Platform Layer ──── Skills 2.0 Spec ──────────────────────┐
│  frontmatter · auto-invocation · subagent · hooks · evals   │
├─ Content Layer ──── AI_PM_Skills Pattern ──────────────────┤
│  Core Goal → Trigger Gate → Failure Handling                │
│  → Quality Gate → Examples · context/domain.md              │
└─────────────────────────────────────────────────────────────┘
```

### ③ Data Flywheel — PM Tacit Knowledge That Accumulates

muse is the moat. It structures your operational judgment into **TK (Tacit Knowledge) units**, then injects them into agent instructions. The more you use it, the smarter your agents get — and that knowledge **stays yours**.

```
PM 판단 기록 → /extract → TK-NNN 구조화 → PM-ENGINE-MEMORY.md 축적
  → /tk-to-instruction → 에이전트 시스템 프롬프트 업데이트 → 반복
```

This creates **switching cost**: competitors can copy the framework, but they can't copy your accumulated TK.

### ④ Eval-Driven ROI — Proof, Not Promises

Every skill is measured. 10 quality tests with 54 assertions prove what skills add vs base Claude. Result:

| | With Skill | Without Skill | Delta |
|---|-----------|--------------|-------|
| **Pass Rate** | **100%** | 88% | **+12%** |

`pm-framework` without skill drops to 40%. `cost-sim` with skill adds +46.6% output. This is **data-driven proof** that the skills work.

### ⑤ Good/Bad Examples for Data-Driven Improvement

Every skill includes `examples/good-01.md` and `examples/bad-01.md` — concrete right/wrong output pairs. Plus `references/test-cases.md` with edge case tables. These aren't decorative; they're **training signals** that make skill quality measurable and continuously improvable.

### ⑥ Skills 2.0 Full Spec + Instant Onboarding

Built on Claude Code's latest platform spec: auto-invocation, `context: fork`, `allowed-tools`, `model` field, dynamic `!command` injection, marketplace, and eval system. New users start with the [PM-ENGINE-MEMORY Starter Kit](muse/skills/pm-engine/examples/PM-ENGINE-MEMORY-STARTER.md) — 5 seed TK entries so the value is **immediate**, not "someday when I accumulate enough data."

---

## Plugins — Full Skill List

<details>
<summary><strong>1. oracle</strong> — What agent to build? <code>(6 skills, 2 commands)</code></summary>

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `opp-tree` | Build an opportunity tree scored by repeat frequency, automation fit, and judgment dependency | "We have 10 automation candidates — which one first?" |
| `assumptions` | Extract riskiest assumptions across 4 axes (Value/Feasibility/Reliability/Ethics) and design 2-day validation experiments | "What's the biggest risk before we start building?" |
| `build-or-buy` | Score Build vs Buy vs No-code across 6 axes (differentiation, speed, cost, customization, maintenance, domain) | "Should we use Intercom's bot or build our own agent?" |
| `hitl` | Set automation levels (1-5) and escalation triggers via reversibility × error-impact matrix | "Can the agent decide refunds, or must a human approve?" |
| `cost-sim` | Simulate monthly costs at 1→10→100→1,000 users by model pricing × call patterns | "Sonnet at 500 calls/day — what's the monthly bill?" |
| `agent-gtm` | Score beachhead segments (5 criteria) + design Shadow→Co-pilot→Auto→Delegation trust sequence | "How do we roll this agent out to B2B customers?" |

**Commands:** `/discover` · `/validate`
</details>

<details>
<summary><strong>2. atlas</strong> — How to architect it? <code>(7 skills, 2 commands)</code></summary>

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `3-tier` | Design Prometheus (strategy) → Atlas (coordination) → Worker (execution) roles, comms, and delegation | "I need 5 agents — who controls whom?" |
| `orchestration` | Compare Sequential/Parallel/Router/Hierarchical patterns by latency, error rate, and cost | "Should my doc pipeline run serial or parallel?" |
| `biz-model` | Design per-use / subscription / outcome-based pricing + variable cost analysis targeting >70% margin | "Per-API-call billing or monthly flat fee?" |
| `router` | Auto-route tasks to T1-T4 models by complexity + fallback chains for 40-80% cost reduction | "Simple FAQ → Haiku, complex analysis → Opus — auto?" |
| `memory-arch` | Design Working/Episodic/Semantic/Procedural memory layers + token-budget-aware retrieval | "How does today's session recall yesterday's context?" |
| `moat` | Diagnose 6 moat types: data flywheel, workflow lock-in, network effects, switching costs, specialization, brand | "A competitor ships a GPT clone — what's our defense?" |
| `growth-loop` | Design usage→data→improvement→re-use loops + cold-start solutions + anti-loop identification | "How do we make recommendations improve with every use?" |

**Commands:** `/architecture` · `/strategy-review`
</details>

<details>
<summary><strong>3. forge</strong> — How to spec and ship it? <code>(12 skills, 3 commands)</code></summary>

> **Onboarding (1):** claude-md
> **Core Spec (7):** instruction · prd · prompt · ctx-budget · okr · stakeholder-map · agent-plan-review
> **Communication (4):** gemini-image-flow · infographic-gif-creator · pptx-ai-slide · agent-demo-video

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `claude-md` ⭐ | Scan project structure → auto-generate CLAUDE.md → recommend matching AI_PM_Skills plugins | "New project — set up Claude Code context and find the right skills" |
| `instruction` | Define Role/Context/Goal/Tools/Memory/Output/Failure with least-privilege tool access | "What goes in (and out of) the system prompt?" |
| `prd` | 7-section agent spec: Instruction/Tools/Memory/Triggers/Output/Failure with dual narrative (tech + biz) | "I need a PRD that covers hallucination recovery and tool permissions" |
| `prompt` | CRISP framework (Context/Role/Instruction/Scope/Parameters) + Why-First principle + 7 failure pattern avoidance | "Longer prompts make my agent behave worse" |
| `ctx-budget` | Estimate per-file token usage → classify Essential/Conditional/Excluded → 70% threshold alerts | "How do I fit 5 RAG docs + chat history into 128K?" |
| `okr` | Dual-axis OKRs: Business Impact + Operational Health with mandatory cost KR | "Is 95% accuracy enough, or do I need cost metrics too?" |
| `stakeholder-map` | Power-Interest matrix + blocker response strategies + internal champion cultivation | "Legal is blocking the agent rollout — how do I get buy-in?" |
| `agent-plan-review` | 4-axis review + failure mode matrix (5+ types) + Mermaid output | "Find the holes in this design before we start coding" |
| `gemini-image-flow` | End-to-end Gemini API image pipeline with model tier selection | "Build a sketch→code pipeline" |
| `infographic-gif-creator` | Convert architecture / workflow into HTML/CSS → GIF/MP4 animations | "Show the multi-agent flow to execs" |
| `pptx-ai-slide` | Story-driven slide decks (pitch / review / investor variants) | "Board presentation — 10 slides max" |
| `agent-demo-video` | Screen recordings + animations + narration via Remotion | "Show non-technical stakeholders what the agent does" |

**Commands:** `/write-prd` · `/set-okr` · `/sprint`
</details>

<details>
<summary><strong>4. argus</strong> — How to measure and improve? <code>(8 skills, 2 commands)</code></summary>

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `kpi` | Define 5-7 operational + business metrics with leading/lagging split | "What goes on the agent dashboard?" |
| `reliability` | Quantify P95/P99 worst cases + design safeguards + set SLA tiers | "3 out of 100 responses hallucinate — acceptable?" |
| `premortem` | Score 10-15 failure modes by Severity × Likelihood × Detection Difficulty | "Give me a 'this must not break' list" |
| `burn-rate` | Visualize token costs by model/task + spike detection + budget caps | "Token costs jumped 40% — what caused it?" |
| `north-star` | Select one metric via 5 criteria + set anti-metrics | "Team doesn't know which KPI matters most" |
| `agent-ab-test` | Calculate MDE + concurrent experiments + control for LLM nondeterminism | "Prompt A vs B — real difference or noise?" |
| `cohort` | Track performance by deployment cohort (4-week minimum, n≥100) | "Did v2.1 actually improve over v2.0?" |
| `incident` | Detect silent failures + triage + contain blast radius + 5 Whys | "Agent silent for 30 min — no alerts fired" |

**Commands:** `/health-check` · `/cost-review`
</details>

<details>
<summary><strong>5. muse ⭐</strong> — Turn PM tacit knowledge into agent assets <code>(3 skills, 3 commands)</code></summary>

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `pm-framework` | Convert implicit judgment into TK-NNN units with activation/deactivation conditions + knowledge graph linking | "3 years of agent ops experience is stuck in my head" |
| `pm-decision` | Build a pattern library of recurring PM decisions with context, criteria, and known failures | "I've seen this situation before — why did I decide that way?" |
| `pm-engine` | Agents dynamically query TK knowledge graph at runtime + auto-extract 1 TK/day + auto-update instructions | "I want my agents to leverage my operational know-how automatically" |

**Commands:** `/extract` · `/decide` · `/tk-to-instruction`

> Start with the [PM-ENGINE-MEMORY Starter Kit](muse/skills/pm-engine/examples/PM-ENGINE-MEMORY-STARTER.md) — 5 seed TK entries to get going immediately.

> The framework is open-source; your data (PM-ENGINE-MEMORY.md) is your own asset.
</details>

---

## Installation

### Option 1: GitHub Marketplace (Recommended)

```bash
/plugin marketplace add kimsanguine/AI_PM_Skills
/plugin install oracle@kimsanguine-AI_PM_Skills   # or atlas, forge, argus, muse
```

### Option 2: Clone Locally

```bash
git clone https://github.com/kimsanguine/AI_PM_Skills.git
claude --plugin-dir ./AI_PM_Skills/oracle   # pick what you need
```

**First time with Claude Code?** → Start with `forge/claude-md` — it scans your project and recommends the right skills.
Not sure which agent to build yet? → Start with `oracle`.
Already know what to build? → Start with `forge`.

### Other AI Tools

| Tool | Skills | Commands | How to use |
|------|:------:|:--------:|-----------|
| **Gemini CLI** | ✅ | ❌ | Copy to `.gemini/skills/` |
| **Cursor** | ✅ | ❌ | Copy to `.cursor/skills/` |
| **Codex CLI** | ✅ | ❌ | Copy to `.codex/skills/` |
| **Kiro** | ✅ | ❌ | Copy to `.kiro/skills/` |

---

<details>
<summary><strong>📐 Architecture Deep-Dive</strong> — Two Layers, Skills 2.0, Trigger Gate, Commands</summary>

### Auto-Invocation

You don't call skills by name. Describe your task in natural language, and Claude matches it against each SKILL.md's `description` field to auto-load the best fit. Trigger accuracy: **97.9%** across 96 test queries.

### Cross-Plugin Routing

The Trigger Gate's "Route" field enables routing between plugins:

| From | Trigger Condition | Route To |
|------|------------------|----------|
| `opp-tree` | "Validate assumptions for top opportunity" | `assumptions` |
| `burn-rate` | "Need model routing change" | `router` |
| `prd` | "Need instruction design" | `instruction` |
| `pm-framework` | "Convert TK to agent instruction" | `pm-engine` |

### Command Chaining

| Command | Chained Skills | Plugin |
|---------|---------------|--------|
| `/discover` | opp-tree → assumptions → build-or-buy | oracle |
| `/architecture` | orchestration → 3-tier → memory-arch | atlas |
| `/write-prd` | prd → instruction → ctx-budget | forge |
| `/health-check` | kpi → reliability → burn-rate | argus |
| `/tk-to-instruction` | pm-engine → instruction | muse+forge |

### Skills 1.0 vs Skills 2.0

| Feature | 1.0 (2025) | 2.0 (2026) | AI_PM_Skills |
|---------|-----------|-----------|-------------|
| Auto-invocation | ❌ | ✅ | ✅ 97.9% |
| Subagent (`context: fork`) | ❌ | ✅ | ✅ 5 skills |
| Tool restriction | ❌ | ✅ | ✅ 3-tier |
| Marketplace + Evals | ❌ | ✅ | ✅ Full |
| Dynamic injection | ❌ | ✅ | ✅ 5 skills |
| Hooks | ❌ | ✅ | ⚠️ Spec-ready |

> ⚠️ `hooks` have a known issue ([#17688](https://github.com/anthropics/claude-code/issues/17688)). Fallback `validate_*.sh` scripts available in `references/`.

### File Structure

```
AI_PM_Skills/
├── oracle/           # Discovery (6 skills, 2 commands)
├── atlas/            # Architecture (7 skills, 2 commands)
├── forge/            # Execution (12 skills, 3 commands)
├── argus/            # Monitoring (8 skills, 2 commands)
├── muse/             # Knowledge (3 skills, 3 commands)
├── evals/            # Quality + trigger evals
├── docs/images/      # Diagrams
├── validate_plugins.py
└── CONTRIBUTING.md
```

### Skill Anatomy — What's Inside Each Skill

Every skill follows a consistent internal structure. This isn't just Skills 2.0 spec compliance — it's a **content architecture** designed for measurable quality and continuous improvement:

```
oracle/skills/opp-tree/           ← example skill
├── SKILL.md                      ← Core: frontmatter (name, description,
│                                    argument-hint, allowed-tools) +
│                                    Trigger Gate (Use/Route/Boundary) +
│                                    Failure Handling + Quality Gate
├── context/
│   └── domain.md                 ← Domain knowledge injected at runtime
│                                    (e.g., agent economics, industry benchmarks)
├── examples/
│   ├── good-01.md                ← ✅ Reference output — "this is what great looks like"
│   └── bad-01.md                 ← ❌ Anti-pattern — "this is what to avoid and why"
└── references/
    ├── test-cases.md             ← Edge cases, boundary conditions, eval criteria
    └── troubleshooting.md        ← Common failures + recovery patterns
```

**Why this matters:**

| Component | Purpose | Impact |
|-----------|---------|--------|
| `SKILL.md` Trigger Gate | Use/Route/Boundary → prevents wrong skill from firing | 97.9% trigger accuracy |
| `context/domain.md` | Domain expertise Claude doesn't have natively | +12~46% output quality |
| `examples/good-01.md` | Concrete "gold standard" output | Anchors Claude's generation |
| `examples/bad-01.md` | Explicit anti-patterns with explanations | Prevents common failures |
| `references/test-cases.md` | Edge cases + assertions | Powers eval system (54 assertions) |

This pattern repeats across all 36 skills — **130+ supporting files** that make each skill measurable, testable, and improvable.

</details>

<details>
<summary>📐 Plugin Lifecycle Diagram</summary>
<p align="center">
  <img src="docs/images/plugin-lifecycle.svg" alt="Agent Product Lifecycle" width="800"/>
</p>
</details>

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. New skills, improvements, and translations (EN↔KO) are all welcome.

---

## Author

**Sanguine Kim** — 20-year PM veteran, AI Agent Builder & Educator

Built and scaled AI Dubbing and AI Avatar products, then led Agentic AI product development. Currently exploring the path of AI Agent PM educator — helping PMs navigate the shift from "using AI" to "building agents as products."

📬 **For training, consulting, or workshop inquiries:** kimsanguine@gmail.com

If you're using this project for corporate training or educational content, I'd appreciate a quick note. Customized consulting and co-teaching are welcome.

- References: Teresa Torres (*Continuous Discovery Habits*), Anthropic ("Building Effective Agents"), Steve Yegge (Gas Town parallel agent design), Byeonghyeok Kwak (MCP-Skills hierarchy), Michael Polanyi (*The Tacit Dimension*)

---

## Related

| Repo | What | Link |
|------|------|------|
| **AI_PM** | Claude Code guide for PMs — learn the why and how | [github.com/kimsanguine/AI_PM](https://github.com/kimsanguine/AI_PM) |
| **AI_PM_Skills** | Ready-to-use agent skillset — the tools *(this repo)* | [github.com/kimsanguine/AI_PM_Skills](https://github.com/kimsanguine/AI_PM_Skills) |

> **AI_PM** teaches the thinking. **AI_PM_Skills** gives you the tools.

---

## License

MIT — [LICENSE](LICENSE)
