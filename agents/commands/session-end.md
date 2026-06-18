# Session End

Closing procedure. Do all of it before you say "done." No step is optional; none is deferred to "next session." **Execute these steps — do not merely read them.**

1. **Session log** — `docs/sessions/YYYY-MM-DD-<topic>.md`
   Fill the scaffold created at session start: what was done, found, decided, what is open. Line 1 is the greppable abstract: `date | project | one-line-summary`. If work is unfinished, add a "State at close" section so the next session can resume without re-reading the whole chat.
   **Soft limit: 600 words. Hard limit: 1 000 words.** Over 1 000 words means something belongs in a spec, operational memory, or research doc — extract it and leave a pointer.

2. **Work ledger** — `agents/notes/work-backlog.md` + `agents/notes/work-log.md`
   - Finished items: **move** the line from `work-backlog.md` to `work-log.md` (append-only) with `[DONE]` and today's date. Do not leave a `[DONE]` line behind in the backlog.
   - New open items found this session: add to `work-backlog.md` as `[OPEN]`/`[ACTIVE]`/`[FIND]`.
   - Update the ledger the moment state changes — not in a batch here.
   - If `work-backlog.md` is over 20 open items: alert the operator (real backlog problem or a mis-set preference, not a formatting issue).

3. **Scratchpad** — `agents/notes/scratchpad.md`
   Reconcile both sections:
   - **Carry-forward:** remove items that are resolved or captured elsewhere; add anything the next session must know. Keep it ≤15 lines.
   - **Working space:** remove resolved threads. Move matured ones to the backlog or a plan. Keep it lean.
   If the total file is over soft limit (30 lines) after pruning, inform the operator — there may be stale content worth reviewing together.

4. **Memory** — `agents/memory/procedural.md` / `agents/memory/operational.md`
   - *Strengthen on recall:* if you used an entry and it helped, patch its tag — today's date, counter +1 (`[YYYY-MM-DD xN]`).
   - *New gotchas:* add to `operational.md` only — recurring, non-obvious from the error, not reachable by reading nearby docs. Start new entries at `x1` with today's date.
   - *Operator observations:* if you learned something meaningful about how the operator thinks or works, record it in `~/projects/OPERATOR.md` — NEVER in the project tree. The operator profile is per-VM and is PII; it must not be committed.
   - *Promotion to a procedural rule:* only when something has become an automatic instinct that applies to every session. The operator decides — never self-promote.
   - If `operational.md` is over soft limit (35 lines): flag to operator. If over hard limit (50 lines): run decay sweep (step 5).

5. **Decay sweep (operator-gated)** — if `operational.md` is over 50 lines, or the operator asks. This is a deterministic agent procedure, no script:
   - Parse each entry's `[YYYY-MM-DD xN]` tag.
   - Compute `recall_rate = counter / age_in_days`; entries younger than 30 days are protected.
   - Sort lowest-rate first; whole tie-groups move together.
   - Show the operator the list you intend to move; on an explicit yes, move those entries to `historical.md` under `## stale operations` until the file is back under 50 lines.
   `procedural.md` is never touched. Include changed files in the step-8 commit.

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
- [ ] Session log filled (≤1 000 words, or extracted)
- [ ] Finished items moved backlog → log; new open items in backlog
- [ ] Scratchpad reconciled (carry-forward ≤15 lines)
- [ ] Memory updated (strengthen on recall; new gotchas → operational; operator observations → OPERATOR.md, never the tree)
- [ ] Decay sweep checked if operational over threshold
- [ ] Specs verified accurate
- [ ] CHANGELOG updated (if user-visible changes)
- [ ] Committed + pushed if enabled; tree clean
