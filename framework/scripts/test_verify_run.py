#!/usr/bin/env python3
"""verify_run.py on small fixtures: evidence kept before removal, and a removal only when every check holds.

Each case builds a toy source repository and a private temp and evidence directory; nothing here touches the real /tmp, the corpus or another session's run.
"""
from __future__ import annotations

import io
import json
import os
import signal
import subprocess
import sys
import tarfile
import tempfile
import time
import unittest
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_run as vr  # noqa: E402

PY = sys.executable


def sh(cwd, *args):
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        t = Path(self._tmp.name).resolve()
        self.t, self.tmp, self.keep, self.src = t, t / "tmp", t / "keep", t / "src"
        self.tmp.mkdir()
        self.old_env = dict(os.environ)
        self.old_tempdir = tempfile.tempdir
        os.environ.update(TMPDIR=str(self.tmp), LEGEND_VERIFY_KEEP=str(self.keep), CLAUDE_CODE_SESSION_ID="session-A")
        tempfile.tempdir = str(self.tmp)
        self.src.mkdir()
        sh(self.src, "git", "init", "-q", "-b", "main")
        (self.src / ".gitignore").write_text("files/\n__pycache__/\n")
        (self.src / "a.txt").write_text("hello\n")
        (self.src / "files").mkdir()
        (self.src / "files" / "corpus.bin").write_bytes(b"corpus" * 1000)
        sh(self.src, "git", "add", ".")
        sh(self.src, "git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "init")
        self.sha = sh(self.src, "git", "rev-parse", "HEAD")

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self.old_env)
        tempfile.tempdir = self.old_tempdir
        for p in self.tmp.glob("*"):                      # a test that left a process behind must not leave it running
            for pid in vr.processes_using(p) if p.is_dir() and not p.is_symlink() else []:
                try:
                    os.kill(int(pid.split()[0]), signal.SIGKILL)
                except OSError:
                    pass
        self._tmp.cleanup()

    def run_cmd(self, code: str, *extra: str):
        out = io.StringIO()
        with redirect_stdout(out):
            rc = vr.main(["run", "--sha", self.sha, "--repo", str(self.src), "--label", "t", "--mandate", "TASK-1", *extra, "--", PY, "-c", code])
        return rc, out.getvalue()

    def runs(self):
        return sorted(p for p in self.keep.iterdir() if p.is_dir())

    def manifest(self):
        (run_dir,) = self.runs()
        return run_dir, json.loads((run_dir / "manifest.json").read_text())

    def boxes(self):
        return [p for p in self.tmp.iterdir() if p.name.startswith(vr.PREFIX)]


