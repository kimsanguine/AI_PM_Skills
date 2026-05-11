# Good Example — MeetFlow v2 idea, scored 80/100 → `interview`

## Input

```json
{
  "idea": "솔로 PM이 클라이언트 미팅 직후 60초 안에 액션 아이템·후속 메일 초안을 자동 생성하는 도구",
  "target": "주 5회 이상 외부 클라이언트 미팅을 진행하는 B2B SaaS PM/창업자 (현재 Granola를 buffer로만 사용)",
  "hypothesis": "미팅 직후 30-60분을 결과물 정리에 쓰는데, 늦어지면 같은 안건이 다음 미팅에서 반복된다",
  "alternatives": "Granola, Otter, Fireflies, 수작업 정리, ChatGPT 복붙",
  "features": "60초 액션 아이템 초안, 후속 메일 1-click, Mermaid 다이어그램",
  "interview_notes": "PM_A: 지난주에 30분 또 날렸어요. 안 되면 영업 못 따요.\nPM_C: Granola 쓰는데 결과물이 부족해서 매번 다시 정리.\nPM_D: 고객 답신 못 보내면 deal 깨져요. 매주 반복."
}
```

## Why this is a *good* input

- **ICP behavior**: "주 5회 외부 미팅 + Granola buffer로만 사용" — 행동 + 현재 도구 명시. 인구통계만 있는 게 아니다.
- **Recent painful event**: "지난주에 30분 또 날렸어요" — 30일 안의 사건.
- **Current workaround**: Granola/Otter/Fireflies/ChatGPT/수작업 5개 — 사용자가 이미 시간/주의를 지불 중.
- **Economic pain**: "안 되면 영업 못 따요", "deal 깨져요" — 매출 손실.
- **Switching trigger**: "Granola 결과물이 부족해서" — 이유 명시.
- **MVP narrowness**: features 3개 — 좁다.
- **Repetition**: "매주 반복".

## Output (실측)

```
decision: interview (인터뷰 먼저)
score: 80/100
missing axes: ['Acquisition path to first 5 users']
```

## Why `interview`, not `build`?

점수는 75+를 넘었지만 **interview_notes가 3 lines + 강한 경제적 통증이 명시**되어 build를 제안할 수 있는데도, `Acquisition path to first 5 users` 점수가 낮아 build에 도달하지 못함. **5명을 어디서 만날지 모르면 build 안 된다**.

## Next Action

- `interview-synthesis` skill로 라우팅
- 5명 distinct strong-push pattern까지 인터뷰 진행
- Acquisition path 명시 (LinkedIn DM 20명, 특정 커뮤니티 등)
