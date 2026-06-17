# Session Start

Orient yourself before doing anything. Follow this order exactly.
**Execute these steps — do not merely read them.**

0. **Greet** the operator warmly. If the project has multiple known speakers
   and it's not clear who this is, ask once.

1. **Load orientation, in this order:**
   - `~/workspace/AGENTS.md` — global rules (if not already loaded)
   - `AGENTS.md` (this project) — identity, rules, tools, memory system
   - `ROADMAP.md` — current direction and active plans
   - `agents/procedural-memory.md` — rules and operator profile.
     **Always load fully.**
   - `agents/operational-memory.md` — do NOT load. Grep only when stuck.

2. **Check memory state:**
   - `agents/scratchpad.md` — your carry-forward and any open threads.
     If over soft limit (30 lines): note it, prune at session end.
     If over hard limit (60 lines): prune now before doing anything else.

3. **Scan the worklog** — `agents/worklog.md`.
   Run cleanup if > 60 lines or > ~4 KB: move `[DONE]`/`[NOTE]` entries
   older than 30 days to `agents/worklog-archive.md`. `[OPEN]`/`[ACTIVE]`
   never age out.

4. **Check git state:** `git status`, `git log --oneline -10`, `git pull`.
   If `git pull` reports divergence or conflict: do not edit anything —
   report to the operator first.

5. **Read the last session log** — newest file in `changelog/session-logs/`,
   first ~10 lines (title, date, goal, status). Load fully only if this
   session continues the same task directly.

6. **Check for a spec.** Before doing any work, check `docs/specs/` for a
   spec covering the work ahead. If one exists, read it. If the planned work
   is non-trivial and no spec exists, flag it to the operator before starting.

7. **Prepare the session log scaffold.** Create an empty
   `changelog/session-logs/YYYY-MM-DD-<topic>.md` with title and date.
   Fill it throughout the session; complete it at session end.

**Report to the operator:**
- What the last session accomplished (from session log / worklog)
- What is open or in progress (latest `[OPEN]`/`[ACTIVE]` worklog entries)
- Any open questions, blockers, or spec gaps carried forward

Do not begin any task before this orientation is complete.
