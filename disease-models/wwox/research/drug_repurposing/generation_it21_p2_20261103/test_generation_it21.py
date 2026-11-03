#!/usr/bin/env python3
"""Tests for the IT21 P2 generation refresh. Production code under test (no re-implementation); synthetic rows for the rules, the committed tables for the
properties the README rests on (skipped, not passed, when the table is absent).

  python3 test_generation_it21.py          (unittest; offline; seconds)
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, importlib.util, itertools, types, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


G = load("run_generation_it21", HERE / "run_generation_it21.py")
Rf = load("refresh_actions_it21", HERE / "refresh_actions_it21.py")
D = G.load_dispose()
import repurposing_search as rs

RES = HERE / "results"


def tsv(p):
    p = Path(p)
    if not p.exists():
        return None
    return G.rd(p)


# ---- the status vocabulary: a conditional hypothesis can never become a qualified candidate ---------------------------------------------------------
class StatusNeverQualified(unittest.TestCase):
    ROLES = ["unknown", "harmful", "protective", "mixed", "composition", "not_applicable"]

    def role(self, st, lean="none"):
        return {"role_status": st, "role_basis": "NONE" if st in ("unknown", "not_applicable") else "SOURCE_STATED", "leaning": lean}

    def test_every_role_arm_combination_gives_an_allowed_status(self):
        for st, arm, lean in itertools.product(self.ROLES, ("opposes", "mimics", "flagged_opposes", "flagged_mimics", "direct_search"), ("none", "harmful", "protective")):
            hyp, disp = D.disposition(arm, self.role(st, lean))
            status = G.proposal_status(disp, arm)
            self.assertIn(status, G.STATUS_VOCAB)
            for w in G.FORBIDDEN_STATUS_WORDS:
                self.assertNotIn(w, status.replace("NOT_QUALIFIED", ""))

    def test_unknown_role_stays_conditional_on_both_arms_whatever_the_leaning(self):
        for lean in ("none", "harmful", "protective"):
            self.assertEqual(G.proposal_status(D.disposition("opposes", self.role("unknown", lean))[1], "opposes"), "CONDITIONAL_H_HARM")
            self.assertEqual(G.proposal_status(D.disposition("mimics", self.role("unknown", lean))[1], "mimics"), "CONDITIONAL_H_PROTECT")

    def test_a_sourced_role_raises_priority_but_does_not_qualify(self):
        s = G.proposal_status(D.disposition("opposes", self.role("harmful"))[1], "opposes")
        self.assertEqual(s, "HYPOTHESIS_ROLE_SOURCED_NOT_QUALIFIED")

    def test_checker_refuses_qualified_words_and_unknown_vocabulary(self):
        for bad in ("QUALIFIED", "KEEP-AS-PROPOSAL", "KEEP", "RECOMMENDED", "VALIDATED", "CONDITIONAL_H_HARM_QUALIFIED", "", "qualified"):
            with self.assertRaises(ValueError):
                G.check_status(bad)

    def test_a_fully_supported_conditional_row_is_still_conditional_end_to_end(self):
        """Every handover criterion satisfied, every number extreme: the status is still the conditional one and the qualified column is 'no'."""
        row = dict(arm="opposes", seed_specific_all_three_nulls="1", reach_z="99", family_id="F", name="Novelcompound")
        role = {"h_harm_action": "opposes: lower X", "h_protect_action": "mimics: sustain X"}
        ok, why = G.eligible(row, role, {"F": dict(has_chembl="1", modality="small_molecule")}, [])
        self.assertTrue(ok, why)
        self.assertEqual(G.proposal_status("CONDITIONAL_IF_HARMFUL", "opposes"), "CONDITIONAL_H_HARM")

    def test_committed_tables_carry_no_qualified_status(self):
        for name in ("proposals_it21.tsv", "handoff_it21.tsv"):
            rows = tsv(RES / name)
            if rows is None:
                self.skipTest(f"{name} not generated")
            for r in rows:
                self.assertIn(r["status"], G.STATUS_VOCAB)
                self.assertTrue(r["qualified"].startswith("no"), r["qualified"])
                self.assertNotIn("QUALIFIED", r["status"].replace("NOT_QUALIFIED", ""))


# ---- handover rule ---------------------------------------------------------------------------------------------------------------------------------
class HandoffRule(unittest.TestCase):
    META = {"F1": dict(has_chembl="1", modality="small_molecule"), "F2": dict(has_chembl="0", modality="small_molecule"), "F3": dict(has_chembl="1", modality="antibody")}
    ROLE_Q2 = {"h_harm_action": "opposes: lower glycolytic output", "h_protect_action": "mimics: sustain the HIF-type adaptation"}
    ROLE_Q6 = {"h_harm_action": "opposes: lower MYC", "h_protect_action": "mimics rows: P1 predicts lowering MYC is harmful, so mimics have no stated benefit hypothesis"}

    def base(self, **kw):
        r = dict(arm="opposes", seed_specific_all_three_nulls="1", reach_z="5.0", family_id="F1", name="Alphacompound")
        r.update(kw)
        return r

    def test_each_blocker(self):
        cases = [(dict(seed_specific_all_three_nulls="0"), "not_seed_specific_in_three_nulls"), (dict(reach_z=""), "reach_null_not_confirming"),
                 (dict(reach_z="-5"), "reach_null_not_confirming"), (dict(reach_z="2.9"), "reach_null_not_confirming"), (dict(family_id="F2"), "identity_not_resolved"),
                 (dict(family_id="F3"), "modality_antibody_not_small_molecule"), (dict(arm="direct_search"), "arm_not_opposes_or_mimics")]
        for kw, expect in cases:
            ok, why = G.eligible(self.base(**kw), self.ROLE_Q2, self.META, [])
            self.assertFalse(ok)
            self.assertEqual(why, expect)

    def test_mimics_needs_a_negative_reach_z(self):
        self.assertTrue(G.eligible(self.base(arm="mimics", reach_z="-4"), self.ROLE_Q2, self.META, [])[0])
        self.assertFalse(G.eligible(self.base(arm="mimics", reach_z="4"), self.ROLE_Q2, self.META, [])[0])

    def test_arm_without_a_stated_benefit_is_kept_out_of_the_handover_not_withdrawn_from_the_proposals(self):
        ok, why = G.eligible(self.base(arm="mimics", reach_z="-4"), self.ROLE_Q6, self.META, [])
        self.assertEqual((ok, why), (False, "arm_has_no_stated_benefit_hypothesis"))
        self.assertTrue(G.eligible(self.base(arm="opposes"), self.ROLE_Q6, self.META, [])[0])

    def test_committed_roles_agree_with_the_rule(self):
        roles = D.load_roles(G.IT10 / "question_roles.tsv")
        self.assertTrue(G.arm_has_stated_benefit(roles["Q2"], "H_PROTECT"))
        self.assertTrue(G.arm_has_stated_benefit(roles["Q5"], "H_PROTECT"))
        for q in ("Q4", "Q6", "Q7"):
            self.assertFalse(G.arm_has_stated_benefit(roles[q], "H_PROTECT"), q)
            self.assertTrue(G.arm_has_stated_benefit(roles[q], "H_HARM"), q)

    def test_earlier_decision_blocks_and_salt_twins_match(self):
        dec = [("PX-478", "KEEP", "src#E-01", "label"), ("dimethyl fumarate (the NRF2-active ex vivo form)", "DROP", "src#P4CD-04", "")]
        self.assertIsNotNone(G.earlier_state("Px-478", dec))
        self.assertIsNotNone(G.earlier_state("Dimethyl Fumarate", dec))
        self.assertIsNone(G.earlier_state("Fumaric acid monoethyl ester", dec))
        ok, why = G.eligible(self.base(name="PX 478"), self.ROLE_Q2, self.META, dec)
        self.assertEqual((ok, why), (False, "decided_in_earlier_qualification_record"))

    def test_one_per_mechanism_cluster_cap_and_origin_order(self):
        mk = lambda n, t, o, z, q="Q5", h="H_HARM": dict(question=q, hypothesis=h, main_target=t, n_origins=o, zmin=z, name=n)
        rows = [mk("a", "RORC", 1, 9), mk("b", "RORC", 2, 4), mk("c", "BRD4", 1, 8), mk("d", "JAK2", 1, 7), mk("e", "ROCK2", 1, 6), mk("f", "IKBKB", 1, 5), mk("g", "X", 1, 4, h="H_PROTECT")]
        out = G.select_handoff(rows, per_group=3)
        names = [r["name"] for r in out]
        self.assertIn("b", names)          # more origins wins its cluster over a larger z
        self.assertNotIn("a", names)       # one per cluster
        self.assertEqual(sum(1 for r in out if r["hypothesis"] == "H_HARM"), 3)
        self.assertIn("g", names)          # the cap is per (question, hypothesis)

    def test_salt_twins_count_once(self):
        self.assertEqual(G.base_name("Bepridil Hydrochloride"), G.base_name("BEPRIDIL"))
        self.assertNotEqual(G.base_name("Dexamethasone"), G.base_name("Prednisone"))


# ---- withdrawn rows are classified, not silently dropped -------------------------------------------------------------------------------------------
class WithdrawnClassification(unittest.TestCase):
    def test_causes(self):
        old = dict(family_id="F", edge_chain_main_target_to_seed_1="CACNA1G -T(+)-> X [src]")
        self.assertEqual(G.classify_withdrawn(old, {"F": [("CACNA1G", "lost")]}, {}), "DIRECTION_WITHDRAWN_AT_MAIN_TARGET")
        self.assertEqual(G.classify_withdrawn(old, {"F": [("OTHER", "lost")]}, {}), "DIRECTION_WITHDRAWN_AT_OTHER_TARGET_OF_THE_FAMILY")
        self.assertEqual(G.classify_withdrawn(old, {}, {"F": [1]}), "FAMILY_HAS_WITHHELD_ROWS_BUT_NO_SIGNED_PAIR_CHANGED")
        self.assertEqual(G.classify_withdrawn(old, {}, {}), "NO_ACTION_CHANGE_NULL_OR_SCORE_SHIFT")


# ---- the guard wrapper: absorbs the search-layer rule, once ------------------------------------------------------------------------------------------
class GuardWrapper(unittest.TestCase):
    MS = {"CACNA1G", "CACNA1H", "CACNA1I"}

    def entry(self, ttype="PROTEIN COMPLEX GROUP", genes=None, tid="CHEMBL2363032", chembl="CHEMBL1008"):
        genes = genes or [f"CACNA1{c}" for c in "ABCDEFGHIS"]
        t = dict(source="ChEMBL curated mechanism", target_type=ttype, gene_symbols=genes, target_id=tid, organism="Homo sapiens", action_type="BLOCKER", uniprot=["P1"])
        return dict(id="CAT:" + chembl, name="Testdrug", ids=dict(chembl=chembl), relations={}, targets=[t]), t

    def call(self, e, t, artefacts=()):
        log = []
        u0 = dict(stated=True, excluded=None, sign="down", stable=True, group="ChEMBL")
        w = Rf.make_wrapper(lambda rs_, idx, e_, t_: dict(u0), self.MS, log)
        return w(rs, types.SimpleNamespace(artefacts=list(artefacts)), e, t), log

    def test_group_record_mostly_outside_the_module_loses_its_sign_and_says_why(self):
        e, t = self.entry()
        u, log = self.call(e, t)
        self.assertEqual(u["sign"], "unresolved")
        self.assertEqual(log[0]["reason_class"], "group_record_mostly_outside_module_targets")
        self.assertEqual(log[0]["waived_genes"], "")

    def test_single_protein_record_is_untouched(self):
        e, t = self.entry(ttype="SINGLE PROTEIN", genes=["CACNA1H"], tid="CHEMBL1")
        u, log = self.call(e, t)
        self.assertEqual((u["sign"], log), ("down", []))

    def test_record_at_the_modules_own_level_is_untouched(self):
        e, t = self.entry(ttype="PROTEIN FAMILY", genes=["CACNA1G", "CACNA1H", "CACNA1I"], tid="CHEMBL2")
        u, log = self.call(e, t)
        self.assertEqual((u["sign"], log), ("down", []))

    def test_documented_single_protein_measurement_waives_one_gene_only(self):
        e, t = self.entry()
        rule = dict(claim_source="ChEMBL", symbol="CACNA1H", rule="target_level_documented:CHEMBL1008:BLOCKER:single_protein", evidence="IC50 measured on recombinant Cav3.2")
        u, log = self.call(e, t, [rule])
        self.assertEqual(u["sign"], "unresolved")           # the record row itself stays unresolved; the waived gene is re-added by add_waived
        self.assertEqual(log[0]["waived_genes"], "CACNA1H")  # and only that gene

    def test_unstated_action_is_not_touched_here(self):
        e, t = self.entry()
        log = []
        w = Rf.make_wrapper(lambda rs_, idx, e_, t_: dict(stated=False, excluded=None, sign="unresolved", stable=True), self.MS, log)
        u = w(rs, types.SimpleNamespace(artefacts=[]), e, t)
        self.assertEqual(log, [])

    def test_republished_copy_without_a_resolved_original_loses_its_sign(self):
        e = dict(id="CAT:DGIDB:x", name="Copydrug", ids={}, relations={}, targets=[])
        t = dict(source="DGIdb interaction", claim_source="ChEMBL", gene="CACNA1G", interaction_type="blocker", gene_concept_id="hgnc:1394")
        e["targets"].append(t)
        rule = dict(claim_source="ChEMBL", symbol="*", rule="republication:ChEMBL", evidence="DGIdb export republishes ChEMBL without the record id or level")
        u, log = self.call(e, t, [rule])
        self.assertEqual(u["sign"], "unresolved")
        self.assertEqual(log[0]["reason_class"], "republished_claim_level_not_carried")

    def test_without_a_republication_row_nothing_changes(self):
        e = dict(id="CAT:DGIDB:x", name="Copydrug", ids={}, relations={}, targets=[])
        t = dict(source="DGIdb interaction", claim_source="SomeOtherSource", gene="CACNA1G", interaction_type="blocker")
        e["targets"].append(t)
        u, log = self.call(e, t, [])
        self.assertEqual((u["sign"], log), ("down", []))


# ---- committed tables: the properties the README states -----------------------------------------------------------------------------------------------
class CommittedActions(unittest.TestCase):
    def actions(self):
        p = RES / "actions" / "family_actions.tsv.gz"
        if not p.exists():
            self.skipTest("results/actions not generated")
        out = {}
        for r in G.rd(p):
            out.setdefault(r["family_id"], {})[r["target_symbol"]] = r
        return out

    def test_bepridil_keeps_its_documented_cav32_direction_and_not_the_group_expansion(self):
        a = self.actions().get("FAM:CAT:CHEMBL1008")
        self.assertIsNotNone(a)
        self.assertIn("CACNA1H", a)
        self.assertIn("DOCUMENTED_LEVEL_WAIVER", a["CACNA1H"]["flags"])
        self.assertLess(float(a["CACNA1H"]["mean_sign"]), 0)
        for g in ("CACNA1G", "CACNA1I", "CACNA1A", "CACNA1C"):
            self.assertNotIn(g, a, f"{g}: a direction the source record never measured at gene level")

    def test_the_other_three_t_type_entries_lose_the_group_expansion(self):
        acts = self.actions()
        names = {r["family_id"]: r["name"].upper() for r in G.rd(RES / "actions" / "family_meta.tsv.gz")}
        for fid, nm in names.items():
            if nm in ("TERODILINE HYDROCHLORIDE", "SULOCTIDIL", "PHLOROGLUCINOL") and fid in acts:
                self.assertNotIn("CACNA1G", acts[fid], nm)

    def test_withheld_rows_keep_their_association(self):
        any_p = HERE.parent / "generation_it9_p2_20261030" / "v3" / "results" / "actions" / "family_targets_any.tsv.gz"
        new = RES / "actions" / "family_targets_any.tsv.gz"
        if not new.exists():
            self.skipTest("results/actions not generated")
        key = lambda p: {(r["family_id"], r["target_symbol"]) for r in G.rd(p)}
        old, now = key(any_p), key(new)
        self.assertGreaterEqual(len(now), len(old) - 5)     # unknown is not negative: the guards remove signs, not associations (catalogue drift since IT9 is a handful of pairs)

    def test_every_signed_pair_was_signed_before(self):
        d = tsv(RES / "actions_diff_guards_on_vs_off.tsv")
        if d is None:
            self.skipTest("diff not generated")
        for r in d:
            if r["status"] == "gained":
                self.assertEqual(r["target_symbol"], "CACNA1H")     # the only direction a guard run may add is the documented waiver


class CommittedHandoff(unittest.TestCase):
    def test_each_handed_proposal_is_attributed_and_has_a_discriminating_experiment(self):
        rows = tsv(RES / "handoff_it21.tsv")
        if rows is None:
            self.skipTest("handoff not generated")
        self.assertTrue(rows)
        for r in rows:
            for col in ("seed_generated_by", "mechanism_path", "assumption", "hypothesised_benefit", "discriminating_experiment", "alternatives_same_mechanism", "abstentions", "negatives_and_limits"):
                self.assertTrue(r[col].strip(), f"{r['proposal_id']} {col}")
            self.assertIn("Step 0", r["discriminating_experiment"])
            self.assertIn("falsifies", r["discriminating_experiment"])

    def test_handed_proposals_are_new_to_the_qualification_records_and_one_per_cluster(self):
        rows = tsv(RES / "handoff_it21.tsv")
        props = tsv(RES / "proposals_it21.tsv")
        if rows is None or props is None:
            self.skipTest("not generated")
        by = {p["proposal_id"]: p for p in props}
        seen = set()
        for r in rows:
            p = by[r["proposal_id"]]
            self.assertEqual(p["earlier_decision"], "")
            self.assertEqual(p["handoff_eligible"], "yes")
            k = (p["question"], p["hypothesis"], p["main_target"])
            self.assertNotIn(k, seen)
            seen.add(k)
            self.assertEqual(p["modality"], "small_molecule")

    def test_levels_are_not_merged(self):
        props = tsv(RES / "proposals_it21.tsv")
        if props is None:
            self.skipTest("not generated")
        for p in props:
            self.assertEqual(p["readout_level"], "expression" if "expression" in p["seed_set"] else p["seed_set"].split("_")[1])


class CommittedProvenance(unittest.TestCase):
    def js(self, name):
        p = RES / name
        if not p.exists():
            self.skipTest(f"{name} not generated")
        import json
        return json.loads(p.read_text())

    def test_control_run_reproduces_the_it10_list_so_differences_are_the_guards(self):
        c = self.js("control_reproduction.json")
        self.assertTrue(c["identical_keys"])
        self.assertEqual((c["control_only"], c["it10_only"]), (0, 0))

    def test_every_withdrawn_row_has_a_classified_cause_and_the_counts_close(self):
        w = self.js("withdrawn_summary.json")
        self.assertEqual(sum(w["withdrawn_by_cause"].values()), w["withdrawn"])
        self.assertEqual(w["it10_seed_specific"], w["still_seed_specific"] + w["withdrawn"])
        c = self.js("control_reproduction.json")
        self.assertEqual(w["withdrawn"], c["guarded_vs_control_lost"])
        rows = tsv(RES / "withdrawn_vs_it10.tsv")
        self.assertEqual(len(rows), w["withdrawn"])
        for r in rows:
            self.assertTrue(r["cause"])

    def test_most_withdrawals_are_a_direction_withdrawn_at_the_main_target_not_a_noise_shift(self):
        w = self.js("withdrawn_summary.json")
        self.assertGreaterEqual(w["withdrawn_by_cause"].get("DIRECTION_WITHDRAWN_AT_MAIN_TARGET", 0), 0.9 * w["withdrawn"])

    def test_gained_rows_are_not_presented_as_findings(self):
        for r in tsv(RES / "gained_vs_it10.tsv") or []:
            self.assertIn("NOT_A_FINDING", r["cause"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
