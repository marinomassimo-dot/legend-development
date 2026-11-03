#!/usr/bin/env python3
"""Tests for the IT21 P3b tables. Production code under test (build_p3b_it21.py, the P2 status vocabulary); committed tables for the properties the README rests on.

  python3 test_p3b_it21.py          (unittest; offline; seconds)
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, importlib.util, re, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


B = load("build_p3b_it21", HERE / "build_p3b_it21.py")
G = load("run_generation_it21", DR / "generation_it21_p2_20261103/run_generation_it21.py")


def tsv(name):
    return list(csv.DictReader((HERE / name).read_text().splitlines(), delimiter="\t"))


class Proposals(unittest.TestCase):
    def test_count_and_ids(self):
        ids = [p["id"] for p in B.P]
        self.assertTrue(6 <= len(ids) <= 10)
        self.assertEqual(len(ids), len(set(ids)))

    def test_vocabularies(self):
        for p in B.P:
            self.assertIn(p["origin_path"], B.ORIGIN_PATHS)
            self.assertIn(p["mechanism"], B.MECHANISMS)
            self.assertIn(p["goal_depth"], B.GOALS)
            self.assertIn(p["disposition"], B.DISPOSITIONS)
            for arm in ("arm_if_process_harmful", "arm_if_process_protective"):
                self.assertIn(p[arm].split(":")[0], B.ARM_STATUS)

    def test_arm_status_goes_through_the_p2_checker(self):
        for p in B.P:
            for arm in ("arm_if_process_harmful", "arm_if_process_protective"):
                G.check_status(p[arm].split(":")[0])

    def test_depth_and_dependence_are_separate_fields(self):
        self.assertIn("goal_depth", B.PROPOSAL_COLS)
        self.assertIn("dependence_on_variant_track", B.PROPOSAL_COLS)
        self.assertEqual(sum(p["goal_depth"] == "deep_recovery" for p in B.P), sum(p["dependence_on_variant_track"].startswith("B") and p["goal_depth"] == "deep_recovery" for p in B.P))
        self.assertGreaterEqual(sum(p["goal_depth"] == "deep_recovery" for p in B.P), 1)
        self.assertGreaterEqual(sum(p["goal_depth"] == "partial_benefit" for p in B.P), 1)

    def test_every_proposal_has_origin_and_assumption(self):
        for p in B.P:
            for k in ("generating_premise_and_pointer", "decisive_assumption", "lever_gene", "documented_action_and_level", "novelty_perimeter_searched_2026_11_03"):
                self.assertTrue(p[k].strip(), (p["id"], k))

    def test_nothing_is_called_qualified(self):
        for p in B.P:
            self.assertNotEqual(p["disposition"], "QUALIFIED_HYPOTHESIS")
        for q in B.Q:
            self.assertNotEqual(q["disposition"], "QUALIFIED_HYPOTHESIS")

    def test_both_conditional_arms_present_when_a_compound_is_proposed(self):
        for p in B.P:
            if p["selected_for_qualification"].startswith("yes"):
                self.assertTrue(p["arm_if_process_harmful"].startswith("CONDITIONAL_H_HARM"))
                self.assertTrue(p["arm_if_process_protective"].startswith("CONDITIONAL_H_PROTECT"))


class Qualification(unittest.TestCase):
    def test_five_fields_novelty_and_disposition(self):
        for q in B.Q:
            for k in ("f1_foundation", "f2_decisive_assumption", "f3_counter_evidence", "f4_next_test", "f5_result_that_changes_the_decision", "novelty_class", "disposition"):
                self.assertTrue(q[k].strip(), (q["id"], k))
            self.assertIn(q["disposition"], B.DISPOSITIONS)
            self.assertTrue(any(q["novelty_class"].startswith(n) for n in B.NOVELTY), q["novelty_class"])

    def test_every_qualification_points_at_a_proposal_with_the_same_disposition(self):
        by = {p["id"]: p for p in B.P}
        for q in B.Q:
            self.assertEqual(by[q["proposal"]]["disposition"], q["disposition"])

    def test_four_or_more_diversified_mechanisms(self):
        by = {p["id"]: p for p in B.P}
        mech = {by[q["proposal"]]["mechanism"] for q in B.Q}
        self.assertGreaterEqual(len(B.Q), 4)
        self.assertGreaterEqual(len(mech), 4)

    def test_dispositions_are_not_all_the_same(self):
        self.assertGreaterEqual(len({q["disposition"] for q in B.Q}), 3)


class PathB(unittest.TestCase):
    def setUp(self):
        self.lev = tsv("pathb_levers_it21.tsv")
        self.comp = tsv("pathb_compounds_it21.tsv")

    def test_no_lever_is_marked_qualified(self):
        for r in self.lev:
            self.assertIn(r["lever_status"], ("LEVER_FOUND_NOT_A_TARGET", "NAMED_ALREADY", "NO_SIGNED_COMPOUND"))

    def test_handles_have_a_declared_basis(self):
        for r in csv.DictReader((HERE / "handles_it21.tsv").read_text().splitlines(), delimiter="\t"):
            self.assertIn(r["basis"], ("LEGEND_RECORD", "BACKGROUND_UNREAD"))
            self.assertTrue(r["pointer"].strip())

    def test_the_proposal_levers_are_reached_by_the_table(self):
        genes = {r["gene"]: r for r in self.lev}
        for g in ("HSPA8", "IMPA1", "THRA", "THRB", "ALOX15", "SIGMAR1"):
            self.assertGreater(int(genes[g]["families_signed"]), 0, g)
        for g in ("ITCH", "LAMP2"):
            self.assertEqual(int(genes[g]["families_signed"]), 0, g)

    def test_a_lever_absent_from_needs_is_reached_without_being_promoted(self):
        genes = {r["gene"]: r for r in self.lev}
        for g in ("IMPA1", "THRA", "ALOX15", "SIGMAR1", "GPR17"):
            self.assertEqual(genes[g]["in_needs"], "0", g)
            self.assertEqual(genes[g]["lever_status"], "LEVER_FOUND_NOT_A_TARGET", g)
        by = {p["id"]: p for p in B.P}
        for pid in ("G02", "G03", "G04", "G05"):
            self.assertNotEqual(by[pid]["disposition"], "QUALIFIED_HYPOTHESIS")

    def test_named_compounds_are_in_the_compound_table(self):
        names = {r["name"].upper() for r in self.comp}
        for n in ("FORIGERIMOD", "LITHIUM CARBONATE", "TIRATRICOL", "LIOTHYRONINE SODIUM", "ML351", "PD-146176", "BLARCAMESINE"):
            self.assertIn(n, names, n)

    def test_signs_are_signed(self):
        for r in self.comp:
            self.assertNotEqual(float(r["sign"]), 0.0)


class ReleaseSurface(unittest.TestCase):
    def test_no_email_like_string_in_the_outputs(self):
        pat = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
        for p in HERE.glob("*"):
            if p.suffix in (".tsv", ".md", ".py"):
                self.assertIsNone(pat.search(p.read_text()), p.name)

    def test_tables_have_no_ragged_rows(self):
        for name, cols in (("proposals_it21_p3b.tsv", B.PROPOSAL_COLS), ("qualification_it21_p3b.tsv", B.QUAL_COLS)):
            rows = tsv(name)
            self.assertTrue(rows)
            for r in rows:
                self.assertEqual(list(r.keys()), cols)
                self.assertNotIn(None, r)


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]], verbosity=2)
