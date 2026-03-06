---
name: agent-business-model
description: "Design a revenue model for an AI agent product or service. Covers 5 agent-specific monetization patterns including the Polsia revenue-share model. Use when transitioning from building an agent to making money from it, or when evaluating business model options for an agent-based product."
---

## Agent Business Model

에이전트를 만드는 것과 에이전트로 돈을 버는 것은 완전히 다른 문제입니다.

> "도구는 빠르게 수렴합니다. 지금 진짜로 고민해야 할 건  
> 이 자동화 구조 위에서 어떻게 수익을 설계할 것인가입니다."  
> — Jeongmin Lee, LinkedIn 2026-03

일반 SaaS와 에이전트 비즈니스의 결정적 차이:
- SaaS: 기능 → 구독 → 사용량 (선형 구조)
- 에이전트: **아웃컴** → 수익 공유 가능 (비선형 구조)

에이전트는 측정 가능한 아웃컴을 만들어냅니다.  
이 아웃컴에 수익을 연결하는 방식이 에이전트 비즈니스 모델의 핵심입니다.

---

### 5가지 에이전트 수익 모델

**Model 1 — Subscription (구독형)**

```
사용자 → 월정액 → 에이전트 무제한 사용
```

**구조:** 기능 접근권에 대한 고정 월정액  
**가격 기준:** 기능 수 / 사용자 수 / 워크스페이스  
**장점:** 예측 가능한 MRR, 낮은 운영 복잡도  
**단점:** 가치 전달이 불명확할 때 해지 급증  
**적합:** 생산성 도구, 내부 업무 자동화, 범용 에이전트  

실제 사례: GitHub Copilot ($19/월), Cursor ($20/월)  

---

**Model 2 — Usage-Based (사용량 과금)**

```
사용자 → 에이전트 실행 횟수/토큰 → 단위 과금
```

**구조:** API 호출 수, 토큰 수, 처리된 문서 수 등 단위 과금  
**가격 기준:** per-call / per-token / per-document  
**장점:** 사용하는 만큼만 부담, 가치와 비용 직결  
**단점:** 수익 예측 어려움, 비용 불확실로 고객 저항  
**적합:** API 형태로 제공하는 에이전트, 개발자 대상  

실제 사례: OpenAI API, Anthropic API  

---

**Model 3 — Outcome-Based / Revenue Share (성과 공유형)** ⭐

```
사용자 → 에이전트 활용 → 매출 발생 → X% 공유
```

**구조:** 에이전트가 만든 아웃컴(매출, 비용 절감, 전환)의 일정 % 공유  
**가격 기준:** 에이전트 기여 매출의 10~30%  
**장점:** 가치와 수익이 완전 정렬, 고객 저항 최소  
**단점:** 아웃컴 측정 인프라 필요, 분쟁 소지  
**적합:** 직접 매출 창출형 에이전트 (영업, 마케팅, 커머스)  

실제 사례:
- **Polsia (Ben Broca)**: 월정액(손익분기) + **사용자 매출 20% 공유**
  → 런칭 1달 만에 ARR $100만 달성
  → 핵심 인사이트: "월정액은 운영비 충당, 진짜 수익은 성과 공유에서"

---

**Model 4 — Platform / Marketplace (플랫폼형)**

```
에이전트 공급자 ←→ [플랫폼] ←→ 에이전트 수요자
                   중개 수수료
```

**구조:** 에이전트 마켓플레이스 운영, 거래 수수료 수취  
**가격 기준:** 거래액의 15~30% 수수료  
**장점:** 공급자 생태계 구축 가능, 네트워크 효과  
**단점:** 양면 시장 구축 필요, 초기 임계점 달성 어려움  
**적합:** 에이전트 전문가 ↔ 기업 연결 플랫폼, 100 Agents 스타일  

---

**Model 5 — Outcome-as-a-Service (결과물 판매)**

```
고객 → 결과물 구매 (보고서, 분석, 콘텐츠) → 에이전트가 생산
```

**구조:** 에이전트의 출력물 자체를 상품으로 판매  
**가격 기준:** 결과물 단위 (보고서 1건 = $X)  
**장점:** 에이전트 기술 불필요, 전문성 포지셔닝 가능  
**단점:** 고객이 직접 에이전트를 쓰면 대체될 위험  
**적합:** 리서치, 콘텐츠, 데이터 분석 전문화  

---

### 하이브리드 전략 (권장)

단일 모델보다 **핵심 + 업사이드** 구조가 최적:

```
Base Revenue:  구독 (예측 가능한 기본 수익 확보)
Upside:        성과 공유 (에이전트 가치에 비례한 추가 수익)
```

Polsia 모델이 증명한 공식:
```
월정액 = 운영 손익분기점
매출 공유 = 실제 성장 엔진
```

이 구조의 장점:
1. 고객이 에이전트를 써야 할 동기가 명확 (같이 잘 되면 같이 수익)
2. 가격 협상 단순화 (구독은 낮게, 성과는 나눠서)
3. 에이전트 품질 개선 동기 자동 생성

---

### 에이전트 비즈니스 모델 캔버스

| 구성요소 | 질문 | 내 에이전트의 답 |
|---|---|---|
| **Value Proposition** | 에이전트가 만드는 측정 가능한 아웃컴은? | |
| **Customer Segment** | 이 아웃컴이 가장 절실한 고객군은? | |
| **Revenue Streams** | 어떤 모델로 수익을 가져올 것인가? | |
| **Pricing Metric** | 무엇을 기준으로 가격을 매기는가? | |
| **Cost Structure** | 모델 API 비용 + 운영 비용의 손익분기는? | |
| **Moat** | 경쟁자가 동일한 에이전트를 만들면? | |
| **Growth Loop** | 사용자가 늘수록 에이전트가 좋아지는가? | |

---

### 사용 방법

`/agent-business-model [에이전트 또는 서비스 설명]`

---

### Instructions

You are helping design a **business model for an agent product**: **$ARGUMENTS**

**Step 1 — 아웃컴 정의**
- 이 에이전트가 고객에게 만들어주는 측정 가능한 아웃컴 3가지
- 아웃컴을 금액/시간/오류율로 수치화

**Step 2 — 고객 세그먼트 분석**
- 이 아웃컴이 가장 절실한 고객군 2~3개
- 각 세그먼트의 지불 의향 (WTP) 추정

**Step 3 — 5가지 모델 적합도 평가**
- 각 모델에 대해 이 에이전트에 맞는지 1~5점
- 상위 2개 모델 선택

**Step 4 — 하이브리드 전략 설계**
- Base + Upside 구조 설계
- 구독 가격 = 손익분기점 계산
- 성과 공유 % = 고객 WTP 내에서 최대화

**Step 5 — 가격 시뮬레이션**
- 시나리오 3개 (보수/중간/낙관) × 고객 수 × 단가
- 월 MRR 목표 달성을 위한 고객 수 계산

**Step 6 — 비즈니스 모델 캔버스 작성**
- 7개 구성요소 채우기

**Step 7 — 다음 단계 연결**
- 차별화 전략: `/agent-moat`
- 성장 전략: 타겟 고객 → ICP 정의

---

### 참고
- Polsia 사례: Ben Broca, LinkedIn 2026-03
- 설계자: Sanguine Kim (이든), 100 Agents 프로젝트 기반
- phuryn/pm-skills `monetization-strategy` + `business-model` 에이전트 특화 재편
