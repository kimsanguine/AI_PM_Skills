---
description: "Manage the append-only Do-Not-Build exclusions registry — add an exclusion with reopen_trigger, or check whether a new idea collides with prior exclusions."
argument-hint: "[add|check|list] <idea or phrase>"
allowed-tools: ["Read", "Write", "Bash"]
---

# /hplan-exclude

Manage the **append-only exclusions registry** at `harness/exclusions.jsonl`.

## Sub-commands

### `add` — record a Do-Not-Build with reason + reopen trigger

```bash
python3 hplan/scripts/exclusions_registry.py add "범용 PRD 생성기" \
  --why "GitHub Spec-Kit이 30개 agent + 93K stars로 점유" \
  --reopen "Spec-Kit이 evidence gate를 추가하거나 enterprise compliance 인터뷰 3건+" \
  --competitor "GitHub Spec-Kit" --competitor "Kiro"
```

### `check` — collision detect for a new idea

```bash
python3 hplan/scripts/exclusions_registry.py check "범용 PRD 자동 생성 도구"
```

Returns `COLLISION` if Jaccard (token or char-bigram) ≥ 0.40, with `guidance` to confirm `reopen_trigger` or pivot.

### `list` — dump all exclusions

```bash
python3 hplan/scripts/exclusions_registry.py list
```

## When to use

- **`add`** — after every `pivot` or `hold` decision in `/hplan-build`
- **`check`** — at the very start of `/hplan-evidence`, before scoring
- **`list`** — onboarding a new PM or quarterly review

## Routing

- After `add` → consider `decision-log log --decision hold/pivot`
- After `check` returns COLLISION → if `reopen_trigger` unmet, exit Evidence Gate

## Boundary

Exclusions are append-only. Wrong entries are not deleted — instead, write a new entry that supersedes the old one (`why: "supersedes ex-..."`).
