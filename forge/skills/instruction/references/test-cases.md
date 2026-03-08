# Test Cases — instruction 스킬

## 1) Trigger Tests

### Should Trigger (5)

1. "뉴스 수집 에이전트의 Instruction을 완전히 다시 설계해줄래? 지금은 역할만 정의돼있고 Anti-Goals도 없어서 에이전트가 예상 밖으로 행동해."
   - 이유: 일관되지 않은 행동, 판단 기준 모호

2. "새로운 에이전트를 만드는데, 의도 기반 설계로 7요소 Instruction을 작성해줄래? 역할과 목표는 있는데, Tool 사용 조건과 Memory 전략이 명확하지 않아."
   - 이유: 새로운 에이전트 설계 초기 단계

3. "기존 3개 에이전트의 Instruction을 표준 포맷으로 통일해줄래? 현재는 포맷이 제각각이라서 이해하기 어려워."
   - 이유: 포트폴리오 표준화

4. "에이전트가 자꾸 확신 없는 답을 하는데, Anti-Goals에 '불확실하면 확인 필요 표시'를 추가해줄래?"
   - 이유: 기존 Instruction 개선

5. "Tool 사용 조건을 더 구체적으로 정의해줄 수 있어? 지금은 어떤 상황에서 어떤 도구를 써야 하는지 불명확해."
   - 이유: Tool 남용 방지 조건 명시

### Should NOT Trigger (5)

1. "프롬프트 토큰을 최적화해줄래?"
   - 올바른 라우팅: `forge/prompt`

2. "컨텍스트 윈도우 예산을 계획해줄래? 메모리 파일 3개를 로드하는데 토큰이 많을 것 같아."
   - 올바른 라우팅: `forge/ctx-budget`

3. "Agent PRD를 작성해줄래? Instruction은 완료됐어."
   - 올바른 라우팅: `forge/prd`

4. "에이전트 오케스트레이션 패턴을 선택해줄래?"
   - 올바른 라우팅: `atlas/orchestration`

5. "메모리 아키텍처를 다시 설계해줄래?"
   - 올바른 라우팅: `atlas/memory-arch`

## 2) Functional Tests (Given-When-Then)

### Test 1: 7요소 완성도 검증

**Given:**
- 에이전트: morning-briefing
- 기존 정보: Role만 정의됨, 나머지 6요소 미정의

**When:**
- `/agent-instruction-design morning-briefing` 스킬 실행

**Then:**
- 7요소가 모두 정의됨:
  1. Role: 뉴스 큐레이터(PM 관점)로서 인사이트 중심 (구체적)
  2. Context: PM 사용자, 매일 아침 8시, 기술 수준 높음
  3. Objective: Primary Goal 1개 + Secondary 3개 + Anti-Goals 4개
  4. Tools: 5개 도구 × (사용 조건 + 제한)
  5. Memory: Working(600 tokens) / Long-term(어제 캐시) / Procedural(요약 SKILL)
  6. Output: Telegram, Markdown, 500자, 한국어, 이모지
  7. Failure: 4개 시나리오 + 대응 방법

---

### Test 2: Anti-Goals 구체화

**Given:**
- 초안 Anti-Goals: "좋은 품질로 해줘", "빨리 해줘", "정확하게 해줘"

**When:**
- Anti-Goals 재작성 요청

**Then:**
- 재작성된 Anti-Goals:
  - "좋은 품질로" → "뉴스 3줄 이상(텍스트 손실), PM 인사이트 포함 필수"
  - "빨리 해줘" → "실제로 신뢰도 낮은 기사를 신뢰할 수 있는 것처럼 전달하지 않기"
  - "정확하게" → "영어 뉴스 불완전 번역 금지, 한국어 자연성 우선"

---

### Test 3: Tool 남용 방지 조건 정의

**Given:**
- Tools 목록: web_search, read_file, write_file, message (각각 조건 명시 안 됨)

**When:**
- 각 도구의 "사용 조건"과 "사용하면 안 되는 경우" 명시

