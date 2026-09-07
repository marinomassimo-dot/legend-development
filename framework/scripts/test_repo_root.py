#!/usr/bin/env python3
"""A control-plane path must not depend on where the caller was standing.

Every test that asserts an answer is paired with an arm that removes the property. The three
wired tools are driven as subprocesses, because what is being measured is the exit code and the
object a gate would read, not an internal return value.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from repo_root import RootError, control_plane, repo_root  # noqa: E402

ROOT = HERE.parent.parent
HERE_SCRIPTS = HERE
LEASE = "runtime/orchestrator_lease.md"


def run(script: str, *args, cwd: Path):
    result = subprocess.run([sys.executable, str(HERE / script), *args],
                            capture_output=True, text=True, cwd=str(cwd))
    return result.returncode, result.stdout + result.stderr


class TheRootIsDerivedNotGuessed(unittest.TestCase):
    def test_every_directory_of_one_checkout_gives_the_same_root(self):
        seen = {repo_root(ROOT), repo_root(ROOT / "framework"),
                repo_root(ROOT / "framework" / "scripts")}
        self.assertEqual(len(seen), 1, f"one checkout produced {len(seen)} roots: {seen}")

    def test_outside_a_working_tree_it_refuses(self):
        with tempfile.TemporaryDirectory() as outside:
            with self.assertRaises(RootError):
                repo_root(outside)

    def test_the_refusal_is_not_a_fallback_to_the_current_directory(self):
        """The arm that matters: a helper that silently answers `cwd` passes every other test."""
        with tempfile.TemporaryDirectory() as outside:
            previous = Path.cwd()
            os.chdir(outside)
            try:
                with self.assertRaises(RootError):
                    repo_root()
            finally:
                os.chdir(previous)

    def test_control_plane_joins_a_name_to_the_derived_root(self):
        self.assertEqual(control_plane(LEASE, ROOT), ROOT / LEASE)
        self.assertEqual(control_plane(LEASE, ROOT / "framework"), ROOT / LEASE)


class TheWiredToolsAgreeAcrossDirectories(unittest.TestCase):
    """Each of these three answered differently depending on the caller's directory."""

    DIRS = (ROOT, ROOT / "framework", ROOT / "framework" / "scripts")

    def test_lease_state_reads_one_object_from_anywhere_in_the_checkout(self):
        answers = set()
        for where in self.DIRS:
            code, output = run("lease_state.py", cwd=where)
            self.assertEqual(code, 0, output)
            answers.add(tuple(l for l in output.splitlines() if l.startswith("  lease #")))
        self.assertEqual(len(answers), 1, "the lease record set depends on the caller's directory")

    def test_legend_lint_gives_one_verdict_from_anywhere_in_the_checkout(self):
        """It returned PASS from the root and BLOCK_SYSTEM from a subdirectory."""
        verdicts = set()
        for where in self.DIRS:
            code, output = run("legend_lint.py", cwd=where)
            verdicts.add(next((l for l in output.splitlines() if l.startswith("VERDICT:")), output))
        self.assertEqual(len(verdicts), 1, f"verdict depends on the directory: {verdicts}")

    def test_sync_epochs_finds_the_same_epoch_from_anywhere(self):
        """It reported "no sync epoch recorded" from a subdirectory — an absence it manufactured."""
        answers = set()
        for where in self.DIRS:
            code, output = run("sync_epochs.py", "status", cwd=where)
            self.assertEqual(code, 0, output)
            answers.add(output.strip())
        self.assertEqual(len(answers), 1, "the epoch found depends on the caller's directory")


class TheWiredToolsFailClosedOutsideARepository(unittest.TestCase):
    def setUp(self):
        self.outside = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.outside, ignore_errors=True)

    def test_lease_state_refuses(self):
        code, output = run("lease_state.py", cwd=self.outside)
        self.assertEqual(code, 2, output)
        self.assertIn("not inside a git working tree", output)

    def test_legend_lint_refuses(self):
        code, output = run("legend_lint.py", cwd=self.outside)
        self.assertNotEqual(code, 0, output)
        self.assertIn("not inside a git working tree", output)

    def test_sync_epochs_refuses(self):
        code, output = run("sync_epochs.py", "status", cwd=self.outside)
        self.assertNotEqual(code, 0, output)
        self.assertIn("not inside a git working tree", output)

    def test_an_explicit_path_still_works_from_outside(self):
        """The control: refusing to GUESS must not mean refusing to be TOLD."""
        code, output = run("lease_state.py", "--home", str(ROOT / LEASE), cwd=self.outside)
        self.assertEqual(code, 0, output)


