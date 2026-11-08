"""Regressions for `owned_scratch.py`: two runs never share a box, and a claim is not a licence.

The 2026-11-08 incident: a session reused the name of a directory in which another session's
release battery was running and moved its checkout under it. These tests run two real processes
at once and check that neither can touch the other's checkout or artefacts, that an existing
directory is never adopted by name, that only a dead owner's (or one's own) box can be removed,
and that a recycled PID does not keep a box alive.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import owned_scratch  # noqa: E402
import process_wait  # noqa: E402

TOOL = HERE / "owned_scratch.py"
PREFIX = "legend-owned-test-"


def run_tool(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True,
                          timeout=120)


def git(cwd: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(cwd), *args], check=True, capture_output=True,
                          text=True).stdout


# One concurrent run: makes its own box through the command line, clones the toy repository into
# it, writes an artefact, moves its checkout to its own commit, and waits to be released.
RUN = """
import subprocess, sys, time
from pathlib import Path
tool, src, tag, ready, go = sys.argv[1:6]
box = Path(subprocess.run([sys.executable, tool, "--make", "{prefix}"], check=True,
                          capture_output=True, text=True).stdout.strip())
clone = box / "clone"
subprocess.run(["git", "clone", "-q", "--no-hardlinks", src, str(clone)], check=True)
subprocess.run(["git", "-C", str(clone), "checkout", "-q", "-b", tag], check=True)
(clone / "tracked.txt").write_text(tag + "\\n")
subprocess.run(["git", "-C", str(clone), "-c", "user.name=t", "-c", "user.email=",
                "commit", "-qam", tag], check=True)
(box / "artefact.txt").write_text(tag + "\\n")
subprocess.run([sys.executable, tool, "--adopt", str(box), "--owner", str(__import__("os").getpid())],
               check=True, capture_output=True)
Path(ready).write_text(str(box))
while not Path(go).exists():
    time.sleep(0.05)
