# PLAN-001: Multi-VM Agent Architecture

**Created:** 2026-06-17 · **Last updated:** 2026-06-17
**Topic:** Global AGENTS.md + per-project override + config + backup + a
visible sync script, for a reusable scaffold deployed identically across
multiple users' VMs.

**Summary (read this first):**
One agent works with one (often non-technical) human across all their
projects on one machine. Instructions are authored in ONE canonical
`~/projects/AGENTS.md`; a visible `agents_sync.sh` copies it into every
project that opts in via a `.agents_sync` marker, so each project repo
carries a working copy for anyone who clones it — while the canonical file
stays the only thing edited by hand. Projects differ only via a small
optional override. Backup is set once per VM, configured per project. The
project list is derived from the folder structure, never stored. This plan
is the spec the build follows.

---

## Goal

Define where the agent's *instructions*, *config*, *backup behavior*, and
*sync mechanism* live so that: (a) the default user touches nothing, (b) an
improvement is applied everywhere by editing one file, (c) instruction files
cannot silently drift apart across projects, and (d) anyone cloning a single
project repo gets a working, fully-instructed agent.

## Non-goals

- NOT: a per-project forked copy of the full instructions
- NOT: agent-created remote repos (no API tokens — see Decision 3)
- NOT: opinionated about backup provider — any git-protocol remote works
- NOT: a sync that touches foreign repos living under `~/projects/`

---

## The two-axis model

- **Instructions** = *how* the agent works. Stable. Shared. → canonical
  `~/projects/AGENTS.md`, copied into each opted-in project.
- **Project context** = memory, decisions, specs, roadmap. Per-project. →
  each project's own folders (unchanged from current template).

Per-project *instruction* differences are rare, so they live in a small
optional override, not a forked file.

> Standards note: `AGENTS.md` is the cross-tool convention (Linux
> Foundation / Agentic AI Foundation; read by Codex, Cursor, Copilot,
> Gemini CLI, Aider, Zed). `AGENTS.override.md` is the spec's own override
> filename, and "global → project override wins" is how these tools already
> merge instructions. We are aligned with the standard, not inventing.

---

## Layout

```
~/projects/
├── AGENTS.md              # canonical instructions — authored by hand, the ONE source of truth
├── agents_sync.sh         # visible sync script (see "Sync mechanism"); VM-local, not committed to any project
├── .projects              # global config FILE (VM backup prefs); set once at VM build
│
├── whisperdog/
│   ├── .agents_sync       # marker: "sync AGENTS.md into me"  ← opt-in, created by `cp -r` of the template
│   ├── AGENTS.md          # generated copy — committed (portability), never hand-edited
│   ├── AGENTS.override.md # authored per project, committed; override wins on conflict
│   ├── .project           # per-project config FILE; gitignored (references key paths)
│   └── agents/            # machinery: memory/, commands/, notes/, rules/
│
├── tradingbot/
│   └── … (same shape)
│
└── some-foreign-repo/     # NO .agents_sync marker → sync skips it; its own AGENTS.md untouched

~/.ssh/
├── <project>_deploy       # private deploy key — NEVER in any project tree
└── <project>_deploy.pub   # public key — operator registers this on the provider
```

`.projects` (plural) = global config file. `.project` (singular) = per-project
config file. Both are plain `key: value` files, not folders.

---

## File inventory

### 1. Canonical instructions — `~/projects/AGENTS.md`
- The ONE file edited by hand. Single source of truth for agent behavior.
- Lives in the `~/projects/` workspace repo (so it is itself versioned/backed up).
- Contains: agent identity, session-start/end routine, universal rules, git
  behavior (keyed on config, not hardcoded), nav conventions, the
  override-loading rule, the backup behavior rules, autonomy-level definitions.
- **Does NOT contain the copy command.** The sync mechanism lives in
  `agents_sync.sh`, never in this content — so a cloner's agent reading a
  project's `AGENTS.md` never executes a destructive copy. (See "Why the
  sync command is not in AGENTS.md.")
- Keep lean: a monolithic always-loaded file wastes context. Target well
  under ~150–200 lines; push detail into the per-project machinery.

