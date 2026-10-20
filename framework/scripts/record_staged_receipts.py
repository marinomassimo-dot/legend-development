#!/usr/bin/env python3
"""Record staged FULLTEXT_READ_RECEIPT JSON files into the ledger, in event-ID order, after a trial.

WHY THIS EXISTS (2026-10-20, metabolic batch, orchestrator)
-----------------------------------------------------------
Parallel Scientists stage receipts as JSON under research/receipt_staging/<actor>/ and the
Orchestrator records them. Seven times in one batch the same hand procedure ran: list the staged
receipts whose event is not in the ledger; make sure no `analysis_at` or `event_at` lies in the
future (the writer stamps `event_at` at record time and refuses `analysis_at` later than it);
trial-record the whole set in a throwaway clone; record for real in event-ID order; copy the
recorded form back over the staged file. This is that procedure, so that the trial is not skipped
and the time rule is applied the same way every time.

  python3 framework/scripts/record_staged_receipts.py            # dry: list, normalise, trial in a clone
  python3 framework/scripts/record_staged_receipts.py --apply    # then record for real

What it does NOT do: regenerate derived surfaces (batch_queue, coverage_report, reading_state,
pathograph) or commit. It prints the commands. A clone's `files/` is a hard-linked copy of this
checkout's evidence tree, because a symlink escapes the artefact workspace and fails validation.

Time rule (applied mechanically, reported per receipt): an `analysis_at` later than now is set to
the date of now at 00:00:00Z, and an `event_at` later than now is set to now. Content is untouched.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LEDGER = "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
STAGING = "disease-models/wwox/research/receipt_staging"


def recorded_ids(ledger: Path) -> set[str]:
    ids: set[str] = set()
    for line in ledger.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                ids.add(str(json.loads(line).get("event_id") or ""))
            except json.JSONDecodeError:
                pass
    return ids


def event_id(path: Path, receipt: dict) -> str:
    return str(receipt.get("event_id") or path.stem)


def normalise(receipt: dict, now: datetime) -> tuple[dict, list[str]]:
    """Return a copy whose timestamps are not in the future, and what was changed."""
    out = dict(receipt)
    changed: list[str] = []
    stamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    day = now.strftime("%Y-%m-%dT00:00:00Z")
    if str(out.get("analysis_at") or "") > stamp:
        out["analysis_at"] = day
        changed.append("analysis_at")
    if str(out.get("event_at") or "") > stamp:
        out["event_at"] = stamp
        changed.append("event_at")
    return out, changed


def unrecorded(root: Path, now: datetime) -> list[tuple[str, Path, dict, list[str]]]:
    have = recorded_ids(root / LEDGER)
    found = []
    for path in sorted((root / STAGING).glob("*/*.json")):
        receipt = json.loads(path.read_text(encoding="utf-8"))
        eid = event_id(path, receipt)
        if eid in have:
            continue
        fixed, changed = normalise(receipt, now)
        found.append((eid, path, fixed, changed))
    return sorted(found, key=lambda item: item[0])


def record(root: Path, receipt_file: Path) -> tuple[bool, str]:
    done = subprocess.run([sys.executable, str(root / "framework/scripts/fulltext_receipts.py"),
                           "record", "--receipt", str(receipt_file)],
                          cwd=root, capture_output=True, text=True)
    return done.returncode == 0, (done.stderr.strip().splitlines() or [""])[-1]


def trial(root: Path, work: Path, items) -> list[str]:
    clone = work / "trial_clone"
    subprocess.run(["git", "clone", "-q", str(root), str(clone)], check=True)
    # Hard links, not a symlink: a symlink "escapes the workspace" and fails artefact checks.
    subprocess.run(["cp", "-al", str(root / "files"), str(clone / "files")], check=True)
    failures = []
    for eid, _path, fixed, _changed in items:
        file = work / f"{eid}.json"
        file.write_text(json.dumps(fixed, indent=1), encoding="utf-8")
        ok, why = record(clone, file)
        if not ok:
            failures.append(f"{eid}: {why}")
    return failures


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--apply", action="store_true", help="record for real after a clean trial")
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args(argv)
    root = Path(args.root).resolve()
    now = datetime.now(timezone.utc)
    items = unrecorded(root, now)
    if not items:
        print("nothing to record: every staged receipt is already in the ledger")
        return 0
    print(f"{len(items)} staged receipt(s) not in the ledger:")
    for eid, path, _fixed, changed in items:
        print(f"  {eid}  ({path.parent.name})" + (f"  time fixed: {', '.join(changed)}" if changed else ""))
    with tempfile.TemporaryDirectory() as tmp:
        failures = trial(root, Path(tmp), items)
        if failures:
            print("TRIAL FAILED — nothing recorded:")
            for line in failures:
                print("  " + line)
            return 1
        print("TRIAL OK in a throwaway clone.")
        if not args.apply:
            print("dry run: re-run with --apply to record for real")
            return 0
        for eid, path, fixed, _changed in items:
            file = Path(tmp) / f"real_{eid}.json"
            file.write_text(json.dumps(fixed, indent=1), encoding="utf-8")
            ok, why = record(root, file)
            if not ok:
                print(f"RECORD FAILED at {eid}: {why} — earlier ones are in the ledger; fix and re-run")
                return 1
            path.write_text(json.dumps(fixed, indent=1), encoding="utf-8")
    print(f"recorded {len(items)}. Next, regenerate and commit:")
    print("  python3 framework/scripts/{batch_queue,coverage_report,reading_state}.py --disease wwox "
          "--out disease-models/wwox/registries/<name>.md --inputs-dirty-because '<reason>'")
    print("  python3 framework/scripts/pathograph.py --disease wwox --out disease-models/wwox/analysis/"
          "pathograph_inventory.md --export disease-models/wwox/analysis/data/pathograph_export.jsonl "
          "--inputs-dirty-because '<reason>'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
