---
name: failure-mode-analysis
description: "Identify, classify, and prioritize failure modes specific to AI agents. Uses a 4-category taxonomy: Technical, Prompt, Data, and Operational failures. Use when debugging a malfunctioning agent, conducting a post-mortem, or proactively stress-testing an agent design."
---

## Agent Failure Mode Analysis

에이전트 실패는 4가지 근본 원인으로 분류됩니다:

```
Technical   → 코드/인프라/API 문제
Prompt      → 지시/프롬프트 설계 문제
Data        → 입력 데이터 품질 문제
Operational → 운영/스케줄/환경 문제
```

실패 원인을 정확히 분류해야 올바른 해결책을 찾을 수 있습니다.  
원인을 잘못 판단하면 수정해도 실패가 반복됩니다.

---

### 4가지 실패 범주

**Category 1 — Technical Failures**

| 실패 유형 | 증상 | 원인 | 해결 |
|---|---|---|---|
| API 오류 | HTTPError, 429 | Rate limit, 서버 오류 | 재시도 로직, 지수 백오프 |
| 타임아웃 | 실행 중단 | 응답 지연, 무한 루프 | 타임아웃 설정, 루프 탈출 조건 |
| 메모리 오류 | 컨텍스트 초과 | 파일 과다 로드 | 컨텍스트 예산 계획 |
| 환경 오류 | 파일 없음, 권한 없음 | 경로 오류, 권한 문제 | 경로 검증, 권한 확인 |
| 모델 쿨다운 | "Provider in cooldown" | 동시 요청 초과 | 스케줄 분산, 재시도 간격 |

---

**Category 2 — Prompt Failures**

| 실패 유형 | 증상 | 원인 | 해결 |
|---|---|---|---|
| 지시 오해 | 엉뚱한 출력 | 모호한 지시 | CRISP 프레임워크 적용 |
| 포맷 불일치 | 파싱 실패 | 출력 형식 미명시 | 출력 형식 명시 + 예시 |
| Anti-Goals 위반 | 금지된 행동 수행 | Anti-Goals 누락 | Anti-Goals 명시 |
| 과도한 추론 | 느린 응답, 비용 급증 | 불필요한 CoT | 직접 지시로 전환 |
| 언어/톤 불일치 | 영어 출력, 격식체 | 언어/톤 미명시 | 언어와 톤 명시 |

---

**Category 3 — Data Failures**

| 실패 유형 | 증상 | 원인 | 해결 |
|---|---|---|---|
| 빈 입력 | 빈 출력 또는 오류 | 데이터 소스 없음 | 빈 케이스 처리 로직 |
| 오래된 데이터 | 틀린 정보 생성 | 캐시/파일 미업데이트 | 데이터 freshness 체크 |
| 인코딩 오류 | 깨진 문자 | 한글 등 비ASCII | UTF-8 명시 처리 |
| 구조 변경 | 파싱 실패 | API 응답 형식 변경 | 방어적 파싱, 버전 고정 |
| 노이즈 데이터 | 품질 저하 | 필터링 부재 | 블랙리스트/화이트리스트 |

---

**Category 4 — Operational Failures**

| 실패 유형 | 증상 | 원인 | 해결 |
|---|---|---|---|
| 스케줄 충돌 | 연쇄 API 쿨다운 | 동시 실행 | 10분 간격 분산 |
| 환경 변수 누락 | 인증 실패 | 키 미설정 | 환경 변수 체크리스트 |
| 채널 전달 실패 | "delivery failed" | Telegram 연결 오류 | 채널 직접 명시 (chatId) |
| 모델 미허용 | "model not allowed" | 허용 목록 미설정 | openclaw.json 업데이트 |
| 디스크 가득 | 파일 쓰기 실패 | 로그/메모리 파일 누적 | 주기적 정리 크론 |

---

### 실패 우선순위 매트릭스

```
          발생 빈도
           낮음 → 높음
영  높음  │  대비   │  즉시   │
향        │  계획   │  해결   │
도  낮음  │  무시   │  모니터 │
```

Priority Score = 발생 빈도(1-5) × 영향도(1-5)

---

### Post-Mortem 템플릿

실패 발생 후 기록:

```
발생일시:
에이전트:
증상:

근본 원인 분류:
☐ Technical  ☐ Prompt  ☐ Data  ☐ Operational

상세 원인:

재현 조건:

해결 방법:

재발 방지 조치:

교훈 (MEMORY.md 저장 여부): Y/N
```

---

### 사용 방법

`/failure-mode-analysis [에이전트 이름 또는 증상]`

---

### Instructions

You are analyzing failure modes for: **$ARGUMENTS**

**Step 1** — 증상 수집  
현재 발생하는 문제 또는 우려되는 실패 시나리오 나열

**Step 2** — 4범주 분류  
각 증상/시나리오를 Technical/Prompt/Data/Operational 분류

**Step 3** — 우선순위 매트릭스  
발생 빈도 × 영향도 점수화 → Top 3 선정

**Step 4** — 근본 원인 분석  
Top 3 각각에 대해 "왜" 5번 반복 (5 Whys)

**Step 5** — 해결 방안 제시  
구체적이고 즉시 실행 가능한 해결책

**Step 6** — Post-Mortem 기록  
발생한 실패라면 템플릿에 기록 + MEMORY.md 저장 여부 판단

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- Operational 실패 패턴: MEMORY.md system_pattern 기반 (2026-02~03 운영 경험)
- "cron announce delivery failed" 오탐 패턴 포함
- 5 Whys: Toyota Production System 방법론 적용
