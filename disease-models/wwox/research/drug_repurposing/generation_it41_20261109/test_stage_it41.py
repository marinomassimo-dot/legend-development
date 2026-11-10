"""IT41: relation-driven search, compound view table and rendered pages. New behaviours only."""
import csv, re, sys, unittest
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = HERE.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import repurposing_view as rv  # noqa: E402

def tsv(p): return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))

class Search(unittest.TestCase):
    def test_every_relation_row_yields_source_rows_and_nothing_is_ranked(self):
        rel = tsv(HERE / "relations_it41.tsv"); rows = tsv(HERE / "search_rows.tsv")
        for r in rel: self.assertTrue(any(x["relation_id"] == r["relation_id"] for x in rows), r["relation_id"])
        self.assertNotIn("score", rows[0]); self.assertNotIn("rank", rows[0])

    def test_s1_separates_what_the_symbol_lookup_would_mix(self):
        s1 = [r for r in tsv(HERE / "search_rows.tsv") if r["relation_id"] == "S1"]
        names = {r["name"] for r in s1}
        self.assertTrue({"RADIPRODIL", "onfasprodil", "NP10679"} <= names)
        gt = [r for r in s1 if r["source"] == "GtoPdb interaction"]
        self.assertGreater(sum(1 for r in gt if "glutamate site" in r["site_or_granularity"] or "glycine site" in r["site_or_granularity"]), 10, "orthosteric ligands are present and must not be read as ifenprodil-site NAMs")
        dq = [r for r in s1 if r["name"] == "DQP-1105"]
        self.assertTrue(dq and "GluN2C" in dq[0]["assay_or_note"], "a row filed under GluN2B whose assay was on GluN2C")

class CompoundView(unittest.TestCase):
    def test_kinds_order_and_editions(self):
        full, share = rv.compound_view(DR, True), rv.compound_view(DR, False)
        self.assertEqual([c["order"] for c in full], sorted({c["order"] for c in full}))
        self.assertEqual(len(full), len(share))
        self.assertTrue(all(c["kind"] in rv.COMPOUND_KINDS for c in full))
        self.assertTrue(all("name_full" in c and "registry_note" in c for c in full))
        self.assertFalse(any("name_full" in c or "registry_note" in c for c in share))
        self.assertTrue({"emerged", "known_requalified", "probe", "control", "weakened", "unresolved"} <= {c["kind"] for c in full})

    def test_no_forced_top_five_and_no_efficacy_claim(self):
        full = rv.compound_view(DR, True)
        self.assertNotEqual(len(full), 5)
        for c in full: self.assertNotRegex(" ".join(c[k] for k in rv.COMPOUND_TEXT), r"(?i)most effective|best (drug|compound)|recommend")

class ReaderConsumption(unittest.TestCase):
    def test_comparison_rows_and_identity_join_are_produced_by_calling_the_reader(self):
        import consume_reader as cr
        cr.main()
        rows = tsv(HERE / "comparison_rows_it41.tsv")
        self.assertTrue({"C1", "C2", "C3", "H_total_gain"} <= {r["key"] for r in rows})
        j = tsv(HERE / "compound_identity_join.tsv")
        g = [r for r in j if r["name"] == "GYKI 52466"]
        self.assertTrue(g and all(r["label_conflict"] == "yes" for r in g), "the label conflict travels with the name")
        self.assertTrue(any(r["name"] == "radiprodil" and r["identity_state"] == "NO_IDENTITY_ROW" for r in j), "a name without a row is stated, not dropped")

class Rendered(unittest.TestCase):
    def test_pages(self):
        n = 0
        for p in sorted((DR / "view").glob("index*.html")):
            h = p.read_text(encoding="utf-8"); n += 1
            self.assertEqual(len(re.findall(r'class="cv-i ', h)), 10, p.name)
            names = len(re.findall(r'class="cv-name"', h))
            self.assertEqual(names > 0, not p.name.startswith("index_shareable"), p.name)
        self.assertEqual(n, 10)

if __name__ == "__main__":
    unittest.main(verbosity=2)
