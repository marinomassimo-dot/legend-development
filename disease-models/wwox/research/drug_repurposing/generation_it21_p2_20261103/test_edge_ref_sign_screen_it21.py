#!/usr/bin/env python3
"""Offline tests of the IT21 F1 edge-reference sign screen: sentence rules on synthetic fixtures, label logic, efetch parsing, and the result tables
(closed label and status vocabulary, no status upgrade, every non-empty label carries its quoted sentence, depth stated, no e-mail string).
  test_edge_ref_sign_screen_it21.py     run all
Standard library only; no network."""
import csv, re, sys, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import edge_ref_sign_screen_it21 as S  # noqa: E402

OUT = HERE / "results" / "edge_ref_screen"
LABELS = {"SUPPORTS", "OPPOSES", "SPLIT", "NO_ABSTRACT_EVIDENCE"}
STATUS = {"CONDITIONAL_H_HARM", "CONDITIONAL_H_PROTECT", "CLOSED_AS_WRITTEN"}


def tsv(p):
    with open(p, newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


class Sentences(unittest.TestCase):
    def sg(self, s, a, b):
        return S.sentence_sign(s, a, b)[0]

    def test_direct_up_and_down(self):
        self.assertEqual(self.sg("EZH2 increased expression of IL-6 in macrophages.", "EZH2", "IL6"), 1)
        self.assertEqual(self.sg("SIRT1 decreased c-Myc stability.", "SIRT1", "MYC"), -1)

    def test_loss_flips(self):
        self.assertEqual(self.sg("Knockdown of EZH2 reduced IL-6 secretion.", "EZH2", "IL6"), 1)
        self.assertEqual(self.sg("EZH2 knockdown increased IL-6 expression.", "EZH2", "IL6"), -1)

    def test_prevents_activation_is_negative(self):
        self.assertEqual(self.sg("BTK prevents activation of STAT3.", "BTK", "STAT3"), -1)

    def test_negation_and_order_and_no_cue(self):
        self.assertEqual(self.sg("EZH2 did not change IL-6 levels.", "EZH2", "IL6"), 0)
        self.assertEqual(self.sg("IL-6 increased EZH2 in cells.", "EZH2", "IL6"), 0)
        self.assertEqual(self.sg("EZH2 and IL-6 were measured.", "EZH2", "IL6"), 0)

    def test_passive_by_regulator(self):
        self.assertEqual(self.sg("IL-6 expression was increased by EZH2.", "EZH2", "IL6"), 1)

    def test_last_clause_only(self):
        self.assertEqual(self.sg("Knockdown of HDAC5 increased GLUT4 but reduced GLUT1 expression.", "HDAC5", "SLC2A1"), 1)


class Labels(unittest.TestCase):
    def test_four_labels(self):
        up, dn = [(1, "s", "r")], [(-1, "s", "r")]
        self.assertEqual(S.label(1, {"1": up})[0], "SUPPORTS")
        self.assertEqual(S.label(1, {"1": dn})[0], "OPPOSES")
        self.assertEqual(S.label(1, {"1": up, "2": dn})[0], "SPLIT")
        self.assertEqual(S.label(1, {})[0], "NO_ABSTRACT_EVIDENCE")
        self.assertEqual(S.label(-1, {"1": up})[0], "OPPOSES")

    def test_chain(self):
        self.assertEqual(S.chain_label(["SUPPORTS", "OPPOSES"]), "OPPOSED")
        self.assertEqual(S.chain_label(["SUPPORTS", "SPLIT"]), "SPLIT")
        self.assertEqual(S.chain_label(["SUPPORTS", "SUPPORTS"]), "CLEAR")
        self.assertEqual(S.chain_label(["SUPPORTS", "NO_ABSTRACT_EVIDENCE"]), "UNSCREENED_PARTLY")


class Parsing(unittest.TestCase):
    def test_path(self):
        self.assertEqual(S.parse_edges("MAPK3 -P(-)-> BRD4 [SIGNOR]; BRD4 -T(+)-> TNF [CollecTRI;CollecTRI2]"),
                         [("MAPK3", "BRD4", "P", -1), ("BRD4", "TNF", "T", 1)])

    def test_refs(self):
        self.assertEqual(S.refs_of([{"references": "CollecTRI:12907458;CollecTRI2:15465827;SIGNOR:12907458;X:abc"}]), ["12907458", "15465827"])

    def test_efetch(self):
        xml = (b"<S><PubmedArticle><MedlineCitation><PMID>1</PMID><Article><ArticleTitle>T</ArticleTitle><Abstract><AbstractText>A b.</AbstractText></Abstract>"
               b"<PublicationTypeList><PublicationType>Review</PublicationType></PublicationTypeList></Article></MedlineCitation></PubmedArticle></S>")
        d = S.parse_efetch(xml)
        self.assertEqual(d["1"]["abstract"], "A b.")
        self.assertIn("Review", d["1"]["types"])

    def test_run_screen_on_fixture(self):
        recs = {"EZH2>IL6": [{"references": "CollecTRI:11111;CollecTRI:12222"}]}
        ab = {"11111": {"title": "T", "abstract": "EZH2 increased IL-6 expression.", "types": []},
              "12222": {"title": "T", "abstract": "Knockdown of EZH2 increased IL-6 expression.", "types": []}}
        rows, q = S.run_screen(recs, ab, [("X", "EZH2", "IL6", "T", 1)])
        self.assertEqual(rows[0]["label"], "SPLIT")
        self.assertEqual({x["side"] for x in q}, {"SUPPORT", "OPPOSE"})


class Tables(unittest.TestCase):
    def test_vocab_and_no_upgrade(self):
        hand = {r["proposal_id"]: r["status"] for r in tsv(S.HANDOFF)}
        rows = tsv(OUT / "dispositions_remaining7.tsv")
        self.assertEqual({r["proposal_id"][-4:] for r in rows}, set(S.REMAINING))
        for r in rows:
            self.assertIn(r["status_after"], STATUS)
            self.assertEqual(r["status_before"], hand[r["proposal_id"]])
            if r["status_after"] != r["status_before"]:
                self.assertEqual(r["status_after"], "CLOSED_AS_WRITTEN")
                self.assertEqual(r["chain_screen"], "OPPOSED")
                self.assertEqual(r["alternative_arm_left"], "no")
            self.assertIn("no full text read", r["depth"])

    def test_labels_closed_and_quotes_present(self):
        for f in ("edge_screen_remaining7.tsv", "edge_screen_p4a6.tsv"):
            rows = tsv(OUT / f)
            q = tsv(OUT / f.replace("edge_screen_", "edge_screen_quotes_"))
            for r in rows:
                self.assertIn(r["label"], LABELS)
                self.assertIn("not a read", r["depth"])
                n = sum(1 for x in q if x["edge"] == r["edge"] and x["proposal_id"] == r["proposal_id"])
                if r["label"] != "NO_ABSTRACT_EVIDENCE":
                    self.assertGreater(n, 0, r["edge"])
                else:
                    self.assertEqual(n, 0)

    def test_validation_reports_the_miss(self):
        v = tsv(OUT / "validation_p4a_edges.tsv")
        self.assertTrue(all(r["outcome"] in {"TP", "TN", "FP", "FN", "NOT_SCORED"} for r in v))
        self.assertTrue(any(r["outcome"] == "FN" for r in v), "the miss is reported, not removed")

    def test_no_email_string(self):
        for p in list(OUT.glob("*.tsv")) + [HERE / "edge_ref_sign_screen_it21.py"]:
            self.assertIsNone(re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}", p.read_text()), p.name)


if __name__ == "__main__":
    unittest.main()
