<!-- kw: file limits, HTML comment, hidden metadata, soft hard, H1 cleanup -->
2026-06-23-023-limits-into-comments.md

# Session 023 — Move file limits from H1 into HTML comments

**Status:** In Progress
**Goal:** Move soft/hard word limits from H1 title text into HTML comments on line 2, invisible in Obsidian/MkDocs, still greppable in source.

Abstract: The `· soft: N · hard: M` suffix clutters rendered headings in every Markdown viewer. The fix is the same pattern already used for keywords: `<!-- soft: N · hard: M -->` on the line immediately after the H1.

## File limits moved to HTML comments <!-- kw: -->

All 10 skeleton files patched: H1 stripped of `· soft: N · hard: M` suffix; `<!-- soft: N · hard: M -->` written on the line immediately after the H1. Invisible in Obsidian/MkDocs/GitHub, greppable in source. Same pattern as `<!-- kw: -->` on line 1 of content docs.

Files: AGENTS.override.md, project.md, personal.md, procedural.md, scratchpad.md, work-backlog.md, session-start.md, ROADMAP.md, ~/projects/AGENTS.md, ~/projects/LOCAL.md.

`~/projects/AGENTS.md` § File limits description updated to document the new comment format.

## Open / carry-forward <!-- kw: -->

- [x] Limits moved to HTML comments on all skeleton files

## Git <!-- kw: -->

Commits: see below · Status: clean, pushed
