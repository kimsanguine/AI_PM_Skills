---
name: prd
description: "Write a PRD specifically for an AI agent — covering Instruction, Tools, Memory, Triggers, Output, and Failure handling. Structurally different from a standard product PRD. Use when formally documenting an agent before implementation, or standardizing agent specs across a portfolio."
argument-hint: "[agent to spec]"
---

## Agent PRD Template

일반 PRD와 에이전트 PRD는 구조가 다릅니다.

| 일반 PRD | 에이전트 PRD |
|---|---|
| 사용자 스토리 중심 | Instruction 설계 중심 |
| 기능 명세 | 행동 + 판단 기준 명세 |
| UI/UX 흐름 | 트리거 → 실행 → 출력 흐름 |
| 성공 지표: DAU, 전환율 | 성공 지표: 정확도, 비용, 신뢰성 |
| 실패 처리: 에러 메시지 | 실패 처리: Fallback + Human escalation |

---

### Agent PRD 7섹션 구조

---

#### Section 1 — Overview

```
에이전트 이름:
버전:
작성일:
작성자:
상태: [Draft / Review / Approved / Deployed]

한 줄 정의:
[누구를 위해] [어떤 목적으로] [어떻게 동작하는] 에이전트

배경 / 만드는 이유:
[왜 지금 이 에이전트가 필요한가]
```

---

#### Section 2 — Instruction Design

에이전트의 정체성과 행동 원칙.  
→ [agent-instruction-design] 스킬의 7요소를 이 섹션에 채운다.

```
Role:
[에이전트의 역할 정의 — 1~3문장]

Primary Goal:
[단 하나의 핵심 목표]

Secondary Goals:
1.
2.

Anti-Goals (하면 안 되는 것):
1.
2.
3.
```

---

#### Section 3 — Tools & Integrations

에이전트가 사용하는 도구와 외부 연결 목록.

| 도구/API | 용도 | 사용 조건 | 호출 제한 |
|---|---|---|---|
| web_search | 최신 정보 수집 | 내부 데이터 부족 시 | 최대 5회/실행 |
| Read/Write | 파일 접근 | 메모리 읽기/저장 | 제한 없음 |
| message | Telegram 전송 | 최종 출력 | 1회/실행 |
| exec | 스크립트 실행 | 계산/데이터 처리 | 명시된 경우만 |

최소 권한 원칙: 필요한 도구만 포함, 각 도구의 사용 범위 명시

---

#### Section 4 — Memory Strategy

```
Working Memory (컨텍스트):
- 항상 로드: [파일 목록]
- 조건부 로드: [파일 목록 + 조건]
- 컨텍스트 예산: [예상 토큰 수]

Long-term Memory (파일):
- 읽기: [어떤 파일에서 무엇을 읽는가]
- 쓰기: [어떤 파일에 무엇을 저장하는가]
- 저장 트리거: [언제 저장하는가]

Procedural Memory (Skills):
- 사용하는 SKILL.md 목록
```

---

#### Section 5 — Trigger & Execution

```
트리거 유형:
☐ Cron (주기적)   — 스케줄:
☐ Event-Driven    — 이벤트:
☐ Manual          — 조건:
☐ Pipeline        — 선행 에이전트:

실행 흐름:
Step 1: [입력 수집]
Step 2: [처리]
Step 3: [출력 생성]
Step 4: [전달/저장]

예상 실행 시간: [초/분]
타임아웃 설정: [초]
```

---

#### Section 6 — Output Specification

```
출력 채널: [Telegram / 파일 / stdout / Notion / API]
출력 형식: [Markdown / Plain text / JSON / 구조화 텍스트]
출력 길이: [최대 N자 / N줄]
언어: [한국어 / 영어]
톤: [간결 / 상세 / 브리핑 / 대화형]

출력 예시:
---
[실제 출력 샘플 작성]
---
```

---

#### Section 7 — Failure Handling & Success Metrics

```
실패 시나리오:

| 시나리오 | 감지 방법 | 대응 행동 |
|---|---|---|
| 데이터 없음 | 빈 결과 반환 | 안내 메시지 전송 후 종료 |
| API 실패 | HTTPError | 3회 재시도 → 실패 알림 |
| 토큰 초과 | 컨텍스트 85%+ | 요약 후 핵심만 처리 |
| 판단 불확실 | 신뢰도 < 임계값 | Human-in-the-loop 에스컬레이션 |

Human-in-the-loop 트리거:
[어떤 상황에서 인간 판단을 요청하는가]

성공 지표:
- 정확도 목표: [%]
- 비용 목표: [월 $ 이하]
- 레이턴시 목표: [초 이하]
- 신뢰성 목표: [% uptime]
```

---

### 간소화 버전 (MVP PRD)

빠른 프로토타이핑용 1페이지 포맷:

```
에이전트: [이름]
목적: [한 줄]
트리거: [언제]
입력: [무엇을 받는가]
처리: [무엇을 하는가]
출력: [무엇을 전달하는가]
도구: [사용하는 도구]
모델: [Haiku / Sonnet / Opus]
실패 시: [어떻게 처리하는가]
성공 기준: [측정 방법]
```

---

### 사용 방법

`/write-agent-prd [에이전트 이름 또는 목적]`

---

### Instructions

You are helping write a complete **Agent PRD** for: **$ARGUMENTS**

**Step 1** — Section 1 Overview 작성 (에이전트 이름, 한 줄 정의, 배경)

**Step 2** — Section 2 Instruction Design  
→ `agent-instruction-design` 스킬의 7요소 적용

**Step 3** — Section 3 Tools & Integrations  
도구 목록 + 최소 권한 원칙 적용

**Step 4** — Section 4 Memory Strategy  
3계층 메모리 계획 (`memory-architecture` 스킬 연계)

**Step 5** — Section 5 Trigger & Execution  
트리거 유형 선택 + 실행 흐름 Step-by-Step

**Step 6** — Section 6 Output Specification  
채널/형식/길이/예시 포함

**Step 7** — Section 7 Failure Handling & Success Metrics  
실패 시나리오 테이블 + KPI 목표값 설정  
(`agent-kpi` 스킬 연계)

**Step 8** — PRD 검토  
- Anti-Goals가 충분히 구체적인가?
- 실패 시나리오가 완전한가?
- 성공 지표가 측정 가능한가?

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- 일반 PM PRD 템플릿 기반 → 에이전트 특화 70% 재작성
- Sections 4~7: OpenClaw 크론잡 운영 경험에서 도출

---

## Further Reading
- Marty Cagan, *INSPIRED* — Product requirements and discovery
- Shreyas Doshi — "Pre-Mortem for PRDs" framework
