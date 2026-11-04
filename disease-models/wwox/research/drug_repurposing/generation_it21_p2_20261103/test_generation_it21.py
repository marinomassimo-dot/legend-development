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

    def test_tie_size_counts_exact_ties_and_h5_text_names_the_real_key(self):     # IT27 P5: the H5 text listed three of the six order terms and said smallest |z|
        mk = lambda n, o, z, el="yes": dict(question="Q8", hypothesis="H_HARM", main_target="EZH2", n_origins=o, zmin=z, name=n, handoff_eligible=el, chain_edges=2)
        self.assertEqual(G.tie_size([mk("a", 2, 5), mk("b", 2, 5), mk("c", 1, 9), mk("d", 2, 5, el="no")]), 2)
        self.assertEqual(G.tie_size([mk("a", 2, 5), mk("c", 1, 9)]), 1)
        self.assertEqual(G.tie_size([mk("a", 2, 5, el="no")]), 0)
        for term in ("cluster work already done", "UNMEASURED", "LARGER smallest-|z|", "tie_size"):
            self.assertIn(term, G.HANDOFF_RULE.replace("no cluster work already done", "cluster work already done"))

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

    # ---- P8-fix finding 1: conflict on action and glue/neosubstrate receptors lose the sign, keep the association ---------------------------------------
    def fam_entry(self, name, chembl, action, genes, ttype="SINGLE PROTEIN"):
        t = dict(source="ChEMBL curated mechanism", target_type=ttype, gene_symbols=genes, target_id="CHEMBL9", organism="Homo sapiens", action_type=action, uniprot=["P1"])
        return dict(id="CAT:" + chembl, name=name, ids=dict(chembl=chembl), relations={}, targets=[t])

    def call_family(self, members, e, t, sign="down"):
        log = []
        idx = types.SimpleNamespace(artefacts=[], family={m["id"]: "F1" for m in members}, members={"F1": members})
        w = Rf.make_wrapper(lambda rs_, i, e_, t_: dict(stated=True, excluded=None, sign=sign, stable=True, group="ChEMBL"), set(), log)
        return w(rs, idx, e, t), log

    def test_family_whose_records_conflict_inhibitor_vs_modulator_gets_no_sign(self):
        a, b = self.fam_entry("Drug", "CHEMBL1", "INHIBITOR", ["XYZ1"]), self.fam_entry("Drug salt", "CHEMBL2", "MODULATOR", ["XYZ1"])
        u, log = self.call_family([a, b], a, a["targets"][0])
        self.assertEqual(u["sign"], "unresolved")
        self.assertEqual(log[0]["reason_class"], "action_conflict_or_glue_modulator")
        self.assertEqual(log[0]["waived_genes"], "")

    def test_family_whose_records_conflict_up_vs_down_gets_no_sign(self):
        a, b = self.fam_entry("Drug", "CHEMBL1", "INHIBITOR", ["XYZ1"]), self.fam_entry("Drug salt", "CHEMBL2", "AGONIST", ["XYZ1"])
        self.assertEqual(self.call_family([a, b], a, a["targets"][0])[0]["sign"], "unresolved")

    def test_agreeing_records_and_a_conflict_at_another_gene_keep_the_sign(self):
        a, b = self.fam_entry("Drug", "CHEMBL1", "INHIBITOR", ["XYZ1"]), self.fam_entry("Drug salt", "CHEMBL2", "INHIBITOR", ["XYZ1"])
        self.assertEqual(self.call_family([a, b], a, a["targets"][0]), (dict(stated=True, excluded=None, sign="down", stable=True, group="ChEMBL"), []))
        c = self.fam_entry("Drug other", "CHEMBL3", "MODULATOR", ["OTHER2"])
        self.assertEqual(self.call_family([a, c], a, a["targets"][0])[0]["sign"], "down")

    def test_a_dgidb_modulator_beside_a_chembl_inhibitor_is_not_a_conflict(self):
        a = self.fam_entry("Drug", "CHEMBL1", "INHIBITOR", ["XYZ1"])
        d = dict(id="CAT:DGIDB:x", name="Drug", ids={}, targets=[dict(source="DGIdb interaction", gene="XYZ1", interaction_type="modulator")])
        self.assertEqual(self.call_family([a, d], a, a["targets"][0])[0]["sign"], "down")

    # ---- IT24 P1: a direction asserted only by a listing-tier claim source (TALC, trial listings) is withheld for the pairs a source check named ----------------------
    def dg_entry(self, claim_source, gene, itype="inhibitor", eid="CAT:DGIDB:x"):
        return dict(id=eid, name="Drug", ids={}, targets=[dict(source="DGIdb interaction", gene=gene, claim_source=claim_source, interaction_type=itype)])

    def call_listing(self, members, e, t, family, mode="pairs", sign="down"):
        log = []
        idx = types.SimpleNamespace(artefacts=[], family={m["id"]: family for m in members}, members={family: members})
        orig = lambda rs_, i, e_, t_: dict(stated=True, excluded=None, sign=sign, stable=True, group="DGIdb_other")
        return Rf.make_wrapper(orig, set(), log, mode)(rs, idx, e, t), log

    def test_a_named_listing_pair_loses_its_sign_and_keeps_its_association(self):
        e = self.dg_entry("TALC", "SIRT1")
        u, log = self.call_listing([e], e, e["targets"][0], "FAM:CAT:DGIDB:be0d8ea27925")
        self.assertEqual(u["sign"], "unresolved")
        self.assertEqual(log[0]["reason_class"], "listing_tier_claim_not_carried")
        self.assertEqual(log[0]["waived_genes"], "")

    def test_an_unnamed_listing_pair_the_same_gene_from_a_measured_source_and_mode_off_keep_the_sign(self):
        e = self.dg_entry("TALC", "HDAC6")                           # the same family, a gene the source check did not name
        self.assertEqual(self.call_listing([e], e, e["targets"][0], "FAM:CAT:DGIDB:be0d8ea27925")[0]["sign"], "down")
        m = self.dg_entry("GuideToPharmacology", "SIRT1")           # a measured-pharmacology claim is not a listing
        self.assertEqual(self.call_listing([m], m, m["targets"][0], "FAM:CAT:DGIDB:be0d8ea27925")[0]["sign"], "down")
        e = self.dg_entry("TALC", "SIRT1")
        self.assertEqual(self.call_listing([e], e, e["targets"][0], "FAM:CAT:DGIDB:be0d8ea27925", mode="off")[0]["sign"], "down")

    def test_the_named_exclusions_still_match_the_committed_tables(self):
        """The exclusion key is (family id, gene, claim source) and a family id is the smallest member id: if a catalogue build joins the record to another family the key stops
        matching and the sign would re-enter silently. Every named family must exist in the committed tables and none of its named pairs may carry a sign."""
        import gzip
        pairs = Rf.load_pair_exclusions()
        self.assertTrue(pairs)
        meta = {r["family_id"] for r in csv.DictReader(gzip.open(HERE / "results/actions/family_meta.tsv.gz", "rt", encoding="utf-8"), delimiter="\t")}
        acts = {(r["family_id"], r["target_symbol"].upper()) for r in csv.DictReader(gzip.open(HERE / "results/actions/family_actions.tsv.gz", "rt", encoding="utf-8"), delimiter="\t")}
        for (fam, gene, _src) in pairs:
            self.assertIn(fam, meta, fam)
            self.assertNotIn((fam, gene), acts, (fam, gene))

    def test_the_wide_listing_sensitivity_needs_a_second_independent_source_with_the_same_direction(self):
        e, m = self.dg_entry("TALC", "ABC1"), self.dg_entry("GuideToPharmacology", "ABC1", eid="CAT:DGIDB:y")
        self.assertEqual(self.call_listing([e], e, e["targets"][0], "F9", mode="tier")[0]["sign"], "unresolved")
        self.assertEqual(self.call_listing([e, m], e, e["targets"][0], "F9", mode="tier")[0]["sign"], "down")

    def test_glue_substrate_receptor_gets_no_sign_whatever_the_records_say(self):
        a = self.fam_entry("Lenalidomide-like", "CHEMBL848", "INHIBITOR", ["CRBN", "CUL4A", "DDB1", "RBX1"], ttype="PROTEIN COMPLEX")
        u, log = self.call_family([a], a, a["targets"][0])
        self.assertEqual(u["sign"], "unresolved")
        self.assertIn("glue substrate receptor", log[0]["reason_class"] + " " + str(log[0]) + " " + Rf.conflict_or_glue(rs, [a], a["targets"][0]))

    def test_committed_crbn_pairs_carry_no_sign_but_keep_the_association(self):
        rows = tsv(RES / "actions" / "family_actions.tsv.gz")
        if rows is None:
            self.skipTest("actions not generated")
        self.assertEqual([r for r in rows if r["target_symbol"] == "CRBN"], [])
        anyt = tsv(RES / "actions" / "family_targets_any.tsv.gz")
        self.assertTrue([r for r in anyt if r["target_symbol"] == "CRBN"])

    # ---- P8-fix findings 2 and 3 --------------------------------------------------------------------------------------------------------------------
    def test_intended_effect_follows_the_seed_direction(self):
        self.assertTrue(G.intended_effect("H_HARM", "up").startswith("lowers"))
        self.assertTrue(G.intended_effect("H_HARM", "down").startswith("raises"))
        self.assertTrue(G.intended_effect("H_PROTECT", "up").startswith("raises or sustains"))
        self.assertTrue(G.intended_effect("H_PROTECT", "down").startswith("lowers"))
        self.assertIn("cannot be written", G.intended_effect("H_HARM", ""))

    def test_earlier_exclusion_lists_are_in_the_perimeter_with_their_reason(self):
        th = G.load_earlier_threads()
        for name, fam in (("Az960", "FAM:CAT:CHEMBL1774055"), ("AZ-960", ""), ("CUDC101", "FAM:CAT:CHEMBL598797"), ("Nanatinostat", "FAM:CAT:CHEMBL1801250"),
                          ("GSK-343", ""), ("Cgi1746", "FAM:CAT:CHEMBL1230541")):
            self.assertTrue(G.earlier_thread(name, fam, th), name)
        self.assertIn("F5_no_human_exposure_statement", G.earlier_thread("Az960", "", th))
        self.assertEqual(G.earlier_thread("Entirely Madeup", "FAM:CAT:CHEMBL0000001", th), "")

    def test_closed_as_written_is_a_closed_status_not_a_promotion(self):
        self.assertIn("CLOSED_AS_WRITTEN", G.STATUS_VOCAB)
        self.assertEqual(G.check_status("CLOSED_AS_WRITTEN"), "CLOSED_AS_WRITTEN")
        for disp in ("CONDITIONAL_IF_HARMFUL", "CONDITIONAL_IF_PROTECTIVE", "PRIMARY_RELIEVE", "NOT_APPLICABLE", "X"):
            for arm in ("opposes", "mimics"):
                self.assertNotEqual(G.proposal_status(disp, arm), "CLOSED_AS_WRITTEN")   # this module never produces it; only a qualification record does

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


