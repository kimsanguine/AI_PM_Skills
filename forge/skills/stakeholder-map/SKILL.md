---
name: stakeholder-map
description: "Map and manage stakeholders for AI agent adoption — identify decision-makers, blockers, and champions across engineering, legal, operations, and leadership. Use when introducing an agent to an organization, navigating internal resistance, or planning change management for AI adoption."
argument-hint: "[agent initiative to map stakeholders for]"
---

# Agent Stakeholder Map

## Core Goal

- 에이전트 도입의 성공을 좌우하는 모든 이해관계자(경영진, 사용자, 엔지니어, 법무, 재무)를 미리 식별하고 맵핑하여 기술적 성공이 조직적 실패로 끝나는 것 방지
- Power-Interest Matrix로 각 이해관계자의 우선순위를 결정하고, 저항 요인별 맞춤 대응 전략 수립
- 내부 챔피언을 발굴하고 강화하여 에이전트 도입의 변화 주체를 확보

---

## Trigger Gate

### Use This Skill When

- 새로운 에이전트 도입이 조직 전체에 영향을 미칠 때 (특히 기존 업무 변화 유발)
- 에이전트 도입에 대한 내부 저항이나 반발을 예상할 때
- 여러 팀(엔지니어링, 법무, 운영, 경영진)의 합의가 필요한 경우
- 변화 관리 전략과 커뮤니케이션 계획이 필요할 때

### Route to Other Skills When

- 에이전트 설계 검증 필요 → `agent-plan-review` 스킬로 라우팅
- 신뢰성/SLO 설계 필요 → `argus/reliability` 스킬로 라우팅 (운영팀의 우려 기술적 대응)
- GTM 전략 필요 → `oracle/agent-gtm` 스킬로 라우팅 (조직 내 출시 전략)

### Boundary Checks

- 이해관계자 맵핑은 정치적 질문이 아니라 **조직 설계 질문** — 저항 요인을 개인 탓으로 돌리지 말고, 시스템 문제로 봐야 함
- Power-Interest Matrix는 가이드일 뿐, 모든 조직이 동일한 분류를 갖지는 않음 — 조직 문화/규모별로 조정 필요
- 변화 관리는 일회성이 아닌 **지속적 과정** — 도입 후 3개월은 집중 커뮤니케이션 필요

---

## Failure Handling

| 실패 상황 | 감지 | 대응 |
|----------|------|------|
| 주요 이해관계자(법무, 재무)를 처음부터 빼고 진행했다가 나중에 블로킹 | 에이전트 구축이 거의 완료된 후 법무팀에서 "AI 규제 미준수" 지적 | 법무와 재무를 즉시 engaged 상태로 전환, 관련 기술 미팅 제안, 미팅 결과에 따라 설계 수정 가능성 인정 |
| Champions를 정했지만 "의무적으로" 참여하게 되어 동기 감소 | 지정된 champion이 프로젝트에 참여는 하지만 적극성 없음 | champion의 실제 pain point를 재확인하고, 에이전트가 정말 그 pain을 해결하는지 검증 (안 하면 다른 champion 찾기) |
| Power-Interest Matrix에서 Low Power/Low Interest로 분류한 그룹이 나중에 저항 | 처음엔 무관심했던 그룹이 실제 도입 시점에 갑자기 반발 | "Monitor Only" 그룹을 주기적(월 1회)으로 업데이트하여 정보 격차 해소, 필요시 Inform 레벨로 상향 |
| 저항 유형 분석이 추상적이어서 대응 전략이 효과 없음 | 예: "신뢰 부족" 원인은 알았는데, 대응이 "더 설득하기" 수준으로만 작성 | 저항 유형별로 구체적 실행 전략 수립 (예: Trust Deficit → Shadow Mode 시작 → 3주 정확도 데이터 수집 → 공식 발표) |
| 커뮤니케이션 계획을 세웠지만 실제로는 일관되지 않음 (경영진용 자료, 사용자용 자료가 서로 다른 메시지) | 이해관계자들이 서로 다른 설명을 듣고 혼란 | 커뮤니케이션 계획 초안 후 모든 이해관계자 대표 1명씩과 사전 검토 미팅 (메시지 일관성 확인) |

---

## Quality Gate

