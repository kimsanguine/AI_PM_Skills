# Bad Example — Unlimited Sonnet at low ARPU, RED

## Input

```bash
python3 hplan/scripts/cogs_sentinel.py \
  --provider anthropic --model claude-sonnet-4-6 \
  --tokens-in 8000 --tokens-out 2000 --calls-per-user-month 120 \
  --arpu 19 --paid-conversion 0.04 --free-abuse-multiplier 8
```

## Output (실측)

```json
{
  "monthly_cogs_per_paid_user_usd": {"p50": 6.63, "p90": 13.90, "worst": 28.78},
  "gross_margin": {"p50": 0.64, "p90": 0.25, "with_free_user_load": -19.61},
  "decision": "CONDITIONAL_GO",
  "reasons": [
    "p90 gross margin 25% below target 70%",
    "free-user blended margin -1961% — abuse cap or paywall first call"
  ]
}
```

## Why this fails

- ARPU $19 + 4% conversion + 8x abuse → 무료 24명이 paid 1명을 짓누름
- Worst $28.78 ≈ ARPU $19 → 최악의 달엔 사용자당 적자
- Blended margin -1961% — 무료 사용 제한 없이는 제품 자체 viable 아님

## Anti-pattern lessons

1. **무제한 free tier + 변동 비용** — 거의 항상 RED.
2. **Sonnet/Opus를 모든 호출에 쓰는 시나리오** — Haiku로 라우팅 가능한 경로를 찾지 않으면 RED.
3. **paid_conversion < 5%** + **abuse_multiplier > 5** 조합 — blended가 음수.

## Mitigation 시나리오

이 시나리오를 GREEN으로 옮기려면:
- abuse_multiplier 8 → 2 (paywall first call 후 사용량 캡)
- arpu $19 → $39 (가격 인상) — 인터뷰 evidence로 정당화 필요
- 또는 model을 Haiku로 routing — re-run sentinel
