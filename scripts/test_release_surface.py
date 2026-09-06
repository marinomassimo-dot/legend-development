#!/usr/bin/env python3
"""Ensure .gitignore cannot silently remove public capabilities at publication."""

from __future__ import annotations

import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# One definition of "this directory is another checkout", shared with the publication gate.
_GATE_PATH = Path(__file__).with_name("public_release_gate.py")
_SPEC = importlib.util.spec_from_file_location("public_release_gate", _GATE_PATH)
assert _SPEC and _SPEC.loader
GATE = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = GATE
_SPEC.loader.exec_module(GATE)
EXPECTED_IGNORED_PARTS = {
    ".DS_Store",
    "__pycache__",
    "node_modules",
}
EXPECTED_IGNORED_SUFFIXES = {".pyc", ".log", ".dcd"}
# Explicit private runtime surfaces, not public capabilities hidden by a broad glob.
LOCAL_RUNTIME_FILES = {".claude/settings.local.json", "deployment/local_instance.md"}
REQUIRED_ROOT_FILES = {
    ".gitignore",
    "LICENSE",
    "README.md",
    "DATA_SOURCES.md",
    "THIRD_PARTY_NOTICES.md",
}
FORBIDDEN_PUBLIC_DIRECTORIES = {
    "_qa",
    "backup",
    "files",
    "overlay",
    "staging",
}
MAX_PUBLIC_FILE_BYTES = 20 * 1024 * 1024


def tracked_paths() -> frozenset[str]:
    """Files in the index — i.e. the ones that actually reach a published clone."""
    completed = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        check=False, capture_output=True, text=True,
    )
    return frozenset(entry for entry in completed.stdout.split("\0") if entry)


class TheIndexIsThePopulation(unittest.TestCase):
    """🔴 Five checks in this file take `tracked_paths()` as their population, and an empty
    population makes all five pass without examining anything.

    `check=False` means a git failure returns no output rather than raising, so outside a
    checkout every one of them is vacuous. Found on 2026-08-11 by the mutation battery: the
    "executable bit stripped" defect ESCAPED in the throwaway export the battery's own
    docstring tells you to use, because `git archive | tar -x` produces a directory with no
    index. The guard was never weak — it was never run.

    The same primitive in `public_release_gate.unpublishable_paths` returns empty outside a
    checkout deliberately, and is tested for it. That is correct THERE: an empty exemption
    list scans more, so its failure direction is strict. Here an empty population checks
    less. Same call, opposite safety direction, which is why this is a refusal rather than a
    copied behaviour.
    """

    def test_an_empty_index_is_a_refusal_not_a_pass(self) -> None:
        self.assertTrue(
            tracked_paths(),
            "git listed no tracked files, so every index-derived check in this file would "
            "pass without examining anything. Run this suite in a real checkout.")


def tracked_public_content_roots() -> frozenset[str]:
    """Top-level directories that hold at least one tracked (published) file.

    Derived from the index rather than hardcoded, so it can't go stale as the
    repository grows. A directory with no tracked files (`grants/`, `staging/`,
    `files/`, `backup/`, ...) is deliberately private working material, not a
    silently-hidden public capability — it is exempt by construction, the same
    way `unpublishable_paths` in public_release_gate.py exempts it.
    """
    return frozenset(
        entry.split("/", 1)[0] for entry in tracked_paths() if "/" in entry
    )


