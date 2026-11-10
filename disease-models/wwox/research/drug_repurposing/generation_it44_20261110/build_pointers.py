#!/usr/bin/env python3
"""IT44 P2: pointers_it44.tsv and summary_it44.tsv from the activity-path outputs (run activity_search.py first; the full activity tables are not committed). A pointer is a molecule with a catalogue status and an OK read state; a screening deposit or a truncated read is counted, never listed.
  python3 build_pointers.py OUTDIR [OUTDIR ...]"""
import csv, json, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
base = defaultdict(set)
for f in (DR / "generation_it41_20261109/molecules.tsv", DR / "generation_it43_20261110/s9/molecules.tsv", DR / "generation_it43_20261110/s10/molecules.tsv", HERE / "s11/molecules.tsv"):
    if f.exists():
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"): base[r["relation_id"]].add(r["molecule"].replace("CAT:", ""))
allm = []
unres = defaultdict(list)
for d in sys.argv[1:]:
    mf = Path(d) / "activity_manifest.json"
    if mf.exists():
        for k, v in json.load(open(mf)).get("_symbols", {}).items():
            if v != "TARGETS_FOUND": unres[k.split(":")[0]].append(k.split(":")[1])
for d in sys.argv[1:]: allm += list(csv.DictReader(open(Path(d) / "activity_molecules.tsv", encoding="utf-8"), delimiter="\t"))
F = ["relation_id", "parent_chembl_id", "catalogue_name", "catalogue_status", "catalogue_origin", "in_mechanism_path", "read_state", "n_activities", "n_functional", "n_documents", "types", "targets", "coverage", "verdict", "unknown_fields"]
S = []
with open(HERE / "pointers_it44.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, F, delimiter="\t", lineterminator="\n", extrasaction="ignore"); w.writeheader()
    for m in allm:
        if m["catalogue_status"] != "none" and m["read_state"] == "OK": m["in_mechanism_path"] = "yes" if m["parent_chembl_id"] in base[m["relation_id"]] else "no"; w.writerow(m)
for rid in sorted({m["relation_id"] for m in allm} | {"S4"}, key=lambda s: int(s[1:])):
    ms = [m for m in allm if m["relation_id"] == rid]; ok = [m for m in ms if m["read_state"] == "OK"]; cs = [m for m in ok if m["catalogue_status"] != "none"]
    S.append(dict(relation_id=rid, activity_molecules=len(ms), screening_deposit_or_truncated=len(ms) - len(ok), ok_molecules=len(ok), pointers_with_catalogue_status=len(cs), pointers_not_in_mechanism_path=sum(1 for m in cs if m["parent_chembl_id"] not in base[rid]), ok_research_compounds_no_status=len(ok) - len(cs), unread_symbols=";".join(sorted(set(unres[rid]))) or "none"))
with open(HERE / "summary_it44.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, list(S[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(S)
for s in S: print(s)
