# AI_PM_Skills

> An open-source skillset for PMs who design, build, and operate AI agents as products

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-35-blue?style=flat-square)]()
[![Plugins](https://img.shields.io/badge/plugins-5-purple?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![한국어](https://img.shields.io/badge/lang-한국어-blue?style=flat-square)](README-ko.md)

<p align="center">
  <img src="docs/images/plugin-lifecycle.svg" alt="Agent Product Lifecycle" width="800"/>
</p>

```bash
/discover customer support workflow to automate
/architecture multi-language FAQ + escalation agent
/write-prd customer support auto-response agent
/health-check support agent weekly review
/extract "80% of customers who say 'urgent' aren't actually urgent"
```

---

## The Problem This Project Solves

In 2026, PMs are being asked to "build an agent" — but existing PM skills don't prepare you for that.

General PM skills teach you to **use AI as a tool** — write PRDs faster, generate OKRs, analyze competitors. But when you're **building agents as products**, the questions are fundamentally different:

- "What would it cost to run this agent at 1,000 users/day?"
- "How does an agent recover from hallucination?"
- "How do I orchestrate multiple agents together?"
- "How do I encode 3 months of operational judgment into the agent's instructions?"

This project turns those questions into skills.

---

## What Makes This Different?

### 1. Skills Built for Agent Building

Where general PM skills cover "how to write a good PRD," this skillset covers "how to spec failure recovery, context window management, and tool permissions in an agent PRD." Every skill addresses the decisions agent-building PMs actually face — multi-agent orchestration, model routing, memory architecture, cost scaling.

### 2. Validate Before Building, Reference While Building

| Tool | What it does |
|------|-------------|
| **Build vs Buy** | Compare build-vs-buy across 6 axes before committing |
| **Reliability/Ethics 4-Axis Validation** | Validate reliability and ethics assumptions, not just value |
| **Human-in-the-Loop Design** | Draw the boundary between agent autonomy and human intervention |
| **Token Cost Simulation** | Project monthly costs at 10 → 100 → 1,000 user scale |
| **4-Axis Pre-Impl Review** | Final checkpoint before coding — value, feasibility, reliability, ethics + Mermaid visualization |
| **Image Gen Pipeline** | Reference architecture for building Gemini-based image generation agents |

### 3. Tacit Knowledge That Accumulates

Most skills are one-shot — use them and move on. The `muse` plugin is different. It structures your operational judgment into TK (Tacit Knowledge) units, then injects them into agent instructions. The more you use it, the smarter your agents get — and that knowledge stays yours.

### 4. Claude Spec Compliance

```
marketplace.json          ← Claude Code marketplace schema
evals/evals.json          ← Quality evals (10 tests, 54 assertions)
evals/trigger-evals.json  ← Trigger accuracy evals (96 queries)
evals/per-skill/*.json    ← Per-skill evals
plugin.json (×5)          ← Plugin manifests
```

Full compliance with Claude Code's official spec — marketplace JSON schema, plugin manifests, and eval system. Automated structure validation via `validate_plugins.py`.

### 5. MCP vs Skills Layer Guide

When building agents, the question always comes up: "Should this be an MCP server or a skill?" This skillset guides the architectural decision of how to divide external API connections (MCP) and domain knowledge (Skills) at design time.

### 6. Content Structural Rigor

Every skill follows a consistent content structure: **Core Goal → Trigger Gate → Failure Handling → Quality Gate → Examples**. The Trigger Gate (Use / Route / Boundary) ensures the right skill fires for the right task. The Failure Handling table covers detection and fallback for each failure mode. The Quality Gate is a self-check before delivery. This isn't formatting — it's the difference between a prompt and a production-grade skill.

> This content structure is a separate layer from Claude's "Skills 2.0" platform spec. See [Skill Internals](#skill-internals) below for how the two layers relate.

---

## How It Works

<p align="center">
  <img src="docs/images/how-it-works.svg" alt="How It Works — Skills, Commands, Plugins" width="700"/>
</p>

**Skills** are building blocks. Describe your task, and the matching skill loads automatically.

**Commands** chain multiple skills into workflows. Type `/write-prd` and it runs research → architecture → spec writing in sequence.

**Plugins** are installable packages. Install one or all five.

```
Plugin (oracle)
  ├── Skills: opp-tree, assumptions, build-or-buy, hitl, cost-sim, agent-gtm
  └── Commands: /discover, /validate
```

> Skills are standard SKILL.md files — they work with Gemini CLI, Cursor, Codex CLI, and Kiro too.

---

## Skill Internals

### Auto-Invocation

You don't call skills by name. **Describe your task in natural language, and Claude matches it against each SKILL.md's `description` field to auto-load the best fit.**

```
User:  "How does the agent recover from hallucination?"
         ↓
Claude: description matching → reliability skill auto-loads
         ↓
Skill:  Trigger Gate check → condition met → skill executes
```

Trigger accuracy is **97.9%** across 96 test queries. Every skill's `description` is 200+ characters long with explicit "Use when..." trigger patterns.

### SKILL.md Content Structure

All 35 skills follow the same content structure:

```
┌─────────────────────────────────────────────┐
│  Frontmatter                                │
│  - name, description (200+ chars), arg-hint │
├─────────────────────────────────────────────┤
│  Core Goal          ← 1-2 sentence purpose  │
├─────────────────────────────────────────────┤
│  Trigger Gate                               │
│  - Use: when to use this skill              │
│  - Route: when to redirect to another skill │
│  - Boundary: what's out of scope            │
├─────────────────────────────────────────────┤
│  Concepts + Procedures   ← main content     │
├─────────────────────────────────────────────┤
│  Failure Handling                           │
│  - Failure mode │ Detection │ Fallback      │
├─────────────────────────────────────────────┤
│  Quality Gate     ← pre-delivery checklist  │
├─────────────────────────────────────────────┤
│  Examples         ← good/bad output signals │
└─────────────────────────────────────────────┘
```

The **Trigger Gate** is the key innovation. Use / Route / Boundary conditions determine whether this skill should fire, redirect to another, or declare out-of-scope — eliminating skill collisions.

### Command Chaining

Commands (`/write-prd`, `/discover`, etc.) chain multiple skills into sequential workflows.

```
/discover customer support automation
  ① opp-tree     → opportunity mapping
  ② assumptions  → assumption validation
  ③ build-or-buy → feasibility scoring
  → consolidated report
```

| Command | Chained Skills | Plugin |
|---------|---------------|--------|
| `/discover` | opp-tree → assumptions → build-or-buy | oracle |
| `/validate` | assumptions → hitl → cost-sim | oracle |
| `/architecture` | orchestration → 3-tier → memory-arch | atlas |
| `/strategy-review` | moat → biz-model → growth-loop | atlas |
| `/write-prd` | prd → instruction → ctx-budget | forge |
| `/set-okr` | okr → kpi → north-star | forge+argus |
| `/sprint` | stakeholder-map → agent-plan-review | forge |
| `/health-check` | kpi → reliability → burn-rate | argus |
| `/cost-review` | burn-rate → cost-sim → router | argus+oracle+atlas |
| `/extract` | pm-framework (TK capture) | muse |
| `/decide` | pm-decision (pattern matching) | muse |
| `/tk-to-instruction` | pm-engine → instruction | muse+forge |

> Commands are Claude Code only. Other tools can use individual skills but not command chaining.

### Platform Spec vs Content Structure — Two Layers

AI_PM_Skills is built on two independent layers.

```
┌─ Platform Layer (Skills 2.0 Spec) ──────────────────────────┐
│  Skill platform spec defined by Claude Code                  │
│  frontmatter · auto-invocation · subagent · hooks            │
│  marketplace · evals · plugin directory structure             │
├─ Content Layer (AI_PM_Skills Structure) ─────────────────────┤
│  Skill content design pattern defined by this project        │
│  Core Goal → Trigger Gate → Failure Handling                 │
│  → Quality Gate → Examples                                   │
└──────────────────────────────────────────────────────────────┘
```

**Platform Layer** defines *how Claude Code discovers and executes skills*. YAML frontmatter schema, directory structure, and `description`-based auto-invocation live here. This spec is provided by Claude Code and evolved from Skills 1.0 (2025) to Skills 2.0 (2026).

**Content Layer** is about *what goes inside each skill*. On the same platform, skills without Trigger Gates cause collisions, and skills without Failure Handling break in production. AI_PM_Skills' content structure (Core Goal → Trigger Gate → ... → Examples) is the design pattern for this layer — and this project's unique contribution.

> To avoid confusion: "Skills 2.0" in this doc refers to Claude Code's **platform spec**. "Content structure" refers to AI_PM_Skills' **skill design pattern**.

### Skills 1.0 vs Skills 2.0 — What AI_PM_Skills Uses

Claude Code's skill platform evolved from Skills 1.0 (2025) to Skills 2.0 (2026). AI_PM_Skills runs on Skills 2.0 and leverages the following features.

| Feature | Skills 1.0 (2025) | Skills 2.0 (2026) | AI_PM_Skills Usage |
|---------|-------------------|-------------------|-------------------|
| **Skill location** | `.claude/commands/` | `.claude/skills/` + plugin directories | ✅ 5 plugin directory structure |
| **Frontmatter** | None (plain markdown) | `name`, `description`, `argument-hint`, `allowed-tools`, `context`, etc. | ✅ `name`, `description` (200+ chars), `argument-hint`, `context`, `allowed-tools` |
| **Auto-invocation** | ❌ Explicit `/` commands only | ✅ Auto-load via `description` matching | ✅ 97.9% accuracy on 96 queries |
| **Command integration** | Commands and skills separate | Commands merged into skill system | ✅ 12 commands |
| **Variable substitution** | ❌ | `$ARGUMENTS`, `${CLAUDE_SKILL_DIR}`, etc. | ✅ `$ARGUMENTS` in all commands |
| **Subagent execution** | ❌ | `context: fork` for isolated execution | ✅ 5 review/analysis skills (`premortem`, `agent-plan-review`, `reliability`, `cohort`, `agent-ab-test`) |
| **Tool restriction** | ❌ | `allowed-tools` limits available tools | ✅ All 35 skills — 3-tier classification (Read/Write · +WebSearch · +Edit/Bash) |
| **Marketplace** | ❌ | `marketplace.json` schema | ✅ Marketplace registration |
| **Eval system** | ❌ | `evals.json` schema | ✅ 10 tests, 54 assertions |
| **Model selection** | ❌ | `model` field for execution model | ✅ All 35 skills default to `model: sonnet` (user-configurable) |
| **Dynamic injection** | ❌ | `` !`command` `` injects external data at runtime | ✅ 5 core skills — project memory + PM tools (Linear/GitHub) auto-integration |
| **Hooks** | ❌ | `hooks` for skill lifecycle events | ✅ 5 core skills — Quality Gate validation scripts on Stop |

> ⚠️ `hooks` inside plugin skills have a known issue where they may not trigger ([#17688](https://github.com/anthropics/claude-code/issues/17688)). Implementation follows the spec and will auto-activate when the issue is resolved.

---

## File Structure

```
AI_PM_Skills/
├── .claude-plugin/
│   └── marketplace.json              # Marketplace registration
│
├── oracle/                           # Discovery — What agent to build?
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── opp-tree/SKILL.md         #   Opportunity Solution Tree
│   │   ├── assumptions/SKILL.md      #   4-axis assumption validation
│   │   ├── build-or-buy/SKILL.md     #   Build vs Buy decision
│   │   ├── hitl/SKILL.md             #   Human-in-the-Loop scope
│   │   ├── cost-sim/SKILL.md         #   Token cost simulation
│   │   └── agent-gtm/SKILL.md        #   Go-to-Market strategy
│   └── commands/
│       ├── discover.md               #   /discover
│       └── validate.md               #   /validate
│
├── atlas/                            # Architecture — How to structure it?
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── 3-tier/SKILL.md           #   3-tier multi-agent design
│   │   ├── orchestration/SKILL.md    #   Orchestration patterns
│   │   ├── biz-model/SKILL.md        #   Revenue model design
│   │   ├── router/SKILL.md           #   LLM model routing
│   │   ├── memory-arch/SKILL.md      #   Memory architecture
│   │   ├── moat/SKILL.md             #   Competitive moat analysis
│   │   └── growth-loop/SKILL.md      #   Data flywheel design
│   └── commands/
│       ├── architecture.md           #   /architecture
│       └── strategy-review.md        #   /strategy-review
│
├── forge/                            # Execution — How to spec and ship it?
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── instruction/SKILL.md      #   7-element instruction design
│   │   ├── prd/SKILL.md              #   Agent-specific PRD
│   │   ├── prompt/SKILL.md           #   PM-perspective prompt (CRISP)
│   │   ├── ctx-budget/SKILL.md       #   Context window budget
│   │   ├── okr/SKILL.md              #   Agent OKR
│   │   ├── stakeholder-map/SKILL.md  #   Stakeholder mapping
│   │   ├── agent-plan-review/SKILL.md#   4-axis pre-impl review
│   │   ├── gemini-image-flow/SKILL.md#   Image generation pipeline
│   │   ├── infographic-gif-creator/SKILL.md  # Animated infographic creation
│   │   ├── pptx-ai-slide/SKILL.md     #   Agent presentation deck
│   │   └── agent-demo-video/SKILL.md   #   Remotion-based demo video
│   └── commands/
│       ├── write-prd.md              #   /write-prd
│       ├── set-okr.md                #   /set-okr
│       └── sprint.md                 #   /sprint
│
├── argus/                            # Monitoring — How to measure and improve?
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── kpi/SKILL.md              #   Operational + business KPIs
│   │   ├── reliability/SKILL.md      #   Reliability audit
│   │   ├── premortem/SKILL.md        #   Failure mode analysis (FMEA)
│   │   ├── burn-rate/SKILL.md        #   Cost tracking/optimization
│   │   ├── north-star/SKILL.md       #   North Star Metric
│   │   ├── agent-ab-test/SKILL.md    #   A/B test design
│   │   ├── cohort/SKILL.md           #   Cohort analysis
│   │   └── incident/SKILL.md         #   Incident response protocol
│   └── commands/
│       ├── health-check.md           #   /health-check
│       └── cost-review.md            #   /cost-review
│
├── muse/                             # Knowledge — Turn PM tacit knowledge into agent assets
│   ├── .claude-plugin/plugin.json
│   ├── skills/
│   │   ├── pm-framework/SKILL.md     #   TK-NNN classification
│   │   ├── pm-decision/SKILL.md      #   Decision patterns
│   │   └── pm-engine/SKILL.md        #   PM-ENGINE-MEMORY
│   └── commands/
│       ├── extract.md                #   /extract
│       ├── decide.md                 #   /decide
│       └── tk-to-instruction.md      #   /tk-to-instruction
│
├── evals/                            # Eval system
│   ├── evals.json                    #   Quality evals (10 tests, 54 assertions)
│   ├── trigger-evals.json            #   Trigger accuracy (96 queries)
│   └── per-skill/                    #   Per-skill evals
│
├── eval-workspace/                   # Eval results + benchmarks
├── docs/images/                      # Diagrams, screenshots
├── validate_plugins.py               # Automated structure validation
├── GUIDE-ko.md                       # Scenario-based usage guide (KO)
├── CONTRIBUTING.md                   # Contribution guide
└── LICENSE                           # MIT
```

---

## Installation

### Option 1: Register via GitHub Marketplace (Recommended)

Register the marketplace in Claude Code, then install individual plugins.

```bash
# Step 1: Register marketplace
/plugin marketplace add kimsanguine/AI_PM_Skills

# Step 2: Install individual plugins
/plugin install oracle@kimsanguine-AI_PM_Skills
/plugin install atlas@kimsanguine-AI_PM_Skills
/plugin install forge@kimsanguine-AI_PM_Skills
/plugin install argus@kimsanguine-AI_PM_Skills
/plugin install muse@kimsanguine-AI_PM_Skills
```

> Restart Claude Code after installation to load the skills.

### Option 2: Clone and Load Locally

Clone from GitHub and load directly with `--plugin-dir`.

```bash
# Clone the repo
git clone https://github.com/kimsanguine/AI_PM_Skills.git

# Load individual plugins (pick what you need)
claude --plugin-dir ./AI_PM_Skills/oracle
claude --plugin-dir ./AI_PM_Skills/forge

# Or load all at once
claude --plugin-dir ./AI_PM_Skills/oracle \
       --plugin-dir ./AI_PM_Skills/atlas \
       --plugin-dir ./AI_PM_Skills/forge \
       --plugin-dir ./AI_PM_Skills/argus \
       --plugin-dir ./AI_PM_Skills/muse
```

Not sure which agent to build yet? → Start with `oracle`.
Already know what to build? → Start with `forge`.

### Other AI Tools

Skill files (SKILL.md) are standard Markdown — they work outside Claude Code too. Command chaining (`/write-prd`, etc.) is Claude Code only.

| Tool | Skills | Commands | How to use |
|------|:------:|:--------:|-----------|
| **Gemini CLI** | ✅ | ❌ | Copy to `.gemini/skills/` |
| **Cursor** | ✅ | ❌ | Copy to `.cursor/skills/` |
| **Codex CLI** | ✅ | ❌ | Copy to `.codex/skills/` |
| **Kiro** | ✅ | ❌ | Copy to `.kiro/skills/` |

```bash
# Copy all skills to another tool
for plugin in oracle atlas forge argus muse; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

---

## Plugins

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

**Examples:**
```
"Is it worth building an agent to automate customer onboarding?"
→ build-or-buy skill auto-loads

/discover customer support workflow
→ opportunity mapping → assumption check → feasibility scoring
```

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

**Examples:**
```
"This agent handles 5 task types — what architecture should I use?"
→ orchestration skill auto-loads

/architecture multi-step document processing pipeline
→ pattern selection → tier structure → memory architecture
```

</details>

<details>
<summary><strong>3. forge</strong> — How to spec and ship it? <code>(11 skills, 3 commands)</code></summary>

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `instruction` | Define Role/Context/Goal/Tools/Memory/Output/Failure with least-privilege tool access | "What goes in (and out of) the system prompt?" |
| `prd` | 7-section agent spec: Instruction/Tools/Memory/Triggers/Output/Failure with dual narrative (tech + biz) | "I need a PRD that covers hallucination recovery and tool permissions" |
| `prompt` | CRISP framework (Context/Role/Instruction/Scope/Parameters) + Why-First principle + 7 failure pattern avoidance | "Longer prompts make my agent behave worse" |
| `ctx-budget` | Estimate per-file token usage → classify Essential/Conditional/Excluded → 70% threshold alerts | "How do I fit 5 RAG docs + chat history into 128K?" |
| `okr` | Dual-axis OKRs: Business Impact (time/cost/error savings) + Operational Health (accuracy/cost/reliability) with mandatory cost KR | "Is 95% accuracy enough, or do I need cost metrics too?" |
| `stakeholder-map` | Power-Interest matrix + blocker-by-type response strategies + internal champion cultivation | "Legal is blocking the agent rollout — how do I get buy-in?" |
| `agent-plan-review` | Scope/Architecture/Instruction/Reliability 4-axis review + failure mode matrix (5+ types) + Mermaid output | "Find the holes in this design before we start coding" |
| `gemini-image-flow` | End-to-end Gemini API image pipeline (Phase 0-7) with model tier selection (Flash/Pro) | "Build a sketch→code or image→marketing asset pipeline" |
| `infographic-gif-creator` | Convert agent architecture / workflow / data flows into HTML/CSS → GIF/MP4 animations | "Show the multi-agent flow to execs in a 1-min animation" |
| `pptx-ai-slide` | Translate agent project into story-driven slide decks (pitch / review / investor variants) | "I present to the board next week — 10 slides max" |
| `agent-demo-video` | Compose screen recordings + architecture animations + narration + subtitles via Remotion | "Show non-technical stakeholders what the agent actually does" |

**Commands:** `/write-prd` · `/set-okr` · `/sprint`

**Examples:**
```
"Write the PRD for a meeting summarizer agent"
→ prd skill loads (includes failure recovery, context management, tool permissions)

/write-prd customer support escalation agent
→ requirements → instruction design → full agent PRD
```

</details>

<details>
<summary><strong>4. argus</strong> — How to measure and improve? <code>(8 skills, 2 commands)</code></summary>

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `kpi` | Define 5-7 operational (latency/success/error rate) + business (completion/satisfaction/cost-per-task) metrics with leading/lagging split | "What goes on the agent dashboard?" |
| `reliability` | Quantify P95/P99 worst cases + design safeguards by input/model/integration failure type + set SLA tiers (Basic→Critical) | "3 out of 100 responses hallucinate — is that acceptable?" |
| `premortem` | Score 10-15 failure modes by Severity × Likelihood × Detection Difficulty (RPN) + quarterly re-review | "Give me a 'this must not break' list before launch" |
| `burn-rate` | Visualize token costs by model/task/segment + spike detection + monthly budget caps with alerts | "Token costs jumped 40% this week — what caused it?" |
| `north-star` | Select one metric via 5 criteria (Actionable/Measurable/Owner/Directional/Feasible) + set anti-metrics | "We track 8 KPIs but the team doesn't know which one matters most" |
| `agent-ab-test` | Calculate MDE + run concurrent (not sequential) experiments + control for LLM nondeterminism + p-value validation | "Prompt A vs B — is the difference real or just noise?" |
| `cohort` | Track performance by deployment cohort (4-week minimum, n≥100) + control external variables | "Did v2.1 actually improve over v2.0?" |
| `incident` | Detect silent failures + triage severity + contain blast radius + 5 Whys postmortem (3+ iterations) | "The agent has been silent for 30 minutes — no alerts fired" |

**Commands:** `/health-check` · `/cost-review`

**Examples:**
```
"Token costs jumped 40% this week — what happened?"
→ burn-rate skill loads (cost analysis + optimization)

/health-check onboarding agent
→ KPI review → reliability check → cost anomaly detection → weekly summary
```

</details>

<details>
<summary><strong>5. muse ⭐</strong> — Turn PM tacit knowledge into agent assets <code>(3 skills, 3 commands)</code></summary>

| Skill | What it does | When to use |
|-------|-------------|-------------|
| `pm-framework` | Convert implicit judgment into TK-NNN units with activation/deactivation conditions + knowledge graph linking | "3 years of agent ops experience is stuck in my head" |
| `pm-decision` | Build a pattern library of recurring PM decisions with context, criteria, and known failures | "I've seen this situation before — why did I decide that way?" |
| `pm-engine` | Agents dynamically query TK knowledge graph at runtime + auto-extract 1 TK/day + auto-update instructions | "I want my agents to leverage my operational know-how automatically" |

**Commands:** `/extract` · `/decide` · `/tk-to-instruction`

**Examples:**
```
/extract "When reviewing agent PRDs, I always check if failure mode covers hallucination recovery"
→ capture TK → classify → link to knowledge graph

/tk-to-instruction onboarding agent
→ find relevant TK units → translate to agent instructions
```

> The framework is open-source; your data (PM-ENGINE-MEMORY.md) is your own asset.

</details>

---

## Benchmark

10 tests with 54 assertions measure what the skills actually add on top of base Claude.

| | With Skill | Without Skill | Delta |
|---|-----------|--------------|-------|
| **Pass Rate** | **100%** | 88% | **+12%** |
| **Avg Time** | 62s | 42s | +20s |

- **Capability-gating** — without the skill, Claude can't do it at all. `pm-framework` (TK structuring) drops to 40%, `3-tier` (multi-agent design) drops to 60-80%.
- **Quality-amplifying** — both pass, but the skill produces deeper output. `cost-sim` adds +46.6% output, `premortem` generates 2× more failure modes.
- **Agent-specific** — `prd` and `premortem` pass either way, but with-skill output follows agent-specific templates instead of generic PM structures.

Full data: [`eval-workspace/iteration-1/benchmark.json`](eval-workspace/iteration-1/benchmark.json)

> **Note:** Benchmark was measured on 32 skills (v0.4). Re-measurement with 35 skills and v1.0 structure is planned for the next iteration.

---

## Skill Origin

| Type | Count | Description |
|------|-------|-------------|
| 🟢 Adapted | 3 | Classic PM frameworks (OST, FMEA), recontextualized for agents |
| 🟡 Extended | 6 | Standard PM concepts, heavily extended with agent-specific dimensions |
| 🔴 New | 26 | Agent-only domains — cost-sim, 3-tier, TK-NNN, moat, reliability, growth-loop, etc. |

**74% is original work.**

---

## Status

**v1.0** — All 5 plugins complete (35 skills, 12 commands) with v1.0 structural upgrade

| Plugin | Skills | Commands | Trigger Accuracy | Status |
|--------|--------|----------|-----------------|--------|
| oracle | 6 | 2 | 18/20 (90%) | ✅ |
| atlas | 7 | 2 | 24/24 (100%) | ✅ |
| forge | 11 | 3 | 20/20 (100%) | ✅ |
| argus | 8 | 2 | 20/20 (100%) | ✅ |
| muse | 3 | 3 | 12/12 (100%) | ✅ |
| **Total** | **35** | **12** | **94/96 (97.9%)** | |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. New skills, improvements, and translations (EN↔KO) are all welcome.

---

## Author

**Sanguine Kim** — 20-year PM, AI Agent Builder

References & inspiration:
- Teresa Torres — *Continuous Discovery Habits*
- Anthropic — "Building Effective Agents"
- Steve Yegge — Gas Town parallel agent design principles
- Byeonghyeok Kwak — MCP-Skills hierarchy design principles
- Michael Polanyi — *The Tacit Dimension*

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
