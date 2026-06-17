# PLAN-002: AGENTS.md Authoring

**Created:** 2026-06-17 · **Last updated:** 2026-06-17
**Topic:** Author the canonical `~/projects/AGENTS.md` content deferred by
PLAN-001 — the startup flow, the three-tier read model, document conventions,
and the dependent file renames and doc cleanup.

**Summary (read this first):**
PLAN-001 locked the multi-VM *architecture* (layout, sync script, configs,
git keyed on config) but explicitly deferred *what the file says and how it
reads*. This plan captures those content decisions, made with the operator
across session 09: the exec-1/exec-2 startup sequence, which files are read
whole vs. partially vs. on-demand, a delimiter-based greppable abstract
convention, awk-based section reading so large docs need no splitting, and
the work-backlog / work-log rename that fixes buried TODOs. It also lists the
ripple edits these decisions force in existing docs. This plan is the spec
the AGENTS.md draft follows.

---

## Goal

Produce the canonical `~/projects/AGENTS.md` (PLAN-001 file 1) — lean, under
its line budget, containing: identity, ground truth, folder-derived project
selection, the two-call startup sequence, the three-tier document read model,
document conventions (abstract + headings), the memory model, and git
behavior keyed on config. And: execute the dependent renames and doc fixes so
no document keeps asserting the superseded contracts.

## Non-goals

- NOT re-deciding PLAN-001 architecture — that is locked.
- NOT the sync mechanism itself (`agents_sync.sh`) — PLAN-001 owns it; the
  copy command must never appear in AGENTS.md content (PLAN-001 Decision 7).
- NOT rewriting CREATE_PROJECT.md in full — that is its own later task; only
  a forward-note was added this session.

---

## Decisions locked this session

### 1. Startup is two exec calls, project list folder-derived

1. **Exec 1:** `agents_sync.sh && cat AGENTS.md && ls -d ~/projects/*/`.
   The script self-enumerates folders, so it does not need the list from
   AGENTS.md first. Project registry is derived from folders, never stored
   (PLAN-001 Decision 9).
2. **Agent selects:** 1 project → pick; >1 and prompt >50% clear → pick;
   unclear → if last 3 session logs are the same project pick it, else
   **stop and ask**. None / new → project setup, stop here.
3. **Exec 2:** one call that reads the project's guaranteed startup set
   (below). `cat`/`awk`/`tail` pipeline OR a multi-file read tool — either
   way, one tool call.
4. Work from the operator's prompt.

### 2. Three-tier read model

| Tier | Files | Operation | When |
|------|-------|-----------|------|
| Load whole | `AGENTS.override.md`, `.project`, `agents/memory/procedural.md`, `agents/commands/session-start.md` | `cat` | every startup (exec-2) |
| Load partial | `ROADMAP.md` (abstract + active section), `agents/notes/work-backlog.md` (complete — bounded by design) | `awk` / `cat` | every startup (exec-2) |
| Orient on demand | `agents/rules/global.md` + SPECS (heading-grep); PLANS, RESEARCH, last 3 SESSIONS (abstract) | `grep` / `awk` / `head` | only when the task needs it (session-start steps, not exec-2) |

exec-2 contains ONLY files every project is guaranteed to have. Optional
material (research, session logs) is never in exec-2 — it is conditional
orientation inside session-start.md.

Candidate exec-2 pipeline:
```bash
cat AGENTS.override.md .project agents/memory/procedural.md \
    agents/commands/session-start.md \
&& echo "=== ROADMAP ===" \
&& awk '/^## /&&++n==2{exit} 1' ROADMAP.md \
&& echo "=== WORK-BACKLOG ===" \
&& cat agents/notes/work-backlog.md
```

### 3. Document convention: greppable abstract + headings

- Every SPEC, PLAN, research doc, and session log opens with an **abstract**:
  everything from the top of the file down to the **first `##` heading**.
- **Terminator is the first `##`, NOT `---`.** Chosen on failure-cost: a
  forgotten `##` effectively never happens (structured docs have headings),
  whereas a forgotten `---` would make awk read the entire file by accident.
  Authoring rule: do not put a `##` inside an abstract.
- **No fixed line count.** Abstract length is whatever the author needs;
  the delimiter bounds it, not a counter (a counter rots on edit).

### 4. awk section-reading — large docs are NOT split into files

Three retrieval moves keep orientation O(1) regardless of doc size:
```bash
awk '/^## /{exit} {print}' FILE.md                 # (a) abstract / gist
grep -n '^#\+ ' FILE.md                             # (b) heading map
awk '/^## SECTION/{f=1;print;next} f&&/^## /{exit} f' FILE.md   # (c) one section
```
A 2,000-line spec costs the same to orient as a 200-line one. This is why
big specs/plans stay single files — sectioned at read-time, not split on
disk (consistent with the consolidation principle).

### 5. work-backlog / work-log split (renames + contract fix)

