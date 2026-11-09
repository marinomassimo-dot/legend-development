#!/usr/bin/env python3
"""IT40: conditional physiological proposals, mechanism-first search, identity of named tools, reader view. New behaviours only."""
import csv, re, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = HERE.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import conditional_proposals as cp  # noqa: E402
import repurposing_view as rv  # noqa: E402

def tsv(p): return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
NAMES = re.compile(r"perampanel|radiprodil|ifenprodil|memantine|ivabradine|ZD7288|TCN-201|carbenoxolone|NBQX|GYKI|XE991|retigabine|brilliant blue|d-APV", re.I)

class Conditional(unittest.TestCase):
    def test_six_rows_without_gene_arc(self):
        r = cp.rows(True)
        self.assertEqual(sorted(x["proposal_id"] for x in r), ["CP-BH1", "CP-BH2", "CP-BH3", "CP-MH1", "CP-MH2", "CP-MH3"])
        for x in r:
            blob = " ".join(x.values())
            self.assertNotRegex(blob, r"HGNC:\d|-T\(|-P\(|gene_arc\s*=\s*True")
            self.assertEqual(x["kind"], "conditional_physiological_hypothesis")

    def test_seven_things_are_kept(self):
        for x in cp.rows(True):
            for f in ("starting_observation_and_chain", "context", "competing_explanations", "premise_and_action", "source_and_limits", "decision_measure"):
                self.assertTrue(x[f].strip(), (x["proposal_id"], f))
            self.assertNotIn("[:", x["expected_result_by_explanation"])
            self.assertIn("INFERENZA", x["corrections_it40"])
        for x in cp.rows(True):
            if x["proposal_id"].startswith("CP-BH"):
                self.assertTrue(x["expected_result_by_explanation"].strip(), x["proposal_id"])

    def test_abstention_is_kept_where_the_package_nominates_nothing(self):
        m = {x["proposal_id"]: x["nomination"] for x in cp.rows(True)}
        self.assertEqual(m["CP-MH1"], "ABSTAIN"); self.assertEqual(m["CP-MH3"], "ABSTAIN")
        self.assertTrue(m["CP-BH2"].startswith("NAMED_BY_PACKAGE_ONLY"))

    def test_link_adds_what_the_free_text_did_not_carry(self):
        on, off = {x["proposal_id"]: x for x in cp.rows(True)}, {x["proposal_id"]: x for x in cp.rows(False)}
        for k in on:
            self.assertEqual(off[k]["expected_result_by_explanation"], "")
        self.assertGreater(len(on["CP-BH2"]["competing_explanations"]), len(off["CP-BH2"]["competing_explanations"]))
        self.assertIn("AB04", on["CP-BH2"]["competing_explanations"])

class MechanismSearch(unittest.TestCase):
    def test_record_granularity_is_not_read_as_selectivity(self):
        rows = [r for r in tsv(DR / "mechsearch_it40_20261109/by_action.tsv") if r["relation"] == "R1"]
        g = {r["name"]: r["target_record_granularity"] for r in rows}
        for n in ("RADIPRODIL", "TRAXOPRODIL", "RISLENEMDAZ", "EVT-101"): self.assertEqual(g[n], "two_gene_assembly_record")
        self.assertEqual(g["MEMANTINE HYDROCHLORIDE"], "family_record_subunit_unresolved")
        for r in cp.rows(True):
            self.assertNotRegex(r["catalogue_by_action"], r"subunit-specific|not subunit-selective")

    def test_counts_are_distinct_molecules(self):
        ba = cp.by_action()
        r3 = [r for r in ba["R3"] if r["catalogue_id"]]
        self.assertGreater(len(r3), len({r["parent_molecule"] for r in r3}))
        self.assertIn("distinct parent molecules", cp.catalogue_summary(["R3"], ba))

    def test_r6_placeholder_is_not_a_catalogue_row(self):
        self.assertNotRegex(cp.catalogue_summary(["R6"], cp.by_action()), r"\b1 catalogue rows")

    def test_direction_is_kept(self):
        r3 = [r for r in tsv(DR / "mechsearch_it40_20261109/by_action.tsv") if r["relation"] == "R3"]
        self.assertTrue(any(r["direction"] == "up" for r in r3), "positive modulators must not sit in an antagonist request")

    def test_identity_of_named_tools(self):
        v = {r["package_name"]: r["verdict"] for r in tsv(DR / "mechsearch_it40_20261109/identity_check.tsv")}
        self.assertNotEqual(v["GYKI 52466"], "TARGET_CONFIRMED")
        self.assertEqual(v["brilliant blue FCF"], "NOT_IN_CATALOGUE")
        self.assertEqual(v["d-APV (D-Ap5)"], "TARGET_CONFIRMED")
        self.assertEqual(v["TCN-201"], "TARGET_CONFIRMED")

class ReaderView(unittest.TestCase):
    def test_reader_table_matches_the_links_and_names_no_compound(self):
        rows = tsv(DR / rv.PHYSIO_FILE)
        ids = {r["hyp_id"] for r in rows}
        linked = set()
        for pkg in ("ampa_nmda_discrim_20261108", "membrane_hypotheses_20261108"):
            linked |= {r["hyp_id"] for r in tsv(DR / pkg / "output/consumer_links.tsv")}
        self.assertEqual(ids, linked)
        for r in rows:
            self.assertIsNone(NAMES.search(" ".join(r[k] for k in rv.PHYSIO_FIELDS)), r["hyp_id"])

    def test_view_map_by_investigation(self):
        m = rv.physiological_view(DR)
        self.assertEqual({k: len(v) for k, v in m.items()}, {"INV-05": 3, "INV-18": 3})

class Rendered(unittest.TestCase):
    """The built pages: both editions, all five languages, carry the block under both investigations, with the language's own heading and no compound name."""
    HEAD = {"it": "Ipotesi fisiologiche condizionali", "en": "Conditional physiological hypotheses", "fr": "Hypothèses physiologiques conditionnelles", "es": "Hipótesis fisiológicas condicionales", "de": "Bedingte physiologische Hypothesen"}

    def test_pages(self):
        seen = set()
        for p in sorted((DR / "view").glob("index*.html")):
            h = p.read_text(encoding="utf-8")
            lang = re.search(r'<html lang="(\w+)"', h).group(1)
            seen.add((p.name.startswith("index_shareable"), lang))
            self.assertEqual(h.count('class="inv-phys"'), 2, p.name)
            self.assertIn(self.HEAD[lang], h, p.name)
            blocks = re.findall(r'<details class="inv-phys">.*?</details>', h, re.S)
            self.assertEqual(len(blocks), 2)
            for b in blocks:
                self.assertIsNone(NAMES.search(re.sub(r"<[^>]+>", " ", b)), p.name)
        self.assertEqual(len(seen), 10, sorted(seen))


if __name__ == "__main__":
    unittest.main()
