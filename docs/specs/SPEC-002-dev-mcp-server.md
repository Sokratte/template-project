<!-- keywords: MCP server, dev tools, file tools, create, edit, overwrite, git, read, project-scoped, stdio -->
SPEC-002-dev-mcp-server.md

# SPEC-002 — Project-Scoped Dev MCP Server

> A local, stdio-based MCP server that gives an AI agent a small, safe set of
> tools for working inside a single project: run tests, read and search the
> codebase, and operate git. Five tools, designed to be cheap in context and
> understood by any model with function calling.

**Status:** Active
**Applies to:** any project copied from the workspace template
**Reference implementations:** `WhisperDog/tools/test_mcp.py`, `TradingBot/tools/test_mcp.py`

---

## 1. Purpose and design philosophy

This server exists so the agent can drive the read → understand → change →
verify → commit → push loop without the operator copy-pasting terminal output
by hand. It deliberately exposes a *small* surface.

Three principles shape every decision in it:

1. **Minimal token footprint.** Every tool's schema (name, description,
   parameters) is injected into *every* request to the model. Fewer tools with
   tighter descriptions means more of the context window is left for actual
   work. The server went through several rounds of consolidation: 17 narrow
   tools collapsed into 5 general ones with parameters.

2. **Safety by construction, not by trust.** Every path is confined to the
   project root. No shell string is ever interpreted — commands are built as
   argument lists. Sensitive files are refused. Output is capped so a huge diff
   can't flood the model's context.

3. **Model-agnostic.** The tools follow conventions any function-calling model
   can pick up from the schema alone: list-typed `args`, relative paths, plain
   return strings. No Anthropic-specific assumptions.

---

## 2. The welcome message (server instructions)

When the server first connects to the client during the MCP handshake, it sends
a one-line instruction:

```python
mcp = FastMCP(
    "whisperdog-dev",
    instructions="Start every session: call read_file('AGENTS.md') before using any other tool.",
)
```

**Why this matters:** the `instructions` string is transmitted **once**, at
connection time — not on every message. It costs nothing per turn. It replaces
what was previously a dedicated `project_info()` tool, which wasted ~80 tokens
of schema on every single request just to say "open this file." Since
`read_file` already exists, a tool that only opens one file is redundant
abstraction. The instruction points the agent at `AGENTS.md` and gets out of
the way.

**The contract:** the agent's first action in any session is
`read_file("AGENTS.md")`. Everything the agent needs to orient itself —
project purpose, directory layout, test command, commit conventions, the
session-start checklist — lives there, not in tool schemas.

---

## 3. AGENTS.md — the orientation document

`AGENTS.md` is the de-facto standard instruction file that Cursor, Claude Code,
Codex, Copilot, and most agents look for on session start. It is the single
source of truth that makes this server work for *any* model, not just one that
has prior memory of the project.

A well-written `AGENTS.md` answers, in its first screenful:

- **What** the project is and who it's for (one sentence).
- **Where** the source lives — the directory map.
- **How** to run tests (the exact command / which marker conventions exist).
- **Commit style** (Conventional Commits, push-after-commit discipline).
- **The session-start checklist** — the exact reading order each session.
- **One or two gotchas** that would otherwise cost the agent several wasted
  tool calls to discover.

The token economics: a foreign model dropped in cold otherwise burns 5–6
exploratory tool calls just figuring out the language, layout, and test
command. A tight `AGENTS.md` collapses that into a single `read_file` call.
Keep it short and imperative — prose paragraphs get distorted under attention
compression; bullet points and imperative sentences survive.

---

## 4. The tools

Five tools. Each section gives the signature, the parameters, the behaviour,
the safety boundary, and a complete set of non-redundant examples.

### 4.1 `run_pytest`

```
run_pytest(path: str = "tests/", args: Optional[List[str]] = None) -> str
```

Runs the project's test suite through the venv interpreter (`sys.executable`,
so it always uses the right environment). Returns captured output plus exit
code. Read-only with respect to source; only writes `.pyc` caches.

| Parameter | Type | Default | Meaning |
|-----------|------|---------|---------|
| `path` | str | `"tests/"` | File, directory, or pytest node id, relative to project root. |
| `args` | list of str | `None` | Extra pytest flags. **Always a list, never a shell string.** |

`args` is the key to never having to edit the server when the project grows.
Markers, filters, coverage, plugins — all flow through pytest's own CLI.

