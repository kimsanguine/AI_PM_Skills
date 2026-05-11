# Good Example — instruction 스킬

## 사용자 요청

"뉴스 수집 에이전트의 instruction을 완전히 다시 설계해줄래? 지금은 역할만 정의돼있고 Anti-Goals도 없어서 에이전트가 예상 밖으로 행동해."

## 승인 이유

- 에이전트의 일관된 행동 기준이 부족
- 7요소(Role/Context/Objective/Tools/Memory/Output/Failure) 중 일부만 정의됨
- Anti-Goals가 명시되지 않아 예외 상황에서 판단 기준 없음

## 예상 처리

1. Role 재정의: "뉴스 큐레이터(PM 관점)로서 단순 요약이 아닌 인사이트 중심"
2. Context 추가: "PM 사용자, 매일 아침 8시 Cron 실행, 영어/한국어 모두 이해"
3. Objective 확장: Primary Goal 1개 + Secondary Goals 3개 + Anti-Goals 4개
4. Tools 명시: web_search(조건: 캐시 부족 시만), read_file, write_file, message
5. Memory 3계층 정의: 단기(SOUL.md), 장기(어제 뉴스 캐시), 절차적(요약 스타일 SKILL)
6. Output Format: Telegram, Markdown, 최대 500자, 한국어, 이모지 활용
7. Failure Handling: 4가지 실패 시나리오별 대응 방법

## 최종 결과물

7요소가 완성된 Instruction 세트로 개발자가 이것만으로 에이전트 동작 구현 가능
