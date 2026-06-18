<!-- Gotchas, grepped only when stuck — see README. Group under a `## heading`; add as `- surprising fix [2026-06-18 x1]`; each time one proves useful, set today's date and raise the xN count by one. -->

## Tooling

- Sandbox tools (`str_replace`, `create_file`, `view`, `bash_tool`) operate on the agent sandbox, NOT the operator's real filesystem — they fail or silently mislead on project files. Use the filesystem MCP tools (`filesystem:read_text_file`, `filesystem:write_file`, etc.) for all project work. `bash_tool` also cannot reach the real FS, so no grep/git from there. [2026-06-18 x1]
- `filesystem:write_file` overwrites whole files; there is no partial-edit MCP tool. To change one line, read the file first, then rewrite it complete. [2026-06-18 x1]
