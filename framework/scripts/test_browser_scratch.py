"""browser_scratch: a failing or timed-out browser run leaves no profile folder and no child process behind."""
import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import browser_scratch as bs  # noqa: E402

# A stand-in "browser": writes into its profile, starts a child that keeps writing, then hangs or fails.
FAKE = r"""
import os, subprocess, sys, time
profile = [a.split('=', 1)[1] for a in sys.argv if a.startswith('--user-data-dir=')][0]
os.makedirs(profile + '/Cache', exist_ok=True)
open(profile + '/Cache/data', 'w').write('x' * 1000)
child = subprocess.Popen([sys.executable, '-c', "import sys,time\nwhile True:\n open(sys.argv[1]+'/Cache/more','a').write('y'); time.sleep(0.05)", profile])
mode = sys.argv[1]
if mode == 'hang':
    time.sleep(600)
sys.exit(3 if mode == 'fail' else 0)
"""


def alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return Path(f"/proc/{pid}/status").read_text().split("State:")[1].split()[0] != "Z"
    except (OSError, IndexError):
        return False


class BrowserScratch(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="bs-test-"))
        self.addCleanup(bs.remove_tree, str(self.root))
        self.script = self.root / "fake.py"
        self.script.write_text(FAKE)
        self.profile = self.root / "p"

    def cmd(self, mode):
        return [sys.executable, str(self.script), mode, f"--user-data-dir={self.profile}"]

    def children(self):
        return bs._holders(str(self.profile))

    def test_failing_run_leaves_no_folder_and_no_child(self):
        done = bs.run_browser(self.cmd("fail"), timeout=20)
        self.assertEqual(done.returncode, 3)
        self.assertEqual([p for p in self.children() if alive(p)], [])
        self.assertTrue(bs.remove_tree(str(self.root)))
        self.assertFalse(self.root.exists())

    def test_timed_out_run_kills_the_whole_group(self):
        with self.assertRaises(subprocess.TimeoutExpired):
            bs.run_browser(self.cmd("hang"), timeout=1)
        time.sleep(0.3)
        self.assertEqual([p for p in self.children() if alive(p)], [])
        self.assertTrue(bs.remove_tree(str(self.root)))
        self.assertFalse(self.root.exists())

    def test_remove_tree_stops_a_live_writer_then_removes(self):
        subprocess.Popen([sys.executable, str(self.script), "hang", f"--user-data-dir={self.profile}"], start_new_session=True)
        time.sleep(0.5)
        self.assertTrue(self.profile.exists())
        self.assertTrue(bs.remove_tree(str(self.root)))
        self.assertFalse(self.root.exists())


class ClassLevelCleanup(unittest.TestCase):
    """The shape used by test_repurposing_view.Browser: the class-level folder is gone after a run in which a test failed."""

    def test_class_cleanup_removes_the_folder_after_a_failing_test(self):
        holder = {}

        class Inner(unittest.TestCase):
            @classmethod
            def setUpClass(cls):
                cls.tmp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
                cls.addClassCleanup(bs.remove_tree, cls.tmp.name)
                holder["path"] = cls.tmp.name
                (Path(cls.tmp.name) / "p").mkdir()

            def test_fails(self):
                self.fail("deliberate")

        result = unittest.TextTestRunner(stream=open(os.devnull, "w")).run(unittest.defaultTestLoader.loadTestsFromTestCase(Inner))
        self.assertEqual(len(result.failures), 1)
        self.assertFalse(Path(holder["path"]).exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
