<!-- file: 2026-06-24-031-introduce-doc-type.md · keywords: session, new document type, introduce doc type, TEST chain, ADR SPEC PLAN TEST, PLAN-003, kw rename, revert -->

# Session 031 — Introduce doc type & kw rename

**Status:** Completed
**Goal:** Rename kw: → keywords: repo-wide; write a plan for introducing a new document type.

## keywords: rename across all docs

121 occurrences, 46 files. Token renamed in all headers (line-1 + section-level), 4 session logs converted from pipe-form to comment form, spec sources updated (session-start, session-end, PLAN-002). Committed `50175e9`.

## PLAN-003 — procedure for introducing a new document type

Six-step procedure for adding a doc type: register in `docs/README.md` (tables + template), create directory + README, declare place in ADR → SPEC → PLAN → TEST chain, name any workflow hook separately. TEST type used as worked example. Committed `9e5ffee`.

## Open / carry-forward

- [ ] Overshot the task mid-session: built a full test suite + gate before writing the plan. Reverted (`c99cbbd`, `f9ae4bc`). Lesson: scope creep from "plan" to "build" without sign-off.
- [ ] Memory baselines revisit still open (was due session 030).
- [ ] `~/projects/README.md` still describes stale startup scripts — backlog item open.

## Git

Commits: 50175e9 (kw rename), revert pair (c99cbbd/f9ae4bc), b032874 (header fixes), 9e5ffee (PLAN-003). Status: clean, pushed.
