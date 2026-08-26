#!/usr/bin/env python3
"""Proof that the parity battery can go red.

A battery that only ever passes is a green light, not a check. Each test below breaks
exactly one thing — in a copy, never in the repository — and asserts the matching check
fails. Between them they cover every failure the operator specified: the router stops
routing, a skill becomes unreachable, the Codex hook is absent, the Codex hook lets a
prohibited write through, and the two runtimes derive different authority.
"""
from __future__ import annotations

import importlib.util
import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
ENTRY = HERE / "runtime_parity.py"
SPEC = importlib.util.spec_from_file_location("runtime_parity", ENTRY)
rp = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rp
SPEC.loader.exec_module(rp)


def outcome(check) -> tuple[bool, str]:
    result = rp.Result()
    check(result)
    _, ok, detail = result.rows[0]
    return ok, detail


class TheBatteryPassesOnTheRealRepositoryExceptWhereItShouldNot(unittest.TestCase):
    def test_seven_of_eight_pass_and_the_eighth_is_the_declared_unknown(self) -> None:
        result = rp.run_battery()
        failed = [name for name, ok, _ in result.rows if not ok]
        self.assertEqual(len(result.rows), 8, "eight checks, per the protocol's table")
        self.assertTrue(
            set(failed) <= {"NO_RUNTIME_AUTHORITY_ESCALATION"},
            f"only the unverified-hook check may fail here; got {failed}",
        )

    def test_the_lease_predicate_is_not_the_exit_code(self) -> None:
        """`lease_state.py --check` exits 0 *while reporting findings*, deliberately.

        So a bootstrap that reads its exit code learns nothing about whether a laboratory
        is running. The predicate is the derived `ACTIVE` count. This test pins both
        halves: the tool really does exit 0 here, and the state derived from it is really
        not `ACTIVE` — so an exit-code reading and the correct reading disagree today,
        which is the only condition under which this distinction is worth code.
        """
        tool = rp.ROOT / "framework" / "scripts" / "lease_state.py"
        raw = subprocess.run([sys.executable, str(tool), "--check"],
                             capture_output=True, text=True, cwd=str(rp.ROOT))
        self.assertEqual(raw.returncode, 1, "findings on a historical row exit 1")
        self.assertIn("FINDING:", raw.stdout)

        state, detail = rp.lease_state()
        self.assertEqual(state, "NO_ACTIVE_LEASE",
                         "rc=1 is a finding about 2026-08-18, not a reason to halt today")
        self.assertRegex(detail, r"^\d+ ACTIVE by derivation")

    def test_the_fatal_exit_code_is_honoured_even_though_it_is_not_zero(self) -> None:
        """`rc=3` is the singleton violation and must stop a session; `rc=1` must not."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fake = root / "framework" / "scripts" / "lease_state.py"
            fake.parent.mkdir(parents=True)
            fake.write_text(
                "import sys\n"
                "print('ACTIVE by derivation: 2')\n"
                "sys.exit(3)\n",
                encoding="utf-8",
            )
            with mock.patch.object(rp, "ROOT", root):
                state, detail = rp.lease_state()
        self.assertEqual(state, "SINGLETON_VIOLATION")
        self.assertIn("fatal", detail)


class RouterCanStopRouting(unittest.TestCase):
    def test_agents_md_without_claude_md_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            broken = Path(tmp) / "AGENTS.md"
            broken.write_text("# a router that routes nowhere\n", encoding="utf-8")
            with mock.patch.object(rp, "CODEX_ROUTER", broken):
                ok, detail = outcome(rp.check_router_reachability)
        self.assertFalse(ok)
        self.assertIn("no longer routes to CLAUDE.md", detail)

    def test_agents_md_that_drops_a_chain_member_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            partial = Path(tmp) / "AGENTS.md"
            partial.write_text("read CLAUDE.md and stop there\n", encoding="utf-8")
            with mock.patch.object(rp, "CODEX_ROUTER", partial):
                ok, detail = outcome(rp.check_router_reachability)
        self.assertFalse(ok)
        self.assertIn("not named in AGENTS.md", detail)

    def test_missing_actor_id_declaration_fails_no_self_election(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            silent = Path(tmp) / "AGENTS.md"
            silent.write_text("CLAUDE.md\n", encoding="utf-8")
            with mock.patch.object(rp, "CODEX_ROUTER", silent):
                ok, detail = outcome(rp.check_no_self_election)
        self.assertFalse(ok)
        self.assertIn("assigned", detail)


class SkillsCanBecomeUnreachableOrDuplicated(unittest.TestCase):
    def test_missing_skill_fails(self) -> None:
        with mock.patch.object(rp, "PROBE_SKILLS", ("legend-start", "not-a-real-skill")):
            ok, detail = outcome(rp.check_skill_reachability)
        self.assertFalse(ok)
        self.assertIn("not-a-real-skill", detail)

    def test_a_second_copy_of_one_skill_fails(self) -> None:
        """The failure the bridge exists to prevent: two sources for one rule."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            subprocess.run(["git", "-C", str(root), "init", "-q", "."], check=True)
            body = "# a skill\nprocedure\n"
            for rel in (".claude/skills/legend-start/SKILL.md",
                        "vendor/copied/SKILL.md"):
                path = root / rel
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(body, encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "-f", "."], check=True,
                           capture_output=True)
            with mock.patch.object(rp, "ROOT", root), \
                 mock.patch.object(rp, "PROBE_SKILLS", ("legend-start",)):
                ok, detail = outcome(rp.check_skill_reachability)
                rows = rp.skill_report()
        self.assertFalse(ok, "two byte-identical copies must fail the bridge")
        self.assertIn("legend-start", detail)
        self.assertFalse(rows[0]["NO_DUPLICATED_NORMATIVE_COPY"])
        self.assertEqual(len(rows[0]["copies"]), 2)


