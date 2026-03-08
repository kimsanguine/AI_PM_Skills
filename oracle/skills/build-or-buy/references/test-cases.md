# Test Cases — build-or-buy

## 1) Trigger Tests

### Should Trigger (5)

1. **Document Summarization vs Glean**
   - Query: "문서 요약 에이전트를 만들려는데, 직접 개발할지 Glean 같은 기존 솔루션을 쓸지 고민이야. 우리 팀은 엔지니어 2명이고 3개월 안에 런칭해야 해."
   - Reason: 특정 에이전트에 대한 Build/Buy 선택 필요
   - Expected: 6개 항목 평가 + 권장 선택지

2. **Customer Support (Intercom vs Custom)**
   - Query: "Should we build our own customer support agent or use Intercom's AI features? We handle about 500 tickets/day and need Korean language support."
   - Reason: 기존 솔루션(Intercom) vs 자체 구축 비교
   - Expected: 평가 매트릭스 + 하이브리드 검토

3. **Content Moderation with Resource Constraint**
   - Query: "콘텐츠 모더이션 에이전트를 만들어야 하는데, 풀타임 엔지니어가 1명뿐이고 2개월 내 검증이 필요해. Build하면 시간이 부족할 것 같고, No-Code 플랫폼도 있는데..."
   - Reason: 리소스 제약 + 시간 제약 + 노코드 옵션 검토

4. **Data Pipeline Agent (Build with Tech Moat)**
   - Query: "우리 특수한 데이터 포맷을 처리하는 에이전트가 필요한데, 시장에 없는 기능이야. 외부 솔루션으로는 30% 밖에 못 한다고 했어. 그럼 Build가 맞을까?"
   - Reason: 도메인 특화 + 차별화 높음

5. **Scaling Decision (Buy → Build Transition)**
   - Query: "초기에는 Zapier로 빠르게 구축했는데, 이제 사용자가 100개 고객사로 늘었어. 이 단계에서 No-Code → Build로 전환해야 할까? 비용은 얼마나 차이날까?"
   - Reason: 시간 경과에 따른 재검토 (Buy → Build 전환 고려)

---

### Should NOT Trigger (5)

1. **Opportunity Discovery**
   - Query: "에이전트 기회를 탐색하고 싶어. 우리 서비스에서 자동화할 수 있는 영역을 찾아줘."
   - Reason: 아직 어떤 에이전트를 만들지 결정 안 함 → opp-tree 스킬
   - Correct Route: oracle/opp-tree

2. **Architecture Design**
   - Query: "에이전트 아키텍처를 3-tier로 설계하고 싶어. Prometheus-Atlas-Worker 패턴 적용해줘."
   - Reason: Build 선택 후 기술 구현 방식 → architecture 스킬
   - Correct Route: architecture/3-tier-design

3. **PRD Writing**
   - Query: "에이전트 PRD 작성해줘. 이미 빌드하기로 결정했고 스펙이 필요해."
   - Reason: Build 선택 후 구현 상세 스펙 → instruction-design 스킬
   - Correct Route: forge/instruction-design

4. **Pricing Strategy**
   - Query: "에이전트 제품 가격을 얼마로 책정하면 좋을까?"
   - Reason: GTM/비즈니스 모델 → agent-gtm 스킬
   - Correct Route: oracle/agent-gtm

5. **Performance Optimization (Already Built)**
   - Query: "우리가 이미 만든 에이전트 비용이 너무 비싼데, 외부 서비스로 바꿀 수 있을까?"
   - Reason: 이미 Build한 후 최적화 단계 → cost-sim/burn-rate 스킬
   - Correct Route: argus/burn-rate

---

## 2) Functional Tests (Given-When-Then)

### Test 2-1: 가중치 적용이 부정확한 경우

**Given:**
- 프로젝트 컨텍스트: "우리는 빠르게 검증하고 싶어" (속도 최우선)
- 모든 항목을 동일 가중치로 평가

**When:**
- Quality Gate 체크

**Then:**
- ✗ 거절: "속도가 최우선이라고 명시되었는데 가중치가 동일"
- ✓ 재평가 유도:
  - "속도를 2배 가중치로 재계산해보세요"
  - Build (느림) vs Buy/No-Code (빠름) 점수 재계산

---

### Test 2-2: 외부 솔루션 조사 부족

**Given:**
- 요청: "계약서 검토 에이전트, Build vs Buy?"
- 조사된 솔루션: 1개 (Glean만)

**When:**
- Quality Gate 체크

**Then:**
- ✗ 거절: "솔루션이 1개만 조사됨, 최소 2~3개 필수"
- ✓ 추가 조사 요청:
  - "비슷한 솔루션으로 LawGeex, Kira, ContractPodAi 등 비교해보세요"
  - 각 솔루션의 비용/제약/커스터마이징 한계 정리

---

### Test 2-3: 하이브리드 전략이 너무 복잡

**Given:**
- 제안: "오케스트레이션은 Build, 도메인 로직은 Buy(A), UI는 Buy(B), 모니터링은 No-Code(C), 백업은 Build(D)"
- 통합 지점: 5개 이상

**When:**
- 복잡도 평가

**Then:**
- ✗ 거절: "통합 지점이 5개 → 관리 불가능"
- ✓ 단순화 유도:
  - "핵심 2개 레이어만: 오케스트레이션(Build) + 나머지(단일 Buy 솔루션)"
  - 또는 "전체를 1개 플랫폼에 Buy하기"

---

## 3) Error Cases

### Error 3-1: Build/Buy 점수가 균형잡힘 (모두 비슷)

**Scenario:**
- Build: 45점, Buy: 43점, No-Code: 44점
- 점수가 너무 가까워 선택 어려움

