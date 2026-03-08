# Test Cases — moat 스킬

## 1) Trigger Tests

### Should Trigger (5)

1. "우리 에이전트가 경쟁사와 어떻게 다른지, 오래 유지할 수 있는 우위가 뭔지 알고 싶다"
   - 이유: 6가지 moat 유형 평가와 경쟁 우위 분석

2. "We're launching an agent product next quarter. How do we make sure competitors can't easily copy us?"
   - 이유: Moat 구축 로드맵과 장기 방어 전략 설계

3. "우리 moat이 약하다는 걸 깨달았다. 지금부터 뭘 강화해야 할까?"
   - 이유: Moat 약화 시 대체 전략과 취약점 보강 계획

4. "데이터 moat을 믿었는데 경쟁사가 빠르게 따라잡는다. 뭐가 문제일까?"
   - 이유: Anti-moat 패턴 감지 및 진정한 moat vs 거짓 moat 구분

5. "초기 우위는 UX인데, 장기 방어는 뭘로 할까? 로드맵을 짜고 싶다"
   - 이유: Moat 단계별 구축(Phase 1~4) 전략

### Should NOT Trigger (5)

1. "우리 데이터 플라이휠은 어떻게 설계할까?"
   - 올바른 라우팅: `growth-loop` (플라이휠 설계)

2. "경쟁사는 누가 있고 뭘 하는가?"
   - 올바른 라우팅: oracle의 `competitor` 스킬

3. "Moat를 지키려면 비용이 얼마나 들까?"
   - 올바른 라우팅: `biz-model` (비용 시뮬레이션)

4. "Workflow lock-in을 기술적으로 어떻게 구현할까?"
   - 올바른 라우팅: `3-tier` 또는 `orchestration` (기술 아키텍처)

5. "우리 moat이 법적으로 보호되나?"
   - 올바른 라우팅: 법률 전문가 또는 compliance 팀

## 2) Edge Cases

### 경계 사례 (4)

1. **거짓 Moat 감지: "우리 UI가 정말 예쁘다"**
   - 입력: "우리의 moat은 UX다. 경쟁사가 따라올 수 없다"
   - 예상 행동: Anti-moat 패턴 확인 — UI는 3~6개월이면 복제 가능, true moat이 아님을 지적
   - 근거: Moat SKILL.md의 "Anti-Moat Patterns" — Speed/UX moat은 Copy-Time 6~9개월 = weak moat

2. **Copy-Time 18개월 미만 = 진정한 moat 아님**
   - 입력: "우리 moat 강도는 4/5인데, 경쟁사가 12개월이면 따라할 수 있다"
   - 예상 행동: Copy-Time 재평가 — 12개월 < 18개월이므로 진정한 moat이 아님, 강화 필요 또는 다른 moat 추가
   - 근거: Moat의 "Step 4 — Moat Vulnerability & Copy-Time Analysis" — 18개월 미만이면 false moat

3. **Network Effect moat 가정이 실제로 성립하지 않음**
   - 입력: "Network Effect가 우리 moat인데, 사용자 수가 2배 늘었는데 NPS는 안 올랐다"
   - 예상 행동: "실제로는 Network Effect가 아닐 가능성" 진단 → 다른 moat으로 전환 제안
   - 근거: Failure Handling의 "Network Effect moat 실패"

4. **Moat 구축 비용이 예상 초과**
   - 입력: "데이터 moat 구축에 필요한 리소스(팀, 시간)가 예상의 3배다"
   - 예상 행동: 빠른 UX로 초기 lock-in 확보 후, 나중에 data moat 추구 전략 제안
   - 근거: Failure Handling의 "Moat 구축 비용이 초과"

