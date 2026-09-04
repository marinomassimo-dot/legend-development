#!/usr/bin/env python3
"""The destination parser is checked against REAL GIT, not against spellings I thought of.

Two hand-rolled versions of `worktree_add_destination` shipped holes, and both were found
by a reviewer rather than by this repository's own tests, for the same reason each time:
the test population was "argument spellings that occurred to the author". Version one
missed `--reason <decoy> <peer>`. Version two missed `-fb hijack <peer>`, which git parses
as `-f` plus `-b hijack`. Enumerating harder is the strategy that has now failed twice.

So the oracle is git itself. Each spelling below is executed in a throwaway repository, and
the directory git ACTUALLY creates is compared with the path the guard predicted. A
disagreement is a finding whether it points at a bypass (guard predicted somewhere
harmless, git wrote somewhere else) or at a control wrongly refused (guard predicted
nothing, git wrote a checkout).

🔴 The comparison is one-directional on purpose. The guard is allowed to predict None where
git succeeds — that denies, which is safe. It is NOT allowed to predict a path git did not
write, because that is the shape both holes took: a decoy judged while the real destination
went unlooked-at.

This test needs a real `git` and skips without one rather than asserting on its absence.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import guard_policy as gp  # noqa: E402

# `DEST` is substituted with the throwaway destination, `REF` with a valid branch name.
SPELLINGS = [
    "add DEST",
    "add DEST -b REF",
    "add -b REF DEST",
    "add -B REF DEST",
    "add DEST -B REF",
    "add -bREF DEST",
    "add -BREF DEST",
    "add -fb REF DEST",
    "add -fB REF DEST",
    "add -qb REF DEST",
    "add -fbREF DEST",
    "add -f -b REF DEST",
    "add --force -b REF DEST",
    "add --detach DEST",
    "add --lock DEST",
    "add --lock --reason locked DEST",
    "add --reason=locked --lock DEST",
    "add --no-checkout DEST",
    "add --orphan DEST",
    "add DEST --orphan",
    "add --quiet DEST",
    "add -- DEST",
    "add --checkout DEST",
    "add --lock --reason locked -b REF DEST",
    "add -b REF -- DEST",
]


def git_available() -> bool:
    return shutil.which("git") is not None


class TheParserAgreesWithGit(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if not git_available():
            raise unittest.SkipTest("no git on PATH")
        cls._tmp = tempfile.TemporaryDirectory()
        cls.origin = Path(cls._tmp.name) / "origin"
        cls.origin.mkdir(parents=True)
        for argv in (["init", "-q", "-b", "main"],
                     ["-c", "user.email=t@t", "-c", "user.name=t",
                      "commit", "-q", "--allow-empty", "-m", "base"]):
            subprocess.run(["git", "-C", str(cls.origin), *argv], check=True,
                           capture_output=True, text=True)

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def what_git_creates(self, argv: list[str], destination: Path):
        """Run it for real, and report whether that directory came into existence."""
        result = subprocess.run(["git", "-C", str(self.origin), "worktree", *argv],
                                capture_output=True, text=True)
        created = destination.is_dir()
        if created:
            subprocess.run(["git", "-C", str(self.origin), "worktree", "remove",
                            "--force", str(destination)], capture_output=True, text=True)
            shutil.rmtree(destination, ignore_errors=True)
        return created, result.returncode

    def test_the_guard_never_predicts_a_path_git_did_not_write(self) -> None:
        disagreements = []
        for index, template in enumerate(SPELLINGS):
            destination = Path(self._tmp.name) / f"wt{index}"
            argv = template.replace("DEST", str(destination)).replace(
                "REF", f"br{index}").split()
            created, code = self.what_git_creates(argv, destination)
            predicted = gp.worktree_add_destination(argv)
            if not created:
                # git refused the spelling; the guard's answer cannot be wrong about a
                # write that never happens, so this case carries no claim either way.
                continue
            if predicted is None:
                # Allowed: predicting nothing DENIES, which is the safe direction.
                continue
            if Path(predicted) != destination:
                disagreements.append(
                    f"{template!r}: git wrote {destination}, guard predicted {predicted!r}")
        self.assertEqual(
            [], disagreements,
            "the guard predicted a destination git did not write — this is the exact shape "
            "of both shipped holes, a decoy judged while the real path went unlooked-at:\n  "
            + "\n  ".join(disagreements))

    def test_the_oracle_actually_exercises_something(self) -> None:
        """POSITIVE CONTROL: if git refused every spelling, the test above is vacuous."""
        created_count = 0
        for index, template in enumerate(SPELLINGS):
            destination = Path(self._tmp.name) / f"ctl{index}"
            argv = template.replace("DEST", str(destination)).replace(
                "REF", f"cb{index}").split()
            created, _ = self.what_git_creates(argv, destination)
            created_count += int(created)
        self.assertGreaterEqual(
            created_count, len(SPELLINGS) - 3,
            f"git only created {created_count}/{len(SPELLINGS)} worktrees, so the "
            "comparison above is mostly skipping rather than agreeing")

    def test_a_deliberately_broken_parser_is_caught_by_this_oracle(self) -> None:
        """The differential test must be able to FAIL, or it certifies nothing.

        Reproduces version two's defect — treating a short cluster as one opaque flag —
        and requires the comparison to notice.
        """
        def broken(rest):
            tokens = [t for t in rest if not t.startswith("-")]
            if tokens and tokens[0] == "add":
                tokens = tokens[1:]
            return tokens[0] if tokens else None

        caught = []
        for index, template in enumerate(SPELLINGS):
            destination = Path(self._tmp.name) / f"brk{index}"
            argv = template.replace("DEST", str(destination)).replace(
                "REF", f"kb{index}").split()
            predicted = broken(argv)
            if predicted is not None and Path(predicted) != destination:
                caught.append(template)
        self.assertTrue(
            caught,
            "the broken parser agreed with git on every spelling, so this oracle would "
            "not have caught either shipped hole")


if __name__ == "__main__":
    unittest.main(verbosity=2)
