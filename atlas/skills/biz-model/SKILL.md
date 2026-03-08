---
name: biz-model
description: "Design a sustainable business model for AI agent products — pricing strategy (per-use, subscription, outcome-based), cost structure, unit economics, and value capture. Use when planning agent monetization, evaluating pricing models, or building a business case for agent development."
argument-hint: "[agent product to model]"
allowed-tools: ["Read", "Write", "WebSearch", "WebFetch"]
model: sonnet
---

# Agent Business Model

> AI 에이전트 제품의 비즈니스 모델 설계

## Core Goal

- 가치 창출(사용자가 얻는 절감액/개선도)과 가치 포획(수익 모델) 사이의 균형을 설정하여 지속 가능한 비즈니스 구조 설계
- 에이전트의 변수 비용(LLM API, 인프라) 구조를 이해하고 목표 이윤률(Gross Margin >70%)을 달성 가능한 가격 전략 수립
- 각 가격 모델(사용 기반, 구독, 성과 기반)의 장단점을 평가하여 제품과 고객 특성에 최적 모델 선택

## Trigger Gate

### Use This Skill When

- 새로운 에이전트 제품 출시를 위해 가격 전략을 수립하는 경우
- 기존 에이전트의 수익성을 개선하거나 가격을 조정해야 하는 상황
- VC 피칭, 비즈니스 케이스 작성, 또는 고객 구매 의사 결정 근거 제시

### Route to Other Skills When

- 데이터 누적을 통한 경쟁 우위 분석 → growth-loop (그로스 루프 설계)
- 시장 지속 가능성 평가 → moat (해자 분석)
- 제품 출시 전략과 GTM → oracle의 agent-gtm 또는 forge의 prd
- 비용 추적 및 실제 운영 메트릭 모니터링 → argus의 burn-rate

### Boundary Checks

- 아직 제품 MVP가 없거나 고객 가치가 검증 안 됨 → growth-loop 먼저 설계, 가치 입증 후 모델링
- 가격 책정 전에 실제 고객이 얼마나 절감하는지 조사하지 않은 상태 → 추측 기반 모델이 됨, 고객 인터뷰 필수
- 경쟁 제품 가격을 모르는 상태에서 가격 결정 → 시장 조사 먼저 수행

## 개념

에이전트 제품은 전통적 SaaS와 다른 비용 구조(사용량 기반)를 가진다. 가치 창출(value creation)과 가치 포획(value capture)을 분리해서 설계해야 한다.

## Instructions

You are designing a **business model** for an AI agent product: **$ARGUMENTS**

### Step 1 — Value Creation Analysis

Define the value the agent creates:
```
Time Saved: [hours/week] × [hourly cost] = [$/week]
Error Reduction: [error rate before] → [after] × [cost per error]
New Capability: [what was impossible before]
Scale Factor: [1 person can now do X people's work]
```

### Step 2 — Cost Structure

Map the variable cost elements:
| Cost Element | Unit | Estimated Cost | Scaling Behavior |
|-------------|------|----------------|-----------------|
| LLM API calls | per execution | $ | Linear with usage |
| External APIs | per call | $ | Linear |
| Compute/hosting | per month | $ | Step function |
| Human review | per edge case | $ | Decreasing over time |
| Data storage | per GB/month | $ | Linear |

**Key Metric**: Cost Per Execution (CPE) = Total cost ÷ Number of executions

### Step 3 — Pricing Model Selection

| Model | Best When | Risk |
|-------|-----------|------|
| **Per-execution** | Clear, countable outputs | Usage anxiety |
| **Tiered subscription** | Predictable usage patterns | Over/under provisioning |
| **Outcome-based** | Measurable business outcome | Attribution difficulty |
| **Seat-based + usage** | Team tool with variable intensity | Complexity |
| **Freemium** | Network effects, viral potential | Conversion rate |

### Step 4 — Unit Economics

Calculate the fundamental economics:
```
Revenue per Customer (monthly): $___
Cost per Customer (monthly):
  - LLM costs: $___
  - Infrastructure: $___
  - Support: $___
  - CAC amortized: $___
Gross Margin: ___%
Target Gross Margin: >70% (SaaS standard)
```

### Step 5 — Value Capture Strategy

Answer: "How much of the value created can you capture?"
- **Rule of thumb**: Charge 10-20% of value created
- **Anchor**: Compare to the cost of the human equivalent
- **Ceiling**: What alternatives exist? (competing agents, manual process, outsourcing)

### Step 6 — Moat Assessment

How defensible is this business model?
- Data moat: Does usage improve the product?
- Switching cost: How hard is it to leave?
- Network effect: Does more users = more value?
- See: `/agent-moat` for detailed moat analysis

