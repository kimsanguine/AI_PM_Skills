---
name: build-or-buy
description: "Decide whether to build a custom agent, buy/subscribe to an existing solution, or use a no-code/low-code platform. Use before committing to agent development — this decision affects cost, time-to-value, differentiation, and long-term maintenance burden. Prevents the 'build everything from scratch' default trap."
argument-hint: "[agent concept to evaluate]"
---

## Build or Buy: 에이전트 의사결정 프레임워크

에이전트 개발에서 가장 흔한 실수:
- 외부 서비스로 충분한데 직접 구축 → 개발 시간 낭비
- 차별화 핵심인데 외부 솔루션에 의존 → 경쟁력 상실
- 빌드/바이 결정 없이 시작 → 중간에 방향 전환으로 매몰 비용 발생

이 스킬은 **에이전트 단위로** 빌드/바이/노코드 중 최적 선택지를 결정합니다.

---

### 의사결정 3가지 선택지

**Option A — Build (직접 구축)**
커스텀 에이전트를 처음부터 설계하고 구현

적합 조건:
- 이 에이전트가 핵심 차별화 요소
- 외부 솔루션이 없거나 요구사항의 70% 이상을 충족 못함
- 도메인 특화 데이터/워크플로우가 필요 (남에게 맡길 수 없음)
- 장기 운영이 확정되어 있음

비용 구조: 개발 시간 + 모델 API 비용 + 유지보수
예상 리드타임: 1~4주 (MVP 기준)

**Option B — Buy / Subscribe (구독/외부 서비스)**
기존 AI 에이전트 솔루션이나 SaaS를 활용

적합 조건:
- 범용 기능 (요약, 번역, 일정관리, 이메일 처리 등)
- 빠른 시간 내 검증이 필요한 실험
- 개발 리소스가 없거나 부족
- 규제/보안 이슈로 외부 솔루션이 더 안전

비용 구조: 구독료 (월 $20~$500+)
예상 리드타임: 즉시~3일

**Option C — No-Code / Low-Code 플랫폼**
Make, Zapier, n8n, Notion AI, 노션 워크플로우 등 활용

적합 조건:
- 트리거-액션 패턴이 명확한 단순 자동화
- 비기술 팀이 직접 운영해야 함
- 빠른 프로토타이핑 후 검증 먼저 필요
- 외부 SaaS 연동이 핵심 (Zapier 커넥터 활용)

비용 구조: 플랫폼 구독료 + 실행 횟수 과금
예상 리드타임: 1~3일

---

### 결정 트리

```
1. 이 에이전트가 핵심 차별화 요소인가?
   YES → Build (go to step 3)
   NO  → go to step 2

2. 외부 솔루션이 요구사항의 70% 이상 충족하는가?
   YES → Buy (go to step 4)
   NO  → go to step 3

3. 도메인 특화 데이터 / 판단 로직이 필요한가?
   YES → Build
   NO  → No-Code 플랫폼 검토

4. 개발 리소스 없이 즉시 검증이 필요한가?
   YES → No-Code 플랫폼 → 검증 후 Build 전환 검토
   NO  → Buy
```

---

### 평가 매트릭스

각 항목을 1(낮음)~5(높음)로 점수화:

| 평가 항목 | Build | Buy | No-Code |
|---|---|---|---|
| 차별화 기여도 | ★★★★★ | ★★☆☆☆ | ★☆☆☆☆ |
| 구현 속도 | ★★☆☆☆ | ★★★★★ | ★★★★☆ |
| 장기 비용 효율 | ★★★★☆ | ★★☆☆☆ | ★★★☆☆ |
| 커스터마이징 자유도 | ★★★★★ | ★★☆☆☆ | ★★★☆☆ |
| 유지보수 부담 | ★★★★☆ | ★☆☆☆☆ | ★★☆☆☆ |
| 도메인 특화 가능성 | ★★★★★ | ★★☆☆☆ | ★★★☆☆ |

**점수 계산**: 프로젝트 우선순위에 따라 항목별 가중치 부여 후 합산

---

### 하이브리드 전략 (권장)

단일 에이전트라도 레이어를 나눠 최적 선택을 섞을 수 있습니다:

```
[오케스트레이션 레이어]  → Build (Prometheus-Atlas)
[도메인 로직 레이어]     → Build (커스텀 Workers)
[외부 연동 레이어]       → Buy/MCP (Zapier, API 서비스)
[UI/채널 레이어]         → Buy (Telegram Bot, Slack App)
```

예시:
- 에이전트 오케스트레이션: 직접 구축 (OpenClaw + Claude)
- 이메일 발송: 외부 API (SendGrid 구독)
- 캘린더 연동: No-Code (Zapier 커넥터)

→ 핵심에 집중하고, 주변은 사는 전략

---

### 재검토 트리거

처음 결정이 맞지 않을 때 신호:
- **Build → Buy 전환**: 유지보수 시간이 실제 사용 시간보다 길 때
- **Buy → Build 전환**: 외부 솔루션 비용이 월 $500 초과하거나 커스터마이징 한계에 부딪힐 때
- **No-Code → Build 전환**: 검증 완료 후 스케일 필요 시

---

### 사용 방법

`/build-or-buy [만들려는 에이전트 또는 자동화 기능]`

---

### Instructions

You are helping decide the optimal strategy (Build / Buy / No-Code) for: **$ARGUMENTS**

**Step 1 — 요구사항 명확화**
- 이 에이전트가 해결하는 문제를 1문장으로 정의
- 핵심 기능 3가지 나열
- 사용자 및 사용 빈도 파악

**Step 2 — 차별화 판단**
- 이 에이전트가 제품/서비스의 핵심 차별화 요소인가?
- 경쟁사가 동일한 솔루션을 쉽게 구현할 수 있는가?
- 도메인 특화 데이터나 판단 로직이 필수인가?

**Step 3 — 외부 솔루션 조사**
- 요구사항을 70% 이상 충족하는 기존 솔루션 2~3개 탐색
- 각 솔루션의 비용, 제약, 커스터마이징 한계 확인

**Step 4 — 평가 매트릭스 적용**
- 6개 항목에 점수 부여
- 프로젝트 맥락에 따른 가중치 적용
- Build / Buy / No-Code 합산 점수 비교

**Step 5 — 하이브리드 전략 검토**
- 레이어별로 다른 선택지 조합 가능한가?
- 핵심 레이어는 Build, 주변 레이어는 Buy/No-Code

**Step 6 — 최종 권장 + 근거**
- 선택지 1개 추천 (또는 하이브리드 전략)
- 주요 근거 3가지
- 재검토 트리거 조건 명시

**Step 7 — 다음 단계 연결**
- Build 선택: `/agent-instruction-design`으로 연결
- Buy 선택: 선택한 솔루션의 통합 방법 가이드
- No-Code: 플랫폼 선택 기준 제공

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- 하이브리드 전략 원칙: MCP-Skills 레이어 설계에서 발전
- 재검토 트리거: OpenClaw 운영 경험 기반 (크론잡 build-or-buy 반복 경험)

---

## Further Reading
- Marty Cagan, *INSPIRED* — Build vs Buy decision frameworks
- Martin Fowler, "Build vs Buy" — Architecture decision trade-offs
