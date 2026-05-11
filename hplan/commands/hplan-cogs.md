---
description: "Quick COGS sentinel — provider, model, usage parameters → deterministic p50/p90 monthly margin + GREEN/CONDITIONAL_GO/RED decision. Skips evidence/product gates."
argument-hint: "[provider] [model] [tokens-in tokens-out calls/mo ARPU paid_conv abuse_mult]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-cogs

Quick COGS check — useful when:
- Comparing providers (Anthropic ↔ OpenAI ↔ Google)
- Stress-testing a pricing scenario
- Pre-commitment check before `/hplan-build`

This is a **subset of `/hplan-build`** — it does not record a decision, just calculates margin.

## Default invocation

```bash
python3 hplan/scripts/cogs_sentinel.py \
  --provider anthropic --model claude-sonnet-4-6 \
  --tokens-in 3000 --tokens-out 1500 \
  --calls-per-user-month 40 \
  --arpu 29 --paid-conversion 0.05 \
  --free-abuse-multiplier 3 \
  --target-gross-margin 0.70
```

## When to chain

- After `/hplan-cogs`, if user wants to commit → use `/hplan-build` for full decision + handoff
- After `/hplan-cogs`, if RED → invoke `exclusions` to record the price/cost wedge that failed

## Pairing

- `oracle/cost-sim` first (LLM scenario thinking)
- Then `/hplan-cogs` (deterministic numbers)

## Output

- Prints markdown report with p50/p90/worst monthly COGS, margin, decision, reasons
- Optionally writes to `--out path.md`
