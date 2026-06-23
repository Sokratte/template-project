<!-- ================================================================
     SETUP GUIDE — FOR THE AGENT CREATING A NEW PROJECT
     ================================================================
     Read this top-to-bottom. Follow every step. When done, delete
     everything from the top of the file down to "--- END OF SETUP ---".
     What remains is the project's permanent AGENTS.md.

     NOTE (2026-06-18): the permanent-AGENTS.md body below is a holdover
     skeleton. The canonical AGENTS.md is being authored separately
     (PLAN-002 main deliverable). Until that lands, this guide carries the
     session-10 architecture in its setup steps; the body skeleton will be
     replaced by the synced canonical file + AGENTS.override.md.

     Do NOT work inside ~/projects/template-project/.
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
cp -r ~/projects/template-project ~/projects/<name>
```
The copy carries the `.agents_sync` marker, which opts it into canonical
`AGENTS.md` sync. Then `cd` into the copy and continue.

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

## Step 2 — Choose the agent's persona and name

The persona is prompt-tuning: it modifies every prompt the agent will ever
process in this project, and it sets a default autonomy level. Offer the user
these presets (default: **Craftsman**, named **Tinkerbuddy**):

| Persona | Default autonomy | Behavioral tuning |
|---------|-----------------|-------------------|
| ⚡ Operator | `autonomous` | Bias to action, terse, acts then reports. Fewer check-ins. |
| 🛠️ Craftsman (default) | `checkpoint` | Correctness > speed, specs before code, pushes back on weak ideas, pauses before irreversible actions. |
| 🔍 Reviewer | `confirm` | Proposes before acting, explains reasoning, you approve each step. |
| ✍️ Custom | (ask) | You describe the persona in your own words; pick an autonomy level too. |

- **Autonomy levels:** `autonomous` = acts and reports after; `checkpoint` =
  acts on routine work, pauses for consequential/irreversible actions;
  `confirm` = proposes before nearly every action.
- The user may override the persona's default autonomy.
- **Name:** ask what the agent should be called (default **Tinkerbuddy**).
- Record persona, name, and `autonomy:` in `AGENTS.override.md`.

---

## Step 3 — Fill in AGENTS.override.md

`AGENTS.override.md` holds everything project-specific: identity diffs from
the canonical instructions, the persona + name + `autonomy` from Step 2, the
`push:` toggle (Step 6), and any project-specific rule exceptions (override
wins on conflict). Keep it small — it is an override, not a forked file.

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

## Step 5 — Ensure LOCAL.md exists (once per VM, not per project)

The operator profile — who you are working with and how — lives in
`~/projects/LOCAL.md`. It is **per-operator and per-VM, never committed,
never cloned** (it is personal observation about a named human: PII). It is
created once per machine, so a second project on the same VM reuses it.

If `~/projects/LOCAL.md` does not exist yet, create it with the user:
their name, communication style, how they like to work, the backup provider
they use (`backup: none` or `backup: <provider>`), and the SSH key naming
convention (`~/.ssh/<project>`). Do NOT put any of this in the project tree.

---

## Step 6 — Git and backup

Backup behavior is keyed on `~/projects/LOCAL.md` (`backup:`) and the
per-project `push:` toggle in `AGENTS.override.md`. The remote URL is git's
own (`.git/config`) — never store it separately.

- `backup: none` → local-only git, auto-commit at session end, no push, git
  never mentioned to the user.
- `backup: <provider>` + `push: on` → auto-commit AND push.
- `git add`: specific files only — **never** `git add -A`.
- `git commit`: automatic at session end, Conventional Commits.
- Never force-push. A non-fast-forward rejection is a safety net.

Record `push:` in the override.

---

## Step 7 — Create the repository (one of the last steps)

If this project is backed up, guide the user:

> Create the repository on your provider (e.g. github.com/new or
> `gh repo create`). For deploy keys, generate the keypair
> (`~/.ssh/<project>`), register the PUBLIC key on the provider, and ENABLE
> WRITE ACCESS (deploy keys are read-only by default — forgetting this
> silently blocks every push). Then give me the remote URL.

Once you have the URL:
```
git init
git remote add origin <URL>
```
From here git owns the remote. Do NOT commit yet — fill in files first.

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
git add <specific files>     # never -A; stage the scaffold files explicitly
git commit -m "chore: initial project scaffold from template"
git push -u origin main       # if backed up and push: on
```

Guide the user to create the first Milestone — the first meaningful version
goal. Help break it into Issues.

Delete everything from the top of this file down to and including the line
below. The project is ready.

--- END OF SETUP ---


# TODO: Project Name — Agent Instructions

TODO: What this project does and for whom. (one sentence)
TODO: What kind of project and where it runs. (one sentence)

