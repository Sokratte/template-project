#!/usr/bin/env python3
"""Decay sweep for the operational memory file.

Deterministic, no LLM — pure arithmetic on the recall tags. Moves the
least-recalled entries from operational-memory.md to historical-memory.md
once the operational file exceeds a line threshold.

Memory model: operational memory entries carry a tag `[YYYY-MM-DD xN]` —
the date last recalled and a recall counter. The metric is
recall_rate = N / age_in_days. Lowest rates go first; whole tie-groups move
together; entries younger than 30 days are protected.

Procedural memory (procedural-memory.md) is NEVER swept — only the
operator retires a procedural rule or updates the operator profile.

Usage:
    python3 tools/scripts/sweep-knowledge.py            # dry-run
    python3 tools/scripts/sweep-knowledge.py --apply    # move them

Operator-gated. The session-end procedure runs the dry-run, shows the
operator the list, and only applies on an explicit yes.
"""

import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO_ROOT   = Path(__file__).resolve().parent.parent.parent
OPERATIONAL = REPO_ROOT / "agents" / "operational-memory.md"
HISTORICAL  = REPO_ROOT / "agents" / "historical-memory.md"

LINE_THRESHOLD  = 50
PROTECT_DAYS    = 30
ARCHIVE_HEADING = "## stale operations"

TAG_RE   = re.compile(r"\[(\d{4}-\d{2}-\d{2})\s+x(\d+)\]")
ENTRY_RE = re.compile(r"^- ")


def parse_entry(line: str):
    """Return (recall_rate, age_days, counter) or None if not sweepable."""
    m = TAG_RE.search(line)
    if not m:
        return None
    tag_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
    counter  = int(m.group(2))
    age      = max((date.today() - tag_date).days, 0)
    if age < PROTECT_DAYS:
        return None
    rate = counter / age if age > 0 else float(counter)
    return (rate, age, counter)


def main():
    apply = "--apply" in sys.argv
    if not OPERATIONAL.exists():
        print(f"no operational memory file at {OPERATIONAL}")
        return

    lines = OPERATIONAL.read_text("utf-8").splitlines()
    if len(lines) <= LINE_THRESHOLD:
        print(f"under threshold ({len(lines)} ≤ {LINE_THRESHOLD} lines) — nothing to do")
        return

    candidates = []
    for i, line in enumerate(lines):
        if ENTRY_RE.match(line):
            parsed = parse_entry(line)
            if parsed is not None:
                candidates.append((parsed[0], i, line))

    if not candidates:
        print("no sweepable entries (all protected or untagged)")
        return

    candidates.sort(key=lambda c: c[0])
    over    = len(lines) - LINE_THRESHOLD
    to_move = candidates[:over] if over < len(candidates) else candidates

    print(f"{len(lines)} lines, {over} over threshold. Would move {len(to_move)} entries:\n")
    for rate, _, line in to_move:
        print(f"  (rate={rate:.4f}) {line.strip()[:100]}")

    if not apply:
        print("\nDry-run. Re-run with --apply to move these.")
        return

    move_indices = {i for _, i, _ in to_move}
    kept  = [l for j, l in enumerate(lines) if j not in move_indices]
    moved = [l for _, i, l in to_move]

    OPERATIONAL.write_text("\n".join(kept) + "\n", encoding="utf-8")

    arch = HISTORICAL.read_text("utf-8") if HISTORICAL.exists() else f"{ARCHIVE_HEADING}\n"
    if ARCHIVE_HEADING not in arch:
        arch += f"\n{ARCHIVE_HEADING}\n"
    stamp = f"\n<!-- swept {date.today()} -->\n" + "\n".join(moved) + "\n"
    arch  = arch.replace(ARCHIVE_HEADING, ARCHIVE_HEADING + stamp, 1)
    HISTORICAL.write_text(arch, encoding="utf-8")

    print(f"\nMoved {len(moved)} entries to {HISTORICAL.name}.")


if __name__ == "__main__":
    main()
