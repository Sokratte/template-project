# agents/rules/ — working rules

Two files, two scopes. Both loaded at every session start.

| File | Scope | Committed |
|------|-------|-----------|
| `project.md` | This project — tech stack, naming conventions, local workflow rules | ✅ Yes |
| `personal.md` | Operator preferences, working style, signal phrases, anti-patterns | ❌ No (person-bound) |

## `project.md`

Rules specific to this project. Anything the agent must know about how to work here that is not a learned lesson (`agents/memory/procedural.md`) and not a workspace-wide rule (`~/projects/AGENTS.md`). Committed; travels with every clone.

## `personal.md`

Operator profile and preferences. Person-bound — never committed. The test: if a rule is about *this person's* working style, it goes here. If it's about *this project's craft*, it goes in `project.md`.
