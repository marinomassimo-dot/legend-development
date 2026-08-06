#!/usr/bin/env python3
"""Guard structural completeness of the four public scientific current files."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRIES = ROOT / "disease-models" / "wwox" / "registries"
# Updated deliberately by BATCH_20260806_002: +4 claims (036, 037, 038, 039), +3 papers
# (057, 058, 059), +1 tracking record (LIT-0405). The corpus placeholder count is unchanged:
# CORPUS P295 and P363 were promoted to PAPER 057 and 058 but are preserved append-only as
# triage lineage, and PMID 17803050 had no placeholder at all — it reached the registry only
# through the multi-hop expansion of two other readings.
# Prev, BATCH_20260726_001: +2 claims (034, 035), +3 papers (054, 055, 056), +3 tracking
# records (LIT-0402/0403/0404).
EXPECTED_COUNTS = {
    "claims": 39,
    "papers": 49,
    "corpus": 356,
    "literature": 386,
}


def text(name: str) -> str:
    return (REGISTRIES / name).read_text(encoding="utf-8")


class CanonicalStructureTests(unittest.TestCase):
    def test_claim_paper_corpus_and_literature_cardinality(self) -> None:
        claims = re.findall(
            r"^##\s+(CLAIM\s+\d+)\s*$",
            text("claim_registry_current.md"),
            re.M,
        )
        papers_text = text("paper_registry_current.md")
        papers = re.findall(r"^##\s+(PAPER\s+\d+)\s*$", papers_text, re.M)
        corpus = re.findall(
            r"^##\s+(CORPUS(?:-STUB-|\s+P)\d+)\s*$",
            papers_text,
            re.M,
        )
        literature = re.findall(
            r"^##\s+(LIT-(?!\[)[A-Z0-9-]+)\s*$",
            text("literature_tracking_log_current.md"),
            re.M,
        )
        observed = {
            "claims": len(claims),
            "papers": len(papers),
            "corpus": len(corpus),
            "literature": len(literature),
        }
        self.assertEqual(EXPECTED_COUNTS, observed)
        for identifiers in (claims, papers, corpus, literature):
            self.assertEqual(len(identifiers), len(set(identifiers)))

    def test_working_model_keeps_required_architecture(self) -> None:
        working = text("working_model_current.md")
        required = (
            "# BLOCK 1",
            "# BLOCK 2",
            "# BLOCK 3",
            "## Changelog",
        )
        missing = [marker for marker in required if marker not in working]
        changelog = working.split("## Changelog", 1)[-1]
        missing.extend(
            marker
            for marker in (
                "BATCH_20260710_A",
                "BATCH_20260714_001",
                "WM_v2.1",
                "WM_v3.0",
            )
            if marker not in changelog
        )
        self.assertEqual(
            [],
            missing,
            "Working-model architecture/changelog markers missing:\n"
            + "\n".join(missing),
        )

    def test_currents_are_substantive_not_lint_stubs(self) -> None:
        minimum_bytes = {
            "working_model_current.md": 20_000,
            "claim_registry_current.md": 50_000,
            "paper_registry_current.md": 250_000,
            "literature_tracking_log_current.md": 350_000,
        }
        failures = []
        for name, minimum in minimum_bytes.items():
            size = (REGISTRIES / name).stat().st_size
            if size < minimum:
                failures.append(f"{name}: {size} < {minimum} bytes")
        self.assertFalse(failures, "\n".join(failures))


if __name__ == "__main__":
    unittest.main(verbosity=2)
