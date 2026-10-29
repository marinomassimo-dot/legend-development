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
import re
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

    def test_a_condemned_entry_whose_repair_was_never_re_judged_is_its_own_state(self):
        """`auditors: 1` from the audit that CONDEMNED an entry is not a repair anyone checked.

        Measured 2026-10-24: 178 entries across 71 manifests sat in this state while reading as
        audited, and a held research candidate waited three days on exactly that. The last case
        is the one that keeps the rule honest: OVERSHOOT followed by SUPPORTED is a repair that
        WAS re-judged and held, so it must not count here.
        """
        tmp = Path(tempfile.mkdtemp(prefix="join_"))
        try:
            def decl(verdicts, auditors=1):
                return {"manifest": "PMID1.json", "entry": 1, "what_changed": "x",
                        "audit": {"auditors": auditors, "verdicts": verdicts}}
            manifest = {"verbatim_locators": {"entries": [
                {"contradicts_locator": decl(["OVERSHOOT"])},
                {"contradicts_locator": decl(["UNDERSHOOT"])},
                {"contradicts_locator": decl(["OVERSHOOT", "SUPPORTED"])},
                {"contradicts_locator": decl(["SUPPORTED"])},
                {"contradicts_locator": decl(["OVERSHOOT"], auditors=0)}]}}
            (tmp / "PMID888888.json").write_text(json.dumps(manifest), encoding="utf-8")
            original = rj.MANIFESTS
            rj.MANIFESTS = tmp
            row = rj.manifest_evidence("888888")
            self.assertEqual(row["repair_unverified"], 2, "OVERSHOOT and UNDERSHOOT alone")
            self.assertEqual(row["audited_entries"], 2, "re-judged-and-held, and plain SUPPORTED")
            self.assertEqual(row["unaudited_contradictions"], 1, "auditors 0 stays its own state")
        finally:
            rj.MANIFESTS = original

    def test_unsupported_is_adverse_and_does_not_read_as_supported(self):
        """UNSUPPORTED contains the letters of SUPPORTED; the distinction is the whole point."""
        self.assertTrue(rj.adverse_and_not_cleared("UNSUPPORTED"))
        self.assertFalse(rj.adverse_and_not_cleared("SUPPORTED"))
        self.assertFalse(rj.adverse_and_not_cleared("OVERSHOOT/SUPPORTED"))
        self.assertTrue(rj.adverse_and_not_cleared(
            "blind locator audit 2026-10-23: OVERSHOOT at quote level, repaired at source"))

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
            # an abstention is what a card without drug-side rows says; a linked curated card that carries
            # drug-side rows (e.g. lithium, G01) is a card with comparisons and no abstention
            self.assertEqual(card["abstention"],
                             None if card["input"]["drug_assertions"] else "NO_DRUG_ASSERTIONS_SUPPLIED")
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
        evidence = json.loads((self.tmp / "evidence.json").read_text(encoding="utf-8"))
        text = rj.render_handoff(rows, "2026-01-01", "wnt", evidence)
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
            self.assertIn(row["binding"]["binding"], ("PRIMARY_WITH_ENDPOINT_WORDS", "UNVERIFIED", "NOT_CHECKED",
                                                      "BOUND_BY_FULLTEXT_LOCATOR"))
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


