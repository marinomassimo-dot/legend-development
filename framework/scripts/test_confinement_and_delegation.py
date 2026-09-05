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
import runtime_config as rc  # noqa: E402
import session_binding as sb  # noqa: E402

GUARD_ENTRY = HERE / "pre_tool_use_guard.py"


def git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


def hook_env(assigned, home=None):
    """The environment a runtime would start the hook in, with the frame stated.

    🔴 `CLAUDE_PROJECT_DIR` is CLEARED. Under a live session it points at this worktree,
    and every fixture case would then be judged against the session's own repository
    instead of the scene the test built — which is a suite passing for a reason it never
    wrote down. `assigned=None` is a state, not an omission: it is a session with no
    trusted binding at all, and it must be reachable from here or the fail-closed branch
    is untestable.
    """
    env = {**os.environ}
    env.pop("CLAUDE_PROJECT_DIR", None)
    env.pop("LEGEND_ASSIGNED_WORKTREE", None)
    if assigned is not None:
        env["LEGEND_ASSIGNED_WORKTREE"] = str(assigned)
    env.update(home or {})
    return env


def ask_full(command, cwd, workdir=None, tool="Bash", key="command",
             assigned=..., program=None, home=None):
    """`(verdict, decision code)` from the real hook engine, exactly as a runtime runs it.

    The code is returned because a denial is not one fact. `DENY` alone cannot tell
    `CONFINED_PEER_WORKTREE` from `SESSION_ASSIGNMENT_UNDERIVABLE`, and a confinement
    suite whose engine had simply lost its binding would be uniformly green — every
    `deny` assertion satisfied, and nothing confined by anything.
    """
    tool_input = {"input": program} if program is not None else {key: command}
    if workdir is not None and program is None:
        tool_input["workdir"] = workdir
    payload = {"session_id": "s", "transcript_path": "/tmp/t", "cwd": cwd,
               "hook_event_name": "PreToolUse", "tool_name": tool,
               "tool_input": tool_input}
    result = subprocess.run(
        [sys.executable, str(GUARD_ENTRY)], input=json.dumps(payload),
        capture_output=True, text=True,
        env=hook_env(cwd if assigned is ... else assigned, home))
    if result.returncode != 0:
        return "ERROR", "ERROR"
    if not result.stdout.strip():
        return "ALLOW", ""
    decision = json.loads(result.stdout)["hookSpecificOutput"]
    if decision["permissionDecision"] != "deny":
        return "ALLOW", ""
    trailer = [line for line in decision["permissionDecisionReason"].splitlines()
               if line.startswith("LEGEND_GUARD")]
    code = trailer[0].split("DECISION_CODE=")[1].split()[0] if trailer else "NO_TRAILER"
    return "DENY", code


