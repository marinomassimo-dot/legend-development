#!/usr/bin/env python3
"""The surfaces that say the guard does not consult `push_authorization`. Only code knows.

The count is deliberately not written into this sentence any more. It was "four" here while
`NOT_ENFORCED_MARKERS` held three, and the number was wrong in the direction that hides a
gap: the real fourth surface — the DEC's own D-2 row — existed and was uncovered, so the
prose was simultaneously miscounting and describing something true. `len(NOT_ENFORCED_MARKERS)`
is the count, and the tests below iterate it rather than a number anyone typed.

This is prose that has already been false. `6f8e73d` is titled *"The callout that said the
guard consults it"* — for one commit §21d's own provenance callout asserted the opposite of
what the code did, and nothing caught it, because the equality assertion in
`test_stop_policy.py` skips the leading callout before comparing. A sentence about what
code does, sitting in the one place a reader is most likely to trust and no checker looks,
is a sentence that will be wrong again.

So the sentence is made executable here. The derived fact is computed from source bytes;
the declared fact is parsed from each surface that states it; and they must agree. The test
is bidirectional by construction:

* while the guard does NOT consult the module, every surface must carry its "not enforced"
  marker — a surface that quietly drops the caveat is a surface that reads as a permission;
* the moment the guard DOES consult it, every one of those markers must be gone — the
  wiring commit cannot land while any of these files still tells an actor it is absent.

The second direction needs no guess about how a future commit will word the enforced case,
which is why it is stated as the ABSENCE of the current marker rather than the presence of
some predicted replacement.

🔴 One of these surfaces is inside the ratified body of §21d, whose text is reserved to
the operator by its own RESERVED list. If this suite goes red because the guard started
consulting the module, the repair to THAT surface is an operator act — a re-ratification —
and not an edit an agent may make to turn the suite green. The failure message says so.

Two things this suite deliberately does NOT do. It never imports `guard_policy`: an import
resolves through `sys.path` and can be served from a stale `__pycache__` outside the
repository, so what it would measure is a bytecode artefact rather than the file under
review. And it does not stop at the premise — it also runs the real hook on a real push
command, because "the guard does not consult it, SO every push is refused" is two claims
and only the second one is the behaviour anybody depends on.
"""
from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "scripts"
POLICY_DIR = ROOT / "framework" / "scripts"

MODULE = "push_authorization"
# The deployed guard is the hook Claude registers, not `guard_policy.py` alone. Walking
# from the entry point is what makes the population "everything the running guard can
# reach" rather than "the file this suite happened to name".
ENTRYPOINTS = (
    HERE / "guard_bash_command.py",
    POLICY_DIR / "pre_tool_use_guard.py",
    POLICY_DIR / "guard_policy.py",
)


def local_imports(tree: ast.AST) -> set[str]:
    """Module names imported by real import statements — not names in comments or strings."""
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.level == 0:
                names.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call):
            # `importlib.import_module("push_authorization")` and `__import__(...)` are
            # imports that no `ast.Import` node records.
            target = node.func
            named = (getattr(target, "attr", None) or getattr(target, "id", None))
            if named in {"import_module", "__import__"} and node.args:
                first = node.args[0]
                if isinstance(first, ast.Constant) and isinstance(first.value, str):
                    names.add(first.value.split(".")[0])
    return names


SPAWNERS = {"run", "Popen", "call", "check_call", "check_output", "system", "execv"}


def spawns_the_script(tree: ast.AST) -> bool:
    """Shelling out to the script is consulting it just as much as importing it.

    Scoped to the ARGUMENTS OF A CALL, not to any string in the file. `guard_policy.py`
    names `push_authorization.py` inside its denial message; a check that treated every
    occurrence as a subprocess would report the live tree as consulting the module, and
    this whole suite would then assert the exact opposite of the truth.
    """
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        named = getattr(node.func, "attr", None) or getattr(node.func, "id", None)
        if named not in SPAWNERS:
            continue
        for argument in ast.walk(ast.Module(body=list(node.args), type_ignores=[])):
            if isinstance(argument, ast.Constant) and isinstance(argument.value, str):
                if argument.value.endswith(f"{MODULE}.py"):
                    return True
    return False


