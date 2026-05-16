#!/usr/bin/env python3
"""
validate-craft-lint.py — craft 플러그인의 결정론 검증 스크립트.

DESIGN.md (Google 표준 base) + RESPECT.md (hplan extension) 두 파일의
구조·필수 필드·cross-reference 일관성을 검증한다.

Phase 4 hierarchy-rules 가 픽셀 분석 (런타임 측정) 을 담당하고,
이 스크립트는 메타데이터·일관성 (정적 검증) 만 책임진다.

사용:
    python3 scripts/validate-craft-lint.py
    python3 scripts/validate-craft-lint.py --respect path/to/RESPECT.md --design path/to/DESIGN.md
    python3 scripts/validate-craft-lint.py --strict   # warning도 exit 1

Rule 5 준수:
    LLM 호출 0. YAML 파싱·정규식·dict lookup 만으로 모든 검증 수행.
    [[feedback_doc_consistency_audit]] 7개소 grep 매트릭스 패턴의 craft 적용.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RESPECT = REPO_ROOT / ".design" / "RESPECT.md"
DEFAULT_DESIGN = REPO_ROOT / ".design" / "DESIGN.md"

RESPECT_REQUIRED_FIELDS = [
    "three_second_rule",
    "next_action",
    "social_proof",
    "hierarchy_rules",
    "motion_language",
]

HIERARCHY_REQUIRED = [
    "max_elements_above_fold",
    "max_type_scale_per_screen",
    "color_ratio",
    "whitespace_to_content_min",
    "cta_count_above_fold",
]

THREE_SECOND_FORBIDDEN_WORDS = [
    "차세대", "혁신적", "최첨단", "솔루션", "플랫폼",
    "next-generation", "innovative", "cutting-edge", "solution platform",
]


def load_yaml_block(path: Path) -> dict | None:
    """YAML dict 만 안전 로드. 파싱 실패·dict 아닌 결과는 None (controlled error)."""
    if not path.exists():
        return None
    try:
        import yaml
    except ImportError:
        print("❌ pip install pyyaml 필요", file=sys.stderr)
        sys.exit(2)
    text = path.read_text(encoding="utf-8")
    fenced = re.search(r"```ya?ml\n(.+?)\n```", text, re.DOTALL)
    try:
        parsed = yaml.safe_load(fenced.group(1) if fenced else text)
    except yaml.YAMLError as e:
        print(f"⚠️  YAML 파싱 실패: {path.name}: {e}", file=sys.stderr)
        return None
    # Markdown text / scalar / list 등 dict 아닌 결과는 controlled None
    if not isinstance(parsed, dict):
        return None
    return parsed


def check_respect_required(respect: dict) -> list[str]:
    errors = []
    for f in RESPECT_REQUIRED_FIELDS:
        if f not in respect:
            errors.append(f"RESPECT.md: 필수 필드 '{f}' 누락")
    return errors


def check_hierarchy_rules(respect: dict) -> list[str]:
    errors = []
    h = respect.get("hierarchy_rules", {})
    for f in HIERARCHY_REQUIRED:
        if f not in h:
            errors.append(f"RESPECT.md hierarchy_rules: '{f}' 누락")
    ratio = h.get("color_ratio")
    if ratio and isinstance(ratio, list):
        if sum(ratio) != 100:
            errors.append(f"hierarchy_rules.color_ratio 합이 {sum(ratio)} ≠ 100 (60/30/10 룰)")
        if len(ratio) != 3:
            errors.append(f"hierarchy_rules.color_ratio 항목 수 {len(ratio)} ≠ 3")
    cta = h.get("cta_count_above_fold")
    if cta is not None and cta != 1:
        errors.append(f"hierarchy_rules.cta_count_above_fold = {cta} (권장 1, 영상 5번 원칙)")
    return errors


def check_three_second_rule(respect: dict) -> list[str]:
    errors = []
    rule = respect.get("three_second_rule", {})
    what = rule.get("what_is_this", "")
    if not what or len(what.strip()) == 0:
        errors.append("three_second_rule.what_is_this 비어 있음 (한 문장 필수)")
        return errors
    word_count = len(what.split())
    if word_count > 20:
        errors.append(f"three_second_rule.what_is_this 단어 수 {word_count} > 20 (3초에 못 읽음)")
    for forbidden in THREE_SECOND_FORBIDDEN_WORDS:
        if forbidden in what:
            errors.append(f"three_second_rule.what_is_this 금지어 '{forbidden}' 사용 (의미 0)")
    return errors


def check_next_action(respect: dict) -> list[str]:
    errors = []
    na = respect.get("next_action", {})
    primary = na.get("primary_cta")
    secondary = na.get("secondary_cta")
    if not primary:
        errors.append("next_action.primary_cta 누락 (1개 필수)")
    if secondary and secondary != "null":
        errors.append(f"next_action.secondary_cta = '{secondary}' (처음엔 None 권장 — 영상 5번)")
    return errors


def check_cross_ref(respect: dict, design: dict) -> list[str]:
    errors = []
    if not design or not isinstance(design, dict):
        return ["DESIGN.md 누락 또는 YAML dict 아님 — Google 표준 base 필수 (fenced ```yaml 블록 또는 `npx @google/design.md init`). craft-lint 통과 거부."]

    respect_ref = respect.get("references_design_md")
    if not respect_ref:
        errors.append("RESPECT.md: references_design_md 필드 누락 (DESIGN.md 명시 참조)")

    design_colors = design.get("colors", {})
    if design_colors:
        primary_keys = [k for k in design_colors if "primary" in k.lower() or "accent" in k.lower() or "cta" in k.lower()]
        if not primary_keys:
            errors.append("DESIGN.md colors: primary/accent/cta 키 없음 (CTA 색 명시 필요)")

    type_scale = design.get("typography", {})
    if type_scale and "scale" in type_scale:
        scale_count = len(type_scale["scale"]) if isinstance(type_scale["scale"], list) else 0
        max_scale = respect.get("hierarchy_rules", {}).get("max_type_scale_per_screen", 4)
        if scale_count > max_scale:
            errors.append(
                f"DESIGN.md typography.scale 항목 {scale_count} > RESPECT.md max_type_scale_per_screen {max_scale}"
            )
    return errors


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--respect", default=str(DEFAULT_RESPECT))
    ap.add_argument("--design", default=str(DEFAULT_DESIGN))
    ap.add_argument("--strict", action="store_true", help="warning도 exit 1")
    args = ap.parse_args()

    respect_path = Path(args.respect)
    design_path = Path(args.design)

    if not respect_path.exists():
        print(f"❌ RESPECT.md 없음: {respect_path}")
        print("   craft/respect-brief 스킬로 먼저 생성하세요.")
        return 2

    respect = load_yaml_block(respect_path)
    design = load_yaml_block(design_path)
    if not isinstance(respect, dict):
        print(f"❌ RESPECT.md YAML 파싱 실패: {respect_path}")
        return 2

    print(f"📋 RESPECT.md: {respect_path}")
    print(f"📋 DESIGN.md:  {design_path}  {'✅' if design else '⚠️  (없음)'}")

    all_errors: list[str] = []
    all_errors.extend(check_respect_required(respect))
    all_errors.extend(check_hierarchy_rules(respect))
    all_errors.extend(check_three_second_rule(respect))
    all_errors.extend(check_next_action(respect))
    cross = check_cross_ref(respect, design or {})
    warnings = [c for c in cross if "warning" in c or "건너뜀" in c]
    cross_errors = [c for c in cross if c not in warnings]
    all_errors.extend(cross_errors)

    if not all_errors and not warnings:
        print("✅ craft-lint 통과 — 위반 0건")
        return 0

    if warnings:
        print(f"\n⚠️  Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if all_errors:
        print(f"\n❌ Errors ({len(all_errors)}):")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    return 1 if args.strict and warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
