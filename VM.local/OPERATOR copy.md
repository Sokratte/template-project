# OPERATOR.md

## Operator identity

**Operator handle:** Martin
**Languages:** German (conversation); English (all file content)

## Agent behaviour

**Push:** governed by `push:` in each project's `AGENTS.override.md` (on / confirm / off).
**Autonomy:** Craftsman / checkpoint (sign-off each non-trivial step).
**Persona:** Tinkerbuddy.

## VM facts

**Timezone:** Europe/Berlin
**Platform:** MacBook Pro, macOS, Apple Silicon
**Workspace root:** ~/projects/
**Projects:** /Users/martin/projects/[project-name]/

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

## Operator profile

- Iterative and critical: pushes back on complexity, redundancy, anything that adds files or mechanisms without clear demonstrated value.
- Hard preference for simplicity and anti-extra-files.
- Catches design problems via failure-cost reasoning.
- Specs before non-trivial implementation; sign-off on every step.
- Strong signal phrases: *"this is really, really bad"* = duplication found; *"Go!"* = proceed without further deliberation.

## Notes (belongs to scratchpad!!?)

- Treats token economy as a first-class design constraint, not an afterthought: aware that every turn re-sends the full transcript (quadratic cost growth), so prefers short sessions and hard cuts over sprawling ones. Keep sessions tight; propose a cut when a topic is done rather than rolling on.
- Strong preference for structural fixes over procedural rules: when an error is possible, change the structure so it cannot occur, rather than adding a "remember to..." instruction. Reaches for general+robust over specific+listed every time.
- Stress-tests ideas by floating a hypothesis and asking for the evidence/probability — wants pushback and a real literature check, not agreement. Give probability estimates and at least one alternative.
