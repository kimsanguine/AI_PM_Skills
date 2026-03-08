# Domain Context — prompt 스킬

## 1) Domain Scope

**이 스킬이 소유하는 영역:**
- System Prompt 또는 Agent Instruction 초안 작성 후 검토 및 최적화
- CRISP 프레임워크(Context/Role/Instruction/Scope/Parameters) 체계적 적용
- 판단 기준 명시화(정성적 → 정량적) 및 실패 패턴 회피

**이 스킬이 소유하지 않는 영역:**
- 7요소 Instruction 설계 전체 (→ `forge/instruction`)
- 컨텍스트 윈도우 토큰 최적화 (→ `forge/ctx-budget`)
- 판단 로직의 암묵지 추출 (→ `muse/pm-engine`)

## 2) Primary Users

- **초안 작성자**: System Prompt 초안 이후 최적화 필요
- **디버깅 담당**: 에이전트가 예상 밖의 행동을 할 때 프롬프트 문제점 진단
- **PM**: 기술적이지 않은 관점에서 프롬프트 설계 의도 명확화

## 3) Required Inputs

**필수 입력:**
1. 현재 프롬프트 또는 초안
2. 문제점 또는 최적화 목표
3. 에이전트의 역할/목표

**선택 입력:**
- 사용 중인 모델(Haiku/Sonnet/Opus)
- 컨텍스트 윈도우 제약사항

## 4) Output Contract

**산출물:**
- CRISP 5요소가 명확한 최적화된 프롬프트
- Why-First 원칙 적용으로 의도 기반 설계
- 판단 기준 테이블(정량적)

| 항목 | 보증 |
|------|------|
| CRISP 5요소 | 최소 4개 명시 |
| 명확성 | 모호한 표현 제거 |
| 판단 기준 | 정량적 기준 제시 |
| Anti-Goals | 최소 2개 명시 |
| 실패 처리 | 데이터 없음/불확실 케이스 정의 |

## 5) Guardrails

**라우팅 규칙:**
- 7요소 Instruction 전체 설계 필요 → `forge/instruction`
- 컨텍스트 윈도우 최적화 필요 → `forge/ctx-budget`
- PM 암묵지 추출 → `muse/pm-engine`

**품질 기준:**
- 프롬프트는 기술적 완벽성이 아닌 "의도 명확성" 우선
- 정성적 표현("좋은", "빠른") 금지, 정량적 기준 필수
- 7가지 실패 패턴 체크필수

## 6) Working Facts

**CRISP 5요소 작성 시간:**

| 요소 | 예상 시간 | 토큰 |
|------|----------|------|
| Context | 5분 | 100~150 |
| Role | 5분 | 100~150 |
| Instruction | 10분 | 200~300 |
| Scope | 10분 | 200~300 |
| Parameters | 5분 | 100~150 |
| **Total** | **35분** | **~700~1,050 tokens** |

**프롬프트 실패 패턴 7가지 (예시값):**
1. 목표 모호성
2. Anti-Goals 누락
3. 출력 형식 미명시
4. 컨텍스트 과부하
5. 판단 기준 부재
6. 실패 처리 누락
7. 역할 충돌

**TO BE UPDATED by reviewer:**
- 조직별 판단 기준의 정량화 기준
- 프롬프트 복잡도별 최적 길이
- CRISP 5요소의 필수/선택 여부

## 7) Fill-in Checklist

- [ ] CRISP 5요소 중 최소 4개가 명시되었는가?
- [ ] 목표가 명확하고 모호하지 않은가?
- [ ] Anti-Goals가 최소 2개 이상인가?
- [ ] 판단 기준이 정량적인가? (수치, 임계값, 점수)
- [ ] 7가지 실패 패턴 체크를 완료했는가?
- [ ] Why-First 원칙이 적용되었는가? (주요 지시마다 "왜" 명시)
- [ ] 실패 처리 케이스가 정의되었는가?
- [ ] 프롬프트 길이가 컨텍스트 윈도우의 5% 이내인가?

---

## 8) 참고 사례: ReAct 패턴과 도구 기반 에이전트 프롬프트

> **아래는 특정 프로덕션 환경에서의 사례입니다. 조직과 도메인에 따라 다르게 설계할 수 있습니다.**

### ReAct 패턴 간단 소개

ReAct (Reasoning + Acting)은 에이전트가 **Thought → Action → Observation → 최종 답변**의 4단계 루프를 따르도록 유도하는 패턴입니다. 사용자 질문 → 내부 분석 → 도구 호출 → 결과 확인 → 정제된 답변으로 진행되며, 이를 통해 투명성과 디버깅 가능성이 높아집니다. 자세한 ReAct 패턴은 AI 에이전트 프롬프팅 문헌을 참고하세요.