def ask(command, cwd, workdir=None, tool="Bash", key="command", assigned=...,
        program=None, home=None):
    """Run the real hook engine exactly as a runtime would."""
    return ask_full(command, cwd, workdir, tool, key, assigned, program, home)[0]


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

    #: 🔴 The codes a CONFINEMENT denial may legitimately carry. Anything else — most of
    #: all `SESSION_ASSIGNMENT_UNDERIVABLE` — is a denial for a different reason, and a
    #: suite that accepted it would be green with the confinement gone.
    CONFINED_CODES = frozenset({"CONFINED_PEER_WORKTREE", "CONFINED_SHARED_CHECKOUT",
                                "CONFINED_GIT_COMMON_DIR", "CONFINED_MULTIPLE_SCOPES"})

    def deny(self, command):
        rt.reset()
        outcome, code = ask_full(command, str(self.fx.assigned),
                                 assigned=str(self.fx.assigned))
        self.assertEqual(outcome, "DENY", command)
        self.assertIn(code, self.CONFINED_CODES,
                      f"{command!r} was refused as {code}, which is not confinement")

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

    def test_the_confined_set_is_not_empty(self):
        """🔴 A property quantified over a set is vacuously true when the set is empty.

        Every assertion below iterates `em.CONFINED`. Emptying it makes all of them
        pass while the confinement is gone — and that mutation survived this suite until
        this test existed. A quantified property needs its domain pinned as well as its
        predicate.
        """
        self.assertEqual(em.CONFINED,
                         frozenset({em.PEER_WORKTREE, em.SHARED_CHECKOUT,
                                    em.GIT_COMMON_DIR}))
        for scope in em.CONFINED:
            self.assertIn(scope, em.SCOPES)
            self.assertIn(scope, em.NAMEABLE,
                          "a confined scope IS nameable; what stops it is that no "
                          "authority grants it, which is a different denial message")

    def test_no_authority_grants_any_mutation_across_the_repository(self):
        # DEC-20260905-AGILE-HARNESS-MODE (LEGEND_CORE §21e): the ONE pair that does reach
        # across is `(COMMIT, SHARED_CHECKOUT)` — a worktree session landing its finished
        # branch on `main` with `git -C <root> merge`. It is named in
        # `em.UNGRANTED_EXCEPTIONS`, asserted on its own in `test_effect_model.py`, and
        # skipped here so that every OTHER pair keeps the property this test exists for.
        for name, authority in em.AUTHORITIES.items():
            for kind in em.MUTATING:
                for scope in em.CONFINED:
                    if (kind, scope) in em.UNGRANTED_EXCEPTIONS:
                        continue
                    with self.subTest(authority=name, kind=kind, scope=scope):
                        self.assertFalse(
                            authority.permits(kind, scope),
                            f"{name} grants {kind} at {scope}; no rung may reach across")

    def test_the_landing_merge_is_the_only_thing_that_reaches_across(self):
        """The carve-out, pinned from this suite's side too: a worktree session may land on
        the shared checkout's `main` and may not stage, write, delete or reset there."""
        self.assertEqual(frozenset({(em.COMMIT, em.SHARED_CHECKOUT)}), em.UNGRANTED_EXCEPTIONS)
        shell = em.AUTHORITIES["SHELL_DEFAULT"]
        self.assertTrue(shell.permits(em.COMMIT, em.SHARED_CHECKOUT))
        for kind in (em.STAGE, em.WRITE, em.DELETE, em.RENAME, em.REF_MUTATION):
            with self.subTest(kind=kind):
                self.assertFalse(shell.permits(kind, em.SHARED_CHECKOUT))
        for scope in (em.PEER_WORKTREE, em.GIT_COMMON_DIR):
            with self.subTest(scope=scope):
                self.assertFalse(shell.permits(em.COMMIT, scope))

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
        return ask(command, cwd, workdir=workdir, assigned=str(self.fx.assigned))

    def code(self, cwd, workdir, command="echo x > probe.md"):
        rt.reset()
        return ask_full(command, cwd, workdir=workdir,
                        assigned=str(self.fx.assigned))[1]

    def test_inside_inside_denies(self):
        self.assertEqual(self.verdict(str(self.fx.assigned), str(self.fx.assigned)),
                         "DENY")

    def test_outside_cwd_with_inside_workdir_denies(self):
        """🔴 The bypass: the command RUNS in the worktree."""
        self.assertEqual(self.verdict("/tmp", str(self.fx.assigned)), "DENY")

    def test_the_2x2_denies_for_the_right_reason_in_every_cell(self):
        """🔴 The assignment is HELD FIXED across all four cells — revision 10.

        Every cell here varies only where the command RUNS. Letting the assignment move
        with the cwd, as revision 9 did, makes the outside-cwd rows deny because the
        binding vanished rather than because the target is in the repository — the same
        verdict from a derivation that has stopped working, which is what the decision
        code is for.
        """
        self.assertEqual(
            self.code(str(self.fx.assigned), str(self.fx.assigned)),
            "SHELL_WRITE_IN_ASSIGNED_WORKTREE")
        self.assertEqual(
            self.code("/tmp", str(self.fx.assigned)),
            "SHELL_WRITE_IN_ASSIGNED_WORKTREE",
            "the target is in the assigned worktree wherever the session's cwd is")

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

    def test_a_nonexistent_workdir_denies_even_where_falling_back_would_allow(self):
        """🔴 The DISCRIMINATING case, and the reason the one above is not enough.

        With the workdir check removed, a nonexistent path still yields no repository
        root, and an unknown root makes every non-scratch target `INSIDE_REPO` — so the
        command denies anyway and the test above passes with the guarantee deleted.
        That mutation survived until this case existed.

        Point the nonexistent workdir at SCRATCH space and the two readings separate:
        falling back derives `/tmp/<gone>/probe.md`, which is scratch and ALLOWED, while
        refusing to guess denies. Same rule, and now only one answer satisfies it.
        """
        self.assertEqual(self.verdict("/tmp", "/tmp/no-such-directory-here"), "DENY")

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

    def test_a_binary_files_content_change_is_never_read_as_no_change(self):
        """🔴 `git diff --numstat` prints `-` for both counts on a binary file.

        Reading that as zero makes a content rewrite invisible, so an authorised
        `chmod` would cover a rewrite of the bytes — `content_moved` returning False is
        a claim that nothing changed, and git declining to COUNT lines is not evidence
        that none moved. That mutation survived until this test existed, because every
        other fixture here is a text file.
        """
        d = self.repo()
        Path(d, "blob.bin").write_bytes(bytes(range(256)))
        git(d, "add", "blob.bin")
        git(d, "commit", "-qm", "binary")
        Path(d, "blob.bin").write_bytes(bytes(reversed(range(256))))
        self.assertTrue(pev.content_moved(d, "blob.bin"),
                        "a binary rewrite must be reported as a content change")

    def test_a_binary_file_left_alone_is_not_reported_as_changed(self):
        """The positive control: `content_moved` must not simply always say yes."""
        d = self.repo()
        Path(d, "blob.bin").write_bytes(bytes(range(256)))
        git(d, "add", "blob.bin")
        git(d, "commit", "-qm", "binary")
        self.assertFalse(pev.content_moved(d, "blob.bin"))

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


