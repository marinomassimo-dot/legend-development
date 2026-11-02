#!/usr/bin/env python3
# IT20 P7 trial: reads ChEMBL public mechanism/target endpoints for four named compounds; stdlib only; prints, writes nothing.
import argparse
argparse.ArgumentParser(description='Read-only ChEMBL mechanism/target lookup for four named compounds (about 11 public GETs, 1.5 s apart).').parse_args()
import json,urllib.request,urllib.parse,time,sys
B="https://www.ebi.ac.uk/chembl/api/data/"
def g(p):
    time.sleep(1.5)
    return json.load(urllib.request.urlopen(B+p,timeout=40))
n=0
for name in ["TERODILINE","SULOCTIDIL","PHLOROGLUCINOL","BEPRIDIL"]:
    m=g("molecule.json?pref_name__iexact="+name)['molecules']
    if not m: print(name,"no molecule"); continue
    cid=m[0]['molecule_chembl_id']
    mech=g(f"mechanism.json?molecule_chembl_id={cid}")['mechanisms']
    print(name,cid,"n_mech",len(mech))
    for x in mech:
        t=g("target/"+x['target_chembl_id']+".json") if x['target_chembl_id'] else {}
        print("  ",x['action_type'],x['target_chembl_id'],t.get('target_type'),t.get('pref_name'),
              "| comps",len(t.get('target_components',[])),"| refs",[(r['ref_type'],r['ref_id']) for r in x.get('mechanism_refs',[])][:3],"| max_phase",x.get('max_phase'), "| rec", x.get('mec_id'), "| comment", (x.get('mechanism_comment') or '')[:60])
