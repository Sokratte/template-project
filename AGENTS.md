<!-- ================================================================
     SETUP GUIDE — FOR THE AGENT CREATING A NEW PROJECT
     ================================================================
     Read this top-to-bottom. Follow every step. When done, delete
     everything from the top of the file down to "--- END OF SETUP ---".
     What remains is the project's permanent AGENTS.md.

     Do NOT work inside ~/workspace/template-project/.
     That folder is the template. You are working in the copy.
     ================================================================ -->

# New Project Setup Guide

You are setting up a new project from the workspace template. This guide
walks you through it as a conversation with the user — not a checklist you
rush through silently. Take your time. The decisions made now shape every
session that follows.

---

## Step 0 — Verify location

Confirm you are NOT inside `~/workspace/template-project/`. Run `pwd` and
check. If you are in the template folder, stop — copy it first:
```
cp -r ~/workspace/template-project ~/workspace/projects/<n>
```
Then `cd` into the copy and continue.

---

## Step 1 — Understand what the user wants to build

Before touching any file, have a short conversation. Ask the user:

1. **What** are you building? (one sentence)
2. **Who** is it for? (yourself, a team, the public?)
3. **What kind** of project is it? (app, library, server, content, hardware?)
4. **Where** does it run? (local only, server, cloud, embedded?)
5. **What should it explicitly NOT be?** (scope boundaries, anti-goals)

Listen to the answers. You will use them to fill in the project description,
select optional sections, and calibrate your domain research. Do not proceed
until you have clear answers to at least questions 1, 3, and 5.

---

## Step 2 — Create the GitHub repository

You cannot create the repo yourself — it requires the user's credentials.
Guide them through it:

> I need you to create a GitHub repository for this project. You can do this
> at github.com/new or by running `gh repo create` from the terminal.
> Once created, tell me the remote URL.

Once you have the URL:
```
git init
git remote add origin <URL>
```

Do NOT commit yet — we need to fill in files first.

---

## Step 3 — Fill in the permanent sections

Scroll down to "--- END OF SETUP ---". Below it is the permanent AGENTS.md.
Fill in every `TODO:` field using the answers from Step 1:

- Project name and description (2 sentences max)
- What this project is NOT (from question 5)
- Any project-specific git exceptions
- Remove the `TODO:` markers when done

---

## Step 4 — Create ADR-001: Project Definition

Open `docs/decisions/ADR-000-template.md`, copy it to `ADR-001-project-definition.md`.
Fill it in. This is the project's founding document:

- **Context:** Why does this project exist? What triggered it?
- **Decision:** What are we building, with what stack, for what audience?
- **Consequences:** What does this commit us to? What does it rule out?

The user must review and approve this before you continue.

---

## Step 5 — Select optional sections

Read the "OPTIONAL SECTIONS" block at the bottom of the permanent AGENTS.md.
For each section, decide whether it applies based on what you learned in
Step 1. Have a brief conversation — group obvious ones:

> "This is a Python server project, so I'll include Environment, Testing,
> Error Handling, and Services. I'll skip Before Writing Code since you're
> using TypeScript with static types. Sound right?"

Uncomment the sections you keep. Delete the ones you don't. Delete the
menu header and instructions too — they are setup scaffolding.