---

### 도구 설명 구조화: 효과적인 도구 명세서 작성 방법

에이전트가 도구를 올바르게 선택하려면, 각 도구의 설명이 **이름 → 설명 → 입력 파라미터 → 예시**의 4단계 구조를 따라야 합니다:

```markdown
도구명: [tool_name]
설명: [이 도구가 해결하는 사용자 의도]
입력: [파라미터명 (타입) — 역할 설명]
출력: [반환되는 데이터 구조 및 형식]
예시:
  입력: tool_name(param1=value1, param2=value2)
  출력: [실제 반환 예시]
```

이 구조를 따르면 에이전트가 "언제" "어떻게" 도구를 쓸지 명확히 이해합니다.

---

### Agent 프롬프트 설계의 핵심: "도구 선택 능력"을 프롬프트로 부여

#### 좋은 프롬프트 vs 나쁜 프롬프트

**나쁜 예 (도구 선택 능력 없음):**
```
system_prompt = """
당신은 AI 어시스턴트입니다. 사용자의 질문에 답변하세요.
사용 가능한 도구:
1. notion_query
2. github_search
3. slack_send

사용자 질문에 대해 도움이 되는 답변을 주세요.
"""

문제점:
- "도구를 언제 써야 할까?" 아무도 모름
- "notion_query가 뭘 하는 건지?"도 불명확
- 에이전트가 도구 선택을 못 함
```

**좋은 예 (도구 선택 능력 명시):**
```
system_prompt = """
당신은 팀 일정 관리 어시스턴트입니다.

당신이 할 수 있는 일:
1. 팀 회의 일정 조회 (Notion 사용)
   - 언제 써?: "이 주 회의", "다음 달 스프린트 일정"
   - 도구: notion_query(database="Team Schedule")
   - 예: "목요일 회의가 뭐야?" → notion_query 호출

2. 코드 변경 조회 (GitHub 사용)
   - 언제 써?: "최근 PR", "누가 뭘 수정했어?"
   - 도구: github_search(repo="our-repo")
   - 예: "Authentication 코드 변경 이력?" → github_search 호출

3. Slack에 알림 (Slack 사용)
   - 언제 써?: "팀에 알려줄래?", "메시지 보낼래?"
   - 도구: slack_send(channel="general")
   - 예: "내일 회의 오지말라고 공지" → slack_send 호출

당신이 하지 말아야 할 일:
- ✗ 확실하지 않은 날짜 만들기 (항상 Notion에서 확인)
- ✗ 사용자 동의 없이 Slack 메시지 보내기 (항상 "이렇게 할까요?" 물어보기)
- ✗ 없는 도구 호출 (위 3가지만 가능)

추론 과정 (ReAct):
1. Thought: 사용자가 뭘 원하는지 분석
2. Action: 필요한 도구 선택 및 호출
3. Observation: 도구 결과 확인
4. Final Answer: 사용자에게 답변
"""
```

**차이점:**
- 나쁜 예: 도구 목록만 나열 (선택 기준 없음)
- 좋은 예: "이 상황에선 이 도구", "이렇게 호출" 구체적 지침

---

### System Prompt에서 도구 설명을 어떻게 구조화하는가

#### 구조 1: 기능 중심 (Function-Centric)
```
도구: notion_query
설명: Notion 데이터베이스 조회
사용법: notion_query(database, filter, limit)
예시: notion_query("Tasks", "status=pending", limit=10)
```

**장점:** 기술적으로 명확
**단점:** 에이전트가 "언제" 써야 할지 모름

#### 구조 2: 의도 중심 (Intent-Centric) ← 추천
```
의도: "팀의 미처리 업무를 알고 싶다"
도구: notion_query
사용 조건: 사용자가 "할 일", "뭘 해야 해?", "과제가 뭐야?" 물을 때
구체적 호출:
  notion_query(
    database="Tasks",
    filter="status=pending AND assignee=user_id",
    limit=10
  )
```

**장점:** 에이전트가 "언제" 쓸지 이해
**단점:** 약간 더 길지만, 정확도 훨씬 높음

---

### 적용 교훈: "좋은 에이전트 프롬프트의 3가지 조건"

#### 조건 1: 도구 선택의 트리거가 명확한가?

```
나쁜 예:
"notion_query를 사용할 수 있습니다"

좋은 예:
"사용자가 '팀 일정', '회의', '스케줄' 같은 단어를 쓸 때
 → notion_query를 호출하세요"
```

#### 조건 2: 각 도구의 입력/출력이 정의되어 있는가?

