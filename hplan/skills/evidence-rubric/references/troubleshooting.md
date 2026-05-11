# troubleshooting — evidence-rubric

## "Score keeps showing 0 even with detailed input"

- 입력 JSON의 field name 오타? `target`이 아니라 `audience`로 적었다면 점수 0.
- `interview_notes`가 `[]` 배열이면 안 됨 — single string with newlines.

## "Decision is `interview` but I have 5 interviews"

- `interview_notes`가 한 줄당 ≥ 9 chars여야 1 line으로 카운트됨.
- 짧은 발화("좋아요", "Yeah")는 카운트 안 됨 — 의도된 noise filter.

## "Decision is `build` but I want to push back"

- `build`는 추천이지 명령이 아님.
- `decision-log` skill로 기록해두면 3-6개월 뒤 audit으로 hit-rate 측정 가능.

## "Score 80인데 missing이 비어있지 않다"

- 정상. 80점이라도 한두 축이 < 55%면 missing에 표시됨.
- 다음 인터뷰에서 그 축을 우선 보강.

## "Sequence는 어떻게?"

```
evidence-rubric  →  (점수 낮으면) interview-synthesis
              →  (collision 의심) exclusions check
              →  (점수 OK) cogs-sentinel  →  decision-log  →  handoff
```