class TheAssignedWorktreeIsSessionBound(unittest.TestCase):
    """🔴 R1, as the cross-product the brief asks for, through the PRODUCTION adapter.

        MODEL-SELECTED EXECUTION LOCATION
        MUST NOT CHANGE
        THE ACTOR'S AUTHORITY PERIMETER.

    Revision 9 tested confinement and `workdir` in separate files, and each passed. The
    defect lived in the cell where they cross: confinement was measured with the target
    named absolutely and the frame left alone, `workdir` was measured with the target
    relative and the frame moved, and nobody moved the frame ONTO a confined target. Six
    spellings reached `ALLOW` at ordinary `SHELL_DEFAULT`.

    So the axes are crossed here, in one table, and every cell goes through
    `pre_tool_use_guard` rather than through `guard_policy` — the adapter is where the
    assignment is derived, and a policy-level test would pass with the adapter still
    handing it the workdir.
    """

    #: The mutating families `SHELL_DEFAULT` GRANTS inside the assigned worktree. That
    #: is what makes them the interesting ones: rotating the frame does not defeat a
    #: rule, it moves the target into the class the rule permits.
    FAMILIES = (
        ("named staging", "git add framework/probe.md"),
        ("commit", "git commit -m x framework/probe.md"),
        ("a content write", "echo x > framework/probe.md"),
        ("a delete", "rm framework/probe.md"),
    )

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()
        rt.reset()

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()
        rt.reset()

    def targets(self):
        return (("assigned", str(self.fx.assigned), None),
                ("peer", str(self.fx.peer), "CONFINED_PEER_WORKTREE"),
                ("shared", str(self.fx.shared), "CONFINED_SHARED_CHECKOUT"))

    # ── the cross-product ──────────────────────────────────────────────────────────

    def test_every_rotation_of_the_execution_frame_is_refused(self):
        """target × invocation × family, with the assignment held fixed throughout."""
        assigned = str(self.fx.assigned)
        probed = 0
        for label, target, code in self.targets():
            if code is None:
                continue
            for spelling, cwd, workdir in (
                ("workdir", assigned, target),
                ("cwd", target, None),
                ("cwd and workdir", target, target),
                ("cwd assigned, workdir peer-ish", assigned, target),
            ):
                for family, command in self.FAMILIES:
                    with self.subTest(target=label, via=spelling, family=family):
                        rt.reset()
                        outcome, observed = ask_full(command, cwd, workdir=workdir,
                                                     assigned=assigned)
                        probed += 1
                        self.assertEqual(outcome, "DENY")
                        self.assertEqual(
                            observed, code,
                            "refused, but not as a cross-repository act — a denial "
                            "from a lost binding is a different failure")
        # 🔴 A loop that ran zero cells is a green test that measured nothing.
        self.assertEqual(probed, 2 * 4 * len(self.FAMILIES))

    def test_git_dash_C_and_a_rotated_workdir_agree(self):
        """The two spellings of one act must reach the same verdict AND the same code.

        Under revision 9 they did not: `git -C <peer>` was refused and `workdir=<peer>`
        was allowed. That disagreement was the tell, and it is asserted here so a repair
        that closes one spelling and not the other cannot pass.
        """
        assigned = str(self.fx.assigned)
        for family, command in self.FAMILIES:
            if not command.startswith("git "):
                continue
            with self.subTest(family=family):
                rt.reset()
                rotated = ask_full(command, assigned, workdir=str(self.fx.peer),
                                   assigned=assigned)
                rt.reset()
                retargeted = ask_full(
                    command.replace("git ", f"git -C {self.fx.peer} ", 1),
                    assigned, assigned=assigned)
                self.assertEqual(rotated, retargeted)

    def test_a_code_mode_inner_workdir_cannot_rotate_the_frame_either(self):
        """One payload, several execution bases, exactly one actor.

        The recorded 2026-08-28 Codex session called `tools.exec_command({...})` twenty
        times with a `workdir` per call. Revision 9 honoured each inner workdir for path
        resolution AND for the assignment, so code mode carried the bypass too.
        """
        assigned = str(self.fx.assigned)
        body = ("await tools.exec_command("
                + json.dumps({"cmd": "git add framework/probe.md",
                              "workdir": str(self.fx.peer)}) + ");")
        rt.reset()
        outcome, code = ask_full("", assigned, tool="exec", program=body,
                                 assigned=assigned)
        self.assertEqual((outcome, code), ("DENY", "CONFINED_PEER_WORKTREE"))

    # ── the other direction ────────────────────────────────────────────────────────

    def test_the_assigned_worktree_keeps_every_granted_family(self):
        """🔴 The control. An engine that closed the rotations by refusing these would
        pass every assertion above and be useless."""
        assigned = str(self.fx.assigned)
        for spelling, cwd, workdir in (("no workdir", assigned, None),
                                       ("workdir=assigned", assigned, assigned),
                                       ("workdir=assigned, cwd elsewhere", "/tmp",
                                        assigned)):
            for family, command in (("named staging", "git add framework/probe.md"),
                                    ("commit", "git commit -m x framework/probe.md")):
                with self.subTest(via=spelling, family=family):
                    rt.reset()
                    self.assertEqual(ask(command, cwd, workdir=workdir,
                                         assigned=assigned), "ALLOW")

    def test_the_shared_checkout_is_writable_by_the_actor_assigned_to_it(self):
        """🔴 Confinement is a RELATION, not a directory.

        An Orchestrator whose session is bound to the shared checkout owns it, and the
        same command that F6 refuses must succeed for that actor. An engine that
        hard-coded "the main working tree is never writable" would pass every rotation
        case and fail here.
        """
        rt.reset()
        self.assertEqual(ask("git add CLAUDE.md", str(self.fx.shared),
                             assigned=str(self.fx.shared)), "ALLOW")
        rt.reset()
        self.assertEqual(
            ask_full("git add framework/probe.md", str(self.fx.peer),
                     assigned=str(self.fx.shared)),
            ("DENY", "CONFINED_PEER_WORKTREE"),
            "and the actor assigned the shared checkout still has peers")

    def test_reads_survive_every_rotation(self):
        assigned = str(self.fx.assigned)
        for label, target, _ in self.targets():
            with self.subTest(target=label):
                rt.reset()
                self.assertEqual(ask("git status --short", target, workdir=target,
                                     assigned=assigned), "ALLOW")

    # ── the binding itself ─────────────────────────────────────────────────────────

    def test_with_no_binding_every_repository_mutation_is_refused(self):
        assigned = str(self.fx.assigned)
        for family, command in self.FAMILIES:
            with self.subTest(family=family):
                rt.reset()
                outcome, code = ask_full(command, assigned, assigned=None)
                self.assertEqual((outcome, code),
                                 ("DENY", "SESSION_ASSIGNMENT_UNDERIVABLE"))

    def test_with_no_binding_scratch_and_reads_survive(self):
        assigned = str(self.fx.assigned)
        rt.reset()
        self.assertEqual(ask("echo x > /tmp/legend-probe.txt", assigned, assigned=None),
                         "ALLOW")
        rt.reset()
        self.assertEqual(ask("git status --short", assigned, assigned=None), "ALLOW")

    def test_the_binding_never_comes_from_the_payload(self):
        """🔴 The property, asserted on the module rather than on an example.

        `session_binding` names every source it will read. `workdir`, `cwd` and any key
        inside `tool_input` must not be among them — a source added there later would
        hand the perimeter back to the model with no test failing anywhere else.
        """
        forbidden = {"workdir", "cwd", "command", "cmd", "script", "tool_input"}
        for source, _ in sb.candidates({"workdir": "/x", "cwd": "/y"}, {}):
            self.assertNotIn(source.lower(), forbidden)
        self.assertEqual(sb.PAYLOAD_KEY, "workspace_root",
                         "the only payload key read is the ENVELOPE's workspace root, "
                         "which the runtime writes and the model does not")
        found = sb.derive({"workdir": str(self.fx.peer), "cwd": str(self.fx.peer)}, {})
        self.assertIsNone(found.worktree)
        self.assertEqual(found.source, sb.NONE)