### Output Format

Present as a Business Model Canvas adapted for agents:
```
┌─────────────────────────────────────────┐
│ Value Proposition: [what + for whom]     │
├──────────────┬──────────────────────────┤
│ Cost Structure│ Revenue Model            │
│ CPE: $___    │ Pricing: ___             │
│ Fixed: $___  │ Target ACV: $___         │
│ Margin: ___%  │ Payback: ___ months      │
└──────────────┴──────────────────────────┘
```

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---------|-----|-----|
| 가격 대비 가치가 명확하지 않음 | 고객이 구매 가치 설명 이해 못함, 전환율 <5% | 고객 인터뷰 재실시, 실제 절감 금액 재계산, 가치 전 조정 또는 가격 인하 |
| CPE(Cost Per Execution)가 목표 이윤율을 초과 | 수익성 분석 결과 Gross Margin <50% | API 비용 최적화(모델 라우팅), 배치 처리 도입, 또는 가격 인상(고객 반발 가능성 검토) |
| 가격 모델이 고객 사용 패턴과 맞지 않음 | 고객 이탈 증가, 월 사용량 편차 큼 | 하이브리드 모델 도입(구독 + 사용량), 또는 다른 가격 모델로 전환 |
| 경쟁사가 대폭 낮은 가격 제시 | 시장 가격 급락 또는 새 경쟁자 출현 | 원가 구조 재최적화, 또는 가치 차별화 강화 (moat 스킬 활용) |

## Quality Gate

- [ ] 가치 창출 계산: 시간 절감, 에러 감소, 새로운 능력 등 3가지 이상 정량화 (Yes/No)
- [ ] 비용 구조: CPE(Cost Per Execution) 계산 및 각 비용 요소 근거 명확 (Yes/No)
- [ ] 가격 모델 선택: 3개 이상 가격 모델 검토 후 선택 근거 문서화 (Yes/No)
- [ ] 이윤율 검증: 목표 Gross Margin >70% 달성 가능 확인 (Yes/No)
- [ ] 고객 검증: 실제 또는 예상 고객 2명 이상과 가격 타당성 확인 (Yes/No)

## Examples

### Good Example

```
에이전트 제품: "고객 서비스 자동화 챗봇"

[가치 창출]
- 고객 상담사 1명이 월 160시간 근무
- 챗봇 도입으로 상담사가 40% 시간 절감 = 64시간/월
- 한국 상담사 평균 시급 15,000원
- 월간 가치 창출: 64시간 × 15,000원 = 960,000원

[비용 구조]
- LLM API 비용: 상담 1건당 $0.05 (Claude 3.5 Sonnet 사용)
- 월간 상담 2,000건 = $100
- 인프라: $500/월
- 지원: $200/월
- CPE: $100 ÷ 2,000 = $0.05/건

[가격 모델]
선택: 하이브리드 (월정액 + 초과분 사용료)
- 기본: $500/월 (상담 1,500건 포함)
- 초과: $0.20/건

[이윤율]
- 고객당 월 수익: $500 + (평균 초과 500건 × $0.20) = $600
- 고객당 월 비용: $100 + $500 + $200 = $800
- 음수? → 비용 최적화 필요
  → 인프라 $200으로 축소
  → 지원 자동화로 $50으로 축소
  → 수정 후: $100 + $200 + $50 = $350
- Gross Margin: ($600 - $350) ÷ $600 = 42% (목표 미달)
  → 가격 인상: $800/월로 조정 → 53% Margin

[가치 포획]
- 월간 절감액 $960,000 중 0.08%만 청구
- 고객에게는 여전히 매력적 (ROI 160배)
```

### Bad Example

```
반사례 1: 가치 계산 없는 가격 책정
- "경쟁사가 $500/월이니까 우리도 $500/월"
- 실제 고객 절감액을 모른 상태에서 가격 결정
- 결과: 너무 비싸거나 너무 저가 정책

반사례 2: 비용 구조 미검토
- CPE 계산 없이 "구독 $100/월로 충분하겠지" 예상
- API 호출량이 예상보다 10배 증가
- 결과: 심각한 적자 운영

반사례 3: 고객 이질성 무시
- 모든 고객을 일률적으로 $X/월
- 스타트업은 월 100건, 대기업은 50,000건 사용
- 결과: 스타트업은 과다 지불, 대기업은 저가격 이탈 유도
```

---

## Further Reading
- Alexander Osterwalder, *Business Model Generation* — Business Model Canvas
- Ash Maurya, *Running Lean* — Lean Canvas for startups

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
