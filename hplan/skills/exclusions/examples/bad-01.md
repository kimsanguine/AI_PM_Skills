# Bad Example — Vague exclusion that won't help future runs

## Add (bad)

```bash
python3 hplan/scripts/exclusions_registry.py add "이거" \
  --why "별로" \
  --reopen "나중에"
```

## Why this fails

- `exclusion = "이거"` — 토큰화하면 1 token. Future check가 collision을 잡지 못함.
- `why = "별로"` — 6개월 뒤 누구도 이게 왜 막혔는지 모름.
- `reopen_trigger = "나중에"` — 행동 가능한 evidence 아님 → 영구 차단과 같음.
- `--competitor` 없음 — 누구한테 진 건지 모름.

## Anti-pattern lessons

1. **모호한 exclusion은 미래의 자기 자신을 막는다**.
2. `reopen_trigger`는 *어떤 evidence가 들어오면 reopen하나*를 측정 가능한 형태로.
3. competitor 없는 exclusion은 **검색이 안 된다**.
