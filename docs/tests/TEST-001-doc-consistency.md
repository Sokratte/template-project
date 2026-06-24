<!-- keywords: doc consistency, dead refs, kw residual, pipe header, line-1 header, executable checks, session-end gate -->
TEST-001-doc-consistency.md

# TEST-001: Documentation Consistency

**Status:** Active
**Created:** 2026-06-24 · **Updated:** 2026-06-24
**Suite:** `tests/test_docs.py` · **Run:** `python3 -m pytest tests/test_docs.py`

The drift this suite catches is the kind Session 030 had to find by hand: a retired document still referenced elsewhere, a renamed header token left behind in one file, a malformed line-1 index. Each is mechanical, repeatable, and invisible until someone greps for it. The checks below run on the live tree (excluding `.trash/`) so the audit happens every session instead of by luck.

## No legacy `kw:` header token survives <!-- keywords: kw token, rename residual -->

Guarantees that the keyword-header token is `keywords:`, never the old `kw:`, in any header form (`<!-- kw:` or a `filename | kw:` line). Prose may still discuss the migration. Catches a half-finished rename. Function: `test_no_kw_token_residual`.

## No pipe-form line-1 header survives <!-- keywords: pipe header, line-1 format -->

Guarantees no file starts with the superseded `filename | keywords` pipe form; all headers are the `<!-- keywords: … -->` comment. Catches a file that missed the format migration. Function: `test_no_pipe_form_headers`.

## Content docs carry the keywords-comment header <!-- keywords: content doc, header, bare filename -->

Guarantees every numbered/dated content doc (decisions, specs, plans, philosophy, research, sessions, tests — excluding READMEs and `-000` templates) has line 1 `<!-- keywords: … -->` and line 2 the bare filename. Catches a wrong or missing filename anchor (e.g. a copy-pasted log header). Function: `test_content_docs_line1_is_keywords_comment`.

## No dead doc-type references <!-- keywords: dead ref, ADR SPEC PLAN DP -->

Guarantees no living doc references an `ADR/SPEC/PLAN/DP-NNN` (NNN ≥ 001) whose file is absent. History (session logs, CHANGELOG, work-log), code blocks, backtick spans, and `-000` template placeholders are exempt. Catches a reference left dangling after a doc is retired or renamed. Function: `test_no_dead_doctype_references`.

## Last run <!-- keywords: last run, result -->

2026-06-24 · green (4/4) · Session 031, after introducing the suite and fixing the drift it found (session-030 pipe header, session-028 wrong filename anchor).
