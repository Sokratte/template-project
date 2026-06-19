# OPERATOR.md

*VM-local. Not committed. Not synced. PII — stays on this machine only.*
*One file per VM. Edit freely; the agent reads this at every session start.*

---

## Identity

**Operator handle:** Martin
**VM:** MacBook2
**Platform:** MacBook Pro, macOS, Apple Silicon
**Timezone:** Europe/Berlin
**Primary language:** German (conversation); English (all file content)

---

## Operator profile

- Iterative and critical: pushes back on complexity, redundancy, anything that adds files
  or mechanisms without clear demonstrated value.
- Hard preference for simplicity and anti-extra-files.
- Catches design problems via failure-cost reasoning.
- Specs before non-trivial implementation; sign-off on every step.
- Strong signal phrases: *"this is really, really bad"* = duplication found;
  *"Go!"* = proceed without further deliberation.

---

## VM facts

**Workspace root:** ~/projects/
**Projects:** /Users/martin/projects/[project-name]/
**Filesystem MCP allowed:** /Users/martin/projects, /Users/martin/recovery

**Active projects:**
- template-project — canonical pattern / infra work
- WhisperDog — TODO
- TradingBot — TODO
- maisig — TODO
- tbh — TODO

---

## Conventions on this VM

- All document content in English; conversation with operator in German.
- No hard line breaks in documents — soft-wrap only.
- Edit with caution: server configuration files, firewall rules, SSH config,
  specs (update sections, never rewrite from scratch).
- Never touch without a plan and operator approval: filesystem layout and mount
  points, encryption keys and credentials, design philosophies.
- Plans are reusable reference documents, not disposable checklists. Update them
  when implementation differs from the plan.
- Scripts run from the repo using bash only. Never chmod +x. One-time
  non-persistent tasks only (install files, start services).
- No live project files may link to or run from the repo.

## Anti-patterns to avoid

- Building from scratch without checking if the prototype already solved it.
- Guessing instead of asking — a question costs 30 seconds, a wrong build costs hours.

---

## Agent behaviour on this VM

**Push:** governed by `push:` in each project's `AGENTS.override.md` (on / confirm / off).
**Autonomy:** Craftsman / checkpoint (sign-off each non-trivial step).
**Persona:** Tinkerbuddy.

---

## Notes

*(Observations about this operator that don't fit above — working style, recurring
preferences, things to remember. Append; do not overwrite.)*

- TODO: fill in as sessions accumulate.
