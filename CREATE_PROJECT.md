<!-- ================================================================
     SETUP GUIDE — FOR THE AGENT CREATING A NEW PROJECT
     ================================================================
     Read this top-to-bottom. Follow every step. When done, delete
     everything from the top of the file down to "--- END OF SETUP ---".
     What remains is the project's permanent AGENTS.md.

     Do NOT work inside ~/workspace/template-project/.
     That folder is the template. You are working in the copy.
     ================================================================ -->

# New Project Setup Guide

You are setting up a new project from the workspace template. This guide
walks you through it as a conversation with the user — not a checklist you
rush through silently. Take your time. The decisions made now shape every
session that follows.

---

copy it first:
```
cp -r ~/workspace/template-project ~/workspace/projects/<name>
```
Then `cd` into the copy and continue.

---

## Step 1 — Understand what the user wants to build

Before touching any file, have a short conversation. Ask the user:

1. **What** are you building? (one sentence)
2. **Who** is it for? (yourself, a team, the public?)
3. **What kind** of project is it? (app, library, server, content, hardware?)
4. **Where** does it run? (local only, server, cloud, embedded?)
5. **What should it explicitly NOT be?** (scope boundaries, anti-goals)

Do not proceed until you have clear answers to at least 1, 3, and 5.

---

## Step X — Create the GitHub repository (one of the last steps)

Guide the user:

> I need you to create a GitHub repository for this project. You can do this
> at github.com/new or by running `gh repo create`. Once created, tell me
> the remote URL.

Once you have the URL:
```
git init
git remote add origin <URL>
```

Do NOT commit yet — fill in files first.

---

## Step 3 — Fill in the permanent sections

Scroll to "--- END OF SETUP ---". Fill in every `TODO:` field:

- Project name and description (2 sentences max)
- What this project is NOT
- Tools section — which MCP servers this project uses
- Git automation choices (Step 6 below)
- Remove `TODO:` markers when done

---

## Step 4 — Create the first specification

Open `docs/specs/SPEC-000-template.md`, copy it to
`docs/specs/SPEC-001-<project-name>.md`. This is the founding spec —
the written definition of what you are building:

- **What:** the goal, stated precisely enough to judge whether code meets it
- **Why:** what problem it solves and for whom
- **What it is NOT:** explicit scope boundaries (from Step 1 question 5)
- **Success criteria:** how you will know when it is done

The user must review and approve this spec before any code is written.
This is the most important document in the project — it is the target
everything else aims at.

---

## Step 5 — Select optional sections

Read the "OPTIONAL SECTIONS" block at the bottom of the permanent AGENTS.md.
Uncomment what applies, delete the rest, delete the menu block itself.

---

<!-- TODO (PLAN-001 rewrite): this setup guide predates the multi-VM
     architecture. When rewriting, the config step must CREATE the
     per-project `.project` file (key:value): autonomy, and — if backed up —
     provider, remote_url, repo_name, push, key_path. `.project` is gitignored
     and never committed, so a fresh clone won't have it; setup is where it is
     generated. Also: root is now `~/projects/`, the `.agents_sync` marker
     opts the project into canonical-AGENTS.md sync, and `AGENTS.override.md`
     (not a forked AGENTS.md) holds project-specific rules. See
     docs/plans/PLAN-001-multi-vm-agent-architecture.md. -->

## Step 6 — Git automation choices

Decide with the user which git operations are automatic at session end.
Record the choices in the permanent "Git" section.

- **`git add` (specific files):** automatic by default. The agent stages only
  files it worked on — never blind `git add -A`.
- **`git commit`:** automatic by default, at session end.
- **`git push`:** **off by default — ask the user explicitly.** Recommended
  on for solo work on one machine (protects against data loss). Whatever
  they choose, record it so every future session behaves consistently.

---

## Step 8 — Memory system: disable platform memory

This project uses file-based memory. Set a memory edit in the AI client:

