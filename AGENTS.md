<!-- ================================================================
     SETUP GUIDE — FOR THE AGENT CREATING A NEW PROJECT
     ================================================================
     Read this top-to-bottom. Follow every step. When done, delete
     everything from the top of the file down to "--- END OF SETUP ---".
     What remains is the project's permanent AGENTS.md.

     Do NOT work inside ~/workspace/template-project/.
     That folder is the template. You are working in the copy.
     ================================================================ -->

# New Project Setup Guide

You are setting up a new project from the workspace template. This guide
walks you through it as a conversation with the user — not a checklist you
rush through silently. Take your time. The decisions made now shape every
session that follows.

---

## Step 0 — Verify location

Confirm you are NOT inside `~/workspace/template-project/`. Run `pwd` and
check. If you are in the template folder, stop — copy it first:
```
cp -r ~/workspace/template-project ~/workspace/projects/<n>
```
Then `cd` into the copy and continue.

---

## Step 1 — Understand what the user wants to build

Before touching any file, have a short conversation. Ask the user:

1. **What** are you building? (one sentence)
2. **Who** is it for? (yourself, a team, the public?)
3. **What kind** of project is it? (app, library, server, content, hardware?)
4. **Where** does it run? (local only, server, cloud, embedded?)
5. **What should it explicitly NOT be?** (scope boundaries, anti-goals)

Listen to the answers. You will use them to fill in the project description,
select optional sections, and calibrate your domain research. Do not proceed
until you have clear answers to at least questions 1, 3, and 5.

---

## Step 2 — Create the GitHub repository

You cannot create the repo yourself — it requires the user's credentials.
Guide them through it:

> I need you to create a GitHub repository for this project. You can do this
> at github.com/new or by running `gh repo create` from the terminal.
> Once created, tell me the remote URL.

Once you have the URL:
```
git init
git remote add origin <URL>
```

Do NOT commit yet — we need to fill in files first.

---

## Step 3 — Fill in the permanent sections

Scroll down to "--- END OF SETUP ---". Below it is the permanent AGENTS.md.
Fill in every `TODO:` field using the answers from Step 1:

- Project name and description (2 sentences max)
- What this project is NOT (from question 5)
- Any project-specific git exceptions
- Remove the `TODO:` markers when done

---

## Step 4 — Create ADR-001: Project Definition

Open `docs/decisions/ADR-000-template.md`, copy it to `ADR-001-project-definition.md`.
Fill it in. This is the project's founding document:

- **Context:** Why does this project exist? What triggered it?
- **Decision:** What are we building, with what stack, for what audience?
- **Consequences:** What does this commit us to? What does it rule out?

The user must review and approve this before you continue.

---

## Step 5 — Select optional sections

Read the "OPTIONAL SECTIONS" block at the bottom of the permanent AGENTS.md.
For each section, decide whether it applies based on what you learned in
Step 1. Have a brief conversation — group obvious ones:

> "This is a Python server project, so I'll include Environment, Testing,
> Error Handling, and Services. I'll skip Before Writing Code since you're
> using TypeScript with static types. Sound right?"

Uncomment the sections you keep. Delete the ones you don't. Delete the
menu header and instructions too — they are setup scaffolding.

---

## Step 6 — Domain research (mandatory — do not skip)

This is the most valuable thing you do at project start. Search the web.
Your goal: become an expert on this kind of project as of today.

Research:
- What tools, frameworks, and libraries are industry-standard right now?
- What do experienced practitioners consider the most common pitfalls?
- Are there open-source projects or templates worth studying?
- What standards, protocols, or specs apply?
- What non-obvious decisions will the user face soon?

Write the results to `docs/research/YYYY-MM-DD-initial-domain-research.md`.
This file is for future agents — it prevents re-researching the same ground
every session. Include sources and dates so future agents know when to
refresh.

Then brief the user:
- What the standard approach looks like
- 2–3 things worth doing from the start that save pain later
- Trade-offs in any non-obvious choices ahead

---

## Step 7 — Tool-specific setup

**If the user works with Claude Code:** Create a symlink so Claude Code
finds the instructions:
```
ln -s AGENTS.md CLAUDE.md
```
The `.claude/commands/` directory already contains `session-start.md`,
`wrap-up.md`, and `daily-digest.md`. Review them and adjust paths to
match this project — especially the vault path in `daily-digest.md`
(`~/workspace/vault/Projects/TODO.md`). Verify the commands work.

**If the user works with Codex:** Codex reads AGENTS.md only. The session
start checklist in the permanent section already covers the reading order.
Delete the `.claude/` directory — it will not be used. The daily digest
can still be run manually: ask the agent to read the project state and
write a summary to `~/workspace/vault/Projects/<project-name>.md`.

**If the user works with claude.ai or other agents:** Same as Codex — the
AGENTS.md is self-sufficient. Delete `.claude/` if it will never be used.
The daily digest can be triggered by asking the agent directly.

---

## Step 8 — First commit and first Milestone

```
git add -A
git commit -m "chore: initial project scaffold from template"
git push -u origin main
```

Then guide the user to create the first GitHub Milestone:

