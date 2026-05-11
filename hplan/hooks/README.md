# hplan Claude Code Hooks

`gate_guard.py` is a PreToolUse hook that blocks edits on Build Gate artifacts
(`PRD.md`, `AGENTS.md`, `ARCHITECTURE.md`, `IMPLEMENTATION_READINESS.md`,
`METRICS.md`, `specs/NNN-*/`, `.kiro/specs/**`) until the human has approved
`harness/build-gate/checkpoint.json`.

## Wire In

Add to `.claude/settings.json` in your project:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "python3 $CLAUDE_PROJECT_DIR/hooks/gate_guard.py"
          }
        ]
      }
    ]
  }
}
```

If hplan is installed as a global skill, point the command at the skill path:

```bash
python3 ~/.claude/skills/hplan/hooks/gate_guard.py
```

## Approve The Gate

Create `harness/build-gate/checkpoint.json`:

```json
{
  "status": "approved",
  "approved_by": "human operator",
  "approved_at": "2026-05-11",
  "evidence_gate": "approved",
  "product_gate": "approved",
  "cogs_sentinel": "GREEN"
}
```

The hook reads only `status`. The other fields document why.

## One-Off Bypass

```bash
CLAUDE_HPLAN_BYPASS=1 claude
```

The hook prints a warning to stderr but exits 0. Use this only for emergencies.

## Test

```bash
echo '{"tool_input": {"file_path": "docs/PRD.md"}}' | python3 hooks/gate_guard.py; echo "exit=$?"
```

Without approval → exit 2 + blocked message.
With `harness/build-gate/checkpoint.json` status=approved → exit 0.
