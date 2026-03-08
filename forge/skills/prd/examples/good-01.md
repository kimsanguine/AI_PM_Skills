# Good Example — prd 스킬

## 사용자 요청

"비용 분석 에이전트(cost-analyst)를 정식 구현하기 전에 완전한 Agent PRD를 작성해줘. 지난 3개월 비용 데이터, 절감 기회 식별, 그리고 실패 처리까지 모두 포함해야 해."

## 승인 이유

- 프로토타입 검증이 완료되었고 구현팀에 넘기기 전 공식 명세서 필요
- 에이전트의 모든 설계 요소(지시사항, 도구, 메모리, 트리거, 출력, 실패 처리)를 7개 섹션으로 체계화해야 함
- 기술 스펙과 사업 가치를 동시에 명시해야 함

## 예상 처리

1. Section 1 Overview 작성: 에이전트 이름, 한 줄 정의, 배경
2. Section 2 Instruction Design: Role, Primary Goal, Secondary Goals, Anti-Goals 정의
3. Section 3 Tools & Integrations: Google Cloud Billing API, Anthropic API, 파일 읽기/쓰기, Telegram 메시지 메시징 도구 목록
4. Section 4 Memory Strategy: 3계층 메모리(Working/Long-term/Procedural) 계획
5. Section 5 Trigger & Execution: Cron 트리거(매월 1일), Step-by-Step 실행 흐름
6. Section 6 Output Specification: Telegram Markdown 포맷, 최대 1000자, 한국어, CSV 첨부
7. Section 7 Failure Handling & Success Metrics: 실패 시나리오 테이블(4개 이상), 성공 지표 5개 정의

## 최종 결과물

완전한 Agent PRD 문서로 구현팀이 이 문서만으로도 코드 작성 가능한 수준의 명세서
