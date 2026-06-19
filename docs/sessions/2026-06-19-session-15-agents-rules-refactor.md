2026-06-19-session-15-agents-rules-refactor.md | AGENTS.md refactor, four principles Karpathy, workflow consolidation, file limits soft hard, words not tokens, startup index, lost in the middle, recency, doc-type caps, v2 files, soft-wrap

# 2026-06-19 · template-project · session 15 — AGENTS.md + session-start refactor (v2)

**Status:** open — v2 drafts written, awaiting operator review; AGENTS.md proper deferred to session 16.

## Goal

Overhaul AGENTS.md and rules: kill redundancy below the four principles, consolidate the scattered workflow descriptions, settle the file-size-governance mechanism. Work captured in `-v2` files; originals untouched on operator's instruction.

## What was decided

**Four principles kept (Karpathy-style).** "Think before acting / Simplicity first / Surgical changes / Goal-driven execution" pulled to the top under `## How you work`, renumbered 1–4. Workflow and Laws now reference them instead of repeating. (Side note: attributed to Karpathy in conversation, but he is OpenAI/Tesla, not Anthropic — attribution not verified, irrelevant to keeping them.)

**Workflow consolidated.** The old 6-step `## Workflow` collapsed to a 3-step `## Task workflow` = Spec → Plan → Build → Test. *Orient* and *Wrap up* removed from the per-task loop — they are per-session, living in session-start/-end. This resolved the operator's "overlap with session-start" inline comment.

**Deletions (operator-approved):** Quality-standards #3 "Surface assumptions" (dup of principle 1); Workflow step-2 multi-step-plan sentence (dup of principle 4); Goal-driven verify-block; the `### More rules — to be reviewed ###` separator. Workflow steps Orient/Prepare/Wrap-up removed.

**File-size governance — redesigned (the session's main structural win).** The old `## Skeleton` section (token thresholds in OPERATOR.md, yellow/red, a startup scan over a file list) is replaced by `## File limits`:
- A file that should not grow unbounded declares its own limits in **line 1**, in **words** (e.g. `soft limit: 600 · hard limit: 1200`).
- **Words, not tokens** — a file cannot know the reader's tokenizer; word count is model-independent. The ×1.3 factor and per-number reasoning stay in the context-budget research doc. A different model derives different word limits through the same mechanism → portable.
- **soft/hard** replaces yellow/red (more established terms).
- The check is a **property of reading**, not a startup step: the MCP returns word count on every read; over soft → inform; over hard → stop and force prune-or-defer. No list of governed files, no scan, no "skeleton" vocabulary. This dropped session-start step 3 entirely.

**Startup index — added.** New session-start step: read line 1 (`filename | keywords`) of every doc, as the **last** startup step so it sits in the recency zone just before the operator's first instruction. Backed by a web-research pass on Lost-in-the-Middle (Liu et al. 2024; Veseli et al. 2025 on window-size-dependent primacy/recency): loading at startup-end is the reliable position, and the operator's instruction keeps the very-last recency slot. Caveat: studies measure *retrieval*, not *instruction-following* — transfer is plausible but an analogy, ~P75.
- **Per-doc-type caps** to keep the index bounded: all decisions/specs/plans; last 10 research; last 5 sessions. ~660 tokens, fits the ~600-token post-skeleton buffer. Rationale: sessions need only continuity (5), research the current landscape (10), forward-looking docs are few and always relevant. Caps apply to the auto-scan only; older docs remain reachable by targeted read.

## What was changed (files)

- `~/projects/AGENTS-v2.md` — full v2 draft. NB: lives on `~/projects/` root, which is **not** a git repo (manually backed up), so it will not appear in `git status` / commits.
- `agents/commands/session-start-v2.md` — v2 draft: 4 steps, skeleton-check removed, startup index added as final step, memory-check reworded to silent/background, log-scaffold reworded to "during, not retrospective".
- `docs/research/2026-06-19-context-budget-and-file-limits.md` — appended `## Startup index budget` section (the per-doc-type cap table). This is a real edit to a tracked file.

## Open / next session

- **AGENTS.md proper** — apply the v2 design to the real canonical file (operator wants to do this next session, after reviewing v2).
- **Backlog items filed this session** (see work-backlog): soft-wrap template fix (option A); MCP returns word count on read/write.
- **Soft-wrap still unsolved at the behavioural level** — even this session, several files were first written hard-wrapped. The v2 session-start was rewritten soft-wrapped; AGENTS-v2 file-limits block is soft-wrapped. But the root fix (templates) is not done. This is exactly backlog item A.
- **`soft limit` line-1 convention not yet applied** to any actual skeleton file — the mechanism is defined in AGENTS-v2 but no file carries the line-1 limit yet. Apply when AGENTS.md goes live.

## Process note (self-critique)

The session log scaffold was NOT created at session start — it was written retrospectively at session end, the exact anti-pattern we tightened in session-start-v2 this same session. Flag for next time: scaffold first.

## State at close

v2 drafts complete and verified on disk. Originals (`~/projects/AGENTS.md`, `session-start.md`) deliberately untouched. Research doc edited. Ready for operator review of v2, then promotion to canonical in session 16.
