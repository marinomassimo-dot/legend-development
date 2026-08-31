#!/usr/bin/env python3
"""The effect model, and the revision-8 test floor's own index.

Two kinds of test live here. The first is the algebra: the vocabulary is closed, the
ladder is monotone, `UNKNOWN_EFFECT` is granted by nobody, and a comparison fails on an
extra effect and on a missing one.

The second is `TheTestFloorIsActuallyCovered`, which reads the eighteen numbered items
of the revision-8 brief and asserts that the test each one names EXISTS and RUNS. A
coverage table that is prose can claim anything; this one fails when it lies.
"""
from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import effect_model as em  # noqa: E402
import guard_policy as policy  # noqa: E402

ROOT = HERE.parent.parent


#: The rev8 brief's TEST FLOOR, item by item, each bound to the test that carries it.
#: 🔴 Bound to a test NAME, not to a description, so `TheTestFloorIsActuallyCovered` can
#: check the binding by import. Revision 7's claim of "31/31 mutation score" was a
#: statement about coverage that nothing checked was coverage of anything in particular.
TEST_FLOOR = {
    1: ("test_pre_tool_use_guard", "FailsClosed",
        "test_4_malformed_payload_denies_in_both_shapes"),
    2: ("test_effect_model", "UnknownEffectIsDeniedByEveryAuthority",
        "test_no_authority_in_the_table_grants_an_unknown_effect"),
    3: ("test_runtime_parity", "TheResidualDebtStaysDeclared",
        "test_every_closed_gap_stays_closed_on_both_sides"),
    4: ("test_runtime_parity", "TheResidualDebtStaysDeclared",
        "test_the_positive_floor_survives_in_both_runtimes"),
    5: ("test_effect_model", "AuthorisationIsPerKindAndPerScope",
        "test_an_effect_outside_the_grant_is_denied"),
    6: ("test_post_effect_verify", "TheObservedSetMustEqualTheAuthorisedSet",
        "test_an_extra_observed_effect_invalidates_the_write"),
    7: ("test_post_effect_verify", "TheObservedSetMustEqualTheAuthorisedSet",
        "test_a_missing_authorised_effect_invalidates_the_write"),
    8: ("test_execution_attestation", "AResumeMayNotInheritAuthority",
        "test_a_changed_actor_is_a_binding_mismatch"),
    9: ("test_execution_attestation", "AResumeMayNotInheritAuthority",
        "test_a_changed_worktree_is_a_binding_mismatch"),
    10: ("test_execution_attestation", "AResumeMayNotInheritAuthority",
         "test_a_changed_head_is_a_binding_mismatch"),
    11: ("test_execution_attestation", "AResumeMayNotInheritAuthority",
         "test_a_changed_task_fingerprint_is_a_binding_mismatch"),
    12: ("test_execution_attestation", "AResumeMayNotInheritAuthority",
         "test_a_changed_runtime_version_is_a_binding_mismatch"),
    13: ("test_execution_attestation", "AResumeMayNotInheritAuthority",
         "test_a_resumed_session_with_a_changed_binding_is_refused"),
    14: ("test_execution_attestation", "AResumeMayNotInheritAuthority",
         "test_a_resumed_session_with_an_identical_binding_revalidates"),
    15: ("test_effect_model", "DestructiveGitClassesNeedAnAuthorityNobodyGrants",
         "test_ref_mutation_and_network_write_are_above_the_shell_default"),
    16: ("test_effect_model", "AnUndeclaredExtractionIsDenied",
         "test_an_extraction_without_a_named_destination_is_denied"),
    17: ("test_effect_model", "AnInterpreterWriteWithoutADerivableTargetIsDenied",
         "test_a_program_body_whose_target_cannot_be_derived_is_denied"),
    18: ("test_runtime_parity", "TheBootstrapRefusesRatherThanReports",
         "test_undemonstrated_hook_forces_read_only"),
}