**Examples**

```python
# Full suite, default path
run_pytest()

# One test file
run_pytest("tests/test_audio.py")

# A single test by node id
run_pytest("tests/test_audio.py::test_vad_threshold")

# Stop at first failure, short tracebacks
run_pytest(args=["-x", "--tb=short"])

# Re-run only what failed last time
run_pytest(args=["--lf"])

# Filter by name expression
run_pytest(args=["-k", "transcription and not slow"])

# Run by marker
run_pytest(args=["-m", "integration"])

# Verbose, no output capture (see prints / logging live)
run_pytest(args=["-v", "-s"])

# Collect-only: list tests without running them. Also verifies a file
# imports cleanly — this subsumes the old standalone py_compile tool.
run_pytest("src/app.py", args=["--co"])

# Linting and type-checking via pytest plugins, instead of separate tools.
# Requires: pip install pytest-ruff pytest-mypy
# This subsumes the old standalone run_linter (ruff / mypy) tool.
run_pytest(args=["--ruff", "--mypy"])
```

---

### 4.2 `list_dir`

```
list_dir(path: str = ".") -> str
```

Lists one directory. Directories are marked with a trailing `/`. Files sort
after directories, then alphabetically. Answers the question *"what is here?"*

| Parameter | Type | Default | Meaning |
|-----------|------|---------|---------|
| `path` | str | `"."` | Directory relative to project root. |

**Examples**

```python
# Project root
list_dir()

# A subdirectory
list_dir("src")

# Nested
list_dir("docs/decisions")

# Check what test files exist before running a subset
list_dir("tests")
```

---

### 4.3 `read_file`

```
read_file(path: str, start_line: Optional[int] = None, end_line: Optional[int] = None) -> str
```

Reads a UTF-8 text file, optionally a line range. Answers *"what does this
file (or this part of it) say?"* The line-range parameters absorb what used to
be a separate `read_section` tool: instead of teaching the server to parse
Markdown headings, the agent finds a heading's line number with
`search(headings_only=True)` and reads from there.

| Parameter | Type | Default | Meaning |
|-----------|------|---------|---------|
| `path` | str | — (required) | File relative to project root. |
| `start_line` | int | `None` | First line to return (1-based, inclusive). |
| `end_line` | int | `None` | Last line to return (1-based, inclusive). |

**Guards:** refuses files matching the sensitive denylist (`.env`, `.pem`,
keys, credentials). Refuses files larger than 512 KiB. Non-UTF-8 / binary
files return a clear error rather than garbage.

**Examples**

```python
# Session-start orientation — the contract from the welcome message
read_file("AGENTS.md")

# A whole source file
read_file("src/transcription/whisper.py")

# Just the top of a long file (imports, module docstring)
read_file("src/supervisor.py", start_line=1, end_line=40)

# Read a specific line range — e.g. a function you already know the location of
read_file("src/audio/recorder.py", start_line=120, end_line=160)

# A section located by a prior heading search (see §4.4):
# search returned "docs/decisions/ADR-004.md:67: ## Consequences"
read_file("docs/decisions/ADR-004.md", start_line=67)

# Bound the section read if you also know the next heading's line
read_file("docs/decisions/ADR-004.md", start_line=67, end_line=95)

# Read the latest changelog entry
read_file("CHANGELOG.md", start_line=1, end_line=30)
```

---

### 4.4 `search`

```
search(pattern: str, path: str = ".", max_matches: int = 100,
       regex: bool = False, headings_only: bool = False,
       level: Optional[int] = None) -> str
```

Recursively searches file contents. Returns `relpath:lineno: matching_line`
for each hit. Skips `.git`, `.venv`, caches, and sensitive files. This one
tool covers four jobs that were once separate tools: literal substring search,
regex search, Markdown-heading search (the old `grep_heading`), and locating a
section's line number to feed into `read_file`.

| Parameter | Type | Default | Meaning |
|-----------|------|---------|---------|
| `pattern` | str | — (required) | Text or regex to find. |
| `path` | str | `"."` | Directory (or file) to search under. Narrows scope. |
| `max_matches` | int | `100` | Stop after this many hits. |
| `regex` | bool | `False` | `False` = literal substring; `True` = Python `re`. |
| `headings_only` | bool | `False` | `True` = match only Markdown heading lines, in `.md` files only. |
| `level` | int | `None` | With `headings_only=True`: restrict to heading depth 1–6 (`#`=1, `##`=2, …). |

