<!-- kw: document size, traffic-light, skeleton vs content, token budget, autonomous memory lifecycle, per-session usefulness M/sessions_alive, operational.md no-limit index floor, promotion demotion, memory_cutoff -->
ADR-002-document-size-governance.md

# ADR-002: Document size governance — traffic-light, human-decided

**Status:** Accepted (amended 2026-06-22)
**Created:** 2026-06-18 · **Updated:** 2026-06-22

We split project documents into two classes by load behaviour and govern
their size differently. **Skeleton files** (loaded in full at every session
start) are kept small, because their size costs tokens on every start,
forever. **Content documents** (read by index, abstract, or section, never
loaded whole) may be as long as they need to be. For skeleton files, size is
governed by a yellow/red traffic-light that operates purely on the language
level — the agent warns (yellow) or stops and forces a decision (red) at
session start. There is no deterministic algorithm that deletes or moves
content automatically. This supersedes the operational-memory decay sweep
defined in SPEC-003 §8.5.

## Amendment — 2026-06-22: autonomous memory lifecycle (supersedes the no-automatism rule for the two memory files)

The no-automatism rule below is **superseded for `procedural.md` and `operational.md` only.** Memory now self-manages at session end with no operator prompt: entries are promoted operational→procedural and demoted procedural→operational by a deterministic, session-based metric. The traffic-light + human-decided governance in the rest of this ADR remains in force for every other skeleton file (`scratchpad.md`, `work-backlog.md`, `AGENTS.override.md`, the ROADMAP abstract).

**What changed in the model:**
- `historical.md` is removed. `operational.md` becomes the unlimited, section-indexed floor — every `## heading` carries a keyword list and the file is navigated by grep / the header index. Demoted and stale knowledge lives there, greppable, with its value shown beside it.
- Tag is `[sNN xM]` — born session NN, useful M times. `value = M / sessions_alive` (sessions, not days). A newborn is born at the maximum, `1.00`.
- Cutoff `memory_cutoff` (default `0.01`) lives in `AGENTS.override.md`. Prune when `value < cutoff`; only `procedural.md` (the loaded file) is size-triggered.

**Why automation is safe now — answering this ADR’s own two objections:**
1. *“Assessment needs time; twenty rules found in one day cannot be judged that day.”* The metric **is** time, counted in sessions. A newborn is born at the maximum value (1.00), so the twenty-rules-in-one-day case cannot misfire — new entries are the highest-valued, never the prune target. Time does the assessing, exactly as this ADR demanded; the original mistake was the wall-clock-and-lines mechanism, not the principle.
2. *“An algorithm will eventually move the wrong thing.”* It no longer matters, because a move is now **reversible**: a prune is a demotion into the unlimited `operational.md`, not a deletion and not a one-way trip to a terminal file. A wrongly demoted rule stays greppable and re-promotes itself the moment it proves useful again. The risk this ADR guarded against — losing the right thing — cannot occur when nothing is lost.

The recall counter therefore returns to being **algorithm input** for these two files (its 2026-06-18 demotion to “human reading-aid only” is reversed here), while staying a reading aid for the human-governed files.

Full model: `agents/memory/README.md`. Executable form: `agents/commands/session-end.md` §5. SPEC-003 §8 is updated to match.

## Context

The system reads large files the right way: an index over first lines
(`head -qn1`), an abstract per file (`awk` to the first `##`), and a heading
map (`grep '^#'`) for section reads. Given that, a hard size cap on a large
reference document is a contradiction — it forces you to cut content apart
that the read mechanism already handles section by section. You cut yourself
off from your own material.

But there is a real case where size limits matter: files that are loaded *in
full* at every session start. A 50 KB notes file `cat` into the context
window at every start is pure, permanent performance loss, multiplied by
every session. The more we load, the worse the start performs.

The earlier mechanism for keeping operational memory small was the decay
sweep (SPEC-003 §8.5): a deterministic procedure that scored entries by
recall rate and proposed moving the weakest to historical memory. The
problem with any such automatism is the special case — find twenty new rules
in one day and the file is suddenly large, but you cannot judge *that day*
which twenty to remove. Assessment needs time. An algorithm that deletes or
moves on fixed criteria will eventually move the wrong thing.

## Decision

**Two document classes, governed differently:**

- **Skeleton** — loaded in full at every session start: `procedural.md`,
  `AGENTS.override.md`, `session-start.md`, `scratchpad.md`,
  `work-backlog.md`, and the ROADMAP abstract+active section. Size is
  governed; the metric is **tokens** (the honest unit for load cost).
- **Content** — read by index/abstract/section, never loaded whole: the five
  document types (session, research, decision, plan, spec), plus
  `operational.md` and `work-log.md`. **No size limit** —
  as long as needed.

**The traffic-light, for skeleton files only:**

- **Green** — no action.
- **Yellow** — the agent *informs* the operator at session start ("this file
  is getting large, we should look at it soon"). Work continues; no decision
  is forced.
- **Red** — the agent *halts and forces a conscious decision* at session
  start: "This file is too large. Do we deal with it now — yes or no?" On no,
  the same question returns next session, and the one after, until it is
  resolved.

Both signals are **language-level only**. The agent never runs a script that
deletes or moves content automatically. The pressure to shrink a file rises
proportionally to its size, because the red question recurs at every start
until the human acts. **The human holds both the authority and the duty** for
how large these files grow.

**The recall counter `[YYYY-MM-DD xN]` is kept** — but its role changes from
*input to an algorithm* to *reading aid for the human*. When the operator
cleans a file by hand, "used 8× / never used" is exactly the signal they want
to decide what goes.

**Concrete thresholds are per-file and deferred.** This ADR fixes the
principle. Each skeleton file will need its own metric and its own green/
yellow/red token thresholds, worked out separately (see SPEC-003 §10).

## Consequences

**Positive:**
- One model everywhere — no automatism to misfire, no special case to
  remember. Idiot-proof and portable across projects.
- Nothing is ever deleted or moved by a machine on questionable criteria.
- Large content documents stay whole and are read the way the system was
  built to read them.
- Rising, recurring pressure reliably gets files shrunk without coercion.

**Negative:**
- Cleanup depends on the human acting; a stubborn operator can defer the red
  signal indefinitely (by design — the duty is theirs).
- Per-file thresholds must still be defined; this ADR alone does not make any
  file shrink.
- Operational memory now grows until a human prunes it, where the sweep
  previously offered to do so.

## Alternatives considered

| Option | Why rejected |
|--------|-------------|
| Keep the decay sweep | A deterministic algorithm cannot judge the special case (twenty rules found in one day); assessment needs time only a human has. |
| Hard cap on all files | Forces cutting content the index/abstract/section reads already handle. You cut yourself off from your own material. |
| Automatic write-lock at red | Blocks the operator mid-work; a forced conscious decision at start is enough and keeps control human. |
| Auto-eviction of weakest entry | Same flaw as the sweep — it may evict the wrong thing on fixed criteria. |
