#!/usr/bin/env python3
"""The revision-9 guarantees, asserted end to end against a real multi-worktree fixture.

Four properties, each of which was false in revision 8 and each measured false before
being repaired:

1. one actor cannot mutate another actor's worktree or shared git state;
2. a relative target resolves against the directory the command will RUN in;
3. an authorised `git commit` verifies, and a smuggled ref mutation does not;
4. a `chmod` is observed as a permission change, not as a write.

🔴 The post-effect cases AUTHORISE, EXECUTE, OBSERVE and VERIFY. A suite of static
policy calls cannot tell a guard that predicts correctly from one that also verifies
correctly, and revisions 1–7 had no way to notice the difference.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import effect_model as em  # noqa: E402
import guard_policy  # noqa: E402
import post_effect_verify as pev  # noqa: E402
import repo_topology as rt  # noqa: E402

GUARD_ENTRY = HERE / "pre_tool_use_guard.py"


def git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


def ask(command, cwd, workdir=None, tool="Bash", key="command"):
    """Run the real hook engine exactly as a runtime would."""
    tool_input = {key: command}
    if workdir is not None:
        tool_input["workdir"] = workdir
    payload = {"session_id": "s", "transcript_path": "/tmp/t", "cwd": cwd,
               "hook_event_name": "PreToolUse", "tool_name": tool,
               "tool_input": tool_input}
    result = subprocess.run([sys.executable, str(GUARD_ENTRY)],
                            input=json.dumps(payload), capture_output=True, text=True)
    if result.returncode != 0:
        return "ERROR"
    if not result.stdout.strip():
        return "ALLOW"
    return ("DENY" if json.loads(result.stdout)["hookSpecificOutput"][
        "permissionDecision"] == "deny" else "ALLOW")


class Fixture:
    """A shared checkout with an assigned worktree and a peer, nested as here."""

    def __init__(self):
        self.base = Path(tempfile.mkdtemp(prefix="confinement-"))
        self.shared = self.base / "shared"
        self.shared.mkdir()
        git(self.shared, "init", "-q", "-b", "main")
        git(self.shared, "config", "user.email", "t@t")
        git(self.shared, "config", "user.name", "t")
        (self.shared / "CLAUDE.md").write_text("router\n")
        git(self.shared, "add", "CLAUDE.md")
        git(self.shared, "commit", "-qm", "base")
        holder = self.shared / ".claude" / "worktrees"
        holder.mkdir(parents=True)
        self.assigned = holder / "assigned"
        self.peer = holder / "peer"
        git(self.shared, "worktree", "add", "-q", "-b", "assigned", str(self.assigned))
        git(self.shared, "worktree", "add", "-q", "-b", "peer", str(self.peer))
        self.common = Path(rt.of(str(self.assigned)).git_common_dir)

    def close(self):
        shutil.rmtree(self.base, ignore_errors=True)


class OneActorCannotMutateAnother(unittest.TestCase):
    """🔴 The revision-9 headline invariant."""

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        rt.reset()

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()
        rt.reset()

    def deny(self, command):
        rt.reset()
        self.assertEqual(ask(command, str(self.fx.assigned)), "DENY", command)

    def test_a_peer_worktree_is_not_writable_absolutely(self):
        self.deny(f"echo x > {self.fx.peer}/framework/pwned.md")

    def test_a_peer_worktree_is_not_writable_relatively(self):
        self.deny("echo x > ../peer/framework/pwned.md")

    def test_a_peer_worktree_is_not_deletable(self):
        self.deny("rm -rf ../peer/framework")

    def test_a_peer_file_is_not_movable_out(self):
        self.deny(f"mv {self.fx.peer}/CLAUDE.md /tmp/stolen")

    def test_the_shared_checkout_is_not_writable(self):
        self.deny(f"echo x > {self.fx.shared}/CLAUDE.md")

    def test_the_shared_git_config_is_not_writable(self):
        self.deny(f"echo x >> {self.fx.common}/config")

    def test_a_shared_hook_is_not_installable(self):
        self.deny(f"echo x > {self.fx.common}/hooks/pre-commit")

    def test_a_shared_ref_is_not_writable(self):
        self.deny(f"echo deadbeef > {self.fx.common}/refs/heads/main")

    def test_another_worktrees_administrative_head_is_not_writable(self):
        self.deny(f"echo x > {self.fx.common}/worktrees/peer/HEAD")

    def test_a_symlink_into_a_peer_does_not_launder_the_write(self):
        link = self.fx.assigned / "shortcut"
        if not link.exists():
            os.symlink(str(self.fx.peer), str(link))
        self.deny("echo x > shortcut/pwned.md")

    def test_a_symlink_into_the_common_dir_does_not_launder_the_write(self):
        link = self.fx.assigned / "gitlink"
        if not link.exists():
            os.symlink(str(self.fx.common), str(link))
        self.deny("echo x > gitlink/config")

    def test_git_dash_C_does_not_carry_the_subcommand_across(self):
        """The same act with better tooling. `-m <path>` alone is ALLOWED here."""
        self.deny("git -C ../peer commit -m x CLAUDE.md")

    def test_parent_relative_traversal_reaches_no_further(self):
        self.deny("echo x > ../../../CLAUDE.md")

    # ── the other direction: the guard must not block ordinary work ────────────────

    def test_reading_a_peer_stays_allowed(self):
        """🔴 Reading a peer is how review works here."""
        rt.reset()
        self.assertEqual(ask("cat ../peer/CLAUDE.md", str(self.fx.assigned)), "ALLOW")

    def test_reading_the_common_dir_stays_allowed(self):
        rt.reset()
        self.assertEqual(ask(f"cat {self.fx.common}/config", str(self.fx.assigned)),
                         "ALLOW")

    def test_the_actors_own_worktree_keeps_the_ordinary_ladder(self):
        rt.reset()
        self.assertEqual(ask("git add CLAUDE.md", str(self.fx.assigned)), "ALLOW")
        rt.reset()
        self.assertEqual(ask("echo x > /tmp/fine.txt", str(self.fx.assigned)), "ALLOW")


class NoAuthorityReachesAcrossTheRepository(unittest.TestCase):
    """The table property, asserted over `AUTHORITIES` rather than over examples.

    🔴 The confined scopes are absent from every grant by OMISSION, and an omission can
    be undone by someone adding a grant with no error anywhere. This is what closes
    that: a seventh authority class inherits the property or fails here.
    """

    def test_no_authority_grants_any_mutation_across_the_repository(self):
        for name, authority in em.AUTHORITIES.items():
            for kind in em.MUTATING:
                for scope in em.CONFINED:
                    with self.subTest(authority=name, kind=kind, scope=scope):
                        self.assertFalse(
                            authority.permits(kind, scope),
                            f"{name} grants {kind} at {scope}; no rung may reach across")

    def test_reading_across_the_repository_is_granted_everywhere(self):
        for name, authority in em.AUTHORITIES.items():
            for scope in em.CONFINED:
                with self.subTest(authority=name, scope=scope):
                    self.assertTrue(authority.permits(em.READ, scope),
                                    "a read confinement would break review")

    def test_no_authority_grants_delegation(self):
        for name, authority in em.AUTHORITIES.items():
            for scope in em.SCOPES:
                with self.subTest(authority=name, scope=scope):
                    self.assertFalse(authority.permits(em.DELEGATE, scope))

    def test_a_confined_denial_names_the_scope_and_not_a_missing_rung(self):
        """A denial that says 'you need REF_WRITE' invites an escalation request."""
        effect = em.Effect(em.WRITE, "x", em.PEER_WORKTREE)
        decision = em.authorize([effect], "PUBLISH")
        self.assertFalse(decision.authorized)
        self.assertIn("no authority class", decision.reason())


class TheEffectiveWorkdirIsTheExecutionDirectory(unittest.TestCase):
    """The 2×2, plus the malformed cases that must fail closed."""

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        rt.reset()

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()
        rt.reset()

    def verdict(self, cwd, workdir, command="echo x > probe.md"):
        rt.reset()
        return ask(command, cwd, workdir=workdir)

    def test_inside_inside_denies(self):
        self.assertEqual(self.verdict(str(self.fx.assigned), str(self.fx.assigned)),
                         "DENY")

    def test_outside_cwd_with_inside_workdir_denies(self):
        """🔴 The bypass: the command RUNS in the worktree."""
        self.assertEqual(self.verdict("/tmp", str(self.fx.assigned)), "DENY")

    def test_inside_cwd_with_outside_workdir_allows(self):
        """The other direction. A guard that refuses scratch work gets turned off."""
        self.assertEqual(self.verdict(str(self.fx.assigned), "/tmp"), "ALLOW")

    def test_outside_outside_allows(self):
        self.assertEqual(self.verdict("/tmp", "/tmp"), "ALLOW")

    def test_an_absent_workdir_falls_back_to_cwd(self):
        rt.reset()
        self.assertEqual(ask("echo x > probe.md", str(self.fx.assigned)), "DENY")

    def test_a_relative_workdir_resolves_against_cwd(self):
        self.assertEqual(
            self.verdict(str(self.fx.shared), ".claude/worktrees/assigned"), "DENY")

    def test_a_nonexistent_workdir_denies_rather_than_falling_back(self):
        """🔴 Falling back to cwd would restore the revision-8 reading for the one
        input designed to defeat it."""
        self.assertEqual(self.verdict("/tmp", "/no/such/directory/anywhere"), "DENY")

    def test_an_expanding_workdir_denies(self):
        self.assertEqual(self.verdict("/tmp", "$HOME/x"), "DENY")

    def test_an_empty_workdir_denies(self):
        self.assertEqual(self.verdict("/tmp", "   "), "DENY")

    def test_code_mode_uses_the_workdir_of_each_inner_call(self):
        """🔴 One payload, several execution bases — the recorded Codex session shape."""
        body = ("await tools.exec_command("
                + json.dumps({"cmd": "echo x > /tmp/ok.txt", "workdir": "/tmp"})
                + ");\nawait tools.exec_command("
                + json.dumps({"cmd": "echo x > probe.md",
                              "workdir": str(self.fx.assigned)}) + ");")
        rt.reset()
        payload = {"hook_event_name": "PreToolUse", "tool_name": "exec",
                   "cwd": "/tmp", "tool_input": {"input": body}}
        result = subprocess.run([sys.executable, str(GUARD_ENTRY)],
                                input=json.dumps(payload), capture_output=True, text=True)
        self.assertTrue(result.stdout.strip(),
                        "the second call runs in the worktree and must be refused")


class DelegationFailsClosed(unittest.TestCase):

    def verdict(self, command):
        rt.reset()
        return ask(command, str(Path(__file__).resolve().parents[2]))

    def test_codex_exec_is_refused(self):
        self.assertEqual(self.verdict("codex exec 'write the files'"), "DENY")

    def test_codex_full_auto_is_refused(self):
        self.assertEqual(self.verdict("codex exec --full-auto 'go'"), "DENY")

    def test_claude_print_is_refused(self):
        self.assertEqual(self.verdict("claude -p 'write framework/x'"), "DENY")

    def test_a_delegation_hidden_in_a_shell_wrapper_is_refused(self):
        self.assertEqual(self.verdict("bash -c \"codex exec 'go'\""), "DENY")

    def test_asking_a_runtime_its_version_is_not_delegation(self):
        """🔴 The control that keeps DELEGATE from becoming a ban on a binary."""
        self.assertEqual(self.verdict("codex --version"), "ALLOW")
        self.assertEqual(self.verdict("claude --version"), "ALLOW")

    def test_the_local_hook_state_service_is_not_delegation(self):
        """`codex_hook_state.py` documents this as the no-spend way to read hooks."""
        self.assertEqual(self.verdict("codex app-server"), "ALLOW")

    def test_an_unknown_subcommand_delegates_rather_than_passing(self):
        """A subcommand shipped after this table was written must fail closed."""
        self.assertEqual(self.verdict("codex somethingnobodyhaswritten"), "DENY")


class PostEffectVerificationMatchesTheAuthorisedSurface(unittest.TestCase):
    """AUTHORISE → EXECUTE → OBSERVE → VERIFY, in a disposable fixture."""

    def repo(self):
        d = tempfile.mkdtemp(prefix="post-effect-")
        self.addCleanup(shutil.rmtree, d, ignore_errors=True)
        for args in (("init", "-q", "-b", "work"), ("config", "user.email", "t@t"),
                     ("config", "user.name", "t")):
            git(d, *args)
        Path(d, "a.md").write_text("one\n")
        Path(d, "s.sh").write_text("#!/bin/sh\necho hi\n")
        git(d, "add", "a.md", "s.sh")
        git(d, "commit", "-qm", "base")
        return d

    # ── M-04 ──

    def test_an_authorised_commit_verifies(self):
        """🔴 A commit that succeeds MOVES THE BRANCH. That is not a side effect."""
        d = self.repo()
        Path(d, "a.md").write_text("two\n")
        result = pev.run("git commit -q -m x a.md", d, authority="SHELL_DEFAULT")
        self.assertEqual(result["result"], pev.VALID, result["result_reason"])
        self.assertEqual(result["extra_effect"], [])

    def test_an_empty_commit_verifies(self):
        d = self.repo()
        result = pev.run("git commit -q --allow-empty -m x", d, authority="SHELL_DEFAULT")
        self.assertEqual(result["result"], pev.VALID, result["result_reason"])

    def test_a_commit_plus_an_unrelated_ref_mutation_is_invalid(self):
        """🔴 The negative control. COMMIT covers ONE ref, not any ref."""
        d = self.repo()
        # 🔴 `other` starts AT the old HEAD and is moved to the NEW one. An earlier
        # draft of this test moved it to the old head, where it already pointed — a
        # no-op that mutated no ref, so the "negative control" observed nothing and
        # passed the comparison it was written to fail.
        git(d, "branch", "other")
        Path(d, "a.md").write_text("two\n")
        authorized = guard_policy.authorized_effects(
            "git commit -q -m x a.md", cwd=d, repo_root=d)
        snap_before = pev.snapshot(d)
        subprocess.run("git commit -q -m x a.md && "
                       "git update-ref refs/heads/other HEAD",
                       shell=True, cwd=d, capture_output=True)
        snap_after = pev.snapshot(d)
        self.assertNotEqual(snap_before.refs.get("refs/heads/other"),
                            snap_after.refs.get("refs/heads/other"),
                            "the fixture must actually move the second ref")
        observed = pev.resolve_head_kind(pev.delta(snap_before, snap_after, d), d,
                                         snap_before, snap_after)
        comparison = pev.verify(authorized, observed, d,
                                current_branch=snap_before.branch,
                                branch_after=snap_after.branch)
        self.assertFalse(comparison.valid,
                         "a ref the commit did not move must remain EXTRA")
        self.assertTrue(any(e.target == "refs/heads/other" for e in comparison.extra))

    def test_a_detached_head_commit_covers_no_ref(self):
        d = self.repo()
        git(d, "checkout", "-q", "--detach")
        self.assertEqual(pev.commit_covered_refs("", ""), frozenset())

    def test_a_commit_that_also_switches_branch_covers_nothing(self):
        self.assertEqual(pev.commit_covered_refs("work", "other"), frozenset())

    # ── M-05 ──

    def test_a_chmod_is_observed_as_a_permission_change(self):
        """🔴 Revision 8 read the mode from the INDEX, which a bare chmod never touches."""
        d = self.repo()
        result = pev.run("chmod +x s.sh", d, authority="REF_WRITE")
        self.assertEqual(result["result"], pev.VALID, result["result_reason"])
        kinds = {e["kind"] for e in result["observed_effect"]}
        self.assertIn(em.PERMISSION_CHANGE, kinds)
        self.assertNotIn(em.WRITE, kinds, "a mode-only change is not a content write")

    def test_reverting_a_mode_is_also_observed(self):
        d = self.repo()
        subprocess.run(["chmod", "+x", "s.sh"], cwd=d, capture_output=True)
        result = pev.run("chmod 644 s.sh", d, authority="REF_WRITE")
        self.assertEqual(result["result"], pev.VALID, result["result_reason"])

    def test_a_chmod_plus_a_content_write_reports_both(self):
        """A mode-only change and a mode-plus-content change give the identical ` M`."""
        d = self.repo()
        snap_before = pev.snapshot(d)
        subprocess.run("chmod +x s.sh && echo more >> s.sh", shell=True, cwd=d,
                       capture_output=True)
        observed = pev.delta(snap_before, pev.snapshot(d), d)
        kinds = {(e.kind, e.target) for e in observed}
        self.assertIn((em.PERMISSION_CHANGE, "s.sh"), kinds)
        self.assertIn((em.WRITE, "s.sh"), kinds)

    def test_a_chmod_is_refused_from_the_shell_floor(self):
        d = self.repo()
        result = pev.run("chmod +x s.sh", d, authority="SHELL_DEFAULT")
        self.assertEqual(result["result"], pev.REFUSED)
        self.assertFalse(result["executed"])

    def test_an_unobservable_effect_is_never_an_assumed_match(self):
        """🔴 UNOBSERVABLE must not be a synonym for 'assume it happened'."""
        self.assertNotIn(em.PERMISSION_CHANGE, pev.UNOBSERVABLE)

    # ── the surface that is authorised is the surface that is observed ──

    def test_no_effect_class_is_authorised_and_unobserved(self):
        """Every kind an authority grants inside the repository leaves a trace here,
        or is declared UNOBSERVABLE and refused rather than assumed."""
        granted = set()
        for authority in em.AUTHORITIES.values():
            for kind, scopes in authority.grants.items():
                if em.INSIDE_REPO in scopes and kind in em.MUTATING:
                    granted.add(kind)
        for kind in granted:
            with self.subTest(kind=kind):
                if kind in pev.UNOBSERVABLE:
                    continue
                # 🔴 Ask through `expand`, which is what the comparison actually does.
                # RENAME never reaches `COVERS` — it becomes DELETE + WRITE on both
                # sides first — so testing `COVERS` directly reports an authorised,
                # observed effect as unobserved. The property is about the pipeline,
                # not about one table in it.
                pieces = pev.expand([em.Effect(kind, "probe", em.INSIDE_REPO)])
                for piece in pieces:
                    self.assertTrue(
                        pev.COVERS.get(piece.kind),
                        f"{kind} is granted inside the repository and, after expansion, "
                        f"{piece.kind} is observed by nothing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