### 2. Generated per-project copy — `<project>/AGENTS.md`
- A **committed copy** of the canonical file, placed by `agents_sync.sh`.
- Treated as a **generated artifact, not source.** Header marks it:
  "Do not edit — synced from ~/projects/AGENTS.md. Project-specific rules go
  in AGENTS.override.md."
- Exists so a cloner of the single project repo gets working instructions.

### 3. Per-project override — `<project>/AGENTS.override.md`
- **Normally empty or absent.** Exists only when a project genuinely needs
  to differ from global rules. Authored by hand, committed.
- Rule (stated in the canonical file): "load me, then load the project
  override if one exists; on conflict, the override wins."
- Bounded: a small override, never a forked full file.

### 4. Global config — `~/projects/.projects`
- The one genuinely per-VM-variable file. Set ONCE by operator at VM build.
- Keeps the canonical `AGENTS.md` identical across VMs.
- Format: plain `key: value`.
- Holds the backup answer:
  - `backup: none` → fully automatic local-only git. Agent never says the
    words "git" or "GitHub." Local commits are an invisible undo net.
  - `backup: <provider1>, <provider2>, ...` → comma-separated list of
    backup destinations the user has. Enables the per-project remote flow.
- Not project-relevant → not copied into projects. Cloner never needs it.

### 5. Per-project config — `<project>/.project`
- Present when this project is backed up, OR to record the autonomy
  preference (autonomy applies even with `backup: none`).
- Format: plain `key: value`. Angle-bracket placeholders = "fill in per
  project." **Gitignored** (see Decision 7).

  ```
  # backup (only if global backup != none and this project is backed up)
  provider:   <provider>          # e.g. github   — matches a name in ~/projects/.projects
  remote_url: <url>               # e.g. git@github.com:<user>/<repo>.git
  repo_name:  <repo>              # human-readable; redundant with url, kept for clarity
  push:       <on|off>            # e.g. on
  key_path:   <path>              # e.g. ~/.ssh/<project>_deploy

  # autonomy (applies to every project, backup or not)
  autonomy:   <level>             # see "Agent autonomy"
  ```

- `key_path` is per-project because per-repo **deploy keys** are the default
  (Decision 4): a leaked key compromises one repo, not the account. An
  account-level key is supported by pointing several projects at one `key_path`.
- The key itself is NEVER here — only its path. Keys live in `~/.ssh/`.

### 6. Sync script — `~/projects/agents_sync.sh`
- **Visible** (not dot-prefixed), sits next to `AGENTS.md`.
- VM-local: lives only on the operator's VM, is **not committed** into any
  project repo, so a cloner's machine never has it and can never run the
  destructive copy.
- Behavior: for each directory in `~/projects/*/`, **if it contains a
  `.agents_sync` marker**, copy `~/projects/AGENTS.md` into it. Folders
  without the marker (foreign clones, reference repos) are skipped entirely.
- Self-enumerates the project list — does not depend on `AGENTS.md` having
  been read first, so it can run as the first thing in startup call 1.

### 7. Opt-in marker — `<project>/.agents_sync`
- Empty marker file. Its presence means "this project is template-derived,
  sync the canonical AGENTS.md into it."
- Created automatically by `cp -r template-project <new>`, so the operator's
  own projects opt in with zero thought. Foreign repos lack it → safe by default.

### 8. Per-project machinery — `<project>/agents/`  *(unchanged)*
- Existing template folder: `memory/`, `commands/`, `notes/`, `rules/`.
- The *machinery* (how work is tracked), distinct from the *instructions* in
  `AGENTS.md` / the override.
- Naming note: `AGENTS.md` (instructions, standard) vs `agents/` (machinery,
  our own folder). Folder keeps its plain name (no dot prefix).

### 9. SSH keys — `~/.ssh/<project>_deploy[.pub]`
- Private + public deploy key per repo. **Outside every project tree**,
  never committed, `600` perms. `.project` references the private key by path.

---

## Sync mechanism — the drift-proof + cloner-safe design

The problem: the canonical file must be edited once and apply everywhere
(drift-proof), AND a working copy must ride inside each project repo so a
cloner gets a usable agent (portability). Naively committing N copies
reintroduces drift; a symlink breaks on clone; an in-`AGENTS.md` copy command
makes a cloner's agent overwrite the cloner's own file every session.

