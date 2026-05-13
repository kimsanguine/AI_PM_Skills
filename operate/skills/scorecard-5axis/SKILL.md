---
name: scorecard-5axis
description: "Score agents on a 5-axis weighted rubric — Accuracy, Reliability, Cost, Velocity, User Satisfaction — to produce a single comparable number per agent per period. Use when comparing N agents head-to-head, ranking weekly performance, or deciding which agent to invest in vs sunset. Pairs with operate/weekly-rollup for trend views."
argument-hint: "[agent or 'all']"
allowed-tools: ["Read", "Write", "Edit", "Bash"]
model: sonnet
---

## Core Goal

- 에이전트 성능을 **5축 가중 평가**로 단일 점수화한다.
- 축별 가중치를 사업 컨텍스트에 맞게 조정 가능하게 한다.
- 주차 간·에이전트 간 비교 가능한 결정론적 숫자를 만든다.

---

## 5개 축 (기본 가중치)

| 축 | 정의 | 측정 | 기본 가중치 |
|---|---|---|---|
| **Accuracy** | 출력이 사양을 충족하는가 | LLM-as-judge / 사람 평가 (0~100) | 25 |
| **Reliability** | 실행 성공률 + P95 latency | uptime % × latency 충족률 | 25 |
| **Cost** | 1회 실행 평균 비용 vs 목표 | (목표 / 실측) × 100, 상한 100 | 20 |
| **Velocity** | 호출 수 + TTV(time-to-value) | 정규화 호출 수 × TTV 충족 | 15 |
| **User Satisfaction** | 사용자 피드백 (좋아요/싫어요, NPS) | 정규화 점수 (0~100) | 15 |

> 합계 100. 가중치는 사업 컨텍스트에 맞게 재배분 가능.

---

## Trigger Gate

### Use This Skill When
- 5+ 에이전트를 헤드 투 헤드로 비교해야 할 때
- 주간/월간 운영 회의에서 단일 비교 가능한 점수가 필요할 때
- 어떤 에이전트에 추가 투자할지 결정할 때
- T5 sunset 후보를 객관 데이터로 가려낼 때

### Route to Other Skills When
- 단일 에이전트 KPI 정의가 우선이면 → `measure/kpi`
- 신뢰도 SLO 설계 → `measure/reliability`
- 비용만 보고 싶으면 → `measure/burn-rate`
- 포트폴리오 티어링이 우선이면 → `operate/agent-portfolio`

### Boundary Checks
- 이 스킬은 **상대 비교**용이다. 절대 품질 인증이 아니다.
- 가중치 조정 없이 디폴트 적용은 **3분 결정 한정**용. 본격 운영은 가중치 명시.

---

## Instructions

You are scoring agents for: **$ARGUMENTS**

**Step 1 — 가중치 결정**
- 디폴트 사용? 또는 사업 컨텍스트 맞춤?
- 맞춤이면 5개 축에 합 100 재분배
- 결정 근거 한 줄 기록

**Step 2 — 축별 점수 산출**
- 각 에이전트 × 5축 = 점수 25개 (5 에이전트 가정)
- 산출 방법은 결정론적으로 (LLM-as-judge는 동일 프롬프트·동일 평가셋)

**Step 3 — 가중 합산**
- 단일 점수 = Σ(축 점수 × 가중치) / 100
- 0~100 범위

**Step 4 — 비교 표 출력**
- 에이전트별 5축 점수 + 단일 점수
- 단일 점수 내림차순 정렬
- 전주 대비 ±N 표시

**Step 5 — 의사결정 권고**
- 점수 ≥ 80: 정상
- 60~79: 모니터링 강화
- < 60: 즉시 개선 또는 sunset 검토

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 가중치 합이 100이 아님 | Step 1 검증 | 자동 정규화 + 사용자 확인 요청 |
| 축별 측정 방법 불일치 | 같은 축인데 에이전트마다 다른 방식 | 측정 방법을 references/measurement-protocols.md에 고정 |
| Accuracy LLM-as-judge bias | 같은 모델로 자기 채점 | 채점 모델을 평가 대상과 다른 패밀리로 변경 |
| 비용 축 100점 만점인데 의미 없음 | 모든 에이전트가 비용 100 | 목표 비용을 더 타이트하게 재설정 |

---

## Quality Gate

- [ ] 가중치 합 = 100
- [ ] 5개 축 모두 측정 방법이 명시되었는가
- [ ] 단일 점수가 0~100 범위인가
- [ ] 전주 대비 변화량이 표시되었는가
- [ ] < 60 에이전트에 대한 권고가 있는가

---

## Examples

### Good Example
**입력:** "운영 중 에이전트 8개 이번 주 점수 비교. 비용 민감 사업이라 Cost 가중치 35로 올려줘."

**기대 출력:**
- 가중치: Accuracy 20 / Reliability 25 / Cost 35 / Velocity 10 / Satisfaction 10
- 표: 8개 에이전트 × 5축 + 단일 점수 + Δ주차
- 권고: cost-monitor 단일점수 56 → 즉시 개선 또는 sunset 검토

### Bad Example
**입력:** "에이전트들 점수 매겨봐."

**왜 나쁜가:**
- 가중치 의도 없음
- 측정 데이터 없음 → 환각 점수 위험

---

## Contextual Knowledge (auto-loaded)

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Measurement Protocols
!`cat references/measurement-protocols.md 2>/dev/null || echo ""`

### Weight Tuning
!`cat references/weight-tuning.md 2>/dev/null || echo ""`
