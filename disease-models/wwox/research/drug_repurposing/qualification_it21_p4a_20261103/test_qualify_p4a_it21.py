#!/usr/bin/env python3
"""Tests of the IT21 P4a qualification tables: closed disposition vocabulary, no status upgrade, every number quoted for a decision traced to a retrieved table,
verbatim locators matched to the saved text when it is present, receipts consistent with the reading-depth table, no e-mail string in the package.
  test_qualify_p4a_it21.py            run all
Standard library only; offline."""
import csv, json, re, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
P2 = HERE.parent / "generation_it21_p2_20261103" / "results" / "handoff_it21.tsv"
FULLTEXT = HERE.parents[4] / "files" / "fulltext" / "PMC4678600_PMID26682036_Hopkinson2013_IOX1.xml.txt"


def tsv(name):
    with open(HERE / name, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


Q = tsv("qualification_it21_p4a.tsv")
VOCAB = {"KEPT_CONDITIONAL", "QUALIFIED_HYPOTHESIS", "REJECTED_INFORMATIVE", "INCONCLUSIVE"}


def act(pid, gene_or_name, std="IC50"):
    rows = [r for r in tsv("chembl_activities_by_target.tsv") if r["proposal"] == pid and r["standard_type"] == std and r["gene_symbols"] == gene_or_name]
    return rows


class Dispositions(unittest.TestCase):
    def test_six_rows_all_from_the_handoff(self):
        hand = {r["proposal_id"]: r for r in csv.DictReader(open(P2, newline=""), delimiter="\t")}
        self.assertEqual(len(Q), 6)
        for q in Q:
            self.assertIn(q["proposal_id"], hand)
            self.assertEqual(q["status_before"], hand[q["proposal_id"]]["status"])

    def test_vocabulary_closed_and_nothing_qualified(self):
        for q in Q:
            self.assertIn(q["disposition"], VOCAB)
        self.assertEqual([q["proposal_id"] for q in Q if q["disposition"] == "QUALIFIED_HYPOTHESIS"], [], "a qualified hypothesis needs a sourced role and a measured link in a WWOX system")

    def test_status_never_promotes_and_a_rejection_closes_the_row_as_written(self):
        # P8-fix (verifier B4): a rejected row no longer reads as a live conditional; CLOSED_AS_WRITTEN is a closed status, not a promotion.
        for q in Q:
            if q["disposition"] == "REJECTED_INFORMATIVE":
                self.assertEqual(q["status_after"], "CLOSED_AS_WRITTEN")
            else:
                self.assertEqual(q["status_after"], q["status_before"])
                self.assertTrue(q["status_after"].startswith("CONDITIONAL_H_"))
        self.assertEqual(sum(q["status_after"] == "CLOSED_AS_WRITTEN" for q in Q), 3)
        for r in tsv("status_after_it21_p4a.tsv"):
            self.assertEqual(r["status_changed"].startswith("yes"), r["disposition"] == "REJECTED_INFORMATIVE")
            self.assertTrue(r["qualified"].startswith("no"))
            self.assertNotIn("QUALIFIED", r["status_after"].replace("NOT_QUALIFIED", ""))

    def test_status_vocabulary_is_the_generators_closed_vocabulary(self):
        import importlib.util, sys
        spec = importlib.util.spec_from_file_location("run_generation_it21_for_p4a", HERE.parent / "generation_it21_p2_20261103" / "run_generation_it21.py")
        g = importlib.util.module_from_spec(spec); sys.modules[spec.name] = g; spec.loader.exec_module(g)
        for q in Q:
            self.assertEqual(g.check_status(q["status_after"]), q["status_after"])

    def test_five_part_output_filled(self):
        for q in Q:
            for k in ("foundation", "decisive_assumption", "counter_evidence", "next_test", "result_that_would_change_the_decision", "reasons", "classification", "unverified"):
                self.assertTrue(q[k].strip(), (q["proposal_id"], k))

    def test_no_rename_called_new_relation(self):
        for q in Q:
            c = q["classification"]
            self.assertEqual(c.count("new relation"), c.count("not a new relation"), q["proposal_id"])
            self.assertIn("re-emitted", c, "every handed-over proposal is a thread already generated in IT9/IT10")

    def test_records_in_ranking_format(self):
        recs = tsv("it21_p4a_records.tsv")
        self.assertEqual(list(recs[0].keys()), ["cand_id", "package", "compound", "state", "decision", "unit_id", "class", "origin", "need"])
        for r in recs:
            self.assertIn(r["state"], {"KEEP", "INCONCLUSIVE", "DROP", "REFERENCE", "CONDITIONAL"})
            self.assertTrue(r["decision"].startswith(r["state"]))


class NumbersTraceToTables(unittest.TestCase):
    def test_nanatinostat(self):
        v = {g: float(act("IT21P2-0006", g)[0]["min_value"]) for g in ("HDAC1", "HDAC2", "HDAC3", "HDAC5", "HDAC6")}
        self.assertEqual((v["HDAC1"], v["HDAC2"], v["HDAC3"], v["HDAC5"], v["HDAC6"]), (3.0, 4.0, 7.0, 200.0, 2100.0))
        self.assertAlmostEqual(v["HDAC5"] / v["HDAC1"], 66.7, delta=0.1)

    def test_iox1(self):
        egln = act("IT21P2-0008", "EGLN1")
        self.assertEqual((min(float(r["min_value"]) for r in egln), max(float(r["max_value"]) for r in egln)), (14300.0, 15000.0))
        k4c = act("IT21P2-0008", "KDM4C")
        self.assertEqual((float(k4c[0]["min_value"]), round(float(k4c[0]["max_value"]))), (200.0, 631.0))

    def test_gsk343_and_tizaterkib_and_cgi(self):
        self.assertTrue(any(float(r["min_value"]) == 4.0 for r in tsv("chembl_activities_by_target.tsv") if r["proposal"] == "IT21P2-0195" and r["standard_type"] == "IC50" and "EZH2" in r["gene_symbols"]))
        self.assertTrue(any(float(r["min_value"]) == 9000.0 for r in tsv("chembl_activities_by_target.tsv") if r["proposal"] == "IT21P2-0195" and r["target_name"] == "Unchecked"))
        self.assertTrue(any(r["gene_symbols"] == "CDK5;CDK5R1" and float(r["min_value"]) == 300.0 for r in tsv("chembl_activities_by_target.tsv") if r["proposal"] == "IT21P2-0374"))
        btk = [r for r in tsv("chembl_activities_by_target.tsv") if r["proposal"] == "IT21P2-0057" and r["gene_symbols"] == "BTK" and r["target_organism"] == "Homo sapiens"]
        self.assertEqual((float(btk[0]["min_value"]), float(btk[0]["max_value"])), (0.61, 81.0))

    def test_srt2104_has_no_sirt1_activity_row_and_a_clinical_mechanism_label(self):
        self.assertFalse([r for r in tsv("chembl_activities_by_target.tsv") if r["proposal"] == "IT21P2-0512" and "SIRT1" in r["gene_symbols"]])
        mech = [r for r in tsv("chembl_mechanism.tsv") if r["proposal"] == "IT21P2-0512"]
        self.assertEqual(len(mech), 1)
        self.assertEqual(mech[0]["action_type"], "ACTIVATOR")
        self.assertEqual(sorted(json.loads(mech[0]["refs"])), ["23770971", "26556603", "27239324"])

    def test_expression_claims(self):
        rows = {}
        with open(HERE / "organoid_target_gene_rows.tsv", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                rows[r["gene"]] = r
        self.assertAlmostEqual(float(rows["SLC2A1"]["meanKO_over_meanWT_cpm"]), 2.67, places=2)
        self.assertAlmostEqual(float(rows["HDAC5"]["meanKO_over_meanWT_cpm"]), 0.81, places=2)
        self.assertLess(max(float(rows["BTK"][f"cpm_{c}"]) for c in ("cko1", "cko2", "cko3", "cko4", "cwt1", "cwt2")), 0.6)
        self.assertLess(max(float(rows["NPY"][f"cpm_{c}"]) for c in ("cko1", "cko2", "cko3", "cko4")), 0.15)
        self.assertGreater(min(float(rows["NPY"][f"cpm_{c}"]) for c in ("cwt1", "cwt2")), 3.0)
        self.assertEqual(float(rows["IL6"]["cpm_cko1"]), 0.0)
        h = {r["gene"]: r for r in csv.DictReader(open(HERE / "hnpc_target_gene_rows.tsv", newline=""), delimiter="\t")}
        for g in ("BTK", "NPY", "IL6", "TNF", "KDM4C", "SIRT1", "BCL3"):
            self.assertEqual(h[g]["hNSC"], "ABSENT", g)

    def test_edge_signs_recorded_against_the_network(self):
        e = {(r["proposal_id"], r["edge"]): r for r in tsv("edge_provenance_it21_p4a.tsv")}
        self.assertTrue(e[("IT21P2-0195", "EZH2 -T(+)-> IL6")]["matches"].startswith("NO"))
        self.assertTrue(e[("IT21P2-0512", "SIRT1 -T(-)-> MYC")]["grade"].startswith("CONTESTED"))
        om = {r["edge"]: r for r in tsv("edge_records_omnipath.tsv")}
        self.assertIn("22190494", om["SIRT1>MYC"]["references"])
        self.assertIn("29132376", om["EZH2>IL6"]["references"])
        self.assertIn("22991226", om["HDAC5>SLC2A1"]["references"])


class ReadingsAndReceipts(unittest.TestCase):
    def test_locators_verbatim_in_saved_text(self):
        if not FULLTEXT.exists():
            self.skipTest("saved text is under the gitignored files/ tree of the checkout that fetched it")
        txt = FULLTEXT.read_text()
        for r in tsv("locators_it21_p4a.tsv"):
            self.assertIn(r["verbatim_quote"], txt, r["locator_id"])

    def test_receipts_match_reading_table(self):
        rec = {p.stem for p in (HERE / "receipts").glob("*.json")}
        used = {r["receipt_prepared"].split("/")[-1][:-5] for r in tsv("reading_depth_it21_p4a.tsv") if r["receipt_prepared"].startswith("receipts/")}
        self.assertEqual(rec, used)
        for p in (HERE / "receipts").glob("*.json"):
            d = json.loads(p.read_text())
            self.assertEqual(d["event_id"], p.stem)
            self.assertIn(d["evidence_depth"], {"abstract_only", "partial_fulltext_read"})
            self.assertNotEqual(d["evidence_depth"], "complete_fulltext_read")
            if d["evidence_depth"] == "abstract_only":
                self.assertEqual(d["coverage"]["results"], "unavailable")
            self.assertNotIn("is explicitly NOT in the ledger", d["workflow"])

    def test_title_only_is_never_receipted(self):
        for r in tsv("reading_depth_it21_p4a.tsv"):
            if r["depth_in_this_package"].startswith("TITLE_ONLY"):
                self.assertEqual(r["receipt_prepared"], "none")


class Privacy(unittest.TestCase):
    def test_no_email_string(self):
        pat = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
        for p in HERE.rglob("*"):
            if p.is_file() and p.suffix in {".tsv", ".md", ".py", ".json"} and p.name != "test_qualify_p4a_it21.py":
                self.assertFalse(pat.search(p.read_text(errors="ignore")), p.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
