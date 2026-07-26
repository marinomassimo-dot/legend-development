#!/usr/bin/env python3
"""Convert a PubMed Clipboard text export into a de-identified dated seed TSV.

Only bibliographic fields are emitted. Mail headers, sender/recipient details and all text
outside numbered PubMed records are discarded by construction.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path


RECORD_START = re.compile(r"(?m)^\d+\.\s*$")
PMID_LINE = re.compile(r"(?m)^PMID:\s*(\d+)\b([^\n]*)")
DOI = re.compile(r"(?i)\bdoi:\s*(10\.\d{4,9}/\S+?)(?:\.\s|\s|$)")


def parse(text: str) -> list[dict[str, str]]:
    starts = list(RECORD_START.finditer(text))
    rows: list[dict[str, str]] = []
    for position, start in enumerate(starts):
        end = starts[position + 1].start() if position + 1 < len(starts) else len(text)
        body = text[start.end() : end]
        lines = [line.strip() for line in body.splitlines() if line.strip()]
        match = PMID_LINE.search(body)
        if not lines or not match:
            raise ValueError(f"record {position + 1} has no title or PMID")

        title = lines[0].rstrip(".")
        pmid = match.group(1)
        pmid_tail = match.group(2)
        citation = body[: match.start()]
        doi_match = DOI.search(citation)
        doi = doi_match.group(1).rstrip(".,;") if doi_match else ""
        after_title = citation[citation.find(lines[0]) + len(lines[0]) :]
        year_match = re.search(r"\b((?:19|20)\d{2})\b", after_title)
        if not year_match:
            raise ValueError(f"PMID {pmid} has no publication year")

        if re.search(r"\[Preprint\]", citation, re.IGNORECASE):
            publication_type = "preprint"
        elif "Review." in pmid_tail or re.search(
            r"(?:systematic review|report and review|case study and literature review)$",
            title,
            re.IGNORECASE,
        ):
            publication_type = "review"
        else:
            publication_type = "primary"

        rows.append(
            {
                "pmid": pmid,
                "year": year_match.group(1),
                "free_full_text": "yes" if "Free PMC article." in pmid_tail else "no",
                "type": publication_type,
                "doi": doi,
                "title": title,
            }
        )

    if not rows:
        raise ValueError("no numbered PubMed records found")
    if len({row["pmid"] for row in rows}) != len(rows):
        raise ValueError("duplicate PMID in Clipboard export")
    return sorted(rows, key=lambda row: int(row["pmid"]), reverse=True)


def render(rows: list[dict[str, str]]) -> str:
    from io import StringIO

    handle = StringIO(newline="")
    fields = ("pmid", "year", "free_full_text", "type", "doi", "title")
    writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)
    return handle.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="PubMed Clipboard plain-text export")
    parser.add_argument("--out", help="destination corpus_seed_pubmed_YYYYMMDD.tsv")
    parser.add_argument("--check", help="compare parsed output with an existing seed TSV")
    args = parser.parse_args()

    try:
        rows = parse(Path(args.input).read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    output = render(rows)

    if args.check:
        expected = Path(args.check)
        existing = ""
        if expected.is_file():
            with expected.open(encoding="utf-8", newline="") as handle:
                existing = handle.read()
        if existing != output:
            print(f"DRIFT: {expected} does not match the Clipboard export", file=sys.stderr)
            return 1
        print(f"OK: {len(rows)} records match {expected}")
        return 0
    if not args.out:
        print("ERROR: provide --out or --check", file=sys.stderr)
        return 2
    destination = Path(args.out)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="") as handle:
        handle.write(output)
    print(f"written: {destination} ({len(rows)} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
