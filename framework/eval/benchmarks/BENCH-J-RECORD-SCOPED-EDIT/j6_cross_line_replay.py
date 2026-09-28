#!/usr/bin/env python3
"""J6 — replay `record_scoped_edit.cross_line_moves` over J0's corpus and count the refusals.

🔴 WHY THIS IS A SCRIPT AND NOT A SENTENCE IN A COMMIT MESSAGE
-------------------------------------------------------------
`CROSS_LINE_MOVE` refuses an edit that re-parents content from one statement line of the addressed
record onto another (`record_scoped_edit.py`, `MOVED_BYTES_FLOOR`). An invariant that refuses a
fifth of real batch history is not shippable, and the number — not the argument — is the decision.
So the number is re-derivable: this replays the invariant over the 72 historical (commit, file)
events J0 recorded, at several byte floors, and prints how many CHANGED RECORDS each floor would
have refused. It reads git history and writes nothing.

Measured 2026-09-28 on `7352d52`, 72 events / 337 changed records:

    floor  40 B → 23 records (6.82 %)     floor 120 B → 0
    floor  80 B →  2 records (0.59 %)     floor 200 B → 0   (shipped)
                                          floor 400 B → 0

`B2`'s own moved run is 487 bytes, so the shipped floor leaves margin on both sides: ~2.4× above
the last floor that reported anything, and ~2.4× below the defect it exists to catch.

    python3 framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/j6_cross_line_replay.py
    python3 .../j6_cross_line_replay.py --floors 40 200 --since 2026-09-01   # recent history too

Exit codes: 0 replayed · 2 the corpus or the repository is unreadable.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
import record_scoped_edit as rse  # noqa: E402
import registry_records as rr  # noqa: E402

CORPUS = HERE / "j0_corpus.json"
RECORD_SCOPED = (
    "disease-models/wwox/registries/working_model_current.md",
    "disease-models/wwox/registries/claim_registry_current.md",
    "disease-models/wwox/registries/literature_tracking_log_current.md",
    "disease-models/wwox/registries/paper_registry_current.md",
)


def blob(commit: str, path: str) -> str | None:
    """One file at one commit, or None where that pair does not exist (a file added later)."""
    done = subprocess.run(["git", "-C", str(ROOT), "show", f"{commit}:{path}"],
                          capture_output=True, check=False)
    return done.stdout.decode("utf-8", "replace") if done.returncode == 0 else None


def corpus_events() -> list[tuple[str, str, str]]:
    """(parent, commit, file) for every non-duplicate event J0 recorded."""
    data = json.loads(CORPUS.read_text(encoding="utf-8"))
    return [(commit["parent"], commit["commit"], event["file"])
            for commit in data["commits"] if not commit.get("duplicate_of")
            for event in commit["files"]]


def recent_events(since: str) -> list[tuple[str, str, str]]:
    """The same shape, for commits touching the record-scoped files since a date."""
    events: list[tuple[str, str, str]] = []
    for rel in RECORD_SCOPED:
        log = subprocess.run(["git", "-C", str(ROOT), "log", "--format=%H",
                              f"--since={since}", "--", rel],
                             capture_output=True, check=False).stdout.decode()
        for sha in (line.strip() for line in log.splitlines()):
            parent = subprocess.run(["git", "-C", str(ROOT), "rev-parse", f"{sha}^"],
                                    capture_output=True, check=False)
            if parent.returncode == 0:
                events.append((parent.stdout.decode().strip(), sha, rel))
    return events


def replay(events: list[tuple[str, str, str]],
           floors: list[int]) -> tuple[int, int, dict[int, list[tuple[str, str, str, int]]]]:
    """(events read, changed records, {floor: [(commit, file, record, bytes moved)]})."""
    fired: dict[int, list[tuple[str, str, str, int]]] = {floor: [] for floor in floors}
    read = changed = 0
    for parent, commit, rel in events:
        before, after = blob(parent, rel), blob(commit, rel)
        if before is None or after is None:
            continue
        read += 1
        levels = rse.levels_for(rel)
        old = {b.key: before[b.start:b.end] for b in rr.partition(before, levels)}
        new = {b.key: after[b.start:b.end] for b in rr.partition(after, levels)}
        for key, text in old.items():
            successor = new.get(key)
            if successor is None or successor == text:
                continue
            changed += 1
            for floor in floors:
                moves = rse.cross_line_moves(text, successor, floor)
                if moves:
                    fired[floor].append((commit[:8], rel, key,
                                         max(len(run.encode()) for _a, _b, run in moves)))
    return read, changed, fired


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--floors", type=int, nargs="+", default=[40, 80, 120, 200, 400],
                        help="byte floors to replay (default: 40 80 120 200 400)")
    parser.add_argument("--since", default="",
                        help="also replay commits touching the record-scoped files since this "
                             "date — history J0 does not cover")
    args = parser.parse_args(argv)
    try:
        events = corpus_events() + (recent_events(args.since) if args.since else [])
    except (OSError, ValueError, KeyError) as error:
        print(f"TOOL ERROR: cannot read the corpus: {error}", file=sys.stderr)
        return 2
    read, changed, fired = replay(events, args.floors)
    print(f"replayed {read} (commit, file) event(s); {changed} changed record(s)")
    print(f"shipped floor: MOVED_BYTES_FLOOR = {rse.MOVED_BYTES_FLOOR}")
    for floor in args.floors:
        rows = fired[floor]
        share = f"{len(rows) / changed * 100:.2f}%" if changed else "—"
        counts = Counter(rel for _c, rel, _k, _b in rows)
        print(f"\nfloor {floor:>4} B → {len(rows):>3} changed record(s) refused ({share})")
        for rel, count in sorted(counts.items()):
            print(f"       {count:>4}  {rel}")
        for commit, rel, key, moved in rows[:20]:
            print(f"         {commit} {Path(rel).name} {key!r} — {moved} B moved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
