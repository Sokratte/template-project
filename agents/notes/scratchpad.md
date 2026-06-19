<!-- Working space, checked every session — see README. Carry-forward (top): what the next session must know, kept tight. Working space (below the line): live threads, pruned at session end. Size governed by the traffic-light (SPEC-003 §10, ADR-002). -->

## Carry-forward

- Git rules + universal craft now live ONLY in canonical `~/projects/AGENTS.md` (global.md was merged in and trashed). The file read/write protocol and the MCP-server design are settled — see docs/research/2026-06-19-mcp-file-tool-design.md. Do not restate the protocol elsewhere; point to it.
- NEXT (filed in backlog): reconcile session-start.md + session-end.md against session-14 decisions. session-start is partly done (git-step and last-log-step removed, Abschluss-Signal added) but session-end.md still references the old git-check flow and needs the same alignment. This is the natural next task.
- Also open (backlog): AGENTS.md redundancy review — the merged content works but was not yet tightened for overlap. And `template-project/README.md` is stale (describes .claude/, ~/workspace/, Obsidian, ADR-000 templates) — a real bug, not yet filed as a backlog line; file it when picked up.
- README documentation pass: `agents/` fully complete; `docs/README.md` written (doc-format source of truth). Remaining: `docs/*` per-directory READMEs (structure/convention only, NOT per-file listings) and bare-scaffold READMEs (src/, docs/tests/, tools/).
- Pattern to follow: skeleton files keep ONE self-explanatory comment line; explanation lives in the per-directory README (READMEs may be long). Soft-wrap everywhere; data lines one-per-record.
- PLAN-001/PLAN-002 still in the old doc format (backlog item). Mechanical, not urgent.

---

## Working space
