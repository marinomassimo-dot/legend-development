#!/usr/bin/env python3
"""Regressions for oa_status_dissent.py.

Every case below is anchored to a real measurement or to a defect the tool must not have.
The first is the case that motivated the tool and is reproduced from the 2026-09-09
wave-3 reading of PMID 24510053; the rest are the ways a crude name comparison can go
wrong, which is the only interesting part of the logic.
"""

import csv
import hashlib
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

import oa_status_dissent as M

SCRIPT = pathlib.Path(__file__).with_name("oa_status_dissent.py")
ROOT = SCRIPT.resolve().parents[2]

#: A real, tracked corpus artefact: the PubMed corpus seed. The motivating DOI is read OUT of
#: it rather than retyped here — retrospective 9.4, "identifiers must come from the artefact".
CORPUS_SEED = ROOT / "disease-models" / "wwox" / "registries" / "corpus_seed_pubmed_20260705.tsv"
MOTIVATING_PMID = "24510053"


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




class TheVerdictNamesWhatItCompared(unittest.TestCase):
    """Retrospective 9.2: a verdict is a record carrying the digest of what was screened."""

    def screen(self, doi, publisher, prefix_owner, **cr):
        crossref = {"publisher": publisher, "container_title": cr.get("title"),
                    "licence_urls": cr.get("licence_urls", []), "link_urls": []}
        return M.screen(doi, fetcher=lambda _d: crossref,
                        prefix_fetcher=lambda _p: prefix_owner)

    def test_a_migration_is_refused_and_names_the_signature(self):
        verdict = self.screen("10.1177/1535370213519213", "Frontiers Media SA",
                              "SAGE Publications")
        self.assertEqual(verdict.verdict, "REFUSED")
        self.assertEqual(verdict.signature, "DOI_PREFIX_STALE")
        self.assertEqual(verdict.evidence["verdict"], M.VERDICT_MIGRATION)

    def test_agreement_is_clean_and_carries_a_digest(self):
        verdict = self.screen("10.1177/x", "SAGE Publications", "SAGE Publications")
        self.assertTrue(verdict.is_clean)
        self.assertTrue(verdict.digest.startswith("sha256:"))
        self.assertGreater(verdict.screened["bytes"], 0)

    def test_undetermined_is_insufficient_data_naming_the_absent_field(self):
        """🔴 The old wording said 'did not supply both' without saying which one."""
        missing_publisher = self.screen("10.1177/x", None, "SAGE Publications")
        self.assertTrue(missing_publisher.is_insufficient)
        self.assertIn("current publisher", missing_publisher.missing)
        self.assertNotIn("prefix owner", missing_publisher.missing)

        missing_owner = self.screen("10.1177/x", "SAGE Publications", None)
        self.assertTrue(missing_owner.is_insufficient)
        self.assertIn("prefix owner", missing_owner.missing)

        both = self.screen("10.1177/x", "", "")
        self.assertTrue(both.is_insufficient)
        self.assertIn("current publisher", both.missing)
        self.assertIn("prefix owner", both.missing)

    def test_a_pmid_handed_where_a_doi_belongs_is_insufficient_data(self):
        """A screen over the wrong KIND of identifier asserts nothing about the DOI."""
        for wrong in ("24510053", "https://doi.org/10.1177/x", "", None):
            with self.subTest(wrong=wrong):
                verdict = self.screen(wrong, "Frontiers", "SAGE")
                self.assertTrue(verdict.is_insufficient)
                self.assertEqual(verdict.missing, "a syntactically valid DOI")

    def test_the_digest_is_of_the_compared_fields_not_of_the_doi(self):
        """Two DOIs compared on identical publisher fields differ; the same fields agree."""
        one = self.screen("10.1177/a", "Frontiers Media SA", "SAGE Publications")
        two = self.screen("10.1177/a", "Frontiers Media SA", "SAGE Publications")
        other = self.screen("10.1177/a", "Wiley", "SAGE Publications")
        self.assertEqual(one.digest, two.digest)
        self.assertNotEqual(one.digest, other.digest)


