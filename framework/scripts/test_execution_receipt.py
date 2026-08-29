#!/usr/bin/env python3
"""RECEIPT BINDING — and the one thing a receipt must never be allowed to do.

A receipt that records a verdict without its provenance proves nothing. Revision 7
wrote that sentence about the Codex hook probe and asserted it there; here it is the
validator's entire job, applied to a ledger about the control plane rather than about
the scientific corpus.
"""
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import effect_model as em  # noqa: E402
import execution_attestation as ea  # noqa: E402
import execution_receipt as er  # noqa: E402


def binding(**overrides) -> ea.Binding:
    fields = dict(
        actor="plan", runtime="claude-code", runtime_version="2.1.232",
        session="sess-abc", task=ea.task_fingerprint("rev8"),
        worktree="/repo/wt", branch="rev8", head="a" * 40,
        authority="SHELL_DEFAULT",
    )
    fields.update(overrides)
    return ea.Binding(**fields)


def report(**overrides) -> dict:
    base = {
        "command": "git add framework/x",
        "predicted_effect": [em.Effect(em.STAGE, "framework/x", em.INSIDE_REPO).as_dict()],
        "authorized_effect": [em.Effect(em.STAGE, "framework/x", em.INSIDE_REPO).as_dict()],
        "observed_effect": [em.Effect(em.STAGE, "framework/x", em.INSIDE_REPO).as_dict()],
        "head_before": "a" * 40,
        "head_after": "a" * 40,
        "result": "WRITE_RESULT_VALID",
        "match": em.MATCH,
        # ── revision 9 ──
        #
        # 🔴 A COMPLETE report carries these, and the fixture supplies them because the
        # suite's job is to test the receipt and not to freeze the report's shape at
        # revision 8. `test_a_receipt_missing_any_required_field_is_invalid` iterates
        # `er.REQUIRED`, so these four are covered in the missing direction the moment
        # they were declared required — which is why adding them here does not weaken
        # anything: the negative arm is generated from the table, not written by hand.
        "repository_id": "/repo/.git",
        "effective_workdir": "/repo/wt",
        "target_scope": em.INSIDE_REPO,
        "guard_generation": "REV9",
        "guard_policy_hash": "0" * 16,
    }
    base.update(overrides)
    return base


class AReceiptNamesTheBasisOfItsOwnVerdict(unittest.TestCase):
    """🔴 Revision 9: which repository, which base, which policy.

    A receipt that omits these is not merely less informative — it is not comparable
    with any other receipt. `GUARD_REVISION_UNIFORM` is NO across this repository, so
    two receipts from two worktrees were produced by two different rule sets, and a
    reader who assumes otherwise is comparing verdicts that do not share a basis.
    """

    def test_the_repository_the_worktree_and_the_engine_are_all_recorded(self) -> None:
        receipt = er.build(binding(), report())
        for field in ("repository_id", "effective_workdir",
                      "guard_generation", "guard_policy_hash"):
            with self.subTest(field=field):
                self.assertIn(field, er.REQUIRED)
                self.assertTrue(receipt[field])
                self.assertNotEqual(receipt[field], ea.UNDERIVABLE)

    def test_repository_identity_is_not_the_worktree(self) -> None:
        """Two worktrees of one repository share an object store and not a toplevel."""
        receipt = er.build(binding(), report())
        self.assertNotEqual(receipt["repository_id"], receipt["worktree"])

    def test_an_absent_field_is_never_filled_from_the_recorders_environment(self) -> None:
        """🔴 A gap becomes UNDERIVABLE, never this machine's own topology — otherwise
        every receipt describes the process that read it rather than the run."""
        thin = {k: v for k, v in report().items()
                if k not in ("repository_id", "effective_workdir", "guard_generation",
                             "guard_policy_hash")}
        receipt = er.build(binding(), thin)
        for field in ("repository_id", "effective_workdir", "guard_generation",
                      "guard_policy_hash"):
            with self.subTest(field=field):
                self.assertEqual(receipt[field], ea.UNDERIVABLE)
        ok, problems = er.validate(receipt)
        self.assertFalse(ok, "an unbound receipt must not validate")
        self.assertTrue(problems)

    def test_the_effective_workdir_is_what_gives_the_action_a_meaning(self) -> None:
        """`echo x > framework/probe.md` is a repository write or a scratch write
        depending entirely on this field, so it may not be UNDERIVABLE."""
        self.assertNotIn("effective_workdir", er.MAY_BE_UNDERIVABLE)
        self.assertNotIn("repository_id", er.MAY_BE_UNDERIVABLE)


