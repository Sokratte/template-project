<!-- file: docs/README.md · keywords: document conventions, line-1 index, section keywords, abstract, awk grep, skeleton vs content, word limits, status vocabulary, section matrix, structural content headings, implications palette, anti-drift, doc types, design philosophy, adding doc type -->

# docs/ — Document conventions

Everything in this folder follows a single structure: **line 1 is the index entry, the abstract runs to the first `##`.** This is uniform across all document types — sessions, research, decisions, plans, specs, and design philosophies.

## Reading conventions <!-- keywords: index, abstract, section map, awk, grep, head -->

**Index a directory** (one line per file, no full reads):
```bash
for f in docs/sessions/*.md; do head -1 "$f"; done
for f in docs/decisions/*.md; do head -1 "$f"; done
```

**Read a file's abstract** (everything before the first `##`):
```bash
awk '/^## /{exit} 1' docs/specs/SPEC-NNN-topic-slug.md
```

**Get a file's section map** (heading outline, keywords included):
```bash
grep -n '^#\+ ' docs/specs/SPEC-NNN-topic-slug.md
```

**Find the right section by keyword** (the section-level index):
```bash
grep -rin 'keywords:.*memory' docs/specs/
```

**Read one section** (e.g. `## Design`):
```bash
awk '/^## Design/{f=1;print;next} f&&/^## /{exit} f' FILE.md
```

These moves — index, abstract, section-map, keyword-grep, section-read — cover every read pattern. Documents are never split into files for size; they are sectioned at read-time and grow as large as they need to.

## Line-1 format <!-- keywords: line 1, filename, keywords, HTML comment, hidden, self-identifying, relationship graph -->

```
<!-- file: filename.md · keywords: keyword keyword keyword -->
```

Line 1 is a single HTML comment carrying both the filename and the keyword index. The comment is invisible in rendered Markdown and fully greppable in source. The filename lives inside the line itself, so one harvested line (`head -1`) is self-identifying: it traces back to its file without depending on the reading tool to emit the path. This works whether the index is built by an exec-run loop, a path-less read tool, or an agent given no exec at all — the line carries its own identity.

The `file:` value is the **bare filename** when that name is unique across the repo (`ADR-001-project-standard.md`, `SPEC-002-dev-mcp-server.md`). When the basename is **not** unique — every directory has its own `README.md` — use the **repo-relative path** instead (`docs/decisions/README.md`, `src/README.md`) so the harvested line still resolves to exactly one file. Uniqueness is the rule; the path is how you buy it where the basename can't.

Keywords are the relationship graph: no `Related:` fields, no bidirectional links. A keyword that appears in two files is the connection. If a directed relationship matters, write it as prose where it belongs.

## Section-level keywords <!-- keywords: section keywords, HTML comment, hidden, uniform rule, grep -->

Section headings carry their own keyword list so a grep can land on the right section of a long document without reading the whole file:

```
## Section title <!-- keywords: term, term, term -->
```

The keywords live inside an HTML comment. Every Markdown renderer drops HTML comments from the rendered page, so the reader sees a clean heading while the terms stay fully greppable in source. **This is the uniform rule: keywords are always hidden in `<!-- keywords: … -->`, everywhere** — line 1 and every section heading. Keywords are noise for the human eye; hiding them costs nothing and keeps rendered docs clean.

## Abstract and head block <!-- keywords: abstract, status, created, updated, head block -->

The abstract is everything from line 1 down to (not including) the first `##` heading. It must stand on its own in the index — one sentence is too little for a 1,000-line spec.

ADRs, specs, and plans open with the same head block in this order — `**Status:**`, then `**Created:** · **Updated:**` — followed by a standalone summary long enough to stand on its own. Sessions and research use a lighter head (see templates below). The terminator is the first `##` — a forgotten `##` is essentially impossible in a structured document, whereas a forgotten `---` delimiter would silently make awk read the whole file.

Do not put a `##` heading inside an abstract.

## Status vocabulary <!-- keywords: status, draft, accepted, active, plan ready, in progress, completed, superseded, deprecated, cancelled -->

