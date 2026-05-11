# 도메인 컨텍스트 — Model Router

## 1) Domain Scope
에이전트 시스템에서 **작업 복잡도에 따라 최적의 LLM 모델을 선택**하는 영역.
- 포함: T1-T4 모델 분류, 라우팅 결정 매트릭스, 폴백 전략
- 포함: 비용 최적화, 품질 게이트, 모니터링 지표
- 제외: 특정 모델 성능 비교, 미세 튜닝, 모델 훈련

## 2) Primary Users
- **시스템 아키텍트**: 모델 라우팅 전략 수립
- **비용 최적화 담당자**: 월간 비용 예산 관리
- **품질 보증**: 모델 선택이 품질에 미치는 영향 추적

## 3) Required Inputs
- 에이전트 시스템의 주요 작업 목록:
  - 각 작업의 입력 복잡도 (Low/Medium/High)
  - 출력 품질 민감도 (Low/Medium/High)
  - 지연시간 요구사항
  - 비용 허용도
- 사용 가능한 모델 목록과 가격
- 월간 사용량 예측

## 4) Output Contract
- **작업 분류**: T1-T4로 모든 작업 분류
- **라우팅 결정 매트릭스**: 각 작업별 추천 모델 + 선택 근거
- **비용 비교**: 라우팅 vs 단일 모델 시나리오 계산
- **폴백 체인**: Primary → Fallback 1 → Fallback 2 명시
- **품질 검증**: 최종 품질 점수 ≥90% 달성 방법
- **모니터링 계획**: 주간/월간 추적 지표

## 5) Guardrails
- 라우팅 오버헤드가 절감액보다 크면 라우팅 금지
- 모든 작업이 고복잡도면 T3 고정 (라우팅 불필요)
- 폴백 체인 없이 라우팅 결정 금지
- 품질 측정 방법 없이 라우팅 확정 금지
- False Moat 제거: "우리 UI가 더 좋다" 같은 근거 없는 선택 금지

## 6) Working Facts (TO BE UPDATED by reviewer)
- [ ] T1-T2 성능 차이: 정형 데이터 작업은 <5% (예시값), 창의 작업은 15-20% (예시값)
- [ ] 라우팅 정확도 목표: >85% (예시값, 이하면 폴백 빈도 >20%)
- [ ] 폴백 비율: 이상적으로 <5% (예시값, >10%면 라우팅 규칙 재검토)
- [ ] 비용 절감 달성률: 실무 평균 30-50% (예시값, 목표: 40-60%)

## 7) Fill-in Checklist

### 작업 분류
- [ ] T1 (간단): 작업 __개 (데이터 파싱, 분류)
- [ ] T2 (표준): 작업 __개 (요약, 비교, 진단)
- [ ] T3 (복잡): 작업 __개 (전략, 창의, 분석)
- [ ] T4 (전문): 작업 __개 (코드, 수학, 도메인)

### 라우팅 결정 매트릭스
- [ ] 최소 5개 작업에 대해 라우팅 결정 정당화

### 비용 비교
- [ ] "모두 T3" 시나리오: $____ /월
- [ ] "라우팅" 시나리오: $____ /월
- [ ] 절감율: ___% (목표: >40%)
- [ ] 품질 점수: ___ (목표: >90%)

### 폴백 전략
- [ ] Primary 모델: ____
- [ ] Fallback 1 모델: ____
- [ ] Fallback 2 모델: ____
- [ ] 각 단계의 재시도 조건 명시 (timeout, quality score)

### 모니터링 계획
- [ ] 추적 지표 1: 각 모델별 호출 수 및 비용
- [ ] 추적 지표 2: 라우팅 정확도 (오분류 비율)
- [ ] 추적 지표 3: 폴백 발동 빈도
- [ ] 추적 지표 4: 최종 품질 점수

### Quality Gate
- [ ] 작업 분류가 명확하고 일관성 있는가?
- [ ] 라우팅 결정이 데이터 기반인가? (추측 아님)
- [ ] 폴백 전략이 완전하고 자동으로 작동하는가?
- [ ] 최종 품질 목표 ≥90%를 달성할 수 있는가?
- [ ] 실제 비용 절감이 라우팅 오버헤드보다 큰가?

