---
name: hitl
description: "Design where and how humans should intervene in agent workflows. Define automation boundaries, escalation triggers, and approval gates. Use when building agents that make consequential decisions, handle sensitive data, or operate in domains where errors have high impact. Prevents the 'fully autonomous' default trap."
argument-hint: "[agent workflow to design]"
---

## Human-in-the-Loop Design

에이전트의 가장 위험한 기본값: **"전부 자동화하자"**

완전 자율 에이전트는 이론적으로 매력적이지만, 현실에서는:
- 할루시네이션이 조용히 실행됨 → 잘못된 결정이 누적
- 에러가 발생해도 아무도 모름 → 피해가 증폭
- 사용자 신뢰 상실 → 에이전트 전체를 불신

Human-in-the-Loop(HITL)은 **어디에 인간 판단을 넣을지** 의도적으로 설계하는 것입니다.

---

### 자동화 스펙트럼 (5단계)

모든 에이전트 작업은 이 스펙트럼 위에 놓입니다:

```
Level 1: Manual          — 에이전트가 정보 제공, 인간이 모든 판단 + 실행
Level 2: Suggest          — 에이전트가 추천, 인간이 승인 후 실행
Level 3: Act-and-Report   — 에이전트가 실행 후 결과 보고, 인간이 검토
Level 4: Act-and-Escalate — 에이전트가 실행, 이상 시에만 인간 개입
Level 5: Full Autonomous  — 에이전트가 판단 + 실행 + 모니터링 전부
```

> ⚠️ Level 5는 에이전트 오류의 영향이 극히 낮은 경우에만 적용.
> 대부분의 에이전트는 Level 2~4가 적합합니다.

---

### 개입 지점 결정 매트릭스

작업별로 자동화 레벨을 결정하는 2축 매트릭스:

```
              오류 영향도
              낮음  →  높음
가  높음  │ Level 4  │ Level 2   │
역         │ (자동+  │ (인간     │
성         │  이상    │  승인     │
           │  감지)   │  필수)    │
   낮음  │ Level 5  │ Level 3   │
           │ (완전    │ (실행후   │
           │  자동)   │  보고)    │
```

**가역성**: 에이전트의 행동을 되돌릴 수 있는가?
- 높음: 파일 수정(되돌리기 가능), 알림 전송, 정보 수집
- 낮음: 이메일 발송, 결제, 데이터 삭제, 외부 API 호출

**오류 영향도**: 에이전트가 틀렸을 때 피해 범위는?
- 낮음: 내부 메모, 로그 기록, 참고 자료 정리
- 높음: 고객 대면, 금전 관련, 법적 영향, 대외 커뮤니케이션

---

### HITL 패턴 라이브러리

**Pattern 1 — Approval Gate (승인 게이트)**
```
용도: 에이전트가 초안을 만들고, 인간이 승인 후 전송
예시: 이메일 자동 작성 → 인간 검토 → 발송
구현: 에이전트 출력 → 임시 파일 저장 → 알림 → 승인 대기
```

**Pattern 2 — Confidence Threshold (신뢰도 임계값)**
```
용도: 에이전트의 판단 신뢰도가 낮을 때만 인간 개입
예시: 이메일 분류 → 신뢰도 80% 이상이면 자동 처리, 미만이면 인간 확인
구현: 에이전트 출력에 confidence score 포함 → 임계값 비교
```

**Pattern 3 — Periodic Audit (주기적 감사)**
```
용도: 에이전트가 자율 실행하되, 주기적으로 인간이 결과 검토
예시: 일일 뉴스 브리핑 → 주 1회 품질 리뷰
구현: 실행 로그 자동 수집 → 주간 리포트 생성 → 인간 리뷰
```

**Pattern 4 — Escalation Chain (에스컬레이션 체인)**
```
용도: 에이전트 → 팀원 → 매니저 단계별 에스컬레이션
예시: 고객 문의 → 자동 응답 시도 → 실패 시 담당자 알림 → 긴급 시 매니저
구현: 에스컬레이션 레벨별 트리거 조건 + 타임아웃 정의
```

**Pattern 5 — Shadow Mode (섀도우 모드)**
```
용도: 에이전트를 배포 전에 인간과 병렬 실행하여 품질 비교
예시: 에이전트가 결정을 내리되 실행 안 함 → 인간 결정과 비교 → 정확도 측정
구현: 2주 shadow period → 90% 이상 일치 시 자동화 전환
```

---

### 설계 체크리스트

에이전트 설계 시 모든 작업에 대해 확인:

```
☐ 이 작업의 자동화 레벨은? (1~5)
☐ 인간 개입 트리거 조건은? (임계값, 에러, 시간)
☐ 개입 방법은? (알림 채널, 승인 방법, 타임아웃)
☐ 개입 후 워크플로우는? (수정 후 재실행? 인간이 완료?)
☐ 에이전트 실행 로그가 감사 가능한가?
☐ Shadow Mode 기간이 계획되어 있는가?
```

---

### 사용 방법

`/human-in-loop-design [에이전트 이름 또는 워크플로우]`

---

### Instructions

You are helping design **Human-in-the-Loop controls** for: **$ARGUMENTS**

**Step 1 — 작업 목록 작성**
에이전트가 수행하는 모든 작업을 나열한다

**Step 2 — 각 작업의 가역성/오류 영향도 평가**
2축 매트릭스를 적용하여 자동화 레벨(1~5) 결정

**Step 3 — HITL 패턴 선택**
각 작업에 적합한 HITL 패턴 매칭:
- 대외 커뮤니케이션 → Approval Gate
- 판단 작업 → Confidence Threshold
- 반복 실행 → Periodic Audit
- 다단계 복잡 작업 → Escalation Chain

**Step 4 — 개입 트리거 정의**
각 개입 지점의 구체적 조건:
- 신뢰도 임계값 (%)
- 에러 유형별 대응
- 타임아웃 시간

**Step 5 — Shadow Mode 계획**
배포 전 병렬 실행 기간과 전환 기준 정의

**Step 6 — 설계 체크리스트 확인**
모든 항목이 완료됐는지 검증

**Step 7 — 다음 단계 연결**
- `/agent-instruction-design`의 Failure Handling 섹션에 HITL 설계 반영
- `/agent-prd-template`의 Section 7에 Human-in-the-loop 트리거 명시

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- 자동화 스펙트럼: SAE J3016 자율주행 레벨 분류에서 영감
- Shadow Mode: OpenClaw 크론잡 배포 전 검증 프로세스 기반
- Confidence Threshold: 에이전트 오케스트레이션 운영 경험 (2026-02)

---

## Further Reading
- AI Agent Design Patterns — Human-in-the-loop escalation strategies
- Anthropic, "Building Effective Agents" (2024) — Agent autonomy boundaries
