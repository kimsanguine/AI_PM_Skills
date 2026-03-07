---
name: pm-engine
description: "Interface with the PM-ENGINE-MEMORY file — the operator's accumulated PM tacit knowledge database. Enables agents to reference, search, and apply TK (Tacit Knowledge) entries, and supports the conversion pipeline from TK units to agent instructions. The core of the pm-engine competitive moat."
argument-hint: "[TK query or operation]"
---

## PM-ENGINE-MEMORY Interface

PM-ENGINE-MEMORY는 pm-engine의 심장입니다.

### TK-NNN이란?

**TK** = Tacit Knowledge (암묵지)
**NNN** = **Never-ending Nuance Network** — 끝없이 쌓이는 뉘앙스의 네트워크

번호는 TK-001부터 TK-999까지. 매일 1개씩 축적하면 약 3년 — 그 시점에 에이전트는 PM의 분신이 됩니다. 각 TK는 고립된 지식이 아니라 🔗 연관 TK로 연결된 **지식 그래프**를 형성합니다. TK가 10개일 때는 개별 판단 기준이지만, 100개를 넘으면 TK 간 조합이 만드는 복합 판단이 시작됩니다.

구조:
```
PM-ENGINE-MEMORY.md
├── TK-001: 긴급 요청 우선순위 판단
├── TK-002: AI 네이티브 사고 필터
├── ...
└── TK-999: [999번째 암묵지 — PM 분신 완성]
```

이 파일이 특별한 이유:
- 일반 LLM 지식: 인터넷의 평균
- PM-ENGINE-MEMORY: PM의 실전 경험에서 검증된 판단 기준

TK가 쌓일수록 에이전트의 판단 품질이 올라갑니다.
이것이 복제 불가능한 Domain TK 해자의 실체입니다.

---

### TK → Instruction 변환 파이프라인

```
1일 1프롬프트 크론
        ↓
PM 판단 경험 기록
        ↓
/pm-tacit-extract
        ↓
TK-NNN 구조화
        ↓
PM-ENGINE-MEMORY.md append
        ↓
/tk-to-instruction
        ↓
에이전트 System Prompt 업데이트
        ↓
더 나은 판단을 하는 에이전트
```

---

### TK 참조 방법

에이전트가 PM-ENGINE-MEMORY를 활용하는 2가지 방식:

**방식 1 — 직접 로드 (소규모 TK)**
```
[System Prompt에 포함]
다음 PM 판단 기준을 참고하세요:
<pm-engine-memory>
TK-001: [내용]
TK-003: [내용]
</pm-engine-memory>
```

**방식 2 — 동적 검색 (대규모 TK)**
```
[실행 중]
memory_search("현재 상황과 관련된 PM 판단 기준")
→ 관련 TK 1~3개 반환
→ 컨텍스트에 삽입
→ 판단에 활용
```

Contextual Retrieval (CR) 패턴:
- TK마다 🟢 활성화 조건이 있음
- 현재 상황 → 활성화 조건 매칭 → 관련 TK만 로드
- 전체 파일 로드 없이 정확한 TK만 참조

---

### PM-ENGINE-MEMORY Seed Library (TK-001 ~ TK-010)

아래는 AI 에이전트 제품을 만드는 PM이 축적할 수 있는 시드 TK입니다.
`/extract` 커맨드로 자신의 경험에서 TK-011부터 계속 추가하세요.

---

#### TK-001: 긴급 요청 우선순위 판단

📌 패턴:
"긴급"이라는 표현의 80%는 가짜 긴급. 실제 마감일과 비즈니스 임팩트로만 판단한다.

🟢 활성화 조건: 에이전트가 작업 우선순위를 결정할 때
🔴 비활성화 조건: 실제 SLA가 걸린 장애 대응 상황
💡 Why: 요청자의 압박감과 실제 긴급도는 다르다. 감정이 아닌 임팩트로 판단해야 진짜 중요한 일에 집중 가능.
🔗 연관 TK: TK-004, TK-009

