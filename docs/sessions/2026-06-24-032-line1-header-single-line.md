<!-- file: 2026-06-24-032-line1-header-single-line.md · keywords: line-1 header, Z1/Z2 retired, single-line file+keywords, option A, head -1 index, exec-independent, basename vs path, README path, docs README rule source, template migration, session log headers -->

# Session 032 — Line-1 header: Z1/Z2 → single-line

**Status:** Completed
**Goal:** Replace the two-line line-1/line-2 header (`<!-- keywords: … -->` then bare filename) with a single-line self-identifying header `<!-- file: name.md · keywords: … -->` across all living files and session-log headers. Make the index work without exec, with the filename carried in the harvested line itself.

Abstract: Operator established that the Z1/Z2 convention only yields a path→keyword mapping when an exec-run `for`-loop explicitly emits the path; a path-less read tool (or a tool-restricted operator who gives the agent no exec) breaks it. Fix is structural: fold the filename into the keyword HTML comment so one harvested line is self-identifying regardless of tool. Z2 bare filename retired ersatzlos. Rule source is docs/README.md; no ADR (Z1/Z2 was never ADR-ratified).

## Migrated all docs to the single-line self-identifying header <!-- keywords: migration, 51 files, basename vs path, README path, docs README rewrite -->

- **Format:** `<!-- file: <filename> · keywords: … -->`, separator `·`, standardised on `keywords:` (retired stray `kw:`). Bare line-2 filename removed.
- **`file:` value:** bare basename where unique; repo-relative path where not (the 9 READMEs would otherwise all read `file: README.md`). Verified zero basename collisions across all `file:` values.
- **Scope migrated (51 headers):** all 49 `docs/` files (ADR-001/002, DP-000, SPEC-001/002, PLAN-001/002/003, 3 research, all 31 session logs — header only, narrative untouched) + `src/README.md` + `tools/README.md`.
- **Not affected:** `agents/` and `VM.local/` use H1 + `<!-- soft·hard -->` headers, never the keyword-index convention. `docs/runbooks/README.md` is a plain H1. `.github/` issue templates use YAML frontmatter.
- **`docs/README.md`:** rewrote the Line-1 rule + corrected the now-false rationale; documented the basename-vs-path uniqueness rule; updated all 6 type templates to Option A. (Also fixed a self-inflicted duplicated-section block from a full-file rewrite before switching to exec-based anchor edits.)
- **Prose references updated:** `session-start.md` steps 3+4, `session-end.md`, `PLAN-003` step 3. Historical CHANGELOG/PLAN-002 entries left intact (they correctly describe the past); new CHANGELOG entry added.

## Process notes — write the destination first, verify every write <!-- keywords: exec rediscovered, full-rewrite mistake, timeout, verification -->

- **`macbook-mcp:exec` was available all along.** First tool_search (query "filesystem") returned only read/write wrappers; concluded exec was absent and rewrote docs/README.md as a full 26 KB overwrite — which duplicated a section. Loading the full toolset surfaced exec; switched to in-place `sed`/python anchor edits. Lesson: load the full toolset before concluding a capability is missing.
- **write_file/exec ~4 min timeout** recurred (scratchpad s30): a CHANGELOG heredoc call hung. Recovered by read-verify (entry was NOT written) then re-applying idempotently via `tools/_tmp.py`. Heredocs via exec mostly worked this session but the timeout is real — `_tmp.py` is the safer path.

## Open / carry-forward <!-- keywords: carry-forward -->

- [x] Z1/Z2 → single-line migration complete and verified.
- [ ] Memory baselines revisit (carried from s030/031) — still open.

## Git <!-- keywords: git -->

Commits: (this session) · Status: pushed
