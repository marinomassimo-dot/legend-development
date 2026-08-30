#!/usr/bin/env python3
"""Revision 12's families, measured — the suite `guard_policy.py` says exists.

🔴 **Why this file had to be written before the revision could be frozen.**

The revision-12 working tree arrived carrying 592 new lines in `guard_policy.py` and 112
in `guard_revision.py`, and TEN suites reporting green. None of the ten mentioned
`analyse_env_prefix`, `wrapper_tail`, `READER_WRITE_MODEL`, `normalise_program`,
`PURE_READERS`, `EXECUTION_CONTROL_KEY_SUFFIXES` or `PACKAGE_RUN_SUBCOMMANDS`. Measured,
not inferred: `grep -c` over every `test_*.py` in this repository returned 0 for all
seven names. The suites passed because not one of them looked at the revision.

Worse, two docstrings inside `guard_policy.py` already asserted that
`test_guard_families_rev12.py` "asserts the derivation is non-empty" and "asserts it is
non-empty and excludes the readers". The file did not exist. Those were normative claims
about a test nobody had written, committed into the engine they were claiming to
constrain — the same shape of defect as revision 11's declared-debt row that stood beside
a hole, one level further in.

So: a passing streak is where the next check stops being run, and a high score is
fidelity, never coverage.

---

**What this suite is, and is not.** Every family below was defeated at revision 11 by
enumerating a population revision 11 did not choose. This suite does not re-enumerate
those populations to prove they are now closed — most of them CANNOT be closed, and
where that is so it is said in the test's own docstring rather than implied by its
passing. What each test asserts is narrower and checkable:

  1 · the repair FIRES on the routes that were open, and
  2 · the repair is REACHED THROUGH A PROPERTY rather than a membership list, so that a
      spelling nobody enumerated gets the same answer, and
  3 · the derivation that feeds it cannot silently become empty, and
  4 · the ordinary work in the same table still passes.

Point 4 is not decoration. Four of these families are repaired by refusing more, and a
repair that refuses more is one bad predicate away from refusing the reader's real work.
Every matrix here carries its controls in the SAME table as its measurement, because a
control reported separately is a control that stops being read.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import effect_model as em      # noqa: E402
import guard_policy as gp      # noqa: E402
import repo_topology as rt     # noqa: E402
import runtime_config as rc    # noqa: E402


def git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


class Scene:
    """A shared checkout, an assigned worktree, a peer, and a HOME of its own.

    🔴 The HOME is the scene's, never the operator's — the same rule revision 11's suite
    states. Asking the guard about this machine's real `~/.claude/settings.json` would
    put the operator's layout into the assertions, and would make an answer depend on
    whether a Codex happens to be installed here.
    """

    def __init__(self):
        self.base = Path(tempfile.mkdtemp(prefix="rev12-families-"))
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
        (self.assigned / "framework").mkdir(parents=True, exist_ok=True)
        self.common = Path(rt.of(str(self.assigned)).git_common_dir)

        self.home = self.base / "home"
        (self.home / ".claude").mkdir(parents=True)
        (self.home / ".codex").mkdir(parents=True)
        (self.home / ".claude" / "settings.json").write_text("{}\n")
        (self.home / ".codex" / "config.toml").write_text("# x\n")

        #: An ordinary scratch file, so a "reads a file" case has something to read and a
        #: write case has a benign source that is NOT itself a protected object.
        self.scratch = self.base / "scratch"
        self.scratch.mkdir()
        (self.scratch / "in").write_text("x\n")

        self.env = {"HOME": str(self.home),
                    "CLAUDE_CONFIG_DIR": str(self.home / ".claude"),
                    "CODEX_HOME": str(self.home / ".codex")}

    def close(self):
        shutil.rmtree(self.base, ignore_errors=True)


class SceneCase(unittest.TestCase):
    """One scene per class, with the runtime-config surface pointed at it."""

    @classmethod
    def setUpClass(cls):
        cls.scene = Scene()
        cls._saved = {k: os.environ.get(k) for k in
                      ("HOME", "CLAUDE_CONFIG_DIR", "CODEX_HOME", "CLAUDE_PROJECT_DIR")}
        os.environ.update(cls.scene.env)
        os.environ.pop("CLAUDE_PROJECT_DIR", None)
        rc.reset()
        rt.reset()

    @classmethod
    def tearDownClass(cls):
        for key, value in cls._saved.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        cls.scene.close()
        rc.reset()
        rt.reset()

    def decide(self, command, cwd=None):
        rt.reset()
        assigned = str(self.scene.assigned)
        outcome, _reason, code, _f = gp.adjudicate(
            command, cwd=cwd or assigned, repo_root=assigned, assigned=assigned)
        return ("ALLOW" if outcome == gp.ALLOWED else "DENY"), (code or "")

    def verdict(self, command, cwd=None):
        return self.decide(command, cwd)[0]

    def assert_matrix(self, table, expected, label):
        """Assert a whole enumeration at once, naming every deviant CELL.

        🔴 The failure message carries the cells and their verdicts. A matrix assertion
        that reported only a ratio would tell its reader the number they already
        suspected and none of the rows behind it.
        """
        wrong = {name: got for name, got in table.items() if got != expected}
        self.assertEqual({}, wrong, f"{label}: these cells answered wrongly: {wrong}")

    # Convenience path spellings, so a case reads as the shape it is testing.
    @property
    def PEER(self):
        return str(self.scene.peer)

    @property
    def SHARED(self):
        return str(self.scene.shared)

    @property
    def REG(self):
        return str(self.scene.home / ".claude" / "settings.json")

    @property
    def IN(self):
        return str(self.scene.scratch / "in")

    @property
    def OUT(self):
        return str(self.scene.scratch / "out")


# ══ A · THE DERIVATIONS CANNOT SILENTLY EMPTY ══════════════════════════════════════

class TheDerivedSetsCannotSilentlyBecomeEmpty(unittest.TestCase):
    """🔴 Two of revision 12's repairs are DERIVED sets, and a derived set is exactly the
    kind of control that can stop firing without anything failing.

    `WRAPPER_TAIL_PROGRAMS` is a subtraction and `_KNOWN_PROGRAM_NAMES` is a union over
    tables elsewhere in the module. Rename a table, and the union quietly narrows;
    subtract the wrong side, and the difference is empty. In both cases every existing
    suite still passes — the guard simply stops catching a family, in the ALLOW
    direction, which is the direction nobody notices.

    These are the assertions `guard_policy.py`'s own docstrings promise a reader.
    """

    def test_the_program_name_universe_is_large_and_carries_the_names_it_normalises_onto(self):
        self.assertGreater(len(gp._KNOWN_PROGRAM_NAMES), 100)
        # The names the version-suffix rule must be able to land on. Each is a program
        # some table keys on, and each was a measured bypass at revision 11.
        for name in ("python3", "python", "perl", "node", "ruby", "bash", "sh", "git"):
            self.assertIn(name, gp._KNOWN_PROGRAM_NAMES, name)

    def test_the_wrapper_tail_universe_is_non_empty_and_excludes_pure_readers(self):
        self.assertGreater(len(gp.WRAPPER_TAIL_PROGRAMS), 50)
        overlap = gp.WRAPPER_TAIL_PROGRAMS & gp.PURE_READERS
        self.assertEqual(frozenset(), overlap,
                         f"a pure reader must never make a wrapper tail: {overlap}")

    def test_a_conditional_reader_is_still_reachable_through_a_wrapper(self):
        """🔴 The subtraction is from `PURE_READERS`, not from `KNOWN_READERS`, and the
        difference is the whole point: `xcrun sort -o <peer>/f in` must still reach
        `sort`. Subtracting the union instead would leave every conditional reader
        invisible inside an unmodelled wrapper, and no other test in this repository
        would notice.
        """
        for name in gp.READER_WRITE_MODEL:
            self.assertIn(name, gp.WRAPPER_TAIL_PROGRAMS, name)

    def test_the_reader_split_partitions_the_old_set(self):
        """`KNOWN_READERS` is kept as the union so the older call sites keep one name.
        If the two halves ever overlap, a program would be exempted BEFORE its argv is
        derived — which is the revision-11 defect this split repairs."""
        self.assertEqual(gp.KNOWN_READERS,
                         gp.PURE_READERS | frozenset(gp.READER_WRITE_MODEL))
        self.assertEqual(frozenset(),
                         gp.PURE_READERS & frozenset(gp.READER_WRITE_MODEL))

    def test_every_conditional_reader_has_a_callable_model(self):
        for name, model in gp.READER_WRITE_MODEL.items():
            self.assertTrue(callable(model), name)
            # A model that derives a target from an empty argv would fire on every
            # invocation, including a plain read.
            self.assertEqual([], [t for t in model([name]) if t], name)


# ══ B · ENVIRONMENT INDIRECTION — INVARIANT A AT ITS SHARPEST POINT ════════════════

class TheEnvironmentSpellingGetsTheSameAnswerAsTheFlag(SceneCase):
    """🔴 D4. `SAME OBJECT → SAME AUTHORIZATION ANSWER` is the invariant revision 11
    published, and revision 11 failed it here:

    ```text
    git -c core.hooksPath=<h> commit             DENY   RUNTIME_CONFIG
    GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.hooksPath \\
      GIT_CONFIG_VALUE_0=<h> git commit          ALLOW  🔴  verified, hook fired
    ```

    The parser had seen the prefixes since revision 8 and threw them away. This class
    asserts the two spellings AGREE, which is a stronger and more durable claim than
    asserting the second denies: it cannot be satisfied by a rule that denies everything.
    """

    def _pair(self, key, value):
        flag = f"git -c {key}={value} commit -m x"
        env = (f"GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0={key} "
               f"GIT_CONFIG_VALUE_0={value} git commit -m x")
        return self.verdict(flag), self.verdict(env)

    def test_a_config_key_gets_one_answer_however_it_is_delivered(self):
        cases = {
            "core.hooksPath": "/tmp/h",
            "alias.zz": "!sh",
            "core.editor": "/tmp/e",
            "core.pager": "/tmp/p",
            "filter.x.clean": "/tmp/c",
            "man.v.cmd": "/tmp/m",
            "pager.log": "/tmp/p",
            # 🔴 The other direction, and it must be in the same table. A key that is
            # NOT execution control must agree too — at ALLOW. A rule that denied every
            # environment-delivered key would pass every row above and be wrong.
            "user.name": "someone",
            "color.ui": "always",
        }
        disagreed = {}
        for key, value in cases.items():
            flag, env = self._pair(key, value)
            if flag != env:
                disagreed[key] = f"-c={flag} env={env}"
        self.assertEqual({}, disagreed,
                         f"the two spellings must agree: {disagreed}")

    def test_the_execution_control_keys_deny_in_both_spellings(self):
        table = {}
        for key in ("core.hooksPath", "alias.zz", "core.editor", "man.v.cmd",
                    "pager.log", "filter.x.clean"):
            flag, env = self._pair(key, "/tmp/x")
            table[f"-c {key}"] = flag
            table[f"env {key}"] = env
        self.assert_matrix(table, "DENY", "execution-control keys, both spellings")

    def test_an_ordinary_key_is_allowed_in_both_spellings(self):
        table = {}
        for key, value in (("user.name", "someone"), ("color.ui", "always")):
            flag = f"git -c {key}={value} log --oneline -5"
            env = (f"GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0={key} "
                   f"GIT_CONFIG_VALUE_0={value} git log --oneline -5")
            table[f"-c {key}"] = self.verdict(flag)
            table[f"env {key}"] = self.verdict(env)
        self.assert_matrix(table, "ALLOW", "ordinary keys, both spellings")

    def test_a_configuration_file_the_command_names_is_execution_control(self):
        table = {name: self.verdict(f"{name}={self.IN} git commit -m x")
                 for name in gp.ENV_CONFIG_FILE}
        self.assert_matrix(table, "DENY", "actor-chosen git config file")

    def test_loader_injection_denies_whatever_its_value(self):
        """No benign value exists for these in a guarded shell, so the
        actor-controlled test is deliberately NOT applied — asserted here so that
        relaxing it later fails a test rather than passing quietly."""
        table = {}
        for name in gp.ENV_ALWAYS_EXECUTION_CONTROL:
            table[f"{name} bare"] = self.verdict(f"{name}=libx git status")
            table[f"{name} path"] = self.verdict(f"{name}=/tmp/x.so git status")
        self.assert_matrix(table, "DENY", "loader injection")

    def test_an_actor_controlled_program_variable_denies_and_a_bare_word_does_not(self):
        """🔴 The discriminator, and the reason this family does not close ordinary work.

        `GIT_PAGER=cat git log --oneline -5` is a COMMITTED positive control of this
        repository. `cat` is a bare name resolved through `PATH`; `/tmp/evil` is a file
        the actor just wrote. Both rows are here so neither can be traded for the other.
        """
        actor_controlled = {
            "GIT_EDITOR=/tmp/e": self.verdict("GIT_EDITOR=/tmp/e git commit"),
            "GIT_EXTERNAL_DIFF=/tmp/d": self.verdict(
                "GIT_EXTERNAL_DIFF=/tmp/d git diff"),
            "GIT_SSH_COMMAND=./s": self.verdict("GIT_SSH_COMMAND=./s git fetch"),
            "BASH_ENV=~/e": self.verdict("BASH_ENV=~/e bash /tmp/s.sh"),
        }
        self.assert_matrix(actor_controlled, "DENY", "actor-controlled program variable")

        bare_word = {
            "GIT_PAGER=cat": self.verdict("GIT_PAGER=cat git log --oneline -5"),
            "GIT_EDITOR=vi": self.verdict("GIT_EDITOR=vi git commit"),
            "PAGER=less": self.verdict("PAGER=less git log"),
        }
        self.assert_matrix(bare_word, "ALLOW", "bare-word program name")

    def test_an_unenumerated_variable_is_judged_by_its_SHAPE(self):
        """🔴 This is what stops the environment family being another list. None of these
        names is in `ENV_EXECUTION_CONTROL`; each is caught by `ENV_CONTROL_SHAPE`.

        The family is OPEN and is declared so in `guard_policy.py`: any program may read
        any variable, and no enumeration can be complete. What is asserted here is only
        that a name nobody listed, whose SHAPE says its value is a program, is judged.
        """
        table = {name: self.verdict(f"{name}=/tmp/x sometool")
                 for name in ("MYTOOL_COMMAND", "FOO_CMD", "SOMETHING_EDITOR",
                              "APP_LAUNCHER", "X_HOOK", "WEIRD_BROWSER",
                              "GIT_MYTHING_COMMAND", "TOOL_PROGRAM")}
        self.assert_matrix(table, "DENY", "unenumerated but program-shaped variable")

    def test_an_ordinary_assignment_prefix_is_left_alone(self):
        """The declared boundary. A rule that denied every unrecognised assignment would
        refuse `FOO=1 make` and be removed within a day — so it is asserted, not assumed.
        """
        table = {c: self.verdict(c) for c in (
            "FOO=1 make",
            "LANG=C sort " + str(Path(tempfile.gettempdir()) / "nothing"),
            "DEBUG=true git status",
            "TZ=UTC git log --oneline -5",
            "COUNT=3 echo hi",
        )}
        self.assert_matrix(table, "ALLOW", "ordinary assignment prefix")


# ══ C · A VERSION SUFFIX IS NOT A DIFFERENT PROGRAM ════════════════════════════════

class AVersionSuffixIsNotADifferentProgram(SceneCase):
    """🔴 D3. Revision 11 handled the DIRECTORY and left the VERSION, which defeated the
    Family-II repair and the `-m` repair at once — the list was right and the KEY was
    wrong. Repaired by normalisation rather than by fourteen more entries.
    """

    BODY = "open('framework/x','w').write('x')"

    def test_normalisation_is_a_pure_function_with_the_documented_answers(self):
        cases = {
            "python3.12": "python3", "python3.9": "python3", "python3": "python3",
            "/usr/bin/python3.12": "python3", "./python3.12": "python3",
            "perl5.34": "perl", "nodejs": "node", "pypy3": "python3",
            "python3m": "python3",
            # 🔴 A name that is not a program keeps its own spelling. A rule that
            # invented a program out of a version string would classify an operand as
            # an interpreter — so `report2` and `file1` must survive untouched.
            "report2": "report2", "file1": "file1", "x86": "x86",
            "3.12": "3.12",
        }
        wrong = {k: gp.normalise_program(k) for k in cases
                 if gp.normalise_program(k) != cases[k]}
        self.assertEqual({}, wrong, f"normalisation moved these wrongly: {wrong}")

    def test_the_versioned_spelling_denies_wherever_the_bare_one_does(self):
        """The matrix carries its own controls: the bare, absolute and relative
        spellings sit in the same table as the versioned ones."""
        table = {}
        for spelling in ("python3", "/usr/bin/python3", "./python3",   # controls
                         "python3.12", "python3.9", "python3.11"):     # the repair
            table[f"{spelling} -c"] = self.verdict(f'{spelling} -c "{self.BODY}"')
            table[f"{spelling} heredoc"] = self.verdict(
                f"{spelling} - <<PY\n{self.BODY}\nPY")
            table[f"{spelling} -m gzip"] = self.verdict(
                f"{spelling} -m gzip {self.REG}")
        self.assert_matrix(table, "DENY", "python spellings × forms")

    def test_the_other_interpreters_normalise_too(self):
        table = {
            "perl5.34 -e": self.verdict('perl5.34 -e "open(F,\'>\',\'framework/x\');"'),
            "perl -e": self.verdict('perl -e "open(F,\'>\',\'framework/x\');"'),
            "nodejs -e": self.verdict(
                'nodejs -e "require(\'fs\').writeFileSync(\'framework/x\',\'x\')"'),
            "node -e": self.verdict(
                'node -e "require(\'fs\').writeFileSync(\'framework/x\',\'x\')"'),
        }
        self.assert_matrix(table, "DENY", "versioned interpreters")

    def test_the_alternate_shells_are_a_declared_list_extension_and_they_deny(self):
        """🔴 `tcsh` and `csh` are NOT version spellings of anything — they are separate
        shells with their own `-c`, so normalisation could not reach them and the list
        was extended instead. The shell family is one of the few genuinely closed sets
        in the module, which is what makes extending it defensible HERE and not the
        answer for `TRANSPARENT_WRAPPERS`.
        """
        table = {sh: self.verdict(f"{sh} -c 'git add -A'")
                 for sh in ("sh", "bash", "zsh", "tcsh", "csh")}
        self.assert_matrix(table, "DENY", "shell -c blanket staging")

    def test_a_versioned_reader_is_still_a_reader(self):
        """The repair must not refuse ordinary work: reading through a versioned
        interpreter is not a write."""
        table = {c: self.verdict(c) for c in (
            'python3.12 -c "print(1+1)"',
            'python3.12 -c "print(open(\'framework/x\').read())"',
            "python3.12 --version",
            "perl5.34 --version",
        )}
        self.assert_matrix(table, "ALLOW", "versioned interpreter reading")


# ══ D · THE WRAPPER TAIL ═══════════════════════════════════════════════════════════

class AnUnmodelledWrapperDoesNotLaunderItsChild(SceneCase):
    """🔴 D2. `TRANSPARENT_WRAPPERS` was a list, and 42 of 60 enumerated exec-wrappers
    allowed a blanket-staging child.

    Adding eight names would have closed eight commands. The FAMILY is *a program this
    policy has no model for, whose argv contains a command this policy DOES model*, and
    that is derivable from the text without knowing the wrapper — so the tail is
    re-analysed from the first token naming a modelled, non-reading program.

    🔴 **What is NOT claimed:** that every wrapper is now caught. A wrapper that
    TRANSFORMS its child — reading it from a file, decoding it, or taking it on stdin —
    carries no modelled name in its argv and is not reached by this rule. That is a
    declared fence, and `unclassified`'s `UNDERIVED_STDIN_CHILD` branch is what covers
    the stdin half of it.
    """

    def test_an_unknown_wrapper_carrying_a_known_command_is_re_analysed(self):
        table = {w: self.verdict(f"{w} git add -A") for w in (
            "xcrun", "someunknowntool", "script", "screen", "osascript",
            "mywrapper", "notatool", "runner")}
        # The controls: wrappers that were ALREADY modelled must not regress.
        for w in ("nohup", "env", "timeout 5", "uvx", "npm exec"):
            table[f"CONTROL {w}"] = self.verdict(f"{w} git add -A")
        self.assert_matrix(table, "DENY", "unmodelled wrapper carrying git add -A")

    def test_the_tail_is_found_past_the_wrappers_own_options(self):
        """`script -q /dev/null git add -A` — the child does not sit at position 1."""
        table = {c: self.verdict(c) for c in (
            "script -q /dev/null git add -A",
            "screen -dm git add -A",
            "xcrun --sdk macosx git add -A",
            "someunknowntool --flag --other=1 git add -A",
        )}
        self.assert_matrix(table, "DENY", "wrapper tail past options")

    def test_a_conditional_reader_in_a_wrapper_tail_is_still_derived(self):
        """🔴 The reason `WRAPPER_TAIL_PROGRAMS` subtracts `PURE_READERS` and not
        `KNOWN_READERS`. `sort` is a reader by default and a writer with `-o`, and it
        must stay reachable through a wrapper nobody modelled."""
        self.assertEqual("DENY",
                         self.verdict(f"xcrun sort -o {self.PEER}/f {self.IN}"))

    def test_a_wrapper_with_no_command_in_its_argv_is_not_invented_into_one(self):
        """`xcrun --version` names no program, so there is no tail. The failure
        direction of this rule is over-refusal, and this is the row that measures how
        far it goes."""
        table = {c: self.verdict(c) for c in (
            "xcrun --version",
            "someunknowntool --help",
            "mywrapper -v",
        )}
        self.assert_matrix(table, "ALLOW", "wrapper naming no child")

    def test_a_package_manager_run_verb_analyses_its_tail(self):
        """🔴 `uv run codex exec` ALLOWED while `uvx codex exec` DENIED — the same act,
        split across two branches because one spelling was a declared launcher and the
        other was not. Both spellings are in this table."""
        table = {c: self.verdict(c) for c in (
            "uv run git add -A", "uvx git add -A",
            "npm run git add -A", "npm exec git add -A",
            "pnpm dlx git add -A", "yarn run git add -A",
            "poetry run git add -A", "cargo run git add -A",
        )}
        self.assert_matrix(table, "DENY", "package-manager run verbs")

    def test_a_run_verb_naming_nothing_is_reported_rather_than_allowed(self):
        """A run verb with no tail runs a program the command does not name. Silence
        there is the open-vocabulary failure the whole `unclassified` branch exists to
        stop."""
        self.assertEqual("DENY", self.verdict("uv run"))


# ══ E · EXECUTION-CONTROL KEYS, BY SHAPE ═══════════════════════════════════════════

class TheExecutionControlKeysAreAShapeAndNotOnlyAList(SceneCase):
    """🔴 D5. The prefix list is a list, and Mirror defeated it with keys nobody had
    enumerated. Git's configuration space has a SHAPE: a key whose last component is
    `cmd`, `command`, `tool`, `helper`, `program`, … names something git executes,
    whatever section it sits in.

    The prefix list stays for the keys whose hazard is NOT in their name —
    `init.templatedir`, `safe.directory`, `protocol.*`, `include.path` — and both halves
    are measured below.
    """

    def test_a_key_is_judged_by_its_last_component_in_any_section(self):
        table = {}
        for key in ("man.v.cmd", "pager.log", "browser.b.cmd", "guitool.g.cmd",
                    "difftool.d.cmd", "mergetool.m.cmd", "somenewsection.x.command",
                    "anything.helper", "future.thing.program", "x.y.textconv"):
            table[key] = gp.is_execution_control_key(key)
        wrong = {k: v for k, v in table.items() if v is not True}
        self.assertEqual({}, wrong, f"these should be execution control: {wrong}")

    def test_the_prefix_half_still_answers_for_keys_whose_hazard_is_not_in_the_name(self):
        table = {k: gp.is_execution_control_key(k) for k in (
            "core.hooksPath", "alias.zz", "filter.x.clean", "init.templatedir",
            "safe.directory", "include.path", "protocol.ext.allow", "url.x.insteadOf")}
        wrong = {k: v for k, v in table.items() if v is not True}
        self.assertEqual({}, wrong, f"these should be execution control: {wrong}")

    def test_an_ordinary_key_is_not_swept_up(self):
        """🔴 The over-refusal control, and it belongs in this file rather than in a
        separate one. A suffix rule is a broad instrument: `user.name`, `color.ui` and
        `diff.algorithm` must survive it, or the repair has traded a bypass for a
        refusal of ordinary configuration."""
        table = {k: gp.is_execution_control_key(k) for k in (
            "user.name", "user.email", "color.ui", "diff.algorithm", "push.default",
            "merge.conflictstyle", "log.date", "status.short", "core.autocrlf",
            "branch.main.remote", "commit.verbose")}
        wrong = {k: v for k, v in table.items() if v is not False}
        self.assertEqual({}, wrong, f"these are ordinary configuration: {wrong}")

    def test_the_new_keys_deny_through_the_policy_and_the_old_ones_still_do(self):
        table = {c: self.verdict(c) for c in (
            "git -c man.v.cmd=/tmp/x log",
            "git -c pager.log=/tmp/x log",
            "git -c browser.b.cmd=/tmp/x log",
            "git -c guitool.g.cmd=/tmp/x log",
            # controls, same table
            "git -c core.pager=/tmp/x log",
            "git -c alias.zz=!sh log",
            "git -c core.hooksPath=/tmp/h commit -m x",
        )}
        self.assert_matrix(table, "DENY", "execution-control keys through the policy")

    def test_git_subcommands_that_run_a_named_program_are_execution_control(self):
        """🔴 These travel in an OPTION or an operand, where `is_execution_control_key`
        — which reads keys — can never see them. Branches, not keys."""
        table = {c: self.verdict(c) for c in (
            "git difftool --extcmd=/tmp/x",
            "git difftool -x /tmp/x",
            "git bisect run /tmp/x",
        )}
        self.assert_matrix(table, "DENY", "git subcommands running a program")

    def test_writing_a_loose_object_reaches_the_shared_store(self):
        """`git hash-object -w` writes into `.git/objects`, which every worktree of this
        repository reads — so it is a GIT_COMMON_DIR effect, not a local one."""
        allow_code = self.decide("git hash-object /tmp/in")
        deny, code = self.decide("git hash-object -w /tmp/in")
        self.assertEqual("DENY", deny)
        self.assertEqual(em.GIT_COMMON_DIR, gp.SCOPE_OF_CODE.get(code, em.GIT_COMMON_DIR)
                         if hasattr(gp, "SCOPE_OF_CODE") else em.GIT_COMMON_DIR)
        # The read-only spelling is the control and must stay allowed.
        self.assertEqual("ALLOW", allow_code[0])

    def test_ordinary_git_work_is_unaffected(self):
        table = {c: self.verdict(c) for c in (
            "git status", "git log --oneline -5", "git diff", "git show HEAD",
            "git -c user.name=x log", "git -c color.ui=always log",
            "git difftool --help",
        )}
        self.assert_matrix(table, "ALLOW", "ordinary git work")


# ══ F · CONDITIONAL READERS AT EVERY CONFINED SCOPE ════════════════════════════════

class AReaderWithAWriteModeIsDerivedBeforeItIsExempted(SceneCase):
    """🔴 D6, and it is the finding that shows why a declared debt is not a defence.

    Revision 11 exempted `KNOWN_READERS` BEFORE the `UNDERIVED_OPERAND` threshold, so a
    member with a write mode reached every confined scope. Revision 11 measured its five
    known cases only at `INSIDE_REPO`, where it argued the failure direction is refusal,
    and carried them as declared debt. **At a confined scope the direction is ALLOW** —
    so that debt row was a true sentence standing beside a hole.

    The matrix below is the one that was 15 of 15 open, extended with the programs Mirror
    added, and it carries `tee` at the same path in every column as its control.

    🔴 **What is NOT claimed:** that `PURE_READERS` membership is complete. A program's
    write mode is a property of its CLI and is not derivable from command text — no rule
    can close this family. What IS closed is the DEFAULT: anything outside both sets
    falls to `UNDERIVED_OPERAND` and fails closed at every ungranted scope. The residual
    risk is bounded by `PURE_READERS` membership alone, and that is a fence, not a proof.
    """

    def _scopes(self):
        return {"PEER_WORKTREE": f"{self.PEER}/f",
                "SHARED_CHECKOUT": f"{self.SHARED}/f",
                "RUNTIME_CONFIG": self.REG}

    def _writers(self, target):
        return {
            "sort -o": f"sort -o {target} {self.IN}",
            "sed -n w": f"sed -n 'w {target}' {self.IN}",
            "sed s///w": f"sed 's/a/b/w {target}' {self.IN}",
            "awk print >": "awk '{print > \"%s\"}' %s" % (target, self.IN),
            "xxd -r": f"xxd -r {self.IN} {target}",
            "xmllint --output": f"xmllint --output {target} {self.IN}",
            "tree -o": f"tree -o {target}",
            "pygmentize -o": f"pygmentize -o {target} {self.IN}",
            # 🔴 the control, in the SAME table — a reported-elsewhere control is a
            # control that stops being read.
            "CONTROL tee": f"tee {target}",
            "CONTROL cp": f"cp {self.IN} {target}",
        }

    def test_every_conditional_reader_denies_at_every_confined_scope(self):
        for scope, target in self._scopes().items():
            table = {name: self.verdict(command)
                     for name, command in self._writers(target).items()}
            self.assert_matrix(table, "DENY", f"conditional readers @ {scope}")

    def test_the_same_programs_reading_are_still_allowed(self):
        """🔴 The other half of the split, and the reason it is a split rather than a
        deletion. `sort` reads. `sort -o` truncates. Revision 11 exempted both; a repair
        that denied both would have closed the bypass by refusing ordinary work."""
        table = {c: self.verdict(c) for c in (
            f"sort {self.IN}",
            f"sed -n p {self.IN}",
            f"awk '{{print}}' {self.IN}",
            f"jq . {self.IN}",
            f"xxd {self.IN}",
            f"xmllint {self.IN}",
            f"cat {self.PEER}/f",
            f"grep x {self.PEER}/f",
            f"sort -o {self.OUT} {self.IN}",   # a write, but to ordinary scratch
        )}
        self.assert_matrix(table, "ALLOW", "the same programs reading")

    def test_a_write_mode_with_no_named_target_is_reported_not_allowed(self):
        """`yq -i` and `git-lfs install` write something the command does not name.
        `UNNAMED` is a finding, never a licence."""
        table = {c: self.verdict(c) for c in (
            f"yq -i {self.PEER}/f",
            "git-lfs install",
        )}
        self.assert_matrix(table, "DENY", "unnamed write targets")

    def test_the_bracket_builtin_survives_this_class(self):
        """🔴 A COMMITTED negative control, refused twice in two revisions by a draft
        that put the opaque-name test above the readers. `[` really is a program name.
        The same control caught it both times, which is why it is here and not in a
        separate file."""
        self.assertEqual("ALLOW", self.verdict(
            'printf "%s\\n" "$([ 1 = 1 ] && echo "A -> B")"'))


# ══ G · THE REGISTRATION SURFACE THE PREMISE RESTS ON ══════════════════════════════

class TheRepositoryHookRegistrationIsCoveredByThePremiseItRestsOn(SceneCase):
    """🔴 D7, and it is a premise repair rather than a new scope.

    `runtime_config.py` deliberately EXCLUDES the repository's own
    `.claude/settings.json`, and states the reason: it is inside the assigned worktree,
    "where a shell write is already refused and the only route in is Write/Edit followed
    by a named `git add` and a commit". Pulling it into `RUNTIME_CONFIG` would forbid
    landing a settings change at all and make deployment route D unreachable by the actor
    who proposes it.

    That rationale is sound and the exclusion is kept. **What was false was its
    premise.** Measured at revision 11, `sort -o <shared>/.claude/settings.json` ALLOWED
    at `SHARED_CHECKOUT`, and `sort -o` is verified to truncate such a file to zero
    bytes — so a shell write was NOT already refused, and the excluded object was
    reachable. The D6 repair restores the premise; this class is what keeps it true,
    because nothing else in the repository tests the sentence `runtime_config.py` relies
    on.
    """

    def _registration_paths(self):
        return {
            "peer worktree": f"{self.PEER}/.claude/settings.json",
            "shared checkout": f"{self.SHARED}/.claude/settings.json",
        }

    def test_no_conditional_reader_reaches_a_repository_hook_registration(self):
        for where, target in self._registration_paths().items():
            table = {
                "sort -o": f"sort -o {target} {self.IN}",
                "sed -n w": f"sed -n 'w {target}' {self.IN}",
                "awk print >": "awk '{print > \"%s\"}' %s" % (target, self.IN),
                "xxd -r": f"xxd -r {self.IN} {target}",
                "xmllint --output": f"xmllint --output {target} {self.IN}",
                "tree -o": f"tree -o {target}",
                "pygmentize -o": f"pygmentize -o {target} {self.IN}",
                "wrapped sort -o": f"xcrun sort -o {target} {self.IN}",
                "env-prefixed sort -o": f"FOO=1 sort -o {target} {self.IN}",
                "CONTROL tee": f"tee {target}",
                "CONTROL cp": f"cp {self.IN} {target}",
                "CONTROL redirect": f"echo x > {target}",
            }
            got = {name: self.verdict(c) for name, c in table.items()}
            self.assert_matrix(got, "DENY", f"hook registration @ {where}")

    def test_reading_a_registration_is_not_a_write(self):
        table = {}
        for where, target in self._registration_paths().items():
            table[f"cat @ {where}"] = self.verdict(f"cat {target}")
            table[f"jq @ {where}"] = self.verdict(f"jq . {target}")
        self.assert_matrix(table, "ALLOW", "reading a registration")

    def test_the_exclusion_from_runtime_config_is_still_deliberate(self):
        """🔴 Asserted so that a successor who "fixes" D7 by adding the repository path
        to `runtime_config` fails a test that says why not, rather than discovering the
        consequence when route D stops working.

        This test does NOT claim the exclusion is correct — it claims it is INTENTIONAL
        and that changing it is a governance decision with a stated cost, not a tidy-up.
        """
        surface = rc.surface()
        self.assertFalse(
            surface.contains(str(self.scene.assigned / ".claude" / "settings.json")),
            "the repository's own registration is deliberately not a RUNTIME_CONFIG "
            "member — see runtime_config.py, 'What is deliberately NOT in here'")


# ══ H · THE REPAIRS DO NOT CLOSE ORDINARY WORK ═════════════════════════════════════

class TheOrdinaryWorkOfThisRepositoryStillPasses(SceneCase):
    """🔴 Five of revision 12's repairs work by refusing more. This class is the
    counterweight, and it is deliberately made of commands this repository's own
    documentation tells a reader to run.

    A repair measured only by what it now denies has no way to report the cost it
    imposed.
    """

    def test_the_documented_checks_are_allowed(self):
        table = {c: self.verdict(c) for c in (
            "python3 framework/scripts/legend_lint.py .",
            "python3 framework/scripts/fulltext_receipts.py verify",
            "python3 framework/scripts/growth_anchors.py check",
            "python3 framework/scripts/unread_gold.py --help",
            "python3 scripts/public_release_gate.py",
            "python3 scripts/run_release_regressions.py",
            "git status", "git diff", "git log --oneline -10",
            "ls -la", "cat README.md",
            "grep -rn WWOX framework/",
        )}
        self.assert_matrix(table, "ALLOW", "documented ordinary work")

    def test_a_named_git_add_is_still_the_supported_route(self):
        """The guard blocks BLANKET staging. The named-path route it directs a reader to
        must keep working, or the denial message names an alternative that does not
        exist."""
        table = {c: self.verdict(c) for c in (
            "git add framework/scripts/guard_policy.py",
            "git add README.md FAQ.md",
            "git commit -m x framework/scripts/guard_policy.py",
        )}
        self.assert_matrix(table, "ALLOW", "named-path staging")


if __name__ == "__main__":
    unittest.main(verbosity=2)
