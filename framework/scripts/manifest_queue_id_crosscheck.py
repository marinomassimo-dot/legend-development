#!/usr/bin/env python3
"""Does a manifest's `multihop.queued[].queue` identifier name THIS paper's debt?

🔴 WHY THIS EXISTS, and it is a near-miss rather than a hypothetical.

On 2026-09-09, wave 2 of the Aqeilan sweep, a draft manifest for PMID 18674750 named
`FT-072`, `FT-073`, `FT-074` and `FT-075` as the queue entries carrying its four new
multi-hop debts. All four were live entries about entirely unrelated papers — `FT-072` is
PMID 20530675 (osteosarcoma), `FT-073` is PMID 27845895 (Hyal-2/Smad4), `FT-074` the mTOR
stubs, `FT-075` PMID 18931939 (Runx2). Only `FT-071` was this paper's own. The manifest
passed `STRICT`, and the reader's own note records why:

    "A first draft of this manifest reused FT-072 to FT-075, which would have silently
     collided with four unrelated live entries."

It was caught by the actor's independent grep of the queue AFTER `STRICT` had passed. The
diagnosis in the retrospective (§ 2.2 B7) is exact: *nothing in `deepdive_manifest.py`
checks that a `multihop.queued[].queue` identifier exists or names the same PMID, so a
manifest can point at another paper's debt and every gate stays green.*

WHAT THIS ASKS, and it is two mechanical questions and no more:

    RESOLVES   the identifier has a `## FT-NNN` heading in `full_text_queue_current.md`.
               A reference that does not resolve is not a reference.
    BELONGS    that entry's text names at least one of: the PMID this queued item is
               queueing, or the PMID of the manifest recording the debt. Either is a
               legitimate arrangement — a paper's own entry routinely carries its hops —
               and an entry naming NEITHER is another paper's entry.

WHAT IT DOES NOT CLAIM. It does not check that the entry is the *best* place for the debt,
that the reason is sound, or that the queued PMID is correct. It checks the property whose
absence let four foreign identifiers through a green gate: that the address resolves and
that the thing at the address has something to do with this reading.

🔴 THE PMID SCAN OVER A QUEUE ENTRY IS DELIBERATELY GENEROUS — every 7-to-8 digit token in
the entry body counts, not only the one on the `**Paper:**` line. A queue entry legitimately
names the hops it carries, and a narrow scan would report a correct manifest as foreign. The
generous direction is the safe one here because the check BLOCKS: the failure it exists for
(an entry about a completely unrelated paper) survives the generosity, since such an entry
mentions neither identifier anywhere in its body. Measured on the real defect: all four
foreign identifiers are still caught under the generous scan.

A `queue` value naming no `FT-NNN` at all — `"integrity review"`, a bare
`"full_text_queue_current"` — is NOT an error and is NOT silently passed either: it is
reported as UNCHECKED, because "this checker had nothing to check" and "this checker
approved it" are different facts and only one of them is true.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

QUEUE_RELATIVE = "disease-models/{disease}/research/full_text_queue_current.md"
MANIFEST_RELATIVE = "disease-models/{disease}/research/deepdive_manifests"

# A queue heading. The file writes `## FT-001` through `## FT-096`; the width is a house
# convention and is normalised away below so `FT-71` and `FT-071` are the same address.
QUEUE_HEADING_RE = re.compile(r"(?m)^##\s+(FT-\d+)")

# An FT reference ANYWHERE inside the `queue` value, so `full_text_queue_current#FT-046`
# resolves the same as a bare `FT-046`.
FT_REFERENCE_RE = re.compile(r"\bFT-(\d+)\b")

# PubMed identifiers are 7 or 8 digits today. The lookarounds keep 18674750 from matching
# inside a longer run of digits.
PMID_RE = re.compile(r"(?<!\d)(\d{7,8})(?!\d)")


def canonical(ft_number: str) -> str:
    """`FT-71`, `FT-071` and `full_text_queue_current#FT-71` are one address."""
    return f"FT-{int(ft_number):03d}"


def parse_queue(text: str) -> dict[str, str]:
    """Return {canonical FT id: entry body}, an entry running to the next `## FT-` heading."""
    entries: dict[str, str] = {}
    matches = list(QUEUE_HEADING_RE.finditer(text))
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        identifier = canonical(match.group(1).split("-", 1)[1])
        # A duplicated heading is the queue's own defect, not this checker's business.
        # Concatenate rather than overwrite, so neither copy's PMIDs are lost.
        entries[identifier] = entries.get(identifier, "") + text[match.start():end]
    return entries


def load_queue(root: Path, disease: str) -> dict[str, str] | None:
    """Parsed queue, or None when the file is not in this workspace at all."""
    path = root / QUEUE_RELATIVE.format(disease=disease)
    if not path.is_file():
        return None
    return parse_queue(path.read_text(encoding="utf-8", errors="replace"))


def referenced_ids(value: object) -> list[str]:
    """Every FT address named by a `queue` value, canonicalised, in order."""
    return [canonical(number) for number in FT_REFERENCE_RE.findall(str(value or ""))]


def item_pmids(item: dict, manifest_pmid: str | None) -> set[str]:
    """The identifiers an entry may legitimately name: the hop's, or the reading's own."""
    wanted: set[str] = set()
    for key in ("pmid", "pmids"):
        value = item.get(key)
        candidates = value if isinstance(value, list) else [value]
        for candidate in candidates:
            token = str(candidate or "").strip()
            if PMID_RE.fullmatch(token):
                wanted.add(token)
    if manifest_pmid and PMID_RE.fullmatch(str(manifest_pmid).strip()):
        wanted.add(str(manifest_pmid).strip())
    return wanted


def audit(manifest: dict, queue_entries: dict[str, str]) -> dict:
    """Sort every FT reference in `multihop.queued` into resolves / foreign / unchecked."""
    manifest_pmid = str(manifest.get("pmid") or "").strip()
    queued = (manifest.get("multihop") or {}).get("queued") or []
    resolved: list[dict] = []
    unresolved: list[dict] = []
    foreign: list[dict] = []
    unchecked: list[dict] = []

    for position, item in enumerate(queued):
        if not isinstance(item, dict):
            # A bare PMID string queues a hop without naming a queue entry. There is no
            # address to check, and inventing one would be this checker asserting a fact.
            continue
        raw = item.get("queue")
        if raw is None or not str(raw).strip():
            continue
        addresses = referenced_ids(raw)
        if not addresses:
            unchecked.append({"entry": position, "queue": str(raw)})
            continue
        wanted = item_pmids(item, manifest_pmid)
        for address in addresses:
            body = queue_entries.get(address)
            if body is None:
                unresolved.append({"entry": position, "queue_id": address})
                continue
            present = set(PMID_RE.findall(body))
            if wanted and not (wanted & present):
                foreign.append({
                    "entry": position,
                    "queue_id": address,
                    "expected_any_of": sorted(wanted),
                })
            else:
                resolved.append({"entry": position, "queue_id": address})

    return {
        "pmid": manifest_pmid,
        "resolved": resolved,
        "unresolved": unresolved,
        "foreign": foreign,
        "unchecked": unchecked,
    }


def errors_for(manifest: dict, queue_entries: dict[str, str]) -> list[str]:
    """BLOCK-grade messages for `deepdive_manifest.validate` to append."""
    report = audit(manifest, queue_entries)
    messages: list[str] = []
    for row in report["unresolved"]:
        messages.append(
            f"multihop.queued[{row['entry']}].queue: {row['queue_id']} has no entry in "
            "full_text_queue_current.md. A queue identifier that does not resolve records "
            "no debt — it names an address nobody can visit, and the reading debt it was "
            "supposed to carry is lost silently"
        )
    for row in report["foreign"]:
        messages.append(
            f"multihop.queued[{row['entry']}].queue: {row['queue_id']} is a live queue entry "
            f"about a different paper — it names none of "
            f"{', '.join('PMID ' + p for p in row['expected_any_of'])}. Pointing a hop at "
            "another paper's entry attaches this reading's debt to a record that will be "
            "closed for unrelated reasons. Mint a new identifier, or name the entry that "
            "actually covers this hop"
        )
    return messages


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("manifest", nargs="*",
                        help="manifest paths; default is every manifest of the disease")
    parser.add_argument("--root", default=".")
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 when any identifier is unresolved or foreign")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    queue_entries = load_queue(root, args.disease)
    if queue_entries is None:
        print(f"ERROR: no full-text queue at "
              f"{root / QUEUE_RELATIVE.format(disease=args.disease)}", file=sys.stderr)
        return 2

    if args.manifest:
        paths = [Path(p) for p in args.manifest]
    else:
        paths = sorted(
            (root / MANIFEST_RELATIVE.format(disease=args.disease)).glob("PMID*.json"))

    reports = []
    for path in paths:
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as exc:
            reports.append({"manifest": str(path), "error": str(exc),
                            "resolved": [], "unresolved": [], "foreign": [], "unchecked": []})
            continue
        report = audit(manifest, queue_entries)
        report["manifest"] = str(path)
        reports.append(report)

    totals = {key: sum(len(r[key]) for r in reports)
              for key in ("resolved", "unresolved", "foreign", "unchecked")}

    if args.json:
        print(json.dumps({"queue_entries": len(queue_entries), "reports": reports,
                          "totals": totals}, indent=1))
    else:
        for report in reports:
            if report.get("error"):
                print(f"{report['manifest']}  [UNREADABLE] {report['error']}")
                continue
            for row in report["unresolved"]:
                print(f"{report['pmid']}  [UNRESOLVED] multihop.queued[{row['entry']}]: "
                      f"{row['queue_id']}")
            for row in report["foreign"]:
                print(f"{report['pmid']}  [FOREIGN] multihop.queued[{row['entry']}]: "
                      f"{row['queue_id']} names none of "
                      f"{', '.join(row['expected_any_of'])}")
            for row in report["unchecked"]:
                print(f"{report['pmid']}  [UNCHECKED] multihop.queued[{row['entry']}]: "
                      f"queue value {row['queue']!r} names no FT identifier")
        print(f"manifests: {len(reports)} | queue entries: {len(queue_entries)} | "
              f"FT references checked: {totals['resolved'] + totals['unresolved'] + totals['foreign']}")
        print(f"resolves and belongs: {totals['resolved']} | unresolved: "
              f"{totals['unresolved']} | foreign (names another paper): {totals['foreign']} | "
              f"unchecked (no FT identifier in the queue value): {totals['unchecked']}")
        print("NOTE: 'belongs' means the entry names this hop's PMID or the reading's own. "
              "It does not mean the entry is the right place for the debt, only that it is "
              "not a different paper's record.")

    if args.strict and (totals["unresolved"] or totals["foreign"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
