# Metrics And Launch Gate

Use this reference for 5-layer metrics, launch experiments, paid signal, and proceed/pivot/kill decisions.

## Required Outputs

- MPO / productive outcome definition
- 5-layer metrics table
- Event tracking plan
- Metric formulas
- D30/D90 targets
- Dashboard wireframe
- Launch hypothesis
- Alpha target
- Recruiting messages
- Paid signal ladder
- First 5 / 10 / 30 user milestone plan
- Human metrics review checkpoint
- Proceed / Pivot / Kill rule

## MPO Definition

Define one Minimum Productive Outcome:

> The user inputs [source/context] and completes [paid outcome] under [time/quality/cost constraints].

MPO is not "used the feature." It is the user's real outcome.

## Do Not

- Do not use signups, traffic, impressions, or waitlist size as the main launch success metric.
- Do not claim PMF from 5 interviews, first 5 users, or founder-network enthusiasm.
- Do not launch broadly before the first narrow segment completes the MPO and exposes quality, friction, revenue, and cost signals.
- Do not ignore override rate, failure rate, blocked states, retry rate, or abandoned outputs in AI products.
- Do not optimize only activation when COGS or gross margin fails.
- Do not treat build-in-public attention as product evidence unless it converts into interviews, source/data, repeat usage, preorder, or payment.
- Do not hide `kill` or `hold` as valid outcomes. A failed launch experiment should protect future time and cost.

## 5-Layer Metrics

Use this stack:

| Layer | Metric | What it measures |
|---:|---|---|
| 1 | Sean Ellis or must-have score | PMF signal |
| 2 | TTV | Time to first value |
| 3 | Override Rate | AI/output quality and trust |
| 4 | Frustration Index | Failure, blocked states, retries, abandonment |
| 5 | Indispensability / Repeat MPO | Repeat value and retention |

Add revenue and COGS metrics when the product has paid usage:

- Free to paid conversion
- ARPU/MRR
- Average COGS per paid unit
- Gross margin

Add latency and quality metrics when speed or provider quality is part of the value:

- Time to first useful artifact
- End-to-end processing time
- Realtime factor or equivalent throughput metric
- Fallback rate
- Schema validity
- Evidence alignment
- Numeric/date/money/entity error rate when business-critical
- Heavy override rate by artifact type

## Event Tracking Plan

Use this table:

| Event | Trigger | Properties | Metric |
|---|---|---|---|

Include events for:

- Signup or acquisition source
- Core input/import
- Analysis or processing started/completed
- User review or override
- Paid outcome succeeded
- Download/share/export
- Usage blocked
- Failure/retry
- Upgrade clicked
- Checkout completed
- Processing step started/completed
- Provider fallback used
- Evidence opened
- User correction or uncertainty resolved

## Frustration Index

Create a weighted formula.

Example:

```text
frustration_index =
  failed_job * 3
  + usage_blocked * 2
  + input_blocked * 2
  + retry * 1
  + output_abandoned * 1
  + checkout_failed * 2
```

## Launch Experiment

Launch small. Do not amplify before PMF.

Required:

- Alpha target, normally 20 qualified users
- Screener criteria
- 7-day build-in-public calendar
- Preorder or paid alpha offer
- Funnel
- Paid signal ladder
- Success metrics
- 14-day execution schedule

## First 5 / 10 / 30 Milestones

Use this lightweight milestone ladder for small SaaS or agent products:

| Milestone | Meaning | Required evidence | Decision |
|---|---|---|---|
| First 5 | 5 people love or repeatedly need the outcome | Interviews, repeated use, source/data, or payment | Narrow ICP or pivot |
| First 10 | Pattern survives beyond founder's closest network | Repeat workflow, paid signal, support issues | Improve quality/ops |
| First 30 | Early monetization and retention signal | Paid users or strong repeat MPO | Continue or reprice |

Do not generalize from the first 5 users without segment review. First 5 users can identify a wedge; they do not prove the whole market.

## Paid Signal Ladder

| Signal | Strength | Interpretation |
|---|---|---|
| Compliment | Weak | Ignore for build decision |
| Waitlist | Weak-Medium | Interest only |
| Source/data provided | Medium | Real problem context |
| Feedback interview | Medium | Time commitment |
| Preorder/payment | Strong | Revenue signal |
| Repeat usage | Strong | Retention signal |
| Paid subscription | Strongest | Monetization signal |

## Proceed / Pivot / Kill

Use product-specific numbers, but keep the shape:

| Decision | Criteria | Next action |
|---|---|---|
| Proceed | MPO, paid signal, and COGS targets all pass | Implement MVP |
| Proceed but improve | Paid signal exists but quality or UX metric is weak | Fix prompt/UX/workflow |
| Pivot ICP | MPO exists but payment weak for current segment | Change segment |
| Pivot Product | Interviews reveal a different stronger job | Change workflow |
| Pivot Pricing | Payment exists but margin breaks | Change price/allowance/cost |
| Kill/Hold | No source/data, no MPO, no paid signal | Stop productization |

Launch results must feed the next discovery cycle.

## Human Metrics Checkpoint

Before scaling, ask the human to review:

- Which segment had the strongest "very disappointed" or repeat-MPO signal?
- Did first value happen fast enough?
- Did users heavily override AI output?
- Did frustration come from quality, UX, cost, policy, or onboarding?
- Did paid signal justify the current price and allowance?
- Should the next 14-60 days proceed, pivot ICP, pivot product, pivot pricing, or hold?

## Quality Gates

For AI-generated operational output, measure quality by the downstream artifact, not only raw model output.

Use gates such as:

| Gate | Pass condition | Failure action |
|---|---|---|
| Speed | First useful artifact arrives within SLA | Change workflow, precompute, or show async UX |
| Evidence | Claims map to source/evidence | Restrict generation or require review |
| Numeric/entity | Dates, amounts, names, owners, and deadlines have no critical errors | Add uncertainty UI or fallback provider |
| Decision/action | Decisions and next actions are not missed | Improve extraction or require human review |
| Cost | Quality path preserves margin | Add caps, paid quality mode, or provider routing |
| Friction | Users understand blocked/failed states | Redesign status and recovery UX |