The old `worklog.md` conflated two jobs ("what happened" vs. "open
findings/TODOs"), which buried important TODOs under history. Fix is a
contract change, not a smarter read:

| New name | Was | Holds | On completion | Read at startup |
|----------|-----|-------|---------------|-----------------|
| `work-backlog.md` | `worklog.md` | open items: TODOs, findings, notes | move the line to `work-log.md` | `cat` complete; **alert operator if >20 items** |
| `work-log.md` | `worklog-archive.md` | done items, append-only history | terminal | never auto-read; grep on demand |

- "Append-only" was attached to the wrong file. It belongs to `work-log.md`,
  not the backlog. The backlog is a pruned living list.
- The >20-item alarm is meaningful only for the backlog: 20 open items = real
  backlog problem or a mis-set preference. Prevents the file growing to
  hundreds of lines with TODOs hiding at the top.
- Names: "backlog" = ahead (open), "log" = behind (done). Tense problem gone.

---

## Ripple edits forced by these decisions (execution checklist)

- [ ] `git mv agents/notes/worklog.md agents/notes/work-backlog.md`
- [ ] `git mv agents/notes/worklog-archive.md agents/notes/work-log.md`
- [ ] SPEC-003 (agent memory): rename refs; move "append-only" + large limits
      to `work-log.md`; redefine `work-backlog.md` as pruned open-items list;
      replace 60/100-line limits with the >20-item alarm.
- [ ] CREATE_PROJECT.md budgets table: `worklog` rows → `work-backlog`
      (>20 items) and `work-log` (append-only). Update "Where Things Live"
      and "Memory System" tables to new names.
- [ ] `agents/commands/session-start.md`: rewrite as executable steps for the
      new world (see "session-start rewrite" below); drop old `~/workspace`
      and `changelog/session-logs/` paths; use new file names; the
      on-demand grep/abstract tier lives here, run only when continuing work.
- [ ] `agents/commands/session-end.md`: worklog→backlog/log refs; the
      completion-moves-to-work-log step; fold decay-sweep logic in (per
      PLAN-001 related-cleanup) instead of the standalone script.
- [ ] `agents/README.md`: file inventory rename; drop phantom
      `daily-digest.md` reference (PLAN-001 related-cleanup).
- [ ] `agents/memory/procedural.md`, `operational.md`: worklog refs if any.
- [ ] Remove `tools/scripts/sweep-knowledge.py`; decay logic → session-end
      instruction (PLAN-001 related-cleanup).

These are grouped commits, NOT one sweep. Renames are one commit; doc-contract
fixes another; AGENTS.md draft another.

---

## session-start.md rewrite (target shape)

AGENTS.md (exec-2) does the *reading*; session-start.md is the *steps to
execute* after the guaranteed set is loaded:

1. Confirm platform memory is disabled for this project (remind if missing).
2. Check git status; re-check right before any commit (shared working copy
   moves under you — PLAN-001 git rules).
3. If the task continues prior work: grep SPEC heading-maps; read relevant
   section(s) via awk; read abstracts of related PLANs/RESEARCH; head last 3
   session logs. Skip entirely for fresh work.
4. Open / append the session log (during work, not retrospectively).

---

## Open (decide when drafting)

- [ ] **Autonomy level names + new-project default** (carried from PLAN-001;
      lean `checkpoint` ~70%). AGENTS.md defines what each level means;
      `.project` selects one; agent asks once if unset.
- [ ] AGENTS.md line budget enforcement — what stays vs. pushes to machinery
      to hold under ~150 lines.
- [ ] Whether agent personas (Auditor / Craftsman / Tinkerbuddy) are global
      (in AGENTS.md) or per-project (in AGENTS.override.md). Leaning override
      (~75%) since one file is synced into every project.
- [ ] Rename churn check: keep `work-backlog`/`work-log`, or defer renaming
      until after AGENTS.md draft to avoid drafting against changing names?

---

## Acceptance criteria

- [ ] Canonical AGENTS.md drafted: identity, ground truth, folder-derived
      selection, two-call startup, three-tier read model, document
      conventions, memory model, git-keyed-on-config — under line budget.
- [ ] Copy/sync command absent from AGENTS.md content (PLAN-001 Decision 7).
- [ ] Abstract convention (`##`-terminated) documented once and applied to
      SPEC/PLAN/RESEARCH/SESSION templates.
- [ ] awk three-move retrieval documented as the habit for large docs.
- [ ] work-backlog/work-log renamed on disk with history preserved; all docs
      reference new names; append-only contract on work-log only.
- [ ] >20-item backlog alarm specified in AGENTS.md + session procedures.
- [ ] session-start.md rewritten as executable steps for the new world.
- [ ] No doc still asserts the superseded "append-only worklog" or
      `~/workspace` paths.

---

## Related

- Parent: PLAN-001 (architecture — locked).
- This plan owns the content + the dependent renames/cleanup PLAN-001 listed
  as "Related cleanup (SEPARATE task)."
