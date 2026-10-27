#!/usr/bin/env python3
"""Iteration 2 (scientist-d): resolve the BRD codes of the informative LINCS signatures through PUBLIC, versioned metadata
(GSE92742 and GSE70138 pert_info and cell_info from GEO, checksums verified against the series SHA512SUMS) and verify action/target through
ChEMBL (key-less REST, inchi-key lookup; mechanism endpoint). Failed mappings and ambiguities are kept, not dropped.
Usage: lincs_it2_compound_identity.py <this directory> <dir holding the GEO gz files> [--no-network]
Inputs: tool_responses/IT2_S1_l1000fwd_direct.json, IT2_N1_l1000fwd_direct.json, S1 SigCom response + metadata.  Output: derived/lincs_it2_compound_identity.json/.tsv"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]) or len(_sys.argv) < 3:
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, hashlib, json, re, time, urllib.parse, urllib.request
G, D = _sys.argv[1], _sys.argv[2]; net = "--no-network" not in _sys.argv
sums = {}
for fn in ("GSE92742_SHA512SUMS.txt.gz", "GSE70138_SHA512SUMS.txt.gz"):
    for l in gzip.open(f"{D}/{fn}", "rt"):
        h, n = l.split(); sums[n] = h
files = {"p92": "GSE92742_Broad_LINCS_pert_info.txt.gz", "p70": "GSE70138_Broad_LINCS_pert_info_2017-03-06.txt.gz", "c92": "GSE92742_Broad_LINCS_cell_info.txt.gz", "c70": "GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz"}
verified = {}
for k, fn in files.items():
    verified[fn] = hashlib.sha512(open(f"{D}/{fn}", "rb").read()).hexdigest() == sums[fn]
assert all(verified.values()), verified
def tab(fn): return list(csv.DictReader(gzip.open(f"{D}/{fn}", "rt"), delimiter="\t"))
p92 = {r["pert_id"]: r for r in tab(files["p92"])}; p70 = {r["pert_id"]: r for r in tab(files["p70"])}
cells = {r["cell_id"]: r for r in tab(files["c92"])}
for r in tab(files["c70"]): cells.setdefault(r["cell_id"], r)
# ---- collect codes
hits = []  # (source, direction, set, sig_id or label, brd, cell, time, dose, q)
for tag in ("S1", "N1"):
    d = json.load(open(f"{G}/tool_responses/IT2_{tag}_l1000fwd_direct.json"))["topn"]
    for dirn in ("similar", "opposite"):
        for x in d[dirn]:
            if x["qvals"] >= 0.05: continue
            batch, cell, time_ = x["sig_id"].split(":")[0].split("_"); brd = re.search(r"(BRD-[A-Z]\d{8})", x["sig_id"]).group(1)
            hits.append(("L1000FWD_direct", dirn, tag, x["sig_id"], brd, cell, time_, x["sig_id"].split(":")[-1], x["qvals"]))
meta = {}
for fn in ("signature_metadata_for_returned_uuids.json", "signature_metadata_mimickers.json"):
    meta.update({e["id"].replace("-", ""): e for e in json.load(open(f"{G}/tool_responses/{fn}"))})
resp = json.load(open(f"{G}/tool_responses/S1_sigcom_ranktwosided_response.json"))["results"]
for kind in ("reversers", "mimickers"):
    rs = sorted([x for x in resp if x["type"] == kind], key=lambda x: x["z-sum"], reverse=(kind == "mimickers"))
    for i, x in enumerate(rs):
        m = meta[x["uuid"]]["meta"]; cm = m["cmap_id"]; mb = re.search(r"(BRD-[A-Z]\d{8})", cm)
        hits.append(("SigCom_S1_top100", kind, "S1", f"rank{i + 1}", mb.group(1) if mb else "", m["cell_line"], m["pert_time"], m["pert_dose"], x["z-sum"] and round(x["z-sum"], 2)) + (m["pert_name"], m.get("pubchem_id", "")))
codes = sorted({h[4] for h in hits if h[4]})
out = {}
for c in codes:
    r92, r70 = p92.get(c), p70.get(c); recs = [("GSE92742", r92)] if r92 else []
    if r70: recs.append(("GSE70138", r70))
    names = {r["pert_iname"] for _, r in recs}
    o = {"brd": c, "resolved": bool(recs), "inames": sorted(names), "ambiguous_names": len(names) > 1,
         "inchi_key": next((r["inchi_key"] for _, r in recs if r["inchi_key"] not in ("-666", "")), ""), "pubchem_cid": (r92 or {}).get("pubchem_cid", ""),
         "sources": [s for s, _ in recs], "pert_type": next((r["pert_type"] for _, r in recs), "")}
    out[c] = o
if net:
    B = "https://www.ebi.ac.uk/chembl/api/data"
    j = lambda u: json.load(urllib.request.urlopen(u, timeout=60))
    out["_chembl_release"] = j(f"{B}/status.json").get("chembl_db_version")
    for c, o in list(out.items()):
        if c.startswith("_") or not o["inchi_key"]: continue
        try:
            time.sleep(0.4)
            m = j(f"{B}/molecule.json?molecule_structures__standard_inchi_key={o['inchi_key']}")["molecules"]
            if not m: o["chembl"] = "NO_MATCH_BY_INCHIKEY"; continue
            cid = m[0]["molecule_chembl_id"]; o["chembl"] = {"id": cid, "pref_name": m[0].get("pref_name"), "max_phase": m[0].get("max_phase")}
            time.sleep(0.4)
            mech = j(f"{B}/mechanism.json?molecule_chembl_id={cid}&limit=20")["mechanisms"]
            o["chembl"]["mechanism_query_molecule_id_empty"] = not mech
            if not mech:  # measured 2026-10-27: for e.g. CHEMBL192 (sildenafil) molecule_chembl_id returns 0 rows but parent_molecule_chembl_id returns the PDE5A row
                time.sleep(0.4); mech = j(f"{B}/mechanism.json?parent_molecule_chembl_id={cid}&limit=20")["mechanisms"]
            o["chembl"]["mechanisms"] = sorted({f"{x.get('action_type')}|{x.get('mechanism_of_action')}" for x in mech})
        except Exception as e:
            o["chembl"] = f"QUERY_ERROR {type(e).__name__}"
json.dump({"verified_geo_checksums": verified, "codes": out, "n_codes": len(codes), "hits": hits}, open(f"{G}/derived/lincs_it2_compound_identity.json", "w"), indent=1)
print(len(codes), "codes;", sum(1 for c in codes if out[c]["resolved"]), "resolved;", {k: v for k, v in out.items() if k.startswith("_")})