One master set; each document type draws only the subset that makes sense for it.

| Status | Meaning |
|--------|---------|
| Draft | being written; revisable |
| Accepted | ratified decision or principle; a past commitment (DP, ADR) |
| Active | ratified living target; code is judged against it (SPEC) |
| Plan ready | ratified, not yet started (PLAN) |
| In Progress | work underway |
| Completed | finished |
| Superseded → X | replaced by newer doc X; left in place, not deleted |
| Deprecated | no longer valid, not replaced |
| Cancelled | abandoned before completion |

| Type | Allowed statuses |
|------|-----------------|
| DP | Draft · Accepted · Superseded → · Deprecated |
| ADR | Draft · Accepted · Superseded → · Deprecated |
| SPEC | Draft · Active · Superseded → |
| PLAN | Draft · Plan ready · In Progress · Completed · Cancelled |
| Research | Draft · Completed · Superseded → |
| Session | In Progress · Completed |

The status field tracks the *document*, never the implementation — implementation progress lives in ROADMAP / work-backlog (one fact, one home). The lone exception is PLAN, whose lifecycle *is* the execution it tracks.

## Structural vs. content headings <!-- keywords: structural headings, content headings, descriptive, vocabulary -->

Two kinds of heading, two rules:

**Structural** headings are navigation scaffolding and use a fixed name from the vocabulary in the section matrix below (Context, Design, Implications, References, …). Uniform on purpose, so the eye and the index find them the same way in every document.

**Content** headings *are* the summary — write the actual thing. A research question is the heading (`## Does gVisor RAM overhead scale with tenant count?`), not `## Question`. A session accomplishment is the heading (`## Conformed all six head blocks`), not `## What was done`. An ADR decision is the heading (`## Boot-start the auditor after reboot`), not `## Decision`. The descriptive heading carries information and doubles as the section keyword index.

## Section matrix <!-- keywords: section matrix, required, optional, context, design, implications, alternatives, references, sources, tenet, principle, horizon, anti-goals, goals -->

Required ✓ · optional ○ · n/a — · *italic = content heading (write the actual thing).*

| Section | DP | ADR | SPEC | PLAN | Research | Session |
|---------|:--:|:---:|:----:|:----:|:--------:|:-------:|
| line-1 + H1 + head + Abstract | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tenet (blockquote) | ✓ | — | — | — | — | — |
| Context | ✓ | ✓ | ○ | ○ | ○ | — |
| Principle | ✓ | — | — | — | — | — |
| *Decision(s)* | — | ✓ | — | ○ | — | — |
| Goals | — | — | ✓ | ○ | — | — |
| Non-goals | — | — | ✓ | ✓ | — | — |
| Anti-Goals | ✓ | ○ | — | — | — | — |
| Design | — | — | ✓ | ○ | — | — |
| Acceptance criteria | — | — | ✓ | ✓ | — | — |
| Execution checklist | — | — | — | ✓ | — | — |
| *Findings* | — | — | — | — | ✓ | ○ |
| *What was done* | — | — | — | — | — | ✓ |
| Implications | ○ | ○ | ○ | ○ | ○ | — |
| Alternatives | — | ✓ | ○ | ○ | ○ | — |
| Open questions | — | ○ | ✓ | ○ | ○ | ✓ |
| Horizon | ✓ | — | — | — | — | — |
| References (internal) | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Sources (external) | ○ | — | — | — | ✓ | — |

Section definitions where not obvious:

- **Tenet** — a one-line pull-quote that nails the philosophy. DP only.
- **Principle** — the affirmative stance of a DP, held to. The load-bearing section.
- **Anti-Goals** — what a philosophy refuses to *become* (a permanent refusal on principle, not a scope boundary). Distinct from Non-goals. "Non-goals" is a scope boundary (what is deliberately not built here, possibly built elsewhere later).
- **Implications** — what a choice makes possible and what it costs. Layout is open; pick freely from the palette below.
- **Horizon** — DP only. What this philosophy opens, where it leads, what it becomes the foundation for.
- **References** vs **Sources** — References are internal repo links; Sources are external prior art (papers, vendor docs). A DP carries no References (it never points down; other documents point up to it) but may carry external Sources.

