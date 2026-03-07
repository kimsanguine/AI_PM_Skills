---
name: router
description: "Design a model routing strategy that selects the right LLM for each task type. Balance cost, latency, and quality tradeoffs across models. Use when building agents that call multiple LLMs, optimizing token costs by routing simple tasks to cheaper models, or designing fallback chains."
argument-hint: "[agent system for routing]"
allowed-tools: ["Read", "Write", "WebSearch", "WebFetch"]
model: sonnet
---

# Model Router

> 작업별 최적 LLM 선택 전략 설계

## Core Goal

- 작업 복잡도에 따라 T1(저비용 경량) ~ T4(고성능 전문) 모델을 선택하여 비용 40-80% 절감하면서 품질 유지 (>90%)
- 각 모델의 성능 경계(threshold)를 파악하여 라우팅 규칙을 데이터 기반으로 수립하고 지속적으로 최적화
- 모델 실패 시 자동 폴백(fallback) 전략으로 안정성 확보

## Trigger Gate

### Use This Skill When

- 여러 모델을 쓰는 에이전트 시스템의 비용 최적화 필요
- 간단한 작업에 비싼 모델을 쓰고 있는 경우
- 성능과 비용의 트레이드오프를 의도적으로 설정해야 하는 경우

### Route to Other Skills When

- 작업 분류 로직을 복잡하게 해야 하면 → orchestration (라우터 패턴)
- 라우팅 결과의 비용 영향 분석 → biz-model (단위 경제)
- 라우팅 결정이 품질에 미치는 영향 추적 → argus의 kpi (메트릭 정의)
- 모델 선택이 아니라 에이전트 선택 → orchestration의 Router 패턴

### Boundary Checks

- 단일 모델만 사용하는 경우 → 라우팅 불필요
- 모든 작업이 고복잡도면 → T3 고정, 라우팅 복잡도보다 이득 적음
- 라우팅 오버헤드가 큼 (라우팅 비용 > 저가 모델 절감) → 라우팅 건너뛰기

## 개념

모든 작업에 최고 성능 모델을 사용하는 것은 비용 낭비다. 작업 복잡도에 따라 적절한 모델을 라우팅하면 비용을 50-80% 절감하면서 품질을 유지할 수 있다.

## Instructions

You are designing a **model routing strategy** for: **$ARGUMENTS**

### Step 1 — Task Classification

Classify each agent task by complexity:

| Tier | Complexity | Examples | Recommended Model Class |
|------|-----------|----------|----------------------|
| T1 | Simple extraction | Data parsing, formatting, classification | Small/Fast (Haiku, GPT-4o-mini) |
| T2 | Standard reasoning | Summarization, comparison, basic analysis | Mid (Sonnet, GPT-4o) |
| T3 | Complex reasoning | Strategy, creative, multi-step analysis | Large (Opus, o1) |
| T4 | Specialized | Code generation, math, domain-specific | Specialist (Claude Code, Codex) |

### Step 2 — Routing Decision Matrix

For each task in your agent workflow:
```
Task: [name]
├── Input complexity: Low / Medium / High
├── Output quality sensitivity: Low / Medium / High
├── Latency requirement: <1s / <5s / <30s / Flexible
├── Cost tolerance: $ / $$ / $$$
└── Recommended tier: T1 / T2 / T3 / T4
```

### Step 3 — Cost Comparison

Calculate cost impact of routing vs single-model:

| Approach | Monthly Cost | Quality Score |
|----------|-------------|---------------|
| All T3 (premium) | $____ | 95/100 |
| Routed (mixed) | $____ | 92/100 |
| All T1 (budget) | $____ | 70/100 |

**Target**: Routed approach should achieve >90% quality at <40% of premium cost

### Step 4 — Fallback Strategy

Design graceful degradation:
```
Primary: [preferred model]
  ↓ if failed/timeout
Fallback 1: [alternative model]
  ↓ if failed/timeout
Fallback 2: [minimum viable model]
  ↓ if all fail
Error: [return structured error to user]
```

### Step 5 — Quality Gate

For critical tasks, add a quality verification step:
- Run T1 model first for speed
- Check output confidence/quality score
- If below threshold → re-run with T2 or T3
- Log upgrade frequency to optimize routing rules

### Step 6 — Monitoring Plan

Track these metrics weekly:
- Cost per model tier
- Routing accuracy (was the right tier selected?)
- Fallback trigger frequency
- Quality score by tier

### Output

