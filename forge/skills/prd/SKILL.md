---
name: prd
description: "Write a PRD specifically for an AI agent — covering Instruction, Tools, Memory, Triggers, Output, and Failure handling. Structurally different from a standard product PRD. Use when formally documenting an agent before implementation, or standardizing agent specs across a portfolio."
argument-hint: "[agent to spec]"
allowed-tools: ["Read", "Write"]
model: sonnet
hooks:
  Stop:
    - type: command
      command: "bash scripts/validate-prd.sh . 2>/dev/null || true"
---

## Project Context (auto-injected)

> 아래 섹션은 스킬 실행 시 자동으로 현재 프로젝트 데이터로 치환됩니다.
> 도구가 설치되지 않은 경우 graceful하게 건너뜁니다.

**프로젝트 메모리:**
!`cat .claude/MEMORY.md 2>/dev/null || echo "프로젝트 메모리 없음 — .claude/MEMORY.md를 생성하면 자동 참조됩니다."`

**현재 이슈 (Linear/GitHub):**
!`linear issue list --mine --status "In Progress" --limit 5 2>/dev/null || gh issue list --limit 5 --json number,title --jq '.[] | "#\(.number) \(.title)"' 2>/dev/null || echo "이슈 트래커 연결 없음 — Linear CLI 또는 GitHub CLI 설치 시 자동 연동됩니다."`

---

## Agent PRD Template

## Core Goal

- 에이전트의 모든 설계 요소(지시사항, 도구, 메모리, 트리거, 출력, 실패 처리)를 7개 섹션으로 체계화하여 구현팀이 일관성 있게 구축할 수 있는 정식 명세서 작성
- 기술 스펙과 사업 가치를 동시에 명시하여 엔지니어링과 경영진 모두가 이해 가능한 공식 문서 제공
- 사전 정의된 실패 시나리오와 성공 지표로 배포 후 운영 기준을 명확히 함

---

## Trigger Gate

### Use This Skill When

- 프로토타입 검증이 완료되고 본격 구현에 들어가기 전에 공식 문서화 필요
- 에이전트 포트폴리오를 표준화하고 싶을 때
- 다른 팀이나 외부 엔지니어에게 구현을 위임해야 할 때
- 에이전트 배포 전 최종 리뷰 및 승인 필요

### Route to Other Skills When

- Instruction 7요소 설계 필요 → `forge/instruction` 스킬로 라우팅
- OKR 성공 지표 정의 필요 → `forge/okr` 스킬로 라우팅
- 메모리 아키텍처 상세화 필요 → `atlas/memory-arch` 스킬로 라우팅
- 신뢰성/SLO 정의 필요 → `argus/reliability` 스킬로 라우팅

### Boundary Checks

- PRD는 "무엇을 하는가"를 명시하지만, "어떻게 기술적으로 구현하는가"는 별도 구현 문서 범위
- 각 섹션은 "구현팀이 이것만으로도 구현 가능한가?"의 기준으로 검증
- 실패 시나리오 테이블은 최소 4개 이상의 현실적 상황 포함

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|----------|------|------|
| PRD 작성 중 Instruction과 출력 포맷이 충돌 (예: 출력은 간결인데 instruction은 상세) | Section 2와 6을 읽어보니 일관성 없음 | 어느 것이 정답인지 재결정하고, 양쪽 모두 업데이트 |
| Tools & Integrations 섹션에서 도구 목록만 있고 호출 제한이 없음 | Section 3을 리뷰했을 때 "사용 조건" 컬럼이 비어있거나 모호함 | forge/instruction 스킬로 라우팅하여 도구별 상세 조건 정의 |
| Failure Handling 테이블이 추상적 (예: "데이터 오류 발생 시 처리") | 실제로 어떤 데이터 오류인지, 어떻게 대응하는지 구체적이지 않음 | 각 시나리오를 구체적 에러 상황으로 재정의 (예: "API 응답 없음 → 3회 재시도 → 실패 시 Fallback 값 반환") |
| Success Metrics가 측정 불가능 (예: "정확도 높음") | 수치, 측정 방법, 기한이 없음 | OKR 스킬과 연계하여 "정확도 95% 이상 by 2026-06-30" 형태로 재정의 |
| MVP PRD vs Full PRD 선택 기준이 모호 | 어떤 에이전트는 1page, 어떤 건 7page인지 일관성 없음 | 프로토타입 단계 = MVP, 본격 구현 = Full로 명시적 기준 제시 |

