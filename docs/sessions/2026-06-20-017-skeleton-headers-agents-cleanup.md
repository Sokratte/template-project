<!-- keywords: skeleton files, H1 headers, soft-wrap, AGENTS.md, local.md, gitignore -->
2026-06-20-017-skeleton-headers-agents-cleanup.md

# Session 17 — Skeleton file headers, AGENTS.md cleanup, load order fix

**Goal:** Remove echo markers from startup loader by making skeleton files self-identifying via H1 headers; clean up AGENTS.md hard line breaks and stale LOCAL.md references.

## What was done

**Load order fix (claude.ai project settings):** Discussed why the session-start loader was inconsistently executed — root cause was the U-curve position of `## Startup` in AGENTS.md: it landed in the middle of the total context load because LOCAL.md and projects_list output followed it. Fix: reordered the exec call in claude.ai project settings so AGENTS.md loads last, putting `## Startup` in the strongest recency slot. No file edit required.

**Echo marker removal via H1 convention:** Decided to remove `echo "=== FILE ==="` markers from the startup bash command. Replacement: every skeleton file now opens with `# File Name · soft: N · hard: M` (H1 heading), which serves as an unambiguous file-boundary marker when files are concatenated. HTML comments removed; format instructions kept as one-line prose immediately after the H1 where needed. Applied to: `AGENTS.override.md`, `agents/rules/personal.md`, `agents/memory/procedural.md`, `agents/notes/scratchpad.md`, `agents/notes/work-backlog.md`, `agents/commands/session-start.md`.

**`agents/rules/README.md` rewritten:** Documents two-file scope (`project.md` committed, `personal.md` person-bound), replaces stale `global.md` reference, explains the routing test for where a rule belongs.

**`agents/rules/project.md` stripped to skeleton:** All embedded meta-commentary removed; only H1 and `## Rules` placeholder remain.

**`agents/rules/personal.md` gitignored:** Person-bound file added to `.gitignore` — same rationale as the old `LOCAL.md`.

**`agents/rules/personal.md` cleaned up:** New H1 with limits, two hard line breaks fixed in `## Operator rules`, empty `## Notes` section removed.

**`~/projects/AGENTS.md` (global):** Hard line breaks removed in principles 1–3, Documents section, Git Staging paragraph. Content unchanged.

**`agents/commands/session-start.md`:** `LOCAL.md` reference updated to `LOCAL.md` in step 1.

## Open / carry-forward

- [ ] `agents/commands/session-end.md` step 5 still references `LOCAL.md` — update to `LOCAL.md`
- [ ] CREATE_PROJECT.md: persona step, work-backlog/log table, LOCAL.md doku
- [ ] Canonical `~/projects/AGENTS.md` authoren (PLAN-002 main deliverable)
- [ ] Ripple-edit older session logs 02–11 to new line-1 format
- [ ] README doc pass: docs/*/READMEs, src/, tools/ bare-scaffold READMEs
- [ ] Soft-wrap fix (option A): skeleton files done this session — templates/ still pending

## Git
cec11a5 · Status: clean