class TheSessionBindingReportsWhichSourceAnsweredIt(unittest.TestCase):
    """The precedence table, and the fact that a rejected candidate is not a silent one."""

    @classmethod
    def setUpClass(cls):
        cls.fx = Fixture()

    @classmethod
    def tearDownClass(cls):
        cls.fx.close()

    def test_the_caller_outranks_every_environment_source(self):
        found = sb.derive({}, {sb.OPERATOR_ENV_VAR: str(self.fx.peer)},
                          assigned=str(self.fx.assigned))
        self.assertEqual(found.source, sb.CALLER)
        self.assertEqual(found.worktree, os.path.realpath(str(self.fx.assigned)))

    def test_the_operator_variable_outranks_the_runtime_one(self):
        found = sb.derive({}, {sb.OPERATOR_ENV_VAR: str(self.fx.assigned),
                               sb.RUNTIME_ENV_VAR: str(self.fx.peer)})
        self.assertEqual(found.source, sb.OPERATOR_ENV)

    def test_the_runtime_variable_answers_when_the_operator_sets_none(self):
        found = sb.derive({}, {sb.RUNTIME_ENV_VAR: str(self.fx.assigned)})
        self.assertEqual(found.source, sb.RUNTIME_ENV)

    def test_the_payload_envelope_is_the_last_source(self):
        found = sb.derive({sb.PAYLOAD_KEY: str(self.fx.assigned)}, {})
        self.assertEqual(found.source, sb.RUNTIME_PAYLOAD)

    def test_a_subdirectory_binds_the_worktree_that_contains_it(self):
        """`CLAUDE_PROJECT_DIR` names the directory a session was opened in, which may
        be below the root. The binding is the worktree, not the directory."""
        below = Path(self.fx.assigned) / "framework"
        below.mkdir(exist_ok=True)
        found = sb.derive({}, {sb.RUNTIME_ENV_VAR: str(below)})
        self.assertEqual(found.worktree, os.path.realpath(str(self.fx.assigned)))

    def test_a_candidate_outside_any_working_tree_binds_nothing_and_says_so(self):
        found = sb.derive({}, {sb.OPERATOR_ENV_VAR: "/"})
        self.assertIsNone(found.worktree)
        self.assertIn("not inside a git working tree", found.detail)

    def test_a_candidate_that_needs_a_shell_is_refused(self):
        found = sb.derive({}, {sb.OPERATOR_ENV_VAR: "$HOME/x"})
        self.assertIsNone(found.worktree)

    def test_a_relative_candidate_is_refused(self):
        found = sb.derive({}, {sb.OPERATOR_ENV_VAR: "../peer"})
        self.assertIsNone(found.worktree)

    def test_nothing_set_at_all_is_a_state_with_a_name(self):
        found = sb.derive({}, {})
        self.assertIsNone(found.worktree)
        self.assertEqual(found.source, sb.NONE)
        self.assertFalse(found.ok)