---

## Quality Gate

- [ ] Section 1 완료: 에이전트 이름, 버전, 상태, 한 줄 정의 (Yes/No)
- [ ] Section 2 완료: Role/Primary Goal/Secondary Goals/Anti-Goals (Yes/No)
- [ ] Section 3 완료: Tools 목록 + 사용 조건 + 호출 제한 (Yes/No)
- [ ] Section 4 완료: 3계층 메모리 (Working/Long-term/Procedural) 계획 (Yes/No)
- [ ] Section 5 완료: 트리거 유형 + 실행 흐름 Step-by-Step (Yes/No)
- [ ] Section 6 완료: 채널/형식/길이/언어/톤 + 출력 샘플 (Yes/No)
- [ ] Section 7 완료: 실패 시나리오 테이블 (4개 이상) + 성공 지표 (Yes/No)
- [ ] 전체 일관성 검증: 섹션 간 충돌/누락 없음 (Yes/No)

---

## Examples

### Good Example

```markdown
# Agent PRD — cost-analyst

## Section 1 — Overview

에이전트 이름: cost-analyst
버전: 1.0
작성일: 2026-03-07
작성자: PM (담당자)
상태: Ready for Implementation

한 줄 정의:
cost-analyst는 production agent workspace 시스템의 월간 API 비용을 자동 분석하고, 절감 기회를 식별하는 에이전트다.

배경:
production agent workspace 운영 중 Gemini/Claude API 비용이 예측 불가능하게 증가. 월별 비용 분석을 자동화하고, 상위 10% 비용 소비처를 식별해 최적화 전략을 제시할 필요.

---

## Section 2 — Instruction Design

Role:
cost-analyst는 데이터 분석 PM으로서, Google Cloud Billing과 Anthropic API 청구 데이터를 수집하고,
PM 담당자에게 실행 가능한 비용 절감 권고를 제시한다.

Primary Goal:
월간 API 비용의 상위 10개 비용 소비처(에이전트/도구별)를 식별하고, 각각의 절감 기회를 수치화하여 보고.

Secondary Goals:
1. 전월 대비 비용 증감 추이 시각화
2. 비용 이상 탐지 (예: 예상치의 200% 이상)
3. 절감 우선순위별 권고 (ROI 높은 것부터)

Anti-Goals:
1. 추측 기반 권고 금지 — 모든 수치는 실제 청구 데이터 기반
2. 비용 절감을 위해 기능 제거 권고 금지 — 최적화만 제시
3. 일관되지 않은 계산 방식 — 매달 동일한 로직으로 분석

---

## Section 3 — Tools & Integrations

| 도구 | 용도 | 사용 조건 | 호출 제한 |
|------|------|----------|---------|
| Google Cloud Billing API | 월간 GCP 비용 조회 | 매월 1회 | 1회/실행 |
| Anthropic API | 월간 Claude 사용량 조회 | 매월 1회 | 1회/실행 |
| read_file | production agent workspace 실행 로그 읽기 | 에이전트 사용 기록 분석 시 | 제한 없음 |
| write_file | 분석 결과 저장 | 월말 분석 완료 후 | 1회/실행 |
| message (Telegram) | 최종 리포트 전송 | 분석 완료 후 무조건 | 1회/실행 |

최소 권한 원칙: 읽기 전용 (비용 데이터 열람만, 과금 정책 변경 불가)

---

## Section 4 — Memory Strategy

Working Memory (컨텍스트):
- 항상 로드: 지난 3개월 비용 요약 (CSV) (~2KB = 600 tokens)
- 조건부 로드: 이상 탐지 규칙 SKILL.md (비용 200% 이상 증가 시만) (~1KB = 300 tokens)
- 컨텍스트 예산: 총 10,000 tokens 중 1,000 tokens 사용 (10%)

Long-term Memory (파일):
- 읽기: monthly-cost-2026-01.json, 02.json, 03.json
- 쓰기: monthly-analysis-2026-03.md (분석 결과)
- 저장 트리거: 분석 완료 후 자동 저장

Procedural Memory (Skills):
- cost-analysis.md (비용 분석 프레임워크)
- anomaly-detection.md (이상 탐지 규칙)

---

## Section 5 — Trigger & Execution

트리거 유형:
☑ Cron — 매월 1일 오전 10:00 UTC
☐ Event-Driven
☐ Manual
☐ Pipeline

실행 흐름:
Step 1: Google Cloud Billing API 호출 → 지난 달 비용 데이터 수집
Step 2: Anthropic API 호출 → Claude 사용량 데이터 수집
Step 3: 데이터 통합 및 분석 (상위 10개 소비처 식별)
Step 4: 절감 권고 생성 (각각의 예상 절감액 계산)
Step 5: Telegram 리포트 전송

예상 실행 시간: 2분
타임아웃 설정: 5분

---

## Section 6 — Output Specification

출력 채널: Telegram
출력 형식: Markdown
출력 길이: 최대 1000자 (기본) + CSV 파일 첨부
언어: 한국어
톤: 간결하고 실용적 (수치 우선)

출력 예시:
```
📊 2026년 3월 API 비용 분석

