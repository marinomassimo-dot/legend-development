#!/usr/bin/env python3
"""`manifest_receipt_repoint.py` — the derivation, every refusal, and the byte-identity proof.

🔴 WHY THIS EXISTS
------------------
The writer's whole claim is that it repairs ONE field of ONE manifest and refuses everything
else, and that every other byte survives identical. A claim like that is worth exactly what its
refusals are worth: a tool that writes the right value on the easy case and something plausible
on the hard ones is worse than no tool, because the hard cases are the ones a session cannot
adjudicate by eye. So each refusal has its own fixture, built so the refusal can actually occur,
and the byte-identity post-condition is tested against a manifest whose formatting a naive
`json.dump` round-trip WOULD destroy — two-space indent, a trailing newline, non-ASCII text and
a duplicate of the new value elsewhere in the file.

Run: python3 framework/scripts/test_manifest_receipt_repoint.py
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
import manifest_receipt_repoint as repoint  # noqa: E402

TOOL = HERE / "manifest_receipt_repoint.py"

#: Two spaces, a trailing newline, non-ASCII prose, and the DERIVED value present a second time
#: in a note — every one of which a round-trip through `json.dump` or a global replace would move.
MANIFEST_TEXT = """{
  "schema_version": 2,
  "pmid": "11111111",
  "receipt": "FTR-20260909-11111111-02",
  "landing": [
    "CLAIM 001"
  ],
  "note": "prose naming FTR-20260814-11111111-01 — the é and the — must survive",
  "source_artifacts": [
    {
      "path": "files/fulltext/a.xml",
      "sha256": "aaaa"
    }
  ]
}
"""


def event(event_id: str, pmid: str, outputs: list[str], *, fingerprint: str = "aaaa",
          event_at: str = "") -> dict:
    record = {"event_id": event_id, "study_id": {"pmid": pmid, "doi": "10.1/x"},
              "outputs": outputs, "evidence_depth": "partial_fulltext_read",
              "source_fingerprint": fingerprint}
    if event_at:
        record["event_at"] = event_at
    return record


class Fixture(unittest.TestCase):
    def build(self, manifests: dict[str, object], events: list[dict]) -> Path:
        """A workspace. A manifest value may be raw text, a dict, or None for 'no receipt key'."""
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        directory = mrp.manifest_dir(root, "wwox")
        directory.mkdir(parents=True)
        for name, body in manifests.items():
            if isinstance(body, str):
                text = body
            else:
                text = json.dumps(body, indent=2) + "\n"
            (directory / name).write_text(text, encoding="utf-8")
        ledger = mrp.ledger_path(root, "wwox")
        ledger.parent.mkdir(parents=True, exist_ok=True)
        ledger.write_text("".join(json.dumps(item) + "\n" for item in events), encoding="utf-8")
        return root

    def standard(self, **overrides) -> Path:
        """The repairable case: `-02` touched the manifest, `-01` produced it."""
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID11111111.json"
        return self.build({"PMID11111111.json": overrides.get("text", MANIFEST_TEXT)},
                          overrides.get("events", [
                              event("FTR-20260814-11111111-01", "11111111", [manifest]),
                              event("FTR-20260909-11111111-02", "11111111", [manifest])]))

    def manifest_of(self, root: Path) -> Path:
        return mrp.manifest_dir(root, "wwox") / "PMID11111111.json"

    def run_tool(self, root: Path, *arguments: str):
        return subprocess.run([sys.executable, str(TOOL), "--root", str(root), *arguments],
                              capture_output=True, text=True)


class TheDerivation(Fixture):
    def test_the_target_comes_from_the_ledger_and_the_dry_run_writes_nothing(self) -> None:
        root = self.standard()
        before = self.manifest_of(root).read_bytes()
        done = self.run_tool(root, "--pmid", "11111111")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn("FTR-20260814-11111111-01", done.stdout)
        self.assertIn("DRY RUN", done.stdout)
        self.assertEqual(before, self.manifest_of(root).read_bytes(),
                         "a dry run that writes is not a dry run")

    def test_there_is_no_way_to_supply_a_target(self) -> None:
        """The contract, asserted on the interface: a caller-supplied value is the defect class
        this tool exists to close, so `--to` must not be accepted under any spelling."""
        root = self.standard()
        for flag in ("--to", "--receipt", "--new", "--target"):
            with self.subTest(flag):
                done = self.run_tool(root, "--pmid", "11111111", flag,
                                     "FTR-20260909-11111111-02")
                self.assertEqual(2, done.returncode,
                                 f"{flag} was accepted; the target must always be derived")
        self.assertNotIn("--to", (TOOL.read_text(encoding="utf-8")
                                  .split("def main", 1)[1]))

    def test_apply_writes_the_derived_value_and_exits_zero(self) -> None:
        root = self.standard()
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(0, done.returncode, done.stderr)
        self.assertIn("APPLIED", done.stdout)
        self.assertEqual("FTR-20260814-11111111-01",
                         json.loads(self.manifest_of(root).read_text(encoding="utf-8"))["receipt"])
        self.assertEqual("CONFORMS", mrp.assess(
            self.manifest_of(root),
            mrp.load_events(mrp.ledger_path(root, "wwox"))).verdict)

    def test_every_other_byte_survives_identical(self) -> None:
        root = self.standard()
        before = self.manifest_of(root).read_text(encoding="utf-8")
        self.assertEqual(0, self.run_tool(root, "--pmid", "11111111", "--apply").returncode)
        after = self.manifest_of(root).read_text(encoding="utf-8")
        self.assertEqual(len(before), len(after))
        self.assertEqual(
            before,
            after.replace('"receipt": "FTR-20260814-11111111-01"',
                          '"receipt": "FTR-20260909-11111111-02"', 1),
            "the repair must be reversible by undoing exactly the one substitution")
        self.assertIn("the é and the — must survive", after)
        self.assertTrue(after.endswith("}\n"), "the trailing newline is part of the file")
        self.assertEqual(1, after.count('"receipt":'))
        self.assertEqual(2, after.count("FTR-20260814-11111111-01"),
                         "the prose occurrence must be untouched: only the FIELD moves")

    def test_a_second_run_refuses_because_the_field_now_conforms(self) -> None:
        root = self.standard()
        self.run_tool(root, "--pmid", "11111111", "--apply")
        again = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, again.returncode)
        self.assertIn("CONFORMS", again.stderr)


class TheRefusals(Fixture):
    def test_a_conforming_field_is_never_rewritten(self) -> None:
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID11111111.json"
        root = self.build(
            {"PMID11111111.json": {"schema_version": 2, "pmid": "11111111",
                                   "receipt": "FTR-20260814-11111111-01"}},
            [event("FTR-20260814-11111111-01", "11111111", [manifest])])
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("CONFORMS", done.stderr)

    def test_no_event_names_the_manifest(self) -> None:
        """UNCHECKABLE: the ledger holds no producer, and it is not rewritten to make one."""
        root = self.build(
            {"PMID11111111.json": {"schema_version": 2, "pmid": "11111111",
                                   "receipt": "FTR-20260814-11111111-01"}},
            [event("FTR-20260814-11111111-01", "11111111", ["some/other/file.md"])])
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("no same-study ledger event names this manifest", done.stderr)

    def test_an_unknown_declared_event_with_no_producer_is_a_different_defect(self) -> None:
        root = self.build(
            {"PMID11111111.json": {"schema_version": 2, "pmid": "11111111",
                                   "receipt": "FTR-20260914-11111111-09"}},
            [event("FTR-20260814-11111111-01", "11111111", ["some/other/file.md"])])
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("needs a receipt, not a repoint", done.stderr)

    def test_a_missing_receipt_key_is_not_added(self) -> None:
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID11111111.json"
        root = self.build({"PMID11111111.json": {"schema_version": 2, "pmid": "11111111"}},
                          [event("FTR-20260814-11111111-01", "11111111", [manifest])])
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("never adds a key", done.stderr)

    def test_artifact_divergence_is_refused_with_no_flag_to_waive_it(self) -> None:
        """The derived producer fingerprints a document the manifest does not declare.

        `require_work_manifest` binds a receipt's `source_fingerprint` to the manifest's
        `source_artifacts`, so re-pointing here would satisfy the provenance check and contradict
        that binding. Five live manifests are in this state; the refusal is what keeps a batch
        repair from walking into them.
        """
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID11111111.json"
        root = self.standard(events=[
            event("FTR-20260814-11111111-01", "11111111", [manifest], fingerprint="bbbb"),
            event("FTR-20260909-11111111-02", "11111111", [manifest], fingerprint="aaaa")])
        before = self.manifest_of(root).read_bytes()
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("ARTIFACT DIVERGENCE", done.stderr)
        self.assertEqual(before, self.manifest_of(root).read_bytes())
        self.assertNotIn("allow-artifact", TOOL.read_text(encoding="utf-8"),
                         "this class needs a decision, not a flag")

    def test_a_derivation_that_is_not_unique_is_refused(self) -> None:
        """Earliest by APPEND order and earliest by `event_at` name two different events."""
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID11111111.json"
        root = self.standard(events=[
            event("FTR-20260814-11111111-01", "11111111", [manifest],
                  event_at="2026-09-09T00:00:00Z"),
            event("FTR-20260909-11111111-02", "11111111", [manifest],
                  event_at="2026-08-14T00:00:00Z")])
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("not unique", done.stderr)

    def test_a_needle_that_is_not_unique_in_the_text_is_refused(self) -> None:
        """Not hypothetical: `contradicts_locator` has a `receipt` key of its own, so a manifest
        can legitimately spell the same needle twice — and a tool that replaced the first
        occurrence would rewrite a locator's provenance instead of the manifest's."""
        manifest = "disease-models/wwox/research/deepdive_manifests/PMID11111111.json"
        doubled = MANIFEST_TEXT.replace(
            '  "landing": [',
            '  "contradicts_locator": {\n'
            '    "receipt": "FTR-20260909-11111111-02"\n'
            '  },\n'
            '  "landing": [')
        root = self.standard(text=doubled, events=[
            event("FTR-20260814-11111111-01", "11111111", [manifest]),
            event("FTR-20260909-11111111-02", "11111111", [manifest])])
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("refusing to guess", done.stderr)

    def test_an_absent_manifest_is_refused_not_created(self) -> None:
        root = self.standard()
        done = self.run_tool(root, "--pmid", "99999999", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("manifest(s) match", done.stderr)
        self.assertFalse((mrp.manifest_dir(root, "wwox") / "PMID99999999.json").exists())

    def test_a_manifest_that_is_not_json_is_refused(self) -> None:
        root = self.standard(text="{not json")
        done = self.run_tool(root, "--pmid", "11111111", "--apply")
        self.assertEqual(1, done.returncode)
        self.assertIn("not readable JSON", done.stderr)


class ThePostConditions(Fixture):
    def test_a_failed_post_condition_restores_the_original_bytes(self) -> None:
        """Exit code 2, and the file is what it was.

        The post-conditions cannot be provoked through the CLI — they hold — so the failure is
        injected where a future edit could genuinely break it: `assess` is made to report a
        non-conforming verdict AFTER the write. What is being tested is the rollback, not the
        stub.
        """
        root = self.standard()
        before = self.manifest_of(root).read_bytes()
        original = repoint.provenance.assess
        calls: list[int] = []

        def flaky(path, events):
            finding = original(path, events)
            calls.append(1)
            if len(calls) > 1:  # the post-write call
                finding.verdict = "NOT_THE_PRODUCER"
            return finding

        repoint.provenance.assess = flaky
        try:
            with self.assertRaises(repoint.PostCondition):
                repoint.repoint(root, "wwox", "11111111", apply=True)
        finally:
            repoint.provenance.assess = original
        self.assertEqual(before, self.manifest_of(root).read_bytes(),
                         "a post-condition failure must leave no trace")
        self.assertEqual(2, repoint.TOOL_ERROR)

    def test_a_preexisting_validation_error_does_not_block_the_repair(self) -> None:
        """The manifests that need repair are old ones, and old ones fail today's validator.

        Rolling back on an error the repair did not introduce would make the tool unusable on
        precisely its population — so the comparison is before-versus-after, not pass/fail.
        """
        root = self.standard()
        self.assertTrue(repoint.validation_errors(root, "wwox", "11111111"),
                        "this minimal fixture is expected to be invalid; if it ever validates, "
                        "the test below stops testing anything")
        proof = repoint.repoint(root, "wwox", "11111111", apply=True)
        self.assertTrue(proof["applied"])
        self.assertTrue(proof["preexisting_validation_errors"])

    def test_the_freshness_command_is_always_printed(self) -> None:
        """Three committed derived surfaces declare the manifest directory among their inputs, so
        a landing that carries a repair owes `candidate_tree_freshness.py`. Printing the command
        is the difference between a rule and a habit."""
        root = self.standard()
        for arguments in (("--pmid", "11111111"), ("--pmid", "11111111", "--apply")):
            with self.subTest(arguments):
                done = self.run_tool(root, *arguments)
                self.assertIn("candidate_tree_freshness.py", done.stdout)


class TheLiveCorpus(unittest.TestCase):
    """The repository's own state, not a fixture."""

    def run_tool(self, *arguments: str):
        return subprocess.run([sys.executable, str(TOOL), "--root", str(ROOT), *arguments],
                              capture_output=True, text=True)

    def test_the_repaired_manifest_is_refused_a_second_time(self) -> None:
        done = self.run_tool("--pmid", "42589397")
        self.assertEqual(1, done.returncode, done.stdout)
        self.assertIn("CONFORMS", done.stderr)

    def test_the_five_artifact_divergence_manifests_are_refused(self) -> None:
        """Measured 2026-09-28. These are the ones a batch repair must not walk into."""
        for pmid in ("15070730", "18674750", "20530675", "29724996", "38499540"):
            with self.subTest(pmid):
                done = self.run_tool("--pmid", pmid)
                self.assertEqual(1, done.returncode, done.stdout)
                self.assertIn("ARTIFACT DIVERGENCE", done.stderr)

    def test_the_manifests_with_no_producer_in_the_ledger_are_refused(self) -> None:
        # 15870886 left this list on 2026-09-28 (BATCH_20260928_007): it got a recorded producer
        # (a receipt, which is what this refusal says it needs), and now reads CONFORMS.
        for pmid in ("34214506", "35716775"):
            with self.subTest(pmid):
                done = self.run_tool("--pmid", pmid)
                self.assertEqual(1, done.returncode, done.stdout)
                self.assertIn("needs a receipt, not a repoint", done.stderr)

    def test_the_remaining_repairable_tail_is_named_and_dry_runs_clean(self) -> None:
        """The debt the ceiling keeps visible: derivable, unique, artifact-coherent, unrepaired.

        Asserted as an exact set, because "some of them are repairable" is not a measurement and
        the next pass needs to know which. A manifest leaving this set means it was repaired (and
        the ceiling fell) or it changed class (and that is worth noticing).
        """
        expected = {"19936220", "22193544", "22634283", "23370280", "24550385", "26675548",
                    "30362252", "34831305", "36828035", "42422765"}
        for pmid in sorted(expected):
            with self.subTest(pmid):
                done = self.run_tool("--pmid", pmid)
                self.assertEqual(0, done.returncode, done.stderr)
                self.assertIn("DRY RUN", done.stdout)
        # The no-producer term was 1 (PMID15870886, UNKNOWN_EVENT) until 2026-09-28, when
        # BATCH_20260928_007 recorded its producing reading; 34214506 and 35716775 are UNCHECKABLE,
        # which the ceiling does not count.
        self.assertEqual(len(expected) + 5 + 0, mrp.BASELINE_DEFECTS,
                         "the ceiling must equal repairable + artifact-divergence + no-producer; "
                         "if it does not, one of the three classes has moved unmeasured")


if __name__ == "__main__":
    unittest.main(verbosity=1)
