#!/usr/bin/env python3
"""Regressions for the join (framework/scripts/repurposing_join.py).

Offline throughout: the adapters are not called (an un-cached offline hit is NOT_ATTEMPTED, which
is deliberately not NO_MATCH_FOUND), and the registry inputs are this repository's own files, so
the suite measures the join rather than the network.

Properties pinned:
  1. every query names the record it came from — id, repo-relative file, line — and no query is
     invented: the population is the registries, the map and the pathograph export;
  2. a locator count is len(entries), never len(mapping);
  3. the evidence table carries reading depth and audit status, and NO_RECEIPT / UNAUDITED /
     NO_MANIFEST stay distinct from one another and from zero;
  4. cards are built by the bridge from a composed packet: IPOTESI, canonical false, no score,
     and an abstention when no drug assertion exists;
  5. the run is deterministic (same bytes twice) and incremental (a second run reports every
     item unchanged; a removed query is reported REMOVED);
  6. measure_next names a dependence, a measurement, a sketch and the record it would move;
  7. an external hit is labelled NOT WWOX EVIDENCE and never replaces the LEGEND table;
  8. a derived card can be diffed against a hand-made card in cards/.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_join as rj  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CLI = ROOT / "framework" / "scripts" / "repurposing_join.py"
HANDMADE = ROOT / "disease-models" / "wwox" / "research" / "drug_repurposing" / "cards"


class Queries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.queries = rj.derive_queries()

    def test_population_is_not_empty_and_covers_every_source(self):
        kinds = {query["kind"] for query in self.queries}
        self.assertIn("claim", kinds)
        self.assertIn("lead", kinds)
        self.assertIn("mechanism_record", kinds)
        self.assertIn("mechanism_line", kinds)

    def test_every_query_names_its_origin(self):
        for query in self.queries:
            self.assertTrue(query["origin_id"])
            self.assertTrue(query["origin_file"])
            self.assertFalse(query["origin_file"].startswith("/"), query["origin_file"])
            self.assertTrue((ROOT / query["origin_file"]).exists(), query["origin_file"])
            self.assertIsInstance(query["origin_line"], int)
            self.assertTrue(query["digest"])

    def test_query_ids_are_unique_and_sorted(self):
        ids = [query["query_id"] for query in self.queries]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(ids, sorted(ids))

    def test_axis_filter_narrows_and_names_itself(self):
        wnt = rj.derive_queries(axis="wnt")
        self.assertLess(len(wnt), len(self.queries))
        self.assertTrue(wnt)
        self.assertEqual({query["axis"] for query in wnt}, {"wnt"})

    def test_candidate_names_come_from_the_map_heading_without_its_verdict(self):
        candidates = [query["candidate"] for query in self.queries if query.get("candidate")]
        self.assertTrue(candidates)
        for name in candidates:
            self.assertNotIn("→", name)
            self.assertNotIn("**", name)
            self.assertLess(len(name), 120, name)


class Evidence(unittest.TestCase):
    def test_locator_count_is_the_length_of_entries(self):
        manifest = {"verbatim_locators": {"entries": [{"proposition": "p"}, {"proposition": "q"}],
                                          "mapping_like_key": 1, "note": "x", "waived": False}}
        tmp = Path(tempfile.mkdtemp(prefix="join_"))
        try:
            path = tmp / "PMID999999.json"
            path.write_text(json.dumps(manifest), encoding="utf-8")
            original = rj.MANIFESTS
            rj.MANIFESTS = tmp
            row = rj.manifest_evidence("999999")
            self.assertEqual(row["locator_count"], 2)
        finally:
            rj.MANIFESTS = original
            shutil.rmtree(tmp, ignore_errors=True)

    def test_absent_manifest_is_no_manifest_not_zero_locators(self):
        row = rj.manifest_evidence("00000000")
        self.assertEqual(row["audit_status"], "NO_MANIFEST")
        self.assertEqual(row["manifest"], "")

    def test_unaudited_contradiction_counted_apart_from_an_audited_one(self):
        tmp = Path(tempfile.mkdtemp(prefix="join_"))
        try:
            manifest = {"verbatim_locators": {"entries": [
                {"contradicts_locator": {"verdict": "NARROW", "auditors": ["a", "b"]}},
                {"contradicts_locator": {"verdict": "NARROW", "auditors": []}},
                {"proposition": "no declaration"}]}}
            (tmp / "PMID888888.json").write_text(json.dumps(manifest), encoding="utf-8")
            original = rj.MANIFESTS
            rj.MANIFESTS = tmp
            row = rj.manifest_evidence("888888")
            self.assertEqual(row["locator_count"], 3)
            self.assertEqual(row["audited_entries"], 1)
            self.assertEqual(row["unaudited_contradictions"], 1)
        finally:
            rj.MANIFESTS = original
            shutil.rmtree(tmp, ignore_errors=True)

    def test_a_query_without_papers_abstains(self):
        table = rj.evidence_for({"query_id": "Q-X", "origin_id": "X", "pmids": []}, {})
        self.assertEqual(table["abstention"], "NO_RECEIPTED_EVIDENCE_FOR_THIS_QUERY")
        self.assertEqual(table["papers"], 0)

    def test_reading_depth_is_the_strongest_standing_receipt(self):
        events = [{"reading_depth": "partial_fulltext_read"}, {"reading_depth": "complete_fulltext_read"},
                  {"reading_depth": "abstract_only"}]
        self.assertEqual(rj.strongest_depth(events), "complete_fulltext_read")
        self.assertEqual(rj.strongest_depth([]), "UNKNOWN")


class Run(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="joinrun_"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_run_is_deterministic_and_incremental(self):
        first = rj.run(self.tmp, axis="wnt", live=False)
        bytes_first = {name: (self.tmp / name).read_bytes()
                       for name in ("queries.json", "evidence.json", "cards.json", "measure_next.json")}
        second = rj.run(self.tmp, axis="wnt", live=False)
        bytes_second = {name: (self.tmp / name).read_bytes() for name in bytes_first}
        self.assertEqual(bytes_first, bytes_second)
        self.assertEqual(first["queries"], second["queries"])
        for section in ("queries", "evidence", "cards"):
            self.assertEqual(second["changes"][section]["added"], [])
            self.assertEqual(second["changes"][section]["changed"], [])
            self.assertEqual(second["changes"][section]["removed"], [])
            self.assertGreater(second["changes"][section]["unchanged"], 0)

    def test_a_narrower_run_reports_the_dropped_queries_as_removed(self):
        rj.run(self.tmp, axis="wnt", live=False)
        narrowed = rj.run(self.tmp, axis="wnt", live=False, limit=3)
        self.assertTrue(narrowed["changes"]["queries"]["removed"])

    def test_cards_are_hypotheses_with_no_score_and_an_abstention(self):
        rj.run(self.tmp, axis="wnt", live=False)
        cards = json.loads((self.tmp / "cards.json").read_text(encoding="utf-8"))
        self.assertTrue(cards)
        for row in cards:
            card = row["card"]
            self.assertEqual(card["epistemic_status"], "IPOTESI")
            self.assertFalse(card["canonical"])
            self.assertEqual(card["abstention"], "NO_DRUG_ASSERTIONS_SUPPLIED")
            self.assertEqual(card["directional_summary"], "UNRESOLVED")
            text = json.dumps(card, ensure_ascii=False).lower()
            for word in ("\"score\"", "\"rank\"", "\"probability\""):
                self.assertNotIn(word, text)

    def test_external_sources_are_labelled_and_do_not_replace_the_legend_table(self):
        rj.run(self.tmp, axis="wnt", live=False)
        for row in json.loads((self.tmp / "cards.json").read_text(encoding="utf-8")):
            card = row["card"]
            self.assertIn("legend_evidence", card)
            for source in card["external_sources"]:
                self.assertEqual(source["evidence_label"], "NOT WWOX EVIDENCE")
            # offline and un-cached: NOT_ATTEMPTED, which is not NO_MATCH_FOUND
            self.assertTrue(all(source["status"] in ("NOT_ATTEMPTED", "MATCH_FOUND",
                                                     "NO_MATCH_FOUND", "QUERY_ERROR")
                                for source in card["external_sources"]))

    def test_measure_next_names_a_dependence_a_measurement_and_what_it_moves(self):
        rj.run(self.tmp, axis="wnt", live=False)
        rows = json.loads((self.tmp / "measure_next.json").read_text(encoding="utf-8"))
        self.assertTrue(rows)
        for row in rows:
            for key in ("dependence", "measurement", "experiment_sketch", "would_move"):
                self.assertTrue(str(row.get(key, "")).strip(), row)
            self.assertIn(":", row["would_move"])

    def test_cli_run_and_diff_against_a_hand_made_card(self):
        done = subprocess.run([sys.executable, str(CLI), "run", "--axis", "wnt", "--out", str(self.tmp)],
                              capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn("JOIN axis=wnt", done.stdout)
        handmade = HANDMADE / "D02_wnt_tankyrase.card.json"
        if not handmade.exists():
            self.skipTest("the hand-made card set is not in this checkout")
        cards = json.loads((self.tmp / "cards.json").read_text(encoding="utf-8"))
        query_id = cards[0]["query_id"]
        done = subprocess.run([sys.executable, str(CLI), "diff", query_id, str(handmade), "--out", str(self.tmp)],
                              capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(done.returncode, 0, done.stderr)
        report = json.loads(done.stdout)
        self.assertIn("only_in_derived", report)
        self.assertIn("only_in_handmade", report)
        self.assertTrue(report["same_value"] or report["different_value"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
