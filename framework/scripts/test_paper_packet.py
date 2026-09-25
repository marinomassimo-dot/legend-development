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

import derived_inputs  # noqa: E402
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
        if not declared:
            # 🔴 THE ARTEFACTS LIVE UNDER `files/`, WHICH IS GITIGNORED. A fresh clone has the
            # manifest that declares them and none of the bytes, so this case cannot run and
            # is NOT thereby satisfied — the sibling wording in
            # `test_locator_obligation_reaches_every_route.py` is the precedent. What it would
            # verify is that a digest is COMPUTED rather than quoted, which needs the bytes.
            absent = [row["path"] for row in packet["artefacts"] if row["declared"]][:3]
            self.skipTest(
                f"no declared artefact is present in this checkout "
                f"(e.g. {', '.join(absent) or '(none declared)'}) — `files/` is gitignored, so "
                f"this case does not run in a fresh clone. It is skipped, never passed.")
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


class ThePacketNamesTheTreeItDescribes(unittest.TestCase):
    """Every other field is a fact about a file at a moment. Without the commit, a packet read
    back from a transcript cannot be tied to a checkout, and a reader cannot tell whether an
    artefact digest it quotes was computed against committed state or against somebody's
    uncommitted edit."""

    def test_the_packet_carries_the_commit_and_the_three_state_verdict(self) -> None:
        packet = pp.build(ROOT, "wwox", LIVE_PMID)
        block = packet["repository"]
        self.assertIn(block["verdict"],
                      (derived_inputs.BOUND, derived_inputs.DIRTY, derived_inputs.UNBOUND))
        self.assertRegex(block["commit"], r"^[0-9a-f]{40}$")

    def test_the_block_names_the_sources_the_packet_actually_read(self) -> None:
        packet = pp.build(ROOT, "wwox", LIVE_PMID)
        joined = " ".join(packet["repository"]["inputs"])
        self.assertIn(f"deepdive_manifests/PMID{LIVE_PMID}.json", joined)
        self.assertIn("fulltext_read_receipts.jsonl", joined)

    def test_the_commit_reaches_the_rendered_form_and_the_json(self) -> None:
        packet = pp.build(ROOT, "wwox", LIVE_PMID)
        self.assertIn("read at commit", pp.render(packet))
        done = subprocess.run(
            [sys.executable, str(ROOT / "framework/scripts/paper_packet.py"),
             "packet", "--pmid", LIVE_PMID, "--json"],
            capture_output=True, text=True, cwd=str(ROOT))
        self.assertRegex(json.loads(done.stdout)["repository"]["commit"], r"^[0-9a-f]{40}$")

    def test_naming_the_tree_did_not_breach_the_firewall(self) -> None:
        """The block carries PATHS, never CONTENT. A provenance field that quoted a registry
        line would smuggle a conclusion past `scientist_reading_modes.md` 3.1/3.3 — which is
        exactly the shape of mistake a 'harmless' envelope addition makes."""
        block = pp.build(ROOT, "wwox", LIVE_PMID)["repository"]
        for forbidden in pp.FORBIDDEN_SOURCES:
            self.assertNotIn(forbidden.format(disease="wwox").rstrip("/"),
                             json.dumps(block, ensure_ascii=False))

# --------------------------------------------------------------------------- procedures
#
# Expected states below were fixed BY HAND from the manifests and the disk listing on
# 2026-09-12 — `source_artifacts` paths and suffixes, `retraction_check` fields, locator entry
# counts, `files/` contents — before the selector ran on them. The selector is never the oracle.
#
#   29724996  XML+PDF present, 15 artefacts, ErratumIn (Fig 3A, 3D), 38 entries, supplement PDF
#   33914858  no manifest, no artefact on disk, three failed routes in the retrieval ledger
#   18460020  PDF+TXT only (no XML/HTML), CLEAN retraction_check, 34 entries
#   38499540  XML present, three .pptx on disk UNDECLARED, .docx declared, no notice
#   34268881  XML present, six binary containers ALL declared (xlsx as table, docx as text)
#   16223882  PDF only, 12 crops under page_adjudications/, ExpressionOfConcernIn, 26 entries

