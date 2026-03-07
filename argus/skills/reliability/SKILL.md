---
name: reliability
description: "Systematically review and improve AI agent reliability — identify failure patterns, assess error handling, design safeguards, and set reliability targets. Use when agents are producing inconsistent results, after incidents, or when preparing for production deployment."
argument-hint: "[agent to assess]"
---

# Reliability Review

> 에이전트 신뢰성 체계적 점검 및 개선

## 개념

에이전트 신뢰성은 "평균적으로 잘 되는가"가 아니라 "최악의 경우에도 허용 가능한가"로 측정한다. 99%의 성공률은 100번 중 1번 실패를 의미하고, 실패 1번의 비용이 99번의 가치를 초과할 수 있다.

## Instructions

You are conducting a **reliability review** for: **$ARGUMENTS**

### Step 1 — Reliability Baseline

Collect current data:
```
Total executions (last 30 days): ___
Successful: ___ (___%)
Failed: ___ (___%)
Partially correct: ___ (___%)
```

### Step 2 — Failure Taxonomy

Classify all failures:

| Category | Count | Severity | Example |
|----------|-------|----------|---------|
| **Input Error** | | Low-High | Malformed input, missing data |
| **Model Error** | | Medium | Hallucination, wrong format |
| **Tool Error** | | Medium | API timeout, rate limit |
| **Logic Error** | | High | Wrong decision, missed edge case |
| **Output Error** | | Medium | Correct answer, wrong format |

### Step 3 — Failure Pattern Analysis

For each failure category:
```
Pattern: [description]
Frequency: [how often]
Root Cause: [why it happens]
Impact: [what goes wrong for the user]
Detection: [how we know it failed]
Recovery: [what happens after failure]
```

### Step 4 — Safeguard Design

For each high-impact failure, design a safeguard:

| Safeguard Type | When to Use | Example |
|---------------|------------|---------|
| **Input Validation** | Predictable bad inputs | Schema validation before execution |
| **Output Validation** | Format/content requirements | JSON schema check, range validation |
| **Confidence Gate** | Uncertain outputs | If confidence < 0.8, escalate to human |
| **Retry with Backoff** | Transient failures | Retry 3x with exponential backoff |
| **Fallback Path** | Critical failures | Switch to simpler model or manual flow |
| **Circuit Breaker** | Cascading failures | Stop after N consecutive failures |

### Step 5 — Reliability Target Setting

| Level | Success Rate | Meaning | Appropriate For |
|-------|-------------|---------|-----------------|
| Basic | 90% | 1 in 10 fails | Internal tools, non-critical |
| Standard | 95% | 1 in 20 fails | Regular business ops |
| High | 99% | 1 in 100 fails | Customer-facing, financial |
| Critical | 99.9% | 1 in 1000 fails | Safety, compliance |

Current level: ___
Target level: ___

### Step 6 — Improvement Roadmap

Prioritize by: Impact × Frequency × Ease of Fix
```
Quick Wins (this week):
- [ ] [safeguard 1]
- [ ] [safeguard 2]

Medium Term (this month):
- [ ] [improvement 1]
- [ ] [improvement 2]

Long Term (this quarter):
- [ ] [architecture change]
```

### Output

Reliability report card:
```
Agent: [name]
Period: [date range]
Reliability: [current%] → Target: [target%]
Top Failure: [category] ([count] occurrences)
New Safeguards: [count] implemented
Next Review: [date]
```

---

## Further Reading
- Google SRE Book — Site Reliability Engineering principles
- Anthropic, "Building Effective Agents" (2024) — Error handling patterns