def guard_consults_push_authorization() -> tuple[bool, list[str]]:
    """Read the guard from disk and say whether it can reach the module. Never imports it.

    Returns the verdict and the transitive module list it was derived from, so a failure
    can name the path rather than asserting a bare boolean.
    """
    seen: set[Path] = set()
    queue = [p for p in ENTRYPOINTS if p.is_file()]
    walked: list[str] = []
    while queue:
        path = queue.pop()
        if path in seen:
            continue
        seen.add(path)
        walked.append(str(path.relative_to(ROOT)))
        tree = ast.parse(path.read_bytes(), filename=str(path))
        names = local_imports(tree)
        if MODULE in names or spawns_the_script(tree):
            return True, walked
        for name in names:
            for directory in (path.parent, POLICY_DIR, HERE):
                candidate = directory / f"{name}.py"
                if candidate.is_file() and candidate not in seen:
                    queue.append(candidate)
    return False, sorted(walked)


BLOCKQUOTE = re.compile(r"(?m)^[ \t]*>[ \t]?")


def flat(text: str) -> str:
    """Strip markdown blockquote prefixes, then collapse whitespace.

    Every marker below is a SENTENCE, and these files hard-wrap at about 95 columns, so a
    sentence spans lines. Two artefacts of that layout are not content and must not be
    matched against: the wrap itself, and the `> ` that prefixes each line of §21d's
    provenance callout — the wrap in the callout falls inside "the guard does / NOT consult
    it", so raw matching failed and whitespace-only flattening left a stray `>` in the
    middle of the sentence.

    The tempting repair both times was to shorten the marker until it fitted on one line.
    That would weaken the assertion precisely in order to make it pass. Rewrapping a
    paragraph is a legitimate edit and must not break this gate; changing what it SAYS
    must.
    """
    return " ".join(BLOCKQUOTE.sub("", text).split())


# Each surface, and the exact sentence by which it declares the module unenforced. These are
# substrings of the live files, checked below to still be present — a marker that stopped
# matching would make this suite vacuously green, which is the failure mode of every
# string-matching gate in this repository.
NOT_ENFORCED_MARKERS = {
    # 🔴 Added after blind review. The docstring and the commit message both said "four
    # surfaces" while this dict held three — a checkable number stated without being
    # checked, inside the suite whose whole purpose is that prose about code must be
    # executable. Worse, the missing fourth was real: the DEC's own D-2 row carries the
    # same claim, was uncovered, and flipping it to "DOES enforce it" left the suite green.
    # That row already records "An earlier version of this row read 'and the guard enforces
    # it', which was false" — so the one surface with a history of stating this wrongly was
    # the one nothing watched.
    "governance/decisions/DEC-20260903-STOP-POLICY-AND-DECISION-AUTHORITY.md": (
        "The guard does NOT enforce it:",
        "the rule self-declares `NOT YET ENFORCED` and every push is refused",
    ),
    "framework/instruction/LEGEND_CORE.md": (
        "the guard does NOT consult it: every push is refused today",
        "NOT YET ENFORCED: `framework/scripts/push_authorization.py` states these conditions",
    ),
    "framework/scripts/guard_policy.py": (
        "it is deliberately NOT consulted here",
        "carries them and is NOT yet consulted here",
    ),
    "framework/scripts/push_authorization.py": (
        "SPECIFIED, NOT ENFORCED.",
        "Nothing consults this module",
    ),
}

# The surface an agent may not repair on its own, and why. Named here so the failure
# message can say it rather than leaving an agent to discover it by being refused.
RESERVED_SURFACE = "framework/instruction/LEGEND_CORE.md"