---

#### TK-002: AI 네이티브 사고 필터

📌 패턴:
새 기능을 기획할 때 "사람이 꼭 해야 하나?"를 먼저 질문한다. AI가 80% 정확도로 처리 가능하면 AI에게 맡기고, 사람은 예외 처리와 최종 판단에 집중.

🟢 활성화 조건: 신규 기능 기획, 워크플로우 설계, 업무 자동화 검토 시
🔴 비활성화 조건: 법적 책임이 수반되는 의사결정 (의료, 법률, 금융 규제)
💡 Why: 디폴트를 "사람이 한다"에서 "AI가 한다"로 바꾸면 제품 설계의 출발점이 달라진다. 80%면 충분한 영역이 놀랍게 많다.
🔗 연관 TK: TK-006, TK-007

---

#### TK-003: 에이전트 비용 10배 법칙

📌 패턴:
POC에서 비용 검증 안 하면 스케일에서 죽는다. 유저 10배 = 토큰 비용 10배. 월 $500 POC도 100명이면 $50K.

🟢 활성화 조건: 에이전트 신규 개발, cost-sim 실행, 스케일 플랜 수립 시
🔴 비활성화 조건: 내부 도구(유저 1~5명 고정)로 비용 임계값이 낮을 때
💡 Why: LLM API 비용은 선형 스케일링. SaaS처럼 "유저 늘면 한계비용 제로"가 아니다. 만들기 전에 모델링하지 않으면 출시 후 좌초.
🔗 연관 TK: TK-007, TK-010

---

#### TK-004: 데이터 없으면 가설이다

📌 패턴:
감으로 내린 결정은 "가설"로 표기한다. 2주 내 데이터 검증 안 되면 자동 폐기. 감 ≠ 의사결정.

🟢 활성화 조건: 제품 방향 결정, 기능 우선순위 토론, OKR 설정 시
🔴 비활성화 조건: 탐색 단계(Discovery Phase)에서 방향성을 잡는 초기 가설 수립
💡 Why: 경험 많은 PM일수록 감을 확신으로 착각한다. "가설" 태그를 붙이면 검증 의무가 자동으로 따라온다.
🔗 연관 TK: TK-001, TK-005

---

#### TK-005: 첫 유저 3명의 함정

📌 패턴:
초기 유저 3명의 피드백은 극단값이다. 10명까지는 패턴이 아님. 10명 넘어야 "반복되는 문제"로 인정한다.

🟢 활성화 조건: 유저 피드백 분석, 기능 요청 우선순위 판단 시
🔴 비활성화 조건: 보안/데이터 유출 같은 크리티컬 이슈 (1건이라도 즉시 대응)
💡 Why: 얼리어답터는 전체 유저를 대표하지 않는다. 3명이 원한다고 만들면, 100명은 안 쓴다. n=10까지 기다려라.
🔗 연관 TK: TK-004, TK-010

---

#### TK-006: 에이전트 환각은 UX로 해결

📌 패턴:
환각률 0%는 불가능하다. "확인해주세요" UX가 해법. 에이전트 출력에 신뢰도 표시 + 사용자 확인 스텝을 삽입한다.

🟢 활성화 조건: 에이전트 PRD 작성, 인스트럭션 설계, 신뢰성 체계 점검 시
🔴 비활성화 조건: 에이전트가 백엔드에서만 동작하고 사용자 인터페이스가 없을 때
💡 Why: 모델을 고치려 하면 끝이 없다. 대신 "에이전트가 틀릴 수 있다"를 전제로 UX를 설계하면, 환각이 사고가 아닌 확인 요청이 된다.
🔗 연관 TK: TK-002, TK-009

---

#### TK-007: Build vs Buy 2주 법칙

📌 패턴:
직접 만들면 2주 넘게 걸리는가? → Buy 먼저 검토. 2주 이내면 Build. 단, 핵심 차별화 기능은 시간과 무관하게 무조건 Build.

