# test-cases — decision-log

## TC-001 — log + audit empty hit_rate
- 결정 1개만 + outcome 없음 → `hit_rate: null`, `pending: 1`

## TC-002 — Build + shipped → correct
- decision=build, outcome=shipped → correct in audit

## TC-003 — Hold + external_success → false_hold
- decision=hold, outcome=external_success → counted in `false_holds` array

## TC-004 — Build + killed → missed_build
- decision=build, outcome=killed → counted in `missed_builds` array

## TC-005 — Invalid decision rejected
- `--decision yolo` → SystemExit "invalid decision"

## TC-006 — Invalid outcome rejected
- `update --outcome maybe` → SystemExit "invalid outcome"

## TC-007 — update preserves order
- update 후 jsonl 순서 보존 (last write wins for same id)
