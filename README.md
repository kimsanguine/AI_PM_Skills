# AI_PM_Skills

> **How PMs Build AI Agents** — An open-source skillset for Product Managers who design, build, and operate AI agents

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![한국어](https://img.shields.io/badge/lang-한국어-blue?style=flat-square)](README-ko.md)

---

## Why This Project?

Most PM skill libraries help you **use AI as a tool** — write PRDs faster, generate OKRs, analyze competitors.

This project is different.

> **Skills for PMs who build, operate, and scale AI agents as products.**

In 2026, the bottleneck for agent-building PMs isn't coding ability. It's **intention and judgment** — what agent to build, how to design it, how to measure it, how to make it defensible.

This project converts 20 years of PM tacit knowledge into an open-source agent skillset.

---

## Quick Start

```bash
# Marketplace install (all 5 plugins at once)
claude plugin marketplace add kimsanguine/AI_PM_Skills

# Or install individually
claude plugin add oracle/    # Discovery
claude plugin add atlas/     # Architecture
claude plugin add forge/     # Execution
claude plugin add argus/     # Monitoring
claude plugin add muse/      # Knowledge
```

```bash
/discover [workflow to automate]       # Discover agent opportunities
/architecture [complex workflow]       # Design agent architecture
/write-prd [agent name]               # Write agent PRD
/health-check [agent name]            # Weekly health check
```

---

## What Makes This Different?

This skillset covers **6 domains that general PM skills don't touch**:

| Domain | What it does | Why it matters |
|--------|-------------|----------------|
| **Agent Economics** | Token cost simulation, scale projections, optimization strategies | An agent that costs $3K/month at 10 users becomes $30K at 100 — you need to model this before building |
| **Multi-Agent Architecture** | Prometheus-Atlas-Worker 3-tier design, orchestration patterns, model routing | Complex workflows need multiple agents working together, not a single monolith |
| **Agent-Specific PRD** | Instruction, Tools, Triggers, Memory, Failure Handling sections | Standard PRDs don't spec how an agent should fail gracefully or manage context windows |
| **Operational Reliability** | FMEA-based premortem, SLO design, error recovery patterns | Agents fail differently than software — hallucination, context drift, cost spikes |
| **Competitive Moats** | Data flywheel, process lock-in, knowledge moat analysis + anti-moat patterns | "We use GPT-4" is not a moat. Accumulated operational data and tacit knowledge is |
| **PM Tacit Knowledge** | TK-NNN (Never-ending Nuance Network) — extract, structure, and inject PM judgment into agent instructions (TK-001 → TK-999) | Your PM experience becomes a reusable asset; each TK links to others forming a knowledge graph that makes every agent smarter |

---

## Plugins

Each plugin is named after a figure from Greek mythology — chosen not as decoration, but because each archetype maps precisely to a phase of the agent product lifecycle.

| Plugin | Archetype | Why this name |
|--------|-----------|--------------|
| **oracle** | Oracle of Delphi — the seer who reveals what to pursue | Discovery phase: seeing which agent to build before committing |
| **atlas** | Atlas — the titan who holds the world's structure | Architecture phase: bearing the weight of system design decisions |
| **forge** | Hephaestus's Forge — where divine tools are crafted | Execution phase: shaping raw ideas into shippable specs |
| **argus** | Argus Panoptes — the hundred-eyed guardian | Monitoring phase: watching every metric, every failure mode |
| **muse** | The Muses — source of creative knowledge and memory | Knowledge phase: transforming experience into reusable wisdom |

The naming follows two rules: (1) the metaphor must be instantly intuitive to anyone who looks it up, and (2) each name should be a single word that works as a CLI namespace (`oracle/skills/cost-sim`).

### 1. `oracle` — What agent to build?

6 skills: `opp-tree` · `assumptions` · `build-or-buy` · `hitl` · `cost-sim` · `agent-gtm`

Commands: `/discover` · `/validate`

### 2. `atlas` — How to architect it?

7 skills: `3-tier` · `orchestration` · `biz-model` · `router` · `memory-arch` · `moat` · `growth-loop`

Commands: `/architecture` · `/strategy-review`

### 3. `forge` — How to spec and ship it?

8 skills: `instruction` · `prd` · `prompt` · `ctx-budget` · `okr` · `stakeholder-map` · `agent-plan-review` · `gemini-image-flow`

Commands: `/write-prd` · `/set-okr` · `/sprint`

### 4. `argus` — How to measure and improve?

8 skills: `kpi` · `reliability` · `premortem` · `burn-rate` · `north-star` · `agent-ab-test` · `cohort` · `incident`

Commands: `/health-check` · `/cost-review`

### 5. `muse` ⭐ — Turn PM tacit knowledge into agent assets

3 skills: `pm-framework` · `pm-decision` · `pm-engine`

Commands: `/extract` · `/decide` · `/tk-to-instruction`

> This plugin has no equivalent in any PM skill marketplace. It grows stronger as the operator accumulates experience.

---

## Skill Origin

| Type | Count | Description |
|---|---|---|
| 🟢 Adapted | 3 | Classic PM frameworks (OST, FMEA), recontextualized for agents |
| 🟡 Extended | 6 | Standard PM concepts, heavily extended with agent-specific dimensions |
| 🔴 New | 23 | Agent-only domains — cost-sim, 3-tier, TK-NNN, moat, reliability, growth-loop, incident, cohort, agent-plan-review, gemini-image-flow, etc. |

**72% is original work** — covering agent economics, multi-agent orchestration, and tacit knowledge capture that no general PM skillset addresses.

---

## Installation

### Marketplace Install (Recommended)
```bash
claude plugin marketplace add kimsanguine/AI_PM_Skills
```
This installs all 5 plugins at once.

### Individual Plugin Install
```bash
claude plugin add oracle/    # Discovery
claude plugin add atlas/     # Architecture
claude plugin add forge/     # Execution
claude plugin add argus/     # Monitoring
claude plugin add muse/      # Knowledge
```

### Manual Install
```bash
# Copy skill directories
for plugin in oracle atlas forge argus muse; do
  cp -r "$plugin/skills/"* ~/.claude/skills/ 2>/dev/null
done
```

### Other AI Tools (Gemini CLI, Cursor, Codex CLI, Kiro)

| Tool | How to use | What works |
|------|-----------|------------|
| **Gemini CLI** | Copy skill folders to `.gemini/skills/` | Skills only |
| **Cursor** | Copy skill folders to `.cursor/skills/` | Skills only |
| **Codex CLI** | Copy skill folders to `.codex/skills/` | Skills only |
| **Kiro** | Copy skill folders to `.kiro/skills/` | Skills only |

```bash
# Example: copy all skills for Gemini CLI
for plugin in oracle atlas forge argus muse; do
  cp -r "$plugin/skills/"* ~/.gemini/skills/ 2>/dev/null
done
```

---

## Benchmark

We run a with-skill vs without-skill eval across 5 representative skills (1 per plugin) to measure what the skills actually add on top of base Claude.

| Metric | With Skill | Without Skill | Delta |
|--------|-----------|--------------|-------|
| **Pass Rate** | **100%** | 88% | **+12%** |
| **Avg Time** | 62.1s | 41.7s | +20.5s |

Key findings from the eval (10 tests, 54 assertions):

- **Capability-gating skills** — without the skill, Claude can't do it at all. `pm-framework` (TK unit structuring) drops to 40%, `3-tier` (Prometheus-Atlas-Worker architecture) drops to 60-80%.
- **Quality-amplifying skills** — both pass, but the skill produces deeper output. `cost-sim` adds context accumulation cost analysis (+46.6% output), `premortem` generates up to 2× more failure modes.
- **Baseline-strong skills** — `prd` and `premortem` pass at 100% either way, but with-skill output follows agent-specific templates rather than generic PM structures.

Full benchmark data: [`eval-workspace/iteration-1/benchmark.json`](eval-workspace/iteration-1/benchmark.json)

## Status

**v0.4** — All 5 plugins complete (32 skills, 12 commands)

| Plugin | Skills | Commands | Trigger Accuracy | Status |
|--------|--------|----------|-----------------|--------|
| oracle | 6 | 2 | 18/20 (90%) | ✅ Complete |
| atlas | 7 | 2 | 24/24 (100%) | ✅ Complete |
| forge | 8 | 3 | 20/20 (100%) | ✅ Complete |
| argus | 8 | 2 | 20/20 (100%) | ✅ Complete |
| muse | 3 | 3 | 12/12 (100%) | ✅ Complete |
| **Total** | **32** | **12** | **94/96 (97.9%)** | |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

New skill ideas, improvements to existing skills, and translations (EN↔KO) are all welcome.

---

## Author

**Sanguine Kim (이든)** — 20-year PM, AI Agent Builder
Building 100 Agents | Operating OpenClaw agent orchestration system

References & inspiration:
- Teresa Torres — *Continuous Discovery Habits* (OST origin)
- Anthropic — "Building Effective Agents" (multi-agent patterns)
- Steve Yegge — Gas Town parallel agent design principles
- Byeonghyeok Kwak — MCP-Skills hierarchy design principles
- Michael Polanyi — *The Tacit Dimension* (TK-NNN theoretical foundation)

---

## Related

| Repo | What | Link |
|------|------|------|
| **AI_PM** | Claude Code guide for PMs — Discovery → Definition → Delivery → Growth | [github.com/kimsanguine/AI_PM](https://github.com/kimsanguine/AI_PM) |
| **AI_PM_Skills** | Open-source agent skillset — 5 plugins, 32 skills, 12 commands *(this repo)* | [github.com/kimsanguine/AI_PM_Skills](https://github.com/kimsanguine/AI_PM_Skills) |

> **AI_PM** teaches *why and how*. **AI_PM_Skills** gives you *ready-to-use tools*.

---

## License

MIT — [LICENSE](LICENSE)
