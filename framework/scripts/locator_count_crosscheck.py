#!/usr/bin/env python3
"""Does the registry's declared locator count match the manifest it names?

🔴 WHY THIS EXISTS, and it is a measurement rather than a worry.

On 2026-09-21 a scientist checked four `paper_registry_current.md` records against the
manifests on disk and found three wrong. The full sweep run the same hour found **16 of 34
declarations wrong**, and the pattern is the finding:

    EVERY ONE OF THE SIXTEEN UNDERSTATES THE MANIFEST. Not one overstates.
    Deltas run +2 to +27 (PMID 38499540 declared 7, manifest holds 34).

Random transcription error produces both directions. One direction means a systematic
cause, and the direction rules out the frightening reading: the registry is not claiming
evidence it does not have, it is **failing to claim evidence it does have**. The counts
were true when written and were never re-derived as their manifests grew — a locator count
is a *measurement of another file*, and this repository already knows that a measurement
copied by hand decays while the thing it measures moves on.

Two of the wrong records carry, in their own text, the sentence *"declaration reconciled
from the ledger by `CC-20260920-REGISTRY-LEDGER-DEPTH-01` (BATCH_20260920_001)"* — **the
batch that reconciled those declarations left both counts wrong.** A reconciliation that
does not re-derive is a restatement.

One further cause is proven and worth naming, because two independent actors hit it on the
same day: `verbatim_locators` is an **object**, not a list. `len()` on it returns **6** —
its keys (`waived`, `source_fulltext_indexed`, `source_fulltext_indexed_evidence`,
`abstract_anchoring_waived`, `surface_note`, `entries`) — while the locators live in
`entries`. Any count of 6 in this repository should be read twice.

WHAT THIS ASKS, and it is one mechanical question and no more:

    for every `deepdive_manifests/PMID<n>.json (N locators` declaration in the registry,
    does N equal `len(manifest["verbatim_locators"]["entries"])`?

WHAT THIS DOES NOT ASK. Whether the locators are good, whether they verify, whether the
reading was adequate, or whether the manifest should hold more. `deepdive_manifest.py`,
`locator_audit.py` and `dossier_quote_audit.py` own those questions. **This one only asks
whether a number in one file still describes another file.**

Exit codes: 0 every declaration matches · 1 at least one mismatch · 2 usage/IO error.
Read-only: it modifies nothing, ever.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REGISTRY = "disease-models/{disease}/registries/paper_registry_current.md"
MANIFEST_DIR = "disease-models/{disease}/research/deepdive_manifests"

# `deepdive_manifests/PMID12345678.json` optionally in backticks, then `(N locators`.
# Anchored on the manifest path so a bare "(7 locators" in prose is never mistaken for a
# declaration about a specific file — the defect this tool reports is a broken *link*
# between two named artefacts, not a loose number.
DECLARATION_RE = re.compile(
    r"deepdive_manifests/PMID(?P<pmid>\d{6,8})\.json`?\s*\(\s*(?P<count>\d+)\s+locators",
    re.IGNORECASE,
)


def manifest_entry_count(manifest: dict) -> int | None:
    """How many locators the manifest actually holds.

    Tolerates both shapes deliberately. The current schema puts the locators under
    `verbatim_locators.entries`; older manifests carry `verbatim_locators` as a bare list.
    A tool that understood only one shape would report the other as zero, and a zero from a
    parser is not evidence.
    """
    locators = manifest.get("verbatim_locators")
    if isinstance(locators, dict):
        entries = locators.get("entries")
        return len(entries) if isinstance(entries, list) else None
    if isinstance(locators, list):
        return len(locators)
    return None


def load_manifests(root: Path, disease: str) -> dict[str, tuple[int | None, Path]]:
    out: dict[str, tuple[int | None, Path]] = {}
    directory = root / MANIFEST_DIR.format(disease=disease)
    if not directory.is_dir():
        return out
    for path in sorted(directory.glob("PMID*.json")):
        try:
            manifest = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        pmid = str(manifest.get("pmid") or "")
        if pmid:
            out[pmid] = (manifest_entry_count(manifest), path)
    return out


def scan(text: str, manifests: dict[str, tuple[int | None, Path]]) -> list[dict]:
    findings = []
    for match in DECLARATION_RE.finditer(text):
        pmid = match.group("pmid")
        declared = int(match.group("count"))
        line = text.count("\n", 0, match.start()) + 1
        actual, path = manifests.get(pmid, (None, None))
        findings.append({
            "line": line,
            "pmid": pmid,
            "declared": declared,
            "actual": actual,
            "manifest": path.name if path else None,
            "state": (
                "no_manifest" if actual is None and path is None else
                "unreadable" if actual is None else
                "match" if declared == actual else "mismatch"
            ),
        })
    return findings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", default=".", type=Path)
    parser.add_argument("--disease", default="wwox")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    registry = args.root / REGISTRY.format(disease=args.disease)
    if not registry.exists():
        print(f"ERROR: {registry} not found", file=sys.stderr)
        return 2

    manifests = load_manifests(args.root, args.disease)
    findings = scan(registry.read_text(encoding="utf-8"), manifests)

    if args.json:
        print(json.dumps(findings, indent=2))
        return 1 if any(f["state"] == "mismatch" for f in findings) else 0

    mismatches = [f for f in findings if f["state"] == "mismatch"]
    matches = [f for f in findings if f["state"] == "match"]
    missing = [f for f in findings if f["state"] in ("no_manifest", "unreadable")]

    if not findings:
        # Anti-vacuity. A guard whose population is empty passes by agreeing with nothing,
        # and this file's whole value is that it looked at something.
        print("NO DECLARATIONS FOUND — this is a FAILURE of the scan, not a clean registry. "
              "The declaration format has changed or the registry moved.")
        return 2

    for f in sorted(mismatches, key=lambda f: f["line"]):
        delta = f["actual"] - f["declared"]
        print(f"  [MISMATCH] {registry.name}:{f['line']} — PMID {f['pmid']}: "
              f"declared {f['declared']}, manifest holds {f['actual']} ({delta:+d})")
    for f in sorted(missing, key=lambda f: f["line"]):
        print(f"  [NO MANIFEST] {registry.name}:{f['line']} — PMID {f['pmid']}: "
              f"declares {f['declared']} locators, manifest absent or unreadable")

    print(f"\ndeclarations: {len(findings)} | match: {len(matches)} | "
          f"mismatch: {len(mismatches)} | manifest absent: {len(missing)}")

    if mismatches:
        under = [f for f in mismatches if f["actual"] > f["declared"]]
        over = [f for f in mismatches if f["actual"] < f["declared"]]
        print(f"direction: {len(under)} understate the manifest, {len(over)} overstate it.")
        if over:
            print("🔴 An OVERSTATEMENT is the serious direction: the registry claims evidence "
                  "depth the manifest does not hold. Treat it before any understatement.")
        else:
            print("Every mismatch understates. The registry is failing to claim evidence it "
                  "has — which is the benign direction, and still a false number in a "
                  "canonical file.")
        print("VERDICT: MISMATCH — re-derive from the manifests; do not retype.")
        return 1

    print("VERDICT: OK — every declared locator count matches its manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