class TheVocabularyIsClosed(unittest.TestCase):

    def test_an_effect_outside_the_vocabulary_cannot_be_constructed(self) -> None:
        with self.assertRaises(ValueError):
            em.Effect("SORT_OF_A_WRITE", "x", em.INSIDE_REPO)
        with self.assertRaises(ValueError):
            em.Effect(em.WRITE, "x", "SOMEWHERE_ELSE")

    def test_unknown_effect_is_a_mutation_and_never_a_read(self) -> None:
        """The failure direction of not knowing is 'it might write', never 'it reads'."""
        self.assertIn(em.UNKNOWN_EFFECT, em.MUTATING)
        self.assertNotIn(em.READ, em.MUTATING)

    def test_a_malformed_effect_record_raises_rather_than_defaulting(self) -> None:
        for raw in ({}, {"kind": "WRITE"}, {"scope": "INSIDE_REPO"},
                    {"kind": "WRITE", "scope": "INSIDE_REPO", "target": 7}, "x", None):
            with self.subTest(raw=raw):
                with self.assertRaises(ValueError):
                    em.Effect.from_dict(raw)


class UnknownEffectIsDeniedByEveryAuthority(unittest.TestCase):
    """TEST FLOOR 2. The rule with no override."""

    def test_no_authority_in_the_table_grants_an_unknown_effect(self) -> None:
        # Over the TABLE, not over a list of authorities someone remembered to write a
        # case for. A seventh rung added later inherits this or fails here.
        for name, grant in em.AUTHORITIES.items():
            with self.subTest(authority=name):
                self.assertEqual(frozenset(), grant.grants.get(em.UNKNOWN_EFFECT,
                                                               frozenset()))
                effect = em.Effect(em.UNKNOWN_EFFECT, None, em.UNDERIVABLE)
                self.assertFalse(em.authorize([effect], name).authorized)

    def test_no_authority_reaches_an_unnamed_or_underivable_target(self) -> None:
        for name in em.AUTHORITIES:
            for scope in (em.UNNAMED, em.UNDERIVABLE):
                for kind in sorted(em.MUTATING - {em.UNKNOWN_EFFECT}):
                    with self.subTest(authority=name, scope=scope, kind=kind):
                        effect = em.Effect(kind, None, scope)
                        self.assertFalse(em.authorize([effect], name).authorized)

    def test_no_authority_grants_a_mutation_in_any_ungranted_scope(self) -> None:
        """🔴 Over `UNGRANTED`, which is `CONFINED` plus `RUNTIME_CONFIG` — revision 10.

        The confined scopes are absent from every grant by OMISSION, and an omission can
        be undone by someone writing `_L7 = {WRITE: {RUNTIME_CONFIG}}` with no error
        anywhere. Quantifying over the SET rather than over a list of expected denials is
        what makes a scope added later inherit the property — or fail here.
        """
        self.assertTrue(em.UNGRANTED, "an empty set makes this vacuously true")
        self.assertEqual(em.UNGRANTED, em.CONFINED | {em.RUNTIME_CONFIG})
        for name, grant in em.AUTHORITIES.items():
            for kind in sorted(em.MUTATING):
                for scope in sorted(em.UNGRANTED):
                    with self.subTest(authority=name, kind=kind, scope=scope):
                        self.assertFalse(grant.permits(kind, scope))

    def test_reading_is_granted_in_every_ungranted_scope(self) -> None:
        """🔴 The other direction. A read confinement on the runtime configuration would
        stop `codex_registration.py` diagnosing a registration at all, and a read
        confinement on a peer would break review — which is how a rule gets turned off."""
        for name, grant in em.AUTHORITIES.items():
            for scope in sorted(em.UNGRANTED):
                with self.subTest(authority=name, scope=scope):
                    self.assertTrue(grant.permits(em.READ, scope))

    def test_every_ungranted_scope_is_nameable(self) -> None:
        """What stops them is that no authority grants them, which is a different
        sentence from 'the guard could not see the path' and a different repair."""
        for scope in sorted(em.UNGRANTED):
            with self.subTest(scope=scope):
                self.assertIn(scope, em.SCOPES)
                self.assertIn(scope, em.NAMEABLE)

    def test_an_unresolvable_authority_is_no_authority(self) -> None:
        """Not a weaker grant — none. A typo must not become a permissive default."""
        decision = em.authorize([em.Effect(em.READ, "x", em.INSIDE_REPO)], "PUBLICH")
        self.assertFalse(decision.authorized)

    def test_the_unnameable_refusal_happens_BEFORE_the_grant_is_consulted(self) -> None:
        """🔴 M37 survived, and it survived because the rule is defence in depth.

        Removing the pre-check that refuses UNNAMED and UNDERIVABLE targets changes no
        verdict: those scopes appear in no authority's grant, so the per-kind check
        refuses them anyway. The mutant is EQUIVALENT for the answer and not for the
        REASON — and the reason is the part that survives a refactor. A future rung that
        listed `UNNAMED` in its scopes for some plausible-sounding purpose would be
        stopped by the pre-check and waved through by the grant alone.

        So the ORDER is asserted, not only the outcome.
        """
        for scope in (em.UNNAMED, em.UNDERIVABLE):
            with self.subTest(scope=scope):
                decision = em.authorize([em.Effect(em.WRITE, None, scope)], "PUBLISH")
                self.assertFalse(decision.authorized)
                _, why = decision.denials[0]
                self.assertIn("a mutation whose target is", why,
                              "the refusal must come from the pre-check, which names the "
                              "scope, and not from the grant, which names a rung")

    def test_an_unnamed_effect_carries_no_target_at_all(self) -> None:
        """🔴 M12: an UNNAMED target must not acquire a resolvable one.

        `guard_policy` maps the UNNAMED sentinel to `target=None`. A mutation that maps
        it to `"."` instead still denies — the scope is computed from the sentinel and
        stays UNNAMED — so the verdict is unchanged and the RECEIPT is not: an effect
        recorded against `.` covers every path in the repository under
        `post_effect_verify._under`, and would silently match any observed write.
        """
        derived, _, _ = policy.effects("git ls-files | xargs git add", str(ROOT), str(ROOT))
        unnameable = [e for e in derived if e.scope == em.UNNAMED]
        self.assertTrue(unnameable, "this command must derive an unnamed effect")
        for effect in unnameable:
            self.assertIsNone(effect.target,
                              "an unnamed effect must carry no target; a placeholder "
                              "target is a wildcard in every comparison downstream")

    def test_a_write_outside_the_floor_reaches_the_catch_all_and_is_refused(self) -> None:
        """🔴 M45: the last branch of `classify` was never exercised.

        Every denial in the suite was caught by an earlier, specific message branch, so
        the catch-all could be turned into an ALLOW and nothing noticed. It is reachable:
        a scratch write under `READ_ONLY` — the authority an UNATTESTED session holds, so
        the ordinary state of any session that has not attested — is denied by the grant
        and matches none of the specific branches.
        """
        outcome, reason, _ = policy.classify(
            "echo x > /tmp/probe.txt", str(ROOT), str(ROOT), authority=em.UNATTESTED)
        self.assertEqual(policy.PROHIBITED, outcome,
                         "an unattested session may not write, even to scratch")
        self.assertIn("READ_ONLY", reason,
                      "the catch-all must name the authority that refused it")


class TheAuthorityLadderIsMonotone(unittest.TestCase):

    def test_each_rung_grants_everything_the_rung_below_grants(self) -> None:
        for lower, higher in zip(em.LADDER, em.LADDER[1:]):
            with self.subTest(pair=f"{lower} < {higher}"):
                low, high = em.AUTHORITIES[lower], em.AUTHORITIES[higher]
                for kind, scopes in low.grants.items():
                    self.assertTrue(
                        scopes <= high.grants.get(kind, frozenset()),
                        f"{higher} does not grant {kind} everywhere {lower} does")

    def test_a_denial_names_the_rung_that_would_permit_it(self) -> None:
        """A refusal that only says no teaches the reader to route around it."""
        decision = em.authorize(
            [em.Effect(em.NETWORK_WRITE, "origin", em.NONLOCAL)], "SHELL_DEFAULT")
        self.assertFalse(decision.authorized)
        self.assertIn("PUBLISH", decision.reason())

    def test_the_unattested_floor_is_a_real_authority(self) -> None:
        self.assertIn(em.UNATTESTED, em.AUTHORITIES)
        self.assertEqual(frozenset(), em.AUTHORITIES[em.UNATTESTED].kinds - {em.READ})


class AuthorisationIsPerKindAndPerScope(unittest.TestCase):
    """TEST FLOOR 5, and the reason the grant is a mapping and not a product."""

    def test_an_effect_outside_the_grant_is_denied(self) -> None:
        inside_write = em.Effect(em.WRITE, "framework/x", em.INSIDE_REPO)
        self.assertFalse(em.authorize([inside_write], "SHELL_DEFAULT").authorized)
        self.assertTrue(em.authorize([inside_write], "WORKTREE_WRITE").authorized)

    def test_stage_inside_the_repo_and_write_inside_the_repo_are_different(self) -> None:
        """The whole reason `kinds x scopes` was the wrong shape.

        Both land at INSIDE_REPO. A product that admits the commit admits the write.
        """
        stage = em.Effect(em.STAGE, "framework/x", em.INSIDE_REPO)
        write = em.Effect(em.WRITE, "framework/x", em.INSIDE_REPO)
        self.assertTrue(em.authorize([stage], "SHELL_DEFAULT").authorized)
        self.assertFalse(em.authorize([write], "SHELL_DEFAULT").authorized)

    def test_one_denied_effect_denies_the_whole_command(self) -> None:
        effects = [em.Effect(em.READ, "a", em.INSIDE_REPO),
                   em.Effect(em.WRITE, "/tmp/b", em.SCRATCH),
                   em.Effect(em.WRITE, "framework/c", em.INSIDE_REPO)]
        self.assertFalse(em.authorize(effects, "SHELL_DEFAULT").authorized)

    def test_a_refused_command_is_authorised_for_nothing(self) -> None:
        """Not 'for the subset that passed'. `post_effect_verify` relies on this: an
        empty authorised set makes every effect a refused command produced EXTRA."""
        effects = [em.Effect(em.WRITE, "/tmp/b", em.SCRATCH),
                   em.Effect(em.WRITE, "framework/c", em.INSIDE_REPO)]
        self.assertEqual([], em.authorize(effects, "SHELL_DEFAULT").authorized_effects)


