#!/usr/bin/env python3
"""Assemble a schema-v2 deep-dive manifest from a JSON spec, computing every artefact digest.

WHY THIS EXISTS (2026-10-20, W4-W2A-C). Eight first-read manifests in one wave were assembled by hand:
each carries the same fourteen required slots, a SHA-256 for every artefact, and the same skills block,
and the only defects the validator found were assembly slips (a digest typed from a stale file, a missing
slot). This tool does the mechanical part and nothing else: it never writes a locator, a proposition or a
verdict. Those come from the reader in the spec. It refuses a missing artefact, refuses to overwrite an
existing manifest without --force, and leaves the `retraction_check.dependencies` block to
`dependency_integrity.py screen --manifest-block` (run from the checkout that holds the snapshot).

Usage:
    python3 framework/scripts/manifest_scaffold.py --spec spec.json --root <artefact root> --out <manifest dir>
Then validate with `deepdive_manifest.py --disease <d> --pmid <PMID> --verify-artifacts --require-current-schema`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

REQUIRED = ("pmid", "doi", "receipt", "group_assessment", "field_density", "multihop", "corpus_crossquery",
            "retraction_result", "artifacts", "entries", "indexed_evidence")
DEFAULT_SKILLS = [
    {"skill": "find-fulltext", "used": True},
    {"skill": "legend-deepdive", "used": True, "reason": "Run inline; the manifest and the analysis note carry what the skill would produce."},
    {"skill": "legend-discovery", "used": False, "reason": "Leads are staged in a commit candidate; the shared ledger is written by the Orchestrator."},
    {"skill": "legend-hypothesis-forge", "used": False, "reason": "No lever matured by this reading."},
    {"skill": "legend-safety-triage", "used": False, "reason": "No molecule is triaged."},
    {"skill": "legend-commit", "used": False, "reason": "Scientists do not touch the four current files."},
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def build(spec: dict, root: Path) -> dict:
    missing = [k for k in REQUIRED if k not in spec]
    if missing:
        raise ValueError(f"spec lacks required keys: {missing}")
    artifacts = []
    for a in spec["artifacts"]:
        p = root / a["path"]
        if not p.is_file():
            raise FileNotFoundError(f"artefact absent under {root}: {a['path']}")
        a = dict(a)
        a["sha256"] = sha256(p)
        artifacts.append(a)
    return {
        "schema_version": 2,
        "pmid": spec["pmid"],
        "doi": spec["doi"],
        "receipt": spec["receipt"],
        "context_policy": spec.get("context_policy", "SOURCE_FIRST"),
        "landing": spec.get("landing", []),
        "skills_considered": spec.get("skills_considered", DEFAULT_SKILLS),
        "group_assessment": spec["group_assessment"],
        "field_density": spec["field_density"],
        "multihop": spec["multihop"],
        "corpus_crossquery": spec["corpus_crossquery"],
        "retraction_check": {"checked": True, "result": spec["retraction_result"]},
        "source_artifacts": artifacts,
        "verbatim_locators": {
            "waived": False,
            "source_fulltext_indexed": spec.get("indexed", True),
            "source_fulltext_indexed_evidence": spec["indexed_evidence"],
            "abstract_anchoring_waived": spec.get("abstract_anchoring_waived",
                "No locator uses the abstract as evidence; every locator quotes the body, a table, a supplement text layer or a figure image."),
            "entries": spec["entries"],
        },
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--spec", required=True)
    ap.add_argument("--root", required=True, help="artefact root (the shared checkout that holds files/)")
    ap.add_argument("--out", required=True, help="directory that receives PMID<PMID>.json")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args(argv)
    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    try:
        m = build(spec, Path(a.root))
    except (ValueError, FileNotFoundError) as e:
        print(f"refused: {e}", file=sys.stderr)
        return 2
    out = Path(a.out) / f"PMID{m['pmid']}.json"
    if out.exists() and not a.force:
        print(f"refused: {out} exists (use --force)", file=sys.stderr)
        return 3
    out.write_text(json.dumps(m, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(m['source_artifacts'])} artefacts, {len(m['verbatim_locators']['entries'])} locators); "
          "next: dependency_integrity.py screen --manifest-block, then deepdive_manifest.py --verify-artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