class Lifecycle(Base):
    def test_pass_keeps_the_evidence_and_removes_the_clone(self):
        rc, out = self.run_cmd("print('VERDICT: PASS')")
        run_dir, m = self.manifest()
        self.assertEqual((rc, m["state"], m["exit_code"], m["cleanup"]["state"]), (0, "CONCLUDED", 0, "REMOVED"))
        self.assertEqual(self.boxes(), [])
        self.assertIn("VERDICT: PASS", (run_dir / "run.log").read_text())
        self.assertEqual((m["sha"], m["session"], m["mandate"], m["source_repo"]), (self.sha, "session-A", "TASK-1", str(self.src)))
        self.assertTrue(m["supervisor"] and m["child"] and (run_dir / "clone_state.txt").is_file())
        self.assertGreater(m["cleanup"]["freed_bytes"], 0)
        self.assertIn("clone REMOVED", out)

    def test_fail_keeps_the_log_and_the_command_and_still_removes_the_clone(self):
        rc, _ = self.run_cmd("import sys; print('FAILED (failures=1)'); sys.exit(3)")
        run_dir, m = self.manifest()
        self.assertEqual((rc, m["exit_code"], m["cleanup"]["state"]), (3, 3, "REMOVED"))
        self.assertIn("FAILED (failures=1)", m["verdict_lines"][0])
        self.assertEqual(m["command"][0], PY)        # command and SHA reproduce the failure; the clone is not what is kept
        self.assertEqual(self.boxes(), [])

    def test_the_task_record_points_at_the_evidence(self):
        rec = self.t / "record.json"
        rec.write_text(json.dumps({"TASK_ID": "TASK-1"}))
        self.run_cmd("print('ok')", "--task-record", str(rec))
        run_dir, m = self.manifest()
        entry = json.loads(rec.read_text())["VERIFICATION_EVIDENCE"][0]
        self.assertEqual((entry["run_id"], entry["evidence_dir"], entry["clone"], entry["exit_code"]), (m["run_id"], str(run_dir), "REMOVED", 0))
        self.assertEqual(len(entry["log_sha256"]), 64)

    def test_a_hard_linked_corpus_original_survives_the_removal(self):
        original = self.src / "files" / "corpus.bin"
        self.run_cmd("import os; print(os.stat('files/corpus.bin').st_nlink)")
        self.assertEqual("2", (self.runs()[0] / "run.log").read_text().strip())     # the clone really shared the file
        self.assertEqual((original.read_bytes(), original.stat().st_nlink), (b"corpus" * 1000, 1))

    def test_a_worktree_source_gets_the_corpus_of_its_main_checkout(self):
        wt = self.t / "wt"
        sh(self.src, "git", "worktree", "add", "-q", "-b", "side", str(wt), self.sha)
        out = io.StringIO()
        with redirect_stdout(out):
            vr.main(["run", "--sha", self.sha, "--repo", str(wt), "--label", "t", "--", PY, "-c", "import os; print(os.path.exists('files/corpus.bin'))"])
        run_dir, m = self.manifest()
        self.assertEqual((run_dir / "run.log").read_text().strip(), "True")                 # without it a battery skips every corpus suite and says PASS
        self.assertEqual(m["files_linked_from"], str(self.src / "files"))

    def test_a_second_call_changes_nothing(self):
        self.run_cmd("print('x')")
        run_dir, before = self.manifest()
        again = vr.conclude(run_dir)
        out = io.StringIO()
        with redirect_stdout(out):
            vr.main(["reap"])
        self.assertEqual(again["cleanup"], before["cleanup"])
        self.assertIn("0 run(s) examined", out.getvalue())
        self.assertEqual(self.manifest()[1]["cleanup"], before["cleanup"])


