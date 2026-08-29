#!/usr/bin/env python3
"""The confinement unit: does a path land in the subdivision that actually owns it?

Every case here is built on a REAL multi-worktree fixture — `git worktree add`, not a
directory named to look like one — because the property under test is derived from git
and a fixture that only resembles the shape would test the resemblance.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import repo_topology as rt  # noqa: E402


def git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


class Fixture:
    """A shared checkout, two linked worktrees, one of them nested INSIDE the checkout.

    🔴 The nesting is the point. This repository puts its worktrees under
    `<REPO>/.claude/worktrees/`, so a peer path is under the shared checkout too, and a
    classifier that scans an unordered root list answers whichever it tried first.
    """

    def __init__(self):
        self.base = Path(tempfile.mkdtemp(prefix="topology-fixture-"))
        self.shared = self.base / "shared"
        self.shared.mkdir()
        git(self.shared, "init", "-q", "-b", "main")
        git(self.shared, "config", "user.email", "t@t")
        git(self.shared, "config", "user.name", "t")
        (self.shared / "CLAUDE.md").write_text("router\n")
        git(self.shared, "add", "CLAUDE.md")
        git(self.shared, "commit", "-qm", "base")

        # One peer OUTSIDE the checkout, one nested INSIDE it, as this repository has.
        self.outside_peer = self.base / "outside-peer"
        git(self.shared, "worktree", "add", "-q", "-b", "outside", str(self.outside_peer))
        self.nested = self.shared / ".claude" / "worktrees"
        self.nested.mkdir(parents=True)
        self.assigned = self.nested / "assigned"
        self.peer = self.nested / "peer"
        git(self.shared, "worktree", "add", "-q", "-b", "assigned", str(self.assigned))
        git(self.shared, "worktree", "add", "-q", "-b", "peer", str(self.peer))

    def close(self):
        shutil.rmtree(self.base, ignore_errors=True)


class TheTopologyIsDerivedFromTheSharedObjectStore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        rt.reset()
        cls.topology = rt.of(str(cls.fx.assigned))

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()
        rt.reset()

    def test_repository_identity_is_the_common_dir_not_the_toplevel(self):
        """🔴 Two worktrees have two toplevels and ONE repository.

        Keying identity on `--show-toplevel` says two actors worked in two different
        repositories, which is the fact that would have to be true for a cross-worktree
        write to be nobody's business.
        """
        other = rt.of(str(self.fx.peer))
        self.assertEqual(self.topology.repository_id, other.repository_id)
        self.assertNotEqual(self.topology.assigned_worktree, other.assigned_worktree)

    def test_the_shared_checkout_is_the_first_worktree_git_lists(self):
        self.assertEqual(Path(self.topology.shared_checkout).resolve(),
                         self.fx.shared.resolve())

    def test_every_other_worktree_is_a_peer(self):
        peers = {Path(p).resolve() for p in self.topology.peer_worktrees}
        self.assertIn(self.fx.peer.resolve(), peers)
        self.assertIn(self.fx.outside_peer.resolve(), peers)
        self.assertNotIn(self.fx.assigned.resolve(), peers)
        self.assertNotIn(self.fx.shared.resolve(), peers)


class LongestPrefixWins(unittest.TestCase):
    """The nesting trap, asserted directly rather than trusted to iteration order."""

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        rt.reset()
        cls.topology = rt.of(str(cls.fx.assigned))

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()
        rt.reset()

    def test_the_root_table_is_ordered_longest_first(self):
        """🔴 The ORDERING, asserted directly — the classification results do not pin it.

        Every nesting case below happens to answer correctly under declaration order
        too, because the table is built with the subdivisions before the shared
        checkout. So a mutation replacing the sort with `return table` survived: the
        property held by luck, and luck is not a property. What must be true is that no
        shorter root can win over a longer one, whatever order they were appended in.
        """
        roots = self.topology.roots()
        lengths = [len(root) for root, _ in roots]
        self.assertEqual(lengths, sorted(lengths, reverse=True))
        # And the pair that actually collides: the common dir sits INSIDE the shared
        # checkout, so its entry must precede it.
        order = [scope for _, scope in roots]
        self.assertLess(order.index(rt.GIT_COMMON_DIR), order.index(rt.SHARED_CHECKOUT))
        self.assertLess(order.index(rt.ASSIGNED_WORKTREE), order.index(rt.SHARED_CHECKOUT))

    def test_ordering_survives_a_reversed_table(self):
        """The same question asked so it cannot pass by construction order: build a
        topology whose shared checkout is listed first and longest-prefix must still
        put a nested peer in the peer."""
        shuffled = rt.Topology(
            repository_id=self.topology.git_common_dir,
            assigned_worktree=self.topology.assigned_worktree,
            shared_checkout=self.topology.shared_checkout,
            git_common_dir=self.topology.git_common_dir,
            peer_worktrees=list(reversed(self.topology.peer_worktrees)),
        )
        self.assertEqual(shuffled.classify(str(self.fx.peer / "x.md")), rt.PEER_WORKTREE)
        self.assertEqual(shuffled.classify(str(self.fx.assigned / "x.md")),
                         rt.ASSIGNED_WORKTREE)

    def test_a_nested_peer_is_a_peer_and_not_the_shared_checkout(self):
        self.assertEqual(self.topology.classify(str(self.fx.peer / "framework" / "x.md")),
                         rt.PEER_WORKTREE)

    def test_the_assigned_worktree_beats_the_checkout_containing_it(self):
        self.assertEqual(self.topology.classify(str(self.fx.assigned / "x.md")),
                         rt.ASSIGNED_WORKTREE)

    def test_the_common_dir_beats_the_checkout_containing_it(self):
        common = Path(self.topology.git_common_dir)
        for leaf in ("config", "hooks/pre-commit", "refs/heads/main",
                     "worktrees/peer/HEAD"):
            with self.subTest(leaf=leaf):
                self.assertEqual(self.topology.classify(str(common / leaf)),
                                 rt.GIT_COMMON_DIR)

    def test_the_shared_checkout_keeps_what_no_subdivision_claims(self):
        self.assertEqual(self.topology.classify(str(self.fx.shared / "CLAUDE.md")),
                         rt.SHARED_CHECKOUT)

    def test_a_peer_outside_the_checkout_is_still_a_peer(self):
        self.assertEqual(self.topology.classify(str(self.fx.outside_peer / "CLAUDE.md")),
                         rt.PEER_WORKTREE)


class SymlinksAreResolvedAndTheStricterAnswerWins(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        rt.reset()
        cls.topology = rt.of(str(cls.fx.assigned))

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()
        rt.reset()

    def test_a_link_from_the_assigned_worktree_into_a_peer_is_a_peer_write(self):
        """Lexically this path is inside the assigned worktree. It is not."""
        link = self.fx.assigned / "shortcut"
        os.symlink(str(self.fx.peer), str(link))
        self.assertEqual(self.topology.classify(str(link / "pwned.md")),
                         rt.PEER_WORKTREE)

    def test_a_link_into_the_common_dir_is_a_common_dir_write(self):
        link = self.fx.assigned / "gitlink"
        os.symlink(self.topology.git_common_dir, str(link))
        self.assertEqual(self.topology.classify(str(link / "config")),
                         rt.GIT_COMMON_DIR)

    def test_a_target_that_does_not_exist_yet_still_resolves_its_ancestors(self):
        """🔴 A write target usually does NOT exist — that is what makes it a write.

        A resolver that needed the leaf to exist would answer for `<peer>/existing` and
        not for `<peer>/newfile`, and the second is the one an attacker writes.
        """
        link = self.fx.assigned / "later"
        os.symlink(str(self.fx.peer), str(link))
        self.assertFalse((link / "not-created-yet.md").exists())
        self.assertEqual(self.topology.classify(str(link / "not-created-yet.md")),
                         rt.PEER_WORKTREE)


class ScratchAndOutsideAreStillDerivable(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        rt.reset()
        cls.topology = rt.of(str(cls.fx.assigned))

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()
        rt.reset()

    def test_scratch_prefixes_in_both_spellings(self):
        """macOS resolves `/tmp` to `/private/tmp`; both must read as scratch."""
        for path in ("/tmp/x", "/private/tmp/x", "/var/folders/zz/x",
                     "/private/var/folders/zz/x"):
            with self.subTest(path=path):
                self.assertEqual(self.topology.classify(path), rt.EXTERNAL_SCRATCH)

    def test_a_scratchpad_segment_anywhere_is_scratch(self):
        self.assertEqual(self.topology.classify("/opt/work/scratchpad/notes.txt"),
                         rt.EXTERNAL_SCRATCH)

    def test_somewhere_else_entirely_is_external_other(self):
        self.assertEqual(self.topology.classify("/opt/unrelated/file"),
                         rt.EXTERNAL_OTHER)

    def test_a_relative_path_is_underivable_and_never_silently_anchored(self):
        """🔴 Anchoring to this PROCESS's cwd would answer about the wrong directory."""
        self.assertEqual(self.topology.classify("framework/x.md"), rt.UNDERIVABLE)


