# Unit Economics And COGS Gate

Use this reference for monetization, COGS, allowance, payment, and usage design.

## Required Outputs

- Pricing assumptions
- Platform/payment fee assumptions
- Net revenue calculation
- Target gross margin
- Allowed COGS per user and per usage unit
- Cost unit separation
- COGS measurement template
- Free-user cost and abuse scenario
- Plan allowance table
- Usage / payment boundary
- Proceed / Pivot / Hold economics decision

## Cost Unit Separation

Never calculate "AI usage" as one blob.

Separate units such as:

- Source import
- Audio minute
- Analysis run
- Model call
- Translation
- Render
- Storage
- CDN/download
- Retry
- Export
- Agent task
- Paid usage unit

If a unit has unknown or volatile cost, it must be excluded from basic allowance until measured.

## Do Not

- Do not call a product build-ready when COGS is unknown, volatile, or measured only on best-case samples.
- Do not offer unlimited AI, render, export, storage, import, transcription, or agent-run usage before caps and abuse scenarios exist.
- Do not let the payment provider be the usage meter. Payment status and in-app usage enforcement are separate systems.
- Do not charge users for failed paid outcomes unless the product explicitly sells attempts and the UI says so.
- Do not bury variable cost behind vague "credits" unless the actual paid usage unit is defined internally and in user-facing copy.
- Do not choose a provider by unit price alone. Measure latency, quality, retry rate, fallback behavior, privacy fit, and margin.
- Do not defer pricing review when the product's core workflow creates cost before the user sees value.

## Net Revenue And COGS

Use this pattern:

```text
net_revenue =
  gross_price
  - percentage_fee
  - fixed_fee
  - expected_refund_or_tax_buffer

allowed_monthly_cogs =
  net_revenue * (1 - target_gross_margin)

allowed_unit_cogs =
  allowed_monthly_cogs / included_usage_units
```

If fees are unknown, use conservative assumptions and label them.

## COGS Measurement Template

| Sample | Input size | Unit count | Model/API cost | Render/compute | Storage/CDN | Retry cost | Total COGS | Pass |
|---:|---:|---:|---:|---:|---:|---:|---:|---|

Pass criteria should include average and p90 cost, not only best-case cost.

## Free Usage Risk

Always model free users separately.

Include:

- Free allowance
- Expected usage rate
- Source/import cap
- Model/run cap
- Abuse vectors
- Monthly cost at 100, 1,000, and 10,000 free users when relevant

Free user cost must not silently consume all paid gross profit.

## Payment / Usage Boundary

Payment providers manage checkout and subscription status. The app manages usage limits.

Use this responsibility split:

| Responsibility | Payment provider | App DB |
|---|---|---|
| Checkout | Yes | Link to checkout |
| Subscription status | Source of truth | Replicated by webhook |
| Plan mapping | Product/variant | Internal plan |
| Usage allowance | No | Yes |
| Usage blocking | No | Yes |
| Usage charge/decrement | No | Yes |
| Billing period reset | Event source | Usage period reset |

## Usage Event Requirements

Track:

- Usage started
- Usage succeeded
- Usage failed
- Usage blocked
- Cost per event
- Plan and billing period
- Reason for blocked/failed state

Only charge allowance when the paid outcome succeeds, unless the product explicitly sells analysis attempts.

## Success-Only Charge Rule

For products where the user pays for an outcome, usage should usually be charged only after the outcome succeeds.

Define:

- When work is allowed to start
- Which intermediate steps create cost but do not decrement user allowance
- Which final event increments usage
- Which failure events record cost but do not charge allowance
- Which blocked states prevent job creation

Example rule shape:

```text
input accepted
→ processing started
→ user review / selection
→ final output succeeded
→ usage charged in the same transaction
```

Failure examples:

- Processing failed: record event and cost, do not decrement paid allowance.
- Output failed: record failure and retry count, do not decrement paid allowance.
- Usage blocked: do not create job.
- Payment past due: block new paid outcomes but preserve existing outputs according to policy.

## Provider Policy

If a workflow uses external AI, transcription, rendering, search, storage, or enrichment providers:

- Pick a default provider for MVP.
- Define fallback providers and when they trigger.
- Record provider, unit price, measured usage, total cost, fallback flag, and quality flags.
- Do not self-host by default just to avoid API cost; compare fixed ops cost, utilization, reliability, and maintenance burden.
- Revisit self-hosting only when usage volume, data policy, or quality constraints justify it.

## Provider Routing

For workflows with variable cost, speed, or quality, define routing instead of picking one provider blindly.

Common pattern:

1. Use the lowest-cost provider that clears minimum speed and quality gates.
2. Detect risky units: low confidence, missing entities, numeric/date/money fields, unusually short/long output, schema invalidity, or downstream uncertainty.
3. Reprocess only risky units with a higher-quality or faster fallback provider.
4. Expose uncertainty to the user when providers disagree.
5. Offer a paid or capped "quality mode" only if COGS supports it.

Routing table:

| Task | Default provider/path | Fallback provider/path | Trigger | Cost guardrail |
|---|---|---|---|---|

Provider selection must consider:

- Latency
- Unit cost
- Output quality
- Structured output validity
- Downstream task quality
- Privacy/data policy
- Failure/retry behavior
- Gross margin impact

## Economics Decision

- `GO`: unit COGS is measured, p90 is acceptable, free abuse is capped, and target gross margin survives.
- `CONDITIONAL_GO`: likely viable but sample measurement, fees, or usage caps are incomplete.
- `PIVOT_PRICING`: pain exists but allowance, price, or cost unit breaks margin.
- `HOLD`: COGS is unknown or gross margin is structurally impossible.
