docs/README.md | document conventions, line-1 index, abstract, head awk grep, skeleton vs content, traffic-light, keywords as relationship graph, two document classes

# docs/ — Document conventions

Everything in this folder follows a single structure: **line 1 is the index
entry, the abstract runs to the first `##`.** This is uniform across all five
document types — sessions, research, decisions, plans, specs.

## Reading conventions

**Index a directory** (one line per file, no full reads):
```bash
for f in docs/sessions/*.md; do head -1 "$f"; done
for f in docs/decisions/*.md; do head -1 "$f"; done
```

**Read a file's abstract** (everything before the first `##`):
```bash
awk '/^## /{exit} 1' docs/specs/SPEC-003-agent-memory-system.md
```

**Get a file's section map** (heading outline):
```bash
grep -n '^#\+ ' docs/specs/SPEC-003-agent-memory-system.md
```

**Read one section** (e.g. `## Design`):
```bash
awk '/^## Design/{f=1;print;next} f&&/^## /{exit} f' FILE.md
```

These three moves — index, abstract, section — cover every read pattern.
Documents are never split into files for size; they are sectioned at read-time
and grow as large as they need to.

## Line-1 format

```
filename | keyword keyword keyword ...
```

The filename is in line 1 because the index is read without headers — a bare
keyword line cannot be traced back to its file. Keywords are the relationship
graph: no `Related:` fields, no bidirectional links. A keyword that appears
in two files is the connection. If a directed relationship matters, write it
as prose where it belongs.

## Abstract

The abstract is everything from line 1 down to (not including) the first `##`
heading. ADRs, specs, and plans open with the same head block in this order —
`**Status:**`, then `**Created:** · **Updated:**` — followed by a standalone
summary in plain language of what the document decides, describes, or records, long enough to
stand on its own in the index (one sentence is too little for a 1,000-line
spec). Sessions and research use their own lighter heads (see the templates
below). The terminator is the first `##` — a forgotten `##` is essentially
impossible in a structured document, whereas a forgotten `---` delimiter would
silently make awk read the whole file.

Do not put a `##` heading inside an abstract.

## Document classes and size governance

| Class | Files | Size |
|-------|-------|------|
| **Skeleton** | `agents/memory/procedural.md`, `AGENTS.override.md`, `agents/commands/session-start.md`, `agents/notes/scratchpad.md`, `agents/notes/work-backlog.md`, ROADMAP active section | Governed by traffic-light (ADR-002) |
| **Content** | Everything in `docs/` | No limit — as long as needed |

Content documents are never loaded whole. The read mechanism (index, abstract,
section) already handles any size; a cap would force cutting material you need.

Size governance for skeleton files is defined in ADR-002.

## Document types

| Type | Location | Naming | Line 1 |
|------|----------|--------|--------|
| Session log | `docs/sessions/` | `YYYY-MM-DD-topic-slug.md` | `filename \| keywords` |
| Research | `docs/research/` | `YYYY-MM-DD-topic-slug.md` | `filename \| keywords` |
| Decision (ADR) | `docs/decisions/` | `ADR-NNN-topic-slug.md` | `filename \| keywords` |
| Plan | `docs/plans/` | `PLAN-NNN-topic-slug.md` | `filename \| keywords` |
| Spec | `docs/specs/` | `SPEC-NNN-topic-slug.md` | `filename \| keywords` |

## Lifecycle notes

How each type changes over time and where its status values come from. The
status field tracks the *document*, never the implementation — implementation
progress lives in ROADMAP / work-backlog (one fact, one home).

**Session log** — created at session start, filled during the work.

**Research** — archive when stale.

**Decision (ADR)** — a durable record, not a frozen one. Typo or small
clarification: fix in place, check the blast radius first (what cites this?).
Real change of substance: do not rewrite the old text away — mark the
superseded passage (`~~SUPERSEDED~~`), set `**Status:** Superseded`, append a
dated `## Addendum` explaining what changed and why. The old reasoning stays
visible as the record of what was true before. (Legal texts amend this way:
strike, don't delete; append.) Status: `Draft | Accepted | Superseded by
ADR-NNN | Deprecated`.

**Plan** — a living reference, not a disposable checklist. When implementation
is finished, move it to `docs/plans/archive/`. Status: `Draft plan` (still
being written) → `Plan ready` (ratified, not yet started) → `Implementation in
progress` → `Implementation completed`.

**Spec** — the target; defines what "done" looks like. Code that contradicts a
spec is a bug. A spec is the living reference and is not archived for being
implemented. Status: `Draft` (still being written) → `Active` (ratified, code
is judged against it) → `Superseded` (replaced by a newer spec; left in place,
not deleted).

## Templates

The canonical shape of each document type — copy the block, keep the structure.

### Decision (ADR)

```
ADR-001-project-standard.md | workspace template, industry standards, pointer pattern, cp -r, agent orientation

# Decision NNN: Title

**Status:** Draft | Accepted | Superseded by Decision NNN | Deprecated
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract: the decision and why.

## Context

What forced this decision. What constraints exist.

## Decision

We will use X because Y.

## Consequences

**Positive:** what gets easier.
**Negative:** what gets harder; new risks.

## Alternatives considered

| Option | Why rejected |
|--------|-------------|
| …      | …           |
```

### Plan

```
PLAN-001-multi-vm-agent-architecture.md | canonical AGENTS.md, agents_sync.sh, OPERATOR.md, deploy keys, override, marker file

# PLAN NNN: Title

**Status:** Draft plan | Plan ready | Implementation in progress | Implementation completed
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract: what's missing, what this achieves, why it matters
now.

## Goal

Short Description

## Non-goals

- NOT: …

## Decisions locked

### 1. Title
The decision, 2–4 lines. Add more as they're made.

## Execution checklist

- [ ] step | file-ref

## Acceptance criteria

- [ ] …
```

### Spec

```
SPEC-003-agent-memory-system.md | file-based memory, procedural, operational, work-backlog, session lifecycle, decay sweep

# Specification NNN: Title

**Status:** Draft | Active | Superseded
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract: what this builds and why.

## Non-goals

- NOT: …

## Acceptance criteria

- [ ] binary, yes/no, no subjectivity
- [ ] tests cover happy path + one error case

## Design

What to build — modules, data flow, interfaces. Not line-by-line instructions.

## Open questions

- [ ] …
```

### Research

```
2026-04-17-project-structure-standards.md | AGENTS.md, conventional commits, semver, ADR, spec-driven, context budget

# Research: Topic title

**Scope:** the question.

Abstract: short summary of findings & answer.

## Question

What was asked.

## Answer

The findings, structured to fit.

## Sources

- URL / citation
```

### Session log

```
2026-06-18-NNN-readme-pass.md | readme, docs convention, skeleton slimming, soft-wrap

# Session NNN — Title

**Goal:** What we set out to do.

## What was done

Narrative of the work. Extract durable findings to their permanent home
(spec, research, operational memory) and leave a pointer here, not the full
finding.

## Open / carry-forward

- [ ] still open
- [x] resolved this session

## Git

Commits: abc1234 · Status: clean / pending push
```
