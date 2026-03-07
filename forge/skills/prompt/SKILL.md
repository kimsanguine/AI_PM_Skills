---
name: prompt
description: "Design prompts from a PM perspective — focusing on intent and outcome rather than syntax. Covers the CRISP framework, common prompt failure patterns, and how to encode PM judgment into agent instructions. Use when writing System Prompts, crafting agent instructions, or debugging underperforming prompts."
argument-hint: "[prompt or instruction to optimize]"
---

## Prompt Engineering for PMs

프롬프트 엔지니어링을 기술자 관점과 PM 관점에서 보면 완전히 다릅니다.

| 기술자 관점 | PM 관점 |
|---|---|
| 토큰 최적화 | 의도 명확화 |
| 구문 형식 | 판단 기준 정의 |
| Few-shot 예시 | 아웃컴 명세 |
| Temperature 조정 | Anti-Goals 설정 |

> "프롬프트는 신입 직원에게 주는 업무 지시서다.  
> 기술이 아니라 커뮤니케이션의 문제다."

---

### CRISP 프레임워크

PM이 쓸 수 있는 프롬프트 설계 5요소:

**C — Context (맥락)**
에이전트가 알아야 할 배경 정보
```
당신은 [역할]입니다.
사용자는 [누구]이고, 현재 [상황]에 있습니다.
```

**R — Role (역할)**
에이전트의 전문성과 페르소나
```
당신은 PM 20년 경력의 AI 에이전트 전문가입니다.
기술적 판단보다 '왜'를 먼저 설명하는 방식을 선호합니다.
```

**I — Instruction (지시)**
구체적인 행동 지시 — 무엇을, 어떻게, 순서대로
```
다음 순서로 진행하세요:
1. [입력] 분석
2. [프레임워크] 적용
3. [출력 형식]으로 결과 제시
```

**S — Scope (범위)**
해야 할 것과 하지 말아야 할 것
```
포함: [명시적으로 해야 하는 것]
제외: [절대 하지 말아야 하는 것 — Anti-Goals]
제한: [길이, 언어, 형식 제한]
```

**P — Parameters (파라미터)**
출력 형식, 길이, 톤, 채널
```
형식: [Markdown / Plain / JSON]
길이: [최대 N줄]
언어: [한국어]
톤: [간결하고 실용적으로]
```

---

### 프롬프트 실패 패턴 7가지

**Pattern 1 — 목표 모호성**
```
❌ "뉴스를 요약해줘"
✅ "오늘 AI 에이전트 관련 뉴스 5건을 각 3줄 이내로 요약하고,
    PM 관점의 인사이트 1줄을 추가해줘"
```

**Pattern 2 — Anti-Goals 누락**
```
❌ "최선을 다해 분석해줘"
✅ "분석해줘. 단, 확실하지 않은 내용은 추측하지 말고
    '확인 필요'로 표시해줘"
```

**Pattern 3 — 출력 형식 미명시**
```
❌ "결과 알려줘"
✅ "결과를 다음 형식으로 Telegram에 전송 가능한 텍스트로 작성:
    - [제목]
    - [3줄 요약]
    - [행동 제안 1개]"
```

**Pattern 4 — 컨텍스트 과부하**
```
❌ [5000줄 파일 전체 로드] + "분석해줘"
✅ 관련 섹션만 추출 후 → "다음 내용을 기준으로 분석해줘: [핵심 섹션]"
```

**Pattern 5 — 판단 기준 부재**
```
❌ "중요한 이메일을 선별해줘"
✅ "다음 기준으로 중요도를 판단해줘:
    높음: 직접 답장 필요, 마감 포함, 의사결정 요청
    중간: 참고 필요, FYI
    낮음: 뉴스레터, 마케팅, 자동 발송"
```

**Pattern 6 — 실패 처리 누락**
```
❌ "데이터를 가져와서 분석해줘"
✅ "데이터를 가져와서 분석해줘.
    데이터가 없으면: '데이터 없음'으로 표시하고 계속 진행해줘.
    API 오류 시: 오류 메시지를 포함해서 결과를 전송해줘."
```

**Pattern 7 — 역할 충돌**
```
❌ "창의적이고 정확하고 간결하게 작성해줘"
    (창의성 ↔ 정확성 ↔ 간결성은 종종 충돌)
✅ "정확성을 최우선으로, 간결하게 작성해줘.
    창의적 표현보다 명확한 전달을 선호해줘."
```

---

### PM 판단을 프롬프트에 녹이는 방법

PM의 핵심 가치는 **판단 기준**을 명확히 하는 것입니다.

**판단 기준 명시화 패턴:**

```
[상황 A]이면 → [행동 X]
[상황 B]이면 → [행동 Y]
판단이 어려우면 → [에스컬레이션 방법]
```

예시 (이메일 우선순위 에이전트):
```
발신자가 CEO/임원이면 → 항상 '높음'
마감일이 24시간 이내이면 → '높음'
키워드 [계약, 결제, 긴급]이면 → '높음'
뉴스레터/자동발송이면 → 자동 제외
판단이 불확실하면 → '확인 필요' 태그 추가
```

---

### Why-First 프롬프트 원칙

이든의 PM 철학 — 기술이 아닌 의도를 먼저:

```
❌ 기술 중심: "Chain-of-thought로 step-by-step 분석해줘"
✅ 의도 중심: "이 결정이 왜 중요한지 먼저 설명하고,
               그 이유를 기반으로 분석해줘"
```

에이전트가 "왜"를 이해하면:
- 예외 상황에서도 올바른 방향으로 판단
- 지시가 불완전해도 의도에 맞게 처리
- 새로운 상황에 유연하게 대응

---

### 사용 방법

`/prompt-engineering-pm [작성하려는 프롬프트 목적]`

---

### Instructions

You are helping design a PM-perspective prompt for: **$ARGUMENTS**

**Step 1** — CRISP 5요소 채우기  
Context / Role / Instruction / Scope / Parameters 순서로 작성

**Step 2** — 판단 기준 명시화  
[상황] → [행동] 매핑 테이블 작성  
판단이 어려운 경우의 에스컬레이션 방법 포함

**Step 3** — Anti-Goals 추가  
절대 하지 말아야 할 것 최소 3개 명시

**Step 4** — 실패 처리 추가  
데이터 없음 / API 실패 / 판단 불확실 케이스 처리 방법

**Step 5** — 7가지 실패 패턴 체크  
작성한 프롬프트가 각 패턴을 피하고 있는지 검토

**Step 6** — Why-First 검토  
"이 에이전트가 왜 이 작업을 하는지"가 프롬프트에 녹아 있는가?

**Step 7** — 최종 프롬프트 출력  
사용 가능한 형태로 완성된 프롬프트 제시

---

### 참고
- CRISP 프레임워크: Sanguine Kim (이든) 설계, 2026-03
- Why-First 원칙: PM-ENGINE 철학 (이든의 20년 PM 암묵지)
- 7가지 실패 패턴: OpenClaw 크론잡 운영 및 디버깅 경험 기반

---

## Further Reading
- Anthropic Documentation — https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering
- OpenAI Prompt Engineering Guide — https://platform.openai.com/docs/guides/prompt-engineering
