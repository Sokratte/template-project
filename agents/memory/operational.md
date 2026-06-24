# Operational Memory · no size limit · grep when stuck — the section headers below are the index

<!-- What the agent KNOWS: gotchas + rules demoted from procedural. Grepped, never auto-loaded — see README. File under a keyworded `## heading`; add the entry's distinctive terms to that heading. Entry: `- surprising fix [sNN xM]` (born session NN, useful M times). On recall, bump M. No pruning here; operational is the floor. -->

## Tooling · keywords: macbook-mcp, maisig-auditor scope, python heredoc edits, str.replace assert count, python3 stdin heredoc, python3 dash heredoc, write_file timeout hang

- maisig-auditor MCP tools are scoped to a different repo (`/srv/mcp/maisig/`) and cannot read `/Users/...`; never use them for workspace files. [s18 x1]
- Surgical multi-section Markdown edits on the real FS: `macbook-mcp:write_file` overwrites whole files and there is no anchor-edit tool, so for multi-block edits run `python3` via `exec` heredoc (`<<'PYEOF'`) doing `str.replace` with `assert s.count(old)==1` per block — the assertion catches a stale/changed anchor before it silently misfires; more reliable than `sed` for multi-line patterns. [s18 x2]
- `python3 /dev/stdin << 'PYEOF'` does NOT work reliably in `macbook-mcp:exec` — the heredoc is consumed by bash before Python reads it, producing silent no-ops. Use `macbook-mcp:write_file` to write the script to `tools/_tmp.py`, then `macbook-mcp:exec` `python3 tools/_tmp.py`, then delete the file. [s27 x1]
- `python3 - << 'PYEOF'` (dash form, stdin) DOES run reliably in `macbook-mcp:exec` — used repeatedly this session for multi-block `str.replace` edits. The s27 failure was specific to the `/dev/stdin` path form, not heredoc-to-python as such; prefer `python3 - <<` over the tmp.py dance. [s30 x1]
- `macbook-mcp:write_file` (and occasionally `:exec`) can hang ~4 min and return "unresponsive"; the write may or may not have landed. Fall back to an `exec` heredoc (`cat > f << 'EOF'`), and always re-check the FS state before retrying so you neither double-write nor assume a no-op. [s30 x1]

## Git recovery · keywords: git bisect, git checkout file, discard uncommitted changes, find bad commit, gitignored mv shows as delete, trash

- **`git bisect`** — finds the commit that introduced a bug by binary-searching history. Run `git bisect start`, mark a known-bad commit with `git bisect bad`, a known-good one with `git bisect good <hash>`, then test each revision git checks out until it isolates the culprit. Useful when a bug appeared "somewhere in the last N commits" and you cannot tell where. [s18 x1]
- **`git checkout <file>`** — discards all uncommitted working-tree changes to a specific file and restores the last committed version. Safer than manual revert when a change went wrong. Example: `git checkout agents/notes/scratchpad.md`. [s18 x1]
- A `mv` into a gitignored dir (e.g. `.trash/`) shows in `git status` as ` D path` (delete) even though the file is preserved on disk — git only sees it leave the tracked tree. Not data loss; stage the `D` to record the de-versioning. [s30 x1]
