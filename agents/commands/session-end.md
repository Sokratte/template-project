# Session End

Closing procedure. Do all of it before you say "done." No step is optional; none is deferred to "next session." **Execute these steps — do not merely read them.**

1. **Session log** — `docs/sessions/YYYY-MM-DD-<topic>.md`
   Fill the scaffold created at session start: what was done, found, decided, what is open. Line 1 is the greppable index entry: `filename | keywords`. If work is unfinished, add a "State at close" section so the next session can resume without re-reading the whole chat.
   **No word limit** — a session log is a content document, read by section, not loaded whole. But extract durable findings (specs, operational memory, research) and leave a pointer rather than burying them here.

2. **Work ledger** — `agents/notes/work-backlog.md` + `agents/notes/work-log.md`
   - Finished items: **move** the line from `work-backlog.md` to `work-log.md` (append-only) with `[DONE]` and today's date. Do not leave a `[DONE]` line behind in the backlog.
   - New open items found this session: add to `work-backlog.md` as `[OPEN]`/`[ACTIVE]`/`[FIND]`.
   - Update the ledger the moment state changes — not in a batch here.
   - If `work-backlog.md` is over 20 open items: alert the operator (real backlog problem or a mis-set preference, not a formatting issue).

3. **Scratchpad** — `agents/notes/scratchpad.md`
   Reconcile both sections:
   - **Carry-forward:** remove items that are resolved or captured elsewhere; add anything the next session must know. Keep it tight — it is re-read at every start.
   - **Working space:** remove resolved threads. Move matured ones to the backlog or a plan.
   If the file is at its yellow/red signal (§10) after pruning, inform the operator — there may be stale content worth reviewing together.

4. **Memory** — `agents/memory/procedural.md` / `agents/memory/operational.md`
   - *Strengthen on recall:* if you used an entry and it helped, patch its tag — today's date, counter +1 (`[YYYY-MM-DD xN]`).
   - *New gotchas:* add to `operational.md` only — recurring, non-obvious from the error, not reachable by reading nearby docs. Start new entries at `x1` with today's date.
   - *Operator observations:* if you learned something meaningful about how the operator thinks or works, record it in `~/projects/OPERATOR.md` — NEVER in the project tree. The operator profile is per-VM and is PII; it must not be committed.
   - *Promotion to a procedural rule:* only when something has become an automatic instinct that applies to every session. The operator decides — never self-promote.
   - If `operational.md` is at its yellow/red signal (§10): flag it. At red, prune with the operator (step 5).

5. **Prune at red (operator-decided)** — if any skeleton file is at its red signal (§10, ADR-002). There is no automatic sweep:
   - Show the operator the file and, for memory files, the recall counters (`[YYYY-MM-DD xN]`) as a guide to what is least used.
   - The operator decides which entries are stale. On an explicit yes, move the chosen lines to `historical.md` under `## stale operations`.
   - `procedural.md` is never pruned this way — retiring a rule is a separate, deliberate operator decision. Include changed files in the step-8 commit.

6. **Specs** — if any spec was changed or a new one created this session, verify it accurately reflects what was actually built or decided.

7. **CHANGELOG.md** — add entries under `[Unreleased]` for any user-visible changes: Added, Changed, Fixed, Removed, Deprecated, Security.

8. **Commit and push:**
   ```
   git status                  # check first — parallel edits?
   git add <specific files>    # only the files you worked on — never -A
   git commit -m "<type>(scope): <description>"
   git push                    # if push: on for this project (override) and
                               # OPERATOR.md backup != none and origin is set
   ```
   Never force-push. If rejected, diff against remote, merge by hand, then push. Confirm with `git status` afterward — tree must be clean.

9. **Report** — one sentence each: what was accomplished, what is open, what the next session should open first.

---

Checklist (tick before "done"):
- [ ] Session log filled (line 1: `filename | keywords`; durable findings extracted with pointers)
- [ ] Finished items moved backlog → log; new open items in backlog
- [ ] Scratchpad reconciled (carry-forward kept tight)
- [ ] Memory updated (strengthen on recall; new gotchas → operational; operator observations → OPERATOR.md, never the tree)
- [ ] Traffic-light checked; pruned with operator if any skeleton file at red
- [ ] Specs verified accurate
- [ ] CHANGELOG updated (if user-visible changes)
- [ ] Committed + pushed if enabled; tree clean
