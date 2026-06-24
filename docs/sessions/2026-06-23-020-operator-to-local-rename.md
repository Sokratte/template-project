<!-- keywords: OPERATOR.md rename, LOCAL.md, repo-wide, grep, sed, bulk edit -->
2026-06-23-020-operator-to-local-rename.md

# Session 020 — OPERATOR.md → LOCAL.md rename

**Status:** In Progress
**Goal:** Rename all occurrences of `OPERATOR.md` to `LOCAL.md` across the repo — file references in prose, code blocks, and the one actual file if it exists.

Abstract: Bulk text-replacement across the template-project repo. The file `LOCAL.md` already exists at the workspace root; `OPERATOR.md` is the old name still referenced in docs, agents files, and session logs.

## OPERATOR.md → LOCAL.md renamed across all living docs <!-- keywords: -->

Dry-run first: `grep -rn 'OPERATOR\.md'` returned 93 hits across 28 files. Categorised into living documents (update) vs. historical session logs + CHANGELOG + work-log (leave as-is — they record what the name was at the time).

73 replacements applied across 11 living files: README.md, CREATE_PROJECT.md, agents/README.md, agents/commands/README.md, agents/notes/scratchpad.md, agents/notes/work-backlog.md, SPEC-003, PLAN-001 (28 hits), PLAN-002 (15 hits), research/context-budget, session-017.

Zero hits remain in living docs. Backlog item moved to work-log. Scratchpad carry-forward line removed. Session-019 checkbox ticked.

Side-effect: the backlog item's own description was itself renamed (`LOCAL.md -> LOCAL.md`). Extracted the correct text from the file and removed it cleanly.

## Open / carry-forward <!-- keywords: -->

- [x] OPERATOR.md → LOCAL.md rename complete

## Git <!-- keywords: -->

Commits: see below · Status: clean, pushed
