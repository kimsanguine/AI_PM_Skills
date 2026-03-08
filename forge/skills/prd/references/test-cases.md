# Test Cases — prd 스킬

## 1) Trigger Tests

### Should Trigger (5)

1. "비용 분석 에이전트의 PRD를 작성해줘. Instruction, Tools, Memory, Trigger, Output, Failure handling 전부 포함해서. 기존 BI 대시보드와 연동해야 해."
   - 이유: 구현 전 공식 명세서 필요

2. "I need a formal spec document for our content generation agent before handing it off to engineering. Should cover the agent's capabilities, failure modes, and integration points."
   - 이유: 구현팀 인수도 전 PRD 필요

3. "기존 뉴스 수집 에이전트(v1.0)를 확장하면서 PRD를 업데이트해야 해. 새로운 기능(이미지 첨부)을 추가하고, 메모리 전략도 재설계했어."
   - 이유: 기존 PRD 버전 업데이트

4. "에이전트 포트폴리오 표준화를 위해 3개 에이전트의 PRD를 일괄로 만들어줄래? 각각의 instruction은 있는데, PRD 포맷으로 통일하고 싶어."
   - 이유: 포트폴리오 표준화 목표

5. "배포 전 최종 리뷰를 위해 작성한 PRD 초안을 완성해줄래? 실패 시나리오와 성공 지표가 아직 미완성이야."
   - 이유: 배포 전 PRD 완성도 체크

### Should NOT Trigger (5)

1. "에이전트 오케스트레이션 패턴을 선택해줘."
   - 올바른 라우팅: `atlas/orchestration`

2. "PM 암묵지를 추출하고 TK 유닛으로 구조화해줘."
   - 올바른 라우팅: `muse/pm-engine`

3. "Instruction 7요소를 다시 설계해줄래? Role과 Anti-Goals이 명확하지 않아."
   - 올바른 라우팅: `forge/instruction`

4. "메모리 아키텍처를 다시 설계해야 해. 현재 모든 파일을 로드하는데 토큰 오버플로우 문제가 있어."
   - 올바른 라우팅: `forge/ctx-budget` 또는 `atlas/memory-arch`

5. "신뢰성 SLO를 정의하고, 장애 모드를 체계화해줄래?"
   - 올바른 라우팅: `argus/reliability`

## 2) Functional Tests (Given-When-Then)

### Test 1: 기본 PRD 작성 (7섹션 완성)

**Given:**
- 에이전트: morning-briefing (뉴스 수집 및 요약)
- 기존 정보: instruction.md 완료, 도구 목록 5개, 메모리 파일 3개

**When:**
- `/write-agent-prd morning-briefing` 스킬 실행

**Then:**
- 7섹션이 모두 작성됨:
  1. Overview: 이름, 버전, 한 줄 정의, 배경
  2. Instruction: Role, Primary Goal, Secondary Goals, Anti-Goals 명시
  3. Tools: 5개 도구 × (용도, 사용 조건, 호출 제한)
  4. Memory: Working/Long-term/Procedural 3계층 정의
  5. Trigger: Cron/Event/Manual/Pipeline 유형 명시, Step 5~10개
  6. Output: 채널(Telegram), 형식(Markdown), 길이(1000자), 예시 포함
  7. Failure: 실패 시나리오 4개 이상, 성공 지표 5개 이상
- 섹션 간 일관성 검증 완료

---

### Test 2: 기존 PRD 버전 업데이트

**Given:**
- 기존 PRD v1.0 존재 (sections 1~6 완료)
- 새 기능: 이미지 첨부, 메모리 전략 변경
- 불완전: Section 7 (Failure Handling) 미작성

**When:**
- 새 기능을 포함한 업데이트 요청

**Then:**
- Section 1, 3, 4 부분 업데이트
- Section 7 신규 작성
- 변경 사항이 명확히 기록됨

---

### Test 3: Anti-Goals 충분성 검증

**Given:**
- 초안 PRD의 Anti-Goals: 3개
- 검토 결과: "절대 하지 말아야 할 것" 불명확

**When:**
- 각 Anti-Goals가 구체적인 시나리오로 재작성되는지 검증

**Then:**
- 기존 Anti-Goals:
  - "추측 기반 권고 금지"
  - "비용 절감을 위해 기능 제거 권고 금지"
  - "일관되지 않은 계산 방식 금지"
