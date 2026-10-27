#!/usr/bin/env python3
"""Iteration 2 (scientist-d): direct L1000FWD public API (key-less) for declared sets, to separate wrapper limits from service limits.
POST https://maayanlab.cloud/l1000fwd/sig_search {up_genes, down_genes} -> result_id; GET .../result/topn/<id> -> {similar, opposite}.
(The old path /L1000FWD/ answers 307 to this one; the body keys are up_genes/down_genes, and wrong keys give HTTP 500 KeyError.)
One request pair per set, no retry. Usage: lincs_it2_l1000fwd_direct.py <this directory> SET [SET ...]   SET in S1, N1, K1, ..."""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]) or len(_sys.argv) < 3:
    print(__doc__)
    raise SystemExit(0)
import datetime, hashlib, json, time, urllib.request
G = _sys.argv[1]
sets = json.load(open(f"{G}/derived/query_sets.json")); sets.update(json.load(open(f"{G}/derived/query_sets_it2_nulls.json")))
for n, tag in enumerate(_sys.argv[2:]):
    if n: time.sleep(15)
    s = sets[tag]; t = datetime.datetime.now(datetime.timezone.utc).isoformat()
    r = urllib.request.urlopen(urllib.request.Request("https://maayanlab.cloud/l1000fwd/sig_search", json.dumps({"up_genes": s["up"], "down_genes": s["down"]}).encode(), {"Content-Type": "application/json"}), timeout=300)
    rid = json.loads(r.read())["result_id"]
    raw = urllib.request.urlopen(f"https://maayanlab.cloud/l1000fwd/result/topn/{rid}", timeout=120).read()
    d = json.loads(raw)
    json.dump({"utc": t, "set": tag, "result_id": rid, "n_similar": len(d["similar"]), "n_opposite": len(d["opposite"]), "verbatim_sha256": hashlib.sha256(raw).hexdigest(), "topn": d},
              open(f"{G}/tool_responses/IT2_{tag}_l1000fwd_direct.json", "w"))
    print(tag, rid, len(d["similar"]), len(d["opposite"]), flush=True)
