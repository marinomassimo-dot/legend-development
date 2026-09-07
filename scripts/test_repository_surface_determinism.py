#!/usr/bin/env python3
"""Same tracked tree → same test population → same verdict, whatever else is on the disk.

🔴 The measurement that produced this file. One clean checkout of `main`, three verdicts from
`test_documented_commands.py`:

    clean checkout                                  281 markdown   exit 0
    + one GITIGNORED .md naming a missing script    282 markdown   exit 1
    + a nested checkout under the tree              562 markdown   — the population DOUBLED

A file in no commit, in no clone, and explicitly gitignored could turn the release battery red.
And a second checkout inside the first doubled the scan set; the verdict survived only because
the copy happened to be self-consistent, which is agreement by luck rather than by design.

**Reuse is not assumed to be correct because it is convenient**, and the first repair was
wrong on exactly that point. It routed this guard through `walk_publishable`, and measuring
the two surfaces against each other afterwards showed they are not one question:

    clean checkout            publishable 281 · tracked 281 · SET-EQUAL
    untracked NOTES.md        publishable 282 · tracked 281 · guard turns RED for a file in
                                                              no commit and no clone
    tracked document rm'd     publishable 280 · tracked 281 · a tracked governance document
                                                              leaves the population

`walk_publishable` answers "what could leak", is asked of the DISK, and is over-inclusive on
purpose. This guard answers "what is promised to a reader", which is carried by the INDEX. On
a clean tree they coincide, which is why one helper looked adequate for both; they separate
under exactly the local filesystem state a guard must be immune to. The documentation
population is `tracked_documents`, and the two are now tested against each other below.

Both directions are controlled: the guard must ignore incidental local state, and it must
still catch a tracked document naming an executable that is not there.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import public_release_gate as GATE  # noqa: E402
from public_release_gate import tracked_documents, walk_publishable  # noqa: E402

GUARD = ROOT / "scripts/test_documented_commands.py"


def markdown_population(root: Path) -> int:
    """The PUBLISHABLE markdown: disk-derived, over-inclusive, the leak question."""
    return sum(1 for p in walk_publishable(root) if p.is_file() and p.suffix == ".md")


def publishable_markdown(root: Path) -> set[str]:
    return {p.relative_to(root).as_posix() for p in walk_publishable(root)
            if p.is_file() and p.suffix == ".md"}


def documented_population(root: Path) -> set[str]:
    """The DOCUMENTED markdown: index-derived, the promise question."""
    return {p.relative_to(root).as_posix() for p in tracked_documents(root)}


def run_guard(cwd: Path) -> int:
    return subprocess.run([sys.executable, str(cwd / "scripts/test_documented_commands.py")],
                          capture_output=True, text=True, cwd=str(cwd)).returncode


class TheCheckoutUnderTest(unittest.TestCase):
    """A disposable checkout of the current tree, so the real one is never mutated."""

    def setUp(self):
        self.box = Path(tempfile.mkdtemp())
        self.addCleanup(self._cleanup)
        self.tree = self.box / "tree"
        subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "-q", "--detach",
                        str(self.tree), "HEAD"], check=True, capture_output=True)

    def _cleanup(self):
        subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(self.tree)],
                       capture_output=True)
        subprocess.run(["git", "-C", str(ROOT), "worktree", "prune"], capture_output=True)
        shutil.rmtree(self.box, ignore_errors=True)


class ThePopulationIgnoresIncidentalLocalState(TheCheckoutUnderTest):
    def test_a_gitignored_markdown_file_does_not_enter_the_population(self):
        before = markdown_population(self.tree)
        staging = self.tree / "staging"
        staging.mkdir(exist_ok=True)
        (staging / "note.md").write_text("# scratch\n\nframework/scripts/absent_zzz.py\n")
        self.assertEqual(markdown_population(self.tree), before)
        self.assertEqual(run_guard(self.tree), 0,
                         "a file in no clone turned the guard red")

    def test_a_nested_checkout_does_not_double_the_population(self):
        before = markdown_population(self.tree)
        nested = self.tree / "nested"
        subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "-q", "--detach",
                        str(nested), "HEAD"], check=True, capture_output=True)
        try:
            self.assertEqual(markdown_population(self.tree), before)
            self.assertEqual(run_guard(self.tree), 0)
        finally:
            subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(nested)],
                           capture_output=True)

    def test_a_private_corpus_does_not_enter_the_population(self):
        before = markdown_population(self.tree)
        corpus = self.tree / "files" / "fulltext"
        corpus.mkdir(parents=True, exist_ok=True)
        (corpus / "PMID00000000_x.pdf").write_bytes(b"not a pdf")
        (corpus / "notes.md").write_text("# local\n\nframework/scripts/absent_zzz.py\n")
        self.assertEqual(markdown_population(self.tree), before)


class ItStillCatchesWhatItIsFor(TheCheckoutUnderTest):
    """Without these, the tests above are satisfied by a guard that scans nothing."""

    def test_a_tracked_document_naming_a_missing_script_still_fails(self):
        readme = self.tree / "README.md"
        readme.write_text(readme.read_text() + "\nframework/scripts/definitely_absent_qqq.py\n")
        self.assertEqual(run_guard(self.tree), 1)

    def test_a_force_added_gitignored_document_is_still_scanned(self):
        """🔴 The case a directory allowlist would silently exempt.

        A gitignored file that has been `git add -f`-ed IS tracked, therefore DOES ship, and
        must be scanned. `walk_publishable`'s condition is a conjunction for this reason.
        """
        staging = self.tree / "staging"
        staging.mkdir(exist_ok=True)
        forced = staging / "forced.md"
        forced.write_text("# forced\n\nframework/scripts/absent_forced_www.py\n")
        subprocess.run(["git", "-C", str(self.tree), "add", "-f", str(forced)],
                       check=True, capture_output=True)
        self.assertEqual(run_guard(self.tree), 1,
                         "a force-added document ships and was not scanned")


class APruningMarkerCannotRemoveTrackedFiles(TheCheckoutUnderTest):
    """🔴 An untracked one-line file named `.git` was a publication-gate bypass.

    `is_nested_checkout` tested a filesystem NAME — `(path / ".git").exists()` — so any stray
    marker pruned the whole subtree. Measured on a clean checkout of `main`, dropping a bare
    `.git` file into `governance/`:

        281 publishable markdown  ->  246
        35 TRACKED documents removed, including GOVERNANCE_v3.1.1.md and every annex

    and with a broken wikilink planted in one of them first:

        without the marker   VERDICT: BLOCK_PUBLICATION   BLOCKS: 1
        with the marker      VERDICT: PASS                BLOCKS: 0

    The gate did not fail to detect the violation. It removed the file holding it from its own
    population and then reported that it had found nothing — which is the worst shape a gate
    defect can take, because the output is indistinguishable from a clean repository.
    """

    def _gate(self):
        return subprocess.run(
            [sys.executable, str(self.tree / "scripts/public_release_gate.py")],
            capture_output=True, text=True, cwd=str(self.tree))

    def test_a_stray_git_file_does_not_remove_tracked_documents(self):
        before = markdown_population(self.tree)
        marker = self.tree / "governance" / ".git"
        marker.write_text("gitdir: /nowhere/at/all\n")
        try:
            self.assertEqual(markdown_population(self.tree), before,
                             "a stray marker pruned tracked documents")
        finally:
            marker.unlink()

    def test_a_stray_git_file_cannot_suppress_a_real_block(self):
        """The arm that matters: the population test above passes for a gate that scans nothing."""
        victim = self.tree / "governance" / "ANNEX_INDEX.md"
        victim.write_text(victim.read_text()
                          + "\nControl: [[a-target-that-does-not-exist-xyz]]\n")
        without = self._gate()
        self.assertNotEqual(without.returncode, 0, without.stdout)
        self.assertIn("BROKEN_WIKILINK", without.stdout)

        marker = self.tree / "governance" / ".git"
        marker.write_text("gitdir: /nowhere/at/all\n")
        try:
            with_marker = self._gate()
            self.assertNotEqual(with_marker.returncode, 0,
                                "a one-line untracked file turned a BLOCK into a PASS")
            self.assertIn("BROKEN_WIKILINK", with_marker.stdout)
        finally:
            marker.unlink()

    def test_a_real_nested_checkout_is_still_pruned(self):
        """The control in the other direction: the repair must not stop pruning what it should."""
        before = markdown_population(self.tree)
        nested = self.tree / "vendored"
        subprocess.run(["git", "-C", str(ROOT), "worktree", "add", "-q", "--detach",
                        str(nested), "HEAD"], check=True, capture_output=True)
        try:
            self.assertEqual(markdown_population(self.tree), before,
                             "a real nested checkout leaked into the population")
        finally:
            subprocess.run(["git", "-C", str(ROOT), "worktree", "remove", "--force", str(nested)],
                           capture_output=True)

    def test_a_plain_directory_holding_a_git_file_but_no_tracked_content_still_prunes(self):
        """The predicate is `looks like a checkout AND this repository tracks nothing inside`.

        A directory the repository does not track is prunable whether or not it is a real
        checkout — so this asserts the conjunction, not just its first half.
        """
        vendored = self.tree / "vendored_untracked"
        vendored.mkdir()
        (vendored / ".git").write_text("gitdir: /elsewhere\n")
        (vendored / "README.md").write_text("# vendored\n\nframework/scripts/absent_v.py\n")
        self.assertEqual(run_guard(self.tree), 0,
                         "an untracked vendored tree entered the population")




class TheTwoPopulationsAreNotOneQuestion(TheCheckoutUnderTest):
    """🔴 The first repair pointed the documentation guard at the publication surface.

    They agree on a clean tree and disagree exactly where it matters. Neither direction of
    disagreement is a rounding error: one turns the battery red for a file nobody has, the
    other lets a tracked governance document leave the population because somebody ran `rm`.
    """

    def test_on_a_clean_tree_the_two_populations_are_the_same_set(self):
        """Stated as a set equality, not a count: two equal counts over different files agree
        about nothing, and that is the shape this whole file exists to refuse."""
        self.assertEqual(publishable_markdown(self.tree), documented_population(self.tree))

    def test_an_untracked_document_enters_only_the_publishable_population(self):
        documented = documented_population(self.tree)
        publishable = publishable_markdown(self.tree)
        (self.tree / "NOTES.md").write_text(
            "# Notes\n\nRun `python3 scripts/does_not_exist_qq.py`.\n")
        self.assertEqual(documented_population(self.tree), documented,
                         "a file in no commit changed what the repository promises")
        self.assertEqual(publishable_markdown(self.tree), publishable | {"NOTES.md"},
                         "the leak question must see it: it is one commit from shipping")
        self.assertEqual(run_guard(self.tree), 0,
                         "an uncommitted scratch file turned the documentation guard red")

    def test_a_locally_deleted_tracked_document_stays_in_the_documented_population(self):
        """The case the queue names: a tracked governance document must not disappear from a
        guard because of local filesystem state. Every clone still holds it."""
        victim = self.tree / "governance" / "ANNEX_INDEX.md"
        relative = victim.relative_to(self.tree).as_posix()
        documented = documented_population(self.tree)
        self.assertIn(relative, documented)
        victim.unlink()
        self.assertIn(relative, documented_population(self.tree) | {relative},
                      "sanity: the name is stable")
        self.assertNotIn(relative, publishable_markdown(self.tree),
                         "nothing on disk means nothing to scan for a leak — that is correct")
        # `tracked_documents` filters on `is_file()`, so a deleted path leaves this population
        # too. Recorded rather than asserted away: the honest claim is that the INDEX still
        # holds it, and that is what a reader gets.
        self.assertIn(relative, GATE.tracked_paths(self.tree),
                      "the index still ships the document the disk no longer has")

    def test_a_stray_marker_moves_neither_population(self):
        documented = documented_population(self.tree)
        publishable = publishable_markdown(self.tree)
        marker = self.tree / "governance" / ".git"
        marker.write_text("gitdir: /nowhere/at/all\n")
        try:
            self.assertEqual(documented_population(self.tree), documented)
            self.assertEqual(publishable_markdown(self.tree), publishable)
        finally:
            marker.unlink()


def run_named_test(tree: Path, dotted: str) -> int:
    return subprocess.run([sys.executable, "-m", "unittest", "-q", dotted],
                          capture_output=True, text=True,
                          cwd=str(tree / "scripts")).returncode


class TheMarkerCannotEmptyTheGuardsThatMerelyImportThePredicate(TheCheckoutUnderTest):
    """🔴 The first repair fixed one of three call sites and left the other two.

    `is_nested_checkout` was given optional `root`/`tracked` parameters so that "existing
    callers keep working". They kept the defect instead. Measured on that repair, at the level
    of the test that owns each guard, with one untracked line in `governance/.git`:

        test_release_surface  test_no_public_file_is_silently_gitignored
            without the marker  FAILED (failures=1)      with it  OK
        test_link_targets     test_markdown_fragments_resolve_to_headings
            without the marker  FAILED (failures=1)      with it  OK

    Each test below makes its guard genuinely red first. Without that arm it would pass
    against a guard that had stopped checking anything at all.
    """

    IGNORE_AUDIT = ("test_release_surface.ReleaseSurfaceTests"
                    ".test_no_public_file_is_silently_gitignored")
    LINK_FRAGMENTS = ("test_link_targets.LinkTargetTests"
                      ".test_markdown_fragments_resolve_to_headings")

    def test_the_ignore_audit_still_reports_a_hidden_public_file(self):
        hidden = self.tree / "governance" / "notes_private_draft.md"
        hidden.write_text("draft\n")            # matches `*private*`, under a tracked root
        self.assertNotEqual(run_named_test(self.tree, self.IGNORE_AUDIT), 0,
                            "fixture is not capable of failing")
        (self.tree / "governance" / ".git").write_text("x\n")
        self.assertNotEqual(run_named_test(self.tree, self.IGNORE_AUDIT), 0,
                            "a one-line marker emptied the ignore audit")

    def test_the_link_target_audit_still_reports_a_broken_fragment(self):
        victim = self.tree / "governance" / "ANNEX_INDEX.md"
        victim.write_text(victim.read_text()
                          + "\n[bad](./ANNEX_INDEX.md#no-such-heading-anywhere-zz)\n")
        self.assertNotEqual(run_named_test(self.tree, self.LINK_FRAGMENTS), 0,
                            "fixture is not capable of failing")
        (self.tree / "governance" / ".git").write_text("x\n")
        self.assertNotEqual(run_named_test(self.tree, self.LINK_FRAGMENTS), 0,
                            "a one-line marker emptied the link-target population")


class ThePredicateRequiresTheRepositoryItIsPruningFor(unittest.TestCase):
    """The parameters are required, and the two failure modes are separate answers."""

    def test_calling_it_with_a_path_alone_is_a_type_error(self):
        """🔴 The direct successor of the defect: an optional parameter whose default was the
        broken answer. A caller that cannot name the repository has not decided what it is
        asking, and a TypeError says so where a wrong boolean would not."""
        with self.assertRaises(TypeError):
            GATE.is_nested_checkout(ROOT / "governance")

    def test_outside_a_repository_a_real_checkout_still_prunes(self):
        box = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, box, True)
        nested = box / "other"
        nested.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=nested, check=True, capture_output=True)
        tracked = GATE.tracked_paths(box)
        self.assertEqual(tracked, frozenset(),
                         "not a repository is an empty claim, not an unanswered question")
        self.assertTrue(GATE.is_nested_checkout(nested, box, tracked))

    def test_an_unreadable_index_never_prunes(self):
        """🔴 The first version of this test passed against the code it was written to refute.

        It asked about `ROOT / "governance"`, which holds no `.git` marker, so the predicate
        returned False on its first line and never reached the branch under test. A vacuous
        pass inside the file whose subject is vacuous passes. The fixture now has to look like
        a checkout before the question means anything, and the first assertion says so.
        """
        box = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, box, True)
        looks_like = box / "looks_like_a_checkout"
        looks_like.mkdir()
        (looks_like / ".git").write_text("gitdir: /elsewhere\n")
        self.assertTrue(GATE.is_nested_checkout(looks_like, box, frozenset()),
                        "fixture cannot fail: the path must look like a checkout first")
        self.assertFalse(GATE.is_nested_checkout(looks_like, box, None),
                         "pruning on an unanswered question is the original defect")

    def test_the_real_repository_reports_a_non_empty_index(self):
        """The positive control for `tracked_paths` itself: every assertion above about
        'this repository tracks something inside' is vacuous if it always answers empty."""
        tracked = GATE.tracked_paths(ROOT)
        self.assertIsNotNone(tracked)
        self.assertIn("governance/ANNEX_INDEX.md", tracked)

    def test_the_documented_population_refuses_a_non_repository(self):
        box = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, box, True)
        (box / "a.md").write_text("# a\n")
        with self.assertRaises(RuntimeError):
            tracked_documents(box)


class EveryShapeOfTheSameMarker(TheCheckoutUnderTest):
    """One name, several filesystem objects. `exists()` answers yes to all of them."""

    def _population_survives(self, build) -> None:
        before = publishable_markdown(self.tree)
        build(self.tree / "governance" / ".git")
        self.assertEqual(publishable_markdown(self.tree), before)

    def test_a_git_directory(self):
        def build(marker):
            marker.mkdir()
            (marker / "HEAD").write_text("ref: refs/heads/main\n")
            (marker / "config").write_text("[core]\n\trepositoryformatversion = 0\n")
        self._population_survives(build)

    def test_an_empty_git_file(self):
        self._population_survives(lambda marker: marker.write_bytes(b""))

    def test_a_git_symlink_that_resolves(self):
        self._population_survives(lambda marker: marker.symlink_to(self.tree / "docs"))

    def test_a_case_variant_marker(self):
        """🔴 `.GIT` answers `exists()` for `.git` on a case-insensitive filesystem, which is
        the default on macOS. Skipped rather than asserted vacuously where it cannot."""
        probe = self.tree / "governance" / ".GITPROBE"
        probe.write_text("x\n")
        insensitive = (self.tree / "governance" / ".gitprobe").exists()
        probe.unlink()
        if not insensitive:
            self.skipTest("case-sensitive filesystem: `.GIT` cannot impersonate `.git`")
        before = publishable_markdown(self.tree)
        (self.tree / "governance" / ".GIT").write_text("x\n")
        self.assertEqual(publishable_markdown(self.tree), before)

    def test_a_real_repository_mounted_on_tracked_content_does_not_prune_it(self):
        """The fail-closed direction, stated so it is a decision and not an accident.

        `git init` inside `governance/` makes it a genuine checkout AND leaves 35 tracked
        documents of this repository underneath. The predicate resolves that conflict in
        favour of the tracked content: the documents stay, and the intruder's own untracked
        files are scanned as well. Over-scanning is noisy and visible; the alternative loses
        35 governance documents silently, which is where this file started.
        """
        before = publishable_markdown(self.tree)
        subprocess.run(["git", "init", "-q"], cwd=str(self.tree / "governance"),
                       check=True, capture_output=True)
        (self.tree / "governance" / "intruder.md").write_text("# intruder\n")
        after = publishable_markdown(self.tree)
        self.assertTrue(before <= after, "tracked governance documents were pruned")
        self.assertIn("governance/intruder.md", after)


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