> "Do not generate or retain memories from this project's conversations.
> The entire context is versioned in the repo. Memories are deliberately
> disabled for this project."

The session-start procedure reminds the user if this edit is missing.

---

## Step 9 — Domain research (when relevant)

For projects where domain expertise matters — new technology, unfamiliar
field, competitive landscape — search the web before writing a line of code.

Write findings to `docs/research/YYYY-MM-DD-<topic>.md`. Include sources
and dates. Brief the user: standard approach, 2–3 early decisions that save
pain later, non-obvious trade-offs ahead.

Skip this step for projects where the domain is already well understood.

---

## Step 10 — First commit and first milestone

```
git add -A
git commit -m "chore: initial project scaffold from template"
git push -u origin main
```

Guide the user to create the first GitHub Milestone — the first meaningful
version goal. Help break it into Issues.

Delete everything from the top of this file down to and including the line
below. The project is ready.

--- END OF SETUP ---


# TODO: Project Name — Agent Instructions

TODO: What this project does and for whom. (one sentence)
TODO: What kind of project and where it runs. (one sentence)

**This project is NOT:**
- TODO: anti-goal or scope boundary
- TODO: another one

Global rules: `~/workspace/..............` — read before every session.
Only project-specific additions and exceptions appear below.

**This file is deliberately STABLE.** It orients every agent at every
session start and changes only when something fundamental changes. It holds
what never changes: identity, rules, tools, the memory system. Everything
that changes regularly lives elsewhere — direction in `ROADMAP.md`, the
work list in `agents/worklog.md`.

**AGENTS.md is not a scratchpad.** Do not log work, jot notes, or record
findings here. If information has a home in another file, put it there.
Duplicated information becomes stale and contradictory — that is the failure
this rule prevents.

**Soft limit: ~150 lines. Hard limit: ~250 lines.** If this file is growing,
something belongs elsewhere.


## Session Lifecycle — EXECUTE, do not merely read

Every session has two anchors — both are procedures to execute step by step.

**At the start of every session, EXECUTE `agents/commands/session-start.md`.**
Do no work before it is complete.

**At the end of every session, EXECUTE `agents/commands/session-end.md`.**
Do not say "done" before it is complete.

If you detect a closing signal ("that's it", "thanks", "see you tomorrow",
"good job", "done for today"), ask once: "Shall we close the session now?"
— and on yes, execute `agents/commands/session-end.md`.


## Specifications

Specifications live in `docs/specs/`. They are the written definition of
what this project builds — the target that every session aims at.

**Before writing any code or making any significant change, check whether a
spec exists for the work at hand.** If it does, read it. If it doesn't and
the work is non-trivial, write one first.

A spec is not a plan (what to do next) and not a decision record (why we
chose X). It is the definition of what done looks like. Code that contradicts
a spec is a bug, not a feature. A change that would alter a spec requires
the operator's explicit approval before implementation.


## Memory System

Context persists across sessions through files in the repo — not through
the AI platform's server-side memory, which is deliberately disabled (Step 8).
Full specification: `docs/specs/SPEC-003-agent-memory-system.md`.

**Session memory** — what is happening now:

| File | Role | Size limits |
|------|------|-------------|
| `agents/worklog.md` | Append-only work ledger | Soft: 60 lines → cleanup; Hard: 100 lines → force cleanup |
| `agents/scratchpad.md` | Carry-forward + working space | Soft: 30 lines → prune; Hard: 60 lines → must prune first |

**Long-term memory** — what has been learned over time:

| File | Role | Loaded |
|------|------|--------|
| `agents/procedural-memory.md` | Rules + operator profile — what the agent IS | Fully, every session |
| `agents/operational-memory.md` | Gotchas — what the agent KNOWS | Grep only when stuck |
| `agents/historical-memory.md` | Retired — what the agent WAS | Never automatically |

`operational-memory.md` soft limit: ~35 lines → flag to operator.
Hard limit: 50 lines → offer decay sweep before adding new entries.

