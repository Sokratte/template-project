# agents/memory/ — the agent's memory

Two files, one axis: **how universal the knowledge is.** An entry moves between them **automatically** as it earns or loses that status — the operator never has to touch a memory file. Nothing is ever discarded by the system: `operational.md` is the floor, and it has no size limit, so knowledge only ever moves *down* into it, never out.

The files themselves carry almost nothing but a one-line reminder of the entry format and (in `operational.md`) the section index. Everything about *why* the system is shaped this way, what belongs where, and how the promotion and pruning machinery works lives here. That is deliberate: the memory files are loaded (or grepped) during real work, so every line in them is a recurring cost. This README is read by a human setting up or auditing the project, and by an agent only when it needs the full picture — so it can be as long as it needs to be.

| File | Holds | Loaded at session start | Size-limited |
|------|-------|--------------------------|--------------|
| `procedural.md` | Rules the agent follows automatically, every session, regardless of topic | Yes — fully (`cat`) | Yes — limit is the prune trigger |
| `operational.md` | Everything else worth keeping: gotchas, and demoted rules. Looked up by grep / section index | No — grep on demand | No — grows freely; it is the archive |

(*Which file is loaded when is set by the startup sequence in `AGENTS.md` and `agents/commands/session-start.md`, not by the files themselves.*)

## Why two files, not three

There used to be a third file (`historical.md`) for retired knowledge. It is gone. Because `operational.md` has no size limit and is fully indexed by section headers with keywords, it *is* the archive: a demoted or stale rule sits there, greppable, with its usefulness value visible next to it. A separate terminal file bought nothing but an extra file to maintain. One fewer file, and old knowledge stays findable by the same grep you already use.

A rule that must be followed has to be in front of the agent the moment it acts — so `procedural.md` is loaded whole, every session, and is kept short, which is why it is the only file with a size limit. A gotcha you need three times a year would be pure token cost if loaded every session — so `operational.md` is never auto-loaded; the agent greps it (by keyword, via the section index) when it needs something.

## The lifecycle — how knowledge moves on its own

Everything runs unattended at session end, so an operator who never wants to think about memory files doesn't have to.

**Tag.** Every entry carries `[sNN xM]`: born in session `NN`, useful `M` times. A new entry is born `[s<current> x1]` — it was useful once (that is why you are writing it down), so `M` starts at 1, never 0.

**Usefulness value** = `M / sessions_alive`, where `sessions_alive = current_session − NN + 1`. A same-session newborn is `1 / 1 = 1.00` — the maximum. It is a lifetime average measured in sessions, not days: calendar gaps never count against an entry, only sessions where it *could* have helped and didn't. **Strengthen on recall:** whenever an entry earns its keep this session, bump `M` by one; its value jumps back up. Left unused, the value drifts down session by session.

**Cutoff.** One threshold, `memory_cutoff`, in `AGENTS.override.md`, default `0.01`. An entry is prunable when `value < cutoff`. Floor, default, cutoff — all the same number; raise it to forget more aggressively, lower it to keep almost everything. At the 0.01 default it takes ~100 unused sessions for a newborn to become prunable, so nothing is lost lightly.

**Promotion (operational → procedural), autonomous.** When an operational entry has become topic-independent (the agent should do it *every* session regardless of subject), is proven (`M ≥ 3`), and is currently useful (`value ≥ cutoff`), the agent promotes it at session end — no prompt. The line moves to `procedural.md`, tag intact. The "currently useful" condition is what keeps a freshly demoted rule from bouncing straight back up.

**Pruning / demotion (procedural → operational), autonomous, size-triggered.** `procedural.md` is the only file with a limit, because it is the only one loaded every session. The prune fires *only* when it crosses that limit, in two stages:

- Over the **soft** limit → demote only entries with `value < cutoff`. Entries at or above cutoff are spared, even if that leaves the file over soft. (Soft = clear the dead wood.)
- Over the **hard** limit → demote everything below cutoff, then keep demoting the lowest-valued survivors (entries of equal value move as a whole group — all of them or none) until the file is back under hard. Stop the moment you are under.

Demote means **move the line into `operational.md`** under its topical section (extend that section's keywords), not delete it. Since `operational.md` has no limit, the demotion always lands. A wrongly promoted rule is self-correcting: if it was not really universal it stops earning recalls, its value falls, and a future prune demotes it back to `operational.md` — the test of time, enforced mechanically.

The executable form of all this is `agents/commands/session-end.md` step 5.

## procedural.md — what the agent DOES

Always loaded, short by design, the only size-limited memory file. **Admission threshold:** the constraint applies to *every* session regardless of topic. Domain-specific how-to does not go here — it goes in `operational.md`.

- **Entries arrive by promotion** from `operational.md` (topic-independent + `M ≥ 3` + useful). The operator may also add a rule directly.
- **Entries leave by demotion** to `operational.md` when a size-triggered prune finds them below cutoff or among the lowest survivors at the hard limit. Nothing is deleted.
- **No operator profile here.** Who the operator is and how to work with them lives in `~/projects/LOCAL.md` — per-VM, never committed, because it is personal observation about a named human (PII). This file is committed and travels with the repo; the profile must not. See SPEC-003 §8 and PLAN-001.

**Entry format:** `- rule text [sNN xM]`. **Strengthen on recall:** when it prevents a mistake, bump `M`. One edit.

## operational.md — what the agent KNOWS

Never auto-loaded; grepped when stuck. No size limit — it is the floor and the archive. Navigated by its **section index**: every `## heading` carries a keyword list, so a grep on a keyword (or a scan of the headers) finds the right section without loading the file.

**Admission threshold:** recurring (not a one-off), not obvious from the error message, not reachable by reading nearby docs or config. If the fix lives in the config or the code, it does not belong here. Decisions go in `docs/decisions/`, not here.

- You never refuse a write here and it is never pruned — it is kept navigable by the section index, not bounded by a limit.
- Group entries under keyworded headings: `## Tooling · keywords: …`. Add the entry's distinctive terms to the heading's keyword list.
- **Entry format:** under a heading, `- gotcha [sNN xM]`.
- **Strengthen on recall** exactly like procedural: bump `M`.
- Entries are scored (the value is computed and visible) even though `operational.md` itself is never pruned today. Keeping the score live means a future operational-forgetting policy is a switch to flip, not a migration.

## Tags, in one place

Every memory entry carries `[sNN xM]`: born in session `NN`, useful `M` times. `value = M / (current_session − NN + 1)` drives everything — "strengthen on recall" raises it (promoting the best operational entries up), the size-triggered prune demotes the lowest procedural entries down. Higher value means more proven, which means safer.
