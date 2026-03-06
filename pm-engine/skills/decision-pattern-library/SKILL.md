---
name: decision-pattern-library
description: "Access and apply a growing library of PM decision patterns derived from real experience. Each pattern describes a recurring decision scenario with context, judgment criteria, and known failure modes. Use when facing a recurring decision, onboarding a new agent to PM thinking, or reviewing whether a past decision followed established patterns."
---

## Decision Pattern Library

PM이 매일 하는 결정의 80%는 반복입니다.  
패턴 라이브러리는 그 반복을 구조화합니다.

이 스킬은 pm-engine의 **살아있는 문서**입니다.  
TK 시리즈가 쌓일수록 이 라이브러리는 강해집니다.

---

### 패턴 라이브러리 구조

각 패턴은 3가지 요소로 구성됩니다:

```
[패턴 이름]
상황: [언제 이 패턴이 등장하는가]
판단: [어떻게 결정하는가]
함정: [흔히 빠지는 실수]
```

---

### 핵심 패턴 모음

---

**Pattern: Why-First Decision Making**

```
상황: 요청/아이디어가 들어왔을 때

판단:
1. "왜 이것이 필요한가?" 먼저 묻는다
2. 요청자의 진짜 목표 파악
3. 그 목표를 달성하는 최적 방법을 역산
4. 요청한 방법이 아닐 수도 있음 — 그게 PM의 역할

함정: 요청을 그대로 수행하고 "왜"를 묻지 않음
→ 올바른 문제의 잘못된 해결책을 만드는 가장 흔한 실수

에이전트 적용:
Instruction에 "항상 요청의 배경 목적을 파악하고,
요청된 방법이 최적인지 먼저 검토한다"
```

---

**Pattern: Prototype-First Validation**

```
상황: 새로운 기능/에이전트를 만들려 할 때

판단:
1. 스펙 작성 전에 가장 빠른 프로토타입부터
2. 45분 프로토타입 → 검증 → 스펙 (역순)
3. 프로토타입이 틀리면 스펙 폐기 비용 = 0

함정: "제대로 된 것"을 만들려다가 시작을 못함
→ 완벽한 PRD를 쓰는 동안 시장이 바뀜

에이전트 적용:
agent-opportunity-tree → 3번의 가정 검증 → Instruction 작성
(스펙 먼저 쓰지 않음)
```

---

**Pattern: Minimum Viable Agent**

```
상황: 에이전트 설계 초안을 잡을 때

판단:
1. 이 에이전트가 해야 할 단 하나의 핵심 기능 정의
2. 그 핵심만으로 작동하는 최소 버전 배포
3. 실사용 데이터로 확장 방향 결정

함정: 처음부터 모든 기능을 넣으려 함
→ 복잡도 급증, 실패 원인 파악 어려움

에이전트 적용:
MVP: Single Agent (1개 기능)
검증 후: Pipeline 또는 Hierarchical 확장
```

---

**Pattern: Stakeholder Energy Management**

```
상황: 여러 이해관계자의 요청이 동시에 들어올 때

판단:
1. 각 요청을 "비즈니스 임팩트"로만 평가
2. 발신자의 직급/압박감은 우선순위 기준이 아님
3. 데이터로 설명 가능한 우선순위 기준 사전 수립

함정: 가장 많이 요청하는 사람 요청이 올라감
→ 핵심 작업이 밀림, 팀 집중력 분산

에이전트 적용:
에이전트 task-prioritization: 임팩트 기준만 사용,
발신자 정보는 참조하되 우선순위 결정에 미포함
```

---

**Pattern: Data-Before-Opinion**

```
상황: 무언가를 결정해야 하는데 의견이 갈릴 때

판단:
1. "이것을 검증할 수 있는 가장 작은 실험은?"
2. 실험 설계 → 데이터 수집 → 결정
3. 실험 비용이 너무 높으면 가정을 명시하고 진행

함정: 회의에서 의견으로 결정하고 실행
→ 나중에 틀렸을 때 근거 없이 방향 전환 어려움

에이전트 적용:
agent-assumption-map의 실험 설계 패턴과 직결
```

---

**Pattern: Scope Creep Prevention**

```
상황: 프로젝트/에이전트 진행 중 "이것도 추가하면 어때?"가 나올 때

판단:
1. 추가 요청을 즉시 수용하지 않음
2. "이것이 현재 목표와 어떻게 연결되는가?" 검토
3. 연결되면 → 다음 이터레이션
4. 연결 안 되면 → 백로그 추가, 현재 스프린트 유지

함정: 좋은 아이디어를 모두 넣으려다 아무것도 못 냄

에이전트 적용:
에이전트 Instruction의 Scope 섹션 — 명시적 Anti-Goals로 관리
```

---

### 패턴 추가 방법

pm-engine이 성장할수록 이 라이브러리는 확장됩니다:

```
새로운 의사결정 경험 발생
        ↓
/pm-tacit-extract로 구조화
        ↓
TK-NNN 번호 부여
        ↓
PM-ENGINE-MEMORY.md에 저장
        ↓
/tk-to-instruction으로
에이전트 Instruction에 반영
        ↓
decision-pattern-library 업데이트
```

---

### 사용 방법

`/pm-decision-log [현재 직면한 결정 상황]`

---

### Instructions

You are helping apply decision patterns to: **$ARGUMENTS**

**Step 1** — 상황 파악  
어떤 의사결정 상황인지 명확히 정의

**Step 2** — 패턴 매칭  
라이브러리에서 가장 유사한 패턴 1~2개 찾기

**Step 3** — 패턴 적용  
해당 패턴의 판단 기준을 현재 상황에 적용

**Step 4** — 함정 체크  
해당 패턴의 흔한 실수를 현재 상황에서 피하고 있는가?

**Step 5** — 신규 패턴 가능성**  
현재 상황이 기존 패턴에 없는 새로운 패턴인가?  
→ YES: `/pm-tacit-extract`로 새 TK 추출

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- 패턴 원천: PM-ENGINE-MEMORY TK 시리즈 (누적 중)
- "Taste at Speed": Boris Cherny (Anthropic), Aakash Gupta 분석 (2026-03-06)
- Why-First 원칙: 이든의 20년 PM 핵심 철학
