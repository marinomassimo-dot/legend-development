#!/usr/bin/env python3
"""IT10 P2.4 trial 2: reversal with a GEO-derived drug-perturbation library (Enrichr Drug_Perturbations_from_GEO_up/down), see PRE_DECLARATION.md.
Sends gene symbols only. Usage: trial2_enrichr_geo.py --derived gse156243/derived --out DIR"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, json, os, time, math, urllib.request, urllib.parse, uuid
ap = argparse.ArgumentParser(); ap.add_argument("--derived", required=True); ap.add_argument("--out", required=True); a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
H = "https://maayanlab.cloud/Enrichr/"
def add(genes, desc):
    b = uuid.uuid4().hex; body = (f'--{b}\r\nContent-Disposition: form-data; name="list"\r\n\r\n' + "\n".join(genes) + f'\r\n--{b}\r\nContent-Disposition: form-data; name="description"\r\n\r\n{desc}\r\n--{b}--\r\n').encode()
    r = urllib.request.Request(H + "addList", data=body, headers={"Content-Type": "multipart/form-data; boundary=" + b})
    return json.load(urllib.request.urlopen(r, timeout=60))["userListId"]
def enrich(uid, lib):
    u = H + "enrich?" + urllib.parse.urlencode({"userListId": uid, "backgroundType": lib})
    for k in range(4):
        try: return json.load(urllib.request.urlopen(u, timeout=90))[lib]
        except Exception: time.sleep(3)
    raise RuntimeError("enrich failed " + lib)
sets = {}
d = json.load(open(os.path.join(a.derived, "query_sets.json")))
for k in ("S1", "S3", "S0"): sets[k] = d[k]
for f, k in (("query_sets_S1P.json", "S1P"), ("query_sets_S1P2.json", "S1P2")): sets[k] = json.load(open(os.path.join(a.derived, f)))[k]
out = {}; rows = []
for k, s in sets.items():
    up, dn = s["up"], s["down"]
    # reverser: up-set in the _down library, down-set in the _up library
    r_up = enrich(add(up, k + "_up"), "Drug_Perturbations_from_GEO_down"); time.sleep(1)
    r_dn = enrich(add(dn, k + "_down"), "Drug_Perturbations_from_GEO_up"); time.sleep(1)
    # mimic: up-set in _up, down-set in _down
    m_up = enrich(add(up, k + "_up"), "Drug_Perturbations_from_GEO_up"); m_dn = enrich(add(dn, k + "_down"), "Drug_Perturbations_from_GEO_down")
    # Enrichr row: rank, term, p, z, combined, overlapping genes, adj p, ...
    A = {r[1]: r[6] for r in r_up}; B = {r[1]: r[6] for r in r_dn}
    both = sorted(((-math.log10(max(A[t], 1e-300)) - math.log10(max(B[t], 1e-300)), t, A[t], B[t]) for t in A if t in B and A[t] < 0.05 and B[t] < 0.05), reverse=True)
    A2 = {r[1]: r[6] for r in m_up}; B2 = {r[1]: r[6] for r in m_dn}
    mboth = [t for t in A2 if t in B2 and A2[t] < 0.05 and B2[t] < 0.05]
    out[k] = {"n_up": len(up), "n_down": len(dn), "reverser_terms_both_arms_adjp_lt_0.05": len(both), "mimic_terms_both_arms_adjp_lt_0.05": len(mboth),
              "n_terms_up_arm_adjp_lt_0.05": sum(v < 0.05 for v in A.values()), "n_terms_down_arm_adjp_lt_0.05": sum(v < 0.05 for v in B.values())}
    for sc, t, p1, p2 in both[:40]: rows.append((k, round(sc, 2), t, p1, p2))
json.dump(out, open(os.path.join(a.out, "trial2_counts.json"), "w"), indent=1)
with open(os.path.join(a.out, "trial2_reverser_terms_top40_per_set.tsv"), "w") as fh:
    fh.write("set\tscore\tterm\tadjp_upset_in_down_lib\tadjp_downset_in_up_lib\n")
    for r in rows: fh.write("\t".join(map(str, r)) + "\n")
print(json.dumps(out, indent=1))
