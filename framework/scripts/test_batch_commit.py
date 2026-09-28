#!/usr/bin/env python3
"""Round-trip test for the public BATCH_COMMIT snapshot helper."""

from __future__ import annotations

import contextlib
import io
import subprocess
import tempfile
import unittest
from pathlib import Path

import shutil

import batch_commit
from batch_commit import main, restore, snapshot
from legend_lint import CURRENTS

REPO = Path(__file__).resolve().parents[2]


def declared_fixture(root: Path) -> list[str]:
    """A temp root carrying the real snapshot declaration and every file it names.

    Since 2026-09-28 the snapshot's coverage comes from `prompt_batch_commit.md`, and it
    REFUSES when a declared path is absent — so a fixture that wants a snapshot must hold the
    declaration and the declared files, exactly as the repository does.
    """
    (root / batch_commit.PROTOCOL).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO / batch_commit.PROTOCOL, root / batch_commit.PROTOCOL)
    written = []
    for pattern in batch_commit.declared_patterns(str(root)):
        if any(character in pattern for character in "*?["):
            continue  # an empty family is legitimate; nothing to materialise
        (root / pattern).parent.mkdir(parents=True, exist_ok=True)
        (root / pattern).write_text(f"seed {pattern}\n", encoding="utf-8")
        written.append(pattern)
    return written


class SnapshotTests(unittest.TestCase):
    def test_snapshot_then_restore_in_temporary_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            declared_fixture(root)
            current = root / CURRENTS[0]
            current.write_text("v1", encoding="utf-8")
            state = root / "framework/state/state_manifest_current.md"
            state.write_text("current_state: READY\n", encoding="utf-8")

            snapshot_dir = root / "backup" / "snapshot"
            snapshot(str(root), str(snapshot_dir))
            current.write_text("corrupted", encoding="utf-8")
            state.write_text("current_state: BROKEN\n", encoding="utf-8")
            restore(str(snapshot_dir), str(root))

            self.assertEqual(current.read_text(encoding="utf-8"), "v1")
            self.assertEqual(
                state.read_text(encoding="utf-8"),
                "current_state: READY\n",
            )

    def test_the_state_history_is_restored_with_the_manifest(self) -> None:
        """A batch writes its scope to the cold half; an ABORT must not keep that half."""
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            declared_fixture(root)
            history = root / "framework/state/state_history.md"
            history.write_text("batch_1_scope: before\n", encoding="utf-8")
            snapshot_dir = root / "backup" / "snapshot"
            snapshot(str(root), str(snapshot_dir))
            history.write_text("batch_2_scope: half a batch\n", encoding="utf-8")
            restore(str(snapshot_dir), str(root))
            self.assertEqual(history.read_text(encoding="utf-8"), "batch_1_scope: before\n")

    def test_restore_cli_requires_explicit_confirmation(self) -> None:
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as context:
                main(
                    [
                        "restore",
                        "--snapshot-dir",
                        "/tmp/example-snapshot",
                        "--repo-root",
                        "/tmp/example-repo",
                    ]
                )
        self.assertEqual(2, context.exception.code)