🟢 활성화 조건: 신규 기능 개발 결정, 도구/인프라 선택, 아키텍처 리뷰 시
🔴 비활성화 조건: 이미 깊이 투자한 기술 스택을 교체 검토할 때 (전환 비용 별도 계산 필요)
💡 Why: PM은 "우리가 만들면 더 좋다"는 편향이 있다. 2주 기준을 두면 감정이 아닌 리소스로 판단하게 된다.
🔗 연관 TK: TK-003, TK-008

---

#### TK-008: 경쟁사 카피는 해자가 아님

📌 패턴:
경쟁사 기능을 따라하면 영원히 추격자다. 자체 운영 데이터 + PM 암묵지 축적이 진짜 해자. "GPT-4를 씁니다"는 차별화가 아니다.

🟢 활성화 조건: 경쟁 분석, 전략 리뷰, 로드맵 우선순위 결정 시
🔴 비활성화 조건: Table stakes 기능(없으면 시장 진입 자체가 안 되는 기능) 대응 시
💡 Why: 모든 팀이 같은 LLM을 쓴다. 모델이 아닌, 그 위에 쌓이는 도메인 데이터와 판단 기준(TK)이 진짜 경쟁력.
🔗 연관 TK: TK-002, TK-003

---

#### TK-009: 질문의 품질이 에이전트 품질을 결정

📌 패턴:
에이전트에게 "뭘 하라"보다 "왜 하는지 + 판단 기준"을 주면 결과가 3배 좋아진다. Instruction에 맥락과 판단 근거를 넣어라.

🟢 활성화 조건: 에이전트 인스트럭션 작성, 프롬프트 설계, TK→Instruction 변환 시
🔴 비활성화 조건: 단순 포맷 변환 등 판단이 필요 없는 기계적 작업
💡 Why: LLM은 "왜"를 알면 예외 상황에서도 적절한 판단을 내린다. "뭘"만 알면 규칙에 없는 상황에서 환각한다.
🔗 연관 TK: TK-006, TK-001

---

#### TK-010: 그로스는 리텐션 다음

📌 패턴:
리텐션 없이 acquisition에 투자하면 밑 빠진 독. 에이전트도 마찬가지 — 재사용률(WAU/MAU) 60% 넘기 전에는 신규 기능보다 기존 기능 개선.

🟢 활성화 조건: 그로스 전략 수립, OKR 설정, 마케팅 예산 배분 시
🔴 비활성화 조건: 신규 시장 진입(PMF 탐색 단계)으로 리텐션 데이터 자체가 없을 때
💡 Why: 에이전트 DAU 100명, 재사용 10%면 실질 유저 10명이다. 1000명으로 키워봐야 100명. 리텐션을 먼저 고치면 같은 유저 풀에서 10배 효과.
🔗 연관 TK: TK-003, TK-005

---

### PM-ENGINE-MEMORY 파일 구조

위 TK들은 아래 형식으로 PM-ENGINE-MEMORY.md에 저장됩니다:
```markdown
## TK-NNN: [제목]
📌 패턴: [핵심 판단]
🟢 활성화 조건: [언제 쓰는가]
🔴 비활성화 조건: [언제 안 쓰는가]
💡 Why: [근거]
🔗 연관 TK: [TK-XXX, TK-YYY]
```

---

### tk-to-instruction 변환

TK를 에이전트 Instruction으로 변환하는 방법:

**예시 1 — TK-001: 긴급 요청 우선순위 판단**
```
[변환 전 — TK]
패턴: 긴급해 보이는 요청이 와도 실제 임팩트 먼저 확인.
      실제 마감 없는 '인식된 긴급'은 우선순위에서 제외.

[변환 후 — Instruction 조각]
작업 우선순위를 결정할 때:
- 요청자의 직급이나 압박감이 아닌 비즈니스 임팩트로 판단
- "긴급"이라는 표현이 있어도 실제 마감일을 먼저 확인
- 실제 마감 없는 긴급 요청은 중간 우선순위로 분류
```

