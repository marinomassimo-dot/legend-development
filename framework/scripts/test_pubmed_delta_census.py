#!/usr/bin/env python3
"""Regressions for `pubmed_delta_census.py`: no network, fixture answers, three exit statuses."""
import io
import json
import os
import tempfile
import unittest
import urllib.error
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

import pubmed_delta_census as pdc

ANSWER = b"""<?xml version="1.0"?><eSearchResult><Count>3</Count><RetMax>3</RetMax>
<IdList><Id>40000001</Id><Id>40000002</Id><Id>1234567</Id></IdList></eSearchResult>"""

LONG_TITLE = "A preprint about the WWOX gene and a splice allele in a developmental model"


def make_root(tmp: str, text: str, name: str = "registries/paper.md") -> Path:
    root = Path(tmp)
    path = root / "disease-models" / "wwox" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return root


def no_summary(ids):
    return {pmid: {"title": "", "doi": ""} for pmid in ids}


def run(root: Path, fetcher, *extra: str, summariser=no_summary) -> tuple[int, str]:
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        code = pdc.main(["--root", str(root), "--no-wox1-probe", *extra],
                        fetcher=fetcher, summariser=summariser)
    return code, buffer.getvalue()


class Response:
    def __init__(self, data: bytes):
        self.data = data

    def read(self) -> bytes:
        return self.data

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class Tokenisation(unittest.TestCase):
    def test_the_labelled_forms_the_repository_writes(self):
        text = ("PMID 12345678 and PMID: 2345678; PMIDs 3456789, 4567890 and 5678901. "
                "https://pubmed.ncbi.nlm.nih.gov/6789012/ done")
        self.assertEqual(pdc.tokens(text), {"12345678", "2345678", "3456789", "4567890",
                                            "5678901", "6789012"})

    def test_a_bare_number_is_not_a_pmid(self):
        self.assertEqual(pdc.tokens("accession 12345678, n = 7654321, 2026"), set())

    def test_the_pmid_column_of_a_tsv_is_read_apart(self):
        self.assertEqual(pdc.column_pmids("pmid\tyear\n11111111\t2000\nx\t1\n22222222\t2001\n"),
                         {"11111111", "22222222"})
        self.assertEqual(pdc.column_pmids("id\tyear\n11111111\t2000\n"), set())


class TheQueries(unittest.TestCase):
    def test_the_standing_term_is_wwox_only_and_the_probe_removes_the_plant_genes(self):
        self.assertNotIn("WOX1", pdc.STANDING_TERM)
        self.assertIn("WWOX", pdc.STANDING_TERM)
        self.assertIn("WW domain-containing oxidoreductase", pdc.STANDING_TERM)
        self.assertIn("WOX1", pdc.WOX1_PROBE)
        self.assertIn("oxidoreductase", pdc.WOX1_PROBE)


class TheDelta(unittest.TestCase):
    def test_true_misses_are_listed_and_exit_1(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "cited PMID 40000001 only")
            code, out = run(root, lambda term: {"40000001", "40000002", "1234567"})
            self.assertEqual(code, pdc.EXIT_NEW)
            self.assertIn("true misses (no PMID, DOI or title in the repository): 2", out)
            self.assertIn("40000002", out)
            self.assertNotIn("    40000001 ", out)
            self.assertIn("Nothing was written", out)

    def test_nothing_new_is_exit_0(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "PMIDs 40000001, 40000002 and 1234567")
            code, out = run(root, lambda term: {"40000001", "40000002", "1234567"}, "--json")
            self.assertEqual(code, pdc.EXIT_NONE)
            report = json.loads(out)
            self.assertEqual((report["status"], report["new_count"]), ("NO_NEW_RECORDS", 0))

    def test_a_preprint_registered_by_doi_before_its_pmid_is_a_false_absent_not_a_miss(self):
        info = {"40000001": {"title": LONG_TITLE, "doi": "10.1101/2026.01.02.123456"},
                "40000002": {"title": "A different title of sufficient length to be compared", "doi": ""}}
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "Preprint, doi:10.1101/2026.01.02.123456, registered as CORPUS.")
            code, out = run(root, lambda term: {"40000001", "40000002"}, "--json",
                            summariser=lambda ids: {i: info[i] for i in ids})
            report = json.loads(out)
        self.assertEqual(report["new_pmids"], ["40000002"])
        self.assertEqual([(r["pmid"], r["via"]) for r in report["false_absent"]],
                         [("40000001", ["doi"])])
        self.assertEqual(code, pdc.EXIT_NEW)

    def test_a_record_registered_by_normalised_title_is_a_false_absent(self):
        info = {"40000001": {"title": LONG_TITLE + ".", "doi": ""}}
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "Listed as: " + LONG_TITLE.upper().replace(" ", "  "))
            code, out = run(root, lambda term: {"40000001"}, "--json",
                            summariser=lambda ids: {i: info[i] for i in ids})
        report = json.loads(out)
        self.assertEqual(code, pdc.EXIT_NONE)
        self.assertEqual(report["false_absent"][0]["via"], ["title"])

    def test_a_short_title_never_matches(self):
        info = {"40000001": {"title": "WWOX", "doi": ""}}
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "WWOX is everywhere in this file")
            code, out = run(root, lambda term: {"40000001"}, "--json",
                            summariser=lambda ids: {i: info[i] for i in ids})
        self.assertEqual(json.loads(out)["new_pmids"], ["40000001"])

    def test_a_seed_only_row_is_apart_from_absent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "pmid\ttitle\n40000002\tx\n", "registries/corpus_seed.tsv")
            code, out = run(root, lambda term: {"40000001", "40000002"}, "--json")
            report = json.loads(out)
            self.assertEqual(report["new_pmids"], ["40000001"])
            self.assertEqual(report["seed_only_pmids"], ["40000002"])
            self.assertEqual(code, pdc.EXIT_NEW)

    def test_the_probe_is_reported_apart_and_never_changes_the_exit_status(self):
        answers = {pdc.STANDING_TERM: {"40000001"}, pdc.WOX1_PROBE: {"40000001", "40000009"}}
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "PMID 40000001")
            buffer = io.StringIO()
            with redirect_stdout(buffer):
                code = pdc.main(["--root", str(root), "--json"],
                                fetcher=lambda term: answers[term], summariser=no_summary)
            report = json.loads(buffer.getvalue())
        self.assertEqual(code, pdc.EXIT_NONE)
        self.assertEqual(report["wox1_probe"]["new_pmids"], ["40000009"])
        self.assertEqual(report["wox1_probe"]["returned"], 1)

    def test_the_term_override_reaches_the_fetcher_and_the_default_is_the_constant(self):
        seen = []
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "")
            run(root, lambda term: seen.append(term) or set(), "--term", "WWOX AND 2026[dp]")
            run(root, lambda term: seen.append(term) or set())
        self.assertEqual(seen, ["WWOX AND 2026[dp]", pdc.STANDING_TERM])

    def test_a_failed_route_is_exit_3_and_makes_no_claim(self):
        def broken(term):
            raise pdc.RouteFailed("offline")
        with tempfile.TemporaryDirectory() as tmp:
            code, out = run(make_root(tmp, ""), broken)
        self.assertEqual(code, pdc.EXIT_ROUTE_FAILED)
        self.assertIn("No claim about the delta is made", out)
        self.assertNotIn("true misses", out)

    def test_the_tool_writes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp, "")
            before = sorted(str(p) for p in root.rglob("*"))
            run(root, lambda term: {"40000001"})
            self.assertEqual(sorted(str(p) for p in root.rglob("*")), before)


