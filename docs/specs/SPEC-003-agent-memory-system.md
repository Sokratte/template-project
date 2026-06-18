# SPEC-003 — Agent Memory & Session System

> A file-based memory and session-lifecycle system that lets an AI agent
> work across many sessions without losing context — and without relying on
> the AI platform's server-side memory. Every mechanism is a file in the
> repo. The repo is the single source of truth.

**Status:** Active
**Applies to:** any project copied from the workspace template

---

## 1. Design principles

**One fact, one home.** Every piece of information has exactly one
authoritative location. Duplication produces stale, contradictory documents.

**Lean and interlocked.** No file exists unless it earns its place. Every
file references the others. The set makes sense as a whole.

**Loaded by need, not by default.** Files that must be active every session
are small and loaded fully. Large reference files are searched on demand.
This keeps per-session token cost low.

**Model-agnostic.** Plain Markdown, plain git, imperative procedures. No
dependence on one vendor's features or memory system.

**Specifications before code.** The most dangerous AI failure mode is
building the wrong thing — changing behaviour that was correct, breaking
constraints that were implicit, misunderstanding the goal. A written spec is
the defence: it makes the goal explicit and provides a standard against which
code can be judged wrong. The session-start procedure checks for a spec
before any non-trivial work begins.

---

## 2. Why file-based memory, not platform memory

Platform memory (Claude, ChatGPT) stores a summary on the vendor's servers
and re-injects it. It is opaque, unversioned, a single flat blob, lives off
your machine, and diverges from the repo over time.

File-based memory — this system — keeps context in versioned files in the
repo. Transparent, diffable, structured by purpose, travels with the code,
works with any model that can read and write files.

