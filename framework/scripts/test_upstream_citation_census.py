#!/usr/bin/env python3
"""Regressions for the upstream-citation census (CC-20260826-UPSTREAM-CITATION-FAILURE-01 §6).

The census answers one mechanical question — how many of the citations in play can this
checkout adjudicate — and keeps the judgement (does the cited paper contain the fact) with the
reader. These tests keep it on that side of the line, and keep the denominator unavoidable.
"""
from __future__ import annotations

import importlib.util
import io
import json
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("upstream_citation_census",
                                              HERE / "upstream_citation_census.py")
census = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(census)

JATS = (
    "<article><back><ref-list><title>References</title>"
    "<ref id='r1'><element-citation><pub-id pub-id-type=\"pmid\">111</pub-id>"
    "</element-citation></ref>"
    "<ref id='r2'><element-citation><source>A book with no PMID</source></element-citation></ref>"
    "<ref id='r3'><mixed-citation><pub-id pub-id-type='doi'>10.1/x</pub-id>"
    "<pub-id pub-id-type='pmid'> 333 </pub-id></mixed-citation></ref>"
    "</ref-list></back></article>"
)
READ = {"111": "FTR-A", "333": "FTR-C"}


class TheDenominatorIsAlwaysThere(unittest.TestCase):
    def test_every_ref_is_counted_and_a_ref_without_a_pmid_is_not_dropped(self) -> None:
        """Dropping a reference with no PMID would make the resolvable share look larger."""
        self.assertEqual(["111", None, "333"], census.jats_references(JATS))

    def test_the_ref_list_element_is_not_mistaken_for_a_ref(self) -> None:
        self.assertEqual([], census.jats_references("<ref-list><title>x</title></ref-list>"))

    def test_the_denominator_names_what_cannot_be_adjudicated(self) -> None:
        result = census.census(["111", None, "999"], READ, {})
        self.assertEqual((3, 1, 1), (result["cited"], result["resolvable"],
                                     result["without_pmid"]))
        line = census.denominator_line(result)
        self.assertIn("1 of 3", line)
        self.assertIn("not evidence of support", line)
        self.assertIn(line, census.render(result))

    def test_a_tally_is_reported_against_the_resolvable_denominator(self) -> None:
        result = census.census(["111", "333", "999"], READ,
                               {"111": "SUPPORTED", "333": "CONTRADICTED"})
        self.assertEqual({"SUPPORTED": 1, "NOT_CONTAINED": 0, "CONTRADICTED": 1},
                         result["tally"])
        self.assertIn("ADJUDICATED: 2 of 2 resolvable", census.render(result))


class TheJudgementStaysWithTheReader(unittest.TestCase):
    def test_a_verdict_on_a_citation_never_read_in_full_is_refused(self) -> None:
        """A verdict with no read behind it is the defect the census exists to find."""
        with self.assertRaisesRegex(ValueError, "no complete read"):
            census.census(["999"], READ, {"999": "SUPPORTED"})

    def test_an_unknown_verdict_is_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "not one of"):
            census.census(["111"], READ, {"111": "PROBABLY"})

    def test_a_verdict_on_a_citation_not_in_play_is_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "not among the citations"):
            census.census(["333"], READ, {"111": "SUPPORTED"})

    def test_an_unadjudicated_resolvable_citation_is_left_blank_not_guessed(self) -> None:
        out = census.render(census.census(["111", "999"], READ, {}))
        self.assertIn("| 111 | FTR-A | ____ |", out)
        self.assertIn("| 999 | no | not adjudicable here |", out)

    def test_no_source_genre_is_taken_or_reported(self) -> None:
        """The proposal forbids an automatic distrust of reviews: no genre column exists."""
        out = census.render(census.census(["111"], READ, {})).lower()
        self.assertNotIn("review", out)


class TheCommandLine(unittest.TestCase):
    ROOT = HERE.parents[1]

    def run_main(self, *argv) -> tuple[int, str]:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            code = census.main(["--root", str(self.ROOT), *argv])
        return code, buffer.getvalue()

    def test_nothing_to_count_is_void_not_clean(self) -> None:
        with TemporaryDirectory() as stack:
            empty = Path(stack) / "empty.xml"
            empty.write_text("<article/>", encoding="utf-8")
            code, out = self.run_main("--from-jats", str(empty))
        self.assertEqual(3, code)
        self.assertIn("void, not clean", out)

    def test_a_non_pmid_is_an_invalid_invocation(self) -> None:
        self.assertEqual(2, self.run_main("--cited", "12ab")[0])

    def test_a_refused_adjudication_exits_2(self) -> None:
        with TemporaryDirectory() as stack:
            verdicts = Path(stack) / "v.json"
            verdicts.write_text(json.dumps({"1": "SUPPORTED"}), encoding="utf-8")
            code, _ = self.run_main("--cited", "1", "--adjudications", str(verdicts))
        self.assertEqual(2, code)

    def test_the_real_ledger_is_read_and_the_json_carries_the_denominator(self) -> None:
        ledger = self.ROOT / "disease-models/wwox/registries/fulltext_read_receipts.jsonl"
        if not ledger.is_file():
            self.skipTest("skipped: no receipt ledger in this checkout")
        read = census.complete_reads(self.ROOT, "wwox")
        self.assertTrue(all(event.startswith("FTR-") for event in read.values()))
        code, out = self.run_main("--cited", "1", "--json")
        self.assertEqual(0, code)
        self.assertIn("DENOMINATOR:", json.loads(out)["denominator"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
