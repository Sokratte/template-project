<!-- file: 2026-06-23-021-agents-md-overhaul.md · keywords: AGENTS.md overhaul, tbh-era cruft, global.md stale pointer, pointer pattern, agents README -->

# Session 021 — AGENTS.md Overhaul: stale pointers & tbh-era cruft

**Status:** In Progress
**Goal:** Find and fix all stale `global.md` pointers and tbh-era cruft in living docs. Verify AGENTS.md itself is clean.

Abstract: `global.md` was merged into `~/projects/AGENTS.md` in session 14 and moved to `.trash`. Two living files still reference it: `agents/README.md` (rules/ table row) and `docs/plans/PLAN-002` (three-tier read model table). Fix both surgically. AGENTS.md itself is already clean.

## Stale global.md pointers removed <!-- keywords: -->

**AGENTS.md (`~/projects/AGENTS.md`):** already clean — no `global.md` refs, no tbh-era sections. No changes needed.

**`agents/README.md` table row:** `rules/` row described `global.md` (merged+trashed session 14). Updated to reflect actual contents: `personal.md` (operator profile, gitignored) + `project.md` (project-specific rules).

**`docs/plans/PLAN-002` three-tier read table:** "Orient on demand" row had `agents/rules/global.md` as the source. Updated to `~/projects/AGENTS.md` (where those rules now live).

**Remaining `global.md` hits:** 2 — `work-backlog` (this task, now closed) and `docs/research/mcp-file-tool-design.md` line 154 (research archive, not an actionable pointer). Both left as-is.

**tbh-era cruft:** none found. Grep across living docs returned zero hits for `tbh`.

## Open / carry-forward <!-- keywords: -->

- [x] AGENTS.md overhaul complete

## Git <!-- keywords: -->

Commits: see below · Status: clean, pushed
