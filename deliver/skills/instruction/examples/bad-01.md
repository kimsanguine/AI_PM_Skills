# Bad Example — instruction 스킬

## 사용자 요청

"에이전트 지시를 좀 정리해줄래?"

## 거절 이유

- 어떤 에이전트인지 불명확
- 현재 Instruction 상태(완성도, 문제점)가 정의되지 않음
- 7요소 중 어떤 부분이 부족한지 불명확

## 올바른 라우팅

1. 에이전트 이름과 역할 확인
2. 기존 Instruction이 있으면 제공
3. 부족한 7요소 명시 후 스킬 호출

## 수정 방향

"뉴스 수집 에이전트(morning-briefing)의 Instruction을 완전히 다시 설계해줄래? 지금은 역할만 정의돼있고, Context, Tools, Memory, Output Format, Failure Handling이 모두 미정의 상태야. 7요소를 모두 포함해줘."
