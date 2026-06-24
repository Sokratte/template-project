<!-- file: PLAN-002-agents-md-authoring.md · keywords: canonical AGENTS.md, startup sequence, three-tier read model, abstract convention, awk, persona, autonomy, work-backlog, session-start -->

# PLAN-002: AGENTS.md Authoring

**Status:** Implementation in progress
**Created:** 2026-06-17 · **Updated:** 2026-06-18

PLAN-001 locked the multi-VM *architecture* (layout, sync script, the `LOCAL.md` identity file, git keyed on git+override) but deferred *what the canonical file says and how it reads*. This plan captures those content decisions across sessions 09–10: the exec-1/exec-2 startup sequence, which files are read whole vs. partially vs. on-demand, a `##`-terminated greppable abstract convention, awk-based section reading so large docs need no splitting, the persona/autonomy model, and the work-backlog / work-log rename that fixes buried TODOs. It also lists the ripple edits these decisions force in existing docs. This plan is the spec the AGENTS.md draft follows.

## Goal

Produce the canonical `~/projects/AGENTS.md` (PLAN-001 file 1) — lean, under its line budget, containing: identity + persona model, ground truth, folder-derived project selection, the two-call startup sequence, the three-tier document read model, document conventions, the memory model, and git behavior keyed on git+override. And: execute the dependent renames and doc fixes so no document keeps asserting the superseded contracts.

## Non-goals

- NOT re-deciding PLAN-001 architecture — that is locked (incl. the session-10 revision: no `.project`/`.projects`, `LOCAL.md` introduced).
- NOT the sync mechanism itself (`agents_sync.sh`) — PLAN-001 owns it; the copy command must never appear in AGENTS.md content (PLAN-001 Decision 7).
- NOT rewriting CREATE_PROJECT.md in full — its own later task; this plan adds the persona-selection step and the budgets-table fix.

## Decisions locked

### 1. Startup is two exec calls, project list folder-derived

1. **Exec 1:** `agents_sync.sh && cat AGENTS.md LOCAL.md && bash projects_list.sh`. The sync script self-enumerates folders, so it needs nothing from AGENTS.md first. Project registry is derived from folders, never stored (PLAN-001 Decision 9). `LOCAL.md` is read here (VM/operator identity); if absent, the agent prompts to create one.
2. **Agent selects:** 1 project → pick; >1 and prompt >50% clear → pick; unclear → if the 3 `projects_list.sh` recent-session lines point to one project pick it, else **stop and ask**. None / new → project setup, stop here.
3. **Exec 2:** one call that reads the project's guaranteed startup set (below).
4. Work from the operator's prompt.

### 2. Three-tier read model

| Tier | Files | Operation | When |
|---|---|---|---|
| Load whole | `AGENTS.override.md`, `agents/memory/procedural.md`, `agents/commands/session-start.md` | `cat` | every startup (exec-2) |
| Load partial | `ROADMAP.md` (abstract + active section), `agents/notes/work-backlog.md` (complete — bounded by design) | `awk` / `cat` | every startup (exec-2) |
| Orient on demand | `~/projects/AGENTS.md` + SPECS (heading-grep); PLANS, RESEARCH, last 3 SESSIONS (abstract) | `grep` / `awk` / `head` | only when the task needs it |

exec-2 contains ONLY files every project is guaranteed to have. `.project` is gone, so it is no longer in the set. Operator identity is loaded in exec-1 (`LOCAL.md`), not exec-2, because it is VM-scoped not project-scoped.

Candidate exec-2 pipeline:
```bash
cat AGENTS.override.md agents/memory/procedural.md \
    agents/commands/session-start.md \
&& echo "=== ROADMAP ===" \
&& awk '/^## /&&++n==2{exit} 1' ROADMAP.md \
&& echo "=== WORK-BACKLOG ===" \
&& cat agents/notes/work-backlog.md
```

### 3. Document convention: `##`-terminated abstract

- Every SPEC, PLAN, research doc, and session log opens with an **abstract**: everything from the top of the file down to the **first `##` heading**.
- **Terminator is the first `##`, NOT `---`.** Chosen on failure-cost: a forgotten `##` effectively never happens (structured docs have headings), whereas a forgotten `---` would make awk read the entire file by accident. Authoring rule: do not put a `##` inside an abstract.
- **No fixed line count.** The delimiter bounds it, not a counter (a counter rots on edit).
- **Session-log line 1 is `<!-- keywords: … -->`** (bare filename on line 2) per the docs/README.md convention; `projects_list.sh` uses path-parsing (not file content) to derive the project name.

### 4. awk section-reading — large docs are NOT split into files

```bash
awk '/^## /{exit} {print}' FILE.md                              # abstract
grep -n '^#\+ ' FILE.md                                         # heading map
awk '/^## SECTION/{f=1;print;next} f&&/^## /{exit} f' FILE.md  # one section
```

A 2,000-line spec costs the same to orient as a 200-line one. Big specs/plans stay single files — sectioned at read-time, not split on disk.

### 5. work-backlog / work-log split (renames + contract fix)

| New name | Was | Holds | On completion | Read at startup |
|---|---|---|---|---|
| `work-backlog.md` | `worklog.md` | open items: TODOs, findings, notes | move the line to `work-log.md` | `cat` complete; **alert operator if >20 items** |
| `work-log.md` | `worklog-archive.md` | done items, append-only history | terminal | never auto-read; grep on demand |

