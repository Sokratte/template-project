<!-- kw: doc format conversion, line-1 index, abstract, Created Updated Status, ADR not immutable, supersede in place, spec status Draft Active Superseded, docs README, templates -->
2026-06-18-013-doc-format-conversion.md

# Session 13 — Document format conversion + format refinements

**Goal:** Convert the remaining docs (ADRs, SPECs, research) to the line-1
index format, write docs/README.md, remove the template files, and resolve
several format questions that surfaced mid-conversion.

## What was done

**ADRs.** Restored the date field carelessly dropped in session 12. ADR-001
and ADR-002 now carry the metadata block; ADR-000 template moved to `.trash`.

**SPECs.** SPEC-000 (template) moved to `.trash`. SPEC-001 and SPEC-003
brought to the agreed spec shape: line-1 keyword index, `**Status:**` only in
the head, goal folded into the standalone abstract (no separate `## Goal`),
`Related ADR` dropped to prose. First attempt used the wrong head (Date /
Milestone / Applies-to / Goal section) — corrected to the session-12 widget
form after operator caught it.

**docs/README.md.** Written as the single source of truth for the document
format — previously the format only lived in a chat widget. Contains: the
three read moves (`head -qn1` index, `awk` abstract, `grep` section map), the
line-1 convention, the abstract rule, the two document classes, and the
canonical template block for all five doc types. This is what makes the
"don't go re-read the old chat" problem go away for good.

**Research doc** converted to `# Research:` head, `**Scope:**` only, abstract
as the short answer, stray `---` removed.

**Format refinements decided this session (operator-driven):**
- Line-1 wording fixed everywhere: "this file's entry in the directory index",
  not "the keyword index across all X" (the latter implied one file holds every
  doc's keywords).
- ADRs are **not immutable**. Changed by supersede-in-place (mark the old
  passage, set Status, append a dated `## Addendum`) — never silent rewrite;
  check blast radius first. Legal-text amendment model.
- Unified head for ADR / SPEC / PLAN: **Status, then Created · Updated**, in
  that order. `**Date:**` replaced by `**Created:** · **Updated:**`. PLAN
  gained a Status field.
- **Spec status reduced to Draft | Active | Superseded.** "Done" was
  ambiguous (document-finished vs. code-implemented). Status now tracks the
  *document* only; implementation progress lives in ROADMAP / work-backlog
  (one fact, one home). "Move to specs/archive when done" removed entirely —
  a spec is the living reference, it does not get archived for being
  implemented. SPEC-001 Done → Active.

## Open / carry-forward

- [x] ADRs, SPECs, research doc converted; docs/README.md written; templates trashed
- [ ] PLAN-001 / PLAN-002 still in the old format — no line-1 index, no Status,
      `**Last updated:**` (not `**Updated:**`), a `**Topic:**` field. Not in
      scope this session; align in a later pass.
- [ ] Session logs (02–11) still in old format — operator deferred (01 may stay short)
- [ ] Other docs/* READMEs + bare-scaffold READMEs (src/, docs/tests/, tools/) — backlog
- [ ] Concrete per-file token thresholds for skeleton files — backlog

## Git

Committed + pushed per project settings. See CHANGELOG [Unreleased].
