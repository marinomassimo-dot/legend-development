#!/usr/bin/env python3
"""Regressions for `extraction_damage_report.py`.

The tool's job is to stop a reader offering an italic-class zero as evidence. Its own failure mode
is the same one in miniature: a pattern that matches inside ordinary words would report truncations
as scars, and a tool whose examples are artefacts of its own regex teaches readers to discount it.
Most tests here are therefore FALSE-POSITIVE tests.

Run: `python3 framework/scripts/test_extraction_damage_report.py`
"""
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extraction_damage_report import analyse  # noqa: E402


def report(text: str) -> dict:
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as fh:
        fh.write(text)
        path = Path(fh.name)
    try:
        return analyse(path)
    finally:
        path.unlink()


CLEAN = ("The knockout mice were compared with wild type littermates. "
         "Expression of the gene was measured by western blot (P < 0.05, n = 6). "
         "We used bafilomycin and chloroquine.\n\nReferences\n1. Someone et al.\n")

DAMAGED = ("In our recently developedgene knockout mouse embryonic fibroblasts, increased "
           "expression of LC3-II was detected in theandcells (). Humangene expression fell "
           "(< 0.05). See Figure () and (,). The murinegene was unchanged.\n")


class DetectsRealDamage(unittest.TestCase):
    def test_damaged_text_is_flagged_inadmissible(self):
        r = report(DAMAGED)
        self.assertFalse(r["italic_class_counts_admissible"])
        self.assertIn("ITALIC-CLASS COUNTS INADMISSIBLE", r["verdict"])

    def test_roman_class_is_always_admissible(self):
        for text in (CLEAN, DAMAGED):
            self.assertTrue(report(text)["roman_class_counts_admissible"])

    def test_fused_scars_are_whole_tokens_not_truncations(self):
        for example in report(DAMAGED)["fused_examples"]:
            self.assertGreaterEqual(len(example), 5, example)
            self.assertIn(example, DAMAGED, f"{example!r} is not a substring of the source")

    def test_empty_cross_reference_stubs_counted(self):
        self.assertGreaterEqual(report(DAMAGED)["empty_cross_reference_stubs"], 3)

    def test_absent_reference_list_blocks_attribution_tracing(self):
        r = report(DAMAGED)
        self.assertFalse(r["reference_list_present"])
        self.assertFalse(r["citation_attribution_traceable"])
        self.assertIn("REFERENCE LIST IS ABSENT", r["verdict"])


class DoesNotCryWolf(unittest.TestCase):
    def test_clean_text_is_not_flagged(self):
        r = report(CLEAN)
        self.assertTrue(r["italic_class_counts_admissible"])
        self.assertEqual(r["fused_token_scars"], 0, r["fused_examples"])

    def test_clean_verdict_does_not_claim_a_guarantee(self):
        self.assertIn("not a guarantee", report(CLEAN)["verdict"])

    def test_ordinary_english_is_not_a_scar(self):
        r = report("Within the cohort, another analysis of the data followed.\n")
        self.assertEqual(r["fused_token_scars"], 0, r["fused_examples"])

    def test_camelcase_identifiers_are_not_scars(self):
        r = report("We ran legendLint and sessionSelfEval on the workspace.\n")
        self.assertEqual(r["fused_token_scars"], 0, r["fused_examples"])

    def test_present_reference_list_is_seen(self):
        self.assertTrue(report(CLEAN)["reference_list_present"])

    def test_report_names_the_artifact_and_its_size(self):
        r = report(CLEAN)
        self.assertTrue(r["artifact"].endswith(".txt"))
        self.assertEqual(r["bytes"], len(CLEAN.encode("utf-8")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
