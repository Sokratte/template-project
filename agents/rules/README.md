# agents/rules/ — working rules

Rules for *how the agent works* — project-specific conventions, workspace craft rules.
Two files, two scopes:

| File | Scope | Loaded |
|------|-------|--------|
| `project.md` | This project only — tech stack, naming conventions, local workflow rules | Every session start (in the startup call) |
| `global.md` | *(merged into `~/projects/AGENTS.md`; moved to `.trash`)* | n/a |

## Where rules live

- **`agents/rules/project.md`** — rules specific to *this project*. Anything the agent
  must know about how to work here that is not a memory entry and not an operator
  preference. Committed; travels with the clone.
- **`~/projects/AGENTS.md`** — workspace-wide craft rules (workflow, editing laws, quality
  standards). Fixed; not changed per-project.
- **`agents/memory/procedural.md`** — learned lessons and gotchas for this project.
  Grows over time; pruned when stale.
- **`~/projects/OPERATOR.md`** — who the operator is and how they like to work.
  Person-bound; never committed.

The test for where a rule goes: is it about *this project's craft* (project.md), *this
workspace in general* (AGENTS.md), *a learned lesson* (procedural.md), or *this person*
(OPERATOR.md)?
