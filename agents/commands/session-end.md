# Session End

Closing procedure. Do all of it before you say "done."
No step is optional; none is deferred to "next session."
**Execute these steps — do not merely read them.**

1. **Session log** — `changelog/session-logs/YYYY-MM-DD-<topic>.md`
   Fill the scaffold created at session start: what was done, found, decided,
   what is open. If work is unfinished, add a "State at close" section so the
   next session can resume without re-reading the whole chat.
   **Soft limit: 600 words. Hard limit: 1 000 words.** Over 1 000 words means
   something belongs in a spec, operational memory, or research doc — extract
   it and leave a pointer.

2. **Worklog** — `agents/worklog.md`
   Append new lines only: `[DONE]`, `[OPEN]`, `[FIND]`. Never edit existing
   lines. Update the worklog the moment state changes — not in a batch here.
   If over soft limit (60 lines): run the cleanup pass now.

3. **Scratchpad** — `agents/scratchpad.md`
   Reconcile both sections:
   - **Carry-forward:** remove items that are resolved or captured elsewhere;
     add anything the next session must know. Keep it ≤15 lines.
   - **Working space:** remove resolved threads. Move matured ones to the
     worklog or a plan. Keep it lean.
   If the total file is over soft limit (30 lines) after pruning, inform the
   operator — there may be stale content worth reviewing together.

4. **Memory** — `agents/procedural-memory.md` / `agents/operational-memory.md`

   *Strengthen on recall:* if you used an entry and it helped, patch its tag —
   today's date, counter +1 (`[YYYY-MM-DD xN]`).

   *New gotchas:* add to `operational-memory.md` only — recurring, non-obvious
   from the error, not reachable by reading nearby docs. Start new entries at
   `x1` with today's date.

   *Operator profile:* if you observed something meaningful about how the
   operator thinks or works this session, add or refine a line in the
   `## Operator profile` section of `procedural-memory.md`.

   *Promotion to a procedural rule:* only when something has become an
   automatic instinct. The operator decides — never self-promote.

   If `operational-memory.md` is over soft limit (35 lines): flag to operator.
   If over hard limit (50 lines): run decay sweep (step 5).

5. **Decay sweep (operator-gated)** — if `operational-memory.md` is over 50
   lines, or the operator asks:
   ```
   python3 tools/scripts/sweep-knowledge.py            # dry-run
   python3 tools/scripts/sweep-knowledge.py --apply    # on operator yes
   ```
   Least-recalled entries move to `historical-memory.md` under
   `## stale operations`. `procedural-memory.md` is never touched.
   Include changed files in the step-7 commit.

6. **Specs** — if any spec was changed or a new one created this session,
   verify it accurately reflects what was actually built or decided.

7. **CHANGELOG.md** — add entries under `[Unreleased]` for any user-visible
   changes: Added, Changed, Fixed, Removed, Deprecated, Security.

8. **Commit and push:**
   ```
   git status                  # check first — parallel edits?
   git add <specific files>    # only the files you worked on
   git commit -m "<type>(scope): <description>"
   git push                    # if enabled for this project (see AGENTS.md)
   ```
   Never force-push. If rejected, diff against remote, merge by hand, then
   push. Confirm with `git status` afterward — tree must be clean.

9. **Report** — one sentence each: what was accomplished, what is open, what
   the next session should open first.

---

Checklist (tick before "done"):
- [ ] Session log filled (≤1 000 words, or extracted)
- [ ] Worklog appended (append-only)
- [ ] Scratchpad reconciled (carry-forward ≤15 lines)
- [ ] Memory updated (strengthen on recall; new gotchas → operational;
      operator observations → procedural profile)
- [ ] Decay sweep checked if operational over threshold
- [ ] Specs verified accurate
- [ ] CHANGELOG updated (if user-visible changes)
- [ ] Committed + pushed if enabled; tree clean
