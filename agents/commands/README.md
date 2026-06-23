# agents/commands/ — executable session procedures

Two procedures the agent **runs**, not just reads: one to open a session, one to close it. Unlike `agents/memory/` and `agents/notes/`, where the explanation lives in the README and the files stay near-empty, here the steps *are* the content — the agent executes them in order. So this README does not duplicate the steps; it explains what these files are and when they run. The steps themselves stay in the files, because a procedure with its body moved out would execute as nothing.

| File | Role | When it runs | Triggered by |
|------|------|--------------|--------------|
| `session-start.md` | Orientation — check state, read the last session, look for a spec, scaffold today's session log | At the start of every session, after the project is loaded | The exec-2 startup call (defined in `~/projects/AGENTS.md`) loads this file; the agent then executes its steps |
| `session-end.md` | Closing — write the session log, reconcile the ledger, prune the scratchpad, update memory, commit and push | Before the agent says "done" | The agent at wrap-up, or an explicit operator close signal |

## Where the startup sequence is defined

These files are only the *project-level* half of a session. The two-call bootstrap that loads them — exec-1 (VM level: sync, read `AGENTS.md` + `LOCAL.md`, list projects, pick one) and exec-2 (project level: load the guaranteed set including `session-start.md`) — is documented in `~/projects/README.md` and `~/projects/AGENTS.md`, because it runs *before* these files are read and cannot describe its own loading. `session-start.md` picks up right after exec-2, at its first numbered step.

`session-end.md` is the mirror at the other end. It is not loaded at start; the agent opens and follows it when wrapping up. Every step is mandatory and none is deferred to "next session" — the closing discipline is what makes a session auditable and lets the next one resume cleanly.

## Why both are non-negotiable

The session log created in `session-start.md` and filled in `session-end.md` is the operator's only durable record of what happened in a session. Skipping either end leaves work invisible. The same applies to the ledger move, the scratchpad prune, and the commit/push: each step exists because skipping it once caused a concrete loss — most sharply the push step, since an unpushed commit is a silent data-loss risk on a shared working copy.

## Editing these files

These are procedures under version control, edited deliberately and rarely. When you change a step, check whether `AGENTS.md`, `ROADMAP.md`, or the system spec in `docs/specs/` reference it — the startup/shutdown contract is described in several places and they must not drift apart. Prefer updating a step in place over rewriting the file from scratch.
