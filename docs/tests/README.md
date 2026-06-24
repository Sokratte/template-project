# docs/tests/ — test registry
<!-- soft: 200 · hard: 400 -->

This directory holds **test documents** (`TEST-NNN-topic-slug.md`): one per executable suite. A test document registers a suite — it states what each check guarantees, why it exists, and how to run it. It does not contain the tests themselves.

The executable suites live in `tests/` at the project root as real code that reads the live repo. The split is deliberate: code does the testing, the document carries the rationale (kept out of the code, where it would be noise). See the TEST template and type rules in `docs/README.md`.
