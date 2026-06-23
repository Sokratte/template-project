<!-- kw: context window, context rot, lost in the middle, token budget, skeleton file limits, traffic-light, degradation, startup load, wc tokenizer, Sonnet 4.6, Chroma, U-curve, primacy recency -->
2026-06-19-context-budget-and-file-limits.md

# Context Budget and Skeleton-File Size Limits

**Scope:** How large the loaded-every-session skeleton files may grow, and why.
**Created:** 2026-06-19

The skeleton files (loaded in full at every session start) are governed by a
token budget, not a line budget — tokens are the honest unit of load cost.
This document derives the green/yellow/red thresholds used by the traffic-light
in `AGENTS.md`, from two facts: the usable context window is smaller than the
advertised one, and the start of the context is the most reliable position.
The thresholds it produces are a first baseline, to be tuned from practice.
The applied values live in `OPERATOR.md`; this document is the record of how
they were derived, so that changing the applied numbers never erases the
reasoning.

## Context window: advertised vs. usable

Advertised window for the model in use (Sonnet 4.6) depends on the interface:
200K tokens on claude.ai Free, 500K on Pro/Team, 1M on the API (beta). Working
assumption for this operator: the **500K** Pro window.

But the advertised number is not the usable number. Across long-context
research the consistent finding is that quality degrades well before the limit:
a model rated for 200K becomes unreliable around 130K, i.e. roughly **30–35 %
of the window is effectively lost**, and the drop tends to arrive abruptly
rather than gradually. A 2025 Chroma Research evaluation of 18 production models
(including Claude Sonnet) found monotonically falling accuracy as input grew,
with the steepest decline in the 100K–500K range, and no model holding uniform
retrieval accuracy across its full window.

**Usable budget for a 500K window ≈ 325K tokens.**

## Lost in the middle

Long-context models recall information at the **beginning and end** of the
context reliably, and lose information in the **middle** — a U-shaped accuracy
curve confirmed across many model families. The cause is architectural
(attention falls off with token distance; softmax concentrates on the
highest-scoring tokens), so it cannot be prompted away.

Direct consequence for this system: loading the skeleton files **at session
start** is correct by design — the primacy position is the most reliable zone
of the context. The cost of those files is therefore not that they might be
forgotten, but that they consume reliable budget on every session regardless of
how much work the session does.

## Token accumulation per session

Context grows every turn: `turn N = startup load + Σ(all prior turns) +
current prompt`. At a rough 1–2K tokens per exchange, the usable budget is
reached around 150–200 productive turns — ample for a normal working session.
The startup load is a fixed tax paid up front on all of them.

## Deriving the startup budget

If a session of 100 turns consumes ~135K tokens, a 10K-token startup load is
~7 % of that — acceptable. A 30K startup load would be ~22 % on every session,
short ones included — not acceptable. So the target is a **startup load under
~10K tokens**, which sets the sum of the red thresholds.

## Thresholds

Per-file green/yellow/red, in estimated tokens. Yellow = inform at session
start; red = halt and force a prune-or-defer decision. Both are language-level
only — no file is ever shrunk by a machine.

| File | Yellow | Red | Rationale |
|------|-------:|----:|-----------|
| `AGENTS.override.md` | 200 | 400 | Config only — must stay tiny |
| `agents/rules/project.md` | 500 | 1000 | Grows with the project |
| `agents/memory/procedural.md` | 1500 | 3000 | Legitimate slow growth |
| `agents/notes/scratchpad.md` | 600 | 1200 | Working memory — growth signals unfinished thinking |
| `agents/notes/work-backlog.md` | 800 | 1500 | ~20 items × ~50 tok ≈ 1K; past 1.5K the backlog is broken |
| `agents/commands/session-start.md` | 500 | 800 | Procedure — should stay stable and small |
| `ROADMAP.md` (loaded slice) | 800 | 1500 | Only the abstract + active section is loaded |
| **Sum** | **~4900** | **~9400** | Under the ~10K startup target |

## Measurement method

There is no exact tokenizer in the shell. Tokens are estimated from word count:
`tokens ≈ wc -w × 1.3`. The error is ~±10–15 %, which is fine for a
traffic-light. Example: `awk '/^## /&&++n==2{exit} 1' ROADMAP.md | wc -w` for
the loaded ROADMAP slice; plain `wc -w < FILE` for the rest.

## Status of these numbers

A derived baseline, not a measured optimum. They should be revisited after
about a week of real use; if a file is repeatedly green with huge headroom or
repeatedly nagging at yellow, the threshold is wrong, not the file.

## Sources

- Liu et al. 2024, *Lost in the Middle* (TACL) — U-shaped position accuracy.
- Chroma Research 2025 — 18-model long-context degradation evaluation.
- Anthropic, *Introducing Claude Sonnet 4.6* and Claude Help Center, context
  window sizes per plan.
- Surveys on "context rot" / context-length degradation, 2025.

## Startup index budget (session-15 addition)

The session-start index (line 1 of every doc) must fit inside the ~600-token
buffer remaining after the skeleton-file red-sum of ~9400 tokens. Line 1 is
roughly 15-20 tokens per document. Budget per doc type:

| Type | Cap | Sort | ~Tokens | Rationale |
|------|----:|------|--------:|-----------|
| decisions | all | alpha | ~170 | Slow-growing, always relevant |
| specs | all | alpha | ~135 | Manageable, always relevant |
| plans | all | alpha | ~100 | Manageable, always relevant |
| research | last 10 | date desc | ~170 | Older docs rarely needed at startup |
| sessions | last 5 | date desc | ~85 | Continuity only, not archive |
| **Total** | | | **~660** | Fits inside the ~600-token buffer (+-10%) |

The caps are for the automatic startup scan only. Older documents remain
accessible via targeted reads at any point during the session.

The index is loaded as the final step of session-start, so it sits at the
recency end of the primacy zone: captured reliably, and the operator's first
instruction still lands in the recency slot at the very end of the context.
