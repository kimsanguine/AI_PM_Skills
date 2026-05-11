# troubleshooting — interview-synthesis

## "AI export JSON format이 달라요"

기본 schema:
```json
{"source": "...", "interviews": [{"person": "...", "date": "...", "quotes": [{"text": "...", "theme": "..."}]}]}
```

다른 도구는 변환 필요 — 작은 Python script로 한 번만 작성하면 됩니다.

## "5/3 규칙 너무 보수적이라고 느낌"

SKILL.md 본문 규칙. 완화하려면 `audit` 호출 후 reason에 명시하고 `evidence-rubric` 점수와 함께 결정. 단 hit_rate audit이 보정 시그널 줄 것.

## "동일 인물이 강한 Push를 여러 번 말함"

count = distinct persons, not distinct quotes. PM_A가 3 quotes 모두 strong-push → 1로 카운트.

## "audit가 자꾸 untagged 남았다고 함"

- `list --untagged`로 정확히 어떤 quote인지 확인.
- 모든 quote가 evidence는 아니므로, future intent 같은 건 의도적으로 *태깅 안 함* OK. 단 audit guidance에 reminder로 표시됨.

## "tagging 시점 = 호출 즉시?"

- `tagged_at` field가 ISO timestamp로 기록됨 → audit trail.