ERRATUM_PMID, ABSENT_PMID, PDF_ONLY_PMID = "29724996", "33914858", "18460020"
PPTX_PMID, DECLARED_BINARY_PMID, EOC_PMID = "38499540", "34268881", "16223882"


def _states(pmid: str, signals: set[str] | None = None, observed: set[str] | None = None) -> dict[str, dict]:
    facts = pp.build(ROOT, "wwox", pmid)["technical_facts"]
    return {row["key"]: row for row in pp.procedures(facts, signals, observed)}


class TheProceduresFollowTheFacts(unittest.TestCase):
    """Trigger present, trigger absent with sufficient data, data missing — kept apart."""

    def test_an_erratum_recorded_in_the_manifest_opens_the_integrity_procedure(self) -> None:
        row = _states(ERRATUM_PMID)["integrity_notice"]
        self.assertEqual(row["state"], pp.OPEN)
        self.assertIn("2 corrected item", row["reason"])
        self.assertTrue(any("erratum_scope_check.py" in f for f in row["files"]))

    def test_a_structured_surface_makes_page_adjudication_not_needed(self) -> None:
        self.assertEqual(_states(ERRATUM_PMID)["page_adjudication"]["state"], pp.NOT_NEEDED)

    def test_nothing_on_disk_opens_acquisition_and_leaves_the_rest_to_ascertain(self) -> None:
        rows = _states(ABSENT_PMID)
        self.assertEqual(rows["acquisition"]["state"], pp.OPEN)
        self.assertTrue(any("find-fulltext" in f for f in rows["acquisition"]["files"]))
        for key in ("page_adjudication", "binary_supplement", "integrity_notice", "dependency_integrity"):
            self.assertEqual(rows[key]["state"], pp.TO_ASCERTAIN, key)
            self.assertTrue(rows[key]["to_ascertain"], key)
        self.assertEqual(rows["locator_contradiction"]["state"], pp.NOT_NEEDED)

    def test_everything_present_makes_acquisition_not_needed(self) -> None:
        for pmid in (ERRATUM_PMID, PDF_ONLY_PMID, PPTX_PMID):
            self.assertEqual(_states(pmid)["acquisition"]["state"], pp.NOT_NEEDED, pmid)

    def test_a_pdf_only_surface_is_to_ascertain_until_a_screen_has_run(self) -> None:
        """Unknown is not 'not needed': the packet alone cannot say whether the text layer is sound."""
        row = _states(PDF_ONLY_PMID)["page_adjudication"]
        self.assertEqual(row["state"], pp.TO_ASCERTAIN)
        self.assertIn("check", row["to_ascertain"])

    def test_the_validator_passing_the_pdf_only_surface_settles_it(self) -> None:
        self.assertEqual(_states(PDF_ONLY_PMID, {"VALIDATOR_OK"})["page_adjudication"]["state"],
                         pp.NOT_NEEDED)

    def test_a_suspect_verdict_opens_page_adjudication(self) -> None:
        row = _states(PDF_ONLY_PMID, {"SUSPECT_TEXT_SURFACE"})["page_adjudication"]
        self.assertEqual(row["state"], pp.OPEN)
        self.assertTrue(any("regenerate_adjudications" in f for f in row["files"]))

    def test_an_indexed_hasSuppl_N_closes_the_supplement_question(self) -> None:
        """The reading of 21731849 recorded hasSuppl=N; the rule still said to ascertain, and a
        comparison repeated it over the manifest's own statement (2026-09-12)."""
        row = _states("21731849")["binary_supplement"]
        self.assertEqual(row["state"], pp.NOT_NEEDED, row)
        self.assertIn("hasSuppl=N", row["reason"])

    def test_undeclared_pptx_in_a_pmid_named_directory_opens_binary_supplement(self) -> None:
        """The three .pptx of 38499540 sit in a directory carrying the PMID, not a file name."""
        row = _states(PPTX_PMID)["binary_supplement"]
        self.assertEqual(row["state"], pp.OPEN)
        self.assertIn("MOESM", row["reason"])
        self.assertIn("undeclared", row["reason"])

    def test_declared_binary_containers_do_not_open_the_procedure(self) -> None:
        row = _states(DECLARED_BINARY_PMID)["binary_supplement"]
        self.assertEqual(row["state"], pp.NOT_NEEDED)
        self.assertIn("all declared", row["reason"])

    def test_a_clean_retraction_check_is_not_needed_and_an_absent_one_is_unknown(self) -> None:
        self.assertEqual(_states(PDF_ONLY_PMID)["integrity_notice"]["state"], pp.NOT_NEEDED)
        self.assertEqual(_states(ABSENT_PMID)["integrity_notice"]["state"], pp.TO_ASCERTAIN)

    def test_multiple_conditions_open_together(self) -> None:
        rows = _states(EOC_PMID)
        opened = {key for key, row in rows.items() if row["state"] == pp.OPEN}
        self.assertEqual(opened, {"page_adjudication", "integrity_notice"})
        self.assertIn("ExpressionOfConcernIn", rows["integrity_notice"]["reason"])
        self.assertIn("crop", rows["page_adjudication"]["reason"])

    def test_persisted_locators_leave_the_contradiction_procedure_to_ascertain_until_m3(self) -> None:
        """The trigger datum — does THIS reading change an entry — does not exist before M3."""
        row = _states(ERRATUM_PMID)["locator_contradiction"]
        self.assertEqual(row["state"], pp.TO_ASCERTAIN)
        self.assertIn("38", row["reason"])
        self.assertIn("--working-tree", row["to_ascertain"])
        self.assertIn("M4b", row["phase"])

    def test_an_undeclared_revision_signal_or_a_declaration_opens_it(self) -> None:
        self.assertEqual(_states(ERRATUM_PMID, {"UNDECLARED_LOCATOR_REVISION"})["locator_contradiction"]["state"], pp.OPEN)
        self.assertEqual(_states(ERRATUM_PMID, observed={"contradicts_locator"})["locator_contradiction"]["state"], pp.OPEN)

    def test_an_unscreened_dependency_is_never_reported_as_clean(self) -> None:
        for pmid in (ERRATUM_PMID, PDF_ONLY_PMID, EOC_PMID):
            row = _states(pmid)["dependency_integrity"]
            self.assertEqual(row["state"], pp.TO_ASCERTAIN, pmid)
            self.assertIn("dependency_integrity.py", row["to_ascertain"])

    def test_no_case_with_sufficient_data_opens_everything(self) -> None:
        """Indiscriminate activation is the failure the selector exists to remove."""
        for pmid in (ERRATUM_PMID, PDF_ONLY_PMID, PPTX_PMID, DECLARED_BINARY_PMID):
            states = {row["state"] for row in _states(pmid).values()}
            self.assertIn(pp.NOT_NEEDED, states, pmid)

    def test_every_procedure_names_a_file_that_exists(self) -> None:
        for item in pp.PROCEDURES:
            for spec in item["files"]:
                path = ROOT / spec.split(" (")[0].split(" §")[0].split(" M2")[0]
                self.assertTrue(path.is_file(), spec)


