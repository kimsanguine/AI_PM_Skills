---
name: weekly-rollup
description: "Aggregate weekly performance across an agent portfolio — per-tier averages, week-over-week deltas, top movers and decliners, anomalies. Use at end of week to produce a single rollup brief for ops review. Pairs with operate/scorecard-5axis (input) and operate/agent-portfolio (context)."
argument-hint: "[week ID like 2026-W19]"
allowed-tools: ["Read", "Write", "Edit"]
model: sonnet
---

## Core Goal

- 한 주의 N개 에이전트 성과를 **단일 롤업 브리프**로 압축한다.
- 티어별 평균 + 전주 대비 Δ + 이상치 + Top 이동자(상승/하락 3개씩) 제공.
- 운영팀이 5분 안에 의사결정에 필요한 신호만 받게 한다.

---

## Trigger Gate

### Use This Skill When
- 매주 금요일 운영 리뷰 직전
- 월간 보고 데이터 빌드업
- 새 가중치/티어 적용 후 첫 주 검증

### Route to Other Skills When
- 입력 데이터(점수)가 없으면 → `operate/scorecard-5axis` 먼저
- 티어 미정 에이전트가 있으면 → `operate/agent-portfolio` 먼저
- 단일 에이전트 디테일이 필요하면 → `measure/kpi` / `measure/incident`

### Boundary Checks
- 이 스킬은 **요약**이다. 새로운 점수 계산은 하지 않는다.
- 입력은 scorecard-5axis의 주차별 산출물.

---

## Instructions

You are rolling up: **$ARGUMENTS** (예: `2026-W19`)

**Step 1 — 데이터 적재**
- 이번 주 + 전주 scorecard 결과 로드
- 누락 에이전트 있으면 표시

**Step 2 — 티어별 평균**
- T1~T5 각 티어 단일 점수 평균
- 전주 대비 Δ

**Step 3 — Top 이동자**
- 상승 Top-3 (Δ 양수, 절대값 큰 순)
- 하락 Top-3 (Δ 음수, 절대값 큰 순)

**Step 4 — 이상치 탐지**
- 단일 점수 < 60 에이전트 명단
- 한 축이 30 이상 떨어진 에이전트 명단

**Step 5 — 브리프 출력**
- 4~6줄 요약
- 운영 주의 권고 1~3개

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 입력 데이터 없음 | scorecard 산출물 부재 | scorecard-5axis 먼저 실행 안내 |
| 전주 데이터 없음 (첫 주) | Δ 계산 불가 | "베이스라인 주" 표시 + 다음 주부터 Δ 시작 |
| Top 이동자가 같은 팀에 몰림 | 한 팀에서 3개 이상 | 팀 차원 이슈 의심 → cross-team-routing 점검 |
| 이상치 0건인데 단일 점수 낮음 | 평균은 낮은데 < 60 없음 | 측정 단위 오류 가능 — scorecard 재검토 |

---

## Quality Gate

- [ ] 모든 활성 에이전트가 롤업에 포함되었는가
- [ ] 티어별 평균 Δ가 표시되었는가
- [ ] Top 이동자 상승·하락 각 ≤3개 명시
- [ ] 이상치 명단이 표시되었는가
- [ ] 운영 권고가 1~3개로 압축되었는가

---

## Examples

### Good Example
**입력:** "2026-W19 롤업 만들어줘. 지난 주 데이터 있고 이번 주 scorecard 완료됐어."

**기대 출력:**
```
주차: 2026-W19 (N agents — 예시 수치)

티어 평균:
  T1 84.2 (Δ +1.5)
  T2 76.1 (Δ -2.3)
  T3 71.4 (Δ +0.8)
  T4 68.0 (Δ -5.0)
  T5 — (sunset 1건)

Top 상승: daily-brief +12, cost-guard +9, weekly-recap +7
Top 하락: copywriter-exp -18, mail-router -11, news-curator -8

이상치 (< 60): copywriter-exp(54)
이상치 (한 축 ≥30 하락): mail-router(reliability -34)

운영 권고:
1. mail-router reliability 즉시 진단 (T2)
2. copywriter-exp 4주차인데 평균↓ → 승격 보류 검토
3. T2 평균 -2.3 → cost-guard 외 다른 T2 점검
```

### Bad Example
**입력:** "이번 주 어땠어?"

**왜 나쁜가:**
- 주차 ID 없음
- 입력 데이터 명시 없음 → 환각 위험

---

## Contextual Knowledge (auto-loaded)

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`
