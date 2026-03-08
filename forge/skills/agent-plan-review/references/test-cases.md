# Test Cases — agent-plan-review 스킬

## 1) Trigger Tests

### Should Trigger (5)

1. "morning-briefing 에이전트 설계를 구현 전에 완전히 검토해줄래? PRD가 있고 아키텍처 다이어그램도 있는데, 놓친 게 있을까봐."
   - 이유: 구현 전 4축 검증

2. "새로운 오케스트레이션 패턴(3개 에이전트)을 적용한 설계가 과하지는 않을까요? 구현 가능성을 검토해줄래?"
   - 이유: 복잡도 경고 필요

3. "토큰 비용이 생각보다 많을 수 있어서 설계를 검토하고 싶어. 컨텍스트 윈도우 최적화도 함께 봐줄래?"
   - 이유: 비용 & 스케일 리뷰

4. "에이전트가 실패했을 때 어떤 장애 모드가 있을 수 있는지 사전에 파악하고 싶어."
   - 이유: 장애 모드 분석

5. "기존 에이전트를 재설계하면서 범위가 커졌는데, MVP로 축소해야 할지 검토해줄래?"
   - 이유: Step 0 범위 점검

### Should NOT Trigger (5)

1. "에이전트 Instruction을 설계해줄래?"
   - 올바른 라우팅: `forge/instruction`

2. "컨텍스트 윈도우 예산을 계획해줄래?"
   - 올바른 라우팅: `forge/ctx-budget`

3. "비용 시뮬레이션을 해줄래?"
   - 올바른 라우팅: `oracle/cost-sim`

4. "SLO와 신뢰성 목표를 정의해줄래?"
   - 올바른 라우팅: `argus/reliability`

5. "오케스트레이션 패턴을 선택해줄래?"
   - 올바른 라우팅: `atlas/orchestration`

## 2) Functional Tests (Given-When-Then)

### Test 1: Step 0 범위 점검

**Given:**
- 에이전트: morning-briefing
- 설계: 프로토타입 단계, 도구 4개, 메모리 2개 파일

**When:**
- Step 0 범위 점검 실행

**Then:**
- Q1 기존 자산: "뉴스 수집 에이전트 존재, 요약 로직만 새로 추가"
- Q2 MVA: "단일 에이전트 + Telegram 전송만, 이미지 첨부는 v2로 미룸"
- Q3 복잡도: "도구 4개, 에이전트 1개 → 안전 범위"
- 범위 선택: "전체 리뷰" (또는 사용자가 축소/압축 선택)

---

### Test 2: 장애 모드 매트릭스 작성

**Given:**
- 이미지 생성 에이전트 설계

**When:**
- 장애 모드 분석 요청

**Then:**
- 5개 이상 장애 유형 식별:
  1. API 타임아웃: 확률 중간, 영향도 높음
  2. 안전 필터: 확률 낮음, 영향도 높음
  3. 비용 폭주: 확률 중간, 영향도 높음
  4. 환각 이미지: 확률 낮음, 영향도 중간
  5. 메모리 부족: 확률 낮음, 영향도 높음
- 각 항목별 "설계에 반영?" 확인
- 미반영된 높음/매우높음 = 치명적 gap으로 표시

---

### Test 3: 이슈 보고 및 트레이드오프 제시

**Given:**
- 아키텍처 리뷰에서 "3개 에이전트 오케스트레이션" 발견

**When:**
- 이슈 보고

**Then:**
- 문제: "3개 에이전트 오케스트레이션은 복잡도 경고"
- 옵션 A: "범위 축소 (에이전트 1개로 통합)" - 노력 적음, 위험도 낮음
- 옵션 B: "현 설계 유지 + Hierarchical 패턴" - 노력 많음, 위험도 중간
- 옵션 C: "Sequential로 단순화" - 노력 중간, 기능 제한
- **권고: A를 먼저 검토하세요. 오케스트레이션은 복잡도 증가의 주요 원인입니다.**

## 3) Error Cases

### Error 1: Step 0 범위 점검 건너뜀

