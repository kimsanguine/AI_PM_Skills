---
name: ctx-budget
description: "Plan and optimize the context window usage for an agent. Define file loading priority, estimate token consumption per component, and design a strategy to stay within budget. Use when designing agents that load multiple files, or when diagnosing high token costs or context overflow errors."
argument-hint: "[agent to budget tokens for]"
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

OpenClaw `memory_search` 툴이 이 역할을 수행:
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
- 임계값 기준: OpenClaw 하트비트 컨텍스트 모니터링 운영 경험 (이든, 2026-03)
- 동적 로딩: OpenClaw memory_search + memory_get 툴 실사용 기반
- Tool Search 절감: GPT-5.4 47% 토큰 절감 사례 (OpenAI, 2026-03)

---

## Further Reading
- Anthropic, "Long Context Window Tips" — Context window management
- Token counting tools — https://docs.anthropic.com/en/docs/build-with-claude/token-counting
