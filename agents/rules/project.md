# agents/rules/project.md | project rules, conventions, tech stack, local overrides

This file holds rules and conventions that are specific to *this project* — things that apply to every session here but do not belong in the workspace-wide `AGENTS.md` or in the operator profile.

Loaded at every session start alongside `AGENTS.override.md`. On any conflict with
`AGENTS.md`, this file wins (same scope as the override).

---

## What belongs here

- Project-specific workflow conventions not covered by `AGENTS.md`
- Tech-stack rules (language, framework, toolchain decisions that affect how the agent works — e.g. "always use pnpm, never npm", "migrations require a down step")
- Naming conventions, folder conventions, test conventions for this codebase
- Anything the agent must remember about *this project* that is not a memory entry
  (procedural.md) and not an operator preference (OPERATOR.md)

## What does not belong here

- Operator preferences → `OPERATOR.md`
- Decisions and rationale → `docs/decisions/`
- One-off gotchas and learned lessons → `agents/memory/procedural.md`
- Workspace-wide rules → `AGENTS.md`

---

## Rules

*(Fill in as the project matures. Delete this placeholder section once the first rule is added.)*
