---
name: agent-ab-test
description: "Design and analyze A/B tests for AI agents — compare prompt versions, model choices, or architecture variants with statistical rigor. Use when optimizing agent performance, testing new instructions, evaluating model upgrades, or validating TK-based improvements."
argument-hint: "[agent and variants to A/B test]"
---

# Agent A/B Test

> 에이전트 A/B 테스트 설계 및 분석 — 프롬프트, 모델, 아키텍처 변형을 통계적으로 비교

## 개념

에이전트 A/B 테스트는 웹 A/B 테스트와 다르다. 클릭률이 아닌 "판단의 품질"을 측정해야 하고, LLM의 비결정론적(non-deterministic) 특성 때문에 같은 입력에도 결과가 다를 수 있다. 통계적 유의성 없이 "B가 좋아 보인다"로 판단하면 노이즈에 속는다.

## Instructions

You are designing an **A/B test** for: **$ARGUMENTS**

### Step 1 — Test Hypothesis

```
현재 상태 (Control — A):
  [현재 에이전트 구성]

변형 (Variant — B):
  [변경하려는 요소]

가설:
  "[변경 요소]를 적용하면 [측정 지표]가 [방향]으로 [목표치]만큼 변한다"

변경 유형:
  □ Prompt/Instruction 변경
  □ Model 변경 (예: Sonnet → Haiku)
  □ Architecture 변경 (단일 → 멀티에이전트)
  □ TK Injection (새 TK 추가 전후 비교)
  □ Parameter 변경 (temperature, max_tokens 등)
```

### Step 2 — Metric Selection

| 계층 | 메트릭 | 설명 | 측정 방법 |
|------|--------|------|----------|
| **Primary** | [핵심 지표 1개] | 의사결정 기준 | |
| **Secondary** | [보조 지표 2-3개] | 트레이드오프 확인 | |
| **Guardrail** | [안전 지표] | 악화되면 즉시 중단 | |

에이전트 A/B 테스트 주요 메트릭:
- **Task Accuracy**: 정답률 (human evaluation 기반)
- **Latency**: 응답 시간 (P50, P95, P99)
- **Token Cost**: 태스크당 토큰 비용
- **User Satisfaction**: 유저 평가 (thumbs up/down)
- **Hallucination Rate**: 환각 발생 비율
- **Escalation Rate**: 사람에게 에스컬레이션된 비율

### Step 3 — Sample Size & Duration

```
필요 표본 크기 계산:
  Baseline metric: [현재 값]
  Minimum Detectable Effect (MDE): [최소 감지 차이]
  Significance level (α): 0.05
  Power (1-β): 0.80

  → 필요 표본 수: [N] per variant
  → 예상 기간: [N]일 (일일 트래픽 [N]건 기준)
```

**에이전트 테스트 특이사항:**
- LLM 비결정론 → 같은 입력 5회 반복 실행 권장
- 시간대별 편향 → A/B 동시 실행 (순차 X)
- 프롬프트 캐싱 → 캐시 워밍 후 측정 시작

### Step 4 — Test Execution Plan

```
Traffic Split: [50/50 | 90/10 (canary) | multi-arm bandit]

Execution:
  Day 0: 테스트 환경 세팅, baseline 측정
  Day 1-N: A/B 병렬 실행
  Daily: guardrail 메트릭 모니터링
  Day N+1: 결과 분석

Rollback Trigger:
  - Guardrail 메트릭 [X]% 이상 악화 시 즉시 중단
  - Hallucination rate > [threshold] 시 즉시 중단
```

### Step 5 — Result Analysis

```
Results:
              Control (A)    Variant (B)    Difference
Primary:      [value]        [value]        [+/-N%]
Secondary 1:  [value]        [value]        [+/-N%]
Secondary 2:  [value]        [value]        [+/-N%]
Guardrail:    [value]        [value]        [+/-N%]

Statistical Significance: [p-value]
Confidence Interval: [range]
Practical Significance: [meaningful or noise?]

Decision:
  □ Ship B (모든 지표 개선, 통계적 유의)
  □ Keep A (차이 없거나 guardrail 악화)
  □ Iterate (방향은 맞지만 효과 부족 → B' 설계)
  □ Investigate (예상과 다른 패턴 → 추가 분석 필요)
```

### Output

```
A/B Test Summary: [agent name]
──────────────────────────────
Hypothesis: [one-line]
Variants: A=[description] vs B=[description]
Primary Metric: [metric] — A: [value] vs B: [value]
p-value: [value]
Decision: [Ship B / Keep A / Iterate / Investigate]
Cost Impact: [+/-$N per month]
Next Step: [action]
```

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- LLM 비결정론 대응: 5회 반복 실행 + 시간대 동시 실행 패턴
- TK 주입 효과 측정: TK-NNN 프레임워크와 연결

---

## Further Reading
- Ron Kohavi, *Trustworthy Online Controlled Experiments* — A/B test design and analysis
- Anthropic, "Evaluating AI Models" — LLM evaluation best practices and metrics
