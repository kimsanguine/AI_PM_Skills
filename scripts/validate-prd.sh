#!/bin/bash
# validate-prd.sh — PRD 스킬 완료 시 Quality Gate 검증
# Phase 1: 최소 검증 (출력 파일 존재 + 필수 섹션 확인)

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

if [ $ERRORS -eq 0 ]; then
  echo "✅ Quality Gate 통과 — 필수 7개 섹션 모두 포함"
else
  echo "⚠️ $ERRORS개 섹션 누락 — 검토 권장"
fi

exit 0
