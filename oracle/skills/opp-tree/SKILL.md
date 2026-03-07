---
name: opp-tree
description: "Analyze where AI agents can add value and which tasks to automate — systematically map repetitive workflows, manual processes, and operational bottlenecks to identify the best agent opportunities. Build an Agent Opportunity Tree from desired outcomes to solvable problems, agent solution candidates, and validation experiments. Use when exploring where AI agents could add value to a platform or service, finding automation opportunities in workflows, identifying repetitive tasks worth automating, prioritizing which agent to build first, or mapping the full opportunity space before committing to development. Applicable to any domain — customer support, edtech, SaaS, operations, and more."
argument-hint: "[product or domain to explore]"
---

## Agent Opportunity Tree (AOT)

에이전트를 "만들 수 있냐"가 아니라 "만들어야 하냐"를 결정하는 프레임워크.  
Teresa Torres의 Opportunity Solution Tree를 AI 에이전트 디스커버리에 맞게 재설계했습니다.

---

### 왜 에이전트에는 다른 OST가 필요한가

일반 OST는 제품 기능을 탐색할 때 씁니다.  
에이전트 OST는 다릅니다. 에이전트는 **자율적으로 행동**하기 때문에 잘못된 기회를 선택하면 오류가 조용히 증폭됩니다.

에이전트 디스커버리에서 빠지기 쉬운 함정:
- "기술적으로 가능하니까" 만든다 → 아무도 안 씀
- "반복 작업이니까" 자동화한다 → 판단이 필요한 부분을 건드려 더 큰 문제 발생
- 에이전트 1개로 너무 많은 걸 해결하려 한다 → 실패율 급증

AOT는 이 함정을 피하기 위해 **4개 레이어를 순서대로** 탐색합니다.

---

### 구조 (4 레이어)

```
[Automation Outcome]
        │
   ┌────┴────┐
[Opportunity] [Opportunity] ...
        │
   ┌────┴────┐
[Agent Type] [Agent Type] ...
        │
   ┌────┴────┐
[Experiment] [Experiment] ...
```

**레이어 1 — Automation Outcome (자동화 목표)**

단 하나의 측정 가능한 목표를 정합니다.  
좋은 예: "PM이 뉴스 수집에 쓰는 시간을 주 5시간 → 0시간으로 줄인다"  
나쁜 예: "업무를 AI로 자동화한다" (너무 넓음)

**레이어 2 — Opportunities (기회, 문제 공간)**

자동화로 해결 가능한 반복 작업, 판단 패턴, 병목 지점을 발굴합니다.  
기회 프레이밍 공식:  
`"[누가] [어떤 상황에서] [반복적으로] [무엇을 해야 하는데] [시간/실수/비용이 든다]"`

기회 우선순위 점수:  
`Opportunity Score = 반복빈도(1-5) × 자동화가능성(1-5) × 판단의존도 역수(5=저판단)`

> ⚠️ 판단 의존도가 높을수록 에이전트화가 어렵습니다. 점수가 낮은 기회는 Rule-based 자동화나 인간 처리가 더 적합합니다.

**레이어 3 — Agent Solutions (에이전트 솔루션 후보)**

각 기회마다 최소 3가지 에이전트 유형을 탐색합니다:

| 유형 | 설명 | 언제 적합한가 |
|---|---|---|
| **Trigger Agent** | 이벤트 발생 시 단일 작업 실행 | 명확한 입력/출력, 판단 최소 |
| **Pipeline Agent** | 순차 다단계 처리 | 정해진 워크플로우 자동화 |
| **Research Agent** | 정보 수집 후 요약/판단 | 탐색 범위가 동적인 경우 |
| **Monitor Agent** | 주기적 감시 후 알림/액션 | 임계값 기반 반응 필요 |
| **Orchestrator Agent** | 하위 에이전트를 조율 | 복잡한 멀티스텝, 병렬 처리 |

각 솔루션 후보에 대해 반드시 답해야 할 3가지:
1. **트리거**: 무엇이 에이전트를 시작시키는가?
2. **도구**: 어떤 툴/API/파일에 접근해야 하는가?
3. **종료 조건**: 에이전트가 성공적으로 완료됐다는 것을 어떻게 아는가?

**레이어 4 — Experiments (검증 실험)**

에이전트를 구현하기 전에 핵심 가정을 먼저 테스트합니다.

에이전트 가정 4축:
- **Value**: 이 자동화가 실제로 시간/비용을 절감하는가?
- **Feasibility**: 필요한 데이터/API에 접근 가능한가?
- **Reliability**: 충분한 정확도로 반복 실행 가능한가?
- **Ethics**: 자동화해도 괜찮은 판단인가? 오류 발생 시 영향은?

최소 검증 실험 예시:
- "하루 동안 직접 해보며 실제 반복 패턴 기록"
- "API 호출 5회 테스트 → 응답 품질 점검"
- "MVP 프롬프트 + 수동 실행 10회 → 정확도 측정"

---

### 사용 방법

`/agent-opportunity-tree [자동화하려는 업무 또는 문제]`

---

### Instructions

You are helping to build an **Agent Opportunity Tree** for: **$ARGUMENTS**

**Step 1 — Automation Outcome 확정**
- 측정 가능한 자동화 목표 1개를 명확히 정의한다
- "시간 절감", "오류 감소", "비용 절감" 중 하나에 수치를 붙인다

**Step 2 — Opportunities 발굴 (3~5개)**
- 주어진 문제/업무에서 반복 작업, 판단 패턴, 병목을 추출한다
- 각 기회에 Opportunity Score를 계산한다 (반복빈도 × 자동화가능성 × 판단의존도 역수)
- Score 상위 3개를 선택하고, 낮은 기회는 제외 이유를 명시한다

**Step 3 — Agent Solutions 후보 (기회당 2~3개)**
- 각 기회마다 에이전트 유형 2~3개를 제안한다
- 각 후보의 트리거 / 필요 도구 / 종료 조건을 명시한다
- 구현 난이도를 Low/Medium/High로 표시한다

**Step 4 — Experiments 설계 (최우선 솔루션 1~2개)**
- Value / Feasibility / Reliability / Ethics 4축 가정을 나열한다
- 각 가정의 검증 실험을 2일 이내에 할 수 있는 수준으로 설계한다

**Step 5 — 다음 권장 액션**
- 가장 높은 Opportunity Score + 가장 낮은 구현 난이도 조합을 추천한다
- `/agent-instruction-design`으로 연결할 준비가 됐는지 확인한다

---

### 참고
- 원본 프레임워크: Teresa Torres, *Continuous Discovery Habits* (OST)
- 에이전트 특화 확장: Sanguine Kim (이든), 2026
- Reliability / Ethics 축: Byeonghyeok Kwak의 엔터프라이즈 에이전트 거버넌스 논의에서 영감

---

## Further Reading
- Teresa Torres, *Continuous Discovery Habits* — Opportunity Solution Tree origin
- Marty Cagan, *INSPIRED* — Continuous product discovery
