---
name: prometheus-atlas-pattern
description: "Design a hierarchical multi-agent orchestration system using the Prometheus-Atlas pattern — a 3-tier architecture where a Planner spawns specialized sub-agents and consolidates results. Use when a task is too complex for a single agent, requires parallel execution, or involves multiple domains that need coordination. Based on real-world implementation by Sanguine Kim (2026)."
---

## Prometheus-Atlas Pattern

복잡한 작업을 단일 에이전트로 처리하려 할 때 발생하는 3가지 문제:
1. 컨텍스트 윈도우 초과 → 품질 저하
2. 순차 처리 → 실행 시간 증가
3. 단일 실패 지점 → 전체 작업 실패

Prometheus-Atlas 패턴은 이를 **계층적 역할 분리**로 해결합니다.

---

### 패턴 개요

```
[Prometheus — 계획자]
        │
        │ 작업 분해 + 서브에이전트 스폰
        ↓
[Atlas — 오케스트레이터]
   ┌────┴────┐
   ↓         ↓
[Worker A] [Worker B] ... (병렬 실행)
   └────┬────┘
        ↓
[Consolidation — 통합자]
        ↓
  [최종 출력 → 사용자]
```

---

### 3계층 역할 정의

**Tier 1 — Prometheus (계획자)**

> "무엇을 해야 하는지"를 결정하는 전략 레이어

책임:
- 입력(목표/요청)을 분석하고 작업을 하위 도메인으로 분해
- 각 Worker의 역할과 범위를 정의
- 실행 순서와 의존관계를 결정 (병렬 가능 여부 판단)
- 전체 품질 기준 설정

설계 원칙:
- Prometheus는 직접 실행하지 않는다 → 계획만
- 작업 분해의 기준은 **도메인 독립성** (각 Worker가 서로 의존하지 않을 것)
- Claude Opus / Sonnet급 고성능 모델 권장 (전략적 판단이 핵심)

**Tier 2 — Atlas (오케스트레이터)**

> "어떻게 실행할지"를 관리하는 조율 레이어

책임:
- Prometheus의 계획을 받아 Worker 세션을 스폰
- Worker 간 병렬/순차 실행 조율
- Worker 실패 감지 및 재시도 또는 Prometheus에 에스컬레이션
- Worker 결과를 Consolidation으로 전달

설계 원칙:
- Atlas는 내용을 판단하지 않는다 → 흐름만 관리
- Worker 수는 3~5개 권장 (초과 시 관리 복잡도 급증)
- 타임아웃 설정 필수 (Worker hang 방지)

**Tier 3 — Workers (전문 실행자)**

> "실제 작업"을 수행하는 실행 레이어

Worker 유형 예시:
| Worker 이름 | 역할 | 도구 |
|---|---|---|
| market-scout | 시장 리서치 수집 | web_search, web_fetch |
| action-planner | 실행 계획 설계 | memory_search, Read |
| data-analyst | 데이터 분석 | exec (Python) |
| content-writer | 콘텐츠 생성 | Write |
| reviewer | 품질 검토 | Read, 판단만 |

Worker 설계 원칙:
- 단일 책임: 1 Worker = 1 도메인
- 독립 실행 가능: 다른 Worker 결과에 의존 최소화
- 경량 모델 가능: Haiku로도 충분한 경우 비용 절감

**Consolidation (통합자)**

> "결과를 합치고" 사용자에게 전달하는 레이어

책임:
- 모든 Worker 결과를 수집
- 중복 제거, 품질 기준 적용
- 최종 출력 형식으로 변환 (Telegram / 파일 / Notion)
- 실패한 Worker 결과를 graceful하게 처리

---

### 실제 구현 사례 (agent-goal-advisor, 2026-03)

```
Prometheus (Sonnet)
└── 오늘의 전략 목표 분석 + 시장 리서치 필요 항목 정의
        ↓
Atlas (Sonnet)
├── market-scout (Haiku) ─── 시장 시그널 수집 (web_search 5회)
└── action-planner (Sonnet) ─ 메모리 참조 + 액션 설계
        ↓
Consolidation (Sonnet)
└── 3개 액션 통합 → Telegram 전송
```

