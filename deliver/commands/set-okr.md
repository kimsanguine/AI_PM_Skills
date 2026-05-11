---
name: set-okr
description: "Design OKRs for an AI agent with the 2-axis framework: Business Impact + Operational Health. Use when setting agent performance goals, defining success metrics, or planning quarterly agent objectives."
argument-hint: "[agent name]"
---

# /set-okr

> 에이전트 OKR 설계

## Instructions

You are designing **Agent OKRs** for: **$ARGUMENTS**

### Phase 1: North Star Alignment
- Identify how this agent contributes to the product's North Star metric
- Define the agent's primary value proposition

### Phase 2: 2-Axis OKR Design (okr)
Use the **okr** skill.
- **Axis 1 — Business Impact**: Revenue, engagement, conversion, time-saved
- **Axis 2 — Operational Health**: Reliability, cost efficiency, user satisfaction
- Write 2-3 Objectives with 3-4 Key Results each

### Phase 3: Measurement Plan
- Define data sources for each Key Result
- Set baseline values and targets
- Plan review cadence (weekly metrics, monthly review)

## Output Format

Deliver an **Agent OKR Document** with:
1. North Star alignment statement
2. OKR table (Objectives → Key Results → Baseline → Target)
3. Measurement plan with data sources
4. Review schedule
