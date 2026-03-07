---
name: incident
description: "Respond to and learn from AI agent incidents — triage severity, coordinate response, contain blast radius, and write postmortems. Use when an agent produces harmful outputs, costs spike unexpectedly, accuracy drops suddenly, or users report critical failures."
argument-hint: "[incident description or agent name]"
---

# Agent Incident Response

> 에이전트 장애 대응 프로토콜 — 발견, 분류, 대응, 복구, 학습

## 개념

에이전트 장애는 일반 소프트웨어 장애와 다르다. "서버가 죽었다"는 명확하지만, "에이전트가 환각으로 잘못된 답을 줬다"는 발견 자체가 어렵다. 침묵의 실패(Silent Failure)가 에이전트 장애의 가장 위험한 유형이다.

## Instructions

You are running **incident response** for: **$ARGUMENTS**

### Step 1 — Incident Detection & Classification

```
발견 시각: [timestamp]
발견 방법:
  □ 자동 모니터링 알림
  □ 사용자 신고
  □ 내부 QA 발견
  □ 비용 이상 감지
  □ 외부 보고 (SNS, 언론)
```

**Severity Classification:**

| SEV | 정의 | 예시 | 대응 시간 |
|-----|------|------|----------|
| **SEV-1** | 전체 서비스 중단 또는 데이터 유출 | 에이전트가 PII를 외부에 노출 | 15분 이내 |
| **SEV-2** | 핵심 기능 장애, 다수 유저 영향 | 정확도 50% 이하로 급락, 비용 10배 폭등 | 1시간 이내 |
| **SEV-3** | 일부 기능 저하, 소수 유저 영향 | 특정 입력에서 환각 반복 | 4시간 이내 |
| **SEV-4** | 경미한 품질 저하, 우회 가능 | 응답 속도 저하, 포맷 깨짐 | 24시간 이내 |

### Step 2 — Immediate Response

**에이전트 장애 유형별 긴급 대응:**

```
🔴 환각/오정보 장애:
  1. 해당 에이전트 기능 즉시 비활성화
  2. 영향 범위 확인 (몇 명이 잘못된 정보를 받았는가?)
  3. 영향받은 유저에게 정정 통보
  4. 원인 분석 (프롬프트 문제? 모델 변경? 입력 데이터 오염?)

🔴 비용 폭등 장애:
  1. API 호출 rate limit 즉시 설정
  2. 비용 발생 원인 추적 (무한 루프? 토큰 폭발? 잘못된 모델 라우팅?)
  3. 비용 캡 설정
  4. 영향받은 기간의 비용 산출

🔴 데이터 유출 장애:
  1. 에이전트 즉시 중단
  2. 유출 범위 파악 (어떤 데이터, 누구에게, 어디로)
  3. 법무팀 즉시 통보
  4. 규제 보고 필요 여부 판단 (GDPR, 개인정보보호법)

🔴 연쇄 실패 장애 (멀티에이전트):
  1. 오케스트레이터 에이전트 중단
  2. 하위 에이전트 상태 확인
  3. 실패 전파 경로 추적
  4. 격리 후 개별 에이전트 순차 재시작
```

### Step 3 — Blast Radius Assessment

```
영향 범위:
  유저 수: [N]명
  기간: [start] ~ [end]
  데이터 영향: [none / read / write / delete]
  비용 영향: $[amount]
  평판 영향: [none / internal only / external / media]

영향받은 시스템:
  □ 에이전트 자체
  □ 연동 API/서비스
  □ 데이터 저장소
  □ 하위 에이전트 (멀티에이전트)
  □ 사용자 데이터
```

### Step 4 — Recovery

```
단기 복구:
  ├── Rollback: 이전 안정 버전으로 복구 [Y/N]
  ├── Hotfix: 긴급 수정 배포 [내용]
  ├── Workaround: 임시 우회 방법 [내용]
  └── Communication: 유저/이해관계자 통보 [완료 여부]

장기 복구:
  ├── Root Cause Fix: 근본 원인 해결 [계획]
  ├── Monitoring: 재발 감지 알림 추가 [내용]
  ├── Testing: 회귀 테스트 추가 [내용]
  └── TK Extraction: 이 장애에서 배운 판단 기준 → TK로 추출
```

### Step 5 — Postmortem

```
Postmortem: [incident title]
Date: [date]
Severity: [SEV-1/2/3/4]
Duration: [detection] ~ [recovery] = [N]시간

Timeline:
  [T+0]  [발견]
  [T+Nm] [1차 대응]
  [T+Nh] [원인 파악]
  [T+Nh] [복구 완료]

Root Cause:
  [근본 원인 — "5 Whys" 적용]
  1. Why: [direct cause]
  2. Why: [underlying cause]
  3. Why: [systemic cause]
  4. Why: [process gap]
  5. Why: [cultural/structural root]

What Went Well:
  - [잘 대응한 것]

What Went Wrong:
  - [개선할 것]

Action Items:
  □ [action 1] — Owner: [name] — Due: [date]
  □ [action 2] — Owner: [name] — Due: [date]
  □ [action 3] — Owner: [name] — Due: [date]

TK Extracted:
  TK-[NNN]: [이 장애에서 추출한 암묵지]
```

### Output

```
Incident Report: [title]
──────────────────────────
Severity: [SEV-N]
Status: [Active / Mitigated / Resolved]
Blast Radius: [N] users, $[cost], [duration]
Root Cause: [one-line]
Recovery: [rollback / hotfix / workaround]
Action Items: [N] items, [N] completed
TK Extracted: [TK-NNN title]
```

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- 에이전트 장애 유형 분류: AI Dubbing/Avatar 운영 장애 대응 경험 기반
- Silent Failure 패턴: 환각이 "그럴듯한 답"이라 유저가 장애를 인지 못 하는 케이스
- premortem 스킬과 상호 보완 (사전 예방 vs 사후 대응)

---

## Further Reading
- Google SRE Book, "Managing Incidents" — Incident response process and postmortem culture
- Anthropic, "Building Effective Agents" (2024) — Agent error handling and recovery patterns
