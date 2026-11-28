"""Tests for disk_writer_trace.py: the drop detector, the /proc readers and a one-second end-to-end run (no large writes)."""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import disk_writer_trace as t  # noqa: E402


class Drops(unittest.TestCase):
    def test_finds_only_drops_at_the_threshold(self):
        self.assertEqual(t.drops([1000, 950, 840, 900, 800], 100), [(2, 110.0), (4, 100.0)])

    def test_no_drop_in_a_rising_series(self):
        self.assertEqual(t.drops([100, 200, 300], 50), [])


class Proc(unittest.TestCase):
    def test_reads_own_process_io_and_open_file(self):
        writes = t.proc_writes()
        self.assertIn(os.getpid(), writes)
        with tempfile.NamedTemporaryFile() as handle:
            handle.write(b"x" * 4096)
            handle.flush()
            size, target = t.biggest_open_file(os.getpid())
            self.assertGreaterEqual(size, 4096)
            self.assertTrue(target.startswith("/"))


class EndToEnd(unittest.TestCase):
    def test_short_run_writes_a_small_tsv_and_only_that(self):
        with tempfile.TemporaryDirectory() as td:
            watched = Path(td) / "w"
            watched.mkdir()
            out = Path(td) / "trace.tsv"
            done = subprocess.run([sys.executable, "-I", str(HERE / "disk_writer_trace.py"), "--out", str(out), "--minutes", "0.03",
                                   "--interval", "0.5", "--drop-mb", "100000000", "--path", td, "--watch", str(watched)],
                                  capture_output=True, text=True, timeout=60)
            self.assertEqual(done.returncode, 0, done.stderr)
            text = out.read_text()
            self.assertTrue(text.startswith("kind\ttime\tfree_mb\tmeasure\tdetail\n"))
            self.assertIn("summary", text)
            self.assertLess(len(text), 20000)
            self.assertEqual(sorted(p.name for p in Path(td).iterdir()), ["trace.tsv", "w"])

    def test_a_drop_row_names_the_directory_and_a_process(self):
        with tempfile.TemporaryDirectory() as td:
            watched = Path(td) / "w"
            watched.mkdir()
            seq = iter([10000.0, 9000.0, 9000.0])
            real = t.shutil.disk_usage
            t.shutil.disk_usage = lambda p: type("U", (), {"free": int(next(seq) * t.MB)})()
            try:
                calls = {"n": 0}
                now = {"t": 1000.0}

                def sleep(_):
                    calls["n"] += 1
                    now["t"] += 10
                    (watched / f"f{calls['n']}").write_bytes(b"y" * 2048)
                out = Path(td) / "trace.tsv"
                t.run(td, 0.3, 10, 100, [str(watched)], out, sleep=sleep, clock=lambda: now["t"])
            finally:
                t.shutil.disk_usage = real
            text = out.read_text()
            self.assertIn("DROP", text)
            self.assertIn("dir\t", text)
            self.assertIn("summary", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
