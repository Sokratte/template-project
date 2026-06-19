2026-06-19-mcp-file-tool-design.md | MCP server, file tools, read-before-write, create, anchor-edit, overwrite, CAS, git-diff guard, atomic write, temp-rename, integrity, lost update, silent no-op, partial write

# MCP File Tool Design — Read/Write Protocol

**Status:** Draft
**Created:** 2026-06-19
**Updated:** 2026-06-19

This document specifies the ideal MCP file-tool interface for agent-assisted
development. It covers the integrity model, the four file tools, the atomic
write primitive, output bounds, and the agent-side protocol — including
considered alternatives and the reasoning for rejection.

## 1. The Problem Space

An agent edits files in a shared working directory. Other writers exist:
the operator editing by hand in a terminal or editor, other agent sessions,
background processes. Git tracks committed history but not uncommitted
working-tree changes. Four failure modes must be closed.

**Lost Update — uncommitted:** Agent reads F at time T. Operator modifies F
at T+5min without committing. Agent writes F at T+10min based on the T reading.
The operator's changes are silently overwritten. `git diff` after the write
shows only the agent's changes — the operator's uncommitted V1 never existed
in git, so the diff has no reference for it. The loss is structurally invisible
to any post-write check.

**Lost Update — committed:** Same scenario, but the operator's change was
committed between the agent's read and write. The agent's write reinstates the
pre-commit state. `git diff` after the write shows a revert; detectable in
principle, but the damage is already done and the operator's commit is now
shadowed.

**Silent No-op:** The write tool reports success but nothing was written —
anchor text not found, permission error swallowed, partial MCP response, etc.
The agent proceeds believing the edit landed.

**Partial Write / Corruption:** Process dies between file truncation and write
completion. The file is empty or partial; no error reaches the caller because
the caller process itself may be dead. The OS does not synthesize an error
for a write that was in-progress when the process died.

## 2. Option Analysis

| Option | Lost Update (uncommitted) | Lost Update (committed) | Cost |
|--------|--------------------------|------------------------|------|
| Re-read whole file before write | Only if agent notices diff — unreliable | Only if agent notices | High token cost; relies on attention |
| Re-read only target section | No — misses changes elsewhere | Partial | Medium cost; blind to adjacent changes |
| CAS token (hash on read, check on write) | Yes — if token not refreshed | Yes | No extra calls; **fragile**: re-reading the file silently invalidates the token, disabling the guard |
| **`git diff` guard before overwrite** | **Yes — uncommitted changes are visible** | **Yes** | One internal server call; unconditional; cannot be circumvented by a re-read |
| Anchor-edit (old→new text match) | Yes — anchor mismatch = automatic fail-safe | Yes | No extra calls; self-enforcing by construction |

**Conclusion:** Anchor-edit is the correct default for surgical changes — the
anchor is simultaneously the integrity check, with no extra mechanism required.
Full overwrite of an existing file requires a `git diff` guard run internally
by the server before writing; it is unconditional and cannot be bypassed by
the agent refreshing its read. CAS is retained only as a secondary guard
against concurrent MCP-session races (two agents targeting the same file
simultaneously); it is not sufficient as the primary mechanism.

## 3. The Four File Tools

### 3.1 `read_file`

**Signature:** `read_file(path, start_line?, end_line?) → {content, hash, line_count}`

Returns the file content, a SHA-256 of the on-disk bytes at read time, and
the total line count. `start_line` / `end_line` (1-based, inclusive) enable
partial reads without loading the full file. The hash is informational — it
lets the caller detect that a file has changed between two reads without an
extra round-trip. It is not enforced by the write tools; the git-diff guard
and the anchor are the enforcement mechanisms.

Returns a clear error if the file does not exist. Never returns empty silently.

### 3.2 `create_file`

**Signature:** `create_file(path, content) → {path, bytes_written, diff}`

Precondition: the file must NOT exist. Fails with a clear error if it does —
use `overwrite_file` for intentional replacement of an existing file. This
hard split prevents accidental overwrites by omission of a flag.

Behaviour: creates all missing parent directories automatically (no separate
mkdir call required). Writes via temp file + atomic rename (§5). Returns a
unified diff of `∅ → content`, bounded per §6.

**Rejected alternative — single write tool with mode flag:** Rejected because
distinct tool names make the agent's intent explicit in the call log and prevent
accidental overwrite by a missing argument.

### 3.3 `edit_file` (anchor edit)

**Signature:** `edit_file(path, old_text, new_text) → {path, diff}`

Precondition: `old_text` must appear exactly once in the current file content.

Behaviour: reads the file, locates `old_text` exactly once, replaces it with
`new_text`, writes via temp + rename. Returns a unified diff, bounded per §6.

