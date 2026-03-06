---
name: pm-engine-memory
description: "Interface with the PM-ENGINE-MEMORY file — the operator's accumulated PM tacit knowledge database. Enables agents to reference, search, and apply TK (Tacit Knowledge) entries, and supports the conversion pipeline from TK units to agent instructions. The core of the pm-engine competitive moat."
---

## PM-ENGINE-MEMORY Interface

PM-ENGINE-MEMORY는 pm-engine의 심장입니다.

구조:
```
PM-ENGINE-MEMORY.md
├── TK-001: 긴급 요청 우선순위 판단
├── TK-002: [다음 TK]
├── ...
└── TK-NNN: [최신 TK]
```

이 파일이 특별한 이유:
- 일반 LLM 지식: 인터넷의 평균
- PM-ENGINE-MEMORY: 이든의 20년 경험에서 검증된 판단 기준

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

### PM-ENGINE-MEMORY 파일 구조

```markdown
# PM-ENGINE-MEMORY.md

_마지막 업데이트: YYYY-MM-DD_

---

## TK-001: [제목]

📌 패턴:
[핵심 판단 패턴]

🟢 활성화 조건:
[언제 이 TK를 쓰는가]

🔴 비활성화 조건:
[언제 쓰면 안 되는가]

💡 Why:
[근거]

🔗 연관 TK: [TK-XXX]

---

## TK-002: [제목]
...
```

---

### tk-to-instruction 변환

TK를 에이전트 Instruction으로 변환하는 방법:

```
[변환 전 — TK]
TK-001: 긴급 요청 우선순위 판단

패턴: 긴급해 보이는 요청이 와도 실제 임팩트 먼저 확인.
      실제 마감 없는 '인식된 긴급'은 우선순위에서 제외.

[변환 후 — Instruction 조각]
작업 우선순위를 결정할 때:
- 요청자의 직급이나 압박감이 아닌 비즈니스 임팩트로 판단
- "긴급"이라는 표현이 있어도 실제 마감일을 먼저 확인
- 실제 마감 없는 긴급 요청은 중간 우선순위로 분류
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
