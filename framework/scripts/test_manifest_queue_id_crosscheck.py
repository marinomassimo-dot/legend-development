#!/usr/bin/env python3
"""Regressions for the `multihop.queued[].queue` cross-check.

The defect these exist for is real and is reproduced verbatim in
`test_the_real_2026_09_09_defect_is_refused`: a draft manifest for PMID 18674750 named
`FT-072`–`FT-075`, four live queue entries about four unrelated papers, and passed STRICT.
The reader's own grep caught it after the gate had gone green.

🔴 A fixture that only asserts refusal is half a test. Each refusal below is paired with the
CORRECT arrangement it must not refuse — a paper's hop carried on that paper's own entry, and
a hop carried on the entry for the hop itself — because a check that refuses everything would
pass every refusal test in this file and be worthless.
"""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "manifest_queue_id_crosscheck", HERE / "manifest_queue_id_crosscheck.py")
check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check)

# A miniature queue with the shape of the real one: a heading, a `**Paper:**` line naming a
# PMID, and prose that may name further identifiers.
QUEUE = """# FULL TEXT QUEUE

## FT-071 — The intron-8 regulatory architecture
**Paper:** PMID 18674750 — Lee JC et al., Am J Hum Genet 2008.
**Why:** this paper's own residual debt plus its hops, including ref 42 PMID 17086198.

## FT-072 — The supplement that contains the refutation
**Paper:** PMID 20530675 — Kurek KC et al., Oncogene 2010.
**Why:** an entirely unrelated osteosarcoma reading.

## FT-079 — Protein-level WWOX tissue distribution
**Paper:** PMID 16941225 — the counterpart to the Figure S3 transcript gel.
"""


def manifest(pmid: str, *queued: dict) -> dict:
    return {"pmid": pmid, "multihop": {"queued": list(queued)}}


class TheAddressMustResolve(unittest.TestCase):
    def setUp(self) -> None:
        self.entries = check.parse_queue(QUEUE)

    def test_the_queue_parses_into_its_entries(self) -> None:
        self.assertEqual(sorted(self.entries), ["FT-071", "FT-072", "FT-079"])

    def test_an_identifier_with_no_entry_is_refused(self) -> None:
        errors = check.errors_for(
            manifest("18674750", {"queue": "FT-999", "pmid": "17086198"}), self.entries)
        self.assertEqual(len(errors), 1)
        self.assertIn("FT-999 has no entry", errors[0])

    def test_a_paper_may_carry_its_hop_on_its_own_entry(self) -> None:
        """The correct arrangement of the very manifest that produced the defect."""
        errors = check.errors_for(
            manifest("18674750", {"queue": "FT-071", "pmid": "17086198"}), self.entries)
        self.assertEqual(errors, [])

    def test_a_hop_may_be_carried_on_the_entry_for_the_hop_itself(self) -> None:
        """FT-079 names 16941225 and not 18674750, and that is the OTHER legitimate shape."""
        errors = check.errors_for(
            manifest("18674750", {"queue": "FT-079", "pmid": "16941225"}), self.entries)
        self.assertEqual(errors, [])

    def test_the_reference_may_be_written_as_a_wikilink_style_fragment(self) -> None:
        """`full_text_queue_current#FT-071` is the same address as `FT-071`."""
        errors = check.errors_for(
            manifest("18674750",
                     {"queue": "full_text_queue_current#FT-071", "pmid": "17086198"}),
            self.entries)
        self.assertEqual(errors, [])

    def test_the_zero_padding_is_not_part_of_the_address(self) -> None:
        errors = check.errors_for(
            manifest("18674750", {"queue": "FT-71", "pmid": "17086198"}), self.entries)
        self.assertEqual(errors, [])


