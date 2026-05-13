# Ralph Loop 자율 모드 규약

> "/team" 후속으로 "ralph loop로 진행"이 호출된 경우 적용되는 빌드 자율 모드 표준.

## 핵심 원칙

1. **질문 금지** — 자율 모드는 사용자의 추가 결정 없이 진행한다.
2. **백업 + dry-run 의무** — 모든 비가역 변경 직전.
3. **pending_inputs 배치** — 결정이 필요한 항목은 즉시 묻지 않고 누적.
4. **검증 통과 후 다음** — 단위 테스트 실패 시 즉시 중단.

## 반복 사이클

```
[1] Build phase
    - Builder가 단일 작업 단위 구현
[2] Verify phase
    - Verifier가 테스트 실행 + smoke run
    - 실패 → 즉시 중단, 사용자에게 보고
[3] Review phase
    - Reviewer가 diff 검토 + 일관성 확인
    - 미흡 → Build phase로 회귀
[4] Advance
    - 다음 작업 단위 진입
```

## pending_inputs 포맷

```markdown
# pending_inputs.md

## 2026-05-14 14:30 — landing-redesign

### Q1: 다크모드 토글 위치
- 옵션 A: Header 우측 (디폴트 추천)
- 옵션 B: Footer
- 기본값으로 A 적용, 사용자 확인 필요

### Q2: 컴포넌트 명명 (Card vs Tile)
- 현재 코드는 Card, 디자인 시안은 Tile
- 코드 기준 Card 유지, 사용자 확인 필요
```

## 자율 모드 중단 조건

- 같은 테스트 2회 연속 실패
- 백업 생성 실패
- pending_inputs > 5건 누적
- 사용자 명시적 중단 명령

## 종료 시 표준 산출물

1. 변경 요약 (파일별 +/-)
2. 테스트 결과 (전체 통과 여부)
3. pending_inputs (있으면)
4. 다음 작업 권고 1~3개
