#!/usr/bin/env python3
"""Round-trip test for the public BATCH_COMMIT snapshot helper."""

from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from batch_commit import main, restore, snapshot
from legend_lint import CURRENTS


class SnapshotTests(unittest.TestCase):
    def test_snapshot_then_restore_in_temporary_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            current = root / CURRENTS[0]
            current.parent.mkdir(parents=True)
            current.write_text("v1", encoding="utf-8")
            state = root / "framework/state/state_manifest_current.md"
            state.parent.mkdir(parents=True)
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


class TheRealCurrentFilesAreSnapshotted(unittest.TestCase):
    """``snapshot`` through ``main`` over this checkout: the four current files and the state
    manifest are copied OUT to a temp dir, byte-identical, and the originals are untouched.
    ``restore`` is never pointed at the real root here — that is the BATCH_COMMIT's act, and
    a suite that did it would be the 2026-09-10 incident with a different verb."""

    ROOT = Path(__file__).resolve().parents[2]

    def test_snapshot_copies_every_present_current_file_and_writes_nothing_back(self) -> None:
        from batch_commit import EXTRA
        present = [rel for rel in CURRENTS + EXTRA if (self.ROOT / rel).is_file()]
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
    unittest.main()
