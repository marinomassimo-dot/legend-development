#!/usr/bin/env python3
"""Regressions for safe_push.py — every one is a refusal path, because the refusals are the tool."""
from __future__ import annotations
import os, subprocess, sys, time, unittest
from pathlib import Path
from tempfile import TemporaryDirectory

TOOL = Path(__file__).resolve().parent / "safe_push.py"
# The publishers under test must not count the real machine's live gates (safe_push step 17): their /proc is an empty folder.
_NO_PROCESSES = TemporaryDirectory(prefix="safe-push-test-proc-")
os.environ["LEGEND_SAFE_PUSH_PROC_ROOT"] = _NO_PROCESSES.name
# Nor may a short disk on this machine turn them red (2026-11-28: two real-clone publications failed at 1.1 and 2.0 GB free, and a landing runs this suite).
# The tests of the disk rule set their own floor.
os.environ["LEGEND_SAFE_PUSH_MIN_FREE_GB"] = "0"

GATE_PASS = "import sys\nprint('VERDICT: PASS')\nprint('BLOCKS: 0')\nsys.exit(0)\n"
GATE_BLOCK = ("import sys\nprint('VERDICT: BLOCK_PUBLICATION')\n"
              "print('[BLOCK] EMAIL_ADDRESS somewhere')\nsys.exit(2)\n")


