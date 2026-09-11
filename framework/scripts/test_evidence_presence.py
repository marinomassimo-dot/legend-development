#!/usr/bin/env python3
"""Tests for evidence_presence.py.

Each test is a distinction the tool would be useless without. In particular the third and
fourth: **absent and mismatched must never collapse into one state**, because the recovery
differs completely — absence is re-acquired, a mismatch invalidates every locator drawn from
those bytes. The measurement that motivated the tool found 21 artifacts absent and, once
re-acquired, 21 matching; a tool that reported only "problem/no problem" would have said the
same word about both situations.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "evidence_presence.py"


class EvidencePresenceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    # helpers -----------------------------------------------------------------
    def run_tool(self, root: Path, *extra: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(root), *extra],
            capture_output=True,
            text=True,
        )

    def fixture(self, *, body: bytes = b"hello evidence", declared: str | None = None,
                write_file: bool = True) -> Path:
        root = self.tmp / "repo"
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        man = root / "disease-models" / "wwox" / "research" / "deepdive_manifests"
        man.mkdir(parents=True)
        art = root / "files" / "fulltext"
        art.mkdir(parents=True)
        if write_file:
            (art / "a.xml").write_bytes(body)
        digest = declared if declared is not None else hashlib.sha256(body).hexdigest()
        (man / "PMID111.json").write_text(
            json.dumps(
                {
                    "schema_version": 2,
                    "pmid": "111",
                    "source_artifacts": [
                        {"path": "files/fulltext/a.xml", "sha256": digest, "kind": "article_text"}
                    ],
                }
            ),
            encoding="utf-8",
        )
        return root

    # tests -------------------------------------------------------------------
    def test_present_and_matching_reports_complete(self):
        r = self.run_tool(self.fixture())
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("VERDICT: COMPLETE", r.stdout)
        self.assertIn("present: 1", r.stdout)

    def test_absent_is_reported_and_is_not_an_error(self):
        """A fresh checkout carries no evidence. Normal, and never an exit status."""
        r = self.run_tool(self.fixture(write_file=False), "--fail-on-mismatch")
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("NO LOCAL EVIDENCE", r.stdout)
        self.assertIn("absent: 1", r.stdout)

    def test_mismatch_is_a_distinct_state_from_absent(self):
        """The load-bearing distinction: changed bytes are not missing bytes."""
        r = self.run_tool(self.fixture(declared="0" * 64))
        self.assertIn("DIGEST MISMATCH", r.stdout)
        self.assertIn("digest_mismatch: 1", r.stdout)
        self.assertIn("absent: 0", r.stdout)

    def test_fail_on_mismatch_raises_status_only_for_mismatch(self):
        root = self.fixture(declared="0" * 64)
        self.assertEqual(self.run_tool(root).returncode, 0)
        self.assertEqual(self.run_tool(root, "--fail-on-mismatch").returncode, 1)

    def test_pmid_filter_selects_nothing_when_unmatched(self):
        r = self.run_tool(self.fixture(), "--pmid", "999")
        self.assertIn("manifests: 0", r.stdout)

    def test_json_emits_one_record_per_manifest(self):
        r = self.run_tool(self.fixture(), "--json")
        lines = [l for l in r.stdout.splitlines() if l.startswith("{")]
        self.assertEqual(len(lines), 1)
        rec = json.loads(lines[0])
        self.assertEqual(rec["pmid"], "111")
        self.assertEqual(rec["artifacts"][0]["state"], "PRESENT")

    def test_unreadable_manifest_is_a_finding_not_a_crash(self):
        root = self.fixture()
        bad = root / "disease-models" / "wwox" / "research" / "deepdive_manifests" / "PMID222.json"
        bad.write_text("{ not json", encoding="utf-8")
        r = self.run_tool(root)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("UNREADABLE", r.stdout)


class TheRealManifestsAreAudited(unittest.TestCase):
    """One real manifest through ``main`` over this checkout — read, reported, unchanged.

    The bytes it fingerprints live under gitignored ``files/``, so on a bare host every
    artifact is ABSENT and the verdict says so; that is the tool's documented answer, not a
    failure. The manifest itself is tracked and must be byte-identical afterwards.
    """

    ROOT = Path(__file__).resolve().parents[2]

    def test_one_real_manifest_through_main_in_json_and_text(self) -> None:
        manifests = sorted((self.ROOT / "disease-models/wwox/research/deepdive_manifests")
                           .glob("PMID*.json"))
        if not manifests:
            self.skipTest("skipped: no deepdive manifest in this checkout")
        chosen = manifests[0]
        pmid = chosen.stem.removeprefix("PMID")
        before = chosen.read_bytes()
        script = self.ROOT / "framework/scripts/evidence_presence.py"
        machine = subprocess.run(
            [sys.executable, str(script), "--root", str(self.ROOT), "--disease", "wwox",
             "--pmid", pmid, "--json"], capture_output=True, text=True, timeout=300)
        self.assertEqual(machine.returncode, 0, machine.stderr)
        lines = [line for line in machine.stdout.splitlines() if line.startswith("{")]
        self.assertEqual(len(lines), 1, "--pmid must select exactly one manifest record")
        record = json.loads(lines[0])
        self.assertEqual(record["pmid"], pmid)
        self.assertEqual(record["manifest"], chosen.relative_to(self.ROOT).as_posix())
        for row in record["artifacts"]:
            self.assertIn(row["state"], ("PRESENT", "ABSENT", "DIGEST_MISMATCH", "NO_DIGEST",
                                         "MISMATCH", "UNDECLARED"))
        self.assertRegex(machine.stdout, r"manifests: 1 \| artifacts: \d+ \| present: \d+ \| "
                                         r"absent: \d+ \| digest_mismatch: \d+ \| no_digest: \d+")
        text = subprocess.run(
            [sys.executable, str(script), "--root", str(self.ROOT), "--disease", "wwox",
             "--pmid", pmid], capture_output=True, text=True, timeout=300)
        self.assertEqual(text.returncode, 0, text.stderr)
        self.assertIn("VERDICT:", text.stdout)
        self.assertEqual(chosen.read_bytes(), before, "the audit wrote a real manifest")


if __name__ == "__main__":
    unittest.main()