**예시 2 — TK-009: 질문의 품질이 에이전트 품질을 결정**
```
[변환 전 — TK]
패턴: "뭘 하라"보다 "왜 하는지 + 판단 기준"을 주면 결과가 3배.

[변환 후 — Instruction 조각]
사용자에게 응답을 생성할 때:
- 단순 실행 전에 "이 작업의 목적이 무엇인지" 맥락을 파악
- 판단이 필요한 지점에서는 판단 근거를 함께 제시
- 규칙에 없는 예외 상황이면 "왜"를 기준으로 추론하되, 확신이 없으면 사용자에게 확인 요청
```

---

### Instruction 품질 개선 루프

```
에이전트 실행
     ↓
출력 품질 평가 (Accuracy KPI)
     ↓
품질 저하 원인 분석
     ↓
관련 TK 부재 확인
     ↓
/pm-tacit-extract로 새 TK 추출
     ↓
PM-ENGINE-MEMORY append
     ↓
Instruction 업데이트
     ↓
다음 실행 품질 향상
```

---

### 운영 원칙

**1. 매일 1개 TK 원칙**
`one-day-one-prompt` 크론이 매일 PM 판단 경험에서 TK를 추출합니다.  
작은 것도 기록합니다. 나중에 어떤 것이 중요해질지 모릅니다.

**2. 활성화 조건 필수**
TK마다 반드시 🟢 활성화 조건을 작성합니다.  
조건 없는 TK는 검색에서 잘 찾히지 않습니다. (CR 패턴)

**3. 연관 TK 링크**
TK는 고립된 것이 아닙니다. 서로 연결된 지식 그래프입니다.  
연관 TK를 링크하면 관련 지식이 함께 검색됩니다.

**4. 주기적 증류**
`weekly-memory-distill` 크론이 TK를 검토하고 정리합니다.  
오래되거나 더 나은 버전이 생긴 TK는 업데이트합니다.

---

### 사용 방법

```
# TK 추출 및 저장
/pm-tacit-extract [PM 판단 경험]

# TK → Instruction 변환
/tk-to-instruction [TK 번호 또는 주제]

# TK 기반 의사결정
/pm-decision-log [현재 상황]
```

---

### Instructions

**[/pm-tacit-extract 실행 시]**

사용자의 PM 경험에서 암묵지를 추출합니다: **$ARGUMENTS**

Step 1 — 경험 청취 및 판단 패턴 포착
Step 2 — TK 유형 분류 (Decision/Failure/Heuristic/Anti-Pattern/Insight)
Step 3 — TK-NNN 구조로 작성 (활성화/비활성화 조건 포함)
Step 4 — PM-ENGINE-MEMORY.md에 append할 형식으로 출력
Step 5 — 기존 TK와 연관 관계 제안

**[/tk-to-instruction 실행 시]**

TK 내용을 에이전트 Instruction 조각으로 변환: **$ARGUMENTS**

Step 1 — 해당 TK 내용 파악
Step 2 — Instruction 7요소 중 어느 섹션에 들어가는지 결정
Step 3 — 에이전트가 따를 수 있는 구체적 지시 문장으로 변환
Step 4 — 변환된 Instruction 조각 출력
Step 5 — 기존 Instruction과의 충돌 여부 검토

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- PM-ENGINE-MEMORY.md: OpenClaw 워크스페이스 실제 운영 파일
- one-day-one-prompt 크론 (20:00): TK 자동 추출 파이프라인
- weekly-memory-distill 크론: CR 필드 자동 채움 (2026-03-01 도입)
- Contextual Retrieval: PM-ENGINE-MEMORY CR 패턴 (2026-03-01)

---

## Further Reading
- Ikujiro Nonaka, "The Knowledge-Creating Company" — Knowledge management
- Ethan Kim, "TK-NNN: Never-ending Nuance Network" — Agent-native tacit knowledge system (TK-001→TK-999)
