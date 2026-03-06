# phuryn/pm-skills 참고 레포 분석
> 작성일: 2026-03-06 | 목적: ethan-agent-pm-skills 설계 기준 수립

---

## 전체 스펙

| 항목 | 수치 |
|---|---|
| 플러그인 | 8개 |
| 스킬 | 65개 |
| 커맨드 | 36개 |
| GitHub Stars | 1,100+ (3일 만에) |
| 라이선스 | MIT |
| 지원 플랫폼 | Claude Code, Cowork, Gemini CLI, Cursor, Codex CLI, Kiro |

### 플러그인 목록
1. `pm-product-discovery` — 13 skills, 5 commands
2. `pm-product-strategy` — 12 skills, 5 commands
3. `pm-execution` — 15 skills, 10 commands (가장 강력)
4. `pm-market-research` — 7 skills, 3 commands
5. `pm-data-analytics` — 3 skills, 3 commands
6. `pm-go-to-market` — 6 skills, 3 commands
7. `pm-marketing-growth` — 5 skills, 2 commands
8. `pm-toolkit` — 4 skills, 5 commands (이력서, NDA, 문법 교정)

---

## ✅ 장점 (배울 점)

### 1. 구조 설계가 탁월하다
Skills → Commands → Plugins 3계층이 명확하다.
- Skills: 단일 프레임워크/지식 캡슐
- Commands: 스킬을 체인으로 연결한 워크플로우
- Plugins: 도메인별 패키지
→ **ethan-agent-pm-skills도 이 구조 그대로 채택**

### 2. 커맨드 체이닝 설계가 자연스럽다
각 커맨드 완료 후 "다음 권장 커맨드"를 자동 제안.
`/discover` → `/strategy` → `/write-prd` → `/plan-launch` 흐름이 PM 실무와 일치.
→ **우리 프로젝트도 Step N의 마지막에 "다음 권장 액션" 명시 패턴 적용 중**

### 3. 검증된 프레임워크 인코딩
Teresa Torres OST, Marty Cagan, Alberto Savoia, Dan Olsen 등
PM 업계 검증 프레임워크를 구조화해 스킬에 녹였다.
→ **우리도 프레임워크 출처 명시 (author + book) 패턴 채택**

### 4. 크로스 플랫폼 설계
Claude Code 전용 기능(Commands)과 범용 기능(Skills)을 분리해
Gemini CLI, Cursor, Codex CLI에서도 SKILL.md 재사용 가능.
→ **우리도 OpenClaw 네이티브 + Claude Code 듀얼 구조로 채택**

### 5. pm-execution이 특히 강력하다
15개 스킬 × 10개 커맨드 — PRD, OKR, 로드맵, 스프린트, 회고,
스테이크홀더맵, 유저스토리, 테스트시나리오까지 커버.
→ **우리의 pm-agent-execution 설계 시 구조 참고**

---

## ❌ 단점 (우리가 해결하는 것)

### 1. 에이전트 빌딩 관점이 전혀 없다 ← 핵심 공백
65개 스킬 전부가 "AI 도구를 쓰는 PM"을 위한 것.
"AI 에이전트를 만드는 PM"을 위한 스킬은 단 하나도 없다.
- 오케스트레이션 패턴? 없음
- 에이전트 Instruction 설계? 없음
- 토큰 비용 모델링? 없음
- 메모리 아키텍처? 없음
→ **이것이 ethan-agent-pm-skills의 존재 이유**

### 2. Reliability / Ethics 축 부재
일반 제품 디스커버리의 가정 검증은 Value / Usability / Viability / Feasibility 4축.
에이전트는 여기에 Reliability (신뢰성: 반복 정확도)와 Ethics (안전성: 오류의 영향)가 필수.
자율 에이전트가 잘못된 판단을 조용히 실행하면 피해가 증폭된다.
→ **agent-assumption-map에서 4축 재정의**

### 3. 빌드 vs 바이 의사결정 도구가 없다
에이전트를 직접 만들지, 외부 API를 쓸지, 기존 SaaS를 쓸지 결정하는 프레임워크 부재.
→ **build-or-buy SKILL.md로 해결**

### 4. 운영 비용 모델링이 없다
제품 비용은 인프라 비용 → 클라우드 단가 계산이 표준.
에이전트 비용은 토큰 수 × 호출 빈도 × 모델 단가 → 완전히 다른 계산 구조.
→ **agent-cost-model SKILL.md로 해결**

### 5. 실패 모드 분석이 AI-specific하지 않다
pre-mortem 스킬이 있지만 일반 제품 리스크 분석.
에이전트의 실패 유형 (할루시네이션 / 타임아웃 / 프롬프트 인젝션 / 비용 폭증)
을 다루지 않는다.
→ **failure-mode-analysis SKILL.md로 해결**

### 6. 운영자 고유 암묵지 축적 불가
스킬이 일반 PM 지식을 인코딩한 것.
"이 운영자 20년의 경험"을 누적하고 재활용하는 메커니즘이 없다.
→ **pm-engine 플러그인 + PM-ENGINE-MEMORY TK 시리즈로 해결**

### 7. pm-toolkit이 맥락에 안 맞는다
이력서 리뷰, NDA 초안, 문법 교정은 PM 도구로 어색하다.
전략적 방향성보다 유틸리티에 치우쳐 있다.
→ **우리는 pm-engine에 고유 자산 집중**

### 8. 영어 단일 언어
한국 시장, 아시아 PM 커뮤니티를 위한 로컬라이제이션 없음.
→ **우리는 한/영 이중 언어 SKILL.md로 차별화 가능**

### 9. Human-in-the-loop 설계 도구 없음
자동화가 어디까지 가능하고, 어디서 인간 판단이 필요한지
설계하는 프레임워크가 없다.
→ **human-in-loop-design SKILL.md로 해결**

### 10. MCP vs Skills 레이어 구분 없음
에이전트가 외부 시스템과 연결할 때 어떤 방식을 선택할지
(MCP / REST API / Skills) 가이드가 없다.
→ **prometheus-atlas-pattern에서 계층 설계 원칙 포함**

---

## 요약: 우리 프로젝트의 차별화 포인트

```
phuryn/pm-skills          ethan-agent-pm-skills
─────────────────         ──────────────────────
PM + AI 도구         →    PM + AI 에이전트 설계/운영
일반 제품 프레임워크  →    에이전트 특화 프레임워크
외부 지식 인코딩     →    운영자 암묵지 축적 (pm-engine)
영어 단일           →    한/영 (국내 PM 커뮤니티)
빌딩 과정 없음      →    Reliability/Ethics/Cost 포함
8개 플러그인        →    5개 플러그인 (집중 > 양)
```

**결론**: phuryn/pm-skills의 구조 설계는 채택하되,
내용의 60%를 에이전트 특화로 교체하고 pm-engine으로 고유 자산을 만든다.
