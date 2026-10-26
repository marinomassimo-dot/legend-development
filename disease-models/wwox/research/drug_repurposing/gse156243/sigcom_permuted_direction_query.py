#!/usr/bin/env python3
"""Addendum A of prediction_lincs_context_stratification_20261026.md: S1P = the S1 genes with the up/down labels shuffled (517/317, seed 20261026),
one request to SigCom LINCS enrich/ranktwosided (same database and limit as S1..S0), original response stored verbatim (UUID hyphens removed as elsewhere here).
Run from this directory: python3 sigcom_permuted_direction_query.py [seed [tag]]   (default seed 20261026, tag S1P; the second permutation used 20261027 S1P2)"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):  # answers --help without network or writes
    print(__doc__)
    raise SystemExit(0)
import datetime, hashlib, json, os, random, urllib.request
import transform_uuids as tu
meta1 = json.load(open("tool_responses/S1_sigcom_ranktwosided_meta.json"))
db, limit = meta1["database"], meta1["limit"]
s1 = json.load(open("derived/query_sets.json"))["S1"]
mp = json.load(open("derived/sigcom_entity_map.json"))["map"]
genes = sorted(s1["up"] + s1["down"])
SEED = int(_sys.argv[1]) if len(_sys.argv) > 1 else 20261026
TAG = _sys.argv[2] if len(_sys.argv) > 2 else "S1P"
random.seed(SEED)
shuffled = genes[:]
random.shuffle(shuffled)
up, down = shuffled[:len(s1["up"])], shuffled[len(s1["up"]):]
sets = {TAG: {"up": up, "down": down}}
json.dump(sets, open(f"derived/query_sets_{TAG}.json", "w"), indent=1)
body = {"up_entities": [mp[g] for g in up if g in mp], "down_entities": [mp[g] for g in down if g in mp], "limit": limit, "database": db}
req = urllib.request.Request("https://data-api.sigcom-lincs.k8s.maayanlab.cloud/v1/api/v1/enrich/ranktwosided", json.dumps(body).encode(), {"Content-Type": "application/json"})
t = datetime.datetime.now(datetime.timezone.utc).isoformat()
r = urllib.request.urlopen(req, timeout=600)
raw = r.read()
stripped = tu.strip(raw)
lossless = "LOSSLESS" if tu.restore(stripped) == raw else "MISMATCH"
tag = f"{TAG}_sigcom_ranktwosided"
open(f"tool_responses/{tag}_response.json", "wb").write(stripped)
json.dump({"utc": t, "status": r.status, "database": db, "limit": limit, "request_body_counts": {"up": len(body["up_entities"]), "down": len(body["down_entities"])},
           "verbatim_sha256": hashlib.sha256(raw).hexdigest(), "verbatim_bytes": len(raw)}, open(f"tool_responses/{tag}_meta.json", "w"), indent=1)
json.dump({k: v for k, v in body.items()}, open(f"tool_responses/{tag}_request.json", "w"))
with open("uuid_transform_manifest.tsv", "a") as mf:
    mf.write(f"tool_responses/{tag}_response.json\t{hashlib.sha256(raw).hexdigest()}\t{len(raw)}\t{hashlib.sha256(stripped).hexdigest()}\t{len(stripped)}\t{lossless}\n")
print(len(raw), lossless, body["database"], body["limit"], len(body["up_entities"]), len(body["down_entities"]))
