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


class ReconciledMeasurements(unittest.TestCase):
    """HE51: the ADV-006 reconciliation reaches the generator as design rows (INV-05) without a measurement being listed twice, a conflict resolved, an order turned into a dependency or a design turned into an observation."""
    PKG = "measurement_reconciliation_adv006_20261114"
    SRC = HERE.parent / PKG / "output"

    @classmethod
    def setUpClass(cls):
        cls.rows, cls.unmapped = cp.design_rows()
        cls.mine = {r["design_row_id"]: r for r in cls.rows if r["package"] == cls.PKG}
        def tsv(n):
            with open(cls.SRC / n, encoding="utf-8", newline="") as f:
                return list(csv.DictReader(f, delimiter="\t"))
        cls.meas, cls.conf = tsv("measurements.tsv"), tsv("conflicts.tsv")

    def row(self, table, key):
        return self.mine[f"{self.PKG}::{table}::{key}"]

    def test_every_measurement_and_every_conflict_of_the_package_travels_once_and_the_source_tables_are_not_registered(self):
        self.assertEqual(len([i for i in self.mine if "::measurements.tsv::" in i]), len(self.meas))
        self.assertEqual(len([i for i in self.mine if "::conflicts.tsv::" in i]), len(self.conf))
        listed = {r["package"] for r in self.rows}
        self.assertFalse({"chloride_gradient_sci42_20261110", "inhibitory_defect_sci47_20261112", "glun2b_comparators_sci42_20261110"} & listed)   # one measurement, one row: no second source of the same request
        self.assertEqual({r["inv_id"] for r in self.mine.values()}, {"INV-05"})

    def test_each_mapped_cell_is_the_source_cell_verbatim_with_its_own_column_name(self):
        for m in self.meas:
            r = self.row("measurements.tsv", m["m_id"])
            for col in ("name", "source_names", "requests_merged", "preparation", "mode_and_configuration", "unit_of_analysis", "age_bin", "cohort_and_genotype_arms"):
                if m[col]:
                    self.assertIn(f"{col}: {m[col]}", r["step"])
            self.assertIn(m["interpretable_after"], r["precondition_unmet_until_the_step_before_is_run"])
            self.assertIn(m["not_decided_by_it"], r["scope_and_what_the_result_is_not"])

    def test_missing_fields_stay_explicit_and_a_design_is_not_an_observation(self):
        for i, r in self.mine.items():
            self.assertTrue(r["observation"].startswith("absent"))
            if r["table"] == "measurements.tsv":
                self.assertEqual((r["controls_as_documented_by_the_package"], r["possible_outcomes_conditions_and_cautions_not_observed"], r["hypothesis_link"]), (cp.ABSENT,) * 3)

    def test_open_questions_closed_is_never_a_resolved_state(self):
        for m in self.meas:
            d = self.row("measurements.tsv", m["m_id"])["conditioned_decision"]
            self.assertIn("open_questions_closed [", d)
            self.assertIn("no question is closed by this row", d)
            self.assertIn(m["open_questions_closed"], d)

    def test_the_six_genuine_conflicts_survive_with_both_quotes_and_no_side_chosen(self):
        genuine = sorted(c["conflict_id"] for c in self.conf if c["type"] == "genuine")
        self.assertEqual(genuine, ["CF01", "CF03", "CF04", "CF05a", "CF05b", "CF23"])
        for c in self.conf:
            r = self.row("conflicts.tsv", c["conflict_id"])
            self.assertIn(f"type: {c['type']}", r["step"])
            self.assertIn(c["quote_A"], r["step"]); self.assertIn(c["quote_B"], r["step"])
            self.assertEqual(r["hypothesis_link"], f"m_id: {c['m_id']}")                       # the link is the package's own list ("M01;M03"), not re-split or chosen
            self.assertIn("no side is chosen by this row", r["scope_and_what_the_result_is_not"])
        cf23 = self.row("conflicts.tsv", "CF23")["step"]
        self.assertIn("same percent of evoked synaptic charge removed", cf23); self.assertIn("membrane potential and input resistance", cf23)

    def test_an_order_of_priority_is_not_carried_as_a_dependency_and_a_stated_dependency_is_carried_as_quoted(self):
        first = self.row("measurements.tsv", "M01")["precondition_unmet_until_the_step_before_is_run"]
        self.assertIn("none (first in SCI42's order)", first); self.assertIn("an order of cost or priority inside it is not a dependency", first)
        self.assertIn("interpretable only after mIPSC, agonist response and E_GABA place the deficit", self.row("measurements.tsv", "M16")["precondition_unmet_until_the_step_before_is_run"])

    def test_the_package_local_id_is_not_a_global_one(self):
        other = Path(tempfile.mkdtemp(prefix="he51_")) / "other_pkg"
        (other / "output").mkdir(parents=True)
        (other / "output" / "measurements.tsv").write_text("m_id\tname\nM01\ttissue and bath pH\n", encoding="utf-8")
        pk = hp.load_all() + [dict(hp.load_design_only(other), name="other_pkg", inv_id="INV-05")]
        with mock.patch.object(hp, "load_all", return_value=pk), mock.patch.dict(cp.DESIGN_MAP, {"other_pkg": {"measurements.tsv": dict(step=["name"], precondition=[], controls=[], outcomes=[], decision=[], scope=[], link=[])}}):
            rows, _ = cp.design_rows()
        ids = [r["design_row_id"] for r in rows if r["table"] == "measurements.tsv" and r["step"].startswith("m_id: M01 ")]
        self.assertEqual(len(ids), 2); self.assertEqual(len(set(ids)), 2)

    def test_without_the_package_the_earlier_rows_are_unchanged(self):
        pk = [p for p in hp.load_all() if p["dir"].parent.name != self.PKG]
        with mock.patch.object(hp, "load_all", return_value=pk):
            rows, _ = cp.design_rows()
        self.assertEqual([r for r in rows], [r for r in self.rows if r["package"] != self.PKG])
        self.assertEqual(len(rows), 13)
        self.assertFalse([r for r in cp.package_rows()[0] if self.PKG in r["package_ref"]])      # nothing reached the hypothesis path

    def test_the_investigation_pointer_names_the_design_rows_without_linking_them_to_a_hypothesis(self):
        for r in cp.rows():
            if r["inv_id"] == "INV-05":
                ptr = r["design_rows_same_investigation"]
                self.assertIn("53 design rows", ptr); self.assertIn("not linked to this hypothesis by any package", ptr)
                self.assertIn(f"{self.PKG}::measurements.tsv::M16", ptr); self.assertIn(f"{self.PKG}::conflicts.tsv::CF23", ptr)
                self.assertNotIn("[M01", ptr)                                                         # no bare key that could be read as another package's M01 or M16
                ids = {i for i in ptr.split("design_row_id")[0].replace("; ", " ").split() if "::" in i}
                self.assertTrue(set(i.strip(";") for i in ids) <= set(self.mine))                       # every id named exists as a row of the file
                self.assertNotIn(r["proposal_id"], ptr)
            else:
                self.assertIn("none listed", r["design_rows_same_investigation"])                           # INV-18 has no registered design: said, not left empty
        isr = next(r for r in cp.package_rows()[0] if r["inv_id"] == "INV-02")["design_rows_same_investigation"]
        self.assertIn("not mapped, so not in that file: isrib_discrim_20261108::grid.tsv::G01", isr)               # a reachable table the file does not hold is not advertised as in it
        self.assertEqual(cp.rows(link=False)[0]["design_rows_same_investigation"], "")                      # the ablation still rebuilds what the generator held before

    def test_without_the_package_the_pointer_says_none(self):
        pk = [p for p in hp.load_all() if p["dir"].parent.name != self.PKG]
        self.assertIn("none listed for INV-05", cp.design_pointer("INV-05", pk))


