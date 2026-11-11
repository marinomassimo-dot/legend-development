#!/usr/bin/env python3
"""IT43 P1 regressions: the comparison rows reach the role; three contrast cases on synthetic packages; the view obeys the engine."""
import csv, re, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import comparison_engine as ce  # noqa: E402
import hypothesis_package as hp  # noqa: E402

def pkg(dec, cmp_=None, meas=None):
    return {"dec": {d["prop_id"]: d for d in dec}, "cmp": cmp_ or {}, "meas": meas or {}}
def prop(i, stmt, depth="partial_fulltext_read", cls="compound/class", system="Xenopus oocytes, -40 mV, 50 uM glycine"):
    return {"prop_id": i, "statement": stmt, "depth": depth, "class": cls, "species_system_age_prep_exposure_readout": system}
def item(i, name, kind="probe"): return {"item_id": i, "name_full": name, "kind": kind}

class Contrast(unittest.TestCase):
    def test_measure_does_not_transfer_to_another_molecule(self):
        p = pkg([prop("D01", "DATO: alpha inhibits recombinant GluN1/GluN2B with IC50 72 nM"), prop("D02", "DATO: alpha and beta inhibit GluN1/GluN2B, IC50 72 nM and 9 nM")])
        r = {x["name"]: x for x in ce.derive([item("V1", "alpha; beta")], p)}
        self.assertEqual(r["alpha"]["evidence_tier"], "PRIMARY")
        self.assertEqual(r["beta"]["evidence_tier"], "TRANSFER")      # named only in a statement shared with another compound
        self.assertEqual(r["beta"]["role_derived"], "unresolved")
    def test_incompatible_conditions_give_no_merged_comparison(self):
        p = pkg([prop("D01", "DATO: alpha IC50 72 nM"), prop("D02", "DATO: alpha IC50 0.34 uM", system="Xenopus oocytes, -70 mV, 50 uM glycine")])
        self.assertTrue(ce.derive([item("V1", "alpha")], p)[0]["comparison_state"].startswith("NOT_COMPARABLE"))
        q = pkg([prop("D01", "DATO: alpha IC50 72 nM"), prop("D02", "DATO: alpha IC50 80 nM")])
        self.assertEqual(ce.derive([item("V1", "alpha")], q)[0]["comparison_state"], "COMPARABLE")
    def test_assay_scaffold_and_atp_make_values_not_comparable(self):
        p = pkg([prop("D01", "DATO: alpha IC50 87 nM with the E2p/E3BP core", system="human PDK1, with the E2p/E3BP core, 5 uM ATP"), prop("D02", "DATO: alpha IC50 stimulation core-free, 10 fold", system="human PDK3, core-free, 5 uM ATP")])
        self.assertTrue(ce.derive([item("V1", "alpha")], p)[0]["comparison_state"].startswith("NOT_COMPARABLE"))
        q = pkg([prop("D01", "DATO: alpha IC50 87 nM", system="human PDK1, with the E2p/E3BP core, 5 uM ATP"), prop("D02", "DATO: alpha IC50 90 nM", system="human PDK1, with the E2p/E3BP core, 5 uM ATP")])
        self.assertEqual(ce.derive([item("V1", "alpha")], q)[0]["comparison_state"], "COMPARABLE")
    def test_unknown_premise_stays_conditional_never_refuted(self):
        r = ce.derive([item("V1", "gamma")], pkg([prop("D01", "DATO: alpha IC50 72 nM")]))[0]
        self.assertEqual((r["evidence_tier"], r["role_derived"]), ("NONE", "unresolved"))
        self.assertNotIn("weak", r["role_derived"])                    # not stated is not tested and absent
    def test_limit_proposition_caps_the_limited_datum(self):
        p = pkg([prop("D15", "DATO: nbqx Ki 0.077 uM at GluA2"), prop("D16", "INFERENZA (limit of D15): nbqx used only as a comparator", cls="absence")])
        self.assertEqual(ce.derive([item("V1", "nbqx")], p)[0]["evidence_tier"], "NONE")

class RealPackages(unittest.TestCase):
    def rows(self):
        items = [r for r in csv.DictReader(open(HERE.parent / "generation_it41_20261109/compound_view.tsv", encoding="utf-8"), delimiter="\t") if r["inv_id"] == "INV-05"]
        pk = [p for p in hp.load_all() if p.get("role") == "pharmacological_comparison" and p.get("inv_id") == "INV-05"]
        return items, ce.merge([x for p in pk for x in ce.derive(items, p, p["dir"].parent.name.split("_")[0])])
    def test_view_never_exceeds_the_engine(self):
        items, res = self.rows(); kind = {i["item_id"]: i["kind"] for i in items}; src = {i["item_id"]: i["source_rows"] for i in items}
        for r in res:
            if r["evidence_tier"] == "NONE" and kind[r["item_id"]] in ("probe", "known_requalified"):
                # outside the registered packages the engine cannot adjudicate: the view must cite where its evidence lives (SCI42 package, not a registered comparison)
                self.assertRegex(src[r["item_id"]], r"(?i)search_rows|PMID|sci42", f'{r["item_id"]} {r["name"]} has no cited source outside the perimeter'); continue
            if kind[r["item_id"]] in ("probe", "known_requalified"):
                self.assertEqual(r["role_derived"] in ("probe", "known_requalified"), True, f'{r["item_id"]} {r["name"]}: view says {kind[r["item_id"]]}, engine tier {r["evidence_tier"]}')
    def test_before_after_ro_25_6981(self):
        _, res = self.rows(); d = {r["name"]: r for r in res}
        self.assertEqual(d["ifenprodil"]["role_derived"], "probe")
        self.assertEqual(d["Ro 25-6981"]["role_derived"], "unresolved")
        self.assertEqual(d["d-APV"]["role_derived"], "control")
    def test_decisions_file_is_current(self):
        _, res = self.rows(); got = list(csv.DictReader(open(HERE / "compound_decisions_it43.tsv", encoding="utf-8"), delimiter="\t"))
        self.assertEqual([(r["item_id"], r["name"], r["role_derived"]) for r in res], [(r["item_id"], r["name"], r["role_derived"]) for r in got])

class SecondInvestigation(unittest.TestCase):
    def test_inv07_items_are_derived_and_their_file_is_current(self):
        items = [r for r in csv.DictReader(open(HERE.parent / "generation_it41_20261109/compound_view.tsv", encoding="utf-8"), delimiter="\t") if r["inv_id"] == "INV-07"]
        pk = [p for p in hp.load_all() if p.get("role") == "pharmacological_comparison" and p.get("inv_id") == "INV-07"]
        res = ce.merge([x for p in pk for x in ce.derive(items, p, p["dir"].parent.name.split("_")[0])])
        got = list(csv.DictReader(open(HERE / "compound_decisions_inv07_it44.tsv", encoding="utf-8"), delimiter="\t"))
        self.assertEqual([(r["item_id"], r["name"], r["role_derived"]) for r in res], [(r["item_id"], r["name"], r["role_derived"]) for r in got])
        self.assertTrue({r["name"] for r in res} >= {"dichloroacetate", "AZD7545", "VER-246608"})

if __name__ == "__main__": unittest.main(verbosity=2)
