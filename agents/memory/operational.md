# Operational Memory

*Counter-intuitive gotchas — looked up via grep when stuck. **Never loaded
fully at session start.** This is operational memory: what the agent KNOWS
when it needs to know it, not what it does automatically.*

*Strengthen on recall: if an entry solves your problem, update its tag —
date + counter. Useful entries stay near the top; stale ones fade via sweep.*

*Admission threshold: recurring (not a one-off), not obvious from the error
message, not reachable by reading the nearby docs or config. If the fix is
in the config or the code, it doesn't belong here. Decisions go in
`docs/decisions/`, not here.*

*Decay: when this file exceeds 50 lines, the sweep (`tools/scripts/sweep-knowledge.py`)
moves the least-recalled entries to `historical-memory.md`. Metric:
recall_rate = counter / age_in_days. Entries younger than 30 days are
protected. The sweep is operator-gated — a dry-run is shown first.*

---

<!-- Group entries under project-relevant headings, e.g.:
     ## Tooling, ## Build, ## Environment, ## API quirks
     Each entry one or two lines with a [YYYY-MM-DD xN] tag.
     Delete this comment once real entries exist. -->
