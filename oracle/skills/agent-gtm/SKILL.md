---
name: agent-gtm
description: "Design a Go-To-Market strategy for AI agent products — identify beachhead segments, define launch sequence, and plan adoption motions. Use when preparing to launch an agent product, choosing first customers, or planning the transition from internal tool to external SaaS."
argument-hint: "[agent product to plan GTM for]"
---

# Agent GTM Strategy

> 에이전트 제품의 시장 진입 전략 — 누구에게, 어떤 순서로, 어떻게 팔 것인가

## 개념

에이전트 GTM은 일반 SaaS GTM과 다르다. 에이전트는 "도구"가 아니라 "동료"를 파는 것이기 때문에, 신뢰 구축이 핵심이다. 첫 고객 세그먼트(비치헤드)를 잘못 고르면 신뢰를 쌓기 전에 자원이 바닥난다.

## Instructions

You are designing a **Go-To-Market strategy** for: **$ARGUMENTS**

### Step 1 — Beachhead Segment Selection

에이전트 제품의 첫 번째 고객 세그먼트를 선정합니다.

평가 기준:
| 기준 | 질문 | 점수 (1-5) |
|------|------|-----------|
| Pain Intensity | 이 문제가 얼마나 절실한가? | |
| Willingness to Trust AI | AI에게 이 업무를 맡길 준비가 되었는가? | |
| Data Availability | 에이전트 학습에 필요한 데이터가 있는가? | |
| Budget Authority | 구매 결정을 빨리 내릴 수 있는가? | |
| Reference Potential | 성공 시 다른 고객에게 추천할 의향이 있는가? | |

**총점 20 이상 → 비치헤드 후보**

### Step 2 — Trust Building Sequence

에이전트 제품의 신뢰 구축 4단계:

```
Stage 1 — Shadow Mode (2주)
  에이전트가 추천만 하고, 사람이 실행
  → "이 에이전트 꽤 정확하네" 인식 형성

Stage 2 — Co-pilot Mode (4주)
  에이전트가 실행하되, 사람이 승인
  → "내가 확인하면 안전하구나" 신뢰 축적

Stage 3 — Auto-pilot Mode (제한적)
  특정 태스크만 자동 실행, 나머지는 Co-pilot 유지
  → "이 영역은 맡겨도 되겠다" 부분 위임

Stage 4 — Full Delegation
  에이전트가 자율 실행, 사람은 예외만 처리
  → "없으면 안 되는 동료" 포지셔닝
```

### Step 3 — Launch Sequence

```
Phase 1 — Lighthouse (1~3개 고객)
  └── 목표: 성공 사례 1개 확보
  └── 전략: 무료 또는 원가 제공, 밀착 온보딩
  └── KPI: 에이전트 정확도 > 80%, 재사용률 > 60%

Phase 2 — Wedge (10~30개 고객)
  └── 목표: 반복 가능한 세일즈 모션 확보
  └── 전략: Lighthouse 레퍼런스 활용, 셀프서브 온보딩
  └── KPI: CAC payback < 6개월, NPS > 40

Phase 3 — Expand (100+ 고객)
  └── 목표: 인접 세그먼트 확장
  └── 전략: PLG + 기존 고객 확장(upsell)
  └── KPI: Net Revenue Retention > 120%
```

### Step 4 — Pricing Model

에이전트 제품 가격 모델 선택:

| 모델 | 설명 | 적합한 경우 |
|------|------|-----------|
| Per-task | 에이전트가 완료한 작업당 과금 | 작업 단위가 명확할 때 |
| Per-seat | 사용자 수 기반 | 에이전트가 개인 도구일 때 |
| Outcome-based | 성과(절약 시간, 매출 증가) 기반 | ROI를 직접 증명할 수 있을 때 |
| Token pass-through + margin | API 비용 + 마진 | B2B 에이전트, 비용 투명성 중시 |

### Step 5 — Competitive Positioning

```
Positioning Statement:
For [beachhead segment]
Who [pain point]
[Agent name] is a [category]
That [key benefit]
Unlike [alternative]
Our agent [key differentiator — TK/data moat]
```

### Output

```
Agent GTM Strategy: [agent name]
─────────────────────────────
Beachhead: [segment] (Score: [N]/25)
Trust Sequence: Shadow → Co-pilot → Auto → Delegation
Launch Phase: Lighthouse → Wedge → Expand
Pricing: [model] — [price point]
First 90-Day Goals:
  - Lighthouse customers: [N]
  - Agent accuracy: > [N]%
  - Reuse rate: > [N]%
Positioning: [one-line statement]
```

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- Geoffrey Moore, *Crossing the Chasm* — 비치헤드 전략 원전
- 에이전트 SaaS의 신뢰 구축 시퀀스: OpenClaw 고객 온보딩 경험 기반

---

## Further Reading
- Geoffrey Moore, *Crossing the Chasm* — Technology adoption lifecycle and beachhead strategy
- Anthropic, "Building Effective Agents" (2024) — Agent deployment patterns and trust building
