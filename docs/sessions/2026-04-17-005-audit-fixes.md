# Session Log: Audit Fixes

**Date:** 2026-04-17

## What happened

Audited the template for consistency and found three issues:

1. **Session start checklists misaligned.** AGENTS.md had 5 steps,
   session-start.md had 7. Fixed: AGENTS.md now has the same 7 steps
   including docs/research/ and GitHub Issues.

2. **CLAUDE.md symlink instruction missing from permanent section.**
   The setup guide (Step 7) creates the symlink, but agents arriving
   after setup had no reminder. Fixed: added a note in the Git section.

3. **Size decision rule was undocumented.** When should you create an
   Issue vs a Spec + Milestone + ADR? Added the decision rule after
   the "Where Things Live" navigation table.

## What's next

Add Obsidian vault integration via daily-digest command.
