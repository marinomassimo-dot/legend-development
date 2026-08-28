#!/usr/bin/env python3
"""Proof that the parity battery can go red — and that it goes red for the right reason.

A battery that only ever passes is a green light, not a check. Each test below breaks
exactly one thing — in a fixture tree, never in the repository — and asserts the matching
check fails.

## What revision 2 could not test, and why these fixtures exist

`runtime_parity.py` used to import the guard engine at module scope and mock module-level
path constants. Two consequences, both of which this file now avoids:

1. **the engine-missing arm was unreachable.** With the engine absent the module died at
   import, so the branch that reports it never executed. The test that "covered" it
   asserted a `FileNotFoundError`, which is a fact about Python, not about the battery.
2. **mocking a constant does not move the surface.** Patching `CODEX_REGISTRATION` left
   every other path pointing at the real repository, so no arm ever exercised the battery
   against a tree that was genuinely incomplete.

Both are fixed by `Surface`: the battery takes a root, the tests build roots with one
component removed, and every negative arm runs the real code path against a real tree.
"""
from __future__ import annotations

import importlib.util
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENTRY = HERE / "runtime_parity.py"
REPO = HERE.parents[1]
SPEC = importlib.util.spec_from_file_location("runtime_parity", ENTRY)
rp = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = rp
SPEC.loader.exec_module(rp)

REAL = rp.Surface(REPO)

#: Everything a fixture needs to look like this repository to the battery.
FIXTURE_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    "BOOTSTRAP.md",
    "framework/state/state_manifest_current.md",
    "governance/ANNEX_INDEX.md",
    "framework/protocols/index.md",
    "framework/scripts/pre_tool_use_guard.py",
    "framework/scripts/guard_policy.py",
    "framework/scripts/lease_state.py",
    ".claude/settings.json",
    ".codex/config.toml",
    "roles/orchestrator.md",
    "roles/plan.md",
    "roles/mirror.md",
    "roles/scientist.md",
)


def build_fixture(tmp: str, omit=(), rewrite=None) -> "rp.Surface":
    """A tree the battery can judge, with named components deliberately absent.

    Copied rather than symlinked: a symlinked engine is still an engine, and the arm that
    matters is the one where the file genuinely is not there.
    """
    root = Path(tmp) / "fixture"
    root.mkdir()
    for rel in FIXTURE_FILES:
        if rel in omit:
            continue
        source = REPO / rel
        if not source.exists():
            continue
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(source, target)
    for rel in ("legend-start", "legend-deepdive", "legend-locator-audit"):
        source = REPO / ".claude" / "skills" / rel / "SKILL.md"
        if f".claude/skills/{rel}/SKILL.md" in omit or not source.exists():
            continue
        target = root / ".claude" / "skills" / rel / "SKILL.md"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(source, target)
    fingerprint = REPO / "governance" / "scripts" / "governance_fingerprint.py"
    if "governance/scripts/governance_fingerprint.py" not in omit and fingerprint.exists():
        (root / "governance" / "scripts").mkdir(parents=True, exist_ok=True)
        shutil.copy(fingerprint, root / "governance" / "scripts" / "governance_fingerprint.py")
    for rel, body in (rewrite or {}).items():
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
    subprocess.run(["git", "-C", str(root), "init", "-q", "."], check=True,
                   capture_output=True)
    subprocess.run(["git", "-C", str(root), "add", "-f", "."], check=True,
                   capture_output=True)
    return rp.Surface(root)


def row(surface, check, actor=None):
    result = rp.Result()
    check(surface, result, actor)
    _, ok, detail = result.rows[0]
    return ok, detail


# ── the real repository ────────────────────────────────────────────────────────────