**Then:**
- web_search: "내부 캐시(어제 뉴스) 부족 시만" + "최대 5회 제한"
- read_file: "어제 캐시 조회" + "제한 없음"
- write_file: "발송 완료 후" + "1회/실행"
- message: "요약 완성 후 무조건" + "1회/실행"

## 3) Error Cases

### Error 1: Anti-Goals 부재로 인한 판단 오류

**상황:**
- Instruction에 Primary Goal만 있고 Anti-Goals 미정의
- 에이전트가 확신 없는 내용도 사실처럼 전달

**대응:**
- Anti-Goals 최소 3개 이상 추가: "확신 불가능한 내용은 '❓ 확인 필요' 표시", "추측이 아닌 사실만 전달", "번역 품질 보증 안 될 시 원문 유지"

---

### Error 2: Tool 과다 호출로 인한 비용 폭주

**상황:**
- Tool 목록에는 있지만 "언제 쓸지" 조건 없음
- 에이전트가 모든 상황에서 web_search 호출

**대응:**
- forge/instruction 스킬로 각 도구의 "사용 조건" 명시: "web_search는 내부 데이터 부족 시만, 최대 5회 제한"

## 3) Edge Cases

| # | 쿼리 | 판정 | 이유 |
|---|------|------|------|
| E1 | "이미 쓰고 있는 에이전트가 있는데, System Prompt만 있고 따로 Instruction 문서가 없어. 지금 Instruction을 작성할 가치가 있을까?" | ⚠️ 경계 | 기존 에이전트라도 "유지보수 어려움" 또는 "팀 온보딩 필요"라면 유효. 하지만 "작동 중인 프로덕션 코드"라면 우선순위 낮을 수 있음 |
| E2 | "Memory 전략이 복잡한데, 이걸 Instruction에서 모두 다루기는 힘들 것 같아. ctx-budget 스킬과 어떻게 나눠서 해야 할까?" | ✅ Trigger | instruction은 "어떤 메모리를 쓸지" (전략), ctx-budget은 "토큰 예산을 어떻게 배분할지" (기술). 둘 다 필요하고, instruction이 먼저 완료되어야 함 |
| E3 | "우리 에이전트가 여러 언어를 지원해야 해. Anti-Goals를 언어별로 다르게 정의해야 할까?" | ✅ Trigger | 언어별로 문화적 차이가 있다면 각 언어의 Anti-Goals를 분리 정의하는 것이 맞음. instruction의 "Output Format" 섹션에서 언어별 변주 명시 가능 |
| E4 | "Tool 목록이 계속 늘어나고 있어. 모든 Tool에 대해 "사용 조건"을 명시하면 Instruction이 너무 길어지지 않을까?" | ⚠️ 경계 | 도구가 10개 이상이면 Instruction 분리 또는 Tool별 SKILL.md 외부화 권고. 핵심 도구만 inline으로 명시, 나머지는 링크 |
| E5 | "PM 암묵지를 Instruction에 담고 싶은데, 이건 instruction 범위인지 아니면 pm-engine 스킬인지 헷갈려." | ✅ Trigger | instruction은 "이 에이전트가 어떻게 동작할지" (구현 가이드). pm-engine은 "PM 판단 패턴" (조직 학습). instruction의 "Anti-Goals"에서 PM 암묵지 반영, 세부는 pm-engine으로 외부화 |

---

## 4) With/Without Skill 비교

### 시나리오: Instruction 없이 코드로만 에이전트 구현

**Without Instruction Skill:**
- 개발자가 에이전트 코드 작성 시 판단 기준이 애매함
- "확신 없으면 뭐 하지?" → 추측도 출력
- "tool 몇 번 써도 되지?" → 제한 없이 호출
- "실패하면?" → 에러 메시지만 출력

**With Instruction Skill:**
- 개발자가 Instruction 문서를 읽음
- Anti-Goals 명시: "확신 불가능하면 '확인 필요' 표시"
- Tool 사용 조건: "web_search 최대 5회"
- Failure Handling: "API 타임아웃 시 3회 재시도 → 실패 시 어제 결과 사용"

**결과: 일관되고 예측 가능한 행동**
