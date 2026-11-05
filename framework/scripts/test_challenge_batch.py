#!/usr/bin/env python3
"""Regressions for challenge_batch.py: a malformed challenge, a duplicate relaunch, a motivated re-evaluation, and a result that did not return. Usage: test_challenge_batch.py"""
import sys
if len(sys.argv) > 1:
    print(__doc__); raise SystemExit(0)
import json, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import challenge_batch as C

FULL = dict(id="CH-X", origin=["a"], decision_at_stake="d", available_knowledge="k", decisive_uncertainty="u", discriminating_outcomes="o", prior_work="p", resources="r", reevaluate_when="w", nature="shared_premise")


class T(unittest.TestCase):
    def test_complete_challenge_routes_by_nature(self):
        r = C.assess(FULL, {})
        self.assertEqual((r["problems"], r["route"], r["duplicate"]), ([], "thematic_batch", False))

    def test_challenges_are_found_inside_the_authorised_queue_block(self):
        rec = {"AUTHORISED_QUEUE_X": {"MANDATE_STATE": "OPEN", "OBJ_A": {"steps": [{"step": "s", "challenge": FULL}, "bare string step"]}}}
        self.assertEqual([w for w, _ in C.challenges(rec)], ["OBJ_A[0]"])

    def test_ledger_study_id_object_is_read_by_pmid_or_doi(self):
        with tempfile.TemporaryDirectory() as tmp:
            f = Path(tmp) / "l.jsonl"
            f.write_text(json.dumps({"study_id": {"doi": "10.1/x", "pmid": "5"}, "evidence_depth": "partial_fulltext_read"}) + "\n" + json.dumps({"study_id": "PMID6", "evidence_depth": "abstract_only"}) + "\n")
            d = C.depth_by_study(f)
            self.assertEqual((d["5"], d["10.1/x"], d["6"]), (2, 2, 1))

    def test_missing_field_and_unknown_nature_are_problems(self):
        r = C.assess(dict(FULL, resources="", nature="whatever"), {})
        self.assertEqual(sorted(r["problems"]), ["nature:whatever", "resources"])

    def test_same_sources_read_again_without_a_reason_is_a_duplicate_but_a_reason_reopens(self):
        d = {"1": 2, "2": 3}
        self.assertTrue(C.assess(dict(FULL, sources=["1", "2"]), d)["duplicate"])
        self.assertFalse(C.assess(dict(FULL, sources=["1", "2"], reopen_reason="new assay data"), d)["duplicate"])
        self.assertFalse(C.assess(dict(FULL, sources=["1", "3"]), d)["duplicate"])        # one source unread: new information possible

    def test_unknown_source_is_unread_not_negative_and_return_needs_the_id(self):
        with tempfile.TemporaryDirectory() as t:
            root = Path(t); (root / "ok.txt").write_text("see CH-X here"); (root / "no.txt").write_text("nothing")
            r = C.assess(dict(FULL, sources=["9"], returned=["ok.txt", "no.txt", "gone.txt"]), {}, root)
            self.assertEqual(r["standing"], {"9": 0})
            self.assertEqual(r["returned"], {"ok.txt": True, "no.txt": False, "gone.txt": False})


if __name__ == "__main__":
    unittest.main(verbosity=1)
