# Good Example — Adding Spec-Kit collision territory

## Add

```bash
python3 hplan/scripts/exclusions_registry.py add "범용 PRD 생성기" \
  --why "GitHub Spec-Kit이 30개 agent + 93K stars로 점유" \
  --reopen "Spec-Kit이 evidence gate를 추가하거나 enterprise compliance 인터뷰 3건+" \
  --competitor "GitHub Spec-Kit" --competitor "Kiro" --competitor "BMAD"
```

## Result

```json
{
  "id": "ex-2026-05-11-38213",
  "ts": "2026-05-11T...",
  "exclusion": "범용 PRD 생성기",
  "why": "GitHub Spec-Kit이 30개 agent + 93K stars로 점유",
  "reopen_trigger": "Spec-Kit이 evidence gate를 추가하거나 enterprise compliance 인터뷰 3건+",
  "owned_by_competitor": ["GitHub Spec-Kit", "Kiro", "BMAD"]
}
```

## 3개월 뒤 collision detect

```bash
python3 hplan/scripts/exclusions_registry.py check "범용 PRD 자동 생성 도구"
```

```json
{
  "verdict": "COLLISION",
  "matches": [{"overlap": 0.42, "id": "ex-2026-05-11-38213", ...}],
  "guidance": "Prior exclusion matched. Confirm the reopen_trigger is satisfied before continuing, or pivot."
}
```

## Why this is *good*

- `why`가 구체적 (점유자 + 규모)
- `reopen_trigger`가 행동 가능한 evidence (인터뷰 3건+) — 추상 단어 아님
- 6개월 뒤 새 PM이 같은 아이디어를 들고 와도 자동 차단