class LaunchersReachTheirChild(unittest.TestCase):
    """🔴 R9. Nine measured spellings that put a launcher in `argv[0]`.

    The repair is UNWRAPPING and not a name list: whatever the child does, the launcher
    does. That is why the benign controls matter as much as the delegating ones — a rule
    that denied every `npx` would satisfy the first half and be a ban.
    """

    ROOT = str(Path(__file__).resolve().parents[2])

    def verdict(self, command):
        rt.reset()
        return ask(command, self.ROOT, assigned=self.ROOT)

    def test_every_measured_launcher_reaches_delegate(self):
        for command in ("npx codex exec 'go'", "npx -y codex exec 'go'",
                        "bunx codex exec 'go'", "pnpm dlx codex exec 'go'",
                        "yarn dlx codex exec 'go'", "uvx codex exec 'go'",
                        "pipx run codex exec 'go'", "npm exec codex exec 'go'",
                        "npx claude -p 'write framework/x'"):
            with self.subTest(command=command):
                self.assertEqual(self.verdict(command), "DENY")

    def test_the_denial_is_delegation_and_not_something_else(self):
        _, code = ask_full("npx codex exec 'go'", self.ROOT, assigned=self.ROOT)
        self.assertEqual(code, "DELEGATE")

    def test_a_package_flag_does_not_hide_the_program(self):
        self.assertEqual(self.verdict("npx -p some-package codex exec 'go'"), "DENY")

    def test_a_call_flag_carries_a_shell_string_and_is_read_as_one(self):
        self.assertEqual(self.verdict("npx -c 'codex exec go'"), "DENY")

    def test_a_launcher_inside_a_shell_wrapper_still_reaches_delegate(self):
        self.assertEqual(self.verdict("bash -c \"npx codex exec 'go'\""), "DENY")

    def test_a_launcher_running_an_ordinary_program_stays_allowed(self):
        """🔴 The control. `npx cowsay hi` is an ordinary invocation."""
        for command in ("npx cowsay hi", "npx -y prettier --check .",
                        "uvx ruff check .", "pnpm dlx tsc --noEmit"):
            with self.subTest(command=command):
                self.assertEqual(self.verdict(command), "ALLOW")

    def test_a_launcher_running_a_writer_is_read_as_that_writer(self):
        """The general property, and the reason this is unwrapping: a child that writes
        into the repository is a repository write however it was started."""
        self.assertEqual(self.verdict("npx some-tool > AGENTS.md"), "DENY")

    def test_a_launcher_with_no_program_fails_closed(self):
        self.assertEqual(self.verdict("npx"), "DENY")

    def test_the_launcher_table_is_not_empty(self):
        """A property quantified over a table is vacuously true when the table is empty,
        and emptying it is the mutation that would otherwise survive every case above."""
        self.assertGreaterEqual(len(guard_policy.PACKAGE_LAUNCHERS), 9)
        self.assertIn(("npx",), guard_policy.PACKAGE_LAUNCHERS)
        self.assertIn(("pnpm", "dlx"), guard_policy.PACKAGE_LAUNCHERS)