class ANewConditionAfterThePacket(unittest.TestCase):
    def test_an_observed_condition_opens_its_procedure_over_the_packet_facts(self) -> None:
        row = _states(ERRATUM_PMID, observed={"suspect_text_layer"})["page_adjudication"]
        self.assertEqual(row["state"], pp.OPEN)
        self.assertIn("declared by the reader", row["reason"])

    def test_every_procedure_has_an_observed_condition_and_every_condition_a_procedure(self) -> None:
        self.assertEqual({item["observed"] for item in pp.PROCEDURES}, set(pp.OBSERVED_CONDITIONS))

    def test_free_text_is_refused_by_the_function_and_by_the_parser(self) -> None:
        with self.assertRaises(ValueError):
            pp.procedures(pp.build(ROOT, "wwox", ERRATUM_PMID)["technical_facts"],
                          observed={"CLAIM 030 is wrong"})
        done = subprocess.run([sys.executable, str(HERE / "paper_packet.py"), "procedures",
                               "--pmid", ERRATUM_PMID, "--observed", "CLAIM 030 is wrong"],
                              capture_output=True, text=True)
        self.assertEqual(done.returncode, 2)


class TheBlindPacketIsNotContaminatedThroughTheReasons(unittest.TestCase):
    """A manifest whose prose fields carry a claim: none of it reaches a reason string."""

    MARKERS = ("ZQX_CLAIM_TEXT_MUST_NOT_SURFACE", "ZQX_HOLD_TEXT", "ZQX_PROPOSITION",
               "ZQX_ROUTE_NOTE")

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        folder = self.root / "disease-models/wwox/research/deepdive_manifests"
        folder.mkdir(parents=True)
        manifest = {
            "pmid": "99999901", "doi": "10.1000/zqx", "title": "fixture",
            "source_artifacts": [],
            "retraction_check": {
                "result": "Erratum in Journal of Fixtures 2020; ZQX_CLAIM_TEXT_MUST_NOT_SURFACE "
                          "shows the mechanism is real",
                "hold": "ZQX_HOLD_TEXT", "corrected_items": ["Fig 1A"],
                "route": "ZQX_ROUTE_NOTE",
                "dependencies": {"paper_verdict": "FLAGGED_EXPRESSION_OF_CONCERN ZQX_CLAIM_TEXT_MUST_NOT_SURFACE"},
            },
            "verbatim_locators": {"entries": [{"proposition": "ZQX_PROPOSITION is proven",
                                               "snippet": "ZQX_PROPOSITION"}]},
        }
        (folder / "PMID99999901.json").write_text(json.dumps(manifest), encoding="utf-8")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_markers_never_reach_the_packet_the_reasons_or_the_rendering(self) -> None:
        packet = pp.build(self.root, "wwox", "99999901")
        rows = pp.procedures(packet["technical_facts"], {"SUSPECT_TEXT_SURFACE"},
                             set(pp.OBSERVED_CONDITIONS))
        surfaces = [json.dumps(packet), json.dumps(rows), pp.render(packet),
                    pp.render_procedures("99999901", rows, ["packet"])]
        for marker in self.MARKERS:
            for surface in surfaces:
                self.assertNotIn(marker, surface)
        # and the triggers still fired on the tokens, so the firewall cost no signal
        states = {row["key"]: row["state"] for row in rows}
        self.assertEqual(states["integrity_notice"], pp.OPEN)
        self.assertEqual(states["locator_contradiction"], pp.OPEN)   # observed: contradicts_locator

    def test_a_flagged_dependency_verdict_opens_on_its_token_only(self) -> None:
        packet = pp.build(self.root, "wwox", "99999901")
        row = {r["key"]: r for r in pp.procedures(packet["technical_facts"])}["dependency_integrity"]
        self.assertEqual(row["state"], pp.OPEN)
        self.assertTrue(row["reason"].endswith("FLAGGED_EXPRESSION_OF_CONCERN"), row["reason"])
        self.assertNotIn("ZQX", row["reason"])