class SafePushRefusals(unittest.TestCase):
    def _repo(self, td: str, gate_src: str) -> Path:
        root = Path(td) / "repo"
        (root / "scripts").mkdir(parents=True)
        (root / "scripts" / "gate.py").write_text(gate_src, encoding="utf-8")
        subprocess.run(["git", "init", "-q", str(root)], check=True)
        # Assembled rather than written literally: the publication gate screens public
        # material for address-shaped strings, and a throwaway git fixture is not a reason
        # to make it choose between a false positive and a blind spot.
        fixture_identity = "fixture" + "@" + "invalid"
        subprocess.run(["git", "-C", str(root), "config", "user.email", fixture_identity],
                       check=True)
        subprocess.run(["git", "-C", str(root), "config", "user.name", "t"], check=True)
        (root / "a.txt").write_text("a\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", "init"], check=True)
        return root

    def _run(self, root: Path, *args: str):
        env = dict(os.environ,
                   LEGEND_SAFE_PUSH_ROOT=str(root),
                   LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"))
        return subprocess.run([sys.executable, str(TOOL), *args],
                              capture_output=True, text=True, env=env)

    def test_a_dirty_tree_is_refused_before_the_gate_runs(self) -> None:
        with TemporaryDirectory() as td:
            root = self._repo(td, GATE_PASS)
            (root / "dirt.txt").write_text("x\n", encoding="utf-8")
            r = self._run(root, "origin", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("working tree is not clean", r.stderr)

    def test_a_short_disk_is_refused_at_the_start_before_the_gate_and_before_any_lock(self) -> None:
        """2026-11-24: / was 100% full and a landing died midway with 'No space left on device'. Now it is a one-second refusal that names the number."""
        with TemporaryDirectory() as td:
            marker = Path(td) / "gate-ran"
            root = self._repo(td, f"open({str(marker)!r}, 'w').close()\n" + GATE_PASS)
            env = dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"),
                       LEGEND_SAFE_PUSH_MIN_FREE_GB="100000000")        # no machine has this much free
            r = subprocess.run([sys.executable, str(TOOL), "origin", "main", "--serialize"], capture_output=True, text=True, env=env)
            self.assertEqual(r.returncode, 1)
            self.assertIn("free space", r.stderr)
            self.assertIn("below", r.stderr)
            self.assertIn("Nothing was gated or pushed", r.stderr)
            self.assertFalse(marker.exists(), "the gate must not run on a short disk")
            self.assertNotIn("landing lock", r.stdout + r.stderr)

    def test_the_free_space_check_reads_both_filesystems_and_names_the_scarcer_one(self) -> None:
        import importlib.util
        from unittest import mock
        spec = importlib.util.spec_from_file_location("safe_push_under_test", TOOL)
        sp = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(sp)
        usage = lambda free: mock.Mock(free=free)
        with mock.patch.object(sp, "MIN_FREE_GB", 2.0):
            with mock.patch.object(sp.shutil, "disk_usage", return_value=usage(50e9)):
                self.assertEqual(sp.free_space_refusal(), "")
            with mock.patch.object(sp.shutil, "disk_usage", side_effect=lambda p: usage(0.5e9 if str(p) == str(sp.ROOT) else 50e9)):
                msg = sp.free_space_refusal()
            self.assertIn("0.5 GB", msg)
            self.assertIn(str(sp.ROOT), msg)
            with mock.patch.object(sp.shutil, "disk_usage", side_effect=OSError("unreadable")):
                self.assertEqual(sp.free_space_refusal(), "")

    def test_a_blocking_gate_refuses_the_push(self) -> None:
        """The defect of 2026-09-09: the gate said BLOCK and the push went anyway."""
        with TemporaryDirectory() as td:
            r = self._run(self._repo(td, GATE_BLOCK), "origin", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("not PASS", r.stderr)
            self.assertIn("Nothing was pushed", r.stderr)

    def test_how_the_gate_ran_and_why_it_failed_closed_reach_the_log(self) -> None:
        source = ("import sys\nsys.stderr.write('GATE_SIDE_SCANS: serial, FALLBACK (x)\\nnoise\\nGATE_ERROR: boom\\n')\n"
                  "sys.exit(3)\n")
        with TemporaryDirectory() as td:
            r = self._run(self._repo(td, source), "origin", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("GATE_SIDE_SCANS: serial, FALLBACK (x)", r.stdout)
            self.assertIn("GATE_ERROR: boom", r.stdout)
            self.assertNotIn("noise", r.stdout)

    def test_force_spellings_are_refused(self) -> None:
        with TemporaryDirectory() as td:
            root = self._repo(td, GATE_PASS)
            for bad in ("+main", "--force", "-f"):
                with self.subTest(bad=bad):
                    r = self._run(root, "origin", bad)
                    self.assertEqual(r.returncode, 1)
                    self.assertIn("fast-forward only", r.stderr)

    def test_usage_is_refused_rather_than_guessed(self) -> None:
        with TemporaryDirectory() as td:
            r = self._run(self._repo(td, GATE_PASS))
            self.assertEqual(r.returncode, 1)
            self.assertIn("usage", r.stderr)

    def test_help_prints_and_does_nothing_else(self) -> None:
        """`--help` was once taken as the remote name and walked the whole push workflow."""
        with TemporaryDirectory() as td:
            marker = Path(td) / "gate-ran"
            root = self._repo(td, f"open({str(marker)!r}, 'w').close()\n" + GATE_PASS)
            for args in (("--help",), ("-h",), ("origin", "--help")):
                with self.subTest(args=args):
                    r = self._run(root, *args)
                    self.assertEqual(r.returncode, 0, r.stderr)
                    self.assertIn("Usage: safe_push.py", r.stdout)
                    self.assertNotIn("HEAD before gate", r.stdout)
                    self.assertFalse(marker.exists(), "the gate ran for a help request")

    def test_option_shaped_arguments_are_refused_before_any_git_activity(self) -> None:
        with TemporaryDirectory() as td:
            marker = Path(td) / "gate-ran"
            root = self._repo(td, f"open({str(marker)!r}, 'w').close()\n" + GATE_PASS)
            for args in (("-x",), ("--verbose", "main"), ("origin", "-q")):
                with self.subTest(args=args):
                    r = self._run(root, *args)
                    self.assertEqual(r.returncode, 1)
                    self.assertIn("option-shaped", r.stderr)
                    self.assertFalse(marker.exists())

    def _with_bare_remote(self, td: str) -> tuple[Path, Path]:
        root = self._repo(td, GATE_PASS)
        subprocess.run(["git", "-C", str(root), "branch", "-M", "main"], check=True)
        bare = Path(td) / "remote.git"
        subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
        subprocess.run(["git", "-C", str(root), "remote", "add", "origin", str(bare)], check=True)
        subprocess.run(["git", "-C", str(root), "push", "-q", "origin", "HEAD:refs/heads/main"],
                       check=True)
        return root, bare

    def _commit(self, root: Path, name: str) -> str:
        (root / name).write_text(name + "\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", name], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", name], check=True)
        return subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], check=True,
                              capture_output=True, text=True).stdout.strip()

    def _remote_main(self, bare: Path) -> str:
        return subprocess.run(["git", "-C", str(bare), "rev-parse", "refs/heads/main"],
                              check=True, capture_output=True, text=True).stdout.strip()

    def test_the_commit_pushed_is_the_commit_gated_not_the_local_branch(self) -> None:
        """HEAD ahead of a stale local `main`: the gated HEAD is what the remote receives."""
        with TemporaryDirectory() as td:
            root, bare = self._with_bare_remote(td)
            subprocess.run(["git", "-C", str(root), "checkout", "-q", "--detach"], check=True)
            gated = self._commit(root, "b.txt")
            stale_local_main = subprocess.run(["git", "-C", str(root), "rev-parse", "main"],
                                              check=True, capture_output=True, text=True).stdout.strip()
            self.assertNotEqual(gated, stale_local_main)
            r = self._run(root, "origin", "main")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(self._remote_main(bare), gated)

    def test_a_non_fast_forward_is_refused_and_the_remote_is_unchanged(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._with_bare_remote(td)
            self._commit(root, "b.txt")
            subprocess.run(["git", "-C", str(root), "push", "-q", "origin", "HEAD:refs/heads/main"],
                           check=True)
            published = self._remote_main(bare)
            subprocess.run(["git", "-C", str(root), "checkout", "-q", "--detach", "HEAD~1"],
                           check=True)
            self._commit(root, "c.txt")   # diverges from the published tip
            r = self._run(root, "origin", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("git push exited", r.stderr)
            self.assertEqual(self._remote_main(bare), published)

    def test_a_moved_main_cannot_publish_a_commit_the_caller_did_not_mean(self) -> None:
        """IT35 P2: the 2026-11-07 incident. Main holds another session's unpublished integration commit; the caller wanted a candidate that
        `git merge --ff-only` could not bring in. Without the expectation the tool publishes HEAD (gate PASS on what it pushes); with it, the
        push is refused before the gate and the remote is unchanged."""
        with TemporaryDirectory() as td:
            root, bare = self._with_bare_remote(td)
            base = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
            subprocess.run(["git", "-C", str(root), "checkout", "-q", "-b", "candidate"], check=True)
            candidate = self._commit(root, "candidate.txt")
            subprocess.run(["git", "-C", str(root), "checkout", "-q", "main"], check=True)
            other = self._commit(root, "other_session.txt")                      # the unpublished integration commit now at HEAD
            ff = subprocess.run(["git", "-C", str(root), "merge", "--ff-only", candidate], capture_output=True, text=True)
            self.assertNotEqual(ff.returncode, 0)                                # the integration the caller expected fails
            r = self._run(root, "origin", "main", "--expect-sha", candidate)
            self.assertEqual(r.returncode, 1)
            self.assertIn("caller expected", r.stderr)
            self.assertNotIn("PUBLISHED", r.stdout)
            self.assertEqual(self._remote_main(bare), base)
            ok = self._run(root, "origin", "main", f"--expect-sha={other[:12]}")  # the intended commit, abbreviated: accepted
            self.assertEqual(ok.returncode, 0, ok.stderr)
            self.assertEqual(self._remote_main(bare), other)
            bad = self._run(root, "origin", "main", "--expect-sha", "no-such-rev")
            self.assertEqual(bad.returncode, 1)
            self.assertIn("not a commit", bad.stderr)

    def test_a_passing_gate_reaches_the_push_step(self) -> None:
        """Control: the PASS path is not refused early — it fails at the absent remote instead."""
        with TemporaryDirectory() as td:
            r = self._run(self._repo(td, GATE_PASS), "nosuchremote", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("git push exited", r.stderr)
            self.assertNotIn("working tree", r.stderr)
            self.assertNotIn("not PASS", r.stderr)


def _load_tool():
    import importlib.util
    spec = importlib.util.spec_from_file_location("safe_push_under_test", TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _fake_proc(root: Path, table) -> Path:
    """A /proc-shaped folder from (pid, ppid, argv, environ) rows."""
    for pid, ppid, argv, env in table:
        d = root / str(pid)
        d.mkdir()
        (d / "stat").write_text(f"{pid} (x y) S {ppid} 0 0\n")
        (d / "cmdline").write_bytes("\0".join(argv).encode() + b"\0")
        (d / "environ").write_bytes("\0".join(env).encode())
    return root


class SafePushDiskCountsLiveRuns(unittest.TestCase):
    """Step 17 (2026-11-28): the free-space floor adds the declared peak of every OTHER live run that writes clones, and a publisher waits for that space instead of refusing at once."""

    def test_only_working_runs_of_other_families_are_counted(self) -> None:
        sp = _load_tool()
        gate = ["python3", "scripts/public_release_gate.py"]
        push = ["python3", "framework/scripts/safe_push.py", "development", "main", "--serialize"]
        table = [
            (10, 1, ["bash", "-c", "python3 framework/scripts/safe_push.py development main"], []),      # names it, is not it
            (11, 10, ["timeout", "560", *push], []),
            (12, 11, push, []),                                                                             # working: has a child
            (13, 12, gate, []),                                                                             # staging gate: no clone
            (14, 12, ["python3", "-B", "framework/scripts/candidate_tree_freshness.py", "--regenerate"], []),  # same family as 12
            (20, 1, push, []),                                                                              # queued: no child
            (30, 1, ["python3", "-B", "-u", "framework/scripts/candidate_tree_freshness.py", "--regenerate"], []),
            (31, 1, [*gate, "--mode", "release"], []),
            (40, 1, push, ["LEGEND_SAFE_PUSH_ROOT=/tmp/fixture"]),                                         # a test fixture
            (41, 40, ["git", "status"], []),
            (50, 1, push, []),                                                                              # my own family
            (51, 50, ["python3", "framework/scripts/test_x.py"], []),                                      # me
            (52, 50, ["python3", "scripts/run_release_regressions.py"], []),
            (53, 51, ["python3", "scripts/run_release_regressions.py"], []),
        ]
        with TemporaryDirectory() as td:
            got = sp.live_heavy_runs(_fake_proc(Path(td), table), me=51)
        self.assertEqual([(pid, name) for pid, name, _ in got],
                         [(12, "safe_push.py"), (30, "candidate_tree_freshness.py"), (31, "public_release_gate.py")])

    def _space(self, sp, free_gb, runs):
        from unittest import mock
        usage = mock.Mock(side_effect=lambda p: mock.Mock(free=free_gb.pop(0) * 1e9 if len(free_gb) > 1 else free_gb[0] * 1e9))
        return (mock.patch.object(sp.shutil, "disk_usage", usage), mock.patch.object(sp, "live_heavy_runs", side_effect=runs),
                mock.patch.object(sp, "MIN_FREE_GB", 2.0), mock.patch.object(sp, "DISK_POLL_S", 0.01))

    def test_space_that_covers_one_clone_but_not_a_second_run_is_waited_for_then_refused(self) -> None:
        sp = _load_tool()
        one = [(777, "safe_push.py", 1.4)]
        patches = self._space(sp, [2.5], lambda *a: one)
        with patches[0], patches[1], patches[2], patches[3], mock_wait(sp, 0.05):
            msg = sp.wait_for_space()
        self.assertIn("below 3.4 GB", msg)
        self.assertIn("pid 777 safe_push.py", msg)
        self.assertIn("Waited", msg)
        self.assertIn("Nothing was gated or pushed", msg)

    def test_the_wait_ends_when_the_other_run_ends(self) -> None:
        sp = _load_tool()
        seen = iter([[(777, "safe_push.py", 1.4)], []])
        patches = self._space(sp, [2.5], lambda *a: next(seen))
        with patches[0], patches[1], patches[2], patches[3], mock_wait(sp, 30):
            self.assertEqual(sp.wait_for_space(), "")

    def test_a_shortage_with_no_live_run_refuses_at_once(self) -> None:
        sp = _load_tool()
        patches = self._space(sp, [1.5], lambda *a: [])
        with patches[0], patches[1], patches[2], patches[3], mock_wait(sp, 3600):
            started = time.time()
            msg = sp.wait_for_space()
        self.assertIn("below 2 GB", msg)
        self.assertNotIn("Waited", msg)
        self.assertLess(time.time() - started, 5)

    def test_a_serialized_push_queues_when_a_live_run_accounts_for_the_shortage_and_the_lock_check_still_refuses(self) -> None:
        import shutil
        with TemporaryDirectory() as td, TemporaryDirectory() as proc_dir:
            marker = Path(td) / "gate-ran"
            root = SafePushRefusals._repo(self, td, f"open({str(marker)!r}, 'w').close()\n" + GATE_PASS)
            _fake_proc(Path(proc_dir), [(900001, 1, ["python3", "scripts/run_release_regressions.py"], [])])
            floor = min(shutil.disk_usage(p).free for p in (root, Path(td))) / 1e9 + 0.7      # short now; the 1.4 GB the live run holds would cover it
            env = dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"), TMPDIR=td,
                       LEGEND_SAFE_PUSH_MIN_FREE_GB=f"{floor:.2f}", LEGEND_SAFE_PUSH_PROC_ROOT=proc_dir, LEGEND_SAFE_PUSH_DISK_WAIT_S="1")
            r = subprocess.run([sys.executable, str(TOOL), "origin", "main", "--serialize"], capture_output=True, text=True, env=env, timeout=60)
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            self.assertIn("queueing", r.stdout)
            self.assertIn("landing lock acquired", r.stdout)
            self.assertIn("waiting for disk space", r.stdout)
            self.assertIn("for the live run(s) pid 900001", r.stderr)
            self.assertFalse(marker.exists(), "the gate must not run on a short disk")


def mock_wait(sp, seconds):
    from unittest import mock
    return mock.patch.object(sp, "DISK_WAIT_S", seconds)


GATE_SLOW = ("import os, sys, time\nlog = os.environ['LEGEND_TEST_LOG']\nopen(log, 'a').write('start %s %.2f\\n' % (os.environ.get('LEGEND_TEST_NAME', '?'), time.time()))\n"
             "time.sleep(float(os.environ.get('LEGEND_TEST_SLEEP', '2')))\nopen(log, 'a').write('end %s %.2f\\n' % (os.environ.get('LEGEND_TEST_NAME', '?'), time.time()))\n"
             "print('VERDICT: PASS')\nsys.exit(0)\n")


class SafePushSerialize(unittest.TestCase):
    """`--serialize` (2026-11-16): publishers take turns; a moved remote tip is merged under the lock when the merge is clean, before the gate; nothing else is relaxed."""
    _repo = SafePushRefusals._repo
    _with_bare_remote = SafePushRefusals._with_bare_remote
    _commit = SafePushRefusals._commit
    _remote_main = SafePushRefusals._remote_main

    def _run(self, root: Path, *args: str, **extra_env: str):
        env = dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"), **extra_env)
        return subprocess.run([sys.executable, str(TOOL), *args], capture_output=True, text=True, env=env)

    def _popen(self, root: Path, *args: str, **extra_env: str):
        env = dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"), **extra_env)
        return subprocess.Popen([sys.executable, str(TOOL), *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)

    def _slow_remote(self, td: str):
        root, bare = self._with_bare_remote(td)
        (root / "scripts" / "gate.py").write_text(GATE_SLOW, encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "commit", "-qam", "slow gate"], check=True)
        subprocess.run(["git", "-C", str(root), "push", "-q", "origin", "HEAD:refs/heads/main"], check=True)
        return root, bare

    def _other_clone(self, td: str, bare: Path) -> Path:
        other = Path(td) / "other"
        subprocess.run(["git", "clone", "-q", "-b", "main", str(bare), str(other)], check=True)
        fixture_identity = "fixture" + "@" + "invalid"      # assembled: the publication gate screens address-shaped strings
        subprocess.run(["git", "-C", str(other), "config", "user.email", fixture_identity], check=True)
        subprocess.run(["git", "-C", str(other), "config", "user.name", "t"], check=True)
        return other

    REGEN_OK = ("import subprocess, sys\nsubprocess.run(['git', 'config', 'user.name', 't'])\n"
                "open('derived.txt', 'a').write('regenerated\\n')\nsubprocess.run(['git', 'add', '-A'])\n"
                "subprocess.run(['git', 'commit', '-qm', 'regenerate derived'])\nprint('REGENERATED and committed: derived.txt')\n")
    REGEN_FAIL = "import sys\nprint('boom')\nsys.exit(3)\n"

    def _with_regen(self, root: Path, src: str) -> dict:
        script = root.parent / "regen.py"                                           # outside the repository: a file inside would make the tree unclean
        script.write_text(src, encoding="utf-8")
        return {"LEGEND_SAFE_PUSH_REGEN": str(script)}

    def test_regenerate_derived_needs_serialize_and_changes_nothing_without_the_flag(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            mine = self._commit(root, "mine.txt")
            r = self._run(root, "origin", "main", "--regenerate-derived", **self._with_regen(root, self.REGEN_OK))
            self.assertEqual(r.returncode, 1)
            self.assertIn("--regenerate-derived needs --serialize", r.stderr)
            self.assertEqual(subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(), mine)
            r2 = self._run(root, "origin", "main", "--serialize", "--no-regenerate-derived", "--expect-sha", mine, LEGEND_TEST_LOG=str(Path(td) / "g.log"), LEGEND_TEST_SLEEP="0", **self._with_regen(root, self.REGEN_OK))
            self.assertEqual(r2.returncode, 0, r2.stderr)
            self.assertNotIn("REGENERATED", r2.stdout)                               # opted out, no regeneration
            self.assertFalse((root / "derived.txt").exists())
            self.assertEqual(self._remote_main(bare), mine)

    def test_serialize_regenerates_by_default_and_prints_the_two_times(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            mine = self._commit(root, "mine.txt")
            r = self._run(root, "origin", "main", "--serialize", "--expect-sha", mine, LEGEND_TEST_LOG=str(Path(td) / "g.log"), LEGEND_TEST_SLEEP="0", **self._with_regen(root, self.REGEN_OK))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("REGENERATED derived surfaces under the landing lock", r.stdout)
            self.assertIn("derived-surface regeneration step", r.stdout)
            self.assertIn("landing lock held", r.stdout)

    def test_a_failed_default_regeneration_warns_and_the_push_goes_on(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            mine = self._commit(root, "mine.txt")
            r = self._run(root, "origin", "main", "--serialize", "--expect-sha", mine, LEGEND_TEST_LOG=str(Path(td) / "g.log"), LEGEND_TEST_SLEEP="0", **self._with_regen(root, self.REGEN_FAIL))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("WARNING: derived surfaces NOT regenerated", r.stdout)
            self.assertIn("PUBLISHED", r.stdout)

    def test_regenerate_derived_commits_under_the_lock_and_the_gated_commit_is_the_pushed_one(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            log = Path(td) / "gate.log"
            mine = self._commit(root, "mine.txt")
            r = self._run(root, "origin", "main", "--serialize", "--regenerate-derived", "--expect-sha", mine, LEGEND_TEST_LOG=str(log), LEGEND_TEST_SLEEP="0", **self._with_regen(root, self.REGEN_OK))
            self.assertEqual(r.returncode, 0, r.stderr)
            head = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
            self.assertNotEqual(head, mine)
            self.assertIn(f"REGENERATED derived surfaces under the landing lock: {mine[:12]} -> {head[:12]}", r.stdout)
            self.assertEqual(self._remote_main(bare), head, "the regenerated commit, the one gated, is the one published")
            self.assertEqual(len(log.read_text().splitlines()), 2, "one gate run, on the regenerated commit")

    def test_a_failing_regeneration_gates_and_pushes_nothing(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            before = self._remote_main(bare)
            mine = self._commit(root, "mine.txt")
            r = self._run(root, "origin", "main", "--serialize", "--regenerate-derived", "--expect-sha", mine, LEGEND_TEST_SLEEP="0", **self._with_regen(root, self.REGEN_FAIL))
            self.assertEqual(r.returncode, 1)
            self.assertIn("Nothing was gated or pushed", r.stderr)
            self.assertEqual(self._remote_main(bare), before)

    def test_a_moved_remote_is_merged_under_the_lock_and_the_merged_commit_is_gated_and_pushed(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            log = Path(td) / "gate.log"
            other = self._other_clone(td, bare)
            self._commit(other, "theirs.txt")
            subprocess.run(["git", "-C", str(other), "push", "-q", "origin", "HEAD:refs/heads/main"], check=True)
            theirs = self._remote_main(bare)
            mine = self._commit(root, "mine.txt")
            r = self._run(root, "origin", "main", "--serialize", "--expect-sha", mine, LEGEND_TEST_LOG=str(log), LEGEND_TEST_SLEEP="0")
            self.assertEqual(r.returncode, 0, r.stderr)
            merged = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
            self.assertIn(f"MERGED {theirs[:12]} into {mine[:12]} -> {merged[:12]} under the landing lock", r.stdout)
            self.assertNotEqual(merged, mine)
            self.assertEqual(self._remote_main(bare), merged, "the merged commit, the one gated, is the one published")
            for n in ("mine.txt", "theirs.txt"):
                self.assertTrue((root / n).exists())
            self.assertEqual(len(log.read_text().splitlines()), 2, "one gate run (start and end) on the merged commit")
            self.assertEqual(subprocess.run(["git", "-C", str(root), "status", "--porcelain"], capture_output=True, text=True).stdout, "")

    def test_a_merge_that_changes_the_tool_refuses_and_the_second_run_publishes(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            tool = root / "framework" / "scripts" / "safe_push.py"                     # the tool runs from inside the repository it publishes, as in a worktree
            tool.parent.mkdir(parents=True, exist_ok=True)
            tool.write_bytes(TOOL.read_bytes())
            subprocess.run(["git", "-C", str(root), "add", "framework"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-qm", "the tool"], check=True)
            subprocess.run(["git", "-C", str(root), "push", "-q", "origin", "HEAD:refs/heads/main"], check=True)
            other = self._other_clone(td, bare)
            with (other / "framework" / "scripts" / "safe_push.py").open("a", encoding="utf-8") as f:
                f.write("# a newer sequence\n")
            subprocess.run(["git", "-C", str(other), "commit", "-qam", "newer tool"], check=True)
            subprocess.run(["git", "-C", str(other), "push", "-q", "origin", "HEAD:refs/heads/main"], check=True)
            theirs = self._remote_main(bare)
            log = Path(td) / "gate.log"
            mine = self._commit(root, "mine.txt")
            env = dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"), LEGEND_TEST_LOG=str(log), LEGEND_TEST_SLEEP="0")
            push = lambda sha: subprocess.run([sys.executable, "-B", str(tool), "origin", "main", "--serialize", "--expect-sha", sha], capture_output=True, text=True, env=env)
            first = push(mine)
            merged = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
            self.assertEqual(first.returncode, 1, first.stdout)
            self.assertIn("changed safe_push.py itself", first.stderr)
            self.assertIn(f"--expect-sha {merged[:12]}", first.stderr)
            self.assertEqual(self._remote_main(bare), theirs)
            self.assertFalse(log.exists(), "no gate run by the old process")
            second = push(merged)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(self._remote_main(bare), merged)

    def test_a_conflicting_remote_leaves_the_tree_as_it_was_and_gates_nothing(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            log = Path(td) / "gate.log"
            other = self._other_clone(td, bare)
            (other / "shared.txt").write_text("theirs\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(other), "add", "shared.txt"], check=True)
            subprocess.run(["git", "-C", str(other), "commit", "-qm", "theirs"], check=True)
            subprocess.run(["git", "-C", str(other), "push", "-q", "origin", "HEAD:refs/heads/main"], check=True)
            theirs = self._remote_main(bare)
            (root / "shared.txt").write_text("mine\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "shared.txt"], check=True)
            subprocess.run(["git", "-C", str(root), "commit", "-qm", "mine"], check=True)
            mine = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
            r = self._run(root, "origin", "main", "--serialize", LEGEND_TEST_LOG=str(log))
            self.assertEqual(r.returncode, 1)
            self.assertIn("does not merge cleanly", r.stderr)
            self.assertIn("shared.txt", r.stderr)
            self.assertIn("Nothing was gated or pushed", r.stderr)
            self.assertFalse(log.exists())
            self.assertEqual(self._remote_main(bare), theirs)
            self.assertEqual(subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip(), mine)
            self.assertEqual(subprocess.run(["git", "-C", str(root), "status", "--porcelain"], capture_output=True, text=True).stdout, "")
            self.assertEqual((root / "shared.txt").read_text(), "mine\n")

    def test_expect_sha_still_binds_the_commit_before_the_merge(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            other = self._other_clone(td, bare)
            self._commit(other, "theirs.txt")
            subprocess.run(["git", "-C", str(other), "push", "-q", "origin", "HEAD:refs/heads/main"], check=True)
            mine = self._commit(root, "mine.txt")
            self._commit(root, "extra.txt")
            r = self._run(root, "origin", "main", "--serialize", "--expect-sha", mine, LEGEND_TEST_LOG=str(Path(td) / "g.log"))
            self.assertEqual(r.returncode, 1)
            self.assertIn("the caller expected", r.stderr)
            self.assertNotIn("MERGED", r.stdout)

    def test_an_up_to_date_head_publishes_with_the_same_checks(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            mine = self._commit(root, "mine.txt")
            r = self._run(root, "origin", "main", "--serialize", "--expect-sha", mine, LEGEND_TEST_LOG=str(Path(td) / "g.log"), LEGEND_TEST_SLEEP="0")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("landing lock acquired", r.stdout)
            self.assertIn("VERDICT: PASS", r.stdout)
            self.assertIn("verified=ls-remote", r.stdout)
            self.assertEqual(self._remote_main(bare), mine)

    def test_a_checkout_changed_while_queued_is_preserved_and_not_gated_or_pushed(self) -> None:
        """A clean initial expectation does not survive a peer changing the shared checkout."""
        import fcntl, select
        for mutation in ("commit", "dirt"):
            with self.subTest(mutation=mutation), TemporaryDirectory() as td:
                root, bare = self._slow_remote(td)
                published = self._remote_main(bare)
                mine = self._commit(root, "mine.txt")
                log = Path(td) / "gate.log"
                with (root / ".git/legend_land.lock").open("a+") as guard:
                    fcntl.flock(guard, fcntl.LOCK_EX)
                    proc = self._popen(root, "origin", "main", "--serialize", "--expect-sha", mine,
                                       LEGEND_TEST_LOG=str(log), LEGEND_TEST_SLEEP="0")
                    seen = b""
                    try:
                        deadline = time.monotonic() + 10
                        while b"waiting for the landing lock" not in seen:
                            left = deadline - time.monotonic()
                            ready, _, _ = select.select([proc.stdout], [], [], max(0, left))
                            if not ready or left <= 0:
                                self.fail("publisher did not reach its queued wait")
                            chunk = os.read(proc.stdout.fileno(), 4096)
                            if not chunk:
                                self.fail("publisher exited before its queued wait")
                            seen += chunk
                        later = self._commit(root, "later.txt") if mutation == "commit" else mine
                        if mutation == "dirt":
                            (root / "peer-work.txt").write_text("unfinished peer work\n")
                    finally:
                        fcntl.flock(guard, fcntl.LOCK_UN)
                        out, err = proc.communicate(timeout=15)
                self.assertEqual(proc.returncode, 1, err)
                self.assertIn("while waiting for the landing lock", err)
                self.assertIn("Nothing was gated or pushed", err)
                self.assertFalse(log.exists(), "a stale checkout must be detected before spending a gate run")
                self.assertEqual(self._remote_main(bare), published)
                head = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
                self.assertEqual(head, later, "do not reset another actor's newer commit")
                if mutation == "dirt":
                    self.assertEqual((root / "peer-work.txt").read_text(), "unfinished peer work\n")

    def test_the_gate_verdict_and_the_expectation_still_refuse(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._with_bare_remote(td)
            (root / "scripts" / "gate.py").write_text(GATE_BLOCK, encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "commit", "-qam", "blocking gate"], check=True)
            r = self._run(root, "origin", "main", "--serialize")
            self.assertEqual(r.returncode, 1)
            self.assertIn("not PASS", r.stderr)
            wrong = self._run(root, "origin", "main", "--serialize", "--expect-sha", "no-such-rev")
            self.assertEqual(wrong.returncode, 1)
            self.assertIn("not a commit", wrong.stderr)

    def test_two_publishers_gate_one_at_a_time_and_the_second_merges_the_first_under_the_lock(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            second = Path(td) / "second"
            subprocess.run(["git", "-C", str(root), "worktree", "add", "-q", "--detach", str(second)], check=True)
            for w in (root, second):
                subprocess.run(["git", "-C", str(w), "config", "user.name", "t"], check=True)
            a = self._commit(root, "a.txt"); b = self._commit(second, "b.txt")
            log = Path(td) / "gate.log"
            pa = self._popen(root, "origin", "main", "--serialize", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME="A", LEGEND_TEST_SLEEP="3")
            time.sleep(1.0)
            pb = self._popen(second, "origin", "main", "--serialize", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME="B", LEGEND_TEST_SLEEP="3")
            oa, ea = pa.communicate(timeout=60); ob, eb = pb.communicate(timeout=60)
            self.assertEqual(pa.returncode, 0, ea)
            self.assertEqual(pb.returncode, 0, eb)
            self.assertIn("waiting for the landing lock", ob)
            self.assertIn(f"MERGED {a[:12]} into {b[:12]}", ob)
            self.assertNotEqual(self._remote_main(bare), a)
            self.assertTrue(subprocess.run(["git", "-C", str(bare), "merge-base", "--is-ancestor", a, "refs/heads/main"]).returncode == 0)
            names = [l.split()[1] for l in log.read_text().splitlines()]
            self.assertEqual(names, ["A", "A", "B", "B"], "the gates ran one at a time; B merged A under the lock and gated the merged commit once")

    def _three(self, td):
        root, bare = self._slow_remote(td)
        wts = [root]
        for n in ("second", "third"):
            w = Path(td) / n
            subprocess.run(["git", "-C", str(root), "worktree", "add", "-q", "--detach", str(w)], check=True); wts.append(w)
        for w in wts:
            subprocess.run(["git", "-C", str(w), "config", "user.name", "t"], check=True)
        for w, nm in zip(wts, ("a.txt", "b.txt", "c.txt")):
            self._commit(w, nm)
        return wts, bare

    def test_the_ticket_queue_lands_publishers_in_arrival_order(self) -> None:
        with TemporaryDirectory() as td:
            wts, bare = self._three(td); log = Path(td) / "gate.log"
            ps = []
            for w, nm in zip(wts, ("A", "B", "C")):
                ps.append(self._popen(w, "origin", "main", "--serialize", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME=nm, LEGEND_TEST_SLEEP="2"))
                time.sleep(1.0)
            outs = [p.communicate(timeout=90) for p in ps]
            for p, (o, e) in zip(ps, outs):
                self.assertEqual(p.returncode, 0, e)
            names = [l.split()[1] for l in log.read_text().splitlines()]
            self.assertEqual(names, ["A", "A", "B", "B", "C", "C"], "gates ran in arrival order, one at a time")
            self.assertTrue(any("queue position" in o for o, _ in outs[1:]), "a waiter prints its queue position")

    def test_a_killed_waiter_and_a_stale_ticket_do_not_block_the_queue(self) -> None:
        import signal as _sig
        with TemporaryDirectory() as td:
            wts, bare = self._three(td); log = Path(td) / "gate.log"
            common = subprocess.run(["git", "-C", str(wts[0]), "rev-parse", "--git-common-dir"], capture_output=True, text=True).stdout.strip()
            common = Path(common) if os.path.isabs(common) else wts[0] / common
            (common / "legend_land.queue").write_text("999999 1 2026-11-16T00:00:00Z\n")            # a ticket whose process does not exist, at the head
            a = self._popen(wts[0], "origin", "main", "--serialize", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME="A", LEGEND_TEST_SLEEP="3"); time.sleep(1.0)
            b = self._popen(wts[1], "origin", "main", "--serialize", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME="B", LEGEND_TEST_SLEEP="2"); time.sleep(1.0)
            c = self._popen(wts[2], "origin", "main", "--serialize", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME="C", LEGEND_TEST_SLEEP="2"); time.sleep(1.0)
            b.send_signal(_sig.SIGKILL); b.wait(timeout=10)                     # B dies while waiting: its ticket stays in the file until the next waiter prunes it
            oa, ea = a.communicate(timeout=90); oc, ec = c.communicate(timeout=90)
            self.assertEqual(a.returncode, 0, ea); self.assertEqual(c.returncode, 0, ec)
            names = [l.split()[1] for l in log.read_text().splitlines()]
            self.assertEqual(names, ["A", "A", "C", "C"], "the dead ticket at the head and the killed waiter were skipped")
            self.assertEqual((common / "legend_land.queue").read_text().strip(), "", "every live ticket was released at exit")

    def test_a_killed_publisher_releases_the_lock_and_a_timeout_refuses(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._slow_remote(td)
            second = Path(td) / "second"
            subprocess.run(["git", "-C", str(root), "worktree", "add", "-q", str(second), "-b", "other"], check=True)
            subprocess.run(["git", "-C", str(second), "config", "user.name", "t"], check=True)
            log = Path(td) / "gate.log"
            pa = self._popen(root, "origin", "main", "--serialize", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME="A", LEGEND_TEST_SLEEP="6")
            for _ in range(50):
                if log.exists(): break
                time.sleep(0.1)
            self.assertTrue(log.exists(), "A's gate should have started")
            timed = self._run(second, "origin", "main", "--serialize", "--lock-timeout", "2", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME="B")
            self.assertEqual(timed.returncode, 1)
            self.assertIn("not free within 2s", timed.stderr)
            pa.kill(); pa.communicate()
            free = self._run(second, "origin", "main", "--serialize", "--lock-timeout", "20", LEGEND_TEST_LOG=str(log), LEGEND_TEST_NAME="B", LEGEND_TEST_SLEEP="0")
            self.assertEqual(free.returncode, 0, free.stderr)
            self.assertIn("landing lock acquired", free.stdout)


VIEW_STUB_CURRENT = "import sys\nprint('view is current (stub)')\nsys.exit(0)\n"
VIEW_STUB_STALE_VIEW = ("import sys\nif sys.argv[1:] == ['check']:\n    print('STALE: view/index.html differs from a fresh full build (it); run: python3 -B framework/scripts/repurposing_view.py run')\n    sys.exit(1)\n"
                        "print('inventory current (stub)')\nsys.exit(0)\n")
VIEW_STUB_STALE_PACKAGE = ("import sys\nif sys.argv[1:] == ['package', '--check']:\n    print('STALE: index.html')\n    print('STALE: manifest.json')\n    print('package differs: run python3 -B framework/scripts/repurposing_view.py package')\n    sys.exit(1)\n"
                           "print('view is current (stub)')\nsys.exit(0)\n")
VIEW_STUB_STALE_INVENTORY = ("import sys\nif sys.argv[1:3] == ['i18n', '--what']:\n    print('inventory STALE: view/i18n/content_source.json differs from a fresh collection')\n    sys.exit(0)\n"
                             "print('view is current (stub)')\nsys.exit(0)\n")


class SafePushCopiedSentences(unittest.TestCase):
    """The copied-card-sentence step (2026-11-25, ADV): the default under `--serialize`, a stub tool stands for the real one, which has its own tests."""
    _repo = SafePushRefusals._repo
    _with_bare_remote = SafePushRefusals._with_bare_remote
    _remote_main = SafePushRefusals._remote_main

    def publish(self, td: str, code: int, *args: str):
        root, bare = self._with_bare_remote(td)
        tool = Path(td) / "copies.py"
        tool.write_text("import sys\nprint('COPIED_CARD_SENTENCES: stub', ' '.join(sys.argv[1:]))\nprint('[1] card c\\n    old text: the old words')\n"
                        f"sys.exit({code})\n", encoding="utf-8")
        (root / "b.txt").write_text("b\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", "b"], check=True)
        before = self._remote_main(bare)
        env = dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"),
                   LEGEND_SAFE_PUSH_REGEN=str(root.parent / "no_regen.py"), LEGEND_SAFE_PUSH_COPIES=str(tool))
        done = subprocess.run([sys.executable, str(TOOL), "origin", "main", *args], capture_output=True, text=True, env=env)
        return root, done, before, self._remote_main(bare)

    def test_a_held_sentence_refuses_before_the_gate_and_names_the_text(self) -> None:
        with TemporaryDirectory() as td:
            _, done, before, after = self.publish(td, 1, "--serialize")
            self.assertEqual((done.returncode, after), (1, before), done.stdout)
            self.assertIn("old text: the old words", done.stderr)
            self.assertIn("--no-copied-sentence-check", done.stderr)
            self.assertIn(f"--base {before}", done.stdout)
            self.assertNotIn("VERDICT", done.stdout)

    def test_a_check_that_cannot_run_refuses(self) -> None:
        with TemporaryDirectory() as td:
            _, done, before, after = self.publish(td, 3, "--serialize")
            self.assertEqual((done.returncode, after), (1, before), done.stdout)
            self.assertIn("could not run (exit 3)", done.stderr)

    def test_a_clean_check_publishes(self) -> None:
        with TemporaryDirectory() as td:
            _, done, before, after = self.publish(td, 0, "--serialize")
            self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
            self.assertNotEqual(after, before)

    def test_the_opt_out_skips_the_check_and_is_recorded_in_the_history(self) -> None:
        with TemporaryDirectory() as td:
            root, done, before, after = self.publish(td, 1, "--serialize", "--no-copied-sentence-check")
            self.assertEqual(done.returncode, 0, done.stdout + done.stderr)
            self.assertNotEqual(after, before)
            message = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%B"], capture_output=True, text=True).stdout
            self.assertIn("Copied-Sentence-Check: skipped (--no-copied-sentence-check)", message)
            self.assertNotIn("COPIED_CARD_SENTENCES: stub", done.stdout)


class SafePushLandingSuites(unittest.TestCase):
    """Landing suites (2026-11-25, ADV): the default under `--serialize`; a suite the push turns red refuses, one already red on the remote tip does not; the opt-out is recorded in the history.
    Fixture repository with a stub selector; the real selector has its own tests."""
    _repo = SafePushRefusals._repo
    _with_bare_remote = SafePushRefusals._with_bare_remote
    _remote_main = SafePushRefusals._remote_main
    SELECTOR = ("def changes(root, base):\n    return [('M', 'x')]\n"
                "def select(changed, root):\n    return sorted(str(p.relative_to(root)) for p in (root / 'suites').glob('*.py'))\n")
    RED = "import sys\nprint('FAIL: test_x (s.C.test_x)')\nsys.exit(1)\n"

    def publish(self, root: Path, *args: str):
        env = dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"), LEGEND_SAFE_PUSH_REGEN=str(root.parent / "no_regen.py"))
        return subprocess.run([sys.executable, str(TOOL), "origin", "main", *args], capture_output=True, text=True, env=env)

    def commit_all(self, root: Path, message: str) -> None:
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", message], check=True)

    def with_suites(self, td: str, suites: dict, selector: str = ""):
        root, bare = self._with_bare_remote(td)
        (root / "framework" / "scripts").mkdir(parents=True)
        (root / "framework" / "scripts" / "landing_suites.py").write_text(selector or self.SELECTOR, encoding="utf-8")
        (root / "suites").mkdir()
        for name, text in suites.items():
            (root / "suites" / name).write_text(text, encoding="utf-8")
        self.commit_all(root, "suites")
        return root, bare

    def on_the_remote(self, root: Path) -> None:
        subprocess.run(["git", "-C", str(root), "push", "-q", "origin", "HEAD:refs/heads/main"], check=True)

    def test_a_suite_the_push_turns_red_refuses_by_default_under_serialize(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"a_ok.py": "print('ok')\n", "b_red.py": self.RED})
            before = self._remote_main(bare)
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("LANDING-SUITE PASS suites/a_ok.py", r.stdout)
            self.assertIn("LANDING-SUITE RED suites/b_red.py", r.stdout)
            self.assertIn("2 run, 1 not passing, 1 turned red by this push", r.stdout)
            self.assertIn("FAIL: test_x", r.stderr)
            self.assertIn("--no-landing-suites", r.stderr)
            self.assertEqual(self._remote_main(bare), before)

    def test_a_green_selection_is_published(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"a_ok.py": "print('ok')\n"})
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("1 run, 0 not passing, 0 turned red by this push", r.stdout)
            self.assertIn("PUBLISHED", r.stdout)

    def test_a_suite_already_red_on_the_remote_tip_does_not_refuse(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"b_red.py": self.RED})
            self.on_the_remote(root)
            (root / "mine.txt").write_text("mine", encoding="utf-8")
            self.commit_all(root, "mine")
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("LANDING-SUITE PRE-EXISTING RED suites/b_red.py", r.stdout)
            self.assertIn("FAIL: test_x", r.stdout.split("PRE-EXISTING RED", 1)[1])
            self.assertIn("PUBLISHED", r.stdout)

    def test_a_new_failing_test_in_an_already_red_suite_refuses(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"b_red.py": self.RED})
            self.on_the_remote(root)
            (root / "suites" / "b_red.py").write_text("print('FAIL: test_y (s.C.test_y)')\n" + self.RED, encoding="utf-8")
            self.commit_all(root, "one more failure")
            before = self._remote_main(bare)
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("FAIL: test_y", r.stderr)
            self.assertNotIn("FAIL: test_x", r.stderr)
            self.assertEqual(self._remote_main(bare), before)

    def test_a_class_entry_is_run_as_a_file_and_an_argument(self) -> None:
        with TemporaryDirectory() as td:
            selector = "def changes(root, base):\n    return []\ndef select(changed, root):\n    return ['suites/c.py Named']\n"
            root, bare = self.with_suites(td, {"c.py": "import sys\nsys.exit(0 if sys.argv[1:] == ['Named'] else 1)\n"}, selector)
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("LANDING-SUITE PASS suites/c.py Named", r.stdout)

    def test_the_opt_out_runs_nothing_and_is_recorded_in_the_history(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"b_red.py": self.RED})
            r = self.publish(root, "--serialize", "--no-landing-suites")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertNotIn("LANDING-SUITE ", r.stdout)
            self.assertIn("LANDING SUITES SKIPPED", r.stdout)
            message = subprocess.run(["git", "-C", str(bare), "log", "-1", "--format=%B", "main"], capture_output=True, text=True, check=True).stdout
            self.assertIn("Landing-Suites: skipped (--no-landing-suites)", message)

    def test_both_flags_are_refused(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {})
            r = self.publish(root, "--serialize", "--landing-suites", "--no-landing-suites")
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("together", r.stderr)

    def test_without_the_flag_no_suite_runs(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"b_red.py": "raise SystemExit(1)\n"})
            r = self.publish(root)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertNotIn("LANDING", r.stdout)

    def test_a_suite_that_dirties_the_tree_meets_the_clean_tree_refusal(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"w.py": "open('left_behind.txt', 'w').write('x')\n"})
            before = self._remote_main(bare)
            r = self.publish(root, "--landing-suites")
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("left the working tree unclean", r.stderr)
            self.assertEqual(self._remote_main(bare), before)


class SafePushParallelChecks(unittest.TestCase):
    """Concurrent checks (2026-11-25, ADV): under `--serialize` the view checks, the gate and the landing suites run together, the suites in a throwaway clone of the gated commit because the gate
    reads the worktree. Refusals and their order are the serial ones; the clone is removed whatever happens; `--serial-checks` is recorded in the history."""
    _repo = SafePushRefusals._repo
    _with_bare_remote = SafePushRefusals._with_bare_remote
    _remote_main = SafePushRefusals._remote_main
    SELECTOR, RED = SafePushLandingSuites.SELECTOR, SafePushLandingSuites.RED
    with_suites, commit_all = SafePushLandingSuites.with_suites, SafePushLandingSuites.commit_all
    WHERE = "import os\nopen(os.environ['LEGEND_TEST_WHERE'], 'w').write(os.getcwd())\n"

    def env(self, root: Path, **extra: str) -> dict:
        clones = root.parent / "clones"                      # the tool's temporary folder, so that what it leaves behind can be listed
        clones.mkdir(exist_ok=True)
        return dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(root / "scripts" / "gate.py"), LEGEND_SAFE_PUSH_REGEN=str(root.parent / "no_regen.py"),
                    LEGEND_TEST_WHERE=str(root.parent / "where.txt"), LEGEND_TEST_LOG=str(root.parent / "log.txt"), TMPDIR=str(clones), **extra)

    def publish(self, root: Path, *args: str, **extra: str):
        return subprocess.run([sys.executable, str(TOOL), "origin", "main", *args], capture_output=True, text=True, env=self.env(root, **extra))

    def left_behind(self, root: Path) -> list:
        return sorted(p.name for p in (root.parent / "clones").glob("legend-landing-suites-*"))

    def test_the_suites_run_in_a_clone_of_the_gated_commit_which_is_removed(self) -> None:
        with TemporaryDirectory() as td:
            suite = self.WHERE + "import subprocess\nopen(os.environ['LEGEND_TEST_LOG'], 'w').write(subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip())\n"
            root, bare = self.with_suites(td, {"where.py": suite})
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 0, r.stderr)
            where = Path((root.parent / "where.txt").read_text())
            self.assertIn("legend-landing-suites-", str(where))
            self.assertEqual((root.parent / "log.txt").read_text(), self._remote_main(bare))
            self.assertFalse(where.exists())
            self.assertEqual(self.left_behind(root), [])
            self.assertIn("LANDING CHECKS parallel: wall ", r.stdout)
            self.assertLess(r.stdout.index("LANDING SUITES: 1 run"), r.stdout.index("VERDICT"))

    def test_the_gate_runs_while_a_suite_is_running(self) -> None:
        with TemporaryDirectory() as td:
            suite = ("import os, sys, time\nlog = os.environ['LEGEND_TEST_LOG']\nfor _ in range(600):\n"
                     "    if os.path.exists(log) and 'gate' in open(log).read():\n        sys.exit(0)\n    time.sleep(0.05)\nsys.exit(1)\n")
            root, bare = self.with_suites(td, {"waits_for_the_gate.py": suite})
            (root / "scripts" / "gate.py").write_text("import os\nopen(os.environ['LEGEND_TEST_LOG'], 'a').write('gate\\n')\n" + GATE_PASS, encoding="utf-8")
            self.commit_all(root, "gate that says it ran")
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_a_red_suite_refuses_stops_the_gate_and_removes_the_clone(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"b_red.py": self.RED})
            (root / "scripts" / "gate.py").write_text("import time\ntime.sleep(120)\n" + GATE_PASS, encoding="utf-8")
            self.commit_all(root, "slow gate")
            before, started = self._remote_main(bare), time.time()
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertLess(time.time() - started, 90, "a refusal must not wait for the gate")
            self.assertIn("turns a suite red", r.stderr)
            self.assertNotIn("VERDICT", r.stdout)
            self.assertEqual(self._remote_main(bare), before)
            self.assertEqual(self.left_behind(root), [])

    def test_a_blocking_gate_refuses_after_green_suites(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"a_ok.py": "print('ok')\n"})
            (root / "scripts" / "gate.py").write_text(GATE_BLOCK, encoding="utf-8")
            self.commit_all(root, "blocking gate")
            before = self._remote_main(bare)
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 1, r.stdout)
            self.assertIn("not PASS", r.stderr)
            self.assertIn("EMAIL_ADDRESS", r.stderr)
            self.assertEqual(self._remote_main(bare), before)

    def test_a_suite_that_dirties_its_clone_or_the_worktree_is_refused(self) -> None:
        for name, text in (("clone", "open('left_behind.txt', 'w').write('x')\n"),
                           ("worktree", "import os\nopen(os.path.join(os.environ['LEGEND_SAFE_PUSH_ROOT'], 'left_behind.txt'), 'w').write('x')\n")):
            with self.subTest(dirtied=name), TemporaryDirectory() as td:
                root, bare = self.with_suites(td, {"w.py": text})
                before = self._remote_main(bare)
                r = self.publish(root, "--serialize")
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("left the working tree unclean", r.stderr)
                self.assertEqual(self._remote_main(bare), before)
                self.assertEqual(self.left_behind(root), [])

    def test_files_is_hard_linked_into_the_clone_and_survives_its_removal(self) -> None:
        with TemporaryDirectory() as td:
            suite = "import os, sys\nsys.exit(0 if os.stat('files/held.bin').st_nlink > 1 else 1)\n"
            root, bare = self.with_suites(td, {"linked.py": suite})
            (root / ".gitignore").write_text("files/\n", encoding="utf-8")
            self.commit_all(root, "ignore files")
            (root / "files").mkdir()
            (root / "files" / "held.bin").write_text("held\n", encoding="utf-8")
            r = self.publish(root, "--serialize")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertEqual((root / "files" / "held.bin").read_text(), "held\n")
            self.assertEqual((root / "files" / "held.bin").stat().st_nlink, 1)

    def test_serial_checks_run_in_the_worktree_and_are_recorded_in_the_history(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"where.py": self.WHERE})
            r = self.publish(root, "--serialize", "--serial-checks")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(Path((root.parent / "where.txt").read_text()).resolve(), root.resolve())
            self.assertNotIn("LANDING CHECKS parallel", r.stdout)
            self.assertNotIn("concurrent landings", r.stdout)
            message = subprocess.run(["git", "-C", str(bare), "log", "-1", "--format=%B", "main"], capture_output=True, text=True, check=True).stdout
            self.assertIn("Landing-Checks: serial (--serial-checks)", message)

    def test_without_the_lock_the_checks_stay_one_after_another(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self.with_suites(td, {"where.py": self.WHERE})
            r = self.publish(root, "--landing-suites")
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(Path((root.parent / "where.txt").read_text()).resolve(), root.resolve())
            self.assertNotIn("LANDING CHECKS parallel", r.stdout)

    def test_when_no_clone_can_be_built_the_suites_run_in_the_worktree_after_the_gate(self) -> None:
        with TemporaryDirectory() as td:
            suite = self.WHERE + "import sys\nsys.exit(0 if 'gate' in open(os.environ['LEGEND_TEST_LOG']).read() else 1)\n"
            root, bare = self.with_suites(td, {"where.py": suite})
            (root / "scripts" / "gate.py").write_text("import os, time\ntime.sleep(1)\nopen(os.environ['LEGEND_TEST_LOG'], 'a').write('gate\\n')\n" + GATE_PASS, encoding="utf-8")
            self.commit_all(root, "gate that says it ran")
            shim = root.parent / "bin"
            shim.mkdir()
            (root / ".gitignore").write_text("files/\n", encoding="utf-8")
            self.commit_all(root, "ignore files")
            (root / "files").mkdir()
            (shim / "cp").write_text("#!/bin/sh\necho no hard links here >&2\nexit 1\n", encoding="utf-8")
            (shim / "cp").chmod(0o755)
            r = self.publish(root, "--serialize", PATH=f"{shim}{os.pathsep}{os.environ['PATH']}")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("PARALLEL CHECKS: no suite clone", r.stdout)
            self.assertEqual(Path((root.parent / "where.txt").read_text()).resolve(), root.resolve())
            self.assertEqual(self.left_behind(root), [])

    def test_a_terminated_publisher_removes_the_clone(self) -> None:
        with TemporaryDirectory() as td:
            suite = self.WHERE + "import time\ntime.sleep(120)\n"
            root, bare = self.with_suites(td, {"slow.py": suite})
            process = subprocess.Popen([sys.executable, str(TOOL), "origin", "main", "--serialize"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=self.env(root))
            try:
                deadline = time.time() + 60
                while not (root.parent / "where.txt").exists() and time.time() < deadline:
                    time.sleep(0.05)
                self.assertEqual(len(self.left_behind(root)), 1)
                process.terminate()
                process.communicate(timeout=60)
            finally:
                if process.poll() is None:
                    process.kill()
                    process.communicate()
            self.assertEqual(process.returncode, 143)
            self.assertEqual(self.left_behind(root), [])


class SafePushViewCurrency(unittest.TestCase):
    """2026-11-24 (ADV): a committed derived view that is behind its sources turned CI red for hours because nothing before the landing checked it. `check` and the i18n inventory check
    (about 12 s together) now run before the gate; a stale answer refuses and names the regeneration commands."""
    _repo = SafePushRefusals._repo
    _with_bare_remote = SafePushRefusals._with_bare_remote
    _remote_main = SafePushRefusals._remote_main

    def _run(self, root: Path, gate: Path | None = None, *args: str):
        env = dict(os.environ, LEGEND_SAFE_PUSH_ROOT=str(root), LEGEND_SAFE_PUSH_GATE=str(gate or root / "scripts" / "gate.py"))
        return subprocess.run([sys.executable, str(TOOL), *(args or ("origin", "main"))], capture_output=True, text=True, env=env)

    def _with_view_stub(self, td: str, stub_src: str):
        root, bare = self._with_bare_remote(td)
        (root / "framework" / "scripts").mkdir(parents=True)
        (root / "framework" / "scripts" / "repurposing_view.py").write_text(stub_src, encoding="utf-8")
        subprocess.run(["git", "-C", str(root), "add", "-A"], check=True)
        subprocess.run(["git", "-C", str(root), "commit", "-qm", "view stub"], check=True)
        return root, bare

    def test_a_stale_view_refuses_before_the_gate_and_names_the_regeneration_commands(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._with_view_stub(td, VIEW_STUB_STALE_VIEW)
            before = self._remote_main(bare)
            r = self._run(root)
            self.assertEqual(r.returncode, 1, r.stderr)
            self.assertIn("a committed derived view is behind its sources", r.stderr)
            self.assertIn("python3 -B framework/scripts/repurposing_view.py run --source shareable", r.stderr)
            self.assertIn("i18n --what collect", r.stderr)
            self.assertIn("Nothing was gated or pushed", r.stderr)
            self.assertNotIn("VERDICT", r.stdout)                       # the gate never ran
            self.assertEqual(self._remote_main(bare), before)

    def test_a_stale_package_refuses_when_the_pages_and_the_inventory_are_current_and_names_the_package_command(self) -> None:
        """CI #2187/#2188 (2026-11-24): the pages and the inventory were current, view/shareable_package/ was not, and no check before the gate looked at it."""
        with TemporaryDirectory() as td:
            root, bare = self._with_view_stub(td, VIEW_STUB_STALE_PACKAGE)
            before = self._remote_main(bare)
            r = self._run(root)
            self.assertEqual(r.returncode, 1, r.stderr)
            self.assertIn("a committed derived view is behind its sources", r.stderr)
            self.assertIn("[repurposing_view.py package --check]", r.stderr)
            self.assertIn("STALE: manifest.json", r.stderr)
            self.assertIn("python3 -B framework/scripts/repurposing_view.py package", r.stderr)
            self.assertIn("Nothing was gated or pushed", r.stderr)
            self.assertNotIn("VERDICT", r.stdout)
            self.assertEqual(self._remote_main(bare), before)

    def test_the_package_check_is_the_third_call_after_check_and_the_inventory(self) -> None:
        with TemporaryDirectory() as td:
            log = Path(td) / "calls.txt"
            stub = f"import sys\nopen({str(log)!r}, 'a').write(' '.join(sys.argv[1:]) + '\\n')\nprint('view is current (stub)')\nsys.exit(0)\n"
            root, bare = self._with_view_stub(td, stub)
            r = self._run(root)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertEqual(log.read_text().splitlines(), ["check", "i18n --what check", "package --check"])

    def test_a_stale_i18n_inventory_refuses_even_though_the_tool_exits_zero(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._with_view_stub(td, VIEW_STUB_STALE_INVENTORY)
            r = self._run(root)
            self.assertEqual(r.returncode, 1, r.stderr)
            self.assertIn("inventory STALE", r.stderr)
            self.assertIn("Nothing was gated or pushed", r.stderr)

    def test_current_views_and_a_repository_without_the_tool_reach_the_push(self) -> None:
        with TemporaryDirectory() as td:
            root, bare = self._with_view_stub(td, VIEW_STUB_CURRENT)
            r = self._run(root)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("PUBLISHED", r.stdout)
        with TemporaryDirectory() as td:                                # no framework/scripts/repurposing_view.py at all: skipped, not refused
            root, bare = self._with_bare_remote(td)
            r = self._run(root)
            self.assertEqual(r.returncode, 0, r.stderr)

    def test_a_deliberately_stale_view_in_a_scratch_clone_of_this_repository_is_refused(self) -> None:
        """The real tool on a real clone (never the checkout this test runs from): regenerate, publish to a scratch bare remote (control), then make the shareable page stale and commit it."""
        repo = TOOL.resolve().parents[2]
        if not (repo / "framework" / "scripts" / "repurposing_view.py").is_file():
            self.skipTest("this repository has no repurposing view")
        with TemporaryDirectory() as td:
            clone = Path(td) / "clone"
            made = subprocess.run(["git", "clone", "-q", "--depth", "1", "--no-hardlinks", f"file://{repo}", str(clone)], capture_output=True, text=True)
            if made.returncode != 0:
                self.skipTest(f"no shallow clone available: {made.stderr.strip()[:120]}")
            bare = Path(td) / "scratch_remote.git"
            subprocess.run(["git", "init", "-q", "--bare", str(bare)], check=True)
            subprocess.run(["git", "-C", str(bare), "config", "receive.shallowUpdate", "true"], check=True)   # the clone is shallow
            fixture_identity = "fixture" + "@" + "invalid"                 # assembled: the publication gate screens address-shaped strings
            for cmd in (["config", "user.email", fixture_identity], ["config", "user.name", "t"], ["remote", "set-url", "origin", str(bare)]):
                subprocess.run(["git", "-C", str(clone), *cmd], check=True)   # origin is the scratch remote BEFORE anything can be pushed
            gate = Path(td) / "gate_pass.py"
            gate.write_text(GATE_PASS, encoding="utf-8")
            for cmd in (["run"], ["run", "--source", "shareable"], ["package"], ["i18n", "--what", "collect"]):
                done = subprocess.run([sys.executable, "-B", "framework/scripts/repurposing_view.py", *cmd], cwd=clone, capture_output=True, text=True)
                self.assertEqual(done.returncode, 0, done.stdout[-300:] + done.stderr[-300:])
            subprocess.run(["git", "-C", str(clone), "add", "-A"], check=True)
            subprocess.run(["git", "-C", str(clone), "commit", "-qm", "regenerated", "--allow-empty"], check=True)
            ok = self._run(clone, gate)
            self.assertEqual(ok.returncode, 0, ok.stderr)             # control: current views are published
            self.assertIn("PUBLISHED", ok.stdout)
            page = clone / "disease-models" / "wwox" / "research" / "drug_repurposing" / "view" / "index_shareable.html"
            page.write_text(page.read_text(encoding="utf-8") + "<!-- stale -->\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(clone), "commit", "-qam", "stale shareable page"], check=True)
            stale_head = subprocess.run(["git", "-C", str(clone), "rev-parse", "HEAD"], check=True, capture_output=True, text=True).stdout.strip()
            bad = self._run(clone, gate)
            self.assertEqual(bad.returncode, 1, bad.stderr)
            self.assertIn("index_shareable.html differs from a fresh shareable build", bad.stderr)
            self.assertIn("repurposing_view.py run --source shareable", bad.stderr)
            self.assertNotEqual(self._remote_main(bare), stale_head)


if __name__ == "__main__":
    unittest.main(verbosity=2)