class TheRealRepositoryScoresWhatItShould(unittest.TestCase):
    def test_ten_dimensions_are_reported(self) -> None:
        result = rp.run_battery(REAL, "mirror")
        names = [n for n, _, _ in result.rows]
        self.assertEqual(len(result.rows), 10, "the protocol's table has ten rows")
        self.assertEqual(names, list(dict.fromkeys(names)), "no dimension is reported twice")

    def test_read_only_floor_passes_and_write_floor_does_not(self) -> None:
        """The two verdicts are separate, and today they genuinely differ."""
        result = rp.run_battery(REAL, "mirror")
        self.assertTrue(result.subset(rp.READ_ONLY_REQUIRES),
                        "the read-only floor holds on this tree")
        self.assertFalse(result.subset(rp.WRITE_ENABLED_REQUIRES),
                         "the write floor must not pass while the hook is undemonstrated")

    def test_only_the_hook_rows_fail(self) -> None:
        failed = {n for n, ok, _ in rp.run_battery(REAL, "mirror").rows if not ok}
        self.assertEqual(failed, {"HOOK_DEMONSTRATED", "NO_RUNTIME_AUTHORITY_ESCALATION"},
                         f"unexpected failures: {failed}")

    def test_the_lease_predicate_is_not_the_exit_code(self) -> None:
        """`lease_state.py --check` exits 0 *while reporting findings*, deliberately.

        So a bootstrap that reads its exit code learns nothing about whether a laboratory
        is running. The predicate is the derived `ACTIVE` count. This test pins both
        halves: the tool really does exit non-zero here, and the state derived from it is
        really not `ACTIVE` — so an exit-code reading and the correct reading disagree
        today, which is the only condition under which this distinction is worth code.
        """
        raw = subprocess.run([sys.executable, str(REAL.lease_tool), "--check"],
                             capture_output=True, text=True, cwd=str(REPO))
        self.assertEqual(raw.returncode, 1, "findings on a historical row exit 1")
        state, _ = rp.lease_state(REAL)
        self.assertNotEqual(state, "UNDERIVABLE")
        self.assertNotEqual(state, "ACTIVE")


# ── P0-D · a missing safety component must never be green ──────────────────────────

