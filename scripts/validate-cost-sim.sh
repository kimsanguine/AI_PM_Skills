#!/bin/bash
# validate-cost-sim.sh — 비용 시뮬레이션 스킬 완료 시 Quality Gate 검증
# Phase 1: 최소 검증 (비용 템플릿 필수 항목 확인)

OUTPUT_DIR="${1:-.}"
ERRORS=0

# 최근 생성된 비용 시뮬레이션 파일 찾기
COST_FILE=$(find "$OUTPUT_DIR" -name "*cost*" -o -name "*비용*" | head -1)

if [ -z "$COST_FILE" ]; then
  echo "⚠️ 비용 시뮬레이션 파일을 찾을 수 없습니다."
  exit 0
fi

echo "💰 Cost-Sim Quality Gate 검증: $COST_FILE"

# 필수 항목 체크
REQUIRED=("토큰" "호출" "월간" "스케일" "최적화")
for item in "${REQUIRED[@]}"; do
  if ! grep -q "$item" "$COST_FILE" 2>/dev/null; then
    echo "❌ 누락된 항목: $item"
    ERRORS=$((ERRORS + 1))
  fi
done

# 스케일 시나리오 3단계 확인
SCALE_COUNT=$(grep -cE "(1명|10명|100명|사용자 1|사용자 10|사용자 100)" "$COST_FILE" 2>/dev/null)
if [ "$SCALE_COUNT" -lt 3 ]; then
  echo "⚠️ 스케일 시나리오 $SCALE_COUNT/3 단계만 포함"
  ERRORS=$((ERRORS + 1))
fi

if [ $ERRORS -eq 0 ]; then
  echo "✅ Quality Gate 통과"
else
  echo "⚠️ $ERRORS개 항목 누락 — 검토 권장"
fi

exit 0
