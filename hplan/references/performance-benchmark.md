# Performance Benchmark Gate

Use this reference when speed, realtime behavior, provider quality, or latency is part of the product promise.

## Required Outputs

- Product speed promise
- Latency budget by artifact
- Benchmark paths
- Provider benchmark matrix
- Quality gates
- Provider routing policy
- UX policy for waiting, partial output, fallback, and uncertainty
- Benchmark artifact format
- Product decision: `GO`, `LIMITED_GO`, `PIVOT_UX`, `PIVOT_PROVIDER`, or `NO_GO`

## Product Speed Promise

Write the user-facing promise as a measurable statement.

Examples:

- "First useful draft within 2 minutes."
- "Search results update within 500ms after filter change."
- "Live notes appear during the session; final summary is ready within 60 seconds after the session ends."
- "Batch import completes in less than 20% of the input duration."

If the promise cannot be measured, it is marketing copy, not a product gate.

## Do Not

- Do not promise realtime, instant, live, or high-accuracy behavior without a latency budget and benchmark artifact.
- Do not average input-only, full-processing, live/incremental, and fallback paths into one performance number.
- Do not pick a provider because a single sample looked good. Measure p50, p90/p95, quality, failure, retry, privacy, and cost.
- Do not make the slowest secondary artifact block the first useful artifact.
- Do not use a spinner as the entire UX for a multi-step or expensive workflow.
- Do not hide uncertainty, conflicts, schema failures, fallback use, or quality flags behind generic "AI generated" labels.
- Do not benchmark only happy-path small inputs when real users will upload messy, large, private, or mixed-quality inputs.

## Latency Budget

Use this table:

| Artifact / step | Target | Maximum allowed | Product feeling |
|---|---:|---:|---|
| First useful artifact |  |  |  |
| Core output |  |  |  |
| Secondary output |  |  |  |
| Full batch processing |  |  |  |

Rules:

- The first useful artifact should arrive before the rich/final artifact when possible.
- If batch processing is slow, position it as upload/background mode, not instant workflow.
- If realtime is expensive, cap it by plan or offer it as a premium path.

## Benchmark Paths

Measure separate paths:

| Path | Purpose | Example |
|---|---|---|
| Input-only baseline | Measure model/workflow latency after input is already prepared | structured text, clean records, prepared dataset |
| Full processing path | Measure raw input to final output | file/data import to output |
| Live/incremental path | Measure partial processing during the user's active workflow | streaming, incremental parsing, background precompute |
| Fallback path | Measure provider/tool failure and recovery | default provider fails, fallback succeeds |

Do not average these together. They answer different product questions.

## Provider Benchmark Matrix

Use:

| Provider/path | Latency | Unit cost | Quality | Failure rate | Privacy fit | Margin fit | Decision |
|---|---:|---:|---|---:|---|---|---|

Quality must include downstream task quality, not just raw provider output.

## Quality Gates

Use gates relevant to the domain:

| Gate | Pass condition | Failure action |
|---|---|---|
| Speed gate | Meets latency budget | Change UX, precompute, or choose another provider |
| Schema gate | Structured output validates | Retry/fallback or block use |
| Evidence gate | Claims map to source/evidence | Require review or suppress claim |
| Numeric/entity gate | Critical facts are correct | Mark uncertain, fallback, or ask user |
| Action/decision gate | Required actions are not missed | Re-prompt or human review |
| Cost gate | Provider route preserves gross margin | Cap, route, price, or defer |
| Privacy gate | Input is approved for provider path | Block or local-only path |

## Provider Routing Policy

Prefer routing over one-size-fits-all providers.

Default pattern:

1. Run the cheapest acceptable path.
2. Score output quality and uncertainty.
3. Route risky chunks/items/fields to a better or faster fallback.
4. Show uncertainty when providers conflict.
5. Save provider, latency, cost, fallback reason, and quality flags.

## UX Policy

When users wait, show:

- Current step
- ETA or elapsed time
- Completed artifacts
- Next artifact expected
- Fallback action
- Partial result when safe
- Background job status for secondary artifacts

Do not use a spinner as the whole UX for a multi-step workflow.

When quality is uncertain, show:

- `confirmed`
- `review`
- `missing`
- `conflict`
- `fallback used`

Use domain-appropriate labels; do not hide uncertainty behind "AI generated."

## Benchmark Artifact Format

Record:

- Input type and size
- Provider/path
- Step-level seconds
- Total seconds
- Throughput metric such as realtime factor, records/sec, pages/min, or tokens/sec
- Unit cost
- Retry/fallback count
- Schema validity
- Quality flags
- Downstream output quality
- Pass/fail against latency and quality gates

## Product Decision

| Decision | Criteria | Next action |
|---|---|---|
| `GO` | Latency, quality, privacy, and cost gates pass | Implement build path |
| `LIMITED_GO` | One path passes only under cap or controlled context | Limit plan, scope, or input size |
| `PIVOT_UX` | Product works but not as fast/live as promised | Reposition to async/background |
| `PIVOT_PROVIDER` | Better provider/routing needed | Re-run benchmark |
| `NO_GO` | SLA, quality, privacy, or margin structurally fails | Stop implementation |