class AReceiptWithoutProvenanceProvesNothing(unittest.TestCase):

    def test_a_complete_receipt_validates(self) -> None:
        ok, problems = er.validate(er.build(binding(), report()))
        self.assertTrue(ok, problems)

    def test_a_receipt_missing_any_required_field_is_invalid(self) -> None:
        """Asserted over REQUIRED, not over the fields someone remembered to remove."""
        complete = er.build(binding(), report())
        for field in er.REQUIRED:
            with self.subTest(field=field):
                truncated = {k: v for k, v in complete.items() if k != field}
                ok, problems = er.validate(truncated)
                self.assertFalse(ok, f"a receipt without {field!r} validated")

    def test_a_verdict_alone_is_not_a_receipt(self) -> None:
        ok, _ = er.validate({"schema": er.SCHEMA, "result": "WRITE_RESULT_VALID"})
        self.assertFalse(ok)

    def test_underivable_is_allowed_only_where_it_is_declared_allowed(self) -> None:
        for field in ("actor", "worktree", "branch", "head_before", "authority"):
            with self.subTest(field=field):
                receipt = er.build(binding(), report())
                receipt[field] = ea.UNDERIVABLE
                receipt["receipt_id"] = _reseal(receipt)
                self.assertFalse(er.validate(receipt)[0])
        for field in ("session", "tool_call_id", "transcript"):
            with self.subTest(field=field, allowed=True):
                receipt = er.build(binding(session=None), report())
                receipt[field] = ea.UNDERIVABLE
                receipt["receipt_id"] = _reseal(receipt)
                self.assertTrue(er.validate(receipt)[0], f"{field} may be UNDERIVABLE")

    def test_a_receipt_cannot_assert_its_own_conclusion(self) -> None:
        """🔴 The authorised effect set is RE-DERIVED against the authority the receipt
        names. A receipt claiming a repository write under SHELL_DEFAULT is
        self-refuting and would otherwise validate perfectly."""
        receipt = er.build(binding(), report(
            authorized_effect=[em.Effect(em.WRITE, "framework/x",
                                         em.INSIDE_REPO).as_dict()]))
        ok, problems = er.validate(receipt)
        self.assertFalse(ok)
        self.assertTrue(any("not authorised by the authority" in p for p in problems))

    def test_a_receipt_whose_attestation_failed_may_not_claim_authority(self) -> None:
        """The exact shape of an authority inherited across a resume."""
        for verdict in (ea.UNATTESTED, ea.RESUME_BINDING_MISMATCH):
            with self.subTest(attestation=verdict):
                receipt = er.build(binding(), report(), attestation_verdict=verdict)
                ok, problems = er.validate(receipt)
                self.assertFalse(ok)
                self.assertTrue(any("confers" in p for p in problems))

    def test_a_failed_attestation_with_the_floor_authority_is_a_valid_record(self) -> None:
        """It records a REFUSAL honestly, which is a thing a ledger must be able to do."""
        receipt = er.build(binding(authority=em.UNATTESTED),
                           report(authorized_effect=[], result="WRITE_REFUSED"),
                           attestation_verdict=ea.RESUME_BINDING_MISMATCH)
        ok, problems = er.validate(receipt)
        self.assertTrue(ok, problems)

    def test_an_unknown_result_value_is_invalid(self) -> None:
        receipt = er.build(binding(), report(result="PROBABLY_FINE"))
        self.assertFalse(er.validate(receipt)[0])

    def test_a_malformed_effect_record_invalidates_the_receipt(self) -> None:
        receipt = er.build(binding(), report(observed_effect=[{"kind": "WRITE"}]))
        self.assertFalse(er.validate(receipt)[0])

    def test_an_edited_receipt_fails_its_own_id(self) -> None:
        receipt = er.build(binding(), report())
        receipt["result"] = "WRITE_RESULT_INVALID"
        ok, problems = er.validate(receipt)
        self.assertFalse(ok)
        self.assertTrue(any("receipt_id" in p for p in problems))

    def test_every_bound_field_reaches_the_receipt_id(self) -> None:
        base = er.build(binding(), report())["receipt_id"]
        for field in ("actor", "runtime", "runtime_version", "session", "task",
                      "worktree", "branch", "authority"):
            with self.subTest(field=field):
                moved = er.build(binding(**{field: "different"}), report())
                self.assertNotEqual(base, moved["receipt_id"])
        for field in ("head_before", "head_after", "result", "command"):
            with self.subTest(field=field):
                moved = er.build(binding(), report(**{field: "different"}))
                self.assertNotEqual(base, moved["receipt_id"])


