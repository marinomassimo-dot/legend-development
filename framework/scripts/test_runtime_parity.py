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
        """§ 38, mechanically: CONFIGURED != PROVEN.

        🔴 The real surface now derives NOT_LOADED rather than TRUST_PENDING, and the
        change is a strengthening, not a relaxation: revision 7 could not tell a hook
        awaiting review from a hook that was never registered, so it said the kinder of
        the two. `hooks/list` tells them apart, and for every LEGEND worktree the
        answer is zero. Both states are asserted non-passing, and the assertion that
        carries the weight is the second one.
        """
        state = rp.hook_status(REAL)[0]
        self.assertIn(state, (rp.NOT_LOADED, rp.TRUST_PENDING, rp.UNDERIVABLE))
        for unpassing in (rp.TRUST_PENDING, rp.NOT_LOADED, rp.CONFIGURED,
                          rp.NOT_CONFIGURED, rp.NOT_FIRING, rp.UNDERIVABLE):
            self.assertNotIn(unpassing, rp.PASSING_HOOK_STATES)

    def test_not_loaded_is_strictly_worse_than_trust_pending(self) -> None:
        """A registration that never loaded is not on either side of the trust gate.

        Reporting TRUST_PENDING for it names a gate it never reached, and that is the
        sentence revision 7 shipped for a registration that policed nothing in every
        worktree for every actor.
        """
        self.assertNotEqual(rp.NOT_LOADED, rp.TRUST_PENDING)
        self.assertNotIn(rp.NOT_LOADED, rp.PASSING_HOOK_STATES)

    #: A receipt that identifies the engine that answered. Every field below is required,
    #: and the tests underneath remove them one at a time.
    DISCRIMINATING_RECEIPT = {
        "schema": "codex_hook_probe/2", "recorded_on": "2026-08-30",
        "codex_version": "0.150.0-alpha.8", "cwd": "/x",
        "probe_command": "git -C <PEER_WORKTREE> commit -m x <path>",
        "observed": "REFUSED", "guard_generation": "REV12",
        "decision_codes": {"2": "CONFINED_PEER_WORKTREE"},
    }

    def _status(self, tmp, receipt):
        surface = build_fixture(tmp, rewrite={
            "framework/state/codex_hook_probe.json": json.dumps(receipt)})
        return rp.hook_status(surface)[0], surface

    def test_a_refusal_receipt_reaches_demonstrated(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            state, surface = self._status(tmp, self.DISCRIMINATING_RECEIPT)
            self.assertEqual(state, rp.DEMONSTRATED)
            self.assertTrue(row(surface, rp.check_hook_demonstrated)[0])

    def test_the_revision_9_receipt_shape_no_longer_reaches_demonstrated(self) -> None:
        """🔴 R2, where it actually bites: the INSTRUMENT, not the protocol document.

        Revision 9 returned `DEMONSTRATED` from `observed == "REFUSED"` alone. The legacy
        single-file guard on `main` refuses `git add -A` too, with byte-identical text — so
        that receipt records that A guard ran and nothing about WHICH. It is the false GO
        the whole R2 repair exists to prevent, and it lived in this branch while the
        protocol document was being rewritten around it.

        Repairing the description of a control and leaving the control reading one bit is
        the shape of a repair that changes no behaviour.
        """
        with tempfile.TemporaryDirectory() as tmp:
            state, _ = self._status(tmp, {
                "schema": "codex_hook_probe/1", "recorded_on": "2026-08-28",
                "codex_version": "0.150.0-alpha.8", "cwd": "/x",
                "probe_command": "git add -A", "observed": "REFUSED"})
            self.assertEqual(state, rp.UNDERIVABLE)
            self.assertNotIn(state, rp.PASSING_HOOK_STATES)

    def test_a_refusal_without_a_discriminating_code_is_underivable(self) -> None:
        """The right schema and generation, and the code of the ONE refusal both engines
        produce. It identifies neither, and must not pass."""
        with tempfile.TemporaryDirectory() as tmp:
            state, _ = self._status(tmp, {
                **self.DISCRIMINATING_RECEIPT,
                "probe_command": "git add -A",
                "decision_codes": {"3": "BLANKET_STAGING"}})
            self.assertEqual(state, rp.UNDERIVABLE)

    def test_a_refusal_recording_the_wrong_generation_is_underivable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            state, _ = self._status(tmp, {**self.DISCRIMINATING_RECEIPT,
                                          "guard_generation": "REV9"})
            self.assertEqual(state, rp.UNDERIVABLE)

    def test_an_older_schema_is_refused_even_carrying_every_newer_field(self) -> None:
        """🔴 The schema gate, made load-bearing — and it was not.

        A mutation deleting the schema check SURVIVED: a revision-9 receipt has no
        `guard_generation`, so the next check caught it anyway, and the two tests above
        passed with the gate gone. That is an EQUIVALENT MUTANT only for the receipts
        anyone has actually written; it is not equivalent for this one.

        A receipt that declares `codex_hook_probe/1` and then carries every v2 field is a
        producer that did not agree to the v2 contract. `pre_tool_use_guard` already
        applies this rule to its own payloads — *a payload declaring a schema this parser
        does not implement is not a schema it may read leniently* — and the same rule
        holds for a receipt that a spend produced.
        """
        with tempfile.TemporaryDirectory() as tmp:
            state, _ = self._status(tmp, {**self.DISCRIMINATING_RECEIPT,
                                          "schema": "codex_hook_probe/1"})
            self.assertEqual(state, rp.UNDERIVABLE)
        with tempfile.TemporaryDirectory() as tmp:
            state, _ = self._status(tmp, {**self.DISCRIMINATING_RECEIPT,
                                          "schema": "codex_hook_probe/3"})
            self.assertEqual(state, rp.UNDERIVABLE,
                             "a LATER schema is refused too: this parser implements one "
                             "contract, and a future one may mean something else by the "
                             "same field names")

    def test_the_blanket_staging_code_is_excluded_from_the_discriminators(self) -> None:
        """🔴 The table, not an example. `BLANKET_STAGING` is the code for the one command
        both engines refuse identically; every other code is one the legacy engine has no
        branch for. An empty discriminator table would make every receipt UNDERIVABLE,
        which is safe but useless, so the size is asserted too."""
        self.assertNotIn("BLANKET_STAGING", rp.PROBE_DISCRIMINATING_CODES)
        self.assertIn("CONFINED_PEER_WORKTREE", rp.PROBE_DISCRIMINATING_CODES)
        self.assertIn("RUNTIME_CONFIG", rp.PROBE_DISCRIMINATING_CODES)
        self.assertGreater(len(rp.PROBE_DISCRIMINATING_CODES), 10)

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
        self.assertNotIn(rp.DEMONSTRATED, result.stdout.split("\n")[0])
        self.assertTrue(
            any(state in result.stdout for state in
                (rp.NOT_LOADED, rp.TRUST_PENDING, rp.UNDERIVABLE)),
            "the CLI must name which undemonstrated state it is in")


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

    def test_a_missing_matcher_for_a_tool_the_runtime_uses_is_named(self) -> None:
        """The condition a failing sibling row was hiding.

        🔴 Found by mutation M25: `NO_RUNTIME_AUTHORITY_ESCALATION` already fails today on
        the hook state, so deleting the matcher check entirely changed no verdict and no
        test noticed. The row's *detail* is therefore asserted, not just its boolean —
        which is the only way to test one condition of a check that has several.
        """
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                ".codex/config.toml":
                    '[hooks]\nPreToolUse = [{ matcher = "shell_command", hooks = ['
                    '{ type = "command", command = '
                    '"python3 framework/scripts/pre_tool_use_guard.py" }] }]\n',
            })
            _, detail = row(surface, rp.check_no_runtime_authority_escalation)
        self.assertIn("no matcher for Codex tool `exec`", detail)
        self.assertIn("no matcher for Codex tool `unified_exec`", detail)

    def test_the_real_registration_declares_every_tool_the_check_requires(self) -> None:
        _, detail = row(REAL, rp.check_no_runtime_authority_escalation)
        self.assertNotIn("no matcher", detail,
                         "the shipped registration must not be missing a matcher")

    def test_matchers_are_whole_values_not_substrings(self) -> None:
        """`exec` is a substring of `unified_exec`, and that once passed the check."""
        with tempfile.TemporaryDirectory() as tmp:
            surface = build_fixture(tmp, rewrite={
                ".codex/config.toml":
                    '[hooks]\nPreToolUse = [{ matcher = "unified_exec", hooks = ['
                    '{ type = "command", command = '
                    '"python3 framework/scripts/pre_tool_use_guard.py" }] }]\n',
            })
            declared = rp.codex_matchers(surface)
            _, detail = row(surface, rp.check_no_runtime_authority_escalation)
        self.assertEqual(declared, {"unified_exec"})
        self.assertIn("no matcher for Codex tool `exec`", detail,
                      "a substring test would have reported `exec` as declared")

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

    def test_every_closed_gap_stays_closed_on_both_sides(self) -> None:
        """🔴 The mirror assertion, and the one revision 7 did not have.

        A table that only asserts gaps are OPEN cannot notice one re-opening. Every
        family revision 8 closed is pinned here in the deny direction, in BOTH
        runtimes, so a later edit that restores a bypass fails as loudly as closing one
        used to — and closing a gap without moving its entry fails too.
        """
        probed = 0
        for label, template in rp.GUARD_CLOSED_DEBT:
            with self.subTest(gap=label):
                command = rp.expand_placeholders(template, REAL)
                if command is None:
                    self.skipTest(f"{label!r} needs a topology this surface lacks")
                probed += 1
                claude = rp._hook(REAL, rp.claude_payload(REAL, command))
                codex = rp._hook(REAL, rp.codex_payload(REAL, command))
                self.assertEqual(claude, codex,
                                 "a control on one side only is an escalation by runtime")
                self.assertEqual(claude, "deny",
                                 f"{label!r} was closed and is open again")
        # 🔴 A loop that skipped every case is a green test that measured nothing, and
        # `skipTest` inside `subTest` does not fail the method. The counter is what makes
        # "all closed" distinguishable from "none asked".
        self.assertGreater(probed, 0, "no closed-debt entry was actually probed")

    def test_the_positive_floor_survives_in_both_runtimes(self) -> None:
        """A write-control system that blocks everything is not a write-control system.

        FORBIDDEN_WRITE → REFUSED is half a claim. This is the other half, and it runs
        against the SAME policy revision, the SAME engine and both payload shapes, so
        the two halves cannot be measured on different trees.
        """
        for label, command in rp.GUARD_POSITIVE_FLOOR:
            with self.subTest(act=label):
                claude = rp._hook(REAL, rp.claude_payload(REAL, command))
                codex = rp._hook(REAL, rp.codex_payload(REAL, command))
                self.assertEqual(claude, codex,
                                 "an act permitted in one runtime only is an escalation")
                self.assertEqual(claude, "allow",
                                 f"{label!r} is how work lands here and it is refused")


