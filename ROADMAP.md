# Roadmap · soft: 600 · hard: 1200 (loaded slice only)

> The volatile counterpart to AGENTS.md. Where the project is going —
> current priority, tracks, milestones, active plans. Read at session start
> alongside AGENTS.md. Changes regularly; AGENTS.md stays stable.

## Current priority

Draft the canonical `AGENTS.md` for the multi-VM agent architecture
(PLAN-001), with operator sign-off on every step.

## Tracks

TODO: the parallel lines of work. For each, a one-line statement of where
it stands.

## Milestones

| Milestone | Goal | Status |
|-----------|------|--------|
| v0.1.0 | TODO | planned |

## Active Plans

Plans in progress. Each entry: plan file link, ~50-word abstract written in
plain language (what's missing, what it will achieve, why it matters now —
not technical shorthand). When a plan is done, move the file to
`docs/plans/archive/` and remove it from this table.

| Plan | Abstract |
|------|---------|
| [PLAN-001](docs/plans/PLAN-001-multi-vm-agent-architecture.md) | Architecture for deploying this template across many users' VMs: one canonical `~/projects/AGENTS.md` synced into each project via a visible `agents_sync.sh` (gated by a `.agents_sync` marker), small per-project overrides, file-based configs, provider-agnostic backup with per-repo deploy keys. Design locked; content drafting moved to PLAN-002. |
| [PLAN-002](docs/plans/PLAN-002-agents-md-authoring.md) | Authors the AGENTS.md content PLAN-001 deferred: the two-call startup flow, a three-tier read model (whole / partial / on-demand), a `##`-terminated greppable abstract so large docs are sectioned by awk rather than split into files, and the work-backlog / work-log rename that stops open TODOs being buried under history. Carries the dependent doc renames and cleanup. |

## Registers

TODO: project-specific lists that change over time and have no better home
(risks, budget, key dependencies). If something has a better dedicated home,
put it there — one source of truth per fact.

---
*Volatile by design. Durable rules and structure live in `AGENTS.md`.*
