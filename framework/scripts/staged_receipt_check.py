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


def pubmed_doi(pmid: str, get=None) -> str | None:
    """The DOI PubMed stores for a PMID (esummary), or None when it cannot be read."""
    import subprocess
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    try:
        body = get(url) if get else subprocess.run(["curl", "-sS", "-A", "", "-m", "40", url],
                                                    capture_output=True, text=True).stdout
        ids = json.loads(body)["result"][str(pmid)]["articleids"]
        return next((x["value"] for x in ids if x["idtype"] == "doi"), None)
    except Exception:
        return None


def doi_errors(receipt: dict, get=None) -> list[str]:
    """study_id.doi must equal the DOI PubMed carries. A DOI recalled from memory is the failure this
    catches: on 2026-10-20 a staged receipt carried a DOI whose last digit was wrong and every other
    validator passed it."""
    sid = receipt.get("study_id") or {}
    pmid, doi = sid.get("pmid"), sid.get("doi")
    if not pmid or not doi:
        return []
    stored = pubmed_doi(str(pmid), get)
    if stored is None:
        return [f"doi check: PubMed DOI for {pmid} could not be read, so {doi} is unverified"]
    return [] if stored.lower() == str(doi).lower() else [
        f"doi check: receipt DOI {doi} differs from the DOI PubMed stores for {pmid} ({stored})"]


def check(receipt: dict, root: Path, check_doi: bool = False, get=None) -> list[str]:
    errs = list(fr.validate_new_receipt(receipt)) + list(fr.validate_receipt(receipt, root))
    if check_doi:
        errs += doi_errors(receipt, get)
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--artifact-root", required=True, type=Path)
    ap.add_argument("--check-doi", action="store_true",
                    help="also require study_id.doi to equal the DOI PubMed stores for the PMID (network)")
    ap.add_argument("receipts", nargs="+", type=Path)
    a = ap.parse_args()
    bad = 0
    for p in a.receipts:
        try:
            errs = check(json.loads(p.read_text()), a.artifact_root, a.check_doi)
        except (OSError, ValueError) as exc:
            errs = [f"unreadable: {exc}"]
        print(json.dumps({"receipt": str(p), "verdict": "OK" if not errs else "REFUSED", "errors": errs}))
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
