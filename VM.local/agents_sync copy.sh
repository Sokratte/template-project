#!/usr/bin/env bash
# agents_sync.sh — sync the canonical AGENTS.md into every opted-in project.
#
# LOCATION ON THE VM: ~/projects/agents_sync.sh  (VM-local; NOT committed into
#   any project repo — a cloner must never receive it, or their agent would
#   overwrite their own AGENTS.md every session. See PLAN-001.)
#
# Behavior: for each directory under ~/projects/ that contains a `.agents_sync`
#   marker, copy ~/projects/AGENTS.md into it as a read-only (444) artifact.
#   Unmarked folders (foreign clones, reference repos) are skipped entirely.
#
# The read-only "permission dance": the project copy is chmod 444 so accidental
#   editor saves to the wrong file fail. The script owns the only legitimate
#   write path: chmod u+w -> cp -> chmod 444.

set -euo pipefail

PROJECTS_ROOT="${HOME}/projects"
CANONICAL="${PROJECTS_ROOT}/AGENTS.md"
MARKER=".agents_sync"

if [[ ! -f "${CANONICAL}" ]]; then
  echo "agents_sync: canonical not found at ${CANONICAL}" >&2
  exit 1
fi

synced=0
for dir in "${PROJECTS_ROOT}"/*/; do
  [[ -d "${dir}" ]] || continue
  [[ -f "${dir}${MARKER}" ]] || continue   # opt-in only

  dest="${dir}AGENTS.md"

  # Skip if an identical copy is already in place (avoids needless churn and
  # a no-op chmod on every run).
  if [[ -f "${dest}" ]] && cmp -s "${CANONICAL}" "${dest}"; then
    continue
  fi

  chmod u+w "${dest}" 2>/dev/null || true   # may not exist yet, or be 444
  cp "${CANONICAL}" "${dest}"
  chmod 444 "${dest}"
  echo "agents_sync: synced -> ${dest}"
  synced=$((synced + 1))
done

echo "agents_sync: ${synced} project(s) updated."
