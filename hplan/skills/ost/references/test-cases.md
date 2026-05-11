# test-cases — ost

## TC-001 — Valid tree generates Mermaid
- outcome + 2 opportunities + 3 solutions + 3 experiments → Mermaid with all nodes

## TC-002 — Empty opportunities → empty tree
- `opportunities: []` → outcome node only, no edges

## TC-003 — Solution without experiment
- `solutions: [{"name": "X"}]` (no experiment field) → renders solution node but no experiment node

## TC-004 — Korean characters in names
- "솔로 PM이 미팅 직후 결과물을 못 만든다" → Mermaid label correctly escaped (newline as \\n)

## TC-005 — File overwrite
- 두 번 호출 → 두 번째 호출이 파일 덮어씀 (regenerate semantics)

## TC-006 — Output directory creation
- `--out non/existent/dir/file.md` → mkdir parents 자동