class TheActiveRuntimeConfigurationCannotEraseItself(unittest.TestCase):
    """🔴 R7. The registration is the switch, and revision 9 let the actor move it."""

    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix="runtime-config-"))
        self.addCleanup(shutil.rmtree, self.base, ignore_errors=True)
        (self.base / ".claude").mkdir()
        (self.base / ".codex" / "sessions").mkdir(parents=True)
        (self.base / ".claude" / "settings.json").write_text("{}\n")
        (self.base / ".codex" / "config.toml").write_text("# x\n")
        self.env = {"HOME": str(self.base),
                    "CLAUDE_CONFIG_DIR": str(self.base / ".claude"),
                    "CODEX_HOME": str(self.base / ".codex")}
        rc.reset()
        self.addCleanup(rc.reset)

    def verdict(self, command):
        rt.reset()
        return ask(command, str(Path(__file__).resolve().parents[2]),
                   assigned=str(Path(__file__).resolve().parents[2]), home=self.env)

    def test_the_active_claude_registration_is_not_writable(self):
        self.assertEqual(
            self.verdict(f"echo x > {self.base}/.claude/settings.json"), "DENY")

    def test_the_machine_local_claude_layer_is_not_writable(self):
        self.assertEqual(
            self.verdict(f"echo x > {self.base}/.claude/settings.local.json"), "DENY")

    def test_the_active_codex_registration_is_not_writable(self):
        self.assertEqual(
            self.verdict(f"echo x > {self.base}/.codex/config.toml"), "DENY")

    def test_deleting_the_codex_home_is_not_allowed(self):
        """🔴 The directory holds the config without naming it, which is why membership
        is equal-or-ancestor rather than equality."""
        self.assertEqual(self.verdict(f"rm -rf {self.base}/.codex"), "DENY")

    def test_moving_the_codex_home_aside_is_not_allowed(self):
        self.assertEqual(
            self.verdict(f"mv {self.base}/.codex {self.base}/.codex-off"), "DENY")

    def test_the_denial_names_the_runtime_configuration(self):
        _, code = ask_full(f"echo x > {self.base}/.codex/config.toml",
                           str(Path(__file__).resolve().parents[2]),
                           assigned=str(Path(__file__).resolve().parents[2]),
                           home=self.env)
        self.assertEqual(code, "RUNTIME_CONFIG")

    # ── the other direction ────────────────────────────────────────────────────────

    def test_unrelated_contents_beside_the_registration_stay_writable(self):
        """🔴 The control that keeps this a RESOLUTION and not a prefix ban. Sessions,
        caches and plugin data are not control surfaces."""
        for path in (f"{self.base}/.codex/sessions/rollout.jsonl",
                     f"{self.base}/.claude/cache.json",
                     f"{self.base}/notes.txt"):
            with self.subTest(path=path):
                self.assertEqual(self.verdict(f"echo x > {path}"), "ALLOW")

    def test_reading_the_registration_stays_granted(self):
        self.assertEqual(self.verdict(f"cat {self.base}/.codex/config.toml"), "ALLOW")

    def test_an_unresolvable_surface_claims_nothing(self):
        """🔴 The honest direction: with no HOME there are no members, `ok` is False, and
        the readiness table must say UNDERIVABLE rather than PASS."""
        surface = rc.resolve({})
        self.assertFalse(surface.ok)
        self.assertEqual(surface.members, frozenset())
        self.assertFalse(surface.contains("/anything"))

    def test_a_member_that_does_not_exist_yet_is_still_a_member(self):
        """Creating the file IS the registration act."""
        surface = rc.resolve({"HOME": "/nowhere-at-all"})
        self.assertTrue(surface.contains("/nowhere-at-all/.codex/config.toml"))

    def test_the_repositorys_own_settings_are_not_runtime_config(self):
        """Inside the worktree the governance surface already exists — Write/Edit, a
        named `git add`, a reviewed commit. Pulling it in here would make deployment
        route D unreachable by the actor who proposes it."""
        root = Path(__file__).resolve().parents[2]
        surface = rc.resolve(self.env)
        self.assertFalse(surface.contains(str(root / ".claude" / "settings.json")))

    def test_the_repository_scopes_are_consulted_BEFORE_the_runtime_config_scope(self):
        """🔴 The ordering, pinned — and it was pinned because a mutation survived.

        `classify_target` returns early for the four repository scopes, and that early
        return LOOKS redundant: the fall-through re-consults the same topology and maps
        the same scopes through `_FROM_TOPOLOGY`. Deleting it changes nothing for any
        path outside the repository, which is why the mutation that deletes it survived
        the whole suite — an EQUIVALENT MUTANT everywhere except here.

        It is load-bearing for exactly one case, and this is it: a runtime-config member
        that lives INSIDE the assigned worktree — an operator who pointed `CODEX_HOME` at
        a directory in the repository — must stay `INSIDE_REPO`, where a named `git add`
        and a reviewed commit are the governance surface, rather than becoming
        `RUNTIME_CONFIG`, where nothing can land at all.
        """
        root = Path(__file__).resolve().parents[2]
        inside = root / ".codex"
        env = {"HOME": str(root), "CODEX_HOME": str(inside),
               "CLAUDE_CONFIG_DIR": str(root / ".claude")}
        rc.reset()
        self.addCleanup(rc.reset)
        self.assertTrue(rc.resolve(env).contains(str(inside / "config.toml")),
                        "the fixture must actually put a member inside the worktree, or "
                        "this test asserts nothing about the ordering")
        rt.reset()
        self.assertEqual(
            ask("git add .codex/config.toml", str(root), assigned=str(root), home=env),
            "ALLOW",
            "a config file inside the assigned worktree keeps the repository's own "
            "governance surface; RUNTIME_CONFIG would make it unlandable")