> "What should the first milestone be? This is the first meaningful version
> goal — something like 'v0.1.0 — basic working prototype' or
> 'v0.1.0 — initial data pipeline'. I'll help you break it into Issues."

Finally, delete everything from the top of this file down to and including
the line below. The project is ready.

--- END OF SETUP ---


# TODO: Project Name — Agent Instructions

TODO: What this project does and for whom. (one sentence)
TODO: What kind of project it is and where it runs. (one sentence)

**This project is NOT:**
- TODO: anti-goal or scope boundary
- TODO: another one

Global rules: `~/workspace/AGENTS.md` — read before every session.
Only project-specific additions and exceptions appear below.


## Session Start Checklist

Every session, every agent, every time. Read in this order:

1. `~/workspace/AGENTS.md` — global rules (if not already loaded)
2. This file — project-specific context
3. `git status` and `git log --oneline -10` — what changed recently
4. `changelog/session-logs/` — find the latest session log, read it
5. `docs/plans/` — any active task plans still in progress
6. `docs/research/` — skim the latest entry to refresh domain context
7. GitHub Issues (current Milestone) — what is in progress

If any of these are missing or stale, say so before starting work.
If AGENTS.md has not been reviewed in 90+ days, flag it.


## Where Things Live

| Question | Location |
|----------|----------|
| What's been completed | `CHANGELOG.md` and `changelog/session-logs/` |
| What's in progress now | GitHub Issues — open, current Milestone |
| What's planned next | GitHub Milestones |
| Architecture decisions | `docs/decisions/` (ADRs — immutable) |
| Feature specs | `docs/specs/` |
| Domain research | `docs/research/` (AI-maintained, dated) |
| Task plans (short-lived) | `docs/plans/` (delete when task is done) |
| Operations guides | `docs/runbooks/` |
| Claude Code commands | `.claude/commands/` (if using Claude Code) |
| Human overview (Obsidian) | `~/workspace/vault/Projects/TODO.md` (generated) |


## Git and GitHub

One canonical repo. Check `.git/config` for the remote URL.
All git discipline rules live in `~/workspace/AGENTS.md` — not repeated here.

**Claude Code users:** If `CLAUDE.md` does not exist in the project root,
create it as a symlink: `ln -s AGENTS.md CLAUDE.md`. Claude Code reads
`CLAUDE.md` as its primary instruction file.

Project-specific exceptions: TODO (delete this line if none)


## Tribal Knowledge

Things every agent must know that aren't documented anywhere else.
Each entry: date, category tag, the knowledge, and why it matters.

<!-- Example:
- [2026-04-17] [deploy] Never run `deploy.sh` without first checking
  that the control directory ownership hasn't been overwritten by step 9b.
  Root cause: `install -d` resets ownership on every run.
-->

- TODO: first entry goes here


<!--
====================================================================
OPTIONAL SECTIONS — Setup agent: uncomment what applies, delete the rest.
After setup, delete this instruction block too.

Each section says when to include it. Read the condition, decide, act.
====================================================================

INCLUDE IF: code lives in more than one place, or runs on a server.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Environment

| Location | Path | Access |
|----------|------|--------|
| Mac (dev) | `~/workspace/projects/TODO/` | python-container, editors |
| Server    | `/srv/TODO/`                 | SSH, MCP                 |

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INCLUDE IF: any code that can be tested automatically.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Testing

```
TODO: the exact command to run tests (e.g. pytest, npm test, go test ./...)
```

"Green" means: all tests pass, no silent skips, no unhandled warnings.
A skipped test must have a comment explaining why.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INCLUDE IF: project structure is non-obvious or has more than ~5 directories.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Project Structure

```
TODO: annotated directory tree
```

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INCLUDE IF: multiple agents/contributors, or non-obvious style choices.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Conventions

- Language: TODO (e.g. "English for code and docs, German OK in discussions")
- TODO: naming, formatting, or style rules worth making explicit

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INCLUDE IF: certain directories or services must not be touched without care.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Write Boundaries

| May edit freely | Requires caution | Never touch |
|-----------------|------------------|-------------|
| TODO            | TODO             | TODO        |

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INCLUDE IF: code project where wrong names/types cause real bugs
(Python without static types, dynamic APIs, complex class hierarchies).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Before Writing Code

- Read the file you are about to edit. Verify function and attribute names
  against the actual source — never assume from memory or convention.
- Check return types of functions you call.
- Run `python3 -m py_compile` (or equivalent) before committing.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INCLUDE IF: Python with threading, OS callbacks, or hardware I/O.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Error Handling

Three zones require try/except without exception:

1. **OS callbacks** — exceptions are silently swallowed; the callback
   stops firing. (CGEventTap, audio, signals, filesystem watchers)
2. **Thread entry points** — uncaught exceptions kill the thread silently.
   (every `threading.Thread(target=...)` function)
3. **System boundary calls** — hardware I/O, ML inference, external
   processes, cross-framework calls. Wrap the boundary, not every line.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
INCLUDE IF: deployed services that other things depend on.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## Services and Live Operations

| Service | Port | Path | Source |
|---------|------|------|--------|
| TODO    | TODO | TODO | TODO   |

Before touching live infrastructure: read the relevant runbook in
`docs/runbooks/`. After any change, run health checks for every service.

====================================================================
-->
