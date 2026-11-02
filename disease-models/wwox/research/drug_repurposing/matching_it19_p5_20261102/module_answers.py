#!/usr/bin/env python3
"""IT19 P5 step 3: the module's own answers for the selected pairs, produced from the code alone.

  module_answers.py --selection F --catalog F --needs F [--roles F] [--artefacts F] --out F --digest F [--guard]

For every selected (need, compound) pair it records what the ACTIVE path
(`framework/scripts/repurposing_search.py`) says today: whether it proposes the compound for the
need, the consistency label it attaches, the ChEMBL record and action behind it, whether that record
is above single-protein level, and the IT18 locked L v1 / L v2 labels carried unchanged. `--guard`
runs the same path with the module-wide group-transfer guard switched on, so the two runs are
comparable. No reference file is read by this script.
"""
import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
sys.path.insert(0, str(REPO / "framework/scripts"))
import compound_catalog as cc  # noqa: E402
import repurposing_search as rs  # noqa: E402

HEADER = ["pair_id", "need_id", "parent_chembl_id", "active_path_proposes", "active_consistency", "active_reason",
          "chembl_record", "chembl_record_type", "chembl_action", "record_components", "components_in_module_targets",
          "it18_L_v1", "it18_L_v2"]


def read_tsv(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def answers(selection, entries, needs, roles, artefacts, guard):
    module_symbols = rs.module_intervention_symbols(needs)
    idx = rs.Index(entries, artefacts, module_symbols if guard else None)
    by_need = {n["id"]: n for n in needs}
    per_need = {}
    fam = {}
    for e in entries:
        cid = (e.get("ids") or {}).get("chembl")
        par = (e["relations"].get("parent") or "").replace("CAT:", "") or cid
        if par:
            fam.setdefault(par, []).append(e)
    out = []
    for s in selection:
        nid, pid = s["need_id"], s["parent_chembl_id"]
        if nid not in per_need:
            per_need[nid] = rs.associations_for_need(by_need[nid], idx, roles)["associations"]
        ids = {e["id"] for e in fam.get(pid, [])} | {"CAT:" + pid}
        rows = [a for a in per_need[nid] if a["catalogue_id"] in ids and a["target_kind"] in rs.LINK_KINDS
                and a["link_source"].startswith("ChEMBL") and not a["excluded_from_counts"]]
        if not rows:
            out.append([s["pair_id"], nid, pid, "no", "-", "no ChEMBL human mechanism row on this need's intervention targets",
                        "-", "-", "-", "", "", s["it18_L_v1"], s["it18_L_v2"]])
            continue
        labels = {a["consistency"] for a in rows}
        label = "consistent" if labels == {"consistent"} else "opposed" if labels == {"opposed"} else \
            "direction_unresolved" if labels <= {"direction_unresolved"} else "mixed:" + "|".join(sorted(labels))
        recs, types, acts, comps, inmod = set(), set(), set(), set(), set()
        for a in rows:
            for e in fam.get(pid, []) + [x for x in entries if x["id"] == "CAT:" + pid]:
                for t in e["targets"]:
                    if t.get("source") != "ChEMBL curated mechanism" or t.get("organism") != "Homo sapiens":
                        continue
                    g = {x.upper() for x in t.get("gene_symbols") or []}
                    if a["target"].upper() not in g:
                        continue
                    recs.add(t["target_id"])
                    types.add(t.get("target_type") or "SINGLE PROTEIN")
                    acts.add((t.get("action_type") or "UNSTATED").upper())
                    comps.add(len(g))
                    inmod.add(len(g & rs.module_intervention_symbols(needs)))
        why = sorted({a["consistency_why"] for a in rows})[0]
        out.append([s["pair_id"], nid, pid, "yes", label, why[:200], ";".join(sorted(recs)), ";".join(sorted(types)),
                    ";".join(sorted(acts)), ";".join(str(x) for x in sorted(comps)), ";".join(str(x) for x in sorted(inmod)),
                    s["it18_L_v1"], s["it18_L_v2"]])
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selection", required=True)
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--needs", required=True)
    ap.add_argument("--roles", default=str(rs.DEFAULT_ROLES))
    ap.add_argument("--artefacts", default=str(rs.DEFAULT_ARTEFACTS))
    ap.add_argument("--out", required=True)
    ap.add_argument("--digest", required=True)
    ap.add_argument("--guard", action="store_true", help="run with the module-wide group-transfer guard on")
    a = ap.parse_args(argv)
    sel = read_tsv(a.selection)
    entries = cc.load(Path(a.catalog))
    needs = rs.load_needs(Path(a.needs))["needs"]
    rows = answers(sel, entries, needs, rs.load_roles(Path(a.roles)), rs.load_artefacts(Path(a.artefacts)), a.guard)
    with open(a.out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(HEADER)
        w.writerows(rows)
    dig = {"answers_sha256": hashlib.sha256(Path(a.out).read_bytes()).hexdigest(),
           "selection_sha256": hashlib.sha256(Path(a.selection).read_bytes()).hexdigest(),
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "repurposing_search_sha256": hashlib.sha256((REPO / "framework/scripts/repurposing_search.py").read_bytes()).hexdigest(),
           "catalog_sha256": hashlib.sha256(Path(a.catalog).read_bytes()).hexdigest(),
           "needs_sha256": hashlib.sha256(Path(a.needs).read_bytes()).hexdigest(),
           "guard": bool(a.guard), "rows": len(rows)}
    Path(a.digest).write_text(json.dumps(dig, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"rows": len(rows), "proposed": sum(1 for r in rows if r[3] == "yes"),
                      "consistency": {k: sum(1 for r in rows if r[4] == k) for k in sorted({r[4] for r in rows})},
                      "guard": bool(a.guard)}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
