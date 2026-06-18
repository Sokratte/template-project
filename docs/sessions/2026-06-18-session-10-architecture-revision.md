# 2026-06-18 · template-project · session 10 — architecture revision + doc propagation

**Task:** Continue PLAN-001/PLAN-002. Settle deferred architecture questions
(autonomy, persona, config-file model), propagate the resulting changes through
every affected doc, and write the two VM-local scripts.

**Outcome:** Major architecture revision locked and propagated. Operator profile
moved out of the repo (PII → `~/projects/OPERATOR.md`); both standalone config
files (`.project`, `.projects`) eliminated; persona/autonomy model defined.
All reachable docs updated to match. Two scripts written. Canonical AGENTS.md
still deliberately undrafted — moved to next session behind an fs-verification
step. Workspace relocated mid-session from `~/workspace/` to `~/projects/`.

---

## Decided (the substance of the session)

- **work-backlog / work-log renamed on disk** via `git mv` (commit `4a00939`),
  history preserved 100%.
- **Autonomy model:** `autonomous` / `checkpoint` (default) / `confirm`.
  Resolution: override `autonomy:` → persona default → hardcoded `checkpoint`.
  Agent does NOT ask at setup except for a Custom persona. Silent fallback
  (no token spent deliberating).
- **Persona model:** behavioral prompt-tuning, each with a default autonomy —
  Operator (`autonomous`) / Craftsman (`checkpoint`, default) / Reviewer
  (`confirm`) / Custom (asked). Personas defined by what they change in
  outputs, never risk-flavor. Full table in CREATE_PROJECT; chosen contract
  written to the override so it travels with clones.
- **Agent name:** operator-chosen, independent of persona, default
  **Tinkerbuddy**. New-project defaults: Craftsman / checkpoint / Tinkerbuddy.
- **`.project` eliminated.** Its fields were either derivable (`provider`,
  `repo_name`, `key_path` from a `~/.ssh/<project>` convention) or git's own
  (`remote_url` in `.git/config`). The two real toggles (`push`, `autonomy`)
  moved to `AGENTS.override.md`.
- **`.projects` reframed and renamed → `~/projects/OPERATOR.md`.** It was never
  a project registry; it is operator + VM identity. Markdown, never committed,
  never cloned. **Rationale is privacy:** the operator profile is PII and must
  not enter a backed-up, possibly public repo. It is also the per-VM seam that
  keeps the canonical AGENTS.md byte-identical across machines.
- **Operator profile single-homed.** Removed from `procedural.md` (now
  rules-only); its sole home is `OPERATOR.md`.
- **recent_sessions.sh** added to exec-1: prints `date | project | summary`
  for the 3 newest session logs across all projects, for greeting + project
  disambiguation.
- **Synced AGENTS.md is read-only (444)** with a "do not edit" header; the
  sync script owns the chmod u+w → cp → chmod 444 dance.

## Done

- **Plans updated:** PLAN-001 (session-10 revision: OPERATOR.md, config
  elimination, git-owns-remote table, persona/autonomy, Decisions 10–12,
  acceptance criteria) and PLAN-002 (checklist progress, exec pipelines,
  locked decisions).
- **SPEC-003 updated** (two passes): backlog/log split + append-only contract
  fix + >20-item alarm + decay-as-session-end-procedure (no script) + Claude
  symlink section removed + file map to real paths; then OPERATOR.md added to
  map, §8.1 rewritten rules-only, §9.1 two-call startup loading OPERATOR.md.
- **Procedures rewritten:** session-start.md (two-call world, OPERATOR.md in
  exec-1), session-end.md (backlog→log move, decay folded in, profile→
  OPERATOR.md).
- **Memory/notes:** procedural.md (profile removed), operational.md (sweep
  ref fixed), README.md (names + daily-digest dropped), work-backlog.md /
  work-log.md headers rewritten to correct contracts; stale [DONE] lines
  moved backlog→log.
- **CREATE_PROJECT.md:** scoped fixes per PLAN-002 — budgets/memory tables,
  Where-Things-Live, persona step (Step 2), OPERATOR.md step, git/backup,
  `~/projects` paths, `git add -A` removed. Full body rewrite deferred (depends
  on canonical AGENTS.md not yet authored).
- **Scripts written:** `agents_sync.sh` (marker-gated, chmod-444 dance),
  `recent_sessions.sh` (3 newest session-log head lines). Paths formed for
  `~/projects/`. Now present at `~/projects/` root.
- **Verified clean (no edit):** ROADMAP.md, SPEC-002.

## Open / next session

- **FIRST: verify the new fs is sound.** Workspace moved `~/workspace/` →
  `~/projects/` mid-session (allowed roots changed to `~/projects` + `~/recovery`).
  Confirm final layout: `OPERATOR.md`, both scripts, `AGENTS.md`,
  `AGENTS_MAC.md` (new, unexamined), template-project, and the real projects
  all present under `~/projects/`.
- Author canonical `~/projects/AGENTS.md` — the PLAN-002 headline deliverable.
- Confirm `sweep-knowledge.py` removed from git (working tree already clean).
- Confirm operator-profile lines made it into `OPERATOR.md` (they are in no
  committed file by design).

## State at close

Honest status: the docs now describe an architecture whose executable pieces
(canonical AGENTS.md, the live scripts wired into startup) are only partly in
place — scripts exist, AGENTS.md does not. Committed [DONE] items reflect
documentation completed, not a running system. Tooling note persists: sandbox
bash can't reach the real FS; use filesystem MCP for all project files, and
note `edit_file` (line-based) is now available for surgical edits.
Session log written late (after scripts) — operator caught the omission.
