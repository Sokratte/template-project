#!/usr/bin/env bash
# projects_list.sh — VM-level orientation at session start.
#
# LOCATION ON THE VM: ~/projects/projects_list.sh  (VM-local; NOT committed
#   into any project repo.)
#
# Prints all projects under ~/projects/, then the 3 most-recently-touched
#   session logs across projects. Run once at startup before loading a project.

set -euo pipefail

echo "=== LIST OF ALL PROJECTS ==="
ls -d "${HOME}/projects"/*/  2>/dev/null | xargs -n1 basename

echo "=== 3 MOST RECENT SESSIONS ==="
PROJECTS_ROOT="${HOME}/projects"
N=3
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
