# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- **SPEC-003 retired (session 030):** the agent-memory/session system spec (12 sections, ~3560 words) was almost entirely re-described in the agents READMEs, CREATE_PROJECT, and ADR-002. Moved to `.trash/` (not deleted from disk). Its exclusive content was rehomed: §4 (AGENTS.md anchor) + §11 (git automation) + §2 (why file-based) → `~/projects/README.md` (+ VM.local mirror); §9 (session lifecycle) + §10 (document size governance) → `template-project/README.md`. All living references deleted or repointed (ADR-002, CREATE_PROJECT, agents READMEs, docs/README.md, PLAN-001). `~/projects/README.md` also pulled from stale `OPERATOR.md` onto current `LOCAL.md`.
- **agents/commands/README.md:** corrected the causally-wrong "Triggered by" cell for `session-start.md` — exec-2 loads the file into context; the session-setup instruction in the system prompt triggers execution.

- **Audit fixes (session 029):** `CREATE_PROJECT.md` operational.md budget row corrected to no-limit; `VM.local/README.md` OPERATOR.md → LOCAL.md (6 occurrences); `PLAN-001` checklist updated; `ADR-002` historical.md removed from Content class list; `PLAN-002` session-end.md item checked; `agents/rules/README.md` stale placeholder removed.

- **Line-1 format for all docs changed to HTML comment + bare filename** (`<!-- keywords: keywords -->` on line 1, filename on line 2). Uniform across all doc types; hidden in Markdown renderers, greppable in source. Migrated: ADR-001/002, SPEC-001/002/003, PLAN-001/002, sessions 011-017+019, all research docs. Sessions 001-010 and session-018 grandfathered.
- **`docs/README.md` rewritten** as single source of truth for document conventions: section-level keywords (`<!-- keywords: -->` on every heading), status master vocabulary table with per-type subsets, structural vs. content heading distinction, section matrix (required/optional/n/a per type), implications palette, Design Philosophy (DP) type added, anti-drift rule, `Adding a new doc type` section, all inline templates updated.
- **Skeleton-file soft/hard limits moved from H1 text into HTML comments** (`<!-- soft: N · hard: M -->` on line after H1). Invisible in Obsidian/MkDocs/GitHub, greppable in source. Applies to all 10 skeleton files.
- **`AGENTS.md` file-limits section** updated to document the HTML-comment format.
- **`OPERATOR.md` renamed to `LOCAL.md`** repo-wide (73 replacements across 11 living files: README, CREATE_PROJECT, SPEC-003, PLAN-001/002, agents READMEs, research, scratchpad, backlog, session-017). Historical logs untouched.
- **Stale `global.md` pointer removed** from `agents/README.md` (rules/ table) and `PLAN-002` (three-tier read table); `AGENTS.md` itself was already clean.

### Added

- **`VM.local/`** refreshed: stale copy-files trashed, current `~/projects/` files (`AGENTS.md`, `LOCAL.md`, `README.md`, `agents_sync.sh`, `projects_list.sh`) copied in and committed under correct names.
- **READMEs added** to all scaffold directories missing one: `docs/decisions/`, `docs/specs/`, `docs/plans/`, `docs/sessions/`, `docs/research/`, `docs/philosophy/`, `src/`, `tools/`. Each follows the line-1 `<!-- keywords: -->` + bare-filename convention.
- **Session logs 01-11 converted** to line-1 format (`<!-- keywords: ... -->` + bare filename on line 2).
- **`docs/philosophy/`** directory with `DP-000-template.md` skeleton — Design Philosophy document type now part of the scaffold.
- **Soft/hard word limits added** to all skeleton files that were missing them: `AGENTS.override.md` (150/300), `agents/rules/project.md` (400/800), `agents/commands/session-start.md` (400/600), `ROADMAP.md` (600/1200), `~/projects/AGENTS.md` (1200/2000), `~/projects/LOCAL.md` (200/400).


### Removed

- `agents/memory/historical.md` — removed (moved to `.trash/`); `operational.md` is now the unlimited, section-indexed floor that absorbs demoted and stale knowledge

### Changed

- **Agent memory system redesigned to a two-file autonomous lifecycle** (supersedes the 3-file model; ADR-002 amended). `procedural.md` (loaded, word-limited) and `operational.md` (no limit, section-indexed) self-manage at session end with no operator prompt: entries carry `[sNN xM]`, `value = M / sessions_alive`; proven topic-independent operational entries are promoted to procedural, and procedural entries below `memory_cutoff` (default 0.01) are demoted back when the file exceeds its size limit. Rewrote `agents/memory/README.md`, `agents/commands/session-end.md` §5, `SPEC-003` §8, `CREATE_PROJECT.md`, root `README.md`
- `agents/memory/operational.md`: line-1 declares no size limit; `## headings` carry keyword lists (section index); entry tags migrated to `[sNN xM]`
- `AGENTS.override.md`: added `memory_cutoff` (default 0.01)
- `agents/rules/README.md` rewritten: documents `project.md` (committed) and `personal.md` (person-bound, gitignored); removes stale `global.md` reference
- `agents/rules/project.md` stripped to skeleton: H1 + `## Rules` placeholder only
- All skeleton files (`AGENTS.override.md`, `agents/rules/personal.md`, `agents/memory/procedural.md`, `agents/notes/scratchpad.md`, `agents/notes/work-backlog.md`, `agents/commands/session-start.md`): new H1 headers with word limits where applicable, HTML comments removed, hard line breaks fixed
- `agents/commands/session-start.md`: `OPERATOR.md` reference updated to `LOCAL.md`
- `~/projects/AGENTS.md` (global): hard line breaks removed in principles 1–3, Documents and Git Staging

