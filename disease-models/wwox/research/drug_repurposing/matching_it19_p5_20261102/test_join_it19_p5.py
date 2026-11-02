#!/usr/bin/env python3
"""Tests for join_it19_p5.py (IT19 P5 step 5). Run: python3 test_join_it19_p5.py"""
import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import join_it19_p5 as j  # noqa: E402


def ref(pid, label, status="determinate_functional", dep="independent_of_module_input", err="none"):
    return {"pair_id": pid, "need_id": "N", "parent_chembl_id": "C" + pid, "compound": "c" + pid,
            "reference_label": label, "status": status, "dependency_on_module_sources": dep, "error_attribution": err}


def ans(pid, consistency, v1="compatible", v2="compatible"):
    return {"pair_id": pid, "active_consistency": consistency, "it18_L_v1": v1, "it18_L_v2": v2}


class Join(unittest.TestCase):
    def test_module_direction_reads_mixed_rows(self):
        self.assertEqual(j.module_direction("consistent"), "compatible")
        self.assertEqual(j.module_direction("mixed:consistent|direction_unresolved"), "compatible")
        self.assertEqual(j.module_direction("mixed:direction_unresolved|opposed"), "opposite")
        self.assertIsNone(j.module_direction("direction_unresolved"))
        self.assertIsNone(j.module_direction("mixed:consistent|opposed"))

    def test_unknown_reference_is_never_scored_as_an_error(self):
        rows, s = j.join([ref("P1", "unknown", "unknown_no_source_in_bounded_search")], [ans("P1", "consistent")], [ans("P1", "direction_unresolved")])
        self.assertEqual(s["active_path_before_fix"]["asserted_on_determinate"], 0)
        self.assertEqual(s["active_path_before_fix"]["accuracy"], None)
        self.assertEqual(rows[0]["before_class"], "asserted_reference_not_determinate")

    def test_a_disagreement_is_counted(self):
        _, s = j.join([ref("P1", "opposite")], [ans("P1", "consistent")], [ans("P1", "consistent")])
        self.assertEqual(s["active_path_before_fix"]["agrees"], 0)
        self.assertEqual(s["active_path_before_fix"]["asserted_on_determinate"], 1)

    def test_fix_verdicts_separate_the_two_kinds_of_change(self):
        _, s = j.join([ref("P1", "indeterminable", "indeterminable_family_level_only"), ref("P2", "compatible")],
                      [ans("P1", "consistent"), ans("P2", "consistent")],
                      [ans("P1", "direction_unresolved"), ans("P2", "direction_unresolved")])
        verdicts = {r["pair_id"]: r["verdict"] for r in s["rows_changed_by_fix"]}
        self.assertEqual(verdicts["P1"], "removed_unsupported_attribution")
        self.assertEqual(verdicts["P2"], "abstained_although_the_reference_holds_a_direction")

    def test_wilson_interval(self):
        self.assertEqual(j.wilson(0, 0), [None, None])
        lo, hi = j.wilson(12, 12)
        self.assertEqual(hi, 1.0)
        self.assertTrue(0.7 < lo < 0.8)

    def test_real_tables_reproduce_the_committed_results(self):
        _, s = j.join(j.read_tsv(HERE / "reference_it19_p5.tsv"), j.read_tsv(HERE / "module_answers_prefix.tsv"),
                      j.read_tsv(HERE / "module_answers_guarded.tsv"))
        committed = json.loads((HERE / "results_it19_p5.json").read_text(encoding="utf-8"))
        self.assertEqual(s, committed)

    def test_help_is_safe(self):
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run([sys.executable, str(HERE / "join_it19_p5.py"), "--help"], cwd=d, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0)
            self.assertEqual(list(Path(d).iterdir()), [])
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            j.main([])


if __name__ == "__main__":
    unittest.main(verbosity=2)