""".format(prefix=PREFIX)


class ConcurrentRuns(unittest.TestCase):
    def setUp(self):
        self.work = Path(tempfile.mkdtemp(prefix="legend-owned-test-work-"))
        self.addCleanup(subprocess.run, ["rm", "-rf", str(self.work)])
        self.src = self.work / "src"
        subprocess.run(["git", "init", "-q", str(self.src)], check=True)
        (self.src / "tracked.txt").write_text("base\n")
        git(self.src, "add", "tracked.txt")
        git(self.src, "-c", "user.name=t", "-c", "user.email=", "commit", "-qm", "base")
        self.procs: list[subprocess.Popen] = []
        self.addCleanup(self._stop)

    def _stop(self):
        (self.work / "go").write_text("")
        for proc in self.procs:
            try:
                proc.wait(timeout=30)
            except subprocess.TimeoutExpired:
                proc.kill()
        for box in Path(tempfile.gettempdir()).glob(PREFIX + "*"):
            if box.is_dir() and not owned_scratch.owner_alive(box):
                owned_scratch.release(box)

    def start(self, tag: str) -> Path:
        ready = self.work / f"ready-{tag}"
        proc = subprocess.Popen([sys.executable, "-c", RUN, str(TOOL), str(self.src), tag,
                                 str(ready), str(self.work / "go")])
        self.procs.append(proc)
        deadline = time.time() + 60
        while not ready.exists():
            self.assertLess(time.time(), deadline, "a run did not come up")
            self.assertIsNone(proc.poll(), "a run died before it was ready")
            time.sleep(0.05)
        return Path(ready.read_text())

    def test_two_concurrent_runs_get_distinct_boxes_and_cannot_touch_each_other(self):
        a, b = self.start("alpha"), self.start("beta")
        self.assertNotEqual(a, b)
        # Each checkout and artefact is its own run's, after the other has run to completion.
        for box, tag, other in ((a, "alpha", "beta"), (b, "beta", "alpha")):
            self.assertEqual((box / "clone" / "tracked.txt").read_text(), tag + "\n")
            self.assertEqual((box / "artefact.txt").read_text(), tag + "\n")
            self.assertEqual(git(box / "clone", "rev-parse", "--abbrev-ref", "HEAD").strip(), tag)
            self.assertNotIn(other, git(box / "clone", "log", "--format=%s"))
        # The one thing that put the incident right: neither can release or reap the other's box.
        refused = run_tool("--release", str(a))
        self.assertEqual(refused.returncode, 2, refused.stderr)
        self.assertIn("still running", refused.stderr)
        self.assertEqual(run_tool("--prefix", PREFIX).stdout.splitlines()[-1], "0 box(es)")
        self.assertTrue((a / "clone" / "tracked.txt").exists() and (b / "clone" / "tracked.txt").exists())

    def test_a_run_that_ends_leaves_a_box_the_next_reap_removes_and_only_that_one(self):
        a, b = self.start("alpha"), self.start("beta")
        owner_a = owned_scratch.owner_of(a)
        os.kill(owner_a[0], 9)
        for proc in self.procs:
            if proc.pid == owner_a[0]:
                proc.wait(timeout=30)
        out = run_tool("--prefix", PREFIX).stdout
        self.assertIn(str(a), out)
        self.assertFalse(a.exists())
        self.assertTrue(b.exists())


class ClaimIsNotALicence(unittest.TestCase):
    def setUp(self):
        self.made: list[Path] = []
        self.addCleanup(self._clean)

    def _clean(self):
        for path in self.made:
            if path.exists():
                (path / owned_scratch.OWNER).write_text("999999999\n") if (path / owned_scratch.OWNER).exists() else None
                subprocess.run(["rm", "-rf", str(path)])

    def box(self, owner_text: str | None) -> Path:
        path = Path(tempfile.mkdtemp(prefix=PREFIX))
        self.made.append(path)
        if owner_text is not None:
            (path / owned_scratch.OWNER).write_text(owner_text + "\n")
        return path

    def test_make_never_returns_an_existing_directory(self):
        taken = self.box(None)
        (taken / "somebody-elses-checkout").write_text("keep\n")
        fresh = [owned_scratch.make(PREFIX) for _ in range(3)]
        self.made.extend(fresh)
        self.assertEqual(len({str(p) for p in fresh} | {str(taken)}), 4)
        self.assertEqual((taken / "somebody-elses-checkout").read_text(), "keep\n")

    def test_a_directory_with_the_prefix_but_no_owner_file_is_neither_reaped_nor_released(self):
        foreign = self.box(None)
        (foreign / "work").write_text("a human's directory\n")
        old = time.time() - 7 * 86400
        os.utime(foreign, (old, old))              # even a week old, it is not ours to judge
        self.assertNotIn(foreign, owned_scratch.reap(PREFIX))
        with self.assertRaises(owned_scratch.Refused):
            owned_scratch.release(foreign)
        self.assertTrue((foreign / "work").exists())

    def test_release_refuses_a_box_whose_owner_still_runs_and_allows_a_dead_one(self):
        sleeper = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(60)"])
        self.addCleanup(sleeper.kill)
        live = self.box(process_wait_identity(sleeper.pid))
        with self.assertRaises(owned_scratch.Refused):
            owned_scratch.release(live)
        self.assertTrue(live.exists())
        sleeper.kill()
        sleeper.wait()
        owned_scratch.release(live)
        self.assertFalse(live.exists())

    def test_release_refuses_paths_that_are_not_boxes(self):
        with tempfile.TemporaryDirectory(prefix="legend-owned-test-outer-") as outer:
            nested = Path(outer) / "inner"
            nested.mkdir()
            (nested / owned_scratch.OWNER).write_text(f"{os.getpid()}\n")
            with self.assertRaises(owned_scratch.Refused):      # owner file, but not in /tmp itself
                owned_scratch.release(nested)
            self.assertTrue(nested.exists())
        target = self.box(f"{os.getpid()}")
        link = Path(tempfile.gettempdir()) / (PREFIX + "link")
        link.symlink_to(target)
        self.addCleanup(link.unlink)
        with self.assertRaises(owned_scratch.Refused):
            owned_scratch.release(link)
        self.assertTrue(target.exists())

    def test_a_recycled_pid_does_not_keep_a_box_alive_but_an_unrecorded_start_does(self):
        me = os.getpid()
        start = process_wait.start_ticks(me)
        self.assertIsNotNone(start)
        recycled = self.box(f"{me}:{start + 1}")        # same PID, a different incarnation
        no_start = self.box(f"{me}")                    # start unknowable: kept, the safe side
        reaped = owned_scratch.reap(PREFIX)
        self.assertIn(recycled, reaped)
        self.assertNotIn(no_start, reaped)
        self.assertFalse(recycled.exists())


def process_wait_identity(pid: int) -> str:
    return f"{pid}:{process_wait.start_ticks(pid)}"


if __name__ == "__main__":
    unittest.main(verbosity=2)