The resolution, four parts:

1. **Canonical file** `~/projects/AGENTS.md` is the only hand-edited copy.
2. **`agents_sync.sh`** copies it into every project bearing `.agents_sync`.
   The in-project copy is a generated artifact, overwritten each run →
   cannot drift by accident on this VM.
3. **The copy command lives in the script, not in `AGENTS.md`.** Portable
   content carries no instruction to overwrite anything, so a cloner's agent
   never clobbers the cloner's file. (See below.)
4. **`.agents_sync` marker gates the sync** → foreign repos under `~/projects/`
   are never touched. Protects reference repos (tbh, maisig, tinkerbuddy, …).

### Why the sync command is not in AGENTS.md
If the copy instruction lived inside `AGENTS.md`, any agent reading a cloned
project's `AGENTS.md` would run it and overwrite the cloner's own file every
session — forcing repeated cleanup. Keeping the mechanism in a VM-local
script that foreign machines never receive removes the footgun entirely.

### Cloner cases
- **Operator's VM:** `agents_sync.sh` keeps every marked project's copy
  matching the canonical file.
- **Cloner with the full workspace:** their own `agents_sync.sh` + canonical
  file sync their version in. Fine.
- **Cloner of a single project repo, no workspace:** no script exists to run,
  so nothing overwrites anything. The committed in-repo `AGENTS.md` (file 2)
  stands as the working fallback. This is why the copy is committed.

---

## Agent autonomy (what the agent does on the user's behalf)

What the agent may do unprompted vs. what needs a check-in is **agreed
between agent and user** and recorded per project in `.project` as
`autonomy: <level>`. Proposed levels (refine when drafting AGENTS.md):

- `autonomous` — commits, pushes, edits, proceeds without asking; reports
  after. Trusting users / low-stakes projects.
- `checkpoint` — acts freely on routine work but pauses for explicit approval
  before consequential or irreversible actions (deleting files, schema
  changes, anything force-relevant in git).
- `confirm` — proposes before nearly every action; user approves each step.
  Cautious users / high-stakes projects.

Default for a new project: `<default>` — **decide when drafting** (lean
`checkpoint`, ~70%: safe for non-technical users without being paralyzing).
The canonical `AGENTS.md` defines what each level *means*; the per-project
value selects one. On first session in a project with no `autonomy` set, the
agent asks once and writes the answer.

---

## Startup sequence

1. **Tool search** → returns tools + "before anything, run startup."
2. **Exec call 1 — sync, then read global, then list projects** (one call;
   the script self-enumerates folders, so it does not need the project list
   from `AGENTS.md` first):
   ```
   bash ~/projects/agents_sync.sh \
     && cat ~/projects/AGENTS.md \
     && echo "\nProjects:" \
     && ls -d ~/projects/*/ 2>/dev/null | xargs -n1 basename
   ```
   Project list is **derived from folders, never stored.** `ls -d ~/projects/*/`
   lists directories and the `*` glob already excludes dot-prefixed entries.
   Adding a project = `cp -r template-project <name>` (carries `.agents_sync`);
   the folder appearing IS the registration.
3. Agent selects the project: 1 → pick; >1 and clear from prompt → pick;
   unclear → ask. (Logic ported from old session-start.)
4. **Exec call 2 — load the chosen project's startup set** in one cat
   (`AGENTS.override.md` + `.project` + `ROADMAP.md` + procedural memory).

---

## Git behavior (keyed on config, provider-agnostic)

git the protocol ≠ the host. The agent pushes to whatever `remote_url` is
configured; provider is irrelevant. Only auth (`key_path`) and the URL differ.

- `backup: none` → `git init`, auto-commit at session end, **no remote, no
  push, git never mentioned to the user.**
- `backup: <provider(s)>` + project configured → auto-commit AND `git push`
  to `remote_url` using `key_path`, per the `push` toggle and `autonomy`.

**Operator setup responsibilities (the agent cannot do these):**
- Generate the keypair on the VM.
- Register the **public** key on the provider (per-repo deploy key, or
  per-account).
- For deploy keys: **enable write access** (default read-only; forgetting
  this silently blocks every push).

