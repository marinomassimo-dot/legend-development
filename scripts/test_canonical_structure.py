#!/usr/bin/env python3
"""Guard structural completeness of the four public scientific current files."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRIES = ROOT / "disease-models" / "wwox" / "registries"
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
import growth_anchors  # noqa: E402


def text(name: str) -> str:
    return (REGISTRIES / name).read_text(encoding="utf-8")


class CanonicalStructureTests(unittest.TestCase):
    def test_cardinality_matches_the_declared_growth_anchor(self) -> None:
        """No expected counts live here any more.

        This test used to pin `EXPECTED_COUNTS = {claims: 35, ...}` and every batch edited
        those four numbers by hand. That is the failure the growth principle names: updating
        the constraint cost four keystrokes while complying with it cost a whole commit, so
        the number tracked whatever made the suite green. On 2026-08-06 it was duly bumped
        35 → 39 with an explanatory comment, which is exactly what the check existed to
        prevent, and nobody noticed until the operator asked whether the design assumed growth.

        Now the counts are anchored in `framework/state/growth_anchors.jsonl` by a recorder
        that re-measures the registries and refuses a declared delta that does not match them.
        Growth is legal and cheap; undeclared growth is not possible to anchor at all.
        """
        violations, _improvements, _live = growth_anchors.evaluate(ROOT, "wwox")
        structural = [item for item in violations if item.startswith("STRUCTURAL_")]
        self.assertEqual(
            [], structural,
            "Registry cardinality moved without a declared delta. Record it with:\n"
            "  python3 framework/scripts/growth_anchors.py record --batch <ID> --claims +N\n"
            + "\n".join(structural))

    def test_record_identifiers_are_unique(self) -> None:
        identifiers = growth_anchors.structural_identifiers(
            text("claim_registry_current.md"),
            text("paper_registry_current.md"),
            text("literature_tracking_log_current.md"))
        duplicates = {
            kind: sorted({i for i in found if found.count(i) > 1})
            for kind, found in identifiers.items()
            if len(found) != len(set(found))
        }
        self.assertEqual({}, duplicates, f"Duplicate record identifiers: {duplicates}")

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