class TheCommandLine(unittest.TestCase):
    """Nothing in this suite entered main() until 2026-09-10. No network: fixtures only."""

    def run_cli(self, *args):
        proc = subprocess.run([sys.executable, str(SCRIPT), *args],
                              capture_output=True, text=True)
        return proc.returncode, proc.stdout + proc.stderr

    def fixture(self, tmp, doi, publisher, prefix_owner):
        path = pathlib.Path(tmp) / "fx.json"
        path.write_text(json.dumps({
            "doi": doi, "prefix_owner": prefix_owner,
            "crossref": {"publisher": publisher, "container_title": "Journal",
                         "licence_urls": [], "link_urls": []}}), encoding="utf-8")
        return str(path)

    def test_the_cli_reports_the_verdict_and_its_digest(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = self.run_cli("--offline-fixture", self.fixture(
                tmp, "10.1177/1535370213519213", "Frontiers Media SA", "SAGE Publications"))
            self.assertEqual(code, 0)
            self.assertIn("[REFUSED]", out)
            self.assertIn("DOI_PREFIX_STALE", out)
            self.assertIn("sha256:", out)

    def test_the_cli_json_carries_both_the_verdict_and_the_domain_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = self.run_cli("--offline-fixture", self.fixture(
                tmp, "10.1177/x", "SAGE Publications", "SAGE Publications"), "--json")
            record = json.loads(out)
            # 🔴 Two vocabularies, and they must not collide: the screen verdict is CLEAN,
            # the domain assessment is PREFIX_CONSISTENT. An earlier version of this JSON
            # let the domain record overwrite `verdict`, so the tool reported a word the
            # screen contract never emits.
            self.assertEqual(record["verdict"], "CLEAN")
            self.assertEqual(record["assessment_verdict"], M.VERDICT_CONSISTENT)
            self.assertEqual(record["screen"], "oa_status_dissent")
            self.assertTrue(record["screened"]["digest"].startswith("sha256:"))
            self.assertEqual(record["doi_prefix"], "10.1177")
            self.assertEqual(code, 0)

    def test_an_absent_fixture_is_insufficient_data_and_exits_two(self):
        code, out = self.run_cli("--offline-fixture", "/nonexistent/fixture.json")
        self.assertEqual(code, 2)
        self.assertIn("[INSUFFICIENT_DATA]", out)

    def test_undetermined_exits_nonzero(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, out = self.run_cli("--offline-fixture", self.fixture(
                tmp, "10.1177/x", None, None))
            self.assertEqual(code, 1)
            self.assertIn("[INSUFFICIENT_DATA]", out)


class TheMotivatingCaseFromTheCorpus(unittest.TestCase):
    """A case drawn from a real corpus artefact, degrading to a declared skip when absent."""

    def test_the_doi_comes_from_the_corpus_seed_not_from_this_file(self):
        if not CORPUS_SEED.exists():
            self.skipTest(f"real artefact absent: {CORPUS_SEED.name}")
        with CORPUS_SEED.open(encoding="utf-8") as handle:
            row = next((r for r in csv.DictReader(handle, delimiter="\t")
                        if r.get("pmid") == MOTIVATING_PMID), None)
        self.assertIsNotNone(row, f"PMID {MOTIVATING_PMID} is not in the seed")
        doi = row["doi"].strip()

        crossref = {"publisher": "Frontiers Media SA", "container_title": row["title"],
                    "licence_urls": [], "link_urls": []}
        verdict = M.screen(doi, fetcher=lambda _d: crossref,
                           prefix_fetcher=lambda _p: "SAGE Publications")
        self.assertEqual(verdict.verdict, "REFUSED")
        self.assertEqual(verdict.evidence["doi_prefix"], "10.1177")
        # The digest is of the compared surface and is recomputable outside the tool.
        self.assertEqual(
            verdict.digest,
            "sha256:" + hashlib.sha256(
                M.screened_surface(verdict.evidence).encode("utf-8")).hexdigest())


if __name__ == "__main__":
    unittest.main(verbosity=2)
