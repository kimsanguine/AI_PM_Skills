#!/usr/bin/env python3
"""validate_docs.py — Deterministic cross-reference validator for hplan projects.

Runs three checks that catch the drift patterns observed in production:

  1. Path existence   — every file path declared in docs/ must exist on disk
  2. Price consistency — price/plan tokens must come from a single source file
  3. Condition coverage — every CONDITIONAL_GO condition must have a
                          @pytest.mark.hplan_condition tag in a test file

Run after gate generation or on every docs/ change (add to pre-commit or CI).

Usage:
    python3 hplan/scripts/validate_docs.py [--root <project-root>] [--check <name>]
    python3 hplan/scripts/validate_docs.py --json

Checks:
    path_existence     File paths referenced in docs/ (Implementation anchor,
                       Verified by, AGENTS.md, CLAUDE.md references) exist on disk.
    price_consistency  All price tokens ($X / ₩X,XXX) are consistent across docs/.
    condition_coverage Each CONDITIONAL_GO condition has a matching pytest mark.

Exit codes:
    0  — all checks pass
    1  — one or more checks failed
    2  — usage error
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

_DOC_EXTENSIONS = {".md", ".txt", ".rst", ".yaml", ".yml"}
_TEST_EXTENSIONS = {".py"}

# Patterns that declare a file path inside docs
_PATH_ANCHOR_RE = re.compile(
    r"(?:"
    r"\*\*(?:Implementation anchor|Verified by|implementation_anchor|verified_by)\*\*"  # bold fields
    r"|anchor:|verified_by:"                                                              # yaml-style
    r")\s*[:`]?\s*`?([^\s`\n]+\.[a-zA-Z]{1,6}(?:::[^\s`\n]+)?)`?",                      # path[::]
    re.IGNORECASE,
)

# Price tokens: $99, $49/mo, ₩135,000, ₩135,000/월 etc.
_PRICE_RE = re.compile(r"(?:\$[\d,]+(?:/\w+)?|₩[\d,]+(?:/\w+)?)")

# CONDITIONAL_GO condition lines in checkpoint.json
_CONDITION_RE = re.compile(r'"([^"]{5,})"')  # strings of 5+ chars in conditions list

# pytest mark for condition coverage
_PYTEST_MARK_RE = re.compile(
    r'@pytest\.mark\.hplan_condition\(\s*["\']([^"\']+)["\']'
)


def collect_docs(root: Path) -> list[Path]:
    """All doc files under docs/ (and specs/ if present)."""
    targets = [root / "docs", root / "specs", root / "harness"]
    files: list[Path] = []
    for base in targets:
        if base.is_dir():
            for p in base.rglob("*"):
                if p.is_file() and p.suffix.lower() in _DOC_EXTENSIONS:
                    files.append(p)
    return files


def collect_tests(root: Path) -> list[Path]:
    tests_dir = root / "tests"
    if not tests_dir.is_dir():
        return []
    return [p for p in tests_dir.rglob("*.py") if p.is_file()]


# ---------------------------------------------------------------------------
# Check 1: Path existence
# ---------------------------------------------------------------------------

def check_path_existence(root: Path) -> list[dict]:
    """Return list of findings: {doc, declared_path, exists}."""
    findings: list[dict] = []
    for doc in collect_docs(root):
        text = doc.read_text(encoding="utf-8", errors="ignore")
        for m in _PATH_ANCHOR_RE.finditer(text):
            raw = m.group(1)
            # Strip ::function suffix if present
            file_part = raw.split("::")[0].strip("`")
            candidate = (root / file_part).resolve()
            if not candidate.exists():
                findings.append({
                    "doc": str(doc.relative_to(root)),
                    "declared_path": file_part,
                    "exists": False,
                })
    return findings


# ---------------------------------------------------------------------------
# Check 2: Price consistency
# ---------------------------------------------------------------------------

def check_price_consistency(root: Path) -> list[dict]:
    """Detect duplicate conflicting price tokens across docs.

    A 'conflict' is two different price values for the same plan keyword.
    Strategy: find all (plan_keyword, price) pairs; flag when the same keyword
    maps to more than one price.
    """
    # Patterns like "Pro: $99" / "Pro plan ₩135,000" / "Starter $49"
    _PLAN_PRICE_RE = re.compile(
        r"(\bPro\b|\bStarter\b|\bFree\b|\bEnterprise\b|\bBasic\b)"
        r"[^\n$₩]{0,20}"
        r"(\$[\d,]+(?:/\w+)?|₩[\d,]+(?:/\w+)?)",
        re.IGNORECASE,
    )

    plan_prices: dict[str, dict[str, list[str]]] = {}  # plan → {price → [docs]}
    for doc in collect_docs(root):
        text = doc.read_text(encoding="utf-8", errors="ignore")
        rel = str(doc.relative_to(root))
        for m in _PLAN_PRICE_RE.finditer(text):
            plan = m.group(1).lower()
            price = m.group(2)
            plan_prices.setdefault(plan, {}).setdefault(price, []).append(rel)

    findings: list[dict] = []
    for plan, price_map in plan_prices.items():
        if len(price_map) > 1:
            findings.append({
                "plan": plan,
                "prices_found": {p: docs for p, docs in price_map.items()},
            })
    return findings


# ---------------------------------------------------------------------------
# Check 3: Condition coverage
# ---------------------------------------------------------------------------

def _load_conditions(root: Path) -> list[str]:
    """Read CONDITIONAL_GO conditions from checkpoint.json."""
    cp = root / "harness" / "build-gate" / "checkpoint.json"
    if not cp.exists():
        return []
    try:
        data = json.loads(cp.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    if data.get("decision") != "CONDITIONAL_GO":
        return []
    return data.get("conditions") or []


def _load_marked_conditions(root: Path) -> set[str]:
    """Collect all @pytest.mark.hplan_condition values from test files."""
    marked: list[str] = []
    for tf in collect_tests(root):
        text = tf.read_text(encoding="utf-8", errors="ignore")
        for m in _PYTEST_MARK_RE.finditer(text):
            marked.append(m.group(1))
    return set(marked)


def check_condition_coverage(root: Path) -> list[dict]:
    """Return conditions that lack a @pytest.mark.hplan_condition test."""
    conditions = _load_conditions(root)
    if not conditions:
        return []
    marked = _load_marked_conditions(root)
    findings: list[dict] = []
    for cond in conditions:
        # Fuzzy match: condition substring in any mark
        covered = any(cond.lower() in mark.lower() or mark.lower() in cond.lower()
                      for mark in marked)
        if not covered:
            findings.append({
                "condition": cond,
                "covered": False,
                "hint": f'Add @pytest.mark.hplan_condition("{cond}") to a test.',
            })
    return findings


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_all(root: Path, checks: list[str]) -> dict:
    results: dict[str, dict] = {}

    if "path_existence" in checks:
        findings = check_path_existence(root)
        results["path_existence"] = {
            "passed": len(findings) == 0,
            "findings": findings,
        }

    if "price_consistency" in checks:
        findings = check_price_consistency(root)
        results["price_consistency"] = {
            "passed": len(findings) == 0,
            "findings": findings,
        }

    if "condition_coverage" in checks:
        findings = check_condition_coverage(root)
        results["condition_coverage"] = {
            "passed": len(findings) == 0,
            "findings": findings,
        }

    return results


def print_report(results: dict, root: Path) -> int:
    all_pass = True
    for check, result in results.items():
        status = "✅ PASS" if result["passed"] else "❌ FAIL"
        print(f"\n{status}  {check}")
        if not result["passed"]:
            all_pass = False
            for f in result["findings"]:
                if check == "path_existence":
                    print(f"  ✗ {f['doc']}: declared path not found → {f['declared_path']}")
                elif check == "price_consistency":
                    print(f"  ✗ Plan '{f['plan']}' has conflicting prices:")
                    for price, docs in f["prices_found"].items():
                        print(f"      {price} ← {', '.join(docs)}")
                elif check == "condition_coverage":
                    print(f"  ✗ {f['hint']}")
    print()
    return 0 if all_pass else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="hplan cross-reference validator")
    parser.add_argument("--root", default=".", help="Project root (default: cwd)")
    parser.add_argument(
        "--check",
        action="append",
        choices=["path_existence", "price_consistency", "condition_coverage"],
        dest="checks",
        help="Run specific check(s). Default: all.",
    )
    parser.add_argument("--json", action="store_true", help="Output JSON instead of human report")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    checks = args.checks or ["path_existence", "price_consistency", "condition_coverage"]

    results = run_all(root, checks)

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0 if all(r["passed"] for r in results.values()) else 1

    return print_report(results, root)


if __name__ == "__main__":
    sys.exit(main())