class TheTransport(unittest.TestCase):
    def test_the_requests_carry_no_email_and_no_key_whatever_the_environment_holds(self):
        summary = json.dumps({"result": {"uids": ["40000001"], "40000001": {
            "title": "t", "articleids": [{"idtype": "doi", "value": "10.1/x"}]}}}).encode()
        with mock.patch.dict(os.environ, {"NCBI_EMAIL": "contact-token-for-the-test",
                                          "NCBI_API_KEY": "secret-key"}):
            seen = []

            def fake(url, timeout=0):
                seen.append(url)
                return Response(summary if "esummary" in url else ANSWER)
            self.assertEqual(pdc.fetch_pmids("WWOX", fake, lambda s: None),
                             {"40000001", "40000002", "1234567"})
            self.assertEqual(pdc.fetch_summaries(["40000001"], fake, lambda s: None),
                             {"40000001": {"title": "t", "doi": "10.1/x"}})
        self.assertEqual(len(seen), 2)
        for url in seen:
            for forbidden in ("email", "contact-token", "api_key", "secret"):
                self.assertNotIn(forbidden, url.lower())
        self.assertIn("retmax=10000", seen[0])
        self.assertNotIn("efetch", " ".join(seen))

    def test_a_503_then_an_answer_is_retried_with_a_pause(self):
        calls, pauses = [], []

        def flaky(url, timeout=0):
            calls.append(1)
            if len(calls) == 1:
                raise urllib.error.HTTPError(url, 503, "busy", {}, None)
            return Response(ANSWER)
        self.assertEqual(len(pdc.fetch_pmids("WWOX", flaky, pauses.append)), 3)
        self.assertEqual(len(calls), 2)
        self.assertTrue(pauses and pauses[0] >= 1)

    def test_a_400_is_reported_at_once(self):
        calls = []

        def refused(url, timeout=0):
            calls.append(1)
            raise urllib.error.HTTPError(url, 400, "bad", {}, None)
        with self.assertRaises(pdc.RouteFailed):
            pdc.fetch_pmids("WWOX", refused, lambda s: None)
        self.assertEqual(len(calls), 1)

    def test_a_count_that_disagrees_with_the_ids_is_a_failed_route(self):
        short = b"<eSearchResult><Count>5</Count><IdList><Id>40000001</Id></IdList></eSearchResult>"
        with self.assertRaises(pdc.RouteFailed):
            pdc.parse_esearch(short)

    def test_an_error_element_and_a_non_xml_answer_are_failed_routes(self):
        with self.assertRaises(pdc.RouteFailed):
            pdc.parse_esearch(b"<eSearchResult><ERROR>Invalid query</ERROR></eSearchResult>")
        with self.assertRaises(pdc.RouteFailed):
            pdc.parse_esearch(b"<html>gateway timeout")

    def test_more_than_the_ceiling_is_refused_not_truncated(self):
        big = b"<eSearchResult><Count>10001</Count><IdList></IdList></eSearchResult>"
        with self.assertRaises(pdc.RouteFailed):
            pdc.parse_esearch(big)

    def test_an_esummary_that_misses_an_id_or_is_not_json_is_a_failed_route(self):
        with self.assertRaises(pdc.RouteFailed):
            pdc.parse_esummary(b'{"result": {"uids": []}}', ["40000001"])
        with self.assertRaises(pdc.RouteFailed):
            pdc.parse_esummary(b"not json", ["40000001"])


class TheEntryPoint(unittest.TestCase):
    def test_the_real_repository_is_readable_with_fixture_answers(self):
        code, out = run(Path(__file__).resolve().parents[2], lambda term: {"1", "99999999"})
        self.assertIn(code, (pdc.EXIT_NONE, pdc.EXIT_NEW))
        self.assertIn("PUBMED DELTA CENSUS", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
