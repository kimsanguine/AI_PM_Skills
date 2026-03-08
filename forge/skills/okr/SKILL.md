---
name: okr
description: "Design OKRs specifically for AI agents — defining measurable Key Results around accuracy, cost, reliability, and business impact. Use when setting performance goals for a deployed agent, reviewing agent effectiveness, or aligning agent metrics with business objectives."
argument-hint: "[agent to set OKRs for]"
allowed-tools: ["Read", "Write"]
model: sonnet
---

## Agent OKR

## Core Goal

- 에이전트 고유의 성과 측정을 위해 비즈니스 임팩트(시간/비용/오류 절감)와 운영 건강성(정확도/비용/신뢰성)의 2축 OKR 설계
- 측정 가능한 Key Result로 에이전트의 가치를 정량화하고, 주간/월간/분기 리뷰 사이클 수립으로 지속적 개선 추진
- 비용 KR을 항상 포함하여 스케일 시에도 운영 비용이 통제 가능한 범위 내에서 증가하도록 제약

---

## Trigger Gate

### Use This Skill When

- 새로운 에이전트가 배포될 때 초기 성과 목표 설정
- 배포된 에이전트의 분기별 성과 검토 및 다음 분기 OKR 재설정
- 에이전트 포트폴리오의 우선순위 결정이 필요할 때 (KR 달성률로 비교)
- 에이전트 개선 기회 식별 (비용 KR 초과, 정확도 KR 미달 등)

### Route to Other Skills When

- 에이전트 전체 설계 검증 필요 → `agent-plan-review` 스킬로 라우팅
- 비용 시뮬레이션/분석 필요 → `oracle/cost-sim` 스킬로 라우팅 (비용 KR의 베이스라인 추정)
- 신뢰성/SLO 설계 필요 → `argus/reliability` 스킬로 라우팅 (신뢰성 KR의 구체화)
- 비용 추적/모니터링 필요 → `argus/burn-rate` 스킬로 라우팅 (비용 KR 모니터링)

### Boundary Checks

- OKR은 기술 구현(API 호출, 프롬프트 최적화)은 아니며, **성과 측정 프레임워크**임
- Business Impact KR은 최소 1개, Operational Health KR도 최소 1개 필요 (한쪽으로 치우친 OKR 금지)
- 베이스라인(현재값)을 모르면 목표 설정 불가 → 처음 2주는 데이터 수집 기간으로 설정

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|----------|------|------|
| 비즈니스 임팩트 KR이 측정 불가능 (예: "사용자 만족도 높이기") | KR을 읽었을 때 정량화 방법이 불명확 | 프록시 지표로 변경 (예: "사용자 만족도" → "재사용률 80% 이상" 또는 "에이전트 호출 주 3회 이상") |
| 월간 리뷰 시 데이터 부재로 KR 달성률 계산 불가 | 주간 로그가 없거나 측정 도구 설정 안 됨 | 다음 달부터 자동 로깅 설정 (예: 성공/실패 건수 기록), 현재 달은 추정값으로 임시 평가 |
| KR이 너무 높게 설정되어 분기 중반부터 달성 불가능 확실 | 주간 검토 시 KR 달성 가능성 1% 미만 | 즉시 KR 재협상 (낮게 재설정하되, 이유 문서화 — 아키텍처 문제/스코프 미포함 등) |
| 비용 KR 초과 (예: 월 $50 예정이던 게 $150) | 비용 모니터링 중 임계값 초과 감지 | "원인 분석 + 즉시 수정" 액션 필요 (프롬프트 최적화/도구 호출 감소/배치 처리 전환 등) |
| 여러 에이전트의 KR이 충돌 (예: A 에이전트 비용 ↑ vs B 에이전트 비용 ↓) | 포트폴리오 리뷰에서 총합 비용이 예산 초과 | 우선순위 재조정 (고임팩트 에이전트에 리소스 집중), 저임팩트 에이전트 일시 중지 검토 |

---

## Quality Gate

- [ ] Objective: 야심차고 질적인 1개 명시 (Yes/No)
- [ ] Business Impact KR 2개: 시간/비용/오류 절감 중 2개 선택 (Yes/No)
- [ ] Operational Health KR 2개: 정확도/비용/신뢰성/레이턴시 중 2개 선택 (Yes/No)
- [ ] 각 KR: 현재값 → 목표값 → 달성 기한 명시 (Yes/No)
- [ ] 비용 KR 포함 여부 (항상 포함) (Yes/No)
- [ ] 베이스라인 데이터 수집 계획 (처음 2주 이상) (Yes/No)
- [ ] 측정 방법 정의 (자동/수동, 사용 도구) (Yes/No)
- [ ] 리뷰 사이클 설정 (주간/월간/분기) (Yes/No)