class RecordScopedPropagation(unittest.TestCase):
    """``propagate`` — Phase 4 for the files Benchmark J supported, refused for the others."""

    CLAIMS = "disease-models/wwox/registries/claim_registry_current.md"
    TEXT = ("# Claim Registry Current\n\n## CLAIM 001\n**Status:** in observation\n\n---\n\n"
            "## CLAIM 002\n**Status:** in observation\n")

    def _repo(self, temporary: str, rel: str) -> Path:
        path = Path(temporary) / rel
        path.parent.mkdir(parents=True)
        path.write_bytes(self.TEXT.encode())
        return path

    def _ops(self, temporary: str, ops: list) -> str:
        import json
        path = Path(temporary) / "ops.json"
        path.write_text(json.dumps(ops), encoding="utf-8")
        return str(path)

    def test_supported_file_dry_run_then_apply(self) -> None:
        from batch_commit import propagate
        with tempfile.TemporaryDirectory() as temporary:
            path = self._repo(temporary, self.CLAIMS)
            ops = self._ops(temporary, [{"op": "replace-within", "id": "CLAIM 002",
                                         "old": "in observation", "new": "consolidated baseline"}])
            code, message = propagate(temporary, self.CLAIMS, ops)
            self.assertEqual((code, path.read_bytes()), (0, self.TEXT.encode()), message)
            code, message = propagate(temporary, self.CLAIMS, ops, apply=True)
            self.assertEqual(code, 0, message)
            expected = self.TEXT[::-1].replace("in observation"[::-1],
                                               "consolidated baseline"[::-1], 1)[::-1]
            self.assertEqual(path.read_bytes(), expected.encode())

    def test_refusal_writes_nothing(self) -> None:
        from batch_commit import propagate
        with tempfile.TemporaryDirectory() as temporary:
            path = self._repo(temporary, self.CLAIMS)
            ops = self._ops(temporary, [{"op": "replace-within", "id": "CLAIM 001",
                                         "old": "in observation", "new": "x"},
                                        {"op": "delete", "id": "CLAIM 404"}])
            code, message = propagate(temporary, self.CLAIMS, ops, apply=True)
            self.assertEqual(code, 3)
            self.assertIn("ANCHOR_MISSING", message)
            self.assertEqual(path.read_bytes(), self.TEXT.encode())

    def test_paper_registry_keeps_the_full_rewrite(self) -> None:
        from batch_commit import RECORD_SCOPED, propagate
        papers = "disease-models/wwox/registries/paper_registry_current.md"
        self.assertNotIn(papers, RECORD_SCOPED)
        self.assertTrue(set(RECORD_SCOPED) <= set(CURRENTS))
        with tempfile.TemporaryDirectory() as temporary:
            path = self._repo(temporary, papers)
            ops = self._ops(temporary, [{"op": "delete", "id": "CLAIM 001"}])
            code, message = propagate(temporary, papers, ops, apply=True)
            self.assertEqual(code, 4)
            self.assertIn("full rewrite", message)
            self.assertEqual(path.read_bytes(), self.TEXT.encode())


class TheRealCurrentFilesAreSnapshotted(unittest.TestCase):
    """``snapshot`` through ``main`` over this checkout: the four current files and the state
    manifest are copied OUT to a temp dir, byte-identical, and the originals are untouched.
    ``restore`` is never pointed at the real root here — that is the BATCH_COMMIT's act, and
    a suite that did it would be the 2026-09-10 incident with a different verb."""

    ROOT = Path(__file__).resolve().parents[2]

    def test_snapshot_copies_every_present_current_file_and_writes_nothing_back(self) -> None:
        # The population is the protocol's declaration, not a list repeated here: that
        # duplication is exactly the defect of 2026-09-28. `test_batch_commit_snapshot.py`
        # owns the declaration's own coverage; this case owns byte fidelity and no write-back.
        present = [rel for rel in batch_commit.snapshot_targets(str(self.ROOT))
                   if (self.ROOT / rel).is_file()]
        if not present:
            self.skipTest("skipped: no current file present in this checkout")
        before = {rel: (self.ROOT / rel).read_bytes() for rel in present}
        with tempfile.TemporaryDirectory() as temporary:
            dest = Path(temporary) / "snapshot"
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                code = main(["snapshot", "--repo-root", str(self.ROOT), "--dest", str(dest)])
            self.assertEqual(code, 0)
            self.assertIn(f"Snapshot written to {dest}", buffer.getvalue())
            for rel in present:
                self.assertEqual((dest / rel).read_bytes(), before[rel], rel)
            # `snapshot_contents` is the repository's own answer to "what does this snapshot
            # hold", and it is what `restore` copies back — so the fidelity assertion is made
            # against it rather than against a raw walk. The raw walk also holds
            # `SNAPSHOT_BASE.json`, which is metadata about the snapshot and must NOT be
            # restored into the repository root; the two cases below pin both halves.
            copied = batch_commit.snapshot_contents(str(dest))
            self.assertEqual(copied, sorted(present),
                             "the snapshot copied more or less than declared")
            self.assertTrue((dest / batch_commit.BASE_FILE).is_file(),
                            "Phase 3 requires the pre-batch commit beside the snapshot")
            base = batch_commit.read_base(str(dest))
            self.assertRegex(base["pre_batch_commit"], r"^[0-9a-f]{40}$")
            self.assertIn(base["pre_batch_commit"], buffer.getvalue(),
                          "the SHA must be printed where the aborting actor reads it")
        self.assertEqual({rel: (self.ROOT / rel).read_bytes() for rel in present}, before,
                         "snapshot wrote a current file")