### Added

- `agents/rules/personal.md` added to `.gitignore` (person-bound, never committed)


### Added

- `## Startup index budget` section in `docs/research/2026-06-19-context-budget-and-file-limits.md`: per-doc-type caps for the session-start index (all decisions/specs/plans, last 10 research, last 5 sessions; ~660 tokens) and the recency-position rationale
- File read/write protocol in `AGENTS.md`: read-before-write, anchor-edit as the default (the anchor is the integrity check), `overwrite_file` only with a git-diff guard, verify-via-returned-diff, never hard-delete (move to `.trash/`)
- Git section in `AGENTS.md`: explicit `git add` paths (never `-A`), Conventional Commits, push governed by `push:` (on/confirm/off), no force-push, mid-session `git status` timing, index-lock handling
- `docs/research/2026-06-19-mcp-file-tool-design.md` — design of the ideal MCP file server: four tools (read with hash, create, anchor-edit, guarded overwrite), atomic temp+rename write, diff-in-result with size cap, with rejected alternatives recorded
- `## Git recovery` in `operational.md` (`git bisect`, `git checkout <file>`)
- Abschluss-Signal trigger in `session-start.md`: a closing word from the operator prompts one question before running session-end
- `docs/README.md` — the single source of truth for the document format: the three read moves (`head -qn1` index, `awk` abstract, `grep` section map), the line-1 convention, the abstract rule, the two document classes, and a canonical template block for all five doc types. The format previously lived only in a chat widget
- ADR-002: document size governance — two document classes by load behaviour (skeleton vs. content), a language-level yellow/red traffic-light for skeleton files, and the principle that no algorithm deletes or moves content automatically
- Per-directory READMEs for the `agents/` machinery (memory, notes, commands, rules) plus an `agents/` index README — the documentation that explains each skeleton file now lives in the README, not in the file
- `~/projects/README.md` — workspace-level orientation: what lives at the workspace root, the two-call startup bootstrap (exec-1), and a note that these files are machine-specific
- Canonical header in `~/projects/AGENTS.md` (identity, startup with exec-2, override loading, autonomy levels, git behaviour), separated from the existing brainstorming material by a visible separator
- PLAN-002: AGENTS.md authoring — startup flow, three-tier read model,
  `##`-terminated greppable abstract convention, awk section-reading, and the
  work-backlog / work-log rename that stops open TODOs being buried
- PLAN-001: multi-VM agent architecture (design only) — canonical
  `~/projects/AGENTS.md` synced into projects via `agents_sync.sh` + a
  `.agents_sync` marker, per-project overrides, file-based configs,
  provider-agnostic backup with per-repo deploy keys

### Changed