- [ ] Stakeholder Identification 완료: 6개 그룹 이상 식별 (경영진, 사용자, 엔지니어링, 법무, 운영, 재무) (Yes/No)
- [ ] Power-Interest Matrix: 각 이해관계자를 4개 사분면 중 하나에 배치 (Yes/No)
- [ ] Resistance Analysis: 저항 유형 3개 이상 식별 + 대응 전략 각각 (Yes/No)
- [ ] Champion Strategy: 실제 champions 이름/역할 + 동기/무장/확산 경로 명시 (Yes/No)
- [ ] Communication Plan: 이해관계자별 메시지 + 포맷 + 주기 정의 (Yes/No)
- [ ] Go/No-Go Confidence: Low/Medium/High 명시 + 이유 설명 (Yes/No)

---

## Examples

### Good Example

```markdown
# Stakeholder Map — cost-analyst 에이전트 도입

## Step 1: Stakeholder Identification

| 이해관계자 | 역할 | 관심사 | 에이전트 태도 |
|-----------|------|--------|-----------------|
| **CFO (경영진)** | 최종 승인자 | ROI, 규제 준수, 예산 | 비용 절감에 긍정적 |
| **이든 (직접 사용자)** | 매월 비용 분석 담당자 | 작업 부하 감소, 의사결정 품질 향상 | 매우 긍정적 (주도자) |
| **DevOps/Engineering** | 구축, 모니터링 | 기술 부채, 운영 복잡도 | 처음엔 의심적 |
| **CFO 산하 Accounting** | 비용 데이터 제공 | 데이터 정확성, 감사 추적성 | 데이터 보안 우려 |
| **Legal/Compliance** | 규제 검토 | AI 규제, 데이터 프라이버시 | 신중함 |
| **CTO (경영진)** | 기술 승인 | 아키텍처, 운영 가능성 | 검증 데이터 필요 |

---

## Step 2: Power-Interest Matrix

```
          High Power
              │
   MANAGE    │    ENGAGE
  CLOSELY   │   ACTIVELY
  (모니터) │
─────────────┼───────────── High Interest
            │
  MONITOR   │   KEEP
    ONLY    │ INFORMED
            │
          Low Power
