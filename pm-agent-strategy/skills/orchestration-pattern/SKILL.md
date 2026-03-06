---
name: orchestration-pattern
description: "Select the optimal orchestration pattern for a multi-agent or complex automation task — Single, Pipeline, Parallel, Hierarchical, or Event-Driven. Use when designing how multiple agents or steps should be coordinated. Prevents over-engineering simple tasks and under-engineering complex ones."
---

## Orchestration Pattern 선택 가이드

에이전트 설계에서 가장 흔한 두 실수:
- 단순한 작업에 Prometheus-Atlas 같은 복잡한 계층 구조 → 과설계 + 비용 낭비
- 복잡한 멀티도메인 작업을 단일 에이전트에게 → 컨텍스트 초과 + 실패율 급증

이 스킬은 **작업의 복잡도와 특성**에 따라 5가지 패턴 중 최적 선택을 돕습니다.

---

### 패턴 1 — Single Agent (단일 에이전트)

```
[Input] → [Agent] → [Output]
```

**언제 쓰는가:**
- 단일 도메인 작업 (번역, 요약, 분류, 생성)
- 입력 → 출력이 명확하고 단계가 1~2개
- 컨텍스트 윈도우 안에 모든 정보가 들어옴
- 실행 시간 < 30초 목표

**장점:** 가장 빠르고 저렴. 디버깅 단순.  
**단점:** 복잡한 작업에는 품질 저하.

**비용 수준:** ⭐ (가장 낮음)  
**구현 난이도:** ⭐

**예시:**
- 링크 URL → 요약 텍스트 생성
- 뉴스 제목 → 카테고리 분류
- 사용자 질문 → 답변

---

### 패턴 2 — Pipeline (순차 파이프라인)

```
[Input] → [Agent A] → [Agent B] → [Agent C] → [Output]
```

**언제 쓰는가:**
- 각 단계의 출력이 다음 단계의 입력 (순차 의존)
- 단계마다 전문화된 역할이 필요
- 중간 결과를 검토/수정할 수 있어야 함

**장점:** 각 단계 품질 검증 가능. 단계별 모델 최적화 가능.  
**단점:** 앞 단계 실패 시 전체 중단. 순차이므로 느림.

**비용 수준:** ⭐⭐  
**구현 난이도:** ⭐⭐

**예시:**
- 원문 수집 → 번역 → 요약 → 발송
- 데이터 추출 → 분석 → 인사이트 생성 → 리포트 작성

---

### 패턴 3 — Parallel (병렬 실행)

```
         ┌→ [Agent A] →┐
[Input] →┼→ [Agent B] →┼→ [Merge] → [Output]
         └→ [Agent C] →┘
```

**언제 쓰는가:**
- 독립적인 도메인을 동시에 처리해야 할 때
- 실행 시간 단축이 중요할 때
- 각 서브태스크가 서로 의존하지 않음

**장점:** 실행 시간 대폭 단축. 각 Agent 독립 실패 허용.  
**단점:** 결과 병합(Merge) 로직 필요. 동시 API 호출 비용.

**비용 수준:** ⭐⭐⭐ (동시 호출)  
**구현 난이도:** ⭐⭐⭐

**예시:**
- 시장 리서치 + 경쟁사 분석 + 재무 분석 동시 수행
- 여러 소스에서 병렬 데이터 수집 후 통합

---

### 패턴 4 — Hierarchical (계층형, Prometheus-Atlas)

```
[Planner]
    │ 작업 분해
    ↓
[Orchestrator]
  ┌──┴──┐
[W1]  [W2]  (병렬)
  └──┬──┘
[Consolidation]
    ↓
[Output]
```

**언제 쓰는가:**
- 2개 이상의 독립 도메인 + 병렬 처리 + 품질 통합 모두 필요
- 작업 규모가 커서 단일 컨텍스트로 처리 불가
- Reviewer Agent가 필요한 품질 기준
- → [prometheus-atlas-pattern] 참조

