# Troubleshooting — moat 스킬

## 1) 의존 조건 부재: Moat 전략이 실제로 불가능한 경우

**증상:**
- "데이터 모아 moat"인데 실제로 고객이 데이터 공유를 거부
- "Network Effect"라고 했는데 고객들이 자유롭게 이동 가능
- Moat 강도는 높게 평가했는데 실행 불가능

**확인:**
- Moat 평가 당시 "Depends on" 항목을 확인했는가?
  - Data Flywheel: "고객이 데이터 공유에 동의"해야 함
  - Network Effects: "고객이 네트워크 효과를 체감"해야 함
  - Workflow Lock-in: "고객의 핵심 업무에 통합"되어야 함
- 실제 상황: 이 의존 조건들이 현재 충족되고 있는가?

**조치:**
1. **의존 조건 재검증**: 각 moat의 "Depends on" 항목을 고객과 재확인
2. **해당 moat 포기 고려**: 조건을 충족할 수 없으면 다른 moat 우선순위 상향
   - 예: Data Flywheel 불가능 → Workflow Lock-in 또는 Proprietary Knowledge로 전환
3. **고객 계약 재협상**: 데이터 공유 문제면 incentive 제공 (가격 할인 등)
4. **Alternative moat 구축**: Network Effect 실패면 → Switching Cost 강화 (고객 데이터 종속)
5. **타이밍 재조정**: "지금은 불가능하지만 1년 뒤라면?"을 고려

---

## 2) Moat 침식: 경쟁사가 빠르게 따라잡음

**증상:**
- 12개월 전: 우리가 30% 정확도 우위
- 지금: 경쟁사와 동등 수준 (±5%)
- "우리의 차별화가 사라졌네?"

**확인:**
- 실제 침식 원인은 무엇인가?
  - 경쟁사가 더 나은 모델(GPT-5 등) 사용? → 기술 commodity화
  - 경쟁사가 데이터 모으기 시작? → 우리의 Data Flywheel 약화
  - 고객이 경쟁사로 이동? → Workflow Lock-in 약함
  - 우리의 개선 속도 > 경쟁사의 따라잡기 속도는 아닌가?

**조치:**
1. **근본 원인 분석**: 기술 commodity? 데이터 부족? Lock-in 약함? 정확히 파악
2. **투자 방향 재조정**:
   - 기술 commodity면 → proprietary knowledge 강화 (도메인 전문성)
   - 데이터 부족이면 → Data Flywheel 가속 (수집 속도 2배)
   - Lock-in 약하면 → Workflow 통합 깊이 증가
3. **신규 moat 추가**: 기존 moat이 침식되면 추가 moat으로 보강
4. **가격 전략 변경**: Commodity화되면 가격 인하는 최후의 수단 — 차라리 고객 세그먼트 변경 고려
5. **6개월 재평가**: 투자 후 실제 격차 회복 여부 측정

---

## 3) Moat 구축 비용이 초과: 예상 리소스 3배 필요

**증상:**
- 계획: "Data Flywheel 구축 3개월, 팀 3명"
- 현실: "6개월 경과, 팀 9명, 아직도 진행 중"
- 수익으로 moat 비용 회수 불가능해 보임

**확인:**
- 실제 병목은 무엇인가?
  - 데이터 수집 속도 예상 오류?
  - 모델 평가/개선 사이클이 생각보다 느림?
  - 팀의 컨텍스트 부족?
- 다른 moat이 더 빠르고 저비용인가?
  - Workflow Lock-in: 3개월만으로 가능?
  - Proprietary Knowledge: 기존 전문가 활용?

**조치:**
1. **현재 진행 상황 멈추고 재평가**: "이 속도라면 6개월 더 필요한가?"
2. **빠른 Win 추구**: Data Flywheel 대신 Speed/UX moat으로 초기 고객 확보 (1개월)
3. **Hybrid 접근**: 작은 Data Flywheel (30일 사이클)로 시작, 확대는 나중에
4. **타이밍 조정**: Data Flywheel은 연기, Workflow Lock-in 우선 (더 빠름)
5. **자원 효율화**: 팀 규모 축소 또는 focus 재정의 (모든 기능 vs 핵심 기능)

---

## 4) Anti-Moat 패턴: "우리는 GPT-4를 쓴다"는 주장

**증상:**
- "우리의 moat은 최신 GPT-4 모델"
- 또는 "우리 프롬프트는 비밀"
- 또는 "우리 UI가 예쁘다"
- 하지만 경쟁사도 즉시 복제 가능 (1~3개월)

**확인:**
- Anti-moat 10가지 패턴에 해당하는가?
  - "We use GPT-4/Claude" → 모두 사용 가능 (~1주)
  - "Our prompts are secret" → 역설계 가능 (1~3개월)
  - "We were first" → First-mover advantage 약함 (6~18개월)
  - "Our UI is better" → 가장 쉽게 복제 (6~9개월)
  - "기술이 복잡하다" → 역설계/모방 가능 (3~9개월)

**조치:**
1. **Anti-moat 제거**: 위 5가지 항목 중 하나라도 있으면 삭제
2. **진정한 moat으로 재구성**:
   - Data Flywheel (경쟁사 데이터 접근 불가) — Copy-Time 24~36개월
   - Workflow Lock-in (고객 workflow에 깊이 통합) — Copy-Time 18~24개월
   - Proprietary Knowledge (도메인 전문성 인코딩) — Copy-Time 24~36개월
3. **"우리만의 데이터"라는 증거 제시**: "고객 X의 사례로 정확도가 75% → 92%로 올랐다" 같은 구체적 proof
4. **경쟁사 추적**: 정말로 경쟁사가 1주일 안에 복제했는가? 추적 및 검증