class WhatIsKept(Base):
    def test_a_directory_in_use_is_kept_and_removed_on_the_next_call(self):
        code = "import subprocess; subprocess.Popen(['sleep', '60'], start_new_session=True)"     # outlives the command, inherits the clone as its cwd
        self.run_cmd(code)
        run_dir, m = self.manifest()
        self.assertEqual(m["cleanup"]["state"], "KEPT")
        self.assertIn("in use by process", m["cleanup"]["reasons"][0])
        self.assertEqual(len(self.boxes()), 1)
        pid = int(m["cleanup"]["reasons"][0].split("process ")[1].split()[0])
        os.kill(pid, signal.SIGKILL)       # the test's own process, not something the module killed
        deadline = time.time() + 5
        while vr.processes_using(Path(m["box"])) and time.time() < deadline:
            time.sleep(0.1)
        out = io.StringIO()
        with redirect_stdout(out):
            vr.main(["reap"])
        self.assertEqual(self.manifest()[1]["cleanup"]["state"], "REMOVED")
        self.assertEqual(self.boxes(), [])

    def test_a_stranger_and_a_look_alike_are_not_touched(self):
        stranger = self.tmp / (vr.PREFIX + "stranger")
        (stranger / ".git").mkdir(parents=True)
        lookalike = self.tmp / "bat_it99"
        lookalike.mkdir()
        (lookalike / "keep.txt").write_text("x")
        out = io.StringIO()
        with redirect_stdout(out):
            vr.main(["unrecognised"])
            vr.main(["reap"])
        self.assertIn("stranger", out.getvalue())
        self.assertTrue(stranger.is_dir() and lookalike.is_dir())
        run_dir = self.keep / "run-x"
        run_dir.mkdir(parents=True)
        (run_dir / "run.log").write_text("log")
        m = {"run_id": "x", "state": "CONCLUDED", "exit_code": 0, "box": str(stranger), "box_inode": stranger.stat().st_ino, "sha": self.sha, "source_repo": str(self.src)}
        (run_dir / "manifest.json").write_text(json.dumps(m))
        got = vr.conclude(run_dir)
        self.assertEqual(got["cleanup"]["state"], "KEPT")                    # the manifest names it, but it carries no .run_id of this run
        self.assertTrue(stranger.is_dir())
        m["box"], m["box_inode"] = str(lookalike), lookalike.stat().st_ino
        (run_dir / "manifest.json").write_text(json.dumps(m))
        self.assertIn("prefix", vr.conclude(run_dir)["cleanup"]["reasons"][0])
        self.assertTrue(lookalike.is_dir())

    def test_a_missing_path_or_an_incomplete_manifest_is_a_diagnosis_not_a_deletion(self):
        bystander = self.tmp / "bystander"
        bystander.mkdir()
        for name, m in (("no-box", {"run_id": "a", "state": "CONCLUDED", "exit_code": 0}), ("empty", {}), ("gone", {"run_id": "b", "state": "CONCLUDED", "exit_code": 0, "box": str(self.tmp / "legend-verify-gone"), "box_inode": 1})):
            d = self.keep / name
            d.mkdir(parents=True)
            (d / "manifest.json").write_text(json.dumps(m))
            got = vr.conclude(d)
            self.assertIn(got["cleanup"]["state"], ("KEPT", "REMOVED"), name)
        broken = self.keep / "broken"
        broken.mkdir()
        (broken / "manifest.json").write_text("{not json")
        self.assertEqual(vr.conclude(broken)["cleanup"]["state"], "KEPT")
        self.assertTrue(bystander.is_dir())

    def test_unsaved_changes_are_archived_before_the_clone_is_removed(self):
        self.run_cmd("open('note.txt', 'w').write('only here\\n'); print('ok')")
        run_dir, m = self.manifest()
        self.assertEqual(m["cleanup"]["state"], "REMOVED")
        with tarfile.open(run_dir / "unsaved_changes.tar.gz") as tar:
            self.assertEqual(tar.extractfile("note.txt").read(), b"only here\n")

    def test_unsaved_changes_above_the_limit_keep_the_directory(self):
        self.run_cmd("open('note.txt', 'w').write('0123456789'); print('ok')", "--max-archive-mb", "0")
        _, m = self.manifest()
        self.assertEqual(m["cleanup"]["state"], "KEPT")
        self.assertIn("archive limit", m["cleanup"]["reasons"][0])
        self.assertTrue((Path(m["box"]) / "clone" / "note.txt").is_file())

    def test_unique_corpus_data_keeps_the_directory(self):
        self.run_cmd("open('files/new_result.tsv', 'w').write('a\\tb\\n'); print('ok')")
        _, m = self.manifest()
        self.assertEqual(m["cleanup"]["state"], "KEPT")
        self.assertIn("unique data", m["cleanup"]["reasons"][0])

    def test_a_commit_that_only_the_clone_holds_keeps_the_directory(self):
        code = "import subprocess; subprocess.run(['git','-c','user.name=t','-c','user.email=t@t','commit','--allow-empty','-qm','only here'], check=True)"
        self.run_cmd(code)
        _, m = self.manifest()
        self.assertEqual(m["cleanup"]["state"], "KEPT")
        self.assertIn("absent from the source", m["cleanup"]["reasons"][0])

    def test_a_symlink_is_unlinked_and_its_target_is_left_alone(self):
        outside = self.t / "outside"
        outside.mkdir()
        (outside / "precious.txt").write_text("keep me")
        self.run_cmd(f"import os; os.symlink({str(outside)!r}, 'link'); print('ok')")
        run_dir, m = self.manifest()
        self.assertEqual(m["cleanup"]["state"], "REMOVED")
        self.assertEqual((outside / "precious.txt").read_text(), "keep me")
        with tarfile.open(run_dir / "unsaved_changes.tar.gz") as tar:
            self.assertEqual(tar.getnames(), ["link"])           # the link is stored as a link, not the directory behind it

    def test_a_box_replaced_by_a_symlink_is_refused(self):
        outside = self.t / "outside2"
        outside.mkdir()
        (outside / "precious.txt").write_text("keep me")
        link = self.tmp / (vr.PREFIX + "swapped")
        link.symlink_to(outside)
        d = self.keep / "swap"
        d.mkdir(parents=True)
        (d / "run.log").write_text("log")
        (d / "manifest.json").write_text(json.dumps({"run_id": "s", "state": "CONCLUDED", "exit_code": 0, "box": str(link), "box_inode": outside.stat().st_ino, "sha": self.sha, "source_repo": str(self.src)}))
        got = vr.conclude(d)
        self.assertEqual(got["cleanup"]["state"], "KEPT")
        self.assertTrue((outside / "precious.txt").is_file())

    def test_another_sessions_run_is_not_this_sessions_to_reap(self):
        self.run_cmd("import subprocess; subprocess.Popen(['sleep', '60'], start_new_session=True)")   # kept: in use
        run_dir, m = self.manifest()
        os.environ["CLAUDE_CODE_SESSION_ID"] = "session-B"
        out = io.StringIO()
        with redirect_stdout(out):
            vr.main(["reap"])
        self.assertIn("0 run(s) examined", out.getvalue())
        self.assertEqual(self.manifest()[1]["cleanup"]["state"], "KEPT")


