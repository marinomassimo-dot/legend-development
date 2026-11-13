#!/usr/bin/env python3
"""HE50: a design-only package reaches the generator as steps, controls and decision branches kept apart; a possible outcome is never data, a control never a hypothesis, a missing field stays missing."""
import csv, sys, tempfile, unittest
from pathlib import Path
from unittest import mock
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import conditional_proposals as cp  # noqa: E402
import hypothesis_package as hp  # noqa: E402


class DesignRows(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows, cls.unmapped = cp.design_rows()
        cls.by = {r["design_row_id"]: r for r in cls.rows}

    def isr(self, step):
        return next(r for i, r in self.by.items() if i.startswith(f"isrib_discrim_20261108::design.tsv::{step} "))

    def test_every_branch_of_the_first_fork_travels_including_the_contrary_and_the_uninformative_one(self):
        out = self.isr("1")["possible_outcomes_conditions_and_cautions_not_observed"]
        for branch in ("(a) phospho-eIF2alpha raised and ISRIB restores translation", "(b) phospho-eIF2alpha not raised and translation lowered: go to step 2",
                       "(c) translation not lowered: stop, change stage or cell type before concluding", "(d) engagement control fails: uninformative"):
            self.assertIn(branch, out)
        self.assertTrue(out.startswith("if_result_X_then: "))                             # the column keeps its own name: the cell is a set of possible outcomes, not a result

    def test_a_possible_outcome_is_never_presented_as_an_observation(self):
        self.assertTrue(self.rows and all(r["observation"].startswith("absent") for r in self.rows))
        self.assertTrue(all("observation" not in r["step"].lower().split("|")[0] for r in self.rows))

    def test_a_control_the_package_says_is_not_qualified_is_not_turned_into_a_qualified_one(self):
        self.assertIn("second chemotype is NOT qualified in the module", self.isr("2")["controls_as_documented_by_the_package"])
        self.assertTrue(self.isr("2")["controls_as_documented_by_the_package"].startswith("controls_already_qualified_in_module: "))

    def test_the_precondition_is_carried_as_stated_and_step_zero_has_none(self):
        self.assertEqual(self.isr("1")["precondition_unmet_until_the_step_before_is_run"], "condition_on: step 0 passed")
        self.assertEqual(self.isr("0")["precondition_unmet_until_the_step_before_is_run"], "condition_on: nothing")

    def test_a_field_the_table_does_not_have_is_absent_and_an_empty_cell_is_a_different_statement(self):
        self.assertEqual(self.isr("1")["scope_and_what_the_result_is_not"], cp.ABSENT)
        self.assertEqual(self.isr("1")["hypothesis_link"], cp.ABSENT)
        with tempfile.TemporaryDirectory() as t:
            o = Path(t) / "pkg" / "output"; o.mkdir(parents=True)
            (o / "design.tsv").write_text("step\tquestion\tcondition_on\tif_result_X_then\nS1\tdoes A change B?\t\tif yes go on\n", encoding="utf-8")
            pk = [dict(hp.load_design_only(Path(t) / "pkg"), name="pkg", inv_id="INV-9")]
            with mock.patch.object(hp, "load_all", return_value=pk), mock.patch.dict(cp.DESIGN_MAP, {"output": {}, "pkg": {"design.tsv": dict(step=["question"], precondition=["condition_on"], controls=["controls"], outcomes=["if_result_X_then"], decision=[], scope=[], link=[])}}):
                rows, unmapped = cp.design_rows()
        self.assertEqual(rows[0]["precondition_unmet_until_the_step_before_is_run"], "condition_on: " + cp.EMPTY)    # the column exists, the author left it empty
        self.assertEqual(rows[0]["controls_as_documented_by_the_package"], "controls: " + cp.ABSENT)                # the column does not exist

    def test_a_second_layout_keeps_its_hypothesis_link_so_h2_rows_do_not_raise_the_h1_investigation(self):
        ex = {i.rsplit("::", 1)[1]: r for i, r in self.by.items() if i.startswith("myelin_generative_it36_20261108/levers_bc::")}
        self.assertEqual(sorted(ex), [f"EX{n}" for n in range(1, 8)])
        self.assertEqual({k: v["hypothesis_link"] for k, v in ex.items() if k in ("EX5", "EX6", "EX7")}, {k: "hyp_id: H2" for k in ("EX5", "EX6", "EX7")})
        self.assertEqual({v["inv_id"] for v in ex.values()}, {"INV-12"})                  # one investigation per registration: the link cell is what tells H2 from H1
        self.assertIn("mechanism_control: none possible in pooled data", ex["EX1"]["controls_as_documented_by_the_package"])   # 'none possible' stays absent, not satisfied
        self.assertIn("not_a_substitute_for: EX2 and EX3", ex["EX1"]["scope_and_what_the_result_is_not"])

    def test_a_table_the_reader_reaches_but_no_map_covers_is_reported_not_guessed(self):
        self.assertEqual(self.unmapped, {("INV-02", "isrib_discrim_20261108", "grid.tsv"): 12})

    def test_the_earlier_paths_are_unchanged_by_the_new_role(self):
        pr, unm = cp.package_rows()
        self.assertEqual(unm, {})
        self.assertTrue(pr and not [r for r in pr if "::design.tsv::" in r["package_ref"] or "::experiments.tsv::" in r["package_ref"] or "::grid.tsv::" in r["package_ref"]])   # no design row leaked into the hypothesis path
        self.assertEqual(hp.hypotheses_for(hp.load_all(), "INV-12")["state"], "NO_HYPOTHESES_LISTED")                                          # registering a design adds no hypothesis to its investigation

    def test_the_committed_table_is_what_the_generator_writes(self):
        committed = list(csv.DictReader(open(HERE / "conditional_design_steps_it50.tsv", encoding="utf-8", newline=""), delimiter="\t"))
        self.assertEqual(committed, [dict(r) for r in self.rows])


if __name__ == "__main__":
    unittest.main(verbosity=2)
