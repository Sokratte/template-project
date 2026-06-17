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
agents/
  commands/
    session-start.md       ← orientation procedure — EXECUTE at session start
    session-end.md         ← closing procedure — EXECUTE at session end
    daily-digest.md        ← on-demand human overview (not part of lifecycle)
  worklog.md               ← append-only work ledger
  worklog-archive.md       ← aged-out worklog entries
  scratchpad.md            ← carry-forward + working space
  procedural-memory.md     ← rules + operator profile — what the agent IS
  operational-memory.md    ← gotchas — what the agent KNOWS
  historical-memory.md     ← retired — what the agent WAS
  README.md                ← index of the above
tools/scripts/
  sweep-knowledge.py       ← deterministic decay sweep for operational-memory.md
ROADMAP.md                 ← project direction, milestones, active plans
AGENTS.md                  ← stable project identity, rules, tools, this system
docs/specs/                ← what the project builds — the target
docs/plans/                ← short-lived task plans
docs/decisions/            ← architecture decision records (immutable once ratified)
changelog/session-logs/    ← per-session technical record
```

Optional (add if the project needs them):
```
docs/research/             ← domain knowledge, market analysis, dated
docs/runbooks/             ← operational guides for live services
```

---

## 4. AGENTS.md — the stable anchor

Loaded first, every session. **Stable by design** — changes only when
something fundamental changes. **Never a scratchpad.**

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

Work logs → `agents/worklog.md`.
Loose notes → `agents/scratchpad.md`.
Procedures and operator profile → `agents/procedural-memory.md`.
Operational gotchas → `agents/operational-memory.md`.
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

### 7.1 worklog.md — the central ledger

The single live work list. **Append-only** — existing lines never edited.
Updated the moment state changes, not batched at session end.

**Line format:**
```
YYYY-MM-DD HH:MM | MODULE     | [TAG]    | Description | file-ref
```

- **MODULE** — project-relevant category (PROJECT, META, DOCS, CODE, TEST,
  INFRA, etc.). Keep the set small and stable.
- **TAG** — `[OPEN]` not started · `[ACTIVE]` in progress · `[DONE]`
  finished · `[NOTE]` context without action · `[FIND]` agent discovery
  needing discussion.
- **file-ref** — path or `-`.

**Size:** soft 60 lines → run `[DONE]`/`[NOTE]` cleanup at session start.
Hard 100 lines → force cleanup before adding anything new.

**Cleanup:** `[DONE]`/`[NOTE]` entries older than 30 days move to
`worklog-archive.md`. `[OPEN]`/`[ACTIVE]` never age out.

### 7.2 scratchpad.md — carry-forward and working space

One file, two structured sections:

**`## Carry-forward` (≤15 lines)** — things to remember at the next session
start. Open threads, context not captured elsewhere. If an item matures into
real work, it moves to the worklog. If this section grows past 15 lines,
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

### 8.1 procedural-memory.md — what the agent IS

**Always loaded fully at session start.** Contains two sections:

**Operator profile** — who the operator is and how to work with them. A few
stable lines written during setup and refined as patterns emerge. Examples:
communication style, decision-making approach, when to push back vs execute.
This is the "relationship memory" that makes collaboration increasingly
effective over time.

**Procedural rules** — constraints applied proactively every session,
regardless of topic. The admission bar is high: only things that apply to
*every* session, every kind of work. Domain-specific how-to belongs in
operational memory.

Never decays. Operator-only changes. Promotion of an operational fact to a
procedural rule is a deliberate human act, never automatic.

### 8.2 operational-memory.md — what the agent KNOWS

Counter-intuitive gotchas. **Never loaded fully.** Grepped only when stuck.

Admission threshold: recurring (not a one-off), not obvious from the error
message, not reachable by reading the nearby docs or config. If the fix is
in the config or the code, it doesn't belong here. Decisions go in
`docs/decisions/`.

**Size:** soft 35 lines → flag to operator. Hard 50 lines → offer decay
sweep before adding new entries.

### 8.3 historical-memory.md — what the agent WAS

Never loaded automatically. Two sections with exact headings the sweep uses:
`## retired procedures` (operator decision) and `## stale operations` (sweep).
Append-only, never deleted — the past is auditable.

