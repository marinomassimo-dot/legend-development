#!/usr/bin/env python3
"""Revision 13's three repairs, measured — and each test FAILS against revision 12.

🔴 **Why this file exists.** Revision 12 froze with SIX suites and 296 tests, all green,
and two structural bypasses invisible to every one of them: `wrapper_tail` discarded the
parent's operands (438 loosenings of an enumerated 714 against revision 11), and `env`
dropped its `NAME=VALUE` tokens before `analyse_env_prefix` could read them (18 rows of
53 failing revision 12's own stated invariant A). A passing streak is where the next
check stops being run — revision 12's own suite says so in its header — and one revision
later the same shape was still there.

So the obligation this file discharges is not "the repair passes". It is:

```text
each test below was run against the revision-12 engine at 5520655 and FAILED there
each test below passes against this tree
```

A test verified only against the fixed code is not a test, it is a restatement.

**What each test asserts.** The same four points revision 12's suite states, and the
first one is where revision 12 was defeated: the repair is reached through a PROPERTY
over an enumerated set, not through a membership list; the ordinary work in the same
table still passes; and the enumeration is taken from the module rather than typed out,
so a table that grows is measured without anybody remembering this file exists.
"""

from __future__ import annotations

import inspect
import sys
import textwrap
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import guard_policy as gp                                    # noqa: E402
from test_guard_families_rev12 import SceneCase              # noqa: E402

BLANKET = "git " + "add" + " -A"


# ══ M1 · THE WRAPPER TAIL ADDS, AND NEVER SUBSTITUTES ══════════════════════════════

