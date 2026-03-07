# Contributing to AI_PM_Skills

Thank you for your interest in contributing!

## Project Structure

```
AI_PM_Skills/
├── oracle/                    # Discovery — what agent to build
│   ├── .claude-plugin/
│   │   └── plugin.json        # Plugin manifest (required)
│   ├── skills/
│   │   ├── opp-tree/SKILL.md
│   │   ├── assumptions/SKILL.md
│   │   └── ...
│   └── commands/
│       ├── discover.md
│       └── validate.md
├── atlas/                     # Strategy — how to architect it
├── forge/                     # Execution — spec and ship
├── argus/                     # Metrics — measure and improve
├── muse/                      # PM tacit knowledge management
├── evals/                     # Trigger eval queries + benchmark data
│   ├── evals.json             # Quality eval definitions
│   ├── trigger-evals.json     # Trigger accuracy queries (96 total)
│   └── per-skill/             # Per-skill eval files
├── eval-workspace/            # Eval run outputs + benchmark results
├── README.md                  # English
├── README-ko.md               # Korean (한국어)
├── progress.md                # Phase-by-phase progress log
└── CONTRIBUTING.md            # This file
```

## File Conventions

### SKILL.md Format

```markdown
---
name: skill-name-in-kebab-case
description: "One-line English description"
---

# Skill Title

> Korean one-line description (한국어 요약)

## 개념 (Concept)
Korean explanation of the core idea

## Instructions
English instructions with $ARGUMENTS variable
```

**Key rules:**
- `name` in frontmatter = directory name (kebab-case)
- `description` in English (for GitHub discoverability)
- Concept section in Korean (for primary audience)
- Instructions in English (for LLM execution quality)
- Always include `$ARGUMENTS` as the user input variable
- Keep skill names **short and intuitive** (e.g., `kpi`, `moat`, `prd`)

### Command Format

```markdown
---
description: "One-line English description with 'Use when...' trigger pattern"
---

# /command-name

> Korean description (한국어 요약)

## Instructions
Multi-phase workflow that references skills by name.
Use "invoke the X skill" rather than listing skills in frontmatter.
```

**Note:** Command frontmatter only supports `description:` as an official field. Do not use `skills:` or `name:` — these are not recognized by Claude Code.

### Plugin Manifest (plugin.json)

Each plugin has a `.claude-plugin/plugin.json` manifest (not PLUGIN.md):

```json
{
  "name": "plugin-name",
  "version": "0.3.0",
  "description": "Discovery-oriented description with 'Use when...' trigger phrases",
  "author": {
    "name": "Your Name",
    "url": "https://github.com/yourname"
  },
  "repository": "https://github.com/yourname/your-repo",
  "license": "MIT",
  "keywords": ["agent", "pm", "your-domain-keywords"],
  "skills": "./skills/",
  "commands": "./commands/"
}
```

## Naming Convention

### Plugin Names — Greek Mythology Archetypes

Each plugin is named after a Greek mythological figure whose archetype maps to a phase of the agent product lifecycle:

| Plugin | Archetype | Phase | Why |
|--------|-----------|-------|-----|
| **oracle** | Oracle of Delphi (the seer) | Discovery | Reveals which agent to build |
| **atlas** | Atlas (the titan) | Architecture | Bears the structural weight of design |
| **forge** | Hephaestus's Forge | Execution | Crafts raw ideas into specs |
| **argus** | Argus Panoptes (100-eyed) | Monitoring | Watches every metric and failure |
| **muse** | The Muses | Knowledge | Transforms experience into wisdom |

Rules for new plugin names: (1) the metaphor must be instantly intuitive, (2) must work as a single-word CLI namespace.

### Skill Names — Short Functional Handles

**Skills** use short, functional names that anyone can understand at a glance (e.g., `kpi` not `agent-key-performance-indicators`, `3-tier` not `three-tier-orchestrator-architecture`).

Good examples: `prd`, `moat`, `cost-sim`, `premortem`, `hitl`

## How to Contribute

### Adding a New Skill

1. Choose the right plugin (oracle / atlas / forge / argus / muse)
2. Create directory: `[plugin]/skills/[skill-name]/SKILL.md`
3. Follow the SKILL.md format above
4. Add a trigger eval query to `evals/per-skill/[skill-name].json` (2 positive + 2 negative)
5. If the skill chains with others, update or create a Command

### Improving Existing Skills

- Fix instructions that produce poor LLM outputs
- Add missing edge cases or anti-patterns
- Improve examples and templates
- Translate or improve Korean/English sections

## PM-Framework Note

The `muse` plugin provides frameworks for managing PM tacit knowledge. **Frameworks** (TK structure, decision patterns) are open source. **Data** (your personal TK entries in `PM-ENGINE-MEMORY.md`) is yours and should never be committed.

## Questions?

Open an issue or reach out to [@sanguinekim](https://github.com/sanguinekim).
