# Session Start
<!-- soft: 400 · hard: 600 -->

Orient yourself before doing anything. Follow these steps in order. **Execute them — do not merely read them.** They run after the project's startup set has been loaded (see `AGENTS.md` for the loading call).

1. **Greet** the operator (use `LOCAL.md`).
2. **Reconcile out-of-repo memory silently.** The repo is the single source of truth and implements filesystem-as-memory. If you hold any memory of this project from parametric, in-context, or ephemeral sources, treat the repo as authoritative and let your own diverging memory go.
3. **Prepare the session log scaffold.** Create `docs/sessions/YYYY-MM-DD-NNN-<topic>.md`. Line 1: `filename | keywords`.
4. **Build the startup index.** Read line 1 (`filename | keywords`) of every doc — this is the last step so it sits at the recency end of the startup load, just before the operator's first instruction:
   ```bash
   for f in \
     docs/decisions/*.md \
     docs/specs/*.md \
     docs/plans/*.md \
     $(ls -t docs/research/*.md 2>/dev/null | head -10) \
     $(ls -t docs/sessions/*.md 2>/dev/null | head -5); do
     [ -f "$f" ] && head -1 "$f"
   done
   ls -t docs/sessions/*.md | head -5 # Determine session log numbering
   ```
   Caps: all decisions/specs/plans; last 10 research; last 5 sessions. See `docs/research/2026-06-19-context-budget-and-file-limits.md` for the budget derivation (~660 tokens total).

**Report to the operator** what is open: anything unresolved in the scratchpad or backlog, so it doesn't fall through the cracks.

---

**Closing signal:** If the operator signals the session is over — done for the day, signing off, saying goodbye or thanks, in any language — ask once whether to close out the session. On yes, read and run `agents/commands/session-end.md`. Do not remind, do not push — ask once and wait.
