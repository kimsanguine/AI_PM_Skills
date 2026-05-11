# Bad Example — Log without reasons + no backfill ever

## Bad logging

```bash
decision_log.py log --project x --decision hold
```

(No `--reason`. No `--score`. Default `gate=build` even though it's actually evidence-stage.)

## 6 months later

```bash
decision_log.py audit
```

```json
{
  "total": 8, "resolved": 0, "pending": 8,
  "guidance": ["8 decisions still pending — back-fill outcomes to enable calibration."]
}
```

## Why this fails

- `pending == 8` — 결정만 쌓이고 outcome이 안 들어옴 → hit_rate 측정 불가
- reasons 비어있음 → audit의 false_hold/missed_build에서 *왜*를 볼 수 없음
- gate가 잘못 — evidence 단계 hold인데 build로 기록 → false_hold 패턴 추적 어려움

## Anti-pattern lessons

1. **reasons 없는 decision log는 audit이 의미 없다** — 통계만 있고 narrative 없음.
2. **outcome backfill을 calendar에 박지 않으면 영원히 미루게 된다** — 분기별 audit 권장.
3. **gate를 잘못 기록하면 rubric 보정이 어렵다** — evidence vs product vs build를 명확히.
