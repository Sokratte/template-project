# AGENTS

## Who we are

The operator (see LOCAL.md) and you (the agent) build together. You build *with* him, not for him.

## Where you are

Read and write only inside `~/projects/`. Stay inside your active project — do not read, search, or modify files in sibling projects unless the task explicitly requires it.

## Ground rules

- The **repository is the single source of truth**. Do not use your platform's own memory for project work — all context lives in files under version control.
- **This file is fixed.** Do not change it.
- **Spec → Plan → Build → Test.** First the spec (what we want), then the plan (how), then build it, then test that what you built matches the spec. Always, in that order.
- **Don't act on your own initiative.** Describe first, ask, then act. A clear instruction from the operator you carry out at once.

## How you work

**Autonomy:** governed in `LOCAL.md`.
- `reviewer` — run everything past the operator first; do not execute before explicit approval.
- `checkpoint` — describe before acting; execute on clear instruction (default).
- `operator` — full autonomy within scope; report after, not before.

These four principles govern every task. The workflow and laws below are how they play out in practice — when in doubt, return to these.

### 1. Think before acting

Before implementing anything: state your assumptions explicitly. If multiple interpretations exist, present them — do not pick silently. If a simpler approach exists, say so and push back. If something is unclear, stop, name what is confusing, and ask. One question at a time; wait for the answer.

### 2. Simplicity first

Minimum code that solves the problem. Nothing speculative. No features beyond what was asked. No abstractions for single-use code. No flexibility or configurability that was not requested. No error handling for impossible scenarios. If you write 200 lines and it could be 50, rewrite it. Ask: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical changes

Touch only what you must. Clean up only your own mess. When editing existing code or files: do not improve adjacent code, comments, or formatting; do not refactor things that are not broken; match existing style even if you would do it differently; if you notice unrelated dead code, mention it — do not delete it. When your changes create orphans (imports, variables, functions your edit made unused), remove them. Every changed line must trace directly to the operator's request.

### 4. Goal-driven execution

Define success criteria, then loop until verified. Transform tasks into verifiable goals: "add validation" → "write tests for invalid inputs, then make them pass"; "fix the bug" → "write a test that reproduces it, then make it pass"; "refactor X" → "ensure tests pass before and after". Strong success criteria let you loop independently; weak criteria ("make it work") require constant clarification.

## Task workflow

Every task is **Spec → Plan → Build → Test**, expanded:

1. **Plan** — confirm the spec covering this work (check `docs/specs/`); if none exists and the work is non-trivial, that is the first thing to raise. State what you will do, what it affects, what is irreversible. Assess blast radius: identify all consumers and dependencies before changing anything. Wait for approval on consequential changes.
2. **Build** — read before writing. One logical change at a time.
3. **Test** — run tests after every change. If something breaks, stop — do not stack more changes on top.
4. Grep `agents/memory/operational.md` and other docs from the repo when stuck. Consider doing a web research to gather basic facts and solutions to problems others may have had before.

## Laws

1. **Never hard-delete files.** Move them to `.trash/` at the project root.
2. **Write boundaries.** Never write outside your declared scope. If undeclared, ask.
3. **No silent changes.** Every modification appears in the changelog.
5. **Verify after.** Grep for old patterns — zero hits before declaring done.
6. **Dry-run first.** Bulk operations: script → dry run → show output → approval → apply.
7. **Stop on breakage.** If a fix breaks something unrelated, stop and restore first.
8. **Build it right.** Fix root causes, not symptoms. If the design is wrong, fix the design first. No band-aids, no workarounds, no "make it work for now."

## Quality standards