- "Append-only" belongs to `work-log.md`, not the backlog. The backlog is a pruned living list.
- Names: "backlog" = ahead (open), "log" = behind (done).
- **Done on disk (session 10):** both `git mv`s committed (`4a00939`), history preserved 100%.

### 6. Persona + autonomy model (session 10)

Two separate knobs, both in `AGENTS.override.md`; defined in AGENTS.md / CREATE_PROJECT; selected per project.

- **Autonomy:** `autonomous` / `checkpoint` (default) / `confirm`. Resolution: override `autonomy:` → persona default → hardcoded `checkpoint`. Agent does NOT ask at setup except for a Custom persona.
- **Personas:** Operator (`autonomous`) / Craftsman (`checkpoint`, default) / Reviewer (`confirm`) / Custom (asked). Each is behavioral prompt-tuning, not risk-flavor. Full table in CREATE_PROJECT, chosen contract written to the override so it travels with clones.
- **Name:** operator-chosen, independent of persona, default **Tinkerbuddy**.
- New-project defaults: Craftsman / checkpoint / Tinkerbuddy.

### 7. LOCAL.md + config elimination (session 10)

- `.project` and `.projects` both removed (PLAN-001 session-10 revision).
- Operator profile has ONE home, `~/projects/LOCAL.md`, NEVER committed (privacy: PII must not enter a backed-up, possibly public repo). It is REMOVED from `procedural.md`, which becomes procedural-rules-only.
- The two real per-project toggles (`push`, `autonomy`) live in the override.
- `remote_url`/`provider`/`repo_name`/`key_path` are not stored — derived from `.git/config` and a key naming convention.

## Execution checklist

- [x] `git mv worklog.md → work-backlog.md`, `worklog-archive.md → work-log.md` (session 10, committed `4a00939`)
- [x] append-only → `work-log.md`; backlog as pruned open-items list; >20-item alarm; decay folded into session-end; Claude symlink section removed; file-map paths fixed to disk (session 10)
- [x] procedural-rules-only; update startup to load LOCAL.md in exec-1; drop `.project` from exec-2
- [x] `agents/commands/session-start.md`: rewrite as executable steps for the new world; new file names; `docs/sessions/` path; LOCAL.md loaded in exec-1; on-demand grep/abstract tier lives here
- [x] `agents/commands/session-end.md`: backlog/log refs; completion-moves-to-work-log step; decay-sweep instruction folded in
- [x] `agents/README.md`: file inventory rename; drop phantom `daily-digest.md`
- [x] `agents/memory/procedural.md`: REMOVE operator-profile section (→ LOCAL.md); keep procedural rules only
- [x] `agents/memory/operational.md`: fix sweep-script reference (decay is now a session-end instruction)
- [x] Remove `tools/scripts/sweep-knowledge.py` (needs `git rm` from operator)
- [x] `.gitignore`: remove the `.project` line (file no longer exists)
- [ ] CREATE_PROJECT.md: budgets table → `work-backlog` (>20 items) + `work-log` (append-only); add persona-selection step (table + Custom + name default Tinkerbuddy); document LOCAL.md creation; key convention
- [ ] Author canonical `~/projects/AGENTS.md` (the main deliverable) — last, against the now-consistent codebase

## session-start.md rewrite (target shape)

AGENTS.md (exec) does the *reading*; session-start.md is the *steps to execute* after the guaranteed set is loaded:

1. Confirm platform memory is disabled for this project (remind if missing).
2. Check git status; re-check right before any commit (shared working copy moves under you — PLAN-001 git rules).
3. If the task continues prior work: grep SPEC heading-maps; read relevant section(s) via awk; read abstracts of related PLANs/RESEARCH; head last 3 session logs. Skip entirely for fresh work.
4. Open / append the session log (during work, not retrospectively).

## Open

- [ ] AGENTS.md line budget enforcement — what stays vs. pushes to machinery to hold under ~150 lines. (Persona table → CREATE_PROJECT helps.)

## Acceptance criteria

- [ ] Canonical AGENTS.md drafted: identity + persona model, ground truth, folder-derived selection, two-call startup (exec-1 loads LOCAL.md), three-tier read model, document conventions, memory model, git-keyed-on-git+override — under line budget.
- [ ] Copy/sync command absent from AGENTS.md content (PLAN-001 Decision 7).
- [x] Abstract convention (`##`-terminated) documented once; session-log line 1 is `<!-- keywords: … -->` (bare filename on line 2).
- [x] awk three-move retrieval documented as the habit for large docs.
- [x] work-backlog/work-log renamed on disk with history preserved; append-only on work-log only.
- [ ] All other docs reference new names; no doc asserts superseded contracts ("append-only worklog", `~/workspace`, `.project`/`.projects`, operator profile in procedural.md).
- [ ] >20-item backlog alarm specified in AGENTS.md + session procedures.
- [x] session-start.md rewritten as executable steps for the new world.
- [ ] LOCAL.md documented; operator profile single-homed; CREATE_PROJECT persona step added. *(partial: single-homed ✓, CREATE_PROJECT persona step still open)*
