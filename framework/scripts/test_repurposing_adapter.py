#!/usr/bin/env python3
"""Regressions for the repurposing adapter seam (framework/adapters/ + repurposing_adapter.py).

Offline: every case runs through canned responses. The live measurement of each adapter is done
by hand with `selftest --live` and recorded with its date in the task record, because a
regression that needs six external services up is a regression that gets disabled.

Properties pinned:
  1. discovery is the directory listing — no registration anywhere;
  2. removing each adapter in turn leaves the CLI and every other adapter green (one-file removal);
  3. every shipped adapter's offline selftest is green and its output meets the convention;
  4. `add` writes a loadable module that passes the contract check; `remove` deletes only that file;
  5. a QUERY_ERROR, a NO_MATCH_FOUND and a MATCH_FOUND stay three different states, and
     NO_MATCH_FOUND carries the "never absence" note;
  6. no output hit carries a score/rank/probability/belief key.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repurposing_adapter as ra  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
CLI = ROOT / "framework" / "scripts" / "repurposing_adapter.py"
ADAPTERS = ROOT / "framework" / "adapters"


def cli(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(CLI), *args], capture_output=True, text=True, cwd=cwd)


class Discovery(unittest.TestCase):
    def test_population_is_the_directory_listing(self):
        names = ra.discover(ADAPTERS)
        on_disk = sorted(p.stem for p in ADAPTERS.glob("*.py") if not p.name.startswith("_"))
        self.assertEqual(names, on_disk)
        self.assertGreaterEqual(len(names), 1)
        self.assertNotIn("_http", names)

    def test_list_prints_every_adapter(self):
        done = cli("list")
        self.assertEqual(done.returncode, 0, done.stderr)
        for name in ra.discover(ADAPTERS):
            self.assertIn(name, done.stdout)


class ShippedAdapters(unittest.TestCase):
    def test_every_adapter_selftest_is_green_offline(self):
        for name in ra.discover(ADAPTERS):
            with self.subTest(adapter=name):
                report = ra.run_selftest(name, ADAPTERS, live=False)
                self.assertTrue(report.get("ok"), report)

    def test_every_adapter_output_meets_the_convention(self):
        for name in ra.discover(ADAPTERS):
            with self.subTest(adapter=name):
                module = ra.load(name, ADAPTERS)
                self.assertEqual(ra.check_info(module), [], name)
                self.assertEqual(module.INFO["name"], name)
                self.assertRegex(module.INFO["licence_read_on"], r"^\d{4}-\d{2}-\d{2}$")
                self.assertTrue(module.INFO["licence_url"].startswith("http"))
                result = module.query(module.SAMPLE["request"], fetch=lambda *a, **k: ra._sample_response(module))
                self.assertEqual(ra.check_output(result), [], name)
                self.assertEqual(result["licence"], module.INFO["licence"])
                self.assertEqual(result["citation"], module.INFO["citation"])

    def test_no_record_carries_an_email_address(self):
        for path in list(ADAPTERS.glob("*.py")) + [ra.DEFAULT_ACK]:
            self.assertNotRegex(path.read_text(encoding="utf-8"), r"[\w.+-]+@[\w-]+\.[\w.]+", path.name)


class Acknowledgements(unittest.TestCase):
    def test_committed_file_matches_the_adapters(self):
        self.assertTrue(ra.DEFAULT_ACK.exists(), ra.DEFAULT_ACK)
        self.assertEqual(ra.DEFAULT_ACK.read_text(encoding="utf-8"), ra.render_acknowledgements(ADAPTERS),
                         "ACKNOWLEDGEMENTS.md is stale: run repurposing_adapter.py acknowledgements --write")

    def test_every_adapter_has_a_section_with_licence_and_citation(self):
        text = ra.render_acknowledgements(ADAPTERS)
        for name in ra.discover(ADAPTERS):
            module = ra.load(name, ADAPTERS)
            self.assertIn(f"## {name}", text)
            self.assertIn(module.INFO["citation"], text)
            self.assertIn(module.INFO["licence_url"].split(" ")[0], text)
        self.assertIn("grateful", text)

    def test_remove_rerenders_the_list_without_the_removed_adapter(self):
        tmp = Path(tempfile.mkdtemp(prefix="ack_"))
        try:
            work = tmp / "adapters"
            shutil.copytree(ADAPTERS, work, ignore=shutil.ignore_patterns("__pycache__"))
            victim = ra.discover(work)[0]
            done = cli("--dir", str(work), "remove", victim)
            self.assertEqual(done.returncode, 0, done.stderr)
            rendered = (work / "ACKNOWLEDGEMENTS.md").read_text(encoding="utf-8")
            self.assertNotIn(f"## {victim}", rendered)
            for other in ra.discover(work):
                self.assertIn(f"## {other}", rendered)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_transport_failure_is_query_error_with_text(self):
        for name in ra.discover(ADAPTERS):
            with self.subTest(adapter=name):
                module = ra.load(name, ADAPTERS)
                result = module.query(module.SAMPLE["request"], fetch=lambda *a, **k: (0, "URLError: name resolution"))
                self.assertEqual(result["status"], "QUERY_ERROR")
                self.assertIn("URLError", result["error"])
                self.assertEqual(ra.check_output(result), [])

    def test_empty_request_is_query_error_not_no_match(self):
        for name in ra.discover(ADAPTERS):
            with self.subTest(adapter=name):
                module = ra.load(name, ADAPTERS)
                result = module.query({}, fetch=lambda *a, **k: (200, {}))
                self.assertEqual(result["status"], "QUERY_ERROR")
                self.assertTrue(result["error"])


class OneFileRemoval(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="adapters_"))
        self.dir = self.tmp / "adapters"
        shutil.copytree(ADAPTERS, self.dir, ignore=shutil.ignore_patterns("__pycache__"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_removing_each_adapter_in_turn_leaves_the_rest_green(self):
        names = ra.discover(self.dir)
        self.assertGreaterEqual(len(names), 2)
        for victim in names:
            with self.subTest(removed=victim):
                work = self.tmp / f"minus_{victim}"
                shutil.copytree(self.dir, work)
                done = cli("--dir", str(work), "remove", victim)
                self.assertEqual(done.returncode, 0, done.stderr)
                self.assertFalse((work / f"{victim}.py").exists())
                remaining = sorted(set(names) - {victim})
                self.assertEqual(ra.discover(work), remaining)
                done = cli("--dir", str(work), "selftest")
                self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
                self.assertIn(f"{len(remaining)} adapter(s), 0 red", done.stdout)
                for other in remaining:  # the other adapter files are byte-identical: nothing else was edited by hand
                    self.assertEqual((work / f"{other}.py").read_bytes(), (self.dir / f"{other}.py").read_bytes())

    def test_add_writes_a_loadable_module_and_remove_deletes_only_it(self):
        before = {p.name: p.read_bytes() for p in self.dir.glob("*.py")}
        done = cli("--dir", str(self.dir), "add", "example_source")
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertIn("example_source", ra.discover(self.dir))
        report = ra.run_selftest("example_source", self.dir, live=False)
        # The template loads and runs, but is red until its licence fields are filled from the
        # source's own terms page: an unfilled adapter is never green.
        self.assertFalse(report.get("ok"), report)
        self.assertTrue(any("placeholder" in p for p in report.get("contract_problems", [])), report)
        self.assertIn("## example_source", (self.dir / "ACKNOWLEDGEMENTS.md").read_text(encoding="utf-8"))
        done = cli("--dir", str(self.dir), "remove", "example_source")
        self.assertEqual(done.returncode, 0, done.stderr)
        after = {p.name: p.read_bytes() for p in self.dir.glob("*.py")}
        self.assertEqual(before, after)
        self.assertNotIn("## example_source", (self.dir / "ACKNOWLEDGEMENTS.md").read_text(encoding="utf-8"))

    def test_add_refuses_a_private_or_existing_name(self):
        self.assertEqual(cli("--dir", str(self.dir), "add", "_private").returncode, 2)
        self.assertEqual(cli("--dir", str(self.dir), "add", ra.discover(self.dir)[0]).returncode, 2)


class ThreeStates(unittest.TestCase):
    def test_pubtator_empty_list_is_no_match_with_the_note(self):
        module = ra.load("pubtator3", ADAPTERS)
        result = module.query({"gene": "WWOX", "type": "treat"}, fetch=lambda *a, **k: (200, []))
        self.assertEqual(result["status"], "NO_MATCH_FOUND")
        self.assertIn("never absence", result["note"])
        self.assertEqual(result["hits"], [])

    def test_openfda_404_is_no_match_not_error(self):
        module = ra.load("openfda", ADAPTERS)
        result = module.query({"drug": "amlexanox"}, fetch=lambda *a, **k: (404, {"error": {"code": "NOT_FOUND"}}))
        self.assertEqual(result["status"], "NO_MATCH_FOUND")
        self.assertEqual(result["error"], "")

    def test_server_error_is_query_error(self):
        module = ra.load("opentargets", ADAPTERS)
        result = module.query({"ensembl_id": "ENSG00000186153"}, fetch=lambda *a, **k: (503, "down"))
        self.assertEqual(result["status"], "QUERY_ERROR")
        self.assertIn("503", result["error"])

    def test_opentargets_drops_the_association_score(self):
        module = ra.load("opentargets", ADAPTERS)
        result = module.query(module.SAMPLE["request"], fetch=lambda *a, **k: module.SAMPLE["response"])
        self.assertNotIn("score", json.dumps(result["hits"]).lower())

    def test_contract_check_flags_a_score_key(self):
        bad = {"adapter": "x", "retrieved_at": "t", "request": {}, "requests_sent": [], "status": "MATCH_FOUND",
               "hits": [{"score": 0.9}], "source_version": "UNKNOWN", "evidence_label": "NOT WWOX EVIDENCE",
               "licence": "CC0; key-less", "citation": "x", "note": "never absence", "error": ""}
        self.assertTrue(any("score" in p for p in ra.check_output(bad)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
