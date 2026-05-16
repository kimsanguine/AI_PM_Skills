---
name: pmf-gate
description: "PMF Gate — post-launch measurement loop that converts operational data (COGS sentinel results + behavioral metrics) into Evidence Gate inputs for the next build cycle. Closes the hplan loop: Evidence → Product → Build → [ship] → PMF → Evidence (next). Use when the product has shipped and one of these is true: 30+ days post-beta, 10+ paid users, COGS delta ±15pp from prediction, or STATE.md next-entry condition is met."
argument-hint: "[--mode realtime] [--actual-calls N] [--actual-tokens-in N] [--actual-tokens-out N]"
allowed-tools: ["Read", "Write", "Bash"]
model: sonnet
---

# PMF Gate — Post-Launch Measurement Loop

Running for: **$ARGUMENTS**

## Core Goal

- hplan 루프를 닫는다: Evidence → Product → Build → [출시] → PMF Gate → Evidence (다음).
- 운영 데이터(COGS 실측 + 행동 지표)를 다음 Evidence Gate의 인풋 형식(`harness/pmf-output.yaml`)으로 변환.
- "계속 만들어야 하는가"를 데이터로 답한다 — LLM 직감 아님.

## Trigger Gate

### Use This Skill When

- 베타 출시 후 N일 경과 (PROGRESS.md에 명시된 Wx 마감)
- 유료 사용자 M명 도달 또는 베타 사용자 K명 N주 연속 재방문
- 실측 p90 margin이 Build Gate 예측과 ±15pp 이상 차이
- `harness/STATE.md`의 "다음 진입 조건" 항목이 충족됨

**기본값 (PROGRESS.md에서 오버라이드)**:
- 시간: 베타 출시 후 30일
- 사용자: 유료 전환 10명 또는 베타 30일 이상 재방문

### Route to Other Skills When

- PMF_SIGNAL → 다음 `evidence-rubric` 실행 (evidence_carry_over 인풋 사용)
- ECONOMICS_MISS → `cogs-sentinel` predict 모드로 재산정 후 pricing 조정
- RETENTION_MISS → `ost` 재검토 (opportunities 재우선순위)
- PIVOT → `decision-log` pivot 기록 후 Evidence Gate 재시작

### Boundary Checks

- ❌ 행동 지표(retention, conversion)는 이 스킬이 수집하지 않는다 — 사용자가 직접 입력해야 함.
- ❌ `cogs_sentinel.py --mode realtime`은 실측 호출 수 없이는 의미 있는 결과를 내지 못함.
- ❌ 이 스킬은 Build Gate를 대체하지 않는다 — 다음 사이클의 Evidence Gate 인풋을 준비할 뿐.

## Inputs

### COGS 실측

```bash
python3 hplan/scripts/cogs_sentinel.py --mode realtime \
  --provider anthropic --model claude-sonnet-4-6 \
  --actual-calls-per-user-month [실측값] \
  --actual-tokens-in [실측 평균 input tokens] \
  --actual-tokens-out [실측 평균 output tokens] \
  --arpu [현재 ARPU] \
  --out harness/pmf-output-cogs.md
```

Build Gate 예측(`harness/build-gate/cogs_input.json`)과 자동 비교. delta ±15pp 초과 시 경고.

### 행동 지표 (사용자 직접 입력)

```yaml
retention:
  day_7: [%]
  day_30: [%]
engagement:
  core_flow_completion: [%]
  workaround_reduction: [%]
revenue:
  paid_conversion: [%]
  churn_30d: [%]
signal:
  strong_push_quotes: [N]
  nps_qualitative: [한 줄]
```

## Steps

1. `harness/STATE.md`에서 트리거 조건 충족 여부 확인.
2. `cogs_sentinel.py --mode realtime` 실행 — delta 계산.
3. 행동 지표를 사용자로부터 수집 (위 YAML 형식).
4. PMF 판정 기준 적용 (아래 표).
5. `harness/pmf-output.yaml` 저장.
6. `evidence_carry_over` 항목을 추출해 다음 `/hplan-evidence` 컨텍스트로 명시.

## Outputs

### PMF 판정 기준

| 조건 | 판정 |
|------|------|
| Day-30 retention ≥ 30% + COGS GREEN + strong_push ≥ 3 | **PMF_SIGNAL** |
| COGS 실측 p90 < 20% | **ECONOMICS_MISS** |
| Day-7 retention < 20% | **RETENTION_MISS** |
| strong_push_quotes < 3 | **EVIDENCE_THIN** |
| 위 조건 복합 | **PIVOT** |

### pmf-output.yaml 형식

```yaml
pmf_date: YYYY-MM-DD
verdict: PMF_SIGNAL | ECONOMICS_MISS | RETENTION_MISS | EVIDENCE_THIN | PIVOT
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
    - [인용 또는 데이터 포인트]
  new_hypotheses:
    - [신규 가설]
```

## Verification

- [ ] `cogs_sentinel.py --mode realtime` 실행 성공 — `harness/pmf-output-cogs.md` 생성
- [ ] delta_pp 계산 정상 (예측 vs 실측 비교 블록 출력)
- [ ] `harness/pmf-output.yaml` 저장 완료 + `evidence_carry_over` 비어 있지 않음
- [ ] 판정 결과가 다음 Gate 행동과 연결됨 (PMF_SIGNAL → Evidence Gate, PIVOT → decision-log)
