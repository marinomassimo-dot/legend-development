#!/usr/bin/env python3
"""Fallback target discovery by gene-symbol search (different request form than the failed accession query) via framework/adapters/chembl.py. Same retry policy (2 retries, 6 s). --help is safe."""
import json, os, sys, time, argparse
argparse.ArgumentParser(description=__doc__).parse_args()
sys.argv=[sys.argv[0]]
import pull_it15_qa as P
for g in ("GRIN2A","GRIN2B","GRIN1","GRIN2C","GRIN2D"):
    o = P.chembl.query({"gene": g}, fetch=P.fetch); P.save(f"genesearch_{g}.json", o)
    print(g, o["status"], len(o["hits"]), o.get("error","")[:60], flush=True)
    for h in o["hits"]: print("  ", h["target_chembl_id"], h["target_type"], h["organism"], h["pref_name"], flush=True)
json.dump(P.FAILS, open(os.path.join(P.HERE,"raw",f"failures_genesearch_{int(time.time())}.json"),"w"))
