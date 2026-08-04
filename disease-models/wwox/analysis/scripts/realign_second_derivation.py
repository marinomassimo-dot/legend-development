#!/usr/bin/env python3
"""Re-index the independent derivation's sentence ordinals, without re-authoring it.

The first independent run indexed sentences from 1 while the reference derivation
indexed from 0 — a base the anchor format never declared. Every shared anchor therefore
pointed one sentence late, the comparator compared unrelated text, and the result read as
total semantic disagreement. It was an off-by-one.

This tool corrects the indexing and nothing else. It is deliberately not a re-derivation:

* the authored output is read-only and stays byte-identical to its attestation;
* only `registry_anchor` changes, and only its `sent[n]` component, to `sent[n-1]`;
* propositions, contexts, locators, epistemic types and relations are copied verbatim —
  the judgement of the independent reader is not touched;
* `occurrence_id` is recomputed because it is a function of the anchor, and the original
  is retained as `pre_realignment_occurrence_id` so the link back to the attested output
  survives;
* every record records the transformation applied to it.

**It verifies before it transforms.** The hypothesis — that each declared span is the
registry text at `sent[n-1]` — is checked against every record. One counterexample and
nothing is written: a transformation that is right for most records and wrong for some is
worse than none, because the survivors look trustworthy.

Usage
-----
    realign_second_derivation.py --check          # verify the hypothesis, write nothing
    realign_second_derivation.py --out <file>     # verify, then write the realigned copy
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[0] / "data"
SOURCE = DATA / "dismech_second_derivation_authored_016_024_035.jsonl"

_spec = importlib.util.spec_from_file_location("derive", HERE / "derive_dismech_sidecar.py")
derive = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(derive)

ANCHOR = re.compile(r"^(?P<head>.*)\|sent\[(?P<n>\d+)\]$")


def _parse(anchor: str) -> tuple[str, str, int] | None:
    match = ANCHOR.match(anchor)
    if not match:
        return None
    head = match.group("head")
    body = head.split("#", 1)[1]
    claim = body.split("|")[0].replace("CLAIM ", "")
    field = body.split("|", 1)[1]
    return claim, field, int(match.group("n"))


def _normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def check(records: list[dict]) -> tuple[list[str], int]:
    """Confirm every declared span is the registry text one sentence earlier."""
    problems: list[str] = []
    confirmed = 0
    for record in records:
        if record.get("record_kind") != "assertion_candidate":
            continue
        anchor = record.get("registry_anchor") or ""
        parsed = _parse(anchor)
        if parsed is None:
            continue                      # whole-field anchor, no ordinal to shift
        claim, field, ordinal = parsed
        span = _normalise(record.get("raw_registry_span", ""))
        if ordinal < 1:
            problems.append(f"{anchor}: sent[{ordinal}] cannot shift below zero")
            continue
        try:
            shifted = _normalise(derive.read_anchor(claim, field, ordinal - 1))
        except SystemExit as exc:
            problems.append(f"{anchor}: {exc}")
            continue
        if shifted == span:
            confirmed += 1
        else:
            problems.append(
                f"{anchor}: declared span is not the registry text at sent[{ordinal - 1}]")
    return problems, confirmed


def realign(records: list[dict]) -> list[dict]:
    out: list[dict] = []
    for record in records:
        row = dict(record)
        anchor = row.get("registry_anchor")
        if anchor:
            parsed = _parse(anchor)
            if parsed is not None:
                claim, field, ordinal = parsed
                row["registry_anchor"] = derive.anchor_str(claim, field, ordinal - 1)
                row["pre_realignment_registry_anchor"] = anchor
        out.append(row)

    # occurrence_id is a function of the anchor, so it follows the correction.
    anchors = {r["candidate_id"]: r["registry_anchor"]
               for r in out if r.get("record_kind") == "assertion_candidate"}
    for row in out:
        if row.get("record_kind") != "assertion_occurrence":
            continue
        anchor = anchors.get(row.get("candidate_id"))
        if not anchor:
            continue
        ordinal = row.get("registry_ordinal", 0)
        row["pre_realignment_occurrence_id"] = row.get("occurrence_id")
        row["registry_anchor"] = anchor
        row["occurrence_id"] = "OCC-" + derive.fp(row["claim_id"], anchor, ordinal)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify only, write nothing")
    parser.add_argument("--out", type=Path, help="write the realigned copy")
    parser.add_argument("--source", type=Path, default=SOURCE)
    arguments = parser.parse_args()

    original = arguments.source.read_bytes()
    records = [json.loads(line) for line in original.decode("utf-8").splitlines() if line.strip()]
    problems, confirmed = check(records)

    print(f"records: {len(records)} | anchors confirmed shifted by one: {confirmed}")
    if problems:
        print(f"HYPOTHESIS REJECTED: {len(problems)} record(s) do not fit — nothing written")
        for problem in problems[:10]:
            print(f"  - {problem}")
        return 2
    print("HYPOTHESIS CONFIRMED on every record with a sentence ordinal")

    if arguments.check or not arguments.out:
        return 0

    corrected = realign(records)
    payload = "".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in corrected)
    arguments.out.write_text(payload, encoding="utf-8")

    manifest = {
        "record_kind": "realignment_manifest",
        "source": str(arguments.source.relative_to(arguments.source.parents[4])),
        "source_sha256": hashlib.sha256(original).hexdigest(),
        "output_sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
        "transformation": "registry_anchor sent[n] -> sent[n-1]; occurrence_id recomputed",
        "fields_left_verbatim": ["proposition", "context", "locator", "epistemic_type",
                                 "evidence_relation", "source_id", "terminal_state"],
        "anchors_confirmed": confirmed,
        "reason": "the anchor format did not declare its sentence-ordinal base; the "
                  "independent run indexed from 1 and the reference from 0",
    }
    manifest_path = arguments.out.with_name(arguments.out.stem + "_manifest.json")
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                             encoding="utf-8")
    print(f"written: {arguments.out.name} and {manifest_path.name}")
    print(f"source unchanged: sha256 {manifest['source_sha256'][:16]}…")
    return 0


if __name__ == "__main__":
    sys.exit(main())
