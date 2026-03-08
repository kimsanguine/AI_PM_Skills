# Domain Context — instruction 스킬

## 1) Domain Scope

**이 스킬이 소유하는 영역:**
- Agent Instruction의 7요소(Role/Context/Objective/Tools/Memory/Output/Failure) 구조화
- 의도 기반 설계로 판단 기준과 트레이드오프 명시
- 반복 판단 패턴의 외부화(SKILL.md 분리)

**이 스킬이 소유하지 않는 영역:**
- 프롬프트 토큰 최적화 (→ `forge/prompt`)
- 컨텍스트 윈도우 예산 계획 (→ `forge/ctx-budget`)
- PRD 공식 문서화 (→ `forge/prd`)

## 2) Primary Users

- **새로운 에이전트 설계자**: Instruction 초안이 없는 상태에서 7요소 완성
- **기존 에이전트 문제 해결자**: 일관되지 않은 행동이나 판단 기준 불명확한 에이전트 개선
- **포트폴리오 표준화 담당**: 여러 에이전트의 Instruction을 일관된 포맷으로 통일

## 3) Required Inputs

**필수 입력:**
1. 에이전트 이름/목적
2. 에이전트가 누구를 위해 존재하는지
3. 에이전트가 해야 할 일(Primary Goal)

**선택 입력:**
- 기존 Instruction 초안 (있으면 검토 대상)
- 사용할 도구 목록
- 메모리 파일 목록

## 4) Output Contract

**산출물:**
- 7요소 완성된 Instruction 문서
- 각 요소가 개발자의 의문을 명확히 답변

| 요소 | 보증 |
|------|------|
| Role | 에이전트의 전문성 범위가 명확함 |
| Context | 사용자/환경/데이터가 명시됨 |
| Objective | Primary Goal 1개 + Secondary 우선순위 + Anti-Goals 3개 이상 |
| Tools | 각 도구의 사용 조건과 제한 명시 |
| Memory | 단기/장기/절차적 메모리 분리 정의 |
| Output | 채널/형식/길이/언어/톤 모두 명시 |
| Failure | 4개 이상 실패 시나리오 + 대응 방법 |

## 5) Guardrails

**라우팅 규칙:**
- 프롬프트 최적화 필요 → `forge/prompt` (CRISP 프레임워크 적용)
- 컨텍스트 윈도우 예산 계획 필요 → `forge/ctx-budget` (메모리 전략의 토큰 배분)
- PRD 공식 문서화 필요 → `forge/prd` (Instruction → PRD 변환)

**품질 기준:**
- Instruction 설계는 의도를 명확히 하는 것이지, 특정 기술 구현은 아님
- 7요소는 순서가 정해져 있지 않으며 유기적으로 연결
- Tool 목록은 "필요한 도구만" — 최소 권한 원칙 적용

## 6) Working Facts

**Instruction 7요소 작성 시간 기준:**

| 요소 | 예상 시간 | 토큰 |
|------|----------|------|
| Role | 5분 | 150~200 |
| Context | 10분 | 200~300 |
| Objective | 15분 | 300~400 |
| Tools | 10분 | 200~400 |
| Memory | 10분 | 200~300 |
| Output | 10분 | 250~350 |
| Failure | 15분 | 300~500 |
| **Total** | **75분** | **~1,600~2,450 tokens** |

**에이전트 유형별 Instruction 복잡도:**

| 유형 | 도구 수 | 메모리 계층 | Anti-Goals | 난이도 |
|------|--------|----------|-----------|--------|
| 단순 (1도구) | 1~2 | 1 | 2~3 | 낮음 |
| 표준 (3~5도구) | 3~5 | 2~3 | 3~4 | 중간 |
| 복잡 (5개+ 또는 오케스트레이션) | 5+ | 3 | 4+ | 높음 |

**TO BE UPDATED by reviewer:**
- 조직별 Anti-Goals 기준 (일반적으로 3~4개가 충분한가, 더 필요한가?)
- 메모리 3계층의 최적 로드 순서
- Tool 목록의 평균 항목 수

## 7) Fill-in Checklist

- [ ] Role이 구체적이고 도메인 명시되어 있는가?
- [ ] Context에 사용자 프로필, 실행 환경, 접근 데이터가 명시되었는가?
- [ ] Objective가 Primary Goal 1개 + Secondary Goals + Anti-Goals 3개 이상인가?
- [ ] Tools 각각에 "사용 조건"과 "제한"이 명시되었는가?
- [ ] Memory가 단기/장기/절차적 3계층으로 분리되었는가?
- [ ] Output Format이 채널/형식/길이/언어/톤 모두 명시되었는가?
- [ ] Failure Handling이 4가지 이상 시나리오 + 구체적 행동을 포함하는가?
- [ ] Anti-Goals가 추상적이지 않고 구체적인 시나리오로 작성되었는가?