## Implications palette <!-- keywords: implications, opportunities, risks, benefits, costs, trade-offs -->

No fixed layout — the author picks per document. Non-exhaustive palette:

Paired axes (suggestions, not a rule): Opportunities ↔ Risks · Benefits ↔ Costs · Drivers ↔ Obstacles · Strengths ↔ Weaknesses · Gains ↔ Losses · Upsides ↔ Downsides · Advantages ↔ Liabilities

Standalone terms: Trade-offs · Dependencies · Constraints · Assumptions · Requirements · Interactions · Consequences · Complications · Failure modes

## Document classes and size governance <!-- keywords: skeleton, content, word limits, never loaded whole -->

| Class | Files | Size |
|-------|-------|------|
| **Skeleton** | `agents/memory/procedural.md`, `AGENTS.override.md`, `agents/commands/session-start.md`, `agents/notes/scratchpad.md`, `agents/notes/work-backlog.md`, ROADMAP active section | Governed by word limits declared in file headers |
| **Content** | Everything in `docs/` | No limit — as long as needed |

Content documents are never loaded whole at session start. The read mechanism (index, abstract, section) handles any size; a cap would force cutting material you need.

## Document types — location and naming <!-- keywords: naming, locations, NNN, dated, templates -->

| Type | Location | Naming | Template |
|------|----------|--------|----------|
| Design philosophy (DP) | `docs/philosophy/` | `DP-NNN-topic-slug.md` | see template below |
| Decision (ADR) | `docs/decisions/` | `ADR-NNN-topic-slug.md` | see template below |
| Specification | `docs/specs/` | `SPEC-NNN-topic-slug.md` | see template below |
| Plan | `docs/plans/` | `PLAN-NNN-topic-slug.md` | see template below |
| Research | `docs/research/` | `YYYY-MM-DD-topic-slug.md` | see template below |
| Session log | `docs/sessions/` | `YYYY-MM-DD-NNN-topic-slug.md` | see template below |

## Using the templates <!-- keywords: anti-drift, copy template, do not copy last file -->

To create a new document, copy the template block below for that type. **Never orient off the most recent file of that type.** Copying the latest file lets the format drift one small, invisible change at a time; over many sessions the result no longer resembles the template. The template is the single source of *shape*; this README is the single source of *rules*.

## Lifecycle notes <!-- keywords: lifecycle, supersede, archive, amend, immutable, append-only -->

**Design philosophy (DP)** — ratified DPs (Status: Accepted) are immutable. To change one, supersede and archive: move the old file to `docs/philosophy/archive/` under its dated name, write a fresh same-numbered DP in the current format, and port the intent. Drafts are revisable until ratified. A DP never references specs, ADRs, or plans — it never points down; other documents point up to it.

**Decision (ADR)** — a durable, append-only record. Typo or small clarification: fix in place, check the blast radius first. Real change of substance: mark the superseded passage `~~SUPERSEDED~~`, set Status, append a dated `## Addendum` explaining what changed and why. The old reasoning stays visible.

**Spec** — the target; defines what "done" looks like. Code that contradicts a spec is a bug. A spec is the living reference and is not archived for being implemented. Draft → Active → Superseded.

**Plan** — a living rebuild guide, not a disposable checklist. Tick steps as done, keep the prose truer than you found it, and move to `docs/plans/archive/` when fully complete.

**Research** — reference material; grepped by keyword, never loaded whole. Archive to `docs/research/archive/` when stale.

**Session log** — created at session start, filled during the work, closed at session end. The technical record: what was done, what broke, what is next.

## Adding a new document type <!-- keywords: extend, new type, flexibility -->

Pick a location and naming pattern (numbered `XXX-NNN` or dated `YYYY-MM-DD-NNN`), choose the status subset from the master vocabulary above, choose sections from the matrix (or add a new structural section here first), write a template block in this file following the line-1 and hidden-keyword rules, and register the type in the table above.

