# Bad Example — Import 후 audit 바로 → INTERVIEW_OR_HOLD

## Bad sequence

```bash
python3 hplan/scripts/interview_synthesis.py import /tmp/ai_export.json
# NO TAGGING
python3 hplan/scripts/interview_synthesis.py audit
```

## Output

```json
{
  "interviews": 5,
  "tagged_quotes": 0,
  "untagged_quotes": 6,
  "verdict": "INTERVIEW_OR_HOLD",
  "guidance": [
    "6 untagged quote(s) — AI synthesis is not evidence until a human assigns strength/axes.",
    "5+ interviews but only 0 repeated strong Push. Re-interview ICP variants or pivot."
  ]
}
```

## Why this fails

- AI extraction만으로 Product Gate로 갈 수 없음
- 그래도 가려면 PM의 직감만 의존 → 다음 분기 false_build 위험

## Common mistake

"AI가 다 정리해줬으니 됐다" — the existing incumbents/BuildBetter 모두 sentiment를 표시하지만 **sentiment ≠ evidence strength**. 인간 판단이 필요한 이유:

| AI sentiment | Human evidence strength |
|---|---|
| "Positive" | "약함 (칭찬일 뿐, 행동 없음)" |
| "Negative" | "강함 (해결책 부재로 매출 손실)" |
| "Neutral" | "강함 (workaround 명시)" |

태깅 안 한 quote는 evidence가 아니다.
