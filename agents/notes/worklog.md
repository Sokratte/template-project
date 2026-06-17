# Worklog — Central Work Ledger

# Append-only. Never edit or delete existing lines — only add new ones.
# Scanned at session start. Line format:
#   YYYY-MM-DD HH:MM | MODULE     | [TAG]     | Description | file-ref
#
# MODULE (col 2, ~9 chars): a category that fits this project. Suggested
#   starting set — adapt per project: PROJECT, META, DOCS, CODE, TEST,
#   INFRA, DESIGN, RESEARCH. Keep the set small and stable.
# TAG (col 3): [OPEN]=not started, [ACTIVE]=in progress, [DONE]=finished,
#   [NOTE]=context without an action, [FIND]=agent discovery needing
#   discussion or a decision.
# file-ref (col 5): path to the relevant file, or "-".
#
# Cleanup (run at session start): if this file is > ~60 lines or > ~4 KB,
#   move [DONE]/[NOTE] entries older than 30 days to worklog-archive.md.
#   [OPEN]/[ACTIVE] entries NEVER age out.
# ---------------------------------------------------------------------------
2026-06-17 | META       | [DONE]    | PLAN-001 multi-VM agent architecture finalized | docs/plans/PLAN-001-multi-vm-agent-architecture.md
2026-06-17 | META       | [DONE]    | Session log written | docs/sessions/2026-06-17-session-08-multi-vm-architecture.md
2026-06-17 | DESIGN     | [DONE]    | AGENTS.md content decisions locked in PLAN-002 (startup flow, 3-tier read, abstract convention, backlog/log split) | docs/plans/PLAN-002-agents-md-authoring.md
2026-06-17 | DESIGN     | [OPEN]    | Execute PLAN-002: draft canonical AGENTS.md prose (sign-off each step); decide autonomy names+default, persona placement, line budget | docs/plans/PLAN-002-agents-md-authoring.md
2026-06-17 | DOCS       | [OPEN]    | PLAN-002 ripple edits: rename worklog->work-backlog & worklog-archive->work-log; fix SPEC-003 append-only contract; CREATE_PROJECT budgets; rewrite session-start/end; README phantom ref; remove sweep script | -
2026-06-17 | DOCS       | [DONE]    | Repo restructure committed as moves; tree clean | -
