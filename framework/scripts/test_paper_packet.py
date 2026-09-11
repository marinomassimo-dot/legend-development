#!/usr/bin/env python3
"""Regressions for `paper_packet.py` — and the firewall is the first of them.

The packet exists to save a reading the lookups it was doing by re-reading registries into its
own context. The risk that buys is precise and it is named in `scientist_reading_modes.md` § 3.1
and § 3.3: a packet that also carried the laboratory's conclusions would be cheaper AND
contaminating. So the first test does not check a feature; it checks an absence, against the real
workspace, using the real claim text.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import paper_packet as pp  # noqa: E402

LIVE_PMID = "29724996"   # complete read, 15 artefacts present, two receipts
PARTIAL_PMID = "20146584"  # partial read, figures captions_only, failed acquisition routes


class TheFirewallHolds(unittest.TestCase):
    """No claim, dossier, commit candidate, prior locator or interpretation reaches the packet."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.packet = pp.build(ROOT, "wwox", LIVE_PMID)
        cls.serialised = json.dumps(cls.packet, ensure_ascii=False)

    def test_no_claim_title_appears_in_the_packet(self) -> None:
        registry = (ROOT / "disease-models/wwox/registries/claim_registry_current.md").read_text(
            encoding="utf-8")
        titles = [line.split("**Title:**", 1)[1].strip()
                  for line in registry.splitlines() if line.startswith("**Title:**")]
        self.assertGreater(len(titles), 10, "the fixture needs real claim titles to look for")
        for title in titles:
            self.assertNotIn(title, self.serialised)

    def test_no_locator_proposition_from_the_manifest_appears(self) -> None:
        """The prior reading's propositions are its conclusions; coverage is not."""
        manifest = json.loads(pp.manifest_path(ROOT, "wwox", LIVE_PMID).read_text(encoding="utf-8"))
        entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
        self.assertGreater(len(entries), 5, "the fixture needs real locators to look for")
        for entry in entries:
            proposition = str(entry.get("proposition") or "")
            if len(proposition) > 40:
                self.assertNotIn(proposition[:40], self.serialised)

    def test_the_dossier_is_never_opened(self) -> None:
        dossier = ROOT / f"disease-models/wwox/research/fulltext_dossiers/PMID{LIVE_PMID}.md"
        if dossier.is_file():
            for line in dossier.read_text(encoding="utf-8").splitlines():
                if len(line.strip()) > 60:
                    self.assertNotIn(line.strip()[:60], self.serialised)

    def test_the_forbidden_list_names_the_surfaces_that_carry_conclusions(self) -> None:
        joined = " ".join(pp.FORBIDDEN_SOURCES)
        for surface in ("claim_registry_current", "fulltext_dossiers", "commit_candidates",
                        "working_model_current", "discovery_ledger_current"):
            self.assertIn(surface, joined)
        self.assertEqual(list(pp.FORBIDDEN_SOURCES), self.packet["excludes"])

    def test_the_packet_declares_its_own_firewall(self) -> None:
        self.assertIn("scientist_reading_modes", self.packet["firewall"])


class ThePacketCarriesTheTechnicalState(unittest.TestCase):
    def test_a_complete_read_reports_its_depth_and_receipts(self) -> None:
        packet = pp.build(ROOT, "wwox", LIVE_PMID)
        self.assertEqual("complete_fulltext_read", packet["prior_reading"]["depth"])
        self.assertGreaterEqual(len(packet["prior_reading"]["receipts"]), 1)
        self.assertEqual("ok", packet["prior_reading"]["chain"])

    def test_a_partial_read_names_the_sections_a_resume_owes(self) -> None:
        packet = pp.build(ROOT, "wwox", PARTIAL_PMID)
        self.assertEqual("partial_fulltext_read", packet["prior_reading"]["depth"])
        self.assertTrue([item for item in packet["prior_reading"]["uncovered"]
                         if item.startswith("figures=")], packet["prior_reading"])

    def test_a_settled_section_is_not_reported_as_owed(self) -> None:
        """`read` and `not_present` are settled; reporting them would be noise on every resume."""
        packet = pp.build(ROOT, "wwox", PARTIAL_PMID)
        owed = " ".join(packet["prior_reading"]["uncovered"])
        self.assertNotIn("=read", owed)
        self.assertNotIn("=not_present", owed)

    def test_artefact_digests_are_verified_not_quoted(self) -> None:
        packet = pp.build(ROOT, "wwox", LIVE_PMID)
        declared = [row for row in packet["artefacts"] if row["declared"] and row["present"]]
        self.assertTrue(declared)
        self.assertTrue(all(row["digest"] in {"match", "MISMATCH", ""} for row in declared))
        self.assertIn("match", {row["digest"] for row in declared})

    def test_a_declared_route_that_never_ran_is_not_reported_as_a_failure(self) -> None:
        """The retrieval ledger holds back-fill declarations and replay verdicts; the packet
        must not print '(no verdict)' over a route that was declared and never replayed."""
        packet = pp.build(ROOT, "wwox", PARTIAL_PMID)
        verdicts = {row["verdict"] for row in packet["acquisition_history"]}
        self.assertTrue(verdicts)
        self.assertNotIn("", verdicts)
        self.assertTrue(any(v.startswith("declared, never replayed") for v in verdicts), verdicts)
        self.assertTrue(any("FAILED" in v or "RECOVERED" in v for v in verdicts), verdicts)

    def test_applicable_checks_follow_the_surfaces_that_exist(self) -> None:
        packet = pp.build(ROOT, "wwox", LIVE_PMID)
        names = {check["name"] for check in packet["applicable_checks"]}
        self.assertIn("manifest validator", names)
        self.assertIn("undeclared locator revision", names)

    def test_a_pmid_the_workspace_knows_nothing_about_exits_2(self) -> None:
        self.assertEqual(2, pp.main(["packet", "--pmid", "99999999", "--root", str(ROOT)]))

    def test_a_malformed_pmid_is_refused(self) -> None:
        with self.assertRaises(SystemExit):
            pp.main(["packet", "--pmid", "not-a-pmid", "--root", str(ROOT)])

    def test_the_cli_renders_and_the_json_is_the_same_object(self) -> None:
        done = subprocess.run(
            [sys.executable, str(HERE / "paper_packet.py"), "packet", "--pmid", LIVE_PMID,
             "--root", str(ROOT), "--json"], capture_output=True, text=True)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual("paper_work_packet", json.loads(done.stdout)["record_kind"])


