#!/usr/bin/env python3
"""Flag retracted, corrected, or otherwise qualified PubMed records.

The script uses NCBI E-utilities and the Python standard library only. Exit 2
means a retracted publication or expression of concern was found; exit 1 means
a hard error; exit 0 means no blocking status was found.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path


ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PT_RETRACTED = "Retracted Publication"
PT_RETRACTION_NOTICE = "Retraction of Publication"
PT_EOC = "Expression of Concern"

REFTYPE_PROBLEM = {
    "retractionin": "RETRACTED",
    "expressionofconcernin": "EXPRESSION_OF_CONCERN",
    "erratumin": "ERRATUM/CORRECTION",
    "correctionin": "ERRATUM/CORRECTION",
    "republishedin": "REPUBLISHED",
}


def _norm_reftype(value: str) -> str:
    return (value or "").replace(" ", "").lower()


def chunked(sequence: list[str], size: int):
    for index in range(0, len(sequence), size):
        yield sequence[index:index + size]


def fetch_summaries(pmids: list[str], retries: int = 3) -> dict:
    params = urllib.parse.urlencode(
        {"db": "pubmed", "id": ",".join(pmids), "retmode": "json"}
    )
    url = f"{ESUMMARY}?{params}"
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(
                url, headers={"User-Agent": "legend-retraction-check/1.0"}
            )
            with urllib.request.urlopen(request, timeout=30) as response:
                data = json.loads(response.read().decode("utf-8"))
            return data.get("result", {})
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"esummary failed after {retries} tries: {last_error}")


def classify(record: dict) -> tuple[str, str]:
    """Return one status and an audit note for an NCBI esummary record."""
    publication_types = record.get("pubtype", []) or []
    problems: list[str] = []
    notes: list[str] = []

    if PT_RETRACTED in publication_types:
        problems.append("RETRACTED")
    if PT_RETRACTION_NOTICE in publication_types:
        problems.append("RETRACTION_NOTICE")
    if PT_EOC in publication_types:
        problems.append("EXPRESSION_OF_CONCERN")

    for reference in record.get("references", []) or []:
        reference_type = reference.get("reftype", "")
        mapped = REFTYPE_PROBLEM.get(_norm_reftype(reference_type))
        if mapped:
            problems.append(mapped)
        if reference_type and _norm_reftype(reference_type) not in ("cites", "citedby"):
            source = reference.get("refsource", "").strip()
            if source:
                notes.append(f"{reference_type}: {source}")

    for level in (
        "RETRACTED",
        "RETRACTION_NOTICE",
        "EXPRESSION_OF_CONCERN",
        "ERRATUM/CORRECTION",
        "REPUBLISHED",
    ):
        if level in problems:
            return level, "; ".join(notes)
    return "OK", "; ".join(notes)


def check(pmids: list[str]) -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for batch in chunked(pmids, 100):
        summaries = fetch_summaries(batch)
        for pmid in batch:
            record = summaries.get(pmid)
            if record is None or "error" in (record or {}):
                results.append(
                    {
                        "pmid": pmid,
                        "status": "NOT_FOUND",
                        "title": "",
                        "source": "",
                        "note": "",
                    }
                )
                continue
            status, note = classify(record)
            results.append(
                {
                    "pmid": pmid,
                    "status": status,
                    "title": (record.get("title", "") or "").rstrip("."),
                    "source": record.get("source", ""),
                    "note": note,
                }
            )
        time.sleep(0.34)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag retracted, EoC, and corrected PubMed records."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pmids", help="comma-separated list of PMIDs")
    group.add_argument("--file", help="file containing comma/space/newline-separated PMIDs")
    parser.add_argument("--json", action="store_true", help="emit machine-readable output")
    parser.add_argument("--all", action="store_true", help="show clean rows too")
    args = parser.parse_args()

    if args.pmids:
        raw = args.pmids
    else:
        raw = Path(args.file).read_text(encoding="utf-8")
    pmids = [token for token in raw.replace(",", " ").split() if token.isdigit()]
    if not pmids:
        print("No valid PMIDs given.", file=sys.stderr)
        return 1

    try:
        results = check(pmids)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        flagged = [row for row in results if row["status"] != "OK"]
        rows = results if args.all else flagged
        print(f"Checked {len(results)} PMIDs | flagged {len(flagged)}\n")
        if rows:
            print(f"{'PMID':<10} {'STATUS':<22} {'SOURCE':<14} TITLE")
            print("-" * 100)
            for row in rows:
                print(
                    f"{row['pmid']:<10} {row['status']:<22} "
                    f"{row['source'][:13]:<14} {row['title'][:60]}"
                )
                if row["note"]:
                    print(f"{'':<10} └─ {row['note']}")
        else:
            print("No retractions, expressions of concern, or corrections found.")

    blocking = {"RETRACTED", "EXPRESSION_OF_CONCERN"}
    return 2 if any(row["status"] in blocking for row in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
