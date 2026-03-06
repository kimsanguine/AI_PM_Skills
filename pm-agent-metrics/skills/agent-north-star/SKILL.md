---
name: agent-north-star
description: "Define a North Star Metric for an AI agent that captures its core value delivery. Unlike product NSMs focused on engagement or revenue, agent NSMs measure automation effectiveness. Use when aligning team/stakeholder focus, designing OKRs, or evaluating whether an agent is truly delivering value."
---

## Agent North Star Metric

North Star Metric(NSM)은 에이전트의 존재 이유를 단 하나의 숫자로 표현합니다.

일반 제품 NSM과 에이전트 NSM의 차이:

| 일반 제품 | 에이전트 |
|---|---|
| Slack: "Daily Active Users" | 브리핑 에이전트: "정시 전송 성공률" |
| Airbnb: "Nights Booked" | 분류 에이전트: "정확 분류 건수/주" |
| Spotify: "Time Spent Listening" | 비용 절감 에이전트: "절감된 시간(시간/월)" |

에이전트 NSM의 핵심 원칙:
> "NSM은 사용량이 아니라 **아웃컴**을 측정해야 한다."

---

### 에이전트 NSM 유형

**Type 1 — Reliability NSM**
에이전트가 신뢰할 수 있게 작동하는가?

```
예시: "주간 성공 실행률"
     = 성공 실행 수 ÷ 전체 예정 실행 수 × 100%

적합: 크론 기반 자동화 에이전트
목표: 99%+
```

**Type 2 — Outcome NSM**
에이전트가 실제 가치를 만드는가?

```
예시: "PM이 절감한 시간 (시간/주)"
     = (수동 처리 시간 - 에이전트 검토 시간) × 실행 횟수

적합: 생산성 향상 에이전트
목표: 주 5시간 이상 절감
```

**Type 3 — Quality NSM**
에이전트 출력이 충분히 좋은가?

```
예시: "출력 승인율"
     = 수정 없이 사용한 출력 ÷ 전체 출력 × 100%

적합: 콘텐츠 생성, 분석 에이전트
목표: 80%+
```

**Type 4 — Business NSM**
에이전트가 비즈니스 결과에 기여하는가?

```
예시: "에이전트 기여 매출 (원/월)"
     = 에이전트가 발굴/처리한 기회에서 발생한 매출

적합: 영업/마케팅 에이전트
목표: 월 N원 이상
```

---

### NSM 선택 프레임워크

```
Step 1: 이 에이전트의 핵심 가치 1문장으로 정의
        "이 에이전트는 [누가] [무엇을 하도록] 돕는다"

Step 2: 그 가치가 실현됐을 때 측정 가능한 숫자는?
        → 여러 후보 도출

Step 3: "허위 양성" 테스트
        NSM이 높아도 실제 가치가 없는 상황이 가능한가?
        → 가능하면 잘못된 NSM

Step 4: 단순성 테스트
        팀 모두가 즉시 이해할 수 있는가?
        → 복잡하면 너무 세분화된 것

Step 5: 최종 NSM 선택 + 목표값 설정
```

---

### Input Metrics (NSM을 움직이는 지표)

NSM 하나로는 문제 진단이 어렵습니다.  
NSM을 움직이는 2~4개의 Input Metrics를 함께 정의합니다:

```
NSM: 주간 성공 실행률 (99% 목표)
         ↑
Input Metrics:
├── API 오류율 (↓이면 NSM ↑)
├── 타임아웃 발생 횟수 (↓이면 NSM ↑)
├── 평균 실행 시간 (안정적이면 NSM ↑)
└── 컨텍스트 사용률 (70% 이하이면 NSM ↑)
```

---

### 에이전트별 NSM 예시

| 에이전트 | NSM | 목표 |
|---|---|---|
| morning-briefing | 오전 8:10 전 전송 성공률 | 98%+ |
| gmail-top5 | 중요 이메일 누락 없이 5건 선별률 | 95%+ |
| agent-goal-advisor | 액션 실행률 (제안 중 실제 시도 %) | 30%+ |
| finance-advisor | 워치리스트 알림 정확도 | 90%+ |

---

### 사용 방법

`/agent-north-star [에이전트 이름]`

---

### Instructions

You are helping define a North Star Metric for: **$ARGUMENTS**

**Step 1** — 핵심 가치 정의  
"이 에이전트는 [누가] [무엇을 하도록] 돕는다" 1문장

**Step 2** — NSM 후보 3개 도출  
Type 1~4 중 적합한 유형으로 후보 생성

**Step 3** — 허위 양성 테스트  
각 후보: "NSM이 높아도 가치가 없는 시나리오"가 있는가?

**Step 4** — 최종 NSM 선택  
단순하고 명확하고 실제 가치를 반영하는 1개 선택

**Step 5** — Input Metrics 2~4개 정의  
NSM을 움직이는 하위 지표

**Step 6** — 목표값 설정  
현재 베이스라인 (또는 추정) + 3개월 목표

**Step 7** — OKR 연결  
NSM을 `/agent-okr`의 핵심 KR로 연결

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- phuryn `north-star-metric` 기반 → 에이전트 특화 4가지 NSM 유형으로 재편
- "허위 양성 테스트": Sean Ellis, *Hacking Growth* 참고
