# test-cases — handoff

## TC-001 — `--target all` writes 9 files
- spec-kit (3) + kiro (3) + gstack (1) + claude (2) = 9

## TC-002 — spec-kit number auto-increment
- First run: `specs/001-slug/`
- Second run with different product name: `specs/002-slug/`

## TC-003 — Existing files not overwritten without --force
- Second run with same product name → skipped, second specs dir not created

## TC-004 — `--force` overwrites
- Second run with `--force` → overwrites

## TC-005 — Korean product name slug
- `"SocialDraft"` → slug `socialdraft-v2` (hyphenated lowercase)
- 한국어 ICP/problem text는 그대로 유지

## TC-006 — Single target works
- `--target spec-kit` → only spec-kit files generated

## TC-007 — Idempotent skip
- 같은 target 두 번 → 두 번째는 `skipped` (force 없으면)
