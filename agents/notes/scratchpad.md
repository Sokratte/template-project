<!-- Working space, checked every session — see README. Carry-forward (top): what the next session must know, kept tight. Working space (below the line): live threads, pruned at session end. Size governed by the traffic-light (SPEC-003 §10, ADR-002). -->

## Carry-forward

- AGENTS.md overhaul is drafted as `~/projects/AGENTS-v2.md` (NOT yet promoted to canonical — operator reviews first, then session 16 applies it). Same for `agents/commands/session-start-v2.md`. Originals untouched on purpose. NEXT SESSION = promote v2 → canonical.
- File-size governance was redesigned this session: limit lives in **line 1** of each governed file, in **words**, as `soft limit: N · hard limit: M`. Check happens on every read (MCP returns word count), not as a startup scan. No file list, no "skeleton" vocabulary. Defined in AGENTS-v2 `## File limits` — but NOT yet applied to any real file's line 1. Apply when v2 goes live.
- Startup index added to session-start-v2 as the LAST step (recency position; see research doc `## Startup index budget`). Caps: all decisions/specs/plans, last 10 research, last 5 sessions.
- Git rules + universal craft live ONLY in canonical `~/projects/AGENTS.md`. File read/write protocol + MCP-server design settled — see docs/research/2026-06-19-mcp-file-tool-design.md. Point to it, don't restate.
- Still open (backlog): session-end.md reconcile against session-14 decisions (it was executed this session but not yet rewritten); `template-project/README.md` is stale (.claude/, ~/workspace/, Obsidian, ADR-000) — still not filed as its own backlog line; README doc pass (docs/* per-dir READMEs, bare-scaffold READMEs); PLAN-001/002 still old format; **macbook-mcp `exec` output: revisit `truncated` flag vs. `output_length`** — current flag signals file-completeness but creates confusion when response is truncated in chat context; should clarify with byte/char count or alternative signal to prevent future misreadings.
- Pattern: skeleton files keep ONE self-explanatory comment line; explanation lives in the per-directory README. Soft-wrap everywhere; data lines one-per-record.

---

## Working space
