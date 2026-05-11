---
name: write-prd
description: "Write a complete Agent PRD — chains instruction design, tools/memory planning, and failure handling into a formal 7-section document. Use when speccing out a new agent, documenting agent requirements, or preparing agent development handoff."
argument-hint: "[agent name or idea]"
---

# /write-prd

> 에이전트 전용 PRD 작성 워크플로우

## Instructions

You are writing an **Agent PRD** for: **$ARGUMENTS**

### Phase 1: Instruction Design (instruction)
Use the **instruction** skill.
- Define the 7 elements: Role, Goal, Constraints, Tools, Memory, Output, Fallback
- Draft the core instruction structure

### Phase 2: Prompt Engineering (prompt)
Use the **prompt** skill with CRISP framework.
- Refine instructions using Context/Role/Instruction/Scope/Parameters
- Optimize for clarity and consistency

### 🔍 Checkpoint
Before proceeding to context budgeting, present the user with:
1. **Summary**: Draft instruction set + refined prompts from Phases 1-2
2. **Options**:
   - "Continue with context budget and full PRD assembly"
   - "Refine the instruction design further"
   - "Add more tool/integration requirements first"

Wait for user confirmation before continuing to Phase 3.

### Phase 3: Context Budget (ctx-budget)
Use the **ctx-budget** skill.
- Calculate token allocation: System prompt / User input / Tools / Memory / Output
- Identify budget constraints and tradeoffs

### Phase 4: PRD Assembly (prd)
Use the **prd** skill to assemble the final document.
- Compile all phases into the 7-section PRD template
- Add success criteria and failure modes
- Include testing strategy

## Output Format

Deliver a complete **Agent PRD** with 7 sections:
1. Overview & Problem Statement
2. Agent Persona & Instruction Set
3. Tools & Integrations
4. Memory & Context Design
5. Failure Modes & Fallbacks
6. Success Criteria & OKRs
7. Development & Testing Plan
