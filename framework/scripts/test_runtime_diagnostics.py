#!/usr/bin/env python3
"""The three read-only measurements revision 9 adds, and the traps in each.

`codex_hook_state.diagnose`  — do different causes get different names?
`guard_revision.survey`      — is the engine the same in every worktree?
`hostile_corpus`             — is the headline ratio reproducible from the tree?

🔴 None of these is a control. They are instruments, and an instrument that reports a
comfortable number is worse than no instrument, so what is asserted here is mostly the
uncomfortable direction: that a skipped case is not a pass, that an engine which failed
to run is not an engine that refused, and that "not uniform" and "could not be measured"
are different answers.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import codex_hook_state as chs  # noqa: E402
import guard_revision as gr  # noqa: E402
import hostile_corpus as hc  # noqa: E402

ROOT = HERE.parents[1]


def git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


class TheHookDiagnosticSeparatesItsCauses(unittest.TestCase):

    def test_the_state_vocabulary_is_closed_and_distinct(self):
        self.assertEqual(len(set(chs.DIAGNOSTIC_STATES)), len(chs.DIAGNOSTIC_STATES))

    def test_config_absent_and_trust_blocked_are_different_states(self):
        """🔴 The whole repair. Revision 8 returned NOT_LOADED for both, and they need
        opposite fixes: one wants a file placed, the other wants a human decision."""
        self.assertNotEqual(chs.CONFIG_ABSENT, chs.TRUST_BLOCKED)
        self.assertIn(chs.CONFIG_ABSENT, chs.DIAGNOSTIC_STATES)
        self.assertIn(chs.TRUST_BLOCKED, chs.DIAGNOSTIC_STATES)

    def test_a_config_off_the_resolution_path_is_its_own_state(self):
        """The measured cause here, and NOT a trust problem: nothing was ever offered
        for review, so no decision was ever withheld."""
        self.assertIn(chs.CONFIG_OFF_RESOLUTION_PATH, chs.DIAGNOSTIC_STATES)
        self.assertNotEqual(chs.CONFIG_OFF_RESOLUTION_PATH, chs.TRUST_BLOCKED)

    def test_firing_and_enforcing_are_never_derived_from_hooks_list(self):
        """🔴 `hooks/list` reports what is LOADED. Loaded is not trusted, trusted is not
        fired, and fired is not enforcing. Only a session probe reaches those."""
        report = chs.diagnose(str(ROOT))
        self.assertEqual(report["firing"], "NOT_TESTED")
        self.assertEqual(report["enforcing"], "NOT_TESTED")
        for state in chs.DIAGNOSTIC_STATES:
            self.assertNotIn(state, chs.NOT_DERIVABLE_WITHOUT_A_SESSION)

    def test_a_linked_worktree_is_recognised_as_one(self):
        """The config layer that is read depends on this, so it must be derived and
        not assumed."""
        report = chs.config_layer(str(ROOT))
        self.assertIn("linked_worktree", report)
        self.assertIsInstance(report["linked_worktree"], bool)

    def test_a_directory_outside_any_repository_still_answers(self):
        with tempfile.TemporaryDirectory() as raw:
            report = chs.diagnose(raw)
        self.assertIn(report["diagnostic_state"], chs.DIAGNOSTIC_STATES)

    def test_both_streams_are_carried_not_only_the_failing_one(self):
        report = chs.diagnose(str(ROOT))
        self.assertIn("stderr", report)
        self.assertIn("codex_version", report)


class GuardRevisionUniformityIsMeasuredAndNotAssumed(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.report = gr.survey(str(ROOT))

    def test_every_worktree_is_surveyed(self):
        listed = len(gr.worktrees(str(ROOT)))
        self.assertEqual(len(self.report["worktrees"]), listed)
        self.assertGreater(listed, 0)

    def test_the_verdict_is_one_of_three_values(self):
        self.assertIn(self.report["guard_revision_uniform"], ("YES", "NO", "UNDERIVABLE"))

    def test_an_unreadable_worktree_makes_the_answer_underivable_not_no(self):
        """🔴 'Not uniform' is a measurement; 'one could not be read' is a failure to
        measure, and reporting the second as the first makes an unreadable worktree
        look like a merely stale one."""
        with tempfile.TemporaryDirectory() as raw:
            empty = Path(raw) / "nothing"
            empty.mkdir()
            self.assertEqual(gr.generation_of(empty), gr.ABSENT)

    def test_the_generation_is_derived_from_the_import_not_the_file(self):
        """🔴 A stray untracked `repo_topology.py` beside a revision-8 policy must not
        report REV9: the generation has to describe what the code DOES."""
        base = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, base, ignore_errors=True)
        (base / "scripts").mkdir(parents=True)
        (base / "framework" / "scripts").mkdir(parents=True)
        (base / gr.GUARD_ENTRY).write_text("# shim\n")
        (base / gr.GUARD_POLICY).write_text("# a policy with no topology import\n")
        (base / gr.GUARD_TOPOLOGY).write_text("# present but unused\n")
        self.assertEqual(gr.generation_of(base), gr.REV8)
        (base / gr.GUARD_POLICY).write_text("import repo_topology as rt\n")
        self.assertEqual(gr.generation_of(base), gr.REV9)

    def test_a_legacy_worktree_is_named_legacy(self):
        base = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, base, ignore_errors=True)
        (base / "scripts").mkdir(parents=True)
        (base / gr.GUARD_ENTRY).write_text("# the single-file guard\n")
        self.assertEqual(gr.generation_of(base), gr.LEGACY)

    def test_this_worktree_carries_the_revision_under_test(self):
        mine = [row for row in self.report["worktrees"]
                if Path(str(row["worktree"])).resolve() == ROOT.resolve()]
        self.assertEqual(len(mine), 1)
        self.assertEqual(mine[0]["guard_generation"], gr.REV9)

    def test_the_survey_writes_nothing(self):
        """🔴 Upgrading a peer from here would be the cross-worktree write that
        `repo_topology` exists to forbid, performed by the tool that measures it."""
        source = (HERE / "guard_revision.py").read_text()
        for forbidden in ("write_text(", "write_bytes(", "open(", "mkdir(", "unlink("):
            self.assertNotIn(forbidden, source,
                             f"the survey must not call {forbidden}")


class TheHostileCorpusIsSelfDescribing(unittest.TestCase):

    def test_every_case_has_a_unique_id(self):
        ids = [case.id for case in hc.CASES]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_case_carries_semantics_not_only_a_verdict(self):
        """🔴 `expected: DENY` records what someone observed, not why it should be so.
        A case with no rationale cannot tell a reader whether a flipped verdict is a
        fix or a regression."""
        for case in hc.CASES:
            with self.subTest(case=case.id):
                self.assertTrue(case.effect_class)
                self.assertGreater(len(case.rationale), 40)
                self.assertIn(case.provenance,
                              (hc.PLAN_BRIEF, hc.MIRROR_FINDING, hc.REV9_NEW_CONTROL))
                self.assertIn(case.rev9, (hc.DENY, hc.ALLOW))

    def test_the_corpus_covers_every_demonstrated_mirror_finding(self):
        classes = {case.effect_class for case in hc.CASES}
        for required in ("WRITE@PEER_WORKTREE", "WRITE@SHARED_CHECKOUT",
                         "WRITE@GIT_COMMON_DIR", "REF_MUTATION@GIT_COMMON_DIR",
                         "DELETE@PEER_WORKTREE", "RENAME@PEER_WORKTREE", "DELEGATE",
                         "UNKNOWN_EFFECT"):
            with self.subTest(effect_class=required):
                self.assertIn(required, classes)

    def test_it_carries_a_positive_floor(self):
        controls = [case for case in hc.CASES if case.positive_control]
        self.assertGreaterEqual(len(controls), 10,
                                "a corpus with no positive floor scores a guard that "
                                "denies everything as perfect")

    def test_a_positive_control_is_never_counted_as_a_bypass(self):
        """🔴 The first counter reported eight bypasses for a revision that had one;
        seven were the positive floor. A corpus that counts its own controls as
        bypasses improves every time someone adds a control."""
        rows = [{"mutating": True, "positive_control": True, "observed": hc.ALLOW},
                {"mutating": True, "positive_control": False, "observed": hc.ALLOW}]
        counted = [r for r in rows
                   if r["mutating"] and not r["positive_control"]
                   and r["observed"] != hc.SKIP]
        self.assertEqual(len(counted), 1)

    def test_the_reconstruction_shas_are_real_commits(self):
        """A revision reconstructed from a SHA nobody can resolve is a quotation."""
        for revision, spec in hc.ENGINES.items():
            if spec["sha"] is None:
                continue
            with self.subTest(revision=revision):
                out = git(ROOT, "cat-file", "-t", str(spec["sha"]))
                self.assertEqual(out.stdout.strip(), "commit")

    def test_every_reconstructed_file_exists_at_its_sha(self):
        """🔴 The first draft named revision 7's engine as a single file that was
        already a shim at that SHA. Every case raised ImportError, and the runner
        scored an engine that never ran as one that refused everything."""
        for revision, spec in hc.ENGINES.items():
            if spec["sha"] is None:
                continue
            for relative in spec["files"]:
                with self.subTest(revision=revision, path=relative):
                    out = git(ROOT, "cat-file", "-t", f"{spec['sha']}:{relative}")
                    self.assertEqual(out.stdout.strip(), "blob")
            with self.subTest(revision=revision, entry=spec["entry"]):
                self.assertIn(spec["entry"], spec["files"])

    def test_the_committed_text_carries_no_machine_specific_path(self):
        """The corpus must be publishable: placeholders, resolved at run time."""
        source = (HERE / "hostile_corpus.py").read_text()
        for case in hc.CASES:
            with self.subTest(case=case.id):
                self.assertNotIn("/Users/", case.command)
                self.assertNotIn("/Users/", case.cwd or "")
                self.assertNotIn("/Users/", case.workdir or "")
        self.assertNotIn("/Users/", source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