class TheCodexHookCanBeAbsentOrPermissive(unittest.TestCase):
    def test_absent_codex_registration_fails(self) -> None:
        with mock.patch.object(rp, "CODEX_REGISTRATION", Path("/nonexistent/config.toml")):
            ok, detail = outcome(rp.check_no_runtime_authority_escalation)
        self.assertFalse(ok)
        self.assertIn("Codex has no registration", detail)

    def test_registration_that_does_not_name_the_shared_engine_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            other = Path(tmp) / "config.toml"
            other.write_text(
                '[hooks]\nPreToolUse = [{ matcher = "shell_command", hooks = ['
                '{ type = "command", command = "python3 codex_only_guard.py" }] }]\n',
                encoding="utf-8",
            )
            with mock.patch.object(rp, "CODEX_REGISTRATION", other):
                ok, detail = outcome(rp.check_no_runtime_authority_escalation)
        self.assertFalse(ok)
        self.assertIn("does not name the shared engine", detail)

    def test_a_codex_payload_that_slips_a_prohibited_write_through_fails_parity(self) -> None:
        """The exact bug a naive port ships: argv stringified instead of reduced.

        `str(['bash','-lc','git add -A'])` wraps the command in quotes and the policy
        ignores quoted spans, so this shape is ALLOWED — while the Claude shape of the
        same command is DENIED. That is a runtime granting authority, and the check must
        see it.
        """
        def naive(command: str) -> dict:
            return {"hook_event_name": "PreToolUse", "tool_name": "shell_command",
                    "tool_input": {"cmd": str(["bash", "-lc", command])}}

        with mock.patch.object(rp, "codex_payload", naive):
            ok, detail = outcome(rp.check_write_guard_parity)
        self.assertFalse(ok, "a Codex-only permission must fail WRITE_GUARD_PARITY")
        self.assertIn("claude=deny", detail)
        self.assertIn("codex=allow", detail)


class AuthorityCanDivergeBetweenRuntimes(unittest.TestCase):
    def test_a_fingerprint_that_reads_the_runtime_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tool = root / "governance" / "scripts" / "governance_fingerprint.py"
            tool.parent.mkdir(parents=True)
            tool.write_text(
                "import os, sys\n"
                "sys.stdout.write(os.environ.get('LEGEND_RUNTIME', 'none') + '\\n')\n",
                encoding="utf-8",
            )
            tool.chmod(tool.stat().st_mode | stat.S_IEXEC)
            with mock.patch.object(rp, "ROOT", root):
                ok, detail = outcome(rp.check_authority_parity)
        self.assertFalse(ok)
        self.assertIn("differ between runtimes", detail)

    def test_absent_fingerprint_tool_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(rp, "ROOT", Path(tmp)):
                ok, detail = outcome(rp.check_authority_parity)
        self.assertFalse(ok)
        self.assertIn("absent", detail)


class FailClosedCanLeak(unittest.TestCase):
    def test_an_engine_that_stays_silent_fails_the_fail_closed_check(self) -> None:
        """A guard that answers nothing is a guard that answers yes."""
        with tempfile.TemporaryDirectory() as tmp:
            permissive = Path(tmp) / "pre_tool_use_guard.py"
            permissive.write_text("import sys\nsys.stdin.read()\n", encoding="utf-8")
            with mock.patch.object(rp, "GUARD_ENTRY", permissive):
                ok, detail = outcome(rp.check_fail_closed)
        self.assertFalse(ok)
        self.assertIn("->allow", detail)


class TheBootstrapRefusesRatherThanReports(unittest.TestCase):
    def test_unassigned_actor_id_blocks(self) -> None:
        env = {k: v for k, v in os.environ.items() if k != rp.ACTOR_ID_ENV}
        with mock.patch.dict(os.environ, env, clear=True):
            _, blockers = rp.bootstrap(None)
        self.assertIn("ACTOR_ID is unassigned", blockers)

    def test_unverified_write_guard_forces_read_only(self) -> None:
        _, blockers = rp.bootstrap("mirror")
        self.assertTrue(
            any("READ-ONLY" in b for b in blockers),
            "an unverified guard must pin the actor read-only, not merely be reported",
        )

    def test_cli_exits_non_zero_while_blocked(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ENTRY), "--bootstrap", "--actor", "mirror"],
            capture_output=True, text=True, cwd=str(rp.ROOT),
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("BLOCKED_BY_GOVERNANCE", result.stdout)


class TheDeclaredGapsStayDeclared(unittest.TestCase):
    def test_every_characterised_gap_is_identical_on_both_sides(self) -> None:
        for label, command in rp.GUARD_GAPS:
            with self.subTest(gap=label):
                self.assertEqual(
                    rp._hook(rp.claude_payload(command)),
                    rp._hook(rp.codex_payload(command)),
                    "a gap that is runtime-specific is an escalation, not debt",
                )


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
