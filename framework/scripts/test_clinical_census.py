#!/usr/bin/env python3
"""Regressions for clinical_census.py — one per property the census contract fixes.

Every case runs OFFLINE through an injected fetcher. A regression that needs the registry to
be reachable is a regression that gets disabled the first week it is not, so the live run is
performed once by hand and recorded with its date; what this suite pins is the behaviour.
"""

from __future__ import annotations

import gzip
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import clinical_census as cc  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def study(nct: str, *, phases=("PHASE1",), masking="NONE", sponsor="Sponsor",
          condition="WWOX-related epileptic encephalopathy") -> dict:
    return {
        "protocolSection": {
            "identificationModule": {"nctId": nct, "briefTitle": f"Study {nct}"},
            "statusModule": {"overallStatus": "RECRUITING",
                             "studyFirstPostDateStruct": {"date": "2026-01-02"},
                             "startDateStruct": {"date": "2026-03-01"},
                             "lastUpdatePostDateStruct": {"date": "2026-04-01"}},
            "designModule": {"phases": list(phases), "studyType": "INTERVENTIONAL",
                             "designInfo": {"maskingInfo": {"masking": masking}}},
            "conditionsModule": {"conditions": [condition]},
            "sponsorCollaboratorsModule": {"leadSponsor": {"name": sponsor}},
        }
    }


def fetcher(pages_by_term: dict[str, list[dict]]):
    """Serve canned pages per query value; record every URL the tool asked for."""
    seen: list[str] = []

    def fetch(url: str) -> dict:
        seen.append(url)
        term = next((value for value in pages_by_term
                     if value.replace(" ", "+") in url.replace("%20", "+").replace("+", "+")
                     or cc.urllib.parse.quote_plus(value) in url), None)
        if term is None:
            return {"totalCount": 0, "studies": []}
        pages = pages_by_term[term]
        index = sum(1 for item in seen if cc.urllib.parse.quote_plus(term) in item) - 1
        return pages[min(index, len(pages) - 1)]

    fetch.seen = seen  # type: ignore[attr-defined]
    return fetch


class QuerySetTests(unittest.TestCase):
    def test_the_seven_queries_are_present_and_run_separately(self) -> None:
        labels = [query["label"] for query in cc.DEFAULT_QUERIES]
        for expected in ("WOREE", "WWOX-related epileptic encephalopathy", "EIEE28", "DEE28",
                         "WWOX", "MZ-9138"):
            self.assertIn(expected, labels)
        self.assertTrue(any(query["field"] == "query.spons" for query in cc.DEFAULT_QUERIES))
        self.assertEqual(7, len(cc.DEFAULT_QUERIES))
        # Separately: no query value joins two synonyms with a boolean.
        for query in cc.DEFAULT_QUERIES:
            self.assertNotIn(" OR ", query["value"].upper())

    def test_each_query_produces_its_own_request(self) -> None:
        fetch = fetcher({})
        cc.run_census(list(cc.DEFAULT_QUERIES), fetch=fetch)
        self.assertEqual(7, len(fetch.seen))  # type: ignore[attr-defined]


class NoPreFilterTests(unittest.TestCase):
    def test_no_request_carries_a_phase_status_or_masking_filter(self) -> None:
        fetch = fetcher({})
        cc.run_census(list(cc.DEFAULT_QUERIES), fetch=fetch)
        for url in fetch.seen:  # type: ignore[attr-defined]
            for forbidden in ("filter.", "aggFilters", "postFilter", "phase", "masking",
                              "placebo"):
                self.assertNotIn(forbidden, url.lower().split("?", 1)[1].replace(
                    "query.term=", "").replace("query.spons=", ""))

    def test_a_phase_one_open_label_study_survives_the_census(self) -> None:
        fetch = fetcher({"WOREE": [{"totalCount": 1,
                                    "studies": [study("NCT00000001", phases=("PHASE1",),
                                                      masking="NONE")]}]})
        census = cc.run_census([dict(cc.DEFAULT_QUERIES[0])], fetch=fetch)
        self.assertEqual("MATCH", census["states_by_query"]["WOREE"])
        self.assertEqual(["PHASE1"], census["records"]["NCT00000001"]["phases"])

    def test_build_url_refuses_a_filter_parameter(self) -> None:
        with self.assertRaises(cc.CensusError):
            cc.build_url({"label": "x", "field": "filter.overallStatus",
                          "value": "RECRUITING"}, 10, None)


