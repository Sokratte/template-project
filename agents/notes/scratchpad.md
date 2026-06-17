# Scratchpad

*The agent's working space. Two sections — keep both lean.*

**Carry-forward** (top, ≤15 lines): things to remember at the next session
start — open threads, operator instructions, context that isn't captured
elsewhere. If a carry-forward item matures into real work, move it to the
worklog. If this section grows past 15 lines, something belongs in a plan,
a spec, or tribal knowledge instead.

**Working space** (below the divider): current focus, half-formed thoughts,
loose threads being actively worked. Prune at every session end — remove
resolved threads entirely, don't just strike through.

*Keep it temporary. If it's growing, something belongs somewhere else.*

**Soft limit: ~30 lines.** Prune resolved threads at session end; if still
over, inform the operator — there may be stale content worth reviewing.
**Hard limit: ~60 lines.** Must prune before adding anything new.

---

## Carry-forward

*(≤15 lines — things to remember next session)*

- PLAN-001 is the locked spec for the multi-VM agent architecture. Build
  follows it. Read it first next session.
- NEXT: draft the canonical `AGENTS.md`. Operator rule: **sign-off on every
  step — write nothing without approval.**
- First sub-decisions when drafting: autonomy level names
  (autonomous/checkpoint/confirm) + the new-project default; the ~150-line
  budget split (what stays vs. goes to machinery).
- Separate deferred task: stale-doc cleanup (paths → on-disk names; remove
  sweep-knowledge.py into session-end.md; drop daily-digest.md). Touches the
  command files — do in one pass.
- Note: sandbox tools (str_replace/create_file/view) can't see the real FS;
  use the filesystem MCP tools for all project files.

---

## Working space

*(Current focus, loose threads — prune at session end)*
