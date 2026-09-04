#!/usr/bin/env python3
"""`Write` and `Edit` reach the same scope decision `echo x >` reaches, minus one rule.

Until this change the hook was registered on `Bash` alone, so a `Write` aimed at a peer
worktree was never evaluated while `echo x >` at the identical path was refused. Same act,
two doors, one lock. This suite covers the POLICY half; the registration is a separate
task, and the order is not a preference:

🔴 An unknown tool name raises `Undecidable`, which fails CLOSED. Registering the matcher
before teaching the guard these names would have denied EVERY `Write` and `Edit` in the
session, legitimate ones included, from the moment the matcher landed. Measured before it
was written, not discovered after.

The projection onto `echo x > <path>` then produced a second, better failure, and it is
the reason for the single carve-out below: `SHELL_WRITE_IN_ASSIGNED_WORKTREE` refuses a
shell write in the actor's own worktree and says *"Use Write or Edit"*. Projecting a Write
onto that shape made the guard answer every legitimate Write with an instruction to use
Write. The rule is skipped for this tool family and for that code alone; every rule ABOVE
it in the priority chain — `RUNTIME_CONFIG`, the `CONFINED` scopes, a missing session
assignment — still decides, and the cases below assert exactly that.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOOK = ROOT / "scripts" / "guard_bash_command.py"
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

import pre_tool_use_guard as ptug  # noqa: E402


def peers() -> list[str]:
    out = subprocess.run(["git", "-C", str(ROOT), "worktree", "list", "--porcelain"],
                         capture_output=True, text=True)
    found = [line.split(" ", 1)[1].strip()
             for line in out.stdout.splitlines() if line.startswith("worktree ")]
    return [p for p in found if Path(p).resolve() != ROOT.resolve()]


def decide(payload: dict) -> str:
    env = {**os.environ, "LEGEND_ASSIGNED_WORKTREE": str(ROOT)}
    env.pop("CLAUDE_PROJECT_DIR", None)
    result = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(payload),
                            capture_output=True, text=True, env=env)
    out = result.stdout.strip()
    if not out:
        return "allow"
    return json.loads(out)["hookSpecificOutput"]["permissionDecision"]


def write_to(path: str, tool: str = "Write") -> dict:
    """A payload for `tool`, keyed the way that tool actually carries its path.

    🔴 The key is read from `FILE_WRITE_TOOLS`, never hard-coded to `file_path`. The first
    version hard-coded it and `NotebookEdit` — which carries `notebook_path` — was refused,
    correctly, for having no path at all. A fixture that sends the wrong key tests the
    guard's fail-closed branch under the name of whatever it meant to test, and it does it
    silently, because a denial is what most of these cases expect anyway.
    """
    key = ptug.FILE_WRITE_TOOLS[tool]
    body: dict = {key: path}
    body.update({"content": "x"} if tool in ("Write",)
                else {"new_source": "x"} if tool == "NotebookEdit"
                else {"old_string": "a", "new_string": "b"})
    return {"tool_name": tool, "cwd": str(ROOT), "tool_input": body}


class TheFileToolsAreDecidableAtAll(unittest.TestCase):
    def test_every_name_the_guard_claims_to_police_is_in_the_known_set(self) -> None:
        for tool in ptug.FILE_WRITE_TOOLS:
            with self.subTest(tool=tool):
                self.assertNotEqual(
                    "deny", decide(write_to(str(ROOT / "notes.md"), tool)),
                    f"`{tool}` is refused inside the actor's OWN worktree — registering the "
                    "matcher in this state would deny all file authoring")

    def test_an_unknown_tool_still_fails_closed(self) -> None:
        """The positive control for the mechanism that made the order matter."""
        self.assertEqual("deny", decide(
            {"tool_name": "Sculpt", "cwd": str(ROOT), "tool_input": {"file_path": "/tmp/x"}}))

    def test_a_payload_naming_no_file_fails_closed(self) -> None:
        self.assertEqual("deny", decide(
            {"tool_name": "Edit", "cwd": str(ROOT),
             "tool_input": {"old_string": "a", "new_string": "b"}}))

    def test_a_file_path_that_is_not_a_string_fails_closed(self) -> None:
        for bogus in (None, 42, [], {}):
            with self.subTest(value=bogus):
                self.assertEqual("deny", decide(
                    {"tool_name": "Write", "cwd": str(ROOT),
                     "tool_input": {"file_path": bogus, "content": "x"}}))


class ThePeerLockIsTheSameThroughBothDoors(unittest.TestCase):
    def test_a_peer_worktree_is_refused_through_write_and_edit(self) -> None:
        """🔴 SKIPPED where there are none. A fresh clone has one worktree, so asserting
        that peers exist made this red in every clone — measuring the checkout it ran in
        and reporting it as a property of the repository."""
        found = peers()
        if not found:
            self.skipTest("this checkout has no peer worktrees; nothing to refuse")
        for peer in found:
            for tool in ("Write", "Edit"):
                with self.subTest(peer=peer, tool=tool):
                    self.assertEqual("deny", decide(write_to(f"{peer}/CLAUDE.md", tool)))

    def test_the_two_doors_agree_on_every_path(self) -> None:
        """The property, not a list: a scope decision may not depend on which tool asked.

        The one permitted disagreement is the actor's OWN worktree, where the shell is
        refused precisely in order to send the caller to `Write` — so `Write` allowing what
        `echo x >` denies there is the rule working, not a gap. It is asserted separately
        below rather than hidden in a tolerance here.
        """
        for path in peers() + ["/tmp/coverage-probe.md"]:
            with self.subTest(path=path):
                shell = decide({"tool_name": "Bash", "cwd": str(ROOT),
                                "tool_input": {"command": f"echo x > {path}/CLAUDE.md"
                                               if path in peers() else f"echo x > {path}"}})
                tool = decide(write_to(f"{path}/CLAUDE.md" if path in peers() else path))
                self.assertEqual(shell, tool,
                                 f"Bash and Write disagree about {path}")

    def test_the_one_permitted_disagreement_is_the_actors_own_worktree(self) -> None:
        own = str(ROOT / "notes.md")
        self.assertEqual("deny", decide({"tool_name": "Bash", "cwd": str(ROOT),
                                         "tool_input": {"command": f"echo x > {own}"}}))
        self.assertNotEqual("deny", decide(write_to(own)))

    def test_the_carve_out_is_narrower_than_the_tool_family(self) -> None:
        """It removes ONE code, not the guard. The confined scopes still decide.

        Named explicitly because "skip a denial for this tool" is exactly the shape that
        turns into an off switch when nobody pins how far it reaches.
        """
        self.assertEqual("deny", decide(write_to(str(ROOT / ".git" / "config"))))
        for peer in peers():
            self.assertEqual("deny", decide(write_to(f"{peer}/CLAUDE.md")))


class ARelativePathWithNoBaseIsNotAPath(unittest.TestCase):
    """🔴 The carve-out let an unanchored relative path walk past the guard.

    With no `cwd` key, `derive_workdir` yields `""`, `../peer/CLAUDE.md` fell to the
    INSIDE_REPO default, and skipping `SHELL_WRITE_IN_ASSIGNED_WORKTREE` then allowed it —
    while the identical path through `Bash` was denied. `file_target` promised to "fail
    closed on every shape that is not a plain non-empty string", and that was true of the
    STRING and silent about the BASE. A relative path with no base is a path-shaped string.
    """

    def payload(self, path: str, cwd=...) -> dict:
        body = {"tool_name": "Write", "tool_input": {"file_path": path, "content": "x"}}
        if cwd is not ...:
            body["cwd"] = cwd
        return body

    def test_a_relative_path_with_no_cwd_key_fails_closed(self) -> None:
        self.assertEqual("deny", decide(self.payload("../elsewhere/CLAUDE.md")))

    def test_a_relative_path_with_an_empty_cwd_fails_closed(self) -> None:
        self.assertEqual("deny", decide(self.payload("notes.md", cwd="")))

    def test_an_absolute_path_needs_no_base_and_is_unaffected(self) -> None:
        """The positive control: refusing everything unanchored must not refuse the
        anchored case, or the repair is just a denial."""
        self.assertNotEqual("deny", decide(self.payload(str(ROOT / "notes.md"), cwd=None)))

    def test_a_relative_path_WITH_a_cwd_still_resolves_and_still_locks_peers(self) -> None:
        self.assertNotEqual("deny", decide(self.payload("notes.md", cwd=str(ROOT))))
        for peer in peers():
            name = Path(peer).name
            if Path(peer).parent == ROOT.parent:
                self.assertEqual("deny", decide(
                    self.payload(f"../{name}/CLAUDE.md", cwd=str(ROOT))))


class WhatThisChangeDoesNotProtect(unittest.TestCase):
    """Stated as a test so it is read, and so it goes red if the reasoning stops holding."""

    def test_the_repositorys_own_control_files_stay_writable_by_design(self) -> None:
        """`runtime_config.py` excludes the repo's own `.claude/settings.json` on purpose:
        "the only route in is Write/Edit followed by a named `git add` and a commit — which
        is a review surface". The protection is the reviewable commit, not the guard, and
        this change does not alter that. If these ever start denying, the exclusion's
        reasoning has changed and the docstring above it must change with it."""
        for control in (".claude/settings.json", "framework/scripts/guard_policy.py"):
            with self.subTest(control=control):
                self.assertNotEqual("deny", decide(write_to(str(ROOT / control))))


if __name__ == "__main__":
    unittest.main(verbosity=2)
