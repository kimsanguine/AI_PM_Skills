# hplan — Product Build Gate Plugin

> Evidence + COGS + Decision gate that runs **BEFORE** you build.

While [`oracle`](../oracle/), [`atlas`](../atlas/), [`forge`](../forge/), [`argus`](../argus/), and [`muse`](../muse/) help you build, ship, and operate AI agents — **hplan decides whether the thing deserves to be built at all**.

The wedge: mandatory competitor research, user interview evidence, **executable** COGS sentinel, append-only Do-Not-Build exclusions registry, self-eval decision log, and multi-target handoff. None of which other spec-driven coding agents (Spec-Kit, Kiro, GStack, Superpowers) enforce.

## Lifecycle Position

```text
hplan  →  oracle  →  atlas  →  forge  →  argus  →  muse
(Gate)    (Discover)  (Architect)  (Build)  (Measure)  (Knowledge)
```

hplan is **Stage 0**. The other 5 plugins inherit decisions from hplan's gates.

## Skills

| Skill | Purpose | Gate |
|---|---|---|
| [`evidence-rubric`](./skills/evidence-rubric/) | Score an idea against the 100-point evidence rubric (ICP / Recent painful event / Workaround / Repetition / Economic pain / Switching trigger / MVP narrowness / Acquisition path) | Evidence |
| [`interview-synthesis`](./skills/interview-synthesis/) | Import AI synthesis output (BuildBetter / Perspective AI / Granola), force human strength + Push/Pull/Habit/Anxiety axes tagging, audit the 5-vs-3 repeated Push rule | Evidence |
| [`exclusions`](./skills/exclusions/) | Append-only "Do Not Build" registry with collision detector (Korean-aware char-bigram match). Each exclusion carries a reopen_trigger | cross-cutting |
| [`cogs-sentinel`](./skills/cogs-sentinel/) | Executable COGS gate — p50/p90 margin from lognormal token-cost sampling, free-user abuse blend, GREEN / CONDITIONAL_GO / RED decision | Build (blocker) |
| [`ost`](./skills/ost/) | Generate Teresa Torres-style Opportunity Solution Tree with Mermaid + outcome → opportunity → solution → experiment + decision_rule | Product |
| [`decision-log`](./skills/decision-log/) | Append-only build/interview/pivot/hold log + 3-6 month self-eval audit (hit_rate, false_holds, missed_builds) | cross-cutting |
| [`handoff`](./skills/handoff/) | Build Gate brief → Spec-Kit `specs/NNN-slug/`, Kiro `.kiro/specs/`, GStack `/office-hours` brief, Claude Code `AGENTS.md` + `CLAUDE.md` | Build (terminal) |

## Commands

| Command | Function |
|---|---|
| `/hplan-evidence <idea>` | Run Evidence Gate (rubric → interview synthesis → exclusions check) |
| `/hplan-product` | Run Product Gate (OST + journey + sitemap + design pointers) |
| `/hplan-build` | Run Build Gate (cogs-sentinel + decision-log + handoff) |
| `/hplan-cogs <provider> <model>` | Run COGS sentinel only |
| `/hplan-exclude <idea>` | Add or check an exclusion |
| `/hplan-handoff <target>` | Export Build Gate brief to spec-kit / kiro / gstack / claude / all |

## Cross-Cutting Assets

| Asset | Purpose |
|---|---|
| [`hplan_mcp/`](./hplan_mcp/) | MCP server exposing 6 tools so Cursor / Windsurf / Kiro / Codex / Goose can call hplan primitives |
| [`hooks/gate_guard.py`](./hooks/) | Claude Code PreToolUse hook that blocks writes to PRD.md / AGENTS.md / `specs/` / `.kiro/specs/` until `harness/build-gate/checkpoint.json` reports `status: "approved"` |
| [`agents/`](./agents/) | 4 role-locked reviewer agents: evidence / product / economics / build |
| [`references/`](./references/) | 14 playbooks (market research, ICP/interview, product planning, design gate, unit economics, performance benchmark, implementation readiness, project scaffold, HITL, competitive landscape, source integration notes, diagnosis rubric, metrics/launch, provider_pricing.json snapshot) |
| [`scripts/`](./scripts/) | 9 executable Python scripts backing each skill |

## Routing — When hplan paired with this marketplace's other plugins

| Other skill | hplan partner | Relationship |
|---|---|---|
| `oracle/cost-sim` (LLM scenario) | `hplan/cogs-sentinel` (deterministic) | cost-sim thinks → cogs-sentinel calculates |
| `oracle/opp-tree` (exploration) | `hplan/ost` (persistence) | opp-tree explores → ost validates + persists + Mermaid |
| `oracle/hitl` (agent runtime) | `hplan/hooks/gate_guard` (build time) | Different time horizons — runtime vs build-time HITL |
| `oracle/assumptions` (V/F/R/E) | `hplan/evidence-rubric` (100-pt) | Same intent, different axes — complement |
| `oracle/build-or-buy` (vendor) | `hplan/exclusions` (do-not-build) | Vendor decision vs permanent exclusion memory |
| `forge/prd` (agent PRD shape) | `hplan/handoff` (multi-target export) | forge canonicalizes shape, hplan exports across 4 ecosystems |
| `argus/burn-rate` (post-deploy) | `hplan/cogs-sentinel` (pre-deploy) | Sequential — predict → track |

## Install

This plugin is part of the [AI_PM_Skills marketplace](../README.md). Install the marketplace and `hplan` is included.

For standalone Claude Code skill install:

```bash
git clone https://github.com/kimsanguine/AI_PM_Skills.git ~/.claude/skills/AI_PM_Skills
# hplan plugin is at ~/.claude/skills/AI_PM_Skills/hplan/
```

For MCP usage (Cursor / Windsurf / Kiro / Codex):

```bash
pip install mcp
python3 hplan/hplan_mcp/server.py    # stdio MCP server
```

See [`hplan_mcp/README.md`](./hplan_mcp/README.md) for host registration.

## Operating Rules

1. Do not skip competitor or alternative research.
2. Do not skip user interviews unless strong behavior evidence already exists.
3. Do not treat compliments, waitlists, or "I would use this" as build-ready evidence.
4. Do not define persona by demographics only.
5. Do not write PRD seed or AGENTS.md brief before the Product Gate is credible.
6. Do not assume a paid AI product is viable before COGS, usage caps, and gross margin are calculated.
7. Do not claim realtime / instant / live value without latency budget and benchmark results.
8. Do not advance Evidence, Product, or Build Gate without a visible human checkpoint.

(Full 22 rules in [`SKILL.md`](./skills/evidence-rubric/SKILL.md) and `references/human-in-loop.md`.)

## Decision Vocabulary

| Decision | Meaning |
|---|---|
| `build` | Evidence + product plan + design + economics + readiness all credible |
| `interview` | Idea plausible, behavior evidence thin |
| `pivot` | Real problem, but ICP / wedge / workflow / pricing / COGS / UX breaks |
| `hold` | Differentiation, evidence, and economics too weak |
| `CONDITIONAL_GO` | Build allowed only on narrow blockers or prototype paths |
| `WAITING_FOR_HUMAN` | Approval missing — produce smallest decision needed |

## License

MIT — see [LICENSE](./LICENSE).
