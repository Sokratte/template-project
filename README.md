# template-project

Reusable AI agent scaffold for all projects on this machine. Copy it to start a new project with the full structure, agent instructions, and conventions in place from the first commit.

## What this is

A meta-structure template: how work is tracked, how agents orient themselves, how decisions are recorded, how knowledge is preserved across sessions. Not opinionated about language, framework, or domain — that is the project's concern, not the template's.

The canonical agent instructions live in `~/projects/AGENTS.md` and are synced into every template-derived project via `agents_sync.sh`. Per-project differences go in `AGENTS.override.md`. Who the operator is and what this machine is like lives in `~/projects/OPERATOR.md` (never committed — PII).

## How to use

```bash
cp -r ~/projects/template-project ~/projects/<new-project-name>
```

Then open `CREATE_PROJECT.md` in the copy and follow the setup guide. Do not work inside `template-project/` itself.

## What’s inside

```
template-project/
├── AGENTS.md                  # synced copy of ~/projects/AGENTS.md (read-only, do not edit)
├── AGENTS.override.md         # project-specific overrides: persona, autonomy, push
├── CREATE_PROJECT.md          # setup guide — run once, then the preamble self-deletes
├── ROADMAP.md                 # project direction and active milestones
├── CHANGELOG.md               # Keep a Changelog format
├── .agents_sync               # opt-in marker: agents_sync.sh will sync AGENTS.md into this project
├── .gitignore
│
├── agents/                    # agent machinery (not instructions — those are in AGENTS.md)
│   ├── commands/
│   │   ├── session-start.md   # orientation procedure — execute at session start
│   │   └── session-end.md     # closing procedure — execute at session end
│   ├── memory/
│   │   ├── procedural.md      # rules every session — loaded, size-limited
│   │   └── operational.md     # gotchas + demoted rules — no limit, indexed by section
│   ├── notes/
│   │   ├── work-backlog.md    # open items (pruned living list; alarm at >20)
│   │   ├── work-log.md        # done items (append-only)
│   │   └── scratchpad.md      # carry-forward + working space
│   ├── rules/
│   │   └── project.md         # project-specific working rules
│   └── README.md              # map of the above
│
├── docs/
│   ├── README.md              # document conventions (line-1 format, abstract, templates)
│   ├── decisions/             # ADRs — immutable once ratified
│   ├── specs/                 # what the project builds — the target
│   ├── plans/                 # how to build it — living task plans
│   ├── sessions/              # per-session technical record
│   └── research/              # domain knowledge, dated
│
├── src/                       # source code
└── tests/                     # tests
```

## Conventions

| Convention | What it provides |
|---|---|
| AGENTS.md | Cross-tool agent instructions (Codex, Cursor, Copilot, Gemini CLI, Aider, Zed) |
| Conventional Commits | `type(scope): description` — [conventionalcommits.org](https://www.conventionalcommits.org/en/v1.0.0/) |
| Keep a Changelog | Human-readable change history — [keepachangelog.com](https://keepachangelog.com/en/1.1.0/) |
| ADRs | Immutable design decisions with full context — [cognitect.com](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) |
| Spec-driven development | Spec → Plan → Build → Test, always in that order |
