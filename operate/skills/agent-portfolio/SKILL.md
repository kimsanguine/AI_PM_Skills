---
name: agent-portfolio
description: "Design and maintain a multi-agent portfolio dashboard — tier agents (T1~T5) by business criticality, track health across N agents, and prioritize ops attention by tier × incident weight. Use when running 5+ agents in production, when a single-agent KPI view (measure plugin) loses signal across teams, or when an exec asks 'which agents matter most this week?'."
argument-hint: "[portfolio name or 'all']"
allowed-tools: ["Read", "Write", "Edit"]
model: sonnet
---

## Core Goal

- N개 에이전트를 사업 임팩트·신뢰성·운영 비용 기준으로 **T1~T5 5단계 티어링**한다.
- 티어 × 인시던트 가중치로 운영 주의력을 분배해 "어디부터 손볼지" 결정한다.
- 한 화면에서 포트폴리오 헬스를 본다 (총 N개, 활성 비율, T1 우선순위 리스트).

---

## Trigger Gate

### Use This Skill When
- 운영 중인 에이전트가 5개를 넘어서 단일 에이전트 KPI 뷰로는 우선순위가 안 보일 때
- 새 에이전트를 포트폴리오에 편입할 때 (티어 부여 필수)
- 분기/월간 포트폴리오 리뷰 미팅 준비할 때
- 예산 삭감 요구가 와서 어떤 에이전트를 sunset 할지 결정할 때

### Route to Other Skills When
- 개별 에이전트 KPI 정의가 우선이면 → `measure/kpi`
- 에이전트별 신뢰도 SLO 설계는 → `measure/reliability`
- 5축 가중 평가가 필요하면 → `operate/scorecard-5axis`
- 주차별 합산/트렌드 뷰가 필요하면 → `operate/weekly-rollup`
- 에이전트 ↔ 에이전트 라우팅 결정은 → `operate/cross-team-routing`

### Boundary Checks
- 이 스킬은 **포트폴리오 메타 뷰**이지 개별 에이전트 진단이 아니다.
- 에이전트 수 < 5면 과중 — measure/kpi로 충분하다.
- 티어링은 **사업 영향**을 기준으로 한다. "내가 좋아하는 에이전트"가 아니다.

---

## Tier 정의 (T1~T5)

| 티어 | 정의 | 운영 주의력 | 예시 |
|---|---|---|---|
| **T1** | 사업 핵심·실시간·고객 직접 노출 | 24/7 모니터, 인시던트 즉시 대응 | 결제 라우터, 고객 응대 1차 |
| **T2** | 사업 중요·매일 실행·내부 의존 | 매일 헬스체크, 4시간 SLA | 데일리 브리핑, 비용 모니터 |
| **T3** | 운영 효율·주기적·내부용 | 주 1회 리뷰 | 주간 회고, 콘텐츠 큐레이션 |
| **T4** | 실험·신규·검증 단계 | 격주 리뷰 + 자체 평가 | 신규 카피라이팅 에이전트 |
| **T5** | 레거시·sunset 후보 | 월 1회 점검, 삭제 후보군 | 사용 빈도 < 월 1회 |

---

## Instructions

You are designing a portfolio view for: **$ARGUMENTS**

**Step 1 — 인벤토리**
- 운영 중 에이전트 전수 목록화 (이름, 담당팀, 활성 여부, 마지막 실행일)
- 각 에이전트의 1줄 정의 + Primary Goal

**Step 2 — 티어 부여**
- 각 에이전트를 T1~T5 중 하나로 배정
- **근거 한 줄 명시** (사업 영향, 호출 빈도, 의존도)

**Step 3 — 운영 주의력 분배**
- T1 합산 % / T2 합산 % / ... 백분율 계산
- 권장 균형: T1 ≤ 20%, T2 30~40%, T3 30~40%, T4~T5 ≤ 15%
- 균형 벗어나면 조정 권고

**Step 4 — 헬스 시그널**
- 각 에이전트의 마지막 인시던트 / 비용 / 호출 수 요약
- 티어 가중치 × 인시던트 = 우선순위 점수

**Step 5 — 출력**
- 포트폴리오 헬스 표 (티어별 그룹화)
- 이번 주 운영 주의 권고 Top-3

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 티어 부여 근거가 추상적 ("중요해서 T1") | Step 2 출력 점검 | 사업 영향 수치(매출/비용/사용자 수)로 재정의 |
| T1이 50% 초과 | Step 3 백분율 점검 | 진짜 T1인지 재검토 — 통상 T1은 ≤ 20% |
| 새 에이전트 추가 시 티어 누락 | 인벤토리 vs 티어 갭 발견 | 추가 시점에 티어 부여 강제 (체크리스트) |
| sunset 후보가 T5에 안 모임 | T5가 비어있음 | 사용 빈도 < 월 1회인 에이전트 명시 → T5 분류 |

---

## Quality Gate

- [ ] 모든 활성 에이전트가 정확히 한 티어에 속하는가
- [ ] 각 티어 부여 근거가 수치 기반인가
- [ ] T1 비율이 ≤ 20%인가
- [ ] 운영 주의 권고 Top-3가 명시되었는가
- [ ] 다음 리뷰 일정이 명시되었는가

---

## Examples

### Good Example
**입력:** "운영 중인 에이전트 N개, 여러 팀. 분기 리뷰용 포트폴리오 뷰 만들어줘."

**기대 출력 (예시 수치):**
- T1: 4개 (18%) — 결제, 응대 1차, 인시던트 라우터, 비용 가드
- T2: 8개 (36%) — 데일리 브리핑, 주간 회고 등
- T3: 7개 (32%) — 콘텐츠 큐레이션, 리뷰 봇 등
- T4: 2개 (9%) — 신규 카피라이팅(2주 운영), 신규 분석
- T5: 1개 (5%) — sunset 검토: legacy-summarizer (월 0회 실행)

운영 주의 Top-3:
1. T1 응대 1차 — 어제 P99 latency 2배 증가, 즉시 조사
2. T2 데일리 브리핑 — 3일 연속 실패, SLA 임박
3. T5 legacy-summarizer — sunset 결정 필요

### Bad Example
**입력:** "에이전트들 어떻게 운영 중인지 알려줘."

**왜 나쁜가:**
- 운영 중 에이전트 인벤토리 없음 → 답변 불가
- 어떤 척도로 비교할지 명세 없음

---

## Contextual Knowledge (auto-loaded)

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`

### Tier Definitions
!`cat references/tier-definitions.md 2>/dev/null || echo ""`
