<!-- keywords: workspace template, project structure, AGENTS.md, setup flow, agent orientation, cp -r, ADR-001 -->
SPEC-001-template-standard.md

# SPEC-001: Workspace Project Template Standard

**Status:** Active
**Created:** 2026-04-17 · **Updated:** 2026-04-17

Defines what a workspace project template must include and how the setup flow
works, so every new project starts with proven structure and AI agents can
orient themselves in under 2 minutes. The template is a directory tree copied
verbatim by `cp -r`; the intelligence lives in AGENTS.md, whose setup guide
customizes the copy for the specific project and then self-destructs. Implements
ADR-001 (adopt industry standards for workspace project structure).

## Non-goals

- NOT: a CLI tool or generator script — `cp -r` is the mechanism
- NOT: opinionated about language, framework, or domain
- NOT: a replacement for project-specific documentation

## Acceptance criteria

- [x] AGENTS.md with self-destructing setup guide (Steps 0–8)
- [x] Permanent AGENTS.md sections: identity, checklist, nav table, git, tribal knowledge
- [x] Optional sections menu with selection guidance
- [x] ADR template (ADR-000) and spec template (SPEC-000)
- [x] GitHub Issue templates for bugs and features
- [x] Claude Code commands: session-start, wrap-up, daily-digest
- [x] Domain research document saved to docs/research/
- [x] Session log directory with year-based subdirectories
- [x] Keep a Changelog format with Semantic Versioning
- [x] Conventional Commits enforced by convention
- [x] README with usage instructions and standards table
- [x] MIT LICENSE

## Design

The template is a directory tree that gets copied verbatim. The intelligence
is in AGENTS.md: a setup guide walks the agent through an 8-step process that
customizes the template for the specific project. When setup completes, the
guide self-destructs, leaving a lean permanent section under 300 lines.

Key patterns:
- **Pointer pattern:** AGENTS.md tells agents where to look, not what's there.
  Content lives in its own files.
- **Just-in-time loading:** The session start checklist reads files in
  priority order. Agents load only what they need.
- **Archive, don't delete:** Completed specs and plans move to `archive/`
  subdirectories. Nothing is lost.

## Open questions

- None remaining — all criteria met.
