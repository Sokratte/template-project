# Work Backlog
<!-- soft: 500 · hard: 1000 -->

One line per item: `YYYY-MM-DD | MODULE | [TAG] | description | file-ref`; TAG is `[OPEN]`, `[ACTIVE]`, or `[FIND]`. When done, move the line to `work-log.md`. Alarm if over 20 items.

2026-06-20 | INFRA      | [OPEN]    | MCP server tool ordering: order exec first in registry response (primary tool), then git, then read/write/search/list (convenience wrappers). Ensures exec loads on generic tool_search, avoids second search when operator provides argv. | MCP server
2026-06-18 | DOCS       | [OPEN]    | Finish README documentation pass: docs/* READMEs (specs, plans, sessions, decisions, research — structure/convention only, NOT per-file listings) and bare-scaffold READMEs (src/, docs/tests/, tools/). agents/ is done. | docs/, src/, tools/
2026-06-18 | DOCS       | [OPEN]    | Ripple-edit remaining docs to new line-1 format + abstract convention: session logs 02-11 (01 may stay short). ADRs, SPECs, research doc done session 13. | docs/sessions/
2026-06-19 | INFRA      | [OPEN]    | Design and build ideal MCP server: write tools (create_file, edit_file/anchor, overwrite_file/git-diff-guard+CAS), read_file with hash, atomic write (temp+rename), diff-in-result with size cap, auto parent-dir creation. Research doc: docs/research/2026-06-19-mcp-file-tool-design.md | -
2026-06-19 | DOCS       | [OPEN]    | Soft-wrap fix (option A): convert all templates + skeleton files to genuine soft-wrap (no hard line breaks mid-paragraph), so the agent imitates the right pattern. Root cause of the never-working soft-wrap rule is hard-wrapped examples, not weak wording. Option B (MCP rejects mid-paragraph \n) deferred. | templates/, agents/, docs/
2026-06-19 | INFRA      | [OPEN]    | MCP file tools return word count on every read/write (len(content.split())) — feeds the soft/hard line-1 file-limit check in AGENTS.md. Cheap: content is already in hand. Words chosen over bytes (closer to tokens, model-independent). | MCP server
2026-06-23 | MEMORY     | [OPEN]    | Revisit memory baselines: operational soft/hard 500/1000 words, promotion proof M>=3, cutoff 0.01. No practice data yet. Revisit at session 030. | agents/memory/

