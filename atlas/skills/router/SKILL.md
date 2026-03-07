---
name: router
description: "Design a model routing strategy that selects the right LLM for each task type. Balance cost, latency, and quality tradeoffs across models. Use when building agents that call multiple LLMs, optimizing token costs by routing simple tasks to cheaper models, or designing fallback chains."
argument-hint: "[agent system for routing]"
---

# Model Router

> 작업별 최적 LLM 선택 전략 설계

## 개념

모든 작업에 최고 성능 모델을 사용하는 것은 비용 낭비다. 작업 복잡도에 따라 적절한 모델을 라우팅하면 비용을 50-80% 절감하면서 품질을 유지할 수 있다.

## Instructions

You are designing a **model routing strategy** for: **$ARGUMENTS**

### Step 1 — Task Classification

Classify each agent task by complexity:

| Tier | Complexity | Examples | Recommended Model Class |
|------|-----------|----------|----------------------|
| T1 | Simple extraction | Data parsing, formatting, classification | Small/Fast (Haiku, GPT-4o-mini) |
| T2 | Standard reasoning | Summarization, comparison, basic analysis | Mid (Sonnet, GPT-4o) |
| T3 | Complex reasoning | Strategy, creative, multi-step analysis | Large (Opus, o1) |
| T4 | Specialized | Code generation, math, domain-specific | Specialist (Claude Code, Codex) |

### Step 2 — Routing Decision Matrix

For each task in your agent workflow:
```
Task: [name]
├── Input complexity: Low / Medium / High
├── Output quality sensitivity: Low / Medium / High
├── Latency requirement: <1s / <5s / <30s / Flexible
├── Cost tolerance: $ / $$ / $$$
└── Recommended tier: T1 / T2 / T3 / T4
```

### Step 3 — Cost Comparison

Calculate cost impact of routing vs single-model:

| Approach | Monthly Cost | Quality Score |
|----------|-------------|---------------|
| All T3 (premium) | $____ | 95/100 |
| Routed (mixed) | $____ | 92/100 |
| All T1 (budget) | $____ | 70/100 |

**Target**: Routed approach should achieve >90% quality at <40% of premium cost

### Step 4 — Fallback Strategy

Design graceful degradation:
```
Primary: [preferred model]
  ↓ if failed/timeout
Fallback 1: [alternative model]
  ↓ if failed/timeout
Fallback 2: [minimum viable model]
  ↓ if all fail
Error: [return structured error to user]
```

### Step 5 — Quality Gate

For critical tasks, add a quality verification step:
- Run T1 model first for speed
- Check output confidence/quality score
- If below threshold → re-run with T2 or T3
- Log upgrade frequency to optimize routing rules

### Step 6 — Monitoring Plan

Track these metrics weekly:
- Cost per model tier
- Routing accuracy (was the right tier selected?)
- Fallback trigger frequency
- Quality score by tier

### Output

Present the routing table:
```
┌─────────────┬──────┬──────────┬───────┐
│ Task         │ Tier │ Model    │ $/run │
├─────────────┼──────┼──────────┼───────┤
│ [task 1]    │ T1   │ [model]  │ $0.01 │
│ [task 2]    │ T2   │ [model]  │ $0.05 │
│ [task 3]    │ T3   │ [model]  │ $0.15 │
└─────────────┴──────┴──────────┴───────┘
Monthly estimate: $____
vs all-premium: $____ (___% savings)
```

---

## Further Reading
- Anthropic Model Comparison — https://docs.anthropic.com/en/docs/about-claude/models
- OpenAI Model Overview — Model selection for different tasks