---

## Examples

### Good Example

```markdown
# Agent OKR — morning-briefing v2

## Objective
morning-briefing이 PM 담당자의 정보 수집 시간을 완전히 제로화하고,
매일 아침 8분 내에 핵심 정보를 신뢰 가능한 파트너로서 전달한다.

---

## Business Impact KRs

**KR1: 정보 수집 시간 절감**
- 측정: PM 담당자가 뉴스 수집에 쓰는 주간 시간 (현재: 주 5시간)
- 목표: 0시간 (morning-briefing이 대체)
- 목표값: 0시간 (브리핑 자동 수신)
- 목표 기한: 2026-03-31

**KR2: 정보 신뢰도 유지**
- 측정: PM 담당자 피드백 기반 "쓸모 있는 기사" 비율
- 현재: 미측정 (데이터 수집 기간)
- 목표: 80% 이상 (기사 5개 중 4개 이상이 읽을 가치 있음)
- 목표 기한: 2026-03-31

---

## Operational Health KRs

**KR3: 비용 효율성**
- 측정: 월간 API 비용 (Gemini + Claude)
- 현재: $0.50 (2026-01 실적)
- 목표: $2 이하 (스케일 여유 확보)
- 목표 기한: 2026-03-31

**KR4: 신뢰성 (No Timeout)**
- 측정: 월간 타임아웃 발생 건수
- 현재: 간헐적 (약 2회/월 추정)
- 목표: 0회/월
- 목표 기한: 2026-03-31

---

## 측정 방법

| KR | 자동/수동 | 도구/방법 |
|----|----------|---------|
| KR1 (시간 절감) | 수동 | PM 담당자의 주간 활동 로그 (매주 금요일 리뷰) |
| KR2 (신뢰도) | 수동 | PM 담당자의 월간 피드백 (Telegram 반응 점수) |
| KR3 (비용) | 자동 | Google Cloud + Anthropic 청구 API |
| KR4 (신뢰성) | 자동 | Sentry / 에이전트 실행 로그 |

---

## 리뷰 사이클

**주간 (매주 금요일):**
- KR1~4 현재 진행도 확인
- 이슈 발견 시 즉시 대응

**월간 (매월 마지막 금요일):**
- KR1~4 누적 성과 정산
- 원인 분석 (달성 또는 미달)
- 추가 액션 필요 여부 판단

**분기 (분기 말):**
- Objective 재검토 (여전히 유효한가?)
- 다음 분기 OKR 설정 (현재 데이터 기반)
- 에이전트 개선 기회 정의

---

초기 데이터 수집 기간: 2026-03-01 ~ 03-14 (2주)
정식 OKR 리뷰: 2026-03-15부터
```

### Bad Example

```markdown
# OKR — news-agent

Objective: news-agent가 좋은 뉴스를 잘 전달한다.

KR1: 정확도 향상
KR2: 비용 절감
KR3: 신뢰성 높이기

---

문제점:
- Objective가 추상적 ("좋은 뉴스", "잘 전달")
- KR이 측정 불가능 (수치/기준 없음)
- Business Impact KR인지 Operational Health KR인지 불명확
- 현재값 없음 → 목표 설정 불가능
- 달성 기한 없음 → 언제까지?
- 측정 방법 정의 없음 → 실제로 어떻게 측정?
- 리뷰 사이클 없음 → 주간/월간/분기 리뷰 계획 불명확
```

---

## Agent OKR

일반 제품 OKR과 에이전트 OKR의 차이:

| 일반 제품 OKR | 에이전트 OKR |
|---|---|
| KR: MAU 10만 달성 | KR: 에이전트 정확도 95% 달성 |
| KR: 전환율 3% 향상 | KR: 월 운영 비용 $50 이하 유지 |
| KR: NPS 50+ | KR: 타임아웃 발생률 1% 이하 |

에이전트는 사람이 직접 쓰는 제품이 아닙니다.  
에이전트의 성과는 **아웃컴**과 **운영 건강성** 두 가지로 측정합니다.

---

### 에이전트 OKR 2축 구조

**Axis 1 — Business Impact (비즈니스 임팩트)**
> 에이전트가 존재하는 이유 — 어떤 가치를 만드는가

측정 지표 유형:
- 시간 절감: "PM이 뉴스 수집에 쓰는 시간 주 5시간 → 0시간"
- 비용 절감: "반복 작업 자동화로 월 N시간 × 시급 절감"
- 매출 기여: "리드 발굴 에이전트 → 월 N건 추가 파이프라인"
- 오류 감소: "수동 데이터 입력 오류율 X% → Y%"