**상황:**
- 사용자가 "그냥 전체 리뷰해줄래?"만 하고, 기존 자산/MVA/복잡도 점검 안 함
- 설계가 실제로는 과도한데 미결정 상태로 진행

**대응:**
- Step 0을 강제로 실행
- 3개 질문 응답을 받을 때까지 다른 섹션으로 진행 안 함
- "먼저 범위를 명확히 해야 리뷰의 의미가 있습니다"

---

### Error 2: 장애 모드 매트릭스 불완전

**상황:**
- 장애 유형 3개만 식별, 영향도 높음인데 설계 미반영 항목 있음
- 치명적 gap 수 명시 안 함

**대응:**
- 장애 유형 최소 5개까지 확대
- 영향도 높음/매우높음 + 설계 미반영 = 치명적 gap 강조
- "이 gap을 구현 전에 반드시 해결해야 합니다"

## 3) Edge Cases

| # | 쿼리 | 판정 | 이유 |
|---|------|------|------|
| E1 | "에이전트 설계 리뷰를 하는데, 기술적 구현은 다 봤어. 이제 뭘 더 봐야 할까?" | ⚠️ 경계 | agent-plan-review는 "설계 검증"이므로 기술 구현 완료 후에는 범위 밖. 하지만 "배포 전 최종 리뷰"라면 여전히 유효 |
| E2 | "우리가 이미 premortem을 했어. 그래서 위험은 다 파악했는데, 또 agent-plan-review가 필요해?" | ✅ Trigger | premortem(위험 분석) vs agent-plan-review(범위/복잡도/비용/장애모드)는 다른 관점. 둘 다 필요할 수 있음. agent-plan-review는 "설계 완성도"에 초점 |
| E3 | "에이전트 아키텍처를 설계하는 중이야. 아직 PRD나 Instruction은 없는데 리뷰할 수 있을까?" | ⚠️ 경계 | agent-plan-review는 "구현 전 완성된 설계" 가정. 아키텍처만 있으면 Step 1 (범위) 검증 불가. "최소한 PRD 초안" 필요 |
| E4 | "설계는 완벽한데, 팀 리소스가 부족해서 MVP로 축소하고 싶어. 이것도 agent-plan-review로 검토할 수 있을까?" | ✅ Trigger | "범위 축소"는 Step 0 (범위 점검)에서 다뤄짐. "기존 자산/MVA/복잡도" 재평가로 축소 근거 제시 가능 |
| E5 | "에이전트를 구현하다가 설계 문제를 발견했어. 이제 다시 plan-review를 해야 할까, 아니면 대기 중인 이슈로 기록할까?" | ❌ Route → argus/incident 또는 backlog | 구현 중 발견된 문제는 agent-plan-review 범위 밖. incident 처리 또는 기술 부채 추적 영역 |

---

## 4) With/Without Skill 비교

### 시나리오: 리뷰 없이 곧바로 구현

**Without Agent-Plan-Review:**
- 설계 → 구현 시작
- 절반쯤 진행: "아, 비용이 너무 많네"
- 마지막 단계: "이 아키텍처 너무 복잡한데?"
- 결과: **재작업 필요**

**With Agent-Plan-Review:**
- Step 0 범위 점검: MVP로 축소하기로 결정
- 장애 모드: 5개 유형 사전 파악, 대응 계획 수립
- 비용 추정: 구현 전에 가능성 확인
- 결과: **일사천리 구현**

## 5) Skill Creation Gate 기반 추가 테스트 케이스

### Test Case 1: Core-5 정상 통과 (모든 필수 입력 제공)

**Given:**
- 에이전트 리뷰 요청
- 리뷰 메타데이터:
  - owner: "Alice (리드 엔지니어)"
  - due_date: "2026-03-14 17:00"
  - problem_statement: "오케스트레이션 패턴(3개 에이전트) 복잡도 검증 필요" + "현재 비용 예상 미정" + "구현 전 설계 재검토 필요"
  - priority: "P1 (구현 차단)"
  - trace_links: "PRD: ./agent-prd.md | Instruction: ./instruction.md | Slack: https://slack.com/...""

