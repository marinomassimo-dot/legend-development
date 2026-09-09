#!/usr/bin/env python3
"""Measurement behind proposal §4.1 of 2026-09-09_receipt_schema_proposals.md.

Read-only. Numbers move; re-run rather than quoting the table.
Run from the repository root: python3 framework/protocols/proposals/measure_4_1.py
"""
import os, sys, pathlib
_ROOT = pathlib.Path(__file__).resolve().parents[3]
os.chdir(_ROOT)
sys.path.insert(0, str(_ROOT / "framework/scripts"))
import sys, pathlib
import fulltext_receipts as R

RANK = {"not_read": 0, "unknown_legacy": 0, "captions_only": 1,
        "unavailable": 2, "not_present": 2, "read": 3}

def complete_qualified(cov):
    """Exactly the predicate validate_receipt enforces for complete_fulltext_read."""
    vals = {cov.get(k, "not_read") for k in R.COVERAGE_KEYS}
    return (not ({"not_read", "unknown_legacy", "captions_only"} & vals)) and "read" in vals

rows = R.load_ledger(pathlib.Path('disease-models/wwox/registries/fulltext_read_receipts.jsonl'))
active = R.active_receipts(rows)
by = {}
for r in active:
    s = r['study_id']
    by.setdefault(str(s.get('pmid') or R.normalise_doi(s.get('doi'))), []).append(r)

gap = []
for k, g in sorted(by.items()):
    if max(R.DEPTHS[r['evidence_depth']] for r in g) >= R.DEPTHS['complete_fulltext_read']:
        continue
    union = {}
    for r in g:
        for sec, st in r['coverage'].items():
            if RANK.get(st, 0) > RANK.get(union.get(sec, "not_read"), 0):
                union[sec] = st
    if complete_qualified(union):
        gap.append((k, g, union))

print(f"studies with at least one active receipt : {len(by)}")
print(f"studies union-complete but recorded partial : {len(gap)}")
for k, g, union in gap:
    print(f"  PMID {k}: {len(g)} receipt(s) -> " + ", ".join(
        f"{r['event_id']}({r['evidence_depth'][:8]})" for r in g))
receipts_cited = sum(len(g) for _, g, _ in gap)
print(f"receipts that a rollup would cite as parents : {receipts_cited}")
print(f"receipts whose own meaning changes under the additive design : 0 (none is rewritten)")

print()
print("--- the same measurement, with parents restricted to actual full-text readings ---")
strict = []
for k, g in sorted(by.items()):
    if max(R.DEPTHS[r['evidence_depth']] for r in g) >= R.DEPTHS['complete_fulltext_read']:
        continue
    eligible = [r for r in g
                if R.DEPTHS[r['evidence_depth']] >= R.DEPTHS['partial_fulltext_read']]
    if not eligible:
        continue
    union = {}
    for r in eligible:
        for sec, st in r['coverage'].items():
            if RANK.get(st, 0) > RANK.get(union.get(sec, "not_read"), 0):
                union[sec] = st
    if complete_qualified(union):
        strict.append((k, eligible))
print(f"studies union-complete, parents >= partial_fulltext_read : {len(strict)}")
for k, g in strict:
    print(f"  PMID {k}: {len(g)} parent receipt(s)")
print(f"receipts cited as parents : {sum(len(g) for _, g in strict)}")