class TheChecksRecordSignalsForTheProcedures(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.out = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_signal_tokens_are_reduced_from_outputs(self) -> None:
        self.assertIn("SUSPECT_TEXT_SURFACE",
                      pp.check_signals("manifest validator", 1, "… SUSPECT text surface: x.txt …"))
        self.assertIn("VALIDATOR_OK", pp.check_signals("manifest validator", 0, "VERDICT: PASS"))
        self.assertIn("ERRATUM_REVIEW_REQUIRED",
                      pp.check_signals("erratum scope", 0, "[REVIEW_REQUIRED] PMID 1: Fig 3A"))
        self.assertEqual([], pp.check_signals("undeclared locator revision", 0,
                                              "no undeclared locator revision in the working tree"))
        self.assertIn("UNDECLARED_LOCATOR_REVISION",
                      pp.check_signals("undeclared locator revision", 1, "entries[3] changed"))

    def test_a_check_run_writes_the_signals_beside_the_detail_and_procedures_reads_them(self) -> None:
        report = pp.run_checks(ROOT, "wwox", PDF_ONLY_PMID, out_dir=self.out)
        self.assertTrue((self.out / f"PMID{PDF_ONLY_PMID}.json").is_file())
        self.assertTrue(all("signals" in row for row in report["results"]))
        signals, source = pp.load_check_signals(ROOT, PDF_ONLY_PMID, self.out)
        self.assertIn("VALIDATOR_OK", signals)
        self.assertTrue(source)
        self.assertEqual(_states(PDF_ONLY_PMID, signals)["page_adjudication"]["state"], pp.NOT_NEEDED)

    def test_the_cli_procedures_json_matches_the_function(self) -> None:
        done = subprocess.run([sys.executable, str(HERE / "paper_packet.py"), "procedures",
                               "--pmid", EOC_PMID, "--json", "--out-dir", str(self.out)],
                              capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr)
        rows = {row["key"]: row["state"] for row in json.loads(done.stdout)["procedures"]}
        self.assertEqual(rows, {key: row["state"] for key, row in _states(EOC_PMID).items()})


class TheVerifierFoundThese(unittest.TestCase):
    """Four defects from the independent verification of 2026-09-12, each pinned."""

    def test_a_negated_token_is_not_a_notice(self) -> None:
        """Three corpus manifests say 'there is no RetractionIn … link' and opened the procedure."""
        self.assertEqual("", pp.notice_token(
            "CLEAN. PubMed ESummary: there is no RetractionIn, RetractionOf or expression-of-concern link."))
        for pmid in ("17803050", "19500159", "19936220"):
            self.assertEqual(_states(pmid)["integrity_notice"]["state"], pp.NOT_NEEDED, pmid)
        self.assertEqual("Erratum", pp.notice_token(
            "No retraction and no expression of concern. One ORDINARY ERRATUM is attached: "
            "'Erratum in' Cell Death Dis 2018"))

    def test_pubmed_display_forms_with_a_colon_or_lower_case_are_notices(self) -> None:
        self.assertEqual("Erratum", pp.notice_token("Erratum in: Cell Death Dis. 2018;9:1159"))
        self.assertEqual("Expression of concern",
                         pp.notice_token("Expression of concern in: Proc Natl Acad Sci"))

    def test_a_pdf_derived_txt_alone_is_a_pdf_surface_to_screen(self) -> None:
        facts = {"present": 1, "declared_absent": 0, "digest_mismatch": 0, "digest_unverifiable": 0,
                 "declared_present": 1, "structured_surface": False, "pdf_surface": True,
                 "binary_containers": [], "binary_undeclared": [], "supplement_declared": False,
                 "adjudication_artefacts": 0, "locator_entries": 0, "manifest": True,
                 "retraction_check": "recorded", "notice_token": "", "corrected_items": 0,
                 "dependencies_verdict": ""}
        row = {r["key"]: r for r in pp.procedures(facts)}["page_adjudication"]
        self.assertEqual(row["state"], pp.TO_ASCERTAIN)
        self.assertIn("check", row["to_ascertain"])
        self.assertIn(".txt", pp.PDF_SUFFIXES)

    def test_a_malformed_declared_digest_is_named_not_counted_as_agreeing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "files/fulltext").mkdir(parents=True)
            (root / "files/fulltext/PMID99999903.pdf").write_bytes(b"%PDF-1.4 fixture")
            folder = root / "disease-models/wwox/research/deepdive_manifests"
            folder.mkdir(parents=True)
            (folder / "PMID99999903.json").write_text(json.dumps({
                "source_artifacts": [{"path": "files/fulltext/PMID99999903.pdf",
                                      "kind": "article_binary", "sha256": "NOT-A-DIGEST"}]}))
            packet = pp.build(root, "wwox", "99999903")
            self.assertEqual(packet["artefacts"][0]["digest"], "UNVERIFIABLE")
            row = {r["key"]: r for r in packet["procedures"]}["acquisition"]
            self.assertNotIn("digests agree", row["reason"])
            self.assertIn("unverifiable", row["reason"])


