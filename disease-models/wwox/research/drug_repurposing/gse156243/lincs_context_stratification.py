#!/usr/bin/env python3
"""Context stratification of the stored SigCom LINCS reversal responses of GSE156243 (scientist-c, 2026-10-26).
Pre-registered in prediction_lincs_context_stratification_20261026.md (committed before this ran). Re-reads tool_responses/S*_sigcom_ranktwosided_response.json;
the only network call is the key-less metadata API for signature ids not yet annotated (the mimickers), stored verbatim.
Run from this directory: python3 lincs_context_stratification.py   (writes derived/lincs_context_stratification.json and .tsv)"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):  # a documented command answers --help without network or writes
    print(__doc__)
    raise SystemExit(0)
import collections, json, os, urllib.parse, urllib.request

RUNS = ["S1", "S2", "S3", "S0"]
resp = {s: json.load(open(f"tool_responses/{s}_sigcom_ranktwosided_response.json")) for s in RUNS}
meta_file = "tool_responses/signature_metadata_for_returned_uuids.json"
meta = {e["id"].replace("-", ""): e for e in json.load(open(meta_file))}
need = sorted({x["uuid"] for s in RUNS for x in resp[s]["results"]} - set(meta))
extra_file = "tool_responses/signature_metadata_mimickers.json"
if need and not os.path.exists(extra_file):
    B = "https://maayanlab.cloud/sigcom-lincs/metadata-api/signatures?filter="
    raw = []
    for i in range(0, len(need), 100):
        f = {"where": {"id": {"inq": need[i:i + 100]}}, "limit": 200}
        raw += json.load(urllib.request.urlopen(B + urllib.parse.quote(json.dumps(f)), timeout=120))
    import hashlib, sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import transform_uuids as tu  # the publication gate flags UUID fragments: hyphens are removed, losslessly (README of this folder)
    verbatim = json.dumps(raw).encode()
    stripped = tu.strip(verbatim)
    lossless = "LOSSLESS" if tu.restore(stripped) == verbatim else "MISMATCH"
    open(extra_file, "wb").write(stripped)
    with open("uuid_transform_manifest.tsv", "a") as mf:
        mf.write(f"{extra_file}\t{hashlib.sha256(verbatim).hexdigest()}\t{len(verbatim)}\t{hashlib.sha256(stripped).hexdigest()}\t{len(stripped)}\t{lossless}\n")
if os.path.exists(extra_file):
    meta.update({e["id"].replace("-", ""): e for e in json.load(open(extra_file))})

def rows(s, kind):
    r = [x for x in resp[s]["results"] if x["type"] == kind]
    r.sort(key=lambda x: x["z-sum"], reverse=(kind == "mimickers"))
    out = []
    for x in r:
        m = meta[x["uuid"]]["meta"]
        out.append({"uuid": x["uuid"], "z": x["z-sum"], "pert": m["pert_name"], "cell": m["cell_line"], "dose": m["pert_dose"],
                    "time": m["pert_time"], "ptype": m.get("pert_type", ""), "tissue": m.get("tissue", "NOT_PROVIDED"),
                    "disease": m.get("disease", "NOT_PROVIDED"), "library": meta[x["uuid"]].get("library", ""),
                    "batch": m["cmap_id"].split("_")[0]})
    return out

R = {s: rows(s, "reversers") for s in RUNS}
M = {s: rows(s, "mimickers") for s in RUNS}
res = {}
top = lambda s, n: [r["pert"] for r in R[s][:n]]
res["P1_S0_vs_S1_top25_compound_overlap"] = len(set(top("S0", 25)) & set(top("S1", 25)))
res["P1_S0_vs_S1_top100_signature_overlap"] = len({r["uuid"] for r in R["S0"]} & {r["uuid"] for r in R["S1"]})
res["P1_S0_vs_S1_top100_compound_overlap"] = len(set(top("S0", 100)) & set(top("S1", 100)))
def share(rs, pred): return round(100 * sum(1 for r in rs if pred(r)) / len(rs), 1)
mclf = lambda r: r["cell"].startswith("MCLF")
prot = lambda r: r["cell"].startswith("MCLF") and r["dose"] == "4 uM" and r["time"] == "6 h"
res["P2_share_MCLF_top100"] = {s: share(R[s], mclf) for s in RUNS}
res["P2_share_MCLF_4uM_6h_top100"] = {s: share(R[s], prot) for s in RUNS}
res["P2_share_MCLF_4uM_6h_top100_mimickers"] = {s: share(M[s], prot) for s in RUNS}
res["P3_S1_compounds_in_both_reversers_and_mimickers_top100"] = {
    "n_reverser_compounds": len(set(top("S1", 100))),
    "n_also_mimicker": len(set(top("S1", 100)) & {r["pert"] for r in M["S1"]}),
    "which": sorted(set(top("S1", 100)) & {r["pert"] for r in M["S1"]})}
res["P4_S3_vs_S1_top25_compound_overlap"] = len(set(top("S3", 25)) & set(top("S1", 25)))
res["P4_S2_vs_S1_top25_compound_overlap"] = len(set(top("S2", 25)) & set(top("S1", 25)))
em = json.load(open("derived/sigcom_entity_map.json")); qs = json.load(open("derived/query_sets.json"))
unm = set(em["unmapped"]); res["P5_unmapped_share_per_set"] = {}
for s in RUNS:
    genes = qs[s]["up"] + qs[s]["down"]
    res["P5_unmapped_share_per_set"][s] = {"n": len(genes), "unmapped": sum(1 for g in genes if g in unm), "pct": round(100 * sum(1 for g in genes if g in unm) / len(genes), 2)}
res["ranking_size_per_set"] = {s: {"reversers_total": resp[s]["reversers"], "mimickers_total": resp[s]["mimickers"], "maxRank": resp[s]["maxRank"]} for s in RUNS}
# strata of the S1 and S0 top-100 reversers, kept separate
def strata(rs):
    return {"cell_lines": dict(collections.Counter(r["cell"] for r in rs).most_common(12)), "n_cell_lines": len({r["cell"] for r in rs}),
            "doses": dict(collections.Counter(r["dose"] for r in rs).most_common(6)), "times": dict(collections.Counter(r["time"] for r in rs)),
            "pert_types": dict(collections.Counter(r["ptype"] for r in rs)), "batches": dict(collections.Counter(r["batch"] for r in rs).most_common(8)),
            "libraries": dict(collections.Counter(r["library"] for r in rs)), "tissue_field": dict(collections.Counter(r["tissue"] for r in rs).most_common(6))}
res["strata_S1_reversers_top100"] = strata(R["S1"]); res["strata_S0_reversers_top100"] = strata(R["S0"])
# P6: non-MCLF reversers of S1, listed as returned (classification by the reader, in the report, not computed)
res["P6_S1_non_MCLF_reversers_top100"] = [[r["pert"], r["cell"], r["tissue"], r["dose"], r["time"], round(r["z"], 2)] for r in R["S1"] if not mclf(r)]
# stratum replication rule: top-100 reverser in >=3 distinct cell lines of >=2 tissues at the same dose and time
rep = collections.defaultdict(lambda: collections.defaultdict(set))
for r in R["S1"]:
    rep[(r["pert"], r["dose"], r["time"])]["cells"].add(r["cell"]); rep[(r["pert"], r["dose"], r["time"])]["tissues"].add(r["tissue"])
res["stratum_replicated_S1"] = [list(k) + [len(v["cells"]), sorted(v["tissues"])] for k, v in rep.items() if len(v["cells"]) >= 3 and len(v["tissues"]) >= 2]
res["compounds_in_>=3_cell_lines_S1_any_tissue"] = sorted(k for k, v in collections.Counter(
    (r["pert"]) for r in {(x["pert"], x["cell"]): x for x in R["S1"]}.values()).items() if v >= 3)
# POST HOC (not pre-registered; added after the pre-registered readout showed S0 and S1 differ in context): is the MCLF 4 uM / 6 h concentration direction-specific?
res["POSTHOC_MCLF_4uM_6h_count_reversers_vs_mimickers_top100"] = {s: [sum(1 for r in R[s] if prot(r)), sum(1 for r in M[s] if prot(r))] for s in RUNS}
multi = {}
for c in res["compounds_in_>=3_cell_lines_S1_any_tissue"]:
    multi[c] = {"reverser_cell_lines_S1": sorted({r["cell"] for r in R["S1"] if r["pert"] == c}),
                "mimicker_cell_lines_S1": sorted({r["cell"] for r in M["S1"] if r["pert"] == c}),
                "doses_times_reverser": sorted({(r["dose"] + " " + r["time"]) for r in R["S1"] if r["pert"] == c})}
res["POSTHOC_multi_line_compounds_S1"] = multi
res["POSTHOC_S1_reverser_signatures_with_no_tissue_field"] = sum(1 for r in R["S1"] if r["tissue"] == "NOT_PROVIDED")
json.dump(res, open("derived/lincs_context_stratification.json", "w"), indent=1, sort_keys=True)
with open("derived/lincs_context_stratification.tsv", "w") as f:
    f.write("set\tkind\trank\tpert\tcell\ttissue\tdose\ttime\tpert_type\tbatch\tz_sum\n")
    for s in RUNS:
        for kind, rs in (("reverser", R[s]), ("mimicker", M[s])):
            for i, r in enumerate(rs):
                f.write(f"{s}\t{kind}\t{i + 1}\t{r['pert']}\t{r['cell']}\t{r['tissue']}\t{r['dose']}\t{r['time']}\t{r['ptype']}\t{r['batch']}\t{r['z']:.3f}\n")
print(json.dumps({k: v for k, v in res.items() if not k.startswith("strata") and k != "P6_S1_non_MCLF_reversers_top100"}, indent=1))