```

배치:

**Engage Actively (즉시 협력):**
- CFO: Power 5, Interest 5 → 전략적 제휴 (월 1회 진행률 리뷰)
- 이든: Power 4, Interest 5 → 매주 피드백 수렴

**Manage Closely (조건부 협력):**
- Engineering: Power 4, Interest 3 → 구축은 필요하지만 우선순위 낮음 → 스프린트 단위로 예정 공유
- CTO: Power 4, Interest 3 → 기술 승인 필요 → POC 결과 시연 계획

**Keep Informed (정기 업데이트):**
- Accounting: Power 2, Interest 4 → 월 1회 데이터 정확성 점검
- Legal: Power 3, Interest 2 → 분기 1회 규제 준수 확인

---

## Step 3: Resistance Analysis

| 저항 유형 | 근본 원인 | 현 상황 | 대응 전략 |
|----------|----------|--------|---------|
| **Trust Deficit** (Accounting) | "AI가 정말 정확한가?" | 과거 자동화 도구 실패 경험 | Shadow Mode 시작 → 3주 검증 → "AI 수동 결과 99% 일치" 데이터 공개 |
| **Control Loss** (Engineering) | "누가 책임지는가?" | 기술 부채 우려 | RACI 매트릭스 제시 (데이터 오류 = Accounting, API 오류 = Engineering, 분석 오류 = CFO) |
| **Risk Aversion** (Legal) | "AI 규제 문제는?" | GDPR/AI Act 미숙함 | AI 리스크 체크리스트 제시 + "읽기 전용 + 감사 로그" 기술 구현 |

---

## Step 4: Champion Strategy

**Champion: 이든 (사용자)**

프로필:
- 현재: 매월 비용 분석에 10시간/월 소요
- 동기: "이 시간을 전략적 분석에 사용하고 싶음"
- Pain: 매월 마지막 주는 수작업으로 바쁨

무장:
- 데이터: "월 10시간 × 시급 $50 = $500 절감 (연 $6,000)"
- 데모: POC 실행해서 "원본 vs AI 분석 결과 99% 일치" 시연
- ROI: "첫 달 투자 회수, 2개월차부터 순이익"

확산 경로:
1. 이든이 CFO에게 "시간 절감 효과" 보고
2. CFO가 경영진 회의에서 "비용 절감 + 분석 정확도 향상" 공식화
3. Accounting도 "월별 검증 작업 자동화 가능" 리스트 추가
4. Engineering도 "작은 투자, 큰 효과" 사례로 제시

---

## Step 5: Communication Plan

**경영진 (CFO/CTO):**
- 메시지: "AI로 월 $500 비용 절감 + 의사결정 속도 50% 향상"
- 포맷: 1-page ROI 요약 + 위험 mitigation 계획
- 주기: 월 1회 progress report

**직접 사용자 (이든):**
- 메시지: "반복 작업에서 해방 — 전략 분석에 집중하세요"
- 포맷: 주 1회 짧은 데모 + Q&A (도입 초기 4주)
- 주기: 주 1회 (도입 후 월 1회로 축소)

**Engineering:**
- 메시지: "깔끔한 API 통합 + 명확한 소유권 분리"
- 포맷: 기술 스펙 (API 명세, 에러 처리, 로깅 구조)
- 주기: 스프린트 단위 기술 미팅

**Accounting:**
- 메시지: "100% 감사 추적 가능 — 규제 준수 + 수동 검증 필요 X"
- 포맷: 데이터 플로우 다이어그램 + 감시 로그 샘플
- 주기: 월 1회 데이터 정확성 점검 (처음 3개월), 이후 분기 1회

**Legal:**
- 메시지: "리스크 통제 가능 — HITL(Human-in-the-loop) + 감사 로그"
- 포맷: AI 리스크 체크리스트 + 규제 매핑 테이블
- 주기: 마일스톤 단위 (POC → 파일럿 → 프로덕션)

---

## Output

Stakeholder Map: cost-analyst 에이전트 도입
────────────────────────────────────────
Total Stakeholders: 6명/팀
Champions: 이든 (user/driver)
Blockers: Legal/Compliance (CFO 지시 필요) — Mitigation: AI Risk Checklist 사전 제시
Decision Maker: CFO — Engage via: 월 1회 ROI 리뷰
Top Resistance: Trust Deficit (Accounting) — Counter: Shadow Mode 검증 → 99% 일치 증명
Communication Cadence:
  - 경영진: 월 1회
  - 사용자: 주 1회 (4주), 이후 월 1회
  - Engineering: 스프린트 단위
  - Accounting: 월 1회
  - Legal: 마일스톤 단위
Go/No-Go Confidence: **HIGH** (Champion 강함 + CFO 지지 명확 + Technical Risk 낮음)
```

### Bad Example

```markdown
# Stakeholder Map — agent-z

이해관계자:
- 경영진
- 사용자
- 팀들

파워-인터레스트: 높은 사람도 있고 낮은 사람도 있습니다.

저항:
- 사람들이 새 도구를 안 좋아할 수 있음
- 기술 문제가 있을 수 있음

전략:
- 더 설득하세요
- 좋은 커뮤니케이션을 하세요

---

문제점:
- 이해관계자 구체적 식별 없음 (이름, 역할 불명확)
- Power-Interest Matrix에 실제 배치 없음 (누가 어디에?)
- 저항 유형이 추상적 ("사람들이 안 좋아할" → 원인은?)
- 대응 전략이 실행 불가능 ("더 설득하세요" → 어떻게?)
- Champions 식별 없음 (누가 주도하는가?)
- 커뮤니케이션 계획이 없음 (누구에게 뭘 언제 말할지?)
- Go/No-Go 신뢰도 언급 없음 (도입 가능성은?)
```

---

# Agent Stakeholder Map

> 에이전트 도입 시 이해관계자 지도 — 누가 찬성하고, 누가 막고, 누가 결정하는가

## 개념

에이전트 도입은 기술 문제가 아니라 조직 변화 문제다. "AI가 내 일을 빼앗는다"는 불안이 가장 큰 저항 요인이고, 법무팀의 AI 리스크 우려, 엔지니어링의 기술 부채 걱정이 뒤를 따른다. 이해관계자를 미리 매핑하지 않으면 기술적으로 성공한 에이전트가 조직적으로 실패한다.

## Instructions

You are mapping **stakeholders for AI agent adoption**: **$ARGUMENTS**

### Step 1 — Stakeholder Identification

에이전트 도입에 관련된 이해관계자를 식별합니다:

