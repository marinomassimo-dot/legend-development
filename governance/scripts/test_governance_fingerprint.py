#!/usr/bin/env python3
"""Regression suite for `governance_fingerprint.py` — Annex A.6's resume predicate.

Why this file exists. A.6 refuses to resume a checkpoint whose
`APPLICABLE_GOVERNANCE_FINGERPRINT` no longer matches. That refusal is read as a boolean by a
FROZEN annex, and until this suite existed the tool computing it had no test and sat in no
release inventory — one of exactly two governance tools in that position, the other being the
lease derivation.

Every fixture is a throw-away governance tree. Nothing here reads this repository's own
`governance/`, which matters more than usual: the properties under test are *relational* — a
change here moves that fingerprint and not the other three — and a suite anchored to the live
constitution would go red every time the constitution legitimately moved.

**Each arm that asserts a value is paired with a mutation that must change it.** A fingerprint
test that only checks "the tool prints 64 hex characters" would pass on a tool that returned a
constant, which is the exact failure A.6 cannot survive.

    python3 governance/scripts/test_governance_fingerprint.py
"""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import governance_fingerprint as fingerprint  # noqa: E402

CompositionError = fingerprint.CompositionError


PARAMETERS = """# Plan-defined parameters (fixture)

## P2 · Governance fingerprint

### P2.2 · Pertinence sets

```
CORE = GOVERNANCE_v3.1.1.md
     + annex_a_task_contract.md
     + annex_j_runtime_control_plane.md § J.0
     + <the actor's own role contract>
```

| Role | CORE plus |
|---|---|
| `scientist` (A/B/C) | Annex C |
| `plan` | Annex D, Annex J § J.1 |
| `mirror` | Annex C, Annex D |
| `orchestrator` | Annex C, Annex D, Annex J § J.1 |

### P2.3 · Something after the section, so the slice has an end
"""

ANNEX_J = """# Annex J — runtime control plane (fixture)

## J.0 · What is not guaranteed

No lock exists. This paragraph is J.0 and nothing else.

## J.1 · Event ledger

This paragraph is J.1 and nothing else.

## J.4 · Cost policy

This paragraph is J.4 and is in nobody's fixture pertinence set.
"""


def _tree(root: Path, *, parameters: str = PARAMETERS, annex_j: str = ANNEX_J,
          roles=("plan", "mirror", "orchestrator", "scientist"),
          duplicate_annex_d: bool = False) -> None:
    governance = root / "governance"
    governance.mkdir(parents=True, exist_ok=True)
    (governance / "plan_defined_parameters.md").write_text(parameters, encoding="utf-8")
    (governance / "GOVERNANCE_v3.1.1.md").write_text("# body (fixture)\n", encoding="utf-8")
    (governance / "annex_a_task_contract.md").write_text("# Annex A (fixture)\n", encoding="utf-8")
    (governance / "annex_c_review_protocol.md").write_text("# Annex C (fixture)\n", encoding="utf-8")
    (governance / "annex_d_commit_batch.md").write_text("# Annex D (fixture)\n", encoding="utf-8")
    (governance / "annex_j_runtime_control_plane.md").write_text(annex_j, encoding="utf-8")
    if duplicate_annex_d:
        # Annex D is referenced BY LETTER in the fixture's per-role rows, so this is the
        # only shape of duplicate `_annex_path` is ever asked to resolve. A second
        # `annex_a_*.md` would not reach it: CORE names Annex A by filename.
        (governance / "annex_d_commit_batch_v2.md").write_text("# duplicate\n", encoding="utf-8")
    contracts = root / "roles"
    contracts.mkdir(parents=True, exist_ok=True)
    for role in roles:
        (contracts / f"{role}.md").write_text(f"# contract {role} (fixture)\n", encoding="utf-8")


@contextlib.contextmanager
def governance_tree(**kwargs):
    """Rebind the module's three path globals at a fixture root, and restore them after."""
    saved = (fingerprint.GOVERNANCE_DIR, fingerprint.REPO_ROOT, fingerprint.PARAMETERS)
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        _tree(root, **kwargs)
        fingerprint.REPO_ROOT = root
        fingerprint.GOVERNANCE_DIR = root / "governance"
        fingerprint.PARAMETERS = root / "governance" / "plan_defined_parameters.md"
        try:
            yield root
        finally:
            (fingerprint.GOVERNANCE_DIR,
             fingerprint.REPO_ROOT,
             fingerprint.PARAMETERS) = saved