## 8) 참고 사례: 프로덕션 라우팅 시스템

> 아래는 특정 프로덕션 환경에서의 사례입니다. 조직과 도메인에 따라 다르게 설계할 수 있습니다.

### 비용 비교 가이드

모델 라우팅의 경제성을 평가하기 위한 비용 계산 방법:

**단일 모델 (항상 T3 사용) 시나리오 (예시값)**:
```
월간 작업 수: 10,000개
T3 평균 비용/작업: $0.02 (예시값)
월간 총 비용 = 10,000 × $0.02 = $200/월
```

**라우팅 시나리오 (예시값)**:
```
T1 (40%): 4,000개 × $0.005/작업 = $20
T2 (35%): 3,500개 × $0.01/작업 = $35
T3 (20%): 2,000개 × $0.02/작업 = $40
T4 (5%): 500개 × $0.05/작업 = $25
라우팅 오버헤드: $10 (보통 전체 비용의 1-5%, 예시값)
월간 총 비용 = $20 + $35 + $40 + $25 + $10 = $130/월
```

**비용 절감 = ($200 - $130) / $200 = 35% (예시값)**

**총 비용 계산 프레임워크**:

라우팅 시스템의 실제 비용을 정확히 평가하려면 다음 요소들을 고려해야 합니다:

```
총 비용 = API 호출 비용 + (지연시간 비용) + (재처리 비용)

세부 항목:
1. API 호출 비용 = Σ(모델별 토큰 단가 × 예상 호출 수)
2. 지연시간 비용 = 평균 지연시간(초) × 시간당 비용 × 월간 요청 수
   - 사용자가 기다리는 시간이 비용으로 환산됨 (생산성 손실)
3. 재처리 비용 = 오류율 × 재처리 모델 비용 × 월간 요청 수
   - 폴백 발동 시 추가 비용 발생
```

**예시 계산**:
```
조건:
- 월간 요청 수: 1,000개
- 오류율: 5% (50개 재처리)
- 시간당 비용: $100 (사용자 시간 가치)

API 비용: $130 (위 시나리오)
지연시간 비용: 평균 2초 × ($100/3600) × 1,000 = $55
재처리 비용: 50개 × $0.02 (T3 모델) = $1

총 비용 = $130 + $55 + $1 = $186/월
```

**체크리스트:**
- [ ] 절감액 > 라우팅 오버헤드 (일반적으로 절감이 10배 이상일 때 도입 가치)
- [ ] T1 작업 비율이 30% 이상일 때 경제성 최대화
- [ ] 정확도 90% 이상 확보 후 폴백 비용 고려
- [ ] 지연시간 비용도 포함하여 총 비용 평가

### 2단계 품질 게이트

라우팅 결정의 신뢰성을 검증하기 위한 2단계 게이트 설계:

**Stage 1: Confidence Threshold Check (라우팅 전)**
- 라우터가 작업 분류를 정하기 전에 신뢰도 점수 계산
- 신뢰도 > 85% (예시값)이면 선택 모델로 라우팅
- 신뢰도 ≤ 85%이면 Clarification 미들웨어 실행 (사용자 확인)
- 목표: 오분류율 <10%

**Stage 2: Output Validation (라우팅 후)**
- 모델의 응답 품질을 검증 (길이, 형식, 컨텍스트 관련성)
- 품질 점수 < 80% (예시값)이면 폴백 모델로 재시도
- 폴백 모델도 실패 시 T3 모델로 최종 재시도
- 목표: 최종 품질 점수 > 90%

**효과:**
- 잘못된 라우팅 조기 감지
- 사용자 만족도 유지 (품질 저하 최소화)
- 비용과 품질의 균형 유지

### Subagent Registry: 모델과 에이전트의 분리

프로덕션 시스템은 **모델 선택(Router)**과 **에이전트 선택(Orchestration)**을 명확히 분리합니다.

```
사용자 요청
    ↓
[Clarification 미들웨어]
  → 모호성 해소
    ↓
리더 에이전트 (모델 선택 결정)
  → 작업 복잡도 평가
  → Primary 모델 선택
  → 폴백 체인 설정
    ↓
[Registry 쿼리]
  ├─ Subagent 목록 조회 (config.yaml)
  ├─ 선택된 모델로 인스턴스 생성
  └─ Timeout override 적용
    ↓
서브에이전트 실행
  (선택된 모델로 작업 수행)
    ↓
실패 → [폴백 1] → [폴백 2] → 최종 재시도
```

