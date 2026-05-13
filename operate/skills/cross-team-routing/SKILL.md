---
name: cross-team-routing
description: "Decide which agent should handle an incoming request across multiple teams — based on tier, capability map, current load, and inter-team handoff cost. Use when a request could plausibly be served by 2+ agents from different teams, when load-balancing across an agent fleet, or when introducing a new agent and deciding which team's traffic it absorbs."
argument-hint: "[request type or 'all']"
allowed-tools: ["Read", "Write", "Edit"]
model: sonnet
---

## Core Goal

- 들어온 요청을 N개 팀 × M개 에이전트 중 **단일 라우팅 결정**으로 보낸다.
- 라우팅 기준은 (1) capability fit, (2) 현재 부하, (3) 티어 우선순위, (4) handoff 비용.
- 라우팅 의사결정 로그를 남겨 사후 audit 가능하게 한다.

---

## Trigger Gate

### Use This Skill When
- 2개 이상 팀의 에이전트가 같은 요청을 처리 가능할 때
- 신규 에이전트 도입 후 트래픽 흡수 정책 결정
- 한 팀에 부하가 몰려 다른 팀으로 분산 필요
- 라우팅 정책 변경 회고 (지난 N주 결정 audit)

### Route to Other Skills When
- 단일 에이전트 capability 정의는 → `deliver/instruction`
- 라우팅 패턴(architecture) 자체는 → `architect/orchestration`
- 운영 부하 평가는 → `operate/weekly-rollup`
- 의사결정 자체 평가는 → `hplan/decision-log`

### Boundary Checks
- 이 스킬은 **운영 라우팅**이다. 아키텍처 설계(`architect/orchestration`)와 다르다.
- 한 팀 내 에이전트 선택은 범위 밖 — 팀 내부 라우터 책임.

---

## Instructions

You are routing: **$ARGUMENTS** (예: "고객 환불 문의")

**Step 1 — capability map 조회**
- 후보 에이전트 N개 나열 (capability 충족 여부)
- 충족 안 하면 즉시 탈락

**Step 2 — 부하 / 티어 우선순위**
- 후보별 현재 부하 (이번 주 호출 수 / capacity)
- 티어 (T1 우선, T5 최저)
- handoff 비용 (요청 출처팀 ↔ 처리팀이 같으면 0, 다르면 +코스트)

**Step 3 — 라우팅 점수 계산**
```
score = capability_fit * 50
      + (1 - load) * 30
      + tier_weight * 15
      - handoff_cost * 5
```
- capability_fit: 0~1
- load: 0~1 (1이 풀 부하)
- tier_weight: T1=1.0, T2=0.8, T3=0.6, T4=0.4, T5=0.2
- handoff_cost: 0(같은 팀), 0.5(인접팀), 1(원격)

**Step 4 — 결정 + 로그**
- 단일 라우팅 대상 결정
- 결정 근거 1줄 + 점수 표

**Step 5 — 사후 audit 훅**
- N주 후: 이 라우팅이 실제로 정답이었나? (실패율, 응답시간, 사용자 만족)

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| 후보 에이전트 0건 | capability map 미스 | 신규 에이전트 필요 → `discover` 플러그인 |
| 동점이 발생 | 동일 점수 2개 | 티어 우선 → 더 낮은 티어 → 더 낮은 부하 순 tie-break |
| handoff_cost 정의 불가 | 팀 인접도 데이터 없음 | 디폴트 0.5 적용 + references/team-adjacency.md 갱신 권고 |
| 매주 같은 에이전트만 선택됨 | 부하 한쪽 쏠림 | capacity 재조정 또는 부하 가중치 +10 |

---

## Quality Gate

- [ ] 단일 라우팅 결정이 명시되었는가
- [ ] 4개 입력(capability, load, tier, handoff) 모두 점수화되었는가
- [ ] 결정 근거가 한 줄로 명시되었는가
- [ ] 사후 audit 일정이 명시되었는가
- [ ] 동점 발생 시 tie-break 규칙이 적용되었는가

---

## Examples

### Good Example
**입력:** "환불 문의가 들어왔는데 응대1차(T1) / 환불전담(T2) / 백오피스(T3) 모두 capability 있어. 라우팅해줘."

**기대 출력:**
```
후보:                응대1차(T1)  환불전담(T2)  백오피스(T3)
capability_fit:      0.7          1.0           0.8
load:                0.85         0.40          0.20
tier_weight:         1.0          0.8           0.6
handoff_cost:        0            0             0.5

score = 50*fit + 30*(1-load) + 15*tier - 5*handoff
응대1차:    35 + 4.5 + 15 + 0  = 54.5
환불전담:   50 + 18 + 12 + 0   = 80.0  ← 선택
백오피스:   40 + 24 + 9 - 2.5  = 70.5

결정: 환불전담(T2) — capability 1.0 + 부하 여유 + 같은 팀
사후 audit: 2026-W21 회고에서 실패율 확인
```

### Bad Example
**입력:** "환불 문의 누가 받지?"

**왜 나쁜가:**
- 후보 명단 없음
- 부하/티어 데이터 없음 → 환각 결정 위험

---

## Contextual Knowledge (auto-loaded)

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Team Adjacency
!`cat references/team-adjacency.md 2>/dev/null || echo ""`