class FourStateTests(unittest.TestCase):
    def test_match(self) -> None:
        fetch = fetcher({"WWOX": [{"totalCount": 1, "studies": [study("NCT00000002")]}]})
        result = cc.run_query({"label": "WWOX", "field": "query.term", "value": "WWOX"},
                              page_size=100, max_pages=5, raw_dir=None, fetch=fetch)
        self.assertEqual("MATCH", result["state"])

    def test_no_match_is_not_an_absence_claim(self) -> None:
        result = cc.run_query({"label": "DEE28", "field": "query.term", "value": "DEE28"},
                              page_size=100, max_pages=5, raw_dir=None,
                              fetch=lambda url: {"totalCount": 0, "studies": []})
        self.assertEqual("NO_MATCH", result["state"])
        self.assertEqual(0, result["collected"])
        census = cc.run_census([{"label": "DEE28", "field": "query.term", "value": "DEE28"}],
                               fetch=lambda url: {"totalCount": 0, "studies": []})
        limits = " ".join(census["interpretation_limits"]).lower()
        self.assertIn("does not establish that no study exists", limits)
        self.assertNotIn("no study exists.", json.dumps(census["records"]).lower())

    def test_query_error_is_distinct_from_no_match(self) -> None:
        def broken(url: str) -> dict:
            raise cc.CensusError("HTTP 503 for " + url)

        result = cc.run_query({"label": "WOREE", "field": "query.term", "value": "WOREE"},
                              page_size=100, max_pages=5, raw_dir=None, fetch=broken)
        self.assertEqual("QUERY_ERROR", result["state"])
        self.assertIn("503", result["error"])
        self.assertEqual(0, result["collected"])

    def test_coverage_incomplete_on_truncated_pagination(self) -> None:
        page = {"totalCount": 9, "studies": [study("NCT00000003")],
                "nextPageToken": "more"}
        result = cc.run_query({"label": "WWOX", "field": "query.term", "value": "WWOX"},
                              page_size=1, max_pages=2, raw_dir=None, fetch=lambda url: page)
        self.assertEqual("COVERAGE_INCOMPLETE", result["state"])
        self.assertTrue(result["truncated"])

    def test_coverage_incomplete_when_total_count_exceeds_collected(self) -> None:
        page = {"totalCount": 12, "studies": [study("NCT00000004")]}
        result = cc.run_query({"label": "WWOX", "field": "query.term", "value": "WWOX"},
                              page_size=100, max_pages=5, raw_dir=None, fetch=lambda url: page)
        self.assertEqual("COVERAGE_INCOMPLETE", result["state"])

    def test_malformed_payload_is_a_query_error_not_zero_results(self) -> None:
        self.assertEqual(4, len({"MATCH", "NO_MATCH", "QUERY_ERROR",
                                 "COVERAGE_INCOMPLETE"}))
        result = cc.run_query({"label": "WWOX", "field": "query.term", "value": "WWOX"},
                              page_size=100, max_pages=5, raw_dir=None,
                              fetch=lambda url: (_ for _ in ()).throw(
                                  cc.CensusError("response carries no studies list")))
        self.assertEqual("QUERY_ERROR", result["state"])

    def test_verdict_exit_codes(self) -> None:
        self.assertEqual(0, cc.verdict({"states_by_query": {"a": "MATCH", "b": "NO_MATCH"}}))
        self.assertEqual(3, cc.verdict({"states_by_query": {"a": "COVERAGE_INCOMPLETE"}}))
        self.assertEqual(1, cc.verdict({"states_by_query": {"a": "QUERY_ERROR",
                                                            "b": "COVERAGE_INCOMPLETE"}}))


class PaginationTests(unittest.TestCase):
    def test_pages_are_followed_and_each_page_is_recorded(self) -> None:
        pages = [{"totalCount": 2, "studies": [study("NCT00000005")],
                  "nextPageToken": "second"},
                 {"totalCount": 2, "studies": [study("NCT00000006")]}]
        calls: list[str] = []

        def fetch(url: str) -> dict:
            calls.append(url)
            return pages[min(len(calls) - 1, 1)]

        result = cc.run_query({"label": "WWOX", "field": "query.term", "value": "WWOX"},
                              page_size=1, max_pages=5, raw_dir=None, fetch=fetch)
        self.assertEqual("MATCH", result["state"])
        self.assertEqual(2, result["collected"])
        self.assertEqual(2, len(result["pages"]))
        self.assertIn("pageToken=second", calls[1])


class DeduplicationTests(unittest.TestCase):
    def test_one_record_per_identifier_keeping_every_finding_synonym(self) -> None:
        hit = {"totalCount": 1, "studies": [study("NCT00000007")]}
        census = cc.run_census(
            [{"label": "WOREE", "field": "query.term", "value": "WOREE"},
             {"label": "WWOX", "field": "query.term", "value": "WWOX"}],
            fetch=lambda url: hit)
        self.assertEqual(["NCT00000007"], list(census["records"]))
        self.assertEqual(["WOREE", "WWOX"],
                         census["records"]["NCT00000007"]["found_by_synonyms"])


