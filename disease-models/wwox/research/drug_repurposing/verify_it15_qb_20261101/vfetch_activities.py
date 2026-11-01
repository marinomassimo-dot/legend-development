#!/usr/bin/env python3
"""Fetch the ChEMBL IC50/Ki/Kd activities of one target (plain GET, at most 3 tries per page).

Reusable tool (class: reusable). `--help` and `import` touch neither the network nor the
disk; acquisition starts only from `main()`. The raw body is a third-party response (CC BY-SA
3.0): write it to the ignored corpus, never into a tracked package.

    vfetch_activities.py CHEMBL1904 --raw-dir files/<package>/raw
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
from pathlib import Path

BASE = "https://www.ebi.ac.uk/chembl/api/data"


def get(url: str, tries: int = 3, pause: float = 6.0):
    for attempt in range(tries):
        try:
            request = urllib.request.Request(url, headers={"Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except Exception as exc:  # a failed page is reported and retried, then the run stops
            print("fail", attempt, url[-80:], str(exc)[:60], flush=True)
            time.sleep(pause)
    return None


def fetch_all(target_id: str, limit: int = 200):
    """Return (total, rows, complete). `complete` is False when a page could not be fetched."""
    rows, offset, total = [], 0, None
    while True:
        page = get(f"{BASE}/activity.json?target_chembl_id={target_id}"
                   f"&standard_type__in=IC50,Ki,Kd&limit={limit}&offset={offset}")
        if page is None:
            print("STOP", offset)
            break
        batch = page["activities"]
        rows += batch
        offset += len(batch)
        total = page["page_meta"]["total_count"]
        if not batch or not page["page_meta"].get("next"):
            break
    return total, rows, total is not None and len(rows) >= total


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("target", help="ChEMBL target id, e.g. CHEMBL1904")
    parser.add_argument("--raw-dir", required=True, type=Path,
                        help="directory for acts_<target>_v.json (the ignored corpus, not a tracked path)")
    args = parser.parse_args(argv)
    total, rows, complete = fetch_all(args.target)
    if total is None:
        print(f"no page retrieved for {args.target}; nothing written", file=sys.stderr)
        return 1
    args.raw_dir.mkdir(parents=True, exist_ok=True)
    out = args.raw_dir / f"acts_{args.target}_v.json"
    out.write_text(json.dumps({"total": total, "rows": rows, "complete": complete}), encoding="utf-8")
    print(args.target, total, len(rows), len({r["activity_id"] for r in rows}),
          "complete" if complete else "INCOMPLETE")
    return 0 if complete else 1


if __name__ == "__main__":
    raise SystemExit(main())
