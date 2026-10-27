#!/usr/bin/env python3
"""scout_daily: baseline selects nothing, no change is silent, a change or a new PMID is selected."""
import json
import tempfile
import unittest
from pathlib import Path

import scout_daily as sd

WATCH = [{"id": "Tool", "kind": "gh", "repo": "o/r", "q": "q?", "vs": "v"},
         {"id": "Acc", "kind": "url", "url": "https://x/ACC", "q": "q?", "vs": "v"},
         {"id": "Db", "kind": "json", "url": "https://x/s", "path": ["v"], "q": "q?", "vs": "v"}]
QUERIES = [("a", "WWOX")]


def make_opener(tag="v1", lic="MIT", acc=401, ver="X_1"):
    def opener(url, method="GET", body=None, etag=None):
        if url.endswith("/releases?per_page=1"):
            return 200, {"ETag": "W/1"}, json.dumps([{"tag_name": tag}]).encode()
        if url.endswith("/repos/o/r"):
            return 200, {}, json.dumps({"license": {"spdx_id": lic}, "archived": False}).encode()
        if url.endswith("/ACC"):
            return acc, {}, b""
        return 200, {}, json.dumps({"v": ver}).encode()
    return opener


def pm(ids):
    def opener(url):
        if "esearch" in url:
            return 200, json.dumps({"esearchresult": {"idlist": ids}}).encode()
        return 200, json.dumps({"result": {i: {"title": f"title {i}"} for i in ids}}).encode()
    return opener


def go(state, **kw):
    ids = kw.pop("ids", ["1", "2"])
    return sd.run(state, WATCH, QUERIES, make_opener(**kw), pm(ids))


