---
name: build-or-buy
description: "Decide whether to build a custom agent, buy/subscribe to an existing solution, or use a no-code/low-code platform. Use before committing to agent development — this decision affects cost, time-to-value, differentiation, and long-term maintenance burden. Prevents the 'build everything from scratch' default trap."
argument-hint: "[agent concept to evaluate]"
allowed-tools: ["Read", "Write", "WebSearch", "WebFetch"]
model: sonnet
---

## Core Goal

- 에이전트 단위로 Build/Buy/No-Code 선택지를 데이터 기반으로 평가하여 개발 리소스와 시간을 낭비하지 않도록 함
- 6개 평가 항목(차별화, 속도, 비용, 커스터마이징, 유지보수, 도메인 특화)에 점수를 부여하고 가중치를 적용하여 최적 선택지를 도출
- 하이브리드 전략을 통해 핵심 레이어는 Build, 주변 레이어는 Buy/No-Code로 혼합하여 최대 효율성 달성

---

## Trigger Gate

### Use This Skill When
- 에이전트 기회를 선택한 후, "이걸 직접 만들까? 사야 할까?"를 결정해야 할 때
- 외부 솔루션이 존재하는데도 팀이 "직접 만드는 게 낫다"고 주장할 때 (또는 반대)
- 개발 리소스가 부족한데 에이전트를 여러 개 구현해야 할 때
- 동일한 에이전트를 여러 번 구현할 기회가 있을 때 (예: 여러 부서의 유사한 요청)

### Route to Other Skills When
- Build 선택 후 에이전트의 아키텍처와 프롬프트를 설계해야 할 때 → `agent-instruction-design` (forge 플러그인)
- Buy 선택 후 외부 솔루션을 우리 워크플로우에 통합해야 할 때 → 통합 가이드 문서 (별도)
- 하이브리드 전략의 오케스트레이션 레이어를 설계할 때 → `agent-gtm` (launch/integration 단계)

### Boundary Checks
- **에이전트 단위 평가**: Build-or-Buy는 전체 제품이 아니라 개별 에이전트(또는 에이전트 모듈)에 대해 결정하는 것 — 같은 제품도 일부는 Build, 일부는 Buy일 수 있음
- **재검토 트리거**: 처음 결정이 최종 결정이 아님 — 6개월마다 또는 선택지 평가 항목이 크게 변하면 재검토 권장

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
- 에이전트 오케스트레이션: 직접 구축 (production agent workspace + Claude)
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

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---|---|---|
| Build 선택 후 유지보수 비용이 예상 대비 3배 이상 높음 | 6개월 후 리뷰에서 "매주 디버깅에 16시간씩 쓴다" 데이터 | Build → Buy 재검토; 외부 솔루션 비용이 월 $500 이하면 즉시 전환 권장 |
| Buy 선택 했는데 솔루션의 커스터마이징 한계에 부딪힘 | 구현 후 "우리 요구사항의 30%만 지원한다" 판명 | No-Code 통합 레이어로 임시 해결하고 Build 전환 검토; 또는 다른 솔루션 탐색 |
| No-Code 선택 후 확장이 필요해졌는데 플랫폼 한계 직면 | 사용량 증가 후 "Rate Limit 또는 복잡도 한계" 발생 | No-Code → Build 전환; 검증된 프롬프트와 워크플로우는 그대로 이관 가능 |
| 하이브리드 전략이 너무 복잡해짐 (레이어 4개 이상) | 통합 지점이 3개 이상, 팀이 "관리가 어렵다" 호소 | 단순화: 핵심 2개 레이어만 남기고 나머지는 단일 솔루션으로 통합 |

---

## Quality Gate

- 평가 항목 6가지(차별화, 속도, 비용, 커스터마이징, 유지보수, 도메인)에 Build/Buy/No-Code 각각 점수가 매겨져 있는가? (Yes/No)
- 프로젝트 맥락에 맞는 가중치가 명시되어 있는가? (e.g., "속도가 최우선이므로 4배 가중치") (Yes/No)
- 최소 2~3개의 외부 솔루션이 조사되었고, 각각의 비용/제약/커스터마이징 한계가 비교 표로 정리되어 있는가? (Yes/No)
- 최종 추천 선택지(Build/Buy/No-Code 또는 하이브리드)의 근거가 3가지 이상 명시되어 있는가? (Yes/No)
- 재검토 트리거 조건(예: "6개월 후", "유지보수 시간이 월 20시간 초과", "외부 솔루션 비용이 월 $300 초과")이 정의되어 있는가? (Yes/No)

