---
name: agent-gtm
description: "Design a Go-To-Market strategy for AI agent products — identify beachhead segments, define launch sequence, and plan adoption motions. Use when preparing to launch an agent product, choosing first customers, or planning the transition from internal tool to external SaaS."
argument-hint: "[agent product to plan GTM for]"
allowed-tools: ["Read", "Write", "WebSearch", "WebFetch"]
model: sonnet
---

## Core Goal

- 에이전트 제품의 첫 고객 세그먼트(비치헤드)를 객관적 점수(5개 기준, 총 25점)로 선정하여 초기 신뢰 구축을 성공시킴
- Shadow → Co-pilot → Auto → Delegation의 4단계 신뢰 구축 시퀀스를 통해 사용자가 에이전트를 점진적으로 신뢰하도록 유도
- Lighthouse → Wedge → Expand 3단계 출시 계획으로 성공 사례를 확보한 후 반복 가능한 세일즈 모션을 구축

---

## Trigger Gate

### Use This Skill When
- 내부에서 성공한 에이전트를 외부 고객에게 팔 준비가 되었을 때
- 여러 고객 세그먼트 중 "누구를 먼저 타겟할지" 결정해야 할 때
- 에이전트 제품의 신뢰 구축 로드맵(어떻게 사용자를 확신시킬 것인가)을 설계해야 할 때
- 출시 후 처음 3개월의 구체적 KPI와 단계별 목표를 정의해야 할 때

### Route to Other Skills When
- Beachhead 선정 후 해당 세그먼트를 위한 에이전트 커스터마이징이 필요할 때 → `agent-instruction-design` (forge 플러그인)
- 신뢰 구축 시퀀스를 에이전트 자체에 설계해야 할 때 → `hitl` (Oracle 플러그인) — Shadow Mode / Co-pilot Mode 구현
- 가격 책정과 가치 제시 방식을 결정해야 할 때 → `cost-sim` (oracle 플러그인) — 예상 ROI 계산

### Boundary Checks
- **B2B 중심**: agent-gtm은 B2B SaaS 또는 엔터프라이즈 에이전트 출시 기준으로 설계됨 — B2C 에이전트(개인 사용자 대상)는 다른 GTM 프레임워크 필요
- **신뢰 구축이 핵심**: 일반 SaaS GTM과 다르게, 에이전트는 "도구"가 아니라 "자율 동료"이므로 신뢰가 최우선 요소 — 가격이나 기능 스펙보다는 "이 에이전트가 정말 정확할까?"라는 의심 해결

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

### Step 6 — 배포 채널 전략

에이전트 제품의 배포 방식을 선택합니다.

**에이전트 배포 채널 선택:**

| 채널 | 설명 | 장점 | 단점 |
|------|------|------|------|
| API 직접 제공 | REST/gRPC API로 고객이 자체 시스템에 통합 | 고객 자율성 높음; 개발 간단 | 고객 온보딩 복잡; 통합 난이도 높음 |
| MCP (Model Context Protocol) | 표준 프로토콜 기반 도구 연동 (Anthropic, OpenAI 호환) | 구현 기간 단축; 유지보수 편함; 에코시스템 활용 | Anthropic Claude 에코시스템 의존 |
| 마켓플레이스 (GPT Store, Vertex Agent Builder) | 플랫폼사 마켓플레이스에 등록 | 플랫폼 트래픽 활용; 신뢰도 높음 | 플랫폼 정책 종속; 수수료 발생 |
| 파트너 통합 | SaaS 파트너(Slack, Zapier, Make 등)를 통한 간접 배포 | 고객 기존 워크플로우와 통합; 채택률 높음 | 파트너 의존성; 마진 감소 |
| 화이트레이블 | 고객 브랜드로 배포 | 고객 로열티 높음; 엔터프라이즈 계약 확대 | 커스터마이징 비용 높음; 유지보수 부담 |