def recipe_accounted_images() -> frozenset[str]:
    """Images an `adjudications.json` declares, and therefore hides on purpose.

    🔴 A page-adjudication crop is deliberately kept out of the public edition: it
    reproduces the author's printed characters, and the articles adjudicated so far carry
    all-rights-reserved notices. But it sits beside a tracked `README.md` and a tracked
    recipe, so from this audit's point of view it looks exactly like a public file an
    ignore rule quietly swallowed — which is the accident this test exists to catch.

    The exemption is **derived from the recipe, never hand-listed**: only a file some
    `adjudications.json` names, with a digest, is allowed to be hidden. An image dropped
    into one of these directories without a recipe still fails, and that is the real
    hazard — a reproduction shipped or hidden with nothing accounting for it.
    """
    accounted: set[str] = set()
    for recipe in ROOT.glob("disease-models/*/research/page_adjudications/*/adjudications.json"):
        try:
            declared = json.loads(recipe.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        directory = recipe.parent.relative_to(ROOT)
        for artifact in declared.get("artifacts", []):
            name = artifact.get("file")
            if name and artifact.get("sha256"):
                accounted.add((directory / name).as_posix())
    return frozenset(accounted)


def is_expected_generated_path(relative: Path) -> bool:
    return (
        any(part in EXPECTED_IGNORED_PARTS for part in relative.parts)
        or relative.suffix in EXPECTED_IGNORED_SUFFIXES
        or relative.parts[:1] == ("md-output",)
        or relative.as_posix() in recipe_accounted_images()
    )


def walk_this_checkout(root: Path) -> list[Path]:
    """Every file of *this* checkout, refusing to descend into another one.

    🔴 This question has to be asked of the disk — that is the whole point of the audit, and
    an exemption keyed on `.gitignore` would answer it in a circle. But a checkout mounted
    inside this one is a different repository's disk, and walking into it made every one of
    its files look like a public file this repository had silently hidden: 351 of them, once
    per-session worktrees appeared under `.claude/worktrees/`.

    Pruning is the only correct instrument here, and `is_nested_checkout` is imported rather
    than re-implemented because a second copy of "what is a checkout" is how the first one
    stops being maintained.
    """
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        here = Path(dirpath)
        dirnames[:] = [name for name in dirnames
                       if not GATE.is_nested_checkout(here / name)]
        found.extend(here / name for name in filenames)
    return found


def unexpectedly_ignored_files() -> list[str]:
    files = sorted(
        path.relative_to(ROOT)
        for path in walk_this_checkout(ROOT)
        if path.is_file() and path.name != ".gitignore"
    )
    with tempfile.TemporaryDirectory(prefix="legend-ignore-audit-") as temporary:
        audit_root = Path(temporary)
        subprocess.run(
            ["git", "init", "--quiet", str(audit_root)],
            check=True,
            capture_output=True,
            text=True,
        )
        shutil.copy2(ROOT / ".gitignore", audit_root / ".gitignore")
        completed = subprocess.run(
            ["git", "-C", str(audit_root), "check-ignore", "--no-index", "--stdin"],
            input="\n".join(path.as_posix() for path in files) + "\n",
            check=False,
            capture_output=True,
            text=True,
        )
        ignored = {
            Path(line)
            for line in completed.stdout.splitlines()
            if line.strip()
        }
    # Checking "is this exact path tracked" is vacuous: a file that just got
    # newly hidden by an ignore-rule edit is untracked in the working tree by
    # definition (that's what "hidden" means), so it would never appear in the
    # index either. The actual risk is a public *directory* — one that already
    # ships tracked content — silently losing a new file to a broad pattern
    # like `*private*`. Scope the check to that: an ignored-and-untracked file
    # is a problem only when it sits under a directory the release already
    # tracks; directories with zero tracked files are private working areas by
    # construction (mirrors `unpublishable_paths` in public_release_gate.py).
    public_roots = tracked_public_content_roots()
    return sorted(
        path.as_posix()
        for path in ignored
        if not is_expected_generated_path(path) and path.parts[0] in public_roots
        and path.as_posix() not in LOCAL_RUNTIME_FILES
    )


class ReleaseSurfaceTests(unittest.TestCase):
    def test_local_runtime_files_are_explicitly_ignored_and_never_tracked(self) -> None:
        patterns = set((ROOT / ".gitignore").read_text().splitlines())
        self.assertTrue(LOCAL_RUNTIME_FILES <= patterns)
        self.assertFalse(LOCAL_RUNTIME_FILES & tracked_paths())

    def test_example_agent_policy_does_not_bypass_permissions(self) -> None:
        settings = json.loads(
            (ROOT / ".claude" / "settings.json.example").read_text(
                encoding="utf-8"
            )
        )
        mode = settings.get("permissions", {}).get("defaultMode")
        self.assertNotEqual(
            "bypassPermissions",
            mode,
            "The public host template must not disable permission checks",
        )

    def test_github_actions_are_pinned_to_commit_shas(self) -> None:
        workflow = (
            ROOT / ".github" / "workflows" / "public-release-gate.yml"
        ).read_text(encoding="utf-8")
        unpinned = [
            line.strip()
            for line in workflow.splitlines()
            if "uses:" in line
            and not re.search(r"@[0-9a-f]{40}(?:\s|$)", line)
        ]
        self.assertEqual(
            [],
            unpinned,
            "GitHub Actions must be pinned to immutable commit SHAs",
        )

    def test_no_public_file_is_silently_gitignored(self) -> None:
        ignored = unexpectedly_ignored_files()
        self.assertEqual(
            [],
            ignored,
            "Public files hidden by .gitignore:\n" + "\n".join(ignored),
        )

    def test_the_ignore_audit_does_not_walk_into_another_checkout(self) -> None:
        """Built here rather than found in the ambient tree.

        🔴 The audit must ask the disk, so no ignore rule can exempt anything from it — which
        means pruning is the only instrument available, and the only one that can be got
        wrong silently. When per-session worktrees appeared, 351 files of another checkout
        were reported as public files this repository had quietly hidden. The fix was then
        verified from inside a worktree, where a nested checkout cannot exist; the suite was
        green because the environment could not exhibit the defect, not because it was gone.
        """
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "own.md").write_text("# Ours\n", encoding="utf-8")
        nested = root / ".claude" / "worktrees" / "session"
        nested.mkdir(parents=True)
        subprocess.run(["git", "init", "-q"], cwd=nested, check=True)
        stray = nested / "hidden.md"
        stray.write_text("# Another repository's file\n", encoding="utf-8")

        walked = walk_this_checkout(root)
        self.assertIn(root / "own.md", walked)
        self.assertNotIn(stray, walked)
        self.assertIn(stray, [p for p in root.rglob("*") if p.is_file()],
                      "the fixture must be capable of failing, or it proves nothing")

    def test_required_release_files_exist(self) -> None:
        missing = sorted(
            name for name in REQUIRED_ROOT_FILES if not (ROOT / name).is_file()
        )
        self.assertEqual([], missing)

    # 🔴 These two asked the local disk a question only the published surface can answer, and
    # a live research workspace always answers wrong: `backup/`, `files/` and `staging/` exist
    # here by design and are gitignored, and one locally cached full text is over the size cap.
    # Both failures were true and permanent, so this file was permanently red — and on
    # 2026-08-06 it swallowed a real defect: two new shebang entrypoints shipped non-executable
    # and were reported as "only the environmental red". An alarm you have learned to ignore is
    # an alarm that will absorb the next real one, which is the argument this repository spent
    # the day making about seals over living state, arriving by the door nobody was watching.
    #
    # The fix is not to split the file or to weaken the checks: it is to ask the question they
    # actually mean. What ships is what git tracks. `tracked_paths()` was already here — its
    # own docstring already said a directory holding no tracked files is fine — and these two
    # simply did not use it. Scoping to tracked content is *stricter*, not looser: an
    # accidentally committed private root or oversized blob still fails, and now it fails
    # somewhere anyone will read.
    def test_no_private_quarantine_root_holds_tracked_content(self) -> None:
        offenders = sorted(
            path for path in tracked_paths()
            if path.split("/", 1)[0] in FORBIDDEN_PUBLIC_DIRECTORIES
        )
        self.assertEqual(
            [], offenders,
            "these tracked files live under a private quarantine root:\n  "
            + "\n  ".join(offenders))

    def test_no_symlinks_or_oversized_public_files(self) -> None:
        symlinks = []
        oversized = []
        for relative in sorted(tracked_paths()):
            path = ROOT / relative
            if path.is_symlink():
                symlinks.append(relative)
            elif path.is_file() and path.stat().st_size > MAX_PUBLIC_FILE_BYTES:
                oversized.append(f"{relative}: {path.stat().st_size} bytes")
        self.assertEqual([], symlinks, "Symlinks require explicit release review")
        self.assertEqual([], oversized, "Oversized files:\n" + "\n".join(oversized))

    # 🔴 These two were the last `rglob` walkers in this file. The comment above already says
    # it — "what ships is what git tracks" — and `tracked_paths()` was already here, used by
    # two other checks. The fourth instance in three days of a pattern solved at one site and
    # not carried to the next. It bit on 2026-08-09: five untracked scratch scripts in an
    # ignored directory turned this suite red, and the "fix" was to chmod files that will
    # never ship, to satisfy a release rule that was never about them. A release check that
    # polices private scratch space trains people to make the working tree lie.
    def test_paths_have_no_case_or_unicode_normalization_collisions(self) -> None:
        folded: dict[str, list[str]] = defaultdict(list)
        for relative in tracked_paths():
            key = unicodedata.normalize("NFC", relative).casefold()
            folded[key].append(relative)
        collisions = [items for items in folded.values() if len(items) > 1]
        self.assertEqual([], collisions)

    def test_shebang_python_entrypoints_are_executable(self) -> None:
        failures = []
        for relative in sorted(tracked_paths()):
            if not relative.endswith(".py"):
                continue
            path = ROOT / relative
            if not path.is_file() or not path.read_bytes().startswith(b"#!"):
                continue
            if not path.stat().st_mode & 0o111:
                failures.append(relative)
        self.assertEqual(
            [],
            failures,
            "Shebang entrypoints missing executable mode:\n"
            + "\n".join(failures),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
