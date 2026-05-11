# Good Example — 5 인터뷰 import + 3 distinct strong-push 태깅 → PROCEED

## Import

```bash
cat > /tmp/ai_export.json <<EOF
{
  "source": "buildbetter",
  "interviews": [
    {"person": "PM_A", "date": "2026-05-09", "quotes": [
      {"text": "지난주에 30분 또 날렸어요", "theme": "manual workaround"},
      {"text": "안 되면 영업 못 따요", "theme": "economic pain"}]},
    {"person": "PM_B", "date": "2026-05-09", "quotes": [
      {"text": "매주 같은 미팅 다시 정리", "theme": "repeated workflow"}]},
    {"person": "PM_C", "date": "2026-05-10", "quotes": [
      {"text": "일반 AI 챗봇 쓰는데 톤이 매번 달라요", "theme": "current workaround"}]},
    {"person": "PM_D", "date": "2026-05-10", "quotes": [
      {"text": "고객 답신 못 보내면 deal 깨져요", "theme": "economic pain"}]},
    {"person": "PM_E", "date": "2026-05-11", "quotes": [
      {"text": "써보고 싶어요", "theme": "future intent"}]}
  ]
}
EOF
python3 hplan/scripts/interview_synthesis.py import /tmp/ai_export.json
```

## Tag PM_A, PM_C, PM_D as strong push

```bash
python3 hplan/scripts/interview_synthesis.py tag q-XXX-A --strength strong --axes push,anxiety
python3 hplan/scripts/interview_synthesis.py tag q-XXX-C --strength strong --axes push,workaround
python3 hplan/scripts/interview_synthesis.py tag q-XXX-D --strength strong --axes push,anxiety
```

## Audit

```json
{
  "interviews": 5,
  "tagged_quotes": 3,
  "by_strength": {"strong": 3},
  "persons_with_strong_push": ["PM_A", "PM_C", "PM_D"],
  "verdict": "PROCEED_TO_PRODUCT_GATE",
  "guidance": ["Repeated Push pattern confirmed across 3+ of 5+ interviews. Product Gate may begin."]
}
```

## Why this is *good*

- **AI did the extraction** (quotes pulled from transcripts) — efficient
- **Human did the judgment** (strong/medium/weak + axes) — fidelity preserved
- 3 distinct persons share strong-push 패턴 — Product Gate로 갈 자격
- PM_E의 "써보고 싶어요"는 의도적으로 *태깅 안 함* — future intent는 evidence 아님