class TheDetectorMeasuresWhatItClaims(unittest.TestCase):
    """A detector nobody has seen fire is a detector nobody knows works."""

    def _tree(self, body: str) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        base = Path(tmp.name)
        (base / f"{MODULE}.py").write_text("CONDITIONS = ()\n", encoding="utf-8")
        (base / "middle.py").write_text(body, encoding="utf-8")
        (base / "entry.py").write_text("import middle\n", encoding="utf-8")
        return base

    def _consults(self, base: Path) -> bool:
        seen: set[Path] = set()
        queue = [base / "entry.py"]
        while queue:
            path = queue.pop()
            if path in seen:
                continue
            seen.add(path)
            names = local_imports(ast.parse(path.read_bytes(), filename=str(path)))
            if MODULE in names:
                return True
            for name in names:
                candidate = base / f"{name}.py"
                if candidate.is_file():
                    queue.append(candidate)
        return False

    def test_it_fires_on_a_direct_import(self) -> None:
        self.assertTrue(self._consults(self._tree(f"import {MODULE}\n")))

    def test_it_fires_on_a_from_import(self) -> None:
        self.assertTrue(self._consults(self._tree(f"from {MODULE} import CONDITIONS\n")))

    def test_it_fires_on_a_dynamic_import(self) -> None:
        """`importlib.import_module` leaves no `ast.Import` node at all."""
        self.assertTrue(self._consults(self._tree(
            f'import importlib\nm = importlib.import_module("{MODULE}")\n')))

    def test_it_fires_one_hop_away_and_not_only_at_the_entry_point(self) -> None:
        """The transitive case: `entry` imports `middle`, `middle` imports the module."""
        base = self._tree(f"import {MODULE}\n")
        self.assertEqual(f"import {MODULE}\n",
                         (base / "middle.py").read_text(encoding="utf-8"))
        self.assertTrue(self._consults(base))

    def test_it_does_not_fire_on_a_mention_in_a_comment_or_a_string(self) -> None:
        """The negative control, and the case the live tree is actually in.

        `guard_policy.py` names the module twice — once in a comment explaining why it is
        not consulted, once inside the denial message. A grep-based detector would call
        that "consults" and this whole suite would then be asserting the opposite of the
        truth with total confidence.
        """
        self.assertFalse(self._consults(self._tree(
            f'# {MODULE} states the conditions and is not consulted\n'
            f'MESSAGE = "see {MODULE}.py for the conditions"\n')))

    def test_the_detector_reads_bytes_and_never_imports_the_guard(self) -> None:
        """A stale `__pycache__` outside the repository must not be able to answer this.

        Checked with the AST, not with `assertNotIn("import guard_policy", source)`. The
        substring form was written first and failed immediately, on itself: the assertion
        string IS an occurrence of the text it proves absent. A negative proved by scanning
        a surface must exclude its own record from that surface, and the reliable way to do
        that is to stop scanning text and ask the parser instead.
        """
        imported = local_imports(ast.parse(Path(__file__).read_bytes(), filename=__file__))
        self.assertNotIn("guard_policy", imported)
        self.assertNotIn("pre_tool_use_guard", imported)
        self.assertNotIn(MODULE, imported)