**Note on `regex=True` and JSON encoding:** the pattern lives inside a JSON
string in the tool call, so backslashes must be doubled — write `\\w+`,
`\\bdef\\b`, `\\d+`. This is the most common mistake foreign models make with
this parameter.

**Examples**

```python
# Literal substring across the whole project
search("VAD_THRESHOLD")

# Scope the search to one subtree (faster, fewer false positives)
search("supervisor", path="src")

# Limit hits when you only need to confirm existence
search("TODO", max_matches=10)

# Regex: find every handler function definition
search(r"def \\w+_handler", regex=True)

# Regex scoped to a directory
search(r"class \\w+Error", path="src", regex=True)

# Regex: find all lines importing from a specific module
search(r"^from src\\.audio", regex=True)

# Find a Markdown section by heading text — the old grep_heading job
search("Consequences", headings_only=True)

# Find only H1 headings containing "ADR"
search("ADR", headings_only=True, level=1)

# Find all H2 headings in the decisions subtree
search("", headings_only=True, level=2, path="docs/decisions")

# Scoped heading search
search("status", path="docs", headings_only=True)

# The locate-then-read pattern — replaces the old read_section tool:
#   Step 1: find the heading's line number
search("Decision", path="docs/decisions/ADR-001-project-definition.md", headings_only=True)
#   Step 2: read from that line (see §4.3)
#   read_file("docs/decisions/ADR-001-project-definition.md", start_line=N)
```

---

### 4.5 `git`

```
git(subcommand: str, args: Optional[List[str]] = None) -> str
```

One tool for all version control, modelled on the maisig-auditor pattern. The
subcommand is checked against an allowlist; everything else goes in `args` as a
list of strings. No shell interpretation. This single tool replaces eight
former tools: `git_status`, `git_diff`, `git_log`, `git_show`, `git_add`,
`git_commit`, `git_push`, and `git_branch`/`git_checkout`.

| Parameter | Type | Default | Meaning |
|-----------|------|---------|---------|
| `subcommand` | str | — (required) | One of the allowlisted git subcommands (see below). |
| `args` | list of str | `None` | Flags and operands. **Always a list, never a shell string.** |

**Allowlist:** `status`, `diff`, `log`, `show`, `add`, `commit`, `push`,
`pull`, `branch`, `checkout`, `stash`, `reset`, `mv`.

Anything not on the list returns an error that includes the permitted set.

**Push is included by design.** The whole reason this server exists is that
work must never be lost. The agent commits *and pushes* as the closing step of
every unit of work — push is part of the contract, not a manual exception. The
earlier "read-only git" design in WhisperDog was a misreading of a past
data-loss incident: the loss happened because nothing was pushed, not because
something was pushed incorrectly.

**`git add .` is intentionally not default practice.** Staging should use
explicit paths or `-u` (tracked files only) so unreviewed files are never
silently included in a commit.

**Examples — read**

```python
# Working tree state — the old git_status
git("status")

# Unstaged changes — the old git_diff
git("diff")

# Staged (index) changes only
git("diff", ["--staged"])

# Diff limited to one file
git("diff", ["--", "src/app.py"])

# Last 10 commits one line each — the old git_log
git("log", ["--oneline", "-n", "10"])

# Filter log by commit message
git("log", ["--oneline", "--grep=feat"])

# Filter log by author and time window
git("log", ["--oneline", "--author=Martin", "--since=1.week"])

# Full history of one file, following renames
git("log", ["--oneline", "--follow", "src/audio/recorder.py"])

# Inspect a specific commit — the old git_show
git("show", ["a3f2c1"])
git("show", ["--stat", "a3f2c1"])

# Inspect a relative ref
git("show", ["HEAD~2"])
```

**Examples — write**

```python
# Stage explicit files — the old git_add
git("add", ["src/app.py", "tests/test_app.py"])

# Stage all tracked changes (no untracked files)
git("add", ["-u"])

# Commit — the old git_commit. Use Conventional Commits format.
git("commit", ["-m", "feat(audio): add VAD threshold config"])
git("commit", ["-m", "fix(supervisor): handle shutdown race condition"])
git("commit", ["-m", "docs: update session-start checklist"])

# Push — the old git_push. Always the closing step after a commit.
git("push")
```

**Examples — branches**

