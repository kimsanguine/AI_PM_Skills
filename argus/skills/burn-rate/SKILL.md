---
name: burn-rate
description: "Track, analyze, and optimize token costs for AI agent operations. Break down costs by model, task type, and user segment. Use when reviewing monthly agent spending, planning cost reduction, comparing model economics, or setting token budgets for new agents."
argument-hint: "[agent to track costs for]"
---

# Token Cost Tracking

> 에이전트 토큰 비용 추적, 분석, 최적화

## 개념

에이전트 비용의 60-90%는 LLM 토큰 비용이다. 토큰 사용을 가시화하고 최적화하지 않으면 비용이 사용량에 비례해 선형 증가하며, 이는 비즈니스 모델을 파괴할 수 있다.

## Instructions

You are setting up **token cost tracking** for: **$ARGUMENTS**

### Step 1 — Cost Baseline

Map current token usage:
```
Agent: [name]
Period: [last 30 days]

Per Execution:
├── Input tokens (avg): ___
├── Output tokens (avg): ___
├── Total tokens (avg): ___
├── Model: [name]
├── Price: $___/1K input, $___/1K output
└── Cost per execution: $___

Monthly:
├── Total executions: ___
├── Total tokens: ___
├── Total cost: $___
└── Cost per user: $___
```

### Step 2 — Cost Breakdown by Component

| Component | Tokens/exec | % of Total | Cost/exec | Optimizable? |
|-----------|------------|------------|-----------|-------------|
| System prompt | | | | Compression |
| Memory injection | | | | Retrieval tuning |
| User input | | | | Summarization |
| Tool calls | | | | Caching |
| Output generation | | | | Length control |

### Step 3 — Optimization Strategies

| Strategy | Effort | Savings | Risk |
|----------|--------|---------|------|
| **Prompt compression** | Low | 10-30% | Quality drop |
| **Response caching** | Medium | 20-50% | Stale results |
| **Model downgrade** (router) | Medium | 40-70% | Quality drop |
| **Batch processing** | Medium | 10-20% | Latency increase |
| **Context pruning** | Low | 15-25% | Missing context |
| **Output length limits** | Low | 10-20% | Truncated info |

### Step 4 — Budget Framework

```
Monthly Budget: $___

Allocation:
├── Core operations: ___% ($___) 
│   └── Alert at: ___% of allocation
├── Experimentation: ___% ($___) 
│   └── Hard cap, no overage
├── Spike buffer: ___% ($___) 
│   └── Auto-scale threshold
└── Reserve: ___% ($___) 
    └── Emergency use only

Daily burn rate target: $___
Daily burn rate alert: >$___
```

### Step 5 — Cost Monitoring Dashboard

Track these metrics:
```
Real-time:
- Current daily spend vs budget
- Cost per execution (rolling average)
- Token count per component

Weekly:
- Cost trend (week-over-week)
- Top 5 expensive operations
- Optimization opportunity score

Monthly:
- Total cost vs budget
- Cost per user trend
- ROI (value created ÷ cost)
```

### Step 6 — Cost Anomaly Detection

Define alerts:
```
⚠️ Warning:
- Daily cost > 1.5× average
- Single execution > 3× average cost
- New model pricing change detected

🔴 Critical:
- Daily cost > 2× average
- Monthly projection exceeds budget by 20%
- Cost per execution trending up for 5+ days
```

### Output

Cost tracking setup:
```
Agent: [name]
Monthly Budget: $___
Current CPE: $___
Target CPE: $___ (after optimization)
Top Optimization: [strategy] — projected ___% savings
Monitoring: [tool/method]
Alert Owner: [who gets notified]
```

---

## Further Reading
- Anthropic API Pricing — https://docs.anthropic.com/en/docs/about-claude/models
- Token optimization strategies — Caching, batching, model routing