class ChmodLocatesItsModeOperand(unittest.TestCase):
    """🔴 R8. A refusal in the WRONG direction, which is still a defect."""

    ROOT = str(Path(__file__).resolve().parents[2])

    def verdict(self, command):
        rt.reset()
        return ask(command, self.ROOT, assigned=self.ROOT)

    def test_short_mode_operands_on_scratch_are_allowed(self):
        for command in ("chmod -x /tmp/probe.sh", "chmod -w /tmp/probe.sh",
                        "chmod -r /tmp/probe.sh", "chmod -R -x /tmp/probe-dir",
                        "chmod u+x /tmp/probe.sh", "chmod a-w /tmp/probe.sh",
                        "chmod +x /tmp/probe.sh", "chmod 755 /tmp/probe.sh"):
            with self.subTest(command=command):
                self.assertEqual(self.verdict(command), "ALLOW")

    def test_the_same_spellings_inside_the_repository_still_need_ref_write(self):
        """🔴 The negative that keeps the repair from being 'stop reading chmod'."""
        for command in ("chmod -x framework/scripts/legend_lint.py",
                        "chmod +x framework/scripts/legend_lint.py",
                        "chmod 755 framework/scripts/legend_lint.py"):
            with self.subTest(command=command):
                self.assertEqual(self.verdict(command), "DENY")

    def test_the_mode_is_located_and_the_path_is_named(self):
        """A receipt has to name what was touched, so the operand split is asserted
        directly rather than through the verdict — both spellings deny, and only this
        can tell a located mode from a lost path."""
        self.assertEqual(guard_policy.chmod_operands(["chmod", "-x", "a.py"]),
                         ("-x", ["a.py"]))
        self.assertEqual(guard_policy.chmod_operands(["chmod", "-R", "-x", "d"]),
                         ("-x", ["d"]))
        self.assertEqual(guard_policy.chmod_operands(["chmod", "755", "a.py"]),
                         ("755", ["a.py"]))
        self.assertEqual(
            guard_policy.chmod_operands(["chmod", "--reference", "b", "a.py"]),
            (None, ["a.py"]),
            "`--reference` supplies the mode, so there is no mode OPERAND and the "
            "positional rule would have eaten the path")

    def test_chown_keeps_its_positional_owner_spec(self):
        """The repair is chmod-shaped. `chown user file` still drops the first operand,
        because `user` is not a path and never looked like a mode."""
        self.assertEqual(self.verdict("chown me /tmp/probe.sh"), "ALLOW")
        self.assertEqual(self.verdict("chown me framework/scripts/legend_lint.py"),
                         "DENY")


if __name__ == "__main__":
    unittest.main(verbosity=2)
