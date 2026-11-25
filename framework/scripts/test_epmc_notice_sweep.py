#!/usr/bin/env python3
"""Offline tests for epmc_notice_sweep.py: partial-date comparison and the receipt index (no network)."""
from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import epmc_notice_sweep as m  # noqa: E402


class DateTests(unittest.TestCase):
    def test_post_pre_between(self):
        self.assertEqual(m.compare("2026-11-20", "2026-07-26", "2026-08-06"), "POST")
        self.assertEqual(m.compare("2026-07-17", "2026-07-26", "2026-08-06"), "PRE")
        self.assertEqual(m.compare("2026-08-01", "2026-07-26", "2026-08-06"), "BETWEEN")

    def test_partial_dates_compare_at_their_own_precision(self):
        self.assertEqual(m.compare("2012 May", "2026-11-07", "2026-11-07"), "PRE")
        self.assertEqual(m.compare("2026 Nov", "2026-11-04", "2026-11-04"), "SAME_DAY_OR_PERIOD")

    def test_unreadable_date_is_unknown_never_pre(self):
        self.assertEqual(m.compare("", "2026-11-07", "2026-11-07"), "UNKNOWN")
        self.assertEqual(m.compare("Oncogene.", "2026-11-07", "2026-11-07"), "UNKNOWN")


class ReferenceTests(unittest.TestCase):
    def test_citation_only_notice_gets_its_date(self):
        self.assertEqual(m.reference_date("Oncogene. 2006 Dec 7;25(58):7662"), "2006 Dec 7")
        self.assertEqual(m.reference_date("Nature.2014 Jul 17;511(7509):370"), "2014 Jul 17")
        self.assertEqual(m.reference_date("PLoS One. 2013;8(8). doi:10.1371/annotation/x"), "2013")
        self.assertEqual(m.compare(m.reference_date("Ann Oncol. 2015 Feb;26(2):445"), "2026-11-04", "2026-11-04"), "PRE")
        self.assertEqual(m.reference_date("no date here"), "")


class IndexTests(unittest.TestCase):
    def test_receipt_index_groups_by_pmid_and_skips_rows_without_one(self):
        rows = [{"event_at": "2026-08-06T11:30:00Z", "event_id": "A", "evidence_depth": "abstract_only", "study_id": {"pmid": "1"}},
                {"event_at": "2026-07-26T07:52:50+02:00", "event_id": "B", "evidence_depth": "partial_fulltext_read", "study_id": {"pmid": "1"}},
                {"event_at": "2026-07-26T07:52:50+02:00", "event_id": "C", "evidence_depth": "abstract_only", "study_id": {"doi": "10.1/x"}}]
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "l.jsonl"
            p.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
            idx = m.receipt_index(p)
        self.assertEqual(sorted(idx), ["1"])
        self.assertEqual(len(idx["1"]), 2)


# SCI's ADV-256 hits of 2026-11-25 (notice_hits.tsv: PMID, Europe PMC link type, notice PMID): 6 retracted, 2 with an expression of concern, 21 corrected.
ADV256_HITS = """\
19357348	Retraction in	42583763
23446842	Retraction in	42464650
25447306	Retraction in	32746981
26041563	Retraction in	32799870
28151481	Retraction in	35680840
32606933	Retraction in	38282791
12719539	Expression of concern in	28373549
16223882	Expression of concern in	28373548
26419537	Erratum in	26496836
38144875	Erratum in	38533474
39934240	Erratum in	40229390
41069084	Erratum in	42043325
41210171	Erratum in	42137596
42769206	Erratum in	42852004
16007179	Erratum in	-
24098343	Erratum in	-
29724996	Erratum in	30470736
30356099	Erratum in	30783266
30820047	Erratum in	31417202
31618474	Erratum in	32176372
32214227	Erratum in	34050322
33074286	Erratum in	33749757
33718178	Erratum in	34513711
37095367	Erratum in	39394494
37461096	Erratum in	37580755
38182577	Erratum in	38355659
40119223	Erratum in	42024171
40198927	Erratum in	40263068
40507943	Erratum in	41373918
"""


def adv256_records() -> dict[str, dict]:
    """The shape Europe PMC answers with, rebuilt from the fixture: one record per paper with its links, one per notice with a date."""
    core: dict[str, dict] = {}
    for pmid, link, notice in (line.split("\t") for line in ADV256_HITS.splitlines()):
        rec = core.setdefault(pmid, {"id": pmid, "commentCorrectionList": {"commentCorrection": []}})
        rec["commentCorrectionList"]["commentCorrection"].append({"type": link, "id": "" if notice == "-" else notice, "reference": "J. 2020 Jan 1"})
        if notice != "-":
            core.setdefault(notice, {"id": notice, "firstPublicationDate": "2026-01-01"})
    return core


def fake_fetch(core):
    def fetch(query):
        return [core[i] for i in query.split("EXT_ID:(")[1].rstrip(")").split(" OR ") if i in core]
    return fetch


class CatalogueTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.registries = Path(self.tmp.name) / "registries"
        self.state = Path(self.tmp.name) / "state"
        self.registries.mkdir()
        self.core = adv256_records()
        self.papers = sorted({line.split("\t")[0] for line in ADV256_HITS.splitlines()}, key=int)
        queue = "".join(f"| [{p}](https://pubmed.ncbi.nlm.nih.gov/{p}) | x |\n" for p in self.papers + ["11111111"])
        (self.registries / m.QUEUE).write_text(queue, encoding="utf-8")

    def run_once(self):
        return m.run_catalogue(self.state, self.registries, fetch=fake_fetch(self.core), pause=0)

    def test_the_first_run_reproduces_the_counts_of_adv256_and_is_a_baseline(self):
        summary = self.run_once()
        self.assertEqual(summary["counts"], {"retraction": 6, "concern": 2, "correction": 21})
        self.assertEqual((summary["baseline"], summary["new"], summary["new_flagged"]), (True, [], []))
        self.assertEqual(summary["not_indexed"], 1)
        self.assertTrue(any("19357348" in line and "42583763" in line for line in summary["proposed"]))
        self.assertTrue((self.state / "notices.tsv").read_text().startswith("pmid\tkind\tnotice_pmid\tnotice_date\n"))

    def test_a_later_retraction_is_new_and_flagged_a_later_correction_is_new_and_not_flagged(self):
        self.run_once()
        paper = self.papers[0]
        self.core[paper]["commentCorrectionList"]["commentCorrection"] += [{"type": "Retraction in", "id": "999", "reference": ""}, {"type": "Erratum in", "id": "998", "reference": ""}]
        summary = self.run_once()
        self.assertEqual(sorted(r[2] for r in summary["new"]), ["998", "999"])
        self.assertEqual([r[2] for r in summary["new_flagged"]], ["999"])
        again = self.run_once()
        self.assertEqual((again["new"], [r[2] for r in again["new_flagged"]]), ([], ["999"]))          # kept until a reader has seen it

    def test_a_stopped_sweep_writes_nothing(self):
        def refused(query):
            raise m.SweepStopped("HTTP 403")
        with self.assertRaises(m.SweepStopped):
            m.run_catalogue(self.state, self.registries, fetch=refused, pause=0)
        self.assertFalse(self.state.exists())

    def test_a_flag_the_repository_already_states_is_not_proposed_again(self):
        (self.registries / m.QUEUE).write_text("| [19357348](u) | RETRACTED 2026 |\n", encoding="utf-8")
        self.assertEqual(m.proposed_flags([("19357348", "retraction", "42583763", "2026-08-12"), ("2", "correction", "3", "-")], self.registries), [])

    def test_a_week_must_pass_before_the_next_run(self):
        self.assertTrue(m.due(self.state))
        self.run_once()
        self.assertFalse(m.due(self.state))
        self.assertTrue(m.due(self.state, now=m.dt.datetime.now(m.dt.timezone.utc) + m.dt.timedelta(days=7)))

    def test_429_is_waited_out_once_and_any_other_refusal_stops(self):
        waits = []

        def answering(codes):
            def opener(request, timeout):
                if codes:
                    raise m.urllib.error.HTTPError("u", codes.pop(0), "no", {"Retry-After": "5"}, None)
                return io.BytesIO(b'{"resultList": {"result": [{"id": "1"}]}}')
            return opener
        self.assertEqual(m.get("q", opener=answering([429]), sleep=waits.append), [{"id": "1"}])
        self.assertEqual(waits, [60])
        self.assertEqual(m.get("q", opener=answering([503]), sleep=waits.append), [{"id": "1"}])
        for codes in ([429, 429], [503, 503], [403]):
            with self.assertRaises(m.SweepStopped):
                m.get("q", opener=answering(list(codes)), sleep=waits.append)

    def test_a_request_with_no_answer_is_tried_once_more(self):
        waits, left = [], [TimeoutError("slow")]

        def opener(request, timeout):
            if left:
                raise left.pop(0)
            return io.BytesIO(b'{"resultList": {"result": []}}')
        self.assertEqual((m.get("q", opener=opener, sleep=waits.append), waits), ([], [30]))
        left[:] = [TimeoutError("a"), TimeoutError("b")]
        with self.assertRaises(m.SweepStopped):
            m.get("q", opener=opener, sleep=waits.append)

    @unittest.skipUnless(os.environ.get("LEGEND_NETWORK_TESTS") == "1", "network test: set LEGEND_NETWORK_TESTS=1")
    def test_live_europe_pmc_still_marks_the_six(self):
        six = ["19357348", "23446842", "25447306", "26041563", "28151481", "32606933"]
        rows, missing = m.catalogue_notices(six)
        self.assertEqual(({r[0] for r in rows if r[1] == "retraction"}, missing), (set(six), []))


if __name__ == "__main__":
    unittest.main(verbosity=2)