| 이해관계자 | 역할 | 관심사 | 에이전트에 대한 태도 |
|-----------|------|--------|-------------------|
| **경영진 (C-Level)** | 최종 승인자 | ROI, 리스크, 경쟁 우위 | |
| **직접 사용자** | 일상 사용 | 업무 효율, 일자리 불안 | |
| **엔지니어링** | 구축/유지보수 | 기술 부채, 인프라 비용 | |
| **법무/컴플라이언스** | 리스크 검토 | 데이터 프라이버시, AI 규제 | |
| **운영/CS** | 장애 대응 | 안정성, 에스컬레이션 경로 | |
| **재무** | 예산 승인 | 비용 예측 가능성, ROI | |

### Step 2 — Power-Interest Matrix

```
        High Power
            │
   Manage   │   Engage
   Closely  │   Actively
            │
 ───────────┼──────────── High Interest
            │
   Monitor  │   Keep
   Only     │   Informed
            │
        Low Power
```

각 이해관계자를 매트릭스에 배치합니다:

```
[이해관계자]: [Power 1-5] × [Interest 1-5] → [사분면]
  └── 전략: [Engage/Manage/Inform/Monitor]
```

### Step 3 — Resistance Analysis

에이전트 도입의 핵심 저항 요인과 대응 전략:

| 저항 유형 | 근본 원인 | 대응 전략 |
|----------|----------|----------|
| **Job Threat** | "AI가 내 일을 대체한다" | Co-pilot 포지셔닝 — "AI가 반복 작업을 하고, 당신은 판단에 집중" |
| **Trust Deficit** | "AI 판단을 믿을 수 없다" | Shadow Mode 시작 → 정확도 증명 후 권한 확대 |
| **Control Loss** | "내가 통제할 수 없다" | Human-in-the-loop 설계 — 승인/거부 권한 보장 |
| **Risk Aversion** | "문제가 생기면 누가 책임?" | 책임 매트릭스(RACI) + 롤백 계획 명시 |
| **Tech Fatigue** | "또 새로운 도구를 배워야?" | 기존 워크플로우에 임베딩 — 별도 UI 최소화 |

### Step 4 — Champion Strategy

에이전트 도입의 내부 챔피언을 발굴하고 무장시킵니다:

```
Champion Profile:
  ├── 누구: [가장 큰 pain을 겪는 사람]
  ├── 동기: [에이전트가 해결하는 구체적 문제]
  ├── 무장:
  │   ├── 데이터: [현재 수동 작업 시간/비용]
  │   ├── 데모: [Shadow Mode 결과]
  │   └── ROI: [3개월 절약 예측]
  └── 확산 경로: [챔피언 → 팀 → 조직]
```

### Step 5 — Communication Plan

이해관계자별 맞춤 커뮤니케이션:

```
경영진:
  메시지: "경쟁사보다 [N]개월 앞서는 기회"
  포맷: 1-page ROI 요약 + 리스크 대비책
  주기: 월 1회 진행 보고

직접 사용자:
  메시지: "반복 작업에서 해방 — 당신의 판단력에 집중"
  포맷: 핸즈온 데모 + Q&A 세션
  주기: 주 1회 (도입 초기)

엔지니어링:
  메시지: "깔끔한 아키텍처 + 명확한 소유권"
  포맷: 기술 스펙 + 인프라 비용 예측
  주기: 스프린트 단위

법무:
  메시지: "리스크 통제 가능 — HITL + 감사 로그"
  포맷: AI 리스크 체크리스트 + 규제 매핑
  주기: 마일스톤 단위
```

### Output

```
Stakeholder Map: [agent initiative]
──────────────────────────────────
Total Stakeholders: [N]
Champions: [names/roles]
Blockers: [names/roles] — Mitigation: [strategy]
Decision Maker: [name/role] — Engage via: [strategy]
Top Resistance: [type] — Counter: [strategy]
Communication Cadence: [summary]
Go/No-Go Confidence: [Low/Medium/High]
```

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- AI 도입 저항 패턴: AI Dubbing/Avatar 조직 도입 경험 기반
- Trust Building Sequence: agent-gtm 스킬과 연결

---

## Further Reading
- John Kotter, *Leading Change* — 8-step change management framework
- Anthropic, "Building Effective Agents" (2024) — Human-agent trust patterns
