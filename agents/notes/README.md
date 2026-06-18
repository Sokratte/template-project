# agents/notes/ — working memory and the work ledger

Three files that track *what is being worked on and what has been done* — as opposed to `agents/memory/`, which holds the rules and knowledge the agent works *by*. Notes are about the work; memory is about how to work.

As with the memory files, the files here carry only a one-line reminder at the top. The full explanation of how each one is meant to be used lives in this README, which a human reads when setting up or auditing the project. The files stay lean because two of them are read on every session start.

| File | Holds | Loaded at session start | Grows? |
|------|-------|--------------------------|--------|
| `scratchpad.md` | The agent's live working space + a carry-forward note to its next self | Yes — checked | Bounded (pruned every session) |
| `work-backlog.md` | Open work: TODOs, findings, pending decisions | Yes — read fully | Bounded (alarm over 20 items) |
| `work-log.md` | Done work, append-only history | No — grep on demand | Unbounded (by design) |

(*When each file is read is set by the startup sequence in `AGENTS.md` and `agents/commands/session-start.md`, not by the files themselves.*)

## The backlog / log split

"Backlog" = ahead of you (open). "Log" = behind you (done). They are two files on purpose:

- **`work-backlog.md` is a pruned, living list** — only things still open. When an item is finished it does **not** get a `[DONE]` tag in place; its line is **moved** to `work-log.md`. Nothing finished is ever left in the backlog. This is what keeps open work from being buried under a growing pile of completed history — the original problem this split was created to fix.
- **`work-log.md` is append-only** — the permanent record. Existing lines are never edited or deleted, so the past stays auditable. It is never loaded at session start; you grep it when you need to know when or how something was done.

Keeping "append-only" on the log and "pruned living list" on the backlog is the whole point: each file has exactly one discipline, and they don't conflict.

### Line format (both files)

```
YYYY-MM-DD | MODULE     | [TAG]    | description | file-ref
```

- **MODULE** (~9 chars): a category that fits this project. A small, stable starting set: PROJECT, META, DOCS, CODE, TEST, INFRA, DESIGN, RESEARCH. Keep the set small — resist inventing a new module per item.
- **TAG:**
  - `[OPEN]` — not started
  - `[ACTIVE]` — in progress
  - `[FIND]` — something the agent discovered that needs operator discussion
  - `[DONE]` — only ever in `work-log.md`, with the completion date
- **file-ref:** the relevant path, or `-`.

### The 20-item alarm

If `work-backlog.md` holds **more than 20 open items**, the agent alerts the operator. That many open items is a signal of a real backlog problem or a mis-set preference — not a formatting issue to be silently tidied. There is no line limit; the item count is the meaningful threshold.

## scratchpad.md — the agent's working space

Two sections, divided by `---`. Keep both lean; this is temporary by nature. If it keeps growing, the content belongs somewhere more permanent — a plan, a spec, the backlog, or operational memory.

- **Carry-forward** (top, **≤15 lines**): the note the agent leaves its next self — open threads, standing operator instructions, context not captured anywhere else. Read first at session start. If a carry-forward item matures into real work, move it to `work-backlog.md`. If this section won't fit in 15 lines, something in it belongs in a plan, a spec, or memory instead.
- **Working space** (below the divider): current focus, half-formed thoughts, threads being actively worked. Pruned at **every** session end — resolved threads are removed entirely, not struck through.

**Limits:** soft at **30 lines** total — prune resolved threads at session end, and if it's still over, tell the operator there may be stale content worth reviewing together. Hard at **60 lines** — must prune before adding anything new.

## Lifecycle, end to end

A thought usually enters as a loose line in the scratchpad working space. If it turns out to be real work, it becomes an `[OPEN]` item in `work-backlog.md`. While being worked it may go `[ACTIVE]`; a discovery that needs you is `[FIND]`. When it's finished, its line moves to `work-log.md` as `[DONE]` with the date, and any related scratchpad thread is pruned. Nothing is duplicated across files at rest — at any moment a given piece of work lives in exactly one of them.
