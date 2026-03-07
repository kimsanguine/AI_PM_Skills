---
name: growth-loop
description: "Design data flywheels and growth loops for AI agent products — model how agent usage generates data, data improves agent quality, and quality drives more usage. Use when designing agent retention mechanics, planning data moat strategies, or building compound growth into agent architecture."
argument-hint: "[agent to design growth loop for]"
---

# Agent Growth Loop

> 에이전트 데이터 플라이휠 설계 — 사용이 데이터를 만들고, 데이터가 에이전트를 개선하고, 개선이 더 많은 사용을 만든다

## 개념

일반 SaaS의 그로스 루프는 "유저가 유저를 데려온다" (바이럴). 에이전트의 그로스 루프는 "사용이 에이전트를 똑똑하게 만든다" (데이터 플라이휠). 이 차이가 에이전트 제품의 진짜 해자를 만든다.

## Instructions

You are designing a **growth loop** for: **$ARGUMENTS**

### Step 1 — Core Loop Identification

에이전트 제품의 핵심 루프 유형을 판별합니다:

```
Type A — Data Quality Loop (가장 강력)
  사용 → 피드백 데이터 축적 → 모델/프롬프트 개선 → 더 좋은 결과 → 더 많은 사용
  예: 고객 상담 에이전트가 상담할수록 FAQ 패턴이 축적되어 정확도 상승

Type B — Content Loop
  사용 → 콘텐츠 생성 → 콘텐츠가 새 유저 유입 → 더 많은 사용
  예: SEO 에이전트가 만든 콘텐츠가 검색 유입을 만듦

Type C — Network Loop
  유저 A 사용 → 유저 B에게 가치 → 유저 B 가입 → 유저 A에게 더 큰 가치
  예: 멀티에이전트 협업 — 팀원이 많을수록 오케스트레이션 가치 상승

Type D — TK Accumulation Loop (이 스킬셋 고유)
  PM 판단 경험 → TK 추출 → 에이전트 인스트럭션 개선 → 더 나은 판단 → 새로운 판단 경험
  예: PM-ENGINE-MEMORY가 쌓일수록 에이전트 판단 품질 상승
```

### Step 2 — Loop Strength Assessment

| 요소 | 질문 | 강도 (1-5) |
|------|------|-----------|
| Data Uniqueness | 이 데이터를 경쟁사가 얻을 수 있는가? | |
| Improvement Speed | 데이터 → 개선까지 얼마나 걸리는가? | |
| User Perception | 유저가 개선을 체감하는가? | |
| Switching Cost | 축적된 데이터 때문에 이탈이 어려운가? | |
| Compounding | 시간이 지날수록 격차가 벌어지는가? | |

**총점 20 이상 → 강한 플라이휠 (방어 가능한 해자)**

### Step 3 — Flywheel Mechanics Design

각 루프 구성 요소를 설계합니다:

```
[Input] ─────────────────────────────────────────┐
  에이전트 사용 데이터                              │
  └── 수집 방법: [implicit / explicit / hybrid]    │
                                                    ↓
[Processing] ──────────────────────────────────────┐
  데이터 → 개선 변환                                │
  └── 방법: [fine-tuning / RAG update / prompt      │
             optimization / TK extraction]          │
                                                    ↓
[Output] ───────────────────────────────────────────┐
  개선된 에이전트 품질                               │
  └── 측정: [accuracy / speed / relevance / cost]   │
                                                    ↓
[Feedback] → 유저가 개선을 체감 → 더 많은 사용 → [Input]
```

### Step 4 — Anti-Loop Detection

플라이휠을 멈추게 하는 역루프를 식별합니다:

- [ ] **Data Decay**: 시간이 지나면 데이터가 쓸모없어지는가? (예: 트렌드 변화)
- [ ] **Privacy Barrier**: 유저가 데이터 수집을 거부하는가?
- [ ] **Cost Escalation**: 데이터 처리 비용이 개선 가치보다 큰가?
- [ ] **Quality Ceiling**: 일정 수준 이상 개선이 안 되는가?
- [ ] **Cold Start**: 초기 데이터 부족으로 루프가 시작 안 되는가?

### Step 5 — Kickstart Strategy

플라이휠 초기 가동 전략:

```
Cold Start 해결:
  ├── Seed Data: [초기 데이터 확보 방법]
  ├── Manual Override: [사람이 채우는 부분]
  ├── Transfer Learning: [유사 도메인 데이터 활용]
  └── TK Injection: [PM 암묵지로 초기 품질 확보] ← TK-NNN 활용
```

### Output

```
Growth Loop Design: [agent name]
─────────────────────────────────
Loop Type: [A/B/C/D]
Loop Strength: [N]/25
Flywheel Mechanics:
  Input: [data source]
  Processing: [improvement method]
  Output: [quality metric]
  Feedback: [user perception trigger]
Anti-Loops: [identified risks]
Kickstart: [cold start strategy]
Time to Flywheel: [estimated weeks to self-sustaining loop]
Moat Depth at 6 months: [competitive advantage description]
```

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- Type D (TK Accumulation Loop): TK-NNN 프레임워크와 연결
- moat 스킬의 해자 분석과 상호 보완

---

## Further Reading
- Andrew Chen, *The Cold Start Problem* — Network effects and growth loops
- Casey Winters, "Growth Loops" — Reforge framework for sustainable growth mechanics
