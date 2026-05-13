# 가중치 튜닝 가이드

## 디폴트 가중치 (합 100)

| 축 | 디폴트 | 의미 |
|---|---|---|
| Accuracy | 25 | 출력 품질 |
| Reliability | 25 | 운영 안정 |
| Cost | 20 | 단가 |
| Velocity | 15 | 처리량 |
| Satisfaction | 15 | 유저 만족 |

## 사업 컨텍스트별 추천 프리셋

### 비용 민감 (스타트업 초기)
```
Accuracy 20 / Reliability 20 / Cost 35 / Velocity 10 / Satisfaction 15
```

### 고객 직접 노출 (B2C 핵심)
```
Accuracy 25 / Reliability 30 / Cost 10 / Velocity 15 / Satisfaction 20
```

### 내부 자동화 (사내 효율)
```
Accuracy 20 / Reliability 30 / Cost 25 / Velocity 20 / Satisfaction 5
```

### R&D / 실험 단계
```
Accuracy 35 / Reliability 15 / Cost 10 / Velocity 30 / Satisfaction 10
```

## 튜닝 원칙

1. **합은 항상 100** — 자동 정규화 권장
2. **변경 사유를 기록** — `decision-log` (hplan 플러그인)에 등록
3. **분기 단위로 재검토** — 사업 단계가 바뀌면 프리셋 재선택
4. **에이전트 그룹별 다른 가중치 가능** — T1과 T4가 같은 가중치일 필요 없음
