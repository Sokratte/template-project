<!-- Working space, checked every session — see README. Carry-forward (top): what the next session must know, kept tight. Working space (below the line): live threads, pruned at session end. Size governed by the traffic-light (SPEC-003 §10, ADR-002). -->

## Carry-forward

- README documentation pass: `agents/` fully complete; `docs/README.md` now written (the doc-format source of truth). NEXT: the remaining `docs/*` per-directory READMEs (specs, plans, sessions, decisions, research — structure/convention each file must follow, NOT individual-file listings) and bare-scaffold READMEs (src/, docs/tests/, tools/).
- Established pattern to follow: loaded/skeleton files keep ONE self-explanatory comment line; all explanation lives in the per-directory README (READMEs may be long). Soft-wrap everywhere (one line per paragraph); data lines stay one-per-record.
- Document format is now fully settled and written in `docs/README.md` (sessions 12–13): line 1 = `filename | keywords`, abstract to first `##`, no Related: fields, head order Status->Created->Updated for ADR/SPEC/PLAN, spec status Draft/Active/Superseded, ADRs supersede-in-place. The remaining docs/* READMEs must follow and point to it — do not restate the format.
- PLAN-001/PLAN-002 are still in the old doc format (now a backlog item). Aligning them is mechanical; not urgent.
- Operator prunes the AGENTS.md brainstorm half (below the separator) himself — do not touch it.

---

## Working space
