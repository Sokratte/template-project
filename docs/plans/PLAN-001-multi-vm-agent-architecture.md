# PLAN-001: Multi-VM Agent Architecture

**Created:** 2026-06-17 · **Last updated:** 2026-06-18
**Topic:** Global AGENTS.md + per-project override + operator/VM identity file
+ backup + a visible sync script, for a reusable scaffold deployed identically
across multiple users' VMs.

**Summary (read this first):**
One agent works with one (often non-technical) human across all their
projects on one machine. Instructions are authored in ONE canonical
`~/projects/AGENTS.md`; a visible `agents_sync.sh` copies it into every
project that opts in via a `.agents_sync` marker, so each project repo
carries a working copy for anyone who clones it — while the canonical file
stays the only thing edited by hand. Projects differ only via a small
optional override (which also carries `push` + `autonomy`). Who the operator
is and what this VM is like lives in a single non-committed `~/projects/OPERATOR.md`.
The project list is derived from the folder structure, never stored. This
plan is the spec the build follows.

> **Session-10 revision.** Earlier drafts had a per-project `.project` config
> file and a global `.projects` config file. Both are gone. `.project`
> collapsed to two non-derivable toggles (`push`, `autonomy`) that moved into
> `AGENTS.override.md`; everything else it held was derivable (`remote_url`
> lives in `.git/config`; `provider`/`repo_name` derive from the remote;
> `key_path` derives from a naming convention). The global `.projects` was
> reframed: it was never a project registry — it is **operator + machine
> identity**, renamed `OPERATOR.md` and deliberately kept out of every repo
> because the operator profile is PII.

---

## Goal

Define where the agent's *instructions*, *operator/VM identity*, *backup
behavior*, and *sync mechanism* live so that: (a) the default user touches
nothing, (b) an improvement is applied everywhere by editing one file, (c)
instruction files cannot silently drift apart across projects, (d) anyone
cloning a single project repo gets a working, fully-instructed agent, and (e)
personal observations about the operator never enter a backed-up repo.

## Non-goals

- NOT: a per-project forked copy of the full instructions
- NOT: agent-created remote repos (no API tokens — see Decision 3)
- NOT: opinionated about backup provider — any git-protocol remote works
- NOT: a sync that touches foreign repos living under `~/projects/`
- NOT: storing anything git already stores (`remote_url`) or anything
  derivable (`provider`, `repo_name`, `key_path`)

---

## The two-axis model (plus an identity file)

- **Instructions** = *how* the agent works. Stable. Shared. → canonical
  `~/projects/AGENTS.md`, copied into each opted-in project.
- **Project context** = memory, decisions, specs, roadmap. Per-project. →
  each project's own folders (unchanged from current template).

Per-project *instruction* differences are rare, so they live in a small
optional override, not a forked file. The override is also where the two
per-project toggles (`push`, `autonomy`) live.

Cutting across both axes is a third thing that belongs to neither: **who the
operator is and what this machine is like.** That is not instructions (it is
not synced/identical across VMs) and not project context (it is not
project-scoped and must never be committed). It gets its own file,
`OPERATOR.md`, at the workspace root.

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
├── OPERATOR.md            # operator + VM identity (PII) — NEVER committed, NEVER cloned
├── agents_sync.sh         # visible sync script; VM-local, not committed to any project
├── recent_sessions.sh     # visible orientation script; VM-local, not committed
│
├── whisperdog/
│   ├── .agents_sync       # marker: "sync AGENTS.md into me"  ← opt-in, created by `cp -r` of the template
│   ├── AGENTS.md          # generated copy — committed (portability), chmod 444, "do not edit" header
│   ├── AGENTS.override.md # authored per project, committed; override wins on conflict; holds push + autonomy
│   └── agents/            # machinery: memory/, commands/, notes/, rules/
│
├── tradingbot/
│   └── … (same shape)
│
└── some-foreign-repo/     # NO .agents_sync marker → sync skips it; its own AGENTS.md untouched