class AMissingSafetyComponentIsNeverGreen(unittest.TestCase):
    """The property the operator named, arm by arm, each executed rather than asserted."""

    def assert_not_green(self, surface, expect_row: str) -> None:
        result = rp.run_battery(surface, "mirror")
        self.assertFalse(result.subset(rp.READ_ONLY_REQUIRES) and
                         result.subset(rp.WRITE_ENABLED_REQUIRES),
                         "a tree missing a safety component reported both floors green")
        self.assertFalse(result.named(expect_row),
                         f"{expect_row} should have failed; rows: "
                         + str([(n, ok) for n, ok, _ in result.rows]))

    def test_ENGINE_MISSING(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=("framework/scripts/pre_tool_use_guard.py",))
            self.assert_not_green(surface, "MISSING_BRIDGE_FAIL_CLOSED")
            ok, detail = row(surface, rp.check_missing_bridge_fail_closed)
            self.assertFalse(ok)
            self.assertIn("shared engine is absent", detail)

    def test_ENGINE_MISSING_does_not_crash_the_battery(self) -> None:
        """The revision-2 defect exactly: the engine's absence was a traceback, not a row.

        The CLI must run to completion and print a FAIL, because an operator reading a
        stack trace cannot tell a broken tool from a broken bridge.
        """
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=("framework/scripts/pre_tool_use_guard.py",))
            result = subprocess.run(
                [sys.executable, str(ENTRY), "--root", str(surface.root), "--actor", "mirror"],
                capture_output=True, text=True,
            )
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Traceback", result.stderr, "the battery must report, not crash")
        self.assertIn("MISSING_BRIDGE_FAIL_CLOSED", result.stdout)
        self.assertIn("FAIL", result.stdout)

    def test_ENGINE_IMPORT_FAILURE(self) -> None:
        """An engine that is present and unimportable is not an engine."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "framework/scripts/guard_policy.py": "raise ImportError('policy is broken')\n",
            })
            self.assert_not_green(surface, "MISSING_BRIDGE_FAIL_CLOSED")
            ok, detail = row(surface, rp.check_missing_bridge_fail_closed)
            self.assertFalse(ok)
            self.assertIn("errored", detail)

    def test_POLICY_MISSING(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=("framework/scripts/guard_policy.py",))
            self.assert_not_green(surface, "MISSING_BRIDGE_FAIL_CLOSED")
            self.assertIn("policy module is absent",
                          row(surface, rp.check_missing_bridge_fail_closed)[1])

    def test_HOOK_REGISTRATION_MISSING_codex(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=(".codex/config.toml",))
            self.assertEqual(rp.hook_status(surface)[0], rp.NOT_CONFIGURED)
            self.assertFalse(row(surface, rp.check_hook_registration_present)[0])
            self.assert_not_green(surface, "HOOK_REGISTRATION_PRESENT")

    def test_HOOK_REGISTRATION_MISSING_claude(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=(".claude/settings.json",))
            ok, detail = row(surface, rp.check_hook_registration_present)
            self.assertFalse(ok)
            self.assertIn("claude registration absent", detail)

    def test_HOOK_CONFIG_MALFORMED(self) -> None:
        """Unparseable TOML is UNDERIVABLE — never quietly `CONFIGURED`."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                ".codex/config.toml": '[hooks\nPreToolUse = "not closed\n',
            })
            state, _ = rp.hook_status(surface)
            self.assertIn(state, (rp.UNDERIVABLE, rp.NOT_CONFIGURED))
            self.assertFalse(row(surface, rp.check_hook_registration_present)[0])

    def test_HOOK_REGISTRATION_NAMES_ANOTHER_ENGINE(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                ".codex/config.toml":
                    '[hooks]\nPreToolUse = [{ matcher = "shell_command", hooks = ['
                    '{ type = "command", command = "python3 codex_only_guard.py" }] }]\n',
            })
            self.assertEqual(rp.hook_status(surface)[0], rp.NOT_CONFIGURED)
            self.assertFalse(row(surface, rp.check_no_runtime_authority_escalation)[0])

    def test_PAYLOAD_MALFORMED(self) -> None:
        """Ten undecidable inputs, each of which must come back `deny`."""
        ok, detail = row(REAL, rp.check_missing_bridge_fail_closed)
        self.assertTrue(ok, detail)
        for raw in ("not json", "", "[]", "null", '{"tool_name":"Bash"}',
                    '{"hook_event_name":"PreToolUse","tool_name":"Bash","tool_input":7}'):
            with self.subTest(raw=raw[:24]):
                result = subprocess.run([sys.executable, str(REAL.guard_entry)], input=raw,
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, "the hook itself must not error")
                self.assertEqual(
                    json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"],
                    "deny")

    def test_A_SILENT_ENGINE_LEAKS_AND_IS_CAUGHT(self) -> None:
        """A guard that answers nothing is a guard that answers yes."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "framework/scripts/pre_tool_use_guard.py": "import sys\nsys.stdin.read()\n",
            })
            ok, detail = row(surface, rp.check_missing_bridge_fail_closed)
        self.assertFalse(ok)
        self.assertIn("->allow", detail)


# ── P0-B · the hook state machine ──────────────────────────────────────────────────

class TheHookStateMachineIsFiveValued(unittest.TestCase):
    def test_configuration_alone_never_reaches_demonstrated(self) -> None:
        """§ 38, mechanically: CONFIGURED != PROVEN."""
        self.assertEqual(rp.hook_status(REAL)[0], rp.TRUST_PENDING)
        self.assertNotIn(rp.TRUST_PENDING, rp.PASSING_HOOK_STATES)

    def test_a_refusal_receipt_reaches_demonstrated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "framework/state/codex_hook_probe.json": json.dumps({
                    "schema": "codex_hook_probe/1", "recorded_on": "2026-08-28",
                    "codex_version": "0.150.0-alpha.8", "cwd": "/x",
                    "probe_command": "git add -A", "observed": "REFUSED"}),
            })
            self.assertEqual(rp.hook_status(surface)[0], rp.DEMONSTRATED)
            self.assertTrue(row(surface, rp.check_hook_demonstrated)[0])

    def test_an_execution_receipt_reaches_not_firing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "framework/state/codex_hook_probe.json": json.dumps({
                    "schema": "codex_hook_probe/1", "recorded_on": "2026-08-28",
                    "codex_version": "0.150.0-alpha.8", "cwd": "/x",
                    "probe_command": "git add -A", "observed": "EXECUTED"}),
            })
            self.assertEqual(rp.hook_status(surface)[0], rp.NOT_FIRING)
            self.assertFalse(row(surface, rp.check_hook_demonstrated)[0])

    def test_an_incomplete_receipt_is_underivable_not_demonstrated(self) -> None:
        """The one shape a fabricated receipt would take: a verdict with no provenance."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "framework/state/codex_hook_probe.json": json.dumps({"observed": "REFUSED"}),
            })
            state, evidence = rp.hook_status(surface)
        self.assertEqual(state, rp.UNDERIVABLE)
        self.assertIn("omits", " ".join(text for _, text in evidence))

    def test_an_unreadable_receipt_is_underivable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "framework/state/codex_hook_probe.json": "{not json",
            })
            self.assertEqual(rp.hook_status(surface)[0], rp.UNDERIVABLE)

    def test_hook_status_cli_exits_non_zero_while_undemonstrated(self) -> None:
        result = subprocess.run([sys.executable, str(ENTRY), "--hook-status"],
                                capture_output=True, text=True, cwd=str(REPO))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("TRUST_PENDING", result.stdout)