Present the routing table:
```
┌─────────────┬──────┬──────────┬───────┐
│ Task         │ Tier │ Model    │ $/run │
├─────────────┼──────┼──────────┼───────┤
│ [task 1]    │ T1   │ [model]  │ $0.01 │
│ [task 2]    │ T2   │ [model]  │ $0.05 │
│ [task 3]    │ T3   │ [model]  │ $0.15 │
└─────────────┴──────┴──────────┴───────┘
Monthly estimate: $____
vs all-premium: $____ (___% savings)
```

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---------|-----|-----|
| 라우팅 오분류: T1 모델이 충분하지 않은 작업으로 갈당 | 출력 품질 점수 <70%, 사용자 피드백 "부정확함" | 폴백: 즉시 T2로 재실행, 라우팅 규칙 업데이트 |
| 비용 절감 목표 미달: 예상보다 고비용 모델 호출 비율 높음 | 실제 T1 사용률 10% (예상 50%) | 라우팅 기준 재설정 (threshold 낮춤), 또는 T1 능력 강화 |
| 모델 API 장애: T2 모델 다운 | T2 호출 timeout | 폴백 1: T3로 재시도, 폴백 2 실패 시: T2 사용 불가 상태 사용자 보고 |
| 품질-비용 균형 붕괴: 비용은 줄었으나 품질 <80% | 전월 만족도 95% → 이번달 82% | 라우팅 회귀, 더 높은 티어로 보수적 조정 |

## Quality Gate

- [ ] 작업 분류: T1-T4 기준을 명확히 정의하고 각 작업을 분류 (Yes/No)
- [ ] 라우팅 결정 매트릭스: 최소 5개 작업의 라우팅 결정 정당화 (Yes/No)
- [ ] 비용 비교: "모두 T3" vs "라우팅" 비용 계산 및 절감율 (___%)
- [ ] 폴백 전략: Primary → Fallback 1 → Fallback 2 체인 정의 (Yes/No)
- [ ] 품질 게이트: 최종 품질 점수 ≥ 90% 목표 및 추적 방법 (Yes/No)

## Examples

### Good Example

```
시스템: "고객 지원 챗봇"

[작업 분류]
- T1 (간단): 상태 조회, 영수증 검색, FAQ 찾기, 형식 변환
  모델: Claude 3.5 Haiku ($0.80/M input)
  특징: 구조화된 데이터, 명확한 기준

- T2 (표준): 문제 진단, 기본 문제 해결, 요약, 이메일 작성
  모델: Claude 3.5 Sonnet ($3/M input)
  특징: 추론 필요, 약간의 창의성

- T3 (복잡): 전략적 조언, 복잡한 분석, 분쟁 중재
  모델: Claude Opus 4.6 ($15/M input)
  특징: 고수준 사고, 미묘한 판단

[라우팅 결정 매트릭스]
Task: "고객이 결제 실패, 무엇인가?"
├── Input complexity: Low
├── Output sensitivity: Medium (고객 만족도 영향)
├── Latency: <2초 (채팅)
├── Cost tolerance: Low
→ T1로 시작 (상태 조회), 필요시 T2 (진단)

Task: "고객 불만 처리 계획"
├── Input: "이 고객은 지난 3개월 5건 환불 신청..."
├── Output sensitivity: High (고객 이탈 방지)
├── Latency: <10초 (시간 여유)
├── Cost tolerance: Medium
→ T3 필수 (복잡한 판단)

[비용 비교]
월간 1,000 작업:
- 600 × T1 (상태/검색): 600 × $0.001 = $0.60
- 300 × T2 (진단/작성): 300 × $0.003 = $0.90
- 100 × T3 (전략): 100 × $0.015 = $1.50
라우팅 합계: $3.00

vs 모두 T2: 1,000 × $0.003 = $3.00 (동일)
vs 모두 T3: 1,000 × $0.015 = $15.00 (5배 비쌈)

→ T2 기준으로는 라우팅 득실 없으나, T3 회피로 지속성 확보

[폴백 전략]
Primary: 라우팅된 모델
  ↓ timeout (3초) or quality score <75%
Fallback 1: 한 등급 높은 모델
  ↓ timeout or quality <75%
Fallback 2: T3 (최고 성능)
  ↓ 모두 실패
Error: 사용자에게 "다시 시도" 요청

[모니터링]
주 1회:
- 각 T별 호출 수 및 비용
- 품질 점수 분포 (T1 평균 82%, T2 92%, T3 96%)
- 폴백 발동 빈도 (<5%)
- 사용자 만족도 추이
```

### Bad Example

```
반사례 1: 무분별한 T1 라우팅
"거의 모든 작업을 T1로"
- 실제로는 많은 작업이 T1 능력 부족
- 품질 점수: 65% (목표 90% 미달)
- 폴백 발동 50% (수익 1.5배, 신뢰도 하락)

반사례 2: 라우팅 규칙이 애매함
"복잡도에 따라 선택" (정의 없음)
- 동일한 작업도 때마다 다른 모델로
- 예측 불가능, 비용 제어 불가

반사례 3: 폴백 없음
"T1으로 했는데 실패하면 그냥 오류"
- 안정성 문제
- 사용자 이탈

반사례 4: 라우팅 비용이 절감보다 큼
"T1 선택 여부를 판단하는 라우터를 T3 모델로 실행"
- 라우터 비용: $0.015
- T1 절감: $0.001
- 순손실: $0.014/요청
```

---

## Further Reading
- Anthropic Model Comparison — https://docs.anthropic.com/en/docs/about-claude/models
- OpenAI Model Overview — Model selection for different tasks
