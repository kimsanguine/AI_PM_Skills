# hplan STATE

> 이 파일은 `/hplan-build` CONDITIONAL_GO 출력 시 자동 생성됩니다.
> 새 Claude Code 세션을 열 때 SessionStart hook이 이 파일을 읽어 게이트 상태를 주입합니다.
> 조건이 검증될 때마다 `verified_by`와 상태를 직접 갱신하세요.

---

gate: build
verdict: CONDITIONAL_GO
decision_id: dec-YYYY-MM-DD-XXXXX
generated: YYYY-MM-DD

## Active 조건 (미검증)

| 조건 | verified_by | 상태 |
|------|-------------|------|
| [조건 이름] | [테스트 파일 경로 — 추후 기입] | ❌ |

**규칙**:
- `verified_by` 파일이 존재하면 ✅로 갱신
- 모든 조건 ✅ 전까지 다음 Build Gate 종료 선언 금지
- 파일 없음 = 조건 미검증 = 게이트 통과 불완전

## 블로커 (외부 의존성)

- [미완료 항목 — 예: API 키 미발급, DB 미생성]

## 다음 진입 조건

[W1 진입 요건 한 줄 — 블로커가 해소되는 시점]

---

<!-- 이 파일은 hplan harness의 일부입니다. 삭제하지 마세요. -->
<!-- validate_docs.py는 이 파일의 verified_by 경로를 검사합니다. -->
