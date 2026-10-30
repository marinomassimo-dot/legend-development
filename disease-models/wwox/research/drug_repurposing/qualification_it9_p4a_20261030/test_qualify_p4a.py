#!/usr/bin/env python3
"""Positive checks for IT9 P4a (present facts by identifier; no absence assertion on live or append-only state). `--help` prints this text only."""
import csv, hashlib, json, subprocess, sys, tempfile, unittest
from pathlib import Path

if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)
HERE = Path(__file__).resolve().parent
DRUG = HERE.parent


def rows(name):
    return list(csv.DictReader(open(HERE / name, encoding="utf-8"), delimiter="\t"))


class T(unittest.TestCase):
    def test_denominators(self):
        s = json.load(open(HERE / "run_summary.json"))
        self.assertFalse(s["ldha"]["truncated"])
        self.assertEqual(s["ldha"]["retrieved"], s["ldha"]["total"])
        self.assertEqual(s["ldhb"]["retrieved"], s["ldhb"]["total"])
        self.assertEqual(s["stiripentol"]["rows"], s["stiripentol"]["total"])
        sel = rows("ldha_nanomolar_selectivity.tsv")
        self.assertEqual(len(sel), s["n_nm"])
        self.assertEqual(sum(1 for r in sel if r["n_same_document_pairs"] != "0"), 89)
        self.assertTrue(all(r["n_ldhb_rows"] != "0" or r["reading"].startswith("no LDHB row") for r in sel))

    def test_pairs_are_same_document_equals(self):
        for r in rows("ldha_ldhb_pairs.tsv"):
            if r["ratio_kind"] == "ratio_equals":
                self.assertEqual(r["ldha_relation"], "=")
                self.assertEqual(r["ldhb_relation"], "=")
                self.assertAlmostEqual(float(r["ldhb_over_ldha"]), float(r["ldhb_nM"]) / float(r["ldha_nM"]), places=3)

    def test_named_facts(self):
        k = {(r["molecule_chembl_id"], r["isoform_target"], r["document"], r["value"]) for r in rows("ldh_key_compounds_rows.tsv")}
        self.assertIn(("CHEMBL3335794", "LDHB", "CHEMBL3763153", "43"), k)
        pdk = [r for r in rows("pdk_documents.tsv") if r["document"] == "CHEMBL6121009" and r["isoform"] == "PDK4"]
        self.assertTrue(any(r["molecule_chembl_id"] == "CHEMBL13960" and r["value"] == "108000" for r in pdk))
        self.assertTrue(any(r["molecule_chembl_id"] == "CHEMBL3727577" and r["value"] == "22" for r in pdk))
        types = {r["standard_type"]: int(r["n_rows"]) for r in rows("stiripentol_types.tsv")}
        self.assertEqual(sum(types.values()), 88)

    def test_consumers_carry_the_restatement(self):
        for card, needle in (("E02_ldh_inhibition", "not sufficiently supported as an LDH-engagement probe"), ("I01_pdk_inhibition_dca_premise_seizure_glycaemia", "more interpretable than dichloroacetate alone"),
                             ("F03_bumetanide_chloride_gradient", "requires verification of relevant exposure")):
            self.assertIn(needle, json.dumps(json.load(open(DRUG / "cards" / f"{card}.card.json"))), card)
        wo = json.load(open(DRUG / "view/work_order.json"))
        by = {e["need"]: e for e in wo["entries"]}
        for n in ("NEED-LACTATE-LDH", "NEED-PDH-PYRUVATE-AXIS"):
            self.assertIn("IT9-P4a", by[n]["updated_by"])
        self.assertIn("IT9-P4a", wo["docs"])

    def test_rebuild_is_byte_identical(self):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "collected.json.gz").write_bytes((HERE / "collected.json.gz").read_bytes())
            subprocess.run([sys.executable, str(HERE / "qualify_p4a.py"), "rebuild", "--out", d], check=True, capture_output=True)
            for n in ("ldha_nanomolar_selectivity.tsv", "ldha_ldhb_pairs.tsv", "pdk_documents.tsv", "pdk_matched_to_dca.tsv", "pdk_named_probe_rows.tsv", "documents_used.tsv", "bumetanide_exposure_arithmetic.tsv"):
                self.assertEqual(hashlib.sha256(Path(d, n).read_bytes()).hexdigest(), hashlib.sha256((HERE / n).read_bytes()).hexdigest(), n)


if __name__ == "__main__":
    unittest.main(verbosity=2)
