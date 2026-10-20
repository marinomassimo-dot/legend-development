#!/usr/bin/env python3
"""Which sections of a paper are STILL owed, counted across every receipt and every staged receipt.

WHY THIS EXISTS (2026-10-20, HELD-PARTIAL-WWOX-C). A selection file listed "HELD-partial" rows from a
receipt that was no longer the latest, so about half the rows named debts that a later wave had
closed, and the 'owed' column of `paper_packet.py` is computed from the LATEST receipt only, which can
be a supplement-only producer receipt that makes the whole body look unread. This tool answers one
question with one rule: for each PMID, the best state each section has reached in ANY contemporaneous
receipt (ledger or staged), and which sections remain below `read`.

Rank (best wins): read > not_present > captions_only > unavailable > not_read > unknown_legacy.
`not_present` and `unavailable` are not debts. `references` is reported separately because a
references-only debt is not a reason to reopen a paper. A staged receipt is attributed to its actor
directory so that two Scientists do not re-read the same paper in one batch.

Read-only. Never writes the ledger. Usage:
    python3 framework/scripts/owed_sections.py [--ledger PATH] [--staging DIR] [--pmid PMID] [--json]
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

RANK = {"read": 5, "not_present": 4, "captions_only": 3, "unavailable": 2, "not_read": 1,
        "unknown_legacy": 0, "unknown": 0}
DEBT = {"captions_only", "not_read", "unknown_legacy", "unknown"}


def _key(study_id: dict) -> str:
    return str(study_id.get("pmid") or study_id.get("doi") or "")


def load(ledger: Path, staging: Path | None):
    events = []
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if line.strip():
            e = json.loads(line)
            events.append(("ledger", e))
    if staging and staging.is_dir():
        for f in sorted(staging.glob("*/*.json")):
            events.append((f.parent.name, json.loads(f.read_text(encoding="utf-8"))))
    return events


def census(events):
    best = defaultdict(dict)
    meta = defaultdict(lambda: {"sources": set(), "latest": None})
    for src, e in events:
        k = _key(e.get("study_id", {}))
        if not k:
            continue
        meta[k]["sources"].add(src)
        meta[k]["latest"] = e.get("event_id")
        if e.get("record_kind") == "legacy_reconstruction":
            continue
        for sec, st in (e.get("coverage") or {}).items():
            if RANK.get(st, -1) > RANK.get(best[k].get(sec), -2):
                best[k][sec] = st
    out = {}
    for k, cov in best.items():
        owed = {s: v for s, v in cov.items() if v in DEBT and s != "references"}
        out[k] = {"owed": owed, "references": cov.get("references"),
                  "staged_by": sorted(s for s in meta[k]["sources"] if s != "ledger"),
                  "latest_event": meta[k]["latest"]}
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--ledger", default="disease-models/wwox/registries/fulltext_read_receipts.jsonl")
    ap.add_argument("--staging", default="disease-models/wwox/research/receipt_staging")
    ap.add_argument("--pmid")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    ledger = Path(a.ledger)
    if not ledger.is_file():
        print(f"ledger not found: {ledger}", file=sys.stderr)
        return 2
    res = census(load(ledger, Path(a.staging)))
    if a.pmid:
        res = {a.pmid: res[a.pmid]} if a.pmid in res else {}
        if not res:
            print(f"no receipt for {a.pmid}", file=sys.stderr)
            return 1
    else:
        res = {k: v for k, v in res.items() if v["owed"]}
    if a.json:
        print(json.dumps(res, indent=1, sort_keys=True))
    else:
        for k in sorted(res):
            v = res[k]
            owed = ", ".join(f"{s}={t}" for s, t in sorted(v["owed"].items())) or "none"
            st = f" staged_by={','.join(v['staged_by'])}" if v["staged_by"] else ""
            print(f"{k}\towed: {owed}\tlatest={v['latest_event']}{st}")
        print(f"{len(res)} paper(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
