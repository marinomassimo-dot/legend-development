#!/usr/bin/env python3
"""EVIDENCE PRESENCE — do the bytes a manifest fingerprints actually exist in THIS checkout?

## The defect this exists to remove

`files/` is gitignored for copyright reasons. A branch, a clone or a fresh worktree therefore
transports every **manifest** and **none of the evidence bytes those manifests fingerprint**.
The protocol already names the hazard — *"a PASS obtained before that temporary workspace
disappears is historically true but operationally unverifiable"* — but nothing measured it.

Measured on **2026-09-09**, `scientist-a`, task `AQEILAN-FT-A-001`. The shared checkout's
`files/` tree was **completely empty**: 0 full texts, 0 figure directories, 12K on disk. The
way that was discovered was by running the strict validator on one PMID and reading **22
BLOCKs**, one per missing artifact, in the middle of a reading. Nothing at session start said
*"this checkout holds none of its evidence"*, and the question is cheap to ask.

All 21 artifacts of `PMID 34268881` were then re-acquired and every one re-derived
**byte-identical** to its declared SHA-256 — which is the other half of why this tool is worth
having. Absence is recoverable and usually cheap. A **digest mismatch** is not: it means the
bytes under a fingerprint changed, and every locator verified against them is in question.
Those two states look identical to a human glancing at `ls`, so they are reported separately
and never merged into "a problem".

## What it does, and what it refuses to do

It reads `deepdive_manifests/*.json`, and for every `source_artifacts[]` entry answers exactly
one question per artifact: **present and matching**, **present and mismatched**, or **absent**.

It changes nothing, fetches nothing and gates nothing by default — the discipline
`artifact_index.py` states and this file follows: *discovery reports, it does not judge*. It
exits 0 whether findings exist or not, so it is safe to run anywhere and safe to run first.

🔴 **`--fail-on-mismatch` is the one exception, and it is deliberately narrow.** It raises exit
status for a **digest mismatch only**, never for absence. Absence is the normal, expected state
of a fresh checkout and making it an error would train every session to ignore the tool. A
mismatch is never normal.

🔴 **It does not verify a reading.** An artifact being present with a matching digest says the
bytes are the ones the manifest names. It says nothing about whether anybody read them, which
is the receipt ledger's question and not this one. Conflating the two is exactly the
`outputs`-attests-reading trap the receipt protocol records.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_root import RootError, add_root_argument, resolve_root_argument  # noqa: E402

PRESENT = "PRESENT"
MISMATCH = "DIGEST_MISMATCH"
ABSENT = "ABSENT"
UNDECLARED = "NO_DIGEST_DECLARED"

_CHUNK = 1 << 20


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(_CHUNK), b""):
            h.update(block)
    return h.hexdigest()


def manifest_paths(root: Path, disease: str | None) -> list[Path]:
    """Every deep-dive manifest, for one disease model or all of them."""
    base = root / "disease-models"
    if not base.is_dir():
        return []
    globs = (
        [base / disease / "research" / "deepdive_manifests"]
        if disease
        else sorted(p for p in base.glob("*/research/deepdive_manifests") if p.is_dir())
    )
    out: list[Path] = []
    for d in globs:
        if d.is_dir():
            out.extend(sorted(d.glob("*.json")))
    return out


def audit_manifest(path: Path, root: Path) -> dict:
    """One manifest -> its artifact verdicts. A manifest that will not parse is a finding."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {"manifest": str(path.relative_to(root)), "error": str(exc), "artifacts": []}

    rows = []
    for index, art in enumerate(data.get("source_artifacts") or []):
        declared = (art or {}).get("sha256")
        rel = (art or {}).get("path")
        if not rel:
            continue
        target = root / rel
        if not target.is_file():
            state, actual = ABSENT, None
        elif not declared:
            state, actual = UNDECLARED, sha256_of(target)
        else:
            actual = sha256_of(target)
            state = PRESENT if actual == declared else MISMATCH
        rows.append(
            {
                "index": index,
                "path": rel,
                "kind": (art or {}).get("kind"),
                "state": state,
                "declared_sha256": declared,
                "actual_sha256": actual,
            }
        )
    return {
        "manifest": str(path.relative_to(root)),
        "pmid": str(data.get("pmid") or path.stem.replace("PMID", "")),
        "artifacts": rows,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=(
            "Report whether the evidence bytes fingerprinted by deep-dive manifests are "
            "present in this checkout, and whether they still match their declared SHA-256."
        )
    )
    add_root_argument(ap)
    ap.add_argument("--disease", help="limit to one disease model (e.g. wwox)")
    ap.add_argument("--pmid", action="append", help="limit to these PMIDs; repeatable")
    ap.add_argument("--json", action="store_true", help="emit one JSON record per manifest")
    ap.add_argument(
        "--fail-on-mismatch",
        action="store_true",
        help="exit non-zero on a DIGEST_MISMATCH only. Absence is never an error here.",
    )
    args = ap.parse_args(argv)

    try:
        root = resolve_root_argument(getattr(args, "root", None))
    except RootError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    wanted = set(args.pmid or [])
    reports = []
    for path in manifest_paths(root, args.disease):
        report = audit_manifest(path, root)
        if wanted and report.get("pmid") not in wanted:
            continue
        reports.append(report)

    totals = {PRESENT: 0, MISMATCH: 0, ABSENT: 0, UNDECLARED: 0}
    for report in reports:
        for row in report["artifacts"]:
            totals[row["state"]] = totals.get(row["state"], 0) + 1

    if args.json:
        for report in reports:
            print(json.dumps(report, ensure_ascii=False))
    else:
        for report in sorted(reports, key=lambda r: r.get("pmid") or ""):
            if report.get("error"):
                print(f"  [UNREADABLE] {report['manifest']}: {report['error']}")
                continue
            rows = report["artifacts"]
            bad = [r for r in rows if r["state"] != PRESENT]
            if not rows:
                continue
            if not bad:
                print(f"  [OK]      PMID {report['pmid']}: {len(rows)}/{len(rows)} present and matching")
                continue
            print(f"  [PARTIAL] PMID {report['pmid']}: {len(rows) - len(bad)}/{len(rows)} present and matching")
            for row in bad:
                marker = "MISMATCH" if row["state"] == MISMATCH else row["state"]
                print(f"            {marker}: {row['path']}")

    total_artifacts = sum(totals.values())
    print(
        f"manifests: {len(reports)} | artifacts: {total_artifacts} | "
        f"present: {totals[PRESENT]} | absent: {totals[ABSENT]} | "
        f"digest_mismatch: {totals[MISMATCH]} | no_digest: {totals[UNDECLARED]}"
    )

    if totals[MISMATCH]:
        print(
            "VERDICT: DIGEST MISMATCH — bytes under a declared fingerprint have changed. "
            "Every locator verified against them is in question until re-derived."
        )
        return 1 if args.fail_on_mismatch else 0
    if totals[ABSENT] and not totals[PRESENT]:
        print(
            "VERDICT: NO LOCAL EVIDENCE — this checkout carries manifests and none of the bytes "
            "they fingerprint. Expected in a fresh checkout; re-acquire before verifying a reading."
        )
        return 0
    if totals[ABSENT]:
        print("VERDICT: PARTIAL — some declared evidence is absent from this checkout.")
        return 0
    print("VERDICT: COMPLETE — every declared artifact is present and matches its digest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
