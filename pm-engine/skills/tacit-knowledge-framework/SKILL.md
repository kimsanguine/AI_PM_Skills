---
name: tacit-knowledge-framework
description: "Extract, classify, and structure PM tacit knowledge into reusable TK (Tacit Knowledge) units. These TK units form the foundation of the pm-engine — the operator's unique IP that differentiates their agents from generic AI. Use when capturing lessons from experience, building the pm-engine library, or converting intuition into agent instructions."
---

## Tacit Knowledge Framework

암묵지(Tacit Knowledge)는 경험에서 나오지만 글로 쓰기 어렵습니다.  
"언제 이걸 해야 하는지 안다"는 것 — 그 '앎'의 근거.

PM 20년의 암묵지를 에이전트에 넣으면 무슨 일이 생기는가:
- 제네릭 AI: "PRD를 작성하세요" → 일반적인 PRD 템플릿 출력
- pm-engine이 있는 에이전트: 이든의 판단 기준을 알고 → 맥락에 맞는 PRD 작성

이것이 **Domain TK 해자**의 실체입니다.

---

### TK 단위 구조

모든 암묵지는 **TK-NNN** 형태로 구조화합니다:

```
TK-NNN: [암묵지 제목]

📌 패턴:
[이 암묵지의 핵심 판단 패턴 — 1~3문장]

🟢 활성화 조건:
[이 암묵지를 적용해야 하는 상황 1~2줄]

🔴 비활성화 조건:
[적용하면 안 되는 상황 1줄]

💡 Why:
[이 판단이 왜 중요한가 — 근거와 경험]

🔗 연관 TK: [TK-XXX, TK-YYY]
```

---

### TK 분류 체계 (5가지 유형)

**Type 1 — Decision Pattern (의사결정 패턴)**
> 반복적인 의사결정에서 사용하는 판단 기준

예시:
```
TK-001: 긴급 요청 우선순위 판단

패턴: 긴급해 보이는 요청이 와도,
      먼저 "이것이 Why-urgent인가"를 확인한다.
      실제 마감이 없는 '인식된 긴급'은 우선순위에서 제외.

활성화: 여러 이해관계자에게 동시 요청이 올 때
비활성화: 실제 비즈니스 임팩트가 명확히 계산된 긴급 요청
Why: 긴급 요청 80%는 발신자의 불안에서 비롯됨.
     맹목적 우선순위 변경은 핵심 작업 방해
연관: TK-003 (이해관계자 관리), TK-007 (우선순위 프레임워크)
```

**Type 2 — Failure Pattern (실패 패턴)**
> "이렇게 하면 망한다" — 직접 겪거나 목격한 실패 패턴

예시:
```
TK-012: 스펙 완성 후 개발 시작의 함정

패턴: 상세 스펙을 완성하고 개발을 시작하면
      스펙 완성 시점에 이미 가정이 틀렸을 확률이 높다.
      프로토타입 → 검증 → 스펙 순서가 더 효과적.

활성화: 새로운 기능 개발 시작 전
비활성화: 규제/컴플라이언스 요구로 사전 문서화 의무인 경우
Why: Boris Cherny(Anthropic)도 PRD 없이 프로토타입 먼저.
     빌드 비용이 낮아질수록 이 원칙은 강화됨.
연관: TK-015 (Prototype-first), TK-021 (PRD 역할 변화)
```

**Type 3 — Heuristic (경험칙)**
> "보통은 이렇게 하면 된다" — 빠른 판단을 위한 경험칙

예시:
```
TK-008: 3회 반복 → 자동화 원칙

패턴: 같은 작업을 3회 이상 반복하면
      4번째부터는 자동화 또는 템플릿화를 검토한다.

활성화: 반복 작업 감지 시
비활성화: 3회 이상이어도 맥락이 매번 다른 경우
Why: 반복 작업은 에너지를 소진하고 창의적 작업 시간을 뺏음.
     에이전트로 전환 시 10분 절감 × 365일 = 61시간/년
연관: TK-008 (build-or-buy), TK-034 (에이전트 기회 발굴)
```

