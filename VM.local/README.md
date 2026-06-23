# ~/projects/ — the workspace

This is the root of every project on this machine. It is **not** a git repository itself — the files here are maintained by hand and backed up by your own means. One agent works with you across all the projects below.

This README explains how the machine is wired *before* any single project is opened: what lives at this level, and the two-step bootstrap the agent runs at the start of every session. The per-project details live inside each project (and in `template-project/`, the canonical pattern every new project is copied from).

## These files are specific to this machine

Everything at this level — `AGENTS.md`, `LOCAL.md`, both scripts — is tuned to *this* VM and *this* operator. Paths, the backup preference, the SSH-key convention, the operator profile: all of it describes one machine. Copying these files verbatim onto another computer will not simply work — the paths and assumptions won't match. That is the reason they live here and not in any git repository: there is no shared, fetchable copy to read, because there is nothing here that is meant to be shared. A different machine gets its own versions. (`LOCAL.md` is also PII and must never be committed for that reason as well.) The *portable* part of the system — how the agent works in general — lives in `template-project/` and is documented there as a spec.

## What lives here

| Item | What it is | Committed / cloned? |
|------|-----------|---------------------|
| `AGENTS.md` | The one canonical instruction file — how the agent works. Edited by hand; the single source of truth. Synced into each opted-in project so a cloner of that project gets a working agent. | The canonical file is not in a repo; the synced per-project copies are committed |
| `LOCAL.md` | Who the operator is + facts about this VM (backup preference, setup habits, SSH-key convention). Personal observation about a named human — PII. | **Never** committed, **never** cloned |
| `agents_sync.sh` | Visible script that copies `AGENTS.md` into every project bearing a `.agents_sync` marker, read-only. VM-local. | Not committed into any project |
| `recent_sessions.sh` | Visible script that prints the newest session line from each project, for cross-project orientation. VM-local. | Not committed into any project |
| `<project>/` | One folder per project. Folders with a `.agents_sync` marker are template-derived and get synced; foreign clones without it are left untouched. | each is its own repo |
| `template-project/` | The canonical scaffold. `cp -r` it to start a new project; the copy opts into sync automatically. | its own repo |

The project list is **derived from the folders here** — never stored in a file. Adding a project means adding a folder.

## The startup bootstrap (two calls)

The agent cannot be told how to load its own instructions *inside* those instructions — by the time it reads them, the call already happened. So the bootstrap is described here and in `AGENTS.md`, in two steps:

**Exec-1 — VM level (before a project is chosen).** One call syncs the instruction file into marked projects, reads the canonical `AGENTS.md` and `LOCAL.md`, lists the project folders, and prints the most recent session lines for orientation:

```bash
bash ~/projects/agents_sync.sh \
  && cat ~/projects/AGENTS.md ~/projects/LOCAL.md \
  && echo "=== PROJECTS ===" && ls -d ~/projects/*/ 2>/dev/null | xargs -n1 basename \
  && echo "=== RECENT ===" && bash ~/projects/recent_sessions.sh
```

`agents_sync.sh` enumerates the folders itself, so it needs nothing from `AGENTS.md` first — which is why it can run as the very first thing. If `LOCAL.md` is absent (fresh clone, new VM), the agent prompts you to create one before going further.

**Project selection.** From what exec-1 returned: exactly one project → pick it; more than one and the prompt makes it >50% clear → pick it; still unclear → if the three recent-session lines all point to one project, pick it, otherwise stop and ask. No projects, or a request to start fresh → run `CREATE_PROJECT.md` and stop.

**Exec-2 — project level (after a project is chosen).** The agent reads the chosen project's guaranteed startup set in one call. **The exact exec-2 command lives in `AGENTS.md`**, because it is identical for every project and belongs with the instructions, not here. It loads the project's override, the procedural memory, the session-start procedure, the roadmap abstract, and the work backlog. After that, the steps in `<project>/agents/commands/session-start.md` run.

The per-project override (`AGENTS.override.md`) carries the project's persona, the agent's name, the `autonomy` level, and the `push` toggle, plus any project-specific instruction differences; on conflict it wins over the canonical `AGENTS.md`.

## Where to read more

- **`AGENTS.md`** — the canonical agent instructions, including the exec-2 command.
- **`LOCAL.md`** — you and this machine.
- **`template-project/`** — the scaffold; its `agents/*/README.md` files explain the memory, notes, and command machinery every project carries.
- **The system specification** in `template-project/docs/specs/` — how the whole agent/memory/session system works and why it is built this way. Read the spec, not the plans; plans are short-lived task records, the spec is the durable definition.