This system deliberately **disables** platform memory for the project (a
memory edit in the AI client; the session-start procedure reminds the user
if it's missing). Running both creates two diverging sources of truth.

---

## 3. File map

```
~/projects/
  AGENTS.md                ← canonical agent instructions (synced; see PLAN-001)
  OPERATOR.md              ← operator + VM identity (PII) — NEVER committed/cloned

<project>/
  AGENTS.md                ← synced copy of canonical (read-only artifact)
  AGENTS.override.md       ← project instruction diffs + persona + name + push + autonomy
  agents/
    commands/
      session-start.md     ← orientation procedure — EXECUTE at session start
      session-end.md       ← closing procedure — EXECUTE at session end
    notes/
      work-backlog.md      ← open items: TODOs, findings, notes (pruned living list)
      work-log.md          ← done items, append-only history
      scratchpad.md        ← carry-forward + working space
    memory/
      procedural.md        ← procedural RULES — what the agent DOES (no operator profile)
      operational.md       ← gotchas — what the agent KNOWS
      historical.md        ← retired — what the agent WAS
    README.md              ← index of the above
  ROADMAP.md               ← project direction, milestones, active plans
  docs/specs/              ← what the project builds — the target
  docs/plans/              ← short-lived task plans
  docs/decisions/          ← architecture decision records (immutable once ratified)
  docs/sessions/           ← per-session technical record
```

Optional (add if the project needs them):
```
  docs/research/           ← domain knowledge, market analysis, dated
  docs/runbooks/           ← operational guides for live services
```

**Where the operator profile lives.** Not in this project tree. It is in
`~/projects/OPERATOR.md` — a per-operator, per-VM file that is never committed
and never cloned, because it contains personal observations about a named
human (PII) that must not enter a backed-up, possibly public repo. See
PLAN-001 for the full multi-VM file model. `procedural.md` holds procedural
rules only.

---

## 4. AGENTS.md — the stable anchor

Loaded first, every session. **Stable by design** — changes only when
something fundamental changes. **Never a scratchpad.**

> Architecture note: the project's `AGENTS.md` is a synced, read-only copy of
> the canonical `~/projects/AGENTS.md`. Project-specific instruction
> differences (and the persona / name / `autonomy` / `push` selections) go in
> `AGENTS.override.md`, not here. See PLAN-001.

### What MUST be in AGENTS.md

1. Project identity — two sentences: what it does and for whom; what kind
   and where it runs. The *full* reasoning lives in the founding spec.
2. "This project is NOT" — explicit anti-goals and scope boundaries.
3. Stability + scratchpad discipline — a statement that the file is stable
   and never used as a scratchpad. Its own size limits.
4. Session lifecycle — EXECUTE (not merely read) session-start and
   session-end. The closing-signal behaviour.
5. Specifications — the instruction to check for a spec before any
   non-trivial work.
6. Tools — every MCP server / tool and what it is for.
7. Memory system — the file tables, limits, strengthen-on-recall, decay,
   pointer to this spec.
8. Where Things Live — the index: one row per kind of question, one answer.
9. Document Budgets — the soft and hard limits for every document type.
10. Git — the automation choices and the never-force-push rule.
11. Optional sections — environment, testing, structure, conventions, write
    boundaries, error handling, services — only when they apply.

### What must NOT be in AGENTS.md

Open work items → `agents/notes/work-backlog.md`.
Completed history → `agents/notes/work-log.md`.
Loose notes → `agents/notes/scratchpad.md`.
Procedural rules → `agents/memory/procedural.md`.
Operator profile → `~/projects/OPERATOR.md` (never in the tree).
Operational gotchas → `agents/memory/operational.md`.
Project direction → `ROADMAP.md`.
Founding reasoning → `docs/specs/SPEC-001-*`.

The test: if the information has a home in another file, it goes there.

**Size limits:** soft 150 lines → review for duplication.
Hard 250 lines → something is wrong; extract to appropriate files.

---

## 5. ROADMAP.md — the volatile complement

Everything that changes regularly: current priority, tracks, milestones,
active plans with abstracts, project-specific registers. Read at session
start alongside AGENTS.md. The split exists so AGENTS.md stays still while
the project moves.

**Active Plans table:** every plan in `docs/plans/` gets one row — a link
and a ~50-word abstract in plain language (what's missing, what it achieves,
why it matters now). When a plan is done, move the file to
`docs/plans/archive/` and remove it from the table.

---

## 6. Specifications — the project's target

`docs/specs/` holds the written definitions of what the project builds.
These are not plans (what to do next) and not decision records (why we chose
X). They are definitions of what *done* looks like.

**Before writing any code or making any significant change, check whether a
spec exists for the work at hand.** If it does, read it. If the work is
non-trivial and no spec exists, write one first and get operator approval.

Code that contradicts a spec is a bug. A change that would alter a spec
requires explicit operator approval before implementation.

The founding spec (`SPEC-001-<project>.md`) is created during project setup
and defines the project's goal, scope, and success criteria.

---

## 7. Session memory

The old single `worklog.md` conflated two jobs — "what happened" and "what is
still open" — which buried live TODOs under history. It is split into two
files with opposite contracts: a **backlog** (open, pruned, living) and a
**log** (done, append-only, terminal). Names map to tense: *backlog* is
ahead, *log* is behind.

### 7.1 work-backlog.md — the live open-items list

The single list of open work: TODOs, findings, decisions pending. **Not
append-only** — it is a pruned, living list. When an item is finished, its
line **moves** to `work-log.md`; it is not left behind with a `[DONE]` tag.

Read fully (`cat`) at session start — it is bounded by design.

**Line format:**
```
YYYY-MM-DD | MODULE     | [TAG]    | Description | file-ref
```

- **MODULE** — project-relevant category (PROJECT, META, DOCS, CODE, TEST,
  INFRA, etc.). Keep the set small and stable.
- **TAG** — `[OPEN]` not started · `[ACTIVE]` in progress · `[FIND]` agent
  discovery needing discussion. (No `[DONE]` here — done items move to the
  log.)
- **file-ref** — path or `-`.

**Size: alarm at >20 open items.** Twenty open items means a real backlog
problem or a mis-set preference, not a formatting issue — the agent alerts
the operator rather than silently letting the list grow. There is no
line-count limit; the item count is the meaningful signal.

### 7.2 work-log.md — the append-only history

Completed items, in the order they were finished. **Append-only** — existing
lines are never edited or deleted; the past is auditable. **Never auto-read**
at session start; grepped on demand when history is needed.

Same line format as the backlog, with `[DONE]` and the completion date. No
size limit — it grows monotonically and is never loaded wholesale.

### 7.3 scratchpad.md — carry-forward and working space

One file, two structured sections:

**`## Carry-forward` (≤15 lines)** — things to remember at the next session
start. Open threads, context not captured elsewhere. If an item matures into
real work, it moves to the backlog. If this section grows past 15 lines,
something belongs in a plan, spec, or operational memory instead.

**`## Working space`** — current focus, half-formed thoughts, loose threads
being actively worked. Pruned at every session end — resolved threads removed
entirely, not struck through.

The distinction is *timescale*, not origin: carry-forward survives to the
next session; working space is cleaned at the end of this one.

**Size:** soft 30 lines → prune at session end; if still over, inform
operator. Hard 60 lines → must prune before adding anything new.

---

## 8. Long-term memory

Knowledge and context that persists across the life of the project, split
by how it is used. The model is cognitive science's ACT-R distinction
between procedural memory (skills applied automatically) and declarative
memory (facts recalled when needed).

> The third member of the classic trio — the *operator profile* ("who I work
> with and how") — deliberately does NOT live here. It is per-operator and
> per-VM, not per-project, and it is PII, so it lives in the non-committed
> `~/projects/OPERATOR.md` (PLAN-001 / §3). Keeping it out of the project tree
> is both a privacy guarantee and a single-home guarantee.

### 8.1 procedural.md — what the agent DOES

**Always loaded fully at session start.** Procedural rules: constraints
applied proactively every session, regardless of topic. The admission bar is
high — only things that apply to *every* session, every kind of work.
Domain-specific how-to belongs in operational memory.

This file is **procedural rules only.** It carries no operator profile (that
is `~/projects/OPERATOR.md`). The separation matters: rules are project-bound
and committed with the repo; the operator profile is person-bound, PII, and
must never be committed.

Never decays. Operator-only changes. Promotion of an operational fact to a
procedural rule is a deliberate human act, never automatic.

### 8.2 operational.md — what the agent KNOWS

Counter-intuitive gotchas. **Never loaded fully.** Grepped only when stuck.

Admission threshold: recurring (not a one-off), not obvious from the error
message, not reachable by reading the nearby docs or config. If the fix is
in the config or the code, it doesn't belong here. Decisions go in
`docs/decisions/`.

**Size:** soft 35 lines → flag to operator. Hard 50 lines → run the decay
sweep (§8.5) before adding new entries.

### 8.3 historical.md — what the agent WAS

Never loaded automatically. Two sections with exact headings the sweep uses:
`## retired procedures` (operator decision) and `## stale operations` (sweep).
Append-only, never deleted — the past is auditable.

### 8.4 Strengthen on recall

Every memory entry carries `[YYYY-MM-DD xN]` — date last used, recall
counter. When an entry helps, the agent patches the tag: today's date,
counter +1. Frequently-useful entries stay strong; unused ones fade.

### 8.5 Decay sweep

When `operational.md` exceeds 50 lines, the least-recalled entries move to
`historical.md` under `## stale operations`. This is a deterministic agent
procedure — pure arithmetic on the tags, no separate script — carried out as
a step in `session-end.md`:

1. Parse each entry's `[YYYY-MM-DD xN]` tag.
2. Compute `recall_rate = counter / age_in_days`. Entries younger than 30
   days are protected (never swept).
3. Sort by lowest rate first; whole tie-groups move together.
4. Move the lowest-rate entries until the file is back under 50 lines,
   appending them under `## stale operations` in `historical.md`.

**Operator-gated.** The agent shows the operator the list it intends to move
and applies the move only on an explicit yes. `procedural.md` is never
touched by the sweep.

---

## 9. The session lifecycle

### 9.1 session-start.md — orientation

Two-call startup (full detail in PLAN-001 / PLAN-002). Exec-1 is VM-level;
exec-2 is project-level; the steps below run after exec-2 has loaded the
guaranteed set.

**Exec-1 (VM level, before a project is chosen):** run the sync script, then
`cat ~/projects/AGENTS.md ~/projects/OPERATOR.md`, list project folders, and
print the 3 newest session-log head lines across all projects. `OPERATOR.md`
carries the operator profile + VM facts; if it is absent (fresh clone / new
VM), prompt to create one. Select the project.

**Exec-2 (project level):** `cat` the guaranteed set — `AGENTS.override.md`,
`agents/memory/procedural.md` (full), `agents/commands/session-start.md` —
plus the ROADMAP abstract+active section and the full `work-backlog.md`. Do
NOT load `operational.md`.

**Then execute:**
1. Greet operator; identify speaker if unclear (use OPERATOR.md).
2. Confirm platform memory is disabled for this project (remind if missing).
3. Check `scratchpad.md`; flag or prune if over limits.
4. Confirm `work-backlog.md` was read; alert the operator if over 20 items.
5. `git status`, `git log --oneline -10`, `git pull`. On divergence,
   report before editing anything.
6. Read newest session log first ~10 lines (full only if continuing it).
7. Check `docs/specs/` for a spec covering the planned work.
8. Create the empty session log scaffold for today (line 1:
   `date | project | one-line-summary`).
9. Report: last session's result, open items, carried-forward blockers
   and spec gaps.

### 9.2 session-end.md — closing

1. Fill the session log (≤600 words target, ≤1 000 hard — extract if over).
2. Update the work ledger: append finished items to `work-log.md`
   (append-only) and remove their lines from `work-backlog.md`; add any new
   open items to the backlog.
3. Reconcile scratchpad (carry-forward ≤15 lines; prune working space).
4. Update long-term memory: strengthen-on-recall; new gotchas to operational
   memory; new procedural rules are operator decisions only. Operator-profile
   observations go to `~/projects/OPERATOR.md`, never into the project tree.
5. Decay sweep (§8.5) if operational memory is over its hard limit.
6. Verify specs are accurate against what was actually built.
7. Update CHANGELOG.md for user-visible changes.
8. Commit specific files + push per project settings. Never force-push.
9. Report: accomplished / open / what the next session opens first.

### 9.3 Closing-signal detection

On detecting a closing phrase ("that's it", "thanks", "good job",
"see you tomorrow", etc.): ask once — "Shall we close the session now?"
On yes, execute `session-end.md`. If `[OPEN]`/`[ACTIVE]` items remain,
note them briefly.

---

## 10. Document budgets

| Document | Soft limit | Hard limit | At soft | At hard |
|----------|-----------|------------|---------|---------|
| `agents/notes/scratchpad.md` | 30 lines | 60 lines | Prune; inform operator if still over | Must prune before adding |
| `agents/memory/operational.md` | 35 lines | 50 lines | Flag to operator | Run decay sweep before adding |
| `agents/notes/work-backlog.md` | 15 items | 20 items | Review for staleness | Alert operator — backlog problem |
| `agents/notes/work-log.md` | — | — | Append-only; never auto-read | — |
| `AGENTS.md` | 150 lines | 250 lines | Review for duplication | Extract to appropriate files |
| Session logs | 600 words | 1 000 words | Compress | Extract findings; leave pointer |
| Plan files | 150 lines | 250 lines | Review and compress | Extract to spec or session log |

---

## 11. Git automation

Set during project setup, recorded in `AGENTS.override.md` (`push`) and
`~/projects/OPERATOR.md` (`backup`), applied by session-end. Remote URL and
provider come from `.git/config`, not from any config file of ours.

| Operation | Default | Notes |
|-----------|---------|-------|
| `git add` (specific files) | Automatic | Only files worked on — never blind `-A`. |
| `git commit` | Automatic | Session end, Conventional Commits message. |
| `git push` | **Off — set per project (`push:` in override)** | On for solo/one-machine work; requires `OPERATOR.md backup` ≠ none and an `origin` remote. |

Never force-push. A non-fast-forward rejection is a safety net.

---

## 12. Adapting to a new project

1. Files ship with the template — already in place.
2. Fill AGENTS.override.md: identity diffs, persona + name, `autonomy`, `push`.
3. Create the founding spec (`SPEC-001-<name>.md`) and get operator approval.
4. Ensure `~/projects/OPERATOR.md` exists (operator profile + VM facts); it is
   per-VM, not per-project, so it is created once per machine, not per project.
5. Choose the work-ledger MODULE set for the project.
6. Set the platform-memory-disable edit in the AI client.
7. Set `push:` in the override; ensure the `origin` remote and key exist.
8. Leave `operational.md` empty — it fills as you learn.