**Type 4 — Anti-Pattern (반대 패턴)**
> "이것만큼은 하지 마라" — 강한 금지 원칙

예시:
```
TK-019: 도구 탓하기 금지

패턴: AI가 틀린 결과를 냈을 때,
      "AI가 못해서"라고 결론 내리기 전에
      프롬프트/컨텍스트/데이터 문제를 먼저 확인한다.

활성화: AI 에이전트 품질 문제 발생 시
비활성화: 모델 자체의 알려진 한계 (예: 수학 계산 정확도)
Why: 대부분의 AI 품질 문제는 설계 문제.
     도구 탓을 하면 개선 기회를 놓침.
연관: TK-022 (실패 모드 분류), TK-028 (프롬프트 디버깅)
```

**Type 5 — Insight (인사이트)**
> "이것을 알고 나서 세상이 달라 보였다" — 패러다임 전환 학습

예시:
```
TK-031: 에이전트의 병목은 코딩이 아니다

패턴: 에이전트를 만드는 PM의 병목은 기술이 아니라
      "어떤 에이전트를 만들지"와 "어떻게 판단하게 할지"다.

활성화: 에이전트 설계를 시작할 때
비활성화: 이미 검증된 에이전트를 구현만 할 때
Why: GPT-5.4, Claude Sonnet은 누구나 쓸 수 있는 API.
     차별화는 의도 설계와 도메인 암묵지에서 나옴.
연관: TK-035 (agent-moat), TK-001 (agent-instruction-design 철학)
```

---

### TK 추출 방법

**방법 1 — 대화 중 추출**
```
대화 중 "이건 어떻게 판단하셨어요?"라는 질문에 대한 답
→ 즉시 TK 후보로 포착
→ /pm-tacit-extract로 구조화
```

**방법 2 — 실수 후 추출**
```
실수 또는 예상 밖 결과 발생
→ "왜 이런 일이 생겼나" 근본 원인 분석
→ 재발 방지 원칙 → TK Anti-Pattern
```

**방법 3 — 반복 패턴 감지**
```
같은 결정을 3회 이상 했을 때
→ "나는 이런 상황에서 항상 이렇게 판단한다"
→ TK Decision Pattern
```

---

### 사용 방법

`/pm-tacit-extract [상황 또는 경험 설명]`

---

### Instructions

You are helping extract and structure PM tacit knowledge from: **$ARGUMENTS**

**Step 1** — 상황/경험 청취  
무슨 일이 있었는지, 어떤 판단을 내렸는지 파악

**Step 2** — 암묵지 패턴 포착  
"당신은 왜 그런 판단을 내렸나요?" 반복 질문  
명시되지 않은 전제와 기준 발굴

**Step 3** — TK 유형 분류  
Decision/Failure/Heuristic/Anti-Pattern/Insight 중 선택

**Step 4** — TK 구조화  
TK-NNN 형식으로 작성  
활성화/비활성화 조건 포함 (Contextual Retrieval 패턴)

**Step 5** — 연관 TK 연결  
기존 TK 중 연관된 것 파악하여 링크

**Step 6** — PM-ENGINE-MEMORY 저장  
작성된 TK를 PM-ENGINE-MEMORY.md에 append  
다음 `/tk-to-instruction`으로 에이전트 Instruction 변환 준비

---

### 참고
- 설계자: Sanguine Kim (이든), 2026-03
- Contextual Retrieval 패턴: PM-ENGINE-MEMORY CR 필드 도입 기반 (2026-03-01)
- TK-001 최초 작성: PM-ENGINE 1-Day-1-Prompt 크론 운영 경험
- Tacit Knowledge 개념: Michael Polanyi, *The Tacit Dimension* (1966)