class LeverJoin(unittest.TestCase):
    """HE53 (ADV's assignment): SCI47's levers are INV-05 hypotheses in their own layout and each joins the ADV-006 rows through keys the packages declare, one hop, nothing read from prose beyond a list that starts a cell."""
    PKG = "inhibitory_defect_sci47_20261112"

    @classmethod
    def setUpClass(cls):
        cls.rows, cls.unm = cp.package_rows()
        cls.by = {r["package_ref"].split(" @ ")[0]: r for r in cls.rows}
        with open(HERE.parent / cls.PKG / "output" / "levers.tsv", encoding="utf-8", newline="") as f:
            cls.src = {r["lever_id"]: r for r in csv.DictReader(f, delimiter="\t")}

    def lever(self, k):
        return self.by[f"{self.PKG}::{k}"]

    def test_six_levers_travel_verbatim_and_the_dropped_ones_stay_dropped(self):
        self.assertEqual(sorted(k.split("::")[1] for k in self.by if k.startswith(self.PKG)), [f"L{n}" for n in range(1, 7)])
        self.assertEqual(self.unm, {})
        for k, src in self.src.items():
            row = self.lever(k)
            self.assertIn(src["status"], row["premise_and_action"])
            self.assertIn(src["result_that_would_reject_it"], row["decision_measure"])
            self.assertIn(src["counter_evidence"], row["competing_explanations"])
        self.assertIn("status: dropped as a drug arm now", self.lever("L3")["premise_and_action"])
        self.assertIn("status: dropped", self.lever("L6")["premise_and_action"])
        self.assertTrue(all("not stated here, not absent" in r["expected_result_by_explanation"] for r in (self.lever(k) for k in self.src)))   # no prediction is invented, and the absence is only of this table

    def test_l1_and_l2_reach_their_measurement_rows_gating_rows_comparator_and_genuine_conflicts_by_declared_keys(self):
        for k, m in (("L1", "M16"), ("L2", "M17")):
            j = self.lever(k)["design_join"]
            self.assertIn(f"{cp.ADV006}::measurements.tsv::{m} (declared by sci47_inhibitory#levers:{k}", j)
            self.assertIn("rows named at the start of that cell: M02, M04, M05", j)
            self.assertRegex(j, r"M15 'every drug arm \(M16, M17, M18, M19, M20\)'")                      # the comparator co-requirement, in its own cell's words
            for cf in ("CF04", "CF05a", "CF05b", "CF23"):
                self.assertIn(f"{cf} [type: genuine", j.split("conflicts of type genuine")[1].split("rows of other types")[0])
            self.assertIn("listed and NOT followed", j); self.assertIn("M01; genuine conflicts on them, for the reader to weigh: CF01, CF03", j)   # reachable only on a second hop, said as such
            self.assertIn("no side is chosen on any conflict; no order here is a result", j)
            self.assertIn("not an observation", j)

    def test_a_lever_no_row_declares_is_not_joined_and_the_absence_says_so(self):
        j = self.lever("L6")["design_join"]
        self.assertIn("not joined (not stated is not tested and absent)", j)

    def test_an_id_inside_a_quotation_is_not_a_pointer_and_the_two_id_spaces_stay_apart(self):
        m20 = {"x": 1}
        rows = [dict(package=cp.ADV006, table="measurements.tsv", key="M20", row=dict(preparation="p", age_bin="a", cohort_and_genotype_arms="c", requests_merged="sci47_inhibitory#levers:L3 ; map#open_questions_map:IT46-Q04", interpretable_after='M05 ("E_GABA measured before and after (M01)" (conditional_prediction.tsv))', lever_or_comparison_gated="E-chloride")),
                dict(package=cp.ADV006, table="measurements.tsv", key="M05", row=dict(preparation="p", age_bin="a", cohort_and_genotype_arms="c", requests_merged="x", interpretable_after="unordered", lever_or_comparison_gated="L3")),
                dict(package=cp.ADV006, table="measurements.tsv", key="M01", row=dict(preparation="p", age_bin="a", cohort_and_genotype_arms="c", requests_merged="sci42_chloride#new_measurements:M01", interpretable_after="none", lever_or_comparison_gated="")),
                dict(package=cp.ADV006, table="conflicts.tsv", key="CF99", row=dict(m_id="M01", type="genuine", cell_type="t", source_A="a", quote_A="qa", source_B="b", quote_B="qb", adjudicable_from_the_packages="no"))]
        j = cp.design_join(self.PKG, "L3", rows)
        self.assertIn("rows named at the start of that cell: M05", j)
        self.assertNotIn("CF99", j.split("second-hop")[0])                                           # M01 sits inside a quotation (SCI42's own M01): never read as ADV-006's M01
        self.assertNotIn("M01", j.split("rows named at the start of that cell: ")[1].split(" |")[0])
        self.assertEqual(cp.design_join("some_other_package", "L1", rows), "")                       # a package without a declared alias gets no join
        self.assertIn("not registered", cp.design_join(self.PKG, "L1", []))                          # without the ADV-006 package the earlier behaviour stays: said, not guessed

    def test_the_earlier_packages_rows_carry_no_join_and_adv004_wording_is_untouched(self):
        self.assertTrue(all(r["design_join"] == "" for r in self.rows if self.PKG not in r["package_ref"]))
        l2 = self.lever("L2")
        self.assertIn(self.src["L2"]["functional_comparator"], l2["decision_measure"])               # the dated ADV-004/ADV-006 notes travel in the owners' own words
        self.assertNotIn("preferring", l2["design_join"].lower())                                    # nothing here carries a subtype preference
        self.assertTrue(all(r["direction_stated"].startswith("none") for r in self.rows if self.PKG in r["package_ref"]))

    def test_it52_findings_the_join_carries_conflict_content_preparation_and_age_and_a_dropped_lever_is_labelled(self):
        j = self.lever("L1")["design_join"]
        self.assertIn("cell_type: other (matching variable of the matched arm)", j)                                   # CF23's content, as the design file carries it, not only its id
        self.assertIn("Matched non-GABAergic suppression of bursts titrated to the same percent of evoked synaptic charge removed", j)
        self.assertIn("membrane potential and input resistance", j)                                                 # both quotes of CF23, side by side, none preferred
        self.assertIn("preparation: ", j); self.assertIn("age_bin: ", j)                                            # each joined row's own preparation and age travel
        l3 = self.lever("L3")
        self.assertEqual((l3["kind"], self.lever("L6")["kind"]), ("package_row_dropped_by_the_package",) * 2)
        self.assertTrue(l3["nomination"].startswith("NOT PROPOSED: the package drops this row"))
        self.assertEqual(self.lever("L1")["kind"], "conditional_hypothesis_from_package")                            # an active lever keeps its label
        self.assertTrue(l3["design_rows_same_investigation"].startswith("dropped by the package"))
        self.assertIn("a source's own id space", l3["design_join"])                                                 # SCI42's M01 inside an ADV-006 cell is named as another id space

    def test_the_sentences_that_were_false_for_this_package_are_gone_and_the_mapping_says_it_is_unconfirmed(self):
        row = self.lever("L1")
        self.assertNotIn("not stated by the package (missing)", row["expected_result_by_explanation"])
        self.assertIn("matrix.tsv", row["expected_result_by_explanation"])                                          # where the package does state what each outcome favours
        self.assertNotIn("does not classify them as rivals, complementary or compatible", row["competing_explanations"])
        self.assertIn("not confirmed by the package's owners", row["nomination"])
        other = next(r for r in self.rows if "hcn_20261107" in r["package_ref"])                                     # a package whose mapping the owners confirmed: its own wording is untouched
        self.assertTrue(other["expected_result_by_explanation"].startswith("not stated by the package (missing)"))
        self.assertIn("the package does not classify them as rivals, complementary or compatible", other["competing_explanations"])

    def test_the_committed_table_is_what_the_generator_writes(self):
        with open(HERE / "conditional_proposals_packages_it47.tsv", encoding="utf-8", newline="") as f:
            committed = list(csv.DictReader(f, delimiter="\t"))
        self.assertEqual(committed, [dict(r) for r in self.rows])


if __name__ == "__main__":
    unittest.main(verbosity=2)
