# Test Cases — agent-gtm 스킬

## 1) Trigger Tests

### Should Trigger (5)

1. "우리 에이전트가 내부에서 성공했다. 이제 외부 고객에게 팔 준비를 하려면?"
   - 이유: Beachhead 선정, Trust Sequence, Launch Phase 설계

2. "여러 고객 세그먼트가 있는데 누구부터 타겟해야 할까? 객관적 기준이 필요하다"
   - 이유: Beachhead Segment Selection (5가지 기준, 총 25점)

3. "고객이 우리 에이전트를 불신한다. 어떻게 신뢰를 구축할까?"
   - 이유: Trust Building Sequence (Shadow → Co-pilot → Auto → Delegation)

4. "첫 3개월 KPI를 뭘로 정할까? 정확도? 매출? 고객 수?"
   - 이유: Launch Phase별 KPI 및 성공 기준 정의

5. "내부 성공 사례를 바탕으로 마케팅 메시지를 만들고 싶다"
   - 이유: Positioning Statement 및 GTM 전략

### Should NOT Trigger (5)

1. "선정한 비치헤드를 위해 에이전트를 커스터마이징해야 한다"
   - 올바른 라우팅: forge의 `agent-instruction-design`

2. "Shadow Mode를 기술적으로 구현하려면?"
   - 올바른 라우팅: oracle의 `hitl` (Human-In-The-Loop)

3. "우리 에이전트의 예상 ROI를 계산하려면?"
   - 올바른 라우팅: oracle의 `cost-sim` (비용 시뮬레이션)

4. "경쟁사 GTM 전략은 뭔가?"
   - 올바른 라우팅: oracle의 `competitor` 스킬

5. "가격을 얼마로 책정할까?"
   - 올바른 라우팅: `agent-gtm` Step 4의 "Pricing Model" 다시 검토 또는 biz-model

## 2) Edge Cases

### 경계 사례 (4)

1. **Beachhead 점수가 불충분 (<20점)**
   - 입력: "우리는 이 세그먼트부터 시작하고 싶은데 총 점수가 15점이다"
   - 예상 행동: "비치헤드 부적합" 지적 → 다음 순위 세그먼트로 전환 또는 조건 개선 제안
   - 근거: Agent-gtm의 "Step 1" — 총점 20 이상이 비치헤드 기준

2. **Shadow Mode 기간이 너무 길어짐**
   - 입력: "고객이 6주 동안 추천만 받으니까 답답해한다"
   - 예상 행동: Shadow Mode 단축 (6주 → 2주) 또는 Co-pilot으로 진입
   - 근거: Failure Handling의 "Shadow Mode 기간이 너무 길어짐"

3. **Lighthouse에서 성공했는데 Wedge에서 안 된다**
   - 입력: "첫 고객은 대성공했는데 다음 고객은 온보딩이 어렵다고 한다"
   - 예상 행동: Lighthouse 고객이 "특수했나?" 재검토 → Wedge 온보딩 자동화 필요
   - 근거: Failure Handling의 "Wedge 고객들은 구축 난이도가 높다"

4. **NPS 또는 정확도 목표 미달**
   - 입력: "Lighthouse KPI: 정확도 > 80%, NPS > 60 — 정확도 85%인데 NPS 35"
   - 예상 행동: 기술 문제가 아니라 신뢰/사용 경험 문제 → Positioning 또는 Trust Sequence 재검토
   - 근거: Failure Handling의 "Shadow Mode 거쳤는데도 Wedge NPS 낮음"