class CuratedLink(unittest.TestCase):
    """P1 (2026-10-26): curated qualifications are consumed by the module, not replaced by fixed labels.
    One offline full run over the real corpus; each test names the defect it pins."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="joincur_"))
        cache = ROOT / "disease-models" / "wwox" / "research" / "drug_repurposing" / "join" / "pubmed_cache"
        if cache.exists():  # the recorded abstract screen of the bound paper, so a failing screen is part of the test
            shutil.copytree(cache, cls.tmp / "pubmed_cache")
        rj.run(cls.tmp, live=False)
        cls.cards = {r["query_id"]: r["card"] for r in json.loads((cls.tmp / "cards.json").read_text(encoding="utf-8"))}
        cls.evidence = {t["query_id"]: t for t in json.loads((cls.tmp / "evidence.json").read_text(encoding="utf-8"))}
        cls.queries = {q["query_id"]: q for q in json.loads((cls.tmp / "queries.json").read_text(encoding="utf-8"))}
        cls.rows = {r["query_id"]: r for r in rj.handoff_rows(
            [{"query_id": k, "card": v} for k, v in cls.cards.items()], cls.queries)}

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def packet(self, name):
        return json.loads((HANDMADE / f"{name}.packet.json").read_text(encoding="utf-8"))

    def test_a_registered_reading_is_not_labelled_wwox_evidence(self):
        for table in self.evidence.values():
            for row in table["rows"]:
                self.assertFalse(row["evidence_label"].startswith("WWOX EVIDENCE"), row["evidence_label"])
                self.assertIn("not implied", row["evidence_label"])
                self.assertTrue(row["evidence_scope"])
        # scope comes only from a curated assertion that cites the reading; otherwise it is said to be unqualified
        self.assertEqual(self.evidence["Q-R-10"]["rows"][0]["evidence_scope"], ["WWOX_BIOLOGY_OTHER_CONTEXT"])
        self.assertIn("DA-LC-ATF4-001", self.evidence["Q-R-10"]["rows"][0]["scope_basis"])
        # a record with no curated card: every row is said to be unqualified, none is inferred
        for row in self.evidence["Q-N-07"]["rows"]:
            self.assertEqual(row["evidence_scope"], ["UNQUALIFIED"])
            self.assertIn("not qualified", row["scope_basis"])
        # a record whose curated card cites one reading qualifies THAT reading only (Q-R-01, linked 2026-10-27)
        by_pmid = {row["pmid"]: row for row in self.evidence["Q-R-01"]["rows"]}
        self.assertEqual(by_pmid["42422765"]["evidence_scope"], ["WWOX_EXPERIMENT_IN_DEE_SYSTEM"])
        self.assertEqual(by_pmid["42128308"]["evidence_scope"], ["UNQUALIFIED"])

    def test_route_and_track_are_the_curated_ones_or_unqualified_never_defaulted(self):
        for query_id, card in self.cards.items():
            curated = self.queries[query_id].get("curated_cards")
            if not curated:
                self.assertEqual(card["input"]["route"], "UNQUALIFIED", query_id)
                self.assertEqual(card["input"]["mission_dimensions"]["track"], "UNQUALIFIED", query_id)
                self.assertEqual(card["input"]["disease_assertion"]["evidence_scope"], "UNQUALIFIED")
        packet = self.packet("E01_isr_modulators")
        card = self.cards["Q-R-10"]["input"]
        self.assertEqual(card["route"], packet["route"])  # BENEFICIO_PRECOCE, not RECUPERO_PROFONDO
        self.assertEqual(card["mission_dimensions"], packet["mission_dimensions"])
        self.assertEqual(card["mission_dimensions"]["track"], "A")
        self.assertNotEqual(card["route"], "RECUPERO_PROFONDO")

    def test_a_card_written_before_track_was_qualified_links_without_a_guessed_track(self):
        """Defects found 2026-10-27 (package W1.1): qualification() raised KeyError on a packet with no
        `mission_dimensions` (the A-D series and the early-benefit cards), and CARD_REF could not name a
        `cards_early/` card (hyphenated id), so those cards could not be linked at all."""
        self.assertEqual(rj.CARD_REF.findall("`research/drug_repurposing/cards_early/EB-KD-01.card.json`"), ["EB-KD-01"])
        self.assertEqual(rj.CARD_REF.findall("`research/drug_repurposing/cards/E04_ketogenic_lactate_axis.card.json`"),
                         ["E04_ketogenic_lactate_axis"])
        old = json.loads(rj.curated_packet_path("D02_wnt_tankyrase").read_text(encoding="utf-8"))
        route, dims = rj.qualification([old])
        self.assertEqual((route, dims["track"]), (old["route"], "UNQUALIFIED"))  # the route as written, the Track not guessed
        self.assertIn(old["candidate"]["id"], dims["route_note"])
        early = json.loads(rj.curated_packet_path("EB-KD-01").read_text(encoding="utf-8"))
        stated = self.packet("E04_ketogenic_lactate_axis")
        route, dims = rj.qualification([early, stated])
        self.assertEqual((route, dims["track"]), ("BENEFICIO_PRECOCE", "A"))  # Track from the card that states it, said in the note
        self.assertIn("EB-KD-01", dims["route_note"])
        # a record naming a card that cannot be found would be skipped silently: none may
        for query_id, query in self.queries.items():
            for name in query.get("curated_cards") or []:
                self.assertIsNotNone(rj.curated_packet_path(name), (query_id, name))
        linked = self.cards["Q-R-05"]["input"]
        self.assertEqual(sorted(linked["curated_from"]), ["cards/E04_ketogenic_lactate_axis.packet.json",
                                                         "cards_early/EB-KD-01.packet.json"])

    def test_curated_observations_arrive_unchanged_with_context_limits_and_a_live_link(self):
        # Q-N-08 names two cards since BATCH_20261019_026 (E03 target engagement, I01 the PDH-restraint premise);
        # their assertions arrive unchanged, one card after the other in the order the record names them
        for query_id, names in (("Q-R-10", ["E01_isr_modulators"]), ("Q-R-11", ["E02_ldh_inhibition"]),
                                ("Q-N-08", ["E03_pdk_inhibition_dca", "I01_pdk_inhibition_dca_premise_seizure_glycaemia"])):
            packets, card = [self.packet(n) for n in names], self.cards[query_id]["input"]
            self.assertEqual(card["disease_assertions"], [r for pk in packets for r in pk["disease_assertions"]], query_id)
            self.assertEqual(card["drug_assertions"], [r for pk in packets for r in pk["drug_assertions"]], query_id)
            for row in card["disease_assertions"] + card["drug_assertions"]:
                for field in ("target_id", "endpoint", "direction", "context", "source", "locator", "reading_depth", "evidence_scope"):
                    self.assertTrue(row.get(field), (query_id, row["id"], field))
            self.assertTrue(self.cards[query_id]["comparisons"], query_id)
            self.assertNotEqual(self.cards[query_id]["abstention"], "NO_DRUG_ASSERTIONS_SUPPLIED", query_id)
        # an abstract-level drug observation keeps its depth: nothing was upgraded to a reading
        depths = {r["id"]: r["reading_depth"] for r in self.cards["Q-R-10"]["input"]["drug_assertions"]}
        self.assertEqual(set(depths.values()), {"abstract_only"})
        checks = self.cards["Q-R-10"]["input"]["curation_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertTrue(check["receipt_in_ledger"], check)
            self.assertTrue(all(m["resolved"] for m in check["manifest_entries"]), check)

    def test_the_handoff_names_the_card_a_record_is_already_qualified_by(self):
        """Package W1.1: a row of a linked record points the next batch at the curated card (with its route, Track,
        row counts, comparison statuses and its own next measurement); an unlinked record carries no such block."""
        for query_id, row in self.rows.items():
            linked = bool(self.cards[query_id]["input"].get("curated_from"))
            self.assertEqual(bool(row["qualification"]), linked, query_id)
        view = self.rows["Q-R-04"]["qualification"]
        self.assertEqual(view["cards"], ["cards/G01_lithium_gsk3.packet.json"])
        self.assertEqual((view["route"], view["track"]), ("BENEFICIO_PRECOCE", "A"))
        self.assertEqual(view["comparisons"], {"OPPOSES_DISEASE_CHANGE": 1, "UNRESOLVED": 2})  # the specificity failure stays visible
        self.assertEqual(self.rows["Q-N-02"]["qualification"]["cards"], view["cards"])  # one candidate, two map records, one card
        text = rj.render_handoff(list(self.rows.values()), "2026-01-01", "all")
        self.assertIn("Records already qualified by a curated card", text)
        self.assertIn("cards/G01_lithium_gsk3.packet.json", text)

    def test_a_locator_pointing_past_the_manifest_is_reported_unresolved(self):
        row = {"id": "X", "locator": "disease-models/wwox/research/deepdive_manifests/PMID42909904.json "
                                     "verbatim_locators.entries[57], [9999]", "receipt": "FTR-20990101-00000000-01"}
        check = rj.curated_checks([row])[0]
        self.assertFalse(check["receipt_in_ledger"])
        self.assertFalse(check["manifest_entries"][0]["resolved"])

    def test_replicate_row_classes_follow_the_curated_packets_not_fixed_labels(self):
        """Derived from the packets on disk: the expected class of every endpoint is recomputed here from the
        curated observations (token subset of target+endpoint, complete read, receipt), then compared with the row."""
        checked = 0
        for query_id, row in self.rows.items():
            curated = self.queries[query_id].get("curated_cards")
            if row["kind"] != "REPLICATE" or not curated:
                continue
            observations = []
            for name in curated:
                observations += self.packet(name).get("disease_assertions", [])
            for c in row["endpoint_classes"]:
                tokens = rj.span_tokens(c["endpoint"])
                matched = [a for a in observations if tokens and tokens <= rj.span_tokens(f"{a['target_id']} {a['endpoint']}")]
                strong = [a for a in matched if a["reading_depth"] == "complete_fulltext_read" and a.get("receipt")]
                if strong:
                    self.assertEqual(c["class"], rj.MEASURED, (query_id, c["endpoint"]))
                    self.assertEqual({o["id"] for o in c["observations"]}, {a["id"] for a in matched}, (query_id, c["endpoint"]))
                else:
                    self.assertNotEqual(c["class"], rj.MEASURED, (query_id, c["endpoint"]))
                    self.assertTrue(c.get("cause") or c["class"] == rj.MECHANISM, (query_id, c["endpoint"]))
                checked += 1
            if any(c["class"] == rj.MECHANISM for c in row["endpoint_classes"]):
                self.assertIn("NOT a replication", row["act"], query_id)
            if any(c["class"] == rj.MEASURED for c in row["endpoint_classes"]):
                self.assertEqual(row["binding"]["binding"], "BOUND_BY_FULLTEXT_LOCATOR", query_id)
                self.assertIn("abstract_screen", row["binding"])
        self.assertGreater(checked, 0)
        # a null in another contrast is carried beside the increase, not dropped (Q-R-10 ATF4)
        atf4 = {c["endpoint"]: c for c in self.rows["Q-R-10"]["endpoint_classes"]}["ATF4 protein"]
        self.assertEqual({o["id"]: o["direction"] for o in atf4["observations"]}, {"DA-LC-ATF4-001": "INCREASE", "DA-LC-ATF4-002": "NO_CHANGE"})
        self.assertEqual([o["id"] for o in atf4["same_molecule_other_endpoint"]], ["DA-GSE-ISR-003"])

    def test_the_mrs_row_states_its_sign_relative_to_each_fly_contrast(self):
        row = next(a for a in self.packet("E02_ldh_inhibition")["disease_assertions"] if a["id"] == "DA-BIO008-001")
        signs = row["sign_vs_contrast"]
        self.assertTrue(signs["DA-LC-LAC-001"].startswith("OPPOSITE"))
        self.assertTrue(signs["DA-LC-LAC-002"].startswith("SAME SIGN"))
        self.assertIn("not a replication", signs["DA-LC-LAC-002"])

    def test_without_a_curated_observation_the_class_is_missing_not_replicate(self):
        for row in self.rows.values():
            if row["kind"] == "REPLICATE" and not self.queries[row["query_id"]].get("curated_cards"):
                self.assertTrue(all(c["class"] == rj.MISSING for c in row["endpoint_classes"]), row["query_id"])
                self.assertNotEqual(row["binding"]["binding"], "BOUND_BY_FULLTEXT_LOCATOR")

    def test_target_to_compounds_keeps_identity_status_coverage_and_truncation_apart_from_name_search(self):
        census = self.cards["Q-N-08"]["input"]["target_compounds"]
        self.assertEqual(census["operation"], "TARGET_TO_COMPOUNDS")
        self.assertEqual(census["evidence_label"], "NOT WWOX EVIDENCE")
        by = {t["symbol"]: t for t in census["targets"]}
        self.assertEqual(by["PDK2"]["identity"]["uniprot"], "Q15119")
        self.assertEqual(by["PDK2"]["sources"]["chembl_mechanisms"]["compounds"][0]["action"], "INHIBITOR")
        self.assertTrue(all("COLLISION" in c["identity_warning"] for c in by["PDK1"]["sources"]["dgidb"]["compounds"]))
        self.assertEqual(by["PDHA1"]["sources"]["dgidb"]["status"], "NOT_ATTEMPTED")
        self.assertEqual(by["PDK2"]["sources"]["opentargets"]["truncation"]["truncated"], False)
        isr = {t["symbol"]: t for t in self.cards["Q-R-10"]["input"]["target_compounds"]["targets"]}
        self.assertEqual(isr["EIF2B3"]["sources"]["dgidb"]["status"], "UNMATCHED")        # DGIdb does not know the symbol
        self.assertEqual(isr["EIF2B2"]["sources"]["dgidb"]["status"], "NO_MATCH_FOUND")   # known, listed nothing
        self.assertTrue(all(s["operation"] == "SEARCH_BY_NAME_OR_IDENTIFIER" for s in self.cards["Q-R-10"]["external_sources"]))

    def test_a_cut_list_is_reported_as_truncated(self):
        folder = self.tmp / "census"
        folder.mkdir()
        (folder / "target_resolution.tsv").write_text(
            "label\thgnc_id\thgnc_symbol\tuniprot\tensembl_gene\tchembl_single_protein_target\tcollision_or_note\n"
            "T1\tHGNC:1\tT1\tP1\tENSG1\tCHEMBL1\t\n", encoding="utf-8")
        (folder / "opentargets_lists.tsv").write_text("label\tensembl\tlist_count\tmolecule\tname\tdrugType\tmaxClinicalStage\tdiseases\n"
                                                      "T1\tENSG1\t5\tM1\tdrugone\tSmall molecule\tPHASE_2\tx\n", encoding="utf-8")
        (folder / "opentargets_adapter_counts.tsv").write_text("label\tensembl\tlist_count\tadapter_count\nT1\tENSG1\t5\t5\n", encoding="utf-8")
        out = rj.target_compounds({"dir": str(folder), "symbols": ["T1"]})
        ot = out["targets"][0]["sources"]["opentargets"]
        self.assertTrue(ot["truncation"]["truncated"])
        self.assertEqual((ot["truncation"]["listed"], ot["truncation"]["reported"]), (1, 5))
        self.assertEqual(out["targets"][0]["sources"]["dgidb"]["status"], "NOT_ATTEMPTED")


class EndpointClassesOnSyntheticFixtures(unittest.TestCase):
    """The classifier follows the observation, shown on invented fixtures (no corpus): an abstract-level or receiptless
    match can never become MEASURED nor BOUND_BY_FULLTEXT_LOCATOR, another molecule never matches, and the cause of a
    MISSING class is named."""

    @staticmethod
    def obs(id_, target, endpoint, depth="complete_fulltext_read", receipt="FTR-20990101-00000001-01", direction="INCREASE"):
        row = {"id": id_, "target_id": target, "endpoint": endpoint, "direction": direction, "reading_depth": depth,
               "locator": "fixture", "context": {"species": "fixture", "genotype": "fixture"}, "measured_result_note": ""}
        if receipt:
            row["receipt"] = receipt
        return row

    @staticmethod
    def card(observations, depth="complete_fulltext_read"):
        return {"input": {"disease_assertions": observations, "candidate": {"id": "X", "name": "fixture"}},
                "legend_evidence": {"rows": [{"pmid": "0", "reading_depth": depth, "manifest": "fixture", "locator_count": 1,
                                              "audit_status": "UNAUDITED", "receipt_id": "FTR-20990101-00000001-01",
                                              "bound_check": {"binding": "UNVERIFIED", "reason": "fixture"}, "unaudited_contradictions": 0}],
                                    "digest": "d", "query_id": "Q-X"},
                "measure_next": {"dependence": "ONE_PAPER (0)", "measurement": "m", "would_move": "w"}, "external_sources": []}

    @staticmethod
    def query(test):
        return {"query_id": "Q-X", "decisive_test": test, "origin_file": "fixture", "origin_line": 1}

    def classes(self, observations, test, depth="complete_fulltext_read"):
        return {c["endpoint"]: c for c in rj.endpoint_classes(self.query(test), self.card(observations, depth))}

    def test_an_abstract_only_match_is_never_measured_nor_bound_by_a_locator(self):
        weak = [self.obs("A1", "foo protein", "foo level", depth="abstract_only", receipt=None)]
        c = self.classes(weak, "**foo protein**")["foo protein"]
        self.assertNotEqual(c["class"], rj.MEASURED)
        self.assertEqual((c["class"], c["cause"]), (rj.MISSING, "OBSERVATION_WEAKER_THAN_FULLTEXT"))
        # complete read but no receipt: still not enough
        c = self.classes([self.obs("A2", "foo protein", "foo level", receipt=None)], "**foo protein**")["foo protein"]
        self.assertEqual(c["class"], rj.MISSING)
        # through the handoff row: the binding stays the abstract screen
        card = self.card(weak)
        row = rj.handoff_rows([{"query_id": "Q-X", "card": card}], {"Q-X": self.query("**foo protein**")})[0]
        self.assertNotEqual(row["binding"]["binding"], "BOUND_BY_FULLTEXT_LOCATOR")
        self.assertNotIn("abstract_screen", row["binding"])
        # the positive control: the same observation, read in full with a receipt, is measured and bound
        strong = self.card([self.obs("A3", "foo protein", "foo level")])
        row = rj.handoff_rows([{"query_id": "Q-X", "card": strong}], {"Q-X": self.query("**foo protein**")})[0]
        self.assertEqual(row["endpoint_classes"][0]["class"], rj.MEASURED)
        self.assertEqual(row["binding"]["binding"], "BOUND_BY_FULLTEXT_LOCATOR")

    def test_another_molecule_does_not_match_and_a_complete_reading_makes_it_a_new_experiment(self):
        other = [self.obs("B1", "pdh activity", "pdh activity")]
        c = self.classes(other, "**lactate**")["lactate"]
        self.assertEqual(c["class"], rj.MECHANISM)
        self.assertEqual(c["observations"], [])

    def test_the_cause_of_a_missing_class_is_named(self):
        self.assertEqual(self.classes([], "**foo**")["foo"]["cause"], "NO_CURATED_OBSERVATION")
        no_span = rj.endpoint_classes(self.query("no bold span here"), self.card([self.obs("C1", "foo", "foo")]))
        self.assertEqual((no_span[0]["class"], no_span[0]["cause"]), (rj.MISSING, "NO_ENDPOINT_DECLARED"))
        c = self.classes([self.obs("C2", "bar", "bar", depth="abstract_only", receipt=None)], "**zzz**", depth="partial_fulltext_read")["zzz"]
        self.assertEqual((c["class"], c["cause"]), (rj.MISSING, "NO_COMPLETE_READING_BOUND"))


class CatalogueLeadsTest(unittest.TestCase):
    """The handoff consumes the catalogue/coverage layer: card-attached pairs and reasoned dispositions become rows."""

    def build(self, tmp: Path, dispositions: list[dict]) -> Path:
        cov = tmp / "coverage"
        cards = tmp / "cards"
        cov.mkdir()
        cards.mkdir()
        (cov / "coverage_matrix.json").write_text(json.dumps({"rows": [
            {"row_id": "FAM:A", "representative": "CAT:A", "cards": [{"card_id": "H99_x"}]}, {"row_id": "FAM:B", "representative": "CAT:B", "cards": []}]}))
        lev = {"L1": "documented", "L2": "coherent", "L3": "none", "L4": "none"}
        pr = lambda row, disp: {"row_id": row, "name": row, "need": "NEED-X", "disposition": disp, "levels": lev}
        (cov / "priorities.json").write_text(json.dumps({"priorities": [
            pr("FAM:A", "consistent_mechanism_candidate"), pr("FAM:A", "not_relevant"), pr("FAM:B", "consistent_mechanism_candidate")]}))
        (cards / "H99_x.packet.json").write_text(json.dumps({"p4_card": {"next_measurement": "the discriminating assay"}}))
        (cov / "lead_dispositions.json").write_text(json.dumps({"dispositions": dispositions}))
        return cov

    def disp(self, **kw):
        row = {"id": "LD-T", "need": "NEED-X", "subject": "s", "catalogue_ids": [], "decision": "abstention", "why": "w",
               "reopening_condition": "r", "next_experiment": "n", "owner": "o", "record": "rec"}
        row.update(kw)
        return row

    def test_only_card_attached_candidate_pairs_are_rows(self):
        with tempfile.TemporaryDirectory() as d:
            cov = self.build(Path(d), [])
            leads = rj.catalogue_leads(cov, Path(d) / "cards")
        self.assertEqual([(r["card"], r["disposition"], r["next_measurement"]) for r in leads["cards"]],
                         [("H99_x", "consistent_mechanism_candidate", "the discriminating assay")])
        self.assertEqual(leads["cards"][0]["owner"], "Scientist (card owner)")

    def test_a_card_attached_twice_to_one_family_gives_one_row(self):
        with tempfile.TemporaryDirectory() as d:
            cov = self.build(Path(d), [])
            matrix = json.loads((cov / "coverage_matrix.json").read_text())
            matrix["rows"][0]["cards"] = [{"card_id": "H99_x", "attachment": "named_member"}, {"card_id": "H99_x", "attachment": "assertion_subject"}]
            (cov / "coverage_matrix.json").write_text(json.dumps(matrix))
            rows = rj.catalogue_leads(cov, Path(d) / "cards")["cards"]
        self.assertEqual(len(rows), 1)

    def test_card_without_next_measurement_names_who_must_define_it(self):
        with tempfile.TemporaryDirectory() as d:
            cov = self.build(Path(d), [])
            (Path(d) / "cards" / "H99_x.packet.json").write_text(json.dumps({"p4_card": {}}))
            row = rj.catalogue_leads(cov, Path(d) / "cards")["cards"][0]
        self.assertEqual(row["next_measurement"], "no next measurement defined")
        self.assertIn("must define", row["owner"])

    def test_leads_needs_omits_the_pairs_a_card_disclaims(self):
        with tempfile.TemporaryDirectory() as d:
            cov = self.build(Path(d), [])
            (Path(d) / "cards" / "H99_x.packet.json").write_text(json.dumps({"leads_needs": ["NEED-OTHER"], "p4_card": {"next_measurement": "m"}}))
            self.assertEqual(rj.catalogue_leads(cov, Path(d) / "cards")["cards"], [])

    def test_invalid_file_duplicate_ids_bad_card_and_unknown_catalogue_id_are_reported(self):
        with tempfile.TemporaryDirectory() as d:
            cov = self.build(Path(d), [self.disp(), self.disp(), self.disp(id="LD-C", card="cards/NOPE.packet.json", catalogue_ids=["CAT:ZZZ"])])
            problems = " | ".join(rj.catalogue_leads(cov, Path(d) / "cards")["problems"])
            (cov / "lead_dispositions.json").write_text("{not json")
            broken = rj.catalogue_leads(cov, Path(d) / "cards")
        self.assertIn("duplicate id", problems)
        self.assertIn("card path", problems)
        self.assertIn("catalogue ids not in the coverage matrix", problems)
        self.assertTrue(any("invalid" in p for p in broken["problems"]))

    def test_long_text_is_not_truncated(self):
        with tempfile.TemporaryDirectory() as d:
            cov = self.build(Path(d), [self.disp(why="w" * 500)])
            text = rj.render_handoff([], "2026-01-01", "all", None, rj.catalogue_leads(cov, Path(d) / "cards"))
        self.assertIn("w" * 500, text)

    def test_dispositions_render_with_reopening_and_next_experiment(self):
        with tempfile.TemporaryDirectory() as d:
            cov = self.build(Path(d), [self.disp(decision="opposite_mechanism")])
            leads = rj.catalogue_leads(cov, Path(d) / "cards")
        text = rj.render_handoff([], "2026-01-01", "all", None, leads)
        self.assertIn("## Catalogue-derived leads", text)
        self.assertIn("**opposite_mechanism**", text)
        self.assertIn("| r | n | o |", text)
        self.assertEqual(leads["problems"], [])

    def test_bad_dispositions_are_reported_not_hidden(self):
        with tempfile.TemporaryDirectory() as d:
            cov = self.build(Path(d), [self.disp(decision="maybe"), self.disp(id="LD-U", need="NEED-NOPE"), self.disp(id="LD-V", why="")])
            leads = rj.catalogue_leads(cov, Path(d) / "cards")
        self.assertEqual(len(leads["problems"]), 3)
        self.assertIn("DISPOSITION PROBLEM", rj.render_handoff([], "2026-01-01", "all", None, leads))

    def test_no_leads_leaves_the_handoff_unchanged(self):
        self.assertNotIn("Catalogue-derived", rj.render_handoff([], "2026-01-01", "all"))
        self.assertEqual(rj.render_catalogue_leads({"cards": [], "dispositions": []}), [])

    def test_shipped_dispositions_are_valid(self):
        leads = rj.catalogue_leads()
        self.assertEqual(leads["problems"], [])
        self.assertTrue(any(r["decision"] == "candidate" for r in leads["dispositions"]))
        self.assertFalse([r for r in leads["cards"] if r["card"].startswith("H01") and r["need"] != "NEED-T-TYPE-CALCIUM"])


class SupersededWordingGone(unittest.TestCase):
    """BATCH_20261019_025: the VABAM wording and the nonsense-allele statements the module consumes.

    The superseded sentence called VABAM in WWOX-DEE «a real safety signal» and glossed the
    label's 22 percent as a «background rate». Two case-selected children with no denominator
    support neither an excess nor a deficit, and 22 percent is the exposed-arm prevalence in
    non-WWOX infants. These are the consumer surfaces of the module (working model, narrative view,
    mechanism map, cards, needs, join output, both view files, the latest handoff); dated historical
    notes and the identifier patch record are quoting the old wording on purpose and are not listed.
    """

    DR = "disease-models/wwox/research/drug_repurposing/"
    SURFACES = [
        "disease-models/wwox/registries/working_model_current.md",
        "disease-models/wwox/registries/claim_registry_current.md",
        "disease-models/wwox/disease_model.md",
        "disease-models/wwox/analysis/mechanism_intervention_map.md",
        DR + "cards/H02_gabaat_inactivator_myelin_exposure.card.json",
        DR + "cards/H02_gabaat_inactivator_myelin_exposure.packet.json",
        DR + "cards_early/EB-VGB-01.card.json",
        DR + "cards_early/EB-VGB-01.packet.json",
        DR + "needs/needs.json",
        DR + "join/queries.json",
        DR + "join/cards.json",
        DR + "join/evidence.json",
        DR + "join/measure_next.json",
        DR + "view/index.html",
        DR + "view/index_shareable.html",
        DR + "closed_loop_it4_e1b_20261028/README.md",
        "disease-models/wwox/research/repurposing_batch_selection_20261029_module.md",
    ]

    def read(self, rel):
        return (ROOT / rel).read_text(encoding="utf-8")

    def test_no_consumer_surface_uses_the_superseded_vabam_wording(self):
        import re
        near = re.compile(r"(VABAM|vigabatrin)[^\n]{0,300}background rate|background rate[^\n]{0,300}(VABAM|vigabatrin)", re.I)
        for rel in self.SURFACES:
            text = self.read(rel)
            self.assertNotIn("a real safety signal", text.lower(), rel)
            self.assertIsNone(near.search(text), rel)

    def test_working_model_states_selected_cases_no_denominator_and_no_enrichment(self):
        line = next(l for l in self.read(self.SURFACES[0]).splitlines() if l.startswith("- **VABAM**"))
        for needed in ("two WWOX-DEE children", "no denominator", "22 percent", "4 percent", "not supported",
                       "exposed-arm prevalence", "cautionary clinical position is unchanged"):
            self.assertIn(needed, line)

    def test_claim_001_carries_the_wave_note_and_keeps_its_status(self):
        text = self.read(self.SURFACES[1])
        block = text.split("## CLAIM 001", 1)[1].split("\n## CLAIM 002", 1)[0]
        self.assertIn("**Status:** conflicting evidence", block)
        self.assertIn("BATCH_20261019_025", block)
        self.assertIn("not supported by any source read", block)

    def test_nonsense_enumeration_is_a_prediction_and_the_nucleotide_is_corrected(self):
        needs = self.read(self.DR + "needs/needs.json")
        self.assertIn("PREDICTION", needs)
        self.assertIn("predictions by the 50-55 nt rule, never measurements", needs)
        self.assertNotIn("no systematic enumeration of nonsense alleles", needs)
        census = self.read("disease-models/wwox/analysis/woree_therapeutic_class_census_20260921.md")
        row = next(l for l in census.splitlines() if l.startswith("| `c.160") and "Arg54" in l)
        self.assertTrue(row.startswith("| `c.160C>T`"))
        b02 = self.read(self.DR + "cards/B02_readthrough_class.packet.json")
        self.assertNotIn("nobody has made it", b02)
        self.assertIn("inference from classification", b02)


class SupersededWordingGoneIT5Batch2(unittest.TestCase):
    """BATCH_20261019_026: the iteration-5 results as the module's consumers must now state them.

    What is asserted, and only this, over the listed SURFACES (consumer files, the generated join
    and views, the latest handoff; dated historical notes are not scanned):
      1. no sentence about the organoid says PDK1 is down / lower / decreased / reduced unless the same
         sentence says «sign» (lower in sign only), case-insensitively, plus a few exact old strings;
      2. no «Potency: UNKNOWN» and no «no cytosolic client (was) tested» (case-insensitive, any spacing);
      3. no sentence reads the GSEA sign as depletion in the silenced cells unless it negates it
         (a «deplet» within a sentence of «silenc» with no «not»/«nor»/«no» before it), in the dossier,
         PAPER 022 and every surface;
      4. DIS-004 keeps its WITHDRAWN heading and carries an UPDATE «restated, not established» / «NOT reversed»;
      5. PAPER 022 carries the adjudication, CLAIM 014 keeps its Status, the working model keeps WM_v7.28
         and does not name this batch; the Guide-to-Pharmacology rows are not explained by family propagation.
    It does not prove that a paraphrase outside these patterns is absent.
    """

    DR = "disease-models/wwox/research/drug_repurposing/"
    SURFACES = [
        "disease-models/wwox/analysis/mechanism_intervention_map.md",
        DR + "cards/E03_pdk_inhibition_dca.card.json",
        DR + "cards/E03_pdk_inhibition_dca.packet.json",
        DR + "cards/A01_pba_class.card.json",
        DR + "cards/A01_pba_class.packet.json",
        DR + "cards/I01_pdk_inhibition_dca_premise_seizure_glycaemia.card.json",
        DR + "needs/needs.json",
        DR + "coverage/lead_dispositions.json",
        DR + "join/queries.json",
        DR + "join/cards.json",
        DR + "join/evidence.json",
        DR + "join/measure_next.json",
        DR + "view/index.html",
        DR + "view/index_shareable.html",
        "disease-models/wwox/research/repurposing_batch_selection_20261029_module.md",
    ]

    def read(self, rel):
        return (ROOT / rel).read_text(encoding="utf-8")

    def sentences(self, text):
        import re
        return re.split(r"(?<=[.;])\s+|\n|\\n", text)

    def test_organoid_pdk1_is_lower_in_sign_only_everywhere(self):
        import re
        pdk = re.compile(r"PDK1\s+(?:is\s+|was\s+|are\s+)?(?:down|lower|decreased|reduced)\b", re.I)
        for rel in self.SURFACES:
            text = self.read(rel)
            for old in ("In the human knockout organoid PDK1 is DOWN", "PDK1 down in human knockout organoid",
                        "glycolytic targets up; PDK1 down", "PDK1 is LOWER, PDHA1"):
                self.assertNotIn(old, text, (rel, old))
            for sent in self.sentences(text):
                if "organoid" in sent.lower() and pdk.search(sent):
                    self.assertIn("sign", sent.lower(), (rel, sent[:200]))
        packet = self.read(self.DR + "cards/E03_pdk_inhibition_dca.packet.json")
        self.assertIn("lower in sign only", packet)
        needs = self.read(self.DR + "needs/needs.json")
        self.assertIn("PDK1 lower in sign only", needs)

    def test_phenylbutyrate_class_wording_no_longer_closed(self):
        import re
        closed = re.compile(r"no\s+cytosolic\s+client\s+(?:was\s+|has\s+been\s+)?tested", re.I)
        for rel in self.SURFACES:
            text = self.read(rel)
            self.assertNotIn("Potency: UNKNOWN", text, rel)
            self.assertIsNone(closed.search(text.replace("**", "")), rel)
        ledger = self.read("disease-models/wwox/research/dismissal_ledger_current.md")
        block = ledger.split("### DIS-004", 1)[1].split("\n### DIS-005", 1)[0]
        self.assertIn("WITHDRAWN", ledger.split("### DIS-004", 1)[1].splitlines()[0])
        self.assertIn("UPDATE 2026-10-29", block)
        self.assertIn("restated, not established", block)
        self.assertIn("NOT reversed", block)

    def test_gsea_sign_is_read_as_the_silenced_end_not_as_depletion(self):
        import re
        dep = re.compile(r"deplet\w*[^.;\n]{0,100}silenc|silenc\w*[^.;\n]{0,100}deplet", re.I)
        negated = re.compile(r"\b(?:not|nor|no|never)\b[^.;\n]{0,40}$", re.I)
        dossier = "disease-models/wwox/research/fulltext_dossiers/PMID31543760.md"
        paper = self.read("disease-models/wwox/registries/paper_registry_current.md")
        p022 = paper.split("## PAPER 022", 1)[1].split("\n## PAPER 023", 1)[0]
        scanned = [(rel, self.read(rel)) for rel in self.SURFACES + [dossier]] + [("PAPER 022", p022)]
        for rel, text in scanned:
            for m in dep.finditer(text):
                self.assertIsNotNone(negated.search(text[max(0, m.start() - 60):m.start()]) or negated.search(m.group(0)[:0]) or re.search(r"\b(?:not|nor)\b", m.group(0), re.I),
                                     (rel, m.group(0)[:160]))
        d = self.read(dossier)
        self.assertIn("silenced (shWWOX) end", d)
        self.assertIn("NOT depleted in the silenced cells", p022)
        self.assertIn("ONE library per arm", p022)

    def test_claim_014_status_and_working_model_version_are_untouched(self):
        """Positive checks only (state that grows is never pinned by absence or by today's value):
        CLAIM 014 keeps its status and names the batch; the working model's version is the one the
        state manifest declares; the batch record says the working model was not changed."""
        claims = self.read("disease-models/wwox/registries/claim_registry_current.md")
        block = claims.split("## CLAIM 014", 1)[1].split("\n## CLAIM 015", 1)[0]
        self.assertIn("**Status:** consolidated baseline", block)
        self.assertIn("BATCH_20261019_026", block)
        wm_version = re.search(r"\*\*Version:\*\* (WM_v\S+)", self.read("disease-models/wwox/registries/working_model_current.md")).group(1)
        manifest = self.read("framework/state/state_manifest_current.md")
        self.assertIn(wm_version.split("_")[1], manifest)       # the version the manifest declares
        record = json.loads(self.read("ledger/tasks/integrator/BATCH_20261019_026.json"))
        self.assertIn("working_model_current.md", json.dumps(record))

    def test_guide_to_pharmacology_rows_are_not_explained_by_family_propagation(self):
        for rel in (self.DR + "coverage/lead_dispositions.json", "disease-models/wwox/research/repurposing_batch_selection_20261029_module.md"):
            text = self.read(rel)
            self.assertNotIn("the same family-level propagation pattern as LD-003", text, rel)
            self.assertIn("GtoPdb target id", text, rel)
        cov = self.read(self.DR + "coverage/README.md")
        self.assertIn("superseded explanation", cov)


# --- the window-wording regression (iteration 7, P0b) -------------------------------------------------------------
# A positive check that the qualified wording exists does not notice an ADDITIONAL active sentence that presents the
# tested ages as a demonstrated therapeutic limit. This detector reads the ACTIVE sentences of a document: a sentence
# that names the window (P0-P5 / P5) and asserts it as measured, critical or demonstrated, without the qualifier, is an
# overreach. A sentence that quotes the old text and says it is superseded is a historical citation and is allowed.
# It never bans a word: the same words are fine when qualified or quoted as history.
_WINDOW_REF = re.compile(r"P0\s*[\u2013\u2014-]\s*P5|\bP5\b(?!\s*(?:redox|metabolism|/|state|conceptual|trafficking))", re.I)
_WINDOW_ASSERT = re.compile(r"\b(critical|demonstrated|established|proven|definitive|measured (?:limit|boundary|window)|therapeutic (?:limit|window)|limit of|shown to (?:close|end))\b", re.I)
_WINDOW_QUALIFIED = re.compile(r"ages tested|not a measured|not a demonstrated|was tested|that was tested|tested, not|not a definitive|never located|not measured|unmeasured|no after-onset", re.I)
_WINDOW_HISTORY = re.compile(r"\b(earlier text|formerly|previously (?:read|stated)|read\b.{0,40}superseded|superseded|replaced|withdrawn|historical|was written)\b", re.I)


def window_overreach(text: str) -> list:
    """Active sentences that present the P0-P5 ages as a measured or demonstrated therapeutic limit."""
    out = []
    for sentence in re.split(r"(?<=\.)\s+|\n", text):
        if _WINDOW_REF.search(sentence) and _WINDOW_ASSERT.search(sentence) \
                and not _WINDOW_QUALIFIED.search(sentence) and not _WINDOW_HISTORY.search(sentence):
            out.append(sentence.strip())
    return out


class SupersededWordingGoneIT6(unittest.TestCase):
    """BATCH_20261019_027: the iteration-6 results as the registries, ledgers, map and consumers must now state them.

    Positive checks only (what each surface DOES say), plus the exact old strings that were replaced in place:
      1. the map no longer calls NMDAR «pharmacologically established with d-APV inside the WWOX system» and states that
         NMDAR activity is required while a raised NMDAR function is not shown; boundary 5 and the R-01 cell state prevention;
      2. every claim that carried a «rescue» or «NMDAR dependence» reading has a dated wave note naming this batch and keeps its Status;
      3. the ledgers carry the dated UPDATE bullets (window state, three readings unranked, sign not resolved, no resolvable sign),
         the earlier headings are still there (append-only), and the magnesium hypothesis exists with Status generated;
      4. the consumers (cards C01 and C04, needs, the p5 tables, the join output, both views) no longer say «R-class demonstrated»
         or «would act in humans at the stage a patient is treated» and say early-window / manifested deficit;
      5. every receipt a PAPER reading update names is recorded in the receipt ledger; the working model is still the version
         the manifest declares and does not name this batch.
    It does not prove that a paraphrase outside these strings is absent.
    """

    DR = "disease-models/wwox/research/drug_repurposing/"
    BATCH = "BATCH_20261019_027"
    SURFACES = [
        "disease-models/wwox/analysis/mechanism_intervention_map.md",
        DR + "cards/C01_aav9_wwox.card.json",
        DR + "cards/C01_aav9_wwox.packet.json",
        DR + "cards/C04_aav9_endpoint_families.card.json",
        DR + "needs/needs.json",
        DR + "p5/cells.json",
        DR + "p5/tables_deep.md",
        DR + "join/cards.json",
        DR + "view/index.html",
        DR + "view/index_shareable.html",
        "disease-models/wwox/research/repurposing_batch_selection_20261029_module.md",
    ]

    def read(self, rel):
        return (ROOT / rel).read_text(encoding="utf-8")

    def block(self, rel, start, end_marker):
        text = self.read(rel)
        head = text.split(start, 1)[1]
        return head.split(end_marker, 1)[0]

    def test_map_says_nmdar_activity_is_required_not_that_nmdar_function_is_raised(self):
        m = self.read(self.SURFACES[0])
        self.assertNotIn("ACTIONABLE NODE: NMDAR (pharmacologically established with d-APV inside the WWOX system)", m)
        self.assertIn("NMDAR ACTIVITY IS REQUIRED for the bursting", m)
        self.assertIn("a RAISED NMDAR function is NOT shown", m)
        self.assertIn("three readings fit it and are not ranked", m)
        self.assertIn("F04_nmdar_intervention_class", m)
        self.assertIn(self.BATCH, m)

    def test_map_states_gene_addition_as_prevention_in_the_mouse(self):
        m = self.read(self.SURFACES[0])
        self.assertIn("5. **Prevention, not recovery (added 2026-10-29", m)
        self.assertIn("PREVENTED or EARLY-WINDOW", m)
        self.assertIn("RECOVERED\n   for none", m)
        self.assertIn("early-window prevention, not recovery of a manifested deficit; CHAIN A boundary 5", m)
        r01 = m.split("### R-01 ", 1)[1].split("### R-02 ", 1)[0]
        self.assertIn("updated 2026-10-29 (IT6 P7): in the mouse this is early-window prevention", r01)

    def test_consumers_say_early_window_and_not_recovery_of_a_manifested_deficit(self):
        for rel in self.SURFACES[1:]:
            text = self.read(rel)
            self.assertNotIn("R-class demonstrated", text, rel)
            self.assertNotIn("act in humans at the stage a patient is treated", text, rel)
        for rel in (self.DR + "cards/C01_aav9_wwox.packet.json", self.DR + "cards/C04_aav9_endpoint_families.card.json"):
            self.assertIn("arly-window", self.read(rel), rel)
        needs = self.read(self.DR + "needs/needs.json")
        self.assertIn("That gene addition would recover a manifested deficit", needs)
        self.assertIn("Do not carry a perinatal result to a later intervention", needs)
        cells = self.read(self.DR + "p5/cells.json")
        self.assertIn("Early-window restoration by replacement", cells)

    def test_claims_carry_the_wave_note_and_keep_their_status(self):
        text = self.read("disease-models/wwox/registries/claim_registry_current.md")
        expect = {
            "CLAIM 004": ("consolidated baseline", "PREVENTED or EARLY-WINDOW"),
            "CLAIM 011": ("flagged for review", "PREVENTED or EARLY-WINDOW"),
            "CLAIM 040": ("in observation", "PREVENTED or EARLY-WINDOW"),
            "CLAIM 002": ("consolidated baseline", "PREVENTION by construction"),
            "CLAIM 021": ("consolidated baseline", "NEEDS NMDAR activity"),
            "CLAIM 005": ("consolidated baseline", "NOT uniform across the Wwox models"),
        }
        for cid, (status, phrase) in expect.items():
            blk = text.split("## " + cid + "\n", 1)[1].split("\n## CLAIM ", 1)[0]
            self.assertIn("**Status:** " + status, blk, cid)
            self.assertIn("**Wave note (2026-10-29, `" + self.BATCH + "`", blk, cid)
            self.assertIn(phrase, blk, cid)
        c21 = text.split("## CLAIM 021\n", 1)[1].split("\n## CLAIM ", 1)[0]
        self.assertIn("It is not shown to be a raised NMDAR function", c21)
        self.assertIn("are NOT ranked here", c21)

    def test_ledgers_carry_the_updates_and_keep_the_earlier_headings(self):
        disc = self.read("disease-models/wwox/research/discovery_ledger_current.md")
        def rec(text, ident, nxt):
            return text.split("### " + ident, 1)[1].split(nxt, 1)[0]
        for ident, nxt, phrase in (
            ("DL-MECH-011 ", "\n### ", "PREVENTED or EARLY-WINDOW"),
            ("DL-MOL-005 ", "\n### ", "early-window prevention in the null mouse"),
            ("DL-MOL-001 ", "\n### ", "NEEDS NMDAR activity"),
            ("DL-REPO-002 ", "\n### ", "NOT resolved across the Wwox models"),
            ("DL-MECH-173 ", "\n### ", "no resolvable sign at about 0.3"),
            ("DL-BIO-085 ", "\n### ", "No function per molecule has been measured for any WWOX allele"),
        ):
            blk = rec(disc, ident, nxt)
            self.assertIn("UPDATE 2026-10-29 (`" + self.BATCH + "`", blk, ident)
            self.assertIn(phrase, blk, ident)
        # append-only: the earlier heading of DL-REPO-002 and the earlier wording of DL-MOL-001 are still there
        self.assertIn("direzione RISOLTA (WWOX-loss → infiammazione ↑ → serve INIBIRE)", disc)
        self.assertIn("dipendenza NMDAR dimostrata (Breton)", disc)
        hyp = self.read("disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md")
        for ident, phrase in (("HYP-20261027-01 ", "F04_nmdar_intervention_class"), ("HYP-20261026-10 ", "no resolvable sign at about 0.3"),
                              ("HYP-20260709-08 ", "wild-type function ruler first")):
            blk = hyp.split("### " + ident, 1)[1].split("\n### ", 1)[0]
            self.assertIn("UPDATE 2026-10-29 (`" + self.BATCH + "`", blk, ident)
            self.assertIn(phrase, blk, ident)
        mg = hyp.split("### HYP-20261029-01 ", 1)[1]
        self.assertIn("**Status:** `generated`", mg)
        self.assertIn("the recording bath is not stated", mg)
        self.assertIn("Not medical advice", mg)
        self.assertNotIn("HYP-20261029-01", self.read("disease-models/wwox/research/dismissal_ledger_current.md"))

    def test_every_receipt_a_registry_note_names_is_recorded_and_the_working_model_is_untouched(self):
        ledger = self.read("disease-models/wwox/registries/fulltext_read_receipts.jsonl")
        recorded = set(re.findall(r'"event_id": ?"(FTR-[0-9]+-[0-9]+-[0-9]+)"', ledger))
        papers = self.read("disease-models/wwox/registries/paper_registry_current.md")
        named = set()
        for line in papers.splitlines():
            if "**Reading update (2026-10-29, `" + self.BATCH in line:
                named |= set(re.findall(r"FTR-[0-9]{8}-[0-9]+-[0-9]+", line))
        self.assertGreaterEqual(len(named), 14)
        self.assertFalse(named - recorded, sorted(named - recorded))
        wm = self.read("disease-models/wwox/registries/working_model_current.md")
        version = re.search(r"\*\*Version:\*\* (WM_v\S+)", wm).group(1)
        self.assertIn(version.split("_")[1], self.read("framework/state/state_manifest_current.md"))
        # BATCH_20261019_027 changed no working-model statement; it is named only in the Last update line of its follow-up 028
        self.assertNotIn(self.BATCH, "\n".join(l for l in wm.splitlines() if not l.startswith("**Last update:**")))

    def test_working_model_wording_after_the_review(self):
        """BATCH_20261019_028 (WM_v7.29): the ages tested are not a measured window; the durable-rescue lines carry the
        early-window qualifier; the early-childhood sentence carries a premise tag; the version equals the manifest's."""
        wm = self.read("disease-models/wwox/registries/working_model_current.md")
        body = "\n".join(l for l in wm.splitlines() if not l.startswith("**Last update:**"))
        self.assertIn("early postnatal window tested (P0–P5 in mouse: ages tested, not a measured boundary)", wm)
        self.assertEqual(window_overreach(body), [], "an active sentence presents the tested ages as a demonstrated limit")
        self.assertEqual(body.count("(early-window prevention in the null mouse; no after-onset mouse arm)"), 3)
        self.assertIn("`PREMISE_TAG: DEFAULT_FROM_TEXTBOOK` — an unsourced expert-sentiment sentence", wm)
        version = re.search(r"\*\*Version:\*\* (WM_v\S+)", wm).group(1)
        manifest = self.read("framework/state/state_manifest_current.md")
        self.assertIn("working_model_version: " + version.split("_20")[0], manifest)
        self.assertIn("`BATCH_20261019_028`", wm.split("\n## Disease identity", 1)[0])
        hist = self.read("disease-models/wwox/registries/working_model_history.md")
        self.assertIn("| **WM_v7.29** |", hist)
        narrative = self.read("disease-models/wwox/disease_model.md")
        self.assertIn("ages tested, not a measured boundary", narrative)
        self.assertEqual(window_overreach(narrative), [])

    def test_window_detector_allows_a_correct_conclusion_with_a_historical_quote(self):
        good = self.read("disease-models/wwox/registries/working_model_current.md")
        quoted = good + '\nThe 2026-10-28 text read "critical early postnatal window (P0–P5 in mouse)"; it was superseded by this update.\n'
        self.assertEqual(window_overreach(quoted), [])

    def test_window_detector_catches_an_active_overinterpretation_beside_the_correct_text(self):
        good = self.read("disease-models/wwox/registries/working_model_current.md")
        for bad in ("P5 is the experimentally demonstrated therapeutic limit of gene addition.",
                    "The critical window closes at P5 in the mouse.",
                    "Treatment after P5 was shown to fail: the limit of the window is established at P0–P5."):
            self.assertEqual(window_overreach(good), [])
            self.assertEqual(len(window_overreach(good + "\n" + bad + "\n")), 1, bad)

    def test_repaired_wording_of_the_review_is_in_place(self):
        m = self.read(self.SURFACES[0])
        self.assertEqual(window_overreach(m), [], "the map presents the tested ages as a demonstrated limit")
        self.assertIn("read in this corpus (two mouse studies; a bounded search for inducible neural Wwox models found none)", m)
        self.assertIn("in part (partial, not normalised) for motor score and, at the high dose only, for gliosis", m)
        self.assertIn("insoluble pellet protein with no measurable activity (yeast and U2OS", m)
        self.assertIn("**needs NMDAR activity** (the gap-junction half withdrawn", m)
        self.assertIn("a proposed order of work, not a ranking", m.lower())
        hyp = self.read("disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md")
        mg = hyp.split("### HYP-20261029-01 ", 1)[1]
        self.assertIn("raised K+ or 4-aminopyridine", mg)
        self.assertIn("so the reachable rise may fall short", mg)
        self.assertIn("uncorrected for the liquid-junction potential", mg)
        self.assertIn("**Lever:** 3 (repurposing, nutrient class)", mg)
        h27 = hyp.split("### HYP-20261027-01 ", 1)[1].split("\n### ", 1)[0]
        self.assertIn("a candidate first drug arm, a proposal and not a ranking", h27)
        self.assertIn("time-stamped before unblinding", h27)
        lit = self.read("disease-models/wwox/registries/literature_tracking_log_current.md")
        self.assertIn("insoluble pellet protein with no measurable activity", hyp)
        self.assertIn("insoluble pellet protein with no measurable activity", lit)
        disc = self.read("disease-models/wwox/research/discovery_ledger_current.md")
        d11 = disc.split("### DL-MECH-011 ", 1)[1].split("\n### ", 1)[0]
        self.assertIn("in part (partial, not normalised) for motor score", d11)
        r2 = disc.split("### DL-REPO-002 ", 1)[1].split("\n### ", 1)[0]
        self.assertIn("superseded in effect by this update", r2)
        self.assertIn("by the catalogue's own fields", r2)
        claims = self.read("disease-models/wwox/registries/claim_registry_current.md")
        c21 = claims.split("## CLAIM 021\n", 1)[1].split("\n## CLAIM ", 1)[0]
        self.assertIn("a competitive antagonist that eliminated the bursting", c21)
        papers = self.read("disease-models/wwox/registries/paper_registry_current.md")
        self.assertIn("the only such rescue noted in the readings of this batch", papers)


if __name__ == "__main__":
    unittest.main(verbosity=2)
