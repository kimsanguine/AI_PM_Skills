---
name: kpi
description: "Define and track Key Performance Indicators for AI agents — operational metrics (latency, success rate, error rate) and business metrics (task completion, user satisfaction, cost per task). Use when setting up agent monitoring dashboards, defining SLAs, or establishing performance baselines."
argument-hint: "[agent to define KPIs for]"
---

# Agent KPI

> AI 에이전트의 핵심 성과 지표(KPI) 정의 및 추적

## 개념

에이전트 KPI는 두 축으로 나뉜다: **운영 건강도**(잘 돌아가는가)와 **비즈니스 임팩트**(가치를 만드는가). 둘 다 측정하지 않으면 "잘 돌아가지만 쓸모없는" 또는 "가치있지만 불안정한" 에이전트가 된다.

## Instructions

You are defining **KPIs** for: **$ARGUMENTS**

### Step 1 — Operational Health Metrics

These measure "Is the agent working correctly?"

| Metric | Formula | Target | Alert Threshold |
|--------|---------|--------|-----------------|
| **Accuracy** | Correct outputs ÷ Total executions | >95% | <90% |
| **Reliability** | Successful runs ÷ Total runs | >99% | <95% |
| **Latency** | Average execution time | <Xs | >2Xs |
| **Cost per Execution** | Total cost ÷ Executions | <$X | >1.5×$X |
| **Error Rate** | Failed runs ÷ Total runs | <1% | >5% |

### Step 2 — Business Impact Metrics

These measure "Is the agent creating value?"

| Metric | Formula | Target |
|--------|---------|--------|
| **Time Saved** | Manual time - Agent time per task | >X hrs/week |
| **Cost Saved** | Manual cost - Agent cost | >$X/month |
| **Throughput Increase** | Tasks completed with agent ÷ without | >Xx |
| **Error Prevention** | Errors caught by agent ÷ Total errors | >X% |
| **User Satisfaction** | NPS or CSAT score from agent users | >X |

### Step 3 — KPI Dashboard Design

For each KPI, define:
```
KPI: [name]
├── Definition: [precise formula]
├── Data Source: [where the data comes from]
├── Collection Method: [automated/manual]
├── Frequency: [real-time/daily/weekly]
├── Owner: [who monitors this]
├── Baseline: [current value]
├── Target: [goal value]
└── Alert: [threshold that triggers review]
```

### Step 4 — Leading vs Lagging Indicators

Separate early warning signals from outcomes:
```
Leading (predict future performance):
- Input data quality score
- Prompt version performance delta
- User engagement frequency

Lagging (confirm past performance):
- Monthly cost savings
- Quarterly business impact
- User retention rate
```

### Step 5 — Review Cadence

| Cadence | What to Review | Action |
|---------|---------------|--------|
| Daily | Error rate, latency spikes | Immediate fix |
| Weekly | Accuracy trends, cost tracking | Optimization |
| Monthly | Business impact KRs | Strategy adjustment |
| Quarterly | North Star metric, OKR review | Goal revision |

### Output

Present KPI card:
```
┌─────────────────────────────────────┐
│ Agent: [name]                        │
├── Operational Health ────────────────┤
│ Accuracy:     [current] → [target]  │
│ Reliability:  [current] → [target]  │
│ Latency:      [current] → [target]  │
│ CPE:          [current] → [target]  │
├── Business Impact ───────────────────┤
│ Time Saved:   [current] → [target]  │
│ Cost Saved:   [current] → [target]  │
│ Throughput:   [current] → [target]  │
└─────────────────────────────────────┘
```

---

## Further Reading
- Alistair Croll & Benjamin Yoskovitz, *Lean Analytics* — Metric design
- Cagan & Jones, *INSPIRED* / *EMPOWERED* — Product metrics
