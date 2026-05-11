#!/usr/bin/env python3
"""hplan MCP server — exposes Product Build Gate primitives to any MCP host.

Why an MCP server in addition to the Claude Code skill:
- Spec-Kit currently lists 30+ agent integrations (Cursor, Windsurf, Codex,
  Gemini CLI, Kiro, Goose, ...). A skill works in Claude Code only.
- MCP lets the same gate enforcement run inside any host. The skill stays
  authoritative for prompt-level rules; this server exposes deterministic tools.

Tools exposed:
- evidence_check(brief): scores Evidence Gate readiness; returns decision + missing
- product_gate(brief): scores Product Gate readiness
- cogs_calc(params): runs the COGS sentinel; returns margin scenarios
- decision_log(entry): appends a build/interview/pivot/hold decision
- exclusion_check(idea): checks idea against the exclusions registry
- handoff(brief, target): writes spec-kit/kiro/gstack/claude export

Install `mcp` (https://pypi.org/project/mcp/) and run
`python3 hplan_mcp/server.py` from the skill root, or register the absolute
path in any MCP host config.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT))

try:
    from mcp.server.fastmcp import FastMCP  # type: ignore
except ImportError:
    print(
        "hplan MCP server requires the `mcp` package.\n"
        "Install with: pip install mcp\n"
        "Then run: python3 hplan_mcp/server.py",
        file=sys.stderr,
    )
    raise

from scripts import cogs_sentinel  # noqa: E402
from scripts import decision_log as decision_log_mod  # noqa: E402
from scripts import exclusions_registry  # noqa: E402
from scripts import export_handoff  # noqa: E402


mcp = FastMCP("hplan")

DATA_ROOT = Path.cwd() / "harness"


@mcp.tool()
def evidence_check(brief: dict) -> dict:
    """Score an Evidence Gate brief.

    Required brief fields: idea, target, hypothesis, alternatives (list),
    interview_notes (str). Returns decision + missing checks.
    """
    from scripts.generate_report import score_diagnosis

    interview_notes = brief.get("interview_notes", "")
    result = score_diagnosis(brief, interview_notes)
    return {
        "gate": "evidence",
        "score": result["score"],
        "decision": result["decision"],
        "missing": result["missing"],
        "breakdown": result["breakdown"],
    }


@mcp.tool()
def product_gate(brief: dict) -> dict:
    """Check Product Gate artifacts. Brief must include keys:
    problem_brief, journey_map, sitemap, design_direction, hypothesis_tree.

    Each value should be a non-empty string or list. Returns missing artifacts.
    """
    required = ["problem_brief", "journey_map", "sitemap", "design_direction", "hypothesis_tree"]
    missing = [k for k in required if not _filled(brief.get(k))]
    decision = "ready" if not missing else "WAITING_FOR_HUMAN"
    return {"gate": "product", "decision": decision, "missing": missing}


@mcp.tool()
def cogs_calc(params: dict) -> dict:
    """Run the COGS sentinel.

    Required: provider, model, tokens_in, tokens_out, calls_per_user_month,
    arpu, paid_conversion, free_abuse_multiplier.
    """
    return cogs_sentinel.run(params)


@mcp.tool()
def decision_log(entry: dict, root: str = ".") -> dict:
    """Append a build/interview/pivot/hold decision to harness/decisions.jsonl."""
    return decision_log_mod.append(Path(root), entry)


@mcp.tool()
def exclusion_check(idea: str, root: str = ".") -> dict:
    """Check whether the idea collides with prior exclusions."""
    return exclusions_registry.check(Path(root), idea)


@mcp.tool()
def handoff(brief: dict, target: str = "all", root: str = ".", force: bool = False) -> dict:
    """Export Build Gate brief to spec-kit/kiro/gstack/claude/all."""
    return export_handoff.export(brief, Path(root).resolve(), [target], force)


def _filled(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return len(value.strip()) >= 12
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return True


if __name__ == "__main__":
    mcp.run()
