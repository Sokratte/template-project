<!-- keywords: session, AGENTS.md, authoring, startup flow, document-read model, PLAN-001, PLAN-002 -->
2026-06-17-009-agents-md-authoring.md

# 2026-06-17 · template-project · session 09

**Task:** Continue PLAN-001 follow-through: repair the uncommitted folder
restructure, then begin authoring the canonical AGENTS.md — settle the
startup flow and document-read model before drafting prose.

**Outcome:** Repo restructure committed (old `.claude/`→`agents/` layout
migration). AGENTS.md content decisions locked and captured in a new PLAN-002;
no AGENTS.md prose written yet (deliberately — design first). ROADMAP updated.

---

## Done

- **Repo fixed.** Committed the on-disk restructure as moves: old layout
  (`.claude/`, root `AGENTS.md`, `changelog/session-logs/`, `tests/`) removed,
  new layout (`agents/`, `docs/sessions/`, `docs/specs/`, `tools/`) tracked.
  Tree clean.
- **PLAN-002 written** (`docs/plans/PLAN-002-agents-md-authoring.md`) and
  registered in ROADMAP. Captures all content decisions below.

## Decided (the substance of the session)

- **Startup = two exec calls.** Exec-1: `agents_sync.sh && cat AGENTS.md &&
  ls ~/projects/*/`. Select project (folder-derived list). Exec-2: one call
  reading the guaranteed startup set.
- **Three-tier read model:** load-whole (override, .project, procedural,
  session-start), load-partial (ROADMAP abstract+active, work-backlog
  complete), orient-on-demand (global.md/SPECS by heading-grep; PLANS/
  RESEARCH/SESSIONS by abstract). exec-2 carries only files every project is
  guaranteed to have; optional material is conditional inside session-start.
- **Abstract convention:** everything above the first `##`. Terminator is
  `##` not `---` — chosen on failure cost (a forgotten `---` makes awk read
  the whole file; a forgotten `##` ~never happens). No fixed line count.
- **awk section-reading:** large specs/plans are NOT split into files —
  sectioned at read time (abstract → heading map → one section). Keeps
  orientation cheap at any doc size.
- **work-backlog / work-log split** (rename + contract fix): old `worklog.md`
  conflated "what happened" with "open TODOs/findings", burying TODOs.
  Resolution: `worklog.md`→`work-backlog.md` (open items only, read complete,
  alert >20 items); `worklog-archive.md`→`work-log.md` (done, append-only,
  grep on demand). "Append-only" belongs to work-log, not the backlog.

## Open / next session

- **Decide first:** rename work-backlog/work-log now, or after drafting
  AGENTS.md? (Leaning rename-first ~65%.)
- Then execute PLAN-002: draft AGENTS.md prose (sign-off each step), settle
  autonomy level names + default, persona placement (global vs override),
  line budget.
- Ripple edits in PLAN-002 checklist: SPEC-003 contract fix, CREATE_PROJECT
  budgets, session-start/session-end rewrite, README phantom ref, sweep
  script removal.

## State at close

CHANGELOG `[Unreleased]` updated. Two commits this session (restructure;
PLAN-002+ROADMAP). Tooling note: sandbox tools can't see the real FS — use
filesystem MCP for all project files. session-end.md procedure itself is
stale (old paths) — fix is in PLAN-002.