**This project is NOT:**
- TODO: anti-goal or scope boundary
- TODO: another one

Canonical instructions are synced into this project's `AGENTS.md` from
`~/projects/AGENTS.md` (read-only artifact). Project-specific additions and
exceptions — plus persona, name, `autonomy`, and `push` — live in
`AGENTS.override.md`. Override wins on conflict.

**This file is deliberately STABLE.** It orients every agent at every
session start and changes only when something fundamental changes. It holds
what never changes: identity, rules, tools, the memory system. Everything
that changes regularly lives elsewhere — direction in `ROADMAP.md`, the open
work list in `agents/notes/work-backlog.md`.

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
The operator profile is NOT in this repo — it lives in `~/projects/LOCAL.md`
(per-VM, never committed; it is PII).

**Session memory** — what is happening now:

| File | Role | Size |
|------|------|------|
| `agents/notes/work-backlog.md` | Open items — pruned living list | Alarm at >20 open items |
| `agents/notes/work-log.md` | Done items — append-only history | No limit; never auto-read |
| `agents/notes/scratchpad.md` | Carry-forward + working space | Soft: 30 lines; Hard: 60 lines |

**Long-term memory** — what has been learned over time:

| File | Role | Loaded |
|------|------|--------|
| `agents/memory/procedural.md` | Rules — what the agent DOES | Fully, every session (size-limited) |
| `agents/memory/operational.md` | Gotchas + demoted rules — what the agent KNOWS | Grep when stuck (no limit, indexed) |

`procedural.md` carries a word limit (line 1); `operational.md` has none — it is the
unlimited, section-indexed floor where demoted and stale knowledge lives, found by grep.

**Tag & value:** every entry is `[sNN xM]` — born session NN, useful M times;
`value = M / sessions_alive`. **Strengthen on recall:** when an entry helps, bump M.

**Autonomous lifecycle (session-end, no prompt):** proven, topic-independent operational
entries are *promoted* to procedural; when procedural exceeds its size limit, its lowest-
value entries are *demoted* back to operational (never deleted). Cutoff `memory_cutoff`
(default 0.01) in `AGENTS.override.md`. Full model: SPEC-003 §8.


## Where Things Live

| Question | Location |
|----------|----------|
| What this project builds (the goal) | `docs/specs/` |
| Open work (TODOs, findings) | `agents/notes/work-backlog.md` |
| Completed work history | `agents/notes/work-log.md` |
| Where the project is going | `ROADMAP.md` |
| What's been completed (user-visible) | `CHANGELOG.md` and `docs/sessions/` |
| What's in progress | GitHub Issues — open, current Milestone |
| Architecture decisions | `docs/decisions/` (ADRs — immutable once ratified) |
| Task plans (short-lived) | `docs/plans/` (archive when done) |
| Research / domain knowledge | `docs/research/` (optional) |
| Operations guides | `docs/runbooks/` (optional) |
| Who the operator is | `~/projects/LOCAL.md` (per-VM, never committed) |
| How the agent works here | `agents/` — see `agents/README.md` |

When to use which artifact:
- Something is broken → **GitHub Issue** (label: bug)
- One-session task → **GitHub Issue** (label: enhancement)
- Non-trivial change that alters what we're building → **Spec update first**
- Multi-session work with architectural choices → **Spec + ADR + Milestone**
- A task that grows in scope → promote from Issue to Spec


## Document Budgets

| Document | Soft limit | Hard limit |
|----------|-----------|------------|
| `agents/notes/scratchpad.md` | 30 lines | 60 lines |
| `agents/memory/operational.md` | 35 lines | 50 lines |
| `agents/notes/work-backlog.md` | 15 items | 20 items |
| `agents/notes/work-log.md` | — (append-only) | — |
| `AGENTS.md` | 150 lines | 250 lines |
| Session logs | 600 words | 1 000 words |
| Plan files | 150 lines | 250 lines |

**At soft limit:** the agent tries to reduce (prune resolved items, extract
mature content to its proper home). If it cannot reduce without losing
information, it informs the operator. For the backlog, >15 open items is a
review prompt; >20 is an alarm (real backlog problem or mis-set preference).

**At hard limit:** the agent must act before adding new content: prune,
extract, or compress. For session logs over 1 000 words, findings must be
extracted to a spec, operational memory, or research doc — a session log is
not a knowledge base.


## Git

One canonical repo. Check `.git/config` for the remote URL (git owns it;
never store it separately). Backup is keyed on `~/projects/LOCAL.md`
(`backup:`) and the `push:` toggle in `AGENTS.override.md`.

- `git add` (specific files only): never `git add -A`
- `git commit` (session end): automatic, Conventional Commits
- `git push` (session end): per `push:` and `autonomy`; requires
  `backup` ≠ none and an `origin` remote

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