성과:
- 단일 에이전트 대비 품질 향상 (Worker 전문화)
- 병렬 실행으로 실행 시간 ~40% 단축
- 각 Worker 독립 재시도 가능

---

### 패턴 선택 가이드

Prometheus-Atlas 패턴이 **적합한 경우**:
- 작업이 2개 이상의 독립 도메인으로 분해 가능
- 병렬 실행으로 시간 단축이 필요
- 단일 에이전트 실패 시 전체 중단이 허용 안 됨
- 품질 검토(Reviewer Worker)가 필요

**적합하지 않은 경우**:
- 단순 단일 작업 (과설계 위험)
- 모든 단계가 순차 의존적 (병렬화 불가)
- 비용 최소화가 최우선 (Worker 수만큼 토큰 비용 증가)

대안 패턴:
| 상황 | 권장 패턴 |
|---|---|
| 단순 단일 작업 | Single Agent |
| 순차 파이프라인 | Chain Pattern |
| 이벤트 감시 | Monitor + Trigger |
| Prometheus-Atlas | 복잡한 멀티도메인 작업 |

---

### MCP vs Skills 계층 설계

Byeonghyeok Kwak의 계층적 분리 원칙을 Prometheus-Atlas에 적용:

```
사고 계층    → Prometheus + Atlas + Workers (LLM + Skills)
연결 계층    → MCP (외부 시스템: ERP, 코어뱅킹, 규제 DB)
거버넌스 계층 → 인증·감사로그·정책 (MCP 위에 구축)
```

실무 적용 규칙:
- Workers의 내부 로직 → Skills로 구현
- Workers의 외부 시스템 연결 → MCP로 구현 (필요 시)
- MCP는 3~5개 전략적 외부 연계 지점에만 집중

---

### 사용 방법

`/orchestration-pattern [자동화하려는 복잡한 작업]`

---

### Instructions

You are helping design a **Prometheus-Atlas multi-agent system** for: **$ARGUMENTS**

**Step 1 — 작업 분해 가능성 확인**
- 작업을 독립적인 하위 도메인으로 분해할 수 있는가?
- 병렬 실행 가능한 부분은 무엇인가?
- Prometheus-Atlas가 적합한지, 더 단순한 패턴이 나은지 판단

**Step 2 — Prometheus 설계**
- 입력 분석 방식 정의
- 작업 분해 기준 (도메인 독립성 기준)
- 사용할 모델 선택 (Sonnet 이상 권장)

**Step 3 — Atlas 설계**
- Worker 목록 정의 (최대 5개)
- 병렬 / 순차 실행 결정
- 실패 처리 전략 (재시도 횟수, 에스컬레이션 조건)
- 타임아웃 설정

**Step 4 — Worker 설계 (각각)**
- 역할 정의 (단일 책임)
- 필요한 도구 목록
- 입력 / 출력 형식
- 사용할 모델 (경량화 가능 여부 검토)

**Step 5 — Consolidation 설계**
- 결과 수집 방식
- 품질 기준 (Worker Reviewer 필요 여부)
- 최종 출력 형식과 채널

**Step 6 — 비용 추정**
- 예상 토큰 사용량 (Prometheus + Atlas + Workers × 평균 토큰)
- 월 실행 횟수 × 단가 = 월 운영 비용
- 최적화 가능 지점 (Haiku로 교체 가능한 Worker)

**Step 7 — 구현 순서 제안**
- MVP 버전: Worker 1~2개로 시작
- 단계별 확장 계획
- `/agent-instruction-design`으로 각 Worker Instruction 작성 연결

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- 실제 구현: agent-goal-advisor 크론잡 (OpenClaw 워크스페이스)
- MCP-Skills 계층 원칙: Byeonghyeok Kwak (aiden-kwak), LinkedIn 2026-03
- Wasteland 연합 구조 참고: Steve Yegge, Gas Town (2026)
