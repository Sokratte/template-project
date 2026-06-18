# Global Rules

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## Environment

- macOS, Apple Silicon. `~/projects/` is the root of all local projects.
- This file sets workspace-wide defaults. Each project has its own `AGENTS.override.md` that overrides these defaults when stricter or more specific.

## Workflow

Every task follows this sequence. No skipping steps.

1. **Orient** — Read global AGENTS.md, then project AGENTS.md. Check for an existing session log. Check `docs/specs/` for a spec covering the work at hand.
2. **Plan** — State what you'll do, what it affects, what's irreversible. Assess blast radius — identify all consumers and dependencies before changing anything. For multi-step tasks, state a brief plan:
   ```
   1. [Step] → verify: [check]
   2. [Step] → verify: [check]
   ```
   Define success criteria before starting: "Add validation" → "Write tests for invalid inputs, then make them pass." Weak criteria ("make it work") require constant clarification. Wait for approval on consequential changes.
3. **Prepare** — Create/update session log. Write changelog entry (intent). Baseline git commit if tree is clean.
4. **Implement** — Read before writing. Verify names against actual code. One logical change at a time.
5. **Test** — Run tests after every change. If something breaks, stop — don't stack more changes.
6. **Wrap up** — Follow the project's `agents/commands/session-end.md`.

## Session Log Discipline (NON-NEGOTIABLE)

Session logs are the operator's only record of what happened. Without them, work is invisible and unverifiable.

1. **Create the session log BEFORE the first code change.** Not after. Not at the end. Before. File naming: `docs/sessions/YYYY-MM-DD-<topic>.md`.
2. **Update after every logical batch of work.** A batch is: a commit, a deploy, a test run, a design decision, or a significant finding. Three commits without a session log update is three violations.
3. **Include what you did, what you found, what broke, and what's next.** Not just "fixed X" — include the reasoning, the verification, the open items.
4. **The changelog is separate.** The session log is the narrative. The changelog is the structured record. Both are required.
5. **Never say "done" without a current session log.**

When debugging: don't blame the environment. Add logging for analysis. Git bisect to isolate. `git checkout` over manual revert.

## Simplicity First

Minimum code that solves the problem. Nothing speculative.

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

If multiple interpretations of a request exist, present them — don't pick silently. If a simpler approach exists, say so and push back. If something is unclear, stop. Name what's confusing. Ask.

## Laws

1. **Read before write.** Never edit without reading current state first.
2. **Write boundaries.** Never write outside your declared scope. If undeclared, ask.
3. **No silent changes.** Every modification appears in the changelog.
4. **Surgical edits only.** Touch only what you must. Don't improve adjacent code, comments, or formatting. Don't refactor things that aren't broken. Match existing style even if you'd do it differently. If you notice unrelated dead code, mention it — don't delete it. *But:* when your changes create orphans, clean them up — remove imports, variables, or functions that YOUR changes made unused. Every changed line should trace directly to the request.
5. **Verify after.** Grep for old patterns — zero hits before declaring done.
6. **DRY_RUN first.** Bulk operations: script → dry run → show output → approval → apply.
7. **Stop on breakage.** If a fix breaks something unrelated, stop and restore first.
8. **Build it right.** Fix root causes, not symptoms. Follow the architecture docs. If the design is wrong, fix the design first, then implement. No band-aids, no workarounds, no "make it work for now."

## Quality Standards

These exist because every one of them was violated and caused real damage.

1. **Test the real code.** If you write a test, it imports and exercises the real module. Copy-pasting logic into a test file is not testing — it is theatre. If a dependency makes direct import hard, fix the dependency (extract a module, use a seam), don't copy the code.
2. **Verify before claiming.** "This API doesn't exist" requires proof: a failing import, a missing method, a documentation link. If you haven't checked, say "I'm not sure" — do not assert. This applies to language features, library APIs, OS capabilities, and system behavior.
3. **Surface assumptions.** State your assumptions explicitly before implementing. If uncertain, ask. Don't pick an interpretation silently when multiple exist — present them.
4. **Design first, implement once.** If a task needs more than one file or touches security-relevant logic, write the module decomposition before writing code. Get approval. Then implement. Incremental band-aid rounds where each review finds the same class of bug means the design was skipped.
5. **Never leak secrets.** Do not print tokens, keys, or credentials to stdout, logs, scrollback, or chat. Tell the operator where to read them.
6. **Put things where they belong.** Config, state, and secrets each have one canonical location that is self-documenting from its path alone.
7. **"Done" means done.** Do not say "ready to deploy," "code complete," or "all tests pass" while known blockers, untested paths, or open questions exist. List what remains. If the list is empty and you are sure, then say done.

## These guidelines are working if

- Fewer unnecessary changes appear in diffs.
- Fewer rewrites due to overcomplication.
- Clarifying questions come before implementation rather than after mistakes.
- "Done" is said once and means it.

## Knowledge Base (tbd.)

Mkdocs at `<user>.domain.tld/projects/<name>/`. Tell the user to go there if he wants to read project-files.