class TheBridgesOwnFilesDoNotAddSurfaceDefects(unittest.TestCase):
    """A delta check, because the absolute one is already red and cannot report a new fault.

    🔴 `scripts/test_release_surface.py` asserts that no tracked `#!` file sits at mode
    `100644`. It has been red for four pre-existing files for weeks, so when this candidate
    added a fifth, and then a sixth, and then a seventh, the suite said exactly what it had
    always said. Two of them were caught only because a peer's tool counted offenders; the
    third was caught only because that count was re-run.

    Fixing each instance was not fixing the class. This is the class: the bridge's own file
    set, asserted to add nothing — a check that can be GREEN, and therefore a check that can
    change to red and mean something.
    """

    #: 🔴 REVISION 9: the list is DERIVED, and the hand-written one is why it was green.
    #:
    #: Revision 8 added five modules and four suites to this bridge and extended this
    #: tuple by none of them. All nine were committed at `100644`, `test_release_surface`
    #: went from four offenders to thirteen, and THIS test — the one written to be the
    #: class fix — stayed green, because a hand-maintained list of what to check does
    #: not grow when someone adds a file. A check that only sees what its author
    #: remembered to enumerate is a check that reports on its author's memory.
    #:
    #: `framework/scripts/` is the bridge's directory and every file in it is an
    #: entrypoint by convention; deriving from the tracked set means a module added
    #: tomorrow is covered the moment it is tracked, with nobody remembering anything.
    EXPLICIT = (
        "scripts/guard_bash_command.py",
        "scripts/test_guard_bash_command.py",
    )

    @property
    def OWNED(self):
        tracked = rp._git(REAL, "ls-files", "framework/scripts").splitlines()
        return tuple(sorted(p for p in tracked if p.endswith(".py"))) + self.EXPLICIT

    def test_every_owned_file_is_tracked(self) -> None:
        """The list is the point; a stale entry would make the next test vacuous."""
        tracked = set(rp._git(REAL, "ls-files").splitlines())
        missing = [path for path in self.OWNED if path not in tracked]
        self.assertEqual([], missing, "this list names a file the repository does not track")

    def test_the_owned_set_actually_grew_with_the_bridge(self) -> None:
        """🔴 A derived list can also be derived WRONG — an empty glob would make the
        mode check below pass over nothing. Ten was the hand-written count."""
        self.assertGreater(len(self.OWNED), 10)
        for required in ("framework/scripts/effect_model.py",
                         "framework/scripts/repo_topology.py",
                         "framework/scripts/post_effect_verify.py",
                         "framework/scripts/hostile_corpus.py"):
            self.assertIn(required, self.OWNED)

    def test_no_owned_shebang_file_sits_at_mode_100644(self) -> None:
        entries = rp._git(REAL, "ls-tree", "-r", "HEAD").splitlines()
        modes = {}
        for line in entries:
            meta, _, path = line.partition("\t")
            modes[path] = meta.split()[0]
        offenders = []
        for path in self.OWNED:
            body = (REPO / path).read_bytes()[:2]
            if body == b"#!" and modes.get(path) == "100644":
                offenders.append(path)
        self.assertEqual([], offenders,
                         "a shebang entrypoint committed non-executable; run "
                         "`git add --chmod=+x <path>`")

    def test_the_check_can_see_an_offender(self) -> None:
        """POSITIVE CONTROL. A green delta check that cannot detect is worse than a red one.

        🔴 This control used to scan the LIVE tree and assert that at least one 100644
        shebang `.py` file existed — "four are known to exist". Repairing all of them made
        it fail, which is the wrong direction for a repository to be pushed in: a control
        that needs the tree to stay defective rewards leaving defects in place, and would
        have been "fixed" by reverting a real repair. The predicate is now exercised
        against a purpose-built fixture, so it proves the detector can see an offender
        without requiring one to exist here.

        The two assertions above it are kept and still run against the real tree, because
        "ls-tree returns entries" and "the mode field is being read at all" are properties
        of the REAL surface and a fixture cannot vouch for them.
        """
        entries = rp._git(REAL, "ls-tree", "-r", "HEAD").splitlines()
        self.assertTrue(entries, "ls-tree returned nothing, so the check above tested nothing")
        modes = {line.partition("\t")[2]: line.split()[0] for line in entries}
        self.assertIn("100755", set(modes.values()),
                      "no executable file at all — the mode field is not being read")

        def offenders(root: Path, tree_modes: dict) -> list:
            return [p for p, m in tree_modes.items()
                    if m == "100644" and p.endswith(".py")
                    and (root / p).exists() and (root / p).read_bytes()[:2] == b"#!"]

        with tempfile.TemporaryDirectory() as tmp:
            fixture = Path(tmp)
            for name, mode in (("offender.py", 0o644), ("proper.py", 0o755),
                               ("plain.py", 0o644)):
                target = fixture / name
                target.write_text(
                    "#!/usr/bin/env python3\n" if name != "plain.py" else "x = 1\n",
                    encoding="utf-8")
                target.chmod(mode)
            for argv in (["init", "-q"], ["add", "-A"],
                         ["-c", "user.email=t@t", "-c", "user.name=t",
                          "commit", "-q", "-m", "fixture"]):
                subprocess.run(["git", "-C", str(fixture), *argv],
                               capture_output=True, text=True, check=True)
            lines = rp._git(rp.Surface(fixture), "ls-tree", "-r", "HEAD").splitlines()
            fixture_modes = {ln.partition("\t")[2]: ln.split()[0] for ln in lines}
            self.assertEqual(
                ["offender.py"], sorted(offenders(fixture, fixture_modes)),
                "the predicate must find the shebang file at 100644, and only it — "
                f"`proper.py` is executable and `plain.py` has no shebang: {fixture_modes}")

        # The live tree is REPORTED, never asserted on: zero offenders here is the goal
        # state, not a failure, and this line is what tells a reader which it is looking at.
        print(f"\n    live-tree shebang offenders: {sorted(offenders(REPO, modes))}")


