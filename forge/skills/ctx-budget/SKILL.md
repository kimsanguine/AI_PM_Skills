---
name: ctx-budget
description: "Plan and optimize the context window usage for an agent. Define file loading priority, estimate token consumption per component, and design a strategy to stay within budget. Use when designing agents that load multiple files, or when diagnosing high token costs or context overflow errors."
argument-hint: "[agent to budget tokens for]"
allowed-tools: ["Read", "Write"]
model: sonnet
---

## Context Window Budget

## Core Goal

- 에이전트가 로드할 모든 파일/데이터의 토큰 소비를 사전에 추정하고 모델의 실용적 한도 내에서 최적 조합 도출
- 필수/조건부/제외 분류를 통해 불필요한 파일 로딩으로 인한 비용 낭비와 응답 품질 저하 방지
- 동적 로딩 전략(memory_search 활용)으로 변수 상황에 대응 가능한 컨텍스트 관리 계획 수립

---

## Trigger Gate

### Use This Skill When

- 새로운 에이전트가 여러 파일(메모리, SKILL.md, 도메인 문서)을 로드할 때
- 컨텍스트 윈도우 사용률이 70% 이상일 때 또는 토큰 예산 재검토가 필요할 때
- 컨텍스트 오버플로우 에러 발생 또는 응답 품질 저하 징후가 보일 때
- 에이전트 규모 확대 시 추가 파일 로딩으로 인한 예산 영향도 분석이 필요할 때

### Route to Other Skills When

- 프롬프트 최적화 필요 → `forge/prompt` 스킬로 라우팅 (프롬프트 토큰 절감)
- 아키텍처 전체 검증 필요 → `agent-plan-review` 스킬로 라우팅 (컨텍스트는 아키텍처 설계의 일부)
- 모델 선택 최적화 필요 → `atlas/router` 스킬로 라우팅 (토큰 한도가 다른 모델 비교)
- 메모리 아키텍처 재설계 필요 → `atlas/memory-arch` 스킬로 라우팅 (단기/장기/절차적 메모리 계층)

### Boundary Checks

- 컨텍스트 윈도우는 **에이전트 한 세션**의 입출력만 관리 — 장기 저장소(데이터베이스) 설계는 memory-architecture 스킬 범위
- 토큰 추정은 **모델별로 다름** — Haiku/Sonnet/Opus 기준을 명시하고, 실제 값은 token-counting API로 검증
- 70% / 85% 임계값은 경험 기반 가이드이지 절대값 아님 — 각 조직의 레이턴시 요구사항에 따라 조정 필요

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|----------|------|------|
| 예산 추정 후 실제 로드 토큰이 예측치보다 50% 이상 초과 | 로그에서 실제 컨텍스트 윈도우 사용률 확인 | 예측 모델 재검증 (파일 크기 재측정, 모델별 토큰 환산율 확인), 다음 사이클에 버퍼 추가 |
| 동적 로딩 전략 설계 후 실제로 memory_search 도구가 없거나 작동 불가 | 에이전트 구현 단계에서 memory_search 도구 미지원 발견 | 정적 로딩으로 fallback하거나, 대체 검색 방식(키워드 기반 필터링) 구현 |
| 조건부 로드 설정 후 실제 시점에 조건을 판단하기 어려움 (예: "관련성 높은 섹션"의 정의가 모호함) | 구현 중 에이전트가 조건 판단 오류로 인한 로드 실패 발생 | 조건을 더 구체적인 규칙으로 재정의 (예: "키워드 포함 여부" → "검색 점수 > 0.7") |
| 70%~85% 구간에서 여러 파일을 추가해야 하는데 예산 초과 불가피한 상황 | 새 파일 추가 시 임계값 초과 확실 | "작업 여유분" 또는 "대화 히스토리" 항목 축소를 먼저 시도, 불가능하면 아키텍처 재검토 (agent-plan-review 연계) |

---

## Quality Gate

- [ ] 로드 파일 목록 완성 (에이전트가 사용할 모든 파일 명시) (Yes/No)
- [ ] 각 파일별 토큰 추정값 계산 (용량 기반 또는 샘플 측정) (Yes/No)
- [ ] 필수/조건부/제외 분류 완료 (예산 내 최적 조합 도출) (Yes/No)
- [ ] 동적 로딩 전략 설계 (memory_search 조건 또는 대체 방식 명시) (Yes/No)
- [ ] 70%/85% 임계값별 모니터링 계획 수립 (Yes/No)
- [ ] 최적화 제안 (현재 대비 절감 가능한 토큰 수와 방법) (Yes/No)

---

## Examples

### Good Example

```markdown
# Context Window Budget — pm-briefing 에이전트

## Step 1: 로드 파일 목록

필수 항목:
- SOUL.md (~600 tokens)
- USER.md (~900 tokens)
- 오늘 메모리 파일 (~1500 tokens)
- 어제 메모리 파일 (~1500 tokens)

조건부 항목:
- MEMORY.md (기본 미로드, 키워드 매칭 시만) (~3000 tokens)
- PM-ENGINE-MEMORY.md (특정 도메인 요청 시만) (~6000 tokens)
- 관련 SKILL.md × 2 (현재 작업 타입별) (~2400 tokens)

## Step 2: 토큰 추정

```
총 80,000 tokens (Sonnet 기준, 실용 한도)

