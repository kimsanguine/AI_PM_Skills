---
name: token-cost-tracking
description: "Track, analyze, and optimize token costs for AI agents. Covers cost calculation formulas, optimization patterns, and budget alerts. Use when managing multiple agents, experiencing unexpected cost spikes, or designing a cost-efficient multi-agent architecture."
---

## Token Cost Tracking

에이전트 비용은 조용히 쌓입니다.  
크론잡 1개가 하루 $0.10이면 연간 $36.5 — 22개면 $803.

비용 추적 없이 에이전트를 운영하면:
- 어떤 에이전트가 비용을 가장 많이 쓰는지 모름
- 비용 최적화 기회를 놓침
- 예상치 못한 비용 폭증 발생

---

### 비용 계산 공식

**기본 공식:**
```
Cost per Run = (Input Tokens × Input Price) + (Output Tokens × Output Price)
Monthly Cost = Cost per Run × Runs per Day × 30
```

**Anthropic 모델 단가 (2026년 기준, 1M tokens당):**
| 모델 | Input | Output | Cache Read |
|---|---|---|---|
| Haiku | $0.25 | $1.25 | $0.03 |
| Sonnet | $3.00 | $15.00 | $0.30 |
| Opus | $15.00 | $75.00 | $1.50 |

**캐시 절감 효과:**
```
캐시 히트율이 높은 에이전트:
→ 동일 시스템 프롬프트를 반복 사용
→ 캐시 읽기 단가 = 일반 읽기의 10~12%
→ 시스템 프롬프트가 큰 에이전트일수록 절감 효과 큼
```

---

### 에이전트별 비용 계층

**Tier 1 — 저비용 ($0~$1/월)**
```
조건: Haiku + 짧은 컨텍스트 + 1회/일 이하
예시:
- 단순 브리핑 (Haiku, 2k tokens/회, 1회/일)
  = $0.25/1M × 2k × 30 = $0.015/월
- 이메일 필터링 (Haiku, 3k tokens/회, 2회/일)
  = $0.25/1M × 3k × 60 = $0.045/월
```

**Tier 2 — 중간 ($1~$10/월)**
```
조건: Sonnet + 중간 컨텍스트 + 1~2회/일
예시:
- AI 뉴스 브리핑 (Sonnet, 8k tokens/회, 1회/일)
  = $3/1M × 8k × 30 = $0.72/월
- 에이전트 목표 어드바이저 (Sonnet × 3, 5k tokens/회, 1회/일)
  = $3/1M × 5k × 3 × 30 = $1.35/월
```

**Tier 3 — 고비용 ($10+/월)**
```
조건: Opus 또는 높은 빈도 Sonnet
예시:
- 실시간 대화 에이전트 (Sonnet, 10k tokens/회, 10회/일)
  = $3/1M × 10k × 300 = $9/월
→ 비용 정당화 필요: ROI 계산 필수
```

---

### 비용 최적화 전략

**전략 1 — 모델 다운그레이드**
```
Before: 전체 Sonnet → After: Haiku로 교체 가능한 Worker
절감율: 최대 92% (Sonnet → Haiku 단가 차이)

판단 기준:
- 단순 분류/변환/포맷팅 → Haiku 교체 가능
- 복잡한 추론/분석 → Sonnet 유지
```

**전략 2 — 컨텍스트 최소화**
```
Before: MEMORY.md 전체 로드 (10k tokens)
After:  memory_search → 관련 섹션만 (2k tokens)
절감율: ~80%

적용 방법: (context-window-budget 스킬 참고)
```

**전략 3 — 배치 처리**
```
Before: 항목 10개 × 개별 API 호출 = 10회 호출
After:  항목 10개 배치 → 1회 호출
절감율: ~70% (오버헤드 제거)
```

**전략 4 — 캐시 활용**
```
시스템 프롬프트를 일정하게 유지
→ 캐시 히트율 증가
→ 캐시 읽기 단가 = 일반의 10%
→ 긴 Instruction 에이전트일수록 효과 큼
```

**전략 5 — 검색 횟수 제한**
```
Before: web_search 무제한 → 16분 실행 (타임아웃)
After:  프롬프트에 "web_search 최대 5회" 명시 → 2분
절감: 실행 시간 87% 단축 + 토큰도 절감
```

---

### 비용 모니터링 대시보드

```
[월별 에이전트 비용 추적]

에이전트          모델    일 실행  예상 월비용  실제 월비용
─────────────────────────────────────────────────────
morning-briefing  Haiku   1회     $0.02       $??
ai-news-briefing  Sonnet  1회     $0.72       $??
agent-goal-advisor Sonnet 1회     $1.35       $??
gmail-top5-morning Haiku  1회     $0.05       $??
...
─────────────────────────────────────────────────────
합계                                $X.XX      $XX.XX

⚠️ 예산 알림: 월 $50 초과 시 Telegram 알림
```

---

### 사용 방법

`/token-cost-tracking [에이전트 또는 전체 시스템]`

---

### Instructions

You are helping track and optimize token costs for: **$ARGUMENTS**

**Step 1** — 에이전트별 비용 계산  
모델 / 평균 토큰 수 / 일 실행 횟수 → 월 비용

**Step 2** — 비용 계층 분류  
Tier 1/2/3로 분류, Tier 3 에이전트는 ROI 검토

**Step 3** — 최적화 기회 발굴  
5가지 전략 중 적용 가능한 것 선별

**Step 4** — 절감 시뮬레이션  
최적화 전 vs 후 비용 비교

**Step 5** — 모니터링 계획  
월 예산 상한 설정 + 알림 임계값

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- 전략 5 (검색 횟수 제한): MEMORY.md system_pattern 기반 실증 (965s → 108s)
- 캐시 히트 패턴: OpenClaw 하트비트 상태 리포트 캐시 히트율 추적
