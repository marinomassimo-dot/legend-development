#!/usr/bin/env python3
"""Consolidate the HUMAN_APPROVAL_QUEUE lineages into one deterministic view.

## Why this exists

`ledger/approvals/HUMAN_APPROVAL_QUEUE.jsonl` diverged into three lineages, and the divergence is
not a corruption — it is what append-only files do when three actors append on three branches.
Measured across every local head and remote-tracking ref:

    20c24a2b   6 records    main + 30 other refs
    95fc8163  14 records    evidence-index, p51c9-rebased-onto-c89c2217
    bb603d9a  10 records    orchestrator

**`main` carries the shortest one.** Four operator approvals — `SUNSET-DEC3`, `SCIAB`, `XPORT`,
`P5DOMAIN`, all `STATE: APPROVED` — exist only on `orchestrator`, and eight records including four
resolutions exist only on `evidence-index`. A reader of `main` sees two approvals out of eighteen
records and has no way to learn that the other sixteen exist.

**No approval should be invisible because of which ref it landed on.** That is what this tool is
for, and it is all it is for: it produces a view. It never writes the canonical file, and it is
not a merge.

## What was measured before anything was designed

Every property below was derived from the three real blobs, not assumed, and each one removes a
design decision that would otherwise have been guesswork:

* **The six records of the short lineage are a BYTE-EXACT prefix of both others** — `cmp` on the
  first six lines, not a record-by-record comparison. So dedup is lossless and cannot lose a field.
* **Zero duplicate identities within any lineage**, and **zero byte-conflicts** across them: the
  six shared records are identical everywhere. There is nothing to reconcile, only to unite.
* **No hash chain.** 0 of 30 records carry a prev-hash. **So no rechain is required and none is
  performed.** Introducing a chain would be a separate, governed change, and doing it here would
  hide a schema change inside a merge.
* **The unique suffixes are date-disjoint**: one lineage's additions are all 2026-08-17, the
  other's are 2026-08-18 and 2026-08-19.
* 🔴 **24 of 27 timestamped records carry a DATE ONLY**, and the schema says why —
  `TIMESTAMP_PRECISION: "date only — the runtime exposed no wall-clock time"`. **A timestamp sort
  therefore cannot totally order this queue**, and § "Ordering" below states what closes the gap.

## Ordering, stated rather than assumed

The sort key is `(timestamp, first-seen position, identity)`.

The second term is load-bearing and is declared as such: **because most records share a day, the
position each record holds inside its own append-only lineage is the only surviving evidence of
what followed what.** Preserving it is correct precisely because the sources are append-only —
position IS chronology there — but it means the output is a function of the sources' content *and*
their internal order, not of their content alone.

Verified: all six orders in which the three lineages can be supplied produce a byte-identical
result. Reversing the records *inside* a lineage does not, and that is the declared limitation
rather than a defect to be papered over with a tie-break that invents an order.

## Provenance

Which lineage a record came from is information the sources do not carry, so writing it into the
records would change their bytes and destroy the byte-identity the dedup depends on. It goes to a
**sidecar**, keyed by identity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ID_FIELDS = ("APPROVAL_ID", "RESOLUTION_ID", "CORRECTION_ID")
TS_FIELDS = ("REQUESTED_AT", "RESOLVED_AT", "RECORDED_AT")
HEADER = "__HEADER__"


class ConflictError(RuntimeError):
    """One identity, two different records. Never merged silently — the operator decides."""


class SourceError(RuntimeError):
    """A source file is not what it claims to be.

    🔴 Distinct from `ConflictError` on purpose, and the distinction is operational rather than
    stylistic. A conflict means two lineages disagree about an approval and a human has to
    choose. A source error means one file is malformed or contradicts *itself*, and there is
    nothing to choose between — it is a corrupt input, and routing it to an operator as a
    decision would be asking them to adjudicate a typo.
    """


def identity(record: dict) -> str:
    for field in ID_FIELDS:
        value = record.get(field)
        if isinstance(value, str) and value:
            return value
    if "_schema" in record:
        return HEADER
    # A record declaring no identity is content-addressed rather than dropped or renumbered:
    # an unidentifiable approval is still an approval, and inventing an id for it would make
    # two runs of this tool disagree.
    return "sha256:" + hashlib.sha256(
        json.dumps(record, sort_keys=True).encode()).hexdigest()[:32]


def timestamp(record: dict) -> str:
    """The record's own ordering evidence, or `""` when it declares none.

    🔴 A non-string value is a SOURCE ERROR, not an absent timestamp, and conflating the two is
    how the sort came to invent an order. The predecessor returned `""` for `20260817` — an
    integer date, which is a plausible thing for a hand-edited file to contain — and `""` sorts
    before every real date, so a record whose date could not be read was presented **first, at
    position 1, ahead of every record whose date was legible.** The consolidator was not
    ordering by time; it was ordering by whether it could parse the time, and saying nothing.
    """
    for field in TS_FIELDS:
        value = record.get(field)
        if value is None:
            continue
        if not isinstance(value, str):
            raise SourceError(
                f"{identity(record)}: {field} is {type(value).__name__} {value!r}, not a string. "
                f"An unreadable timestamp is refused rather than sorted as the earliest record")
        if value:
            return value
    return ""


def digest(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True).encode()).hexdigest()


def load(path: Path) -> list[dict]:
    records = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise SourceError(f"{path}:{number}: not valid JSON — {exc}") from exc
        if not isinstance(record, dict):
            raise SourceError(
                f"{path}:{number}: line is a {type(record).__name__}, not an object. "
                f"JSON Lines permits a bare string or number on a line; this schema does not")
        records.append(record)
    return records


def consolidate(sources: dict[str, list[dict]]) -> tuple[list[dict], list[dict], list[str]]:
    """Return `(records, provenance, warnings)`. Raises rather than merging a conflict."""
    kept: dict[str, dict] = {}
    origins: dict[str, list[str]] = {}
    position: dict[str, int] = {}

    for lineage in sorted(sources):
        for index, record in enumerate(sources[lineage]):
            if not isinstance(record, dict):
                raise SourceError(
                    f"{lineage}[{index}] is a {type(record).__name__}, not an object")
            key = identity(record)
            fingerprint = digest(record)
            timestamp(record)          # raise on an unreadable timestamp before it can sort
            if key in kept:
                if kept[key]["digest"] != fingerprint:
                    # 🔴 Same lineage twice is a different fact from two lineages disagreeing,
                    # and the predecessor reported both with the words "Two lineages disagree" —
                    # emitting "differs between L2 and L2" for a file contradicting itself.
                    # One needs an operator to choose; the other has nothing to choose between.
                    if lineage in origins[key]:
                        raise SourceError(
                            f"{key} appears twice inside {lineage} with different bodies: "
                            f"{kept[key]['digest'][:12]}… vs {fingerprint[:12]}…. A lineage "
                            f"contradicting itself is a corrupt source, not a decision")
                    raise ConflictError(
                        f"{key} differs between {origins[key][0]} and {lineage}: "
                        f"{kept[key]['digest'][:12]}… vs {fingerprint[:12]}…. "
                        f"Two lineages disagree about one approval; this is an operator "
                        f"decision, not a merge rule")
                origins[key].append(lineage)
                position[key] = min(position[key], index)
                continue
            kept[key] = {"record": record, "digest": fingerprint}
            origins[key] = [lineage]
            position[key] = index

    # 🔴 Lineages that share nothing are probably not lineages of one object. Reported, never
    # refused: two genuinely disjoint append-only files ARE unitable, and the union is still
    # correct. What is not acceptable is doing it silently, because the likeliest cause of a
    # zero-overlap "merge" is that someone passed the wrong file.
    disjoint: list[str] = []
    if len(sources) > 1:
        for a, b in ((x, y) for x in sorted(sources) for y in sorted(sources) if x < y):
            shared = {identity(r) for r in sources[a] if isinstance(r, dict)} & \
                     {identity(r) for r in sources[b] if isinstance(r, dict)}
            if not shared:
                disjoint.append(f"{a} and {b} share no record — verify they are the same object")

    body = sorted((k for k in kept if k != HEADER),
                  key=lambda k: (timestamp(kept[k]["record"]), position[k], k))
    order = ([HEADER] if HEADER in kept else []) + body

    records = [kept[k]["record"] for k in order]
    provenance = [{
        "identity": k,
        "lineages": sorted(origins[k]),
        "sha256": kept[k]["digest"],
        "timestamp": timestamp(kept[k]["record"]) or None,
        "state": kept[k]["record"].get("STATE"),
    } for k in order]
    return records, provenance, disjoint


def source_labels(paths: list[Path]) -> dict[str, Path]:
    """Collision-safe labels for the supplied files, shortest-unique-suffix first.

    🔴 `path.stem` is not an identity, and using it as one silently destroyed lineages.
    Reproduced with the three real queues copied into three directories, all named
    `queue.jsonl`:

        sources: queue=10
        consolidated: 10 records from 10 input line(s); 0 deduped, 0 conflicts
        exit 0

    Three files holding 6, 14 and 10 records were supplied. `{path.stem: load(path) …}`
    collapsed all three to one key, last wins, and **20 of 30 records were discarded before
    `consolidate()` was ever called** — reported as a clean, conflict-free consolidation. Even
    the input count was wrong, because it too was derived from the collapsed dict.

    The lineage label is a display name; it must never be the thing that decides whether two
    inputs are the same input. The resolved path decides that.
    """
    resolved = [p.resolve() for p in paths]

    seen: dict[Path, int] = {}
    for path in resolved:
        seen[path] = seen.get(path, 0) + 1
    repeated = sorted(str(p) for p, n in seen.items() if n > 1)
    if repeated:
        # Supplying one file twice would present a lineage as agreeing with itself.
        raise SourceError(
            f"the same file was supplied more than once: {', '.join(repeated)}")

    labels: dict[str, Path] = {}
    for path in resolved:
        parts = path.parts
        for depth in range(1, len(parts) + 1):
            candidate = "/".join(parts[-depth:])
            if not any(candidate == other for other in labels):
                # unique among the labels chosen so far AND among every other input's
                # suffix of the same depth
                rivals = [q for q in resolved if q != path
                          and "/".join(q.parts[-depth:]) == candidate]
                if not rivals:
                    labels[candidate] = path
                    break
        else:  # pragma: no cover - two distinct resolved paths always differ somewhere
            raise SourceError(f"cannot label {path} distinguishably")

    if len(labels) != len(resolved):
        raise SourceError(
            f"{len(resolved)} input(s) produced {len(labels)} label(s); refusing rather than "
            f"dropping a lineage")
    return labels


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("sources", nargs="+", type=Path,
                        help="one .jsonl per lineage; extract them with `git cat-file -p <blob>`")
    parser.add_argument("--out", type=Path,
                        help="write the consolidated view here. NEVER the canonical file: "
                             "this tool produces a view and does not perform the merge")
    parser.add_argument("--provenance", type=Path, help="write the provenance sidecar here")
    arguments = parser.parse_args()

    try:
        labelled = source_labels(arguments.sources)
        sources = {label: load(path) for label, path in labelled.items()}
        if len(sources) != len(arguments.sources):
            raise SourceError(
                f"{len(arguments.sources)} input(s) reduced to {len(sources)} lineage(s)")
        records, provenance, warnings = consolidate(sources)
    except SourceError as exc:
        # Exit 2, distinct from a conflict: nothing here is for an operator to choose between.
        print(f"SOURCE ERROR — not merged: {exc}", file=sys.stderr)
        return 2
    except ConflictError as exc:
        print(f"CONFLICT — not merged: {exc}", file=sys.stderr)
        return 1

    total = sum(len(v) for v in sources.values())
    print("sources: " + ", ".join(f"{k}={len(v)}" for k, v in sorted(sources.items())))
    print(f"consolidated: {len(records)} records from {total} input line(s); "
          f"{total - len(records)} deduped, 0 conflicts")
    for warning in warnings:
        print(f"  ⚠ {warning}", file=sys.stderr)
    for row in provenance:
        print(f"  {row['timestamp'] or '—':22s} {row['identity']:34s} "
              f"{'+'.join(row['lineages']):12s} {row['state'] or ''}")

    if arguments.out:
        arguments.out.write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records),
            encoding="utf-8")
        print(f"\nview written to {arguments.out} — this is NOT the canonical queue")
    if arguments.provenance:
        arguments.provenance.write_text(json.dumps(provenance, indent=2), encoding="utf-8")
        print(f"provenance written to {arguments.provenance}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
