# test-cases — interview-synthesis

## TC-001 — Import → all status awaiting_human_tag
- import 6 quotes → all `status: "awaiting_human_tag"`

## TC-002 — Tag strong/push for 3 distinct persons → PROCEED
- 5 interviews + 3 distinct strong-push tags → `verdict: PROCEED_TO_PRODUCT_GATE`

## TC-003 — 2 persons same strong push → INTERVIEW
- Only 2 distinct persons (same person tagged 3x) → `INTERVIEW_OR_HOLD`

## TC-004 — Invalid strength rejected
- `tag --strength super` → SystemExit

## TC-005 — Invalid axis rejected
- `tag --axes wave` → SystemExit

## TC-006 — Empty axes allowed
- `tag --strength medium` (no `--axes`) → succeeds with `axes: []`

## TC-007 — Untagged-only list filter
- `list --untagged` shows only `status == awaiting_human_tag`