# ── P0-E · role reachability follows the ASSIGNED actor ────────────────────────────

class RoleReachabilityFollowsTheAssignedActor(unittest.TestCase):
    def test_no_actor_never_elects_one(self) -> None:
        ok, detail = row(REAL, rp.check_role_reachability, None)
        self.assertFalse(ok, "an unassigned actor must not resolve to a default contract")
        self.assertIn("UNRESOLVED", detail)
        self.assertIsNone(rp.role_contract_for(REAL, None)[0])

    def test_a_nonexistent_role_is_refused_not_substituted(self) -> None:
        ok, detail = row(REAL, rp.check_role_reachability, "archivist")
        self.assertFalse(ok)
        self.assertIn("names no role contract", detail)

    def test_actor_id_is_not_taken_from_the_cwd(self) -> None:
        """The worktree is named `mirror`; that must not make the actor Mirror."""
        path, why = rp.role_contract_for(rp.Surface(REPO / ".claude" / "worktrees"), None)
        self.assertIsNone(path)
        self.assertIn("no ACTOR_ID assigned", why)

    def test_actor_id_is_not_taken_from_the_runtime(self) -> None:
        env = {k: v for k, v in os.environ.items() if k != rp.ACTOR_ID_ENV}
        env["LEGEND_RUNTIME"] = "codex"
        result = subprocess.run([sys.executable, str(ENTRY), "--bootstrap"],
                                capture_output=True, text=True, cwd=str(REPO), env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ACTOR_ID is unassigned", result.stdout)

    def test_assigned_mirror_with_only_plan_reachable_fails(self) -> None:
        """The arm the operator named: the router arrives somewhere, but not here."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=("roles/mirror.md",))
            ok, detail = row(surface, rp.check_role_reachability, "mirror")
            self.assertFalse(ok)
            self.assertIn("does not exist", detail)
            self.assertTrue(row(surface, rp.check_role_reachability, "plan")[0],
                            "plan is still reachable, which is what makes this arm sharp")

    def test_a_router_that_never_names_roles_fails_even_when_the_file_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "AGENTS.md": "# router\nRead CLAUDE.md, BOOTSTRAP.md, "
                             "governance/ANNEX_INDEX.md, framework/protocols/index.md, "
                             "framework/state/state_manifest_current.md.\n"
                             "Your ACTOR_ID is assigned by the operator.\n",
            })
            ok, detail = row(surface, rp.check_role_reachability, "mirror")
        self.assertFalse(ok, "existing-and-readable is not the same as reachable")
        self.assertIn("never arrives", detail)

    def test_role_contract_hash_changes_are_visible_after_bootstrap(self) -> None:
        """A contract that moves under an actor mid-session must be detectable."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp)
            before = rp.role_contract_digest(surface, "mirror")
            self.assertIsNotNone(before)
            fields, _, _, _ = rp.bootstrap(surface, "mirror")
            self.assertEqual(fields["ROLE_CONTRACT_SHA256"], before)
            (surface.root / "roles" / "mirror.md").write_text("# replaced\n", encoding="utf-8")
            after = rp.role_contract_digest(surface, "mirror")
        self.assertNotEqual(before, after,
                            "the bootstrap records a digest precisely so a later read differs")

    def test_a_missing_contract_has_no_digest(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=("roles/mirror.md",))
            self.assertIsNone(rp.role_contract_digest(surface, "mirror"))


# ── P0-G · the dimensions can each go red ──────────────────────────────────────────

class EachDimensionCanGoRed(unittest.TestCase):
    def test_router_that_stops_routing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={"AGENTS.md": "# routes nowhere\n"})
            ok, detail = row(surface, rp.check_router_parity)
        self.assertFalse(ok)
        self.assertIn("no longer routes to CLAUDE.md", detail)

    def test_router_that_drops_a_chain_member(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "AGENTS.md": "read CLAUDE.md and stop there\n"})
            ok, detail = row(surface, rp.check_router_parity)
        self.assertFalse(ok)
        self.assertIn("not named in AGENTS.md", detail)

    def test_actor_id_declaration_can_disappear(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={"AGENTS.md": "CLAUDE.md\n"})
            ok, detail = row(surface, rp.check_actor_id_parity)
        self.assertFalse(ok)
        self.assertIn("assigned", detail)

    def test_a_missing_skill_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=(".claude/skills/legend-start/SKILL.md",))
            ok, detail = row(surface, rp.check_skill_reachability)
        self.assertFalse(ok)
        self.assertIn("legend-start", detail)

    def test_a_second_copy_of_one_skill_fails(self) -> None:
        """The failure the bridge exists to prevent: two sources for one rule."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp)
            body = (surface.root / ".claude/skills/legend-start/SKILL.md").read_bytes()
            copy = surface.root / "vendor" / "copied" / "SKILL.md"
            copy.parent.mkdir(parents=True)
            copy.write_bytes(body)
            subprocess.run(["git", "-C", str(surface.root), "add", "-f", "."],
                           check=True, capture_output=True)
            ok, detail = row(surface, rp.check_skill_reachability)
            rows = rp.skill_report(surface)
        self.assertFalse(ok, "two byte-identical copies must fail the bridge")
        self.assertFalse(rows[0]["NO_DUPLICATED_NORMATIVE_COPY"])
        self.assertEqual(len(rows[0]["copies"]), 2)

    def test_a_fingerprint_that_reads_the_runtime_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "governance/scripts/governance_fingerprint.py":
                    "import os, sys\n"
                    "sys.stdout.write(os.environ.get('LEGEND_RUNTIME', 'none') + '\\n')\n",
            })
            ok, detail = row(surface, rp.check_governance_fingerprint_parity)
        self.assertFalse(ok)
        self.assertIn("differ between runtimes", detail)

    def test_absent_fingerprint_tool_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(
                tmp, omit=("governance/scripts/governance_fingerprint.py",))
            ok, detail = row(surface, rp.check_governance_fingerprint_parity)
        self.assertFalse(ok)
        self.assertIn("absent", detail)

    def test_guard_policy_parity_fails_when_a_runtime_is_more_permissive(self) -> None:
        """The exact bug a naive port ships: argv stringified instead of reduced."""
        original = rp.codex_payload

        def naive(surface, command: str) -> dict:
            return {"hook_event_name": "PreToolUse", "tool_name": "shell_command",
                    "cwd": str(surface.root),
                    "tool_input": {"cmd": "echo " + json.dumps(command)}}
        try:
            rp.codex_payload = naive
            ok, detail = row(REAL, rp.check_guard_policy_parity)
        finally:
            rp.codex_payload = original
        self.assertFalse(ok, "a Codex-only permission must fail GUARD_POLICY_PARITY")
        self.assertIn("codex=allow", detail)

    def test_guard_policy_parity_fails_when_both_sides_agree_on_the_wrong_answer(self) -> None:
        """Agreement is not correctness — two permissive sides agree perfectly.

        This is the arm revision 2 did not have: it compared the runtimes to each other
        and nothing else, so a policy that allowed blanket staging in both would have
        scored PASS.
        """
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                "framework/scripts/pre_tool_use_guard.py": "import sys\nsys.stdin.read()\n",
            })
            ok, detail = row(surface, rp.check_guard_policy_parity)
        self.assertFalse(ok, "a policy that allows everything must not pass by agreeing")
        self.assertIn("expected deny", detail)


# ── P0-H · stages are not promoted by inheritance ──────────────────────────────────

class StagesAreComputedNotInherited(unittest.TestCase):
    def test_every_stage_is_reported(self) -> None:
        names = [stage for stage, _, _, _ in rp.stage_verdicts(REAL)]
        self.assertEqual(names, [s for s, _, _ in rp.STAGES])

    def test_read_only_stages_go_while_write_stages_do_not(self) -> None:
        verdicts = {stage: v for stage, v, _, _ in rp.stage_verdicts(REAL)}
        self.assertEqual(verdicts["MIRROR_READ_ONLY_CODEX"], "GO")
        self.assertEqual(verdicts["MIRROR_WRITE_CODEX"], "NO_GO")
        self.assertEqual(verdicts["PLAN_CODEX"], "NO_GO")
        self.assertEqual(verdicts["ORCHESTRATOR_CODEX"], "NO_GO")

    def test_orchestrator_carries_a_condition_no_other_stage_has(self) -> None:
        """A stage is not the stage below it plus nothing."""
        blockers = {s: b for s, _, b, _ in rp.stage_verdicts(REAL)}
        self.assertTrue(any("LEASE" in b for b in blockers["ORCHESTRATOR_CODEX"]))
        self.assertFalse(any("LEASE" in b for b in blockers["PLAN_CODEX"]),
                         "the lease binds the Orchestrator stage alone")

    def test_a_read_only_stage_goes_red_when_its_own_role_is_unreachable(self) -> None:
        """A stage's own prerequisite, isolated from the shared ones.

        🔴 A missing role contract ALSO breaks `governance_fingerprint.py compose --all`,
        which is a shared row and takes every stage down with it. So the per-stage
        property is asserted on the per-stage row rather than on the verdict, which the
        shared failure would have supplied for free — an assertion that passes for the
        wrong reason is the failure mode this whole file is about.
        """
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, omit=("roles/scientist.md",))
            blockers = {s: b for s, _, b, _ in rp.stage_verdicts(surface)}
            verdicts = {s: v for s, v, _, _ in rp.stage_verdicts(surface)}
        self.assertEqual(verdicts["SCIENTIST_C_READ_ONLY_CODEX"], "NO_GO")
        self.assertIn("ROLE_REACHABILITY", blockers["SCIENTIST_C_READ_ONLY_CODEX"])
        self.assertNotIn("ROLE_REACHABILITY", blockers["MIRROR_READ_ONLY_CODEX"],
                         "one role's missing contract is not another role's blocker")

    def test_a_shared_surface_failure_blocks_every_stage(self) -> None:
        """The complement: when the shared row breaks, no stage is spared."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(
                tmp, omit=("governance/scripts/governance_fingerprint.py",))
            verdicts = {s: v for s, v, _, _ in rp.stage_verdicts(surface)}
        self.assertEqual(set(verdicts.values()), {"NO_GO"})


