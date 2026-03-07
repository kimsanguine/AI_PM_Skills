---
name: moat
description: "Analyze and design competitive moats for AI agent products — data flywheel, workflow lock-in, network effects, and switching costs. Use when evaluating competitive positioning, planning long-term defensibility, or identifying what makes your agent product hard to replicate."
argument-hint: "[agent product to analyze]"
---

# Agent Moat

> AI 에이전트 제품의 경쟁 우위(Moat) 분석 및 설계

## 개념

AI 에이전트 시장에서 모델 성능은 commodity화되고 있다. 지속 가능한 경쟁 우위는 모델 바깥에서 만들어진다 — 데이터, 워크플로우, 네트워크에서.

## Instructions

You are analyzing and designing **competitive moats** for: **$ARGUMENTS**

### Step 1 — Moat Type Assessment

Evaluate each moat type (1-5 score):

| Moat Type | Description | Your Score | Evidence |
|-----------|-------------|------------|----------|
| **Data Flywheel** | Usage → better data → better product → more usage | /5 | |
| **Workflow Lock-in** | Deep integration into user's daily process | /5 | |
| **Network Effects** | More users = more value for each user | /5 | |
| **Switching Cost** | Pain of moving to competitor | /5 | |
| **Proprietary Knowledge** | Unique domain expertise encoded | /5 | |
| **Speed/UX Moat** | 10x better experience than alternatives | /5 | |

### Step 2 — Data Flywheel Design

The most powerful moat for agent products:
```
Data Flywheel Blueprint:
1. Collect: What data do you uniquely capture through usage?
2. Aggregate: How does combined data create new value?
3. Learn: How does the agent improve from this data?
4. Deliver: How do users experience the improvement?
5. Retain: Why does this make users stay?
```

Key questions:
- What data is generated that competitors cannot access?
- How many executions until the flywheel produces visible improvement?
- Is the improvement per-user or across-all-users?

### Step 3 — Workflow Integration Depth

Rate integration depth (deeper = stronger moat):
```
Level 1: Tool (용tool) — Agent does a task when asked
Level 2: Assistant — Agent proactively suggests actions
Level 3: Workflow — Agent is embedded in daily process
Level 4: System — Agent manages end-to-end process
Level 5: Infrastructure — Removing agent breaks the workflow
```

Current level: ___
Target level: ___
Path to target: ___

### Step 4 — Moat Vulnerability Analysis

For each moat you're building:
```
Moat: [name]
├── Strength today: [1-5]
├── Time to build: [months]
├── Can competitor copy it? [Yes/No/Partially]
│   └── Time for competitor to copy: [months]
├── Depends on: [what must be true]
└── Biggest threat: [what could destroy this moat]
```

### Step 5 — Moat Building Roadmap

Prioritize moat investments:
```
Phase 1 (0-3 months): [Quick wins — usually UX/Speed moat]
Phase 2 (3-6 months): [Workflow integration — lock-in]
Phase 3 (6-12 months): [Data flywheel — compound advantage]
Phase 4 (12+ months): [Network effects — if applicable]
```

### Step 6 — Anti-Moat Patterns

Avoid these false moats:
| False Moat | Why It Fails |
|-----------|-------------|
| "We use GPT-4/Claude" | Everyone can use the same models |
| "Our prompts are secret" | Prompts are easily reverse-engineered |
| "We were first" | First-mover advantage is weak in AI |
| "Our UI is better" | UI is the easiest thing to copy |

### Output

Present moat strategy:
```
Primary Moat: [type] — [description]
Secondary Moat: [type] — [description]
Current Strength: [1-5] / Target: [1-5]
Key Investment: [what to build]
Timeline: [when moat becomes defensible]
Risk: [biggest threat to moat]
```

---

## Further Reading
- Hamilton Helmer, *7 Powers* — Strategic power and competitive advantage
- Jerry Chen, "The New Moats" — AI-era defensibility
