# 좋은 예제 — 3-Tier Pattern

## 사용자 요청
"우리가 분기별 경쟁사 분석 리포트를 만드는 복잡한 프로젝트를 에이전트 3개가 협력해서 하는데, 전략 수립, 작업 분배, 실행, 통합을 어떻게 구조화하면 좋을까?"

## 승인 이유
- 3개 이상의 에이전트가 협력해야 하는 복잡한 시스템
- 전략적 목표(Prometheus)와 실행(Workers) 사이의 조율 필요
- 에이전트 간 데이터 흐름, 에러 처리, 품질 관리 체계화 필요

## 예상 처리
1. 계층 구조 매핑: Prometheus(전략) → Atlas(조율) → Workers(실행)
2. 통신 프로토콜 정의: 각 경계에서의 입출력 형식
3. Atlas 설계: 작업 분해, Worker 할당, 의존성 관리, 결과 통합, 품질 게이트, 에러 복구
4. Worker 설계: 단일 책임, 구조화된 출력, 실패 처리
5. Anti-pattern 제거: God Atlas, Worker Chaining, Missing Prometheus 등

## 처리 결과 예시
```
3-Tier 설계: 분기 경쟁사 분석

[Prometheus] 전략팀
  목표: "5개 경쟁사의 가격/기능/GTM 분석"
  제약: "각 3시간, 마감 2026-03-14"
         ↓
[Atlas] 조율 에이전트
  - Task 1: Competitor A,B,C 병렬 리서치
  - Task 2: 기능 비교 매트릭스
  - Task 3: GTM 패턴 분석
  - Task 4: 결과 통합 및 리포트
         ↓
[Workers]
  - Scraper Worker (웹 데이터)
  - Analysis Worker (패턴 인식)
  - Report Worker (마크다운)
```
