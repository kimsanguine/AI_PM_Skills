# 좋은 예제 — Growth Loop

## 사용자 요청
"우리 문법 검사 에이전트가 시간이 지날수록 더 똑똑해지는 구조를 만들고 싶어. 사용자가 사용할수록 에이전트가 개선되는 루프를 어떻게 설계하면 될까?"

## 승인 이유
- 에이전트 제품의 데이터 수집 및 개선 구조 설계 필요
- 사용 데이터를 어떻게 에이전트 개선으로 전환할지 체계화 필요
- 장기 경쟁력 구축을 위한 데이터 축적 전략 필요

## 예상 처리
1. 루프 유형 판별: Type A (Data Quality Loop) - 가장 강력
2. 루프 강도 평가: 5개 요소(독자성, 속도, 체감, 전환비용, 복합화) 점수화
3. 플라이휠 메커니즘 설계: 데이터 수집 → 처리 → 개선 → 피드백 → 더 많은 사용
4. Anti-loop 식별: Cold Start, Privacy 장벽, 비용 증가, 품질 천장
5. Kickstart 전략: Seed data, Manual override, Transfer learning

## 처리 결과 예시
```
Growth Loop Design: 문법 검사 에이전트

Loop Type: A (Data Quality Loop)
Loop Strength: 20/25 (강한 플라이휠)

Flywheel Mechanics:
- Input: 각 검사 완료 후 사용자 피드백 (맞음/틀림) + implicit 데이터
- Processing: 주 1회 피드백 집계 → 정확도 <80% 패턴 식별
- Output: 해당 규칙 프롬프트 최적화 또는 새 예제 추가
- Feedback: 다음 주 사용자가 "더 정확해졌다" 체감 → 더 많이 사용

6개월 후: 초기 정확도 70% → 90% (경쟁사는 85%)
```
