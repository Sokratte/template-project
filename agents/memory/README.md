# agents/memory/ — the agent's memory

Three files, one axis: **how long the knowledge stays relevant.** Not where it came from — timescale. An item moves between files as its useful life changes.

The files themselves carry almost nothing but a one-line reminder of the entry format. Everything about *why* the system is shaped this way, what belongs where, and how decay works lives here. That is deliberate: the memory files are loaded (or grepped) during real work, so every line in them is a recurring cost. This README is read by a human setting up or auditing the project, and by an agent only when it needs the full picture — so it can be as long as it needs to be.

| File | Holds | Loaded at session start | Decays? |
|------|-------|--------------------------|---------|
| `procedural.md` | Rules the agent follows automatically, every session, regardless of topic | Yes — fully (`cat`) | Never |
| `operational.md` | Counter-intuitive gotchas, looked up only when stuck | No — grep on demand | Yes (sweep) |
| `historical.md` | Retired procedures + decayed gotchas, kept for audit | No | Terminal |

(*Which file is loaded when is set by the startup sequence in `AGENTS.md` and `agents/commands/session-start.md`, not by the files themselves.*)

## Why this split

A rule that must be followed has to be in front of the agent the moment it acts — so `procedural.md` is loaded whole, every session, and is kept short so that staying loaded is cheap. A gotcha you need three times a year would be pure token cost if loaded every session — so `operational.md` is never auto-loaded; the agent greps it when an error doesn't explain itself. Once knowledge stops being used it shouldn't sit in either active file inflating load cost or grep noise — but deleting it loses the audit trail, so it moves to `historical.md`, which is kept out of the startup path entirely and read only when someone goes looking for history.

The practical test for where a piece of knowledge goes is not its subject but its lifespan and its trigger: *does the agent need this every time without being prompted* (procedural), *only when a specific problem recurs* (operational), or *never again, but it should remain on record* (historical).

## procedural.md — what the agent DOES

Always loaded, short by design. **Admission threshold:** the constraint applies to *every* session regardless of topic. Domain-specific how-to does not go here — it goes in `operational.md`.

- **Never decays.** The sweep does not touch this file.
- **Operator-gated.** Entries are added or promoted here only by the operator's decision — the agent never self-promotes a rule. Promotion happens only once something has become an instinct that genuinely applies to every session.
- **No operator profile here.** Who the operator is and how to work with them lives in `~/projects/OPERATOR.md` — per-VM, never committed, because it is personal observation about a named human (PII). This file is committed and travels with the repo; the profile must not. See SPEC-003 §8 and PLAN-001.

**Entry format** (the one line kept in the file): `- rule text [YYYY-MM-DD xN]` — date last useful, `xN` recall counter. **Strengthen on recall:** when an entry prevents a mistake, bump its tag — today's date, counter +1. One edit.

## operational.md — what the agent KNOWS

Never auto-loaded; grepped when stuck. **Admission threshold:** recurring (not a one-off), not obvious from the error message, not reachable by reading nearby docs or config. If the fix lives in the config or the code, it does not belong here. Decisions go in `docs/decisions/`, not here.

- Group entries under project-relevant headings (Tooling, Build, Environment, API quirks…). One or two lines each.
- **Entry format:** under a heading, `- gotcha [YYYY-MM-DD xN]`.
- **Strengthen on recall** exactly like procedural: bump date, +1 counter.

**Decay (the sweep).** This is what keeps `operational.md` from growing unbounded. It runs at **session end**, operator-gated, as a deterministic agent procedure (no script):

- Soft flag at **35 lines**; hard trigger at **50 lines** (or whenever the operator asks).
- For each entry, `recall_rate = counter / age_in_days`.
- Entries younger than **30 days** are protected.
- Sort lowest-rate first; whole tie-groups move together.
- The agent shows the operator the list it intends to move; only on an explicit yes does it move those entries to `historical.md` under `## stale operations`, until the file is back under 50 lines.
- `procedural.md` is never touched by the sweep.

The full procedure also lives in `agents/commands/session-end.md` (step 5) and SPEC-003 §8.5.

## historical.md — what the agent WAS

Append-only, never deleted, kept out of the startup path; read only when someone needs the history. Two fixed headings act as insertion markers for the sweep — **do not rename them**:

- `## retired procedures` — procedures deliberately retired (an operator decision, never the sweep).
- `## stale operations` — gotchas the sweep decayed out of `operational.md`.

## Tags, in one place

Every memory entry carries `[YYYY-MM-DD xN]`: the date it was last useful and a recall counter `N`. The counter drives both directions — "strengthen on recall" lets useful entries rise and survive, while the decay sweep lets unused entries fall. A higher counter means proven useful, which means protected.