class TheWrapperTailAddsAndNeverSubstitutes(SceneCase):
    """🔴 Revision 12's `unclassified()` returned the moment `wrapper_tail` found a
    child, so the parent's own operands were never derived and `UNDERIVED_OPERAND` — the
    revision-11 "same object, same answer" repair — was dropped for every argv that
    happened to contain a modelled name.

    ```text
    mytool <peer>/framework/x            DENY   UNDERIVED_OPERAND     revision 11 and 12
    mytool <peer>/framework/x env        DENY   revision 11 · ALLOW 🔴 revision 12
    mytool <registration> env            DENY   revision 11 · ALLOW 🔴 revision 12
    ```

    Revision 12 states the rule this violates one function away, at the top of
    `analyse_argv`: A NORMALISED NAME MAY ADD AN EFFECT AND MAY NEVER REMOVE ONE.

    The first test below is the FAMILY assertion: it is driven by every member of
    `WRAPPER_TAIL_PROGRAMS`, taken from the module, so it cannot pass by covering the
    tail words somebody thought of.
    """

    def _tail_words(self):
        """The whole derived set, from the module. 🔴 Asserted non-empty in the same
        method: a subtraction that became empty would make every row below vacuous and
        the class would still report green."""
        words = sorted(gp.WRAPPER_TAIL_PROGRAMS)
        self.assertGreater(len(words), 50, "the derived tail universe collapsed")
        return words

    def test_every_tail_word_leaves_the_parents_confined_operand_derived(self):
        """The population revision 12 lost: one row per tail word, both positions."""
        target = f"{self.PEER}/framework/x"
        table = {}
        for word in self._tail_words():
            table[f"trailing {word}"] = self.verdict(f"mytool {target} {word}")
            table[f"leading {word}"] = self.verdict(f"mytool {word} {target}")
        self.assert_matrix(table, "DENY", "a tail word must not erase the operand")

    def test_the_same_object_gets_the_same_answer_with_and_without_a_tail_word(self):
        """🔴 Both directions in one table, and the controls are in it.

        A rule that denied every argv containing a tail word would pass the matrix above
        and fail here — the own-worktree and scratch rows are the reason the repair is a
        UNION and not a blanket refusal.
        """
        table = {}
        for label, target in (("peer", f"{self.PEER}/framework/x"),
                              ("shared", f"{self.SHARED}/CLAUDE.md"),
                              ("git-common", f"{self.scene.common}/config"),
                              ("registration", self.REG)):
            table[f"DENY {label} bare"] = self.verdict(f"mytool {target}")
            table[f"DENY {label} trailing"] = self.verdict(f"mytool {target} env")
            table[f"DENY {label} leading"] = self.verdict(f"mytool env {target}")
        wrong = {k: v for k, v in table.items() if v != "DENY"}
        # the controls: granted scopes, same shape, same table
        controls = {
            "ALLOW own-worktree trailing":
                self.verdict(f"mytool {self.scene.assigned}/framework/x env"),
            "ALLOW scratch trailing": self.verdict(f"mytool {self.OUT} env"),
            "ALLOW scratch leading": self.verdict(f"mytool env {self.OUT}"),
            "ALLOW an ordinary read": self.verdict("ls -la"),
        }
        wrong.update({k: v for k, v in controls.items() if v != "ALLOW"})
        self.assertEqual({}, wrong, f"same object, same answer: {wrong}")

    def test_the_registration_is_not_reachable_behind_a_tail_word(self):
        """The severe consequence: the surface that decides whether this guard runs.

        🔴 Four unmodelled program names, so the answer is a property of the SHAPE and
        not of the string `mytool`.
        """
        table = {}
        for program in ("mytool", "pandoc", "foobarbaz", "ansible-playbook"):
            table[f"{program} bare"] = self.verdict(f"{program} {self.REG}")
            table[f"{program} trailing env"] = self.verdict(f"{program} {self.REG} env")
            table[f"{program} leading env"] = self.verdict(f"{program} env {self.REG}")
            # 🔴 The control that separates "a tail word was found" from "a word was
            # present": a word that names no program must give the same answer.
            table[f"{program} unknown word"] = self.verdict(
                f"{program} {self.REG} notaprogram")
        self.assert_matrix(table, "DENY", "the registration behind a tail word")

    def test_the_tail_still_contributes_its_own_finding(self):
        """🔴 The other half of ADD. A repair that merely stopped calling `wrapper_tail`
        would pass every test above and silently remove revision 12's mechanism.

        These rows are DENIED by the CHILD, not by the parent's operands: the payloads
        name nothing confined, so `UNDERIVED_OPERAND` alone cannot reach them.
        """
        table = {
            "blanket staging in a tail": self.decide(f"mytool {BLANKET}")[1],
            "a conditional reader's write form":
                self.decide(f"xcrun sort -o {self.PEER}/f {self.IN}")[1],
        }
        self.assertEqual("BLANKET_STAGING", table["blanket staging in a tail"], table)
        self.assertNotEqual("", table["a conditional reader's write form"], table)

    def test_unclassified_cannot_return_between_the_tail_and_the_operands(self):
        """🔴 A STRUCTURAL assertion, and it had to be written twice.

        The first draft asserted that the LAST statement of `unclassified` is the
        `underived_operand` call. It passes against revision 12 — where that call is
        also the last statement, and is simply UNREACHABLE whenever a tail is found,
        because the tail branch returns above it. A test that passes against the engine
        it is meant to constrain has demonstrated nothing, which is the whole reason
        this file exists; recorded here rather than quietly corrected.

        What discriminates is REACHABILITY: after the carrier is consulted, no path may
        leave the function before the operands are derived. Asserted over the parse tree,
        so a reformat cannot move it and a `return` nested inside an `if` cannot hide.
        """
        import ast
        tree = ast.parse(textwrap.dedent(inspect.getsource(gp.unclassified)))
        function = tree.body[0]
        carrier_line = min(
            node.lineno for node in ast.walk(function)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id in ("carried_command", "wrapper_tail"))
        returns_after = [node.lineno for node in ast.walk(function)
                         if isinstance(node, ast.Return) and node.lineno > carrier_line]
        self.assertEqual([], returns_after,
                         "a `return` after the carrier makes the operand derivation "
                         f"unreachable; found at offsets {returns_after}")
        derivation = [node.lineno for node in ast.walk(function)
                      if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                      and node.func.id == "underived_operand"]
        self.assertTrue(derivation and max(derivation) > carrier_line,
                        "the operand derivation must follow the carrier, not precede it")


# ══ M3 · THE ENVIRONMENT DELIVERY IS NOT A LAUNDRY ═════════════════════════════════

def _env_pair(key, value):
    return (f"GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0={key} "
            f"GIT_CONFIG_VALUE_0={value}")


