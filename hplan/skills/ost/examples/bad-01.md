# Bad Example — Solutions disguised as opportunities

## Bad input

```json
{
  "outcome": "Make money",
  "opportunities": [
    {
      "name": "AI agent를 만든다",
      "evidence_count": 0,
      "solutions": [
        {"name": "API 만들기"},
        {"name": "프론트엔드"},
        {"name": "DB"}
      ]
    }
  ]
}
```

## Why this fails

| 문제 | 이유 |
|---|---|
| `outcome: "Make money"` | measurable 아님, 시한 없음 |
| `opportunity: "AI agent를 만든다"` | **이건 solution**. opportunity = "사용자가 X를 못 한다" |
| `evidence_count: 0` | 어떤 인터뷰도 이 needs를 backing 안 함 |
| solutions: API, 프론트, DB | 구현 task, 사용자 결과 아님 — experiment + decision_rule 없음 |

## Anti-pattern lessons

1. **Outcome은 "Make money"가 아니라 "ICP X가 90일 내 Y를 N번 함"**
2. **Opportunity는 동사가 "못 한다 / 못 끝낸다 / 못 정리한다"로 시작**해야 함 — "만든다"는 solution
3. **Evidence count 0인 opportunity는 OST에 올라가지 못함** — interview-synthesis로 돌아가서 evidence 채우거나 prune
4. **Solution은 구현 task가 아니라 사용자가 받는 결과**

## What this person should do

1. `interview-synthesis`로 5 인터뷰 후 strong-push quote 모음
2. Quote 패턴에서 "사용자가 못 하는 것" 추출 → opportunity
3. 각 opportunity 당 1-3 solution + 각 solution 당 1 experiment + decision_rule
4. 그제야 `ost_generator.py` 실행