# ── bootstrap ──────────────────────────────────────────────────────────────────────

class TheBootstrapRefusesRatherThanReports(unittest.TestCase):
    def test_unassigned_actor_id_blocks(self) -> None:
        env = {k: v for k, v in os.environ.items() if k != rp.ACTOR_ID_ENV}
        saved = os.environ.pop(rp.ACTOR_ID_ENV, None)
        try:
            _, blockers, _, _ = rp.bootstrap(REAL, None)
        finally:
            if saved is not None:
                os.environ[rp.ACTOR_ID_ENV] = saved
        self.assertIn("ACTOR_ID is unassigned", blockers)

    def test_undemonstrated_hook_forces_read_only(self) -> None:
        _, blockers, write_blockers, _ = rp.bootstrap(REAL, "mirror")
        self.assertEqual(blockers, [], "the read floor holds, so nothing hard-blocks")
        self.assertIn("HOOK_DEMONSTRATED", write_blockers,
                      "an undemonstrated hook must pin the actor read-only")

    def test_cli_reports_read_only_and_exits_non_zero(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ENTRY), "--bootstrap", "--actor", "mirror"],
            capture_output=True, text=True, cwd=str(REPO),
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("READ_ONLY", result.stdout)
        self.assertIn("WRITE_ENABLED_PARITY", result.stdout)


# ── the residual debt stays declared ───────────────────────────────────────────────

class TheResidualDebtStaysDeclared(unittest.TestCase):
    """What the policy still does not stop, asserted open so closing one is deliberate."""

    def test_every_residual_gap_is_open_and_identical_on_both_sides(self) -> None:
        for label, command in rp.GUARD_RESIDUAL_DEBT:
            with self.subTest(gap=label):
                claude = rp._hook(REAL, rp.claude_payload(REAL, command))
                codex = rp._hook(REAL, rp.codex_payload(REAL, command))
                self.assertEqual(claude, codex,
                                 "a gap that is runtime-specific is an escalation, not debt")
                self.assertEqual(claude, "allow",
                                 "if this now denies, close the debt entry with the fix")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
