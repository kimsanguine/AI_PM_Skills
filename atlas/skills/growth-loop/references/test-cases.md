# Test Cases — growth-loop 스킬

## 1) Trigger Tests

### Should Trigger (5)

1. "고객 상담 에이전트가 상담할수록 데이터가 쌓여서 답변 정확도가 자동으로 올라가게 만들고 싶다"
   - 이유: 데이터 모으는 방식 설계 + 사용 데이터를 개선으로 전환하는 루프 설계 필요

2. "Our AI sales assistant currently gets better with each call, but the improvement cycle is too slow. How do we accelerate the feedback loop?"
   - 이유: 플라이휠 주기(feedback cycle) 최적화 필요 — growth-loop의 핵심

3. "에이전트를 만들었는데 초기 사용자가 없어서 데이터를 수집할 수 없다. Cold start를 어떻게 해결할지?"
   - 이유: Cold start 문제는 growth-loop의 Anti-Loop Detection과 직결

4. "우리 에이전트 제품이 시간이 지날수록 경쟁사보다 더 강해지는 해자를 가지려면 어떻게 해야 할까?"
   - 이유: 데이터 플라이휠을 통한 경쟁 우위 설계 — growth-loop → moat으로 연결

5. "사용자가 피드백을 주지 않아서 에이전트 개선이 안 되고 있다. 명시적 피드백을 어떻게 수집할까?"
   - 이유: 데이터 수집 방법(explicit/implicit/hybrid) 설계가 필요

### Should NOT Trigger (5)

1. "우리 플라이휠이 강한지 약한지 경쟁력을 평가하고 싶다"
   - 올바른 라우팅: `moat` (플라이휠 강도 평가)

2. "에이전트가 여러 개인데 각각 학습한 데이터를 공유해야 한다. 어떻게 구조화할까?"
   - 올바른 라우팅: `memory-arch` 또는 `orchestration` (데이터 공유 아키텍처)

3. "우리 데이터 처리 비용이 너무 높아서 더 이상 플라이휠을 유지할 수 없다"
   - 올바른 라우팅: `biz-model` (비용 구조 검토)

4. "사용자가 데이터 수집을 거부해서 플라이휠을 만들 수 없을 것 같다"
   - 올바른 라우팅: `orchestration` (다른 루프 타입 고려) 또는 `moat` (대체 경쟁력)

5. "이 플라이휠 데이터를 에이전트 Instruction에 어떻게 반영할까?"
   - 올바른 라우팅: `pm-engine`의 `/tk-to-instruction` 사용

## 2) Edge Cases

### 경계 사례 (5)

1. **초기 데이터 부족 (Cold Start) 극복**
   - 입력: "우리는 아직 사용자가 거의 없다. 플라이휠을 어떻게 시작할까?"
   - 예상 행동: Seed data (수동 생성), Transfer learning (유사 도메인), TK injection (전문가 개입) 중 최소 1가지 제안
   - 근거: Growth-loop 페이지의 "Kickstart Strategy" — 플라이휠은 초기 데이터 없이 시작 불가능

2. **Anti-Loop 감지 (플라이휠 멈춤)**
   - 입력: "3개월 동안 데이터를 수집했는데 에이전트 성능이 안 올라갔다"
   - 예상 행동: Data decay, Privacy barrier, Cost escalation, Quality ceiling, Cold start 중 어느 것이 문제인지 진단
   - 근거: Failure Handling의 "Anti-Loop 발생" 사례

3. **플라이휠 주기가 너무 김 (4주 이상)**
   - 입력: "데이터 → 모델 업데이트까지 한 달이 걸린다. 사용자가 개선을 못 느낀다"
   - 예상 행동: 배치 처리 속도 개선 또는 자동화 평가 지표 도입 제안
   - 근거: Failure Handling의 "플라이휠 주기" 항목 — 사용자 인식이 핵심

4. **Type 선택 애매 (Type A vs Type B)**
   - 입력: "우리 에이전트는 콘텐츠도 생성하고, 생성한 콘텐츠로 사용자 유입도 되는데 어느 type인가?"
   - 예상 행동: 현재 핵심 차별화가 "더 나은 데이터"인지 "더 나은 콘텐츠"인지 명확히 한 후 Primary type 결정
   - 근거: Growth-loop의 "Step 1 — Core Loop Identification" — 여러 루프가 존재하면 가장 강한 것 우선

5. **Loop Strength 점수 저점 (15점 미만)**
   - 입력: "우리 플라이휠을 설계했는데 점수가 12점이다. 이건 의미가 있나?"
   - 예상 행동: 이 스킬로는 moat이 약함을 진단하고, 다른 전략(workflow lock-in, proprietary knowledge)으로 보완할 것을 제안
   - 근거: Growth-loop의 "Quality Gate — 플라이휠 강도 <15점이면 실제 방어 가능한 해자가 아님"

