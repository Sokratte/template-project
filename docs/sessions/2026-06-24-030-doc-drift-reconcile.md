<!-- file: 2026-06-24-030-doc-drift-reconcile.md · keywords: session, spec-003, session-start, readme, causal chain, documentation drift, audit follow-up, spec retirement, content transfer -->

# Session 030 — Documentation drift reconciliation

**Status:** Completed
**Goal:** Resolve two doc-drift issues from the Session 029 audit; this expanded into retiring SPEC-003 and rehoming its exclusive content.

## What was accomplished

**Task 1 — SPEC-003 §9.1 vs session-start.md drift.** Resolved by deciding session-start.md is authoritative (the lean executable form). SPEC-003 §9.1 was first rewritten to match reality, then SPEC-003 was retired entirely (see below).

**Task 2 — agents/commands/README.md causal chain.** "Triggered by" cell for session-start.md corrected: was "the exec-2 startup call … loads this file; the agent then executes its steps" (causally wrong); now "Loaded into context by exec-2; execution is triggered by the session-setup instruction in the system prompt."

**SPEC-003 retired.** Audit found SPEC-003 (12 sections, ~3560 words) was almost entirely re-described elsewhere. Initial judgement ("no exclusive content") was WRONG — made from an incomplete read (only §1–§9 seen; §10/§11/§12 never read). Corrected after full re-read. Moved to `.trash/` (not git-deleted from disk; git sees it as D because `.trash/` is gitignored). Exclusive content rehomed per operator decision:
- §4 (AGENTS.md anchor) + §11 (git automation) + §2 core (why file-based) → `~/projects/README.md` (+ `VM.local/README.md` mirror).
- §9 (session lifecycle) + §10 (document size governance) → `template-project/README.md`.
- §12 (adapting to new project) — already covered by `CREATE_PROJECT.md`; no transfer.
- §3/§5–§8 — already live in CREATE_PROJECT / agents READMEs.

**Reference cleanup.** All living SPEC-003 refs deleted or repointed: ADR-002 (×4), CREATE_PROJECT (×2), agents/README.md (block removed), agents/memory/README.md, docs/README.md (×2 example paths), PLAN-001:78. PLAN-002 refs removed by operator. History (sessions, work-log, CHANGELOG) intentionally untouched.

**Bonus fix.** `~/projects/README.md` was still on `OPERATOR.md` (the OPERATOR→LOCAL rename had reached the VM.local mirror but never the live file). Pulled live onto mirror state; both now identical and on `LOCAL.md`.

## Open / carry-forward

- [ ] `~/projects/README.md` exec-1 still describes `recent_sessions.sh` + `agents_sync.sh`; reality uses `projects_list.sh`. Pre-existing drift, not touched this session. → backlog.
- [ ] `recent_sessions.sh` vs `projects_list.sh` naming inconsistency across workspace docs.
- [x] SPEC-003 drift + README causal chain (this session).

## Git

One commit: SPEC-003 retirement + content transfer + ref cleanup + Task 2. Push: on.
