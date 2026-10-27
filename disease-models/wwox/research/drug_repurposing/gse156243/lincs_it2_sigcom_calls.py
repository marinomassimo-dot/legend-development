#!/usr/bin/env python3
"""Iteration 2 (scientist-d): the bounded, declared SigCom LINCS enrich/ranktwosided requests of lincs_iteration2_interpretation_20261027.md.
One request per set, sequential, 15 s apart, NO retry. Entity ids are sent with their hyphens (the tracked maps and requests are hyphen-stripped
for the publication gate; transform_uuids.restore re-inserts them). Original bytes stored with hyphens stripped, as elsewhere in this folder.
Usage: lincs_it2_sigcom_calls.py <this directory> TAG [TAG ...]   TAG in: DIAG_S1_STRIPPED, S1P, S1P2, N1, N2, N3, K1, K2"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]) or len(_sys.argv) < 3:
    print(__doc__)
    raise SystemExit(0)
import datetime, hashlib, json, time, urllib.request
import transform_uuids as tu
G = _sys.argv[1]
meta1 = json.load(open(f"{G}/tool_responses/S1_sigcom_ranktwosided_meta.json")); db, limit = meta1["database"], meta1["limit"]
mp = json.load(open(f"{G}/derived/sigcom_entity_map.json"))["map"]
try: mp.update(json.load(open(f"{G}/derived/sigcom_entity_map_it2.json"))["map"])
except FileNotFoundError: pass
sets = json.load(open(f"{G}/derived/query_sets.json")); sets.update(json.load(open(f"{G}/derived/query_sets_it2_nulls.json")))
sets["S1P"] = json.load(open(f"{G}/derived/query_sets_S1P.json"))["S1P"]; sets["S1P2"] = json.load(open(f"{G}/derived/query_sets_S1P2.json"))["S1P2"]
sets["DIAG_S1_STRIPPED"] = sets["S1"]
rest = lambda s: tu.restore(s.encode()).decode()
for n, tag in enumerate(_sys.argv[2:]):
    if n: time.sleep(15)
    s = sets[tag]; hy = tag != "DIAG_S1_STRIPPED"
    f = (lambda x: rest(x)) if hy else (lambda x: x)
    body = {"up_entities": [f(mp[g]) for g in s["up"] if g in mp], "down_entities": [f(mp[g]) for g in s["down"] if g in mp], "limit": limit, "database": db}
    req = urllib.request.Request("https://data-api.sigcom-lincs.k8s.maayanlab.cloud/v1/api/v1/enrich/ranktwosided", json.dumps(body).encode(), {"Content-Type": "application/json"})
    t = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        r = urllib.request.urlopen(req, timeout=600); raw = r.read(); status = r.status; hdr = dict(r.headers)
    except Exception as e:
        raw = repr(e).encode(); status = -1; hdr = {}
    st = tu.strip(raw); t0 = f"{G}/tool_responses/IT2_{tag}_sigcom_ranktwosided"
    open(t0 + "_response.json", "wb").write(st)
    json.dump({"utc": t, "status": status, "hyphens_in_request_ids": hy, "headers": {k: hdr[k] for k in hdr if k in ("Content-Range", "X-Duration", "Date")},
               "request_body_counts": {"up": len(body["up_entities"]), "down": len(body["down_entities"])}, "database": db, "limit": limit,
               "verbatim_sha256": hashlib.sha256(raw).hexdigest(), "verbatim_bytes": len(raw)}, open(t0 + "_meta.json", "w"), indent=1)
    print(tag, status, len(raw), raw[:120], flush=True)
