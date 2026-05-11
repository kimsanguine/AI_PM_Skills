---
name: 3-tier
description: "Design multi-agent systems using the Prometheus-Atlas-Worker 3-tier orchestration pattern. Use when building complex agent systems that need strategic planning, tactical coordination, and task execution layers. Covers role definition, communication protocols, and delegation strategies."
argument-hint: "[system to design]"
allowed-tools: ["Read", "Write"]
model: sonnet
---

# Prometheus-Atlas Pattern

> 복잡한 PM 워크플로우를 위한 3-tier 에이전트 오케스트레이션 패턴

## Core Goal

- 전략 계층(Prometheus)과 실행 계층(Workers) 사이의 조율 레이어(Atlas)를 설계하여 복잡한 멀티 에이전트 시스템의 일관성과 효율성을 보장
- 3계층 간 명확한 통신 프로토콜을 정의하여 목표 달성, 작업 분해, 결과 통합 과정을 체계화
- 각 계층의 책임을 분리하여 스케일 가능하고 유지보수 가능한 에이전트 아키텍처 구축

## Trigger Gate

### Use This Skill When

- 3개 이상의 에이전트가 협력해야 하는 복잡한 시스템을 설계하는 경우
- 전략적 목표(Prometheus)와 실행(Workers) 사이의 조율이 필요한 워크플로우
- 에이전트 간 데이터 흐름, 에러 처리, 품질 관리를 체계적으로 정의해야 하는 상황

### Route to Other Skills When

- 2개 이하의 에이전트로 충분한 경우 → orchestration (패턴 선택)
- 에이전트 간 라우팅만 필요한 경우 → router (모델 선택 또는 작업 분류)
- 이미 정의된 오케스트레이션 패턴의 세부 구현 → moat, growth-loop (설계 강화)

### Boundary Checks

- 단순 시뀀셜 파이프라인은 3-tier 구조가 오버엔지니어링일 수 있음 → orchestration으로 먼저 검토
- Prometheus 계층이 없다면 (전략적 의사결정 없이 Workers만 작동) → 자동화 시스템이지, 의도적 설계가 아님
- Atlas의 책임이 너무 많으면 → 서브 오케스트레이터로 분리 검토

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

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---------|-----|-----|
| Worker가 지정된 시간 내 응답 없음 | 타임아웃 초과 | Atlas가 자동으로 재시도 또는 대체 Worker로 전환, Prometheus에 지연 보고 |
| Worker의 출력 형식이 예상과 다름 | 결과 파싱 실패 또는 유효성 검사 오류 | Atlas가 Worker에 재요청하거나, 예비 Worker 호출, 마지막 수단으로 Prometheus에 수동 개입 요청 |
| Prometheus가 모순된 목표 전달 | Atlas가 목표 분석 시 충돌 감지 | Atlas가 명확화 요청을 Prometheus로 보내고, 재정의된 목표 대기, 그 사이 이전 단계까지만 진행 |
| 최종 결과가 Prometheus 기준 미달 | 품질 게이트 검사 실패 | Atlas가 재작업 사이클 시작, 최대 N회 반복 후 실패 보고 및 원인 분석 |

## Quality Gate

- [ ] Prometheus → Atlas 목표 명세에 제약(constraints)과 마감(deadline) 포함 여부 (Yes/No)
- [ ] Atlas → Workers 작업 지시에 기대 출력 형식 명시 여부 (Yes/No)
- [ ] Workers → Atlas 결과 반환에 신뢰도(confidence) 또는 에러 정보 포함 여부 (Yes/No)
- [ ] Atlas 품질 게이트: 최종 결과가 Prometheus 목표 기준 충족 확인 (N/N 체크리스트)
- [ ] 에러 복구 전략 정의 여부: 재시도, 폴백, 수동 개입 경로 명시 (Yes/No)

## Examples

### Good Example

```
시나리오: Q2 경쟁사 분석 리포트 작성

[Prometheus] 전략팀
  목표: "주요 5개 경쟁사의 가격책정, 기능, GTM 전략 비교 분석"
  제약: "각 경쟁사당 3시간 조사 시간 할당"
  마감: "2026-03-14"
         ↓
[Atlas] 조율 에이전트
  분해:
    - Task 1: Competitor A, B, C 가격 페이지 스크래핑 (병렬)
    - Task 2: 각 경쟁사 기능 매트릭스 작성 (순차)
    - Task 3: GTM 패턴 분석 (병렬)
    - Task 4: 결과 통합 및 리포트 작성
  재시도: 스크래핑 실패 시 최대 2회
  품질 검사: 각 섹션이 5개 경쟁사 모두 포함 확인
         ↓
[Workers]
  - Scraper Worker: 웹 데이터 추출
  - Analysis Worker: 패턴 인식
  - Report Worker: 마크다운 작성

결과: 구조화된 리포트 + 신뢰도 점수 + 미수집 데이터 플래그
```

### Bad Example

```
반사례 1: Atlas 없이 Workers가 직접 협력
  Prometheus → Worker A → Worker B → Worker C
  문제: 각 Worker가 앞 단계를 다시 이해해야 함, 실패 시 복구 전략 없음

반사례 2: Prometheus가 없고 Atlas만 자동 실행
  자동으로 Workers 호출하지만 목표나 제약이 불명확
  문제: 무의미한 작업 실행, 비용 낭비

반사례 3: 모든 작업을 Atlas가 직접 수행
  Prometheus → Atlas(all execution logic)
  문제: Atlas 오버로드, 단순 재사용 패턴을 Worker로 분리할 기회 상실
```

---

## Further Reading
- Anthropic, "Building Effective Agents" (2024) — Multi-agent orchestration patterns
- Steve Yegge, "Gas Town" — Parallel agent design principles

---

## Test Cases

!`cat references/test-cases.md 2>/dev/null || echo ""`

## Troubleshooting

!`cat references/troubleshooting.md 2>/dev/null || echo ""`

---

## Contextual Knowledge (auto-loaded)

> 보조 파일이 존재할 때만 자동 로드됩니다. 파일이 없으면 건너뜁니다.

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`
