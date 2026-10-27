#!/usr/bin/env python3
"""Iteration 2 (scientist-d): which S1 top-100 compounds are frequent hitters, i.e. also appear in the top-100 reversers or mimickers of the NULL
rankings (S0, S1P, S1P2, N1-N3, K1-K2; 7 rankings with a non-empty answer + S0 = 8)? Reads stored responses and held metadata only; no network.
Usage: lincs_it2_frequent_hitters.py   (run from this directory) -> derived/lincs_it2_frequent_hitters.json"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
import glob, json, os
meta = {}
for fn in ("signature_metadata_for_returned_uuids.json", "signature_metadata_mimickers.json", "IT2_signature_metadata.json"):
    meta.update({e["id"].replace("-", ""): e for e in json.load(open(f"tool_responses/{fn}"))})
def names(path):
    d = json.load(open(path)); out = {"reversers": set(), "mimickers": set()}
    for x in d["results"]:
        out[x["type"]].add(meta[x["uuid"]]["meta"]["pert_name"])
    return out
nulls = {"S0": "tool_responses/S0_sigcom_ranktwosided_response.json"}
for t in ("S1P", "S1P2", "N1", "N2", "N3", "K1", "K2"): nulls[t] = f"tool_responses/IT2_{t}_sigcom_ranktwosided_response.json"
N = {k: names(p) for k, p in nulls.items()}
s1 = names("tool_responses/S1_sigcom_ranktwosided_response.json")
res = {}
for tail in ("reversers", "mimickers"):
    for c in sorted(s1[tail]):
        hit = sorted(k for k in N if c in N[k]["reversers"] | N[k]["mimickers"])
        res.setdefault(tail, {})[c] = hit
json.dump({"n_null_rankings": len(N), "S1_compound_to_null_rankings_containing_it_in_either_tail": res}, open("derived/lincs_it2_frequent_hitters.json", "w"), indent=1)
for tail in res:
    fh = {c: h for c, h in res[tail].items() if len(h) >= 2}
    print(tail, "S1 distinct compounds", len(res[tail]), "in >=1 null", sum(1 for h in res[tail].values() if h), ">=2 nulls", len(fh), sorted(fh))
