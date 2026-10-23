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
    def test_every_axis_selects_something_including_early_benefit(self):
        for axis in rj.AXES:
            self.assertTrue(rj.derive_queries(axis=axis), axis)

    def test_leads_behind_any_leading_marker_become_queries(self):
        queries = rj.derive_queries()
        # 7 of 226 leads begin with a star, target, warning, green or medal marker, not the red circle
        ids = {q["origin_id"] for q in queries if q["kind"] == "lead"}
        for lead in ("DL-MECH-033", "DL-MECH-034", "DL-MECH-037", "DL-MECH-040", "DL-MECH-046",
                     "DL-BIO-008", "DL-MOL-012"):
            self.assertIn(lead, ids)

    def test_pathograph_line_reads_the_paper_it_was_bound_from(self):
        queries = rj.derive_queries()
        lines = [q for q in queries if q["kind"] == "mechanism_line"
                 and rj.PMID_IN_TEXT.search(q["bound_from"])]
        self.assertTrue(lines)
        for query in lines:
            self.assertIn(rj.PMID_IN_TEXT.search(query["bound_from"]).group(1), query["pmids"])

    def test_a_line_inherits_the_papers_of_the_claim_it_is_bound_to(self):
        queries = rj.derive_queries()
        claims = {q["origin_id"]: q for q in queries if q["kind"] == "claim"}
        checked = 0
        for query in queries:
            if query["kind"] != "mechanism_line":
                continue
            for name in query["bound_claims"]:
                for pmid in claims.get(name, {}).get("pmids", []):
                    self.assertIn(pmid, query["pmids"])
                    checked += 1
        self.assertGreater(checked, 0)

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

    def test_audit_block_read_nested_flat_and_absent(self):
        tmp = Path(tempfile.mkdtemp(prefix="join_"))
        try:
            real = {"manifest": "PMID1.json", "entry": 3, "what_changed": "x",
                    "audit": {"auditors": 1, "verdicts": ["PARTIAL"]}}
            manifest = {"verbatim_locators": {"entries": [
                {"contradicts_locator": real},
                {"contradicts_locator": {"verdict": "NARROW", "auditors": ["a", "b"]}},
                {"contradicts_locator": {"manifest": "PMID1.json", "entry": 4}}]}}
            (tmp / "PMID777777.json").write_text(json.dumps(manifest), encoding="utf-8")
            original = rj.MANIFESTS
            rj.MANIFESTS = tmp
            row = rj.manifest_evidence("777777")
            self.assertEqual(row["audited_entries"], 2)
            self.assertEqual(row["unaudited_contradictions"], 1)
            self.assertEqual([v["verdict"] for v in row["contradiction_verdicts"]],
                             ["PARTIAL", "NARROW", "UNSTATED"])
            self.assertEqual([v["auditors"] for v in row["contradiction_verdicts"]], [1, 2, 0])
        finally:
            rj.MANIFESTS = original
            shutil.rmtree(tmp, ignore_errors=True)

    def test_strongest_event_carries_its_receipt_id(self):
        events = [{"evidence_depth": "partial_fulltext_read", "event_id": "FTR-1"},
                  {"evidence_depth": "complete_fulltext_read", "event_id": "FTR-2"}]
        self.assertEqual(rj.strongest_event(events), ("complete_fulltext_read", "FTR-2"))

    def test_paper_ids_resolve_to_pmids_through_the_registry(self):
        papers = rj.paper_pmids(ROOT)
        self.assertGreater(len(papers), 100)
        self.assertTrue(all(pmid.isdigit() for pmids in papers.values() for pmid in pmids))
        # a query that names a PAPER inherits its PMIDs, and says through which record
        inherited = [q for q in rj.derive_queries() if q.get("pmids_via_records")]
        self.assertTrue(inherited)
        for query in inherited[:20]:
            for pmid, names in query["pmids_via_records"].items():
                self.assertIn(pmid, query["pmids"])
                self.assertTrue(names)

    def test_a_query_without_papers_abstains(self):
        table = rj.evidence_for({"query_id": "Q-X", "origin_id": "X", "pmids": []}, {})
        self.assertTrue(table["abstention"].startswith("LINKAGE_GAP:"), table["abstention"])
        self.assertIn("missing datum:", table["abstention"])
        self.assertEqual(table["papers"], 0)

    def test_abstention_names_the_state_and_the_missing_datum(self):
        named = {"kind": "mechanism_record", "linkage": {"ids_named": ["DL-MOL-013"], "ids_reaching_a_pmid": [],
                                                       "ids_in_registry_without_pmid": ["DL-MOL-013"],
                                                       "ids_not_found_in_registry": []}}
        text = rj.abstention_for(named)
        self.assertTrue(text.startswith("NO_PAPER:"), text)
        self.assertIn("DL-MOL-013", text)
        named["linkage"] = {"ids_named": ["DL-X-1"], "ids_reaching_a_pmid": [], "ids_in_registry_without_pmid": [],
                            "ids_not_found_in_registry": ["DL-X-1"]}
        self.assertTrue(rj.abstention_for(named).startswith("LINKAGE_GAP:"))
        self.assertIn("not found in the registry", rj.abstention_for(named))
        self.assertTrue(rj.abstention_for({"kind": "lead", "linkage": {}}).startswith("NO_PAPER:"))

    def test_every_abstention_in_the_corpus_has_a_state_and_a_datum(self):
        queries = rj.derive_queries()
        receipts = rj.load_receipts()
        states = set()
        for query in queries:
            table = rj.evidence_for(query, receipts)
            if table["abstention"]:
                states.add(table["abstention"].split(":")[0])
                self.assertIn("missing datum:", table["abstention"])
                self.assertNotIn("NO_RECEIPTED_EVIDENCE", table["abstention"])
        self.assertTrue(states <= {"LINKAGE_GAP", "NO_PAPER"}, states)

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

    def test_handoff_turns_every_card_into_one_assignment_row(self):
        rj.run(self.tmp, axis="wnt", live=False)
        cards = json.loads((self.tmp / "cards.json").read_text(encoding="utf-8"))
        queries = {q["query_id"]: q for q in json.loads((self.tmp / "queries.json").read_text(encoding="utf-8"))}
        rows = rj.handoff_rows(cards, queries)
        self.assertEqual(len(rows), len(cards))
        for row in rows:
            self.assertIn(row["kind"], ("SELECT", "READ", "REPLICATE", "AUDIT"))
            self.assertTrue(row["ask"] and row["who"] and row["origin"])
            if row["kind"] in ("REPLICATE", "AUDIT", "READ") and row["dependence"] not in ("LINKAGE_GAP", "NO_PAPER"):
                self.assertTrue(row["pmids"], row)
            if row["kind"] == "SELECT":
                self.assertIn(row["dependence"], ("LINKAGE_GAP", "NO_PAPER"))
            self.assertTrue(row["acquisition"])
            if row["kind"] == "REPLICATE":
                self.assertEqual(row["lead_spec"]["status"], "open")
                self.assertEqual(row["lead_spec"]["tag"], "INFERENZA")
        text = rj.render_handoff(rows, "2026-01-01", "wnt")
        self.assertIn("NOT WWOX EVIDENCE", text)
        self.assertIn("Not medical advice", text)
        self.assertNotIn("2026-10-2", text.split("\n")[0].replace("2026-01-01", ""))  # the date is the argument, not the clock
        done = subprocess.run([sys.executable, str(CLI), "handoff", "--out", str(self.tmp), "--date", "2026-01-01",
                               "--write", str(self.tmp / "handoff.md")], capture_output=True, text=True, cwd=ROOT)
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual((self.tmp / "handoff.md").read_text(encoding="utf-8"), text)

    def test_replicate_rows_are_screened_and_their_lead_specs_pass_the_ledger_validator(self):
        import discovery_lead as dl
        rows = rj.handoff_rows(*self._cards_and_queries())
        replicate = [r for r in rows if r["kind"] == "REPLICATE"]
        self.assertTrue(replicate)
        for row in replicate:
            self.assertIn(row["binding"]["binding"], ("PRIMARY_WITH_ENDPOINT_WORDS", "UNVERIFIED", "NOT_CHECKED"))
            self.assertIn("independent = a different laboratory", row["act"])
            self.assertEqual(dl.validate(row["lead_spec"]), [], row["lead_spec"])
            self.assertIn("NOT WWOX EVIDENCE", row["lead_spec"]["transfer_limit"])

    def _cards_and_queries(self):
        rj.run(self.tmp, axis="", live=False)
        cards = json.loads((self.tmp / "cards.json").read_text(encoding="utf-8"))
        queries = {q["query_id"]: q for q in json.loads((self.tmp / "queries.json").read_text(encoding="utf-8"))}
        return cards, queries

    def test_bound_check_refuses_a_review_and_a_missing_endpoint(self):
        cache = self.tmp / "pm"
        cache.mkdir()
        record = {"pmid": "1", "status": "MATCH_FOUND", "error": "", "title": "A review", "retrieved_at": "2026-01-01",
                  "source": "t", "publication_types": ["Journal Article", "Review"], "words": ["catenin", "organoid"]}
        (cache / "1.json").write_text(json.dumps(record), encoding="utf-8")
        query = {"decisive_test": "**first measure nuclear catenin state**, then more"}
        verdict = rj.bound_check("1", query, cache, live=False)
        self.assertEqual(verdict["binding"], "UNVERIFIED")
        self.assertIn("not a primary article", verdict["reason"])
        self.assertEqual(verdict["endpoint_words_found"], ["catenin"])
        self.assertEqual(verdict["endpoint_words_missing"], ["nuclear"])
        record["publication_types"] = ["Journal Article"]
        record["words"] = ["catenin", "nuclear"]
        (cache / "1.json").write_text(json.dumps(record), encoding="utf-8")
        self.assertEqual(rj.bound_check("1", query, cache, live=False)["binding"], "PRIMARY_WITH_ENDPOINT_WORDS")
        self.assertIn("declares no endpoint", rj.bound_check("1", {"decisive_test": "UNKNOWN"}, cache, False)["reason"])
        self.assertEqual(rj.bound_check("2", query, cache, live=False)["binding"], "NOT_CHECKED")

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
