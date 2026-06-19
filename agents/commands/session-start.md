# Session Start

Orient yourself before doing anything. Follow these steps in order.
**Execute them — do not merely read them.** They run after the project's
startup set has been loaded (see `AGENTS.md` for the loading call).

1. **Greet** the operator (use `OPERATOR.md`).
2. **Check for project memory outside the repo.** If you hold any memory of
   this project in parametric, in-context, or ephemeral memory, flag it to
   the operator: the repo is the single source of truth and implements
   filesystem-as-memory, so any memory alongside it creates two diverging
   sources.
3. **Check every growable skeleton file against its limit** — scratchpad,
   backlog, and the rest. Surface yellow (inform) and red (force a
   prune-or-defer decision) here, at the top of the session, so the operator
   can act before work starts.
4. **Build a working index.** Before serious work, grep line 1
   (`filename | keywords`) of every doc to learn what exists:
   `head -qn1 docs/{decisions,specs,plans,research,sessions}/*.md`.
5. **Prepare the session log scaffold.** Create
   `docs/sessions/YYYY-MM-DD-<topic>.md`. Line 1: `filename | keywords`.
   Fill it throughout the session; complete it at session end.

**Report to the operator** what is open: anything unresolved in the
scratchpad or backlog, so it doesn't fall through the cracks.

---

**Closing signal:** If the operator signals the session is over — done for
the day, signing off, saying goodbye or thanks, in any language — ask once
whether to close out the session. On yes, run
`agents/commands/session-end.md`. Do not remind, do not push — ask once and
wait.
