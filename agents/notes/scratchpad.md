<!-- Working space, checked every session — see README. Carry-forward (top): what the next session must know, kept tight. Working space (below the line): live threads, pruned at session end. Size governed by the traffic-light (SPEC-003 §10, ADR-002). -->

## Carry-forward

- README documentation pass is partway done. `agents/` fully complete (4 subfolder READMEs + index + slimmed files). NEXT: `docs/*` READMEs (specs, plans, sessions, decisions, research — give the structure/convention each file must follow, do NOT list individual files) and bare-scaffold READMEs (src/, docs/tests/, tools/).
- Established pattern to follow: loaded/skeleton files keep ONE self-explanatory comment line; all explanation lives in the per-directory README (READMEs may be long). Soft-wrap everywhere (one line per paragraph); data lines stay one-per-record.
- Document convention now settled (session 12 / ADR-002): line 1 = `filename | keywords`, abstract to first `##`, no Related: fields, two size classes + traffic-light. The docs/* READMEs above must follow and document this.
- Operator prunes the AGENTS.md brainstorm half (below the separator) himself — do not touch it.

---

## Working space
