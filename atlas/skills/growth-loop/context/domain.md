# 도메인 컨텍스트 — Growth Loop

## 1) Domain Scope
에이전트 제품의 **데이터 플라이휠 설계** — 사용이 데이터를 만들고, 데이터가 에이전트를 개선하고, 개선이 더 많은 사용을 만드는 자기 강화 루프.
- 포함: Loop Type 판별 (A/B/C/D), Loop Strength 평가, Flywheel Mechanics, Anti-loop 식별, Cold Start 전략
- 제외: 데이터 인프라 구축, 구체적 머신러닝 모델 훈련, GTM 전략

## 2) Primary Users
- **제품 경영자**: 데이터 플라이휠 기반 장기 경쟁력 설계
- **데이터 과학자**: 수집할 데이터 유형, 처리 파이프라인 정의
- **초기 창업팀**: Cold Start 문제 해결, 초기 모멘텀 확보

## 3) Required Inputs
- 에이전트의 기본 가치 제안 (어떤 문제를 해결하는가)
- 예상 사용 패턴:
  - 월간 사용량
  - 사용자당 평균 요청 수
  - 데이터 수집 방법 (implicit/explicit)
- 개선 목표:
  - 현재 성능 vs 목표 성능
  - 개선 주기 (주/월)
- 초기 고객 예측 (또는 부재 시 cold start 전략)

## 4) Output Contract
- **Loop Type 판별**: A (Data Quality), B (Content), C (Network), D (TK Accumulation) 중 선택
- **Loop Strength**: 1-25점 평가 (20+ = 방어 가능한 해자)
- **Flywheel Mechanics**: Input → Processing → Output → Feedback 각 단계 명시
- **Anti-loop 식별**: 5가지 위험 (Data Decay, Privacy, Cost, Quality Ceiling, Cold Start) 체크
- **Kickstart 전략**: Cold Start 해결 방법 구체화
- **Timeline**: 루프가 자가 지속하기까지 예상 기간

## 5) Guardrails
- 플라이휠 설계 없이 "자동으로 개선되겠지" 가정 금지
- 데이터 수집 방법 없이 루프 시작 불가능
- Anti-loop 위험 5가지를 모두 검토해야 함
- Cold Start 전략 없으면 초기 데이터 부족으로 루프 시작 불가능
- Loop Strength <15점이면 실제 방어 가능한 해자 아닐 수 있음

## 6) Working Facts (TO BE UPDATED by reviewer)
- [ ] Type A (Data Quality Loop) 구축 시간: 평균 3-6개월
- [ ] Loop Strength 20점 이상 달성률: 약 30-40% (대부분 12-18점)
- [ ] Cold Start 문제: 초기 사용자 <100이면 자동 루프 시작 불가능
- [ ] Anti-loop 중 Privacy 장벽이 가장 높음: 규제 산업 75%, 일반 산업 20-30%
- [ ] Data Decay: 트렌드 변화 많은 도메인 (패션, 뉴스) 7-10일, 안정적 도메인 30-60일

## 7) Fill-in Checklist

### Loop Type 판별
- [ ] Type A (Data Quality): 사용량 → 데이터 축적 → 품질 개선
- [ ] Type B (Content): 사용량 → 콘텐츠 생성 → 새 유저 유입
- [ ] Type C (Network): 유저 증가 → 네트워크 가치 상승
- [ ] Type D (TK Accumulation): 판단 경험 → TK 추출 → 인스트럭션 개선

### Loop Strength 평가
- [ ] 데이터 독자성 (1-5): 경쟁사가 얻을 수 없는 데이터인가?
- [ ] 개선 속도 (1-5): 데이터 → 개선까지 걸리는 시간
- [ ] 사용자 체감 (1-5): 유저가 개선을 인식하는가?
- [ ] 전환 비용 (1-5): 데이터 축적으로 이탈이 어려워지는가?
- [ ] 복합화 (1-5): 시간이 지날수록 격차가 벌어지는가?
- [ ] 총점: ___ / 25

### Flywheel Mechanics 설계
- [ ] Input: 데이터 수집 방법 (implicit/explicit/hybrid) 명시
- [ ] Processing: 데이터 → 개선 변환 방법 (프롬프트/파인튜닝/RAG)
- [ ] Output: 품질 측정 지표 (정확도/속도/관련성)
- [ ] Feedback: 사용자가 개선을 체감하는 트리거

### Anti-loop 위험 식별
- [ ] Data Decay: 시간 경과에 따른 데이터 유효성 감소 여부
- [ ] Privacy Barrier: 사용자 데이터 수집 거부 가능성
- [ ] Cost Escalation: 데이터 처리 비용 > 개선 가치 여부
- [ ] Quality Ceiling: 일정 수준 이상 개선 불가능 여부
- [ ] Cold Start: 초기 데이터 부족 위험

### Cold Start 전략
- [ ] Seed Data: 초기 데이터 확보 방법
- [ ] Manual Override: 사람이 채우는 부분
- [ ] Transfer Learning: 유사 도메인 데이터 활용
- [ ] TK Injection: 전문가 암묵지 활용

### Quality Gate
- [ ] Loop Type이 명확하고 증거 기반인가?
- [ ] Loop Strength 총점이 명시되었는가?
- [ ] Flywheel Mechanics 4단계가 모두 구체적인가?
- [ ] Anti-loop 5가지 위험이 모두 검토되었는가?
- [ ] Cold Start 전략이 최소 2개 이상 준비되었는가?
- [ ] 루프가 자가 지속하기까지 예상 기간이 정의되었는가?
