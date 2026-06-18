docs/README.md | document conventions, line-1 index, abstract, head awk grep, skeleton vs content, traffic-light, keywords as relationship graph, two document classes

# docs/ — Document conventions

Everything in this folder follows a single structure: **line 1 is the index
entry, the abstract runs to the first `##`.** This is uniform across all five
document types — sessions, research, decisions, plans, specs.

## Reading conventions

**Index a directory** (one line per file, no full reads):
```bash
head -qn1 docs/sessions/*.md
head -qn1 docs/decisions/*.md
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
Large documents are not split into files; they are sectioned at read-time.

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
heading. ADRs, specs, and plans open with the same three-field block in this
order — `**Status:**`, then `**Created:** · **Updated:**` — followed by a
standalone summary of what the document decides, describes, or records, long
enough to stand on its own in the index (one sentence is too little for a
1,000-line spec). Sessions and research use their own lighter heads (see the
templates below). The terminator is the first `##` — a forgotten `##` is
essentially impossible in a structured document, whereas a forgotten `---`
delimiter would silently make awk read the whole file.

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

| Type | Location | Naming | Line 1 | Notes |
|------|----------|--------|--------|-------|
| Session log | `docs/sessions/` | `YYYY-MM-DD-topic-slug.md` | `filename \| keywords` | Created at session start, filled during work |
| Research | `docs/research/` | `YYYY-MM-DD-topic-slug.md` | `filename \| keywords` | `**Scope:**` + short answer in abstract |
| Decision (ADR) | `docs/decisions/` | `ADR-NNN-topic-slug.md` | `filename \| keywords` | Changed by supersede-in-place, not rewrite (see below) |
| Plan | `docs/plans/` | `PLAN-NNN-topic-slug.md` | `filename \| keywords` | Move to `plans/archive/` when done |
| Spec | `docs/specs/` | `SPEC-NNN-topic-slug.md` | `filename \| keywords` | Status Draft/Active/Superseded; stays in place |

## Templates

The canonical shape of each document type. Copy the block, keep the structure.
In every case the abstract is everything between line 1 and the first `##`.

### Session log

`docs/sessions/YYYY-MM-DD-slug.md` — line 1 is the index, read via
`head -qn1 docs/sessions/*.md`. Abstract = the Goal block, down to `## What was done`.
Target ~600 words, hard limit 1,000. Over → extract a finding to its permanent
home and leave a pointer.

```
2026-06-18-readme-pass.md | readme, docs convention, skeleton slimming, soft-wrap

# Session NN — Topic

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

### Research

`docs/research/YYYY-MM-DD-slug.md` — line 1 is this file's entry in the
directory index; grep across the index before re-researching. Abstract = Scope
+ the short answer, down to `## Question`. Not loaded at startup; found via the
keyword index. Archive when stale.

```
2026-04-17-project-structure-standards.md | AGENTS.md, conventional commits, semver, ADR, spec-driven, context budget

# Research: Topic title

**Scope:** What question this answers.

Abstract: the short answer to the question, in plain language, enough to be
useful straight from the index. Ends at the first ##.

## Question

What was asked.

## Answer

The findings, structured to fit.

## Sources

- URL / citation
```

### Decision (ADR)

`docs/decisions/ADR-NNN-slug.md` — line 1 is this file's entry in the
directory index. Abstract = Status + the decision paragraph, down to
`## Context`. An ADR is a durable record, not a frozen one: fix typos and
small clarifications in place (check the blast radius first — what cites this?).
For a real change of substance, do **not** rewrite the old text away —
mark the superseded passage (strike it through or label it `~~SUPERSEDED~~`),
set `**Status:** Superseded`, and append a dated `## Addendum` explaining what
changed and why. The old reasoning stays visible as the record of what was
true before. (Legal texts amend this way: strike, don't delete; append.)

```
ADR-001-project-standard.md | workspace template, industry standards, pointer pattern, cp -r, agent orientation

# ADR-NNN: Title

**Status:** Draft | Accepted | Superseded by ADR-NNN | Deprecated
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

One-paragraph abstract: the decision in plain language and why, so the index
hit is self-explanatory. Ends at first ##.

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

`docs/plans/PLAN-NNN-slug.md` — line 1 is this file's entry in the directory
index. Abstract = Created/Updated + the abstract paragraph, down to `## Goal`.
A living reference, not a disposable checklist. Done → move to `docs/plans/archive/`.

```
PLAN-001-multi-vm-agent-architecture.md | canonical AGENTS.md, agents_sync.sh, OPERATOR.md, deploy keys, override, marker file

# PLAN-NNN: Topic

**Status:** Draft | Active | Done | Superseded
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract (plain language): what's missing, what this achieves, why it matters
now. Ends at first ##.

## Goal

One sentence.

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

`docs/specs/SPEC-NNN-slug.md` — line 1 is this file's entry in the directory
index. Abstract = Status + the standalone summary, down to `## Non-goals`. The
target — defines what "done" looks like. Code that contradicts a spec is a bug.
Status tracks the *document*, not the implementation: `Draft` (still being
written), `Active` (ratified, the reference code is judged against), or
`Superseded` (replaced by a newer spec; left in place, not deleted). How far
the code has caught up lives in ROADMAP / work-backlog, not here.

```
SPEC-003-agent-memory-system.md | file-based memory, procedural, operational, work-backlog, session lifecycle, decay sweep

# SPEC-NNN: Feature name

**Status:** Draft | Active | Superseded
**Created:** YYYY-MM-DD · **Updated:** YYYY-MM-DD

Abstract: what this builds and why, enough to stand alone in the index — a
spec can run 1,000+ lines, so one sentence is too little. As long as it needs,
ends at first ##.

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
