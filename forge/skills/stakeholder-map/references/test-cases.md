# Test Cases — Stakeholder Map

## 1) Trigger Tests

### Should Trigger (5)

1. "cost-analyst 에이전트 도입 전에 이해관계자 맵핑을 해줄래? CFO, 엔지니어링, Accounting, Legal 각각의 관심사가 다를 것 같아."
   - 이유: 조직 변화 필요, 다중 팀 합의 필수

2. "데이터 자동화 도구를 도입하면서 내부 저항이 예상돼. 누가 막을 것 같고, 누가 도와줄 것 같은지 지도를 만들어줄 수 있을까?"
   - 이유: 저항 요인 분석 + 극복 전략 필요

3. "신입 온보딩 에이전트를 전사 배포하고 싶은데, HR, 엔지니어링, 재무가 모두 관여할 거 같아. 누가 champion이 될 수 있을까?"
   - 이유: 전사 배포 전 이해관계자 전략 필요

4. "AI 도입 변화 관리 계획이 필요해. 누구와 어떻게 의사소통해야 할지 알고 싶어."
   - 이유: 커뮤니케이션 계획 + 관여 전략 필요

5. "우리 팀이 기존 도구를 에이전트로 대체하려고 하는데, 사용자들이 저항할까봐. 이해관계자 관점에서 분석해줄래?"
   - 이유: 사용자 저항 분석 + 극복 전략 필요

### Should NOT Trigger (5)

1. "에이전트 아키텍처를 설계해줄 수 있을까?"
   - 올바른 라우팅: `3-tier` 또는 `orchestration`

2. "프로젝트 로드맵을 만들어줄 수 있을까?"
   - 올바른 라우팅: `okr` 또는 프로젝트 관리 도구

3. "Legal 팀과 AI 규제에 대해 어떻게 이야기해야 할까?"
   - 올바른 라우팅: `argus/reliability` 또는 컴플라이언스 가이드

4. "신뢰성 SLO와 장애 모드 매트릭스를 설계해줄 수 있을까?"
   - 올바른 라우팅: `argus/reliability`

5. "에이전트의 GTM 전략(시장 진출 전략)을 세워줄래?"
   - 올바른 라우팅: `oracle/agent-gtm`

## 2) Functional Tests (Given-When-Then)

### Test 1: 기본 이해관계자 맵핑 (5섹션 완성)

**Given:**
- 에이전트: expense-analyzer (비용 분석 자동화)
- 조직 규모: 중소기업 (C-Level 2명, 팀 5개)
- 기존 정보: 누가 이 에이전트를 필요로 하는지만 알고 있음

**When:**
- `/stakeholder-map expense-analyzer` 스킬 실행

**Then:**
- 5섹션이 모두 작성됨:
  1. Stakeholder Identification: 6명/팀 이상 식별 (경영진/사용자/엔지니어링/법무/운영/재무)
  2. Power-Interest Matrix: 4개 사분면에 각 이해관계자 배치 (Power/Interest 각 1-5점)
  3. Resistance Analysis: 저항 유형 3개 이상 (Job Threat/Trust Deficit/Control Loss 등) + 대응 전략
  4. Champion Strategy: 1명 이상 champion 선정 (프로필/동기/무장/확산 경로)
  5. Communication Plan: 이해관계자별 메시지/포맷/주기 명시
- Go/No-Go Confidence: Low/Medium/High 중 명시

---

### Test 2: 저항 유형별 대응 전략 구체화

**Given:**
- 초안 Resistance Analysis: "사람들이 새 도구를 싫어할 수 있음"
- 문제: 추상적이고 대응 전략이 "더 설득하기"만 됨

**When:**
- 저항 유형을 구체적 시나리오로 재분류

**Then:**
- 저항 유형별 재작성:
  - "일반적 저항" → "Job Threat (Accounting)" + 대응: "Shadow Mode 3주 검증 → '99% 일치' 데이터 공개"
  - "신뢰 문제" → "Trust Deficit (Engineering)" + 대응: "POC 시연 → 리스크 체크리스트 제시"
  - "통제 우려" → "Control Loss (Legal)" + 대응: "RACI 매트릭스 명시 + 롤백 계획"

---

### Test 3: Champion 동기와 무장이 구체적인가?

**Given:**
- Champion: "PM 담당자 (사용자)"
- 초안 동기: "일을 쉽게 하고 싶음"

**When:**
- Champion의 pain point를 구체적 수치로 재정의

**Then:**
- 동기와 무장 재작성:
  - Pain: "매월 비용 분석에 10시간/월 소요" (구체적 시간)
  - 동기: "이 시간을 전략적 분석에 사용하고 싶음" (구체적 목표)
  - 무장 데이터: "월 10시간 × 시급 $50 = $500 절감 (연 $6,000)" (구체적 수치)
  - 무장 데모: "POC 실행 → '원본 vs AI 분석 99% 일치'" (증명 가능)

