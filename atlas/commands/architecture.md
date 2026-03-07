---
name: architecture
description: "Design the full technical architecture for a multi-agent system — pattern selection, orchestration, memory, and model routing. Use when planning how agents work together, selecting orchestration patterns, or designing system architecture."
argument-hint: "[system or workflow to design]"
---

# /architecture

> 에이전트 시스템 아키텍처 종합 설계

## Instructions

You are designing **Agent System Architecture** for: **$ARGUMENTS**

### Phase 1: Orchestration Pattern (orchestration)
Use the **orchestration** skill.
- Evaluate 4 patterns: Sequential / Parallel / Router / Hierarchical
- Score each pattern against the use case requirements
- Select the optimal pattern with rationale

### Phase 2: 3-Tier Design (3-tier)
Use the **3-tier** skill to design the Prometheus-Atlas-Worker structure.
- Prometheus: Strategic planning layer
- Atlas: Tactical coordination layer
- Worker: Execution layer
- Define responsibilities and communication protocols

### 🔍 Checkpoint
Before proceeding to memory architecture, present the user with:
1. **Summary**: Selected orchestration pattern + 3-tier role definitions
2. **Options**:
   - "Continue with memory and routing design"
   - "Revisit the orchestration pattern choice"
   - "Simplify to single-agent before adding complexity"

Wait for user confirmation before continuing to Phase 3.

### Phase 3: Memory Architecture (memory-arch)
Use the **memory-arch** skill.
- Design the memory system: Working / Episodic / Semantic / Procedural
- Define persistence strategy and retrieval patterns
- Plan context window management

### Phase 4: Model Routing (router)
Use the **router** skill.
- Map task types to appropriate models
- Define routing rules (cost/quality/speed tradeoffs)
- Design fallback chains

## Output Format

Deliver an **Architecture Document** with:
1. System overview diagram (text-based)
2. Orchestration pattern selection with rationale
3. 3-tier role definitions
4. Memory system design
5. Model routing matrix
6. Estimated token budget per interaction
