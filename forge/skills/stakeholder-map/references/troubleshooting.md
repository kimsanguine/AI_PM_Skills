# Troubleshooting — Stakeholder Map

## 1) 이해관계자 식별이 불완전 (주요 팀 누락)

- **증상**: 이해관계자 4-5명만 식별되고, Legal/Finance/Operations 등 주요 팀이 빠짐
- **확인**:
  - 식별된 이해관계자 수가 6개 그룹 미만인가?
  - 에이전트 도입에 영향을 받는 팀 (특히 규제/비용/운영)이 모두 포함되었는가?
- **조치**:
  1. "이 에이전트가 영향을 주는 모든 팀을 생각해보세요" 재질문
  2. 체크리스트 제시: "경영진 ☐ 직접사용자 ☐ 엔지니어링 ☐ 법무 ☐ 운영/CS ☐ 재무 ☐ (기타)"
  3. 누락된 팀 3-4개를 추가로 식별할 때까지 진행 안 함

---

## 2) Power-Interest 배치 기준 모호 (모두 "High Power + High Interest"로 표시)

- **증상**: 모든 이해관계자가 "Engage Actively" 사분면에 배치 → 실제로는 우선순위 구분 불가
- **확인**:
  - Power와 Interest가 각각 1-5점으로 명시되어 있는가?
  - 실제로 이 이해관계자가 에이전트 도입 결정에 절대권(Power 5)을 갖는가?
- **조치**:
  1. Power의 정의 재설명: "도입/중단을 결정할 수 있는 정도" (1=의견만, 5=절대권)
  2. Interest의 정의 재설명: "도입 결과에 관심 있는 정도" (1=무관심, 5=매우 높음)
  3. 각 이해관계자별로 명시적으로 점수 재평가 요청 (예: "CEO는 Power 5, Interest 5" vs "Intern은 Power 1, Interest 2")

---

## 3) 저항 유형이 추상적이고 대응 전략이 실행 불가능

- **증상**:
  - 저항 유형: "사람들이 새 도구를 싫어할 수 있음"
  - 대응: "좋은 커뮤니케이션을 하세요"
  - 실제 실행 방법 불명확
- **확인**:
  - 각 저항 유형이 구체적인가? (예: "Job Threat" vs "일반적 거부")
  - 대응 전략이 actionable(실행 가능)한가? (예: "3주 Shadow Mode → 99% 정확도 검증" vs "설득하기")
- **조치**:
  1. 저항 유형을 "누가 왜 저항하는가"로 재정의:
     ```
     ❌ "신뢰 부족"
     ✅ "Trust Deficit (Accounting): 과거 자동화 도구 실패 경험 → AI도 실패할까봐"
     ```
  2. 각 저항별 구체적 3단계 대응 전략 수립:
     ```
     Step 1: Shadow Mode로 3주 검증
     Step 2: "AI vs 수동 결과 99% 일치" 데이터 공개
     Step 3: 공식 도입 → 월 1회 정확도 리포트
     ```

---

## 4) Champion 선정은 했지만 동기가 실제 pain point와 일치하지 않음

- **증상**:
  - Champion: "PM 담당자 (user)"
  - 동기: "도구를 써보고 싶다"
  - 실제: PM 담당자는 큰 pain point가 없고 관심 낮음
- **확인**:
  - Champion이 실제로 가장 큰 pain을 겪고 있는가?
  - 에이전트가 그 pain을 실제로 해결하는가?
  - Champion의 동기가 자발적인가, 강제된 것은 아닌가?
- **조치**:
  1. Champion 재선정 가이드: "가장 큰 pain을 겪는 사람"을 먼저 식별
  2. 에이전트가 그 pain을 해결하는지 검증: "현재 매월 10시간 소요 → 에이전트로 1시간으로 단축 가능?"
  3. Champion이 "의무적" 느낌이면 다른 champion 찾기

---

## 5) 커뮤니케이션 계획이 일관성 없음 (이해관계자별 메시지 상충)

- **증상**:
  - CFO에게: "비용 50% 절감"
  - Accounting에게: "현재 업무는 그대로, 단순히 데이터 검증만"
  - 이 둘이 모순됨 → 비용 절감 = 일부 인력 재배치 가능성
- **확인**: 모든 이해관계자에게 전달된 메시지가 일관되는가? 상충되는 약속은 없는가?
- **조치**:
  1. 커뮤니케이션 계획 초안 작성 후 모든 이해관계자 대표 1명씩과 사전 검토 미팅
  2. "일관성 체크: CFO와 Accounting 양쪽과 이야기했을 때 메시지가 충돌하지 않는가?" 질문
  3. 필요하면 메시지 재구성 (예: CFO에게는 "비용 효율성", Accounting에게는 "정확도 향상 + 업무 시간 단축")

---

## 6) Go/No-Go Confidence가 근거 없이 High 또는 너무 Low

- **증상**:
  - Go/No-Go: "High"
  - 하지만 Blocker (Legal)가 "Manage Closely"이고 AI 규제 검토는 미완료
  - 또는 "Low"인데 실제로는 champion이 강하고 CEO 지지가 명확
- **확인**:
  - Blocker가 있는가? (High Power + 저항이 강함)
  - 각 Blocker별 명확한 mitigation 계획이 있는가?
  - Champion의 강도와 CFO 지지 수준은?
- **조치**:
  1. Go/No-Go 결정 기준 명시:
     ```
     HIGH: Champion 강함 (Power/Interest 모두 4+) + CEO 명확한 지지 + Blocker 미완료 항목 <1개
     MEDIUM: Champion 있음 + 주요 Blocker 1개 (Legal/Finance) + Mitigation 계획 진행 중
     LOW: Blocker 다수 or Champion 약함 + CEO 신중함 → 설득 단계 필요
     ```
  2. Confidence 수정: "High는 아니고 Medium입니다. 이유: Legal 합의 필요 + Mitigation 계획 준비 중"

