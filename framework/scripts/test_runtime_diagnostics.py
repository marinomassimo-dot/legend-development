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
import codex_registration as cr  # noqa: E402
import guard_policy as gp  # noqa: E402
import guard_revision as gr  # noqa: E402
import hostile_corpus as hc  # noqa: E402
import pre_tool_use_guard as adapter  # noqa: E402

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
        # 🔴 R12. Every DECLARED state must be produced by a fixture above. Revision 9
        # declared `CONFIG_DISCOVERED` with the same comment as `TRUST_BLOCKED` and
        # `classify_state` could not emit it — dead operational vocabulary, which a
        # reader can find in the table, look for in a report, and never see.
        self.assertEqual(set(chs.DIAGNOSTIC_STATES), {c[-1] for c in cases},
                         "every declared diagnostic state is reachable by a concrete "
                         "fixture, and no state is emitted that is not declared")

    def test_the_removed_state_stays_removed(self):
        """🔴 Named, so a reintroduction is a failure rather than a silent regrowth.

        `CONFIG_DISCOVERED` was a second name for `TRUST_BLOCKED` — the two carried
        word-for-word the same comment. Removal was preferred to inventing a transition
        that would make it reachable, because a vocabulary grown to satisfy a coverage
        test is a vocabulary that no longer draws distinctions.
        """
        self.assertNotIn("CONFIG_DISCOVERED", chs.DIAGNOSTIC_STATES)
        self.assertFalse(hasattr(chs, "CONFIG_DISCOVERED"))

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

    def test_a_runtime_that_did_not_answer_is_never_a_trust_diagnosis(self):
        """🔴 R5. Revision 9 reduced a JSON-RPC ERROR to an empty hook list.

        `answer.get("result", {}).get("data", [])` turned `{"error": {...}}` into `[]`,
        which `state_for` reported as `NOT_LOADED`, which `classify_state` crossed with
        the filesystem and named `CONFIG_ABSENT` or `TRUST_BLOCKED` — sending the
        operator to place a file, or to make a trust decision, on the strength of a
        query that FAILED. A non-dict `result` did worse and raised `AttributeError` out
        of a diagnostic.

        Every non-answer is `UNDERIVABLE`, and the two well-formed answers still work,
        which is what keeps this from being "always say UNDERIVABLE".
        """
        original = chs.hooks_list
        self.addCleanup(setattr, chs, "hooks_list", original)

        def replies(answer):
            chs.hooks_list = lambda cwd, env=None, timeout=25.0: (answer, "")
            return chs.state_for(str(ROOT))[0]

        for label, answer in (
            ("a JSON-RPC error", {"jsonrpc": "2.0", "id": 2,
                                  "error": {"code": -32601, "message": "no method"}}),
            ("neither result nor error", {"jsonrpc": "2.0", "id": 2}),
            ("a result that is not an object", {"jsonrpc": "2.0", "id": 2,
                                                "result": "nope"}),
            ("a data member that is not a list", {"jsonrpc": "2.0", "id": 2,
                                                  "result": {"data": {}}}),
            ("an entry carrying no hooks list", {"jsonrpc": "2.0", "id": 2,
                                                 "result": {"data": [{}]}}),
            ("a reply that is not an object", "plain string"),
            ("no reply at all", None),
        ):
            with self.subTest(reply=label):
                self.assertEqual(replies(answer), chs.UNDERIVABLE)

        # 🔴 The other half. A guard that answered UNDERIVABLE to everything would pass
        # every case above and diagnose nothing.
        self.assertEqual(replies({"jsonrpc": "2.0", "id": 2, "result": {"data": []}}),
                         chs.NOT_LOADED)
        self.assertEqual(
            replies({"jsonrpc": "2.0", "id": 2,
                     "result": {"data": [{"hooks": [{"trustStatus": "trusted"}]}]}}),
            chs.LOADED_TRUSTED)
        self.assertEqual(
            replies({"jsonrpc": "2.0", "id": 2,
                     "result": {"data": [{"hooks": [{"trustStatus": "untrusted"}]}]}}),
            chs.LOADED_UNTRUSTED)

    def test_a_non_answer_and_an_empty_answer_are_different_values(self):
        """`None` and `[]` must not be one value: the first is a failure to measure and
        the second is a measurement. Asserted at the boundary that returns them."""
        original = chs.hooks_list
        self.addCleanup(setattr, chs, "hooks_list", original)
        chs.hooks_list = lambda cwd, env=None, timeout=25.0: (
            {"jsonrpc": "2.0", "id": 2, "error": {"code": -1}}, "")
        self.assertIsNone(chs.hooks_for(str(ROOT))[0])
        chs.hooks_list = lambda cwd, env=None, timeout=25.0: (
            {"jsonrpc": "2.0", "id": 2, "result": {"data": []}}, "")
        self.assertEqual(chs.hooks_for(str(ROOT))[0], [])

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
        self.assertEqual(mine[0]["guard_generation"], gr.REV10)

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
                self.assertIn(case.rev10, (hc.DENY, hc.ALLOW))

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
        for revision in hc.ENGINES:
            with self.subTest(revision=revision):
                self.assertIsNotNone(hc.resolve_sha(ROOT, revision),
                                     "the pin does not resolve to a commit")

    def test_no_engine_is_measured_from_the_working_tree(self):
        """🔴 R6. Revision 9 recorded `sha: None` for its own engine and read the DISK.

        The candidate's headline number was therefore a function of disk state: an
        uncommitted edit, a half-applied mutation or a file left executable by a suite
        all moved it, and nobody re-running the corpus from the repository could get the
        same answer.

            CORPUS RESULT = FUNCTION(COMMITTED OBJECTS)     not     FUNCTION(DISK)

        Asserted over the table AND over the code, because a `None` reintroduced in
        `ENGINES` and a working-tree branch reintroduced in `materialise` are two
        different ways back to the same defect.
        """
        for revision, spec in hc.ENGINES.items():
            with self.subTest(revision=revision):
                self.assertIsNotNone(spec["sha"])
                self.assertTrue(str(spec["sha"]).strip())
        source = (HERE / "hostile_corpus.py").read_text()
        self.assertNotIn('spec["sha"] is None', source,
                         "a working-tree branch in materialise is the defect itself")

    def test_a_report_names_the_object_every_number_describes(self):
        """`HEAD` is a pin, and printing `HEAD` beside a ratio names nothing. The runner
        resolves it to a 40-character sha and reports THAT."""
        sha = hc.resolve_sha(ROOT, "rev10")
        self.assertRegex(sha, r"^[0-9a-f]{40}$")
        self.assertEqual(sha, hc.resolve_sha(ROOT, "rev10", {"rev10": "HEAD"}))

    def test_an_override_pins_a_revision_to_a_named_object(self):
        """The candidate's own two-step: commit the content, then re-run against that
        content commit by name rather than against whatever HEAD has become."""
        parent = git(ROOT, "rev-parse", "HEAD~1").stdout.strip()
        self.assertEqual(hc.resolve_sha(ROOT, "rev10", {"rev10": parent}), parent)

    def test_an_unresolvable_pin_is_a_failure_and_not_a_fallback(self):
        self.assertIsNone(hc.resolve_sha(ROOT, "rev10", {"rev10": "no-such-ref-anywhere"}))

    def test_every_reconstructed_file_exists_at_its_sha(self):
        """🔴 The first draft named revision 7's engine as a single file that was
        already a shim at that SHA. Every case raised ImportError, and the runner
        scored an engine that never ran as one that refused everything."""
        for revision, spec in hc.ENGINES.items():
            sha = hc.resolve_sha(ROOT, revision)
            for relative in spec["files"]:
                with self.subTest(revision=revision, path=relative):
                    out = git(ROOT, "cat-file", "-t", f"{sha}:{relative}")
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
                self.assertNotIn("/Users/", case.assigned or "")
                self.assertNotIn("/Users/", case.program or "")
        self.assertNotIn("/Users/", source)

    def test_the_frame_rotation_family_is_present_and_expects_a_change(self):
        """🔴 R1's family, asserted as a FAMILY rather than as thirteen strings.

        Mirror's thirteen bypasses are not the requirement; the architecture closing
        their families is. What this checks is that the corpus records a revision-9 →
        revision-10 verdict CHANGE for the rotation family — a table that carried the
        cases with both columns saying DENY would be recording a repair nobody made.
        """
        rotation = [case for case in hc.CASES if case.id.startswith("F")]
        self.assertGreaterEqual(len(rotation), 13)
        tightened = [c for c in rotation if c.rev9 == hc.ALLOW and c.rev10 == hc.DENY]
        self.assertGreaterEqual(len(tightened), 6,
                                "the six measured rotation spellings must each record "
                                "the verdict they moved")
        self.assertTrue(any(c.positive_control for c in rotation),
                        "a family with no control cannot show the repair is not a ban")

    def test_no_case_loosened_from_revision_9_without_being_a_control(self):
        """🔴 The direction that would hide a regression.

        A case moving DENY → ALLOW is either a false refusal being repaired — which is a
        POSITIVE CONTROL and says so — or a bypass being opened. There is no third
        reading, and leaving the two indistinguishable is how a loosening ships as a fix.
        """
        for case in hc.CASES:
            if case.rev9 == hc.DENY and case.rev10 == hc.ALLOW:
                with self.subTest(case=case.id):
                    self.assertTrue(
                        case.positive_control,
                        f"{case.id} loosened and is not declared a positive control")


