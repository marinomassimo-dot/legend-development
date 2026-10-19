#!/usr/bin/env python3
"""Validate staged FULLTEXT_READ_RECEIPT JSON files in isolation, without touching any ledger.

WHY THIS EXISTS (2026-10-19, interventions wave, scientist-b)
-------------------------------------------------------------
Parallel waves stage receipts as JSON under research/receipt_staging/<actor>/ and the Orchestrator
records them. `fulltext_receipts.py record` rewrites the hash-chained ledger and the state manifest,
so a Scientist cannot use it to check a receipt; it has no read-only `validate --receipt`. Two waves
wrote the same ad hoc script. This is that script: it calls the writer's own validators
(validate_new_receipt and validate_receipt) and appends nothing.

  python3 framework/scripts/staged_receipt_check.py --artifact-root <shared checkout> <receipt.json> ...

Exit 0 only when every receipt returns no error. The artefact root is where the gitignored files/
tree lives (the shared checkout, not the task worktree). Network: none. Spend: none.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fulltext_receipts as fr  # noqa: E402


def check(receipt: dict, root: Path) -> list[str]:
    return list(fr.validate_new_receipt(receipt)) + list(fr.validate_receipt(receipt, root))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--artifact-root", required=True, type=Path)
    ap.add_argument("receipts", nargs="+", type=Path)
    a = ap.parse_args()
    bad = 0
    for p in a.receipts:
        try:
            errs = check(json.loads(p.read_text()), a.artifact_root)
        except (OSError, ValueError) as exc:
            errs = [f"unreadable: {exc}"]
        print(json.dumps({"receipt": str(p), "verdict": "OK" if not errs else "REFUSED", "errors": errs}))
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