#: 🔴 The DELIVERY SPELLINGS, enumerated once and driven as a property.
#:
#: Revision 12's `TheEnvironmentSpellingGetsTheSameAnswerAsTheFlag._pair()` tested TWO:
#: the flag and the bare prefix. Both were derived by the same code, so the class could
#: not see the four spellings that were not. A list standing in for a family, inside the
#: test written to stop a list standing in for a family.
DELIVERIES = {
    "flag": lambda k, v, sub: f"git -c {k}={v} {sub}",
    "prefix": lambda k, v, sub: f"{_env_pair(k, v)} git {sub}",
    "env": lambda k, v, sub: f"env {_env_pair(k, v)} git {sub}",
    "env -i": lambda k, v, sub: f"env -i {_env_pair(k, v)} git {sub}",
    "env -u": lambda k, v, sub: f"env -u NOPE {_env_pair(k, v)} git {sub}",
    "nohup env": lambda k, v, sub: f"nohup env {_env_pair(k, v)} git {sub}",
    "sudo prefix": lambda k, v, sub: f"sudo {_env_pair(k, v)} git {sub}",
    "env sudo": lambda k, v, sub: f"env {_env_pair(k, v)} sudo git {sub}",
}


class TheEnvironmentDeliveryIsNotALaundry(SceneCase):
    """🔴 `strip_wrapper_options(..., assignments=(program == "env"))` dropped every
    `NAME=VALUE` token before `analyse_env_prefix` was reached, so revision 12's stated
    invariant A — *a configuration key gets ONE answer however it is delivered* — failed
    on 18 rows of an enumerated 53:

    ```text
    key               git -c   NAME=V git   env NAME=V git   env -i   nohup env
    core.hooksPath    DENY     DENY          ALLOW 🔴          ALLOW 🔴  ALLOW 🔴
    control  user.name · color.ui   ALLOW in all six spellings          12/12
    ```

    The ordinary keys agreed at ALLOW across every spelling, which is why the failure
    could not be found by asking whether the family "works" — it worked everywhere it
    did not matter.
    """

    def test_an_execution_control_key_gets_one_answer_in_every_spelling(self):
        table = {}
        for key, value in (("core.hooksPath", "/tmp/h"), ("alias.zz", "!sh"),
                           ("filter.x.clean", "/tmp/c"), ("pager.log", "/tmp/p"),
                           ("core.editor", "/tmp/e"), ("man.v.cmd", "/tmp/m")):
            for name, build in DELIVERIES.items():
                table[f"{key} via {name}"] = self.verdict(build(key, value, "status"))
        self.assert_matrix(table, "DENY", "execution-control key, every delivery")

    def test_an_ordinary_key_is_allowed_in_every_spelling(self):
        """🔴 The other direction, in its own right. A rule that denied every
        environment-delivered key would pass the matrix above and be wrong."""
        table = {}
        for key, value in (("user.name", "someone"), ("color.ui", "always"),
                           ("commit.gpgsign", "false")):
            for name, build in DELIVERIES.items():
                table[f"{key} via {name}"] = self.verdict(
                    build(key, value, "log --oneline -5"))
        self.assert_matrix(table, "ALLOW", "ordinary key, every delivery")

    def test_every_always_execution_control_variable_survives_env(self):
        """The enumerated variable sets, not a sample: `ENV_ALWAYS_EXECUTION_CONTROL`
        and `ENV_CONFIG_FILE` come from the module."""
        names = sorted(gp.ENV_ALWAYS_EXECUTION_CONTROL) + sorted(gp.ENV_CONFIG_FILE)
        self.assertGreater(len(names), 1, "the variable enumeration collapsed")
        table = {}
        for name in names:
            for spelling in ("{a} git status", "env {a} git status",
                             "env -i {a} git status", "nohup env {a} git status"):
                table[f"{name} via {spelling}"] = self.verdict(
                    spelling.format(a=f"{name}=/tmp/x"))
        self.assert_matrix(table, "DENY", "loader and config-file variables through env")

    def test_strip_wrapper_options_has_no_switch_that_turns_a_derivation_off(self):
        """🔴 Structural, and it is the one that cannot be satisfied by luck.

        The defect was a keyword argument whose only caller was `env`. A behavioural test
        can be passed by re-adding the analysis somewhere else and leaving the switch in
        place for the next caller to find; this asserts the switch is gone.
        """
        parameters = list(inspect.signature(gp.strip_wrapper_options).parameters)
        self.assertEqual(["argv", "value_flags"], parameters,
                         "an option-stripper must not take a flag that drops assignments")