# --------------------------------------------------------------------------- surfaces
#
# Expected values fixed by hand on 2026-09-12 with two instruments that had to agree, BEFORE the
# subcommand was pointed at them: a stdlib header parse and PyMuPDF's Pixmap. Both `file(1)`'s
# first NxN and a PyMuPDF PAGE rectangle were tried first and each gave a different, wrong table
# (density; points) — which is why the size is asserted against a third, independent parse here.

THIN_PMID = "29724996"     # Fig2 667x340, Fig6 667x385, Fig7 667x296; article PDF on disk
CROPPED_PMID = "16223882"  # PDF-only, page-adjudication crops already on disk
FAILED_ROUTE_PMID = "20146584"   # two NIHMS figures, no PDF, FAILED_HTTP_404 recorded
NO_SURFACE_PMID = "33914858"     # nothing acquired at all


def png_or_jpeg_size(path: Path) -> tuple[int, int]:
    """A third instrument, written here and not imported from the module under test."""
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        import struct as _s
        return _s.unpack(">II", data[16:24])
    import struct as _s
    index = 2
    while index < len(data) - 9:
        if data[index] != 0xFF:
            index += 1
            continue
        marker = data[index + 1]
        if 0xC0 <= marker <= 0xCF and marker not in {0xC4, 0xC8, 0xCC}:
            height, width = _s.unpack(">HH", data[index + 5:index + 9])
            return int(width), int(height)
        index += 2 + _s.unpack(">H", data[index + 2:index + 4])[0]
    raise AssertionError(f"no SOF marker in {path}")


