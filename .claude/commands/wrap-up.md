# Wrap Up

End-of-session protocol. Do all of these before saying "done."

1. **Session log:** Create or update `changelog/session-logs/YYYY-MM-DD-<topic>.md`
   Include: what was done, what was found, what broke, what is next.

2. **CHANGELOG.md:** Add entries under `[Unreleased]` for anything user-visible.
   Use the correct categories: Added, Changed, Fixed, Removed, Deprecated, Security.

3. **Plans cleanup:** If a task plan in `docs/plans/` is complete, delete it.
   If it is partially done, update it with current status and next steps.

4. **Tribal Knowledge:** If you learned something surprising during this session
   that a future agent would get wrong without being told, add it to the
   Tribal Knowledge section in AGENTS.md. Include date and category tag.

5. **Commit:**
   ```
   git add -A
   git status
   ```
   Show the user what will be committed. Wait for approval. Then:
   ```
   git commit -m "<type>(scope): <description>"
   git push origin main
   ```

6. **Report:** Tell the user what was accomplished and what remains open.
