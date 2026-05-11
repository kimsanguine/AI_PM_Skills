# Good Example — SocialDraft idea, scored 80/100 → `interview`

## Input

```json
{
  "idea": "마케팅 담당자가 SNS 게시글 초안을 한 번에 5개 만들어주는 AI 글쓰기 도우미",
  "target": "주 10건 이상 SNS 콘텐츠를 직접 작성하는 1인 마케터 또는 2-3명 소규모 마케팅팀 (현재는 범용 AI 챗봇에 매번 수동 프롬프트)",
  "hypothesis": "미팅 직후 30-60분을 결과물 정리에 쓰는데, 늦어지면 같은 안건이 다음 미팅에서 반복된다",
  "alternatives": "범용 AI 챗봇 수동 프롬프트, 카피 자동화 SaaS, 노션의 AI 글쓰기 기능, 외주 카피라이터",
  "features": "5개 변형 한 번에 생성, 브랜드 가이드 자동 적용, Mermaid 다이어그램",
  "interview_notes": "마케터 A: 매주 월요일에 한 주치 SNS 콘텐츠 만드는데 4시간 걸려요. 캠페인 데드라인 놓치면 노출 손실.\n마케터 B: 일반 AI 챗봇 결과가 매번 톤이 달라서 다시 다듬는 시간이 더 들어요.\n마케터 C: 외주는 한 건당 3-5만원인데 6시간 뒤에 와요. 수정도 1-2회 필요."
}
```

## Why this is a *good* input

- **ICP behavior**: "주 10건+ SNS 콘텐츠 작성 + 범용 AI 챗봇 수동 사용" — 행동 + 현재 도구 명시. 인구통계만 있는 게 아니다.
- **Recent painful event**: "지난주에 30분 또 날렸어요" — 30일 안의 사건.
- **Current workaround**: the existing market alternatives/ChatGPT/수작업 5개 — 사용자가 이미 시간/주의를 지불 중.
- **Economic pain**: "안 되면 영업 못 따요", "deal 깨져요" — 매출 손실.
- **Switching trigger**: "범용 AI 챗봇 결과물의 톤 일관성 부족" — 이유 명시.
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
