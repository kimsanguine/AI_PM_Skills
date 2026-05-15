---
name: pmf-gate
description: "PMF Gate — post-launch measurement loop that converts operational data (COGS sentinel results + behavioral metrics) into Evidence Gate inputs for the next build cycle. Closes the hplan loop: Evidence → Product → Build → [ship] → PMF → Evidence (next)."
---

# PMF Gate (스케치)

> **상태**: 스케치 — cogs_sentinel.py 출력 형식 표준화 완료 후 정식 스킬로 승격.
> Habix Legal 기준 트리거: W6 베타 측정 시점.

## 역할

```text
Evidence Gate → Product Gate → Build Gate → [출시]
     ↑                                           |
     └─────────── PMF Gate ◄────────────────────┘
```

PMF Gate는 운영 데이터를 다음 Evidence Gate의 인풋 형식으로 변환합니다.
"우리가 만든 것을 계속 만들어야 하는가"를 데이터로 답합니다.

## 트리거 기준

PMF Gate는 아래 조건 중 하나가 충족될 때 실행합니다:

| 트리거 | 기준 |
|--------|------|
| 시간 기준 | 베타 출시 후 N일 (PROGRESS.md에 명시된 Wx 마감) |
| 사용자 기준 | 유료 사용자 M명 도달 또는 베타 사용자 K명 N주 연속 사용 |
| COGS 기준 | 실측 p90 margin이 sentinel 예측과 ±15%p 이상 차이 |
| 명시 기준 | `harness/STATE.md`의 "다음 진입 조건" 항목 충족 |

**기본값 (프로젝트별로 PROGRESS.md에 오버라이드)**:
- 시간: 베타 출시 후 30일
- 사용자: 유료 전환 10명 또는 베타 30일 이상 재방문

## 실행 절차

### Step 1 — COGS 실측

```bash
python3 hplan/scripts/cogs_sentinel.py --mode realtime \
  --provider [현재 provider] \
  --model [현재 model]
```

`cogs_sentinel.py`가 이미 존재합니다. 실측 호출 데이터(calls/user/month 실제값)를 주입하면 재계산됩니다.

출력 비교:
- Build Gate 예측 p90 margin
- 실측 p90 margin
- 차이 ±Xp%

### Step 2 — 행동 지표 수집

아래 질문에 대한 데이터를 수집합니다:

```yaml
retention:
  day_7: [%]     # 7일 후 재방문율
  day_30: [%]    # 30일 후 재방문율
engagement:
  core_flow_completion: [%]   # 핵심 플로우 완료율
  workaround_reduction: [%]   # "이전에 수동으로 했던 것"을 대체한 비율
revenue:
  paid_conversion: [%]        # 유료 전환율
  churn_30d: [%]              # 30일 이탈율
signal:
  strong_push_quotes: [N]     # "없으면 못 살아" 수준의 인용 건수
  nps_qualitative: [한 줄]    # 가장 자주 나온 추천 이유
```

### Step 3 — PMF 판정

| 조건 | 판정 |
|------|------|
| Day-30 retention ≥ 30% + COGS GREEN + strong_push ≥ 3 | **PMF_SIGNAL** — 다음 사이클 GO |
| COGS 실측 p90 < 20% | **ECONOMICS_MISS** — pricing 재조정 후 재검토 |
| Day-7 retention < 20% | **RETENTION_MISS** — core flow 재설계 필요 |
| Strong-push < 3 | **EVIDENCE_THIN** — 더 많은 인터뷰 필요 |
| 위 조건 복합 | **PIVOT** → hplan Evidence Gate 재시작 |

### Step 4 — 다음 Evidence Gate 인풋 생성

PMF Gate 결과를 `harness/pmf-output.yaml`로 저장:

```yaml
pmf_date: YYYY-MM-DD
verdict: PMF_SIGNAL | ECONOMICS_MISS | RETENTION_MISS | PIVOT
cogs_realtime:
  p50_margin: [%]
  p90_margin: [%]
  delta_from_prediction: [±pp]
behavior:
  day_30_retention: [%]
  core_flow_completion: [%]
  strong_push_quotes: [N]
next_gate:
  action: continue | reprice | redesign | pivot
  evidence_carry_over:
    # 다음 Evidence Gate에 그대로 들어가는 검증된 신호
    - [인용 또는 데이터 포인트]
  new_hypotheses:
    # 이번 운영에서 새로 발견된 가설
    - [신규 가설]
```

이 파일이 다음 `/hplan-evidence`의 컨텍스트 인풋이 됩니다.

## 출력 형식

```
PMF Gate — [날짜]
트리거: [시간/사용자/COGS/STATE.md 조건]

COGS 실측:  p50 X% / p90 Y% (예측 대비 ±Zpp)
Day-30 retention: X%
Strong-push 인용: N건

판정: PMF_SIGNAL / ECONOMICS_MISS / RETENTION_MISS / PIVOT
다음: [continue | 재실행 target]

harness/pmf-output.yaml 저장 완료.
```

## 연결 지점

- **입력**: `harness/STATE.md` (현재 조건), `cogs_sentinel.py` (재실행), 수동 행동 지표
- **출력**: `harness/pmf-output.yaml` → 다음 `/hplan-evidence` 컨텍스트 인풋
- **하네스**: `validate_docs.py`가 pmf-output.yaml 내 `evidence_carry_over` 경로를 검사 가능 (향후 확장)

## 스케치 → 정식 스킬 조건

- [ ] cogs_sentinel.py `--mode realtime` 파라미터 추가 (현재 예측 모드만 있음)
- [ ] pmf-output.yaml 형식 실사용에서 검증 (Habix Legal W6 측정 후)
- [ ] Evidence Gate 인풋으로의 자동 연결 구현
