#!/usr/bin/env python3
"""hplan gate guard — Claude Code PreToolUse hook.

Why this exists:
- SKILL.md has 22 "Do Not" rules but they live at prompt level. A determined
  agent can rationalize past them.
- This hook intercepts Write/Edit on `**/PRD.md`, `**/AGENTS.md`, `**/ARCHITECTURE.md`,
  `**/IMPLEMENTATION_READINESS.md`, and similar Build Gate artifacts.
- If `harness/build-gate/checkpoint.json` does not have `status: "approved"`,
  the hook BLOCKS the tool call with a clear WAITING_FOR_HUMAN message.

Wire it in `.claude/settings.json`:

  {
    "hooks": {
      "PreToolUse": [
        {
          "matcher": "Write|Edit",
          "hooks": [{
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/hooks/gate_guard.py"
          }]
        }
      ]
    }
  }

Claude Code hooks contract (2026): stdin = JSON event, exit 2 = block.
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import date
from pathlib import Path


# Context freshness thresholds (days). Based on AI market velocity research.
# warn_after / block_after — absent context_dates field = skip (backward-compat).
FRESHNESS_THRESHOLDS: dict[str, dict[str, int]] = {
    "customer_interviews":  {"warn": 60,  "block": 90},
    "competitive_analysis": {"warn": 45,  "block": 90},
    "provider_pricing":     {"warn": 30,  "block": 60},
    "market_size":          {"warn": 90,  "block": 180},
}

GUARDED_PATTERNS = [
    re.compile(r"(^|/)PRD\.md$", re.I),
    re.compile(r"(^|/)AGENTS\.md$", re.I),
    re.compile(r"(^|/)ARCHITECTURE\.md$", re.I),
    re.compile(r"(^|/)IMPLEMENTATION_READINESS\.md$", re.I),
    re.compile(r"(^|/)METRICS\.md$", re.I),
    re.compile(r"specs/\d{3}-", re.I),       # spec-kit
    re.compile(r"\.kiro/specs/", re.I),        # kiro
]


def is_guarded(path: str) -> bool:
    return any(p.search(path) for p in GUARDED_PATTERNS)


def check_freshness(project_dir: Path) -> tuple[str, list[str], list[str]]:
    """Check context_dates in checkpoint.json against FRESHNESS_THRESHOLDS.

    Returns (verdict, warnings, blocks):
      verdict = 'ok' | 'warn' | 'block'
      warnings = list of warn-level messages
      blocks   = list of block-level messages
    Absent context_dates = 'ok' (backward-compatible with existing checkpoint.json).
    """
    cp = project_dir / "harness" / "build-gate" / "checkpoint.json"
    if not cp.exists():
        return "ok", [], []
    try:
        data = json.loads(cp.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return "ok", [], []

    context_dates = data.get("context_dates")
    if not context_dates:
        return "ok", [], []

    today = date.today()
    warnings: list[str] = []
    blocks: list[str] = []
    for key, thresholds in FRESHNESS_THRESHOLDS.items():
        raw = context_dates.get(key)
        if raw is None:
            continue
        try:
            age = (today - date.fromisoformat(raw)).days
        except ValueError:
            continue
        if age >= thresholds["block"]:
            blocks.append(
                f"{key}: {age}d old — block threshold {thresholds['block']}d exceeded"
            )
        elif age >= thresholds["warn"]:
            warnings.append(
                f"{key}: {age}d old — warn threshold {thresholds['warn']}d exceeded"
            )

    if blocks:
        return "block", warnings, blocks
    if warnings:
        return "warn", warnings, []
    return "ok", [], []


def gate_approved(project_dir: Path) -> tuple[bool, str, dict]:
    """Return (approved, reason, data). data is the full checkpoint dict."""
    cp = project_dir / "harness" / "build-gate" / "checkpoint.json"
    if not cp.exists():
        return False, f"missing {cp.relative_to(project_dir)}", {}
    try:
        data = json.loads(cp.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, f"checkpoint.json is invalid JSON: {e}", {}
    status = data.get("status")
    if status == "approved":
        return True, "", data
    return False, f"checkpoint.json status = {status!r} (need 'approved')", data


def check_conditional_scope(data: dict, target: str) -> tuple[str, str]:
    """Enforce CONDITIONAL_GO write-time restrictions.

    Returns ('ok', '') or ('block', reason).
    Absent decision field = treat as GO (backward-compatible).
    """
    decision = data.get("decision", "GO")
    if decision != "CONDITIONAL_GO":
        return "ok", ""

    # Expiry check
    expires_at = (data.get("expires_at") or "").strip()
    if expires_at:
        try:
            if date.today() > date.fromisoformat(expires_at):
                return "block", (
                    f"CONDITIONAL_GO expired on {expires_at}.\n"
                    "  Re-run /hplan to reassess or obtain full GO approval."
                )
        except ValueError:
            pass

    # Scope check: if allowed_paths is non-empty, target must be in scope
    allowed: list[str] = data.get("allowed_paths") or []
    if allowed:
        norm = target.replace("\\", "/")
        in_scope = any(
            norm.endswith(p.lstrip("/")) or p.lstrip("/") in norm
            for p in allowed
        )
        if not in_scope:
            conditions = data.get("conditions") or []
            cond_str = "\n    ".join(conditions) if conditions else "(none listed)"
            return "block", (
                f"CONDITIONAL_GO: write is outside allowed scope.\n"
                f"  Allowed paths: {allowed}\n"
                f"  Target:        {norm!r}\n"
                f"  Outstanding conditions:\n    {cond_str}\n"
                "  Resolve all conditions first or obtain full GO approval."
            )

    return "ok", ""


def main():
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    tool_input = event.get("tool_input") or {}
    target = tool_input.get("file_path") or tool_input.get("path") or ""
    if not target:
        return 0

    target_norm = target.replace("\\", "/")
    if not is_guarded(target_norm):
        return 0

    project_dir = Path(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()).resolve()
    bypass = os.environ.get("CLAUDE_HPLAN_BYPASS") == "1"

    if bypass:
        print("hplan gate guard: bypass via CLAUDE_HPLAN_BYPASS=1", file=sys.stderr)
        return 0

    # --- Freshness check ---
    freshness_verdict, fresh_warns, fresh_blocks = check_freshness(project_dir)
    if freshness_verdict == "warn":
        for w in fresh_warns:
            print(f"hplan freshness ⚠️  {w}", file=sys.stderr)
    elif freshness_verdict == "block":
        lines = ["hplan gate guard BLOCKED: context data is stale."]
        for b in fresh_blocks:
            lines.append(f"  🚫 {b}")
        lines.append(
            "Update context_dates in harness/build-gate/checkpoint.json "
            "and re-run /hplan to refresh the gate."
        )
        print("\n".join(lines), file=sys.stderr)
        return 2

    # --- Approval check ---
    ok, reason, cp_data = gate_approved(project_dir)
    if not ok:
        print(
            f"hplan gate guard BLOCKED write to {target_norm}\n"
            f"reason: {reason}\n"
            "This file is a Build Gate artifact. Before editing:\n"
            "  1. Run hplan Evidence Gate + Product Gate.\n"
            "  2. Approve harness/build-gate/checkpoint.json (status='approved').\n"
            "  3. Or set CLAUDE_HPLAN_BYPASS=1 in your shell for one explicit override.\n"
            "Per SKILL.md: WAITING_FOR_HUMAN.",
            file=sys.stderr,
        )
        return 2

    # --- CONDITIONAL_GO scope check (only when approved) ---
    scope_verdict, scope_reason = check_conditional_scope(cp_data, target_norm)
    if scope_verdict == "block":
        print(
            f"hplan gate guard BLOCKED: CONDITIONAL_GO scope violation.\n{scope_reason}",
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
