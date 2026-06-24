<!-- keywords: memory system redesign, two-file model, per-session usefulness M/sessions_alive, autonomous promotion demotion, operational.md no-limit section index, historical.md removed, ADR-002 amendment, SPEC-003 update, memory_cutoff -->
2026-06-22-018-memory-lifecycle-redesign.md

## Session log

Started on four small items (operational.md searchability, a stale README quoting line-based limits, the line-1 unit, a blank-project spec question). These opened into a full redesign of the long-term memory system.

### Decided
- **Two files, not three.** `historical.md` removed (moved to `.trash/`). `operational.md` becomes the unlimited, section-indexed floor: every `## heading` carries a keyword list; demoted and stale knowledge lives there, greppable. `procedural.md` stays loaded + size-limited.
- **Per-session usefulness metric.** Tag `[sNN xM]` (born session NN, useful M times); `value = M / sessions_alive`, `sessions_alive = current_session - NN + 1`. Newborn = 1.00 (max). Sessions, not wall-clock.
- **One cutoff.** `memory_cutoff` in `AGENTS.override.md`, default 0.01. Prune when `value < cutoff`. Floor = default = cutoff, one number.
- **Autonomous lifecycle, no operator prompt.** Promote operational->procedural (topic-independent + M>=3 + value>=cutoff). Demote procedural->operational, size-triggered two-stage: over soft prune only sub-cutoff; over hard prune sub-cutoff then lowest survivors (tie-groups all-or-none) until under. Demote = move, never delete; operational has no limit so it always lands.
- **Oscillation guard:** promotion requires value >= cutoff, so a just-demoted rule cannot bounce straight back.
- **ADR-002 amended, not replaced** -- the no-automatism rule is superseded for the two memory files only. The amendment answers ADR-002 own two objections: the metric is session-time (newborns at 1.00 cannot be mistaken for stale), and demotion is reversible into an unlimited floor (nothing is ever lost).

### Built -- executable layer
- `session-end.md` step 5 rewritten (metric, two-stage prune, promotion/demotion, oscillation guard, autonomous).
- `agents/memory/README.md` rewritten for the 2-file model.
- `operational.md`: line-1 no-limit; `## heading - keywords:` section index; 5 entries migrated to `[s18 x1]`; added a python-heredoc-edit gotcha.
- `procedural.md`: tag `[sNN xM]`; word limit kept as prune trigger.
- `AGENTS.override.md`: `memory_cutoff: 0.01`.

### Built -- decision/doc layer
- `ADR-002` amended in place (2026-06-18 record preserved).
- `SPEC-003` sections 3, 8.1-8.5, 9.2, 10, header -> 2-file autonomous model.
- root `README.md` tree + `CREATE_PROJECT.md` memory section updated.

### Found / open
- **OPERATOR.md -> LOCAL.md rename still pending, now visible.** New text uses LOCAL.md; SPEC-003 / CREATE_PROJECT / README now mix both. ~19 files. Next session opener. -> backlog.
- Memory baselines (operational 500/1000 words, promotion M>=3, cutoff 0.01) are derived, not validated. -> backlog.
- Tag migration was lossy by necessity: old `[date xN]` recorded last-useful, not birth session; entries re-admitted as `[s18 x1]`. git blame could recover true birth if wanted.
- Stray `VM.local/README copy.md` looks like cruft. -> backlog.
- ADR-002 body still names historical.md (lines ~52, 68) -- intentional point-in-time record.

Committed: 5d6694d
