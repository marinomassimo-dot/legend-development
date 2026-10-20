#!/usr/bin/env python3
"""Offline tests for pubmed_identity_check.verdict (the pure comparison)."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pubmed_identity_check as m


class Verdict(unittest.TestCase):
    def test_hybrid_record_is_title_mismatch(self):
        pm = {"pmid": "31145772", "doi": "10.18388/abp.2020_5563", "first_author": "Permana",
              "title": "East Asian Genome-wide association study derived loci in relation to type 2 diabetes in the Han Chinese population."}
        cr = {"first_author": "Permana", "title": "The combination therapy of targeting both paclitaxel and Dendrophthoe pentandra leaves extract nanoparticles for improvement breast cancer treatment efficacy by reducing TUBB3 and MAP4 expressions"}
        self.assertEqual(m.verdict(pm, cr)["verdict"], "TITLE_MISMATCH")

    def test_consistent_record_matches(self):
        pm = {"pmid": "33520443", "doi": "10.7717/peerj.10604", "first_author": "Baryla",
              "title": "Identification of a novel association for the WWOX/HIF1A axis with gestational diabetes mellitus (GDM)."}
        cr = {"first_author": "Baryla", "title": "Identification of a novel association for the WWOX/HIF1A axis with gestational diabetes mellitus (GDM)"}
        self.assertEqual(m.verdict(pm, cr)["verdict"], "MATCH")

    def test_same_title_other_first_author(self):
        pm = {"pmid": "1", "doi": "10.1/x", "first_author": "Smith", "title": "Glucose transport in neurons and glia"}
        cr = {"first_author": "Jones", "title": "Glucose transport in neurons and glia"}
        self.assertEqual(m.verdict(pm, cr)["verdict"], "AUTHOR_MISMATCH")

    def test_missing_inputs_are_not_a_pass(self):
        self.assertEqual(m.verdict({"pmid": "1", "doi": None, "title": "t"}, None)["verdict"], "NO_DOI")
        self.assertEqual(m.verdict({"pmid": "1", "doi": "10.1/x", "title": "t"}, None)["verdict"], "CROSSREF_UNAVAILABLE")

    def test_doi_comes_from_the_article_not_its_reference_list(self):
        xml = ("<PubmedArticleSet><PubmedArticle><MedlineCitation><Article>"
               "<ArticleTitle>Own title</ArticleTitle>"
               "<AuthorList><Author><LastName>Hong</LastName></Author></AuthorList>"
               "</Article></MedlineCitation><PubmedData><ArticleIdList>"
               "<ArticleId IdType=\"doi\">10.1186/own</ArticleId></ArticleIdList>"
               "<ReferenceList><Reference><ArticleIdList>"
               "<ArticleId IdType=\"doi\">10.1016/cited</ArticleId>"
               "</ArticleIdList></Reference></ReferenceList></PubmedData>"
               "</PubmedArticle></PubmedArticleSet>")
        orig = m._get
        m._get = lambda url, *a, **k: xml
        try:
            self.assertEqual(m.fetch_pubmed("1")["doi"], "10.1186/own")
        finally:
            m._get = orig

if __name__ == "__main__":
    unittest.main(verbosity=2)
