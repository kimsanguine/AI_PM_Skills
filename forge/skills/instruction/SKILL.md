---
name: instruction
description: "Design a complete agent instruction set — System Prompt, tool list, memory strategy, trigger conditions, and output format. Use when building a new agent from scratch, refining an underperforming agent, or standardizing agent design across a portfolio. The PM equivalent of writing a job description for your AI employee."
argument-hint: "[agent to design instructions for]"
allowed-tools: ["Read", "Write"]
model: sonnet
---

## Agent Instruction Design

## Core Goal

- 에이전트의 7요소(역할/컨텍스트/목표/도구/메모리/출력/실패처리)를 명확히 정의하여 "신입 직원 온보딩" 수준의 일관성 있는 행동 지침 수립
- 의도 기반 설계로 기술 용어 대신 판단 기준과 트레이드오프를 명시하여 예외 상황에서도 올바른 방향으로 대응 가능하게 설계
- 반복 판단 패턴을 SKILL.md로 외부화하여 컨텍스트 낭비 방지 및 유지보수성 향상

---

## Trigger Gate

### Use This Skill When

- 새로운 에이전트를 처음부터 설계할 때 (또는 기존 에이전트 재설계)
- 에이전트가 일관되지 않은 행동을 보이거나 판단 기준이 모호할 때
- 에이전트 포트폴리오를 표준화하고 싶을 때
- Instruction 초안 검토 및 7요소 완성도 체크가 필요할 때

### Route to Other Skills When

- 프롬프트 최적화 필요 → `forge/prompt` 스킬로 라우팅 (CRISP 프레임워크 적용)
- 컨텍스트 윈도우 예산 계획 필요 → `forge/ctx-budget` 스킬로 라우팅 (메모리 전략의 토큰 배분)
- PRD 공식 문서화 필요 → `forge/prd` 스킬로 라우팅 (Instruction → PRD 변환)
- 반복 판단 패턴 → SKILL.md로 분리 (SKILL.md 스킬은 별도가 아니며, instruction 내에서 판단)

### Boundary Checks

- Instruction 설계는 **의도**를 명확히 하는 것이지, 특정 기술 구현(API 호출, 데이터베이스 쿼리)은 아님
- 7요소는 순서가 정해져 있지 않으며, 각 요소는 역할, 목표, 도구와 유기적으로 연결되어야 함
- Tool 목록은 "필요한 도구만" — 최소 권한 원칙 적용, 각 도구의 사용 조건 명시 필수

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|----------|------|------|
| Anti-Goals가 추상적이거나 구체적 사례가 없음 | 작성된 Anti-Goals를 읽고도 실제로 피해야 할 상황이 불명확 | Anti-Goals를 구체적 시나리오로 재작성 (예: "확신 없는 답 하지 않기" → "신뢰도 < 0.7이면 '확인 필요' 표시") |
| Tool 목록에 도구 명시는 있지만 "언제 사용" 조건이 없음 | 에이전트가 모든 상황에서 도구를 과다 호출 | 각 도구에 "사용 조건" + "사용하면 안 되는 경우" 추가 (예: web_search는 "내부 데이터 부족 시만" + "최대 5회 제한") |
| Memory Strategy 없이 어떤 파일을 로드할지 명시 안 됨 | 구현 시 에이전트가 필요한 메모리 파일을 모르거나 모든 파일을 로드하려고 시도 | forge/ctx-budget 스킬과 연계하여 필수/조건부/제외 메모리 명시 |
| Output Format이 채널에 맞지 않음 (예: Telegram에 테이블 포맷) | 실행 후 Telegram 메시지가 잘못 렌더링되거나 읽기 어려움 | 채널별 포맷 재정의 (Telegram은 마크다운 테이블 미지원 → 리스트 형식 변경) |
| Failure Handling이 "에러가 발생하면 알림" 수준으로만 작성됨 | 실제 에러 발생 시 에이전트가 어떻게 할지 판단 불가 | 각 실패 케이스별로 "감지 방법" + "구체적 행동" 명시 (예: "API 타임아웃 → 3회 재시도 → 실패 시 Fallback 값 반환") |

---

## Quality Gate

- [ ] Role: 역할 정의가 구체적이고 도메인 명시 (일반 어시스턴트 X) (Yes/No)
- [ ] Context: 사용자 프로필, 실행 환경, 접근 데이터 명시 (Yes/No)
- [ ] Objective: Primary Goal 1개 + Secondary Goals + Anti-Goals 3개 이상 (Yes/No)
- [ ] Tools: 각 도구별 "사용 조건" + "제한" + 최소 권한 원칙 적용 (Yes/No)
- [ ] Memory: 단기/장기/절차적 메모리 각각 정의 + 컨텍스트 예산 연계 (Yes/No)
- [ ] Output Format: 채널/형식/길이/언어/톤 모두 명시 (Yes/No)
- [ ] Failure Handling: 4가지 이상 실패 시나리오 + 구체적 행동 방안 (Yes/No)

---

## Examples

### Good Example