class TheLiveProbeCanTellTheEnginesApart(unittest.TestCase):
    """🔴 R2. The revision-9 probe could return FIRING while measuring the legacy guard.

    Its named discriminator — `"Blanket staging is blocked in this repository."` — is
    BYTE-IDENTICAL in the legacy single-file guard on `main`, and all four of its
    proposed commands return the same high-level verdict under both engines. So the
    protocol's conclusion did not follow from its observation.
    """

    def setUp(self):
        self.legacy = cr.legacy_blob(str(ROOT), "main")
        if not self.legacy:
            self.skipTest("the legacy blob is not reachable from this checkout")

    def test_the_revision_9_discriminator_is_present_in_the_legacy_engine(self):
        """The premise, measured rather than quoted. If this ever goes red, the old
        protocol became sound and this class needs re-reading, not deleting."""
        self.assertIn("Blanket staging is blocked in this repository.", self.legacy)

    def test_no_revision_10_discriminator_appears_in_the_legacy_engine(self):
        for token in cr.discriminators():
            with self.subTest(token=token):
                self.assertNotIn(token, self.legacy)

    def test_the_discriminators_are_read_out_of_the_modules_that_emit_them(self):
        """A discriminator transcribed into this module could drift from what the guard
        says, and the drift would be invisible: the probe would look for a token nothing
        emits and conclude NOT_FIRING."""
        self.assertIn(f"GENERATION={adapter.GUARD_GENERATION}", cr.discriminators()[0])
        self.assertEqual(adapter.GUARD_GENERATION, "REV10")

    def test_every_decision_code_is_absent_from_the_legacy_engine(self):
        for code in gp.DECISION_CODES:
            with self.subTest(code=code):
                self.assertNotIn(f"DECISION_CODE={code}", self.legacy)

    def test_the_probe_refuses_to_start_with_any_precondition_unmet(self):
        met = {name: True for name, _ in cr.PRECONDITIONS}
        self.assertTrue(cr.preconditions_met(met)[0])
        for name, _ in cr.PRECONDITIONS:
            with self.subTest(missing=name):
                partial = dict(met)
                partial[name] = False
                self.assertFalse(cr.preconditions_met(partial)[0])
                self.assertIn(name, cr.preconditions_met(partial)[1])

    def test_a_precondition_nobody_answered_is_not_met(self):
        """🔴 `observations.get(name)` alone would let a caller that FORGOT a
        precondition pass it — the same defect as a diagnostic reading a failed query as
        an empty answer, in the module that exists to stop that."""
        self.assertFalse(cr.preconditions_met({})[0])
        self.assertEqual(len(cr.preconditions_met({})[1]), len(cr.PRECONDITIONS))

    def test_the_probe_verdict_distinguishes_four_outcomes_and_not_two(self):
        """The whole of R2 as a truth table, driven through the real function."""
        base = {"FORBIDDEN_WRITE_DENIED": True, "AUTHORIZED_WRITE_ALLOWED": True,
                "REV10_GENERATION_CONFIRMED": True, "REV10_UNIQUE_DENIAL_OBSERVED": True,
                "OBSERVED_EFFECT_MATCHES_AUTHORIZED": True}
        self.assertEqual(cr.classify_probe(base), cr.REV10_ENFORCING)
        self.assertEqual(cr.classify_probe({**base, "FORBIDDEN_WRITE_DENIED": False}),
                         cr.NOT_FIRING)
        self.assertEqual(
            cr.classify_probe({**base, "REV10_UNIQUE_DENIAL_OBSERVED": False}),
            cr.LEGACY_FIRING,
            "a refusal carrying a sentence both engines contain identifies no engine")
        self.assertEqual(
            cr.classify_probe({**base, "REV10_GENERATION_CONFIRMED": False}),
            cr.LEGACY_FIRING)
        self.assertEqual(cr.classify_probe({**base, "AUTHORIZED_WRITE_ALLOWED": False}),
                         cr.REV10_FIRING)
        self.assertEqual(
            cr.classify_probe({**base, "OBSERVED_EFFECT_MATCHES_AUTHORIZED": False}),
            cr.REV10_FIRING)
        for missing in base:
            with self.subTest(missing=missing):
                partial = {k: v for k, v in base.items() if k != missing}
                self.assertEqual(cr.classify_probe(partial), cr.UNDERIVABLE)

    def test_the_four_verdicts_are_all_reachable(self):
        """No dead vocabulary here either: every declared verdict has a fixture."""
        self.assertEqual(set(cr.PROBE_VERDICTS) - {cr.UNDERIVABLE},
                         {cr.NOT_FIRING, cr.LEGACY_FIRING, cr.REV10_FIRING,
                          cr.REV10_ENFORCING})


