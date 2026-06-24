# Session End

Closing procedure. Do all of it before you say "done." No step is optional, none deferred to "next session." **Execute these steps — do not merely read them.**

Report one line per step, mark first so the lines stack: ✅ checked and clean, ❌ needs attention. Each step names what is worth a ❌; routine mechanics (a file was updated) never count beyond the ✅.

1. **Specs** — `docs/specs/`
   If any spec changed or was created this session, verify it reflects what was actually built or decided.
   *Flag if:* a spec now contradicts a plan, ADR, or the code.

2. **CHANGELOG.md**
   Add entries under `[Unreleased]` for any user-visible change: Added, Changed, Fixed, Removed, Deprecated, Security.
   *Flag if:* a user-visible change has no home in any category.

3. **Session log** — `docs/sessions/YYYY-MM-DD-<topic>.md`
   Fill the scaffold from session start: done, found, decided, open. Line 1 is the greppable index entry: `<!-- keywords: … -->`, with the bare filename on line 2. If work is unfinished, add a "State at close" section. Extract durable findings (specs, operational memory, research) and leave a pointer rather than burying them here.
   *Flag if:* something important was left unfinished, or a finding emerged the next session must act on.

4. **Work ledger** — `agents/notes/work-backlog.md` + `agents/notes/work-log.md`
   - Finished items: **move** the line from `work-backlog.md` to `work-log.md` (append-only) with `[DONE]` and today's date — no `[DONE]` left in the backlog.
   - New open items: add to `work-backlog.md` as `[OPEN]`/`[ACTIVE]`/`[FIND]`.
   *Flag if:* a new `[FIND]` was filed, or an item is now blocking.

5. **Memory maintenance** — `agents/memory/{procedural,operational}.md`
   Autonomous: do it, do not prompt the operator, report what moved in step 8. Full model: `agents/memory/README.md`.
   - *Strengthen on recall:* an entry you used this session earned its keep → bump its tag (`[sNN xM]` → `M+1`). One edit.
   - *New gotchas → `operational.md`:* recurring, non-obvious from the error, not reachable by nearby docs. Born `[s<current> x1]`, filed under the right keyworded section (extend the section keywords if the entry adds a new term).
   - *Promote `operational` → `procedural`:* an operational entry that is **topic-independent** (applies every session, any subject), **proven** (`M ≥ 3`), and **currently useful** (value ≥ cutoff) → move the whole line to `procedural.md`, tag unchanged. The "currently useful" test stops a just-demoted rule from bouncing straight back.
   - *Prune `procedural` (size-triggered only, two stages):* for each entry compute `value = M / (current_session − NN + 1)`. Cutoff = `memory_cutoff` from `AGENTS.override.md` (default 0.01).
     - Over **soft** limit → demote only entries with `value < cutoff`; spare everything at or above cutoff even if still over soft.
     - Over **hard** limit → demote all `value < cutoff`, then keep demoting the lowest-valued survivors (whole tie-groups, all-or-none, lowest first) until back under hard. Stop as soon as you are under.
     - *Demote* = move the line into `operational.md` under its topical section (extend that section's keywords). Never delete. `operational.md` has no size limit, so a demotion always lands.
   - *Operator observations:* record in `~/projects/LOCAL.md` — NEVER in the project tree.
   *Flag if:* anything was promoted or demoted (name it), or a new gotcha changes how future sessions should work.

6. **Scratchpad** — `agents/notes/scratchpad.md`
   Carry-forward: drop what is resolved or captured elsewhere, add what the next session must know, keep it tight. Move matured threads to the backlog or a plan.
   *Flag if:* the carry-forward holds something the next session must not miss.

7. **Doc consistency** — run `python3 -m pytest tests/test_docs.py` (registered in `docs/tests/TEST-001`).
   Green → proceed. Red → fix the offending file before committing, or, if the failure is out of this session's scope, record it as a `[FIND]` in the backlog and note the defer in the report. Never commit over a red suite silently.
   *Flag if:* the suite was red for any reason.

8. **Commit and push** — always.
   Stage only files you worked on (`git add <explicit paths>`), commit with a Conventional Commit message, push if enabled. Verify `git status` — tree must be clean.

9. **Report** — always.
   One sentence each: accomplished, open, what the next session should open first.