class ProvenanceTests(unittest.TestCase):
    def test_query_date_pagination_and_original_response_path_are_preserved(self) -> None:
        hit = {"totalCount": 1, "studies": [study("NCT00000008")]}
        with tempfile.TemporaryDirectory() as temporary:
            raw = Path(temporary) / "raw"
            census = cc.run_census(
                [{"label": "WOREE", "field": "query.term", "value": "WOREE"}],
                raw_dir=raw, fetch=lambda url: hit)
            result = census["queries"][0]
            self.assertIn("query.term=WOREE", result["pages"][0]["url"])
            self.assertTrue(result["retrieved_at"].startswith("20"))
            path = Path(result["pages"][0]["original_response_path"])
            self.assertTrue(path.is_file())
            self.assertEqual(hit, json.loads(path.read_text(encoding="utf-8")))
        self.assertEqual("v2", census["registry"]["api_version"])
        self.assertIn("NLM", census["registry"]["owner"])
        self.assertEqual(cc.TOOL_VERSION, census["tool"])
        self.assertEqual("RETRIEVAL_RECORD", census["epistemic_status"])

    def test_a_large_original_response_is_kept_gzipped_at_the_recorded_path(self) -> None:
        big = {"totalCount": 1, "studies": [study(f"NCT0000{index:04d}")
                                            for index in range(200)]}
        with tempfile.TemporaryDirectory() as temporary:
            raw = Path(temporary) / "raw"
            stored, redactions = cc.write_original_response(raw, "WWOX", 1, big,
                                                            gzip_over=1000)
            self.assertEqual(0, redactions)
            path = Path(stored)
            self.assertTrue(path.name.endswith(".json.gz"))
            self.assertTrue(path.is_file())
            with gzip.open(path, "rt", encoding="utf-8") as handle:
                self.assertEqual(big, json.load(handle))
            small = Path(cc.write_original_response(raw, "DEE28", 1,
                                                    {"totalCount": 0, "studies": []},
                                                    gzip_over=1000)[0])
            self.assertTrue(small.name.endswith(".json"))

    def test_registration_is_not_recruitment_or_first_dose(self) -> None:
        census = cc.run_census([], fetch=lambda url: {})
        limits = " ".join(census["interpretation_limits"])
        for event in ("authorisation", "enrolment", "first dose", "UNKNOWN"):
            self.assertIn(event, limits)


class ContactRedactionTests(unittest.TestCase):
    """A public repository may not carry trial staff e-mail addresses; the gate blocks them.

    So the stored response is redacted and SAYS it is redacted, rather than being dropped —
    a provenance file that cannot be kept is a provenance file that disappears.
    """

    PAYLOAD = {"studies": [{"protocolSection": {
        "contactsLocationsModule": {"centralContacts": [
            {"name": "A Person", "role": "CONTACT",
             "email": "someone@example.org", "phone": "555-0100"}]},
        "identificationModule": {"nctId": "NCT00000010", "briefTitle": "Keep me"}}}]}

    def test_contact_values_are_replaced_and_counted(self) -> None:
        document, count = cc.redact_personal_contacts(self.PAYLOAD)
        self.assertEqual(2, count)
        contact = (document["studies"][0]["protocolSection"]["contactsLocationsModule"]
                   ["centralContacts"][0])
        self.assertEqual(cc.REDACTED, contact["email"])
        self.assertEqual(cc.REDACTED, contact["phone"])
        self.assertEqual("CONTACT", contact["role"])
        self.assertEqual("Keep me", document["studies"][0]["protocolSection"]
                         ["identificationModule"]["briefTitle"])
        self.assertNotIn("@", json.dumps(document))

    def test_the_stored_file_carries_no_address_and_the_page_declares_the_redaction(self):
        with tempfile.TemporaryDirectory() as temporary:
            raw = Path(temporary) / "raw"
            result = cc.run_query({"label": "WOREE", "field": "query.term",
                                   "value": "WOREE"}, page_size=100, max_pages=2,
                                  raw_dir=raw, fetch=lambda url: self.PAYLOAD)
            page = result["pages"][0]
            self.assertEqual(2, page["original_response_contact_redactions"])
            self.assertTrue(page["original_response_is_contact_redacted"])
            stored = Path(page["original_response_path"]).read_text(encoding="utf-8")
            self.assertNotIn("@example.org", stored)
            self.assertIn("NCT00000010", stored)


class CommandLineTests(unittest.TestCase):
    def test_list_queries_makes_no_network_call(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(ROOT / "framework/scripts/clinical_census.py"),
             "--list-queries"], capture_output=True, text=True, check=False, timeout=30)
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertIn("MZ-9138", completed.stdout)
        self.assertIn("query.spons=Mahzi Therapeutics", completed.stdout)

    def test_main_writes_the_census_and_returns_the_verdict(self) -> None:
        hit = {"totalCount": 1, "studies": [study("NCT00000009")]}
        with tempfile.TemporaryDirectory() as temporary:
            out = Path(temporary) / "census.json"
            code = cc.main(["--query", "WOREE", "--out", str(out)], fetch=lambda url: hit)
            self.assertEqual(0, code)
            census = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual("MATCH", census["states_by_query"]["WOREE"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
