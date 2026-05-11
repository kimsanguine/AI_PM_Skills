# Bad Example — Handoff without Build Gate approval

## Bad sequence

```bash
# COGS는 아직 안 돌렸음
# evidence-rubric은 interview 결정만 나옴
python3 hplan/scripts/export_handoff.py brief.json --target spec-kit
```

## What happens

- `gate_guard.py` hook 활성화된 프로젝트라면 → **PRD.md/spec.md write 자체가 차단** (exit 2).
- hook 없는 프로젝트라면 → handoff는 실행되지만 brief의 cogs_ceiling이 "TBD"라 downstream에서 의미 없음.

## Why this fails

- "다음 단계로 가기"가 게이트의 목적이 아니라 **게이트가 통과되어야 다음 단계로 갈 자격이 생긴다**.
- COGS unknown 상태에서 spec-kit specs를 만들면 → 구현팀이 비용 ceiling 모른 채 무제한 free tier 디자인 가능 → Replit-style 마진 붕괴 시나리오.

## Anti-pattern lessons

1. **handoff는 last step**. evidence-rubric → interview-synthesis → ost → cogs-sentinel → decision-log → handoff.
2. **brief의 모든 field가 채워져 있어야** downstream에서 의미 있음. "TBD" 마커가 많으면 게이트 미통과 신호.
3. **PreToolUse hook을 절대 disable로 두지 말 것** — 사고 방지.

## Recovery

1. `decision-log audit`으로 현재 결정 상태 확인.
2. cogs-sentinel 실행해서 GREEN 또는 CONDITIONAL_GO 확보.
3. brief 다시 작성 (cogs_ceiling 채움).
4. 그제야 handoff.
