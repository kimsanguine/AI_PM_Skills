---
name: premortem
description: "Pre-mortem failure analysis for AI agents using FMEA methodology — identify how an agent can fail before it does, assess severity and likelihood, and design prevention strategies. Use before launching a new agent, after a near-miss incident, or when reviewing agent risk profiles."
argument-hint: "[agent to analyze risks for]"
---

# Failure Mode Analysis

> 에이전트 사전 실패 분석 — 실패하기 전에 실패 모드를 식별하고 예방

## 개념

Pre-mortem: "이 에이전트가 3개월 후 완전히 실패했다고 가정하자. 왜 실패했을까?" 이 질문으로 시작하면 사후 대응이 아닌 사전 예방이 가능하다.

## Instructions

You are conducting a **failure mode analysis** for: **$ARGUMENTS**

### Step 1 — Pre-mortem Exercise

Imagine it's 3 months from now. The agent has completely failed.
List all possible reasons:

```
"The agent failed because..."
1. ___
2. ___
3. ___
4. ___
5. ___
```

### Step 2 — FMEA Table (Failure Mode and Effects Analysis)

| Failure Mode | Cause | Effect | Severity (1-10) | Probability (1-10) | Detection (1-10) | RPN |
|-------------|-------|--------|-----------------|--------------------|--------------------|-----|
| | | | | | | |

**RPN** (Risk Priority Number) = Severity × Probability × Detection
- Detection: 1 = easily detected, 10 = undetectable
- Focus on RPN > 100 first

### Step 3 — AI-Specific Failure Modes

Check each category:

**Model Failures**
- [ ] Hallucination in critical outputs
- [ ] Inconsistent outputs for same input
- [ ] Performance degradation after model update
- [ ] Context window overflow losing critical info
- [ ] Prompt injection vulnerability

**Data Failures**
- [ ] Input data format changes (upstream API changes)
- [ ] Missing or null data handling
- [ ] Data drift (input distribution changes over time)
- [ ] PII leakage in outputs

**Integration Failures**
- [ ] API rate limits hit during peak usage
- [ ] External service downtime
- [ ] Authentication token expiration
- [ ] Version mismatch between components

**Business Failures**
- [ ] Cost exceeds budget (token cost explosion)
- [ ] Users stop using it (low adoption)
- [ ] Output doesn't match business need (misaligned objectives)
- [ ] Regulatory/compliance violation

### Step 4 — Prevention Strategy

For each high-RPN failure mode:
```
Failure Mode: [name]
├── Prevention: [how to stop it from happening]
├── Detection: [how to know it happened]
├── Response: [what to do when it happens]
└── Recovery: [how to get back to normal]
```

### Step 5 — Monitoring Triggers

Design early warning alerts:
```
⚠️ Yellow Alert (investigate):
- [metric] drops below [threshold]
- [error type] exceeds [N] per [period]

🔴 Red Alert (immediate action):
- [critical metric] breaches [threshold]
- [cascading failure pattern] detected
```

### Output

Failure Mode Summary:
```
Agent: [name]
Analysis Date: [date]
Total Failure Modes Identified: [N]
Critical (RPN > 200): [N]
High (RPN 100-200): [N]
Mitigated: [N] / [Total]
Top Risk: [failure mode] (RPN: [score])
Next Review: [date]
```

---

## Further Reading
- Gary Klein, "Performing a Project Premortem" — HBR, 2007 (프리모템 원전)
- IEC 60812 — FMEA standard methodology (산업 표준 실패 분석)
- Anthropic, "Building Effective Agents" (2024) — Agent error handling & recovery patterns
- Google, "People + AI Guidebook" — AI failure modes and human-AI interaction design
- NIST AI Risk Management Framework (AI RMF 1.0) — https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence
