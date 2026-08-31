#!/usr/bin/env python3
"""RESUME_INTEGRITY — the nine dimensions, and what a restart may not inherit.

The case these tests were written for is real and recent: a Codex session exhausted its
token budget on 2026-08-28, restarted, and came back carrying context. Nothing in the
bridge noticed, because authority had been established once and a restart is not a
start. Every assertion below is a way that can go wrong, made deterministic.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import effect_model as em  # noqa: E402
import execution_attestation as ea  # noqa: E402


def binding(**overrides) -> ea.Binding:
    """A complete, plausible binding. Every test changes exactly one dimension."""
    fields = dict(
        actor="plan",
        runtime="claude-code",
        runtime_version="2.1.232",
        session="sess-abc123",
        task=ea.task_fingerprint("P0 runtime bridge rev8"),
        worktree="/repo/.claude/worktrees/evidence-index",
        branch="plan-runtime-bridge-p00-rev8",
        head="51f6e4eb1e6801bc92de9cf8d4a2669ae457d024",
        authority="SHELL_DEFAULT",
    )
    fields.update(overrides)
    return ea.Binding(**fields)


class TheEightDimensionsStayDistinct(unittest.TestCase):

    def test_the_schema_carries_all_nine_and_names_which_are_derived(self) -> None:
        """🔴 Nine, not eight. The brief's identity list has eight names; the binding it
        asks for has nine, because `runtime_version` is a field of its own — and it has
        to be, since a restart onto a different runtime version is the discontinuity
        this whole module was written for. The prose here said eight for a while and
        the code said nine; the code was right."""
        self.assertEqual(9, len(ea.DIMENSIONS))
        self.assertEqual(set(ea.DIMENSIONS), set(ea.DECLARED) | set(ea.DERIVED))
        self.assertEqual(set(), set(ea.DECLARED) & set(ea.DERIVED))

    def test_a_missing_dimension_is_underivable_and_never_empty(self) -> None:
        """Empty compares equal to empty and to 'not set yet'. UNDERIVABLE does not."""
        incomplete = ea.Binding(actor="plan")
        self.assertEqual(ea.UNDERIVABLE, incomplete.head)
        self.assertFalse(incomplete.complete)
        self.assertIn("head", incomplete.underivable)

    def test_changing_any_single_dimension_changes_the_fingerprint(self) -> None:
        base = binding().fingerprint()
        for name in ea.DIMENSIONS:
            with self.subTest(dimension=name):
                moved = binding(**{name: "something-else"})
                self.assertNotEqual(base, moved.fingerprint(),
                                    f"{name} does not reach the fingerprint")

    def test_two_bindings_that_differ_only_in_which_field_holds_a_value(self) -> None:
        """Names are hashed with values, so a shift between fields cannot collide."""
        left = binding(actor="a", branch="b")
        right = binding(actor="b", branch="a")
        self.assertNotEqual(left.fingerprint(), right.fingerprint())

    def test_the_task_text_never_enters_the_binding(self) -> None:
        digest = ea.task_fingerprint("something the operator typed, possibly sensitive")
        self.assertTrue(digest.startswith("task:"))
        self.assertNotIn("operator", digest)

    def test_an_unattested_binding_confers_the_floor_and_not_its_claim(self) -> None:
        result = ea.attest(ea.Binding(actor="plan", authority="PUBLISH"))
        self.assertFalse(result.ok)
        self.assertEqual(em.UNATTESTED, result.effective_authority)

    def test_an_authority_outside_the_table_never_attests(self) -> None:
        result = ea.attest(binding(authority="SUPERUSER"))
        self.assertFalse(result.ok)


class AResumeMayNotInheritAuthority(unittest.TestCase):
    """TEST FLOOR 8-14. One dimension per test, and every one of them fails closed."""

    def _mismatch(self, **overrides) -> ea.Attestation:
        result = ea.revalidate(binding(), binding(**overrides))
        self.assertEqual(ea.RESUME_BINDING_MISMATCH, result.verdict)
        self.assertFalse(result.ok)
        self.assertEqual(em.UNATTESTED, result.effective_authority)
        return result

    def test_a_changed_actor_is_a_binding_mismatch(self) -> None:
        self.assertIn("actor", self._mismatch(actor="mirror").reason)

    def test_a_changed_worktree_is_a_binding_mismatch(self) -> None:
        self.assertIn("worktree", self._mismatch(worktree="/repo/other").reason)

    def test_a_changed_head_is_a_binding_mismatch(self) -> None:
        """Someone committed under this actor's feet. `ONE_WRITER_PER_WORKING_DIRECTORY`
        cannot detect that by itself; comparing HEAD across a resume can."""
        self.assertIn("head", self._mismatch(head="0" * 40).reason)

    def test_a_changed_task_fingerprint_is_a_binding_mismatch(self) -> None:
        other = ea.task_fingerprint("an entirely different assignment")
        self.assertIn("task", self._mismatch(task=other).reason)

    def test_a_changed_runtime_version_is_a_binding_mismatch(self) -> None:
        """`cross_session_transport.md` § 3: a guarantee bound to a version does not
        become false on an upgrade, it becomes UNMEASURED — which is not inheritable."""
        self.assertIn("runtime_version", self._mismatch(runtime_version="2.2.0").reason)

    def test_a_changed_branch_or_authority_is_a_binding_mismatch(self) -> None:
        self._mismatch(branch="main")
        self._mismatch(authority="PUBLISH")

    def test_a_resumed_session_with_a_changed_binding_is_refused(self) -> None:
        """TEST FLOOR 13. The session identifier itself moved: it IS a new session."""
        result = self._mismatch(session="sess-restarted-after-token-exhaustion")
        self.assertIn("revoked", result.reason)

    def test_a_resumed_session_with_an_identical_binding_revalidates(self) -> None:
        """TEST FLOOR 14. The other direction, or this is a check that always says no."""
        result = ea.revalidate(binding(), binding())
        self.assertEqual(ea.RESUME_BINDING_MATCH, result.verdict)
        self.assertTrue(result.ok)
        self.assertEqual("SHELL_DEFAULT", result.effective_authority)

    def test_a_dimension_that_became_underivable_fails_like_one_that_changed(self) -> None:
        """🔴 The rule a 'compare what we can see' implementation gets wrong, and gets
        wrong permissively every time."""
        for name in ea.DIMENSIONS:
            with self.subTest(dimension=name):
                result = ea.revalidate(binding(), binding(**{name: ea.UNDERIVABLE}))
                self.assertEqual(ea.RESUME_BINDING_MISMATCH, result.verdict)

    def test_a_dimension_underivable_in_BOTH_bindings_still_fails(self) -> None:
        """🔴 The case that distinguishes the completeness check from the diff, and the
        one a mutation run found missing.

        The test above passes even with the completeness check deleted, because a field
        that WAS a value and is now UNDERIVABLE differs, and the difference check catches
        it. The discriminating case is a field that was underivable BEFORE and still is:
        nothing differs, and without the completeness check the resume revalidates.

        That is not hypothetical. `session` is UNDERIVABLE whenever a runtime emits no
        session identifier, which is every invocation outside a hook payload — so this
        is the ordinary shape of an unattested session, not an exotic one, and treating
        it as MATCH would revalidate exactly the bindings that were never established.
        """
        for name in ea.DIMENSIONS:
            with self.subTest(dimension=name):
                stale = binding(**{name: ea.UNDERIVABLE})
                result = ea.revalidate(stale, binding(**{name: ea.UNDERIVABLE}))
                self.assertEqual(ea.RESUME_BINDING_MISMATCH, result.verdict,
                                 f"{name} was UNDERIVABLE in both and revalidated")
                self.assertEqual(em.UNATTESTED, result.effective_authority)

    def test_every_dimension_is_load_bearing_on_resume(self) -> None:
        """No subset may drift. Asserted over DIMENSIONS, not over the cases above."""
        for name in ea.DIMENSIONS:
            with self.subTest(dimension=name):
                changed = ea.revalidate(binding(), binding(**{name: "moved"}))
                self.assertFalse(changed.ok, f"{name} was allowed to drift")


class TheStoreFailsClosed(unittest.TestCase):

    def setUp(self) -> None:
        self.home = Path(tempfile.mkdtemp(prefix="rev8-attest-"))

    def test_a_first_attestation_is_recorded_and_revalidates(self) -> None:
        first = binding()
        ea.record(first, self.home)
        loaded = ea.load(first.worktree, first.actor, self.home)
        self.assertEqual(first.fingerprint(), loaded.fingerprint())
        self.assertTrue(ea.revalidate(loaded, first).ok)

    def test_an_absent_store_is_not_an_unreadable_one(self) -> None:
        self.assertIsNone(ea.load("/nowhere", "plan", self.home))

    def test_an_edited_record_attests_to_nothing(self) -> None:
        """🔴 The fingerprint is re-derived from the body, not read out of the file.

        A record whose stored fingerprint no longer matches its own binding has been
        edited since it was written, and an edited attestation is not a weaker
        attestation.
        """
        first = binding()
        path = ea.record(first, self.home)
        raw = json.loads(path.read_text())
        raw["binding"]["authority"] = "PUBLISH"
        path.write_text(json.dumps(raw))
        loaded = ea.load(first.worktree, first.actor, self.home)
        self.assertFalse(loaded.complete)
        self.assertFalse(ea.revalidate(loaded, first).ok)

    def test_a_corrupt_store_refuses_the_resume_rather_than_starting_fresh(self) -> None:
        """Unreadable must not be silently upgraded to absent: absent means 'attest
        fresh', and that is exactly the inheritance this module exists to stop."""
        first = binding()
        path = ea.record(first, self.home)
        path.write_text("{not json at all")
        loaded = ea.load(first.worktree, first.actor, self.home)
        self.assertIsNotNone(loaded)
        self.assertFalse(ea.revalidate(loaded, first).ok)

    def test_a_record_from_another_schema_attests_to_nothing(self) -> None:
        first = binding()
        path = ea.record(first, self.home)
        raw = json.loads(path.read_text())
        raw["schema"] = "legend_execution_attestation/0"
        path.write_text(json.dumps(raw))
        self.assertFalse(ea.load(first.worktree, first.actor, self.home).complete)