---

## Examples

### Good Example

```
Scenario: "고객 티켓 자동 분류 에이전트"

평가:

| 항목 | Build | Buy | No-Code | 가중치 |
|------|-------|-----|---------|--------|
| 차별화 기여도 | 4 | 1 | 1 | 3x |
| 구현 속도 | 2 | 5 | 5 | 2x |
| 장기 비용 | 4 | 2 | 3 | 1x |
| 커스터마이징 자유도 | 5 | 2 | 3 | 2x |
| 유지보수 부담 | 3 | 5 | 4 | 1x |
| 도메인 특화 | 5 | 1 | 2 | 2x |

가중 합계:
- Build: 4×3 + 2×2 + 4×1 + 5×2 + 3×1 + 5×2 = 51점
- Buy: 1×3 + 5×2 + 2×1 + 2×2 + 5×1 + 1×2 = 23점
- No-Code: 1×3 + 5×2 + 3×1 + 3×2 + 4×1 + 2×2 = 28점

최종 추천: Build (51점)

근거:
1. 고객 분류는 우리 도메인 데이터(과거 티켓 내용)에 최적화할 수 있음 → 차별화 가능
2. 경쟁사 솔루션은 70% 이상 요구사항 미충족 (너무 일반적)
3. 도메인 특화도가 높아서 Build 투자 정당화 가능

재검토 트리거:
- "3개월 후 유지보수 시간 > 월 20시간이면 Buy 재검토"
- "외부 솔루션이 우리 요구사항 80% 이상 지원하면 즉시 Buy 전환"
```

### Bad Example

```
❌ 평가 항목이 불완전:
"Build가 더 낫다" (근거 없음)
→ 6개 항목 점수 매김 필수; 주관적 판단은 위험

❌ 외부 솔루션 조사 부족:
"우리가 만드는 게 제일 좋다"
→ But: 비슷한 솔루션이 이미 10개 이상 존재할 수 있음
→ 최소 2~3개 솔루션 비교 필수

❌ 가중치 설정 불합리:
"모든 항목에 동일 가중치"
→ But: 프로젝트는 속도가 최우선인데도 차별화와 동일하게 평가
→ 맥락 반영: "우리는 빠르게 검증하고 싶으므로 속도를 2배 가중치"

❌ 하이브리드 전략이 너무 복잡:
"오케스트레이션 레이어: Build
 도메인 로직: Build
 외부 연동: Buy (Zapier + SendGrid + Slack)
 UI: Buy
 모니터링: Buy
 백업: No-Code (Google Sheets)"

→ 통합 지점이 6개 이상 → 관리 불가능
→ 단순화: "핵심 (오케스트레이션 + 도메인): Build / 나머지 모두: Buy (통합 플랫폼)"

❌ 재검토 트리거 없음:
"Build 선택. 끝!"
→ But: 6개월 후 유지보수 비용이 달라질 수 있음
→ 재검토 조건 명시 필수: "월 유지보수 시간 > 20시간" 또는 "월 운영 비용 > $1000"
```

---

### 참고
- 설계자: AI PM Skills Contributors, 2026-03
- 하이브리드 전략 원칙: MCP-Skills 레이어 설계에서 발전
- 재검토 트리거: production agent workspace 운영 경험 기반 (cron job build-or-buy 반복 경험)

---

## Further Reading
- Marty Cagan, *INSPIRED* — Build vs Buy decision frameworks
- Martin Fowler, "Build vs Buy" — Architecture decision trade-offs

## Contextual Knowledge (auto-loaded)

> 보조 파일이 존재할 때만 자동 로드됩니다. 파일이 없으면 건너뜁니다.

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`

### Test Cases
!`cat references/test-cases.md 2>/dev/null || echo ""`

### Troubleshooting
!`cat references/troubleshooting.md 2>/dev/null || echo ""`
