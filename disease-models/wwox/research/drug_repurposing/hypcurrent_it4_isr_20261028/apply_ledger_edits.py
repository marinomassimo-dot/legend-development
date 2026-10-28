#!/usr/bin/env python3
"""Apply the HYPCURRENT ledger edits (old_str -> new_str pairs) to a copy of the hypotheses ledger.

Each old_str must occur exactly once at the moment it is applied, in order; the run is all or
nothing. Default is a dry run that reports; --write rewrites the target file.
Usage: apply_ledger_edits.py LEDGER_PATH [--edits ledger_edits.json] [--write]
"""
import argparse, json, pathlib, sys

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("ledger")
ap.add_argument("--edits", default=str(pathlib.Path(__file__).with_name("ledger_edits.json")))
ap.add_argument("--write", action="store_true")
a = ap.parse_args()
p = pathlib.Path(a.ledger)
s = p.read_text(encoding="utf-8")
for i, e in enumerate(json.loads(pathlib.Path(a.edits).read_text(encoding="utf-8"))):
    n = s.count(e["old_str"])
    if n != 1:
        sys.exit(f"edit {i}: old_str occurs {n} times (need exactly 1): {e['old_str'][:70]!r}")
    s = s.replace(e["old_str"], e["new_str"])
if a.write:
    p.write_text(s, encoding="utf-8")
print("all edits apply" + (" and were written" if a.write else " (dry run)"))
