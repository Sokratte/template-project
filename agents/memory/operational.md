# Operational Memory · no size limit · grep when stuck — the section headers below are the index

<!-- What the agent KNOWS: gotchas + rules demoted from procedural. Grepped, never auto-loaded — see README. File under a keyworded `## heading`; add the entry's distinctive terms to that heading. Entry: `- surprising fix [sNN xM]` (born session NN, useful M times). On recall, bump M. No pruning here; operational is the floor. -->

## Tooling · keywords: sandbox tools, real filesystem, filesystem MCP, bash_tool, maisig-auditor scope, python heredoc edits, str.replace assert count, write_file temp script

- Sandbox tools (`str_replace`, `create_file`, `view`, `bash_tool`) operate on the agent sandbox, NOT the operator's real filesystem — they fail or silently mislead on project files. Use the filesystem MCP tools (`filesystem:read_text_file`, `filesystem:write_file`, etc.) for all project work. `bash_tool` also cannot reach the real FS, so no grep/git from there. [s18 x1]
- Partial edits ARE possible: `filesystem:edit_file` does line-based old/new replacements and returns a diff — use it for surgical changes. `filesystem:write_file` overwrites the whole file; reserve it for new files or full rewrites. [s18 x1]
- maisig-auditor MCP tools are scoped to a different repo (`/srv/mcp/maisig/`) and cannot read `/Users/...`; never use them for workspace files. [s18 x1]
- Surgical multi-section Markdown edits on the real FS: `macbook-mcp:write_file` overwrites whole files and there is no anchor-edit tool, so for multi-block edits run `python3` via `exec` heredoc (`<<'PYEOF'`) doing `str.replace` with `assert s.count(old)==1` per block — the assertion catches a stale/changed anchor before it silently misfires; more reliable than `sed` for multi-line patterns. [s18 x1]
- `python3 /dev/stdin << 'PYEOF'` does NOT work reliably in `macbook-mcp:exec` — the heredoc is consumed by bash before Python reads it, producing silent no-ops. Use `macbook-mcp:write_file` to write the script to `tools/_tmp.py`, then `macbook-mcp:exec` `python3 tools/_tmp.py`, then delete the file. [s27 x1]

## Git recovery · keywords: git bisect, git checkout file, discard uncommitted changes, find bad commit

- **`git bisect`** — finds the commit that introduced a bug by binary-searching history. Run `git bisect start`, mark a known-bad commit with `git bisect bad`, a known-good one with `git bisect good <hash>`, then test each revision git checks out until it isolates the culprit. Useful when a bug appeared "somewhere in the last N commits" and you cannot tell where. [s18 x1]
- **`git checkout <file>`** — discards all uncommitted working-tree changes to a specific file and restores the last committed version. Safer than manual revert when a change went wrong. Example: `git checkout agents/notes/scratchpad.md`. [s18 x1]
