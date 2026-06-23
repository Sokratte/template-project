<!-- kw: PLAN-001, PLAN-002, session-end, README, projects_list.sh, doc format, soft-wrap -->
2026-06-20-016-line1-standardisation-session-end-mcp.md

# Session 16 — Doc format pass, session-end overhaul, README rewrite

**Goal:** Bring PLAN-001/002 to the new doc standard; overhaul session-end.md; fix README.md.

## What was done

**projects_list.sh:** `recent_sessions.sh` was missing from disk. Rather than creating it as a second script, its logic (3 most-recent session log project names) was inlined into `projects_list.sh`, which already prints the project list. `recent_sessions.sh` was briefly created and then deleted; `projects_list.sh` now does both jobs in one script.

**PLAN-001 + PLAN-002 reformatted** to the new doc standard: line-1 `filename | keywords`, `**Status:**` field, `**Created:** · **Updated:**` on one line, soft-wrap throughout (no hard line breaks in prose), `---` separators removed from abstract area (would break awk abstract read), section names normalised (`## Decisions locked`, `## Execution checklist`). Verified with `awk '/^## /{exit} 1'` — abstracts terminate correctly.

**PLAN-002 checklist updated** against actual disk state: SPEC-003 §8.1 follow-up, session-start.md, agents/README.md, procedural.md, operational.md, sweep-knowledge.py, .gitignore, abstract convention, awk three-moves, session-start.md AC — all marked done. Still open: session-end.md reconcile (done this session), CREATE_PROJECT.md, canonical AGENTS.md authoring.

**README.md rewritten:** removed all stale references (.claude/, Obsidian, ~/workspace/, ADR-000, daily-digest.md, GitHub Issues table row). Now reflects the actual architecture: AGENTS.md sync model, OPERATOR.md, CREATE_PROJECT.md, correct directory tree.

**session-end.md overhauled** in two passes: (1) removed prune-at-red step (covered by AGENTS.md file-limits on every read), all `§10`/`ADR-002` dead references, and operational.md over-explanation; (2) collapsed git step — rules already in AGENTS.md, session-end only needs the call-to-action.

**session-end.md restructured (this pass):** steps renumbered cleanly 1–8 (Specs → CHANGELOG → Session log → Work ledger → Memory → Scratchpad → Commit/push → Report); Scratchpad moved to last — the "what remains" step, filled only after ledger/memory have drained matured items. Added a per-step report model: each step emits one line, mark-first (`✓` clean / `✗` needs attention); steps 1–6 are criterion-based, each naming a `*Flag if:*` threshold; steps 7–8 unconditional ("always"). Bottom checklist removed (duplicated the eight steps). Intro trimmed to two sentences. Ordering rationale: memory artefacts describe end-of-session state, so they follow content artefacts; scratchpad last to honour write-first-delete-second.

**SPEC-002 found untracked:** `docs/specs/SPEC-002-dev-mcp-server.md` (Active, project-scoped dev MCP server, 5 tools) sits untracked — belongs to this session's MCP thread but was never committed. Committed separately from the session-end.md change.

## Open / carry-forward

- [ ] CREATE_PROJECT.md: persona step, work-backlog/log table, OPERATOR.md doku
- [ ] Canonical `~/projects/AGENTS.md` authoren (PLAN-002 main deliverable)
- [ ] Ripple-edit older session logs 02–11 to new line-1 format
- [ ] README doc pass: docs/*/READMEs, src/, tools/ bare-scaffold READMEs
- [ ] Soft-wrap fix (option A): convert remaining templates + skeleton files
- [ ] `template-project/README.md` stale note resolved this session ✔

## Git

Commits: 1128eb2 · 2f19f14 · 8fdfc45 · c7be46f · f5498a2 · Status: clean