**월간 총 비용:** $48.50 (전월 대비 +12%)

🏆 상위 5개 비용 소비처:
1. pm-briefing (Gemini 이미지) — $15.30 (32%)
   💡 제안: Flash → 배치 50% 할인 적용 시 -$7.65/월
2. cost-analyst (Claude Sonnet) — $12.80 (26%)
   💡 제안: 요약본 우선 전략으로 -$3.84/월
...

📈 전월 대비: 3월은 pm-briefing 이미지 생성이 40회 → 60회로 증가.
   특정 스타일의 이미지 요청이 많아지면서 비용 상승.

🎯 가장 효과적인 절감: Flash 배치 할인 적용 → 월 -$8 예상

---
자세한 분석은 첨부 CSV 참조.
```

---

## Section 7 — Failure Handling & Success Metrics

실패 시나리오:

| 시나리오 | 감지 방법 | 대응 행동 |
|---------|---------|---------|
| API 응답 없음 (Google Cloud Billing) | 10초 타임아웃 | 3회 재시도 (30초 간격) → 실패 시 "지난달 데이터 없음" 알림 + 진행 중단 |
| API 요금 데이터 불완전 (모든 트랜잭션 누락) | 예상 비용 대비 50% 미만 반환 | "데이터가 불완전합니다. 24시간 후 다시 시도하세요" 알림 |
| 이상 탐지 트리거 (전월 대비 200% 이상 증가) | monthly-cost 비교 | 추가 분석 SKILL 활성화 → "비용 이상 알림" 강조 + 긴급 검토 권고 |
| 계산 오류 (분석 결과 검증 실패) | 수수료 합계 ≠ 리포트 합계 | 로그 재검토 → 재분석 → 재전송 (알림: "재분석 결과") |

Human-in-the-loop 트리거:
비용 이상 감지(200% 이상) → 즉시 PM 담당자에게 알림 (긴급 검토 요청)

성공 지표:
- 정확도: API 청구 데이터 vs 리포트 비용 오차 < 1%
- 비용: 에이전트 월 운영 비용 $5 이하
- 레이턴시: 실행 시간 < 3분
- 신뢰성: 월 28회 실행 중 27회 이상 성공 (99% uptime)
```

### Bad Example

```markdown
# PRD — agent-y

에이전트: 데이터를 분석합니다.

하는 일: 데이터 처리

도구: API 여러 개

메모리: 파일을 로드합니다.

출력: 결과를 전송합니다.

실패 시: 에러 메시지를 보냅니다.

---

문제점:
- 한 줄 정의가 추상적 (누구를 위해? 왜?)
- Instruction 섹션 불완전 (Anti-Goals 없음)
- Tools 섹션이 구체적이지 않음 (도구 명시 X, 사용 조건 X)
- Memory 계획이 없음 (어떤 파일? 언제 로드?)
- Trigger가 명시되지 않음 (Cron? Event?)
- Output 예시가 없음 (어떻게 생겼는지 몰라)
- Failure Handling이 추상적 (구체적 대응 방법 없음)
```

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
- 설계자: AI PM Skills Contributors, 2026-03
- 일반 PM PRD 템플릿 기반 → 에이전트 특화 70% 재작성
- Sections 4~7: production cron job 운영 경험에서 도출

---

## Further Reading
- Marty Cagan, *INSPIRED* — Product requirements and discovery
- Shreyas Doshi — "Pre-Mortem for PRDs" framework

## Contextual Knowledge (auto-loaded)

> 보조 파일이 존재할 때만 자동 로드됩니다. 파일이 없으면 건너뜁니다.

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`

### Test Cases
!`cat references/test-cases.md 2>/dev/null || echo ""`

### Troubleshooting
!`cat references/troubleshooting.md 2>/dev/null || echo ""`
