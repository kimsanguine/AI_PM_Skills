---
name: growth-loop
description: "Design data flywheels and growth loops for AI agent products — model how agent usage generates data, data improves agent quality, and quality drives more usage. Use when designing agent retention mechanics, planning data moat strategies, or building compound growth into agent architecture."
argument-hint: "[agent to design growth loop for]"
allowed-tools: ["Read", "Write", "WebSearch", "WebFetch"]
model: sonnet
---

# Agent Growth Loop

> 에이전트 데이터 플라이휠 설계 — 사용이 데이터를 만들고, 데이터가 에이전트를 개선하고, 개선이 더 많은 사용을 만든다

## Core Goal

- 에이전트 사용 데이터가 자동으로 모델 또는 프롬프트를 개선하는 루프를 설계하여 시간이 지날수록 제품 품질이 자동 향상되는 구조 구축
- 데이터 수집, 처리, 개선의 각 단계에서 속도와 비용의 균형을 맞춰 실행 가능한 플라이휠 설계
- 플라이휠이 시작되지 않거나 중단되는 역루프(anti-loop)를 사전에 식별하고 해결 전략 수립

## Trigger Gate

### Use This Skill When

- 에이전트 제품의 데이터 모아 방식을 설계하는 경우
- 사용 데이터를 어떻게 에이전트 개선으로 전환할지 체계화하는 경우
- 장기 경쟁력(해자) 구축을 위해 데이터 축적 전략이 필요한 상황

### Route to Other Skills When

- 플라이휠을 통한 경쟁 우위의 강도 평가 → moat (해자 분석)
- 사용자가 유입되지 않아 데이터 수집이 안 되는 상황 → 먼저 growth-loop로 cold start 해결
- 비용 구조상 데이터 처리가 불가능할 수 있으면 → biz-model (단위 경제)부터 검토
- 멀티 에이전트 시스템에서 TK 공유 루프 설계 → orchestration 또는 memory-arch

### Boundary Checks

- 아직 사용자가 없는 상태에서 플라이휠 설계 → 가상 고객 또는 seed data로 시작
- 데이터 개선 주기가 너무 길면 (예: 월 단위) → cold start 기간이 길어져 초기 이탈 위험
- 플라이휠 강도(Loop Strength) <15점이면 → 실제 방어 가능한 해자가 아닐 수 있음

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

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|---------|-----|-----|
| Cold Start 문제: 초기 사용자가 충분하지 않아 데이터 수집 불가 | 처음 3개월 사용량 <100건 | Seed data 주입 (수동), Transfer learning 활용 (유사 도메인), 또는 TK 전문가 개입으로 초기 품질 확보 |
| Anti-Loop 발생: 데이터 수집 후 개선이 안 됨 | 추적 지표 상 3개월 동안 품질 개선 없음 | 데이터 처리 파이프라인 재검토, 개선 방법 변경 (프롬프트 → 파인튜닝), 또는 필요 데이터 유형 재정의 |
| Privacy 장벽: 고객이 데이터 수집 거부 | 고객 계약에 데이터 수집 명시 필요 | 명시적 동의 UI 추가, 익명화 정책 강화, 또는 고객 갭 수용하고 다른 루프로 보상 |
| 플라이휠 주기가 너무 김 | 데이터 → 개선까지 >4주 소요 | 배치 프로세싱 속도 개선, 자동화된 평가 지표 도입, 또는 사용자에게 개선 피드백 보여주는 속도 단축 |

## Quality Gate

- [ ] 루프 유형 명확화: Type A/B/C/D 중 선택 및 선택 근거 문서화 (Yes/No)
- [ ] Loop Strength 계산: 5개 요소별 점수 매기고 총점 기록 (총점 ___ / 25)
- [ ] Cold Start 전략 정의: Seed data, Manual override, Transfer learning 중 최소 1개 선택 (Yes/No)
- [ ] Anti-Loop 체크리스트: 5가지 역루프 위험 식별 및 완화 방안 문서화 (Yes/No)
- [ ] Flywheel Mechanics 설계: Input → Processing → Output → Feedback 각 단계 명시 (Yes/No)

## Examples

### Good Example

```
에이전트: "고객 상담 FAQ 자동화"

[루프 유형] Type A — Data Quality Loop

[데이터 수집]
- 각 상담 완료 후 사용자가 "이 답변이 도움됐나?" 피드백 (explicit)
- 답변 길이, 검색 시간, 후속 질문 데이터 (implicit)
- 월 1,000개 상담에서 약 5,000개 피드백 데이터 포인트

[개선 변환]
- 주 1회: 피드백 집계
- 정확도 <80% 질문 식별
- 해당 Q&A 프롬프트 최적화
- 또는 전문가가 새로운 예제 추가 (TK 주입)

[품질 측정]
- "도움됨" 비율: 주 추적
- 평균 답변 길이: 월 추적
- 첫 번째 답변 만족도: 목표 >85%

[피드백 루프 완성]
- 개선된 답변을 다음 주 상담에 적용
- 사용자가 "이전보다 낫다"고 느낌 → 더 많은 피드백 제공
- 6개월 후: Loop Strength 20/25 (강한 플라이휠)

[Cold Start 전략]
- 초기 3주: 전문 상담사가 FAQ 100개 미리 작성 (seed data)
- 1개월 후: 사용자 피드백 시작
- 3개월 후: 자동화된 개선 루프 시작
```

### Bad Example

```
반사례 1: 데이터 수집 없는 "플라이휠"
- 상담 챗봇 출시, 사용자가 사용하지만 피드백 수집 안 함
- 에이전트가 시간이 지나도 개선 안 됨
- 6개월 후: "역시 챗봇은 못하네" → 포기

반사례 2: 개선 주기가 너무 김
- 월 1회만 프롬프트 업데이트
- 사용자는 개선을 못 느낌
- 피드백 제공 동기 없음 → anti-loop 시작

반사례 3: Privacy 장벽 미해결
- 고객이 "데이터 수집 거부"
- Seed data만으로 시작하지만 개선 안 됨
- "데이터가 없으니 개선 못한다" → 루프 불가능

반사례 4: 잘못된 루프 유형 선택
- Type B (Content Loop) 에이전트인데
- Type A (Data Quality) 루프로 설계
- 콘텐츠 생성이 아니라 데이터 개선에만 초점
- 실제 성장 목표와 맞지 않음
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
