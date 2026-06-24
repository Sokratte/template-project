<!-- keywords: skeleton file limits, word limits, soft hard, AGENTS.md LOCAL.md, AGENTS.override, session-start, project.md, ROADMAP -->
2026-06-23-022-skeleton-limits.md

# Session 022 — Skeleton-file word limits

**Status:** In Progress
**Goal:** Write soft/hard word limits into all skeleton files that are missing them: AGENTS.override.md, agents/rules/project.md, agents/commands/session-start.md, ROADMAP.md, ~/projects/AGENTS.md, ~/projects/LOCAL.md.

Abstract: Derived from the token thresholds in research/2026-06-19-context-budget-and-file-limits.md (tokens / 1.3 → words). AGENTS.md and LOCAL.md were not in the original research scope; limits set from first principles matching their role.

## Word limits written to all skeleton files <!-- keywords: -->

Derived from `docs/research/2026-06-19-context-budget-and-file-limits.md` (token thresholds ÷ 1.3 → words, rounded). AGENTS.md and LOCAL.md were not in the original research scope; limits set from first principles.

| File | Soft | Hard | Ist now | Note |
|---|---:|---:|---:|---|
| `AGENTS.override.md` | 150 | 300 | 34 | ✅ |
| `agents/rules/project.md` | 400 | 800 | 20 | ✅ |
| `agents/commands/session-start.md` | 400 | 600 | 273 | ✅ |
| `ROADMAP.md` (slice) | 600 | 1200 | 52 | ✅ |
| `~/projects/AGENTS.md` | 1200 | 2000 | 1519 | ⚠️ over soft — stable, no prune pressure |
| `~/projects/LOCAL.md` | 200 | 400 | 70 | ✅ |

AGENTS.md at 1519 words is over its soft limit of 1200 — flagged here, no action taken. The file is stable and rarely touched; a future AGENTS.md Overhaul session is the right moment to tighten it.

Memory-baselines backlog item updated: no practice data yet, revisit trigger set to session 030.

## Open / carry-forward <!-- keywords: -->

- [x] Skeleton limits written to all missing files
- [ ] AGENTS.md over soft (1519w / soft 1200) — address in future AGENTS.md overhaul
- [ ] Memory baselines: revisit at session 030

## Git <!-- keywords: -->

Commits: see below · Status: clean, pushed