- 재작성된 Anti-Goals:
  - "추측 기반 권고 금지": "모든 수치는 청구 API 데이터 기반, 추정값은 '추정' 표시"
  - "기능 제거 권고 금지": "비용 절감 제안은 최적화만 제시, 기능 제거는 절대 금지"
  - "일관되지 않은 계산 금지": "매달 동일한 로직으로 분석, 계산 방식 변경 시 이전월 재계산"

## 3) Error Cases

### Error 1: 실패 시나리오 불완전성

**상황:**
- 작성한 Failure Handling에 "데이터 없음" 시나리오만 있음
- 누락된 시나리오: API 실패, 토큰 초과, 판단 불확실

**대응:**
- 각 시나리오별 "감지 방법" + "구체적 대응 행동" 추가
- 최소 4개 시나리오까지 확대

---

### Error 2: 성공 지표 정량화 불가능

**상황:**
- 초안 성공 지표: "정확도 높음", "비용 효율적"
- 문제: 측정 방법 불명확

**대응:**
- "정확도 높음" → "API 청구 데이터 vs 리포트 비용 오차 < 1%"
- "비용 효율적" → "월 API 비용 $5 이하"

## 3) Edge Cases

| # | 쿼리 | 판정 | 이유 |
|---|------|------|------|
| E1 | "Instruction은 있는데 PRD를 따로 만들어야 할까? Instruction으로 충분하지 않을까?" | ⚠️ 경계 | Instruction은 "행동 지침" (implementation guide), PRD는 "공식 명세" (requirement doc). 팀 규모/조직 문화에 따라 PRD 필요성 다름. "구현팀 인수도" 필요하면 PRD 강력 권고 |
| E2 | "여러 팀이 같은 에이전트를 다르게 운영해야 해. 이 경우 PRD를 팀별로 여러 개 만들어야 할까?" | ✅ Trigger | 단일 PRD를 "코어 + 팀별 카스터마이징" 섹션으로 구성. 또는 "기본 PRD + 팀별 추가 문서" 방식 |
| E3 | "PRD에서 실패 시나리오를 너무 상세하게 쓰면 겁먹지 않을까?" | ✅ Trigger | 실패 시나리오는 "현실적 대비"를 위한 것. 오히려 팀이 "예상한 리스크는 다뤘다"는 신뢰감 가짐. 톤을 "객관적"으로 유지 |
| E4 | "PRD 작성 중에 기술적 구현 방식까지 명시해야 할까? 아니면 "요구사항만" 써야 할까?" | ⚠️ 경계 | PRD는 "무엇(What)"이고 구현은 "어떻게(How)". 하지만 "기술적 제약"(e.g., "Gemini API만 사용 가능")은 명시해야 함 |
| E5 | "PRD를 구현팀이 보면서 "이게 정말 가능한가" 의문이 생겼어. PRD를 수정해야 할까, 아니면 구현팀이 판단해야 할까?" | ✅ Trigger | "PRD vs 구현 가능성" 불일치는 Step 1 (agent-plan-review)의 영역일 수 있음. PRD 작성 전에 plan-review를 먼저 하는 것이 권장됨 |

---

## 4) With/Without Skill 비교

### 시나리오: 구현팀이 PRD 없이 instruction.md만 받은 경우

**Without PRD Skill:**
- 엔지니어가 instruction.md를 읽음
- 질문: "언제 실행되는 거지?" (Trigger 불명확)
- 질문: "실패하면 뭐 하는 거지?" (Failure Handling 불명확)
- 질문: "이 에이전트의 성공 기준이 뭐지?" (Success Metrics 불명확)
- **결과: 재작업 필요**

**With PRD Skill:**
- 엔지니어가 Section 5 (Trigger & Execution)를 읽음 → "매월 1일 Cron 실행"
- Section 7 (Failure Handling) 읽음 → "API 타임아웃 시 재시도 + Fallback"
- Section 7 (Success Metrics) 읽음 → "정확도 95%, 비용 $5/월 이하"
- **결과: 일사천리 구현 가능**

## 5) Quality Gate 기반 추가 테스트 케이스

### Test Case 1: 추상 표현("충분히", "적절히") 포함 시 → Quality Gate 실패

