# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

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

- Skeleton files (`procedural.md`, `operational.md`, `historical.md`, `scratchpad.md`, `work-backlog.md`, `work-log.md`) slimmed to a single self-explanatory comment line; all explanatory prose moved to the per-directory READMEs to cut per-session token cost
- `session-start.md` no longer carries the exec-1/exec-2 preamble (it cannot describe its own loading); it now begins at the first orientation step. The bootstrap lives in `~/projects/README.md` and `AGENTS.md`
- Applied soft-wrap (one line per paragraph) across session-authored docs, per the standing personal convention; data lines remain one-per-record
- `global.md`: soft-wrapped; fixed stale refs (`AGENTS_override.md` → `AGENTS.override.md`, `docs/session/` → `docs/sessions/`)

### Removed

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