class AFailedDerivationRefuses(unittest.TestCase):

    def test_outside_any_repository_the_topology_is_not_ok(self):
        with tempfile.TemporaryDirectory() as raw:
            rt.reset()
            topology = rt.of(raw)
        self.assertFalse(topology.ok)
        self.assertTrue(topology.detail)

    def test_a_failed_topology_answers_underivable_for_anything_not_scratch(self):
        """Not knowing where you are must fail towards refusal."""
        broken = rt.Topology(ok=False, detail="derivation failed")
        self.assertEqual(broken.classify("/opt/somewhere/file"), rt.UNDERIVABLE)

    def test_a_failed_topology_still_answers_scratch(self):
        """🔴 Scratch is a property of the PATH, not of the repository.

        Refusing `/tmp` whenever git was slow would deny ordinary work, and a guard
        that blocks ordinary work gets turned off.
        """
        broken = rt.Topology(ok=False, detail="derivation failed")
        self.assertEqual(broken.classify("/tmp/notes.txt"), rt.EXTERNAL_SCRATCH)


class TheStrictnessOrderIsTotal(unittest.TestCase):

    def test_every_scope_has_exactly_one_strictness(self):
        """A scope added later must not default to zero, which is the permissive end."""
        self.assertEqual(set(rt.SCOPES), set(rt.STRICTNESS))
        self.assertEqual(len(set(rt.STRICTNESS.values())), len(rt.SCOPES),
                         "two scopes sharing a rank makes the combination ambiguous")

    def test_the_confined_scopes_outrank_the_assigned_worktree(self):
        for scope in (rt.PEER_WORKTREE, rt.SHARED_CHECKOUT, rt.GIT_COMMON_DIR):
            with self.subTest(scope=scope):
                self.assertGreater(rt.STRICTNESS[scope],
                                   rt.STRICTNESS[rt.ASSIGNED_WORKTREE])

    def test_underivable_is_the_strictest(self):
        self.assertEqual(max(rt.STRICTNESS, key=rt.STRICTNESS.get), rt.UNDERIVABLE)


