---
name: validate
description: "Focused assumption analysis — identify, prioritize, and design validation experiments for the riskiest assumptions in an agent idea. Use when you need to stress-test an agent concept before investing in development."
argument-hint: "[agent idea to stress-test]"
---

# /validate

> 에이전트 아이디어의 핵심 가정 검증

## Instructions

You are running **Agent Assumption Analysis** for: **$ARGUMENTS**

### Phase 1: Assumption Extraction (assumptions)
Use the **assumptions** skill.
- Extract ALL implicit assumptions from the agent idea
- Categorize across 4 axes: Value / Feasibility / Reliability / Ethics
- Score each assumption: Confidence (1-5) × Impact (1-5)

### Phase 2: HITL Boundary Design (hitl)
Use the **hitl** skill for the top 3 riskiest assumptions.
- Design the human-in-the-loop boundary for each risky area
- Define automation level (Full Auto / Human Review / Human Approve / Manual)
- Map escalation triggers

## Output Format

Deliver an **Assumption Validation Plan** with:
1. Assumption map (all assumptions categorized and scored)
2. Top 3 risk areas with HITL design
3. Validation experiment design for each risk
4. Go/No-Go criteria