**When:**
- Step 0 범위 점검 실행

**Then:**
- 5가지 요소 모두 검증 완료 (Yes/Yes/Yes/Yes/Yes)
- 리뷰 프로세스 진행 가능
- 산출물에 "Core-5 검증 완료" 배지 추가

---

### Test Case 2: problem_statement 3요소 중 1개 누락 → BLOCK + What/Why/Fix

**Given:**
- 리뷰 요청
- problem_statement: "오케스트레이션 복잡도 검증" (현재 상태만, 바라는 상태 없음)
- 나머지 4가지: 정상

**When:**
- 리뷰 진행 시도

**Then:**
- **BLOCK**: "Problem Statement 불완전. 다음 3가지를 모두 명시하세요."
  - What: 현재 상태 (기술됨 ✓)
  - Why: 바라는 상태 (미기술 ✗)
  - Why-Context: 왜 중요한가 (확인 필요)
- 피드백:
  ```
  What: 현재 3개 에이전트 오케스트레이션 설계 검토 필요

  Why: 오케스트레이션을 일사천리 구현하려면,
  사전에 복잡도 임계값 초과 여부를 확인해야 함

  Fix: Problem Statement에 다음 추가:
  "바라는 상태: 설계를 MVP(에이전트 1개) 또는
  Full(현 설계 유지)로 결정하고, 리스크 맵핑 완료"

  Example:
  - Good: "3개 에이전트 오케스트레이션이
    비용/복잡도 임계값을 초과하는지 검증하고,
    MVP로 축소할지 현 설계를 유지할지 의사결정 필요"
  - Bad: "오케스트레이션이 복잡할 수 있어"
  ```

---

### Test Case 3: 반복 실패 시 피드백 우선순위 재정렬 동작 확인

**Given:**
- 동일한 이슈로 3회 연속 리뷰 요청
- Issue: "장애 모드 매트릭스 불완전 (4개만 식별)"
- 기대: 첫/두/세 번째 피드백이 우선순위 재정렬됨

**When:**
- 1차 리뷰 → 실패 → 2차 리뷰 → 실패 → 3차 리뷰

**Then:**
- **1차 피드백** (P1): "장애 모드 5개 이상 필수. 구체적 6가지 추가 모드 제시"
- **2차 피드백** (P1, with examples): 참고 사례 3가지 + 각 항목별 "설계 반영?" 체크리스트
- **3차 피드백** (Priority 재정렬):
  - **critical**: "API 타임아웃, 인증 실패 = 구현 중 반드시 처리"
  - **non_critical**: "메모리 손상, 권한 부족 = 모니터링으로 관찰 후 v1.1에 반영"
  - 결론: "완벽한 매트릭스보다, 지금은 Critical 3가지를 잘 설계하고 시작하자"

---

### Test Case 4: trace_links 포맷 오류 → 구조화된 피드백 + Good/Bad Example

**Given:**
- trace_links 입력: "뭔가 prd 파일이 있어"
- 포맷: 유효하지 않은 마크다운 링크 또는 절대경로 누락

**When:**
- Core-5 검증 실행

**Then:**
- **BLOCK**: "trace_links 포맷 오류. 다음 구조로 수정하세요."
- 피드백:
  ```
  What: trace_links가 역추적 불가능한 형식

  Why: 이 리뷰 결과가 어느 문서로 영향을 미치는지
  추적할 수 없으면, 차기 리뷰 시 기존 결과를 재사용 불가능

  Fix: 다음 포맷으로 수정:
  - PRD: /path/to/agent-prd.md |
  - Instruction: /path/to/instruction.md |
  - GitHub Issue: https://github.com/...

  Example:
  - Good: "PRD: ~/Documents/3_Code/Vibe/Project/morning-briefing/agent-prd.md | GitHub: https://github.com/org/repo/issues/42"
  - Bad: "PRD 파일이 어딘가 있고", "예전에 본 이슈"
  ```