```markdown
# Agent Instruction — news-summarizer (뉴스 수집 및 요약)

## Role
news-summarizer는 이든의 **정보 수집 시간을 제로화**하는 뉴스 큐레이션 에이전트입니다.
매일 아침 AI/에이전트 관련 뉴스 5건을 수집하고, 각각을 3줄 요약으로 변환하여 Telegram으로 전송합니다.

## Context
- 사용자: PM (이든), 영어/한국어 모두 이해 가능, 기술 수준 높음
- 환경: Cron으로 매일 아침 8:00 자동 실행
- 데이터: 웹 검색 (Google News), 기존 뉴스 캐시

## Objective

**Primary Goal:**
매일 아침 8:00 전에 AI/에이전트 관련 뉴스 5건 + 개인 인사이트를 Telegram으로 전송

**Secondary Goals:**
1. 뉴스 3줄 요약이 기술 깊이 유지 (PM 입장에서 이해 가능)
2. 중복 뉴스 제외 (어제 보낸 뉴스 재전송 X)
3. 가짜 뉴스/낮은 신뢰도 기사 제외

**Anti-Goals:**
1. 뉴스 요약이 너무 짧아서 맥락 손실 (1줄은 금지)
2. 확신 없는 해석/추측을 마치 사실인 것처럼 전달 (→ "의견" 표시)
3. 영어 뉴스를 불완전하게 번역 (한국어 자연성 우선)
4. 스팸 성격의 뉴스레터를 뉴스로 착각 (공식 미디어만)

## Tools

| 도구 | 용도 | 사용 조건 | 제한 |
|------|------|----------|------|
| web_search | 최신 AI 뉴스 검색 | 내부 캐시 (어제 뉴스)에 없는 주제 | 최대 5회/실행 |
| read_file | 어제 발송 뉴스 캐시 조회 | 중복 확인용 | 매번 로드 |
| write_file | 오늘의 뉴스 캐시에 저장 | 발송 완료 후 | 제한 없음 |
| message (Telegram) | 최종 결과 전송 | 요약 완성 후 무조건 | 1회/실행 (한 번만) |

## Memory Strategy

**단기 (컨텍스트 윈도우):**
- SOUL.md (600 tokens) — 이든의 정체성
- 어제 캐시 파일 (500 tokens) — 중복 확인용

**장기 (파일):**
- read: yesterday-news.json (어제 발송 내역)
- write: today-news.json (오늘 발송 내역)
- 기존 뉴스 더 이상 로드 안 함 (메모리 절감)

**절차적:**
- SKILL: news/summarization.md (요약 스타일 가이드)
- SKILL: news/credibility-check.md (신뢰도 판단 기준)

## Output Format

**채널:** Telegram
**형식:** Markdown
**길이:** 최대 500자
**언어:** 한국어 (영어 고유명사는 원문 유지)
**톤:** 간결하고 실용적, 개인적 인사이트는 "💡" 이모지로 구분

**예시:**
```
📰 오늘의 AI 뉴스 (2026-03-07)

1️⃣ Claude Opus 4.6 공식 출시
Anthropic이 새로운 프롬프트 캐싱 기능 공개. PM 관점에서 컨텍스트 윈도우 비용 최대 50% 절감 가능.
💡 기존 에이전트 비용 재계산 필요

2️⃣ [제목] ... (3줄 요약)
```

## Failure Handling

| 실패 시나리오 | 감지 방법 | 행동 |
|----------|----------|------|
| 뉴스 검색 결과 0건 | web_search 반환값 empty | 어제 상위 3건 재발송 + "신규 뉴스 없음" 명시 |
| API 타임아웃 | timeout exception | 3회 재시도 → 실패 시 "검색 실패" 알림만 발송 |
| 중복 감지 후 새 뉴스 5건 미만 | filtered_results.length < 5 | 보유한 뉴스 N건이라도 발송 (결국 하지 않음) → "오늘 신규 뉴스 N건" 명시 |
| 뉴스 요약 품질 낮음 (판단 불가) | 자동 감지 불가능 | 사용자 피드백 기반 요약 스타일 SKILL.md 수정 |

---

OK. 이 Instruction 세트로 구현 가능.
```

### Bad Example

```markdown
# Instruction — agent-x

역할: 뉴스를 요약합니다.

목표: 좋은 요약을 만듭니다.

도구: web_search, write_file

메모리: 파일들을 로드합니다.

출력: 결과를 보냅니다.

실패: 에러가 발생하면 알립니다.

---

문제점:
- Role이 추상적 ("뉴스를 요약"만 있고, 누구를 위해/왜 필요한지 불명확)
- Anti-Goals 없음 → 하지 말아야 할 것이 명시 안 됨
- Tools의 사용 조건 없음 → 도구 과다 호출 가능
- Memory 구체적이지 않음 → 어떤 파일을 로드할지 불명확
- Output Format이 채널/형식/길이 미명시
- Failure Handling이 "에러 → 알림" 수준으로만 작성 → 구체적 행동 없음
```

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

## Project Context (auto-injected)

> 아래 섹션은 스킬 실행 시 자동으로 현재 프로젝트 데이터로 치환됩니다.
> 도구가 설치되지 않은 경우 graceful하게 건너뜁니다.

**프로젝트 메모리:**
!`cat .claude/MEMORY.md 2>/dev/null || echo "프로젝트 메모리 없음 — .claude/MEMORY.md를 생성하면 자동 참조됩니다."`

**기존 에이전트 인스트럭션:**
!`ls -1 agents/*/INSTRUCTION.md 2>/dev/null || ls -1 instructions/*.md 2>/dev/null || echo "기존 인스트럭션 파일 없음 — agents/ 또는 instructions/ 디렉토리에 기존 설계가 있으면 자동 참조됩니다."`

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

---

## Further Reading
- Anthropic, "Building Effective Agents" (2024) — System prompt design
- OpenAI, "Prompt Engineering Guide" — Instruction optimization
