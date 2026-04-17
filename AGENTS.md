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
