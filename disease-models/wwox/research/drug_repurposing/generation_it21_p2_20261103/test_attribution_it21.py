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
            ["6", "noref", "", KEY_A, "", "", "Synthetic organic"]])
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
                                     ("OtherDb", "IUPHAR.LIGAND:1", "NOTGTOPDB"), ("GuideToPharmacology", "drugone", "NAMEONLY")]:
                w.writerow([src, claim, name])
        self.cache = c
        self.entries = [entry("CAT:CHEMBL1", "DRUGONE", "chembl_selected", "CHEMBL1", KEY_A), entry("CAT:CHEMBL2", "DRUGTWO", "chembl_selected", "CHEMBL2", KEY_A),
                        entry("CAT:CHEMBL3", "DRUGTHREE", "chembl_selected", "CHEMBL3", KEY_A), entry("CAT:CHEMBL4", "DRUGFOUR", "chembl_selected", "CHEMBL4", KEY_A),
                        entry("CAT:CHEMBL5", "DRUGFIVE", "chembl_selected", "CHEMBL5", KEY_A),
                        entry("CAT:DGIDB:a", "Drugone", "dgidb_only", dg_name="DRUGONE"), entry("CAT:DGIDB:b", "Drugthree", "dgidb_only", dg_name="DRUGTHREE"),
                        entry("CAT:DGIDB:c", "Drugfour", "dgidb_only", dg_name="DRUGFOUR"), entry("CAT:DGIDB:d", "Drugfive", "dgidb_only", dg_name="DRUGFIVE"),
                        entry("CAT:DGIDB:e", "Sharedname", "dgidb_only", dg_name="SHAREDNAME"), entry("CAT:DGIDB:f", "Notgtopdb", "dgidb_only", dg_name="NOTGTOPDB"),
                        entry("CAT:DGIDB:g", "Nameonly", "dgidb_only", dg_name="NAMEONLY"),
                        entry("CAT:DGIDB:h", "Drugone", "dgidb_only", dg_name="ALREADY", iuphar=["1"])]

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
        self.assertEqual(fb, {"CAT:DGIDB:a": "CAT:CHEMBL1"})


class AttributionScreen(SyntheticCache):
    def aff(self):
        return A.load_gtopdb_affinities(self.cache)

    def test_human_only_and_nm_from_the_original_column_or_the_log_value(self):
        _, aff, _ = self.aff()
        self.assertEqual(aff[("1", "TGT1")], 1.3)
        self.assertNotIn(("1", "TGT9"), aff)
        self.assertAlmostEqual(aff[("9", "TGT2")], 100.0, places=3)

    def test_weak_when_the_main_target_is_at_least_ten_fold_weaker_than_the_best(self):
        _, aff, _ = self.aff()
        a = A.attribution({"1"}, "TGT5", aff)
        self.assertEqual(a["state"], "WEAK_ATTRIBUTION")
        self.assertGreater(a["fold"], 2000)
        self.assertEqual(a["best_target"], "TGT1")

    def test_attributable_at_the_best_target_and_threshold_boundary(self):
        _, aff, _ = self.aff()
        self.assertEqual(A.attribution({"1"}, "TGT1", aff)["state"], "ATTRIBUTABLE")
        aff2 = {("x", "A"): 1.0, ("x", "B"): 9.99, ("x", "C"): 10.0}
        self.assertEqual(A.attribution({"x"}, "B", aff2)["state"], "ATTRIBUTABLE")
        self.assertEqual(A.attribution({"x"}, "C", aff2)["state"], "WEAK_ATTRIBUTION")

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
