<!-- keywords: session, multi-VM, architecture, PLAN-001, design -->
2026-06-17-008-multi-vm-architecture.md

# Session Log: Multi-VM Agent Architecture — design & PLAN-001

**Date:** 2026-06-17
**Project:** template-project
**Goal/outcome:** Designed the multi-VM agent architecture from scratch and
captured it as PLAN-001. No implementation yet — architecture only.

## What happened

Worked through the architecture for deploying this template across multiple
(often non-technical) users' VMs, one agent per VM, many projects. Reached a
locked design after iterative pushback on several points.

Key decisions:
- **Hybrid instruction model:** one canonical `~/projects/AGENTS.md` +
  optional small `AGENTS.override.md` per project (override wins). Rejected
  per-project forked files (drift) and pure-global (no escape hatch).
- **Root is `~/projects/`** (flat); project list **derived from folders**,
  never stored. `ls -d ~/projects/*/ | xargs -n1 basename`.
- **Configs are files:** `~/projects/.projects` (global, VM backup prefs),
  `<project>/.project` (per-project; gitignored — references key paths).
- **Backup is provider-agnostic**, keyed on config; `backup: none` →
  silent local-only git, word "git" never shown to user. SSH **deploy keys
  per repo** in `~/.ssh/`, never in tree; agent never creates remotes (no
  tokens); operator registers public keys + enables write at VM build.
- **Sync mechanism:** visible VM-local `agents_sync.sh` copies canonical
  `AGENTS.md` into each project bearing a `.agents_sync` marker. Copy command
  is deliberately NOT in `AGENTS.md` (else a cloner's agent overwrites the
  cloner's own file every session). In-project `AGENTS.md` is a committed
  generated artifact → portability for cloners; marker gating protects
  foreign repos.
- **Autonomy preference** (`autonomous`/`checkpoint`/`confirm`) recorded per
  project in `.project`.

Resolved at close: `~/projects/` is NOT a git repo (canonical files
hand-maintained). Accepted that editing canonical `AGENTS.md` yields a
committed diff in every marked repo on next sync (intended). Autonomy level
names + new-project default deferred to next session.

## State at close

- PLAN-001 written and finalized at
  `docs/plans/PLAN-001-multi-vm-agent-architecture.md`.
- No code/scaffold changes made. AGENTS.md itself not yet drafted.

## Open / next session

1. **Draft the canonical `AGENTS.md`** (per the operator's sign-off-each-step
   rule — nothing written without approval). First sub-decisions: autonomy
   level names + new-project default; the ~150-line budget split.
2. **Separate deferred cleanup task** (not started): reconcile stale doc
   path references to on-disk names; remove `sweep-knowledge.py` and fold its
   decay logic into `session-end.md`; drop phantom `daily-digest.md` ref.