class ValidComposition(unittest.TestCase):
    def test_every_declared_role_composes(self) -> None:
        with governance_tree():
            values = {role: fingerprint.compose(role)[0]
                      for role in ("plan", "mirror", "orchestrator", "scientist")}
        self.assertEqual(len(values), 4)
        for value in values.values():
            self.assertRegex(value, r"^[0-9a-f]{64}$")

    def test_composition_is_deterministic(self) -> None:
        with governance_tree():
            first = fingerprint.compose("plan")[0]
            second = fingerprint.compose("plan")[0]
        self.assertEqual(first, second)

    def test_distinct_roles_get_distinct_fingerprints(self) -> None:
        """NEGATIVE CONTROL for every arm below: if all four agreed, no mutation could be
        attributed to a role and the role dimension would be decorative."""
        with governance_tree():
            values = [fingerprint.compose(role)[0]
                      for role in ("plan", "mirror", "orchestrator", "scientist")]
        self.assertEqual(len(set(values)), 4)

    def test_the_actors_own_contract_is_in_its_inputs_and_no_other_contract_is(self) -> None:
        with governance_tree():
            inputs = fingerprint.inputs_for("mirror")
        self.assertIn("roles/mirror.md", inputs)
        for other in ("roles/plan.md", "roles/orchestrator.md", "roles/scientist.md"):
            self.assertNotIn(other, inputs)

    def test_inputs_are_sorted_so_declaration_order_cannot_move_the_value(self) -> None:
        with governance_tree():
            inputs = fingerprint.inputs_for("orchestrator")
            baseline = fingerprint.compose("orchestrator")[0]
        self.assertEqual(inputs, sorted(inputs))
        reordered = PARAMETERS.replace(
            "| `orchestrator` | Annex C, Annex D, Annex J § J.1 |",
            "| `orchestrator` | Annex J § J.1, Annex D, Annex C |")
        with governance_tree(parameters=reordered):
            self.assertEqual(fingerprint.compose("orchestrator")[0], baseline)


class MutationArms(unittest.TestCase):
    """A fingerprint that does not move when its inputs move is not a resume predicate."""

    def test_editing_a_core_input_moves_every_role(self) -> None:
        with governance_tree() as root:
            before = {role: fingerprint.compose(role)[0]
                      for role in ("plan", "mirror", "orchestrator", "scientist")}
            (root / "governance/annex_a_task_contract.md").write_text(
                "# Annex A (fixture, edited)\n", encoding="utf-8")
            after = {role: fingerprint.compose(role)[0]
                     for role in ("plan", "mirror", "orchestrator", "scientist")}
        for role in before:
            self.assertNotEqual(before[role], after[role], f"CORE edit did not reach {role}")

    def test_editing_one_roles_own_contract_moves_only_that_role(self) -> None:
        with governance_tree() as root:
            before = {role: fingerprint.compose(role)[0]
                      for role in ("plan", "mirror", "orchestrator", "scientist")}
            (root / "roles/plan.md").write_text("# contract plan (edited)\n", encoding="utf-8")
            after = {role: fingerprint.compose(role)[0]
                     for role in ("plan", "mirror", "orchestrator", "scientist")}
        self.assertNotEqual(before["plan"], after["plan"])
        for role in ("mirror", "orchestrator", "scientist"):
            self.assertEqual(before[role], after[role],
                             f"{role} moved on a change to another actor's contract")

    def test_a_one_byte_edit_is_enough(self) -> None:
        with governance_tree() as root:
            before = fingerprint.compose("plan")[0]
            path = root / "roles/plan.md"
            path.write_text(path.read_text(encoding="utf-8") + " ", encoding="utf-8")
            after = fingerprint.compose("plan")[0]
        self.assertNotEqual(before, after)

    def test_a_section_scoped_input_ignores_edits_outside_its_section(self) -> None:
        """The reason Annex J is split rather than hashed whole, made executable.

        `scientist` carries J.0 and not J.1; editing J.1 must leave it untouched while
        moving `plan`, which carries J.1. Both halves are asserted — a test that only
        checked the invariance would also pass on a tool that hashed nothing at all.
        """
        edited = ANNEX_J.replace("This paragraph is J.1 and nothing else.",
                                 "This paragraph is J.1 and has been edited.")
        with governance_tree():
            before_scientist = fingerprint.compose("scientist")[0]
            before_plan = fingerprint.compose("plan")[0]
        with governance_tree(annex_j=edited):
            after_scientist = fingerprint.compose("scientist")[0]
            after_plan = fingerprint.compose("plan")[0]
        self.assertEqual(before_scientist, after_scientist, "J.1 leaked into a J.0-only set")
        self.assertNotEqual(before_plan, after_plan, "J.1 did not reach the set that carries it")

    def test_a_section_nobody_carries_moves_nothing(self) -> None:
        edited = ANNEX_J.replace("This paragraph is J.4 and is in nobody's fixture pertinence set.",
                                 "Edited J.4.")
        with governance_tree():
            before = [fingerprint.compose(r)[0] for r in ("plan", "mirror", "orchestrator",
                                                          "scientist")]
        with governance_tree(annex_j=edited):
            after = [fingerprint.compose(r)[0] for r in ("plan", "mirror", "orchestrator",
                                                         "scientist")]
        self.assertEqual(before, after)


