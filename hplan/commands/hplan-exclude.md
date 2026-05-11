---
description: "Manage the append-only Do-Not-Build exclusions registry — add an exclusion with reopen_trigger, or check whether a new idea collides with prior exclusions. Use when adding a Do-Not-Build entry to permanent memory, or when checking whether a new idea collides with prior exclusions."
argument-hint: "[add|check|list] <idea or phrase>"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-exclude


## Instructions

You manage the **hplan exclusions registry** for: **$ARGUMENTS**

### Decide sub-command
- If user is recording a Do-Not-Build → `add`
- If user is checking a new idea → `check`
- If listing → `list`

### add
`python3 hplan/scripts/exclusions_registry.py add "<idea>" --why "<reason>" --reopen "<trigger>" --competitor "<name>" [--competitor "<name>"]`. Require `--reopen` to be an action-shaped condition (e.g., "enterprise compliance interviews 3+"), not vague.

### check
`python3 hplan/scripts/exclusions_registry.py check "<idea>"`. Threshold 0.40 by default. If COLLISION, confirm reopen_trigger met before proceeding with other gates.

### list
`python3 hplan/scripts/exclusions_registry.py list` — dump JSONL.

## Output Format

For `add`:

1. **id** — `ex-YYYY-MM-DD-XXXXX`
2. **exclusion text**, **why**, **reopen_trigger**, **competitors**

For `check`:

1. **verdict** — COLLISION or CLEAR
2. **matches** — array of prior exclusions with overlap score
3. **guidance** — next action
