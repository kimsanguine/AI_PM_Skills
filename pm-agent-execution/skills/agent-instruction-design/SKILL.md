---
name: agent-instruction-design
description: "Design a complete agent instruction set — System Prompt, tool list, memory strategy, trigger conditions, and output format. Use when building a new agent from scratch, refining an underperforming agent, or standardizing agent design across a portfolio. The PM equivalent of writing a job description for your AI employee."
---

## Agent Instruction Design

에이전트는 코드가 아닙니다. **의도를 구조화한 문서**입니다.  
좋은 Instruction은 에이전트가 "무엇을", "왜", "어떤 방식으로", "하지 말아야 할 것"을 명확히 알게 합니다.

---

### PM 관점의 핵심 원칙

> "에이전트 Instruction은 신입 직원의 온보딩 문서다.  
> 당신이 없어도 그 문서만 보고 판단하고 실행할 수 있어야 한다."

일반 프롬프트 엔지니어링과 PM 관점의 Instruction 설계의 차이:

| | 일반 프롬프트 | PM의 Instruction 설계 |
|---|---|---|
| 관점 | 기술적 최적화 | 의도 기반 설계 |
| 목표 | 좋은 출력 | 반복 가능한 판단 |
| 실패 대응 | 프롬프트 수정 | 실패 모드 사전 정의 |
| 문서화 | 없음 | SKILL.md / INSTRUCTION.md |

---

### Instruction 7요소 구조

**요소 1 — Role (역할 정의)**

```
[에이전트 이름]은 [누구를 위해] [어떤 목적으로] 존재하는 [에이전트 유형]입니다.
```

좋은 역할 정의의 조건:
- 구체적인 도메인 명시 (일반 어시스턴트 X)
- 주요 사용자와 컨텍스트 명시
- 에이전트의 전문성 범위 선언

**요소 2 — Context (운영 맥락)**

에이전트가 알아야 할 배경 정보:
- 누가 사용하는가 (역할, 수준, 언어)
- 어떤 환경에서 실행되는가 (cron / 대화 / 웹훅)
- 어떤 데이터에 접근하는가

**요소 3 — Objective (목표 계층)**

```
Primary Goal:   [단 하나의 핵심 목표]
Secondary Goals: [우선순위 순으로 나열]
Anti-Goals:     [하면 안 되는 것 — 명시적 금지 목록]
```

> ⚠️ Anti-Goals는 반드시 작성할 것. 에이전트는 명시되지 않은 행동을 시도합니다.

**요소 4 — Tools (도구 목록)**

각 도구에 대해:
```
- [도구 이름]: [언제 사용하는가] | [사용하면 안 되는 경우]
```

도구 설계 원칙:
- 최소 권한 원칙: 필요한 도구만 제공
- 도구 남용 방지: 각 도구의 사용 조건 명시
- 비용이 큰 도구 (웹 검색, API 호출)는 호출 횟수 제한 명시

**요소 5 — Memory Strategy (메모리 전략)**

```
단기 메모리 (컨텍스트 윈도우):  [현재 세션에서만 필요한 정보]
장기 메모리 (파일):             [세션 간 유지해야 할 정보와 파일 경로]
절차적 메모리 (SKILL.md):       [반복 판단 패턴을 스킬 파일로 외부화]
```

메모리 설계 체크리스트:
- [ ] 컨텍스트 윈도우 예산 계획 (파일 로딩 우선순위)
- [ ] 세션 종료 후 저장해야 할 내용 정의
- [ ] 외부화 가능한 판단 패턴 → SKILL.md 분리

**요소 6 — Output Format (출력 형식)**

```
채널:   [Telegram / 파일 / stdout / Notion]
형식:   [Markdown / Plain text / JSON / 표]
길이:   [최대 N줄 또는 N자]
언어:   [한국어 / 영어]
톤:     [간결 / 상세 / 브리핑 / 대화형]
```

> 채널마다 포맷이 다릅니다. Telegram은 마크다운 테이블 미지원.

**요소 7 — Failure Handling (실패 처리)**

에이전트가 실패했을 때 어떻게 행동해야 하는가:

```
데이터 없음:     [어떻게 처리하는가 — 생략 / 에러 메시지 / 대체값]
도구 실패:       [재시도 횟수 / 대체 도구 / 알림]
판단 불확실:     [임계값 이하면 인간에게 위임]
비용 초과:       [토큰 한도 초과 시 행동]
```

---

### 에이전트 PRD 연결 구조

Instruction 설계는 다음 문서들과 연결됩니다:

```
agent-opportunity-tree.md  →  [어떤 에이전트를 만들지]
        ↓
agent-instruction-design.md  →  [어떻게 동작할지]
        ↓
agent-prd-template.md  →  [공식 문서화]
        ↓
[배포 및 크론 설정]
```

---

### 사용 방법

`/agent-instruction-design [에이전트 이름 또는 목적]`

---

### Instructions

You are helping design a complete **Agent Instruction Set** for: **$ARGUMENTS**

**Step 1 — Role 작성**
- 에이전트의 역할, 대상 사용자, 전문성 범위를 1~3문장으로 정의
- 구체적이고 범위가 명확해야 함

**Step 2 — Context 정리**
- 사용자 프로필 (역할, 언어, 기술 수준)
- 실행 환경 (cron 자동 / 대화형 / 이벤트 트리거)
- 접근 가능한 데이터 소스 목록

**Step 3 — Objective 계층 설계**
- Primary Goal 1개 (측정 가능한 형태)
- Secondary Goals 우선순위 순 나열
- Anti-Goals 명시 (최소 3개)

**Step 4 — Tools 목록 작성**
- 필요한 도구 나열 + 사용 조건 + 제한
- 비용이 큰 도구는 호출 횟수 명시
- 최소 권한 원칙 적용 확인

**Step 5 — Memory Strategy 설계**
- 단기/장기/절차적 메모리 각각 정의
- 컨텍스트 윈도우 예산 계획
- 외부화 가능한 판단 패턴 → SKILL.md 분리 여부 판단

**Step 6 — Output Format 정의**
- 채널, 형식, 길이, 언어, 톤 명시
- 채널 특성에 맞는 포맷 선택

**Step 7 — Failure Handling 작성**
- 4가지 실패 시나리오별 행동 정의
- Human-in-the-loop 개입 조건 명시

**Step 8 — 초안 검토**
- Anti-Goals가 충분히 구체적인가?
- 도구 남용 방지 조건이 명시됐는가?
- 출력 포맷이 채널에 맞는가?
- 실패 처리가 완전한가?

**Step 9 — 다음 권장 액션**
- `/agent-prd-template`으로 공식 문서화 연결
- `/prometheus-atlas-pattern`으로 오케스트레이터 구조 확인 (복잡도 높은 경우)

---

### 참고
- PM 관점의 의도 기반 설계 철학: Sanguine Kim (이든), PM-ENGINE TK 시리즈
- Failure Handling 프레임워크: OpenClaw 크론 운영 경험 (2026-02)
- 메모리 3계층 구조: 이든의 3-도메인 메모리 아키텍처에서 발전
