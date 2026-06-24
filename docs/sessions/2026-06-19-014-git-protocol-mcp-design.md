<!-- file: 2026-06-19-014-git-protocol-mcp-design.md · keywords: git protocol, read-before-write, MCP server design, file integrity, CAS, overwrite guard, git rules consolidation, AGENTS.md merge, anchor edit, atomic write, temp-rename -->

# Session 14 — Git protocol + MCP write-tool design

**Status:** Done
**Created:** 2026-06-19
**Updated:** 2026-06-19

## Goal

Design the canonical read/write protocol for MCP file tools, covering integrity
guarantees before and after writes. Consolidate git rules into their final
canonical home. Capture the ideal-MCP-server design as a research document.

## What was done

**Startup design discussion (no files changed).** Decided the session-start load
should drop the git-state check and the last-session-log read; both are lazy /
on-demand, not startup steps. Concluded the scratchpad carry-forward stays as the
cross-session bridge (robust against aborted sessions and parallel module work),
session logs are pure history (grepped on demand, never loaded at start), and
forward-looking work items live in work-backlog.md, not the carry-forward.

**MCP file-tool design → research doc.** Wrote docs/research/2026-06-19-mcp-file-tool-design.md.
Core decisions:
- Four tools: read_file (returns content + SHA-256 hash + line count), create_file
  (fails if exists, auto-creates parent dirs), edit_file (anchor old→new, the anchor
  IS the integrity check), overwrite_file (mandatory internal git-diff guard, optional
  CAS via expected_hash).
- The git-diff guard is the primary protection against lost-update of uncommitted
  changes — chosen over CAS because an agent that re-reads to refresh its plan
  silently invalidates a CAS token. git does NOT watch the filesystem; it only sees
  content at add/commit, so a post-write git diff is structurally blind to an
  overwritten uncommitted version. Hence the guard must run BEFORE the write.
- Atomic write primitive: temp file + fsync + POSIX rename. Protects against partial
  write / corruption when the process dies mid-write (no OS error is raised if the
  caller process itself dies).
- Diff returned in every write result (cannot be forgotten, saves a call), bounded
  to 200 lines to prevent context balloon.

**Git rules consolidated.** Merged agents/rules/global.md into the canonical
~/projects/AGENTS.md (universal craft: read-before-write, anchor-default, diff-verify,
explicit add paths, no force-push, no hard-delete → .trash, index-lock handling, push
governed by override). Moved global.md to .trash/. Reversed the earlier pointer-pattern
"thin AGENTS.md" stance deliberately: craft rules are loaded every session regardless,
so a pointer saves nothing.

**Override slimmed.** AGENTS.override.md reduced to the four settings (name, persona,
autonomy, push). All conventions/anti-patterns moved to OPERATOR.md (per-VM, private),
plus added platform line "MacBook Pro, macOS, Apple Silicon".

**operational.md** gained a `## Git recovery` section (git bisect, git checkout <file>).

**session-start.md** updated: removed the git-state step and the last-session-log step;
added the Abschluss-Signal trigger (closing words → ask once → run session-end).

## Findings surfaced

- git does not run a background watcher; uncommitted hand-edits leave no recoverable
  prior state in git → pre-write guard is mandatory, post-write diff insufficient.
- Stale memory note corrected in understanding: git CAN run via macbook-mcp:exec
  (the old "git cannot be executed remotely, hand off git add commands" rule is
  obsolete on this VM — left for a future memory pass to formally retire).
- macbook-mcp toolset has no edit_file/anchor tool yet (only write_file/read_file/exec)
  — this is exactly why the MCP-server build task was filed.

## State at close

All work committed and pushed (b234591..e9626d3). Tree clean.

Next session should open: session-start.md / session-end.md reconciliation
(backlog item) — the Abschluss-Signal was added but the two command files still
need a full alignment pass against the session-14 decisions, plus session-end
still references the old git-check flow. Also pending: AGENTS.md redundancy review
(merged content not yet tightened), and the stale template-project/README.md
(describes .claude/, ~/workspace/, Obsidian — a separate flagged bug, not yet filed).
