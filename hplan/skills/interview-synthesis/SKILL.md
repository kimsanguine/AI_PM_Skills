---
name: interview-synthesis
description: "Import AI synthesis output (BuildBetter MCP, Perspective AI, Granola, Otter) into hplan, then force a human to tag each quote with strength (strong/medium/weak) and Push/Pull/Habit/Anxiety/workaround/trigger axes. AI extracts quotes; humans assign evidence strength. Audits the SKILL.md rule: 5 interviews with 3 distinct strong-Push signals → proceed to Product Gate."
argument-hint: "[import|tag|audit|list] <path or id>"
allowed-tools: ["Read", "Write", "Bash"]
model: sonnet
---

# Interview Synthesis — AI Extracts, Human Tags

## Core Goal

- 2026 현실 반영 — 78% PM 팀이 AI 합성 사용. **차단하지 말고 받아들이되, evidence strength 태깅은 인간에게 강제**.
- AI는 quote 추출 + 테마 클러스터링; 인간은 strong/medium/weak + Push/Pull/Habit/Anxiety 축 부여.
- "5 interviews 중 3명이 같은 강한 Push를 말하면 Product Gate로" 규칙을 코드로 강제 (`PROCEED_TO_PRODUCT_GATE` verdict).

## Trigger Gate

### Use This Skill When

- BuildBetter / Perspective / Granola / Otter export JSON이 손에 있을 때
- 인터뷰 5건 이상 — 수동 정리는 비용 비효율적
- `evidence-rubric` 점수에서 `interview_notes` 보강이 필요할 때
- 신규 PM이 인터뷰 evidence를 어떻게 태깅해야 하는지 학습할 때

### Route to Other Skills When

- 5/3 패턴 통과 → Product Gate (`ost` skill)
- 5명 미만 → 추가 인터뷰 (skill 외 실세계 행동)
- 태그된 quote 강도가 너무 낮음 → `pivot` 또는 `hold` 결정 → `decision-log`

### Boundary Checks

- ❌ AI 합성이 evidence를 *대체할 수 없다*. 태그 안 된 quote는 evidence가 아니다.
- ❌ AI sentiment ≠ evidence strength. 인간이 직접 판단.

## Inputs

Expected AI export JSON shape:

```json
{
  "source": "buildbetter",
  "interviews": [
    {
      "person": "ICP candidate 1",
      "date": "2026-05-09",
      "quotes": [
        {"text": "지난주에 30분 또 날렸어요", "theme": "manual workaround"},
        {"text": "이거 안 되면 영업 못 따요", "theme": "economic pain"}
      ]
    }
  ]
}
```

## Steps

1. `interview_synthesis.py import <ai_export.json>` — quotes를 `harness/evidence/snapshots.jsonl` 에 ingest (status: awaiting_human_tag).
2. `list --untagged` — 미태깅 quote 확인.
3. quote마다 `tag <quote_id> --strength strong --axes push,anxiety` — 인간 입력.
4. `audit` — 5/3 규칙 통과 여부 + 다음 액션 가이드.

## Outputs

- `harness/evidence/snapshots.jsonl` — append-only quote 저장소
- audit returns: `interviews, tagged_quotes, untagged_quotes, by_strength, persons_with_strong_push, verdict, guidance`

## Verification

- [ ] 모든 imported quote는 처음에 `status: awaiting_human_tag`
- [ ] tag 후 `status: tagged`, `strength`, `axes`, `tagged_at` 채워짐
- [ ] verdict는 `PROCEED_TO_PRODUCT_GATE` (5인터뷰 + 3 distinct strong-push) 또는 `INTERVIEW_OR_HOLD`

## Why this design

다른 인터뷰 도구들은 "AI summary"를 evidence처럼 다룬다 — 위험. 한 LLM이 5개 인터뷰를 요약하면 자기 bias가 들어감. hplan은 **AI = quote 추출기**, **human = strength 판단**으로 명확히 분리.
