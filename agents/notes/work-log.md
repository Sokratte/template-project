# Work Log — Done History

2026-06-17 | META       | [DONE]    | PLAN-001 multi-VM agent architecture finalized | docs/plans/PLAN-001-multi-vm-agent-architecture.md
2026-06-17 | META       | [DONE]    | Session-08 log written | docs/sessions/2026-06-17-session-08-multi-vm-architecture.md
2026-06-17 | DESIGN     | [DONE]    | AGENTS.md content decisions locked in PLAN-002 (startup flow, 3-tier read, abstract convention, backlog/log split) | docs/plans/PLAN-002-agents-md-authoring.md
2026-06-17 | DOCS       | [DONE]    | Repo restructure committed as moves; tree clean | -
2026-06-18 | DOCS       | [DONE]    | Renamed worklog->work-backlog, worklog-archive->work-log (git mv, history preserved, 4a00939) | agents/notes/
2026-06-18 | DESIGN     | [DONE]    | Session-10 architecture: OPERATOR.md replaces .projects; .project eliminated (push+autonomy->override); persona/autonomy model (Operator/Craftsman/Reviewer/Custom, default Craftsman/checkpoint/Tinkerbuddy); recent_sessions.sh; chmod 444 sync | docs/plans/PLAN-001-multi-vm-agent-architecture.md
2026-06-18 | DOCS       | [DONE]    | Updated PLAN-001, PLAN-002, SPEC-003 for session-10 architecture | docs/
2026-06-18 | DOCS       | [DONE]    | Rewrote session-start, session-end, README, procedural.md (profile removed), operational.md (sweep ref), work-ledger headers | agents/
2026-06-18 | INFRA      | [DONE]    | Verified new fs layout: root is ~/projects/, allowed dirs /Users/martin/projects + /recovery; sweep-knowledge.py gone from git; session-10 log present. Corrected stale ~/workspace path via memory edit. | -
2026-06-18 | INFRA      | [DONE]    | Created ~/projects/OPERATOR.md (profile + VM facts + tz Europe/Berlin + persona/autonomy); PII, never committed | OPERATOR.md
2026-06-18 | DOCS       | [DONE]    | Confirmed sweep-knowledge.py removed from git (not just working tree) | -
2026-06-18 | DOCS       | [DONE]    | README documentation pass for agents/ (memory, notes, commands, rules + index); skeleton files slimmed to one self-explanatory line; soft-wrap applied throughout | agents/
2026-06-18 | DOCS       | [DONE]    | Relocated bootstrap: exec-1 -> ~/projects/README.md (new), exec-2 -> canonical header in ~/projects/AGENTS.md (separator above brainstorm); session-start.md preamble removed | ~/projects/
2026-06-18 | DOCS       | [DONE]    | Renamed SPEC-002-dev-mcp-server -> SPEC-XXX and moved to ~/projects/ (project-foreign, linked nowhere) | -
2026-06-18 | DESIGN     | [DONE]    | Settled line-1 index convention for all 5 doc types (`filename | keywords` + abstract to first ##); dropped all Related: fields (keywords are the relationship graph) | docs/sessions/2026-06-18-session-12-document-conventions.md
2026-06-18 | DESIGN     | [DONE]    | ADR-002 document-size-governance: two classes (skeleton/content) by load behaviour, yellow/red traffic-light, no automatic deletion; recall counter kept as human reading-aid; supersedes decay sweep | docs/decisions/ADR-002-document-size-governance.md
2026-06-18 | DOCS       | [DONE]    | Updated SPEC-003 for ADR-002: §4, §7.3, §8.2-8.5 (sweep removed), §9.1-9.2, §10 (Document Budgets -> Document System); reconciled/extended as the system spec | docs/specs/SPEC-003-agent-memory-system.md
2026-06-18 | DOCS       | [DONE]    | Updated session-start/session-end for traffic-light + operator-decided pruning + line-1 format | agents/commands/
2026-06-18 | DOCS       | [DONE]    | Converted ADR-001 to new line-1 index + abstract format | docs/decisions/ADR-001-project-standard.md
2026-06-18 | INFRA      | [DONE]    | Rewrote recent_sessions.sh to print project name from path (3 newest sessions) for selection, not head-1 prose | recent_sessions.sh
2026-06-18 | DOCS       | [DONE]    | Wrote docs/README.md: source of truth for the doc format (read moves, line-1 convention, abstract rule, two classes, canonical template block for all 5 types) | docs/README.md
2026-06-18 | DOCS       | [DONE]    | Restored Created/Updated dates on ADR-001/002 (carelessly dropped session 12); unified head order Status->Created->Updated for ADR/SPEC/PLAN; PLAN gained a Status field | docs/decisions/, docs/README.md
2026-06-18 | DOCS       | [DONE]    | Converted SPEC-001 + SPEC-003 to spec format (line-1 index, Status-only head corrected from wrong first attempt, goal folded into abstract, Related dropped) | docs/specs/
2026-06-18 | DOCS       | [DONE]    | Converted research doc to new format (# Research:, Scope only, abstract as short answer) | docs/research/2026-04-17-project-structure-standards.md
2026-06-18 | DOCS       | [DONE]    | Trashed ADR-000 + SPEC-000 templates (canonical shapes now live in docs/README.md) | .trash/
2026-06-18 | DESIGN     | [DONE]    | ADRs declared not-immutable: supersede-in-place (mark passage, set Status, dated Addendum), check blast radius, never silent rewrite | docs/README.md
2026-06-18 | DESIGN     | [DONE]    | Spec status reduced to Draft/Active/Superseded; status tracks document not implementation; removed Move-to-archive-when-done; SPEC-001 Done->Active | docs/README.md, docs/specs/SPEC-001-template-standard.md
2026-06-18 | INFRA      | [DONE]    | Moved agents_sync.sh + recent_sessions.sh to ~/projects/ root (VM-local, not committed into projects) | ~/projects/agents_sync.sh, ~/projects/recent_sessions.sh
2026-06-18 | DOCS       | [DONE]    | Authored canonical ~/projects/AGENTS.md Part 1 (general orientation, ~473 tok): stripped explanatory prose, autonomy defs, git block, anecdotes; precised do-not-act rule to own-initiative only; removed duplicate memory section | ~/projects/AGENTS.md
2026-06-18 | DOCS       | [DONE]    | Created template AGENTS.override.md (defaults Craftsman/checkpoint/Tinkerbuddy/push + override-wins header); added override-carries line to ~/projects/README.md | template-project/AGENTS.override.md, ~/projects/README.md
2026-06-19 | AGENTS     | [DONE]    | Merged global.md into canonical AGENTS.md (universal craft + git rules); moved global.md to .trash; resolved the architecture-duplication and global.md-overlap FINDs | ~/projects/AGENTS.md, .trash/global.md
2026-06-19 | AGENTS     | [DONE]    | Slimmed AGENTS.override.md to four settings; moved conventions/anti-patterns to OPERATOR.md; added platform line | template-project/AGENTS.override.md, ~/projects/OPERATOR.md
2026-06-19 | INFRA      | [DONE]    | Wrote MCP file-tool design research doc (4 tools, git-diff guard, atomic temp+rename, diff-in-result) | docs/research/2026-06-19-mcp-file-tool-design.md
2026-06-19 | AGENTS     | [DONE]    | session-start.md: removed git-state + last-session-log steps, added Abschluss-Signal trigger; operational.md: added Git recovery section | agents/commands/session-start.md, agents/memory/operational.md
2026-06-19 | DOCS       | [DONE]    | Defined skeleton-file token thresholds (green/yellow/red); ADR-002 deferred numbers now set in OPERATOR.md, derivation recorded in research doc | OPERATOR.md, docs/research/2026-06-19-context-budget-and-file-limits.md
