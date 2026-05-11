# troubleshooting — ost

## "Mermaid가 렌더링 안 됨"

- 라벨에 따옴표가 있으면 escape 필요 — 자동 처리되지만 verify.
- VS Code Mermaid preview / GitHub markdown render에서 확인.

## "Opportunity가 solution처럼 들린다"

- 작성 자체로 검출 안 됨. 가이드: "동사가 *못 한다/없다*로 시작하는가?" 체크.
- "솔로 PM이 미팅 직후 결과물을 못 만든다" ✓
- "AI로 결과물 자동 생성" ✗ (이건 solution)

## "evidence_count는 어디서 가져오나"

- `interview-synthesis audit`의 `persons_with_strong_push` 길이.
- 또는 manual count for non-AI interviews.

## "Outcome 한 줄이 너무 길다"

- 50자 이내 권장. Mermaid 가독성.
- 더 길어지면 \\n으로 줄바꿈하거나 별도 docs/OUTCOME.md.
