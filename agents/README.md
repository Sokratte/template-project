# agents/ — Machinery

**What this is:** everything the AI loads to work in this repo — memory,
commands, the work ledger, the scratchpad. No project content; the *how
of the work*, not the *what*.

| File | Role | Loaded |
|------|------|--------|
| `commands/session-start.md` | Orientation procedure | Executed at session start |
| `commands/session-end.md` | Closing procedure | Executed at session end |
| `commands/daily-digest.md` | Human-readable overview (on demand) | On request only |
| `procedural-memory.md` | Rules + operator profile — what the agent IS | Fully, every session |
| `operational-memory.md` | Gotchas — what the agent KNOWS | Only via grep when stuck |
| `historical-memory.md` | Retired — what the agent WAS | Never automatically |
| `worklog.md` | Central work ledger (append-only) | Scanned at session start |
| `worklog-archive.md` | Aged-out worklog entries | Never |
| `scratchpad.md` | Carry-forward + working space (kept small) | Checked at session start |

The full specification of this system lives in
`docs/specs/SPEC-003-agent-memory-system.md`.