class TheSurfaceInventory(unittest.TestCase):
    def test_a_raster_is_measured_in_pixels_and_two_instruments_must_agree(self) -> None:
        report = pp.surfaces(ROOT, "wwox", THIN_PMID)
        rows = {Path(row["path"]).name: row for row in report["surfaces"]}
        fig6 = rows["41419_2018_510_Fig6_HTML.jpg"]
        self.assertEqual((667, 385), (fig6["width"], fig6["height"]))
        self.assertEqual((667, 385), png_or_jpeg_size(ROOT / fig6["path"]))
        self.assertIn("agree", fig6["measured"])

    def test_the_incident_asset_is_flagged_with_the_render_route(self) -> None:
        """The 2026-09-09 near-error: a bar count taken from this asset, right at 400 dpi."""
        report = pp.surfaces(ROOT, "wwox", THIN_PMID)
        fig6 = next(r for r in report["surfaces"] if r["path"].endswith("Fig6_HTML.jpg"))
        flags = " ".join(fig6["flags"])
        self.assertIn("667x385", flags)
        self.assertIn("native surface", flags)
        self.assertTrue(report["pdf_on_disk"])

    def test_a_large_raster_is_not_flagged_for_size(self) -> None:
        report = pp.surfaces(ROOT, "wwox", THIN_PMID)
        big = next(r for r in report["surfaces"] if r["path"].endswith("SuppFig1_p4-4.png"))
        self.assertGreater(big["width"], 1500)
        self.assertNotIn("px —", " ".join(big["flags"]))

    def test_existing_crops_are_reported_so_they_are_reused_not_regenerated(self) -> None:
        report = pp.surfaces(ROOT, "wwox", CROPPED_PMID)
        self.assertGreaterEqual(len(report["page_adjudications"]), 10)
        on_disk = sorted(p.name for p in
                         (ROOT / f"disease-models/wwox/research/page_adjudications/PMID{CROPPED_PMID}").iterdir()
                         if p.is_file())
        self.assertEqual(on_disk, report["page_adjudications"])

    def test_a_failed_route_is_named_and_a_successful_one_is_not(self) -> None:
        report = pp.surfaces(ROOT, "wwox", FAILED_ROUTE_PMID)
        joined = pp.render_surfaces(report)
        self.assertIn("FAILED_HTTP_404", joined)
        self.assertIn("new route, method or information", joined)
        self.assertNotIn("RECOVERED", joined)
        self.assertNotIn("no recipe", joined)

    def test_no_surface_at_all_is_not_reported_as_everything_being_fine(self) -> None:
        report = pp.surfaces(ROOT, "wwox", NO_SURFACE_PMID)
        self.assertEqual([], report["surfaces"])
        rendered = pp.render_surfaces(report)
        self.assertIn("NO SURFACE", rendered)
        self.assertNotIn("every declared surface is present", rendered)

    def test_an_absent_surface_is_named_and_its_relevance_left_unknown(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "disease-models/wwox/research/deepdive_manifests"
            folder.mkdir(parents=True)
            (folder / "PMID99999904.json").write_text(json.dumps({"source_artifacts": [
                {"path": "files/figures/PMID99999904/fig1.png", "kind": "figure",
                 "sha256": "a" * 64}]}), encoding="utf-8")
            report = pp.surfaces(root, "wwox", "99999904")
            row = report["surfaces"][0]
            self.assertFalse(row["present"])
            self.assertIn("ABSENT", " ".join(row["flags"]))
            self.assertIn("relevance stays unknown", " ".join(row["flags"]))

    def test_the_inventory_never_classifies_a_surface(self) -> None:
        """The four classes are the reader's declaration after inspection. A tool that guessed
        them from a file name is the failure this inventory is written against."""
        for pmid in (THIN_PMID, CROPPED_PMID, FAILED_ROUTE_PMID):
            report = pp.surfaces(ROOT, "wwox", pmid)
            for row in report["surfaces"]:
                said = (" ".join(row["flags"]) + " " + row["measured"]).upper()
                for word in ("DETERMINANTE", "QUALIFICANTE", "ILLUSTRATIVA", "RIDONDANTE",
                             "MARGINAL", "SKIP", "IGNORE", "LOW PRIORITY", "NOT WORTH"):
                    self.assertNotIn(word, said, (pmid, row["path"], word))
            # and the rendering says so in words, so a reader cannot mistake silence for a verdict
            self.assertIn("that is your declaration after inspection",
                          pp.render_surfaces(report))

    def test_a_page_crop_declared_as_a_figure_is_named(self) -> None:
        """Three crops in this corpus are declared `figure` and carry body TEXT, no figure at
        all — found by a blind legibility assessment on 2026-09-12, not by a size rule."""
        report = pp.surfaces(ROOT, "wwox", "28373548")
        crops = [r for r in report["surfaces"] if "page_adjudications/" in r["path"]]
        self.assertGreaterEqual(len(crops), 3)
        named = [r for r in crops if r["kind"] == "figure"]
        for row in named:
            self.assertIn("MISDECLARED_CROP", row["flags"], row["path"])
        rendered = pp.render_surfaces(report)
        self.assertIn("page-adjudication crops", rendered)
        # said once for the paper, not once per crop
        self.assertEqual(1, rendered.count("read each as the page region it is"))

    def test_the_inventory_states_what_it_cannot_see(self) -> None:
        """A partial panel and a truncated crop are invisible to any size rule; both exist here.
        An inventory that stayed silent about its own blind spot would be read as coverage."""
        rendered = pp.render_surfaces(pp.surfaces(ROOT, "wwox", "18460020"))
        self.assertIn("CANNOT see", rendered)
        self.assertIn("PARTIAL figure", rendered)

    def test_the_output_stays_compact_and_the_command_runs(self) -> None:
        for pmid in (THIN_PMID, CROPPED_PMID, NO_SURFACE_PMID):
            report = pp.surfaces(ROOT, "wwox", pmid)
            rendered = pp.render_surfaces(report)
            flagged = [r for r in report["surfaces"] if r["flags"]]
            # compact as a PROPERTY, not as one number: a fixed footer plus a bounded cost per
            # flagged surface. A single cap silently rewards saying less about more surfaces.
            self.assertLess(len(rendered), 1200 + 220 * max(1, len(flagged)), pmid)
            if report["surfaces"]:
                # only where there IS a payload: for a paper with no surface at all the fixed
                # explanatory footer is legitimately larger than an empty record
                self.assertLess(len(rendered), len(json.dumps(report)), pmid)
        done = subprocess.run([sys.executable, str(HERE / "paper_packet.py"), "surfaces",
                               "--pmid", THIN_PMID, "--json"], capture_output=True, text=True)
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertEqual(pp.surfaces(ROOT, "wwox", THIN_PMID)["surfaces"],
                         json.loads(done.stdout)["surfaces"])

    def test_the_header_parser_reads_both_containers(self) -> None:
        # `files/` is gitignored, so a fresh clone has no figures and `next()` raised
        # StopIteration — an ERROR, not a finding (measured 2026-09-14 in a clean worktree at
        # 772ee77). Skip, naming what is missing, only when no real raster of a container
        # exists; wherever one does, the comparison runs exactly as before.
        figures = ROOT / "files/figures"
        png = next(figures.rglob("*.png"), None) if figures.is_dir() else None
        jpg = next(figures.rglob("*.jpg"), None) if figures.is_dir() else None
        if png is None or jpg is None:
            missing = [kind for kind, found in (("png", png), ("jpg", jpg)) if found is None]
            self.skipTest(f"local figure corpus holds no {'/'.join(missing)} under files/figures")
        for path in (png, jpg):
            self.assertEqual(png_or_jpeg_size(path), pp.raster_size_from_header(path), path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
