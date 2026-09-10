#!/usr/bin/env python3
"""Regressions for `scripts/legend_commit.sh`.

Written the way the 2026-09-09 retrospective § 4.1 says this suite was not written the
first time. The wrapper's original smoke test verified that it declines to make an empty
commit — a real property, and not the one that was broken. What broke was argument
ordering with a message containing spaces alongside a `--` pathspec, and the first actor
to use the tool hit it. So the first test below is that exact invocation.

The other two pin the properties three concurrent actors actually depend on: a commit
scoped to the paths named, leaving a peer's in-flight file untouched and unstaged, and a
lock that serialises two simultaneous commits instead of racing on `.git/index.lock`.
"""

from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "scripts" / "legend_commit.sh"


def git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=repo, check=True, capture_output=True, text=True
    ).stdout.strip()


class LegendCommitWrapper(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self._tmp.name)
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "config", "user.email", "test@example.invalid")
        git(self.repo, "config", "user.name", "test")
        (self.repo / "seed.txt").write_text("seed\n", encoding="utf-8")
        git(self.repo, "add", "seed.txt")
        git(self.repo, "commit", "-q", "-m", "seed")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def run_wrapper(self, message: str, *paths: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["bash", str(WRAPPER), message, *paths],
            cwd=self.repo, capture_output=True, text=True,
        )

    def test_message_with_spaces_survives_the_pathspec_separator(self) -> None:
        """The defect of 2026-09-08: `-m` after `--`, a message eaten as a pathspec."""
        (self.repo / "mine.txt").write_text("mine\n", encoding="utf-8")
        message = "A subject with spaces\n\nAnd a body paragraph."
        result = self.run_wrapper(message, "mine.txt")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertEqual(message, git(self.repo, "log", "-1", "--format=%B").strip())

    def test_commit_is_scoped_and_leaves_a_peers_file_untouched(self) -> None:
        """A peer's in-flight edit to a TRACKED file is the case that matters.

        An untracked peer file is safe under almost any implementation — `git commit -a`
        would leave it alone too — so testing only that would be the adjacent property
        again. The dangerous shape is a peer midway through editing a file this
        repository already tracks while another actor commits.
        """
        (self.repo / "mine.txt").write_text("mine\n", encoding="utf-8")
        (self.repo / "seed.txt").write_text("peer is editing this\n", encoding="utf-8")
        (self.repo / "peer_new.txt").write_text("peer in flight\n", encoding="utf-8")
        result = self.run_wrapper("scoped commit", "mine.txt")
        self.assertEqual(0, result.returncode, result.stderr)
        committed = git(self.repo, "show", "--name-only", "--format=", "HEAD").split()
        self.assertEqual(["mine.txt"], committed)
        unstaged = git(self.repo, "diff", "--name-only").split()
        staged = git(self.repo, "diff", "--cached", "--name-only").split()
        untracked = git(
            self.repo, "ls-files", "--others", "--exclude-standard"
        ).split()
        self.assertEqual(["seed.txt"], unstaged)
        self.assertEqual([], staged)
        self.assertEqual(["peer_new.txt"], untracked)

    def test_nothing_to_commit_is_reported_and_not_an_error(self) -> None:
        result = self.run_wrapper("no change here", "seed.txt")
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("NOTHING_TO_COMMIT", result.stdout)

    def test_too_few_arguments_is_refused(self) -> None:
        result = self.run_wrapper("message only")
        self.assertEqual(2, result.returncode)

    def test_the_lock_serialises_two_concurrent_commits(self) -> None:
        """Both commits land, in some order, and neither dies on .git/index.lock."""
        (self.repo / "a.txt").write_text("a\n", encoding="utf-8")
        (self.repo / "b.txt").write_text("b\n", encoding="utf-8")
        env = dict(os.environ)
        procs = [
            subprocess.Popen(
                ["bash", str(WRAPPER), f"concurrent {name}", f"{name}.txt"],
                cwd=self.repo, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, env=env,
            )
            for name in ("a", "b")
        ]
        for proc in procs:
            out, err = proc.communicate(timeout=120)
            self.assertEqual(0, proc.returncode, err or out)
        subjects = git(self.repo, "log", "--format=%s", "-2").splitlines()
        self.assertEqual({"concurrent a", "concurrent b"}, set(subjects))


if __name__ == "__main__":
    unittest.main(verbosity=2)
