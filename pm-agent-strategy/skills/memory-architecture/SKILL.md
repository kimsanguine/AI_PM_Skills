---
name: memory-architecture
description: "Design a memory system for AI agents — defining what to remember, where to store it, and how to retrieve it across sessions. Covers 3 memory types: Working (context window), Long-term (files), and Procedural (skill files). Use when building agents that need to learn, persist state, or accumulate knowledge over time."
---

## Agent Memory Architecture

단일 대화형 AI와 에이전트의 근본 차이:
- 대화형 AI: 매 세션 초기화, 기억 없음
- 에이전트: **세션을 넘어 지식과 상태를 축적**

에이전트 메모리 설계의 3가지 함정:
1. 모든 것을 컨텍스트에 넣는다 → 윈도우 초과, 비용 급증
2. 아무것도 저장하지 않는다 → 반복 작업, 학습 없음
3. 구조 없이 저장한다 → 검색 불가, 노이즈 축적

이 스킬은 **3계층 메모리 아키텍처**로 이 문제를 해결합니다.

---

### 3계층 메모리 구조

```
┌─────────────────────────────────┐
│  Layer 1: Working Memory        │  ← 컨텍스트 윈도우 (휘발성)
│  [현재 세션의 모든 정보]          │
└─────────────────────────────────┘
           ↕ 읽기/쓰기
┌─────────────────────────────────┐
│  Layer 2: Long-term Memory      │  ← 파일 시스템 (영구)
│  [세션 간 유지해야 할 정보]       │
└─────────────────────────────────┘
           ↕ 읽기/쓰기
┌─────────────────────────────────┐
│  Layer 3: Procedural Memory     │  ← SKILL.md 파일 (구조화)
│  [반복 판단 패턴 + 워크플로우]    │
└─────────────────────────────────┘
```

---

### Layer 1 — Working Memory (작업 메모리)

**정의**: 현재 실행 중인 컨텍스트 윈도우 안의 모든 정보  
**특성**: 세션 종료 시 사라짐 (휘발성)  
**한계**: 모델별 최대 윈도우 크기 (Claude: 200k tokens)

**설계 원칙:**

1. **우선순위 로딩** — 컨텍스트 예산 계획
```
High Priority   (항상 로드): SOUL.md, USER.md, 오늘 메모리 파일
Medium Priority (필요시 로드): MEMORY.md, 관련 SKILL.md
Low Priority    (최소화): 로그, 원문 데이터, 중간 결과
```

2. **컨텍스트 오염 방지**
- 불필요한 파일 전체 로드 금지 → 필요한 섹션만 발췌
- 이전 세션 대화 기록 최소화
- 큰 파일은 `memory_search`로 관련 부분만 추출

3. **컨텍스트 사용률 모니터링**
```
70% 미만: 정상
70~85%:  경고 — 중요 내용 파일 저장 시작
85% 이상: 위험 — 컴팩션 임박, 즉시 상태 저장
```

---

### Layer 2 — Long-term Memory (장기 메모리)

**정의**: 파일 시스템에 저장된 영구 정보  
**특성**: 세션 간 유지됨, 읽기/쓰기 가능  
**형태**: Markdown 파일, JSON, 구조화 텍스트

**파일 분류 체계:**

```
memory/
├── YYYY-MM-DD.md          # 일별 원시 로그 (raw notes)
├── heartbeat-state.json   # 하트비트 상태 추적
└── retrospective-YYYY-MM-DD.md  # 회고

MEMORY.md                  # 장기 기억 (큐레이션)
USER.md                    # 사용자 프로필 (불변에 가까움)
SOUL.md                    # 에이전트 정체성 (불변)
```

**도메인별 메모리 파일:**
```
pm-engine/PM-ENGINE-MEMORY.md     # PM 암묵지 TK 시리즈
ai-business/AI-BUSINESS-MEMORY.md # AI 비즈니스 전략
finance/FINANCE-MEMORY.md         # 재무/투자 메모리
```

**메모리 쓰기 원칙:**
- 일별 파일: 날것의 로그 (모든 것 기록)
- MEMORY.md: 증류된 핵심 (중요한 것만 큐레이션)
- 도메인 파일: 도메인 특화 패턴 (구조화)

**메모리 유지보수 사이클:**
```
매일:   memory/YYYY-MM-DD.md에 당일 이벤트 기록
매주:   daily 파일 검토 → MEMORY.md에 핵심 증류
매월:   MEMORY.md 오래된 항목 제거, 도메인 파일 업데이트
```