class RefusesRatherThanGuesses(unittest.TestCase):
    """`CompositionError` is the whole contract: never fall back to a default."""

    def test_missing_parameters_file(self) -> None:
        with governance_tree() as root:
            (root / "governance/plan_defined_parameters.md").unlink()
            with self.assertRaises(CompositionError):
                fingerprint.compose("plan")

    def test_section_p2_2_absent(self) -> None:
        with governance_tree(parameters="# parameters\n\n## P3 · something else\n"):
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("plan")
        self.assertIn("P2.2", str(raised.exception))

    def test_core_block_does_not_parse(self) -> None:
        broken = PARAMETERS.replace("CORE = GOVERNANCE_v3.1.1.md", "CORE_SET: GOVERNANCE_v3.1.1.md")
        with governance_tree(parameters=broken):
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("plan")
        self.assertIn("CORE block", str(raised.exception))

    def test_core_without_the_role_contract_placeholder_is_refused(self) -> None:
        broken = PARAMETERS.replace("     + <the actor's own role contract>\n", "")
        with governance_tree(parameters=broken):
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("plan")
        self.assertIn("own role contract", str(raised.exception))

    def test_no_per_role_rows(self) -> None:
        broken = PARAMETERS
        for role in ("scientist", "plan", "mirror", "orchestrator"):
            broken = "\n".join(line for line in broken.splitlines()
                               if not line.startswith(f"| `{role}`"))
        with governance_tree(parameters=broken):
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("plan")
        self.assertIn("per-role", str(raised.exception))

    def test_a_referenced_artifact_that_does_not_exist(self) -> None:
        """WRONG_REF: the pertinence set names a file nobody wrote."""
        broken = PARAMETERS.replace("| `plan` | Annex D, Annex J § J.1 |",
                                    "| `plan` | annex_z_does_not_exist.md |")
        with governance_tree(parameters=broken):
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("plan")
        self.assertIn("does not exist", str(raised.exception))

    def test_an_unrecognised_reference_shape(self) -> None:
        broken = PARAMETERS.replace("| `plan` | Annex D, Annex J § J.1 |",
                                    "| `plan` | the review annex |")
        with governance_tree(parameters=broken):
            with self.assertRaises(CompositionError):
                fingerprint.compose("plan")

    def test_two_files_claim_the_same_annex_letter(self) -> None:
        """DUPLICATE: `annex_a_*.md` must resolve to exactly one file."""
        with governance_tree(duplicate_annex_d=True):
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("plan")
        self.assertIn("exactly one file", str(raised.exception))

    def test_a_missing_role_contract(self) -> None:
        with governance_tree() as root:
            (root / "roles/mirror.md").unlink()
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("mirror")
        self.assertIn("role contract missing", str(raised.exception))

    def test_an_unknown_role(self) -> None:
        with governance_tree():
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("archivist")
        self.assertIn("unknown role", str(raised.exception))

    def test_a_section_that_is_not_in_the_annex(self) -> None:
        with governance_tree(annex_j=ANNEX_J.replace("## J.0 ·", "## J.9 ·")):
            with self.assertRaises(CompositionError) as raised:
                fingerprint.compose("plan")
        self.assertIn("not found", str(raised.exception))

    def test_mutation_arm_every_refusal_above_composes_once_repaired(self) -> None:
        """The refusals are informative only because the unbroken fixture succeeds."""
        with governance_tree():
            self.assertRegex(fingerprint.compose("plan")[0], r"^[0-9a-f]{64}$")


class SectionSlicing(unittest.TestCase):
    def test_a_section_slice_is_not_the_whole_file(self) -> None:
        with governance_tree():
            whole = fingerprint._digest("governance/annex_j_runtime_control_plane.md")
            sliced = fingerprint._digest("governance/annex_j_runtime_control_plane.md#J.0")
        self.assertNotEqual(whole, sliced)

    def test_a_section_slice_stops_at_the_next_heading_of_equal_level(self) -> None:
        with governance_tree():
            j0 = fingerprint._digest("governance/annex_j_runtime_control_plane.md#J.0")
        shortened = ANNEX_J.replace("## J.4 · Cost policy\n\n"
                                    "This paragraph is J.4 and is in nobody's "
                                    "fixture pertinence set.\n", "")
        with governance_tree(annex_j=shortened):
            j0_again = fingerprint._digest("governance/annex_j_runtime_control_plane.md#J.0")
        self.assertEqual(j0, j0_again)


class CommandLine(unittest.TestCase):
    def _main(self, *argv: str) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        saved = sys.argv
        sys.argv = ["governance_fingerprint.py", *argv]
        try:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = fingerprint.main()
        finally:
            sys.argv = saved
        return code, out.getvalue(), err.getvalue()

    def test_compose_all_prints_one_line_per_role_and_exits_zero(self) -> None:
        with governance_tree():
            code, out, _ = self._main("compose", "--all")
        self.assertEqual(code, 0)
        self.assertEqual(len(out.strip().splitlines()), 4)

    def test_a_composition_failure_exits_two_and_says_so(self) -> None:
        with governance_tree(parameters="# nothing here\n"):
            code, _, err = self._main("compose", "--all")
        self.assertEqual(code, 2)
        self.assertIn("COMPOSITION FAILED", err)

    def test_mutation_arm_the_same_invocation_on_a_sound_tree_exits_zero(self) -> None:
        with governance_tree():
            code, _, _ = self._main("compose", "--all")
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
