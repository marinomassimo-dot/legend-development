#!/usr/bin/env python3
"""Does a deep-dive manifest's `receipt` name the reading that PRODUCED it? Measured, not assumed.

🔴 WHY THIS EXISTS — A DECIDED FIELD, NOT AN OPEN ONE
-----------------------------------------------------
`fulltext_read_receipt.md` carried the target of a manifest's `receipt` field as 🟡 OPEN: does it
name the reading that PRODUCED the manifest, or the most recent reading of that paper? The
validator required the field and checked nothing about its target, so the tooling had no opinion,
and two manifests flagged in the week of 2026-09-28 were wrong under one reading, one under the
other, and nobody could say which was a defect.

**DECIDED 2026-09-28: the field names the event that PRODUCED the manifest** — precisely, the
EARLIEST ledger event for the same study whose `outputs` name that manifest file. Four reasons,
and the first is the one that settles it:

  1. **"Most recent" is a semantics this repository cannot maintain.** Its correct value changes
     every time anybody re-reads the paper, and the only code path that writes the field
     (`fulltext_receipts.py rechain --repoint-manifests`) is rename-driven and is expressly
     forbidden for re-deciding which reading a manifest documents. So "most recent" would make
     every manifest silently wrong at the next reading — a permanent defect generator, not a
     convention. "Produced" is fixed the moment the manifest is written and never moves again.
  2. **It would duplicate the ledger.** "What is the latest reading of this paper, and at what
     depth?" is already answered authoritatively by `fulltext_receipts.py status --pmid`. A
     manifest field that restates it adds nothing and can only drift out of step with it.
  3. **A manifest IS the work record of one reading.** `require_work_manifest` already binds a
     receipt to its own manifest at append time; the relation the tooling enforces runs
     receipt → the manifest that reading produced.
  4. It is DERIVABLE, which is what makes a check possible. "Most recently attests" is not even
     well defined: attests how, by any later receipt for the paper, or only by one that names it?

🔴 **This reads `outputs` for PRODUCTION, which is what `outputs` means — never for ATTESTATION.**
The protocol's 2026-08-11 trap was an inverse index that inferred *what a receipt attests* from
`outputs`, and produced a plausible, well-formed, entirely false picture. `outputs` is what the
run TOUCHED; "which run touched this file first" is exactly a production question, and the answer
is not an attestation claim about anything the manifest says.

Cross-study events are excluded by design. `FTR-20260810-25331887-01` legitimately wrote into
`PMID38499540.json` — real multihop work — and a reading of one paper is never the producer of
another paper's manifest.

VERDICTS
--------
  CONFORMS        the declared receipt is the earliest same-study event naming the manifest
  NOT_THE_PRODUCER  the declared receipt names the manifest, but an earlier same-study event does
                    too: the field points at a later pass over a manifest somebody else produced
  UNNAMED         the declared receipt's `outputs` do not name the manifest AT ALL, while another
                  same-study event's do — the sharper defect, and the one that cannot be read as a
                  difference of convention
  UNKNOWN_EVENT   the declared receipt is not in the ledger
  NO_RECEIPT      the manifest declares no `receipt` (the schema validator already refuses this)
  UNCHECKABLE     no same-study event names the manifest, so the ledger cannot answer. Reported,
                  never a defect: the ledger is append-only and its older events predate the
                  convention of naming the manifest among a reading's outputs.

DECLARED DEBT, AND WHY IT IS A CEILING AND NOT A PASS
-----------------------------------------------------
Closing the field does not retro-fit 116 manifests. Measured on 2026-09-28 the corpus holds
`BASELINE_DEFECTS` non-conforming manifests, most of them written under the reading now retired.
`--check` fails when the count EXCEEDS that ceiling, so a NEW non-conforming manifest is loud while
the known tail stays visible and countable. Lower the ceiling when the tail is repaired; never
raise it.

🔴 **THIS TOOL DOES NOT WRITE. `manifest_receipt_repoint.py` is the instrument that does.**
Written 2026-09-28, the day after this one: it takes a PMID, derives the target through `assess`
below — the same function, so writer and checker cannot drift — and refuses everything the ledger
cannot settle, including the `UNKNOWN_EVENT`/`UNCHECKABLE` classes and the artifact-divergence
class this tool's report does not distinguish. It has no `--to`, because a caller-supplied target
is how a wrong value gets in. `--repoint-manifests` remains what it always was: it only follows a
`--rename`d identifier during a `rechain`, and the protocol still forbids pointing it at a target
decision. This tool's job is to make the tail visible, to stop it growing, and to print the value
each defect SHOULD carry, so the repair starts measured.

    python3 framework/scripts/manifest_receipt_provenance.py                 # report, exit 0
    python3 framework/scripts/manifest_receipt_provenance.py --check         # gate on the ceiling
    python3 framework/scripts/manifest_receipt_provenance.py --json
    python3 framework/scripts/manifest_receipt_provenance.py --pmid 42589397
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

#: Measured 2026-09-28 over 116 manifests: 98 CONFORMS, 16 non-conforming (13 NOT_THE_PRODUCER, 2 UNNAMED, 1 UNKNOWN_EVENT), 2 UNCHECKABLE. A CEILING.
#: It fell from 17 the same day, when `manifest_receipt_repoint.py` repaired PMID42589397.json —
#: the one case wrong under BOTH of the readings the field used to carry. Lowered, never raised.
BASELINE_DEFECTS = 16

DEFECTS = ("NOT_THE_PRODUCER", "UNNAMED", "UNKNOWN_EVENT", "NO_RECEIPT")


@dataclass
class Finding:
    manifest: str
    pmid: str
    declared: str
    verdict: str
    should_be: str
    naming: list[str]
    note: str = ""


def manifest_dir(root: Path, disease: str) -> Path:
    return root / "disease-models" / disease / "research" / "deepdive_manifests"


def ledger_path(root: Path, disease: str) -> Path:
    return root / "disease-models" / disease / "registries" / "fulltext_read_receipts.jsonl"


def load_events(ledger: Path) -> list[dict]:
    if not ledger.is_file():
        raise SystemExit(f"missing receipt ledger: {ledger}")
    events = []
    for number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as error:
            raise SystemExit(f"{ledger}:{number}: not JSON ({error})") from error
    return events


def output_strings(event: dict) -> list[str]:
    """Every path-like string in a receipt's `outputs`, whatever shape it takes.

    The ledger holds `outputs` as a list of strings today; a dict or a list of objects has been
    written in the past, and a shape this function cannot read would silently make every manifest
    UNCHECKABLE — the failure mode that is indistinguishable from a true zero.
    """
    outputs = event.get("outputs") or []
    if isinstance(outputs, dict):
        outputs = list(outputs.values())
    if isinstance(outputs, str):
        outputs = [outputs]
    flat: list[str] = []
    for item in outputs:
        if isinstance(item, str):
            flat.append(item)
        elif isinstance(item, dict):
            flat.extend(str(value) for value in item.values())
        elif isinstance(item, (list, tuple)):
            flat.extend(str(value) for value in item)
    return flat


def study_pmid(event: dict) -> str:
    """The receipt's OWN pmid, off `study_id`, never regex-scraped from the whole record.

    A DOI carries 7-to-9 digit runs (`10.15252/emmm.202114599`), so a regex over the serialised
    event matches the DOI before the PMID and mis-attributes the reading. Measured: that mistake
    alone moved UNCHECKABLE from 3 to 33.
    """
    study = event.get("study_id")
    if not isinstance(study, dict):
        return ""
    return str(study.get("pmid") or "")


def naming_events(events: list[dict], pmid: str, filename: str) -> list[str]:
    """Same-study event ids whose outputs name this manifest file, in ledger (append) order."""
    return [str(event.get("event_id") or "") for event in events
            if study_pmid(event) == pmid
            and any(filename in text for text in output_strings(event))]


def assess(manifest_path: Path, events: list[dict]) -> Finding:
    pmid = manifest_path.stem.removeprefix("PMID")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        return Finding(manifest_path.name, pmid, "", "UNKNOWN_EVENT", "", [],
                       f"manifest is not JSON: {error}")
    declared = str(manifest.get("receipt") or "")
    naming = naming_events(events, pmid, manifest_path.name)
    known = {str(event.get("event_id") or "") for event in events}
    if not declared:
        return Finding(manifest_path.name, pmid, "", "NO_RECEIPT", naming[0] if naming else "",
                       naming, "the schema validator refuses a manifest without this field")
    if declared not in known:
        return Finding(manifest_path.name, pmid, declared, "UNKNOWN_EVENT",
                       naming[0] if naming else "", naming,
                       "no ledger event carries this id")
    if not naming:
        return Finding(manifest_path.name, pmid, declared, "UNCHECKABLE", "", [],
                       "no same-study event names this manifest among its outputs; the ledger "
                       "cannot answer, and an append-only ledger is not rewritten to make it")
    if declared == naming[0]:
        return Finding(manifest_path.name, pmid, declared, "CONFORMS", naming[0], naming)
    if declared in naming:
        return Finding(manifest_path.name, pmid, declared, "NOT_THE_PRODUCER", naming[0], naming,
                       "this reading touched the manifest, but an earlier same-study reading "
                       "produced it")
    return Finding(manifest_path.name, pmid, declared, "UNNAMED", naming[0], naming,
                   "the declared receipt's outputs do not name this manifest at all")


def survey(root: Path, disease: str, pmid: str = "") -> list[Finding]:
    directory = manifest_dir(root, disease)
    if not directory.is_dir():
        raise SystemExit(f"missing manifest directory: {directory}")
    events = load_events(ledger_path(root, disease))
    paths = sorted(directory.glob(f"PMID{pmid}*.json" if pmid else "PMID*.json"))
    return [assess(path, events) for path in paths]


def render(findings: list[Finding]) -> str:
    counts: dict[str, int] = {}
    for finding in findings:
        counts[finding.verdict] = counts.get(finding.verdict, 0) + 1
    lines = [f"{len(findings)} manifest(s) · "
             + " · ".join(f"{verdict} {count}" for verdict, count in sorted(counts.items())),
             "",
             "A manifest's `receipt` names the reading that PRODUCED it: the earliest same-study "
             "ledger event whose outputs name the manifest file (decided 2026-09-28; "
             "fulltext_read_receipt.md)."]
    defects = [finding for finding in findings if finding.verdict in DEFECTS]
    if defects:
        lines += ["", f"{len(defects)} non-conforming (ceiling {BASELINE_DEFECTS}):"]
        for finding in defects:
            lines.append(f"  {finding.verdict:<16} {finding.manifest}")
            lines.append(f"      declared  {finding.declared or '—'}")
            lines.append(f"      should be {finding.should_be or '—'}")
            lines.append(f"      names it  {', '.join(finding.naming) or '—'}")
            if finding.note:
                lines.append(f"      {finding.note}")
        lines.append("  NOTHING IS REPAIRED HERE: this tool reports. The instrument that writes "
                     "the field is `manifest_receipt_repoint.py --pmid <PMID>` (dry run; add "
                     "--apply), which re-derives the target through this module rather than "
                     "taking one from its caller, and refuses the classes the ledger cannot "
                     "settle. `rechain --repoint-manifests` follows a rename and is still "
                     "forbidden for a target decision.")
    unchecked = [finding for finding in findings if finding.verdict == "UNCHECKABLE"]
    if unchecked:
        lines += ["", f"{len(unchecked)} UNCHECKABLE — reported, not a defect: "
                      + ", ".join(finding.manifest for finding in unchecked)]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--pmid", default="", help="one manifest, by its PMID")
    parser.add_argument("--check", action="store_true",
                        help=f"exit 1 when the non-conforming count exceeds the declared ceiling "
                             f"of {BASELINE_DEFECTS}")
    parser.add_argument("--max-defects", type=int, default=None,
                        help="override the ceiling (lower it as the tail is repaired; "
                             "never raise it)")
    parser.add_argument("--json", action="store_true")
    arguments = parser.parse_args(argv)

    findings = survey(arguments.root, arguments.disease, arguments.pmid)
    defects = [finding for finding in findings if finding.verdict in DEFECTS]
    ceiling = BASELINE_DEFECTS if arguments.max_defects is None else arguments.max_defects
    if arguments.json:
        print(json.dumps({"ceiling": ceiling, "defects": len(defects),
                          "findings": [asdict(finding) for finding in findings]},
                         ensure_ascii=False, indent=1))
    else:
        print(render(findings))
    if arguments.check and not arguments.pmid and len(defects) > ceiling:
        print(f"\nFAIL: {len(defects)} non-conforming manifest(s) exceeds the ceiling of "
              f"{ceiling}. A new manifest whose `receipt` does not name the reading that "
              "produced it is a defect at write time, not a convention.", file=sys.stderr)
        return 1
    if arguments.check and arguments.pmid and defects:
        print(f"\nFAIL: {findings[0].manifest} is {findings[0].verdict}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
