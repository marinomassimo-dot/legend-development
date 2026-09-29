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

    def test_refusal_names_the_full_fallback(self) -> None:
        from batch_commit import propagate
        with tempfile.TemporaryDirectory() as temporary:
            self._repo(temporary, self.CLAIMS)
            ops = self._ops(temporary, [{"op": "delete", "id": "CLAIM 404"}])
            code, message = propagate(temporary, self.CLAIMS, ops, apply=True)
            self.assertEqual(code, 3)
            self.assertIn(f"FULL_FALLBACK {self.CLAIMS} ANCHOR_MISSING", message)

    def test_a_b2_shaped_op_is_refused_at_propagate_and_declarable(self) -> None:
        """🔴 The batch-level half of `CROSS_LINE_MOVE`, and why no separate batch check is added.

        The refusal lives in the editor, so `propagate` inherits it for free — earliest, cheapest,
        and it reaches every caller. It needs no op-list-wide counterpart: `apply_ops` anchors each
        op on the text the previous one produced, so a split done by two ops is seen by the second;
        and content cannot cross RECORDS at all, because every other block must stay byte-identical.
        """
        from batch_commit import propagate
        grounds = ("L'evidenza di questa claim e il topo Wwox+/- e i portatori umani: un genotipo "
                   "null/wild-type, con un allele pienamente funzionale. La classe che sopravvive "
                   "meglio in CLAIM 033 porta un allele missense di funzione residua non misurata. "
                   "Concatenarle implica una equivalenza funzionale che nessuna fonte misura.")
        self.assertGreaterEqual(len(grounds.encode()), 200, "the fixture must reach the floor")
        infer = "DO_NOT_INFER — questa claim e CLAIM 033 concordano, e la catena e vietata."
        cite = "DO_NOT_CITE — the P47T/WT heterozygote is not a demonstrated negative."
        text = f"# Claim Registry\n\n## CLAIM 032\n{infer} {grounds}\n{cite}\n"
        moved = f"# Claim Registry\n\n## CLAIM 032\n{infer}\n{cite} {grounds}\n"
        self.assertEqual(len(text.encode()), len(moved.encode()), "B2 was byte-conserving")
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / self.CLAIMS
            path.parent.mkdir(parents=True)
            path.write_bytes(text.encode())
            block = moved[moved.index("## CLAIM 032"):]
            ops = self._ops(temporary, [{"op": "replace", "id": "CLAIM 032", "text": block}])
            code, message = propagate(temporary, self.CLAIMS, ops, apply=True)
            self.assertEqual(code, 3)
            self.assertIn(f"FULL_FALLBACK {self.CLAIMS} CROSS_LINE_MOVE", message)
            self.assertEqual(path.read_bytes(), text.encode(), "a refusal writes nothing")
            declared = self._ops(temporary, [{"op": "replace", "id": "CLAIM 032",
                                              "text": block, "reflow": True}])
            code, message = propagate(temporary, self.CLAIMS, declared, apply=True)
            self.assertEqual(code, 0, message)
            self.assertEqual(path.read_bytes(), moved.encode())

    def test_paper_registry_is_record_scoped_and_under_names_one_purpose(self) -> None:
        """J5: the paper registry joins the other three; its twin `## Purpose` needs `under`."""
        from batch_commit import RECORD_SCOPED, propagate
        papers = "disease-models/wwox/registries/paper_registry_current.md"
        self.assertIn(papers, RECORD_SCOPED)
        self.assertEqual(set(RECORD_SCOPED), set(CURRENTS))
        text = ("# Paper Registry Current\n\n## Purpose\nfirst\n\n## PAPER 001\nbody\n\n"
                "# Triage Corpus\n\n## Purpose\nsecond\n\n## CORPUS P200\nstub\n")
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / papers
            path.parent.mkdir(parents=True)
            path.write_bytes(text.encode())
            bare = self._ops(temporary, [{"op": "replace-within", "heading": "Purpose",
                                          "old": "second", "new": "2nd"}])
            code, message = propagate(temporary, papers, bare, apply=True)
            self.assertEqual(code, 3)
            self.assertIn("ANCHOR_AMBIGUOUS", message)
            self.assertIn("FULL_FALLBACK", message)
            self.assertEqual(path.read_bytes(), text.encode())
            qualified = self._ops(temporary, [
                {"op": "replace-within", "heading": "Purpose", "under": "Triage Corpus",
                 "old": "second", "new": "2nd"},
                {"op": "replace-within", "id": "PAPER 001", "old": "body", "new": "body, read"}])
            code, message = propagate(temporary, papers, qualified, apply=True)
            self.assertEqual(code, 0, message)
            self.assertEqual(path.read_bytes(),
                             text.replace("second", "2nd").replace("body\n", "body, read\n").encode())

    def test_the_command_line_exits_with_the_refusal_code(self) -> None:
        """A batch mid-propagation keys on the PROCESS exit status, not on the function's return:
        4 for a file outside the four, 3 for an editor refusal, 0 for a clean dry run."""
        import subprocess
        import sys
        script = Path(__file__).resolve().parent / "batch_commit.py"
        with tempfile.TemporaryDirectory() as temporary:
            self._repo(temporary, self.CLAIMS)
            other = Path(temporary) / "disease-models/wwox/registries/working_model_history.md"
            other.write_text("# History\n", encoding="utf-8")
            cases = (
                ("disease-models/wwox/registries/working_model_history.md", [], 4),
                (self.CLAIMS, [{"op": "delete", "id": "CLAIM 404"}], 3),
                (self.CLAIMS, [{"op": "replace-within", "id": "CLAIM 002",
                                "old": "in observation", "new": "x"}], 0),
            )
            for rel, ops, code in cases:
                with self.subTest(rel=rel, expected=code):
                    done = subprocess.run(
                        [sys.executable, str(script), "propagate", "--repo-root", temporary,
                         "--file", rel, "--ops", self._ops(temporary, ops)],
                        capture_output=True, text=True)
                    self.assertEqual(done.returncode, code, done.stdout + done.stderr)
                    self.assertEqual(f"exit {code}:" in done.stderr, code != 0, done.stderr)

    def test_a_file_outside_the_four_is_refused_by_name(self) -> None:
        from batch_commit import propagate
        other = "disease-models/wwox/research/some_note.md"
        with tempfile.TemporaryDirectory() as temporary:
            path = self._repo(temporary, other)
            ops = self._ops(temporary, [{"op": "delete", "id": "CLAIM 001"}])
            code, message = propagate(temporary, other, ops, apply=True)
            self.assertEqual(code, 4)
            self.assertEqual(path.read_bytes(), self.TEXT.encode())