class TheRegistrationResolvesToTheEngineItNames(unittest.TestCase):
    """🔴 R3. Revision 9 registered a RELATIVE path in a config the runtime never reads."""

    def test_a_relative_registration_is_unanchored(self):
        self.assertEqual(cr.classify_anchoring("framework/scripts/pre_tool_use_guard.py"),
                         cr.UNANCHORED)

    def test_an_absolute_registration_is_anchored(self):
        self.assertEqual(cr.classify_anchoring("/opt/legend/guard.py"), cr.ABSOLUTE)

    def test_a_runtime_variable_registration_is_anchored(self):
        self.assertEqual(cr.classify_anchoring("$CLAUDE_PROJECT_DIR/scripts/g.py"),
                         cr.RUNTIME_ANCHORED)
        self.assertEqual(cr.classify_anchoring("${CLAUDE_PROJECT_DIR}/scripts/g.py"),
                         cr.RUNTIME_ANCHORED)

    def test_an_unknown_variable_is_not_an_anchor(self):
        """🔴 Only variables a RUNTIME sets count. `$MY_THING` is set by whoever set it,
        and treating it as an anchor would make the check a formatting rule."""
        self.assertEqual(cr.classify_anchoring("$MY_THING/scripts/g.py"), cr.UNANCHORED)

    def test_the_engine_is_the_operand_and_not_the_interpreter(self):
        self.assertEqual(cr.engine_of("python3 /opt/g.py"), "/opt/g.py")
        self.assertEqual(cr.engine_of('python3 "$CLAUDE_PROJECT_DIR/scripts/g.py"'),
                         "$CLAUDE_PROJECT_DIR/scripts/g.py")

    def test_the_claude_registration_in_this_repository_resolves_and_is_rev10(self):
        """The Claude side already meets the bar R3 asks the Codex side to reach, and
        this is what makes that a measurement rather than an assertion about it."""
        found = cr.read_registration(str(ROOT / ".claude" / "settings.json"),
                                     {"CLAUDE_PROJECT_DIR": str(ROOT)})
        self.assertEqual(found.anchoring, cr.RUNTIME_ANCHORED)
        self.assertTrue(found.deterministic)
        self.assertEqual(found.guard_generation, gr.REV10)
        self.assertRegex(found.engine_hash, r"^[0-9a-f]{64}$")

    def test_the_codex_registration_here_is_reported_unanchored_rather_than_ignored(self):
        """🔴 The finding, kept measurable. This file is NOT deployable and the module
        says so; a check that quietly passed it would be the defect one level up."""
        found = cr.read_registration(str(ROOT / ".codex" / "config.toml"))
        self.assertEqual(found.anchoring, cr.UNANCHORED)
        self.assertFalse(found.deterministic)
        self.assertEqual(found.resolved_path, "")

    def test_an_inline_table_registration_is_read_at_all(self):
        """🔴 The first draft anchored its pattern to the start of a line, and this
        repository registers its Codex hooks in INLINE tables — so it reported 'nothing
        registered' about a file with five registrations in it."""
        found = cr.read_registration(str(ROOT / ".codex" / "config.toml"))
        self.assertTrue(found.registered_path,
                        "an inline `{ command = ... }` table must still be read")

    def test_the_renderer_refuses_to_emit_an_unanchored_registration(self):
        with self.assertRaises(ValueError):
            cr.render_registration("framework/scripts/pre_tool_use_guard.py")

    def test_the_rendered_registration_covers_every_codex_tool_the_guard_polices(self):
        rendered = cr.render_registration("/opt/legend/pre_tool_use_guard.py")
        for tool in cr._codex_tool_names():
            with self.subTest(tool=tool):
                self.assertIn(f'matcher = "{tool}"', rendered)

    def test_the_route_table_is_complete_and_selects_nothing(self):
        self.assertEqual(set(cr.ROUTES), {"A", "B", "C", "D"})
        for key, route in cr.ROUTES.items():
            for prop in cr.PROPERTIES:
                with self.subTest(route=key, property=prop):
                    self.assertIsInstance(route[prop], bool)
        self.assertIsNone(cr.ROUTE_SELECTED,
                          "choosing among placements is the operator's call")

    def test_no_route_is_shell_mutable_once_revision_10_is_installed(self):
        """🔴 The column revision 10 moved. B and C were writable at ordinary
        SHELL_DEFAULT under revision 9 and Mirror measured all three shapes."""
        for key, route in cr.ROUTES.items():
            with self.subTest(route=key):
                self.assertFalse(route["SHELL_MUTABLE"])
                self.assertTrue(route["shell_mutable_because"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