**Strengthen on recall:** when a memory entry prevents a mistake or solves a
problem, bump its `[YYYY-MM-DD xN]` tag (today's date, counter +1).

**Decay:** the sweep script (`tools/scripts/sweep-knowledge.py`) moves
least-recalled entries from `operational-memory.md` to `historical-memory.md`.
Operator-gated — dry-run shown first. Never touches `procedural-memory.md`.


## Where Things Live

| Question | Location |
|----------|----------|
| What this project builds (the goal) | `docs/specs/` |
| What's happening now (work list) | `agents/worklog.md` |
| Where the project is going | `ROADMAP.md` |
| What's been completed | `CHANGELOG.md` and `changelog/session-logs/` |
| What's in progress | GitHub Issues — open, current Milestone |
| Architecture decisions | `docs/decisions/` (ADRs — immutable once ratified) |
| Task plans (short-lived) | `docs/plans/` (archive when done) |
| Research / domain knowledge | `docs/research/` (optional — if the project needs it) |
| Operations guides | `docs/runbooks/` (optional) |
| How the agent works here | `agents/` — see `agents/README.md` |

When to use which artifact:
- Something is broken → **GitHub Issue** (label: bug)
- One-session task → **GitHub Issue** (label: enhancement)
- Non-trivial change that alters what we're building → **Spec update first**
- Multi-session work with architectural choices → **Spec + ADR + Milestone**
- A task that grows in scope → promote from Issue to Spec


## Document Budgets

Every document type has a soft and a hard limit. The agent monitors these
and acts when thresholds are crossed.

| Document | Soft limit | Hard limit |
|----------|-----------|------------|
| `agents/scratchpad.md` | 30 lines | 60 lines |
| `agents/tribal-knowledge.md` | 35 lines | 50 lines |
| `agents/worklog.md` | 60 lines | 100 lines |
| `AGENTS.md` | 150 lines | 250 lines |
| Session logs | 600 words | 1 000 words |
| Plan files | 150 lines | 250 lines |

**At soft limit:** the agent tries to reduce (prune resolved items, extract
mature content to its proper home). If it cannot reduce without losing
information, it informs the operator: "File X is over its soft limit — there
may be old content worth reviewing."

**At hard limit:** the agent must act before adding new content: prune,
extract, or compress. For session logs over 1 000 words, findings must be
extracted to a spec, tribal knowledge, or research doc — a session log is
not a knowledge base.


## Git

One canonical repo. Check `.git/config` for the remote URL.
Core git discipline: `~/workspace/.................`.

**Automation (set during setup Step 6):**
- `git add` (specific files only): TODO automatic / manual
- `git commit` (session end): TODO automatic / manual
- `git push` (session end): TODO enabled / disabled

Never force-push. A non-fast-forward rejection is a safety net —
`git diff` against remote, merge by hand, then push.

Project-specific exceptions: TODO (delete if none)


<!--
====================================================================
OPTIONAL SECTIONS — uncomment what applies, delete the rest,
then delete this block.
====================================================================

Other paths or services must not be touched carelessly.

## Write Boundaries

| May edit freely | Requires caution | Never touch |
|-----------------|------------------|-------------|
| TODO            | TODO             | TODO        |
| THIS PROJECT    | www, bin         | OTHER PROJECTS |
====================================================================

INCLUDE IF: Python with threading, OS callbacks, or hardware I/O.

## Error Handling

Three zones require try/except without exception:
1. OS callbacks — exceptions are silently swallowed
2. Thread entry points — uncaught exceptions kill the thread silently
3. System boundary calls — hardware I/O, ML inference, external processes

====================================================================

INCLUDE IF: deployed services that other things depend on.

## Services and Live Operations

| Service | Port | Path | Source |
|---------|------|------|--------|
| TODO    | TODO | TODO | TODO   |

Before touching live infrastructure: read the runbook in `docs/runbooks/`.
After any change, run health checks for every service.

====================================================================
-->