필수 항목: 4,500 (5.6%)
조건부(기본): 2,400 (3.0%) — SKILL.md만 로드
조건부(확장): 9,000 (11.2%) — MEMORY.md + PM-ENGINE 추가

시스템 프롬프트: 3,000 (3.8%)
대화 히스토리: 10,000 (12.5%)
작업 입력 데이터: 15,000 (18.8%)
작업 여유분: 41,600 (52%) ← 출력 + 추론용
```

## Step 3: 필수/조건부/제외 분류

**필수 로드 (항상):**
- SOUL.md, USER.md, 오늘+어제 메모리
- 합계: 4,500 tokens → 예산의 5.6%

**조건부 로드 (if 키워드 매칭):**
- 기본: 활성 SKILL.md × 2개 (~2,400)
- 확장: MEMORY.md (마케팅/재무/에이전트 키워드) → 추가 ~3,000
- 추가: PM-ENGINE-MEMORY.md (OKR/전략 키워드) → 추가 ~6,000

**제외:**
- 2일 이전 메모리 파일 (→ MEMORY.md 요약본으로 통합)
- 무관한 도메인 SKILL.md
- 원문 뉴스 기사 전체 (→ 요약본 3줄만 로드)

## Step 4: 동적 로딩 전략

memory_search("오늘 작업 키워드") → 관련성 상위 N개만 로드

조건 정의:
```python
if "전략" or "OKR" in 입력:
  로드 PM-ENGINE-MEMORY.md
if "비용" or "예산" in 입력:
  로드 MEMORY.md (재무 섹션)
if 컨텍스트 > 70%:
  대화 히스토리 압축 (최근 5개만 유지)
if 컨텍스트 > 85%:
  조건부 항목 제외 (필수만 유지)
```

## Step 5: 최적화 제안

**현재:** 80,000 tokens 기준
**절감 기회:**
1. 요약본 우선 (원문 → 3줄) = 약 2,000 tokens 절감
2. 2일 이전 메모리 제외 = 약 1,500 tokens 절감
3. SKILL.md 청크 분할 (전체 대신 관련 섹션만) = 약 800 tokens 절감
**합계: 약 4,300 tokens (5.4%) 절감 가능**

## Step 6: 모니터링 계획

```
🟢 70% 미만 (56k 이하): 정상 운영
  → 조건부 항목 자유롭게 로드

⚠️ 70~85% (56k~68k): 경고 구간
  → 새 파일 로드 최소화
  → 매 Turn 마다 상태 확인

🔴 85% 이상 (68k~): 위험 구간
  → 조건부 항목 모두 제외
  → 필수 항목만 유지
  → 상태 파일 저장 (다음 세션용)
```
```

### Bad Example

```markdown
# Context Budget — agent-x

## 파일들

SOUL.md
MEMORY.md
USER.md
PM-ENGINE-MEMORY.md
SKILL.md 여러 개

다 로드합니다.

## 결과

모든 파일을 로드하면 충분합니다.

---

문제점:
- 토큰 추정 없음 → 예산 규모를 모름
- 필수/조건부 분류 없음 → 모든 파일을 항상 로드
- 동적 로딩 전략 없음 → 환경에 따른 대응 불가
- 70%/85% 임계값 언급 없음 → 모니터링 계획 없음
- 최적화 제안 없음 → 낭비 요소 발견 불가
```

---

## Context Window Budget

컨텍스트 윈도우는 에이전트의 단기 기억입니다.  
그리고 모든 토큰은 비용입니다.

두 가지 실수:
1. **과소 로드**: 필요한 정보가 없어서 판단 오류
2. **과다 로드**: 불필요한 파일로 컨텍스트 오염 + 비용 낭비

컨텍스트 윈도우 예산 계획은 에이전트 설계의 **숨겨진 핵심**입니다.

---

### 컨텍스트 용량 기준 (Claude 기준)

| 모델 | 최대 컨텍스트 | 실용적 한도 |
|---|---|---|
| Haiku | 200k tokens | 40k (비용 효율) |
| Sonnet | 200k tokens | 80k (균형) |
| Opus | 200k tokens | 100k (품질 우선) |

> 실용적 한도: 성능 저하 없이 안정적으로 사용 가능한 범위  
> 150k 이상에서 응답 품질 저하 및 비용 급증 보고 사례 있음

---

### 토큰 소비 추정 기준

```
일반 텍스트:    ~750 단어 = 1,000 tokens
마크다운 파일:  1KB ≈ 250~350 tokens
코드:           1KB ≈ 200~300 tokens
JSON:           1KB ≈ 150~250 tokens
이미지:         해상도 의존 (Claude: low/high detail)
```

**주요 파일 토큰 추정 예시:**

