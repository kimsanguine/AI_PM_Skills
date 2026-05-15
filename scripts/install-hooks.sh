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

# Parse status, context_dates, and CONDITIONAL_GO fields from staged blob.
if command -v python3 &>/dev/null; then
  read -r STATUS FRESHNESS_VERDICT SCOPE_VERDICT <<< "$(python3 -c "
import json, sys, os
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

    # --- Freshness ---
    blocked_fresh = []
    for field, limit in THRESHOLDS.items():
        val = (d.get('context_dates') or {}).get(field, '')
        if val:
            try:
                age = (today - date.fromisoformat(val)).days
                if age > limit:
                    blocked_fresh.append(f'{field} ({age}d > {limit}d limit)')
            except ValueError:
                pass
    freshness = 'block:' + '|'.join(blocked_fresh) if blocked_fresh else 'ok'

    # --- CONDITIONAL_GO scope (commit-time checks) ---
    decision = d.get('decision', 'GO')
    scope = 'ok'
    if decision == 'CONDITIONAL_GO':
        # Expiry
        expires_at = (d.get('expires_at') or '').strip()
        if expires_at:
            try:
                if today > date.fromisoformat(expires_at):
                    scope = f'expired:{expires_at}'
            except ValueError:
                pass
        # Required tests must exist on disk
        if scope == 'ok':
            missing = [
                t for t in (d.get('required_tests') or [])
                if not os.path.exists(t)
            ]
            if missing:
                scope = 'missing_tests:' + '|'.join(missing)

    print(status, freshness, scope)
except Exception:
    print('', 'ok', 'ok')
" 2>/dev/null)"
  )"
else
  STATUS=$(echo "$STAGED_CHECKPOINT" | awk -F'"' '/"status"/{print $4; exit}')
  FRESHNESS_VERDICT="ok"
  SCOPE_VERDICT="ok"
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

# CONDITIONAL_GO scope checks
if [[ "$SCOPE_VERDICT" == expired:* ]]; then
  EXP_DATE=$(echo "$SCOPE_VERDICT" | sed 's/^expired://')
  echo "" >&2
  echo "hplan pre-commit BLOCKED ──────────────────────────" >&2
  echo "  CONDITIONAL_GO expired on $EXP_DATE." >&2
  echo "  Re-run /hplan to reassess or obtain full GO approval." >&2
  echo "────────────────────────────────────────────────────" >&2
  exit 1
fi

if [[ "$SCOPE_VERDICT" == missing_tests:* ]]; then
  MISSING=$(echo "$SCOPE_VERDICT" | sed 's/^missing_tests://' | tr '|' '\n')
  echo "" >&2
  echo "hplan pre-commit BLOCKED ──────────────────────────" >&2
  echo "  CONDITIONAL_GO requires these test files to exist:" >&2
  echo "$MISSING" | sed 's/^/    /' >&2
  echo "  Create the required tests before committing." >&2
  echo "────────────────────────────────────────────────────" >&2
  exit 1
fi

exit 0
HOOK

chmod +x "$HOOK_PATH"
echo "hplan: pre-commit hook installed at $HOOK_PATH"
echo "       To remove: bash scripts/install-hooks.sh --remove"
