# test-cases — exclusions

## TC-001 — Add → verify in JSONL
```bash
exclusions_registry.py add "X" --why "Y" --reopen "Z"
cat harness/exclusions.jsonl | tail -1 | jq .
```
Expect: last line is valid JSON with non-null id/ts.

## TC-002 — Korean fuzzy match (bigram fallback)
```bash
exclusions_registry.py add "범용 PRD 생성기" --why "..." --reopen "..."
exclusions_registry.py check "범용 PRD 자동 생성 도구"
```
Expect: COLLISION, overlap ~0.42.

## TC-003 — Threshold tunability
`--threshold 0.30` finds matches that 0.40 misses. Default conservative.

## TC-004 — No match
`check "completely unrelated product"` → CLEAR.

## TC-005 — Append-only invariant
Add same exclusion twice → two entries (different ids, different ts). No dedup — intentional history.

## TC-006 — Empty registry
First `check` on fresh repo → `matches: []`, `verdict: "CLEAR"`.