| 파일 | 크기 | 예상 토큰 |
|---|---|---|
| SOUL.md | ~2KB | ~600 |
| USER.md | ~3KB | ~900 |
| MEMORY.md | ~10KB | ~3,000 |
| PM-ENGINE-MEMORY.md | ~20KB | ~6,000 |
| 일별 메모리 파일 | ~5KB | ~1,500 |
| SKILL.md (평균) | ~4KB | ~1,200 |

---

### 컨텍스트 예산 계획 4단계

**Step 1 — 필수 항목 분류**

```
필수 (항상 로드):
- SOUL.md, USER.md (에이전트 정체성 + 사용자 프로필)
- 오늘/어제 메모리 파일
- 현재 작업 관련 핵심 파일

조건부 (필요시 로드):
- MEMORY.md (장기 기억)
- 도메인 메모리 파일
- 관련 SKILL.md

제외 (로드 안 함):
- 오래된 메모리 파일 (2일 이전)
- 무관한 도메인 파일
- 원문 데이터 전체 (→ 요약본 사용)
```

**Step 2 — 예산 배분**

```
총 예산: 80,000 tokens (Sonnet 기준)

항목별 배분:
├── 시스템 프롬프트/Instruction: 3,000 (4%)
├── 필수 메모리 파일: 10,000 (13%)
├── 작업 입력 데이터: 20,000 (25%)
├── SKILL.md (활성): 5,000 (6%)
├── 대화 히스토리: 10,000 (13%)
└── 작업 여유분: 32,000 (40%) ← 출력 + 추론
```

**Step 3 — 동적 로딩 전략**

전체를 미리 로드하는 대신 필요할 때 꺼내는 방식:

```python
# 정적 로드 (비효율)
load([MEMORY.md, PM-ENGINE-MEMORY.md, AI-BUSINESS-MEMORY.md, ...])

# 동적 로드 (효율적)
relevant = memory_search("오늘 작업 관련 키워드")
load(relevant[:3])  # 상위 3개만 로드
```

memory retrieval tool이 이 역할을 수행:
- 키워드 기반 의미론적 검색
- 관련성 높은 섹션만 반환
- 불필요한 전체 파일 로딩 방지

**Step 4 — 임계값 모니터링**

```
70% 미만:  🟢 정상 운영
70~85%:   ⚠️ 경고 — 새 파일 로딩 최소화, 중요 내용 저장
85% 이상:  🔴 위험 — 컴팩션 임박, 즉시 상태 파일 저장
```

---

### 컨텍스트 최적화 패턴

**Pattern 1 — 요약본 우선**
```
❌ 원문 뉴스 기사 10개 전체 로드 (10,000 tokens)
✅ 각 기사 요약 3줄 × 10개 (1,000 tokens)
```

**Pattern 2 — 청크 분할 처리**
```
큰 파일 → 섹션별 분할 → 관련 섹션만 로드
예: PM-ENGINE-MEMORY.md → TK-001~010만 로드 (전체 대신)
```

**Pattern 3 — 절차적 지식 외부화**
```
반복 판단 로직 → SKILL.md로 분리
→ 컨텍스트에 로직 전체 대신 스킬 이름만 참조
```

**Pattern 4 — 출력 후 정리**
```
중간 결과를 파일에 저장 → 컨텍스트에서 제거
→ 다음 단계는 파일을 참조
```

---

### 사용 방법

`/context-window-budget [에이전트 이름 또는 워크플로우]`

---

### Instructions

You are helping plan the context window budget for: **$ARGUMENTS**

**Step 1** — 로드 파일 목록 작성  
이 에이전트가 로드할 모든 파일/데이터 나열

**Step 2** — 토큰 추정  
각 항목의 예상 토큰 수 계산  
총합 vs 모델 한도 비교

**Step 3** — 필수 / 조건부 / 제외 분류  
우선순위별 분류 후 예산 내 최적 조합 도출

**Step 4** — 동적 로딩 전략 설계  
memory_search 활용 방법 + 로딩 조건 정의

**Step 5** — 최적화 제안  
현재 설계에서 절감 가능한 토큰 수와 방법

**Step 6** — 모니터링 계획  
70%/85% 임계값 알림 설정 방법

---

### 참고
- 임계값 기준: agent heartbeat monitoring 컨텍스트 모니터링 운영 경험 (AI PM Skills Contributors, 2026-03)
- 동적 로딩: memory retrieval tool 실사용 기반
- Tool Search 절감: GPT-5.4 47% 토큰 절감 사례 (OpenAI, 2026-03)

---

## Further Reading
- Anthropic, "Long Context Window Tips" — Context window management
- Token counting tools — https://docs.anthropic.com/en/docs/build-with-claude/token-counting

## Contextual Knowledge (auto-loaded)

> 보조 파일이 존재할 때만 자동 로드됩니다. 파일이 없으면 건너뜁니다.

### Test Cases
!`cat references/test-cases.md 2>/dev/null || echo ""`

### Troubleshooting
!`cat references/troubleshooting.md 2>/dev/null || echo ""`

### Good Example
!`cat examples/good-01.md 2>/dev/null || echo ""`

### Bad Example
!`cat examples/bad-01.md 2>/dev/null || echo ""`

### Domain Context
!`cat context/domain.md 2>/dev/null || echo ""`