**Registry 패턴의 장점**:
- 모델 변경 시 코드 수정 불필요 (config.yaml만 수정)
- 런타임에 서브에이전트 추가/제거 가능
- 모델 해석력(explainability)을 위해 선택 이유도 기록

### Config-Driven Timeout Override

프로덕션 시스템의 timeout 설정 방식:

```yaml
# config.yaml (예시값, 프로젝트에 맞게 조정)
app:
  default_timeout: 30  # 글로벌 기본값 (예시값: 30초)

model:
  timeout_override:
    "gpt-4": 60  # 모델별 override (예시값)
    "gpt-3.5-turbo": 30  # (예시값)
    "claude-3-opus": 120  # Opus는 복잡한 작업용 (예시값)

subagents:
  general:
    class: "agents.GeneralPurposeAgent"
    timeout: 45  # 에이전트별 override (예시값)
    model:
      name: "gpt-4"
      fallback: "gpt-3.5-turbo"

  bash:
    class: "agents.BashAgent"
    timeout: 120  # I/O 작업은 더 길게 (예시값)
    model: null

  specialized:
    class: "agents.SpecializedAnalysisAgent"
    timeout: 180  # 전문 작업용 (예시값)
    model:
      name: "claude-3-opus"
      fallback: "gpt-4"
```

**우선순위 (높음→낮음)**:
1. Subagent-specific timeout (config.yaml의 subagents.{name}.timeout)
2. Model-specific timeout (config.yaml의 model.timeout_override)
3. Global default timeout (config.yaml의 app.default_timeout)

### Model Resolution with Fallback

프로덕션 시스템의 모델 해석 로직:

```python
class ModelResolver:
    def resolve_model(self, requested_model: str, subagent_name: str) -> str:
        """
        요청 모델 → 기본값 → None 순서로 폴백

        반환값은 (model_name, timeout, explanation)의 튜플
        """

        # Step 1: 요청된 모델 확인
        if requested_model and is_available(requested_model):
            timeout = config.model.timeout_override.get(
                requested_model,
                config.app.default_timeout
            )
            return (requested_model, timeout, "User requested")

        # Step 2: Subagent 설정의 기본값 확인
        subagent_config = config.subagents[subagent_name]
        if subagent_config.model and subagent_config.model.name:
            primary_model = subagent_config.model.name
            timeout = subagent_config.timeout  # subagent override 우선
            return (primary_model, timeout, "Subagent config")

        # Step 3: 폴백 체인
        if subagent_config.model and subagent_config.model.fallback:
            fallback_model = subagent_config.model.fallback
            timeout = config.model.timeout_override.get(
                fallback_model,
                config.app.default_timeout
            )
            logger.warning(f"Primary model unavailable. Using fallback: {fallback_model}")
            return (fallback_model, timeout, "Fallback chain")

        # Step 4: 시스템 기본값
        default = "gpt-3.5-turbo"
        timeout = config.app.default_timeout
        logger.error(f"No model configured for {subagent_name}. Using system default.")
        return (default, timeout, "System default")

    def create_subagent(self, name: str, requested_model: str = None) -> object:
        """
        1. 모델 해석
        2. 타임아웃 설정
        3. 폴백 준비
        """
        model, timeout, reason = self.resolve_model(requested_model, name)

        subagent_class = import_class(config.subagents[name].class_path)
        subagent = subagent_class(
            model=model,
            timeout=timeout,
            fallback_models=self.get_fallback_chain(name),
            explanation=f"Model selection reason: {reason}"
        )

        logger.info(f"Created {name} with model={model}, timeout={timeout}s ({reason})")
        return subagent
```

### Clarification 미들웨어가 라우팅 전 모호성 해소

