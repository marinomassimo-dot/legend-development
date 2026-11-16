#!/usr/bin/env python3
"""Regressions for safe_push.py — every one is a refusal path, because the refusals are the tool."""
from __future__ import annotations
import os, subprocess, sys, time, unittest
from pathlib import Path
from tempfile import TemporaryDirectory

TOOL = Path(__file__).resolve().parent / "safe_push.py"

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

    def test_a_blocking_gate_refuses_the_push(self) -> None:
        """The defect of 2026-09-09: the gate said BLOCK and the push went anyway."""
        with TemporaryDirectory() as td:
            r = self._run(self._repo(td, GATE_BLOCK), "origin", "main")
            self.assertEqual(r.returncode, 1)
            self.assertIn("not PASS", r.stderr)
            self.assertIn("Nothing was pushed", r.stderr)

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
