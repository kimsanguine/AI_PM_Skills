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
from pathlib import Path


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


def gate_approved(project_dir: Path) -> tuple[bool, str]:
    cp = project_dir / "harness" / "build-gate" / "checkpoint.json"
    if not cp.exists():
        return False, f"missing {cp.relative_to(project_dir)}"
    try:
        data = json.loads(cp.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return False, f"checkpoint.json is invalid JSON: {e}"
    status = data.get("status")
    if status == "approved":
        return True, ""
    return False, f"checkpoint.json status = {status!r} (need 'approved')"


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
    ok, reason = gate_approved(project_dir)
    if ok:
        return 0

    msg = (
        f"hplan gate guard BLOCKED write to {target_norm}\n"
        f"reason: {reason}\n"
        "This file is a Build Gate artifact. Before editing:\n"
        "  1. Run hplan Evidence Gate + Product Gate.\n"
        "  2. Approve harness/build-gate/checkpoint.json (status='approved').\n"
        "  3. Or set CLAUDE_HPLAN_BYPASS=1 in your shell for one explicit override.\n"
        "Per SKILL.md: WAITING_FOR_HUMAN."
    )
    if os.environ.get("CLAUDE_HPLAN_BYPASS") == "1":
        print("hplan gate guard: bypass requested via CLAUDE_HPLAN_BYPASS=1", file=sys.stderr)
        return 0
    print(msg, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
