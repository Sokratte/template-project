<!-- file: ADR-001-project-standard.md · keywords: workspace template, industry standards, conventional commits, semver, AGENTS.md, ADR, spec-driven development, pointer pattern, cp -r, agent orientation -->

# ADR-001: Adopt industry standards for workspace project structure

**Status:** Accepted
**Created:** 2026-04-17 · **Updated:** 2026-04-17

Every project in the workspace used to reinvent its own structure for
tracking work, recording decisions, and orienting AI agents, leaving nothing
to copy and no standard path for an agent arriving cold. We adopt the
converged industry standards — Conventional Commits, Keep a Changelog,
Semantic Versioning, AGENTS.md, Architecture Decision Records, and
spec-driven development — and ship them as a reusable template that new
projects create by `cp -r`. AGENTS.md is the single entry point and follows
a pointer pattern: it tells an agent where to look, not what is there.

## Context

Every project in the workspace eventually developed its own structure for
tracking work, recording decisions, and communicating with AI agents.
Previous projects grew decision trees, milestone prompts, and custom session
logs over months. Others had task specs, reconstruction roadmaps, and
session log files in various locations. Each project reinvented these
structures independently.

The problem: when starting a new project, there was nothing to copy — just
the memory of what worked before. AI agents arriving at a new project had
no standard orientation path.

Meanwhile, the industry has converged on standards:
- **Conventional Commits** (commit message format → automated versioning)
- **Keep a Changelog** (human-readable change history)
- **Semantic Versioning** (version number meaning)
- **AGENTS.md** (cross-tool agent instructions — Claude, Copilot, Cursor, Codex, Gemini, Devin)
- **Architecture Decision Records** (immutable design decisions)
- **Spec-Driven Development** (specs before implementation — see GitHub's spec-kit)
- **GitHub Issues + Milestones + Releases** (work tracking, not custom files)

## Decision

We adopt all of the above as the workspace standard. A reusable template
in `~/workspace/template-project/` provides the directory structure,
blank templates, and a guided setup flow. New projects are created by
copying this template and following the AGENTS.md setup guide.

Key design choices:
- **AGENTS.md is the single entry point** for any agent. It works with all
  major AI coding tools without modification.
- **Pointer pattern over content pattern.** AGENTS.md tells agents where
  to look, not what's there. Content lives in its own files.
- **Under 300 lines** for the permanent AGENTS.md. Context window budget
  is a real constraint.
- **Domain research is saved, not discarded.** `docs/research/` prevents
  agents from re-researching the same ground every session.
- **Plans are ephemeral, decisions are permanent.** `docs/plans/` is a
  scratchpad; `docs/decisions/` is immutable.
- **Optional sections with selection guidance.** Not every project needs
  every section. The setup guide helps the agent choose.
- **Claude Code commands are included but optional.** `.claude/commands/`
  provides session-start, wrap-up, and daily-digest slash commands.
  Deleted for non-Claude-Code workflows; AGENTS.md is self-sufficient.

## Consequences

**Positive:**
- Every new project starts with proven structure from day one.
- AI agents orient themselves in under 2 minutes from a cold start.
- Session logs, changelogs, and ADRs provide a complete audit trail.
- Industry standards mean external contributors (or future tools)
  understand the project without explanation.

**Negative:**
- The template itself must be maintained as standards evolve.
- Projects that outgrow the template will extend it — the template provides
  the base, not the ceiling.
- Copying the template includes example files (this ADR, research docs)
  that the setup agent should be aware of.

## Alternatives Considered

| Option | Why rejected |
|--------|-------------|
| Use GitHub's spec-kit directly | Too heavyweight — full CLI, slash commands, multi-phase SDD pipeline. We adopt the ideas (specs, plans, ADRs) without the tooling dependency. |
| Custom file hierarchy | Already proven to cause drift between projects. Standards exist; use them. |
| No template — start each project from scratch | The exact problem we're solving. Every project reinvents the wheel. |
| Generate with a script or CLI | Adds a dependency. `cp -r` is simpler, more reliable, and the setup guide in AGENTS.md handles the rest. |
