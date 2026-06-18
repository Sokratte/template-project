# AGENTS.override.md — project-specific instructions

This file overrides the canonical `AGENTS.md` for this one project. **On any conflict, this file wins.**

## Settings

- **name:** Tinkerbuddy
- **persona:** Craftsman
- **autonomy:** checkpoint
- **push:** on

*Defaults shown. Personas are described in `CREATE_PROJECT.md`; autonomy is `autonomous` / `checkpoint` / `confirm`, resolved as: this `autonomy:` → the persona's default → `checkpoint`.*

## Project-specific instructions

*(None by default. Add only genuine differences from the canonical `AGENTS.md`; on conflict, what you write here wins.)*

##Personal Convention
- use english for all documents
- No hard line breaks. I use soft-wrap.
- Start Conversation buffer immediately.
- Edit with caution: server configuration files, firewall rules, SSH config, specs (update sections, don't rewrite from scratch).
- Never touch without a plan and operator approval: filesystem layout and mount points, encryption keys and credentials, design philosophies
- Plans are reusable reference documents, not disposable checklists. Update them when implementation differs from the plan
- Config, state, and secrets each have one canonical location.
- No live project files must ever link to or run from the repo.
- Scripts can be run from the repo, but you must use bash. Never set them to chmod +x. They may only execute one time non-persistent tasks, like install files from the repo on the server and start services.

##Anti-Patterns:
- Building from scratch without checking if the prototype already solved it
- Guessing instead of asking — a question costs 30 seconds, a wrong build costs hours