---

### Layer 3 — Procedural Memory (절차적 메모리)

**정의**: 반복적인 판단 패턴과 워크플로우를 구조화한 SKILL.md 파일  
**특성**: 에이전트의 "암묵지"를 명시적 지식으로 전환  
**형태**: SKILL.md 파일 (이 프로젝트의 모든 스킬)

**외부화 기준 — 언제 SKILL.md로 분리하는가?**

```
같은 판단을 3회 이상 반복한다       → SKILL.md 후보
판단 기준이 명확하게 설명 가능하다  → SKILL.md 작성
다른 에이전트도 이 판단을 쓸 수 있다 → SKILL.md 공유
```

**pm-engine의 역할:**
- PM-ENGINE-MEMORY의 TK 시리즈 = 절차적 메모리의 원료
- `/tk-to-instruction`으로 TK → SKILL.md 자동 변환
- 사용할수록 절차적 메모리가 쌓임 → Domain TK 해자 강화

---

### 실제 구현 사례 (OpenClaw 기반)

```
이든의 에이전트 메모리 구조:

Working Memory:
├── SOUL.md (읽기 우선)
├── USER.md
├── memory/2026-03-06.md (오늘)
└── memory/2026-03-05.md (어제)

Long-term Memory:
├── MEMORY.md (장기 기억 큐레이션)
├── pm-engine/PM-ENGINE-MEMORY.md
├── ai-business/AI-BUSINESS-MEMORY.md
└── finance/FINANCE-MEMORY.md

Procedural Memory (Skills):
├── ~/.agents/skills/ (OpenClaw 스킬)
└── 260306_AgentSkills/ (이 프로젝트)
```

결과:
- 컨텍스트 효율: 필요한 파일만 로드 → 평균 사용률 낮게 유지
- 세션 연속성: 매일 memory 파일로 전날 컨텍스트 복원
- 도메인 전문성: TK 시리즈 누적으로 PM 판단 품질 향상

---

### 메모리 설계 체크리스트

**Working Memory:**
- [ ] 컨텍스트 윈도우 예산 계획 수립
- [ ] 파일 로딩 우선순위 정의
- [ ] 70%/85% 경고 임계값 설정

**Long-term Memory:**
- [ ] 일별 / 도메인별 파일 구조 설계
- [ ] 쓰기 트리거 정의 (언제 저장하는가)
- [ ] 유지보수 사이클 설정 (크론)

**Procedural Memory:**
- [ ] 반복 판단 패턴 식별
- [ ] SKILL.md 외부화 기준 명시
- [ ] 메모리 → 스킬 변환 파이프라인 설계

---

### 사용 방법

`/memory-architecture [에이전트 또는 시스템 설명]`

---

### Instructions

You are helping design a memory architecture for: **$ARGUMENTS**

**Step 1 — 메모리 요구사항 파악**
- 이 에이전트가 기억해야 할 정보 유형 나열
- 세션 간 유지 필요 여부 분류
- 반복 판단 패턴 식별

**Step 2 — 3계층 설계**
- Working Memory: 컨텍스트 예산 계획 + 로딩 우선순위
- Long-term Memory: 파일 구조 + 쓰기 트리거
- Procedural Memory: SKILL.md 외부화 후보 목록

**Step 3 — 파일 구조 설계**
- 디렉토리 구조 제안
- 각 파일의 역할과 업데이트 주기

**Step 4 — 유지보수 사이클**
- 일별/주별/월별 메모리 관리 루틴
- 크론잡 설정 제안 (weekly-memory-distill 패턴)

**Step 5 — 컨텍스트 최적화**
- 현재 설계에서 컨텍스트 낭비 요소 진단
- memory_search 활용으로 동적 로딩 설계

**Step 6 — 다음 단계 연결**
- 절차적 메모리 구축: `pm-engine` 플러그인
- 컨텍스트 예산: `context-window-budget` 스킬
- 메모리 → 해자: `agent-moat` (Domain TK 해자)

---

### 참고
- 3계층 구조: Sanguine Kim (이든)의 OpenClaw 메모리 아키텍처 (2026-02)
- 도메인별 메모리: 3-도메인 메모리 아키텍처 (PM-ENGINE / AI-BUSINESS / FINANCE)
- Contextual Retrieval 패턴: PM-ENGINE-MEMORY CR 필드 (2026-03-01 도입)
- 컨텍스트 모니터링: OpenClaw 하트비트 컨텍스트 70%/85% 임계값 운영 경험
