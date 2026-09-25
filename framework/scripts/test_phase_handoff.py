#!/usr/bin/env python3
"""Regressions for `phase_handoff.py`.

The packet exists so a phase can start in a NEW context. Two things can go wrong and both are
silent: the packet can carry something the next phase must not see, and it can go stale under the
artefacts it points at. The first four tests are the firewalls; the next four are the adversarial
cases the mandate names — a missing reference, a changed source, an open question the packet has
lost, and a resumption that would redo finished work.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))

import phase_handoff as ph      # noqa: E402

CONTRADICTION = "21731849"      # complete read, 18 locators, a failed acquisition route
CAVEAT = "26499798"             # complete read, links CLAIM 030 and its mandatory caveat
DEPENDENCY = "18460020"         # complete read, descends from an expression-of-concern source


class TheFirewallOfEachPhase(unittest.TestCase):
    def test_a_blind_reading_is_refused_and_told_where_to_go(self) -> None:
        done = subprocess.run([sys.executable, str(HERE / "phase_handoff.py"), "prepare",
                               "--pmid", CONTRADICTION, "--phase", "reading"],
                              capture_output=True, text=True)
        self.assertEqual(2, done.returncode)
        self.assertIn("paper_packet.py packet", done.stderr)

    def test_verification_never_carries_the_producers_verdict(self) -> None:
        """🔴 The test has to be precise about WHAT must not travel. A dossier quotes the same
        source sentences the manifest holds as `snippet`, so shared text is not a leak — the
        verifier needs the quotes. What must never travel is what only the DOSSIER says: its
        judgement. So the comparison is against the dossier's text MINUS the manifest's."""
        handover = ph.prepare(ROOT, "wwox", CONTRADICTION, "verification")
        serialised = json.dumps(handover, ensure_ascii=False)
        dossier = ROOT / f"disease-models/wwox/research/fulltext_dossiers/PMID{CONTRADICTION}.md"
        manifest_text = ph.packet.manifest_path(ROOT, "wwox", CONTRADICTION).read_text(
            encoding="utf-8")
        self.assertTrue(dossier.is_file(), "the fixture needs a real dossier to exclude")
        producer_only = 0
        for line in dossier.read_text(encoding="utf-8").splitlines():
            stripped = line.strip().lstrip("#*->| ").strip()
            if len(stripped) < 60 or stripped[:60] in manifest_text:
                continue
            producer_only += 1
            self.assertNotIn(stripped[:60], serialised)
        self.assertGreater(producer_only, 20, "the fixture needs real producer prose to exclude")
        self.assertNotIn("fulltext_dossiers", json.dumps(handover["references"]))
        self.assertTrue(handover["excludes"])
        self.assertNotIn("group_assessment", handover["mandated_blocks"])

    def test_comparison_carries_the_dossier_as_a_reference_not_as_a_copy(self) -> None:
        handover = ph.prepare(ROOT, "wwox", CONTRADICTION, "comparison")
        paths = [ref["path"] for ref in handover["references"]]
        self.assertTrue(any("fulltext_dossiers" in path for path in paths))
        dossier = ROOT / f"disease-models/wwox/research/fulltext_dossiers/PMID{CONTRADICTION}.md"
        manifest_text = ph.packet.manifest_path(ROOT, "wwox", CONTRADICTION).read_text(
            encoding="utf-8")
        serialised = json.dumps(handover, ensure_ascii=False)
        for line in dossier.read_text(encoding="utf-8").splitlines():
            stripped = line.strip().lstrip("#*->| ").strip()
            if len(stripped) > 80 and stripped[:80] not in manifest_text:
                self.assertNotIn(stripped[:80], serialised, "the packet copied the dossier")

    def test_the_blocks_m4b_binds_a_comparison_to_carry_are_carried(self) -> None:
        """Two condition-B readers, independently, on 2026-09-12: the packet named the manifest
        where the phase needed its content, so both opened the manifest anyway."""
        handover = ph.prepare(ROOT, "wwox", CONTRADICTION, "comparison")
        blocks = handover["mandated_blocks"]
        self.assertIn("group_assessment", blocks)
        self.assertIn("retraction_check", blocks)
        self.assertIn("multihop", blocks)
        self.assertTrue(any(item["kind"] == "not in any field"
                            for item in handover["open_questions"]),
                        "the fourth element is prose in the dossier; the packet must NAME the gap")

    def test_a_proposition_is_carried_whole_and_with_its_quote(self) -> None:
        """Truncated at 300 characters mid-word, with no snippet, sections A and E could not be
        written from the packet at all."""
        manifest = json.loads(ph.packet.manifest_path(ROOT, "wwox", CONTRADICTION).read_text(
            encoding="utf-8"))
        entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
        carried = ph.prepare(ROOT, "wwox", CONTRADICTION, "comparison")["results"]
        self.assertEqual(len(entries), len(carried))
        for source, row in zip(entries, carried):
            self.assertEqual(str(source.get("proposition") or ""), row["proposition"])
            self.assertEqual(str(source.get("snippet") or ""), row["snippet"])

    def test_the_papers_own_references_are_named_because_hop_one_misses_them(self) -> None:
        found = ph.prepare(ROOT, "wwox", CONTRADICTION, "comparison")["discovery"]
        reached = {row["id"] for row in found["records"]}
        self.assertIn("20530675", found["cited_by_this_paper"],
                      "the primary the whole fidelity test runs against")
        self.assertFalse(any("20530675" in name for name in reached),
                         "if hop 1 ever reaches it, this guard has become unnecessary")

    def test_a_receipt_date_is_not_offered_as_a_pmid_to_look_up(self) -> None:
        """A reader on 2026-09-12 found "20260810" in `cited_by_this_paper`: the date inside a
        receipt id, matched by the eight-digit scan."""
        found = ph.prepare(ROOT, "wwox", CAVEAT, "comparison")["discovery"]
        self.assertNotIn("20260810", found["cited_by_this_paper"])
        self.assertIn("25411445", found["cited_by_this_paper"], "the real reference stays")

    def test_an_undeclared_contradiction_flag_is_not_rendered_as_false(self) -> None:
        """A re-test reader wrote "all 18 entries carry contradicts_locator: false" from the
        packet; the manifest carries the key on none of them."""
        manifest = json.loads(ph.packet.manifest_path(ROOT, "wwox", CONTRADICTION).read_text(
            encoding="utf-8"))
        entries = (manifest.get("verbatim_locators") or {}).get("entries") or []
        carried = ph.prepare(ROOT, "wwox", CONTRADICTION, "comparison")["results"]
        for source, row in zip(entries, carried):
            if "contradicts_locator" not in source:
                self.assertEqual("undeclared", row["contradicts_locator"])
            else:
                self.assertIs(bool(source["contradicts_locator"]), row["contradicts_locator"])
        self.assertTrue(any(row["contradicts_locator"] == "undeclared" for row in carried),
                        "the fixture manifest is expected to carry the key on no entry")

    def test_the_artefact_LIST_appears_once_however_often_a_path_is_cited(self) -> None:
        """A reader measured the same 24 paths rendered three times, about half the packet's
        bytes. A path CITED by a locator or a failed route is not duplication — a second full
        listing is. So: exactly one enumeration, and the others are counts or pointers."""
        handover = ph.prepare(ROOT, "wwox", CONTRADICTION, "comparison")
        self.assertIsInstance(handover["technical_history"]["valid_artefacts"], dict)
        self.assertIn("count", handover["technical_history"]["valid_artefacts"])
        self.assertNotIn("surfaces", handover["coverage"])
        self.assertIn("surfaces_in_full", handover["coverage"])
        listings = [key for key, value in handover.items()
                    if isinstance(value, list) and value
                    and all(isinstance(item, dict) and "sha256" in item for item in value)]
        self.assertEqual(["references"], listings, listings)

    def test_discovery_carries_identifiers_and_never_bodies(self) -> None:
        handover = ph.prepare(ROOT, "wwox", CAVEAT, "comparison")
        found = handover["discovery"]
        self.assertGreater(len(found["records"]), 5)
        for row in found["records"]:
            self.assertLess(len(json.dumps(row)), 400, row["id"])
            self.assertNotIn("**Summary:**", json.dumps(row))
        self.assertIn("registry_records.py get", found["open_with"])
        self.assertIn("not evidence", found["limit"])


class TheAdversarialCases(unittest.TestCase):
    """A packet that cannot detect its own staleness is a free summary with a digest field."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name) / "repo"
        # a copy small enough to mutate: the artefacts the packet references, and nothing else
        for rel in ("disease-models/wwox/research/deepdive_manifests",
                    "disease-models/wwox/research/fulltext_dossiers",
                    "disease-models/wwox/registries",
                    "disease-models/wwox/research/page_adjudications"):
            source = ROOT / rel
            if source.is_dir():
                shutil.copytree(source, self.root / rel)
        for rel in ("disease-models/wwox/research/full_text_queue_current.md",
                    "disease-models/wwox/research/discovery_ledger_current.md",
                    "disease-models/wwox/research/dismissal_ledger_current.md",
                    "disease-models/wwox/research/retrieval_manifest.jsonl",
                    "disease-models/wwox/research/fulltext_read_receipts.jsonl"):
            source = ROOT / rel
            if source.is_file():
                (self.root / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, self.root / rel)
        self.packet_path = Path(self._tmp.name) / "packet.json"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _write(self, pmid: str = CONTRADICTION, phase: str = "comparison") -> dict:
        handover = ph.prepare(self.root, "wwox", pmid, phase)
        self.packet_path.write_text(json.dumps(handover, indent=1, ensure_ascii=False),
                                    encoding="utf-8")
        return handover

    def test_a_packet_still_matching_its_artefacts_is_usable(self) -> None:
        self._write()
        report = ph.check(self.root, self.packet_path)
        self.assertEqual([], report["drift"])
        self.assertEqual("USABLE", report["verdict"])

    def test_an_artefact_absent_at_preparation_is_not_drift(self) -> None:
        """`files/` is gitignored, so on most hosts most artefacts are absent at BOTH ends.
        Calling that drift makes every packet read REBUILD and trains the reader to ignore it."""
        handover = self._write()
        absent = [ref for ref in handover["references"] if not ref["present"]]
        self.assertTrue(absent, "the fixture needs an artefact that is absent on this host")
        report = ph.check(self.root, self.packet_path)
        for line in report["drift"]:
            self.assertNotIn(absent[0]["path"], line)

    def test_an_artefact_that_appears_after_preparation_is_reported(self) -> None:
        handover = self._write()
        absent = next(ref for ref in handover["references"] if not ref["present"])
        target = self.root / absent["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"recovered bytes")
        report = ph.check(self.root, self.packet_path)
        self.assertTrue(any(line.startswith("APPEARED:") for line in report["drift"]), report)

    def test_a_missing_reference_is_named_and_the_packet_is_refused(self) -> None:
        handover = self._write()
        target = next(ref for ref in handover["references"] if ref["present"])
        (self.root / target["path"]).unlink()
        report = ph.check(self.root, self.packet_path)
        self.assertTrue(any(line.startswith("MISSING:") for line in report["drift"]), report)
        self.assertEqual("REBUILD — the inputs moved under the packet", report["verdict"])

    def test_a_source_changed_under_the_packet_is_named(self) -> None:
        handover = self._write()
        target = next(ref for ref in handover["references"] if ref["present"])
        path = self.root / target["path"]
        path.write_bytes(path.read_bytes() + b"\n")
        report = ph.check(self.root, self.packet_path)
        self.assertTrue(any(line.startswith("CHANGED:") for line in report["drift"]), report)

    def test_an_open_question_dropped_from_the_packet_is_caught(self) -> None:
        """The failure mode that loses science: a handoff that simply does not mention something."""
        handover = self._write()
        self.assertTrue(handover["open_questions"])
        handover["open_questions"] = handover["open_questions"][1:]
        self.packet_path.write_text(json.dumps(handover, indent=1), encoding="utf-8")
        report = ph.check(self.root, self.packet_path)
        self.assertTrue(any("OPEN QUESTION NOT IN THE PACKET" in line for line in report["drift"]),
                        report["drift"])

    def test_a_question_closed_since_preparation_is_also_reported(self) -> None:
        handover = self._write()
        handover["open_questions"].append({"kind": "coverage", "what": "figures=not_read",
                                           "why": "planted"})
        self.packet_path.write_text(json.dumps(handover, indent=1), encoding="utf-8")
        report = ph.check(self.root, self.packet_path)
        self.assertTrue(any("CLOSED SINCE PREPARATION" in line for line in report["drift"]),
                        report["drift"])

    def test_the_packet_says_what_is_already_finished_so_it_is_not_redone(self) -> None:
        """A resumption that re-reads a finished paper spends the budget the renewal saved."""
        handover = self._write()
        receipt = handover["work_state"]["receipt"]
        self.assertEqual("complete_fulltext_read", receipt["evidence_depth"])
        self.assertEqual([], receipt["owed"])
        self.assertTrue(receipt["event_id"])
        self.assertIn("after the receipt and never before it", handover["objective"])

    def test_a_paper_with_nothing_persisted_has_no_phase_to_hand_over(self) -> None:
        with self.assertRaises(SystemExit):
            ph.prepare(self.root, "wwox", "99999905", "comparison")


class ThePacketIsDerivedNotWritten(unittest.TestCase):
    def test_every_reference_carries_a_digest_and_a_reason(self) -> None:
        for pmid in (CONTRADICTION, CAVEAT, DEPENDENCY):
            for ref in ph.prepare(ROOT, "wwox", pmid, "comparison")["references"]:
                self.assertTrue(ref["why"], ref)
                if ref["present"]:
                    self.assertRegex(ref["sha256"], r"^[0-9a-f]{64}$")

    def test_the_open_questions_are_derived_from_the_artefacts(self) -> None:
        """Not a list someone remembered to write: the same facts the tools already compute."""
        handover = ph.prepare(ROOT, "wwox", DEPENDENCY, "comparison")
        kinds = {item["kind"] for item in handover["open_questions"]}
        self.assertTrue({"procedure to_ascertain"} <= kinds, kinds)
        self.assertTrue(any("dependencies" in item["what"] for item in handover["open_questions"]))

    def test_the_technical_history_carries_four_things_and_not_the_log(self) -> None:
        history = ph.prepare(ROOT, "wwox", "20146584", "comparison")["technical_history"]
        self.assertTrue(history["valid_artefacts"])
        self.assertTrue(any("FAILED" in row["verdict"] for row in history["failed_routes"]))
        self.assertTrue(history["full_logs"])
        for name in history["full_logs"]:
            self.assertNotIn("\n", name, "the log is NAMED, not carried")

    def test_the_packet_never_claims_the_selection_is_complete(self) -> None:
        """The one overclaim that would make every other guarantee worthless: a packet that
        reads as proof that nothing scientific was omitted. Asserted on the CLAIM, not the key."""
        handover = ph.prepare(ROOT, "wwox", CONTRADICTION, "comparison")
        promise = handover["coverage"]["cannot_promise"].lower()
        self.assertIn("not", promise)
        self.assertNotIn("is complete", promise)
        self.assertNotIn("selection is complete", json.dumps(handover).lower())
        rendered = ph.render(handover).lower()
        self.assertIn("does not mean", rendered)
        self.assertIn("not mean the record selection is scientifically complete", rendered)

    def test_the_cli_and_the_function_agree_and_the_file_is_written(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "p.json"
            done = subprocess.run([sys.executable, str(HERE / "phase_handoff.py"), "prepare",
                                   "--pmid", CONTRADICTION, "--phase", "comparison",
                                   "--json", "--out", str(out)], capture_output=True, text=True)
            self.assertEqual(0, done.returncode, done.stderr)
            self.assertEqual(json.loads(done.stdout)["results"],
                             ph.prepare(ROOT, "wwox", CONTRADICTION, "comparison")["results"])
            self.assertTrue(out.is_file())


class WhatTheReadingLeavesOpenTravelsAsAnAddress(unittest.TestCase):
    """2026-09-12, second pilot: a condition-B comparison wrote that two secondary sources
    "place the same patients" where the dossier says the identity "cannot be settled from either
    secondary source". The sentence was in the reader's context and was still overwritten. The
    packet now names every point the reading declares unsettled — as a dossier line and the
    marker phrase, never as a copy of the prose — and the verifier never gets them."""

    def test_the_caveat_papers_unsettled_points_are_named_with_their_line(self) -> None:
        handover = ph.prepare(ROOT, "wwox", CAVEAT, "comparison")
        left = [item for item in handover["open_questions"]
                if item["kind"] == "left open by the reading"]
        self.assertTrue(any("cannot be settled" in item["what"] for item in left), left)
        dossier = ROOT / f"disease-models/wwox/research/fulltext_dossiers/PMID{CAVEAT}.md"
        lines = dossier.read_text(encoding="utf-8").splitlines()
        for item in left:
            path, _, rest = item["what"].partition(":")
            number = int(rest.split(" ")[0])
            marker = rest.split("«")[1].rstrip("»")
            self.assertEqual(str(dossier.relative_to(ROOT)), path)
            self.assertIn(marker, lines[number - 1].lower(), item)
            self.assertIn("may not", item["why"])

    def test_a_reading_that_declares_an_ambiguity_unresolved_is_seen(self) -> None:
        """A survey over every landed dossier on 2026-09-12 found one form the marker list did
        not see: `UNRESOLVED_AMBIGUITY, recorded and not resolved`. Over the whole corpus the
        list matches 8 points in 47 readings — a detector, not a firehose."""
        left = ph.left_open_by_the_reading(ROOT, "wwox", "38499540")
        self.assertEqual(1, len(left), left)
        self.assertIn("unresolved_ambiguity", left[0]["what"])
        self.assertEqual([], ph.left_open_by_the_reading(ROOT, "wwox", "18460020"),
                         "a reading that declares nothing unsettled yields nothing")

    def test_an_address_is_not_a_copy_of_the_dossier(self) -> None:
        for item in ph.left_open_by_the_reading(ROOT, "wwox", CAVEAT):
            self.assertLess(len(item["what"]), 120, item)

    def test_the_verification_packet_never_carries_them(self) -> None:
        handover = ph.prepare(ROOT, "wwox", CAVEAT, "verification")
        kinds = {item["kind"] for item in handover["open_questions"]}
        self.assertNotIn("left open by the reading", kinds)
        self.assertNotIn("not in any field", kinds,
                         "that entry names the dossier, which the verifier must not be pointed at")

    def test_a_dossier_change_that_settles_a_point_is_drift(self) -> None:
        """The list is derived, so `check` sees it move: a dossier edited to settle a point
        after the packet was prepared is reported, not absorbed."""
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "root"
            for rel in (f"disease-models/wwox/research/deepdive_manifests/PMID{CAVEAT}.json",
                        f"disease-models/wwox/research/fulltext_dossiers/PMID{CAVEAT}.md"):
                (copy / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(ROOT / rel, copy / rel)
            for rel in ("disease-models/wwox/registries", "disease-models/wwox/research/ledgers",
                        "disease-models/wwox/therapeutics"):
                if (ROOT / rel).is_dir():
                    shutil.copytree(ROOT / rel, copy / rel, dirs_exist_ok=True)
            for rel in ("disease-models/wwox/research/full_text_queue_current.md",
                        "disease-models/wwox/research/retrieval_manifest.jsonl",
                        "disease-models/wwox/research/discovery_ledger_current.md",
                        "disease-models/wwox/research/dismissal_ledger_current.md"):
                if (ROOT / rel).is_file():
                    shutil.copy(ROOT / rel, copy / rel)
            packet_path = Path(tmp) / "packet.json"
            packet_path.write_text(json.dumps(ph.prepare(copy, "wwox", CAVEAT, "comparison")),
                                   encoding="utf-8")
            self.assertEqual([], ph.check(copy, packet_path)["drift"])
            dossier = copy / f"disease-models/wwox/research/fulltext_dossiers/PMID{CAVEAT}.md"
            dossier.write_text(dossier.read_text(encoding="utf-8").replace(
                "cannot be settled from", "is settled from"), encoding="utf-8")
            drift = ph.check(copy, packet_path)["drift"]
            self.assertTrue(any("CLOSED SINCE PREPARATION" in line and "cannot be settled" in line
                                for line in drift), drift)


if __name__ == "__main__":
    unittest.main(verbosity=2)
