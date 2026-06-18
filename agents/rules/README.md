# agents/rules/ — workspace-wide working rules

The standing rules for *how the agent works* on this machine — workflow, the laws of editing, quality standards, simplicity discipline. These are not project content and not memory; they are the craft rules that apply to every task in every project, the same way on each.

| File | Holds | Loaded |
|------|-------|--------|
| `global.md` | Workspace-wide default rules: the task workflow, session-log discipline, the editing laws, quality standards, simplicity-first | Read at orientation; the project may tighten them via `AGENTS.override.md` |

## How these relate to the override

`global.md` sets the workspace defaults. A project that needs stricter or more specific rules states them in its `AGENTS.override.md`, and on any conflict the override wins. The base rules here are deliberately general — anything project-specific belongs in the override or in that project's own docs, not in this file.

## Why a separate rules file at all

Three kinds of "how to behave" could blur together, so they are kept apart on purpose:

- **`agents/rules/global.md`** — the craft rules: how to work, in general, on any task. Stable, rarely changed.
- **`agents/memory/procedural.md`** — rules this specific project's agent follows automatically, loaded every session. Project-bound.
- **`~/projects/OPERATOR.md`** — who the operator is and how they like to work. Person-bound, never committed.

The test for where a rule goes: is it about *the craft* (here), *this project* (procedural memory), or *this person* (operator file)?

## Editing global.md

Rarely changed, and changed deliberately. Several of its entries exist because the rule was once violated and caused real damage — treat them as scar tissue, not suggestions. When a rule here overlaps with something stated in `~/projects/AGENTS.md`, they must not drift apart; prefer one canonical home and a pointer over two copies.
