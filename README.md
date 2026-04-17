# Workspace Project Template

> Reusable project scaffold for all workspace projects. Copy this folder
> to start a new project with proper structure, agent instructions, and
> industry-standard conventions built in from day one.

## What

This template provides the starting point for any new project in
your workspace. It includes an AGENTS.md with a guided setup flow,
architecture decision records, spec templates, GitHub Issue templates,
Claude Code slash commands, session logging, Obsidian vault integration,
and a directory structure informed by current industry standards for
AI-agent-assisted development.

The template is not opinionated about language, framework, or domain.
It handles the meta-structure — how work is tracked, how agents orient
themselves, how decisions are recorded, how knowledge is preserved.

## Why

Every project I have worked on eventually needed these things.
Most grew them organically over months. This template captures what
worked and makes it available from the first commit, so no project
starts from scratch again.

## How to use

```
cp -r ~/workspace/template-project ~/workspace/projects/my-new-project
cd ~/workspace/projects/my-new-project
```

Then open `AGENTS.md` and follow the setup guide. The agent walks you
through project clarification, GitHub repo creation, section selection,
domain research, and first commit. When done, the setup guide deletes
itself and you have a clean project.

**Do not modify this folder as part of project work.** Improvements to
the template itself are a separate task — see ADR-001.

## What's inside

```
template-project/
├── AGENTS.md                          # Agent instructions (setup guide + permanent sections)
├── CHANGELOG.md                       # Keep a Changelog format
├── VERSION                            # Semantic version
├── LICENSE                            # MIT
├── .gitignore                         # Python, Node, macOS, secrets, editors
│
├── .claude/                           # Claude Code integration (optional)
│   ├── commands/
│   │   ├── session-start.md           # /session-start — orientation checklist
│   │   ├── wrap-up.md                 # /wrap-up — end-of-session protocol
│   │   └── daily-digest.md            # /daily-digest — Obsidian vault dashboard
│   └── agents/                        # Subagent definitions (empty)
│
├── .github/
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md              # Bug report template
│       └── feature_request.md         # Feature/task template
│
├── docs/
│   ├── decisions/                     # Architecture Decision Records (immutable)
│   │   ├── ADR-000-template.md        # Blank ADR template
│   │   └── ADR-001-project-standard.md # This project's founding decision
│   ├── specs/                         # Feature specifications
│   │   ├── SPEC-000-template.md       # Blank spec template
│   │   └── SPEC-001-template-standard.md # This project as its own spec
│   ├── research/                      # Domain research (AI-maintained, dated)
│   ├── plans/                         # Task plans (short-lived, delete when done)
│   └── runbooks/                      # Operational guides
│
├── changelog/
│   └── session-logs/                  # Session narratives by year
│       └── 2026/
│
├── src/                               # Source code (empty in template)
└── tests/                             # Tests (empty in template)
```

## Standards adopted

| Standard | What it provides | Source |
|----------|------------------|--------|
| AGENTS.md | Cross-tool agent instructions | [humanlayer.dev](https://www.humanlayer.dev/blog/writing-a-good-claude-md) |
| Conventional Commits | Commit message format → automated versioning | [conventionalcommits.org](https://www.conventionalcommits.org/en/v1.0.0/) |
| Keep a Changelog | Human-readable change history | [keepachangelog.com](https://keepachangelog.com/en/1.1.0/) |
| Semantic Versioning | Version number meaning (MAJOR.MINOR.PATCH) | [semver.org](https://semver.org/spec/v2.0.0.html) |
| Architecture Decision Records | Immutable design decisions | [cognitect.com](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) |
| Spec-Driven Development | Specs before implementation | [github/spec-kit](https://github.com/github/spec-kit) |
| GitHub Issues + Milestones | Work tracking without custom files | [docs.github.com](https://docs.github.com/en/issues) |

## Status

See [CHANGELOG.md](CHANGELOG.md) for the latest changes.
