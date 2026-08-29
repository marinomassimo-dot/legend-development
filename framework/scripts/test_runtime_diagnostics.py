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

    def test_every_branch_of_the_decision_is_driven(self):
        """🔴 Through `classify_state`, the real function — not a copy of it.

        The first version of this class asserted that two CONSTANTS were unequal, which
        is true however the branch is written, and a mutation reporting an off-path
        config as TRUST_BLOCKED survived the whole suite.
        """
        def config(layers=(), on_path=False, off_path=False, unreadable=False):
            return {"layers": list(layers), "on_path_names_hooks": on_path,
                    "off_path_names_hooks": off_path, "any_unreadable": unreadable}

        cases = [
            ("no config anywhere", chs.NOT_LOADED, [], config(), chs.CONFIG_ABSENT),
            ("a file that cannot be read", chs.NOT_LOADED, [],
             config(layers=[{}], unreadable=True), chs.CONFIG_INVALID),
            ("files, none naming hooks", chs.NOT_LOADED, [],
             config(layers=[{}]), chs.HOOKS_EMPTY),
            ("hooks named ON the path", chs.NOT_LOADED, [],
             config(layers=[{}], on_path=True), chs.TRUST_BLOCKED),
            ("hooks named only OFF the path", chs.NOT_LOADED, [],
             config(layers=[{}], off_path=True), chs.CONFIG_OFF_RESOLUTION_PATH),
            ("loaded, untrusted", chs.LOADED_UNTRUSTED, [{"trustStatus": "untrusted"}],
             config(), chs.HOOKS_LOADED_UNTRUSTED),
            ("loaded, trusted", chs.LOADED_TRUSTED, [{"trustStatus": "trusted"}],
             config(), chs.HOOKS_LOADED_TRUSTED),
            ("no answer", chs.UNDERIVABLE, [], config(), chs.UNDERIVABLE),
        ]
        for label, runtime, hooks, cfg, expected in cases:
            with self.subTest(case=label):
                self.assertEqual(chs.classify_state(runtime, hooks, cfg), expected)
        self.assertEqual(len({c[-1] for c in cases}), len(cases),
                         "two rows expecting one state would leave a branch undriven")

    def test_an_off_path_config_is_never_reported_as_a_withheld_trust_decision(self):
        """🔴 The distinction that costs a reader a wrong repair: TRUST_BLOCKED sends
        them to ask a human for a decision about a file nothing ever offered."""
        off_path = {"layers": [{}], "on_path_names_hooks": False,
                    "off_path_names_hooks": True, "any_unreadable": False}
        self.assertEqual(chs.classify_state(chs.NOT_LOADED, [], off_path),
                         chs.CONFIG_OFF_RESOLUTION_PATH)
        self.assertNotEqual(chs.classify_state(chs.NOT_LOADED, [], off_path),
                            chs.TRUST_BLOCKED)

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

    def test_the_verdict_is_driven_through_the_real_function(self):
        """🔴 `uniformity`, not a copy of it.

        The first version asserted `generation_of(<empty dir>) == ABSENT` — true, and
        silent about what the SURVEY does with an ABSENT row. A mutation folding
        unreadable worktrees into the YES/NO answer survived the whole suite.

        'Not uniform' is a measurement; 'one could not be read' is a failure to measure,
        and reporting the second as the first is the difference between "nine actors
        need a merge" and "one actor's tree is broken".
        """
        self.assertEqual(gr.uniformity({gr.REV9}), "YES")
        self.assertEqual(gr.uniformity({gr.REV9, gr.LEGACY}), "NO")
        self.assertEqual(gr.uniformity({gr.REV9, gr.ABSENT}), "UNDERIVABLE")
        self.assertEqual(gr.uniformity({gr.REV9, gr.UNKNOWN}), "UNDERIVABLE")
        self.assertEqual(gr.uniformity({gr.ABSENT}), "UNDERIVABLE")
        self.assertEqual(gr.uniformity(set()), "UNDERIVABLE")

    def test_an_unreadable_directory_classifies_as_absent(self):
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

    @staticmethod
    def _row(case_id, observed, mutating=True, control=False, expected=hc.DENY):
        return {"id": case_id, "observed": observed, "expected": expected,
                "mutating": mutating, "positive_control": control,
                "effect_class": "WRITE@ASSIGNED", "provenance": hc.PLAN_BRIEF,
                "agrees": observed == expected}

    def test_a_positive_control_is_never_counted_as_a_bypass(self):
        """🔴 Scored through `hc.score`, the real counter — not a copy of it.

        The first version of this test re-implemented the filter in its own body and
        asserted that the copy behaved like the copy. The mutation that puts positive
        controls back into the denominator survived the whole suite.

        The first counter reported eight bypasses for a revision that had one; seven
        were the positive floor. A corpus that counts its own controls as bypasses gets
        worse every time someone adds a control.
        """
        rows = [self._row("A1-workdir-in-in", hc.DENY),
                self._row("T1-scratch", hc.ALLOW, control=True, expected=hc.ALLOW),
                self._row("T2-commit", hc.ALLOW, control=True, expected=hc.ALLOW),
                self._row("X1-real-bypass", hc.ALLOW)]
        report = hc.score("rev9", rows)
        self.assertEqual(report["bypasses"], 1, "the two controls are not bypasses")
        self.assertEqual(report["mutating_shapes_that_must_be_refused"], 2)
        self.assertEqual(report["positive_controls"], 2)
        self.assertEqual(report["positive_controls_refused"], 0)

    def test_an_unrecognised_scene_scores_nothing_at_all(self):
        """🔴 Through `hc.score`. If the scene control is ALLOWED, every row is
        confounded and no ratio over any subset of them measures a family."""
        rows = [self._row("A1-workdir-in-in", hc.ALLOW),
                self._row("Z2-numbered-redirect", hc.ALLOW),
                self._row("T1-scratch", hc.ALLOW, control=True, expected=hc.ALLOW)]
        report = hc.score("rev8", rows)
        self.assertFalse(report["scene_recognised_as_a_repository"])
        self.assertEqual(len(report["confounded_by_scene_location"]), len(rows))
        self.assertEqual(report["mutating_shapes_that_must_be_refused"], 0)
        self.assertEqual(report["bypasses"], 0)

    def test_a_confounded_rows_recorded_expectation_is_not_scored(self):
        """🔴 `Z2` records rev8=DENY, measured where revision 8 recognises the
        repository. Marking it MISRECORDED here would push a later editor to 'correct'
        the table to say revision 8 never closed the numbered redirect. It did."""
        rows = [self._row("A1-workdir-in-in", hc.ALLOW),
                self._row("Z2-numbered-redirect", hc.ALLOW, expected=hc.DENY)]
        report = hc.score("rev8", rows)
        self.assertEqual(report["misrecorded"], [])
        z2 = next(r for r in report["rows"] if r["id"] == "Z2-numbered-redirect")
        self.assertEqual(z2["expected"], hc.NA)

    def test_a_recognised_scene_does_score_the_recorded_expectations(self):
        """The positive control for the two tests above: with the scene recognised, a
        genuinely wrong record IS reported."""
        rows = [self._row("A1-workdir-in-in", hc.DENY),
                self._row("Z2-numbered-redirect", hc.ALLOW, expected=hc.DENY)]
        report = hc.score("rev8", rows)
        self.assertTrue(report["scene_recognised_as_a_repository"])
        self.assertEqual(report["misrecorded"], ["Z2-numbered-redirect"])

    def test_the_k1_fixture_is_always_built_in_the_system_temp_dir(self):
        """🔴 TMPDIR is the whole content of case K1. Building its fixture beside a
        scene deliberately placed OUTSIDE scratch space would make the case measure an
        ordinary directory, which every revision handles — passing everywhere while the
        defect it names went unmeasured."""
        source = (HERE / "hostile_corpus.py").read_text()
        self.assertIn('self.fixture = Path(tempfile.mkdtemp(prefix="hostile-k1-"))',
                      source)

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
