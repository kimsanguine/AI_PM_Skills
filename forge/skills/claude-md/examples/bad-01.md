# Bad Example — claude-md 스킬

## 사용자 요청

"CLAUDE.md 만들어줘"

## 거절/수정 이유

- 잘못된 처리 1: 프로젝트 스캔 없이 바로 일반 템플릿 생성
- 잘못된 처리 2: 빌드 명령어를 추측으로 기입 (실제 동작 확인 안 함)
- 잘못된 처리 3: 모든 AI_PM_Skills를 무조건 추천 (시그널 무시)

## 잘못된 결과물

```markdown
# CLAUDE.md
이 프로젝트는 웹 앱입니다.
- npm run build
- npm test

모든 플러그인 설치를 권장합니다:
/plugin install oracle
/plugin install atlas
/plugin install forge
/plugin install argus
/plugin install muse
```

## 문제점

1. **프로젝트 개요**: "웹 앱" — 어떤 프레임워크? 누구를 위한 것? 구체성 0
2. **기술 스택**: 누락 — 프레임워크, 언어, 버전 정보 없음
3. **빌드 명령어**: 추측 — package.json scripts를 확인하지 않음
4. **코드 컨벤션**: 완전 누락 — 네이밍, 디렉토리, 스타일 정보 없음
5. **아키텍처**: 완전 누락 — 디렉토리 구조 분석 안 함
6. **주의사항**: 완전 누락 — Anti-Goals 없음
7. **추천**: 무차별 — 에이전트 코드가 없는데 에이전트 스킬 추천

## 올바른 처리

1. Phase 1에서 프로젝트 디렉토리를 먼저 스캔
2. 실제 감지된 기술 스택을 기반으로 CLAUDE.md 생성
3. 에이전트 관련 시그널이 없으면 에이전트 스킬 추천 건너뜀
4. Quality Gate로 각 섹션 완성도 검증
