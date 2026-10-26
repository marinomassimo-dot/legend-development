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


if __name__ == "__main__":
    unittest.main(verbosity=2)
