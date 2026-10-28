#!/usr/bin/env python3
"""Offline checker for needs.json (the biological needs table of the repurposing module).

It protects a few invariants and nothing else:
  * ids are unique and the required fields are present;
  * track and goal are two separate fields with their allowed values;
  * evidence scopes (per need and per observation) are in the vocabulary, and a need-level scope is backed by
    at least one observation carrying it;
  * pointers resolve: a manifest locator names an existing manifest, an entry index in range and an
    anchor text that occurs in that entry; a document locator exists; registry ids, hypothesis ids and
    card files that are cited exist.

It does not judge whether an anchor supports its sentence, whether a statement is true, or what a need
should say. Editing a need is an ordinary revision of needs.json; run this afterwards.

Usage: python3 disease-models/wwox/research/drug_repurposing/needs/check_needs.py [--file PATH] [--summary]
Exit status: 0 no problems, 1 problems, 2 the checker could not run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))

TRACKS = {"A", "B"}
GOALS = {"deep_recovery", "partial_benefit"}
SCOPES = {"WWOX_EXPERIMENT_IN_DEE_SYSTEM", "WWOX_BIOLOGY_OTHER_CONTEXT", "OTHER_DISEASE_PRECEDENT", "COMPUTATIONAL_RESULT", "UNVERIFIED_HYPOTHESIS"}
NEED_KEYS = ("id", "label", "track", "goal", "observed", "inferred", "intervention_direction", "counter_evidence", "sources", "targets", "evidence_scope")
OBS_KEYS = ("id", "statement", "evidence_scope", "locators")
_VIEW: dict = {}


def registry_ids(root: Path) -> set[str]:
    if root not in _VIEW:
        import registry_records as rr
        ids: set[str] = set()
        for stem in ("claim_registry_current", "discovery_ledger_current", "dismissal_ledger_current", "paper_registry_current"):
            for r in rr.parse_records(root, "wwox", stem):
                if r.kind == "record":
                    ids.add(rr.identity_token(r.record_id))
        _VIEW[root] = ids
    return _VIEW[root]


def check(doc: dict, root: Path = ROOT) -> tuple[list[str], dict]:
    problems: list[str] = []
    info = {"needs": len(doc.get("needs", [])), "observations": 0, "locators": {"manifest": 0, "document": 0, "registry": 0, "gap": 0}}
    ids = registry_ids(root)
    hyp = set(re.findall(r"^### (HYP-\d{8}-\d{2})\b", (root / "disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md").read_text(encoding="utf-8"), re.M))
    drp = root / "disease-models/wwox/research/drug_repurposing"
    manifests: dict[str, list] = {}
    seen: set[str] = set()
    for n in doc.get("needs", []):
        nid = n.get("id", "?")
        if nid in seen:
            problems.append(f"{nid}: duplicate id")
        seen.add(nid)
        for k in NEED_KEYS:
            if k not in n:
                problems.append(f"{nid}: missing field {k}")
        for fld, allowed in (("track", TRACKS), ("goal", GOALS)):
            v = n.get(fld)
            if not isinstance(v, dict) or v.get("value") not in allowed:
                problems.append(f"{nid}: {fld} must be an object whose value is one of {sorted(allowed)}")
        if not n.get("evidence_scope") or not set(n["evidence_scope"]) <= SCOPES:
            problems.append(f"{nid}: evidence_scope outside the vocabulary")
        else:
            unbacked = set(n["evidence_scope"]) - {o.get("evidence_scope") for o in n.get("observed", [])}
            if unbacked:
                problems.append(f"{nid}: need-level scope not carried by any observation: {sorted(unbacked)}")
        src = n.get("sources", {})
        for c in src.get("cards", []):
            m = re.match(r"^(\S+)(?: \((cards_early)\))?$", c)
            if not (drp / ("cards_early" if m and m.group(2) else "cards") / f"{m.group(1) if m else c}.card.json").is_file():
                problems.append(f"{nid}: card not found: {c}")
        for h in src.get("hypotheses", []):
            if h not in hyp:
                problems.append(f"{nid}: hypothesis not in the ledger: {h}")
        for dp in src.get("documents", []):
            if not (root / dp).is_file():
                problems.append(f"{nid}: document missing: {dp}")
        for rid in src.get("registry_ids", []):
            if rid not in ids:
                problems.append(f"{nid}: registry id does not resolve: {rid}")
        for o in n.get("observed", []):
            info["observations"] += 1
            oid = f"{nid}/{o.get('id', '?')}"
            for k in OBS_KEYS:
                if k not in o:
                    problems.append(f"{oid}: missing field {k}")
            if o.get("evidence_scope") not in SCOPES:
                problems.append(f"{oid}: evidence_scope outside the vocabulary")
            for loc in o.get("locators", []):
                kind = loc.get("kind")
                if kind in info["locators"]:
                    info["locators"][kind] += 1
                if kind == "manifest":
                    mp = root / loc["manifest"]
                    if not mp.is_file():
                        problems.append(f"{oid}: manifest missing {loc['manifest']}")
                        continue
                    if loc["manifest"] not in manifests:
                        manifests[loc["manifest"]] = json.loads(mp.read_text(encoding="utf-8"))["verbatim_locators"]["entries"]
                    entries = manifests[loc["manifest"]]
                    if not (0 <= loc["entry"] < len(entries)):
                        problems.append(f"{oid}: entry {loc['entry']} out of range in {Path(loc['manifest']).name} ({len(entries)} entries)")
                    elif loc["anchor"].lower() not in (entries[loc["entry"]].get("proposition", "") + " " + entries[loc["entry"]].get("snippet", "")).lower():
                        problems.append(f"{oid}: anchor {loc['anchor']!r} not in {Path(loc['manifest']).name} entry {loc['entry']}")
                elif kind == "document":
                    if not (root / loc["path"]).is_file():
                        problems.append(f"{oid}: document missing {loc['path']}")
                elif kind == "registry":
                    for rid in loc["ids"]:
                        if rid not in ids:
                            problems.append(f"{oid}: registry id does not resolve {rid}")
                elif kind != "gap":
                    problems.append(f"{oid}: unknown locator kind {kind}")
    return problems, info


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Offline checker for needs.json (see the module docstring).")
    ap.add_argument("--file", default=str(HERE / "needs.json"), help="needs table to check (default: the one beside this script)")
    ap.add_argument("--summary", action="store_true", help="print one line per need")
    a = ap.parse_args(argv)
    try:
        doc = json.loads(Path(a.file).read_text(encoding="utf-8"))
        problems, info = check(doc)
    except Exception as exc:
        print(f"CHECKER ERROR: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    print(f"needs: {info['needs']}  observations: {info['observations']}  locators: {info['locators']}")
    if a.summary:
        for n in doc["needs"]:
            print(f"  {n['id']:44s} track {n['track']['value']} goal {n['goal']['value']:15s} {n.get('basis', '?'):20s} observations {len(n['observed'])}")
    for p in problems:
        print("PROBLEM:", p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
