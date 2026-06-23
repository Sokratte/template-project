<!-- kw: AGENTS.md, conventional commits, keep a changelog, semver, spec-driven development, ADR, pointer pattern, context window, tribal knowledge, agentic coding -->
2026-04-17-project-structure-standards.md

# Research: Project Structure Standards for AI-Agent Workflows

**Scope:** How to structure projects where humans and AI agents collaborate on files.

The field has converged on a reusable set of standards — AGENTS.md as the
single cross-tool instruction file (kept under ~300 lines, pointer pattern,
just-in-time loading), Conventional Commits + Keep a Changelog + SemVer for
versioning, ADRs for immutable decisions, and spec-driven development (specs
before code). The 2026 agentic-coding practices that matter most: treat the
context window as the scarcest resource, write specs first (measured ~67%
lower rollback), plan before coding, and assume the session can be
interrupted at any moment — so record state continuously and re-read it at
start. This is the background ADR-001 and SPEC-001 build on.

## Standards adopted

### AGENTS.md (agent instructions)
Open standard for AI coding agent instructions. One file in repo root,
read by Claude Code, GitHub Copilot, Cursor, Windsurf, Codex, Gemini CLI,
and Devin. For Claude Code specifically, symlink `CLAUDE.md → AGENTS.md`.

**Key insight from HumanLayer blog:** Keep AGENTS.md under 300 lines.
Every line competes for context window attention. Focus on what the agent
would get wrong without being told — not on documenting everything that's
true. Claude Code's harness injects ~50 instructions of its own; your file
adds to that budget.

**Best practice:** Use pointer pattern. Don't inline code conventions —
point to a file. Don't inline architecture — point to the ADR. The agent
loads what it needs just-in-time.

Source: https://www.humanlayer.dev/blog/writing-a-good-claude-md

### Conventional Commits v1.0.0
Format: `<type>[optional scope]: <description>`
Types: `feat` (→ MINOR), `fix` (→ PATCH), `BREAKING CHANGE:` footer or `!` (→ MAJOR).
Additional types (no SemVer effect): `docs`, `refactor`, `test`, `chore`, `style`, `build`, `perf`.

Source: https://www.conventionalcommits.org/en/v1.0.0/

### Keep a Changelog 1.1.0
Section names: Added, Changed, Deprecated, Removed, Fixed, Security.
Always have `[Unreleased]` at top. Dates as YYYY-MM-DD.
Versions as `## [X.Y.Z] - YYYY-MM-DD`. Compare links at bottom.

Source: https://keepachangelog.com/en/1.1.0/

### Semantic Versioning 2.0.0
MAJOR.MINOR.PATCH. Driven by commit types via Conventional Commits.

Source: https://semver.org/spec/v2.0.0.html

### GitHub Spec Kit / Spec-Driven Development
GitHub's open-source SDD toolkit. Core idea: specifications are the source
of truth; code is their expression. Specs → Plans → Tasks → Implementation.
The full toolkit (CLI, slash commands, multi-phase pipeline) is heavyweight
for solo projects, but the principles apply:

- Write specs before implementing (we use `docs/specs/SPEC-NNN-*.md`)
- Record architecture decisions immutably (we use `docs/decisions/ADR-NNN-*.md`)
- Task breakdown before coding (we use GitHub Issues + Milestones)
- Research before building (we use `docs/research/`)

Source: https://github.com/github/spec-kit

---

## 2026 industry practices for agentic coding

### Context window is the #1 resource to manage
Claude's performance degrades as context fills. A single debugging session
can consume tens of thousands of tokens. Implication: keep instruction files
short, use just-in-time context loading, start fresh sessions for reviews.

Source: https://code.claude.com/docs/en/best-practices

### Spec-first has measured impact
Teams using written specs before agent runs had 67% lower rollback rate
than teams prompting without specs (Stack Overflow, March 2026).

Source: https://blink.new/blog/agentic-coding-best-practices

### Plan before coding
Cursor has Plan Mode. Claude Code has `/plan`. Plans open as editable
Markdown. Save to workspace for documentation and future agent context.

Source: https://cursor.com/blog/agent-best-practices

### Multi-agent patterns
Writer/Reviewer: one agent writes code, a fresh context reviews it.
Test-first: one agent writes tests, another writes code to pass them.
Parallel sessions for independent tasks. Subagents for isolated work.

Source: https://code.claude.com/docs/en/best-practices

### Tribal Knowledge is first-class
The best AGENTS.md files have dedicated sections for things no docs cover:
"Never destructure X inside Y — causes serialization error." Date-tagged,
category-tagged, accumulated over time.

### .claude/ directory structure
- `.claude/commands/` — slash commands, checked into git. Highest ROI:
  session-start, wrap-up, daily-digest.
- `.claude/agents/` — subagents with YAML frontmatter. Run in isolated
  context with own tool permissions and model selection.
- `.claude/skills/` — knowledge folders with progressive disclosure.
  Skills are folders (not files) with references/, scripts/, examples/.
- Note: `.claude/` is Claude Code only. Codex, claude.ai, Cursor do not
  read it. AGENTS.md must be self-sufficient for all other tools.

Source: https://github.com/shanraisshan/claude-code-best-practice

### "Assume interruption" protocol
Agents must assume their context window can be reset at any moment.
Record progress continuously. Session start always reads last known state.
This is why session logs exist and why the session start checklist is
non-negotiable.

Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool

---

## Tools worth knowing about

| Tool | What it does | When to use |
|------|-------------|-------------|
| Context7 | MCP plugin that gives agents access to current library docs | When agent uses wrong API — docs may have changed |
| Tavily | MCP plugin for web research from within agent sessions | Domain research, finding how others solved similar problems |
| CodeScene | Code health analysis via MCP — gives agents quality metrics | When agents need to measure "is this better or just different" |
| Biome | Linter/formatter that auto-fixes — pair with Claude Code hooks | Pre-commit quality gate |

---

## Key insight: the file hierarchy

For projects using Claude Code, the complete file hierarchy is:

1. **CLAUDE.md** (or AGENTS.md via symlink) — loaded every session, universal rules
2. **AGENTS.md** — cross-tool standard, same content
3. **.claude/commands/** — slash commands, invoked explicitly
4. **.claude/agents/** — subagents, delegated to for isolated tasks
5. **.claude/skills/** — knowledge folders, loaded by agents on demand
6. **docs/** — specs, ADRs, research — loaded just-in-time by checklist

Authority flows top-down. CLAUDE.md overrides everything for Claude sessions.
AGENTS.md is universal project law. Everything else is supplementary.