class DestructiveGitClassesNeedAnAuthorityNobodyGrants(unittest.TestCase):
    """TEST FLOOR 15."""

    def test_ref_mutation_and_network_write_are_above_the_shell_default(self) -> None:
        for kind, scope in ((em.REF_MUTATION, em.INSIDE_REPO),
                            (em.NETWORK_WRITE, em.NONLOCAL),
                            (em.PERMISSION_CHANGE, em.INSIDE_REPO)):
            with self.subTest(kind=kind):
                self.assertFalse(em.AUTHORITIES["SHELL_DEFAULT"].permits(kind, scope))

    def test_the_destructive_git_commands_are_all_refused_by_the_policy(self) -> None:
        for command in ("git reset --hard HEAD~1", "git clean -fd", "git checkout -- .",
                        "git branch -D lettore", "git update-ref refs/heads/main HEAD",
                        "git push development HEAD", "git rebase -i HEAD~3",
                        "chmod 777 AGENTS.md", "git stash push -u -m x"):
            with self.subTest(command=command):
                self.assertIsNotNone(policy.verdict(command, str(ROOT), str(ROOT)))

    def test_a_ref_creation_is_not_a_ref_mutation(self) -> None:
        """🔴 Creating a branch is the remedy for the harm this repository suffered.

        A guard that denies `git checkout -b` pushes actors back onto a shared branch.
        """
        for command in ("git checkout -b plan-something", "git switch -c plan-something",
                        "git branch plan-something", "git tag v1"):
            with self.subTest(command=command):
                self.assertIsNone(policy.verdict(command, str(ROOT), str(ROOT)))


