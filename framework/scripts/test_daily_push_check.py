#!/usr/bin/env python3
"""The daily report detects local-only commits and uses Rome wall-clock time."""

from __future__ import annotations

import datetime as dt
from pathlib import Path
import subprocess
import tempfile
import unittest

import daily_push_check as check


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True,
                            check=True)
    return result.stdout.strip()


class DailyPushCheckTests(unittest.TestCase):
    def test_remote_alias_is_identified_by_url(self) -> None:
        self.assertTrue(check.is_development_url(
            f"git{chr(64)}github.com:marinomassimo-dot/legend-development.git"))
        self.assertTrue(check.is_development_url(
            "https://github.com/marinomassimo-dot/legend-development"))
        self.assertFalse(check.is_development_url(
            f"git{chr(64)}github.com:someone-else/legend-development.git"))

    def test_rome_run_occurs_at_the_two_utc_hours_across_dst(self) -> None:
        self.assertTrue(check.scheduled_time(dt.datetime(
            2026, 1, 15, 18, 45, tzinfo=dt.timezone.utc)))
        self.assertTrue(check.scheduled_time(dt.datetime(
            2026, 7, 15, 17, 45, tzinfo=dt.timezone.utc)))
        self.assertFalse(check.scheduled_time(dt.datetime(
            2026, 7, 15, 18, 45, tzinfo=dt.timezone.utc)))

    def test_commit_absent_from_remote_main_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "-q", "-b", "main")
            git(root, "config", "user.name", "Test")
            git(root, "config", "user.email", "test@example.invalid")
            (root / "file").write_text("first\n")
            git(root, "add", "file")
            git(root, "commit", "-q", "-m", "base")
            base = git(root, "rev-parse", "HEAD")
            (root / "file").write_text("second\n")
            git(root, "commit", "-q", "-am", "new")
            rows = check.local_branches(root, base)
            self.assertEqual(1, len(rows))
            self.assertEqual("main", rows[0]["branch"])
            self.assertEqual(1, rows[0]["commits_absent_from_remote_main"])
            self.assertEqual(1, rows[0]["novel_patches"])
            self.assertEqual([], check.local_branches(root, git(root, "rev-parse", "HEAD")))

    def test_cherry_picked_content_is_not_reported_again(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "-q", "-b", "main")
            git(root, "config", "user.name", "Test")
            git(root, "config", "user.email", "example@example.com")
            (root / "file").write_text("base\n")
            git(root, "add", "file")
            git(root, "commit", "-q", "-m", "base")
            base = git(root, "rev-parse", "HEAD")
            (root / "file").write_text("base\naddition\n")
            git(root, "commit", "-q", "-am", "original")
            git(root, "switch", "-q", "-c", "duplicate", base)
            (root / "file").write_text("base\naddition\n")
            git(root, "commit", "-q", "-am", "same patch, new ID")
            self.assertEqual([], check.local_branches(root, git(root, "rev-parse", "main")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