Failure modes — both are hard errors, not warnings:
- `old_text` not found → file has changed since the agent's read. Agent must
  re-read and reformulate the anchor. Do not retry with a looser anchor.
- `old_text` found more than once → anchor is ambiguous. Agent must use a
  longer, unique anchor string.

Why anchor-edit is the default: the anchor is simultaneously the integrity
check. If anyone has modified the target section since the agent last read it,
the anchor will not match and the write is aborted automatically. No separate
pre-write check is needed; the tool's own precondition enforces it.

**Rejected alternative — line-number-based edit:** Rejected because line
numbers shift when anyone inserts or deletes lines above the target. An anchor
on the actual content is stable in a way line numbers are not.

### 3.4 `overwrite_file`

**Signature:** `overwrite_file(path, content, expected_hash?) → {path, bytes_written, diff}`

Precondition: the file MUST exist. Use `create_file` for new files.

Behaviour — executed in this order:

1. **CAS check (optional):** If `expected_hash` is provided, hash the current
   on-disk file. If it differs from `expected_hash`, fail immediately with a
   clear error before touching anything. This catches concurrent MCP-session
   races; it is secondary to the git-diff guard.

2. **Git-diff guard (mandatory):** Run `git diff <path>` internally.
   - Non-empty output → there are uncommitted changes. Fail with a clear error
     that includes the diff. The agent must show this to the operator and
     receive explicit confirmation before any further write attempt. This guard
     cannot be bypassed by the agent re-reading the file, because it compares
     the working tree against git HEAD, not against the agent's last read.
   - Empty output → working tree matches HEAD. Safe to proceed.

3. Write via temp file + atomic rename (§5).

4. Return a unified diff of `old content → new content`, bounded per §6.
   The new on-disk hash is also returned, so the agent can chain writes
   without re-reading.

When to use: intentional full replacement — the new content is generated from
scratch, or the changes are too extensive for anchor-edit to be practical.
Not for surgical changes; use `edit_file` for those.

**Rejected alternative — CAS as primary guard:** Rejected because an agent
that re-reads the file to refresh its working plan will silently update the
hash it holds, disabling the guard. The git-diff guard is unconditional.

## 4. Agent-Side Protocol

These rules govern agent behaviour. They belong in `AGENTS.md` / `global.md`,
not in the server implementation.

- **Default is anchor-edit.** Use `edit_file` for any surgical change.
  Use `overwrite_file` only for intentional full replacement.
  Use `create_file` for files that do not yet exist.
- **Read before writing.** Always read the current state of a file before
  formulating an edit. Do not edit from memory of a read made many turns ago
  in the same session.
- **Treat an anchor miss as a signal, not an obstacle.** The file changed
  since your read. Re-read, understand what changed, reformulate.
- **Treat a git-diff guard failure as a hard stop.** Show the diff to the
  operator. Do not ask permission to override it; ask how to proceed.
- **Verify via the returned diff.** After every write, inspect the diff in
  the tool result. An empty diff means nothing was written — stop, do not
  proceed as if the edit landed.
- **Never use `overwrite_file` on a file you have not read this session.**

## 5. Atomic Write Implementation (server-side)

All three write tools use the same underlying primitive:

```
tmp = path + ".tmp." + random_suffix   # same directory = same filesystem
write(tmp, content)
fsync(tmp)                              # flush OS write buffer to disk
rename(tmp, path)                       # POSIX: atomic on same filesystem
```

POSIX `rename` is atomic within a filesystem: every observer sees either the
complete old file or the complete new file, never a partial state. If the
process dies after `write` but before `rename`, the original file is untouched;
only the `.tmp` file is left behind (recoverable, not corrupt). If the process
dies during `write`, only the `.tmp` is partial — the original is untouched.

Why not rely on OS error returns alone: the OS reports errors in the write call
itself, but if the process is killed between file truncation (which happens
first in a normal `open(O_TRUNC)` + `write` sequence) and write completion,
the caller process is also dead and no error is propagated. A truncated target
with no error is the silent corruption case. Temp + rename eliminates the window
where a kill produces a corrupt target.

## 6. Output Bounds (anti-balloon)

All write tools return a diff in their result. Diffs are bounded to prevent
large writes from inflating the tool-response context:

- Full unified diff if ≤ 200 lines.
- First 200 lines + `[truncated — N lines omitted]` if larger.
- Stat summary only (`N insertions, M deletions`) for diffs > 1000 lines,
  or on explicit request.

If the agent needs the full diff for a large write, it calls `read_file` after
the write and compares explicitly. The agent must not request unbounded output.