class TheSnapshotCarriesItsAbortBase(unittest.TestCase):
    """🔴 `git checkout -- <path>` is correct only in the window the ABORT does not live in.

    Phase 3 said "restore" without saying "from which base". Before the propagation is staged
    that command restores the pre-batch value; from the first `git add` onward it restores the
    BATCH's own output and exits 0. The Phase 5 ABORT fires after the propagation, so the
    command a protocol reader was given was right in the wrong window. The repair is a base:
    recorded once at Phase 3, where it is the only moment it is knowable.
    """

    def repository(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        declared_fixture(root)
        run = lambda *a: subprocess.run(("git", *a), cwd=root, check=True,
                                        capture_output=True, text=True)
        run("init", "-q")
        run("config", "user.email", "t@example.invalid")
        run("config", "user.name", "t")
        run("add", "-A")
        run("commit", "-qm", "pre-batch")
        return root, run

    def test_the_base_is_the_commit_before_the_batch_wrote_anything(self) -> None:
        root, run = self.repository()
        head = run("rev-parse", "HEAD").stdout.strip()
        snapshot(str(root), str(root / "backup" / "snap"))
        target = root / CURRENTS[0]
        target.write_text("propagated by the batch\n", encoding="utf-8")
        run("add", "-A")
        run("commit", "-qm", "propagation")

        base = batch_commit.read_base(str(root / "backup" / "snap"))
        self.assertEqual(base["pre_batch_commit"], head)
        # The defect, demonstrated: the bare command restores the batch, and says nothing.
        run("checkout", "--", CURRENTS[0])
        self.assertEqual(target.read_text(encoding="utf-8"), "propagated by the batch\n")
        # The base-qualified command is the one that is correct in this window.
        run("checkout", base["pre_batch_commit"], "--", CURRENTS[0])
        self.assertEqual(target.read_text(encoding="utf-8"), f"seed {CURRENTS[0]}\n")

    def test_a_path_already_dirty_at_snapshot_is_named_as_sha_unrestorable(self) -> None:
        root, _ = self.repository()
        (root / CURRENTS[0]).write_text("in flight before the batch\n", encoding="utf-8")
        snapshot(str(root), str(root / "backup" / "snap"))
        base = batch_commit.read_base(str(root / "backup" / "snap"))
        self.assertIn(CURRENTS[0], base["dirty_at_snapshot"])
        self.assertIn(CURRENTS[0], batch_commit.base_report(str(root / "backup" / "snap")))

    def test_the_base_file_is_not_restored_into_the_repository(self) -> None:
        root, _ = self.repository()
        snapshot(str(root), str(root / "backup" / "snap"))
        restored = restore(str(root / "backup" / "snap"), str(root))
        self.assertNotIn(batch_commit.BASE_FILE, restored)
        self.assertFalse((root / batch_commit.BASE_FILE).exists())

    def test_base_subcommand_reports_and_refuses_a_snapshot_without_one(self) -> None:
        root, _ = self.repository()
        snapshot(str(root), str(root / "backup" / "snap"))
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            self.assertEqual(main(["base", "--snapshot-dir", str(root / "backup" / "snap")]), 0)
        self.assertIn("PRE_BATCH_COMMIT:", buffer.getvalue())
        self.assertIn("git checkout", buffer.getvalue())

        bare = root / "backup" / "legacy"
        bare.mkdir(parents=True)
        with contextlib.redirect_stderr(io.StringIO()) as problem:
            self.assertEqual(main(["base", "--snapshot-dir", str(bare)]), 1)
        self.assertIn("records no base", problem.getvalue())

    def test_a_non_git_tree_still_snapshots_and_says_why_there_is_no_sha(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        declared_fixture(root)
        snapshot(str(root), str(root / "backup" / "snap"))
        base = batch_commit.read_base(str(root / "backup" / "snap"))
        self.assertIsNone(base["pre_batch_commit"])
        self.assertIn("only restore source", base["note"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
