#!/usr/bin/env python3
"""Link receipt IDs cited in prose to the events actually in the receipt ledger.

Preparatory texts say "receipt staged" at the time they are written; the integrator records the
event later. This tool reads, never writes: for every FTR event ID cited under a directory it
reports whether the ledger holds it (and its depth), and which citing lines still say "staged"
or "not recorded" although the event exists. The ledger is never edited.

    receipt_linkage.py [--dir DIR] [--disease wwox] [--stale-only]
Exit 0 always; stale lines are reported, not failed (the prose is history).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fulltext_receipts as fr  # noqa: E402

ID = re.compile(r"FTR-\d{8}-\d+-\d+")
STALE = re.compile(r"staged|not (?:yet )?(?:in|recorded)|not in the ledger|until the integrator", re.I)


def scan(root: Path, directory: Path, disease: str):
    # plain JSONL read: schema and chain are fulltext_receipts.py verify's job, not this tool's
    ledger = {}
    for line in fr.default_ledger_path(root, disease).read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            ledger[r.get("event_id")] = r
    cited: dict[str, list[tuple[str, int, bool]]] = {}
    for f in sorted(directory.rglob("*.md")):
        for n, line in enumerate(f.read_text(errors="replace").splitlines(), 1):
            for i in set(ID.findall(line)):
                cited.setdefault(i, []).append((str(f.relative_to(root)), n, bool(STALE.search(line))))
    return ledger, cited


def render(root: Path, directory: Path, disease: str, stale_only: bool) -> str:
    ledger, cited = scan(root, directory, disease)
    rows, stale = [], []
    for i in sorted(cited):
        ev = ledger.get(i)
        state = f"RECORDED ({ev.get('evidence_depth', '?')}, {ev.get('event_at', '?')[:10]})" if ev else "NOT IN LEDGER"
        for path, n, s in cited[i]:
            if s and ev:
                stale.append(f"| `{i}` | {path}:{n} | {state} |")
        rows.append(f"| `{i}` | {state} | {len(cited[i])} |")
    out = [f"# Receipt linkage — {directory.relative_to(root)}", "",
           f"{len(cited)} distinct receipt IDs cited; {sum(1 for i in cited if i in ledger)} recorded in the ledger, "
           f"{sum(1 for i in cited if i not in ledger)} not; {len(stale)} citing lines still say staged/not-recorded for an event that exists.", ""]
    if stale:
        out += ["## Lines to read as superseded by the recorded event", "", "| Event | Citing line | Ledger |", "|---|---|---|", *stale, ""]
    if not stale_only:
        out += ["## All cited IDs", "", "| Event | Ledger | Citations |", "|---|---|---|", *rows, ""]
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dir", default="disease-models/wwox/research/drug_repurposing")
    ap.add_argument("--disease", default="wwox")
    ap.add_argument("--root", default=".")
    ap.add_argument("--stale-only", action="store_true")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    print(render(root, (root / a.dir).resolve(), a.disease, a.stale_only))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