class TheStateOfAFinishedCheck(unittest.TestCase):
    """Unit cases on the classifier, because the integration case can be vacuous.

    Found by mutation: forcing every state to `ok` left the live-corpus test green, since it
    only asserted a property of the reach limits it happened to find. A guard that cannot fail
    proves nothing, so the rule is pinned here where it cannot depend on the corpus.
    """

    def test_exit_zero_is_ok(self) -> None:
        self.assertEqual(("ok", "VERDICT: PASS"), pp.classify(0, "VERDICT: PASS", "VERDICT: PASS"))

    def test_a_non_zero_without_insufficient_data_is_a_refusal(self) -> None:
        state, line = pp.classify(1, "VERDICT: REVIEW_REQUIRED — a locator stands on a corrected panel",
                                  "VERDICT: REVIEW_REQUIRED — a locator stands on a corrected panel")
        self.assertEqual("refused", state)
        self.assertIn("REVIEW_REQUIRED", line)

    def test_a_reach_limit_is_named_apart_and_carries_its_missing_clause(self) -> None:
        output = ("[INSUFFICIENT_DATA] manifest_flag_drift (34607B) missing=a second revision of "
                  "PMID20146584.json to compare against. This is not a pass.")
        state, line = pp.classify(2, output, "VERDICT: INSUFFICIENT_DATA — nothing was screened.")
        self.assertEqual("nothing-to-screen", state)
        self.assertIn("a second revision", line)
        self.assertNotIn("VERDICT:", line)

    def test_a_reach_limit_is_never_reported_as_a_pass(self) -> None:
        state, _line = pp.classify(2, "INSUFFICIENT_DATA: screened nothing", "x")
        self.assertNotEqual("ok", state)


class TheChecksRunInOneCall(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.out = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_one_call_produces_one_line_per_check_and_a_detail_file(self) -> None:
        report = pp.run_checks(ROOT, "wwox", PARTIAL_PMID, out_dir=self.out)
        self.assertGreaterEqual(report["calls"], 3)
        self.assertEqual(report["calls"], len(report["results"]))
        detail = self.out / f"PMID{PARTIAL_PMID}.txt"
        self.assertEqual(str(detail), report["detail"])
        self.assertTrue(detail.is_file())
        self.assertGreater(len(detail.read_text(encoding="utf-8")), 500,
                           "the full output must reach disk, not the caller's context")

    def test_a_reach_limit_and_a_refusal_are_printed_apart_and_neither_is_a_pass(self) -> None:
        """MF-6's rule, kept: INSUFFICIENT_DATA is not a pass. But a flag-drift check that
        exits 2 on every single-revision manifest must not train a reader to ignore reds."""
        report = pp.run_checks(ROOT, "wwox", PARTIAL_PMID, out_dir=self.out)
        states = {row["state"] for row in report["results"]}
        self.assertTrue(states <= {"ok", "nothing-to-screen", "refused"}, states)
        rendered = pp.render_checks(report)
        void = [row for row in report["results"] if row["state"] == "nothing-to-screen"]
        if void:
            self.assertIn("established nothing (not a pass)", rendered)
            self.assertNotIn("ok " + void[0]["check"], rendered)

    def test_a_reach_limit_carries_its_reason_so_the_detail_file_stays_shut(self) -> None:
        report = pp.run_checks(ROOT, "wwox", PARTIAL_PMID, out_dir=self.out)
        for row in report["results"]:
            if row["state"] == "nothing-to-screen":
                self.assertGreater(len(row["headline"]), 30, row)
                self.assertNotIn("VERDICT:", row["headline"])

    def test_the_run_reports_calls_and_seconds(self) -> None:
        report = pp.run_checks(ROOT, "wwox", PARTIAL_PMID, out_dir=self.out)
        self.assertIsInstance(report["seconds"], float)
        self.assertGreater(report["seconds"], 0)

    def test_the_checks_write_nothing_into_the_repository(self) -> None:
        """A preparation step that mutates tracked state is not a preparation step."""
        before = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"],
                                capture_output=True, text=True).stdout
        pp.run_checks(ROOT, "wwox", PARTIAL_PMID, out_dir=self.out)
        after = subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"],
                               capture_output=True, text=True).stdout
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main(verbosity=2)
