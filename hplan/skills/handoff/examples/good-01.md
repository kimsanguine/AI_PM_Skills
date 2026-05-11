# Good Example — SocialDraft brief → all 4 targets

## Run

```bash
python3 hplan/scripts/export_handoff.py socialdraft_brief.json --target all --root .
```

## Output (실측)

```json
{
  "written": [
    "harness/exports/spec-kit/specs/001-socialdraft-v2/spec.md",
    "harness/exports/spec-kit/specs/001-socialdraft-v2/plan.md",
    "harness/exports/spec-kit/specs/001-socialdraft-v2/tasks.md",
    "harness/exports/kiro/.kiro/specs/socialdraft-v2/requirements.md",
    "harness/exports/kiro/.kiro/specs/socialdraft-v2/design.md",
    "harness/exports/kiro/.kiro/specs/socialdraft-v2/tasks.md",
    "harness/exports/gstack/office-hours-brief.md",
    "harness/exports/claude/AGENTS.md",
    "harness/exports/claude/CLAUDE.md"
  ]
}
```

## GStack brief 미리보기 (excerpt)

```markdown
# /office-hours Input — SocialDraft

## Problem
솔로 PM이 미팅 직후 60초 안에 결과물을 못 만든다

## Counter Position
범용 AI 챗봇은 단발성 답변, SocialDraft는 브랜드 톤 학습 + 5개 동시 생성

## What We Will Not Build
- 일반 음성 받아쓰기
- CRM first-class

## Economic Guardrails
- COGS ceiling: $2.70/paid user/month
- Target gross margin: 70%

## Next GStack Steps
1. /office-hours — challenge wedge
2. /plan-ceo-review — confirm scope
3. /qa /review /ship
```

## Why this is *good*

- 같은 brief → 4개 ecosystem 동시 export (재작성 없음)
- 각 ecosystem 네이티브 convention (spec-kit specs/001-, Kiro .kiro/specs, GStack office-hours) 그대로
- "What We Will Not Build" + COGS ceiling이 모든 export에 박힘 → 다른 PM이 받아도 boundary 명확
