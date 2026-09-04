#!/usr/bin/env python3
"""The push permission, stated as the set of pushes it REFUSES.

A permission is only as good as its negative space, and this one replaced a blanket
refusal — so every test that matters here is a refusal that must survive. The four the
operator named explicitly are `--force`, `origin`, `main` after a merge that was not the
agents' to make, and a red gate; each has its own case below, and so does every other
condition the rule states.

🔴 **The last three cases go through `guard_policy.verdict`, not through this module.**
Proving `evaluate` refuses a push proves nothing about what the guard does with a command:
the guard could stop consulting it and every unit test here would stay green. The
integration cases build a real repository, bind the session to it, and assert on the
guard's own answer — which is the only surface a runtime actually meets.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import push_authorization as pa                              # noqa: E402

GOOD_SHA = "a" * 40
OTHER_SHA = "b" * 40


def record(branch="work", sha=GOOD_SHA, verdict="PASS", blocks=0,
           actor="orchestrator", **extra):
    entry = {"branch": branch, "sha": sha, "gate_verdict": verdict,
             "gate_blocks": blocks, "actor": actor}
    entry.update(extra)
    return entry


def judge(rest, records=None, resolve=None):
    return pa.evaluate(rest,
                       records=[] if records is None else records,
                       resolve=resolve or (lambda ref: GOOD_SHA))


class ARefusalKeepsItsShape(unittest.TestCase):
    """Every condition the rule states, exercised as the push that violates it."""

    def test_force_is_refused_in_every_spelling(self) -> None:
        for flag in ("--force", "-f", "--force-with-lease", "--force-if-includes"):
            with self.subTest(flag=flag):
                got = judge(["development", flag, "work"], [record()])
                self.assertFalse(got.allowed)
                self.assertIn(flag, got.reason)

    def test_a_plus_refspec_is_a_non_fast_forward(self) -> None:
        got = judge(["development", "+work"], [record()])
        self.assertFalse(got.allowed)
        self.assertIn("non-fast-forward", got.reason)

    def test_flags_that_push_more_than_the_named_ref_are_refused(self) -> None:
        for flag in ("--all", "--tags", "--follow-tags", "--mirror", "--prune"):
            with self.subTest(flag=flag):
                self.assertFalse(judge(["development", flag, "work"], [record()]).allowed)

    def test_deletion_is_refused(self) -> None:
        for flag in ("--delete", "-d"):
            with self.subTest(flag=flag):
                self.assertFalse(judge(["development", flag, "work"], [record()]).allowed)

    def test_origin_is_refused_even_with_a_perfect_record(self) -> None:
        """The record authorises a push; it does not authorise a repository."""
        got = judge(["origin", "work"], [record()])
        self.assertFalse(got.allowed)
        self.assertIn("origin", got.reason)

    def test_any_other_remote_is_refused(self) -> None:
        for remote in ("upstream", "https://github.com/someone/else.git", "local"):
            with self.subTest(remote=remote):
                self.assertFalse(judge([remote, "work"], [record()]).allowed)

    def test_a_bare_push_is_refused_because_its_destination_is_a_default(self) -> None:
        got = judge([], [record()])
        self.assertFalse(got.allowed)
        self.assertIn("origin", got.reason)

    def test_a_remote_without_a_ref_is_refused(self) -> None:
        self.assertFalse(judge(["development"], [record()]).allowed)

    def test_more_than_one_ref_is_refused(self) -> None:
        self.assertFalse(judge(["development", "work", "other"], [record()]).allowed)

    def test_a_renaming_refspec_is_refused(self) -> None:
        got = judge(["development", "work:refs/heads/other"], [record()])
        self.assertFalse(got.allowed)
        self.assertIn("renames", got.reason)

    def test_a_same_name_refspec_is_accepted(self) -> None:
        self.assertTrue(judge(["development", "work:refs/heads/work"], [record()]).allowed)

    def test_an_unresolvable_branch_is_refused(self) -> None:
        got = judge(["development", "ghost"], [record()], resolve=lambda ref: None)
        self.assertFalse(got.allowed)
        self.assertIn("does not resolve", got.reason)


class VariantsOfThePermittedFormAreStillRefused(unittest.TestCase):
    """The quadrant that can hurt anyone: what a permitted-looking push lets through.

    Every case here was ALLOWED by the first implementation with a valid ledger entry, and
    each was found by pointing the existing harness at a variant of the one spelling the
    original battery tested. They are grouped so that a future widening of the rule has to
    walk past them.
    """

    def test_a_bundled_short_flag_carries_its_letter(self) -> None:
        """`-f` was refused and `-fu` was not: the same forced update, one letter longer."""
        for token in ("-fu", "-uf", "-qf", "-fd"):
            with self.subTest(token=token):
                got = judge(["development", token, "work"], [record()])
                self.assertFalse(got.allowed, f"{token} was allowed")
                self.assertIn("bundles", got.reason)

    def test_a_short_flag_without_a_refused_letter_still_passes(self) -> None:
        """The repair must not refuse by shape. `-u` sets upstream and loses nothing."""
        self.assertTrue(judge(["development", "-u", "work"], [record()]).allowed)

    def test_force_with_lease_carrying_a_value_is_refused(self) -> None:
        got = judge(["development", "--force-with-lease=refs/heads/work", "work"], [record()])
        self.assertFalse(got.allowed)

    def test_a_tag_refspec_is_not_a_branch(self) -> None:
        """`refs/tags/work` was reduced to `work` and gated as the branch of that name."""
        got = judge(["development", "refs/tags/work"], [record()])
        self.assertFalse(got.allowed)
        self.assertIn("renames", got.reason)

    def test_a_remote_tracking_source_cannot_become_the_branch(self) -> None:
        """This published an object the gate never saw, under the authorised branch name."""
        got = judge(["development", "refs/remotes/x/work:refs/heads/work"], [record()])
        self.assertFalse(got.allowed)

    def test_head_is_not_a_branch_name(self) -> None:
        self.assertFalse(judge(["development", "HEAD:refs/heads/work"], [record()]).allowed)

    def test_an_empty_source_is_a_deletion(self) -> None:
        self.assertFalse(judge(["development", ":refs/heads/work"], [record()]).allowed)

    def test_an_opaque_operand_is_refused_and_does_not_crash(self) -> None:
        """`$(echo work)` reaches here as a sentinel carrying NUL. It used to kill the hook,
        and a dead hook is silence, and silence on this channel is ALLOW."""
        got = judge(["development", "\x00OPAQUE\x00"], [record()])
        self.assertFalse(got.allowed)

    def test_a_qualified_branch_ref_is_still_allowed(self) -> None:
        self.assertTrue(judge(["development", "refs/heads/work"], [record()]).allowed)

    def test_a_branch_name_containing_a_slash_is_still_allowed(self) -> None:
        got = pa.evaluate(["development", "feature/work"],
                          records=[record(branch="feature/work")],
                          resolve=lambda ref: GOOD_SHA)
        self.assertTrue(got.allowed)

    def test_a_repository_redirecting_global_is_refused(self) -> None:
        """SHA and ledger read in one repository, objects sent from another."""
        got = pa.evaluate(["development", "work"], records=[record()],
                          resolve=lambda ref: GOOD_SHA, redirected=["-C"])
        self.assertFalse(got.allowed)
        self.assertIn("moves the repository", got.reason)

    def test_a_boolean_block_count_is_not_zero_blocks(self) -> None:
        for blocks in (False, 0.0):
            with self.subTest(blocks=blocks):
                self.assertFalse(judge(["development", "work"],
                                       [record(blocks=blocks)]).allowed)


class TheGateResultIsReadNotAssumed(unittest.TestCase):
    def test_no_record_at_all_is_refused_and_names_the_repair(self) -> None:
        got = judge(["development", "work"], [])
        self.assertFalse(got.allowed)
        self.assertIn("push_authorization.py record", got.reason)

    def test_a_record_for_a_different_sha_does_not_authorise_this_one(self) -> None:
        """The whole point of keying on the SHA: yesterday's PASS is not today's tree."""
        got = judge(["development", "work"], [record(sha=OTHER_SHA)])
        self.assertFalse(got.allowed)
        self.assertIn("no authorisation", got.reason)

    def test_a_red_gate_is_not_published(self) -> None:
        got = judge(["development", "work"], [record(verdict="FAIL")])
        self.assertFalse(got.allowed)
        self.assertIn("not a clean PASS", got.reason)

    def test_a_pass_carrying_blocks_is_not_a_clean_pass(self) -> None:
        self.assertFalse(judge(["development", "work"], [record(blocks=3)]).allowed)

    def test_an_unattributed_authorisation_is_refused(self) -> None:
        for actor in ("", "   ", None):
            with self.subTest(actor=actor):
                got = judge(["development", "work"], [record(actor=actor)])
                self.assertFalse(got.allowed)
                self.assertIn("no actor", got.reason)

    def test_a_clean_record_authorises_an_ordinary_branch(self) -> None:
        self.assertTrue(judge(["development", "work"], [record()]).allowed)

    def test_a_stale_record_beside_a_good_one_does_not_spoil_it(self) -> None:
        got = judge(["development", "work"],
                    [record(sha=OTHER_SHA, verdict="FAIL"), record()])
        self.assertTrue(got.allowed)


class MainIsPublishedOnlyWhenTheMergeWasOurs(unittest.TestCase):
    def resolve_main(self, ref):
        return GOOD_SHA

    def test_main_without_the_assertion_is_the_operators(self) -> None:
        got = pa.evaluate(["development", "main"],
                          records=[record(branch="main")], resolve=self.resolve_main)
        self.assertFalse(got.allowed)
        self.assertIn("operator", got.reason)

    def test_main_with_the_assertion_false_is_the_operators(self) -> None:
        got = pa.evaluate(["development", "main"],
                          records=[record(branch="main",
                                          merge_changed_no_guarantee=False)],
                          resolve=self.resolve_main)
        self.assertFalse(got.allowed)

    def test_main_with_the_assertion_is_allowed(self) -> None:
        got = pa.evaluate(["development", "main"],
                          records=[record(branch="main",
                                          merge_changed_no_guarantee=True)],
                          resolve=self.resolve_main)
        self.assertTrue(got.allowed)

    def test_the_assertion_does_not_rescue_a_red_gate_on_main(self) -> None:
        got = pa.evaluate(["development", "main"],
                          records=[record(branch="main", verdict="FAIL",
                                          merge_changed_no_guarantee=True)],
                          resolve=self.resolve_main)
        self.assertFalse(got.allowed)


class TheLedgerIsReadDefensively(unittest.TestCase):
    def test_a_missing_ledger_reads_as_no_authorisations(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual([], pa.read_ledger(tmp))

    def test_a_malformed_line_is_skipped_and_the_good_one_survives(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / pa.LEDGER_RELATIVE
            path.parent.mkdir(parents=True)
            path.write_text("{not json\n\n" + json.dumps(record()) + "\n", encoding="utf-8")
            got = pa.read_ledger(tmp)
            self.assertEqual(1, len(got))
            self.assertEqual("work", got[0]["branch"])


# --------------------------------------------------------------- through the real guard


def build_repository(root: Path, branch: str) -> str:
    """A real repository with one commit on `branch`, and the SHA it resolves to."""
    def git(*args):
        subprocess.run(["git", "-C", str(root), *args], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    git("init", "-q")
    git("config", "user.email", "t@example.invalid")
    git("config", "user.name", "test")
    (root / "seed.txt").write_text("seed\n", encoding="utf-8")
    git("add", "seed.txt")
    git("commit", "-qm", "seed")
    git("branch", "-M", branch)
    done = subprocess.run(["git", "-C", str(root), "rev-parse", f"refs/heads/{branch}"],
                          stdout=subprocess.PIPE, text=True, check=True)
    return done.stdout.strip()


class KnownHolesThisSpecificationStillHas(unittest.TestCase):
    """Executable record of what `evaluate` still gets WRONG. Every case asserts a DEFECT.

    🔴 A to-do list, not a guarantee. The previous version of this battery recorded these
    holes as English inside a docstring, so 49 tests stayed green over a module that admits
    `--del` and `--exec-path=` — a certificate where a specification was wanted. Written
    this way, closing a hole turns its case RED, which forces whoever closes it to come here
    and invert the assertion deliberately instead of inheriting a passing score.

    The common cause is one defect, not several: the module decides by matching tokens
    against hand-written lists, and git has more spellings than the lists have entries.

    Only ONE further hole is genuinely outside this layer: `git commit … && git push` is a
    second statement, and no parameter here can see it. The other two named in an earlier
    version of this docstring — environment prefixes and the payload's `workdir` — were
    wrongly called inexpressible. `evaluate(..., redirected=("GIT_DIR=…",))` refuses today.
    The channel exists and denies; what is missing is a CALLER that populates it, which is
    guard work. Saying otherwise justified deferring work that is half already done.
    """

    def permits(self, rest) -> bool:
        return pa.evaluate(rest, records=[record()], resolve=lambda ref: GOOD_SHA).allowed

    def test_HOLE_long_options_abbreviate_past_an_exact_match_list(self) -> None:
        """git accepts UNAMBIGUOUS prefixes; the refused list holds only full spellings.

        `--forc` is deliberately absent: it is ambiguous among `--force`,
        `--force-with-lease` and `--force-if-includes`, so git rejects it and it is not a
        hole. The first version of this case asserted it, having tested the module and never
        `git` — the same error, one layer up, as the permission it documents.
        """
        for token in ("--del", "--dele", "--delet", "--prun", "--pru",
                      "--force-w", "--force-i", "--tag", "--ta", "--follow",
                      "--mir", "--mirr", "--mirro"):
            with self.subTest(token=token):
                self.assertTrue(
                    self.permits(["development", token, "work"]),
                    f"`{token}` is refused now — good. Remove it from this class and add it "
                    "to the battery's refusal cases.")

    def test_HOLE_receive_pack_names_the_program_the_far_side_runs(self) -> None:
        """Real options of git-push, and the guard already treats `-c <key>=<program>` as
        EXECUTION_CONTROL — the same family, spelled as a push option, is not looked at."""
        for token in ("--receive-pack=/tmp/x", "--exec=/tmp/x"):
            with self.subTest(token=token):
                self.assertTrue(self.permits(["development", token, "work"]))

    def test_NOT_A_HOLE_repo_loses_to_the_operand(self) -> None:
        """Recorded because an earlier version of this class asserted the opposite.

        git-push(1): "This option is equivalent to the <repository> argument. If both are
        specified, the command-line argument takes precedence." So `--repo=origin` beside the
        operand `development` reaches development, and with no operand the module refuses for
        naming no ref. It was written up as a hole on the strength of reading the module.
        """
        self.assertTrue(self.permits(["development", "--repo=origin", "work"]))
        self.assertFalse(pa.evaluate(["--repo=origin"], records=[record()],
                                     resolve=lambda ref: GOOD_SHA).allowed)


class TheGuardRefusesEveryPushForNow(unittest.TestCase):
    """The permission above is a SPECIFICATION. The guard does not consult it yet.

    🔴 Wiring it in was attempted and reverted. Two review rounds found ten ways to reach a
    real push past a permission that decides by matching tokens against hand-written lists:
    long options abbreviate (`--del`, `--prun`, `--force-w`), the relocating globals have
    environment twins (`GIT_DIR=`, `GIT_NAMESPACE=`), the payload's `workdir` moves the
    command without being a token at all, `--exec-path=` names the program git runs, and
    `git commit … && git push` moves the branch after the hook has already resolved it. The
    last two need the DECISION layer, where `cwd` and the shape of the whole line are known.

    So these cases assert the state that actually holds: every push is refused, including
    one carrying a flawless authorisation. They are written to FAIL the day the permission
    is wired in, which is the point — the day it is wired in, somebody has to come here and
    state the new truth deliberately.
    """

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"
        self.root.mkdir()
        self.sha = build_repository(self.root, "work")

        import guard_policy as gp
        import repo_topology as rt
        import session_binding as sb
        self.gp, self.rt = gp, rt

        # 🔴 Bound through the SESSION BINDING, not through `verdict(assigned=…)`. The
        # analysis layer derives the assignment itself, exactly as the hook process does,
        # so a test that injects it only at the decision layer would exercise a path the
        # runtime never takes — and would have passed while production read another root.
        saved = os.environ.get(sb.OPERATOR_ENV_VAR)
        os.environ[sb.OPERATOR_ENV_VAR] = str(self.root)

        def restore():
            if saved is None:
                os.environ.pop(sb.OPERATOR_ENV_VAR, None)
            else:
                os.environ[sb.OPERATOR_ENV_VAR] = saved
            sb.reset()
            rt.reset()

        self.addCleanup(restore)
        sb.reset()
        rt.reset()

    def authorise(self, **overrides) -> None:
        entry = record(branch="work", sha=self.sha)
        entry.update(overrides)
        path = self.root / pa.LEDGER_RELATIVE
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(entry) + "\n", encoding="utf-8")

    def ask(self, command: str):
        return self.gp.verdict(command)

    def test_an_unauthorised_push_is_refused_by_the_guard(self) -> None:
        reason = self.ask("git push development work")
        self.assertIsNotNone(reason)
        self.assertIn("Publication is an operator act", reason)

    def test_even_a_flawless_authorisation_does_not_move_the_guard(self) -> None:
        """The ledger entry is perfect and the push is still refused: nothing reads it yet."""
        self.authorise()
        reason = self.ask("git push development work")
        self.assertIsNotNone(reason)
        self.assertIn("NOT yet consulted", reason)

    def test_origin_is_refused_by_the_module_and_by_the_guard(self) -> None:
        """Asserting `"origin" in reason` proved nothing: DENY_NETWORK names origin twice,
        so it passed for a `development` push too. The module carries the real distinction."""
        self.authorise()
        self.assertFalse(judge(["origin", "work"], [record()]).allowed)
        self.assertIn("`origin` is denied to every runtime",
                      judge(["origin", "work"], [record()]).reason)
        self.assertIsNotNone(self.ask("git push origin work"))

    def test_the_guard_still_refuses_force_with_a_valid_record(self) -> None:
        self.authorise()
        self.assertIsNotNone(self.ask("git push --force development work"))

    def test_the_guard_still_refuses_a_red_gate(self) -> None:
        self.authorise(gate_verdict="FAIL")
        self.assertIsNotNone(self.ask("git push development work"))

    def test_the_guard_refuses_a_bare_push_with_a_valid_record(self) -> None:
        self.authorise()
        self.assertIsNotNone(self.ask("git push"))

    def test_the_guard_refuses_a_bundled_force(self) -> None:
        """Through the real guard, not just the module: `-fu` published a forced update."""
        self.authorise()
        self.assertIsNotNone(self.ask("git push -fu development work"))

    def test_the_guard_refuses_a_repository_redirecting_push(self) -> None:
        """`git -C <elsewhere> push` verified here and published from there."""
        self.authorise()
        self.assertIsNotNone(self.ask(f"git -C {self.root} push development work"))
        self.assertIsNotNone(self.ask(f"git --git-dir={self.root}/.git push development work"))

    def test_the_guard_refuses_a_tag_refspec(self) -> None:
        self.authorise()
        self.assertIsNotNone(self.ask("git push development refs/tags/work"))

    def test_the_guard_refuses_a_substituted_refspec_without_dying(self) -> None:
        """A crashed hook is silence, and silence on this channel is ALLOW."""
        self.authorise()
        self.assertIsNotNone(self.ask("git push development $(echo work)"))

    def test_the_qualified_form_is_refused_too(self) -> None:
        """`evaluate` would permit this one; the guard refuses it, which is the whole point."""
        self.authorise()
        self.assertTrue(judge(["development", "refs/heads/work"], [record()]).allowed)
        self.assertIsNotNone(self.ask("git push development refs/heads/work"))

    def test_other_network_subcommands_are_untouched_by_this_permission(self) -> None:
        """The carve-out is `push`. `send-pack` and friends keep the blanket refusal."""
        self.authorise()
        self.assertIsNotNone(self.ask("git send-pack development work"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
