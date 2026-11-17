#!/usr/bin/env python3
"""Tests for dropped_commits.py on a throw-away repository: a published tip, a tip reset away and never published, a tip reset away and re-landed as the same patch, and the rescue refs."""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import dropped_commits as dc  # noqa: E402

ENV = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}


def run(root: str, *args: str) -> str:
    return subprocess.run(["git", "-C", root, *args], check=True, capture_output=True, text=True, env=ENV).stdout.strip()


class DroppedCommits(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = self.tmp.name
        run(self.root, "init", "-q", "-b", "main")
        self.commit("base.txt", "base")
        run(self.root, "update-ref", "refs/remotes/development/main", "HEAD")

    def commit(self, name: str, text: str) -> str:
        (Path(self.root) / name).write_text(text, encoding="utf-8")
        run(self.root, "add", name)
        run(self.root, "commit", "-q", "-m", text)
        return run(self.root, "rev-parse", "HEAD")

    def test_a_reset_tip_is_dropped_until_its_patch_is_upstream_and_rescue_keeps_it(self) -> None:
        lost = self.commit("a.txt", "lost work")
        run(self.root, "reset", "-q", "--hard", "development/main")           # the reset the shared main suffered
        rows = {sha: verdict for sha, verdict, _, _ in dc.scan(self.root, "main", "development/main", 50)}
        self.assertEqual(rows.get(lost), "DROPPED")
        self.assertEqual(dc.main(["--root", self.root, "--rescue"]), 1)
        self.assertEqual(run(self.root, "rev-parse", f"refs/rescue/main/{lost[:12]}"), lost)       # kept from garbage collection
        run(self.root, "cherry-pick", "-x", lost)                              # the same patch lands under another SHA (-x changes the message, so the SHA differs)
        run(self.root, "update-ref", "refs/remotes/development/main", "HEAD")
        rows = {sha: verdict for sha, verdict, _, _ in dc.scan(self.root, "main", "development/main", 50)}
        self.assertEqual(rows.get(lost), "equivalent upstream")
        self.assertEqual(dc.main(["--root", self.root]), 0)

    def test_published_tips_are_not_listed_and_a_tip_on_another_branch_is_named(self) -> None:
        kept = self.commit("b.txt", "kept")
        run(self.root, "branch", "keep", kept)
        run(self.root, "reset", "-q", "--hard", "development/main")
        rows = {sha: verdict for sha, verdict, _, _ in dc.scan(self.root, "main", "development/main", 50)}
        self.assertEqual(rows.get(kept), "on branch keep")
        self.assertNotIn(run(self.root, "rev-parse", "development/main"), rows)       # a published tip is not reported

    def test_a_missing_upstream_is_refused_not_read_as_clean(self) -> None:
        self.assertEqual(dc.main(["--root", self.root, "--upstream", "nowhere/main"]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
