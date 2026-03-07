#!/bin/bash
# validate-review.sh — 에이전트 설계 리뷰 완료 시 Quality Gate 검증
# 공용: premortem, reliability, agent-plan-review에서 사용
# Phase 1: 최소 검증 (장애 모드 + 완료 요약 확인)

SKILL_TYPE="${1:-review}"
OUTPUT_DIR="${2:-.}"
ERRORS=0

echo "🔍 $SKILL_TYPE Quality Gate 검증 시작"

# 최근 생성된 리뷰 파일 찾기
REVIEW_FILE=$(find "$OUTPUT_DIR" -name "*review*" -o -name "*premortem*" -o -name "*reliability*" -o -name "*리뷰*" | head -1)

if [ -z "$REVIEW_FILE" ]; then
  echo "⚠️ 리뷰 출력 파일을 찾을 수 없습니다."
  exit 0
fi

# 장애 모드 매트릭스 존재 확인
if ! grep -qE "(장애.*유형|장애.*모드|Failure.*Mode|장애 모드 매트릭스)" "$REVIEW_FILE" 2>/dev/null; then
  echo "❌ 장애 모드 매트릭스 누락"
  ERRORS=$((ERRORS + 1))
fi

# 완료 요약 존재 확인
if ! grep -qE "(완료 요약|Summary|결론)" "$REVIEW_FILE" 2>/dev/null; then
  echo "❌ 완료 요약 누락"
  ERRORS=$((ERRORS + 1))
fi

if [ $ERRORS -eq 0 ]; then
  echo "✅ Quality Gate 통과"
else
  echo "⚠️ $ERRORS개 항목 누락 — 검토 권장"
fi

exit 0
