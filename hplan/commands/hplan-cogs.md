---
description: "Quick COGS sentinel — provider, model, usage parameters → deterministic p50/p90 monthly margin + GREEN/CONDITIONAL_GO/RED decision. Skips evidence/product gates. Use when comparing providers, stress-testing pricing, or pre-checking a scenario before committing to /hplan-build."
argument-hint: "[provider] [model] [tokens-in tokens-out calls/mo ARPU paid_conv abuse_mult]"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-cogs


## Instructions

You are running the **hplan COGS sentinel** for: **$ARGUMENTS**

This is a subset of `/hplan-build` — calculation only, no decision recorded.

### Step 1 — Collect inputs
Provider, model, tokens_in, tokens_out, calls_per_user_month, ARPU, paid_conversion, free_abuse_multiplier, target_gross_margin (default 0.70).

### Step 2 — Run sentinel
Execute: `python3 hplan/scripts/cogs_sentinel.py --provider <p> --model <m> --tokens-in <ti> --tokens-out <to> --calls-per-user-month <c> --arpu <a> --paid-conversion <pc> --free-abuse-multiplier <fa>`.

### Step 3 — Interpret
- GREEN — proceed to `/hplan-build`
- CONDITIONAL_GO — list mitigations, ask user for human approval
- RED — invoke `exclusions` to record the failed pricing wedge

## Output Format

Return:

1. **Per-call cost** — p50 / p90 USD
2. **Monthly COGS per paid user** — p50 / p90 / worst USD
3. **Gross margin** — p50 / p90 / with-free-user-load %
4. **Decision** — GREEN / CONDITIONAL_GO / RED with reasons array
5. **Next step** — `/hplan-build` to commit or pivot
