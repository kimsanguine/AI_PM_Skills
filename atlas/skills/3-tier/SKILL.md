---
name: 3-tier
description: "Design multi-agent systems using the Prometheus-Atlas-Worker 3-tier orchestration pattern. Use when building complex agent systems that need strategic planning, tactical coordination, and task execution layers. Covers role definition, communication protocols, and delegation strategies."
argument-hint: "[system to design]"
---

# Prometheus-Atlas Pattern

> 복잡한 PM 워크플로우를 위한 3-tier 에이전트 오케스트레이션 패턴

## 개념

Prometheus(전략) → Atlas(조율) → Workers(실행)의 3계층 구조로 복잡한 에이전트 시스템을 설계한다.

- **Prometheus**: 목표 설정, 전략 결정, 전체 방향 조율 (인간 또는 상위 에이전트)
- **Atlas**: 작업 분해, Worker 할당, 결과 통합, 품질 관리
- **Workers**: 단일 작업 실행, 도구 사용, 결과 반환

## Instructions

You are designing a **multi-agent system** using the Prometheus-Atlas Pattern for: **$ARGUMENTS**

### Step 1 — Identify the Tier Structure

Map your workflow to the 3 tiers:

| Tier | Role | Decision Type | Example |
|------|------|---------------|---------|
| Prometheus | Strategic direction | What & Why | "We need competitive analysis for Q2 planning" |
| Atlas | Task orchestration | How & When | "Split into 5 competitors, assign research workers, merge results" |
| Workers | Task execution | Do | "Research competitor X pricing page, extract data" |

### Step 2 — Define Communication Protocol

For each tier boundary, specify:
- **Prometheus → Atlas**: Goal format (objective + constraints + deadline)
- **Atlas → Workers**: Task format (input + expected output + tools allowed)
- **Workers → Atlas**: Result format (output + confidence + errors)
- **Atlas → Prometheus**: Summary format (aggregated results + recommendations)

### Step 3 — Design the Atlas Layer

The Atlas is the critical orchestration layer:
```
Atlas Responsibilities:
1. Task Decomposition — break goal into worker-sized tasks
2. Worker Selection — match task to best worker type
3. Dependency Management — order tasks correctly
4. Result Aggregation — merge worker outputs
5. Quality Gate — validate before passing up
6. Error Recovery — retry or escalate failures
```

### Step 4 — Worker Design Principles

Each Worker should follow:
- **Single Responsibility**: One task type per worker
- **Stateless Execution**: No dependency on other workers' state
- **Structured Output**: Consistent format for Atlas to parse
- **Graceful Failure**: Return error info, never crash silently

### Step 5 — Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| God Atlas | Atlas does execution work | Split into Atlas + Workers |
| Worker Chaining | Workers call other workers | Route through Atlas |
| Missing Prometheus | No human oversight | Always have strategic tier |
| Over-orchestration | Simple task uses 3 tiers | Use single agent for simple tasks |

### Step 6 — Output Architecture Diagram

Present the system design:
```
[Prometheus] Human/Strategic Agent
    ↓ Goal + Constraints
[Atlas] Orchestrator Agent
    ↓ Tasks          ↑ Results
[Worker A] [Worker B] [Worker C]
```

Include: tier responsibilities, communication formats, error handling strategy

---

## Further Reading
- Anthropic, "Building Effective Agents" (2024) — Multi-agent orchestration patterns
- Steve Yegge, "Gas Town" — Parallel agent design principles
