<!-- Working space, checked every session — see README. Carry-forward (top): what the next session must know, kept tight. Working space (below the line): live threads, pruned at session end. -->

## Carry-forward

- File-size governance: limit lives in **line 1** of each governed file, in **words**, as `soft limit: N · hard limit: M`. Check on every read. Not yet applied to any real file's line 1 — still pending.
- Git rules + universal craft live ONLY in canonical `~/projects/AGENTS.md`. File read/write protocol + MCP-server design settled — see docs/research/2026-06-19-mcp-file-tool-design.md.
- Pattern: skeleton files keep ONE self-explanatory comment line; explanation lives in the per-directory README. Soft-wrap everywhere; data lines one-per-record.
- **macbook-mcp `exec` output:** revisit `truncated` flag vs. `output_length` — current flag signals file-completeness but creates confusion when response is truncated in chat context; clarify with byte/char count or alternative signal.

---

## Working space