class AnUndeclaredExtractionIsDenied(unittest.TestCase):
    """TEST FLOOR 16."""

    def test_an_extraction_without_a_named_destination_is_denied(self) -> None:
        for command in ("tar -xf /tmp/a.tar", "unzip /tmp/a.zip",
                        "tar --extract --file /tmp/a.tar"):
            with self.subTest(command=command):
                self.assertIsNotNone(policy.verdict(command, str(ROOT), str(ROOT)))

    def test_an_extraction_into_the_repository_is_denied_even_when_named(self) -> None:
        self.assertIsNotNone(
            policy.verdict("tar -xf /tmp/a.tar -C framework", str(ROOT), str(ROOT)))

    def test_an_extraction_into_scratch_is_allowed(self) -> None:
        """The other direction: a guard that blocks ordinary work gets turned off."""
        self.assertIsNone(
            policy.verdict("tar -xf /tmp/a.tar -C /tmp/out", str(ROOT), str(ROOT)))


class AnInterpreterWriteWithoutADerivableTargetIsDenied(unittest.TestCase):
    """TEST FLOOR 17."""

    def test_a_program_body_whose_target_cannot_be_derived_is_denied(self) -> None:
        for command in (
            'python3 -c "open(dest, \'w\').write(x)"',
            'python3 -c "import pathlib; pathlib.Path(p).write_text(v)"',
            'node -e "require(\'fs\').writeFileSync(target, body)"',
        ):
            with self.subTest(command=command):
                self.assertIsNotNone(policy.verdict(command, str(ROOT), str(ROOT)))

    def test_an_interpreter_write_to_a_literal_scratch_path_is_allowed(self) -> None:
        self.assertIsNone(policy.verdict(
            'python3 -c "open(\'/tmp/out.txt\', \'w\').write(\'x\')"',
            str(ROOT), str(ROOT)))


class ComparingObservedToAuthorised(unittest.TestCase):

    def test_an_exact_match_is_a_match(self) -> None:
        want = [em.Effect(em.WRITE, "a.txt", em.INSIDE_REPO)]
        have = [em.Effect(em.WRITE, "./a.txt", em.INSIDE_REPO)]
        self.assertTrue(em.compare(want, have).valid)

    def test_spelling_differences_are_not_mismatches(self) -> None:
        self.assertEqual(em.normalise_target("./framework//x"),
                         em.normalise_target("framework/x"))

    def test_a_url_is_not_normalised_as_a_path(self) -> None:
        self.assertEqual("https://example.com/a/../b",
                         em.normalise_target("https://example.com/a/../b"))


class TheTestFloorIsActuallyCovered(unittest.TestCase):
    """🔴 The table above must name tests that EXIST. Prose cannot be checked; this can.

    Every one of the eighteen numbered floor items in the revision-8 brief names a
    module, a class and a method. This imports each and asserts the method is there and
    is callable. A floor item whose test is renamed, deleted or never written fails
    here rather than being reported as covered.
    """

    def test_every_floor_item_names_a_test_that_exists(self) -> None:
        self.assertEqual(set(range(1, 19)), set(TEST_FLOOR),
                         "the floor has eighteen items and the table must carry all of them")
        missing = []
        for item, (module_name, class_name, method_name) in sorted(TEST_FLOOR.items()):
            try:
                module = importlib.import_module(module_name)
            except ImportError as exc:
                missing.append(f"{item}: cannot import {module_name} ({exc})")
                continue
            suite = getattr(module, class_name, None)
            if suite is None:
                missing.append(f"{item}: {module_name} has no class {class_name}")
                continue
            if not callable(getattr(suite, method_name, None)):
                missing.append(f"{item}: {class_name} has no test {method_name}")
        self.assertEqual([], missing, "the floor table claims coverage it does not have:\n"
                         + "\n".join(missing))


if __name__ == "__main__":
    unittest.main(verbosity=2)