**Given:**
- PRD 초안 Section 6 (Output):
  ```
  출력 길이: 충분히 상세하되, 적절히 간결하게
  응답 시간: 빠르게 처리
  정확도: 높은 수준 유지
  ```
- 다른 섹션: 정상

**When:**
- Quality Gate 검증 실행

**Then:**
- **BLOCK**: "Quality Gate 실패. 추상 표현 3개 발견. 검증 가능한 수치로 수정하세요."
- 상세 피드백:
  ```
  What: 출력 길이/응답 시간/정확도 기준이 측정 불가능

  Why: 구현팀이 "충분히"의 기준을 모르면,
  각자 다르게 해석 (코드 리뷰 분쟁 증가)

  Fix: 모든 요구사항에 단위 추가:
  1. "충분히 상세하되, 적절히 간결하게"
     → "최소 50자, 최대 1000자"
  2. "빠르게 처리"
     → "평균 응답 시간 < 5초, P95 < 15초"
  3. "높은 수준 유지"
     → "정확도 95% 이상 (청구 데이터 vs 리포트 오차 < 1%)"

  Example:
  - Good: "응답 시간: 평균 3초 이내, P99 < 10초"
  - Bad: "빠른 응답 시간"
  ```
- 수정 제출 후 재검증

---

### Test Case 2: 실패 케이스 3개 미만 정의 시 → 실패 처리 규칙 위반 경고

**Given:**
- PRD 초안 Section 7 (Failure Handling)
- 정의된 실패 시나리오: 2개
  - "시나리오 1: API 에러 (타임아웃)"
  - "시나리오 2: 데이터 없음"
- 누락된 시나리오: 인증 실패, 토큰 초과, 판단 불확실 등

**When:**
- Failure Handling 검증 실행

**Then:**
- **WARNING**: "실패 처리 규칙 위반. 최소 3개 이상의 실패 케이스 필수."
- 피드백:
  ```
  What: 실패 시나리오가 2개만 정의됨

  Why: 최소 3개 미만은 프로덕션 환경에서
  예상 못한 실패를 대응하지 못하게 함

  Fix: 다음 3가지 추가 시나리오 검토:
  1. "인증 실패 (API 키 만료, 권한 부족)"
  2. "토큰 초과 (컨텍스트 윈도우 부족)"
  3. "판단 불확실 (신뢰도 < 50%)"

  각 시나리오마다:
  - 감지 방법: [로그에서 뭘 확인할까?]
  - 중단 여부: [즉시 실패 vs 폴백 제공?]
  - 사용자 통지: [뭘 보여줄까?]
  - 재진입: [다음엔 언제 재시도?]

  Example:
  시나리오 3: "인증 실패"
  - 감지: API 응답 코드 401 또는 403
  - 중단: Yes (API 키 갱신 필요, 사용자 개입)
  - 통지: "인증 실패. API 키를 확인해주세요."
  - 재진입: 사용자가 키를 갱신한 후 재실행
  ```

---

### Test Case 3: Trigger Gate 상호배타성 위반 시 → Disambiguation 부재 경고

**Given:**
- PRD 초안의 Trigger 정의:
  ```
  Trigger 1: 사용자가 "PRD를 작성해줄래?"라고 요청
  Trigger 2: 에이전트 Instruction이 불완전할 때 자동 트리거
  Trigger 3: 기존 PRD를 업데이트하고 싶을 때
  ```
- 문제: Trigger 1 vs Trigger 2가 겹칠 수 있음
  (사용자가 Instruction 불완전 상태에서 PRD 요청하면?)

**When:**
- Trigger Gate 상호배타성 검증 실행

**Then:**
- **WARNING**: "Trigger Gate 불명확. Disambiguation 필요."
- 피드백:
  ```
  What: Trigger 1과 Trigger 2가 상충 가능

  Why: 사용자 입력 vs 자동 조건이 겹칠 때
  어떤 스킬을 먼저 실행할지 모호함

  Fix: Disambiguation 문장 추가:
  "PRD는 Instruction이 7요소 모두 정의된 상태에서만 시작.
  Instruction이 불완전하면 forge/instruction 먼저 완료."

  Example:
  - Good: "조건 A이면 이 스킬 | 조건 B이면 저 스킬 | 조건 A&B이면 A 먼저"
  - Bad: "둘 다 가능해" (모호함)
  ```
- 수정 제출 후 재검증
