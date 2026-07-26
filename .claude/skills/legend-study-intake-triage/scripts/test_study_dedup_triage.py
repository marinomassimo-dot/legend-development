#!/usr/bin/env python3
"""Regression tests for the public study deduplication runtime."""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import study_dedup_triage as triage  # noqa: E402


def main() -> int:
    failures: list[str] = []

    identifiers = triage.extract_identifiers(
        "PMID: 12345678 DOI 10.1000/example.1 PMCID PMC123456"
    )
    if identifiers["pmid"] != {"12345678"}:
        failures.append("PMID extraction failed")
    if identifiers["doi"] != {"10.1000/example.1"}:
        failures.append("DOI extraction failed")
    if identifiers["pmcid"] != {"PMC123456"}:
        failures.append("PMCID extraction failed")

    rows = triage.split_input(
        "First paper. Author A. 2020. PMID: 12345678\n"
        "Second paper. Author B. 2021. PMID: 23456789\n"
        "Third paper. Author C. 2022. PMID: 34567890\n"
    )
    if len(rows) != 3:
        failures.append(f"line-per-record split expected 3 rows, got {len(rows)}")

    unknown = {"line": "99999991", "lineno": "1", "aggregate": "no", "raw": ""}
    if triage.match_row(unknown, [], {})["class"] != "NEW":
        failures.append("unknown bare PMID was not classified NEW")

    if triage.match_row(
        {"line": "xx", "lineno": "1", "aggregate": "no", "raw": ""},
        [],
        {},
    )["class"] != "INSUFFICIENT_METADATA":
        failures.append("short metadata was not classified INSUFFICIENT_METADATA")

    with tempfile.TemporaryDirectory() as temporary:
        workspace = Path(temporary)
        registry = workspace / triage.REGISTRY_FILES[0]
        registry.parent.mkdir(parents=True)
        registry.write_text(
            "## PAPER 001\n"
            "**Full title:** A public mechanistic WWOX study\n"
            "**Authors:** Example A\n"
            "**Year:** 2024\n"
            "**Identifier:** PMID: 45678901\n",
            encoding="utf-8",
        )
        records = triage.build_index(workspace)
        index = triage.build_identifier_index(workspace)
        known = {"line": "45678901", "lineno": "1", "aggregate": "no", "raw": ""}
        if triage.match_row(known, records, index)["class"] != "KNOWN_INTEGRATED":
            failures.append("known PMID was not classified KNOWN_INTEGRATED")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("OK — study deduplication guards passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
