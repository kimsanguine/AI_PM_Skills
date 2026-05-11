# test-cases — evidence-rubric

## TC-001 — Strong evidence + 2+ interview lines → `build`

```json
{
  "idea": "...",
  "interview_notes": "Line1 with money loss\nLine2 with money loss",
  ...
}
```

Expect: `decision == "build"`, score ≥ 75.

## TC-002 — Strong rubric but no interviews → `interview`

Same as TC-001 but `interview_notes` empty.
Expect: `decision == "interview"` (build은 인터뷰 ≥ 2 lines 강제).

## TC-003 — Korean compliments-only → `hold`

```json
{
  "interview_notes": "친구가 좋다고 했어요"
}
```

Expect: `decision == "hold"`, score < 35.

## TC-004 — features ≥ 5 → MVP narrowness penalty

`features = "A, B, C, D, E"` → MVP narrowness score ≤ 7.

## TC-005 — alternatives empty → workaround = 0

대체재 비어있으면 workaround axis = 0. Build 결정 불가.

## TC-006 — economic pain keyword absent → build 불가

설령 score ≥ 75라도 combined text에 `돈|매출|비용|결제|리스크|기회|revenue|cost|pay|risk` 없으면 → `interview` 강제.

## TC-007 — interview lines == 1 only → build 불가

`interview_notes.splitlines()`에서 length > 8인 줄이 1개 이하면 → `interview` 강제.
