---
name: discover
description: "End-to-end agent opportunity discovery — from problem space to validated agent idea with cost estimate. Use when exploring new agent opportunities, validating automation ideas, or running a full discovery workshop."
argument-hint: "[workflow or task to automate]"
---

# /discover

> 에이전트 기회 발굴 전체 워크플로우

## Instructions

You are running the **Agent Discovery** workflow for: **$ARGUMENTS**

Execute the following phases in sequence. Each phase builds on the previous.

### Phase 1: Opportunity Mapping (opp-tree)
Use the **opp-tree** skill to build an Agent Opportunity Solution Tree.
- Map the problem space into 4 layers: Outcome → Job → Pain → Agent Opportunity
- Identify the top 3 automation opportunities

### Phase 2: Assumption Analysis (assumptions)
Use the **assumptions** skill on the top opportunity from Phase 1.
- Run the 4-axis analysis: Value / Feasibility / Reliability / Ethics
- Prioritize assumptions by risk level

### 🔍 Checkpoint
Before proceeding to cost simulation, present the user with:
1. **Summary**: Top opportunity from Phase 1 + key risk assumptions from Phase 2
2. **Options**:
   - "Continue with cost simulation for [top opportunity]"
   - "Explore a different opportunity from the tree"
   - "Dive deeper into assumption analysis first"

Wait for user confirmation before continuing to Phase 3.

### Phase 3: Cost Simulation (cost-sim)
Use the **cost-sim** skill to estimate the cost of the top opportunity.
- Model token usage per interaction
- Calculate monthly/annual run cost
- Compare with current manual process cost

### Phase 4: Build vs Buy Decision (build-or-buy)
Use the **build-or-buy** skill to make the final recommendation.
- Evaluate Custom Build / Buy SaaS / No-Code options
- Score each option across 5 dimensions
- Provide a clear recommendation with rationale

## Output Format

Deliver a **Discovery Report** with:
1. Opportunity landscape (from Phase 1)
2. Top opportunity deep dive with validated assumptions
3. Cost projection
4. Build/Buy/No-Code recommendation
5. Recommended next steps
