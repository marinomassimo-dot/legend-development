#!/usr/bin/env python3
"""The Phase 3 snapshot holds every file the protocol says it holds.

🔴 WHY THIS EXISTS
------------------
`prompt_batch_commit.md` Phase 3 lists the files a snapshot must carry; `batch_commit.py`
carried its own, shorter list. Nothing compared them, so the difference was discovered by a
batch: on 2026-09-28 BATCH_20260928_001 edited `therapeutic_strategies_current.md`, found it
absent from the snapshot, and copied it in by hand. Had it not noticed, the § 5 ABORT — "restore
all files to pre-batch values" — would have restored every file except the one the batch had
edited, and reported success. A snapshot that silently omits a file it is supposed to protect
defeats the abort path, which is why the test matters more than the list.

The check runs against the REAL repository declaration and the REAL tool, on a copy of the
working tree, so it fails when either side moves: a file named in the protocol and not
snapshotted, and a scientific current file no longer covered at all.

Run: `python3 framework/scripts/test_batch_commit_snapshot.py`
"""
from __future__ import annotations

import glob
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))

import batch_commit  # noqa: E402
from legend_lint import CURRENTS  # noqa: E402


def declared_files(root: Path) -> list[str]:
    """Expand the protocol declaration against a tree, with no help from the tool."""
    found: list[str] = []
    for pattern in batch_commit.declared_patterns(str(root)):
        if any(character in pattern for character in "*?["):
            found.extend(sorted(os.path.relpath(match, root).replace(os.sep, "/")
                                for match in glob.glob(str(root / pattern))
                                if os.path.isfile(match)))
        else:
            found.append(pattern)
    return found


class SnapshotCoversTheDeclaration(unittest.TestCase):
    def setUp(self) -> None:
        self.dest = Path(tempfile.mkdtemp(prefix="legend-snapshot-"))
        self.addCleanup(shutil.rmtree, self.dest, ignore_errors=True)

    def test_every_declared_path_exists_in_the_repository(self) -> None:
        for rel in declared_files(REPO):
            with self.subTest(rel=rel):
                self.assertTrue((REPO / rel).is_file(),
                                f"{rel} is declared in Phase 3 but not in the working tree")

    def test_snapshot_holds_every_declared_file(self) -> None:
        batch_commit.snapshot(str(REPO), str(self.dest / "snap"))
        held = set(batch_commit.snapshot_contents(str(self.dest / "snap")))
        for rel in declared_files(REPO):
            with self.subTest(rel=rel):
                self.assertIn(rel, held, f"Phase 3 names {rel}; the snapshot does not hold it")

    def test_the_regression_file_is_covered(self) -> None:
        """The exact file whose absence was found by hand, pinned by name."""
        self.assertIn("disease-models/wwox/therapeutics/therapeutic_strategies_current.md",
                      batch_commit.snapshot_targets(str(REPO)))

    def test_scientific_current_files_and_state_are_covered(self) -> None:
        targets = batch_commit.snapshot_targets(str(REPO))
        for rel in CURRENTS + batch_commit.EXTRA:
            with self.subTest(rel=rel):
                self.assertIn(rel, targets)

    def test_snapshot_round_trips_through_restore(self) -> None:
        tree = self.dest / "tree"
        for rel in declared_files(REPO) + list(batch_commit.EXTRA):
            (tree / rel).parent.mkdir(parents=True, exist_ok=True)
            (tree / rel).write_text(f"original {rel}\n", encoding="utf-8")
        (tree / batch_commit.PROTOCOL).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO / batch_commit.PROTOCOL, tree / batch_commit.PROTOCOL)

        snap = self.dest / "snap-round-trip"
        taken = batch_commit.snapshot(str(tree), str(snap))
        for rel in taken:
            (tree / rel).write_text("clobbered by the batch\n", encoding="utf-8")
        restored = batch_commit.restore(str(snap), str(tree))
        self.assertEqual(sorted(taken), sorted(restored))
        for rel in taken:
            with self.subTest(rel=rel):
                self.assertEqual((tree / rel).read_text(encoding="utf-8"), f"original {rel}\n")


class SnapshotRefusesRatherThanUnderCover(unittest.TestCase):
    """A short snapshot that reports success is the failure mode; refusal is the safe one."""

    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="legend-snapshot-refuse-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)
        (self.root / batch_commit.PROTOCOL).parent.mkdir(parents=True, exist_ok=True)

    def write_declaration(self, body: str) -> None:
        (self.root / batch_commit.PROTOCOL).write_text(
            f"### Phase 3\n\n{batch_commit.DECLARATION_MARKER}:\n```\n{body}```\n",
            encoding="utf-8")

    def test_missing_declared_file_refuses(self) -> None:
        self.write_declaration("  - some/where/absent_current.md\n")
        with self.assertRaises(batch_commit.DeclarationError):
            batch_commit.snapshot_targets(str(self.root))

    def test_declaration_without_the_currents_refuses(self) -> None:
        for rel in CURRENTS:
            (self.root / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.root / rel).write_text("x\n", encoding="utf-8")
        self.write_declaration(f"  - {CURRENTS[0]}\n")
        with self.assertRaises(batch_commit.DeclarationError) as caught:
            batch_commit.snapshot_targets(str(self.root))
        self.assertIn("scientific current files", str(caught.exception))

    def test_absent_declaration_refuses(self) -> None:
        (self.root / batch_commit.PROTOCOL).write_text("### Phase 3\n\nno block\n",
                                                       encoding="utf-8")
        with self.assertRaises(batch_commit.DeclarationError):
            batch_commit.snapshot_targets(str(self.root))

    def test_cli_refusal_writes_nothing(self) -> None:
        self.write_declaration("  - some/where/absent_current.md\n")
        dest = self.root / "snap"
        done = subprocess.run(
            [sys.executable, str(HERE / "batch_commit.py"), "snapshot",
             "--repo-root", str(self.root), "--dest", str(dest)],
            capture_output=True, text=True)
        self.assertEqual(done.returncode, 2, done.stdout + done.stderr)
        self.assertIn("REFUSED", done.stderr)
        self.assertFalse(dest.exists(), "a refused snapshot must leave no directory behind")


if __name__ == "__main__":
    unittest.main(verbosity=2)
