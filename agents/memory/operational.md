<!-- Gotchas, grepped only when stuck — see README. Group under a `## heading`; add as `- surprising fix [2026-06-18 x1]`; each time one proves useful, set today's date and raise the xN count by one. -->

## Tooling

- Sandbox tools (`str_replace`, `create_file`, `view`, `bash_tool`) operate on the agent sandbox, NOT the operator's real filesystem — they fail or silently mislead on project files. Use the filesystem MCP tools (`filesystem:read_text_file`, `filesystem:write_file`, etc.) for all project work. `bash_tool` also cannot reach the real FS, so no grep/git from there. [2026-06-18 x2]
- Partial edits ARE possible: `filesystem:edit_file` does line-based old/new replacements and returns a diff — use it for surgical changes. `filesystem:write_file` overwrites the whole file; reserve it for new files or full rewrites. [2026-06-18 x1]
- maisig-auditor MCP tools are scoped to a different repo (`/srv/mcp/maisig/`) and cannot read `/Users/...`; never use them for workspace files. [2026-06-18 x1]