## Templates <!-- keywords: templates, ADR, SPEC, PLAN, research, session, DP -->

The canonical shape of each type — copy the block, keep the structure. **Never copy from the most recent file of that type — always copy from here.**

### Design philosophy (DP)

```
<!-- file: DP-NNN-topic-slug.md · keywords: keyword keyword keyword -->

# DP-NNN: Title

**Status:** Draft | Accepted | Superseded → DP-NNN | Deprecated
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract: the principle in one paragraph — what it holds, why it matters.

> Tenet: one-line pull-quote.

## Context <!-- keywords: -->

What situation or recurring problem this principle addresses.

## Principle <!-- keywords: -->

The affirmative stance, held to. The load-bearing section.

## Anti-Goals <!-- keywords: -->

- NOT: what this philosophy refuses to become.

## Implications <!-- keywords: -->

What this principle makes possible and what it costs.

## Horizon <!-- keywords: -->

What this philosophy opens, where it leads, what it becomes the foundation for.
```

### Decision (ADR)

```
<!-- file: ADR-NNN-topic-slug.md · keywords: keyword keyword keyword -->

# Decision NNN: Title

**Status:** Draft | Accepted | Superseded → ADR-NNN | Deprecated
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract: the decision and why.

## Context <!-- keywords: -->

What forced this decision. What constraints exist.

## *The decision title — write the actual decision* <!-- keywords: -->

We will use X because Y.

## Implications <!-- keywords: -->

**Positive:** what gets easier.
**Negative:** what gets harder; new risks.

## Alternatives considered <!-- keywords: -->

| Option | Why rejected |
|--------|-------------|
| …      | …           |
```

### Spec

```
<!-- file: SPEC-NNN-topic-slug.md · keywords: keyword keyword keyword -->

# Specification NNN: Title

**Status:** Draft | Active | Superseded →
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract: what this builds and why.

## Goals <!-- keywords: -->

What this spec delivers.

## Non-goals <!-- keywords: -->

- NOT: …

## Acceptance criteria <!-- keywords: -->

- [ ] binary, yes/no, no subjectivity

## Design <!-- keywords: -->

What to build — modules, data flow, interfaces. Not line-by-line instructions.

## Open questions <!-- keywords: -->

- [ ] …
```

### Plan

```
<!-- file: PLAN-NNN-topic-slug.md · keywords: keyword keyword keyword -->

# PLAN NNN: Title

**Status:** Draft · Plan ready · In Progress · Completed · Cancelled
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract: what's missing, what this achieves, why it matters now.

## Non-goals <!-- keywords: -->

- NOT: …

## Decisions locked <!-- keywords: -->

### 1. Title
The decision, 2–4 lines.

## Execution checklist <!-- keywords: -->

- [ ] step | file-ref

## Acceptance criteria <!-- keywords: -->

- [ ] …
```

### Research

```
<!-- file: YYYY-MM-DD-topic-slug.md · keywords: keyword keyword keyword -->

# Research: Topic title

**Scope:** the question.

Abstract: short summary of findings and answer.

## *The question — write the actual question* <!-- keywords: -->

What was asked.

## *Findings — write what was found* <!-- keywords: -->

The findings, structured to fit.

## Sources <!-- keywords: -->

- URL / citation
```

### Session log

```
<!-- file: YYYY-MM-DD-NNN-topic-slug.md · keywords: keyword keyword keyword -->

# Session NNN — Title

**Status:** In Progress | Completed
**Goal:** What we set out to do.

Abstract: a sentence or two on the session's purpose.

## *What was accomplished — write the accomplishment* <!-- keywords: -->

Narrative of the work. Extract durable findings to their permanent home (spec, research, operational memory) and leave a pointer here, not the full finding.

## Open / carry-forward <!-- keywords: -->

- [ ] still open
- [x] resolved this session

## Git <!-- keywords: -->

Commits: abc1234 · Status: clean / pending push
```