💡 **MCP 등 플랫폼별 상세 전략은 !domain 참고**

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

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| Beachhead 선정 후 고객이 "이건 우리 요구사항과 안 맞는다"고 판명 | Lighthouse 고객 오보딩 1주 후 이탈 신호 또는 명시적 거절 | 즉시 다음 순위 비치헤드로 전환 (점수 2번째 이상); 탈락한 세그먼트의 이유 기록 (향후 마케팅 메시지 개선에 활용) |
| Shadow Mode 기간이 너무 길어져서(6주+) Lighthouse 고객이 지쳐 버림 | "일단 자동화해 줄래?" 고객 요청 또는 참여도 감소 | Stage 1 기간 단축 (2주 → 1주) 또는 신뢰도 임계값 재조정 (정확도 요구사항 낮추기); Co-pilot Mode로 진전 (사용자가 덜 답답해짐) |
| Trust Sequence를 거쳤는데도 Wedge Phase에서 구매 의향 낮음 (NPS < 30) | Phase 2 10~30개 고객 목표 미달성 | Lighthouse 고객 피드백 재수집; GTM 메시지 또는 가격 재검토; 또는 Beachhead 세그먼트 재평가 (실제 Pain이 충분하지 않았나?) |
| Lighthouse에서는 성공했는데 Wedge 고객들은 구축 난이도가 높다고 불평 | 반복되는 온보딩 이슈 또는 구현 기간 지연 | Lighthouse 고객이 "easy mode"였을 가능성 → Wedge 고객에 맞춘 온보딩 자동화/가이드 강화 필요; 또는 Lighthouse 레퍼런스의 환경이 특수했던 건 아닌지 재검토 |

---

## Quality Gate

- Beachhead Segment가 5개 평가 기준(Pain Intensity, Trust AI, Data Availability, Budget Authority, Reference Potential)에 각각 점수(1~5)를 받았고, 총 20점 이상인가? (Yes/No)
- Trust Building Sequence의 4단계(Shadow/Co-pilot/Auto/Delegation)가 각각 정의되었고, 각 단계의 기간과 성공 기준이 명시되어 있는가? (Yes/No)
- Launch Sequence의 3개 Phase(Lighthouse/Wedge/Expand)가 정의되었고, 각 Phase의 고객 수, 목표, 전략, KPI가 구체적으로 명시되어 있는가? (Yes/No)
- 첫 90일의 구체적 목표(Lighthouse 고객 수, 에이전트 정확도 목표, 재사용률 목표)가 정의되어 있는가? (Yes/No)
- Positioning Statement가 작성되었고, Beachhead/Pain Point/Key Benefit/Differentiator가 명확히 드러나는가? (Yes/No)
- Lighthouse 고객 이탈 신호(정확도 목표 미달성, 참여도 급감, 명시적 거절 등)가 정의되어 있는가? (Yes/No)
- 각 Phase 진입/이탈 기준(Lighthouse → Wedge 전환 조건, Wedge → Expand 기준)이 명확한가? (Yes/No)

---

## Examples

### Good Example

```
Agent Product: "법무팀 계약서 자동 검토 에이전트"

Step 1 — Beachhead Selection:

| 기준 | 점수 | 근거 |
|------|------|------|
| Pain Intensity | 5 | 변호사가 검토에 주 20시간 이상 사용; 계약 지연 비용 연 $500k+ |
| Willingness to Trust AI | 4 | "검토는 AI가, 최종 승인은 변호사가"라는 hybrid 모델에 동의 |
| Data Availability | 5 | 과거 5년 계약서 + 검토 이력 모두 디지털화 완료 |
| Budget Authority | 5 | 법무팀장이 구매 결정 단독 권한 보유 |
| Reference Potential | 4 | 성공 시 다른 법무팀 추천 가능; 사례 발표 동의 |
| **총점** | **23/25** | ✓ Beachhead 적합 |

Step 2 — Trust Building Sequence:

Stage 1 — Shadow Mode (2주)
  - 에이전트가 검토만 하고, 변호사가 최종 판단 수행
  - 성공 기준: 에이전트 평가 vs 변호사 최종 판단 90% 이상 일치

Stage 2 — Co-pilot Mode (4주)
  - 에이전트가 1차 검토 자동 수행 → 변호사가 2차 승인 후 고객 송부
  - 성공 기준: 변호사가 "90% 이상 에이전트 판단에 동의" 피드백

Stage 3 — Auto Mode (제한적)
  - 저위험 계약(템플릿 기반) 자동 통과 → 변호사는 예외(고위험) 건만 검토
  - 성공 기준: 월 계약 80% 이상이 자동 처리되고, 자동 처리 건의 법적 이의 0%

Stage 4 — Full Delegation
  - 변호사는 예외 처리만 담당; 에이전트 정기 모니터링

Step 3 — Launch Sequence:

Phase 1 — Lighthouse (1개 고객)
  - 목표: 성공 사례 1개 확보 + Shadow Mode 검증
  - 기간: 1개월
  - 투자: 변호사 1명 24h + 온보딩 엔지니어 4주
  - KPI: 정확도 > 90%, 변호사 만족도 (NPS) > 60
  - 보상: 무료 또는 원가 ($2k)

Phase 2 — Wedge (10~15개 고객)
  - 목표: 반복 가능한 온보딩 프로세스 검증 + CAC < $50k
  - 기간: 3개월
  - 전략: Lighthouse 고객 레퍼런스 활용 + 세미나 2회 + 직영 영업
  - KPI: CAC payback < 6개월, NPS > 40, 체인 전환율 > 30%

Phase 3 — Expand (50+)
  - 목표: 인접 세그먼트(부동산팀, 조달팀) 확장
  - 전략: PLG (프리 트라이얼 2주) + 기존 고객 upsell (다국어, 맞춤 학습)
  - KPI: NRR > 120%

Step 4 — Pricing:

Outcome-based: "$월정액 + 절감액의 15% 수익공유"
  - 예: "월 $5k + (주 40시간 절감 × $150/시간 × 12개월의 15%) = $월 5k + $8,640"
  - 근거: 변호사가 실제 ROI를 직접 체험하므로 신뢰도 ↑; 우리 성과와 이해관계 일치

Positioning:
"대형 계약을 자주 처리하는 법무팀을 위한 AI 검토 에이전트로,
 계약 심사 시간을 80% 단축하면서도 법률 리스크는 변호사가 최종 관장하는 하이브리드 솔루션"
```