def _reseal(receipt: dict) -> str:
    import hashlib
    body = {k: v for k, v in receipt.items() if k != "receipt_id"}
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


class TheChainIsTamperEvident(unittest.TestCase):

    def setUp(self) -> None:
        self.ledger = Path(tempfile.mkdtemp(prefix="rev8-ledger-")) / "receipts.jsonl"

    def test_a_ledger_of_appended_receipts_verifies(self) -> None:
        for index in range(3):
            er.append(self.ledger, binding(), report(command=f"git add path{index}"))
        ok, problems = er.verify_ledger(self.ledger)
        self.assertTrue(ok, problems)

    def test_an_edited_earlier_receipt_breaks_the_chain(self) -> None:
        for index in range(3):
            er.append(self.ledger, binding(), report(command=f"git add path{index}"))
        lines = self.ledger.read_text().splitlines()
        first = json.loads(lines[0])
        first["normalized_action"] = "git add something-else"
        first["receipt_id"] = _reseal(first)
        lines[0] = json.dumps(first, sort_keys=True)
        self.ledger.write_text("\n".join(lines) + "\n")
        ok, problems = er.verify_ledger(self.ledger)
        self.assertFalse(ok)
        self.assertTrue(any("chain broken" in p for p in problems))

    def test_an_empty_ledger_attests_to_nothing(self) -> None:
        self.ledger.parent.mkdir(parents=True, exist_ok=True)
        self.ledger.write_text("")
        ok, problems = er.verify_ledger(self.ledger)
        self.assertFalse(ok)

    def test_an_unparseable_line_is_reported_rather_than_skipped(self) -> None:
        er.append(self.ledger, binding(), report())
        with self.ledger.open("a") as handle:
            handle.write("{not json\n")
        self.assertFalse(er.verify_ledger(self.ledger)[0])


class TheTwoLedgersAreNotTheSameLedger(unittest.TestCase):
    """🔴 `fulltext_receipts.py` is evidence in a SCIENTIFIC argument; this is evidence
    about a CONTROL PLANE. They share the word 'receipt' and nothing else, and merging
    them would let a control-plane record be cited as a reading, or a reading be cited
    as proof that a command was authorised."""

    def test_the_schemas_are_distinct(self) -> None:
        self.assertNotIn("fulltext", er.SCHEMA)
        self.assertTrue(er.SCHEMA.startswith("legend_execution_receipt/"))

    def test_a_fulltext_receipt_does_not_validate_as_an_execution_receipt(self) -> None:
        ok, problems = er.validate({
            "schema": "fulltext_read_receipt/1", "pmid": "12345678",
            "read_on": "2026-08-29", "reader": "scientist-a",
        })
        self.assertFalse(ok)
        self.assertTrue(any("schema is" in p for p in problems))

    def test_an_execution_receipt_carries_no_scientific_field(self) -> None:
        receipt = er.build(binding(), report())
        for field in ("pmid", "doi", "pmcid", "claim_id", "quote", "locator"):
            self.assertNotIn(field, receipt)

    def test_the_task_text_is_a_digest_and_never_the_text(self) -> None:
        """A task line can carry anything the operator typed. The receipt needs to
        detect that it CHANGED, not to republish it."""
        receipt = er.build(binding(task=ea.task_fingerprint("a sensitive assignment")),
                           report())
        self.assertNotIn("sensitive", json.dumps(receipt))


if __name__ == "__main__":
    unittest.main(verbosity=2)