class IdentityRouteR4(unittest.TestCase):
    """IT26: R4 (G-SRS name -> UNII -> structure) gives an identity, only for rows a second actor confirmed, and never a name-only row."""

    def test_missing_file_means_no_route(self):
        self.assertEqual(G.load_identity_r4(HERE / "no_such_r4.tsv"), {})

    def test_committed_rows_are_confirmed_ones(self):
        r4 = G.load_identity_r4()
        self.assertEqual(len(r4), 19)
        self.assertTrue(all(v.startswith("CHEMBL") for v in r4.values()))
        self.assertIn("FAM:CAT:DGIDB:b34c953dc1fa", r4)                      # idronoxil
        self.assertNotIn("FAM:CAT:DGIDB:ec1f021cf6ea", r4)                   # martinostat: no catalogue key, not carried
        self.assertNotIn("FAM:CAT:DGIDB:b459313a7710", r4)                   # EZN-2968: no hit


class ModalityDeclarations(unittest.TestCase):
    """IT27: a declared modality correction (PX-478) is structure-level, second-actor evidence, never a loosened filter."""

    def test_missing_file_means_no_declaration(self):
        self.assertEqual(G.load_modality_declarations(HERE / "no_such_decl.tsv"), {})

    def test_px478_is_declared_and_a_real_peptide_is_not(self):
        d = G.load_modality_declarations()
        self.assertEqual(d["FAM:CAT:DGIDB:b884da5f3057"], ("protein_or_peptide", "small_molecule"))
        self.assertEqual(len(d), 1)                       # romidepsin, voclosporin, GDC-0152 stay protein_or_peptide (peptide bonds, ring or mimetic)


if __name__ == "__main__":
    unittest.main(verbosity=1)