class DriftDetectsAMovedMain(unittest.TestCase):
    """`drift` — optimistic, early, and from identities: did main move under this batch?

    Real repositories, a real upstream commit: the 2026-09-28 incident (two batches numbered
    BATCH_20260928_004) was found only by a textual merge conflict at landing.
    """

    CLAIMS = "disease-models/wwox/registries/claim_registry_current.md"
    CANDIDATE_DIR = "disease-models/wwox/research/commit_candidates"

    def _git(self, *arguments, cwd=None):
        done = subprocess.run(("git", *arguments), cwd=cwd or self.repo, capture_output=True,
                              text=True)
        self.assertEqual(done.returncode, 0, done.stderr)
        return done.stdout.strip()

    def _write(self, rel, text, cwd=None):
        path = Path(cwd or self.repo) / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.repo = Path(self._tmp.name) / "root"
        self.repo.mkdir()
        self._git("init", "-q", "-b", "main")
        self._git("config", "user.name", "drift-test")
        self._git("config", "user.email", "drift@example.invalid")
        self._write(self.CLAIMS, "# Claims\n\n## CLAIM 001\nbody\n")
        self._write("framework/state/state_history.md", "```yaml\nbatch_20260101_001_scope: x\n```\n")
        self._write("notes/unrelated.md", "n\n")
        self._write(f"{self.CANDIDATE_DIR}/CC-A-01.md", "# A\n")
        self._git("add", "-A")
        self._git("commit", "-q", "-m", "base")
        # the actor's task branch, cut from the base
        self._git("branch", "task/mine")
        self.targets = [self.CLAIMS, "framework/state/state_history.md"]

    def _upstream(self, message, **files):
        """Another actor lands on main while `task/mine` stays where it was."""
        self._git("switch", "-q", "main")
        for rel, text in files.items():
            self._write(rel.replace("__", "/"), text)
        self._git("add", "-A")
        self._git("commit", "-q", "-m", message)
        self._git("switch", "-q", "task/mine")

    def _drift(self, **kwargs):
        from batch_commit import drift
        return drift(str(self.repo), against="main", targets=self.targets, **kwargs)

    def test_nothing_landed_is_fresh(self) -> None:
        self._git("switch", "-q", "task/mine")
        report = self._drift(batch_id="BATCH_20260101_002")
        self.assertFalse(report["stale"])
        self.assertEqual(report["behind"], 0)

    def test_unrelated_upstream_movement_is_fresh_and_says_so(self) -> None:
        from batch_commit import render_drift
        self._git("switch", "-q", "task/mine")
        self._upstream("harness elsewhere", **{"notes/unrelated.md".replace("/", "__"): "changed\n"})
        report = self._drift(batch_id="BATCH_20260101_002", candidates=["CC-A-01"])
        self.assertEqual((report["stale"], report["behind"]), (False, 1))
        self.assertIn("touch none of the declared surfaces", render_drift(report))

    def test_a_declared_surface_changed_upstream_is_stale(self) -> None:
        self._git("switch", "-q", "task/mine")
        self._upstream("a batch", **{self.CLAIMS.replace("/", "__"): "# Claims\n\n## CLAIM 001\nnew\n"})
        report = self._drift()
        self.assertTrue(report["stale"])
        self.assertEqual(report["files"], [self.CLAIMS])

    def test_the_duplicate_batch_id_of_2026_09_28_is_a_collision(self) -> None:
        from batch_commit import render_drift
        self._git("switch", "-q", "task/mine")
        self._upstream("BATCH_20260101_002 landed", **{
            "framework/state/state_history.md".replace("/", "__"):
                "```yaml\nbatch_20260101_002_scope: y\nbatch_20260101_001_scope: x\n```\n"})
        report = self._drift(batch_id="BATCH_20260101_002")
        self.assertTrue(report["collision"] and report["stale"])
        self.assertEqual(report["batches"], ["BATCH_20260101_002"])
        self.assertIn("BATCH ID COLLISION", render_drift(report))
        self.assertFalse(self._drift(batch_id="BATCH_20260101_003")["collision"])

    def test_a_candidate_touched_upstream_is_named(self) -> None:
        self._git("switch", "-q", "task/mine")
        self._upstream("disposition", **{f"{self.CANDIDATE_DIR}/CC-A-01.md".replace("/", "__"): "# A\ndisposed\n"})
        report = self._drift(candidates=["CC-A-01", "CC-B-02"])
        self.assertEqual((report["stale"], report["candidates"]), (True, ["CC-A-01"]))

    def test_after_merging_main_the_same_question_is_fresh(self) -> None:
        self._git("switch", "-q", "task/mine")
        self._upstream("a batch", **{self.CLAIMS.replace("/", "__"): "# Claims\n\n## CLAIM 001\nnew\n"})
        self.assertTrue(self._drift()["stale"])
        self._git("merge", "-q", "--no-edit", "main")
        self.assertFalse(self._drift()["stale"])

    def test_the_command_line_exits_5_stale_0_fresh_2_unresolvable(self) -> None:
        import contextlib
        import io
        from batch_commit import main
        self._write("disease-models/wwox/registries/x.md", "x\n")
        # a protocol declaration naming the two surfaces, so the CLI can derive its targets
        self._write("framework/protocols/prompt_batch_commit.md",
                    "SNAPSHOT_DECLARATION (x)\n```\n  - " + self.CLAIMS
                    + "\n  - framework/state/state_history.md\n```\n")
        self._git("add", "-A")
        self._git("commit", "-q", "-m", "protocol")
        self._git("branch", "-f", "task/mine")
        self._git("switch", "-q", "task/mine")
        self._upstream("a batch", **{self.CLAIMS.replace("/", "__"): "# Claims\n\n## CLAIM 001\nnew\n"})
        codes = {}
        for label, argv in (("stale", ["drift", "--repo-root", str(self.repo), "--against", "main"]),
                            ("fresh", ["drift", "--repo-root", str(self.repo), "--against", "HEAD"]),
                            ("bad", ["drift", "--repo-root", str(self.repo), "--against", "no-such-ref"])):
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                codes[label] = main(argv)
        self.assertEqual(codes, {"stale": 5, "fresh": 0, "bad": 2})


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
