#!/usr/bin/env python3
"""Tests for the ref-scoped commit-metadata scan.

Each test builds a real throwaway repository. A fixture that stubs `git` would test the
stub; the defect being guarded against here lives in what `git rev-list` actually
enumerates, which is precisely the part a stub replaces.

Every address in this file ends in `@example.invalid` — the reserved form the tree scanner
accepts — and the allowlist under test is injected rather than imported. Using the real
project identity here would put a real address in a tracked file, which is the very thing
the surrounding gate exists to prevent.
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import commit_metadata_scan as scanner  # noqa: E402


PROJECT = "project-identity@example.invalid"
PERSONAL = "a-person@example.invalid"
PERMITTED = frozenset({scanner.identity_digest(PROJECT)})


def run_git(root: str, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", root, *args], check=True, capture_output=True, text=True
    )
    return result.stdout.strip()


def commit(root: str, message: str, email: str, filename: str) -> str:
    Path(root, filename).write_text(message + "\n", encoding="utf-8")
    run_git(root, "add", filename)
    env = dict(
        os.environ,
        GIT_AUTHOR_NAME="The LEGEND project", GIT_AUTHOR_EMAIL=email,
        GIT_COMMITTER_NAME="The LEGEND project", GIT_COMMITTER_EMAIL=email,
    )
    subprocess.run(
        ["git", "-C", root, "commit", "-m", message],
        check=True, capture_output=True, text=True, env=env,
    )
    return run_git(root, "rev-parse", "HEAD")


class CommitMetadataScanTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        run_git(self.root, "init", "-q", "-b", "main")
        run_git(self.root, "config", "user.name", "The LEGEND project")
        run_git(self.root, "config", "user.email", PROJECT)
        self.base = commit(self.root, "base", PROJECT, "a.txt")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def scan(self, ref: str, bases: list[str]):
        return scanner.scan(self.root, ref, bases, permitted=PERMITTED)

    # ---- the control must be able to fail ------------------------------------------
    def test_control_fires(self) -> None:
        self.assertTrue(scanner.control_can_fire())

    def test_shipped_allowlist_is_digests_not_addresses(self) -> None:
        """The table must never regress to literal addresses.

        Its literal form made this scanner's own source the only file in the repository
        failing the tree scan, so the shape is load-bearing, not cosmetic.
        """
        for entry in scanner.PERMITTED_COMMIT_IDENTITY_DIGESTS:
            self.assertRegex(entry, r"^[0-9a-f]{64}$")
            self.assertNotIn("@", entry)

    # ---- identity x scope ------------------------------------------------------------
    def test_project_identity_in_scope_passes(self) -> None:
        run_git(self.root, "checkout", "-q", "-b", "feature")
        commit(self.root, "clean work", PROJECT, "b.txt")
        findings, scanned = self.scan("feature", ["main"])
        self.assertEqual(scanned, 1)
        self.assertEqual(findings, [])

    def test_personal_identity_in_scope_blocks(self) -> None:
        run_git(self.root, "checkout", "-q", "-b", "feature")
        sha = commit(self.root, "leaky work", PERSONAL, "b.txt")
        findings, scanned = self.scan("feature", ["main"])
        self.assertEqual(scanned, 1)
        self.assertEqual({f.code for f in findings}, {"NON_PROJECT_COMMIT_IDENTITY"})
        # both published identities are reported, not just the author
        self.assertEqual({f.field for f in findings}, {"author", "committer"})
        self.assertTrue(all(f.commit == sha for f in findings))

    def test_personal_identity_outside_scope_does_not_block(self) -> None:
        """The defect this scoping rule exists to prevent.

        A sibling branch carrying a personal address must not make *this* ref
        unpublishable — otherwise one bad branch blocks the whole repository and the
        check stops being run at all.
        """
        run_git(self.root, "checkout", "-q", "-b", "dirty")
        commit(self.root, "leaky work", PERSONAL, "c.txt")
        run_git(self.root, "checkout", "-q", "main")
        run_git(self.root, "checkout", "-q", "-b", "feature")
        commit(self.root, "clean work", PROJECT, "b.txt")
        findings, scanned = self.scan("feature", ["main"])
        self.assertEqual(scanned, 1)
        self.assertEqual(findings, [])

    def test_already_published_history_is_not_attributed_to_this_ref(self) -> None:
        """A personal address already on the base is out of scope for a new ref."""
        run_git(self.root, "checkout", "-q", "main")
        commit(self.root, "historic leak", PERSONAL, "d.txt")
        run_git(self.root, "checkout", "-q", "-b", "feature")
        commit(self.root, "clean work", PROJECT, "b.txt")
        findings, scanned = self.scan("feature", ["main"])
        self.assertEqual(scanned, 1, "only the new commit is in scope")
        self.assertEqual(findings, [])

    # ---- committer-only leak (the amend shape) --------------------------------------
    def test_committer_only_leak_is_caught(self) -> None:
        run_git(self.root, "checkout", "-q", "-b", "feature")
        Path(self.root, "b.txt").write_text("x\n", encoding="utf-8")
        run_git(self.root, "add", "b.txt")
        env = dict(
            os.environ,
            GIT_AUTHOR_NAME="The LEGEND project", GIT_AUTHOR_EMAIL=PROJECT,
            GIT_COMMITTER_NAME="The LEGEND project", GIT_COMMITTER_EMAIL=PERSONAL,
        )
        subprocess.run(
            ["git", "-C", self.root, "commit", "-m", "amended"],
            check=True, capture_output=True, text=True, env=env,
        )
        findings, _ = self.scan("feature", ["main"])
        self.assertEqual([f.field for f in findings], ["committer"])

    # ---- multiple bases --------------------------------------------------------------
    def test_multiple_bases_narrow_the_population(self) -> None:
        run_git(self.root, "checkout", "-q", "-b", "other")
        commit(self.root, "other work", PROJECT, "e.txt")
        run_git(self.root, "checkout", "-q", "-b", "feature")
        commit(self.root, "feature work", PROJECT, "f.txt")
        _, with_one = self.scan("feature", ["main"])
        _, with_two = self.scan("feature", ["main", "other"])
        self.assertEqual(with_one, 2)
        self.assertEqual(with_two, 1)

    # ---- CLI -------------------------------------------------------------------------
    def test_cli_requires_base(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).parent / "commit_metadata_scan.py"),
             "--root", self.root, "--ref", "main"],
            capture_output=True, text=True,
        )
        self.assertEqual(proc.returncode, 3)
        self.assertIn("--base is required", proc.stderr)

    def test_cli_blocks_and_does_not_echo_the_address(self) -> None:
        run_git(self.root, "checkout", "-q", "-b", "feature")
        commit(self.root, "leaky", PERSONAL, "b.txt")
        proc = subprocess.run(
            [sys.executable, str(Path(__file__).parent / "commit_metadata_scan.py"),
             "--root", self.root, "--ref", "feature", "--base", "main"],
            capture_output=True, text=True,
        )
        self.assertEqual(proc.returncode, 2)
        self.assertIn("BLOCK_PUBLICATION", proc.stdout)
        self.assertIn("NON_PROJECT_COMMIT_IDENTITY", proc.stdout)
        # a scanner that prints the address it objects to has published it
        self.assertNotIn(PERSONAL, proc.stdout)
        self.assertNotIn(PERSONAL, proc.stderr)


if __name__ == "__main__":
    unittest.main()
