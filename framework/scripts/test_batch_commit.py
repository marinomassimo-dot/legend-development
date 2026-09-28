#!/usr/bin/env python3
"""Round-trip test for the public BATCH_COMMIT snapshot helper."""

from __future__ import annotations

import contextlib
import io
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
            copied = sorted(p.relative_to(dest).as_posix() for p in dest.rglob("*") if p.is_file())
            self.assertEqual(copied, sorted(present), "the snapshot copied more or less than declared")
        self.assertEqual({rel: (self.ROOT / rel).read_bytes() for rel in present}, before,
                         "snapshot wrote a current file")


if __name__ == "__main__":
    unittest.main(verbosity=2)
