# agents/ — machinery

Everything the agent loads to work in this repo: its memory, its session procedures, the work ledger, the scratchpad, and the workspace rules. This folder holds the *how of the work*, never project content — the *what* lives in `docs/`, `src/`, and `ROADMAP.md`.

Each subfolder has its own README with the full detail. This page is just the map.

| Subfolder | What it holds | Read its README for |
|-----------|---------------|---------------------|
| `memory/` | Procedural rules, operational gotchas, retired history | The three-tier memory model, decay, the recall-counter system |
| `notes/` | Scratchpad + the work ledger (backlog / log) | The backlog/log split, line format, the 20-item alarm, scratchpad limits |
| `commands/` | `session-start.md`, `session-end.md` — executable procedures | When each runs and why every step is non-negotiable |
| `rules/` | `personal.md` (operator profile, gitignored), `project.md` (project-specific rules) | When to add a rule here vs. in the override or AGENTS.md |

## Naming: `agents/` vs `AGENTS.md`

`AGENTS.md` (the cross-tool instruction file, at the project root) is the *instructions* — how the agent works in general. `agents/` (this folder) is the *machinery* — the files those instructions operate on. Two different things that happen to share a word; the folder keeps its plain lowercase name.

## What is deliberately NOT here

The **operator profile** — who the operator is and how they like to work — is not in this tree at all. It lives in `~/projects/LOCAL.md`: per-operator, per-VM, never committed, because it is PII. `memory/procedural.md` holds procedural rules only.