**Axis 2 — Operational Health (운영 건강성)**
> 에이전트가 지속 가능하게 작동하는가

측정 지표 유형:
- 정확도: "출력 품질 평가 점수 N% 이상"
- 비용: "월 API 비용 $N 이하"
- 신뢰성: "성공 실행률 N% 이상"
- 레이턴시: "평균 응답 시간 N초 이하"

---

### OKR 템플릿

**Objective:** [에이전트가 이번 분기에 달성할 가장 중요한 목표]

```
O: [에이전트 이름]이 [사용자]의 [문제]를 [방식]으로 해결하는
   신뢰할 수 있는 파트너가 된다.

KR1 (Business Impact):
   [측정 지표] [현재값] → [목표값] by [날짜]

KR2 (Business Impact):
   [측정 지표] [현재값] → [목표값] by [날짜]

KR3 (Operational Health):
   [측정 지표] [현재값] → [목표값] by [날짜]

KR4 (Operational Health):
   [측정 지표] [현재값] → [목표값] by [날짜]
```

---

### 실제 예시 — morning-briefing 에이전트

```
O: morning-briefing이 PM 담당자의 정보 수집 시간을 제로화하고
   매일 아침 10분 내에 하루 핵심 정보를 제공한다.

KR1: 브리핑 수신율 100% 유지 (현재: ~95%)
KR2: 브리핑 오전 8:00 전 전송 달성률 98% 이상
KR3: 월 API 비용 $2 이하 (현재: $0.5, 스케일 대비 여유 확보)
KR4: 타임아웃 발생 0회/월 (현재: 간헐적 발생)
```

---

### 에이전트 KR 설정 원칙

**원칙 1 — 측정 가능해야 한다**
```
❌ "에이전트가 잘 작동한다"
✅ "성공 실행률 99% 이상 (주 7일 × 1회 = 28회 중 27.7회 이상 성공)"
```

**원칙 2 — 비즈니스 임팩트 KR이 최소 1개**
```
운영 건강성 KR만 있으면 에이전트의 존재 이유가 불분명해짐
비즈니스 임팩트가 측정 어렵더라도 프록시 지표라도 설정
```

**원칙 3 — 비용 KR을 항상 포함**
```
에이전트는 사용할수록 비용이 발생
비용 상한을 KR로 설정하지 않으면 무한정 증가 가능
"월 $N 이하" 형태로 명시
```

**원칙 4 — 베이스라인 먼저**
```
현재 값을 모르면 목표 설정 불가
처음 2주는 데이터 수집 기간으로 설정
이후 실제 베이스라인 기반으로 OKR 수정
```

---

### OKR 리뷰 사이클

```
주간: 실행 로그 확인 (성공/실패 건수)
월간: KR 달성률 리뷰 + 비용 확인
분기: Objective 재검토 + 다음 분기 OKR 설정
```

---

### 사용 방법

`/agent-okr [에이전트 이름 또는 목적]`

---

### Instructions

You are helping design OKRs for an agent: **$ARGUMENTS**

**Step 1** — 에이전트 Objective 작성  
비즈니스 임팩트 중심의 야심차고 질적인 목표 1개

**Step 2** — Business Impact KR 2개  
측정 가능한 비즈니스 아웃컴 지표  
현재값 → 목표값 → 달성 기한

**Step 3** — Operational Health KR 2개  
정확도 / 비용 / 신뢰성 / 레이턴시 중 가장 중요한 2개  
현재값 베이스라인 추정 또는 수집 계획

**Step 4** — 측정 방법 정의  
각 KR을 어떻게 측정할 것인가 (자동/수동, 도구)

**Step 5** — 리뷰 사이클 설정  
주간/월간/분기 리뷰 루틴 제안

---

### 참고
- 설계자: AI PM Skills Contributors, 2026-03
- 일반 OKR 프레임워크 기반 → 에이전트 특화 2축(운영 건강도 + 비즈니스 임팩트) 구조로 재편
- Christina Wodtke, *Radical Focus* — OKR 원칙 참고

---

## Further Reading
- Christina Wodtke, *Radical Focus* — OKR implementation guide
- John Doerr, *Measure What Matters* — OKR origin and principles

## Contextual Knowledge (auto-loaded)

> 보조 파일이 존재할 때만 자동 로드됩니다. 파일이 없으면 건너뜁니다.

### Test Cases
!`cat references/test-cases.md 2>/dev/null || echo ""`

### Troubleshooting
!`cat references/troubleshooting.md 2>/dev/null || echo ""`

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`
