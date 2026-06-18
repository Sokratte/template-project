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