class TheCandidateFinalisationChecksItsOwnModes(unittest.TestCase):
    """🔴 R11. The committed object is correct and the INDEX is where it can go wrong.

    `chmod` needs `REF_WRITE`, which no runtime, role or lease grants, so the executable
    bit is set with `git add --chmod=+x` and the working tree's on-disk bit stays `644`.
    That residue is cosmetic. What is not cosmetic is the consequence: **a later plain
    `git add` on one of these files silently reverts the mode**, because `git add` reads
    the on-disk bit. It has already happened twice in this candidate series — commit
    `744e0bc` did it to two files, and the repair had to be committed again.

    So the finalisation check is on the INDEX against HEAD, which is exactly where a
    reverted mode shows up before it is committed, and it is the one place a reviewer
    can be shown "nothing about the mode moved in this commit".
    """

    def modes(self, *args):
        out = {}
        for line in rp._git(REAL, *args).splitlines():
            meta, _, path = line.partition("\t")
            out[path] = meta.split()[0]
        return out

    def owned(self):
        tracked = rp._git(REAL, "ls-files", "framework/scripts").splitlines()
        return sorted(p for p in tracked if p.endswith(".py"))

    def test_the_index_mode_matches_the_committed_mode_for_every_owned_file(self):
        """A plain `git add` that reverted an executable bit shows up HERE, staged and
        not yet committed, which is the only moment it can still be repaired cheaply."""
        head = self.modes("ls-tree", "-r", "HEAD")
        index = {}
        for line in rp._git(REAL, "ls-files", "-s", "framework/scripts").splitlines():
            meta, _, path = line.partition("\t")
            index[path] = meta.split()[0]
        drifted = [p for p in self.owned()
                   if p in head and index.get(p) != head[p]]
        self.assertEqual(
            [], drifted,
            "the index disagrees with HEAD about a mode. A plain `git add` reads the "
            "on-disk bit and reverts it; re-stage with `git add --chmod=+x <path>`")

    def test_the_check_reads_a_real_mode_field(self):
        """POSITIVE CONTROL. A comparison over two empty dictionaries agrees perfectly."""
        head = self.modes("ls-tree", "-r", "HEAD")
        self.assertTrue(head, "ls-tree returned nothing, so the check above compared "
                              "two empty maps and agreed")
        self.assertIn("100755", set(head.values()))
        self.assertTrue(self.owned(), "no owned file was enumerated")

    def test_a_path_described_as_mode_residue_really_is_mode_only(self):
        """🔴 The honest half. The on-disk bit CANNOT be repaired at this authority —
        `chmod` inside the repository is `REF_WRITE`, and the guard refuses it, correctly
        (measured: the denial says so). So the candidate reports a worktree residue, and
        the claim that has to be falsifiable is *that it is only a mode*.

        This cross-references the two things git says about the same paths: a path listed
        by `--summary` as a mode change must be listed by `--numstat` as `0 0`. A path
        that is both a mode change AND a content change is not residue, and describing it
        as residue in a candidate manifest would hide a content edit behind a cosmetic
        word.

        It says nothing about paths that carry content changes for ordinary reasons —
        during development that is most of them, and a check that failed on those would
        be a check nobody could run while working.
        """
        changes = [line.strip() for line in
                   rp._git(REAL, "diff", "--summary", "--",
                           "framework/scripts").splitlines()
                   if line.strip().startswith("mode change")]
        for line in changes:
            with self.subTest(change=line):
                self.assertIn(
                    "100755 => 100644", line,
                    "every worktree mode difference here must be the KNOWN residue — "
                    "the disk losing an executable bit the index and HEAD still carry. "
                    "The other direction is an executable bit appearing from nowhere, "
                    "which is a grant of authority and not a cosmetic leftover")

    def test_every_committed_executable_owned_file_is_an_entrypoint(self):
        """The other half of the mode claim, and the one that is always checkable.

        `100755` on a tracked file says *anyone may run this*. Asserting that every owned
        file carrying that mode begins with a shebang is what keeps the executable bit a
        statement about entrypoints rather than a mode someone once staged."""
        head = self.modes("ls-tree", "-r", "HEAD")
        checked = 0
        for path in self.owned():
            if head.get(path) != "100755":
                continue
            with self.subTest(path=path):
                checked += 1
                self.assertEqual((REPO / path).read_bytes()[:2], b"#!")
        self.assertGreater(checked, 10, "no executable owned file was examined")


