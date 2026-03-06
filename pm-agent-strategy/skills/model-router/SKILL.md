---
name: model-router
description: "Select the optimal AI model for each agent task based on reasoning requirements, cost, and latency. Use when designing a multi-agent system, optimizing running costs, or deciding which model tier to assign to each worker. Prevents over-spending on high-cost models for simple tasks."
---

## Model Router — 작업 유형별 모델 선택 전략

에이전트 시스템의 숨겨진 비용 폭탄:
> 모든 작업에 Sonnet/Opus를 쓰면 비용이 10~50배 증가합니다.

모델 선택은 "가장 좋은 모델"이 아닙니다.  
**작업에 맞는 최소 충분 모델**이 맞는 선택입니다.

> "전략을 결정하는 에이전트에는 가장 좋은 추론이 필요하다."  
> — Ben Broca (Polsia), Claude Opus를 CEO 에이전트에만 사용하는 이유

---

### 모델 티어 분류 (Anthropic 기준)

| 티어 | 모델 | 강점 | 비용 수준 | 응답 속도 |
|---|---|---|---|---|
| **경량** | Claude Haiku | 빠른 처리, 단순 작업 | ⭐ | ⚡⚡⚡ |
| **표준** | Claude Sonnet | 복잡한 추론, 분석 | ⭐⭐⭐ | ⚡⚡ |
| **최고** | Claude Opus | 전략 판단, 최고 품질 | ⭐⭐⭐⭐⭐ | ⚡ |

> 비용 비율 (대략): Haiku : Sonnet : Opus = 1 : 15 : 75

---

### 작업 유형별 모델 라우팅 원칙

**Haiku가 적합한 작업 (비용 최소화)**
- ✅ 데이터 변환 (JSON 파싱, 형식 변환)
- ✅ 단순 분류 (카테고리 지정, 태그 부여)
- ✅ 템플릿 기반 생성 (정해진 포맷에 데이터 채우기)
- ✅ 조건 판단 (if-else 수준, 규칙 기반)
- ✅ 단순 요약 (정해진 길이로 요약)
- ✅ 번역 (표준 언어 쌍)
- ✅ 이메일 분류/필터링
- ✅ 알림/브리핑 포맷팅

**Sonnet이 적합한 작업 (추론 + 비용 균형)**
- ✅ 복합 분석 (데이터 패턴 추출, 인사이트 도출)
- ✅ 코드 생성/리뷰
- ✅ 긴 문서 요약 (맥락 이해 필요)
- ✅ 멀티스텝 리서치 결과 통합
- ✅ 전략적 제안 (중간 복잡도)
- ✅ 크로스도메인 연결 (여러 소스 통합)
- ✅ Worker-Reviewer 패턴의 Reviewer

**Opus가 적합한 작업 (최고 품질 필수)**
- ✅ 전략 의사결정 (Prometheus 레이어)
- ✅ 복잡한 추론 체인 (멀티스텝 논리)
- ✅ 최고 품질 콘텐츠 생성 (외부 공개 문서)
- ✅ 모호한 지시 해석 및 계획
- ✅ 리스크가 큰 판단 (실수 비용이 높을 때)

---

### Prometheus-Atlas 패턴에서의 모델 배분

```
[Prometheus — 계획]      → Sonnet / Opus
[Atlas — 조율]           → Sonnet (Haiku 가능)
[Worker: 리서치]         → Haiku (웹 검색 + 수집)
[Worker: 분석]           → Sonnet
[Worker: 코드 실행]      → Haiku (단순) / Sonnet (복잡)
[Consolidation — 통합]   → Sonnet
[Reviewer — 품질검토]    → Sonnet / Opus
```

실제 적용 사례 (agent-goal-advisor):
```
Prometheus     → Sonnet  (전략 목표 분석)
market-scout   → Haiku   (RSS 파싱 + 요약)
action-planner → Sonnet  (액션 설계)
Consolidation  → Sonnet  (통합 + Telegram 발송)
월 절감 효과: ~60% (vs 전체 Sonnet)
```

---

### 비용 계산 공식

```
월 비용 = Σ (모델 단가 × 평균 토큰 수 × 일 실행 횟수 × 30일)

예시:
morning-briefing (Haiku, 2k tokens, 1회/일):
  = $0.00025/1k × 2k × 1 × 30 = $0.015/월

agent-goal-advisor (Sonnet × 2 + Haiku × 1, 각 5k tokens, 1회/일):
  = ($0.003/1k × 5k × 2 × 30) + ($0.00025/1k × 5k × 1 × 30)
  = $0.90 + $0.0375 = ~$0.94/월
```

---

### 모델 업그레이드/다운그레이드 트리거

**다운그레이드 (Sonnet → Haiku) 신호:**
- 출력 품질이 충분히 좋은데 비용이 예상보다 높을 때
- 작업이 분류/변환/포맷팅 수준으로 단순화됐을 때
- 동일 프롬프트 Haiku 테스트에서 90%+ 품질 확인

**업그레이드 (Haiku → Sonnet) 신호:**
- 할루시네이션 또는 일관성 문제가 반복될 때
- 복잡한 지시를 자주 오해할 때
- 출력 품질이 downstream 에이전트에 악영향

**GPT / Gemini 혼용 시:**
- 비용 < 품질이 기준: 동일 가격대 모델 테스트
- 특정 작업 특화 모델 고려 (코드 = Codex, 비전 = 비전 특화)

---

### Tool Search 전략 (GPT-5.4 방식)

컨텍스트에 모든 도구를 로드하지 않고 **필요할 때만** 꺼내 쓰는 전략:

```
전통 방식: [36개 MCP 서버 전부 컨텍스트에 로드] → 토큰 낭비
Tool Search: [필요한 도구만 동적 로드] → 47% 토큰 절감 (GPT-5.4 사례)
```

OpenClaw Skills 방식도 동일 원리:
- 필요한 SKILL.md만 로드 → 컨텍스트 효율
- `memory_search` → 관련 스킬만 검색 → 로드

---

### 사용 방법

`/model-router [에이전트 또는 워크플로우 설명]`

---

### Instructions

You are helping select optimal models for each step of: **$ARGUMENTS**

**Step 1 — 작업 분해**
- 워크플로우의 모든 단계 나열
- 각 단계의 복잡도 분류 (단순/중간/복잡)
- 각 단계의 실패 비용 평가

**Step 2 — 모델 배정**
- 각 단계에 Haiku / Sonnet / Opus 배정
- 배정 근거 설명

**Step 3 — 비용 시뮬레이션**
- 각 단계 예상 토큰 수 추정
- 배정 모델 기준 월 비용 계산
- "전체 Sonnet" 대비 절감율 계산

**Step 4 — 최적화 제안**
- 추가로 Haiku로 교체 가능한 단계
- Haiku 교체 전 테스트 방법

**Step 5 — 다운그레이드 전략**
- 품질 모니터링 지표 설정
- 모델 전환 트리거 조건 명시

---

### 참고
- 설계자: Sanguine Kim (이든), OpenClaw 22개 크론잡 모델 최적화 경험
- Tool Search 사례: GPT-5.4 발표 (OpenAI, 2026-03-05)
- Polsia 모델 배분: Ben Broca, LinkedIn 2026-03
- 허용 모델 목록 관리: openclaw.json `agents.defaults.models` 필드
