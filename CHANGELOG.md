# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
