#!/usr/bin/env bash
# install-hooks.sh — Install hplan git pre-commit hook (dual-defense layer).
#
# Why: Claude Code PreToolUse hook (#17688) is intermittently unreliable.
# Git pre-commit is deterministic — no model behavior dependency.
# Role split:
#   gate_guard.py  → soft warning when Claude attempts the write (UX layer)
#   pre-commit     → hard block before the commit lands (enforcement layer)
#
# Usage:
#   bash scripts/install-hooks.sh          # install
#   bash scripts/install-hooks.sh --remove # uninstall

set -euo pipefail

HOOK_PATH=".git/hooks/pre-commit"
MARKER="# hplan-gate-guard"

remove_hook() {
  if [ ! -f "$HOOK_PATH" ]; then
    echo "hplan: no pre-commit hook found — nothing to remove."
    exit 0
  fi
  if grep -q "$MARKER" "$HOOK_PATH" 2>/dev/null; then
    rm "$HOOK_PATH"
    echo "hplan: pre-commit hook removed."
  else
    echo "hplan: pre-commit hook exists but was not installed by hplan — leaving it."
  fi
  exit 0
}

if [ "${1:-}" = "--remove" ]; then
  remove_hook
fi

if [ ! -d ".git" ]; then
  echo "Error: run from the root of a git repository."
  exit 1
fi

if [ -f "$HOOK_PATH" ] && ! grep -q "$MARKER" "$HOOK_PATH" 2>/dev/null; then
  echo "Warning: existing pre-commit hook found (not from hplan)."
  echo "         Rename it to pre-commit.local and re-run, or chain manually."
  exit 1
fi

cat > "$HOOK_PATH" << 'HOOK'
#!/usr/bin/env bash
# hplan-gate-guard — git pre-commit enforcement layer.
# Blocks commits that include Build Gate artifacts (PRD.md, specs/*, etc.)
# unless harness/build-gate/checkpoint.json shows status="approved".

MARKER="# hplan-gate-guard"

GUARDED_RE="(PRD\.md|AGENTS\.md|ARCHITECTURE\.md|IMPLEMENTATION_READINESS\.md|METRICS\.md|specs/[0-9]{3}-|\.kiro/specs/)"
CHECKPOINT="harness/build-gate/checkpoint.json"

STAGED=$(git diff --cached --name-only 2>/dev/null)
GUARDED=$(echo "$STAGED" | grep -E "$GUARDED_RE" || true)

if [ -z "$GUARDED" ]; then
  exit 0
fi

# Bypass: CLAUDE_HPLAN_BYPASS=1 in environment
if [ "${CLAUDE_HPLAN_BYPASS:-}" = "1" ]; then
  echo "hplan pre-commit: bypass via CLAUDE_HPLAN_BYPASS=1" >&2
  exit 0
fi

# Read checkpoint from the staged index (not working tree) to prevent bypass via
# unstaged approved checkpoint. git show :path reads the index blob.
STAGED_CHECKPOINT=$(git show ":$CHECKPOINT" 2>/dev/null)

if [ -z "$STAGED_CHECKPOINT" ]; then
  echo "" >&2
  echo "hplan pre-commit BLOCKED ──────────────────────────" >&2
  echo "  Staged files require Build Gate approval:" >&2
  echo "$GUARDED" | sed 's/^/    /' >&2
  echo "  Missing from index: $CHECKPOINT" >&2
  echo "  Stage the approved checkpoint first: git add $CHECKPOINT" >&2
  echo "  Run /hplan \"<idea>\" to complete the gate first." >&2
  echo "────────────────────────────────────────────────────" >&2
  exit 1
fi

# Parse status and context_dates from staged blob (python3 or awk fallback)
if command -v python3 &>/dev/null; then
  read -r STATUS FRESHNESS_VERDICT <<< "$(python3 -c "
import json, sys
from datetime import date

THRESHOLDS = {
    'customer_interviews':  90,
    'competitive_analysis': 90,
    'provider_pricing':     60,
    'market_size':          180,
}

try:
    d = json.loads('''$STAGED_CHECKPOINT''')
    status = d.get('status', '')
    today = date.today()
    blocked = []
    for field, limit in THRESHOLDS.items():
        val = (d.get('context_dates') or {}).get(field, '')
        if val:
            try:
                age = (today - date.fromisoformat(val)).days
                if age > limit:
                    blocked.append(f'{field} ({age}d > {limit}d limit)')
            except ValueError:
                pass
    verdict = 'block:' + '|'.join(blocked) if blocked else 'ok'
    print(status, verdict)
except Exception:
    print('', 'ok')
" 2>/dev/null)"
  )"
else
  STATUS=$(echo "$STAGED_CHECKPOINT" | awk -F'"' '/"status"/{print $4; exit}')
  FRESHNESS_VERDICT="ok"
fi

if [ "$STATUS" != "approved" ]; then
  echo "" >&2
  echo "hplan pre-commit BLOCKED ──────────────────────────" >&2
  echo "  Staged files require Build Gate approval:" >&2
  echo "$GUARDED" | sed 's/^/    /' >&2
  echo "  checkpoint.json status = \"$STATUS\" (need \"approved\")" >&2
  echo "  Run /hplan \"<idea>\" to complete the gate first." >&2
  echo "────────────────────────────────────────────────────" >&2
  exit 1
fi

# Freshness check against staged checkpoint context_dates
if [[ "$FRESHNESS_VERDICT" == block:* ]]; then
  STALE=$(echo "$FRESHNESS_VERDICT" | sed 's/^block://' | tr '|' '\n')
  echo "" >&2
  echo "hplan pre-commit BLOCKED ──────────────────────────" >&2
  echo "  Stale context_dates in staged checkpoint:" >&2
  echo "$STALE" | sed 's/^/    /' >&2
  echo "  Re-gather the stale evidence and re-run /hplan." >&2
  echo "────────────────────────────────────────────────────" >&2
  exit 1
fi

exit 0
HOOK

chmod +x "$HOOK_PATH"
echo "hplan: pre-commit hook installed at $HOOK_PATH"
echo "       To remove: bash scripts/install-hooks.sh --remove"
