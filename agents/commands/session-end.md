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
   Fill the scaffold from session start: done, found, decided, open. Line 1 is the greppable index entry: `filename | keywords`. If work is unfinished, add a "State at close" section. Extract durable findings (specs, operational memory, research) and leave a pointer rather than burying them here.
   *Flag if:* something important was left unfinished, or a finding emerged the next session must act on.

4. **Work ledger** — `agents/notes/work-backlog.md` + `agents/notes/work-log.md`
   - Finished items: **move** the line from `work-backlog.md` to `work-log.md` (append-only) with `[DONE]` and today's date — no `[DONE]` left in the backlog.
   - New open items: add to `work-backlog.md` as `[OPEN]`/`[ACTIVE]`/`[FIND]`.
   *Flag if:* a new `[FIND]` was filed, or an item is now blocking.

5. **Memory** — `agents/memory/procedural.md` / `agents/memory/operational.md`
   - *Strengthen on recall:* used an entry and it helped → patch its tag (today's date, counter +1: `[YYYY-MM-DD xN]`).
   - *New gotchas:* add to `operational.md` only — recurring, non-obvious from the error, not reachable by nearby docs. Start at `x1`, today's date.
   - *Operator observations:* record in `~/projects/OPERATOR.md` — NEVER in the project tree.
   *Flag if:* a new gotcha changes how future sessions should work.

6. **Scratchpad** — `agents/notes/scratchpad.md`
   Carry-forward: drop what is resolved or captured elsewhere, add what the next session must know, keep it tight. Move matured threads to the backlog or a plan.
   *Flag if:* the carry-forward holds something the next session must not miss.

7. **Commit and push** — always.
   Stage only files you worked on (`git add <explicit paths>`), commit with a Conventional Commit message, push if enabled. Verify `git status` — tree must be clean.

8. **Report** — always.
   One sentence each: accomplished, open, what the next session should open first.
