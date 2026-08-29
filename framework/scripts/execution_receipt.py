#!/usr/bin/env python3
"""EXECUTION RECEIPTS — what an actor did, bound to who and where it was.

🔴 **This is not `fulltext_receipts.py` and must never be merged with it.** That ledger
records that a human-or-agent READ a scientific source, and it is evidence in a
scientific argument. This one records that a RUNTIME EXECUTED a command, and it is
evidence about a control plane. They have different audiences, different retention
rules and different consequences when wrong, and the only thing they share is the word
"receipt". `test_execution_receipt.py::TheTwoLedgersAreNotTheSameLedger` asserts the
schemas cannot be read by each other's validator.

## What a receipt binds, and why each field is load-bearing

```
actor · runtime · runtime_version · session · task        WHO, and in what incarnation
worktree · branch · head_before · head_after              WHERE, and between which states
normalized_action                                         WHAT was asked for
predicted_effect · authorized_effect · observed_effect    WHAT was expected, permitted, done
result                                                    the verdict over those three
tool_call_id · transcript                                 the runtime's own handle on it
```

A receipt that records a verdict without its provenance proves nothing. Revision 7 had
already written that sentence about the Codex hook probe, and asserted it there; here it
is the validator's whole job. `{"result": "WRITE_RESULT_VALID"}` is not a weak receipt,
it is not a receipt.

## The chain, and what it does and does not give

Each receipt carries `previous`, the id of the one before it, and `receipt_id`, a
SHA-256 over its own canonical body *including* `previous`. Editing any earlier receipt
breaks every id after it, which `verify` reports.

🔴 What that does NOT give: it does not prove the receipt was true when written. A
runtime that never fired its hook writes a perfectly chained ledger of perfectly
authorised commands. The chain protects the record from later editing; it says nothing
about the recording. That is `HOOK_DEMONSTRATED`'s job and it is a different check.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
import effect_model as em  # noqa: E402
import execution_attestation as ea  # noqa: E402

SCHEMA = "legend_execution_receipt/1"

#: Every field a valid receipt must carry. A receipt missing ONE of these is invalid;
#: there is no "mostly bound" state, because the fields nobody filled in are exactly the
#: fields an inherited authority would leave empty.
REQUIRED: Tuple[str, ...] = (
    "schema", "actor", "runtime", "runtime_version", "session", "task",
    "worktree", "branch", "head_before", "head_after", "authority", "attestation",
    "binding_fingerprint", "normalized_action",
    "predicted_effect", "authorized_effect", "observed_effect", "result",
    # ── revision 9 ──
    #
    # 🔴 `worktree` alone cannot answer "was this within the actor's own tree?", and
    # that is now a question the policy decides on. Two worktrees of one repository
    # have two toplevels and one object store, so a receipt keyed on the toplevel
    # records two actors as having worked in two repositories — which is the fact that
    # would have to be true for a cross-worktree write to be nobody's business.
    "repository_id",
    # The base relative targets were resolved against. Without it, `normalized_action`
    # is a command with no meaning: `echo x > framework/probe.md` is a repository write
    # or a scratch write depending entirely on this value.
    "effective_workdir",
    # WHICH policy judged it. `GUARD_REVISION_UNIFORM` is NO across this repository, so
    # a receipt that does not name its engine cannot be compared with one from another
    # worktree — the two were produced by different rules.
    "guard_generation", "guard_policy_hash",
)

VALID_ATTESTATIONS = frozenset({ea.ATTESTED, ea.UNATTESTED,
                                ea.RESUME_BINDING_MATCH, ea.RESUME_BINDING_MISMATCH})

#: Fields whose value may legitimately be UNDERIVABLE, and the reason for each. Anything
#: not listed here must carry a real value: `UNDERIVABLE` in an unlisted field is a
#: refusal to record, not a record of a refusal.
MAY_BE_UNDERIVABLE = {
    "session": "a runtime that emits no session identifier",
    "tool_call_id": "a runtime that does not expose one",
    "transcript": "a runtime that does not expose one",
    "runtime_version": "a runtime whose version could not be read — 🔴 this one is a "
                       "REVALIDATION_TRIGGER, not a shrug",
}

VALID_RESULTS = frozenset({"WRITE_RESULT_VALID", "WRITE_RESULT_INVALID", "WRITE_REFUSED"})


def _canonical(body: Dict[str, object]) -> bytes:
    return json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")


def build(binding: ea.Binding, report: Dict[str, object],
          previous: Optional[str] = None, tool_call_id: Optional[str] = None,
          transcript: Optional[str] = None,
          attestation_verdict: str = ea.ATTESTED) -> Dict[str, object]:
    """One receipt, from a binding and a `post_effect_verify.run` report.

    🔴 `binding.authority` must already be the EFFECTIVE authority — the one the
    command was actually judged under — and not the one the actor declared. The first
    draft of this module recorded the declared value, so a receipt from a session whose
    attestation had FAILED read `"authority": "SHELL_DEFAULT"` while its verdict had
    been computed under `READ_ONLY`. The receipt was internally consistent, validated
    cleanly, and described a basis for its own conclusion that was not the basis used.
    `main` now rebinds before building, and `attestation_verdict` records which of the
    two happened, so the downgrade is legible rather than merely applied.
    """
    body: Dict[str, object] = {
        "schema": SCHEMA,
        "actor": binding.actor,
        "attestation": attestation_verdict,
        "runtime": binding.runtime,
        "runtime_version": binding.runtime_version,
        "session": binding.session,
        "task": binding.task,
        "worktree": binding.worktree,
        "branch": binding.branch,
        "authority": binding.authority,
        "binding_fingerprint": binding.fingerprint(),
        "normalized_action": report.get("command"),
        "predicted_effect": report.get("predicted_effect", []),
        "authorized_effect": report.get("authorized_effect", []),
        "observed_effect": report.get("observed_effect", []),
        "head_before": report.get("head_before"),
        "head_after": report.get("head_after"),
        "result": report.get("result"),
        "match": report.get("match"),
        # 🔴 Read from the report, and UNDERIVABLE when the report does not carry them —
        # never defaulted to this process's own topology. A receipt is a record of what
        # judged THAT command; filling a gap from the recorder's environment would make
        # every receipt describe the machine that read it.
        "repository_id": report.get("repository_id", ea.UNDERIVABLE),
        "effective_workdir": report.get("effective_workdir", ea.UNDERIVABLE),
        "target_scope": report.get("target_scope", ea.UNDERIVABLE),
        "guard_generation": report.get("guard_generation", ea.UNDERIVABLE),
        "guard_policy_hash": report.get("guard_policy_hash", ea.UNDERIVABLE),
        "tool_call_id": tool_call_id or ea.UNDERIVABLE,
        "transcript": transcript or ea.UNDERIVABLE,
        "previous": previous or "",
    }
    body["receipt_id"] = hashlib.sha256(_canonical(body)).hexdigest()
    return body


def validate(raw: object) -> Tuple[bool, List[str]]:
    """Is this a receipt at all? Returns `(ok, problems)`; never raises on bad input."""
    problems: List[str] = []
    if not isinstance(raw, dict):
        return False, ["a receipt must be a JSON object"]
    if raw.get("schema") != SCHEMA:
        return False, [f"schema is {raw.get('schema')!r}, not {SCHEMA!r}"]

    for field in REQUIRED:
        if field not in raw:
            problems.append(f"missing required field {field!r}")
            continue
        value = raw[field]
        if value in (None, ""):
            problems.append(f"{field!r} is empty")
        elif value == ea.UNDERIVABLE and field not in MAY_BE_UNDERIVABLE:
            problems.append(f"{field!r} is UNDERIVABLE, which this field may not be")

    if raw.get("result") not in VALID_RESULTS:
        problems.append(f"result is {raw.get('result')!r}, not one of "
                        + ", ".join(sorted(VALID_RESULTS)))

    for field in ("predicted_effect", "authorized_effect", "observed_effect"):
        value = raw.get(field)
        if not isinstance(value, list):
            problems.append(f"{field!r} must be a list of effect records")
            continue
        for record in value:
            try:
                em.Effect.from_dict(record)
            except ValueError as exc:
                problems.append(f"{field!r}: {exc}")

    if raw.get("authority") not in em.AUTHORITIES:
        problems.append(f"authority {raw.get('authority')!r} is not an authority class")
    if raw.get("attestation") not in VALID_ATTESTATIONS:
        problems.append(f"attestation is {raw.get('attestation')!r}, not one of "
                        + ", ".join(sorted(VALID_ATTESTATIONS)))
    # 🔴 A receipt whose attestation FAILED may not also claim an authority above the
    # floor. That pair is precisely the shape of an inherited authority after a resume,
    # and it is the reason this ledger exists.
    if (raw.get("attestation") in (ea.UNATTESTED, ea.RESUME_BINDING_MISMATCH)
            and raw.get("authority") != em.UNATTESTED):
        problems.append(
            f"attestation is {raw.get('attestation')!r} and yet the receipt claims "
            f"authority {raw.get('authority')!r}; a failed attestation confers "
            f"{em.UNATTESTED} and nothing else")

    # 🔴 The check that makes the rest mean something: a receipt claiming an authorised
    # effect set that its own authority does not grant is self-refuting, and would
    # otherwise validate perfectly. This is the arithmetic being re-derived rather than
    # trusted — the receipt does not get to assert its own conclusion.
    if isinstance(raw.get("authorized_effect"), list) and raw.get("authority") in em.AUTHORITIES:
        try:
            effects = [em.Effect.from_dict(r) for r in raw["authorized_effect"]]
        except ValueError:
            effects = []
        decision = em.authorize(effects, raw["authority"])
        if not decision.authorized:
            problems.append(
                "the authorized_effect set is not authorised by the authority the "
                "receipt names: " + "; ".join(w for _, w in decision.denials))

    body = {k: v for k, v in raw.items() if k != "receipt_id"}
    expected = hashlib.sha256(_canonical(body)).hexdigest()
    if raw.get("receipt_id") != expected:
        problems.append("receipt_id does not match the receipt's own body")

    return not problems, problems


# ── the ledger ──────────────────────────────────────────────────────────────────────

def read(path: Path) -> List[dict]:
    if not Path(path).exists():
        return []
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except ValueError:
            out.append({"schema": "UNPARSEABLE", "raw": line[:200]})
    return out


def append(path: Path, binding: ea.Binding, report: Dict[str, object],
           tool_call_id: Optional[str] = None, transcript: Optional[str] = None,
           attestation_verdict: str = ea.ATTESTED) -> Dict[str, object]:
    path = Path(path)
    existing = read(path)
    previous = existing[-1].get("receipt_id") if existing else ""
    receipt = build(binding, report, previous, tool_call_id, transcript,
                    attestation_verdict)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(receipt, sort_keys=True) + "\n")
    return receipt


def verify_ledger(path: Path) -> Tuple[bool, List[str]]:
    """Every receipt valid, and every link intact."""
    problems: List[str] = []
    receipts = read(path)
    if not receipts:
        return False, [f"{path} holds no receipts; an empty ledger attests to nothing"]
    previous = ""
    for index, receipt in enumerate(receipts):
        ok, issues = validate(receipt)
        problems.extend(f"receipt {index}: {issue}" for issue in issues)
        if ok and receipt.get("previous") != previous:
            problems.append(
                f"receipt {index}: chain broken — it names previous "
                f"{receipt.get('previous', '')[:12]!r} and the receipt before it is "
                f"{previous[:12]!r}")
        previous = receipt.get("receipt_id", "") if ok else previous
    return not problems, problems


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="action", required=True)

    record = sub.add_parser("record", help="run a command under verification and record it")
    record.add_argument("--ledger", required=True)
    record.add_argument("--actor", required=True)
    record.add_argument("--task", required=True)
    record.add_argument("--authority", default="SHELL_DEFAULT")
    record.add_argument("--root", default=".")
    record.add_argument("--tool-call-id")
    record.add_argument("command", nargs=argparse.REMAINDER)

    check = sub.add_parser("verify", help="validate a ledger and its chain")
    check.add_argument("--ledger", required=True)

    args = parser.parse_args(argv)

    if args.action == "verify":
        ok, problems = verify_ledger(Path(args.ledger))
        print("LEDGER_OK" if ok else "LEDGER_INVALID")
        for problem in problems:
            print("  " + problem)
        return 0 if ok else 1

    import post_effect_verify as pev

    root = str(Path(args.root).resolve())
    command = " ".join(args.command).lstrip("- ").strip()
    if not command:
        parser.error("no command given")

    declared = ea.derive(actor=args.actor, task=args.task, authority=args.authority,
                         cwd=root)
    attestation = ea.attest(declared)
    # 🔴 The authority is REVOKED, not merely reported, and the BINDING is rebuilt with
    # the revoked value — so the fingerprint, the receipt and the decision all name the
    # same authority. A receipt that records the declared authority beside a verdict
    # computed under the floor is a receipt that misdescribes its own basis.
    authority = attestation.effective_authority
    binding = ea.derive(actor=args.actor, task=args.task, authority=authority, cwd=root)
    if not attestation.ok:
        print(json.dumps({"verdict": attestation.verdict,
                          "reason": attestation.reason,
                          "declared_authority": args.authority,
                          "effective_authority": authority}, indent=2))
    report = pev.run(command, root, actor=args.actor, authority=authority)
    receipt = append(Path(args.ledger), binding, report, args.tool_call_id,
                     attestation_verdict=attestation.verdict)
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if report["result"] in ("WRITE_RESULT_VALID", "WRITE_REFUSED") else 1


if __name__ == "__main__":
    sys.exit(main())
