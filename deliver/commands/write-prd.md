---
name: write-prd
description: "Write a complete unified PRD covering user/JTBD/decisions/scope/agent-spec/metrics/hypotheses in 14 sections. Single source of truth for both customer-facing products and the LLM agents inside them. Use when a product or agent idea has passed the Evidence and Product Gates and needs a full PRD before build. Chains discover/agent-gtm, discover/build-or-buy, hplan/exclusions, discover/cost-sim, deliver/instruction, measure/north-star, deliver/okr, discover/assumptions, learn/pm-engine."
argument-hint: "[product or agent name]"
---

# /write-prd

> 통합 PRD 14-section 작성 워크플로우

## Instructions

You are writing a **Unified PRD** for: **$ARGUMENTS**

### Phase 1: 사용자·문제·가치 (Section 1-3)

**Section 1 — ICP & 페르소나**
- Use the **discover/agent-gtm** skill — beachhead 5-criteria
- 페르소나 2~3개 (이름·역할·고통·도달 채널)

**Section 2 — JTBD**
- Switch Interview 4 Forces (Push·Pull·Anxiety·Habit)
- Job 1~3개

**Section 3 — 핵심 문제 + 10배 가치**
- 절실히 이해 + 해결 워크플로우 + 정량 가치 (시간/돈/새 가능성)

### 🔍 Checkpoint 1

Before proceeding, present:
1. **Summary**: ICP + 페르소나 + JTBD + 10배 가치
2. **Validation**: "이대로 5명 사랑 인터뷰에 갈 수 있는가?"
3. **Options**:
   - "Phase 2 (결정·범위)로 진행"
   - "ICP 더 좁히기 (beachhead 통과 안 됨)"
   - "JTBD 다시 작성 (솔루션 어조 발견)"

Wait for user confirmation.

### Phase 2: 결정·범위 (Section 4-6)

**Section 4 — 결정 옵션 매트릭스**
- Use **discover/build-or-buy** (6축)
- Use **architect/orchestration** (4패턴)
- Use **discover/hitl** (5레벨)
- 최소 5개 결정 항목 × 옵션 A/B/C + 트레이드오프 + 재검토 시점

**Section 5 — 제외사항 (Out-of-Scope)**
- Use **hplan/exclusions** 레지스트리 fuzzy match
- 최소 5개 — "절대 안 만드는 것" + 이유 + 재검토 신호

**Section 6 — Now/Next/Later**
- Use **discover/cost-sim** — cogs p50/p90 lognormal
- Wave 1 (Day 1~60) · Wave 2 (Day 61~120) · Wave 3 (Day 121+)

### 🔍 Checkpoint 2

Before Phase 3:
1. **Summary**: 결정 매트릭스 + 제외사항 + Now/Next/Later
2. **Validation**: "Wave 1 기능이 60일 안에 가능한가? cogs가 1인 빌더 감당 가능한가?"
3. **Options**:
   - "Phase 3 (에이전트·실행 사양)으로 진행"
   - "Wave 1 기능 축소"
   - "cogs 재산정"

### Phase 3: 에이전트·실행 사양 (Section 7-11)

**Section 7 — Role + Primary Goal + Anti-Goals**
- Use **deliver/instruction** for 7-element detail
- Anti-Goals 최소 3개 (도메인 룰·데이터 정책·법적 책임)
- 일반 SaaS면 "N/A — 일반 SaaS" 표기 가능

**Section 8 — Tools & Integrations**
- 호출 제한 mandatory

**Section 9 — Memory & Context Design**
- 3-tier (Working / Long-term / Procedural)

**Section 10 — Trigger & Execution Flow**
- Cron/Event/Manual/Pipeline 중 명시 + Step-by-Step

**Section 11 — Output Specification**
- 채널/형식/길이/언어/톤 + 실제 출력 샘플 1개

### Phase 4: 지표·가설·실패 (Section 12-14)

**Section 12 — Dual-axis OKR**
- Use **measure/north-star** + **deliver/okr**
- North Star 1 + Business KRs 3~5 + Operational KRs 3~5 (cost KR mandatory) + Anti-Metric 1

**Section 13 — 검증 가능 가설**
- Use **discover/assumptions** — Value/Feasibility/Reliability/Ethics 4축
- Top-3 + 각각 2-day experiment

**Section 14 — 실패 모드 + HITL**
- 시나리오 매트릭스 최소 4개 (감지·대응·사용자 영향)
- HITL 트리거 명시

### Phase 5: TK 인용 & Quality Gate

- Use **learn/pm-engine** to query relevant TK-NNN (3~5개)
- 각 섹션 하단에 관련 TK seed 인용
- Quality Gate 16개 항목 모두 통과 확인
- `docs/PRD.md` 저장

## Output Format

Unified PRD 14-section 자동 인용:
1. ICP / 페르소나 / 도달 채널
2. JTBD / Switch 4 Forces
3. 핵심 문제 / 10배 가치 정량
4. 결정 옵션 매트릭스
5. 제외사항 (Out-of-Scope)
6. Now/Next/Later + cogs p50/p90
7. Role + Primary Goal + Anti-Goals 3+
8. Tools & Integrations + 호출 제한
9. Memory & Context (3-tier)
10. Trigger & Execution Flow
11. Output Specification + 출력 샘플
12. Dual-axis OKR (cost KR mandatory)
13. Top-3 가설 + 2-day experiment
14. 실패 모드 4+ + HITL 트리거
+ TK-NNN 인용 3~5개
