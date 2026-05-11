# Good Example — infographic-gif-creator 스킬

## 사용자 요청

"3-Tier 에이전트 아키텍처를 애니메이션 GIF로 설명해줄래? 사용자 입력 → Orchestrator → Sub-agent 순차 등장으로, README에 삽입 가능하게."

## 승인 이유

- 아키텍처를 애니메이션으로 시각화하여 이해도 상향
- 이해관계자 커뮤니케이션용 GIF 필요
- 문서/README에 바로 삽입 가능

## 예상 처리

1. 장면 설계: "3-Tier 순차 등장", 핵심 메시지, 루프형
2. HTML/CSS 구현: 각 계층이 순차적으로 나타나는 애니메이션
3. 캡처: Puppeteer로 프레임 캡처 (1280×720)
4. 인코딩: 2-pass palettegen (12fps, 3~4MB)
5. QA: 루프 연결성, 텍스트 가독성 확인

## 최종 결과물

1280×720, 12fps GIF로 3-Tier 아키텍처를 직관적으로 설명하는 인포그래픽
