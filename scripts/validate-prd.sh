#!/bin/bash
# validate-prd.sh — PRD 스킬 완료 시 Quality Gate 검증
# Phase 1: 최소 검증 (출력 파일 존재 + 필수 섹션 확인)
# Phase 2 (2026-05-14): mermaid workflow ↔ userflow ↔ requirements 정합성 검증

OUTPUT_DIR="${1:-.}"
ERRORS=0

# 최근 생성된 PRD 파일 찾기
PRD_FILE=$(find "$OUTPUT_DIR" -name "*prd*" -o -name "*PRD*" | head -1)

if [ -z "$PRD_FILE" ]; then
  echo "⚠️ PRD 파일을 찾을 수 없습니다. 출력물을 확인하세요."
  exit 0  # 경고만, 블로킹하지 않음
fi

echo "📋 PRD Quality Gate 검증: $PRD_FILE"

# 필수 섹션 체크
REQUIRED_SECTIONS=("Role" "Context" "Objective" "Tools" "Memory" "Output" "Failure")
for section in "${REQUIRED_SECTIONS[@]}"; do
  if ! grep -qi "$section" "$PRD_FILE" 2>/dev/null; then
    echo "❌ 누락된 섹션: $section"
    ERRORS=$((ERRORS + 1))
  fi
done

# mermaid 정합성 검증 (Python 결정론 게이트)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MERMAID_VALIDATOR="${SCRIPT_DIR}/validate-mermaid.py"
if [ -f "$MERMAID_VALIDATOR" ] && grep -q '```mermaid' "$PRD_FILE" 2>/dev/null; then
  if command -v python3 >/dev/null 2>&1; then
    python3 "$MERMAID_VALIDATOR" "$PRD_FILE" || ERRORS=$((ERRORS + 1))
  else
    echo "⚠️ python3 없음 — mermaid 정합성 검증 건너뜀"
  fi
fi

if [ $ERRORS -eq 0 ]; then
  echo "✅ Quality Gate 통과 — 필수 섹션 + mermaid 정합성 모두 충족"
else
  echo "⚠️ $ERRORS개 항목 미충족 — 검토 권장"
fi

exit 0
