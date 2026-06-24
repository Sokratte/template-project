<!-- keywords: maisig doc layout review, docs README, templates, doc types, section matrix, implications palette, line-1 format -->
2026-06-23-019-maisig-doc-layout-backport.md

# Session 019 — MAISIG doc layout review & backport assessment

**Status:** In Progress
**Goal:** Review MAISIG's recently upgraded file layout, doc types, and templates — identify what is worth backporting to template-project.

Abstract: Read-only reconnaissance session. MAISIG introduced a full docs/README.md convention system, seven *-000-template.md skeletons, a section vocabulary matrix, status master vocabulary, structural vs. content heading distinction, and an implications palette. Assess fit for template-project; no writes until operator sign-off.

## What was implemented <!-- keywords: -->

All changes in a single commit (4150db1).

**docs/README.md** — full rewrite: line-1 format changed to `<!-- keywords: … -->` + bare filename on line 2; section-level keyword rule documented (`<!-- keywords: -->` on every heading); status master vocabulary table with per-type subsets; structural vs. content heading distinction; section matrix (required/optional/n/a per type); implications palette; DP type added to doc-types table and lifecycle notes; anti-drift rule (copy from template, never from latest file); `Adding a new doc type` section; all inline templates updated to new line-1 + `<!-- keywords: -->` heading format.

**docs/philosophy/** — directory + `archive/` subdirectory created; `DP-000-template.md` skeleton written.

**Line-1 migration** — all docs with existing `filename | keywords` format converted to `<!-- keywords: keywords -->` + filename on line 2: ADR-001, ADR-002, SPEC-001, SPEC-002 (had no line-1 at all — added), SPEC-003, PLAN-001, PLAN-002, sessions 011–017 + 019, research 2026-04-17 + 2026-06-19 × 2. Sessions 001–010 and session-018 (old format, no pipe) remain as-is — covered by existing backlog item.

## Open / carry-forward <!-- keywords: -->

- [x] section-level keywords (`<!-- keywords: -->`) — implemented
- [x] status master vocabulary table — implemented
- [x] `*-000-template` files as separate skeleton files — implemented (DP-000-template.md; ADR/SPEC/PLAN templates remain inline in README per existing design)
- [x] Design philosophy (DP) document type — implemented
- [x] line-1 format migrated to `<!-- keywords: -->` for all migrateable docs
- [ ] Sessions 001–010 + session-018 line-1 migration (existing backlog item)
- [x] `OPERATOR.md → LOCAL.md` rename — done session 020

## Git <!-- keywords: -->

Commits: 4150db1 · Status: clean, pushed
