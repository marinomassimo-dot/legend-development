#!/usr/bin/env python3
"""IT24 P2: how many proposal rows of a stage table can be compared by chemical identity, counted as rows, families and distinct substances,
using only routes the repository already holds (no query). Routes, in the order they are trusted:
  R0 catalogue InChIKey of the family's own record
  R1 merged claim-name bridge (attribution_screen_it21.bridge_claim_name_ligands -> family_bridge): the DGIdb-only twin IS the ChEMBL record
  R2 GtoPdb ligand InChIKey of an UNMERGED reconciliation decision (related_not_merged / out_of_selection / unresolved): a structure is known,
     but it is not asserted to be the same substance as a ChEMBL family; reported separately, never merged
  R3 GtoPdb ligand structure through the record's OWN concept-id ligand (ids.iuphar_ligand, one ligand, not labelled/radioactive, reconciliation not rejected):
     the DGIdb record names that ligand itself, so its structure is the record's structure; still not merged into any ChEMBL family
  none: identity unresolved (stays UNKNOWN)
Usage: identity_census_it24.py --proposals PATH --questions Q2,Q4,Q8 --out DIR   (LEGEND_CATALOG_CACHE must point at the catalogue cache)"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, collections, csv, gzip, json, os, re
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = HERE.parent
REPO = DR.parents[3]
sys.path.insert(0, str(REPO / "framework/scripts")); sys.path.insert(0, str(DR / "generation_it21_p2_20261103"))
import compound_catalog as cc, repurposing_search as rs, attribution_screen_it21 as AS


def tsv(p):
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--proposals", required=True); ap.add_argument("--questions", default=""); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    entries = cc.load(DR / "catalog" / "catalog.jsonl.gz")
    fam = rs.families(entries)
    E = {e["id"]: e for e in entries}
    bridges = AS.bridge_claim_name_ligands(entries)
    fb = AS.family_bridge(bridges, fam)
    lig, _, _ = AS.load_gtopdb_affinities()
    recon_ik = {}                       # twin entry id -> (decision, reason, GtoPdb InChIKey) for unmerged decisions
    for eid, recs in bridges.items():
        for r in recs:
            ik = (lig.get(r["ligand_id"]) or {}).get("InChIKey")
            if r["decision"] != "merged" and ik:
                recon_ik.setdefault(fam[eid], []).append((r["decision"], r["reason"], ik, r["ligand_id"]))
    recon = {r["candidate"]: r for r in tsv(DR / "catalog" / "ligand_reconciliation.tsv")}
    concept_ik = {}                     # family -> {(ligand id, InChIKey)} from the record's own concept-id ligand
    for e in entries:
        if e.get("origin") != "dgidb_only":
            continue
        for lid in (e["ids"].get("iuphar_ligand") or []):
            l = lig.get(str(lid))
            if not l or not l.get("InChIKey") or l.get("Labelled") == "yes" or l.get("Radioactive") == "yes":
                continue
            if (recon.get(e["id"]) or {}).get("decision") == "rejected_conflict":
                continue
            concept_ik.setdefault(fam[e["id"]], set()).add((str(lid), l["InChIKey"]))
    fam_ik = {}
    for e in entries:
        k = (e.get("ids") or {}).get("inchikey")
        if k and e["id"] == e["id"]:
            fam_ik.setdefault(fam[e["id"]], k)
    qs = set(filter(None, a.questions.split(",")))
    rows = [r for r in tsv(a.proposals) if not qs or r["question"] in qs]
    out, fams = [], {}
    for r in rows:
        f = r["family_id"]
        if f in fam_ik:
            st, ik, via = "R0_catalogue_inchikey", fam_ik[f], "catalogue record"
        elif f in fb and fb[f] in fam_ik:
            st, ik, via = "R1_merged_bridge", fam_ik[fb[f]], "claim-name ligand -> " + fb[f]
        elif f in concept_ik and len({k.split("-")[0] for _, k in concept_ik[f]}) == 1:
            ligs = sorted(concept_ik[f])
            st, ik, via = "R3_gtopdb_concept_ligand_structure", ligs[0][1], "iuphar.ligand " + ",".join(x[0] for x in ligs)
        elif f in recon_ik:
            d = sorted(recon_ik[f])
            st, ik, via = "R2_structure_known_not_merged", d[0][2], ";".join(sorted({x[0] + ":" + x[1] for x in d}))
        else:
            st, ik, via = "none_unresolved", "", ""
        out.append(dict(proposal_id=r["proposal_id"], question=r["question"], hypothesis=r["hypothesis"], compound=r["compound"], family_id=f, route=st, inchikey=ik, via=via))
        fams[f] = (st, ik, r["compound"])
    os.makedirs(a.out, exist_ok=True)
    cols = list(out[0])
    with open(Path(a.out) / "identity_routes.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
    byr = collections.Counter(x["route"] for x in out)
    fr = collections.Counter(v[0] for v in fams.values())
    subs = collections.defaultdict(set)
    for v in fams.values():
        subs[v[0]].add(v[1].split("-")[0] if v[1] else re.sub(r"[^a-z0-9]", "", v[2].lower()))
    summ = dict(rows=len(out), families=len(fams), rows_by_route=dict(byr), families_by_route=dict(fr), distinct_substances_by_route={k: len(v) for k, v in subs.items()},
                bridges_merged_families=len(fb))
    json.dump(summ, open(Path(a.out) / "summary.json", "w"), indent=1, sort_keys=True)
    print(json.dumps(summ, indent=1, sort_keys=True))


main()
