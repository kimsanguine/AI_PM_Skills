# 나쁜 예제 — 3-Tier Pattern

## 사용자 요청
"에이전트 3개가 있으니 Prometheus → Atlas → Workers 구조로 만들어서 무조건 모든 작업을 3-tier로 통과시키면 되지 않을까?"

## 거절 이유
- **단순한 순차 작업**에 3-tier 구조는 오버엔지니어링
- Prometheus가 없거나 명확하지 않음 (전략적 의사결정 부재)
- 모든 작업을 Atlas를 통해 강제하면 그냥 자동화 시스템 (의도적 설계 아님)
- 통신 프로토콜 미정의로 각 계층이 서로 이해 못함

## 올바른 라우팅
- **2개 이하의 에이전트**: Orchestration 스킬의 Sequential 또는 Parallel 패턴 사용
- **3개 이상이지만 간단한 파이프라인**: Orchestration의 Sequential Chain으로 충분
- **3개 이상 + 전략 필요 + 조율 필요**: 3-Tier 패턴 적절

## 수정 방향
"우리 문제가 정말 3-tier 수준인가?" → Orchestration 스킬으로 먼저 패턴 재평가
"전략(Prometheus), 조율(Atlas), 실행(Workers)의 역할이 명확한가?" → 각 계층의 책임과 통신 형식 정의
"더 간단하게 할 수는 없나?" → 단순한 Sequential이면 충분할 수도 있음
