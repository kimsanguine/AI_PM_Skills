# 좋은 예제 — Orchestration

## 사용자 요청
"우리 팀이 경쟁사 분석, 시장 리포트 작성, 실행 계획 수립을 동시에 진행해야 하는데, 3명의 에이전트를 어떻게 조율하면 좋을까?"

## 승인 이유
- 2개 이상의 에이전트가 협력해야 하는 멀티 에이전트 설계 요청
- 작업 간 의존성 정의와 조율이 필요한 복잡한 시스템
- 성능(속도, 비용)과 신뢰성 요구사항 암시

## 예상 처리
1. 작업 의존성 분석: 경쟁사 분석 → 시장 리포트 → 실행 계획 (순차)
2. 패턴 평가: Sequential Chain 적합도 확인
3. 구체적 설계: 각 에이전트 역할, 입출력 형식, 에러 처리 정의
4. 복잡도 검증: "가장 간단한 패턴인가?" 재확인
5. 최종 산출물: 오케스트레이션 다이어그램 + Quality Gate 체크리스트

## 처리 결과 예시
```
Sequential Chain 패턴 선택:
Analysis Agent (2시간) → Report Agent (1시간) → Planning Agent (1시간)
총 지연: 4시간 (병렬이면 2시간, 의존성 때문에 필요)

에러 처리:
- Analysis 실패: 재시도 1회, 실패 시 시장 리포트 스킵
- Report 실패: Planning에 "데이터 부분 누락" 플래그
- Planning 실패: 사람이 수동으로 검토 (고가치 산출물)
```

## LangGraph 기반 패턴 Good Example

### 설계 구조

사용자 요청을 받은 **리더 에이전트(Lead Agent)**가 다음과 같이 작업을 위임합니다:

```
사용자: "경쟁사 분석, 시장 리포트, 실행 계획을 모두 해줘"
    ↓
[Clarification 미들웨어]
  → "경쟁사는 누구인가? 시장 범위는?"
  → 모호성 해소 후 순차 작업 결정
    ↓
리더 에이전트
  1. Analysis 서브에이전트 위임
     ├─ Registry에서 GeneralPurposeAgent 검색
     ├─ Timeout: 300초 (데이터 수집 작업)
     ├─ Model: gpt-4-turbo (분석 정확도)
     └─ 메모리 주입: 이전 경쟁사 분석 데이터
  ↓
  2. Report 서브에이전트 위임
     ├─ Analysis 결과를 입력으로 받음
     ├─ Summarization 미들웨어 활성화 (긴 분석 결과 처리)
     ├─ Timeout: 180초
     └─ Sandbox에서 리포트 포매팅
  ↓
  3. Planning 서브에이전트 위임
     ├─ Report 결과를 기반으로 실행 계획 수립
     ├─ View Image 미들웨어 (차트/다이어그램 입력)
     ├─ Timeout: 240초
     └─ 결과를 파일로 저장 (Sandbox 도구)
    ↓
[Memory 미들웨어]
  → "분석 결과" 저장 (Episodic)
  → "경쟁사 인사이트" 저장 (Semantic)
    ↓
최종 응답 반환
```

### 미들웨어 체인의 역할

| 단계 | 미들웨어 | 동작 |
|-----|--------|------|
| 사전 처리 | Clarification | "경쟁사 X, Y, Z 맞나요?" → 확인 |
| 메모리 강화 | Memory | 이전 경쟁사 리스트, 시장 정의 주입 |
| 안전성 | Subagent Limit | 최대 3개 서브에이전트만 호출 (무한 루프 방지) |
| 격리 | Thread Data | 사용자별 세션 상태 분리 (멀티 유저 지원) |
| 파일 처리 | Uploads | 사용자가 경쟁사 목록 CSV 업로드 시 처리 |
| 이미지 | View Image | 경쟁사 조직도 이미지 분석 |
| 압축 | Summarization | Report 결과가 100K 토큰 초과 시 자동 요약 |
| 실행 | Sandbox | 리포트 생성, 스크립트 실행 (파일 시스템 격리) |

### Registry 설정 (config.yaml)

```yaml
subagents:
  # 분석 업무 전담
  analysis:
    class: "agents.GeneralPurposeAgent"
    description: "경쟁사 분석, 시장 조사"
    timeout: 300  # 데이터 수집이 오래 걸림
    model:
      name: "gpt-4-turbo"  # 정확도 우선
      fallback: "gpt-3.5-turbo"

  # 리포트 작성 전담
  report:
    class: "agents.GeneralPurposeAgent"
    description: "구조화된 리포트 작성"
    timeout: 180
    model:
      name: "gpt-4"
      fallback: "gpt-3.5-turbo"

  # 실행 계획 수립
  planning:
    class: "agents.GeneralPurposeAgent"
    description: "전략적 실행 계획 수립"
    timeout: 240
    model:
      name: "gpt-4"
      fallback: "gpt-3.5-turbo"

  # 파일 작업 (Bash)
  bash:
    class: "agents.BashAgent"
    description: "파일 저장, 스크립트 실행"
    timeout: 60
    model: null

# Middleware 설정
middlewares:
  - name: "clarification"
    enabled: true
  - name: "memory"
    enabled: true
  - name: "subagent_limit"
    max_calls: 3
  - name: "summarization"
    token_limit: 100000  # 100K 초과 시 요약
```

### 에러 처리 전략

```python
# 리더 에이전트의 위임 로직
def orchestrate():
    try:
        # 1단계: Analysis
        analysis = delegate_to_subagent(
            "analysis",
            task="경쟁사 분석",
            fallback_action="skip_to_planning"  # 실패 시 스킵
        )
    except TimeoutError:
        logger.warn("Analysis timeout (300s)")
        analysis = None  # 부분 진행

    # 2단계: Report
    report = delegate_to_subagent(
        "report",
        context=analysis,
        fallback_action="continue_with_template"  # 기본 템플릿 사용
    )

    # 3단계: Planning (최종, 실패 불가)
    planning = delegate_to_subagent(
        "planning",
        context=report,
        retry_count=3,  # 재시도
        fallback_action="manual_review"  # 사람이 검토
    )

    return merge_results([analysis, report, planning])
```

### 성과 지표

| 지표 | 목표 | 프로덕션 구현 |
|-----|-----|------------|
| 처리 시간 | <10분 | 순차 실행 (병렬 불가, 의존성) → ~4-5분 |
| 성공률 | >95% | 재시도 + 폴백 (partial success 허용) |
| 메모리 활용 | 낮음 | Summarization으로 컨텍스트 압축 |
| 비용 | 최소화 | 각 에이전트마다 timeout 명시적 설정 |
