"""Tests for disk_born.py on a temporary tree: born versus older-modified, hard links, areas, no-birth-time exit."""
import contextlib
import io
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import disk_born as d  # noqa: E402

PAUSE = 0.05  # file timestamps are coarse (a few ms)


def has_birth_time() -> bool:
    with tempfile.NamedTemporaryFile() as handle:
        return d.birth_time(handle.name) is not None


class Pure(unittest.TestCase):
    def test_a_worktree_is_one_area(self):
        self.assertEqual(d.area("/h/u/repo/.claude/worktrees/he_x/a/b/c.txt"), "/h/u/repo/.claude/worktrees/he_x")
        self.assertEqual(d.area("/h/u/.codex/sessions/2026/11/x.jsonl"), "/h/u/.codex/sessions")

    def test_naive_time_is_utc(self):
        self.assertEqual(d.parse_time("2026-11-28T14:48"), d.parse_time("2026-11-28T14:48:00Z"))
        self.assertEqual(d.parse_time("2026-11-28T15:48+01:00"), d.parse_time("2026-11-28T14:48Z"))

    def test_no_birth_time_exits_2_and_prints_no_zero_total(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root, "f").write_bytes(b"x")
            real = d.scan
            out = io.StringIO()
            with mock.patch.object(d, "scan", lambda r, s, u: real(r, s, u, birth=lambda _p: None)), \
                    contextlib.redirect_stdout(out):
                self.assertEqual(d.main(["--since", "2000-01-01", "--root", root]), 2)
            self.assertIn("NO_BIRTH_TIME", out.getvalue())
            self.assertNotIn("BORN 0", out.getvalue())


@unittest.skipUnless(has_birth_time(), "this filesystem records no birth time")
class Tree(unittest.TestCase):
    def test_born_versus_older_modified_and_hard_link_counted_once(self):
        with tempfile.TemporaryDirectory() as root:
            old = Path(root, "old.bin")
            old.write_bytes(b"x" * 8192)
            time.sleep(PAUSE)
            since = time.time()
            time.sleep(PAUSE)
            with old.open("ab") as handle:
                handle.write(b"y" * 8192)
            new = Path(root, "new.bin")
            new.write_bytes(b"z" * 40960)
            os.link(new, Path(root, "again.bin"))
            result = d.scan(root, since, time.time() + 1)
            self.assertEqual(sum(result["born"].values()), os.lstat(new).st_blocks * 512)
            self.assertEqual(sum(result["modified"].values()), os.lstat(old).st_blocks * 512)

    def test_a_window_after_everything_is_empty(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root, "f").write_bytes(b"x" * 4096)
            result = d.scan(root, time.time() + 60, time.time() + 120)
            self.assertEqual((sum(result["born"].values()), sum(result["modified"].values())), (0, 0))


if __name__ == "__main__":
    unittest.main(verbosity=2)
