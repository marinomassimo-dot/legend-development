#!/usr/bin/env python3
"""Regression guards for sweep completeness and integrity routing."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).with_name("batch_inferential_sweep.py")
SPEC = importlib.util.spec_from_file_location("batch_sweep", SCRIPT)
assert SPEC and SPEC.loader
SWEEP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SWEEP)


def main() -> int:
    triage = """## Summary
| Class | Count |
|---|---:|
| NEW | 2 |
| OUT_OF_SCOPE_LIKELY | 1 |
## Rows
"""
    assert SWEEP.parse_expected_count(triage) == 3

    text = "Editorial Expression of Concern: WWOX restoration"
    labels = SWEEP.labels_for(text)
    klass, _score, reason = SWEEP.classify(labels, "NEW", text)
    assert klass == "SAFETY_SIGNAL"
    assert "publication-integrity" in reason

    report = SWEEP.render(
        [
            {
                "sweep_class": "DISCOVERY_ONLY",
                "proband_priority_tier": "P4_BACKGROUND",
                "sweep_score": 1,
                "pmid": "1",
                "intake_class": "NEW",
                "sweep_labels": [],
                "title": "x",
                "sweep_reason": "x",
                "abstract": "",
            }
        ],
        {},
        expected_count=2,
    )
    assert "BLOCKED_INCOMPLETE" in report

    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        raw = root / "raw.txt"
        matrix = root / "matrix.json"
        output = root / "out.md"
        raw.write_text("WWOX test study.\nPMID: 12345678\n", encoding="utf-8")
        matrix.write_text(
            json.dumps(
                {
                    "axes": [],
                    "penalties": [],
                    "boosts": [],
                    "tiers": [{"name": "P4_BACKGROUND", "min_score": -999}],
                }
            ),
            encoding="utf-8",
        )
        result = subprocess.run(
            [
                "python3", str(SCRIPT), "--input", str(raw), "--out", str(output),
                "--proband-matrix", str(matrix),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
        assert output.exists()
        assert "Records emitted by sweep: 1" in output.read_text(encoding="utf-8")

    # Regression: a triage report built from a bare PMID list (no "PMID" prefix in the
    # Input column) must still be parsed. Before 2026-07-26 the prefix-only scan emitted
    # zero records here, so the completeness gate blocked every plain-PMID batch — the
    # most natural input an operator can hand the pipeline.
    bare_triage = (
        "# STUDY INTAKE TRIAGE — 2026-01-01\n\n"
        "## Summary\n\n| Class | Count |\n|---|---:|\n| NEW | 2 |\n\n"
        "## Rows\n\n"
        "| # | Class | Score | Match | Reason | Input |\n"
        "|---:|---|---:|---|---|---|\n"
        "| 1 | NEW | 0 |  | identifier not found | 12345678 |\n"
        "| 2 | CORPUS_CATALOGUED | 0 |  | identifier not found | 23456789 |\n"
    )
    assert SWEEP.triage_row_identifiers(bare_triage) == {
        "12345678": "NEW",
        "23456789": "CORPUS_CATALOGUED",
    }
    assert set(SWEEP.extract_pmids(bare_triage)) == {"12345678", "23456789"}
    assert SWEEP.parse_triage_classes(bare_triage)["12345678"] == "NEW"

    # The bare-identifier scan must stay scoped to the Rows table: years, counts and
    # other 6-9 digit noise outside it must not become PMIDs.
    assert SWEEP.extract_pmids("Coverage years 2001-2026; 161 records; total 4592031 chars") == []

    print("OK — batch sweep completeness/integrity guards passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
