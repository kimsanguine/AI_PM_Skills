# hplan MCP Server

This wraps hplan's deterministic helpers as MCP tools so any MCP-compatible host
(Cursor, Windsurf, Kiro, Codex, Goose, Claude Desktop, ...) can call the same
Product Build Gate primitives that the Claude Code skill uses.

## Install

```bash
pip install mcp
```

## Run

From the skill root directory:

```bash
python3 hplan_mcp/server.py
```

> The local package is named `hplan_mcp/` (not `mcp/`) to avoid shadowing the
> installed `mcp` PyPI package.

## Register

### Claude Desktop / Claude Code

`~/.claude/mcp.json` (or via `claude mcp add`):

```json
{
  "mcpServers": {
    "hplan": {
      "command": "python3",
      "args": ["/absolute/path/to/hplan/skills/hplan/hplan_mcp/server.py"]
    }
  }
}
```

### Cursor / Windsurf / Kiro / Goose

Each host has its own MCP config file but the schema is the same — point
`command` at `python3` and `args` at the `server.py` path.

## Tools

| Tool | Purpose |
|---|---|
| `evidence_check(brief)` | Score Evidence Gate readiness |
| `product_gate(brief)` | Check Product Gate artifacts |
| `cogs_calc(params)` | Run COGS sentinel — p50/p90 margin scenarios |
| `decision_log(entry)` | Append build/interview/pivot/hold decision |
| `exclusion_check(idea)` | Match against append-only exclusions registry |
| `handoff(brief, target)` | Export to spec-kit / kiro / gstack / claude |

## Design Note

The MCP server intentionally exposes **deterministic** primitives only. Prompt-level
gate rules (the 22 "Do Not" rules in `SKILL.md`) stay in the skill — the MCP server
gives every host *measurable* checks, not opinions.
