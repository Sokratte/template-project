# agents/ — machinery

Everything the agent loads to work in this repo: its memory, its session procedures, the work ledger, the scratchpad, and the workspace rules. This folder holds the *how of the work*, never project content — the *what* lives in `docs/`, `src/`, and `ROADMAP.md`.

Each subfolder has its own README with the full detail. This page is just the map.

| Subfolder | What it holds | Read its README for |
|-----------|---------------|---------------------|
| `memory/` | Procedural rules, operational gotchas, retired history | The three-tier memory model, decay, the recall-counter system |
| `notes/` | Scratchpad + the work ledger (backlog / log) | The backlog/log split, line format, the 20-item alarm, scratchpad limits |
| `commands/` | `session-start.md`, `session-end.md` — executable procedures | When each runs and why every step is non-negotiable |
| `rules/` | `global.md` — workspace-wide working rules | How the craft rules relate to the override and the operator profile |

## Naming: `agents/` vs `AGENTS.md`

`AGENTS.md` (the cross-tool instruction file, at the project root) is the *instructions* — how the agent works in general. `agents/` (this folder) is the *machinery* — the files those instructions operate on. Two different things that happen to share a word; the folder keeps its plain lowercase name.

## What is deliberately NOT here

The **operator profile** — who the operator is and how they like to work — is not in this tree at all. It lives in `~/projects/OPERATOR.md`: per-operator, per-VM, never committed, because it is PII. `memory/procedural.md` holds procedural rules only.

## Full specification

The complete definition of this system — every file, limit, and procedure, and the reasoning behind them — is the system spec in `docs/specs/` (SPEC-003). The multi-VM file model (the canonical `AGENTS.md`, the override, `OPERATOR.md`, the sync script) is described there and in `~/projects/README.md`. Read the spec for the durable picture; the plans under `docs/plans/` are short-lived task records, not the reference.