```
나쁜 예:
tools=[
  {
    "name": "notion_query",
    "description": "Notion 쿼리"
  }
]

좋은 예:
notion_query:
  입력: database name (str), filter (str), limit (int — 예시값: 5~10)
  출력: list of {title, date, status}
  예시:
    입력: notion_query("Team Schedule", "date >= 2025-03-07", limit=5)
    출력: [{title: "PM Meeting", date: "2025-03-07", status: "confirmed"}]
```

#### 조건 3: Anti-Goals (하지 말아야 할 것)가 있는가?

```
좋은 프롬프트는 "해야 할 것"뿐만 아니라 "하지 말아야 할 것"도 명시:

Anti-Goals:
- ✗ 사용자 동의 없이 Slack 메시지 보내기
- ✗ 확실하지 않은 날짜 가정하기
- ✗ 없는 팀원의 일정 조회 시도하기
```

---

### 실전 예제: 팀 일정 관리 에이전트의 완전한 프롬프트

```python
SYSTEM_PROMPT = """
## 역할 (Role)
당신은 팀 일정 관리 AI 어시스턴트입니다.
팀원의 회의 일정을 추적하고, 일정 충돌을 방지하며, 회의 알림을 관리합니다.

## 목표 (Goal)
- 팀원이 언제든 자신의 회의 일정을 조회할 수 있도록 지원
- 새로운 회의 일정을 추가할 때 충돌 방지
- 긴급 일정 변경 시 팀에 빠르게 알림

## 사용 가능한 도구

### 1. Notion 일정 조회
언제 사용?
  - 사용자가 "회의", "일정", "스케줄", "언제 뭐 해?" 물을 때

구체적 호출:
  notion_query(
    database="Team Schedule",
    filter="assignee={user_id} AND date >= {today}",
    limit=10  (예시값)
  )

예시:
  사용자: "이 주 내 회의가 뭐야?"
  → notion_query(database="Team Schedule", filter="date >= 2025-03-07 AND assignee=me", limit=10)
  → 결과: [{title: "PM Meeting", time: "10:00", date: "2025-03-09"}]

### 2. GitHub PR 확인
언제 사용?
  - 사용자가 "PR", "코드 리뷰", "변경 사항" 물을 때

구체적 호출:
  github_search(
    repo="our-repo",
    query="assignee:{user_id} is:open"
  )

### 3. Slack 알림
언제 사용?
  - 사용자가 명시적으로 "팀에 알려줘", "공지해줘" 요청할 때만

주의: 사용자 동의 필수 (항상 "이렇게 할까요?" 물어보기)

## 당신이 하지 말아야 할 일

✗ 불명확한 날짜 가정하기
  예: 사용자가 "다음 회의" → "언제?" 물어보기

✗ 사용자 동의 없이 Slack 메시지 보내기
  예: 항상 "팀에 알려드릴까요?" 먼저 확인

✗ 없는 팀원의 일정 조회
  예: "그 팀원은 우리 시스템에 없습니다" 알림

✗ 신뢰도 낮은 정보 제공
  예: "확실한 정보가 없어서 Notion을 확인했는데..."

## 추론 과정 (ReAct Loop — 예시값)

각 질문에 대해 다음 순서로 답변:

1. **Thought**: 사용자가 원하는 게 뭔지 분석
   "사용자가 '이 주 회의'를 원한다.
    → 나는 notion_query로 조회해야 한다.
    → 필터: date >= 이 주, assignee = 사용자"

2. **Action**: 도구 호출
   "notion_query 호출: database='Team Schedule', filter='date >= 2025-03-07' (예시날짜)"

3. **Observation**: 결과 확인
   "결과: 목요일 10:00 PM Meeting, 금요일 14:00 Retrospective"

4. **Final Answer**: 사용자에게 답변
   "이 주 당신의 회의:
    - 목요일 10:00: PM Meeting
    - 금요일 14:00: Retrospective"
"""
```

---

### 체크리스트: ReAct 패턴 프롬프트가 잘 설계됐는가?

- [ ] **도구의 사용 조건이 명확한가?**
  - "언제" 쓸지 구체적 상황 명시

- [ ] **각 도구의 입력/출력이 정의되었는가?**
  - 입력 파라미터, 출력 형식, 예시 3가지

- [ ] **Anti-Goals가 최소 2개 있는가?**
  - "하지 말아야 할 것"도 명시

- [ ] **ReAct 루프의 4단계 (Thought/Action/Observation/Final Answer)가 있는가?**
  - 명시되면 에이전트가 더 좋은 추론 제공

- [ ] **도구 사용이 사용자 동의를 구하는가?**
  - Slack 메시지 같은 "되돌릴 수 없는" 행동은 항상 확인

- [ ] **프롬프트가 도구 기술이 아니라 의도 중심인가?**
  - "함수 호출법" (X) → "언제 어떤 도구를 쓸까?" (O)