class TheAssignmentIsPinnedAndNotDerivedFromTheCwd(unittest.TestCase):
    """🔴 R1, at the topology layer. `of` answers *around this directory*; `of_assigned`
    answers *around this ACTOR* — and only the second may decide anything."""

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()

    def test_of_follows_the_directory_it_is_given(self):
        """The behaviour that made the bypass possible, kept measurable: standing in a
        peer makes `of` call the peer the assignment. That is a true answer to the
        question `of` asks, and the wrong question for a decision."""
        self.assertEqual(rt.of(str(self.fx.peer)).assigned_worktree,
                         os.path.realpath(str(self.fx.peer)))

    def test_of_assigned_pins_the_assignment_whatever_the_cwd(self):
        topology = rt.of_assigned(str(self.fx.assigned))
        self.assertEqual(topology.assigned_worktree,
                         os.path.realpath(str(self.fx.assigned)))
        self.assertEqual(topology.classify(str(self.fx.peer / "x.md")),
                         rt.PEER_WORKTREE)
        self.assertEqual(topology.classify(str(self.fx.assigned / "x.md")),
                         rt.ASSIGNED_WORKTREE)

    def test_the_two_disagree_about_exactly_the_thing_that_matters(self):
        """Standing in the peer, `of` says the peer is mine and `of_assigned` says it is
        a peer. That disagreement IS the repair, so it is asserted rather than implied."""
        from_cwd = rt.of(str(self.fx.peer))
        from_session = rt.of_assigned(str(self.fx.assigned))
        target = str(self.fx.peer / "x.md")
        self.assertEqual(from_cwd.classify(target), rt.ASSIGNED_WORKTREE)
        self.assertEqual(from_session.classify(target), rt.PEER_WORKTREE)

    def test_the_shared_checkout_is_the_assignment_for_the_actor_bound_to_it(self):
        topology = rt.of_assigned(str(self.fx.shared))
        self.assertEqual(topology.classify(str(self.fx.shared / "CLAUDE.md")),
                         rt.ASSIGNED_WORKTREE)
        self.assertEqual(topology.classify(str(self.fx.peer / "x.md")),
                         rt.PEER_WORKTREE)

    def test_an_assignment_that_is_not_a_working_tree_is_not_a_topology(self):
        for candidate in (None, "", "/", str(self.fx.base / "nowhere")):
            with self.subTest(candidate=candidate):
                self.assertFalse(rt.of_assigned(candidate).ok)

    def test_a_failed_assignment_classifies_nothing_as_the_actors_own(self):
        """🔴 The path is deliberately OUTSIDE scratch space. The fixture lives under
        `TMPDIR`, and a failed topology still answers `EXTERNAL_SCRATCH` there — the
        documented carve-out, because scratch is a property of the path. Asserting the
        UNDERIVABLE arm against a fixture path would have measured the carve-out and
        called it the fail-closed branch."""
        broken = rt.of_assigned("/")
        self.assertFalse(broken.ok)
        self.assertEqual(broken.classify("/opt/some-repository/x.md"), rt.UNDERIVABLE)
        self.assertEqual(broken.classify("/tmp/x.md"), rt.EXTERNAL_SCRATCH,
                         "scratch survives a failed derivation; nothing else does")

    def test_the_two_caches_do_not_answer_each_others_question(self):
        """🔴 One cache keyed on a path would return whichever question was asked first,
        and the two questions have different answers for the same path."""
        rt.reset()
        self.assertEqual(rt.cached(str(self.fx.peer)).assigned_worktree,
                         os.path.realpath(str(self.fx.peer)))
        self.assertEqual(rt.cached_for(str(self.fx.peer)).assigned_worktree,
                         os.path.realpath(str(self.fx.peer)))
        self.assertEqual(rt.cached_for(str(self.fx.assigned)).assigned_worktree,
                         os.path.realpath(str(self.fx.assigned)))
        rt.reset()
        self.assertEqual(rt._CACHE, {})
        self.assertEqual(rt._ASSIGNED_CACHE, {})


if __name__ == "__main__":
    unittest.main(verbosity=2)