~/.ssh/
├── <project>              # private deploy key — NEVER in any project tree; path DERIVED from project name
└── <project>.pub          # public key — operator registers this on the provider
```

There are no longer any `.project` / `.projects` config files. Backup remote
config lives in `.git/config` (git's own); operator/VM facts live in
`OPERATOR.md`; the two per-project toggles live in `AGENTS.override.md`.

---

## File inventory

### 1. Canonical instructions — `~/projects/AGENTS.md`
- The ONE file edited by hand. Single source of truth for agent behavior.
- Lives in the `~/projects/` workspace (so it is itself backed up by the
  operator's own means; `~/projects/` is not a project git repo).
- Contains: agent identity + persona model, session-start/end routine,
  universal rules, git behavior (keyed on what git + the override say, not on
  a separate config), nav conventions, the override-loading rule, the backup
  behavior rules, autonomy-level definitions, persona presets.
- **Identical across all VMs.** This is the invariant the whole design
  protects. Nothing VM-specific or operator-specific goes here — that is what
  `OPERATOR.md` is for.
- **Does NOT contain the copy command.** The sync mechanism lives in
  `agents_sync.sh`, never in this content — so a cloner's agent reading a
  project's `AGENTS.md` never executes a destructive copy.
- Keep lean: target well under ~150 lines; push detail into machinery.

### 2. Operator + VM identity — `~/projects/OPERATOR.md`  *(was `.projects`)*
- **What it is:** a file about *the operator and this machine*, not about
  projects. Answers "who am I working with, and what is true about this VM?"
- **Markdown, not `key: value`** — because the agent maintains it as a
  narrative profile that grows over time (communication style, how the
  operator likes to work, standing preferences).
- **NEVER committed, NEVER cloned.** It lives at the workspace root, outside
  every project tree, so it is structurally incapable of being pushed to a
  remote. **Rationale is privacy:** the operator profile is personal
  observation about a named human; publishing it (a repo may be public) would
  be a real privacy breach, not a style slip. This is the single home for the
  operator profile — it was REMOVED from `procedural.md` (see SPEC-003 §8.1).
- **Holds:**
  - Operator profile — name, communication style, decision-making, when to
    push back vs. execute. The relationship memory.
  - Backup preference for this VM/operator — `backup: none` or
    `backup: <provider(s)>` (e.g. "Martin uses GitHub"). VM-level grain; the
    per-project on/off is the finer `push` toggle in the override.
  - Setup habits — e.g. "on a new project, ask whether the remote already
    exists (pull) or must be created."
  - SSH key convention — e.g. "deploy keys are `~/.ssh/<project>`."
  - Any other VM-specific fact that should NOT travel to a cloner.
- A cloner is a different operator on a different machine → they get their own
  `OPERATOR.md`; inheriting the original operator's would be both wrong and a
  privacy leak. That is exactly why it is not cloned.
- Loaded once at startup (exec-1), alongside the canonical `AGENTS.md`.

### 3. Generated per-project copy — `<project>/AGENTS.md`
- A **committed copy** of the canonical file, placed by `agents_sync.sh`.
- Treated as a **generated artifact, not source.** A short header marks it:
  "Do not edit — synced from ~/projects/AGENTS.md. Project rules go in
  AGENTS.override.md."
- **chmod 444 (read-only).** The sync script owns the permission dance:
  `chmod u+w` → `cp` → `chmod 444`. This stops accidental editor saves to the
  wrong file (the same pattern many Linux-managed config files use). It does
  not stop the agent (which can chmod), so it is a guard-rail, not a lock.
- Exists so a cloner of the single project repo gets working instructions.

### 4. Per-project override — `<project>/AGENTS.override.md`
- **Normally minimal.** Authored by hand, committed. Holds:
  - Project-specific instruction differences (rare; override wins on conflict).
  - **Persona** — which preset (or a Custom freeform persona) + the agent's
    chosen **name** (default Tinkerbuddy).
  - **`autonomy: <level>`** — selects one of the levels defined in AGENTS.md.
  - **`push: <on|off>`** — the per-project backup toggle.
- Rule (stated in the canonical file): "load me, then load the project
  override if one exists; on conflict, the override wins."
- Bounded: a small override, never a forked full file.

### 5. Sync script — `~/projects/agents_sync.sh`
- **Visible** (not dot-prefixed), sits next to `AGENTS.md`.
- VM-local: lives only on the operator's VM, **not committed** into any
  project repo, so a cloner's machine never has it and can never run the
  destructive copy.
- Behavior: for each directory in `~/projects/*/`, **if it contains a
  `.agents_sync` marker**, sync `~/projects/AGENTS.md` into it with the
  permission dance (`chmod u+w`, `cp`, `chmod 444`). Unmarked folders
  (foreign clones, reference repos) are skipped entirely.
- Self-enumerates the project list — does not depend on `AGENTS.md` having
  been read first, so it can run first in startup call 1.

### 6. Orientation script — `~/projects/recent_sessions.sh`  *(new)*
- **Visible, VM-local, not committed** (same rationale as the sync script).
- Behavior: across all projects, find the 3 most-recently-modified session
  logs and print `head -1` of each — the abstract's first line, which by
  convention is `date | project | one-line-summary` (SPEC-003 / PLAN-002
  abstract convention).
  ```bash
  ls -t ~/projects/*/docs/sessions/*.md 2>/dev/null | head -3 \
    | while read -r f; do head -1 "$f"; done
  ```
- Purpose: gives the agent cross-project orientation in exec-1 so it can (a)
  greet the operator with "here's where you left off" and (b) disambiguate
  which project to select when the prompt is unclear (startup step 3/4).
- Runs as part of the exec-1 pipeline — no extra tool call.

### 7. Opt-in marker — `<project>/.agents_sync`
- Empty marker file. Its presence means "this project is template-derived,
  sync the canonical AGENTS.md into it."
- Created automatically by `cp -r template-project <new>`, so the operator's
  own projects opt in with zero thought. Foreign repos lack it → safe by default.

### 8. Per-project machinery — `<project>/agents/`  *(unchanged shape)*
- Template folder: `memory/`, `commands/`, `notes/`, `rules/`.
- The *machinery* (how work is tracked), distinct from the *instructions* in
  `AGENTS.md` / the override.
- **Note:** `agents/memory/procedural.md` now holds procedural RULES only —
  the operator-profile section moved to `OPERATOR.md` (Decision 11).
- Naming note: `AGENTS.md` (instructions, standard) vs `agents/` (machinery,
  our folder). Folder keeps its plain name (no dot prefix).

### 9. SSH keys — `~/.ssh/<project>[.pub]`
- Private + public deploy key per repo. **Outside every project tree**,
  never committed, `600` perms. Path is **derived by convention** from the
  project name (documented in `OPERATOR.md`), not stored anywhere.

---

## What git already stores — do not duplicate

A whole class of former `.project` fields were redundant copies of state git
maintains itself. The agent reads them from git, never from our own file:

| Former field | Real source | How the agent gets it |
|--------------|-------------|-----------------------|
| `remote_url` | `.git/config` | `git remote get-url origin` |
| `provider` | the remote host | parse the remote URL host |
| `repo_name` | folder / remote | basename of the remote URL or folder |
| `key_path` | naming convention | `~/.ssh/<project-name>` (per `OPERATOR.md`) |

Storing these separately was two-sources-of-truth-that-drift. `.git/config` is
canonical for the remote; the naming convention is canonical for the key.

---

## Sync mechanism — the drift-proof + cloner-safe design

The problem: the canonical file must be edited once and apply everywhere
(drift-proof), AND a working copy must ride inside each project repo so a
cloner gets a usable agent (portability). Naively committing N copies
reintroduces drift; a symlink breaks on clone; an in-`AGENTS.md` copy command
makes a cloner's agent overwrite the cloner's own file every session.

The resolution, four parts:

1. **Canonical file** `~/projects/AGENTS.md` is the only hand-edited copy.
2. **`agents_sync.sh`** copies it into every project bearing `.agents_sync`,
   with the read-only permission dance. The in-project copy is a generated
   artifact, overwritten each run → cannot drift by accident on this VM.
3. **The copy command lives in the script, not in `AGENTS.md`.** Portable
   content carries no instruction to overwrite anything, so a cloner's agent
   never clobbers the cloner's file.
4. **`.agents_sync` marker gates the sync** → foreign repos under `~/projects/`
   are never touched. Protects reference repos (tbh, maisig, tinkerbuddy, …).

### Why the sync command is not in AGENTS.md
If the copy instruction lived inside `AGENTS.md`, any agent reading a cloned
project's `AGENTS.md` would run it and overwrite the cloner's own file every
session. Keeping the mechanism in a VM-local script that foreign machines
never receive removes the footgun entirely.

### Cloner cases
- **Operator's VM:** `agents_sync.sh` keeps every marked project's copy
  matching the canonical file.
- **Cloner with the full workspace:** their own `agents_sync.sh` + canonical
  file sync their version in. They write their own `OPERATOR.md`.
- **Cloner of a single project repo, no workspace:** no script exists to run,
  so nothing overwrites anything. The committed in-repo `AGENTS.md` stands as
  the working fallback. No `OPERATOR.md` is present (correct — different
  operator), so the agent prompts to create one.

---

## Agent autonomy + persona

Two separate-but-correlated knobs, both recorded per project in
`AGENTS.override.md`. The canonical `AGENTS.md` defines what each means; the
override selects.

### Autonomy levels
- `autonomous` — commits, pushes, edits, proceeds without asking; reports
  after. Trusting users / low-stakes projects.
- `checkpoint` — acts freely on routine work but pauses for explicit approval
  before consequential or irreversible actions (deleting files, schema
  changes, anything force-relevant in git). **Default.**
- `confirm` — proposes before nearly every action; user approves each step.
  Cautious users / high-stakes projects.

**Resolution order:** `AGENTS.override.md autonomy:` → persona's default →
hardcoded `checkpoint`. The agent does **not** ask at project setup unless a
Custom persona is chosen (no preset to imply a level). Silent fallback to
`checkpoint` otherwise — no token spent deliberating.

### Persona presets
Each preset is a behavioral profile that tunes every prompt, and ships a
default autonomy. A persona is prompt-tuning, so presets are defined by what
they change in outputs — never by risk-seeking flavor (a "greedy trader"
persona would degrade the very discipline a trading bot needs).

| Persona | Default autonomy | Tuning |
|---------|-----------------|--------|
| ⚡ Operator | `autonomous` | Bias to action, terse, acts then reports |
| 🛠️ Craftsman (default) | `checkpoint` | Correctness > speed, specs first, pushes back, pauses before irreversible actions |
| 🔍 Reviewer | `confirm` | Proposes before acting, explains reasoning, operator approves each step |
| ✍️ Custom | asked at setup | Operator describes the persona in their own words; pick autonomy at setup |

- **Name:** the agent's name is operator-chosen, independent of persona;
  default **Tinkerbuddy**. Written into the override next to the persona.
- **Defaults for a new project:** Craftsman / checkpoint / Tinkerbuddy.
- The full preset table lives in CREATE_PROJECT (the setup menu), not in the
  synced canonical file — keeps AGENTS.md lean. The chosen persona's
  behavioral contract is written into the override so it travels with clones.

---

## Startup sequence

1. **Tool search** → returns tools + "before anything, run startup."
2. **Exec call 1 — sync, read identity, list projects, orient** (one call;
   the script self-enumerates, so it needs nothing from `AGENTS.md` first):
   ```bash
   bash ~/projects/agents_sync.sh \
     && cat ~/projects/AGENTS.md ~/projects/OPERATOR.md \
     && echo "=== PROJECTS ===" \
     && ls -d ~/projects/*/ 2>/dev/null | xargs -n1 basename \
     && echo "=== RECENT ===" \
     && bash ~/projects/recent_sessions.sh
   ```
   Project list is **derived from folders, never stored.** `OPERATOR.md` may
   be absent (fresh clone, new VM) → the agent prompts to create one.
3. Agent selects the project: 1 → pick; >1 and prompt >50% clear → pick;
   unclear → if the 3 recent-session lines point to one project, pick it,
   else **stop and ask**.
4. **Exec call 2 — load the chosen project's startup set** in one call
   (`AGENTS.override.md` + `ROADMAP.md` abstract+active + `procedural.md` +
   `session-start.md` + `work-backlog.md`).

---

## Git behavior (keyed on git + override, provider-agnostic)

git the protocol ≠ the host. The agent pushes to whatever `origin` is set to
in `.git/config`; provider is irrelevant. Only auth (the convention-named
key) and the URL differ, and both come from git / convention, not our config.

- `OPERATOR.md` says `backup: none` → `git init`, auto-commit at session end,
  **no remote, no push, git never mentioned to the user.**
- `OPERATOR.md` says `backup: <provider(s)>` AND the project override has
  `push: on` AND `origin` is set → auto-commit AND `git push`, gated by
  `autonomy`.

**Operator setup responsibilities (the agent cannot do these):**
- Generate the keypair on the VM (named by convention, `~/.ssh/<project>`).
- Register the **public** key on the provider (per-repo deploy key, or
  per-account).
- Add the remote (`git remote add origin <url>`) — after which git owns it.
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

1. **Root:** `~/projects/`. Canonical `AGENTS.md`, `OPERATOR.md`, and the two
   scripts live there.
2. **No standalone config files.** `.project` and `.projects` are both
   removed. Derivable/git-owned values are not stored; the two real
   per-project toggles (`push`, `autonomy`) live in `AGENTS.override.md`.
3. **Repo creation:** agent never creates remotes. Operator pre-creates an
   empty repo and adds the remote; agent only pushes. No API tokens.
4. **Deploy keys per repo** are the default (security); path derived by
   convention `~/.ssh/<project>`, documented in `OPERATOR.md`. Keys live in
   `~/.ssh/`, never in the tree.
5. **`agents/` machinery folder** keeps its plain name (no dot prefix).
6. **Autonomy + persona + name** recorded per project in `AGENTS.override.md`.
7. **Sync is a visible VM-local script** `agents_sync.sh`, gated by a
   `.agents_sync` marker; copy command is NOT in `AGENTS.md`; sync applies
   chmod 444 to the project copy.
8. **Project `AGENTS.md` is a committed, read-only (444) generated artifact**
   with a "do not edit" header; `AGENTS.override.md` is committed.
9. **Project derivation:** `ls -d ~/projects/*/` → directories, dotfolders
   excluded by the glob.
10. **`OPERATOR.md` (was `.projects`) is operator+VM identity, Markdown,
    NEVER committed, NEVER cloned.** Rationale: privacy (operator profile is
    PII) + it is the per-VM seam that keeps canonical `AGENTS.md` identical.
11. **Operator profile has ONE home: `OPERATOR.md`.** It is REMOVED from
    `agents/memory/procedural.md`, which becomes procedural-rules-only.
12. **`recent_sessions.sh`** prints `date | project | summary` for the 3
    newest session logs across all projects, in exec-1.

## Resolved (session 09–10)

- **`~/projects/` is NOT a git repo.** Canonical `AGENTS.md`, `OPERATOR.md`,
  and the scripts are maintained by hand and backed up by the operator's own
  means.
- **Editing canonical `AGENTS.md` produces a committed diff in every marked
  project on next sync.** Correct, intended — the generated copy tracks
  canonical.
- **Autonomy levels + default:** `autonomous`/`checkpoint`/`confirm`,
  default `checkpoint`, silent fallback (no ask) except for Custom persona.
- **Persona model:** Operator / Craftsman / Reviewer / Custom, each with a
  default autonomy; operator-chosen name, default Tinkerbuddy.
- **`.project` / `.projects` eliminated; `OPERATOR.md` introduced; operator
  profile de-duplicated to a single non-committed home.**

---

## Acceptance criteria

- [ ] Canonical `AGENTS.md` in `~/projects/`, identical across VMs, the only
      hand-edited copy, under line budget
- [ ] `OPERATOR.md` in `~/projects/`: operator profile + backup pref + setup
      habits + key convention; never committed; absent → agent prompts to create
- [ ] Operator profile REMOVED from `procedural.md` (single home in OPERATOR.md)
- [ ] `agents_sync.sh` visible, VM-local, copies into `.agents_sync`-marked
      projects only, applies chmod 444 with the permission dance
- [ ] `recent_sessions.sh` visible, VM-local, prints 3 newest session-log
      head lines across projects; wired into exec-1
- [ ] Copy command absent from `AGENTS.md` content
- [ ] Per-project `AGENTS.md` committed, 444, "do not edit" header; cloner
      fallback verified
- [ ] `AGENTS.override.md`: override-wins rule stated; holds persona + name +
      `autonomy` + `push`
- [ ] No `.project` / `.projects` files anywhere; `.gitignore` line for
      `.project` removed
- [ ] No stored `remote_url`/`provider`/`repo_name`/`key_path` — all derived
- [ ] SSH keys in `~/.ssh/`, named by convention, never in tree
- [ ] Project registry folder-derived, never stored
- [ ] Startup: exec-1 (sync+read AGENTS+OPERATOR+list+recent) and exec-2
      (project set) documented
- [ ] Git behavior keyed on `.git/config` + `OPERATOR.md backup` + override
      `push`; `none` path never mentions git
- [ ] Operator setup checklist: key gen, remote add, public-key registration,
      deploy-key write-enable
- [ ] Autonomy + persona defined in `AGENTS.md`/CREATE_PROJECT; override
      selects; Custom asks once
- [ ] `agents/` (machinery) vs `AGENTS.md` (instructions) distinction explicit

---

## Related cleanup (folded into PLAN-002 execution)

- Reconcile doc references to on-disk names (`agents/memory/procedural.md`,
  `docs/sessions/`, etc.) — edit docs to match disk.
- Remove `tools/scripts/sweep-knowledge.py`; decay logic → `session-end.md`.
- Drop the phantom `daily-digest.md` reference from `agents/README.md`.