## 3) Error Cases

### Error 1: 이해관계자 식별 불완전성

**상황:**
- 식별된 이해관계자: 3명 (CEO, 직접 사용자, 엔지니어)
- 누락: Legal, Accounting, Operations, Finance (도입에 영향을 주는 팀)

**대응:**
- "이 에이전트가 영향을 주는 모든 팀을 식별하세요"로 재요청
- 최소 6개 그룹 식별 가이드라인 제시
- 각 그룹의 "관심사" 컬럼을 채우면서 누락된 팀 발견

---

### Error 2: Power-Interest Matrix 배치 기준 모호

**상황:**
- 모든 이해관계자가 "High Power + High Interest" 사분면에 배치됨
- 실제로는 일부는 "Monitor Only" 또는 "Keep Informed"에 속함

**대응:**
- Power와 Interest를 명시적으로 1-5점으로 채점 요청
- 기준 설명: "Power = 에이전트 도입 의사결정에 영향을 줄 수 있는 정도" (1=전혀 없음, 5=절대권)
- 기준 설명: "Interest = 에이전트 도입 결과에 관심 있는 정도" (1=전혀 없음, 5=매우 높음)

---

### Error 3: Go/No-Go Confidence 미명시 또는 근거 없음

**상황:**
- Go/No-Go Confidence: "High"
- 하지만 매트릭스 보면 Blocker (Legal)이 "Manage Closely"에 있고 저항 전략이 불완전함

**대응:**
- "High는 Blocker가 없거나 명확한 대응책이 있을 때만 가능합니다"로 설명
- "현재 상황을 보면 Medium이 맞습니다. 이유: Legal 합의 필요 + Mitigation 계획 준비 중"으로 수정

## 3) Edge Cases

| # | 쿼리 | 판정 | 이유 |
|---|------|------|------|
| E1 | "우리 조직이 작아서 이해관계자가 3명뿐이야. 그래도 stakeholder-map이 필요할까?" | ⚠️ 경계 | 조직 규모와 관계없이 "합의 필요한 그룹"이 있으면 유효. 3명이라도 각각의 관심사와 저항이 다르면 stakeholder-map 가치 있음 |
| E2 | "이미 Legal, Finance와 사전 협의를 완료했어. 지금 stakeholder-map을 할 필요가 있을까?" | ✅ Trigger | 사전 협의 후라도 "전체 이해관계자 맵핑"은 유효. "예상 저항" 보다는 "실제 저항 대응" 단계로 이행 |
| E3 | "한 팀(예: Engineering)이 매우 파워 있으면서 "관심 없다"고 해. 어떻게 해석해야 할까?" | ✅ Trigger | High Power + Low Interest = "Manage Closely". 무관심이 아니라 "관심을 끌어야 할" 대상으로 재분류. 동기 찾기 필수 |
| E4 | "외부 고객사(Partner)도 이해관계자에 포함해야 할까? 아니면 내부만 맵핑할까?" | ✅ Trigger | 에이전트가 "파트너 사용" 또는 "파트너 데이터 접근"이면 외부도 포함. Power-Interest Matrix에 함께 배치하되 "커뮤니케이션 경로" 별도 관리 |
| E5 | "CEO가 "모든 팀이 다 찬성할 거야"라고 생각해. 저항 분석이 필요하다고 어떻게 설득할까?" | ✅ Trigger | Resistance Analysis 스킬 단계에서 "가정과 실제의 gap"을 데이터로 제시. 과거 사례나 조직 심리(변화 저항)를 근거로 제안 |

---

## 4) With/Without Skill 비교

### 시나리오: 에이전트 도입 계획 세우기

**Without Stakeholder Map Skill:**
- 팀이 "이 에이전트는 좋으니까 다들 받아들일 거야" 가정
- 구현 80% 진행 후 Legal에서 "AI 규제 때문에 배포 못 합니다" 지적
- Accounting은 "데이터 정확성 검증할 프로세스가 없어" 거부
- **결과: 3개월 지연, 재설계 필요, 신뢰도 하락**

**With Stakeholder Map Skill:**
- Step 1에서 Legal/Accounting/Finance를 주요 이해관계자로 식별
- Step 3에서 각 팀의 저항 유형 분석 → "Trust Deficit (Accounting)" 예상
- Step 5에서 Accounting과 커뮤니케이션 계획 수립 → "Shadow Mode 결과 공개" 일정 확정
- Legal은 "마일스톤 단위 AI 리스크 체크리스트" 검토로 사전 승인
- **결과: 일정대로 배포, 조직적 저항 사전 해소**

