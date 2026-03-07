---
name: orchestration
description: "Select and design the right orchestration pattern for multi-agent systems. Evaluate Sequential, Parallel, Router, and Hierarchical patterns against your use case requirements. Use when deciding how multiple agents should coordinate, share context, or delegate tasks to each other."
argument-hint: "[multi-agent scenario]"
---

# Orchestration Pattern

> 멀티 에이전트 오케스트레이션 패턴 선택 및 설계

## 개념

에이전트 시스템의 복잡도와 요구사항에 따라 적절한 오케스트레이션 패턴을 선택한다. 잘못된 패턴 선택은 불필요한 복잡성이나 성능 병목을 만든다.

## Instructions

You are selecting and designing an **orchestration pattern** for: **$ARGUMENTS**

### Step 1 — Assess Requirements

Answer these questions to determine pattern fit:
- How many distinct tasks are involved?
- Are tasks dependent on each other's outputs?
- Is the workflow deterministic or dynamic?
- What is the latency tolerance?
- What is the error tolerance?

### Step 2 — Pattern Selection Matrix

| Pattern | When to Use | Complexity | Latency |
|---------|------------|------------|---------|
| **Sequential Chain** | Tasks have strict dependencies | Low | High (sum of all) |
| **Parallel Fan-out** | Independent tasks, same input | Medium | Low (max of all) |
| **Router** | Input determines which agent | Medium | Low (single path) |
| **Hierarchical** | Complex, multi-level workflows | High | Variable |
| **Event-Driven** | Reactive, async workflows | High | Variable |

### Step 3 — Pattern Deep Dive

#### Sequential Chain
```
Input → Agent A → Agent B → Agent C → Output
```
- Best for: pipelines where each step transforms data
- Risk: single point of failure, high total latency
- PM Example: Research → Analysis → Report Draft → Review

#### Parallel Fan-out / Fan-in
```
         ┌→ Agent A ─┐
Input ───┤→ Agent B ──┤→ Aggregator → Output
         └→ Agent C ─┘
```
- Best for: same task on different data segments
- Risk: aggregation complexity, slowest worker bottleneck
- PM Example: Analyze 5 competitors simultaneously

#### Router (Classifier → Specialist)
```
Input → Router → Agent A (if type X)
              → Agent B (if type Y)
              → Agent C (if type Z)
```
- Best for: varied input types needing different expertise
- Risk: router misclassification
- PM Example: Triage user feedback by category

#### Hierarchical (Prometheus-Atlas)
```
Orchestrator → Sub-orchestrator A → Workers
             → Sub-orchestrator B → Workers
```
- Best for: complex, multi-phase projects
- Risk: over-engineering, communication overhead
- PM Example: Full product launch planning

### Step 4 — Design the Selected Pattern

For the chosen pattern, specify:
1. **Agent Roles**: What each agent does
2. **Data Flow**: Input/output format between agents
3. **Error Handling**: What happens when an agent fails
4. **Scaling Strategy**: How to handle increased load

### Step 5 — Complexity Check

Before finalizing, ask:
- Could a single well-prompted agent do this?
- Is the orchestration overhead justified by the benefit?
- What is the simplest pattern that meets requirements?

**Rule**: Start with the simplest pattern. Upgrade only when proven necessary.

---

## Further Reading
- Anthropic, "Building Effective Agents" (2024) — Workflow vs agent patterns
- LangGraph Documentation — Orchestration pattern implementations