**장점:** 복잡한 작업 처리 가능. 실패 격리. 품질 보장.  
**단점:** 설계 복잡. 비용 높음. 오버헤드 존재.

**비용 수준:** ⭐⭐⭐⭐  
**구현 난이도:** ⭐⭐⭐⭐

**예시:**
- agent-goal-advisor: Prometheus → [market-scout || action-planner] → Consolidation
- 복합 리서치 + 분석 + 실행 계획 통합

---

### 패턴 5 — Event-Driven (이벤트 기반)

```
[Trigger: 이벤트 발생]
         ↓
[Router: 이벤트 유형 분류]
    ┌────┴────┐
[Handler A] [Handler B]
         ↓
[Output / Action]
```

**언제 쓰는가:**
- 특정 이벤트/조건 발생 시 자동 실행
- 크론 스케줄, 웹훅, 파일 변경 감지 등
- 이벤트 유형에 따라 다른 에이전트가 반응

**장점:** 반응형 자동화. 인간 개입 최소화.  
**단점:** 트리거 조건 설계가 핵심. 오탐/미탐 위험.

**비용 수준:** ⭐⭐ (이벤트 발생 시만 비용)  
**구현 난이도:** ⭐⭐⭐

**예시:**
- OpenClaw 크론잡: 시간 트리거 → 브리핑 생성 → Telegram 전송
- GitHub 이슈 생성 → 자동 트리아지 → 담당자 지정

---

### 패턴 선택 결정 트리

```
1. 작업이 단일 도메인이고 1~2단계인가?
   YES → Single Agent

2. 각 단계가 순차적으로 의존하는가?
   YES → Pipeline

3. 독립적인 도메인이 2개 이상이고 동시 처리 가능한가?
   YES + 품질 통합 필요 → Hierarchical
   YES + 단순 병합 → Parallel

4. 이벤트/조건 발생 시 자동 실행인가?
   YES → Event-Driven (내부는 위 패턴 중 조합)
```

---

### 패턴 비교 요약

| 패턴 | 복잡도 | 비용 | 속도 | 적합 작업 규모 |
|---|---|---|---|---|
| Single | ⭐ | ⭐ | ⚡⚡⚡ | 소 |
| Pipeline | ⭐⭐ | ⭐⭐ | ⚡⚡ | 중 |
| Parallel | ⭐⭐⭐ | ⭐⭐⭐ | ⚡⚡⚡ | 중~대 |
| Hierarchical | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⚡⚡ | 대 |
| Event-Driven | ⭐⭐⭐ | ⭐⭐ | 트리거 의존 | 반응형 |

---

### 사용 방법

`/orchestration-pattern [자동화하려는 작업 설명]`

---

### Instructions

You are helping select the optimal orchestration pattern for: **$ARGUMENTS**

**Step 1 — 작업 분석**
- 작업을 구성하는 단계 나열
- 각 단계 간 의존관계 확인 (순차 / 독립)
- 예상 컨텍스트 크기 추정

**Step 2 — 결정 트리 적용**
- 4가지 질문 순서대로 적용
- 복수 패턴이 가능한 경우 비용/속도/복잡도 트레이드오프 설명

**Step 3 — 패턴 상세 설계**
- 선택한 패턴의 구체적 구조도 (텍스트 다이어그램)
- 각 Agent/Worker의 역할 정의
- 사용할 모델 추천 (`model-router` 스킬 연계)

**Step 4 — 비용 추정**
- 예상 토큰 수 × 모델 단가 × 월 실행 횟수
- Haiku로 교체 가능한 단계 식별

**Step 5 — 구현 우선순위**
- MVP 버전 (가장 단순한 형태)
- 단계별 확장 계획

**Step 6 — 다음 단계 연결**
- Hierarchical 선택 시: `/prometheus-atlas-pattern`
- 각 Agent 설계: `/agent-instruction-design`
- 비용 상세: `agent-cost-model`

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- OpenClaw 22개 크론잡 운영 경험에서 패턴 도출
- Hierarchical 패턴: agent-goal-advisor 실제 구현 기반