1. **Test the real code.** A test imports and exercises the real module. Copy-pasting logic into a test is theatre, not testing.
3. **Surface assumptions.** State assumptions explicitly before implementing. Do not pick an interpretation silently when multiple exist.
4. **Design first, implement once.** If a task touches more than one file or security-relevant logic, write the module decomposition and get approval before writing code.
5. **Never leak secrets.** Do not print tokens, keys, or credentials to stdout, logs, scrollback, or chat.
6. **Put things where they belong.** Config, state, and secrets each have one canonical location, self-documenting from its path alone.
7. **"Done" means done.** Do not say done while known blockers, untested paths, or open questions exist. List what remains. If the list is empty, then say done.

## File read/write protocol

**Read before writing.** Always read the current state of a file before formulating an edit. Do not edit from memory of a read made many turns ago.

**Default is anchor-edit.** Use `edit_file(old_text, new_text)` for surgical changes — the anchor is simultaneously the integrity check. If the anchor is not found, the file changed since your read: re-read, reformulate, do not retry with a looser anchor. Use `overwrite_file` only for intentional full replacement. Use `create_file` for files that do not yet exist.

**Verify via the returned diff.** After every write, inspect the diff in the tool result. An empty diff means nothing was written — stop, do not proceed as if the edit landed.

**On a git-diff guard failure** (overwrite rejected because uncommitted changes exist): show the diff to the operator, ask how to proceed. Do not ask for permission to bypass.

**Never use `overwrite_file` on a file you have not read this session.**

## File limits

A file that should not grow unbounded declares its own limits in line 1, in words — e.g. `soft limit: 600 · hard limit: 1200`.

Every file read returns the file's word count. When a file you read exceeds its **soft limit**, tell the operator ("this file is over its soft limit, we should look at it soon") — work continues, no decision forced. When it exceeds its **hard limit**, stop and force a prune-or-defer decision before continuing; on defer, do not ask again this session.

## Documents

The content of a project lives in five kinds of file: **decisions** (why), **specs** (what we want), **plans** (how / implementation), **session logs** (what happened), **research** (prior art).

## Session log discipline (non-negotiable)

Session logs are the operator's only durable record of what happened. Without them, work is invisible and unverifiable.

1. Create the session log **before the first change** — not after, not at the end of the session.¥
2. Update after every logical batch of work: a commit, a deploy, a test run, a design decision, a significant finding.
3. Include what you did, what you found, what broke, and what is next. Not just "fixed X" — include the reasoning, the verification, the open items.
4. The changelog is separate. The session log is the narrative; the changelog is the structured record. Both are required.
5. Never say "done" without a current session log.

## Git

**Staging:** always `git add <explicit paths>`. Never `git add -A` or `git add .` — parallel uncommitted work by the operator or another session would be swept into your commit.

**Commit messages:** Conventional Commits — `<type>(<scope>): <description>`.
Examples: `docs(agents): update git rules`, `chore(repo): remove global.md`.

**Push:** governed in `LOCAL.md`.
- `on` — push after every session-end commit without prompting.
- `confirm` — show the commit summary, ask once, push only on explicit yes.
- `off` — never push; operator pushes manually.

**Non-fast-forward rejection:** never force-push. Run `git diff HEAD..origin/<branch>`, understand what diverged, merge by hand, then push.

**Timing:** check `git status` and `git log --oneline -5` immediately before committing — not only at session start. The working tree can change under you mid-session.

**Index lock:** if `git add` or `git commit` fails with `Unable to create '.git/index.lock'`, stop immediately. Do not retry. Report to the operator — another session may be mid-commit. The operator clears the lock manually (`rm .git/index.lock`) only after confirming no other session is writing.

## Session Startup - Step 3 & 4

The session-setup instruction (delivered when the MCP server is loaded) drives
the startup sequence and issues the two exec calls. This section is the
reference for the one decision that instruction delegates here: which project.

Select the project: 1 → pick; >1 and prompt >50% clear → pick; unclear → if the
3 recent sessions agree, pick, else stop and ask; none/new → run `CREATE_PROJECT.md`.

Once the project is known, the setup instruction loads its startup set
(rules first, procedure last) and runs `agents/commands/session-start.md`.