**Ported hard-won git rules:**
- Never `git add -A`; stage explicit paths.
- Never force-push. On non-fast-forward rejection: diff, merge by hand, push.
- Re-check `git status`/`log` right before committing, not only at orientation.
- Push is REQUIRED when enabled — data loss historically came from failing
  to push, not from pushing.

---

## Decisions (locked)

1. **Root:** `~/projects/`. Canonical `AGENTS.md` and `agents_sync.sh` live there.
2. **Configs are FILES, not folders:** `~/projects/.projects` (global),
   `<project>/.project` (per-project), plain `key: value`.
3. **Repo creation:** agent never creates remotes. Operator pre-creates an
   empty repo; agent only pushes. No API tokens.
4. **Deploy keys per repo** are the default (security); account-level key
   supported via shared `key_path`. Keys live in `~/.ssh/`, never in the tree.
5. **`agents/` machinery folder** keeps its plain name (no dot prefix).
6. **Autonomy preference** recorded per project in `.project`.
7. **Sync is a visible VM-local script** `agents_sync.sh`, gated by a
   `.agents_sync` marker per project; copy command is NOT in `AGENTS.md`.
8. **Project `AGENTS.md` is a committed generated artifact** (portability for
   cloners); `.project` is **gitignored** (`.project` line in template
   `.gitignore`); `AGENTS.md` + `AGENTS.override.md` are committed; `.projects`
   global config is not copied into projects.
9. **Project derivation:** `ls -d ~/projects/*/` → directories, dotfolders
   excluded by the glob.

## Open (decide when drafting AGENTS.md)

- [ ] Exact autonomy level names + the default for new projects
      — **deferred to next session** (settled while drafting AGENTS.md)
- [ ] Keep the canonical file under the ~150-line budget; what gets pushed
      into machinery vs stays in `AGENTS.md`

## Resolved this session

- **`~/projects/` is NOT a git repo.** The canonical `AGENTS.md` and
  `agents_sync.sh` are not versioned at the workspace level; they are
  maintained by hand and backed up by the operator's own means. (No
  `.projects` gitignore question results.)
- **Accepted consequence:** editing the canonical `AGENTS.md` produces a
  committed diff in every marked project repo on the next sync. Correct,
  intended behavior — the generated copy tracks canonical.
- **Autonomy levels + new-project default:** deferred to next session.

---

## Acceptance criteria

- [ ] Canonical `AGENTS.md` in `~/projects/`, the only hand-edited copy
- [ ] `agents_sync.sh` visible, VM-local, copies into `.agents_sync`-marked
      projects only, skips unmarked/foreign folders
- [ ] Copy command absent from `AGENTS.md` content
- [ ] Per-project `AGENTS.md` committed as generated artifact with
      "do not edit" header; cloner fallback verified
- [ ] Override mechanism: `AGENTS.override.md`, absent/empty by default,
      override-wins-on-conflict stated in canonical file
- [ ] `~/projects/.projects` with `backup: none | <list>`
- [ ] `<project>/.project` schema: provider, remote_url, repo_name, push,
      key_path, autonomy — and gitignored
- [ ] SSH keys in `~/.ssh/`, referenced by `key_path`, never in tree
- [ ] Project registry folder-derived, never stored
- [ ] Startup sequence documented (sync+read+list in call 1; project set in call 2)
- [ ] Git behavior keyed on config; `none` path never mentions git
- [ ] Operator setup checklist: key gen, public-key registration, deploy-key
      write-enable
- [ ] Autonomy levels defined in `AGENTS.md`; per-project value selects one;
      agent asks once if unset
- [ ] `agents/` (machinery) vs `AGENTS.md` (instructions) distinction explicit

---

## Related cleanup (SEPARATE task, not started)

Agreed stale-doc fixes, held until this architecture is signed off because
both touch the same command files:
- Reconcile doc references to on-disk names (`agents/memory/procedural.md`,
  `docs/sessions/`, etc.) — direction (a), edit docs to match disk.
- Remove `tools/scripts/sweep-knowledge.py`; fold its decay logic into
  `session-end.md` as an agent instruction.
- Drop the phantom `daily-digest.md` reference from `agents/README.md`.
