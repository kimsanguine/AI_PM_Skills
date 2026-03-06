---
name: agent-assumption-map
description: "Identify and prioritize the riskiest assumptions in an agent idea across four axes: Value, Feasibility, Reliability, and Ethics. Use after defining an agent opportunity and before starting implementation. Prevents building agents that work technically but fail operationally or cause unintended harm."
---

## Agent Assumption Map

에이전트 아이디어에는 수십 개의 숨겨진 가정이 있습니다.
그 중 단 하나만 틀려도 에이전트는 조용히 잘못된 방향으로 실행됩니다.

일반 제품과 다른 점:
- 일반 제품: 사용자가 결과를 보고 판단 → 오류 발견 즉시 가능
- 에이전트: 자율 실행 → 오류가 쌓일 때까지 발견 어려움

Agent Assumption Map은 **4축 분석**으로 핵심 가정을 사전에 발굴합니다.

---

### 4축 정의

**Axis 1 — Value (가치 가정)**
> "이 에이전트가 실제로 의미 있는 문제를 해결하는가?"

검토 질문:
- 자동화 후 실제로 시간/비용/오류가 줄어드는가?
- 사용자가 에이전트의 결과를 실제로 사용하는가?
- 에이전트 없이도 충분히 빠르게/잘 할 수 있지 않은가?
- 자동화로 해결되는 불편함이 진짜 불편함인가, 아니면 낮은 빈도의 사소한 불편인가?

**Axis 2 — Feasibility (실현 가능성 가정)**
> "이 에이전트를 실제로 구현할 수 있는가?"

검토 질문:
- 필요한 데이터에 접근 가능한가? (API 권한, 인증, 비용)
- 필요한 툴이 안정적으로 작동하는가?
- 기술 스택 (모델, 프레임워크) 이 요구사항을 지원하는가?
- 개발 리소스와 타임라인이 현실적인가?
- 외부 의존성 (API 변경, 서비스 중단) 리스크는?

**Axis 3 — Reliability (신뢰성 가정)** ← 에이전트 특화 축
> "이 에이전트가 충분히 정확하고 안정적으로 반복 실행 가능한가?"

검토 질문:
- 정확도 기준은 무엇인가? (90%? 99%? 100%?)
- 오류 발생 시 자동 감지 및 복구 가능한가?
- 컨텍스트 길이 / 모델 응답 일관성이 보장되는가?
- 외부 API 장애 시 에이전트가 어떻게 반응하는가?
- 장기 실행 시 성능 저하 (컨텍스트 오염, 비용 증가) 없는가?

> ⚠️ 신뢰성 기준은 용도에 따라 다릅니다.
> 뉴스 요약 에이전트 (90% 충분) vs 금융 거래 에이전트 (99.9% 이상 필요)

**Axis 4 — Ethics (윤리/안전 가정)** ← 에이전트 특화 축
> "이 에이전트를 자동화해도 괜찮은가? 오류 발생 시 영향은?"

검토 질문:
- 에이전트가 잘못된 판단을 내릴 때 영향 범위는?
- 개인정보 / 민감 데이터를 다루는가?
- 에이전트의 행동이 역추적 가능한가? (감사 로그)
- 에이전트가 인간을 대신해 의사결정하는 영역인가?
- 사용자가 에이전트의 판단을 검토하고 거부할 수 있는가?

> ⚠️ Ethics 축 점수가 낮으면 (위험 높음): Human-in-the-loop 설계 필수

---

### 가정 발굴 방법

**1단계: 브레인스토밍 (제한 없이)**
각 축에 대해 "~라고 가정하고 있다" 형태로 가정을 최대한 많이 나열.

예시 (AI 뉴스 브리핑 에이전트):
- Value: "PM이 AI 뉴스를 매일 읽고 싶어한다고 가정"
- Value: "요약된 뉴스가 원문보다 유용하다고 가정"
- Feasibility: "RSS 피드가 안정적으로 최신 뉴스를 제공한다고 가정"
- Feasibility: "Brave API 없이도 충분한 정보를 수집 가능하다고 가정"
- Reliability: "Haiku 모델이 뉴스 요약을 일관되게 잘 한다고 가정"
- Ethics: "AI가 요약한 뉴스가 원의도를 왜곡하지 않는다고 가정"

**2단계: 우선순위 매핑**
각 가정에 대해 2개 기준으로 점수 부여:

```
위험도 (1~5): 이 가정이 틀렸을 때 에이전트가 얼마나 망가지는가?
검증 난이도 (1~5): 이 가정을 검증하는 것이 얼마나 어려운가?

Priority Score = 위험도 × 검증 난이도
```

매트릭스:
```
             검증 난이도
             낮음  →  높음
위  높음  │ 즉시 검증  │ 최우선 검증 │
험       │            │             │
도  낮음  │ 나중에     │ 모니터링    │
```

**3단계: Top 3 가정 선정**
Priority Score 상위 3개 가정 → 실험 설계로 연결

---

### 가정 검증 실험 유형

| 가정 유형 | 권장 실험 |
|---|---|
| Value | 5일 수동 실행 후 실제 사용 여부 관찰 |
| Feasibility | API 직접 호출 10회 테스트 |
| Reliability | 동일 입력 20회 반복 → 출력 일관성 측정 |
| Ethics | 오류 시나리오 시뮬레이션 + 영향 범위 계산 |

---

### 사용 방법

`/agent-assumptions [에이전트 아이디어 또는 이름]`

---

### Instructions

You are helping identify and prioritize the riskiest assumptions for: **$ARGUMENTS**

**Step 1 — 에이전트 개요 파악**
- 에이전트 목적, 주요 기능, 타겟 사용자 확인
- 이미 정의된 Automation Outcome 확인 (agent-opportunity-tree와 연계)

**Step 2 — 4축 가정 브레인스토밍**
- 각 축 (Value / Feasibility / Reliability / Ethics)에 대해
  최소 3개 이상의 가정을 "~라고 가정하고 있다" 형태로 추출
- 억지로 좋게 보려 하지 말 것 — 부정적 가정도 적극 발굴

**Step 3 — 우선순위 매핑**
- 각 가정에 위험도(1~5) × 검증 난이도(1~5) = Priority Score 계산
- 상위 5개를 표로 정리

**Step 4 — Top 3 가정 심층 분석**
- 각 가정이 틀렸을 때 시나리오 서술
- 검증 실험 설계 (2일 이내 가능한 수준)
- 검증 결과에 따른 피벗 옵션

**Step 5 — Ethics 체크**
- Ethics 축 가정 중 위험도 4 이상인 항목 별도 강조
- Human-in-the-loop 설계가 필요한지 판단

**Step 6 — 다음 단계 연결**
- 검증 실험이 통과되면 `/agent-instruction-design`으로 연결
- Ethics 위험이 높으면 `/human-in-loop-design`으로 먼저 연결
- 검증 결과 실패 시 `agent-opportunity-tree`로 되돌아가 기회 재탐색

---

### 참고
- 원본 프레임워크: phuryn/pm-skills `identify-assumptions-new` (8 risk categories) 적용 후 에이전트 특화 4축으로 재편
- Reliability / Ethics 축: Byeonghyeok Kwak의 엔터프라이즈 에이전트 거버넌스 논의 기반
- 설계자: Sanguine Kim (이든), 2026-03