**Expected Error Handling:**
- ✓ "점수 차이가 작으므로, 위험도 낮은 선택지 추천"
- ✓ "구체적 선택 기준 추가 필요:"
  - "시간 제약 > 리소스 제약 → Buy"
  - "리소스 제약 > 시간 제약 → Build"
  - "검증 먼저 → No-Code"

---

### Error 3-2: 외부 솔루션이 실제로 존재하지 않음

**Scenario:**
- 요청: "매우 특수한 도메인(X) 에이전트, Build vs Buy?"
- 조사 결과: 시장에 유사 솔루션 없음

**Expected Error Handling:**
- ✓ "시장에 솔루션이 없으므로 Build 일택"
- ✓ "No-Code 플랫폼으로 빠르게 프로토타입 후 Build 검토" 대안 제시

---

## 3) Edge Cases

| # | 쿼리 | 판정 | 이유 |
|---|------|------|------|
| E1 | "우리가 만든 에이전트가 있는데, 지금 경쟁 시장에 비슷한 도구가 5개 생겼어. 이미 만든 걸 Buy로 바꾸는 게 맞을까?" | ⚠️ 경계 | Build → Buy 전환은 build-or-buy의 "재검토" 케이스. 정확히는 기존 의사결정 재평가. "유지보수 시간이 월 20시간 이상"이면 Build → Buy 검토 기준점 |
| E2 | "한 가지 에이전트를 여러 부서에서 다르게 써야 해. 중앙에서 Build하고 각 부서별로 커스터마이징하는 게 좋을까?" | ✅ Trigger | 이것도 Build-or-Buy 의사결정. "Hybrid 전략 (Core Build + 주변 커스터마이징)"으로 평가. 6개 평가 항목 중 '커스터마이징 자유도' 가중치 높음 |
| E3 | "특수한 도메인이라 시장에 솔루션이 없어. Build 일택인 건 알겠는데, 일단 No-Code로 프로토타입 만들고 나중에 Build로 전환해야 할까?" | ✅ Trigger | No-Code → Build 전환 시나리오. 이것도 build-or-buy 범위. "검증 완료 후 스케일 필요 시" 전환 기준 명시됨 |
| E4 | "외부 솔루션 비용이 매달 $500인데, 우리가 직접 만들면 개발자 1명 4주(약 $5K) + 유지보수 월 10시간. 어느 게 나을까?" | ✅ Trigger | 정확한 비용 비교. 장기 비용(월 $500 × 12 + 유지보수) vs 개발 초기 비용을 평가 매트릭스로 비교 가능 |
| E5 | "Build와 Buy를 섞으려니까 통합 지점이 6개나 돼. 이게 너무 복잡하지 않을까? 단순화 방법이 있을까?" | ✅ Trigger | 하이브리드 복잡도 경고는 build-or-buy의 Step 5에서 다뤄짐. "통합 지점 3개 이상 = 관리 불가능" 기준으로 단순화 제안 |

---

## 4) With/Without Skill 비교

### Scenario: Customer Support Agent

**Before (build-or-buy 없이):**
- PM: "고객 응대 자동화하려는데, Intercom이 있으니까 쓰는 게 낫지 않을까?"
- Tech Lead: "근데 우리 특수한 프로세스가 있잖아. 직접 만드는 게 나을 것 같은데..."
- 결과: 의견 충돌, 불확실한 결정

**After (build-or-buy 스킬 적용):**

1. **요구사항 명확화**
   - 목적: "일간 500건 고객 문의를 2시간 이내에 응답"
   - 핵심 기능: 자동 분류, 자동 응답, 에스컬레이션

2. **차별화 판단**
   - "고객 응대는 우리 차별화가 아님" → Buy 유리
   - 하지만 "특수 프로세스(우리만의 에스컬레이션 규칙)" → Build 고려

3. **외부 솔루션 조사**
   - Intercom: $500/월, 기본 분류 + 에스컬레이션 지원, 우리 프로세스 80% 커버
   - Freshdesk: $400/월, 동일 기능 + 한국어 지원 좋음, 80% 커버
   - Zendesk: $700/월, 고급 기능 + 완전 커스터마이징, 100% 커버

4. **평가 매트릭스** (가중치: 속도 2배, 비용 1배, 커스터마이징 1배)
   - Build: 차별화 2점, 속도 1점×2=2, 비용 3점, 커스터마이징 5점, 유지보수 3점, 도메인 4점 = 24점
   - Intercom: 차별화 1점, 속도 5점×2=10, 비용 5점, 커스터마이징 2점, 유지보수 5점, 도메인 2점 = 25점
   - Freshdesk: 차별화 1점, 속도 5점×2=10, 비용 5점, 커스터마이징 2점, 유지보수 5점, 도메인 2점 = 25점

5. **하이브리드 검토**
   - Freshdesk (기본 자동화) + 커스텀 에스컬레이션 로직(Build)
   - 통합 지점: 1개 (webhook으로 Freshdesk → 우리 에스컬레이션 로직)

6. **최종 권장**
   - "Freshdesk Buy + 커스텀 에스컬레이션 레이어 Build (하이브리드)"
   - 근거:
     1. 속도: 3개월 내 검증 가능 (1개월 Buy/온보딩 + 2개월 커스텀)
     2. 비용: Freshdesk $400 + 개발 2주 vs Build 4주 전체 = 비용 절감
     3. 차별화: 우리 특수 프로세스는 Build로 보호

7. **재검토 트리거**
   - "6개월 후 실제 운영 비용이 Freshdesk $400 + 유지보수 20시간/월 초과 시 Full Build로 전환"

**Impact:**
- 명확한 의사결정 근거 제공
- Build vs Buy 절충점(하이브리드) 발견
- 3개월 내 검증 가능한 전략 수립
- 향후 재검토 기준 명시