class TheProseAgreesWithTheCode(unittest.TestCase):
    def setUp(self) -> None:
        self.consults, self.walked = guard_consults_push_authorization()

    def test_the_walk_reached_the_guard_and_did_not_stop_at_the_adapter(self) -> None:
        """Guards the derivation itself: a walk that visited one file proves nothing."""
        self.assertIn("framework/scripts/guard_policy.py", self.walked)
        self.assertIn("scripts/guard_bash_command.py", self.walked)
        self.assertGreater(len(self.walked), 3,
                           f"the import walk collapsed to {self.walked}")

    def test_every_surface_still_carries_a_declaration_to_check(self) -> None:
        """A marker that stopped matching would make the real check vacuously green."""
        for relative, markers in NOT_ENFORCED_MARKERS.items():
            text = flat((ROOT / relative).read_text(encoding="utf-8"))
            for marker in markers:
                with self.subTest(file=relative, marker=marker[:40]):
                    self.assertEqual(
                        not self.consults, flat(marker) in text,
                        f"{relative} and the code disagree about `{MODULE}`. The guard "
                        f"{'DOES' if self.consults else 'does NOT'} consult it (walked: "
                        f"{', '.join(self.walked)}), and the marker is "
                        f"{'present' if flat(marker) in text else 'absent'}.\n"
                        + (f"\n🔴 {RESERVED_SURFACE} is the RATIFIED body of §21d. If the "
                           "guard now consults the module, the fix to that file is an "
                           "OPERATOR re-ratification, not an edit to make this green."
                           if relative == RESERVED_SURFACE else ""))

    @staticmethod
    def decision(command: str) -> str:
        """The hook's answer for one command: `deny`, or `allow` when it says nothing.

        Silence IS the allow path — the hook exits 0 and writes no JSON at all, which the
        first version of this helper fed to `json.loads` and got a decode error rather
        than a verdict. An error is not a decision, and a test that cannot tell "allowed"
        from "the harness broke" cannot serve as anyone's positive control. The assignment
        travels in the ENVIRONMENT and never in the payload; put it in the payload and
        every answer here becomes `SESSION_ASSIGNMENT_UNDERIVABLE`, a true answer to a
        different question.
        """
        payload = json.dumps({"tool_name": "Bash", "cwd": str(ROOT),
                              "tool_input": {"command": command}})
        env = {**os.environ, "LEGEND_ASSIGNED_WORKTREE": str(ROOT)}
        env.pop("CLAUDE_PROJECT_DIR", None)
        result = subprocess.run(
            [sys.executable, str(HERE / "guard_bash_command.py")],
            input=payload, capture_output=True, text=True, env=env)
        out = result.stdout.strip()
        if not out:
            return "allow"
        return json.loads(out)["hookSpecificOutput"]["permissionDecision"]

    def test_the_consequence_holds_and_not_only_the_premise(self) -> None:
        """"…so every push is refused." That clause is behaviour; run it.

        The premise could stay true while the consequence broke — a refactor that moved
        the network branch, an allowlist entry, a spelling of `push` the dispatcher stopped
        reaching. Checking only the import graph would call that agreement.
        """
        for command in ("git push development main",
                        "git push",
                        "git push --force-with-lease development plan-x",
                        "git push origin main"):
            with self.subTest(command=command):
                self.assertEqual(
                    "deny", self.decision(command),
                    f"`{command}` was not denied, while {len(NOT_ENFORCED_MARKERS)} files "
                    "say every push is refused until the wiring lands")

    def test_a_command_that_is_not_a_push_is_still_allowed(self) -> None:
        """The positive control: `deny` must not be the answer to everything.

        Without it, a guard that denied every input — a crash path, a fail-closed default
        firing unconditionally — would satisfy all four push assertions perfectly.
        """
        for command in ("git status --porcelain", "git log --oneline -1"):
            with self.subTest(command=command):
                self.assertNotEqual(
                    "deny", self.decision(command),
                    "the guard denies an ordinary read-only command, so the push denials "
                    "above are evidence of nothing")


class TheModuleStillSpecifiesWhatItSaysItSpecifies(unittest.TestCase):
    """`push_authorization` is a specification. An empty one would satisfy every check."""

    def test_the_specification_has_not_been_hollowed_out(self) -> None:
        text = (POLICY_DIR / f"{MODULE}.py").read_text(encoding="utf-8")
        for condition in ("development", "fast-forward", "public_release_gate",
                          "push_authorizations.jsonl"):
            with self.subTest(condition=condition):
                self.assertIn(condition, text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