```python
# List all local and remote branches — the old git_branch (no args)
git("branch", ["-a"])

# Create a branch without switching — the old git_branch(name)
git("branch", ["feature/vad-tuning"])

# Switch to an existing branch — the old git_checkout(branch)
git("checkout", ["main"])

# Create and switch in one step — the old git_checkout(branch, create=True)
git("checkout", ["-b", "feature/mic-rediscovery"])
```

**Examples — stash, reset, mv**

```python
# Save work in progress before switching context
git("stash")
git("stash", ["pop"])

# Unstage a file without touching working tree
git("reset", ["HEAD", "src/app.py"])

# Rename a tracked file, preserving history
git("mv", ["docs/old-name.md", "docs/new-name.md"])

# Pull remote changes
git("pull")
```

---

## 5. Coverage map — the original 17 tools

This server began as 17 narrow tools and was consolidated to 5. Every original
capability is preserved. The table below maps each original tool to where it
now lives and which example exercises it.

| # | Original tool | Now in | Example |
|---|---------------|--------|---------|
| 1 | `project_info()` | Server `instructions` + `read_file("AGENTS.md")` | §2, §4.3 first example |
| 2 | `run_pytest(path)` | `run_pytest(path)` | §4.1 |
| 3 | `py_compile(files)` | `run_pytest(path, args=["--co"])` | §4.1 collect-only example |
| 4 | `run_linter(ruff)` | `run_pytest(args=["--ruff"])` | §4.1 last example |
| 5 | `run_linter(mypy)` | `run_pytest(args=["--mypy"])` | §4.1 last example |
| 6 | `list_dir(path)` | `list_dir(path)` | §4.2 |
| 7 | `read_file(path)` | `read_file(path)` | §4.3 |
| 8 | `read_section(path, heading)` | `search(headings_only=True)` → `read_file(start_line=N)` | §4.3 + §4.4 locate-then-read |
| 9 | `search(literal)` | `search(pattern)` | §4.4 first examples |
| 10 | `search(regex=True)` | `search(pattern, regex=True)` | §4.4 regex examples |
| 11 | `grep_heading(pattern, level)` | `search(headings_only=True, level=N)` | §4.4 heading examples |
| 12 | `git_status()` | `git("status")` | §4.5 |
| 13 | `git_diff(staged, path)` | `git("diff", ["--staged"])` / `git("diff", ["--", path])` | §4.5 |
| 14 | `git_log(n, args)` | `git("log", ["--oneline", "-n", "10", …])` | §4.5 |
| 15 | `git_show(ref)` | `git("show", [ref])` | §4.5 |
| 16 | `git_add` / `git_commit` / `git_push` | `git("add"/"commit"/"push", […])` | §4.5 write examples |
| 17 | `git_branch` / `git_checkout` | `git("branch"/"checkout", […])` | §4.5 branch examples |

---

## 6. Safety boundaries

| Concern | Mechanism |
|---------|-----------|
| Path traversal | Every path resolved against project root; anything escaping it is refused. |
| Shell injection | Commands built as argument lists (`List[str]`); no shell string is ever interpreted. |
| Secret exposure | Sensitive-file denylist (`.env`, `.pem`, keys, credentials) refused in `read_file`, skipped in `search`. |
| Context flooding | Output capped (head + tail with a truncation marker) on large diffs / test runs. |
| Network exposure | stdio transport — a local subprocess, nothing listening on a port. |
| Unbounded git | Subcommand allowlist; unknown subcommands refused with the permitted set listed. |
| Silent process death | stdout reserved for the JSON-RPC channel; all diagnostics go to stderr only. |

---

## 7. Adapting to a new project

1. Copy `tools/test_mcp.py` into the new project's `tools/` directory.
2. The `Path(__file__).resolve().parent.parent` root derivation needs no
   editing if the file lives in `tools/`. For non-standard layouts, set a
   hardcoded `PROJECT_DIR` or `REPO_ROOT` constant instead.
3. Update the server name and `instructions` string in `FastMCP(...)`.
4. Adjust `SKIP_DIRS` / `SENSITIVE` for unusual layouts or secret conventions.
5. Install the dev dependency: `.venv/bin/pip install "mcp[cli]"`. Optionally:
   `pip install pytest-ruff pytest-mypy` to enable the lint/type-check examples.
6. Register in the client config (venv interpreter path + absolute script
   path), restart the client, confirm 5 tools appear.
7. Smoke test live: `git("status")` and `run_pytest()`.
