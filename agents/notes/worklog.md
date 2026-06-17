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
2026-06-17 | DESIGN     | [OPEN]    | Draft canonical AGENTS.md (sign-off each step); decide autonomy level names + default | -
2026-06-17 | DOCS       | [OPEN]    | Cleanup task: reconcile stale doc paths to on-disk names; remove sweep-knowledge.py into session-end.md; drop daily-digest.md ref | agents/commands/, agents/README.md
