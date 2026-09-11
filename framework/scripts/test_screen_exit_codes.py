#!/usr/bin/env python3
"""A screen that examined nothing exits non-zero — at the PROCESS level, not only in its record.

Mirror REV-EXPOST-20260911-001 F6 (task MF-6): `genre_discriminator.py --artifact <empty>` and
`erratum_scope_check.py --pmid <absent>` both wrote honest INSUFFICIENT_DATA records and both
exited 0, so a caller reading the status — a shell `&&`, a harness step, a scientist's M3
checklist — read a pass over nothing screened. This is the 2026-09-09 C10 shape (a green over
an unscreened filename) moved one layer out, to the exit code. The other five screens already
exited 2; these two are pinned here through the real subprocess, with a positive control each
so the suite cannot go green by refusing everything.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GENRE = ROOT / "framework" / "scripts" / "genre_discriminator.py"
ERRATUM = ROOT / "framework" / "scripts" / "erratum_scope_check.py"


def run(*argv: str, cwd: Path = ROOT) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *argv], cwd=cwd, capture_output=True, text=True)


class GenreDiscriminatorExitCode(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_an_empty_artifact_is_exit_2_in_json_mode(self) -> None:
        empty = self.dir / "empty.xml"
        empty.write_bytes(b"")
        result = run(str(GENRE), "--artifact", str(empty), "--json")
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        record = json.loads(result.stdout)
        # The record is unchanged by the repair: still INSUFFICIENT_DATA, still zero bytes.
        self.assertEqual("INSUFFICIENT_DATA", record["verdict"])
        self.assertEqual(0, record["screened"]["bytes"])

    def test_an_empty_artifact_is_exit_2_in_text_mode(self) -> None:
        empty = self.dir / "empty.xml"
        empty.write_bytes(b"")
        result = run(str(GENRE), "--artifact", str(empty))
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("INSUFFICIENT_DATA", result.stdout)

    def test_an_absent_artifact_is_exit_2(self) -> None:
        result = run(str(GENRE), "--artifact", str(self.dir / "nope.xml"))
        self.assertEqual(2, result.returncode)

    def test_a_real_deposit_is_screened_and_exits_0(self) -> None:
        """Positive control: refusing everything would also satisfy the three tests above.

        The deposit is the module's own 26-page, 220-reference review fixture, so the test
        does not depend on the gitignored evidence corpus.
        """
        sys.path.insert(0, str(GENRE.parent))
        import genre_discriminator as tool  # noqa: E402
        deposit = self.dir / "review.xml"
        deposit.write_text(tool._F_REAL_REVIEW, encoding="utf-8")
        result = run(str(GENRE), "--artifact", str(deposit), "--pubtypes", "Review,Journal Article", "--json")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        record = json.loads(result.stdout)
        self.assertEqual("AGREES", record["genre_verdict"])
        self.assertGreater(record["screened"]["bytes"], 0)


class ErratumScopeCheckExitCode(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.manifests = self.root / "disease-models" / "wwox" / "research" / "deepdive_manifests"
        self.manifests.mkdir(parents=True)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def _write(self, pmid: str, manifest: dict) -> None:
        (self.manifests / f"PMID{pmid}.json").write_text(json.dumps(manifest), encoding="utf-8")

    def test_a_pmid_that_matches_no_manifest_is_exit_2_and_names_it(self) -> None:
        self._write("11111111", {"pmid": "11111111", "retraction_check": {"result": "checked"}})
        result = run(str(ERRATUM), "--root", str(self.root), "--disease", "wwox", "--pmid", "99999999")
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)
        self.assertIn("INSUFFICIENT_DATA", result.stdout)
        self.assertIn("99999999", result.stdout)

    def test_an_empty_corpus_is_exit_2(self) -> None:
        result = run(str(ERRATUM), "--root", str(self.root), "--disease", "wwox")
        self.assertEqual(2, result.returncode, result.stdout + result.stderr)

    def test_an_examined_manifest_with_an_undeclared_scope_still_exits_0(self) -> None:
        """SCOPE_UNDECLARED is a reading debt, not a defect: that contract is unchanged."""
        self._write("11111111", {"pmid": "11111111",
                                 "retraction_check": {"result": "an erratum was published"},
                                 "verbatim_locators": {"entries": [
                                     {"proposition": "p", "anchor": "Fig 1A", "surface": "figure"}]}})
        result = run(str(ERRATUM), "--root", str(self.root), "--disease", "wwox", "--pmid", "11111111")
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("manifests examined: 1", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
