# Test Cases — claude-md 스킬

## 1) Trigger Tests

### Should Trigger (5)

1. "이 프로젝트에 CLAUDE.md를 만들어줘"
   - 이유: CLAUDE.md 신규 생성 요청

2. "CLAUDE.md가 오래됐는데 업데이트해줘. TypeScript로 마이그레이션했거든"
   - 이유: 기존 CLAUDE.md 개선 요청

3. "Claude Code가 자꾸 프로젝트 맥락을 잊어. 어떻게 해야 돼?"
   - 이유: CLAUDE.md 부재/부실로 인한 문제 → CLAUDE.md 생성으로 해결

4. "AI_PM_Skills 중에 이 프로젝트에 맞는 게 뭐야?"
   - 이유: 프로젝트 시그널 기반 스킬 추천 요청

5. "새 팀원이 들어오는데 프로젝트 세팅 문서 만들어줘"
   - 이유: CLAUDE.md는 AI 팀원 + 인간 팀원 모두의 온보딩 문서

### Should NOT Trigger (5)

1. "에이전트의 시스템 프롬프트를 설계해줘"
   - 올바른 라우팅: `forge/instruction`

2. "이 프롬프트를 CRISP 프레임워크로 최적화해줘"
   - 올바른 라우팅: `forge/prompt`

3. "PRD를 작성해줘"
   - 올바른 라우팅: `forge/prd`

4. "컨텍스트 윈도우 토큰 예산을 계획해줘"
   - 올바른 라우팅: `forge/ctx-budget`

5. "멀티에이전트 아키텍처를 설계해줘"
   - 올바른 라우팅: `atlas/orchestration`

## 2) Functional Tests (Given-When-Then)

### Test 1: Next.js 프로젝트 신규 생성

**Given:**
- 디렉토리: Next.js 14 + TypeScript + Tailwind
- CLAUDE.md: 없음
- agents/ 디렉토리: 없음

**When:**
- `/claude-md .` 스킬 실행

**Then:**
- CLAUDE.md 생성 (6개 섹션: 개요, 기술스택, 빌드, 컨벤션, 아키텍처, 주의사항)
- AI_PM_Skills 추천: 없음 또는 최소 (에이전트 시그널 없으므로)
- 토큰: ~1,500

---

### Test 2: 에이전트 프로젝트 + 기존 CLAUDE.md

**Given:**
- 디렉토리: Python FastAPI + agents/ (5개 에이전트)
- CLAUDE.md: 존재하지만 에이전트 섹션 없음, 빌드 명령어 오래됨

**When:**
- `/claude-md .` 스킬 실행

**Then:**
- 개선 모드 진입 (기존 CLAUDE.md 분석)
- 에이전트 구조 섹션 추가
- 빌드 명령어 업데이트
- AI_PM_Skills 추천: forge/instruction, atlas/orchestration, argus/kpi
- 변경점 diff 형태로 설명

---

### Test 3: 모노레포 프로젝트

**Given:**
- 디렉토리: Turborepo (apps/web, apps/api, packages/shared)
- CLAUDE.md: 없음

**When:**
- `/claude-md .` 스킬 실행

**Then:**
- 루트 CLAUDE.md + 각 패키지별 CLAUDE.md 분리 생성 제안
- 루트: 전체 구조, 공통 명령어
- apps/web: 프론트엔드 특화
- apps/api: 백엔드 특화

---

### Test 4: 빈 디렉토리 / 설정 파일 없음

**Given:**
- 디렉토리: 빈 폴더 또는 README.md만 있음
- 설정 파일: 없음

**When:**
- `/claude-md .` 스킬 실행

**Then:**
- 자동 감지 실패 → 수동 입력 모드 전환
- "어떤 기술 스택을 사용하나요?" 질문
- 사용자 입력 기반으로 CLAUDE.md 생성

## 3) Error Cases

### Error 1: 기존 CLAUDE.md 덮어쓰기

**상황:**
- 사용자가 "CLAUDE.md 새로 만들어줘"라고 했지만 이미 존재

**대응:**
- 기존 CLAUDE.md 읽고 분석
- "기존 CLAUDE.md를 발견했습니다. 개선하시겠습니까, 새로 만드시겠습니까?" 선택지 제공
- 새로 만들기 선택 시에도 기존 내용 백업 (.claude-md.backup)

---

### Error 2: 추측 기반 빌드 명령어

**상황:**
- package.json의 scripts에 "build"가 없는데 `npm run build`를 기록

**대응:**
- 실제 scripts 목록만 기록
- 없는 명령어는 "설정 필요" 표시
- `npm run` 결과로 사용 가능한 스크립트 목록 제공

## 4) Edge Cases

| # | 쿼리 | 판정 | 이유 |
|---|------|------|------|
| E1 | "CLAUDE.md는 있는데 너무 짧아. 3줄밖에 없어." | ✅ Trigger | 개선 모드 — 기존 내용 유지하면서 부족한 섹션 추가 |
| E2 | "이 프로젝트는 아직 코드가 없고 기획만 있어. CLAUDE.md를 미리 만들 수 있어?" | ✅ Trigger | 기획 기반 CLAUDE.md 생성 가능 (기술 스택 계획, 아키텍처 방향). 스캔 대신 사용자 입력 기반 |
| E3 | "CLAUDE.md말고 AGENTS.md나 SOUL.md도 만들어줄 수 있어?" | ⚠️ 경계 | CLAUDE.md는 이 스킬 범위. AGENTS.md → forge/instruction, SOUL.md → 범위 밖이지만 참고 가이드 제공 가능 |
| E4 | "비공개 레포인데 민감한 정보가 있어. CLAUDE.md에 뭘 넣으면 안 돼?" | ✅ Trigger | 주의사항 섹션에서 민감 정보 필터링 가이드 제공. .env 변수명, API 키 패턴 등은 CLAUDE.md에 포함하지 않음 |
| E5 | "팀원마다 다른 개발 환경을 쓰는데 (Mac/Windows/Linux) CLAUDE.md를 어떻게 만들어?" | ✅ Trigger | OS별 명령어 분기 또는 공통 명령어만 기록. Docker 기반이면 Docker 명령어로 통일 |

---

## 5) With/Without Skill 비교

### 시나리오: 새 프로젝트에 Claude Code 도입

**Without claude-md Skill:**
- 사용자가 CLAUDE.md를 직접 작성 (무엇을 넣어야 할지 모름)
- 빌드 명령어를 빠뜨리거나 잘못 기록
- Claude Code가 프로젝트 컨벤션을 모르고 코드 작성
- AI_PM_Skills 35개 중 어디서 시작해야 할지 막막

**With claude-md Skill:**
- 30초~2분 자동 스캔으로 프로젝트 파악 완료
- 실제 동작하는 명령어만 기록
- Claude Code가 프로젝트 맥락을 이해하고 일관된 코드 작성
- 프로젝트에 맞는 AI_PM_Skills 2~3개만 추천 → 바로 시작

**결과: "CLAUDE.md = AI 팀원의 첫날"이 자동으로 완성**
