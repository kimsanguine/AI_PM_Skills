# Domain Context — stakeholder-map 스킬

## 1) Domain Scope

**이 스킬이 소유하는 영역:**
- 이해관계자 식별 및 Power-Interest Matrix 배치
- 저항 유형 분석 및 맞춤 대응 전략
- Champion 발굴 및 무장(데이터/권고)
- 이해관계자별 커뮤니케이션 계획

**이 스킬이 소유하지 않는 영역:**
- 에이전트 설계 검증 (→ `agent-plan-review`)
- 신뢰성/SLO 정의 (→ `argus/reliability`)
- GTM 전략 전체 (→ `oracle/agent-gtm`)

## 2) Primary Users

- **PM**: 에이전트 도입 변화 관리
- **리더십**: go/no-go 판단
- **팀 리드**: 부서별 대응 전략

## 3) Required Inputs

**필수 입력:**
1. 에이전트 이름/도입 목표
2. 관련 이해관계자 (6개 그룹 이상)
3. 알려진 저항 요인 (있으면)

**선택 입력:**
- 조직 크기/문화
- 기존 도입 경험

## 4) Output Contract

**산출물:**
- Stakeholder 식별표 (6개 이상)
- Power-Interest Matrix 배치
- 저항 유형별 대응 전략 (3개 이상)
- Champion 프로필 + 무장 전략
- 커뮤니케이션 계획 (이해관계자별)
- Go/No-Go Confidence (Low/Medium/High)

## 5) Guardrails

**라우팅 규칙:**
- 에이전트 설계 검증 → `agent-plan-review`
- 신뢰성 우려 해결 → `argus/reliability`
- GTM 전체 전략 → `oracle/agent-gtm`

**품질 기준:**
- 이해관계자 6개 이상 식별
- 저항 유형 3개 이상 분석
- Champion 1명 이상 발굴

## 6) Working Facts

**Power-Interest Matrix 사분면:**

| 사분면 | 영향력 | 관심도 | 전략 |
|--------|--------|--------|------|
| Engage Actively | 높음 | 높음 | 주간 리뷰 |
| Manage Closely | 높음 | 낮음 | 조건부 협력 |
| Keep Informed | 낮음 | 높음 | 월간 업데이트 |
| Monitor Only | 낮음 | 낮음 | 주기적 알림 |

**저항 유형 사례:**

| 저항 유형 | 근본 원인 | 대응 전략 |
|----------|---------|---------|
| Trust Deficit | "AI가 정말 정확한가?" | Shadow Mode 검증 |
| Control Loss | "누가 책임지는가?" | RACI 매트릭스 + 명확한 소유권 |
| Risk Aversion | "AI 규제는?" | 체크리스트 + 감사 로그 |

**Champion 무장 3가지:**
1. **데이터**: 현재 비용/시간 (수치로)
2. **데모**: POC 결과 (Before/After)
3. **ROI**: 3개월 투자 회수 타임라인

**TO BE UPDATED by reviewer:**
- 조직 규모별 이해관계자 포함 범위
- 도입 기간별 커뮤니케이션 강도
- Champion 지원(교육, 보너스) 기준

## 7) Fill-in Checklist

- [ ] 이해관계자 6개 이상 식별했는가?
- [ ] Power-Interest Matrix 배치가 완료되었는가?
- [ ] 저항 유형 3개 이상 분석했는가?
- [ ] 각 저항 유형별 구체적 대응 전략이 있는가?
- [ ] Champion을 발굴하고 무장(데이터/데모/ROI)했는가?
- [ ] 이해관계자별 커뮤니케이션 계획(메시지/포맷/주기)이 정의되었는가?
- [ ] Go/No-Go Confidence 수준을 명시했는가?
