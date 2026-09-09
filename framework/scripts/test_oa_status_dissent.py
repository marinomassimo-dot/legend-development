#!/usr/bin/env python3
"""Regressions for oa_status_dissent.py.

Every case below is anchored to a real measurement or to a defect the tool must not have.
The first is the case that motivated the tool and is reproduced from the 2026-09-09
wave-3 reading of PMID 24510053; the rest are the ways a crude name comparison can go
wrong, which is the only interesting part of the logic.
"""

import unittest

import oa_status_dissent as M


def assess(doi, publisher, prefix_owner, **cr):
    crossref = {"publisher": publisher, "container_title": cr.get("title"),
                "licence_urls": cr.get("licence_urls", []), "link_urls": []}
    return M.assess(doi, fetcher=lambda _d: crossref, prefix_fetcher=lambda _p: prefix_owner)


class TheMotivatingCase(unittest.TestCase):
    """PMID 24510053 / 10.1177/1535370213519213, measured 2026-09-09."""

    def test_sage_prefix_frontiers_publisher_is_flagged(self):
        r = assess("10.1177/1535370213519213", "Frontiers Media SA", "SAGE Publications",
                   title="Experimental Biology and Medicine",
                   licence_urls=["http://journals.sagepub.com/page/policies/text-and-data-mining-license"])
        self.assertEqual(r["verdict"], M.VERDICT_MIGRATION)
        self.assertEqual(r["doi_prefix"], "10.1177")
        self.assertIn("Frontiers", r["explanation"])
        self.assertIn("NOT evidence of a paywall", r["explanation"])

    def test_the_licence_url_still_names_the_old_publisher(self):
        """The licence host lags too — so it must never be used as the migration signal."""
        r = assess("10.1177/1535370213519213", "Frontiers Media SA", "SAGE Publications",
                   licence_urls=["http://journals.sagepub.com/page/policies/x"])
        self.assertEqual(r["verdict"], M.VERDICT_MIGRATION)
        self.assertIn("sagepub", r["licence_urls"][0])


class NameComparison(unittest.TestCase):
    def test_corporate_suffix_differences_are_not_a_migration(self):
        for owner, current in [
            ("SAGE Publications", "SAGE Publications Ltd"),
            ("Elsevier BV", "Elsevier"),
            ("Springer Science and Business Media LLC", "Springer Science & Business Media"),
            ("Wiley", "Wiley-Blackwell"),
        ]:
            with self.subTest(owner=owner):
                r = assess("10.1000/x", current, owner)
                self.assertEqual(r["verdict"], M.VERDICT_CONSISTENT,
                                 "%r vs %r must not be flagged" % (owner, current))

    def test_genuinely_different_publishers_are_flagged(self):
        for owner, current in [
            ("SAGE Publications", "Frontiers Media SA"),
            ("Wiley", "Oxford University Press"),
            ("Karger Publishers", "Springer Science and Business Media LLC"),
        ]:
            with self.subTest(owner=owner):
                r = assess("10.1000/x", current, owner)
                self.assertEqual(r["verdict"], M.VERDICT_MIGRATION)

    def test_missing_data_is_undetermined_not_consistent(self):
        """🔴 The dangerous default. Absent data must never read as 'no migration'."""
        self.assertEqual(assess("10.1000/x", None, "SAGE")["verdict"], M.VERDICT_UNKNOWN)
        self.assertEqual(assess("10.1000/x", "SAGE", None)["verdict"], M.VERDICT_UNKNOWN)
        self.assertEqual(assess("10.1000/x", "", "")["verdict"], M.VERDICT_UNKNOWN)


class Contract(unittest.TestCase):
    def test_prefix_is_parsed_not_guessed(self):
        self.assertEqual(M.doi_prefix("10.1177/1535370213519213"), "10.1177")
        self.assertEqual(M.doi_prefix("10.1073/pnas.0400805101"), "10.1073")

    def test_a_non_doi_is_refused(self):
        with self.assertRaises(ValueError):
            assess("24510053", "X", "Y")
        with self.assertRaises(ValueError):
            assess("https://doi.org/10.1177/x", "X", "Y")

    def test_the_tool_never_claims_the_article_is_open(self):
        """The measurement supports 'the closed verdict is not evidence', and no more."""
        r = assess("10.1177/1535370213519213", "Frontiers Media SA", "SAGE Publications")
        blob = (r["explanation"] + M.render(r)).lower()
        for overclaim in ("is open access", "is freely available", "the article is free"):
            self.assertNotIn(overclaim, blob)

    def test_render_mentions_the_verdict(self):
        r = assess("10.1000/x", "Frontiers Media SA", "SAGE Publications")
        self.assertIn(M.VERDICT_MIGRATION, M.render(r))


if __name__ == "__main__":
    unittest.main(verbosity=2)
