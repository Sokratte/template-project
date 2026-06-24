<!-- keywords: doc consistency tests, test doc type, TEST-NNN, executable checks, dead refs, kw residual, session-end integration, structural over procedural -->
PLAN-003-doc-consistency-tests.md

# PLAN-003: Documentation Consistency Tests

**Status:** Plan ready
**Created:** 2026-06-24 · **Updated:** 2026-06-24

Session 030 closed by hand-grepping for dead `SPEC-003` references, leftover `kw:` tokens, and a corrupted code line. Those checks were correct but manual, so the next drift will go unnoticed until someone happens to look. This plan introduces the structural fix the operator's own principle demands: turn the recurring manual audit into executable checks, and add a lightweight document type that registers each check and records its last run. The split is deliberate — executable code does the testing; the doc only registers and reports. A markdown file that merely *describes* tests would be theatre, not a test.

## Goal

A committed `tests/test_docs.py` that fails on the drift classes we keep hitting (dead doc-type references, residual `kw:`/old-format tokens, malformed line-1 headers), plus a TEST document type that registers each check with its rationale and last-run status, plus a session-end hook so the suite runs before close.

## Non-goals

- NOT a general link-checker for external URLs — only intra-repo doc-type references (ADR/SPEC/PLAN/DP-NNN) and format invariants.
- NOT testing project source code — this suite covers documentation invariants only; real-code tests live beside the code they exercise.
- NOT replacing human review — the suite catches the mechanical, repeatable failures, freeing review for judgement.

## Design — two artifacts, one boundary

The executable check is the test. `tests/test_docs.py` walks the repo (excluding `.trash/`) and asserts the invariants, importing nothing it copies — it reads the live files. Each assertion is a named function so a failure points at the exact invariant. Checks at launch: (1) no living doc references a doc-type id whose file is absent; (2) zero residual `kw:` or `filename | keywords` pipe-headers outside `.trash/`; (3) every governed file's line 1 is a `<!-- keywords: … -->` comment with the bare filename on line 2.

The TEST doc type is the registry, not the test. One file per suite at `docs/tests/TEST-NNN-topic-slug.md`, head block like the other governed types (`**Status:**`, `**Created:** · **Updated:**`), listing each check as a content heading stating what it guarantees and why, plus the command to run it and the last-run result. Status vocabulary subset: Draft · Active · Superseded → (mirrors SPEC — a test suite is a living target). This keeps the *why* in prose (token-economy: out of the code) and the *what* executable.

## Execution checklist

- [ ] Write `tests/test_docs.py` with the three checks above, each a named function, reading live files, excluding `.trash/`.
- [ ] Run it against current repo — must pass (Session 030 already cleaned the drift).
- [ ] Register the TEST doc type in `docs/README.md`: types table row, status subset, a template block following the line-1 + hidden-keyword rules, and the structural-vs-content note.
- [ ] Write `docs/tests/TEST-001-doc-consistency.md` registering the three checks.
- [ ] Add a session-end step in `agents/commands/session-end.md`: run the doc suite before the commit step; a red result blocks close until fixed or explicitly deferred.
- [ ] Update CHANGELOG.

## Acceptance criteria

The suite exists, runs green on a clean repo, and fails when a doc-type reference is broken or a `kw:` token reappears (verify by temporarily reintroducing each defect). The TEST type is registered in `docs/README.md` and discoverable like every other type. session-end runs it automatically.
