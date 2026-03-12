# Good Example — claude-md 스킬

## 사용자 요청

"이 프로젝트에 CLAUDE.md를 세팅해줘. AI 에이전트도 만들고 있어서 그것도 같이 반영해줘."

## 승인 이유

- 프로젝트에 CLAUDE.md가 없어 Claude Code가 매번 프로젝트 맥락을 파악해야 함
- 에이전트 관련 코드가 있어 AI_PM_Skills 추천이 유의미

## 예상 처리

1. **Phase 1 — 스캔**: package.json (Next.js 14 + TypeScript), agents/ 디렉토리 (3개 에이전트), Prisma 스키마, .eslintrc 분석
2. **Phase 2 — 생성**: 프로젝트 개요, 기술 스택, 빌드 명령어, 코드 컨벤션, 아키텍처, 에이전트 구조, 주의사항 섹션 포함 (~2,200 tokens)
3. **Phase 3 — 추천**: agents/ 시그널 → forge/instruction, 3개 에이전트 → atlas/orchestration, 모니터링 없음 → argus/kpi
4. **Phase 4 — 검증**: Quality Gate 전체 체크, CLAUDE.md 프로젝트 루트에 저장

## 최종 결과물

- 프로젝트 특화 CLAUDE.md (7개 섹션, ~2,200 tokens)
- AI_PM_Skills 추천 3개 (시그널 기반, 설치 명령어 포함)
- 다음 액션: "forge/instruction으로 에이전트 Instruction을 설계하세요"