- *(drafted, not yet promoted)* `AGENTS-v2.md` and `session-start-v2.md`: four principles pulled to the top, task workflow reduced to Spec/Plan/Build/Test, `## Skeleton` replaced by `## File limits` (line-1 word-based soft/hard limits checked on read, no file list), startup index added as final session-start step
- Git rules and universal craft consolidated into canonical `~/projects/AGENTS.md`; `agents/rules/global.md` merged in and moved to `.trash`. The earlier thin-pointer stance for AGENTS.md was reversed: craft rules load every session regardless, so a pointer saved nothing
- `AGENTS.override.md` slimmed to the four settings (name, persona, autonomy, push); conventions and anti-patterns moved to `OPERATOR.md` (per-VM, private), which also gained a platform line
- `session-start.md`: removed the git-state check and the last-session-log read (both now lazy / on-demand, not startup steps)
- Document head unified for ADR / SPEC / PLAN: `**Status:**`, then `**Created:** · **Updated:**`, in that order. `**Date:**` replaced by Created/Updated; PLAN gained a Status field; the Created/Updated dates carelessly dropped from ADR-001/002 in the prior pass were restored
- Spec status reduced to `Draft | Active | Superseded`. Status now tracks the document, not the implementation — "Done" was ambiguous (document-finished vs. code-built), and implementation progress belongs in ROADMAP / work-backlog. SPEC-001 moved Done → Active
- ADRs are no longer described as immutable: a real change is made by supersede-in-place (mark the old passage, set Status, append a dated `## Addendum`), never a silent rewrite, and the blast radius is checked first
- SPEC-001, SPEC-003, and the project-structure research doc converted to the line-1 index + abstract format; `Related ADR` / `Related` fields dropped to prose
- Document convention settled for all five doc types: line 1 is `filename | keywords` (read as a lexicon index via `head -qn1`), the abstract runs to the first `##`. Relationships between documents are carried by keywords, not by `Related:` fields (which were removed)
- SPEC-003 updated to the size-governance model: §10 "Document Budgets" became "Document System" (two classes + traffic-light); the operational-memory decay sweep was replaced by operator-decided pruning; the recall counter is retained as a human reading-aid
- `session-start.md` / `session-end.md`: hard size limits replaced by traffic-light checks; the automatic sweep step replaced by operator-decided pruning at a red signal; session-log line 1 now uses the `filename | keywords` format
- `recent_sessions.sh`: prints the project name (from the path) of the three newest session logs for project selection, instead of the first line of each
- ADR-001 converted to the new line-1 index + abstract format
- Skeleton files (`procedural.md`, `operational.md`, `historical.md`, `scratchpad.md`, `work-backlog.md`, `work-log.md`) slimmed to a single self-explanatory comment line; all explanatory prose moved to the per-directory READMEs to cut per-session token cost
- `session-start.md` no longer carries the exec-1/exec-2 preamble (it cannot describe its own loading); it now begins at the first orientation step. The bootstrap lives in `~/projects/README.md` and `AGENTS.md`
- Applied soft-wrap (one line per paragraph) across session-authored docs, per the standing personal convention; data lines remain one-per-record
- `global.md`: soft-wrapped; fixed stale refs (`AGENTS_override.md` → `AGENTS.override.md`, `docs/session/` → `docs/sessions/`)

### Removed

- `agents/rules/global.md` (merged into `AGENTS.md`, moved to `.trash`)
- ADR-000 and SPEC-000 template files (moved to `.trash`) — the canonical shape of each document type now lives in `docs/README.md`, not in standalone template files
- "Move to `specs/archive/` when done" for specs — a spec is the living reference and is not archived for being implemented; a superseded spec stays in place with `Status: Superseded`
- The deterministic operational-memory decay sweep (recall-rate scoring, auto-move to historical) — superseded by ADR-002's operator-decided pruning
- `SPEC-002-dev-mcp-server.md` moved out of the template (project-foreign) to `~/projects/SPEC-XXX-dev-mcp-server.md`; it was linked nowhere

## [0.7.0] - 2026-04-17

### Added

- ADR-001: founding decision — adopt industry standards for project structure
- SPEC-001: template standard specification (the template as its own spec)
- Domain research document on project structure standards (2026-04-17)
- Runbooks README explaining what runbooks are and when to add them
- Complete README with directory tree, standards table, and usage instructions
- MIT LICENSE
- Archive subdirectories for specs and plans

## [0.6.0] - 2026-04-17

### Added

- Claude Code slash command: `/daily-digest` — generates Obsidian vault dashboard
- Obsidian vault integration for human-readable project overview

## [0.5.0] - 2026-04-17

### Fixed

- Session start checklist in AGENTS.md now matches session-start command (7 steps)
- Added CLAUDE.md symlink instruction to permanent section for post-setup agents

### Added

- Artifact size decision rule: Issue vs Spec + Milestone + ADR

## [0.4.0] - 2026-04-17

### Added

- Claude Code slash command: `/session-start` — 7-step orientation checklist
- Claude Code slash command: `/wrap-up` — 6-step end-of-session protocol

## [0.3.0] - 2026-04-17

### Added

- Permanent AGENTS.md sections: project identity, anti-goals, session start checklist
- "Where Things Live" navigation table in AGENTS.md
- Git and GitHub section in AGENTS.md
- Tribal Knowledge section in AGENTS.md (date-tagged, category-tagged entries)
- Optional sections menu with selection guidance (Environment, Testing, Conventions, etc.)
- README skeleton
- ADR-000 template for architecture decision records
- SPEC-000 template for feature specifications
- GitHub Issue templates for bug reports and feature requests

## [0.2.0] - 2026-04-17

### Added

- 8-step setup guide in AGENTS.md (Steps 0–8)
- Step 1: user interview before touching any file
- Step 4: ADR-001 creation as the project's founding document
- Step 6: mandatory domain research saved to docs/research/
- Step 7: tool-specific setup for Claude Code, Codex, and claude.ai
- Step 8: first commit workflow and milestone creation guidance
- Setup guide self-destructs after project creation

## [0.1.0] - 2026-04-17

### Added

- Initial project directory structure (src, tests, docs, changelog)
- `.gitignore` covering Python, Node, macOS, secrets, and editors
- AGENTS.md placeholder for agent instructions
- `.claude/` directory for Claude Code commands and agents
- `.github/ISSUE_TEMPLATE/` directory for GitHub issue templates
