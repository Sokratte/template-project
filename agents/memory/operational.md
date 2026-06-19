<!-- Gotchas, grepped only when stuck — see README. Group under a `## heading`; add as `- surprising fix [2026-06-18 x1]`; each time one proves useful, set today's date and raise the xN count by one. -->

## Tooling

- Sandbox tools (`str_replace`, `create_file`, `view`, `bash_tool`) operate on the agent sandbox, NOT the operator's real filesystem — they fail or silently mislead on project files. Use the filesystem MCP tools (`filesystem:read_text_file`, `filesystem:write_file`, etc.) for all project work. `bash_tool` also cannot reach the real FS, so no grep/git from there. [2026-06-18 x2]
- Partial edits ARE possible: `filesystem:edit_file` does line-based old/new replacements and returns a diff — use it for surgical changes. `filesystem:write_file` overwrites the whole file; reserve it for new files or full rewrites. [2026-06-18 x1]
- maisig-auditor MCP tools are scoped to a different repo (`/srv/mcp/maisig/`) and cannot read `/Users/...`; never use them for workspace files. [2026-06-18 x1]

## Git recovery

- **`git bisect`** — finds the commit that introduced a bug by binary-searching history. Run `git bisect start`, mark a known-bad commit with `git bisect bad`, a known-good one with `git bisect good <hash>`, then test each revision git checks out until it isolates the culprit. Useful when a bug appeared "somewhere in the last N commits" and you cannot tell where. [2026-06-19 x1]
- **`git checkout <file>`** — discards all uncommitted working-tree changes to a specific file and restores the last committed version. Safer than manual revert when a change went wrong. Example: `git checkout agents/notes/scratchpad.md`. [2026-06-19 x1]
