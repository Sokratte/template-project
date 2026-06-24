<!-- file: 2026-06-18-011-readme-documentation-pass.md · keywords: session, README, documentation pass, skeleton files, soft-wrap, SPEC-002, bootstrap -->

# Session 11 — README documentation pass + skeleton-file slimming

**Date:** 2026-06-18
**Project:** template-project
**Goal:** Remove comment-headers from skeleton files (loaded every session = token cost), move the documentation into one README per directory, and make every skeleton file self-explanatory in one line.

## What was done

**Verify (carried from last session, FIND item):** Confirmed the new filesystem layout. Workspace root is `~/projects/` (not `~/workspace/`); filesystem MCP allowed dirs are `/Users/martin/projects` and `/Users/martin/recovery`. `agents_sync.sh` + `recent_sessions.sh` still staged in `template-project/` root (move still open). `sweep-knowledge.py` confirmed gone from git (`git ls-files | grep sweep` empty). Session-10 log does exist. Corrected a stale memory (old `~/workspace/` path) via memory edit.

**OPERATOR.md:** Created `~/projects/OPERATOR.md` with operator profile (the 4 migrated lines), VM facts, timezone Europe/Berlin, persona/autonomy. PII, never committed.

**Skeleton slimming + READMEs (the main work):** Established the pattern — loaded files carry a single self-explanatory comment line (format + counter rule); all explanation moves to a per-directory README which may be as long as needed. Operator preference confirmed mid-session: keep the one line, make it explicit enough for weaker models.
- `agents/memory/` — README written; `procedural.md`, `operational.md`, `historical.md` stripped to one line each (historical keeps its two sweep-marker headings).
- `agents/notes/` — README written (backlog/log split, line format, 20-item alarm, scratchpad limits, lifecycle); three files stripped, data lines kept.
- `agents/commands/` — README written; `session-start.md` had its exec-1/exec-2 preamble removed (it cannot describe its own loading) and now begins at step 1; `session-end.md` soft-wrapped.
- `agents/rules/` — README written; `global.md` soft-wrapped and two stale refs fixed (`AGENTS_override.md`→`AGENTS.override.md`, `docs/session/`→`docs/sessions/`).
- `agents/README.md` — rewritten as an index/map onto the four subfolders.

**Soft-wrap:** Adopted as a general rule (already in AGENTS.md "Personal Convention"). All session-written prose converted to one line per paragraph; data lines unchanged.

**Bootstrap relocation:** exec-1 documented in new `~/projects/README.md`; exec-2 command moved into a freshly-authored canonical header in `~/projects/AGENTS.md`, separated from the brainstorming material by a visible separator (operator prunes the brainstorm half themselves).

**SPEC-002:** Renamed `SPEC-002-dev-mcp-server.md` → `SPEC-XXX-dev-mcp-server.md` and moved out to `~/projects/` (project-foreign; operator will clean up). Confirmed it was linked nowhere.

## State at close

Documentation pass is partway through. `agents/` is fully done (all READMEs + slimmed files). Still open: `docs/*` READMEs (specs, plans, sessions, decisions, research — structure/convention only, not per-file) and the bare-scaffold READMEs (`src/`, `docs/tests/`, `tools/`).

## Findings for next session

- **Duplication risk (raised, not resolved):** the architecture is now described across SPEC-003, `~/projects/README.md`, and several `agents/*/README.md` files, plus the new AGENTS.md header overlaps `global.md` (git rules, quality standards). Belongs to PLAN-002 authoring — decide canonical homes vs. pointers.
- A real system spec is wanted in `template-project/docs/specs/`; SPEC-003 already largely is it. Reconcile rather than write fresh.
- exec-2 now appears both in the new AGENTS.md header and in the brainstorm half below the separator (transitional; operator prunes).
