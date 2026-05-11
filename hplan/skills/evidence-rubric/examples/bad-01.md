# Bad Example — Compliments-only idea, scored 28/100 → `hold`

## Input

```json
{
  "idea": "AI로 사용자 워크플로우를 자동화하는 SaaS",
  "target": "스타트업, 중소기업",
  "hypothesis": "AI가 있으면 더 편하다",
  "alternatives": "",
  "features": "AI 워크플로우, 자동화, 대시보드, 알림, 통합, 챗봇, 추천, 분석",
  "interview_notes": "친구 3명이 좋다고 했어요"
}
```

## Why this fails

| 축 | 문제 |
|---|---|
| ICP | "스타트업, 중소기업" — 인구통계만, 행동 없음. **0/20** |
| Recent painful event | 없음 (compliment만) — **4/15** |
| Workaround | 비어있음 — **0/15** |
| Economic pain | 없음 — **5/15** |
| Switching trigger | 대체재 없으니 switch 자체 의미 없음 — **0/10** |
| MVP narrowness | features 8개 — **3/10** |
| Acquisition path | "친구 3명" — first 5 strangers 아님 — **1/5** |

## Output (예상)

```
decision: hold
score: ~28/100
reasons:
  - "compliments-only evidence는 build evidence가 아니다"
  - "대체재가 비어있으면 사용자가 지금 무엇을 쓰는지 모른다"
  - "MVP 기능이 8개라는 건 아직 MVP가 없다는 뜻"
```

## Anti-pattern lessons

1. **"AI로 X"는 ICP가 아니다** — "주 N회 X를 하는 Y 행동을 가진 사람"이어야 한다.
2. **친구의 칭찬은 evidence가 아니다** — Mom Test "Cool!" 신호. 무시.
3. **features 8개 = MVP 0개** — 기능을 늘려서 evidence 부족을 가린 경우.

## What this person should do instead

- Ditch the idea OR pick ONE workflow that one specific role does 5+ times a week.
- Find 5 strangers (not friends) who currently solve it manually.
- Watch them work for 15 minutes each.
- Then re-score with `evidence-rubric`.
