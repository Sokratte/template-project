#!/usr/bin/env bash
# recent_sessions.sh — cross-project orientation for the agent at startup.
#
# LOCATION ON THE VM: ~/projects/recent_sessions.sh  (VM-local; NOT committed
#   into any project repo. See PLAN-001.)
#
# Prints the PROJECT NAME of each of the 3 most-recently-touched session logs
#   across ALL projects under ~/projects/, newest first. The project name is
#   taken from the path (.../projects/PROJECT/docs/sessions/... → PROJECT),
#   not from the file contents: a session log's line 1 is now the index entry
#   "filename | keywords" (ADR-002 / SPEC-003 §10), which is not prose and not
#   useful for project selection.
#
# Purpose (exec-1 startup): let the agent disambiguate which project to open.
#   If all 3 names are identical, that project is the obvious resume target;
#   load it. Otherwise ask the operator or take the project from the prompt.
#   "What happened last" is NOT derived here — the agent reads the newest
#   session log itself once a project is chosen.
#
# Robust to projects that have no sessions yet, and to paths with spaces.
# Compatible: bash 3.2+, macOS, Debian, any POSIX Linux / container.

set -euo pipefail

PROJECTS_ROOT="${HOME}/projects"
N=3

# ls -t: newest-first by mtime. 2>/dev/null silences "no matches" on empty dirs.
# IFS= + read: POSIX-safe; handles spaces in paths; no mapfile (bash 4+) needed.
count=0
while IFS= read -r f; do
  rel="${f#"${PROJECTS_ROOT}"/}"   # PROJECT/docs/sessions/FILE.md
  echo "${rel%%/*}"                # PROJECT
  count=$((count + 1))
  [ "${count}" -ge "${N}" ] && break
done < <(ls -t "${PROJECTS_ROOT}"/*/docs/sessions/*.md 2>/dev/null)

if [ "${count}" -eq 0 ]; then
  echo "(no session logs found across projects yet)"
fi