class Radar(unittest.TestCase):
    def test_baseline_then_silence_then_changes(self):
        report, state = go({})
        self.assertEqual(("BASELINE", []), (report["verdict"], report["selected"]))
        report, state2 = go(state)
        self.assertEqual("NO_USEFUL_CHANGE", report["verdict"])
        report, _ = go(state2, tag="v2", lic="GPL-3.0", acc=200, ver="X_2", ids=["3", "1", "2"])
        self.assertEqual("SELECTED", report["verdict"])
        by_id = {s["id"]: s for s in report["selected"]}
        self.assertEqual({"Tool", "Acc", "Db", "PubMed:a"}, set(by_id))
        self.assertIn("'MIT' -> 'GPL-3.0'", by_id["Tool"]["detail"])  # licence change is visible
        self.assertIn("401", by_id["Acc"]["detail"])
        self.assertTrue(by_id["PubMed:a"]["detail"].startswith("3 title 3"))

    def test_error_keeps_last_good_fingerprint_and_never_selects(self):
        _, state = go({})
        report, state2 = sd.run(state, WATCH, QUERIES, lambda *a, **k: (500, {}, b""), pm(["1", "2"]))
        self.assertEqual("NO_USEFUL_CHANGE", report["verdict"])
        self.assertEqual(3, len(report["errors"]))
        self.assertEqual(state["watch"], state2["watch"])

    def test_no_contact_parameter_in_pubmed_urls(self):
        urls = []
        def opener(url):
            urls.append(url)
            return 200, json.dumps({"esearchresult": {"idlist": []}}).encode()
        sd.run({}, [], QUERIES, make_opener(), opener)
        self.assertTrue(urls and not any(p in u for u in urls for p in ("email=", "tool=", "api_key=")))

    def test_pending_entry_and_append_log(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            item = {"id": "Tool", "wwox_question": "q?", "contribution_vs_existing": "v", "detail": "d",
                    "estimated_cost": "c", "licence": "MIT", "proof": "p", "outcome": "TO_TRIAGE"}
            (directory / "scout_daily_pending_log.md").write_text(sd.entry_markdown(item, "2026-10-27T05:20:00"))
            log = directory / "log.md"
            log.write_text("# log\n")
            sd.append_log(directory, log)
            self.assertIn("## 2026-10-27 · scout_daily · Tool", log.read_text())
            self.assertFalse((directory / "scout_daily_pending_log.md").exists())


class RelevantResource(unittest.TestCase):
    """Each probe observes the resource whose change matters; availability is not a capability."""

    def opener(self, hf_card="c1", hf_license=None, explorer=503, commit="2024-05-06T00:00:00Z"):
        def opener(url, method="GET", body=None, etag=None):
            if "huggingface.co/api/datasets/o/d/tree" in url:
                return 200, {}, json.dumps([{"path": "README.md", "oid": hf_card}]).encode()
            if "huggingface.co/api/datasets/o/d" in url:
                card = {"license": hf_license} if hf_license else {}
                return 200, {}, json.dumps({"cardData": card, "tags": [], "gated": False}).encode()
            if url == "https://explorer.example":
                return explorer, {}, b""
            if url.endswith("/releases?per_page=1"):
                return 200, {}, b"[]"
            if "/commits?" in url:
                return 200, {}, json.dumps([{"commit": {"committer": {"date": commit}}}]).encode()
            if url.endswith("/repos/o/r"):
                return 200, {}, json.dumps({"license": {"spdx_id": "MIT"}, "default_branch": "main"}).encode()
            return 404, {}, b""
        return opener

    WATCH = [{"id": "Data", "kind": "hf", "repo": "o/d", "q": "licence stated?", "vs": "v"},
             {"id": "Explorer", "kind": "avail", "url": "https://explorer.example", "signal": "availability",
              "q": "up?", "vs": "v"},
             {"id": "Repo", "kind": "gh", "repo": "o/r", "q": "changed?", "vs": "v"}]

    def test_data_licence_explorer_status_and_commit_are_the_signals(self):
        report, state = sd.run({}, self.WATCH, [], self.opener(), pm([]))
        self.assertEqual("BASELINE", report["verdict"])
        self.assertIsNone(state["watch"]["Data"]["fp"]["license"])
        self.assertFalse(state["watch"]["Explorer"]["fp"]["reachable"])
        self.assertEqual("2024-05-06T00:00:00Z", state["watch"]["Repo"]["fp"]["last_commit"])
        report, state = sd.run(state, self.WATCH, [], self.opener(explorer=503), pm([]))
        self.assertEqual("NO_USEFUL_CHANGE", report["verdict"], "a still-down explorer is silence")
        report, _ = sd.run(state, self.WATCH, [], self.opener(hf_card="c2", hf_license="cc-by-4.0", explorer=200,
                                                              commit="2026-10-27T00:00:00Z"), pm([]))
        by_id = {x["id"]: x for x in report["selected"]}
        self.assertEqual({"Data", "Explorer", "Repo"}, set(by_id))
        self.assertIn("'cc-by-4.0'", by_id["Data"]["detail"])
        self.assertTrue(by_id["Explorer"]["outcome"].startswith("AVAILABILITY SIGNAL"))
        self.assertTrue(by_id["Repo"]["outcome"].startswith("TO_TRIAGE"))

    def test_a_redefined_fingerprint_rebaselines_instead_of_reporting_a_change(self):
        state = {"watch": {"Data": {"fp": {"status": 200, "etag": "x"}}}, "pubmed": {}}
        report, _ = sd.run(state, self.WATCH[:1], [], self.opener(), pm([]))
        self.assertEqual("BASELINE", report["watch"][0]["result"])
        self.assertEqual([], report["selected"])


class Discovery(unittest.TestCase):
    THEMES = [{"id": "t1", "gap": "gap one", "epmc": "WWOX", "gh": "q"},
              {"id": "t2", "gap": "gap two", "epmc": None, "gh": "q2"}]
    NOW = sd.dt.datetime(2026, 10, 27, tzinfo=sd.dt.timezone.utc)

    @staticmethod
    def opener(url, method="GET", body=None, etag=None):
        if "europepmc" in url:
            recs = [{"source": "MED", "id": str(n), "title": f"<i>t{n}</i> &amp; x", "firstPublicationDate": "2026-01-01"}
                    for n in range(6)]
            return 200, {}, json.dumps({"resultList": {"result": recs}}).encode()
        items = [{"full_name": f"o/r{n}", "stargazers_count": n, "html_url": "u", "pushed_at": "2026-01-01T00:00:00Z",
                  "license": None} for n in range(5)]
        return 200, {}, json.dumps({"items": items}).encode()

    def test_rotation_once_a_day_dedup_and_cap(self):
        result, st = sd.discover({}, self.THEMES, self.opener, self.NOW)
        self.assertEqual("t1", result["themes"][0]["theme"])
        self.assertEqual(2 * sd.SHOW, result["new_items"])
        self.assertEqual("t0 & x", result["themes"][0]["items"][0]["title"])  # markup and entities removed
        self.assertIsNone(sd.discover(st, self.THEMES, self.opener, self.NOW)[0], "one search per calendar day")
        later = self.NOW + sd.dt.timedelta(days=1)
        result2, st2 = sd.discover(st, self.THEMES, self.opener, later)
        self.assertEqual("t2", result2["themes"][0]["theme"])
        result3, _ = sd.discover(st2, self.THEMES, self.opener, later + sd.dt.timedelta(days=1))
        self.assertEqual("t1", result3["themes"][0]["theme"])
        self.assertEqual(3, result3["new_items"], "shown items are not shown again; the unshown epmc remainder surfaces")

    def test_failure_is_reported_not_raised_and_empty_is_valid(self):
        result, _ = sd.discover({}, self.THEMES, lambda *a, **k: (403, {}, b""), self.NOW)
        self.assertEqual(0, result["new_items"])
        self.assertTrue(result["themes"][0]["errors"])
        self.assertEqual([], sd.discovery_entries(result, "2026-10-27"))

    def test_radar_status_is_information(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            self.assertEqual("NO_REPORT", sd.radar_status(d)["status"])
            (d / "scout_daily.json").write_text(json.dumps({"run_at": "2026-10-27T05:20:01+00:00", "verdict": "SELECTED",
                                                            "errors": ["x"], "selected": [{"id": "A"}]}))
            (d / "scout_daily_pending_log.md").write_text("\n## one\n\n## two\n")
            info = sd.radar_status(d, sd.dt.datetime(2026, 10, 28, 5, 20, tzinfo=sd.dt.timezone.utc))
            self.assertEqual(("OK", ["A"], 2), (info["status"], info["to_examine"], info["pending_log_entries"]))
            stale = sd.radar_status(d, sd.dt.datetime(2026, 10, 30, tzinfo=sd.dt.timezone.utc))
            self.assertEqual("STALE", stale["status"])
            self.assertIn("RADAR STALE", sd.status_line(stale))


if __name__ == "__main__":
    unittest.main(verbosity=2)
