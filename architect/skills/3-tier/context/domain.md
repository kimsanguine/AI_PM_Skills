# 도메인 컨텍스트 — 3-Tier Pattern

## 1) Domain Scope
Prometheus(전략) → Atlas(조율) → Workers(실행)의 **3계층 멀티 에이전트 오케스트레이션 패턴** 설계 및 구현.
- 포함: 계층 역할 정의, 통신 프로토콜, 작업 분해, 결과 통합, 품질 게이트, 에러 복구
- 제외: Orchestration의 기본 패턴 선택 (orchestration 스킬), 개별 에이전트 성능 최적화

## 2) Primary Users
- **시스템 아키텍트**: 3-tier 구조 설계 및 검증
- **PM**: 전략(Prometheus) 계층에서 목표와 제약 정의
- **엔지니어**: Atlas 조율 로직 구현, Workers 작업 명세화

## 3) Required Inputs
- 복잡한 워크플로우의 전체 문제 정의
- 전략적 목표 (Prometheus가 정하는 것)
- 예상 작업 수 및 의존성
- Worker들이 수행할 구체적 작업 목록
- 에러 허용도 및 품질 요구사항

## 4) Output Contract
- **계층별 책임 정의**:
  - Prometheus: 목표, 제약, 마감
  - Atlas: 작업 분해, Worker 할당, 의존성 관리, 결과 통합
  - Workers: 단일 작업 실행, 구조화된 결과 반환
- **통신 프로토콜**:
  - Prometheus → Atlas: 목표 형식
  - Atlas → Workers: 작업 명세 형식
  - Workers → Atlas: 결과 형식 (output + confidence + errors)
  - Atlas → Prometheus: 종합 결과 형식
- **에러 복구 전략**: 재시도, 폴백, 수동 개입 경로
- **아키텍처 다이어그램**: 3계층 구조 및 통신 흐름

## 5) Guardrails
- 2개 이하의 에이전트면 3-tier 불필요 (orchestration으로 충분)
- Prometheus가 없으면 자동화 시스템이지 의도적 설계 아님
- Atlas가 execution work를 직접 수행하면 "God Atlas" anti-pattern
- 통신 프로토콜 미정의 시 각 계층이 서로 이해 못함
- Workers가 다른 Workers를 직접 호출하면 안 됨 (Atlas를 거쳐야 함)

## 6) Working Facts (TO BE UPDATED by reviewer)
- [ ] 3-tier 도입 기준: 3개 이상의 에이전트 + 전략적 조율 필요 + 복잡도 높음
- [ ] Atlas의 작업 분해 정확도: <90%이면 재작업 필요 (평균 5-15% 재작업률)
- [ ] 통신 프로토콜 미정의 시 발생 문제: 결과 파싱 실패율 20-40%
- [ ] 3-tier 구축 시간: 설계 1주, 구현 2-3주, 디버깅 2주 (총 5-6주)
- [ ] 초기 에러율: 대개 20-30% (통신 포맷 불일치), 1주일 내 <5%로 개선

## 7) Fill-in Checklist

### 계층별 역할 명확화
- [ ] Prometheus: 목표 설정, 전략적 결정
  - 정의: ____
- [ ] Atlas: 작업 분해, Worker 할당, 결과 통합
  - 책임 6가지: 분해, 선택, 의존성, 통합, 품질, 에러복구
  - 각 책임별 구현 방법: ____
- [ ] Workers: 단일 작업 실행
  - Worker 유형: __개 (각 유형의 책임)
  - 각 Worker의 입력/출력 형식

### 통신 프로토콜 정의
- [ ] Prometheus → Atlas: 목표 명세 형식
  - 포함 항목: 목표, 제약(constraints), 마감(deadline)
  - 예시: ____
- [ ] Atlas → Workers: 작업 명세 형식
  - 포함 항목: 작업명, 입력, 기대 출력, 사용 가능 도구, 타임아웃
  - 예시: ____
- [ ] Workers → Atlas: 결과 형식
  - 포함 항목: 출력, 신뢰도(confidence), 에러 정보
  - 예시: ____
- [ ] Atlas → Prometheus: 종합 결과 형식
  - 포함 항목: 집계 결과, 권고사항, 미완료 항목
  - 예시: ____

### 에러 복구 전략
- [ ] Worker 타임아웃: 재시도 __회 또는 대체 Worker 사용
- [ ] 결과 파싱 실패: Worker에 재요청 또는 수동 개입
- [ ] 품질 게이트 미달: 재작업 사이클 최대 __회
- [ ] Prometheus 목표 모순: 명확화 요청 후 대기

### Anti-pattern 제거 체크리스트
- [ ] God Atlas: Atlas가 execution work를 직접 수행하지 않는가?
- [ ] Worker Chaining: Workers가 다른 Workers를 호출하지 않는가?
- [ ] Missing Prometheus: 항상 전략 계층이 존재하는가?
- [ ] Over-orchestration: 정말 3-tier 필요한가? (2-tier로는 안 되나?)

### Quality Gate
- [ ] 3계층의 책임이 명확하고 분리되어 있는가?
- [ ] 모든 계층 경계에서 통신 프로토콜이 명시되었는가?
- [ ] 예상 출력 형식이 각 Worker에 명확하게 전달되는가?
- [ ] 에러 복구 경로가 complete한가? (재시도, 폴백, 수동 개입)
- [ ] Anti-pattern이 모두 제거되었는가?
- [ ] 이것이 정말 3-tier 구조가 필요한 문제인가?