### 8.4 Strengthen on recall

Every memory entry carries `[YYYY-MM-DD xN]` — date last used, recall
counter. When an entry helps, the agent patches the tag: today's date,
counter +1. Frequently-useful entries stay strong; unused ones fade.

### 8.5 Decay sweep

When `operational-memory.md` exceeds 50 lines, `tools/scripts/sweep-knowledge.py`
moves the least-recalled entries to the historical file. Deterministic —
pure arithmetic on the tags, no LLM.

Metric: `recall_rate = counter / age_in_days`. Lowest rate first; whole
tie-groups move together; entries younger than 30 days protected.

**Operator-gated.** Dry-run shown first; applies only on explicit yes.
`procedural-memory.md` is never touched.

```
python3 tools/scripts/sweep-knowledge.py            # dry-run
python3 tools/scripts/sweep-knowledge.py --apply    # apply
```

---

## 9. The session lifecycle

### 9.1 session-start.md — orientation

1. Greet operator; identify speaker if unclear.
2. Load: global AGENTS.md → project AGENTS.md → ROADMAP.md →
   `procedural-memory.md` (full). Do NOT load `operational-memory.md`.
3. Check `scratchpad.md`; flag or prune if over limits.
4. Scan `worklog.md`; run cleanup if over soft limit.
5. `git status`, `git log --oneline -10`, `git pull`. On divergence,
   report before editing anything.
6. Read newest session log first ~10 lines (full only if continuing it).
7. Check `docs/specs/` for a spec covering the planned work.
8. Create the empty session log scaffold for today.
9. Report: last session's result, open items, carried-forward blockers
   and spec gaps.

### 9.2 session-end.md — closing

1. Fill the session log (≤600 words target, ≤1 000 hard — extract if over).
2. Append to worklog (append-only).
3. Reconcile scratchpad (carry-forward ≤15 lines; prune working space).
4. Update long-term memory: strengthen-on-recall; new gotchas to operational
   memory; operator observations to procedural profile; promotions to
   procedural rules are operator decisions only.
5. Decay sweep if operational memory is over hard limit.
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
| `agents/scratchpad.md` | 30 lines | 60 lines | Prune; inform operator if still over | Must prune before adding |
| `agents/operational-memory.md` | 35 lines | 50 lines | Flag to operator | Offer sweep before adding |
| `agents/worklog.md` | 60 lines | 100 lines | Cleanup at session start | Force cleanup first |
| `AGENTS.md` | 150 lines | 250 lines | Review for duplication | Extract to appropriate files |
| Session logs | 600 words | 1 000 words | Compress | Extract findings; leave pointer |
| Plan files | 150 lines | 250 lines | Review and compress | Extract to spec or session log |

---

## 11. Git automation

Set during project setup, recorded in AGENTS.md, applied by session-end:

| Operation | Default | Notes |
|-----------|---------|-------|
| `git add` (specific files) | Automatic | Only files worked on — never blind `-A`. |
| `git commit` | Automatic | Session end, Conventional Commits message. |
| `git push` | **Off — ask at setup** | Recommended on for solo/one-machine work. |

Never force-push. A non-fast-forward rejection is a safety net.

---

## 12. Tool compatibility (model-agnostic + Claude Code)

The canonical location for all agent machinery is `agents/commands/`. For
Claude Code compatibility, create symlinks during project setup:

```bash
ln -s AGENTS.md CLAUDE.md
mkdir -p .claude
ln -s ../agents/commands .claude/commands
```

This gives Claude Code its expected file locations while keeping the
canonical files model-agnostic.

---

## 13. Adapting to a new project

1. Files ship with the template — already in place.
2. Fill AGENTS.md: identity, anti-goals, Tools, git automation choices.
3. Create the founding spec (`SPEC-001-<name>.md`) and get operator approval.
4. Fill `procedural-memory.md` operator profile section (brief, a few lines).
5. Choose the worklog MODULE set for the project.
6. Set the platform-memory-disable edit in the AI client.
7. Decide `git push` automation.
8. Optionally create `.claude/` symlinks for Claude Code (setup Step 7).
9. Leave `operational-memory.md` empty — it fills as you learn.
