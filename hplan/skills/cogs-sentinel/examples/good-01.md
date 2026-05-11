# Good Example — hplan-as-a-service hypothetical, GREEN

## Input

```bash
python3 hplan/scripts/cogs_sentinel.py \
  --provider anthropic --model claude-sonnet-4-6 \
  --tokens-in 3000 --tokens-out 1500 --calls-per-user-month 40 \
  --arpu 29 --paid-conversion 0.08 --free-abuse-multiplier 3
```

## Output (실측)

```json
{
  "per_call_cost_usd": {"p50": 0.0315, "p90": 0.0693},
  "monthly_cogs_per_paid_user_usd": {"p50": 1.29, "p90": 2.70, "worst": 5.60},
  "gross_margin": {"p50": 0.95, "p90": 0.90, "with_free_user_load": 0.49},
  "decision": "GREEN",
  "reasons": ["All scenarios within target margin."]
}
```

## Why GREEN

- p90 마진 90% ≥ target 70% ✓
- Blended margin 49% ≥ target × 0.7 = 49% ✓ (간발의 차)
- Worst $5.60 < ARPU $29 ✓

## Why this scenario is realistic

- 솔로 PM이 `evidence-rubric` + `cogs-sentinel` + `handoff`만 호출 → 월 40회
- Sonnet은 PRD-shape input(~3K tokens)에 충분 — Opus 불필요
- $29/mo는 SaaS 최저가 belt

## Caveat

blended 49%가 target × 0.7 임계값과 같음. **free conversion이 8%→4%로 떨어지면 blended가 음수**. abuse cap 필수.
