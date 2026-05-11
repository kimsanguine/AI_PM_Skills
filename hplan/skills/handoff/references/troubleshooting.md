# troubleshooting — handoff

## "Hook이 spec.md 작성을 막음"

기능. `harness/build-gate/checkpoint.json`에 `{"status":"approved"}` 작성 후 재시도. 또는 일회성 `CLAUDE_HPLAN_BYPASS=1` 환경변수.

## "spec-kit specs/ 디렉토리가 NNN-slug 형식 아님"

`scripts/export_handoff.py:next_spec_number()`가 기존 디렉토리 스캔. 이름 형식 다르면 1부터 시작. spec-kit 컨벤션 맞춰서 manual rename도 OK.

## "Kiro에서 import 안 됨"

Kiro는 `.kiro/specs/<slug>/`를 repo root 기준으로 찾음. handoff는 `harness/exports/kiro/.kiro/specs/...`에 출력 → repo root로 symlink 또는 cp:

```bash
cp -r harness/exports/kiro/.kiro .
```

## "한 번에 너무 많은 파일"

`--target` 단일 지정 권장:
```bash
export_handoff.py brief.json --target spec-kit  # 3 files only
```

## "Brief의 field 누락"

기본값으로 채워짐 (예: cogs_ceiling 누락 시 "TBD"). 단 downstream 가치 약화. cogs-sentinel 실행 후 brief 갱신 권장.
