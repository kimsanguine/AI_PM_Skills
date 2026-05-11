# test-cases — cogs-sentinel

## TC-001 — Sonnet light usage at high ARPU → GREEN
- tokens-in 3000, tokens-out 1500, calls 40, arpu 29, conv 8%, abuse 3
- Expect: GREEN, p90 ≥ 70%

## TC-002 — Sonnet heavy + low ARPU + high abuse → RED
- tokens-in 8000, tokens-out 2000, calls 120, arpu 19, conv 4%, abuse 8
- Expect: blended margin negative, decision CONDITIONAL_GO or RED

## TC-003 — Haiku 4.5 same usage → margin improvement
- Same as TC-002 but model claude-haiku-4-5
- Expect: per-call cost ~80% lower, margins recover

## TC-004 — Unknown provider/model → SystemExit
- `--provider unknown` → script exits with error message

## TC-005 — Custom pricing override
- Pass `--params` with `pricing` field overriding snapshot
- Expect: uses provided rate

## TC-006 — Lognormal reproducibility
- Same input run 2x → identical p50/p90 (deterministic seed=7)
