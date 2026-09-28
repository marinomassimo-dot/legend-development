#!/usr/bin/env python3
"""`manifest_receipt_provenance.py` — the decided semantics, and every way it can be violated.

🔴 WHY THIS EXISTS
------------------
The `receipt` field of a deep-dive manifest was 🟡 OPEN between two readings, and a field with two
readings has no defects — only opinions. It is now decided (`fulltext_read_receipt.md`): the field
names the reading that PRODUCED the manifest, i.e. the earliest same-study ledger event whose
`outputs` name the manifest file. This suite is what makes that a check rather than a convention.

Each fixture is built so its verdict can actually occur: `UNNAMED` really names nothing,
`NOT_THE_PRODUCER` really has an earlier producer, the multihop case really is a cross-study
reading that really did touch the file.

Run: python3 framework/scripts/test_manifest_receipt_provenance.py
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
import manifest_receipt_provenance as mrp  # noqa: E402

TOOL = HERE / "manifest_receipt_provenance.py"


def event(event_id: str, pmid: str, outputs: list[str]) -> dict:
    return {"event_id": event_id, "study_id": {"pmid": pmid, "doi": "10.15252/emmm.202114599"},
            "outputs": outputs, "evidence_depth": "partial_fulltext_read"}


class Fixture(unittest.TestCase):
    def build(self, manifests: dict[str, str], events: list[dict]) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        directory = mrp.manifest_dir(root, "wwox")
        directory.mkdir(parents=True)
        for name, receipt in manifests.items():
            payload: dict = {"schema_version": 2, "pmid": name.removeprefix("PMID").removesuffix(
                ".json")}
            if receipt is not None:
                payload["receipt"] = receipt
            (directory / name).write_text(json.dumps(payload), encoding="utf-8")
        ledger = mrp.ledger_path(root, "wwox")
        ledger.parent.mkdir(parents=True, exist_ok=True)
        ledger.write_text("".join(json.dumps(item) + "\n" for item in events), encoding="utf-8")
        return root

    def verdicts(self, root: Path) -> dict[str, str]:
        return {finding.manifest: finding.verdict for finding in mrp.survey(root, "wwox")}


class TheDecidedSemantics(Fixture):
    def test_the_earliest_naming_event_conforms_and_a_later_one_does_not_change_that(self) -> None:
        """The property the decision was made FOR: a later reading of the same paper must not
        turn a correct pointer into a wrong one, because nothing may rewrite it."""
        root = self.build(
            {"PMID42397075.json": "FTR-20260810-42397075-03"},
            [event("FTR-20260809-42397075-01", "42397075", ["staging/notes.md"]),
             event("FTR-20260810-42397075-03", "42397075",
                   ["disease-models/wwox/research/deepdive_manifests/PMID42397075.json"]),
             event("FTR-20260810-42397075-04", "42397075", ["staging/second_pass.md"])])
        self.assertEqual({"PMID42397075.json": "CONFORMS"}, self.verdicts(root))

    def test_a_later_pass_over_the_manifest_is_not_the_producer(self) -> None:
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID15070730.json"
        root = self.build(
            {"PMID15070730.json": "FTR-20260909-15070730-02"},
            [event("FTR-20260814-15070730-01", "15070730", [manifest]),
             event("FTR-20260909-15070730-02", "15070730", [manifest])])
        finding = mrp.survey(root, "wwox")[0]
        self.assertEqual("NOT_THE_PRODUCER", finding.verdict)
        self.assertEqual("FTR-20260814-15070730-01", finding.should_be,
                         "the check must name the value the field should carry")

    def test_a_receipt_that_names_the_manifest_nowhere_is_the_sharper_defect(self) -> None:
        """🔴 `PMID42589397.json`'s exact shape: the declared receipt is real, belongs to the same
        paper, and touched the manifest in no output at all."""
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID42589397.json"
        root = self.build(
            {"PMID42589397.json": "FTR-20260921-42589397-01"},
            [event("FTR-20260921-42589397-01", "42589397", ["files/fulltext/older_surface.txt"]),
             event("FTR-20260927-42589397-02", "42589397", [manifest]),
             event("FTR-20260928-42589397-03", "42589397", [manifest])])
        finding = mrp.survey(root, "wwox")[0]
        self.assertEqual("UNNAMED", finding.verdict)
        self.assertEqual("FTR-20260927-42589397-02", finding.should_be)

    def test_a_cross_study_reading_never_produces_another_papers_manifest(self) -> None:
        """Real multihop: `FTR-20260810-25331887-01` wrote into `PMID38499540.json`. Counting it
        as the producer would make every multihopped manifest a defect and would reward exactly
        the cross-paper reading the protocol wants."""
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID38499540.json"
        root = self.build(
            {"PMID38499540.json": "FTR-20260810-38499540-01"},
            [event("FTR-20260810-25331887-01", "25331887", [manifest]),
             event("FTR-20260810-38499540-01", "38499540", [manifest])])
        self.assertEqual({"PMID38499540.json": "CONFORMS"}, self.verdicts(root))

    def test_an_unknown_and_an_absent_receipt_are_named_separately(self) -> None:
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID15870886.json"
        root = self.build({"PMID15870886.json": "FTR-20260914-15870886-01",
                           "PMID11111111.json": None},
                          [event("FTR-20260927-15870886-09", "15870886", [manifest])])
        self.assertEqual({"PMID15870886.json": "UNKNOWN_EVENT",
                          "PMID11111111.json": "NO_RECEIPT"}, self.verdicts(root))

    def test_an_unanswerable_ledger_is_reported_and_is_not_a_defect(self) -> None:
        root = self.build({"PMID34214506.json": "FTR-20260726-34214506-02"},
                          [event("FTR-20260726-34214506-02", "34214506",
                                 ["staging/dossier.md"])])
        finding = mrp.survey(root, "wwox")[0]
        self.assertEqual("UNCHECKABLE", finding.verdict)
        self.assertNotIn(finding.verdict, mrp.DEFECTS,
                         "an append-only ledger that cannot answer is not a finding against a "
                         "manifest")

    def test_a_doi_is_never_mistaken_for_the_pmid(self) -> None:
        """🔴 `10.15252/emmm.202114599` carries a 9-digit run, so a regex over the serialised
        event matches the DOI before the PMID. That mistake alone moved UNCHECKABLE from 3 to 33
        while it was being measured."""
        self.assertEqual("42589397", mrp.study_pmid(
            event("FTR-1", "42589397", [])), "the pmid must come off study_id")
        self.assertEqual("", mrp.study_pmid({"event_id": "x", "study_id": "42589397"}),
                         "a study_id that is not an object carries no pmid")

    def test_every_outputs_shape_is_read(self) -> None:
        """A shape this could not read would make every manifest UNCHECKABLE — a false zero that
        is indistinguishable from a true one."""
        for outputs in ("a/b.json", ["a/b.json"], {"manifest": "a/b.json"},
                        [{"path": "a/b.json"}], [["a/b.json"]]):
            with self.subTest(repr(outputs)):
                self.assertIn("a/b.json", mrp.output_strings({"outputs": outputs}))
        self.assertEqual([], mrp.output_strings({}))


class TheGate(Fixture):
    def run_tool(self, root: Path, *arguments: str):
        return subprocess.run([sys.executable, str(TOOL), "--root", str(root), *arguments],
                              capture_output=True, text=True)

    def one_defect(self) -> Path:
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID15070730.json"
        return self.build({"PMID15070730.json": "FTR-20260909-15070730-02"},
                          [event("FTR-20260814-15070730-01", "15070730", [manifest]),
                           event("FTR-20260909-15070730-02", "15070730", [manifest])])

    def test_the_default_run_reports_and_exits_zero(self) -> None:
        done = self.run_tool(self.one_defect())
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn("NOT_THE_PRODUCER", done.stdout)
        self.assertIn("NOTHING IS REPAIRED HERE", done.stdout,
                      "the report must say that no instrument writes this field")

    def test_check_fails_only_above_the_ceiling(self) -> None:
        root = self.one_defect()
        self.assertEqual(0, self.run_tool(root, "--check", "--max-defects", "1").returncode)
        above = self.run_tool(root, "--check", "--max-defects", "0")
        self.assertEqual(1, above.returncode)
        self.assertIn("exceeds the ceiling", above.stderr)

    def test_json_carries_the_ceiling_and_every_finding(self) -> None:
        done = self.run_tool(self.one_defect(), "--json")
        payload = json.loads(done.stdout)
        self.assertEqual(mrp.BASELINE_DEFECTS, payload["ceiling"])
        self.assertEqual(1, payload["defects"])
        self.assertEqual("NOT_THE_PRODUCER", payload["findings"][0]["verdict"])


class TheLiveCorpus(unittest.TestCase):
    """Not a fixture: the declared ceiling must be the measured truth of this repository, or the
    gate is either dead or permanently red."""

    def test_the_declared_ceiling_is_the_measured_count(self) -> None:
        findings = mrp.survey(ROOT, "wwox")
        defects = [finding for finding in findings if finding.verdict in mrp.DEFECTS]
        self.assertEqual(mrp.BASELINE_DEFECTS, len(defects),
                         "the ceiling is a measurement, not a guess: re-measure and lower it "
                         "when the tail is repaired — never raise it. Non-conforming now: "
                         + ", ".join(f"{f.manifest} {f.verdict}" for f in defects))
        self.assertEqual(0, mrp.main(["--root", str(ROOT), "--check"]))

    def test_the_two_manifests_the_decision_was_made_on(self) -> None:
        by_name = {finding.manifest: finding for finding in mrp.survey(ROOT, "wwox")}
        self.assertEqual("CONFORMS", by_name["PMID42397075.json"].verdict,
                         "-03 is the event that produced it, so the decision leaves it alone")
        flagged = by_name["PMID42589397.json"]
        self.assertEqual("UNNAMED", flagged.verdict,
                         "-01 names this manifest in no output, so it is wrong under BOTH of the "
                         "readings the field used to carry")
        self.assertEqual("FTR-20260927-42589397-02", flagged.should_be)


if __name__ == "__main__":
    unittest.main(verbosity=1)