```python
class ClarificationMiddleware:
    """요청이 모호하면 리더 에이전트가 명확히 하도록 강제"""

    def process(self, thread_state: ThreadState) -> ThreadState:
        user_input = thread_state.messages[-1].content

        # 모호성 감지 (정규식, 키워드 분석)
        ambiguities = self.detect_ambiguities(user_input)

        if len(ambiguities) > 0:
            # Clarification 질문 생성
            clarification_prompt = self.generate_questions(ambiguities)

            # 리더 에이전트에게 의도 전달
            thread_state.metadata["needs_clarification"] = {
                "questions": clarification_prompt,
                "detected_ambiguities": ambiguities
            }

            # 시스템 프롬프트에 추가
            system_prompt += f"""
사용자 요청에 다음 모호성이 있습니다:
{clarification_prompt}

먼저 사용자에게 확인한 후 작업을 진행하세요.
"""

        return thread_state
```

**예시**:
```
사용자: "보고서 만들어줘"
↓
[Clarification]
  감지된 모호성:
  - 보고서 종류? (기술, 비즈니스, 성과 등)
  - 대상 청중? (임원진, 팀, 클라이언트)
  - 분석 범위? (월간, 분기, 연간)
↓
Clarification 질문 반환:
"어떤 보고서가 필요하신가요? (1) 기술보고서, (2) 비즈니스보고서..."
↓
사용자: "기술보고서, 최근 3개월"
↓
명확해진 요청으로 라우팅 실행
```

### Agent Routing vs Model Routing: 언제 어떤 라우팅을 선택할까?

**Model Routing (이 문서의 주제)**:
- 언제: 같은 작업을 다양한 LLM 모델로 처리 가능할 때
- 예: 데이터 파싱은 T1 모델, 전략 수립은 T3 모델
- 효과: 비용 최적화 (30-60% 절감)
- 특징: 에이전트(도구/기능)는 동일, 모델만 바뀜

**Agent Routing (Orchestration 스킬 참고)**:
- 언제: 다른 전문성/도구가 필요한 작업으로 분기할 때
- 예: 일반 질문은 General Agent, 코드 작업은 Bash Agent
- 효과: 전문성 향상 (정확도 상승)
- 특징: 에이전트 자체가 바뀜 (각각 다른 도구/모델 사용)

**함께 사용하기 (권장)**:
```
사용자 요청
  ↓
[Clarification 미들웨어]
  ↓
[Agent Router]: 어떤 에이전트? (General vs Bash vs Custom)
  ↓
선택된 에이전트 내에서:
[Model Router]: 어떤 모델? (T1 vs T2 vs T3)
  ↓
최종 응답
```

이 구조를 통해 **에이전트 전문성 + 모델 비용 최적화**를 동시에 달성합니다.

### 적용 교훈: 라우터 설계의 핵심 원칙 3가지

| 원칙 | 설계 | 프로덕션 구현 |
|-----|------|-------------|
| **명시성** | 선택 기준을 명시적으로 정의 | Config-driven timeout + explanation 기록 |
| **폴백성** | 모든 경로에 대안 있음 | Primary → Fallback 1 → Fallback 2 체인 |
| **확장성** | 새 모델/에이전트 추가 용이 | Registry 패턴 + config 기반 (코드 수정 불필요) |

**실무 적용 체크리스트**:

1. **Timeout 설정**
   - [ ] 기본값 설정했는가? (보통 30초)
   - [ ] I/O 작업은 더 길게? (bash 60초+)
   - [ ] 전문 작업은? (complex analysis 120초+)
   - [ ] 모니터링 중 자주 timeout나는 에이전트 없는가?

2. **폴백 체인**
   - [ ] Primary 모델이 unavailable이면? (명시적 fallback)
   - [ ] Fallback도 실패하면? (최종 에러 처리)
   - [ ] 폴백 발동 빈도 추적하는가? (>10% = 문제 신호)

3. **Clarification 활성화**
   - [ ] 사용자 요청이 모호할 가능성 높은가? → 미들웨어 활성화
   - [ ] 자동 분류 정확도 낮은가? (90% 미만) → Clarification 필수
   - [ ] 모호성을 줄일 프롬프트 엔지니어링 했는가?

4. **모니터링**
   - [ ] 각 모델별 호출 수 추적
   - [ ] 라우팅 정확도 (올바른 모델 선택 비율)
   - [ ] 폴백 빈도 (낮을수록 좋음, <5% 목표)
   - [ ] 최종 응답 품질 점수 (≥90% 목표)
