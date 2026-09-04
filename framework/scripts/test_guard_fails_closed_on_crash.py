#!/usr/bin/env python3
"""A guard that crashes must SAY no. Writing nothing is not saying no.

`main()` caught `Undecidable` and nothing else, so any other exception — a `KeyError` in
the policy, a `TypeError` on an unanticipated payload shape, an `OSError` out of
`session_binding`, any bug — escaped, and Python's default handler wrote a traceback to
stderr and exited non-zero with an EMPTY STDOUT.

That distinction is the whole suite. A `PreToolUse` hook communicates a refusal by writing
JSON to stdout; an empty stdout is silence, and a harness is free to read silence as no
objection. So the guard was fail-SILENT under the name fail-closed, which is the one
direction a guard must never fail in.

🔴 What no test here can cover, said plainly rather than left to be assumed: a process that
is killed, exhausts memory, or exceeds the harness's timeout also writes nothing, and no
in-process handler speaks for a process that is not running. Only the runtime can fail
closed on a dead hook. This covers the half reachable from inside the process.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY_DIR = ROOT / "framework" / "scripts"

PAYLOAD = json.dumps({"tool_name": "Bash", "cwd": str(ROOT),
                      "tool_input": {"command": "git status --short"}})

# Raised from inside `decide`, in a child process, so the real entry point is measured and
# not a re-implementation of it.
HARNESS = """
import sys
sys.path.insert(0, {policy!r})
import pre_tool_use_guard as g
def boom(payload):
    raise {exception}
g.decide = boom
sys.exit(g.main())
"""


class ACrashedGuardStillAnswers(unittest.TestCase):
    def run_crashing(self, exception: str):
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "crash_hook.py"
            script.write_text(HARNESS.format(policy=str(POLICY_DIR), exception=exception),
                              encoding="utf-8")
            return subprocess.run([sys.executable, str(script)], input=PAYLOAD,
                                  capture_output=True, text=True)

    def test_every_unexpected_exception_becomes_a_denial(self) -> None:
        for exception in ("KeyError('k')", "TypeError('t')", "OSError('io')",
                          "RecursionError('deep')", "RuntimeError('boom')",
                          "AttributeError('a')", "ValueError('v')"):
            with self.subTest(exception=exception):
                result = self.run_crashing(exception)
                self.assertTrue(result.stdout.strip(),
                                f"{exception} produced an EMPTY stdout, which is silence "
                                "and not a denial")
                decision = json.loads(result.stdout)["hookSpecificOutput"]
                self.assertEqual("deny", decision["permissionDecision"])
                self.assertIn("crashed while deciding",
                              decision["permissionDecisionReason"])

    def test_the_denial_names_the_exception_so_the_bug_is_reportable(self) -> None:
        """A denial that hides its cause turns a guard defect into a mystery, and a
        mystery gets worked around."""
        out = self.run_crashing("RuntimeError('a very distinctive message')").stdout
        reason = json.loads(out)["hookSpecificOutput"]["permissionDecisionReason"]
        self.assertIn("RuntimeError", reason)
        self.assertIn("a very distinctive message", reason)

    def test_the_probe_can_distinguish_the_two_outcomes(self) -> None:
        """POSITIVE CONTROL, and this suite is worthless without it.

        Every assertion above passes trivially if the harness always denies. This proves
        the same probe reports ALLOW when nothing crashes — so the denials above are
        caused by the crash and not by the fixture.
        """
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / "clean_hook.py"
            script.write_text(
                f"import sys\nsys.path.insert(0, {str(POLICY_DIR)!r})\n"
                "import pre_tool_use_guard as g\nsys.exit(g.main())\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(script)], input=PAYLOAD,
                                    capture_output=True, text=True)
        self.assertEqual("", result.stdout.strip(),
                         "an allowed command must produce no output, or the contrast above "
                         "means nothing")

    def test_a_crash_in_the_PARSE_is_covered_too_and_not_only_in_decide(self) -> None:
        """🔴 The gap blind review found in the first version of this suite.

        Every case above monkeypatches `decide`, so all of them raise INSIDE the inner
        `try` and none ever reaches `sys.stdin.read()` or `json.loads`. `json.loads` was
        guarded only by `except (json.JSONDecodeError, ValueError)`, and 200k nested
        brackets raise `RecursionError`, which escaped both — rc=1, empty stdout. The
        commit that added the inner handler claimed to close "the half reachable from
        inside the process" and did not, and this suite certified that claim while
        structurally unable to test it.

        These inputs go through the REAL entry point with no patching at all.
        """
        hook = ROOT / "scripts" / "guard_bash_command.py"
        for label, data in (("deeply nested array", "[" * 200000 + "]" * 200000),
                            ("deeply nested object", '{"a":' * 100000 + "1" + "}" * 100000),
                            ("unparseable", "{not json"),
                            ("empty", "")):
            with self.subTest(input=label):
                result = subprocess.run([sys.executable, str(hook)], input=data,
                                        capture_output=True, text=True)
                self.assertTrue(
                    result.stdout.strip(),
                    f"{label} produced an EMPTY stdout — silence, which a harness may read "
                    "as no objection")
                self.assertEqual(
                    "deny",
                    json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"])

    def test_unparseable_stdin_was_already_covered_and_still_is(self) -> None:
        """The pre-existing arm, kept under test so the new one cannot displace it."""
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "guard_bash_command.py")],
            input="{not json", capture_output=True, text=True)
        decision = json.loads(result.stdout)["hookSpecificOutput"]
        self.assertEqual("deny", decision["permissionDecision"])
        self.assertIn("could not read its own input", decision["permissionDecisionReason"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