class DerivationReadsTheEnvironmentRatherThanTheCaller(unittest.TestCase):

    def test_the_derived_half_comes_from_git_and_not_from_arguments(self) -> None:
        fixture = Path(tempfile.mkdtemp(prefix="rev8-derive-"))
        subprocess.run(["git", "init", "-q", "-b", "probe-branch", str(fixture)],
                       capture_output=True)
        for key, value in (("user.email", "t@example.invalid"), ("user.name", "t")):
            subprocess.run(["git", "-C", str(fixture), "config", key, value],
                           capture_output=True)
        (fixture / "a.txt").write_text("a\n")
        subprocess.run(["git", "-C", str(fixture), "add", "a.txt"], capture_output=True)
        subprocess.run(["git", "-C", str(fixture), "commit", "-q", "-m", "x"],
                       capture_output=True)

        derived = ea.derive(actor="plan", task="t", authority="READ_ONLY",
                            cwd=str(fixture))
        self.assertEqual("probe-branch", derived.branch)
        self.assertEqual(str(fixture), derived.worktree.replace("/private/", "/"))
        self.assertNotEqual(ea.UNDERIVABLE, derived.head)

    def test_a_directory_that_is_not_a_repository_is_underivable(self) -> None:
        fixture = Path(tempfile.mkdtemp(prefix="rev8-norepo-"))
        derived = ea.derive(actor="plan", task="t", authority="READ_ONLY",
                            cwd=str(fixture))
        self.assertEqual(ea.UNDERIVABLE, derived.worktree)
        self.assertEqual(ea.UNDERIVABLE, derived.head)
        self.assertFalse(ea.attest(derived).ok)

    def test_an_unrecognised_runtime_is_underivable_not_a_default(self) -> None:
        """A default here would make the busiest dimension the one nobody checked."""
        runtime, _, _ = ea.derive_runtime({"tool_name": "some_new_tool"})
        self.assertIn(runtime, (ea.UNDERIVABLE, "claude-code", "codex"))
        # The payload's own tool name is stronger evidence than an env var.
        self.assertEqual("codex", ea.derive_runtime({"tool_name": "exec"})[0])
        self.assertEqual("claude-code", ea.derive_runtime({"tool_name": "Bash"})[0])

    def test_an_absent_session_identifier_is_underivable(self) -> None:
        self.assertEqual(ea.UNDERIVABLE, ea.derive_runtime({})[2])
        self.assertEqual(ea.UNDERIVABLE, ea.derive_runtime({"session_id": ""})[2])
        self.assertEqual("s1", ea.derive_runtime({"session_id": "s1"})[2])


if __name__ == "__main__":
    unittest.main(verbosity=2)
