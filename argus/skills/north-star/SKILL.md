---
name: north-star
description: "Define the single North Star metric for an AI agent that aligns operational performance with business value. Use when launching a new agent product, realigning team focus, setting up metric hierarchies, or when multiple KPIs are creating conflicting priorities."
argument-hint: "[agent or product]"
---

# Agent North Star

> 에이전트의 단일 핵심 지표(North Star Metric) 정의

## 개념

North Star Metric은 에이전트의 성공을 하나의 숫자로 표현한다. 운영 건강도와 비즈니스 임팩트를 동시에 반영하는 복합 지표여야 하며, 팀 전체가 이 하나의 숫자를 중심으로 의사결정한다.

## Instructions

You are defining a **North Star Metric** for: **$ARGUMENTS**

### Step 1 — North Star Criteria

A good North Star Metric must be:
- [ ] **Actionable**: Team can influence it directly
- [ ] **Measurable**: Can be tracked automatically
- [ ] **Understandable**: Anyone can explain what it means
- [ ] **Leading**: Predicts future success, not just past
- [ ] **Composite**: Reflects both quality and impact

### Step 2 — Candidate Generation

Generate 3-5 candidates using this formula:
```
North Star = f(Quality, Volume, Impact)

Examples:
- "Successful agent actions per week" (volume × quality)
- "Hours saved per user per month" (impact × adoption)
- "Accurate outputs delivered within SLA" (quality × reliability)
- "Revenue-impacting decisions supported" (impact × quality)
```

### Step 3 — Evaluation Matrix

| Candidate | Actionable | Measurable | Understandable | Leading | Composite | Score |
|-----------|:----------:|:----------:|:--------------:|:-------:|:---------:|:-----:|
| | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ | /5 |

### Step 4 — Decomposition Tree

Break down the North Star into input metrics:
```
North Star: [metric]
├── Driver 1: [sub-metric]
│   ├── Lever: [what team controls]
│   └── Lever: [what team controls]
├── Driver 2: [sub-metric]
│   ├── Lever: [what team controls]
│   └── Lever: [what team controls]
└── Driver 3: [sub-metric]
    ├── Lever: [what team controls]
    └── Lever: [what team controls]
```

### Step 5 — Target Setting

```
North Star: [metric name]
Current value: ___
3-month target: ___
6-month target: ___
12-month target: ___

Growth model:
- Conservative: ___% growth/month
- Expected: ___% growth/month
- Ambitious: ___% growth/month
```

### Step 6 — Anti-Metrics

Define what NOT to optimize (guardrails):
```
Anti-metric 1: [metric that shouldn't degrade]
  └── Floor: [minimum acceptable value]
Anti-metric 2: [metric that shouldn't degrade]
  └── Floor: [minimum acceptable value]
```

Example: If North Star is "agent executions per week", anti-metric is "accuracy rate" (floor: 95%)

### Output

North Star Card:
```
┌─────────────────────────────────────────┐
│ 🌟 North Star: [metric name]            │
├─────────────────────────────────────────┤
│ Current: [value]  →  Target: [value]    │
│ Timeframe: [period]                      │
├── Drivers ──────────────────────────────┤
│ 1. [driver] — current: [val]            │
│ 2. [driver] — current: [val]            │
│ 3. [driver] — current: [val]            │
├── Guardrails ───────────────────────────┤
│ ⚠️ [anti-metric 1] must stay > [floor]  │
│ ⚠️ [anti-metric 2] must stay > [floor]  │
└─────────────────────────────────────────┘
```

---

## Further Reading
- Sean Ellis, *Hacking Growth* — North Star Metric framework
- Amplitude, "North Star Playbook" — Metric selection guide
