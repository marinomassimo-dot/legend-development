#!/usr/bin/env python3
"""Iteration 2 (scientist-d): read the stored IT2 SigCom responses (and the S1/S0 ones of iteration 1), annotate returned signature ids from the
key-less SigCom metadata API (only ids not already held), and write derived/lincs_it2_controls.json with the quantities declared in
lincs_iteration2_interpretation_20261027.md. Usage: lincs_it2_summarise.py <this directory>   (run from there; --help answers without network)"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
import collections, glob, hashlib, json, os, urllib.parse, urllib.request
import transform_uuids as tu
G = "."
meta = {}
for fn in ("tool_responses/signature_metadata_for_returned_uuids.json", "tool_responses/signature_metadata_mimickers.json", "tool_responses/IT2_signature_metadata.json"):
    if os.path.exists(fn): meta.update({e["id"].replace("-", ""): e for e in json.load(open(fn))})
resp = {"S1": "tool_responses/S1_sigcom_ranktwosided_response.json", "S0": "tool_responses/S0_sigcom_ranktwosided_response.json"}
for p in sorted(glob.glob("tool_responses/IT2_*_sigcom_ranktwosided_response.json")): resp[p.split("IT2_")[1].split("_sigcom")[0]] = p
data = {k: json.load(open(p)) for k, p in resp.items()}
need = sorted({x["uuid"] for d in data.values() for x in d["results"]} - set(meta))
if need:
    B = "https://maayanlab.cloud/sigcom-lincs/metadata-api/signatures?filter="; raw = []
    for i in range(0, len(need), 100):
        ids = [tu.restore(u.encode()).decode() for u in need[i:i + 100]]
        raw += json.load(urllib.request.urlopen(B + urllib.parse.quote(json.dumps({"where": {"id": {"inq": ids}}, "limit": 200})), timeout=120))
    verbatim = json.dumps(raw).encode(); st = tu.strip(verbatim)
    old = json.load(open("tool_responses/IT2_signature_metadata.json")) if os.path.exists("tool_responses/IT2_signature_metadata.json") else []
    allm = old + json.loads(st); open("tool_responses/IT2_signature_metadata.json", "w").write(json.dumps(allm))
    meta.update({e["id"].replace("-", ""): e for e in allm})
def rows(d, kind):
    r = sorted([x for x in d["results"] if x["type"] == kind], key=lambda x: x["z-sum"], reverse=(kind == "mimickers"))
    out = []
    for x in r:
        e = meta.get(x["uuid"])
        if not e: out.append({"z": x["z-sum"], "pert": "NO_METADATA", "cell": "", "dose": "", "time": "", "tissue": "", "uuid": x["uuid"]}); continue
        m = e["meta"]
        out.append({"z": x["z-sum"], "pert": m.get("pert_name", ""), "cell": m.get("cell_line", ""), "dose": m.get("pert_dose", ""), "time": m.get("pert_time", ""),
                    "tissue": m.get("tissue", "NOT_PROVIDED"), "ptype": m.get("pert_type", ""), "uuid": x["uuid"]})
    return out
prot = lambda r: r["cell"].startswith("MCLF") and r["dose"] == "4 uM" and r["time"] == "6 h"
mclf = lambda r: r["cell"].startswith("MCLF")
res = {}
R1 = [r["pert"] for r in rows(data["S1"], "reversers")[:25]]
for k, d in data.items():
    if not d["results"]: res[k] = {"EMPTY": True, "reversers": d.get("reversers"), "mimickers": d.get("mimickers")}; continue
    R, M = rows(d, "reversers"), rows(d, "mimickers")
    sh = lambda rs, f: round(100 * sum(map(f, rs)) / max(1, len(rs)), 1)
    res[k] = {"n_rev": len(R), "n_mim": len(M), "reversers_total": d["reversers"], "mimickers_total": d["mimickers"],
              "MCLF_share_rev": sh(R, mclf), "MCLF_share_mim": sh(M, mclf), "MCLF_4uM_6h_share_rev": sh(R, prot), "MCLF_4uM_6h_share_mim": sh(M, prot),
              "MCLF_4uM_6h_share_both_tails": sh(R + M, prot), "strongest_rev_z": min(r["z"] for r in R), "strongest_mim_z": max(r["z"] for r in M),
              "top25_rev_compound_overlap_with_S1": len(set(r["pert"] for r in R[:25]) & set(R1)),
              "distinct_cell_lines_rev": len({r["cell"] for r in R}), "top_cell_lines_rev": collections.Counter(r["cell"] for r in R).most_common(5),
              "no_metadata": sum(r["pert"] == "NO_METADATA" for r in R + M)}
json.dump(res, open("derived/lincs_it2_controls.json", "w"), indent=1)
for k, v in res.items(): print(k, v)
