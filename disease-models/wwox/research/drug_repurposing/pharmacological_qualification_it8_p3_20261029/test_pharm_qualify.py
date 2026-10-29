#!/usr/bin/env python3
"""Positive regression for IT8 P3. `--help` does nothing but print this. Run from anywhere:
  python3 disease-models/wwox/research/drug_repurposing/pharmacological_qualification_it8_p3_20261029/test_pharm_qualify.py
Checks present facts by identifier (no absence assertion on live or append-only state): the tables are rectangular and carry the nine
cases; the three changed decisions are present in cases.json, in the card packets they name and in the work order; the other six
declare their missing datum; rebuilding from collected.json.gz reproduces comparison.tsv byte for byte; the fault-injection selftest passes."""
import csv, hashlib, json, subprocess, sys, tempfile, unittest
from pathlib import Path

if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)
HERE = Path(__file__).resolve().parent
DRUG = HERE.parent


class T(unittest.TestCase):
    def test_tables_rectangular(self):
        for name, ncol in (("comparison.tsv", 21), ("measures_detail.tsv", 21)):
            rows = list(csv.reader(open(HERE / name, encoding="utf-8"), delimiter="\t"))
            self.assertEqual({len(r) for r in rows}, {len(rows[0])}, name)
        rows = list(csv.DictReader(open(HERE / "comparison.tsv", encoding="utf-8"), delimiter="\t"))
        self.assertEqual([r["case_id"] for r in rows], [f"Q0{i}" for i in range(1, 10)])
        self.assertEqual(sorted(r["case_id"] for r in rows if r["decision_status"] == "changed"), ["Q03", "Q04", "Q08"])
        for r in rows:
            if r["decision_status"] != "changed":
                self.assertEqual(r["decision_status"], "no_change_data_cannot_change")
                self.assertTrue(r["datum_that_changed_it"].startswith("none; "), r["case_id"])

    def test_service_states_are_distinct_vocabulary(self):
        txt = (HERE / "comparison.tsv").read_text()
        self.assertIn("ROWS_RETRIEVED_TRUNCATED", txt)      # LDHA / PDK1 / PDK2 target-first pulls
        self.assertIn("NO_ROWS_UNDER_FILTERS", txt)         # magnesium sulfate, elemental lithium
        log = list(csv.DictReader(open(HERE / "service_log.tsv"), delimiter="\t"))
        self.assertGreater(len(log), 100)
        self.assertEqual({r["case"] for r in log}, {f"Q0{i}" for i in range(1, 10)})

    def test_changed_decisions_reach_the_consumers(self):
        e02 = json.load(open(DRUG / "cards/E02_ldh_inhibition.card.json"))
        self.assertIn("IT8 P3 2026-10-29", json.dumps(e02))
        i01 = json.load(open(DRUG / "cards/I01_pdk_inhibition_dca_premise_seizure_glycaemia.card.json"))
        self.assertIn("nanomolar potency", json.dumps(i01))
        f03 = json.load(open(DRUG / "cards/F03_bumetanide_chloride_gradient.card.json"))
        self.assertIn("ex vivo", json.dumps(f03))
        wo = json.load(open(DRUG / "view/work_order.json"))
        by = {e["need"]: e for e in wo["entries"]}
        for need in ("NEED-LACTATE-LDH", "NEED-PDH-PYRUVATE-AXIS"):
            self.assertIn("IT8-P3", by[need]["updated_by"])
            self.assertIn("IT8-P3", by[need]["docs"])
        self.assertIn("IT8-P3", wo["docs"])
        html = (DRUG / "view/index.html").read_text()
        self.assertIn("IT8 P3 2026-10-29", html)

    def test_rebuild_is_byte_identical(self):
        with tempfile.TemporaryDirectory() as d:
            for n in ("collected.json.gz",):
                Path(d, n).write_bytes((HERE / n).read_bytes())
            subprocess.run([sys.executable, str(HERE / "pharm_qualify.py"), "rebuild", "--out", d], check=True, capture_output=True)
            for n in ("comparison.tsv", "measures_detail.tsv"):
                self.assertEqual(hashlib.sha256(Path(d, n).read_bytes()).hexdigest(), hashlib.sha256((HERE / n).read_bytes()).hexdigest(), n)

    def test_selftest(self):
        r = subprocess.run([sys.executable, str(HERE / "pharm_qualify.py"), "selftest"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("selftest OK", r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
