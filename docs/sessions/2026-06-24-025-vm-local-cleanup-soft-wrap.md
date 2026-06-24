<!-- file: 2026-06-24-025-vm-local-cleanup-soft-wrap.md · keywords: session, vm-local, cleanup, soft-wrap, readme-pass -->

# Session 025 — VM.local cleanup + README pass

**Status:** Completed
**Goal:** Trash stale VM.local copy-files; copy current ~/projects files in; write missing READMEs for docs/*, src/, tools/.

## VM.local refreshed

All stale `copy`-named files moved to `.trash/VM.local/`. Current `~/projects/` files (`AGENTS.md`, `LOCAL.md`, `README.md`, `agents_sync.sh`, `projects_list.sh`) copied into `VM.local/` under correct names. Committed and pushed.

## README pass

Written: `docs/decisions/`, `docs/specs/`, `docs/plans/`, `docs/sessions/`, `docs/research/`, `src/`, `tools/`. All follow line-1 `<!-- keywords: -->` + bare-filename convention. `docs/philosophy/` discovered and written in session 027.

## Git

Commits: df91a6a (VM.local), 138d27b (READMEs). Status: clean, pushed.