class TheEntryMustBelongToThisReading(unittest.TestCase):
    def setUp(self) -> None:
        self.entries = check.parse_queue(QUEUE)

    def test_the_real_2026_09_09_defect_is_refused(self) -> None:
        """PMID 18674750's hop pointed at FT-072, which is PMID 20530675's entry."""
        errors = check.errors_for(
            manifest("18674750", {"ref": 46, "pmid": "16941225", "queue": "FT-072"}),
            self.entries)
        self.assertEqual(len(errors), 1)
        self.assertIn("FT-072", errors[0])
        self.assertIn("different paper", errors[0])
        # The message must name what it looked for, or the reader cannot act on it.
        self.assertIn("PMID 16941225", errors[0])
        self.assertIn("PMID 18674750", errors[0])

    def test_a_hop_with_no_pmid_still_has_to_land_on_this_paper(self) -> None:
        """Most queued items name only a `ref`; the manifest's own PMID is then the test."""
        errors = check.errors_for(
            manifest("18674750", {"ref": 42, "queue": "FT-072"}), self.entries)
        self.assertEqual(len(errors), 1)
        self.assertIn("different paper", errors[0])

    def test_an_unresolvable_pmid_string_falls_back_to_the_manifest(self) -> None:
        """`"unresolved at read time"` is a real value in this corpus; it is not an address."""
        errors = check.errors_for(
            manifest("18674750",
                     {"pmid": "unresolved at read time", "queue": "FT-071"}), self.entries)
        self.assertEqual(errors, [])

    def test_a_pmids_list_is_read_as_well_as_a_pmid(self) -> None:
        errors = check.errors_for(
            manifest("99999999", {"pmids": ["16941225"], "queue": "FT-079"}), self.entries)
        self.assertEqual(errors, [])


class WhatIsNotChecked(unittest.TestCase):
    """The two honest silences, each asserted so neither can become a silent pass."""

    def setUp(self) -> None:
        self.entries = check.parse_queue(QUEUE)

    def test_a_queue_value_naming_no_ft_identifier_is_unchecked_not_approved(self) -> None:
        report = check.audit(
            manifest("25012504", {"queue": "integrity review", "pmids": []}), self.entries)
        self.assertEqual(report["unchecked"], [{"entry": 0, "queue": "integrity review"}])
        self.assertEqual(report["foreign"], [])
        self.assertEqual(report["unresolved"], [])
        self.assertEqual(check.errors_for(
            manifest("25012504", {"queue": "integrity review"}), self.entries), [])

    def test_a_bare_pmid_string_queues_a_hop_without_naming_an_address(self) -> None:
        """345 of the corpus's 387 queued items are bare strings. There is nothing to check."""
        report = check.audit({"pmid": "15070730",
                              "multihop": {"queued": ["12514174", "11719429"]}}, self.entries)
        self.assertEqual(report["unchecked"], [])
        self.assertEqual(report["resolved"], [])
        self.assertEqual(check.errors_for(
            {"pmid": "15070730", "multihop": {"queued": ["12514174"]}}, self.entries), [])


class TheGenerousScanIsDeliberate(unittest.TestCase):
    def setUp(self) -> None:
        self.entries = check.parse_queue(QUEUE)

    def test_an_identifier_anywhere_in_the_entry_body_counts(self) -> None:
        """FT-071's prose — not its `**Paper:**` line — is where 17086198 appears."""
        errors = check.errors_for(
            manifest("99999999", {"queue": "FT-071", "pmid": "17086198"}), self.entries)
        self.assertEqual(errors, [])

    def test_generosity_does_not_rescue_a_genuinely_foreign_entry(self) -> None:
        """The property that makes the generous scan safe, asserted rather than assumed."""
        errors = check.errors_for(
            manifest("99999999", {"queue": "FT-072", "pmid": "88888888"}), self.entries)
        self.assertEqual(len(errors), 1)
        self.assertIn("different paper", errors[0])


class TheCorpusIsClean(unittest.TestCase):
    """The § 9.5(a) measurement, kept as an executable claim rather than a prose number."""

    def test_no_live_manifest_names_an_unresolved_or_foreign_queue_id(self) -> None:
        root = HERE.parents[1]
        entries = check.load_queue(root, "wwox")
        if entries is None:  # pragma: no cover - only in a stripped workspace
            self.skipTest("no full-text queue in this workspace")
        import json
        offenders = []
        for path in sorted(
                (root / "disease-models/wwox/research/deepdive_manifests").glob("PMID*.json")):
            report = check.audit(json.loads(path.read_text(encoding="utf-8")), entries)
            if report["unresolved"] or report["foreign"]:
                offenders.append((path.name, report["unresolved"], report["foreign"]))
        self.assertEqual(offenders, [], "the corpus baseline was 0/0 on 2026-09-10")


if __name__ == "__main__":
    unittest.main(verbosity=2)
