<!-- file: 2026-06-18-012-document-conventions.md · keywords: document templates, line-1 index, head -qn1, abstract convention, keywords as relationship graph, no Related fields, ADR-002, traffic-light, decay sweep removed, recent_sessions project name -->

# Session 12 — Document conventions + size governance

**Date:** 2026-06-18
**Project:** template-project
**Goal:** Settle the document conventions for the five doc types (session, research, decision, plan, spec) and decide how document size is governed.

## What was done

**Line-1 index convention.** Settled a single uniform rule for all five document types: line 1 is `filename | keywords`, and the abstract is everything from line 1 down to the first `##`. Read with `head -qn1 docs/<type>/*.md` (a lexicon-style index — filename points to the file, keywords say what it is about), `awk '/^## /{exit}` for a file's abstract, `grep '^#'` for a section map. The filename must be in line 1 because the index is read without headers, so a bare keyword line could not be opened. KISS: one structure, no per-type special case, nothing to drift.

**References dropped.** Removed all `Related:` fields (spec had "Related ADR", plan had "Related"). Bidirectional links need two-sided upkeep, break on rename/archive, and rot silently. Keywords are the self-healing, undirected, cross-type relationship graph instead; a genuinely needed directed relationship is written as prose where it belongs, not as a field that promises completeness.

**Size governance → ADR-002.** Decided the model: two document classes by load behaviour. Skeleton files (loaded in full every start) are governed; content files (read by index/abstract/section) have no size limit, because a cap would force cutting content the read mechanism already handles. Governance is a language-level yellow/red traffic-light — yellow informs, red halts at session start and forces a prune-or-defer decision that recurs until resolved. No automatic deletion or movement. The recall counter `[YYYY-MM-DD xN]` is kept, but its role shifts from algorithm-input to human reading-aid. Metric is tokens; concrete per-file thresholds deferred.

**Decay sweep removed.** The deterministic operational-memory sweep (old SPEC-003 §8.5) is superseded by the human-decided pruning above — a machine cannot judge the special case (twenty rules found in one day; assessment needs time). Pruning is now an operator act, guided by the counters.

**Files written.**
- `ADR-002-document-size-governance.md` — new, in the new format.
- `ADR-001` — converted to the new format (line-1 index + abstract); dropped its date field.
- `SPEC-003` — updated §4, §7.3, §8.2–8.5, §9.1–9.2, §10 (Document Budgets → Document System, two classes + traffic-light table).
- `session-start.md` / `session-end.md` — traffic-light checks replace hard limits; sweep step replaced by operator-decided pruning; line-1 format updated.
- `recent_sessions.sh` — now prints the project name from the path (3 newest sessions) for project selection, not `head -1` prose; "what happened last" dropped.

## State at close

Conventions and size-governance model are decided and recorded. Templates exist only as a chat widget — not written to disk as `*-template.md` (operator decision). ADR-000/SPEC-000/001 and the older session/research docs still carry the old line-1 format.

## Findings for next session

- Ripple-edit existing docs to the new line-1 format (backlog).
- Write `docs/README.md` documenting the convention, read-commands, two classes, and keywords-as-graph (backlog).
- Define concrete per-file token thresholds for skeleton files — ADR-002 fixes the model but defers the numbers (backlog).
- Open question raised but not resolved: whether to restore a decision-date line into ADR abstracts (the new format dropped the date field).
