---
name: okr
description: "Design OKRs specifically for AI agents — defining measurable Key Results around accuracy, cost, reliability, and business impact. Use when setting performance goals for a deployed agent, reviewing agent effectiveness, or aligning agent metrics with business objectives."
argument-hint: "[agent to set OKRs for]"
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
O: morning-briefing이 이든의 정보 수집 시간을 제로화하고
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
- 설계자: Sanguine Kim (이든), 2026-03
- 일반 OKR 프레임워크 기반 → 에이전트 특화 2축(운영 건강도 + 비즈니스 임팩트) 구조로 재편
- Christina Wodtke, *Radical Focus* — OKR 원칙 참고

---

## Further Reading
- Christina Wodtke, *Radical Focus* — OKR implementation guide
- John Doerr, *Measure What Matters* — OKR origin and principles