class Interruption(Base):
    def supervisor(self, *command):
        return subprocess.Popen([PY, str(HERE / "verify_run.py"), "run", "--sha", self.sha, "--repo", str(self.src), "--label", "t", "--", *command],
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

    def wait_state(self, state, timeout=20):
        deadline = time.time() + timeout
        while time.time() < deadline:
            if self.keep.is_dir() and self.runs():
                m = json.loads((self.runs()[0] / "manifest.json").read_text())
                if m.get("state") == state:
                    return m
            time.sleep(0.1)
        self.fail(f"run never reached {state}")

    def test_an_interrupt_ends_the_run_and_still_cleans_up(self):
        p = self.supervisor("sleep", "60")
        self.wait_state("RUNNING")
        p.send_signal(signal.SIGTERM)
        out, _ = p.communicate(timeout=30)
        _, m = self.manifest()
        self.assertEqual((m["state"], m["cleanup"]["state"]), ("INTERRUPTED", "REMOVED"))
        self.assertIn("INTERRUPTED", out)
        self.assertEqual(self.boxes(), [])

    def test_a_killed_supervisor_leaves_a_run_the_next_call_concludes_without_killing_anything(self):
        p = self.supervisor("sleep", "60")
        m = self.wait_state("RUNNING")
        p.kill()
        p.communicate()
        child = int(m["child"].split(":")[0])
        out = io.StringIO()
        with redirect_stdout(out):
            vr.main(["reap"])
        self.assertIn("KEPT; the run is still alive", out.getvalue())                    # the command is still running: the directory stays
        self.assertTrue(vr.alive(m["child"]))
        self.assertEqual(len(self.boxes()), 1)
        os.kill(child, signal.SIGKILL)                                                      # the test ends it; the module never does
        deadline = time.time() + 5
        while vr.alive(m["child"]) and time.time() < deadline:
            time.sleep(0.1)
        with redirect_stdout(out):
            vr.main(["reap"])
        got = self.manifest()[1]
        self.assertEqual((got["state"], got["cleanup"]["state"]), ("INTERRUPTED", "REMOVED"))
        self.assertEqual(self.boxes(), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
