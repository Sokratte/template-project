# Session Start

Orient yourself before doing anything. Follow these steps in order. **Execute them — do not merely read them.** They run after the project's startup set has been loaded (see `AGENTS.md` for the loading call).

1. **Greet** the operator (use `OPERATOR.md`). If the project has multiple known speakers and it's not clear who this is, ask once.
2. **Confirm platform memory is disabled** for this project. If it looks enabled, remind the operator — running it alongside file memory creates two diverging sources of truth.
3. **Check the scratchpad** — `agents/notes/scratchpad.md`, against the traffic-light (§10, ADR-002). Yellow: note it, prune at session end. Red: force a prune-or-defer decision before doing anything else.
4. **Confirm the backlog was read** — `agents/notes/work-backlog.md`. Alert the operator if it holds more than 20 open items.
5. **Check skeleton files against the traffic-light** (§10). Surface any yellow (inform) or red (force a decision) signal here, at the top of the session, so the operator can act before work starts.
6. **Check git state:** `git status`, `git log --oneline -10`, `git pull`. If `git pull` reports divergence or conflict, do not edit anything — report to the operator first. (The working copy can move under you; re-check right before any commit, not only here.)
7. **Read the last session log** — newest file in `docs/sessions/`, first ~10 lines (title, date, goal, status). Load fully only if this session continues the same task directly.
8. **Check for a spec.** Before doing any work, check `docs/specs/` for a spec covering the work ahead. If one exists, read it (heading-map via `grep -n '^#\+ '`, then the relevant section via awk). If the planned work is non-trivial and no spec exists, flag it to the operator before starting.
9. **Prepare the session log scaffold.** Create an empty `docs/sessions/YYYY-MM-DD-<topic>.md`. Line 1 is the greppable index entry: `filename | keywords`. Fill it throughout the session; complete it at session end.

**Report to the operator:** what the last session accomplished (from the session log / work ledger); what is open or in progress (latest `[OPEN]`/`[ACTIVE]` backlog entries); any open questions, blockers, or spec gaps carried forward.

Do not begin any task before this orientation is complete.
