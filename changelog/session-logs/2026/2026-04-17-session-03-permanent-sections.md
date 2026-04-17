# Session Log: Permanent Sections and Supporting Files

**Date:** 2026-04-17

## What happened

Built the permanent AGENTS.md sections that remain after setup:
- Project identity block with name, description, and anti-goals
- Session start checklist (currently 5 steps — read global rules,
  read project rules, check git, read session log, check plans)
- "Where Things Live" navigation table mapping questions to file locations
- Git section (defers to global AGENTS.md for discipline rules)
- Tribal Knowledge section with date/category tagging convention
- Optional sections menu with 8 sections and selection guidance

Also added supporting files:
- README skeleton (will be expanded later)
- ADR-000 and SPEC-000 templates
- GitHub Issue templates for bugs and feature requests

## Decisions

- Navigation table uses question-answer format ("What's in progress now"
  → "GitHub Issues") rather than a plain directory listing.
- Optional sections include guidance on when to include each one,
  making the selection conversation faster.
- Tribal Knowledge uses a specific format: date, category tag, the
  knowledge, and why it matters.

## What's next

Add Claude Code slash commands (session-start, wrap-up).
