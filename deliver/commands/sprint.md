---
name: sprint
description: "Plan an agent development sprint using prototype-first methodology — build the smallest working version first, then iterate. Use when kicking off agent development, planning a 3-day prototype sprint, or structuring iterative agent delivery."
argument-hint: "[agent to prototype]"
---

# /sprint

> 에이전트 개발 스프린트 플래닝

## Instructions

You are planning an **Agent Development Sprint** for: **$ARGUMENTS**

### Day 1: Foundation
Use the **instruction** skill to define the core agent instruction.
- Minimal viable instruction (3 elements: Role, Goal, Output)
- Single happy path only
- Manual testing with 5 sample inputs

### Day 2: Hardening
Use the **prd** skill to formalize requirements.
- Add error handling and edge cases
- Implement context budget (use **ctx-budget** skill)
- Expand to 3-5 test scenarios

### Day 3: Optimization
Use the **prompt** skill for prompt refinement.
- Apply CRISP framework to optimize instructions
- Run cost simulation
- Document learnings and plan next sprint

## Output Format

Deliver a **Sprint Plan** with:
1. Sprint goal and success criteria
2. Day-by-day task breakdown
3. Test scenarios for each day
4. Definition of Done for the sprint
5. Backlog for next sprint
