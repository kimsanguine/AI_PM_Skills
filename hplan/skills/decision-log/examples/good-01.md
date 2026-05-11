# Good Example — Self-audit with hit_rate

## 3 decisions logged

```bash
# matae app — build
python3 hplan/scripts/decision_log.py log \
  --project matae --gate build --decision build --score 78 \
  --reason "5/5 강한 신호 (한국 냉장고 관리)" --reason "COGS GREEN with Haiku routing"

# meetflow — hold
python3 hplan/scripts/decision_log.py log \
  --project meetflow --gate build --decision hold --score 32 \
  --reason "Granola/Otter 점유" --reason "enterprise compliance 신호 없음"

# foobar (가상의 사례) — hold
python3 hplan/scripts/decision_log.py log \
  --project foobar --gate evidence --decision hold --score 28 \
  --reason "약한 wedge"
```

## 3-6 months later, backfill

```bash
decision_log.py update --id dec-...-matae   --outcome shipped
decision_log.py update --id dec-...-meetflow --outcome killed
decision_log.py update --id dec-...-foobar   --outcome external_success
```

## Audit

```bash
decision_log.py audit
```

```json
{
  "total": 3,
  "resolved": 3,
  "by_decision": {"build": 1, "hold": 2},
  "by_decision_outcome": {"build->shipped": 1, "hold->killed": 1, "hold->external_success": 1},
  "hit_rate": 0.667,
  "false_holds": [{"id": "...", "project": "foobar", "reasons": ["약한 wedge"]}],
  "guidance": [
    "Hit rate 67% — re-examine rubric thresholds.",
    "1 false-hold(s) detected — review reasons for systematic bias against shippable ideas."
  ]
}
```

## Why this is *good*

- 결정마다 `--reason` 2개 이상 — 미래의 audit에서 "왜 그랬는지" 추적 가능
- outcome backfill 완료 — audit이 정량적 신호 제공
- false_hold 1건이 명확히 드러남 → rubric의 wedge weight 보정 단서

## Action after this audit

- false_hold가 "wedge" 사유 → wedge 판단 기준 검토
- hit_rate 67%는 "rubric 정확함"보다 "표본 작음" 시그널 — 10건+ 모이면 의미 있어짐