class ThePeerPlaceholdersAreDerivedAndNotThisMachinesLayout(unittest.TestCase):
    """🔴 R4. Three debt entries hard-coded `../mirror` beside a placeholder table.

    On a host whose layout has no `../mirror`, those rows silently changed from
    measuring `PEER_WORKTREE` to measuring `OUTSIDE_REPO` — no skip, no warning, and a
    green probe that names one thing and measures another. The rule the fresh-clone case
    pins is that a peer path is DERIVED, so a surface with no peer SKIPS.
    """

    def fresh_clone(self):
        raw = tempfile.mkdtemp(prefix="fresh-clone-")
        self.addCleanup(shutil.rmtree, raw, ignore_errors=True)
        destination = Path(raw) / "clone"
        out = subprocess.run(["git", "clone", "-q", "--no-local", "--depth", "1",
                              str(REPO), str(destination)],
                             capture_output=True, text=True)
        if out.returncode != 0:
            self.skipTest(f"the clone did not succeed: {out.stderr[:200]}")
        return rp.Surface(destination)

    def test_no_debt_entry_hard_codes_a_peer_worktree_name(self):
        """The committed text must name no directory this machine happens to have."""
        for table in (rp.GUARD_CLOSED_DEBT, rp.GUARD_RESIDUAL_DEBT,
                      rp.GUARD_POSITIVE_FLOOR):
            for label, command in table:
                with self.subTest(entry=label):
                    self.assertNotIn("../mirror", command)
                    self.assertNotIn("/Users/", command)

    def test_a_fresh_clone_skips_the_peer_entries_instead_of_measuring_something_else(self):
        """🔴 The requirement, executed rather than asserted: a clone has ONE working
        tree, so every peer placeholder is unresolvable and every row that needs one
        must come back `None`."""
        surface = self.fresh_clone()
        needs_a_peer = [(label, command)
                        for label, command in rp.GUARD_CLOSED_DEBT
                        if "<WORKTREE_B" in command]
        self.assertGreaterEqual(len(needs_a_peer), 4,
                                "no entry needs a peer, so this test measures nothing")
        for label, command in needs_a_peer:
            with self.subTest(entry=label):
                self.assertIsNone(rp.expand_placeholders(command, surface),
                                  "a peer placeholder that cannot be resolved must "
                                  "yield None so the caller SKIPS")

    def test_the_same_entries_do_resolve_where_a_peer_exists(self):
        """The positive control: `None` everywhere would satisfy the test above.

        🔴 It SKIPS where there is no peer, and that is not a weakening — this surface is
        whatever tree the suite is run from, and in a clone there is one. A control that
        FAILED there would be asserting that the machine has a particular layout, which is
        the defect this whole class exists to remove.
        """
        import repo_topology as topo  # noqa: PLC0415 - only on this path
        if not topo.of_assigned(str(REAL.root)).peer_worktrees:
            self.skipTest("this surface has no peer worktree; the negative arm covers it")
        resolved = 0
        for label, command in rp.GUARD_CLOSED_DEBT:
            if "<WORKTREE_B" not in command:
                continue
            filled = rp.expand_placeholders(command, REAL)
            if filled is not None:
                resolved += 1
                self.assertNotIn("<WORKTREE_B", filled)
        self.assertGreater(resolved, 0,
                           "no peer placeholder resolved even here, so the skip above "
                           "proves nothing about the placeholder machinery")

    def test_the_shared_checkout_placeholder_never_names_this_tree(self):
        """🔴 The R4 defect one placeholder further on, found in a fresh clone.

        `<REPO>` is the shared checkout, and in a single-worktree checkout that IS the
        surface's own root. `echo x > <REPO>/CLAUDE.md` then stops being a cross-checkout
        write and becomes an ordinary write into the actor's own tree — still DENY, for an
        entirely different rule, with nothing saying so. `git -C <REPO> add CLAUDE.md`
        becomes ordinary named staging and is ALLOWED, so that row fails on a clone and
        passes in a worktree.

        A row that measures a different family depending on the host's layout is exactly
        what R4 is about, and this half was invisible until the suite was run in a clone.
        """
        surface = self.fresh_clone()
        for label, command in rp.GUARD_CLOSED_DEBT:
            if "<REPO>" not in command:
                continue
            with self.subTest(entry=label):
                self.assertIsNone(
                    rp.expand_placeholders(command, surface),
                    "a shared-checkout row must SKIP where the shared checkout is this "
                    "tree, not silently measure a different rule")

    def test_the_shared_checkout_placeholder_resolves_where_it_is_a_different_tree(self):
        """The positive control for the rule above."""
        import repo_topology as topo  # noqa: PLC0415 - only on this path
        topology = topo.of_assigned(str(REAL.root))
        if not topology.shared_checkout or \
                Path(topology.shared_checkout).resolve() == REAL.root:
            self.skipTest("this surface IS its own shared checkout")
        filled = rp.expand_placeholders("echo x > <REPO>/CLAUDE.md", REAL)
        self.assertIsNotNone(filled)
        self.assertNotIn("<REPO>", filled)

    def test_the_relative_spelling_is_preserved_and_still_points_at_the_peer(self):
        """The relative cases are ABOUT the spelling, so deriving them must not turn
        them into absolute paths."""
        command = rp.expand_placeholders(
            "echo x > <WORKTREE_B_REL>/framework/pwned.md", REAL)
        if command is None:
            self.skipTest("this surface has no peer worktree")
        target = command.split("> ", 1)[1]
        self.assertFalse(target.startswith("/"), "the relative case must stay relative")
        self.assertTrue(target.startswith(".."), "and must climb out of this worktree")

    def test_the_dash_C_entry_is_sensitive_to_its_target(self):
        """🔴 `git -C <peer> commit -am x` denied because of `-a`, identically with a
        peer, with a nonexistent directory and with no `-C` at all. The entry now names
        a path, and the same command WITHOUT `-C` is in the positive floor — so if both
        denied, the row would be recording blanket staging under another name."""
        entry = dict(rp.GUARD_CLOSED_DEBT)["git run in a peer worktree"]
        self.assertNotIn("-am", entry)
        self.assertNotIn("-a ", entry)
        command = rp.expand_placeholders(entry, REAL)
        if command is None:
            self.skipTest("this surface has no peer worktree")
        without = command.split(" commit", 1)[1]
        self.assertEqual(rp._hook(REAL, rp.claude_payload(REAL, command)), "deny")
        self.assertEqual(rp._hook(REAL, rp.claude_payload(REAL, "git commit" + without)),
                         "allow",
                         "the SAME command without -C must be allowed, or the entry is "
                         "measuring something other than its target")


if __name__ == "__main__":
    sys.exit(0 if unittest.main(exit=False, verbosity=2).result.wasSuccessful() else 1)
