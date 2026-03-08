# Domain Context — okr 스킬

## 1) Domain Scope

**이 스킬이 소유하는 영역:**
- 에이전트 고유의 OKR 설계 (Business Impact + Operational Health 2축)
- 측정 가능한 Key Result 정의
- 분기별/월간/주간 리뷰 사이클 수립

**이 스킬이 소유하지 않는 영역:**
- 에이전트 전체 설계 검증 (→ `agent-plan-review`)
- 비용 시뮬레이션 (→ `oracle/cost-sim`)
- 신뢰성 SLO 정의 (→ `argus/reliability`)

## 2) Primary Users

- **PM**: 에이전트 성과 추적 및 개선 기회 식별
- **운영팀**: 에이전트 모니터링 기준 수립
- **경영진**: 에이전트 포트폴리오 의사결정

## 3) Required Inputs

**필수 입력:**
1. 에이전트 이름
2. 에이전트의 목표 및 현황
3. 측정하고 싶은 지표 (최소 2~4개)

**선택 입력:**
- 기존 성과 데이터 (베이스라인)
- 예산 제약

## 4) Output Contract

**산출물:**
- 1개 Objective (야심차고 질적)
- 2개 Business Impact KR
- 2개 Operational Health KR
- 측정 방법 정의
- 리뷰 사이클 설정

| KR 유형 | 필수 | 예시 |
|--------|------|------|
| Business Impact | 2개 이상 | 시간 절감, 비용 절감, 오류 감소 |
| Operational Health | 2개 이상 | 정확도, 비용, 신뢰성, 레이턴시 |

## 5) Guardrails

**라우팅 규칙:**
- 에이전트 전체 설계 검증 → `agent-plan-review`
- 비용 추정 → `oracle/cost-sim`
- 신뢰성 KPI → `argus/reliability`

**품질 기준:**
- Business Impact KR과 Operational Health KR 모두 필수 (한쪽만 X)
- 비용 KR을 항상 포함
- 베이스라인 없으면 처음 2주는 데이터 수집 기간

## 6) Working Facts

**OKR 작성 시간:**

| 단계 | 시간 | 산출물 |
|------|------|--------|
| Objective 정의 | 5분 | 1문장 |
| KR 4개 정의 | 20분 | 현재값/목표값/기한 명시 |
| 측정 방법 | 10분 | 자동/수동 + 도구 명시 |
| 리뷰 사이클 | 5분 | 주간/월간/분기 루틴 |
| **Total** | **40분** | **완성된 OKR** |

**에이전트 유형별 KR 예시:**

| 에이전트 유형 | Business Impact KR | Operational Health KR |
|-------------|------------------|---------------------|
| 시간 절감 | 월 N시간 절감 | 정확도 95%, 비용 $N/월 이하 |
| 수익 창출 | 월 $N 추가 매출 | 신뢰성 99%, 비용 효율 X% |
| 데이터 품질 | 오류율 X% → Y% | 처리량 N건/시간, 레이턴시 <5초 |

**베이스라인 수집 기간:**
- 처음 2주 = 데이터 수집 기간 (정식 리뷰 X)
- 3주차부터 = 실제 베이스라인 기반 OKR 수정

**TO BE UPDATED by reviewer:**
- 조직별 KR 목표값 기준 (정확도 95% vs 90%?)
- 비용 KR의 상한선 (월 $5? $10?)
- 에이전트 유형별 우선 지표 (시간 절감 에이전트는 비용 KR 가능할까?)

## 7) Fill-in Checklist

- [ ] Objective가 야심차고 질적인가? (1문장)
- [ ] Business Impact KR이 2개 이상인가?
- [ ] Operational Health KR이 2개 이상인가?
- [ ] 비용 KR이 포함되었는가?
- [ ] 각 KR에 현재값/목표값/기한이 명시되었는가?
- [ ] 베이스라인 수집 계획(처음 2주)이 있는가?
- [ ] 측정 방법이 정의되었는가? (자동/수동, 도구명)
- [ ] 리뷰 사이클(주간/월간/분기)이 설정되었는가?
