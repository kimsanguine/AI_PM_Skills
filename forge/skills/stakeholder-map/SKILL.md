---
name: stakeholder-map
description: "Map and manage stakeholders for AI agent adoption — identify decision-makers, blockers, and champions across engineering, legal, operations, and leadership. Use when introducing an agent to an organization, navigating internal resistance, or planning change management for AI adoption."
argument-hint: "[agent initiative to map stakeholders for]"
---

# Agent Stakeholder Map

> 에이전트 도입 시 이해관계자 지도 — 누가 찬성하고, 누가 막고, 누가 결정하는가

## 개념

에이전트 도입은 기술 문제가 아니라 조직 변화 문제다. "AI가 내 일을 빼앗는다"는 불안이 가장 큰 저항 요인이고, 법무팀의 AI 리스크 우려, 엔지니어링의 기술 부채 걱정이 뒤를 따른다. 이해관계자를 미리 매핑하지 않으면 기술적으로 성공한 에이전트가 조직적으로 실패한다.

## Instructions

You are mapping **stakeholders for AI agent adoption**: **$ARGUMENTS**

### Step 1 — Stakeholder Identification

에이전트 도입에 관련된 이해관계자를 식별합니다:

| 이해관계자 | 역할 | 관심사 | 에이전트에 대한 태도 |
|-----------|------|--------|-------------------|
| **경영진 (C-Level)** | 최종 승인자 | ROI, 리스크, 경쟁 우위 | |
| **직접 사용자** | 일상 사용 | 업무 효율, 일자리 불안 | |
| **엔지니어링** | 구축/유지보수 | 기술 부채, 인프라 비용 | |
| **법무/컴플라이언스** | 리스크 검토 | 데이터 프라이버시, AI 규제 | |
| **운영/CS** | 장애 대응 | 안정성, 에스컬레이션 경로 | |
| **재무** | 예산 승인 | 비용 예측 가능성, ROI | |

### Step 2 — Power-Interest Matrix

```
        High Power
            │
   Manage   │   Engage
   Closely  │   Actively
            │
 ───────────┼──────────── High Interest
            │
   Monitor  │   Keep
   Only     │   Informed
            │
        Low Power
```

각 이해관계자를 매트릭스에 배치합니다:

```
[이해관계자]: [Power 1-5] × [Interest 1-5] → [사분면]
  └── 전략: [Engage/Manage/Inform/Monitor]
```

### Step 3 — Resistance Analysis

에이전트 도입의 핵심 저항 요인과 대응 전략:

| 저항 유형 | 근본 원인 | 대응 전략 |
|----------|----------|----------|
| **Job Threat** | "AI가 내 일을 대체한다" | Co-pilot 포지셔닝 — "AI가 반복 작업을 하고, 당신은 판단에 집중" |
| **Trust Deficit** | "AI 판단을 믿을 수 없다" | Shadow Mode 시작 → 정확도 증명 후 권한 확대 |
| **Control Loss** | "내가 통제할 수 없다" | Human-in-the-loop 설계 — 승인/거부 권한 보장 |
| **Risk Aversion** | "문제가 생기면 누가 책임?" | 책임 매트릭스(RACI) + 롤백 계획 명시 |
| **Tech Fatigue** | "또 새로운 도구를 배워야?" | 기존 워크플로우에 임베딩 — 별도 UI 최소화 |

### Step 4 — Champion Strategy

에이전트 도입의 내부 챔피언을 발굴하고 무장시킵니다:

```
Champion Profile:
  ├── 누구: [가장 큰 pain을 겪는 사람]
  ├── 동기: [에이전트가 해결하는 구체적 문제]
  ├── 무장:
  │   ├── 데이터: [현재 수동 작업 시간/비용]
  │   ├── 데모: [Shadow Mode 결과]
  │   └── ROI: [3개월 절약 예측]
  └── 확산 경로: [챔피언 → 팀 → 조직]
```

### Step 5 — Communication Plan

이해관계자별 맞춤 커뮤니케이션:

```
경영진:
  메시지: "경쟁사보다 [N]개월 앞서는 기회"
  포맷: 1-page ROI 요약 + 리스크 대비책
  주기: 월 1회 진행 보고

직접 사용자:
  메시지: "반복 작업에서 해방 — 당신의 판단력에 집중"
  포맷: 핸즈온 데모 + Q&A 세션
  주기: 주 1회 (도입 초기)

엔지니어링:
  메시지: "깔끔한 아키텍처 + 명확한 소유권"
  포맷: 기술 스펙 + 인프라 비용 예측
  주기: 스프린트 단위

법무:
  메시지: "리스크 통제 가능 — HITL + 감사 로그"
  포맷: AI 리스크 체크리스트 + 규제 매핑
  주기: 마일스톤 단위
```

### Output

```
Stakeholder Map: [agent initiative]
──────────────────────────────────
Total Stakeholders: [N]
Champions: [names/roles]
Blockers: [names/roles] — Mitigation: [strategy]
Decision Maker: [name/role] — Engage via: [strategy]
Top Resistance: [type] — Counter: [strategy]
Communication Cadence: [summary]
Go/No-Go Confidence: [Low/Medium/High]
```

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- AI 도입 저항 패턴: AI Dubbing/Avatar 조직 도입 경험 기반
- Trust Building Sequence: agent-gtm 스킬과 연결

---

## Further Reading
- John Kotter, *Leading Change* — 8-step change management framework
- Anthropic, "Building Effective Agents" (2024) — Human-agent trust patterns