### Bad Example

```
❌ Beachhead 점수가 불충분:
[세그먼트] 소규모 스타트업 법무팀
  - Pain Intensity: 2 (계약이 적음; 변호사 1명이 주 5시간만 사용)
  - Trust AI: 1 ("AI는 믿을 수 없어")
  - Data: 1 (과거 계약서 10개만 있음)
  → 총 5/25 점수 → 비치헤드 부적합
  → "우리가 이 세그먼트부터 시작한다" 결정은 위험

❌ Trust Sequence가 너무 단순:
"프로덕션 배포하고 사용자 피드백 받자"
→ Shadow Mode, Co-pilot, Auto, Delegation의 4단계 구분 없음
→ 사용자가 처음부터 전적으로 에이전트를 신뢰해야 함 (높은 이탈율)
→ 단계별 신뢰 구축 필수: Shadow (1주) → Co-pilot (2주) → Auto (필요시)

❌ Launch Phase 목표가 불명확:
"여러 고객을 찾자"
→ "몇 개?" "어느 정도 규모?" "언제까지?"
→ 구체화 필수:
  Lighthouse: "1개 고객, 1개월 내 NPS > 50 달성"
  Wedge: "10개 고객, CAC payback < 6개월"
  Expand: "50개 이상"

❌ Positioning이 기술 중심:
"AI를 사용한 지능형 계약 검토 시스템"
→ 비즈니스 가치 부족
→ 재작성: "변호사 검토 시간을 80% 줄이면서 법적 리스크는 변호사가 통제하는 하이브리드 솔루션"
  (Pain, Solution, Benefit이 명확함)

❌ KPI가 기술 중심:
"정확도 95% 달성"
→ 하지만 변호사가 "NPS 30"이면 아무 소용 없음
→ 비즈니스 KPI 우선: "NPS > 60", "재사용률 > 80%", "변호사 만족도 > 4/5"
```

---

### 참고
- 설계자: AI PM Skills Contributors, 2026-03
- Geoffrey Moore, *Crossing the Chasm* — 비치헤드 전략 원전
- 에이전트 SaaS의 신뢰 구축 시퀀스: agent product onboarding 경험 기반

---

## Further Reading
- Geoffrey Moore, *Crossing the Chasm* — Technology adoption lifecycle and beachhead strategy
- Anthropic, "Building Effective Agents" (2024) — Agent deployment patterns and trust building

## Contextual Knowledge (auto-loaded)

> 보조 파일이 존재할 때만 자동 로드됩니다. 파일이 없으면 건너뜁니다.

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`

### Test Cases
!`cat references/test-cases.md 2>/dev/null || echo ""`

### Troubleshooting
!`cat references/troubleshooting.md 2>/dev/null || echo ""`
