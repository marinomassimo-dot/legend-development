#!/usr/bin/env python3
"""Tests for IT21 V1: the claim-name identity bridge, the attribution screen and their use in the hand-over. Production code under test; synthetic caches for the
rules, the committed v1 tables (diagnosis_it21_v1_20261103/results_v1) for the properties the diagnosis rests on (skipped when absent).

  python3 test_attribution_it21.py          (unittest; offline; seconds)
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, importlib.util, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))
sys.path.insert(0, str(HERE))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


A = load("attribution_screen_it21", HERE / "attribution_screen_it21.py")
G = load("run_generation_it21", HERE / "run_generation_it21.py")
V1 = DR / "diagnosis_it21_v1_20261103" / "results_v1"


def tsv(p):
    p = Path(p)
    return G.rd(p) if p.exists() else None


def write_csv(path, header, rows, comment=True):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        if comment:
            w.writerow(["# GtoPdb Version: test"])
        w.writerow(header)
        w.writerows(rows)


def entry(cid, name, origin, chembl=None, inchikey=None, dg_name=None, drugbank=(), iuphar=()):
    return {"id": cid, "name": name, "origin": origin, "ids": {"chembl": chembl, "inchikey": inchikey, "dgidb_drug_name": dg_name, "drugbank": list(drugbank),
                                                                  "iuphar_ligand": list(iuphar), "chembl_from_dgidb_concept_not_enumerated": []}}


KEY_A = "AAAAAAAAAAAAAA-BBBBBBBBBB-N"
KEY_A_STEREO = "AAAAAAAAAAAAAA-CCCCCCCCCC-N"
KEY_OTHER = "ZZZZZZZZZZZZZZ-BBBBBBBBBB-N"


class SyntheticCache(unittest.TestCase):
    LIG = ["Ligand ID", "Name", "ChEMBL ID", "InChIKey", "Labelled", "Radioactive", "Type"]
    INT = ["Target Species", "Ligand ID", "Target Gene Symbol", "Affinity Units", "Affinity Median", "Original Affinity Median nm"]
    DG = ["interaction_source_db_name", "drug_claim_name", "drug_name"]

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        c = Path(self.tmp.name)
        write_csv(c / "gtopdb/ligands.csv", self.LIG, [
            ["1", "drugone", "CHEMBL1", KEY_A, "", "", "Synthetic organic"],
            ["2", "drugtwo", "CHEMBL2", KEY_A, "", "", "Synthetic organic"],
            ["3", "drugthree", "CHEMBL3", KEY_OTHER, "", "", "Synthetic organic"],
            ["4", "drugfour", "CHEMBL4", KEY_A, "yes", "", "Synthetic organic"],
            ["5", "drugfive", "CHEMBL5", KEY_A_STEREO, "", "", "Synthetic organic"],
            ["6", "noref", "", KEY_A, "", "", "Synthetic organic"],
            ["7", "estradiol", "CHEMBL7", KEY_A, "", "", "Synthetic organic"]])
        write_csv(c / "gtopdb/interactions.csv", self.INT, [
            ["Human", "1", "TGT1", "pKi", "8.9", "1.3"], ["Human", "1", "TGT5", "pKi", "5.44", "3600"], ["Mouse", "1", "TGT9", "pKi", "9", "1"],
            ["Human", "9", "TGT2", "pIC50", "7", ""]])
        (c / "dgidb").mkdir()
        with open(c / "dgidb/interactions.tsv", "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(self.DG)
            for src, claim, name in [("GuideToPharmacology", "IUPHAR.LIGAND:1", "DRUGONE"), ("GuideToPharmacology", "IUPHAR.LIGAND:3", "DRUGTHREE"),
                                     ("GuideToPharmacology", "IUPHAR.LIGAND:4", "DRUGFOUR"), ("GuideToPharmacology", "IUPHAR.LIGAND:5", "DRUGFIVE"),
                                     ("GuideToPharmacology", "IUPHAR.LIGAND:1", "SHAREDNAME"), ("GuideToPharmacology", "IUPHAR.LIGAND:2", "SHAREDNAME"),
                                     ("OtherDb", "IUPHAR.LIGAND:1", "NOTGTOPDB"), ("GuideToPharmacology", "drugone", "NAMEONLY"),
                                     ("GuideToPharmacology", "IUPHAR.LIGAND:7", "ESTRADIOL VALERATE"), ("GuideToPharmacology", "IUPHAR.LIGAND:2", "DRUGTWO HYDROCHLORIDE"),
                                     ("GuideToPharmacology", "IUPHAR.LIGAND:2", "SOMETHINGELSE")]:
                w.writerow([src, claim, name])
        self.cache = c
        self.entries = [entry("CAT:CHEMBL1", "DRUGONE", "chembl_selected", "CHEMBL1", KEY_A), entry("CAT:CHEMBL2", "DRUGTWO", "chembl_selected", "CHEMBL2", KEY_A),
                        entry("CAT:CHEMBL3", "DRUGTHREE", "chembl_selected", "CHEMBL3", KEY_A), entry("CAT:CHEMBL4", "DRUGFOUR", "chembl_selected", "CHEMBL4", KEY_A),
                        entry("CAT:CHEMBL5", "DRUGFIVE", "chembl_selected", "CHEMBL5", KEY_A),
                        entry("CAT:DGIDB:a", "Drugone", "dgidb_only", dg_name="DRUGONE"), entry("CAT:DGIDB:b", "Drugthree", "dgidb_only", dg_name="DRUGTHREE"),
                        entry("CAT:DGIDB:c", "Drugfour", "dgidb_only", dg_name="DRUGFOUR"), entry("CAT:DGIDB:d", "Drugfive", "dgidb_only", dg_name="DRUGFIVE"),
                        entry("CAT:DGIDB:e", "Sharedname", "dgidb_only", dg_name="SHAREDNAME"), entry("CAT:DGIDB:f", "Notgtopdb", "dgidb_only", dg_name="NOTGTOPDB"),
                        entry("CAT:DGIDB:g", "Nameonly", "dgidb_only", dg_name="NAMEONLY"),
                        entry("CAT:DGIDB:h", "Drugone", "dgidb_only", dg_name="ALREADY", iuphar=["1"]),
                        entry("CAT:CHEMBL7", "ESTRADIOL", "chembl_selected", "CHEMBL7", KEY_A),
                        entry("CAT:DGIDB:i", "Estradiol Valerate", "dgidb_only", dg_name="ESTRADIOL VALERATE"),
                        entry("CAT:DGIDB:j", "Drugtwo Hydrochloride", "dgidb_only", dg_name="DRUGTWO HYDROCHLORIDE"),
                        entry("CAT:DGIDB:k", "Somethingelse", "dgidb_only", dg_name="SOMETHINGELSE")]

    def tearDown(self):
        self.tmp.cleanup()


class IdentityBridge(SyntheticCache):
    def decisions(self):
        br = A.bridge_claim_name_ligands(self.entries, self.cache)
        return {k: [(r["decision"], r["reason"]) for r in v] for k, v in br.items()}

    def test_equal_structure_through_the_claim_name_ligand_id_is_merged(self):
        self.assertEqual(self.decisions()["CAT:DGIDB:a"][0][0], "merged")

    def test_a_connectivity_conflict_is_rejected_not_merged(self):
        self.assertEqual(self.decisions()["CAT:DGIDB:b"][0][0], "rejected_conflict")

    def test_labelled_form_is_related_not_merged(self):
        self.assertEqual(self.decisions()["CAT:DGIDB:c"][0][0], "related_not_merged")

    def test_different_stereo_layer_is_related_not_merged(self):
        self.assertEqual(self.decisions()["CAT:DGIDB:d"][0][0], "related_not_merged")

    def test_one_record_naming_two_chembl_ids_is_not_joined(self):
        d = self.decisions()["CAT:DGIDB:e"]
        self.assertTrue(all(x[0] == "unresolved" for x in d), d)

    def test_a_claim_from_another_source_a_name_alone_and_an_already_reconciled_record_make_no_bridge(self):
        d = self.decisions()
        for k in ("CAT:DGIDB:f", "CAT:DGIDB:g", "CAT:DGIDB:h"):
            self.assertNotIn(k, d)

    def test_family_bridge_joins_only_merged_and_never_by_name(self):
        fam = {e["id"]: e["id"] for e in self.entries}
        br = A.bridge_claim_name_ligands(self.entries, self.cache)
        fb = A.family_bridge(br, fam)
        self.assertEqual(fb, {"CAT:DGIDB:a": "CAT:CHEMBL1", "CAT:DGIDB:j": "CAT:CHEMBL2"})

    def test_an_ester_twin_is_related_not_merged_even_with_equal_structure(self):        # V1-fix finding 2: estradiol valerate was joined to estradiol
        d = self.decisions()["CAT:DGIDB:i"]
        self.assertEqual(d[0][0], "related_not_merged")
        self.assertIn("derivative", d[0][1])
        fam = {e["id"]: e["id"] for e in self.entries}
        self.assertNotIn("CAT:DGIDB:i", A.family_bridge(A.bridge_claim_name_ligands(self.entries, self.cache), fam))

    def test_a_salt_form_of_the_same_name_still_merges_and_a_twin_with_no_name_match_is_unresolved(self):
        d = self.decisions()
        self.assertEqual(d["CAT:DGIDB:j"][0][0], "merged")
        self.assertEqual(d["CAT:DGIDB:k"][0][0], "unresolved")

    def test_name_relation_is_symmetric_in_the_extra_word_and_ignores_markup(self):
        self.assertEqual(A.name_relation(["Abc Sulfate"], "abc"), "match")
        self.assertEqual(A.name_relation(["abc"], "abc decanoate"), "derivative")
        self.assertEqual(A.name_relation(["abc cilexetil"], "<i>abc</i>"), "derivative")
        self.assertEqual(A.name_relation(["xyz"], "abc", "def"), "none")
        self.assertEqual(A.name_relation(["abc", "xyz"], "xyz"), "match")


class AttributionScreen(SyntheticCache):
    def aff(self):
        return A.load_gtopdb_affinities(self.cache)

    def test_human_only_and_nm_from_the_original_column_or_the_log_value(self):
        _, aff, _ = self.aff()
        # IT22 P2: the loader keeps measures per type (a type-less release row is "?"); the number is the median within the type
        # IT22 P8-fix: a row without an original type takes the type from the release's own affinity column (pKi -> Ki ...), so the key is that type, not "?"
        first = lambda k: next(iter(aff[k].values()))["nm"]
        self.assertEqual(first(("1", "TGT1")), 1.3)
        self.assertNotIn(("1", "TGT9"), aff)
        self.assertAlmostEqual(first(("9", "TGT2")), 100.0, places=3)

    def test_weak_when_the_main_target_is_at_least_ten_fold_weaker_than_the_best(self):
        _, aff, _ = self.aff()
        a = A.attribution({"1"}, "TGT5", aff)
        self.assertEqual(a["state"], "WEAK_ATTRIBUTION")
        self.assertGreater(a["fold"], 2000)
        self.assertEqual(a["best_target"], "TGT1")

    def test_attributable_at_the_best_target_and_threshold_boundary(self):
        _, aff, _ = self.aff()
        self.assertEqual(A.attribution({"1"}, "TGT1", aff)["state"], "ATTRIBUTABLE")
        aff2 = {("x", "A"): 1000.0, ("x", "B"): 9990.0, ("x", "C"): 10000.0}        # nM scale above the potent floor, so the 10-fold boundary is what decides
        self.assertEqual(A.attribution({"x"}, "B", aff2)["state"], "ATTRIBUTABLE")
        self.assertEqual(A.attribution({"x"}, "C", aff2)["state"], "WEAK_ATTRIBUTION")

    def test_a_large_fold_with_a_potent_main_target_is_borderline_not_weak(self):        # V1-fix finding 1
        aff = {("x", "A"): 0.1, ("x", "B"): 100.0, ("x", "C"): 100.5}
        self.assertEqual(A.attribution({"x"}, "B", aff)["state"], "BORDERLINE_POTENT_MAIN_TARGET")      # 1000-fold, but the main target is at the 100 nM floor
        # IT22 P2 (superseded assumption): a main target just above 100 nM is a measured SECONDARY activity, no longer WEAK; WEAK starts above SECONDARY_MAIN_NM (1000 nM)
        self.assertEqual(A.attribution({"x"}, "C", aff)["state"], "SECONDARY_ACTIVITY_MEASURED")
        self.assertEqual(A.attribution({"x"}, "D", {**aff, ("x", "D"): 1500.0})["state"], "WEAK_ATTRIBUTION")
        self.assertEqual(A.attribution({"x"}, "B", aff)["fold"], 1000.0)
        self.assertEqual(A.POTENT_MAIN_NM, G.AS_POTENT_NM)

    def test_a_single_measured_target_has_no_comparison(self):        # V1-fix finding 4
        aff = {("x", "A"): 5.0}
        self.assertEqual(A.attribution({"x"}, "A", aff)["state"], "SINGLE_MEASURED_TARGET")
        self.assertEqual(A.attribution({"x"}, "A", aff)["fold"], 1.0)

    # ---- IT22 P2 fixtures: measures of different types are never compared as if they were one scale --------------------------------------------------
    @staticmethod
    def E(nm, rel="=", assay="unknown"):
        return dict(nm=nm, rel=rel, assay=assay, n=1)

    def test_different_measure_types_are_not_declared_comparable(self):          # the reported synthetic case: EC50 at the proposed target, Ki at the other
        aff = {("x", "A"): {"Ki": self.E(1.0)}, ("x", "B"): {"EC50": self.E(5000.0)}}
        a = A.attribution({"x"}, "B", aff)
        self.assertEqual(a["state"], "NOT_COMPARABLE_MEASURES")
        self.assertEqual(a["fold"], "")                                   # no ratio is formed, so none can become an exclusion
        self.assertIn("EC50", a["values_kept"])
        self.assertIn("Ki 1 nM", a["values_kept"])
        self.assertIn("same type", a["comparison_basis"])

    def test_mixed_measures_are_kept_separate_and_compared_type_by_type(self):
        aff = {("x", "A"): {"IC50": self.E(2.0), "Kd": self.E(400.0)}, ("x", "B"): {"IC50": self.E(10.0), "Kd": self.E(3000.0)}}
        a = A.attribution({"x"}, "B", aff)
        self.assertEqual(a["state"], "ATTRIBUTABLE")                       # both same-type deficits (IC50 5x, Kd 7.5x) are below 10x; neither is pooled
        self.assertIn("IC50", a["context_note"]); self.assertIn("Kd", a["context_note"])
        self.assertEqual(a["best_measure"], "Kd")                          # IT22 P8-fix: the verdict follows the type with the LARGEST deficit
        hide = {("x", "A"): {"IC50": self.E(1.0), "Kd": self.E(5.0)}, ("x", "B"): {"IC50": self.E(5000.0), "Kd": self.E(6.0)}}      # a favourable Kd must not hide a 5000-fold IC50 deficit
        self.assertEqual(A.attribution({"x"}, "B", hide)["state"], "WEAK_ATTRIBUTION")

    def test_a_comparable_pair_keeps_a_real_weak_attribution_signal(self):
        aff = {("x", "A"): {"IC50": self.E(1.3)}, ("x", "B"): {"IC50": self.E(3600.0)}}      # the vorinostat shape: same type, 2769-fold, main target above 1 uM
        a = A.attribution({"x"}, "B", aff)
        self.assertEqual(a["state"], "WEAK_ATTRIBUTION")
        self.assertEqual(a["comparison_basis"], "IC50 at B vs IC50 at A")
        self.assertEqual(a["occupancy"], "")                                  # a ratio is not converted into occupancy

    def test_a_secondary_activity_is_not_excluded_because_another_target_is_more_potent(self):
        aff = {("x", "A"): {"IC50": self.E(3.0)}, ("x", "B"): {"IC50": self.E(200.0)}}       # the nanatinostat shape: a measured 200 nM secondary action
        a = A.attribution({"x"}, "B", aff)
        self.assertEqual(a["state"], "SECONDARY_ACTIVITY_MEASURED")
        self.assertIn("on-target control", G.attribution_note(dict(attribution_state=a["state"], main_target="B", attribution_main_nm=a["main_nm"], attribution_fold=a["fold"],
                                                                     attribution_best_target="A", attribution_best_nm=a["best_nm"], identity_via="")))

    def test_no_ratio_still_states_a_low_absolute_value_without_blocking(self):          # verifier F09: colchicine Kd 20 uM
        aff = {("x", "A"): {"IC50": self.E(11.0)}, ("x", "B"): {"Kd": self.E(20000.0)}}
        a = A.attribution({"x"}, "B", aff)
        self.assertEqual(a["state"], "NOT_COMPARABLE_MEASURES")
        self.assertIn("low potency at the listed target on its own terms", a["context_note"])

    def test_a_missing_measure_never_becomes_a_negative(self):
        aff = {("x", "A"): {"IC50": self.E(3.0)}}
        self.assertEqual(A.attribution({"x"}, "B", aff)["state"], "UNMEASURED_AT_MAIN_TARGET")
        self.assertNotEqual(A.attribution({"x"}, "B", aff)["state"], "WEAK_ATTRIBUTION")

    def test_assay_context_and_censoring_gate_the_pair(self):
        cell = {("x", "A"): {"IC50": self.E(2.0, assay="biochemical")}, ("x", "B"): {"IC50": self.E(5000.0, assay="cell")}}
        self.assertEqual(A.attribution({"x"}, "B", cell)["state"], "NOT_COMPARABLE_MEASURES")           # cell-free against cell-based: not one scale
        unk = {("x", "A"): {"IC50": self.E(2.0)}, ("x", "B"): {"IC50": self.E(5000.0)}}
        a = A.attribution({"x"}, "B", unk)
        self.assertEqual(a["state"], "WEAK_ATTRIBUTION"); self.assertIn("not recorded", a["context_note"])  # unknown context stays visible
        # IT22 P8-fix (superseded assumption, verifier F05): a '<' on the OTHER target can only make the ratio larger, so an exact main value above 1 uM against '<2 nM' is a real weak signal
        cens = {("x", "A"): {"IC50": self.E(2.0, rel="<")}, ("x", "B"): {"IC50": self.E(5000.0)}}
        self.assertEqual(A.attribution({"x"}, "B", cens)["state"], "WEAK_ATTRIBUTION")
        small = {("x", "A"): {"IC50": self.E(2.0, rel="<")}, ("x", "B"): {"IC50": self.E(15.0)}}          # 15/2 = 7.5 at least: the ratio could be 100, so 'attributable' cannot be claimed
        self.assertEqual(A.attribution({"x"}, "B", small)["state"], "NOT_COMPARABLE_MEASURES")
        opp = {("x", "A"): {"IC50": self.E(2.0, rel=">")}, ("x", "B"): {"IC50": self.E(5000.0)}}          # '>' on the best side bounds the ratio from above only
        self.assertEqual(A.attribution({"x"}, "B", opp)["state"], "NOT_COMPARABLE_MEASURES")
        lowmain = {("x", "A"): {"IC50": self.E(2.0)}, ("x", "B"): {"IC50": self.E(50.0, rel=">")}}      # main only known to exceed 50 nM: not enough to call it weak
        self.assertEqual(A.attribution({"x"}, "B", lowmain)["state"], "NOT_COMPARABLE_MEASURES")
        lb = {("x", "A"): {"IC50": self.E(2.0)}, ("x", "B"): {"IC50": self.E(5000.0, rel=">")}}
        self.assertEqual(A.attribution({"x"}, "B", lb)["state"], "WEAK_ATTRIBUTION")                    # '>' on the main side is a lower bound: still weak

    def test_assay_class_never_guesses(self):
        self.assertEqual(A.assay_class("Assay using purified recombinant enzyme"), "biochemical")
        self.assertEqual(A.assay_class("Inhibition of proliferation in HEK cells"), "cell")
        self.assertEqual(A.assay_class(""), "unknown")
        self.assertEqual(A.assay_class("recombinant enzyme in cells"), "unknown")

    def test_the_loader_reports_the_original_measure_types(self):
        _, _, kinds = self.aff()
        self.assertTrue(kinds[("1", "TGT1")])

    def test_unmeasured_and_not_assessable_are_not_negatives(self):
        _, aff, _ = self.aff()
        self.assertEqual(A.attribution({"1"}, "NOPE", aff)["state"], "UNMEASURED_AT_MAIN_TARGET")
        self.assertEqual(A.attribution(set(), "TGT1", aff)["state"], "NOT_ASSESSABLE")
        self.assertEqual(A.attribution({"unknown-ligand"}, "TGT1", aff)["state"], "NOT_ASSESSABLE")

    def test_family_ligands_follow_the_chembl_id_and_the_merged_bridge(self):
        lig, _, _ = self.aff()
        fam = {e["id"]: e["id"] for e in self.entries}
        br = A.bridge_claim_name_ligands(self.entries, self.cache)
        fl = A.family_ligands(self.entries, fam, br, lig)
        self.assertEqual(fl["CAT:CHEMBL1"], {"1"})
        self.assertEqual(fl["CAT:DGIDB:a"], {"1"})
        self.assertNotIn("CAT:DGIDB:b", fl)

    def test_sensitivity_counts_at_each_threshold(self):
        self.assertEqual(A.sensitivity([1, 5, 12, 40, 400]), {"3.0": 4, "10.0": 3, "30.0": 2, "100.0": 1})


class HandoffGate(unittest.TestCase):
    ROLE = {"role_status": "unknown", "role_basis": "NONE", "leaning": "none", "h_harm_action": "x", "h_protect_action": "y"}

    def row(self, **kw):
        r = dict(arm="opposes", seed_specific_all_three_nulls="1", reach_z="4", family_id="F", name="cmpd", attribution_state="ATTRIBUTABLE")
        r.update(kw)
        return r

    META = {"F": {"has_chembl": "1", "modality": "small_molecule"}}

    def test_weak_attribution_blocks_with_its_own_reason(self):
        ok, why = G.eligible(self.row(attribution_state="WEAK_ATTRIBUTION"), self.ROLE, self.META, [])
        self.assertEqual((ok, why), (False, "main_target_weak_attribution"))

    def test_attributable_unmeasured_and_unassessed_rows_are_not_blocked_by_the_screen(self):
        for st in ("ATTRIBUTABLE", "UNMEASURED_AT_MAIN_TARGET", "NOT_ASSESSABLE", ""):
            self.assertNotEqual(G.eligible(self.row(attribution_state=st), self.ROLE, self.META, [])[1], "main_target_weak_attribution")

    def test_a_borderline_potent_main_target_is_not_blocked(self):
        self.assertNotEqual(G.eligible(self.row(attribution_state="BORDERLINE_POTENT_MAIN_TARGET"), self.ROLE, self.META, [])[1], "main_target_weak_attribution")
        self.assertNotEqual(G.eligible(self.row(attribution_state="SINGLE_MEASURED_TARGET"), self.ROLE, self.META, [])[1], "main_target_weak_attribution")

    def test_unmeasured_rows_rank_after_measured_ones_within_the_cap_and_are_labelled(self):        # V1-fix finding 4
        mk = lambda t, st, n, z: dict(question="Q", hypothesis="H", main_target=t, n_origins=n, zmin=z, name=t, chain_edges=1, attribution_state=st)
        rows = [mk("T1", "UNMEASURED_AT_MAIN_TARGET", 5, 9.0), mk("T2", "ATTRIBUTABLE", 1, 3.5), mk("T3", "SINGLE_MEASURED_TARGET", 1, 3.2), mk("T4", "NOT_ASSESSABLE", 1, 3.1)]
        self.assertEqual([r["main_target"] for r in G.select_handoff(rows, per_group=3)], ["T2", "T3", "T4"])
        self.assertEqual([r["main_target"] for r in G.select_handoff([dict(r, attribution_state="") for r in rows], per_group=3)], ["T1", "T2", "T3"])      # without V1: unchanged order
        note = G.attribution_note(dict(attribution_state="UNMEASURED_AT_MAIN_TARGET", main_target="T1", attribution_best_target="T9", attribution_best_nm=3))
        self.assertTrue(note.startswith("UNMEASURED AT MAIN TARGET"))
        self.assertIn("BORDERLINE", G.attribution_note(dict(attribution_state="BORDERLINE_POTENT_MAIN_TARGET", main_target="T", attribution_main_nm=2, attribution_fold=20,
                                                            attribution_best_target="U", attribution_best_nm=0.1)))
        self.assertIn("not attributable by comparison", G.attribution_note(dict(attribution_state="SINGLE_MEASURED_TARGET", main_target="T", attribution_main_nm=2)))

    def test_a_row_without_the_key_behaves_as_before_the_screen(self):
        r = self.row()
        r.pop("attribution_state")
        self.assertEqual(G.eligible(r, self.ROLE, self.META, [])[1], G.eligible(self.row(attribution_state=""), self.ROLE, self.META, [])[1])

    def test_identity_is_still_checked_before_the_screen(self):
        ok, why = G.eligible(self.row(attribution_state="WEAK_ATTRIBUTION"), self.ROLE, {"F": {"has_chembl": "0", "modality": "small_molecule"}}, [])
        self.assertEqual(why, "identity_not_resolved")

    def test_the_p4a_records_are_a_decision_source_only_when_asked(self):
        self.assertFalse(any("qualification_it21_p4a" in d[2] for d in G.earlier_decisions()))
        d = [x for x in G.earlier_decisions(include_p4a=True) if "qualification_it21_p4a" in x[2]]
        self.assertGreaterEqual(len(d), 6)
        self.assertIsNotNone(G.earlier_state("nanatinostat", G.earlier_decisions(include_p4a=True)))

    def test_no_status_word_can_be_qualified(self):
        for w in ("QUALIFIED", "KEEP", "RECOMMEND"):
            with self.assertRaises(Exception):
                G.check_status(w)


@unittest.skipUnless((V1 / "proposals_it21.tsv").exists(), "v1 tables not built")
class CommittedV1Tables(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.new = {r["proposal_id"]: r for r in tsv(V1 / "proposals_it21.tsv")}
        cls.old = {r["proposal_id"]: r for r in tsv(HERE / "results" / "proposals_it21.tsv")}
        cls.hand = tsv(V1 / "handoff_it21.tsv")

    def test_the_fix_changes_hand_over_fields_only_never_the_generated_rows(self):
        self.assertEqual(set(self.new), set(self.old))
        for i, n in self.new.items():
            for c in ("status", "qualified", "z_total", "z_indeg", "z_adm", "z_reach", "compound", "family_id", "main_target", "chain", "hypothesis"):
                self.assertEqual(n[c], self.old[i][c], (i, c))

    def test_no_row_is_qualified_and_every_row_is_conditional(self):
        for n in self.new.values():
            self.assertEqual(n["qualified"], "no")
            self.assertIn(n["status"], ("CONDITIONAL_H_HARM", "CONDITIONAL_H_PROTECT"))
        for h in self.hand:
            self.assertTrue(h["qualified"].startswith("no"))

    def test_the_conditional_probe_and_the_plausible_proposal_stay_conditional(self):
        for pid in ("IT21P2-0195", "IT21P2-0374"):                # GSK343, tizaterkib: contrast cases C1 and C2
            self.assertEqual(self.new[pid]["qualified"], "no")
            self.assertEqual(self.new[pid]["status"], self.old[pid]["status"])

    def test_the_glue_type_case_abstains(self):
        """Upstream abstention (P8-fix guard withholds glue/action-conflict rows before the proposal table): the V1 screen does NOT exercise it. The V1 contrast cases are the next three tests."""
        for n in self.new.values():
            if n["compound"].lower().startswith(("pomalidomide", "lenalidomide", "thalidomide")):
                self.assertNotEqual(n["main_target"].upper(), "CRBN", n["proposal_id"])

    def test_vorinostat_is_joined_to_its_chembl_record_and_stopped_by_the_attribution_not_by_identity(self):
        v = self.new["IT21P2-0031"]
        self.assertEqual(v["compound"].lower(), "vorinostat")
        self.assertEqual(v["sibling_family"], "FAM:CAT:CHEMBL98")
        self.assertEqual(v["attribution_state"], "WEAK_ATTRIBUTION")
        self.assertEqual(v["handoff_blocker"], "main_target_weak_attribution")
        self.assertEqual(v["status"], "CONDITIONAL_H_HARM")

    def test_v1_screen_abstains_on_weak_main_targets_and_not_on_potent_ones(self):        # V1-fix finding 5: a contrast case that does exercise the screen
        floor = A.POTENT_MAIN_NM
        weak = [n for n in self.new.values() if n["attribution_state"] == "WEAK_ATTRIBUTION"]
        self.assertTrue(weak)
        for n in weak:
            self.assertEqual(n["handoff_eligible"], "no", n["proposal_id"])
            earlier_gate = n["handoff_blocker"].startswith(("identity_", "modality_", "arm_", "reach_", "not_seed"))        # gates that precede the screen in eligible()
            self.assertTrue(earlier_gate or n["handoff_blocker"] == "main_target_weak_attribution", (n["proposal_id"], n["handoff_blocker"]))
            self.assertGreater(float(n["attribution_main_nm"]), floor)
            self.assertGreaterEqual(float(n["attribution_fold"]), A.WEAK_FOLD)
        for c in ("vorinostat", "nanatinostat"):
            self.assertIn(c, {n["compound"].lower() for n in weak})
        pot = [n for n in self.new.values() if n["attribution_state"] == "BORDERLINE_POTENT_MAIN_TARGET"]
        self.assertTrue(pot)
        for n in pot:
            self.assertLessEqual(float(n["attribution_main_nm"]), floor)
            self.assertGreaterEqual(float(n["attribution_fold"]), A.WEAK_FOLD)
            self.assertNotEqual(n["handoff_blocker"], "main_target_weak_attribution")
        self.assertIn("progesterone", {n["compound"].lower() for n in pot})        # canonical high-potency target previously blocked by an outlier functional value

    def test_the_estradiol_ester_twin_is_not_bridged_to_estradiol_in_the_committed_tables(self):
        for n in self.new.values():
            if n["compound"].lower() == "estradiol valerate":
                self.assertEqual(n["identity_via"], "")
                self.assertEqual(n["handoff_blocker"], "identity_not_resolved")

    def test_unmeasured_rows_in_the_hand_over_are_labelled_and_chosen_after_the_measured_ones(self):
        self.assertTrue(all(h["attribution_note"] for h in self.hand))
        elig = [r for r in self.new.values() if r["handoff_eligible"] == "yes"]
        self.assertEqual({r["proposal_id"] for r in G.select_handoff(elig)}, {h["proposal_id"] for h in self.hand})        # the table is what the selection rule gives
        for h in self.hand:
            if h["attribution_state"] == "UNMEASURED_AT_MAIN_TARGET":
                self.assertTrue(h["attribution_note"].startswith("UNMEASURED AT MAIN TARGET"))
                best = {}
                for r in elig:
                    if (r["question"], r["hypothesis"]) == (h["question"], h["hypothesis"]) and r["attribution_state"] != "UNMEASURED_AT_MAIN_TARGET":
                        best.setdefault(r["main_target"], r)
                handed_g = [x for x in self.hand if (x["question"], x["hypothesis"]) == (h["question"], h["hypothesis"])]
                self.assertEqual(len(handed_g), len(best) + sum(1 for x in handed_g if x["attribution_state"] == "UNMEASURED_AT_MAIN_TARGET")
                                 if len(best) < 3 else 3)        # an unmeasured row is handed only when the measured clusters of its group do not fill the cap

    def test_propose_without_v1_is_byte_identical_to_the_committed_p2_tables(self):
        import os, subprocess
        cache = os.environ.get("LEGEND_CATALOG_CACHE") or str(DR / "catalog" / "cache")
        if not (Path(cache) / "gtopdb").exists():
            self.skipTest("catalogue cache absent")
        with tempfile.TemporaryDirectory() as t:
            r = subprocess.run([sys.executable, str(HERE / "run_generation_it21.py"), "propose", "--no-v1", "--out-dir", t], capture_output=True, text=True, env=dict(os.environ, LEGEND_CATALOG_CACHE=cache))
            self.assertEqual(r.returncode, 0, r.stderr[-500:])
            for f in ("proposals_it21.tsv", "handoff_it21.tsv", "mechanism_clusters_it21.tsv", "summary_it21.json", "carried_prior_decisions.tsv"):
                self.assertEqual((Path(t) / f).read_bytes(), (HERE / "results" / f).read_bytes(), f)

    def test_the_hand_over_holds_no_weak_attribution_and_nothing_a_p4a_record_already_decided(self):
        ids = {h["proposal_id"] for h in self.hand}
        for i in ids:
            self.assertNotEqual(self.new[i]["attribution_state"], "WEAK_ATTRIBUTION")
            self.assertNotIn("decided", self.new[i]["handoff_blocker"])
        decided = {r["proposal_id"] for r in tsv(DR / "qualification_it21_p4a_20261103" / "qualification_it21_p4a.tsv")}
        self.assertFalse(ids & decided)

    def test_every_hand_over_row_carries_its_attribution_sentence(self):
        for h in self.hand:
            self.assertTrue(h.get("attribution_note"), h["proposal_id"])


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]], verbosity=1)
