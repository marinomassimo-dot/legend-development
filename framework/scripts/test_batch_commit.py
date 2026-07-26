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


if __name__ == "__main__":
    unittest.main()