class TheSingletonInvariantIsNotVerifiableAcrossWorktrees(unittest.TestCase):
    """🔴 A finding this candidate records and does NOT repair.

    Annex I.3: `Un solo ACTIVE`. The lease record is per-worktree, so two worktrees can each
    hold one ACTIVE lease and each report exactly what a healthy singleton looks like. Binding
    the control plane to the shared repository would fix it and would also change which lease
    record is authoritative — a governance decision about the relevance set, not a path helper.

    The test asserts the defect still exists, so that repairing it cannot happen silently.
    """

    def test_two_checkouts_each_with_one_active_lease_both_report_healthy(self):
        workspace = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, workspace, ignore_errors=True)
        block = ("# fixture\n\nLEASE:\n"
                 "  ACTOR_ID:            orchestrator\n"
                 "  SESSION_REF:         session-{n}\n"
                 "  GOVERNANCE_VERSION:  3.1.1\n"
                 "  ACTIVATED_AT:        2026-08-26T09:00:00Z\n"
                 "  EXPIRES_AT:          2099-01-01T00:00:00Z\n"
                 "  STATUS:              ACTIVE\n")
        seen = []
        for name in ("A", "B"):
            home = workspace / name / LEASE
            home.parent.mkdir(parents=True)
            home.write_text(block.format(n=name))
            code, output = run("lease_state.py", "--home", str(home), cwd=ROOT)
            seen.append((code, "ACTIVE by derivation: 1" in output))
        self.assertEqual(seen, [(0, True), (0, True)],
                         "the invariant became verifiable — update the record that says it is not")


class TheAnswerNamesItsSource(unittest.TestCase):
    """A derived answer that does not say what it measured cannot be reconciled with another.

    The same command read a 5-record lease and a 9-record one and printed the same shape of
    answer both times. Naming the object is evidence, not policy: it asserts nothing about
    which object *should* have been read.
    """

    def test_lease_state_reports_the_object_it_measured(self):
        code, output = run("lease_state.py", cwd=ROOT)
        self.assertEqual(code, 0, output)
        for field in ("CONTROL_PLANE_SOURCE_PATH", "CONTROL_PLANE_SOURCE_SHA256",
                      "CONTROL_PLANE_RECORD_COUNT"):
            self.assertIn(field, output)

    def test_the_reported_path_is_the_one_actually_read(self):
        explicit = ROOT / LEASE
        code, output = run("lease_state.py", "--home", str(explicit), cwd=ROOT)
        self.assertEqual(code, 0, output)
        self.assertIn(f"CONTROL_PLANE_SOURCE_PATH {explicit}", output)

    def test_the_reported_digest_matches_the_file(self):
        import hashlib
        code, output = run("lease_state.py", cwd=ROOT)
        declared = next(l.split()[1] for l in output.splitlines()
                        if l.startswith("CONTROL_PLANE_SOURCE_SHA256"))
        self.assertEqual(declared, hashlib.sha256((ROOT / LEASE).read_bytes()).hexdigest())

    def test_the_reported_count_matches_the_lines_printed(self):
        code, output = run("lease_state.py", cwd=ROOT)
        declared = int(next(l.split()[1] for l in output.splitlines()
                            if l.startswith("CONTROL_PLANE_RECORD_COUNT")))
        printed = sum(1 for l in output.splitlines() if l.strip().startswith("lease #"))
        self.assertEqual(declared, printed)


class TheProbeSeesDivergenceAndAgreement(unittest.TestCase):
    """The durable form of the measurement that found the defect.

    NEGATIVE ARM: two checkouts holding different lease histories must come back DIVERGENT.
    POSITIVE ARM: three directories of one checkout must come back UNIFORM.
    Without the second, a probe that always says DIVERGENT would pass the first.
    """

    def probe(self, *dirs):
        result = subprocess.run(
            [sys.executable, str(HERE / "control_plane_probe.py"), *[str(d) for d in dirs]],
            capture_output=True, text=True)
        return result.returncode, result.stdout + result.stderr

    def test_three_directories_of_one_checkout_are_uniform(self):
        code, output = self.probe(ROOT, ROOT / "framework", ROOT / "framework" / "scripts")
        self.assertEqual(code, 0, output)
        self.assertIn("UNIFORM", output)

    def divergent_peer(self) -> Path:
        """A second checkout of this repository whose lease history differs by one record.

        Built here rather than named: the first draft pointed at one machine's peer worktree
        by absolute path and skipped everywhere else, so the negative arm never ran off that
        machine. A detached worktree of HEAD plus one appended lease block is the same
        divergence, reproducible on any clone.
        """
        box = Path(tempfile.mkdtemp())
        peer = box / "peer"
        subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "-q", "--detach",
                        str(peer), "HEAD"], check=True, capture_output=True)

        def cleanup():
            subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(peer)],
                           capture_output=True)
            subprocess.run(["git", "-C", str(ROOT), "worktree", "prune"], capture_output=True)
            shutil.rmtree(box, ignore_errors=True)

        self.addCleanup(cleanup)
        lease = peer / LEASE
        if not lease.is_file():
            self.skipTest(f"{LEASE} is not tracked at HEAD, so no lease lineage can diverge")
        with lease.open("a", encoding="utf-8") as handle:
            handle.write("\n## LEASE (test fixture)\n\n- `LEASE_ID`: TEST-DIVERGENCE-000\n"
                         "- `HOLDER`: test\n- `STATE`: RELEASED\n")
        return peer

    def test_two_checkouts_with_different_histories_diverge(self):
        other = self.divergent_peer()
        code, output = self.probe(ROOT, other)
        self.assertEqual(code, 1, output)
        self.assertIn("DIVERGENT", output)

    def test_divergence_is_reported_as_a_measurement_not_a_verdict(self):
        other = self.divergent_peer()
        _, output = self.probe(ROOT, other)
        self.assertIn("not this tool's to say", output)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
