#!/usr/bin/env python3
"""The existing repurposing adapters, called through their own door for the Lucas-Clarke follow-up targets and compounds.
Each result is kept whole in adapters_raw.json (status, requests_sent, hits). NOT WWOX EVIDENCE. Run from repo root."""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):  # a documented command must answer --help without touching the network or any file
    print(__doc__)
    raise SystemExit(0)

import json, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))
from framework.adapters import pubtator3, openfda, orphadata, ilincs
HERE = Path(__file__).resolve().parent
CALLS = [("openfda", openfda, {"drug": d, "sections": ["indications_and_usage", "pediatric_use", "contraindications"], "faers_limit": 5}) for d in
         ["stiripentol", "trazodone", "guanabenz", "sodium dichloroacetate", "valproic acid"]]
CALLS += [("pubtator3", pubtator3, {"gene": g}) for g in ["LDHA", "PDK2", "EIF2B5", "EIF2AK3"]]
CALLS += [("orphadata", orphadata, {"name": n}) for n in ["WWOX", "vanishing white matter", "Dravet"]]
CALLS += [("ilincs", ilincs, {"where": {"libraryid": "LIB_5", "compound": c}, "limit": 10}) for c in ["stiripentol", "ISRIB", "dichloroacetate", "GSK2606414", "trazodone"]]
out = []
for name, mod, req in CALLS:
    time.sleep(0.6)
    r = mod.query(req)
    out.append({"adapter": name, "request": req, "status": r["status"], "error": r.get("error", ""), "requests_sent": r["requests_sent"],
                "source_version": r.get("source_version"), "retrieved_at": r["retrieved_at"], "n_hits": len(r["hits"]),
                "hits": r["hits"][:12]})
    print(name, json.dumps(req)[:90], r["status"], len(r["hits"]))
(HERE / "adapters_raw.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