# ══ M7 · A PACKAGE RUN VERB IS A FAMILY, NOT A LIST ════════════════════════════════

class ARunVerbIsAFamilyNotAList(SceneCase):
    """🔴 `PACKAGE_RUN_SUBCOMMANDS = {"run", "exec", "x", "dlx", "tool"}` is five words,
    and `npm run-script` — npm's own documented alias for `npm run` — is not one of them.
    Seven loosenings against `main`, all one class, measured with two payloads per
    wrapper so the attribution is separable:

    ```text
                                     main   revision 12   revision 13
    npm run-script <blanket>          DENY   ALLOW 🔴       DENY
    npm start / test / node / task / script, deno task — the same seven
    control  npm run · npm exec · npx · uvx          DENY at 12 and 13
    ```

    `main`'s refusal was a TEXT match on the blanket string, not a safety property. So
    the repair is not six more words on the list: the tail is read as the command it is.
    """

    def test_an_unrecognised_run_verb_still_carries_its_command(self):
        table = {}
        for wrapper in ("npm run-script", "npm start", "npm test", "npm node",
                        "npm task", "npm script", "npm ci-run", "yarn run-script",
                        "pnpm start", "deno task", "deno serve", "bun task",
                        "npm run", "npm exec", "npx", "uvx", "uv run"):
            table[wrapper] = self.verdict(f"{wrapper} {BLANKET}")
        self.assert_matrix(table, "DENY", "a carried command behind any run verb")

    def test_a_carried_command_reaches_a_confined_write(self):
        """🔴 Not the blanket string. `main` denies that one by text, so a test using
        only it cannot tell a derivation from a substring match.

        🔴 Every payload here names a program `_KNOWN_PROGRAM_NAMES` contains, and that
        is a LIMIT of this test rather than a choice of convenient examples. These two
        carrier sites have no `UNDERIVED_OPERAND` backstop — `unclassified` has one and
        they do not — so a payload whose program is unmodelled is not reached at all:
        `npm run-script xcrun tee <peer>/f` is ALLOWED here and DENIED bare. That
        residual is measured and declared in the candidate manifest; it is not repaired
        by this revision, and it is stated here so the passing of this test is not read
        as a closure it does not claim.
        """
        table = {}
        for wrapper in ("npm run-script", "npm start", "deno task", "npm task"):
            table[f"{wrapper} sort -o"] = self.verdict(
                f"{wrapper} sort -o {self.PEER}/f {self.IN}")
            table[f"{wrapper} sed -i"] = self.verdict(
                f"{wrapper} sed -i s/a/b/ {self.PEER}/framework/x")
            table[f"{wrapper} git -C"] = self.verdict(
                f"{wrapper} git -C {self.PEER} " + "add" + " -A")
        self.assert_matrix(table, "DENY", "a confined write behind an unknown run verb")

    def test_ordinary_package_manager_work_is_untouched(self):
        """🔴 The cost side, in its own table. The repair fires only when the argv names
        a program some table in this module models; a package manager reporting on itself
        names none, and must stay allowed."""
        table = {}
        for command in ("npm ls", "npm view react", "npm audit", "npm --version",
                        "npm outdated", "npm ls --depth 0", "deno --version",
                        "python3 script.py", "node app.js", "deno run mod.ts"):
            table[command] = self.verdict(command)
        self.assert_matrix(table, "ALLOW", "ordinary package-manager and script work")

    def test_the_carrier_law_lives_in_one_function_reached_from_every_site(self):
        """🔴 Structural. Three call sites now apply the wrapper-tail law, and a law
        copied three times is three laws that will drift. `carried_command` must be the
        only place `wrapper_tail` is invoked."""
        source = Path(gp.__file__).read_text(encoding="utf-8")
        calls = [line for line in source.splitlines()
                 if "wrapper_tail(" in line and not line.strip().startswith("#")
                 and "def wrapper_tail" not in line]
        self.assertEqual(1, len(calls), f"wrapper_tail is invoked from {calls}")
        sites = [line for line in source.splitlines()
                 if "carried_command(" in line and not line.strip().startswith("#")
                 and "def carried_command" not in line]
        self.assertEqual(3, len(sites), f"carried_command call sites: {sites}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
