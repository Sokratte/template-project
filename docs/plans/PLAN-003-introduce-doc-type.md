<!-- keywords: new document type, introduce doc type, TEST, ADR SPEC PLAN TEST chain, docs README registration, template, status vocabulary, workflow integration -->
PLAN-003-introduce-doc-type.md

# PLAN-003: Introducing a New Document Type

**Status:** Plan ready
**Created:** 2026-06-24 · **Updated:** 2026-06-24

The project recognises six document types (DP, ADR, SPEC, PLAN, Research, Session). Adding a seventh — or any future type — should follow one fixed procedure so the type is discoverable, consistently formatted, and wired into the existing workflow rather than bolted on. This plan is that procedure, written generically and illustrated with a worked example: a **TEST** type that closes the chain ADR → SPEC → PLAN → TEST. It does not build any suite; it defines how a type is introduced.

## Goal

A repeatable, sign-off-gated procedure for adding a document type: where it is registered, what it must declare, and how it joins the ADR → SPEC → PLAN → TEST workflow — such that the next person adding a type copies this plan rather than reverse-engineering the conventions.

## Non-goals

- NOT implementing the TEST type's tooling (a test runner, CI, a suite) — that is separate work, decided on its own merits, never folded into this plan.
- NOT changing the existing six types.
- NOT adding any automation to session-start or session-end as part of introducing a type.

## The workflow the type joins

The four numbered types form a chain, each answering one question:

- **ADR** — *why*: a decision is taken and recorded.
- **SPEC** — *what*: the decision becomes a target the code is judged against.
- **PLAN** — *how*: the target gets an execution path.
- **TEST** — *verified*: the plan's acceptance criteria become a named, runnable check (the document registers it; the executable lives in `tests/`).

A new type must state where in this chain (or beside it) it sits, so a reader knows what it answers and what precedes/follows it. DP and Research sit beside the chain (principle and prior art); Session logs record passage of time. TEST extends the chain to the right.

## Procedure — six steps, sign-off on each

1. **Decide the type is warranted.** One sentence on what question it answers that no existing type does. If an existing type covers it, stop — extend that type instead. (Structural economy: a type that overlaps another is drift waiting to happen.)
2. **Register it in `docs/README.md`.** Add a row to the types/location table (location `docs/<plural>/`, naming `XXX-NNN-topic-slug.md` or dated), a row to the status-per-type table (the subset of the master status vocabulary that makes sense — e.g. TEST: Draft · Active · Superseded →), and an entry in the section matrix if it introduces structural sections.
3. **Write the template block** in `docs/README.md` following the line-1 + hidden-keyword rules: line 1 `<!-- keywords: … -->`, line 2 the bare filename, the standard head block, content headings that *are* the summary. The template must read like a finished document — no instructional prose inside it.
4. **Create the directory and its README**, stating in two sentences what the directory holds and pointing to the type rules in `docs/README.md`. Add `-000-template.md` if the type benefits from a copyable skeleton.
5. **State the workflow hook, if any.** Most types need none. If the type must be produced or checked at a defined moment (e.g. a TEST registered when a PLAN completes), name that hook here and raise it as a *separate* decision — do not wire it in as part of registration.
6. **Record it.** CHANGELOG entry under Added; note the new type in the relevant ADR if it changes a standing convention.

## Worked example — the TEST type

- *Answers:* did the plan's acceptance criteria actually hold? Closes ADR → SPEC → PLAN → **TEST**.
- *Location / naming:* `docs/tests/`, `TEST-NNN-topic-slug.md`.
- *Status subset:* Draft · Active · Superseded → (mirrors SPEC — a test target is living).
- *Content boundary:* the document registers a suite and records what each check guarantees and why; the executable code lives in `tests/`. A document that contained the test logic, or merely described tests in prose, would be theatre.
- *Workflow hook:* optional and separately decided — e.g. a SPEC's acceptance criteria gain a TEST when its PLAN completes. Not introduced by this plan.

## Acceptance criteria

The procedure above can be followed start to finish by someone who has not seen the conventions, producing a type that is registered in `docs/README.md` (all three tables + template), has a directory + README, and declares its place in the chain — with no workflow automation added unless separately signed off.
