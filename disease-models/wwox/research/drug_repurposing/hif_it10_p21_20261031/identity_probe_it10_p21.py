#!/usr/bin/env python3
"""IT10 P2.1 task 2: identity, mechanism and potency rows for the HIF-axis alternatives. Key-less endpoints only (ChEMBL REST, PubChem PUG REST),
no e-mail/contact string, nothing personal sent. Catalogue lookups use LEGEND_CATALOG_CACHE (offline).
Usage: python3 -I identity_probe_it10_p21.py <raw_dir>   (raw_dir: empty directory outside the repo; raw JSON is kept there, sha256 listed in the service log)"""
import csv, gzip, hashlib, json, os, subprocess, sys, time, urllib.parse, urllib.request
from pathlib import Path
RAW = Path(sys.argv[1]); RAW.mkdir(parents=True, exist_ok=True); HERE = Path(__file__).resolve().parent
CAT = HERE.parent / "catalog" / "catalog_build.py"
# name -> (query names tried, branch)
COMP = {
 "PX-478": (["PX-478", "S-2-amino-3-[4'-N,N,-bis(2-chloroethyl)amino]phenyl propionic acid N-oxide"], "lower_HIF1a"),
 "echinomycin": (["echinomycin", "quinomycin A"], "lower_HIF1a"),
 "acriflavine": (["acriflavine", "acriflavinium", "proflavine"], "lower_HIF1a"),
 "KC7F2": (["KC7F2"], "lower_HIF1a"),
 "topotecan": (["topotecan"], "lower_HIF1a"),
 "digoxin": (["digoxin"], "lower_HIF1a"),
 "BAY 87-2243": (["BAY 87-2243", "BAY-87-2243"], "lower_HIF1a"),
 "belzutifan": (["belzutifan", "PT2977", "MK-6482"], "lower_HIF2a"),
 "PT2385": (["PT2385"], "lower_HIF2a"),
 "daprodustat": (["daprodustat"], "raise_PHD"),
 "vadadustat": (["vadadustat"], "raise_PHD"),
 "molidustat": (["molidustat"], "raise_PHD"),
 "enarodustat": (["enarodustat"], "raise_PHD"),
 "desidustat": (["desidustat"], "raise_PHD"),
 "roxadustat": (["roxadustat"], "raise_PHD"),
 "IOX2": (["IOX2"], "raise_PHD"),
 "DMOG": (["dimethyloxalylglycine", "DMOG"], "raise_PHD"),
}
log = []
def get(url, tag):
    for i in range(3):
        try:
            b = urllib.request.urlopen(urllib.request.Request(url, headers={"Accept": "application/json"}), timeout=60).read()
            fn = RAW / (hashlib.sha1(url.encode()).hexdigest()[:16] + ".json"); fn.write_bytes(b)
            log.append([time.strftime("%Y-%m-%d"), tag, url, 200, len(b), hashlib.sha256(b).hexdigest()]); return json.loads(b)
        except Exception as e:
            code = getattr(e, "code", "ERR"); last = (code, str(e)[:80]); time.sleep(1.5)
    log.append([time.strftime("%Y-%m-%d"), tag, url, last[0], 0, last[1]]); return None
env = dict(os.environ)
rows = []; mech = []; act = []
for name, (qs, branch) in COMP.items():
    # catalogue lookup is done separately by catalogue_lookup_it10_p21.py (the first in-line attempt failed to parse the CLI output and was removed)
    # ChEMBL search
    ch = None
    for q in qs:
        d = get("https://www.ebi.ac.uk/chembl/api/data/molecule/search.json?" + urllib.parse.urlencode({"q": q, "limit": 5}), f"chembl_search:{name}")
        if d and d.get("molecules"):
            ch = d["molecules"][0]; break
    if not ch:
        rows.append([name, branch, "", "", "", "", "", "", "", "", "", "NOT_FOUND_IN_CHEMBL_SEARCH"]); continue
    cid = ch["molecule_chembl_id"]; hier = ch.get("molecule_hierarchy") or {}
    props = ch.get("molecule_properties") or {}; st = ch.get("molecule_structures") or {}
    ik = st.get("standard_inchi_key", "")
    # PubChem by InChIKey
    pc = get(f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/{ik}/property/IUPACName,MolecularFormula,MolecularWeight/JSON", f"pubchem:{name}") if ik else None
    pcid = pc["PropertyTable"]["Properties"][0]["CID"] if pc else ""
    rows.append([name, branch, cid, ch.get("pref_name"), ch.get("max_phase"), ch.get("molecule_type"), ch.get("prodrug"), (hier or {}).get("parent_chembl_id"),
                 ik, pcid, f"{props.get('full_mwt','')};{props.get('alogp','')};{props.get('psa','')};{props.get('hba','')}/{props.get('hbd','')}", ""])
    m = get(f"https://www.ebi.ac.uk/chembl/api/data/mechanism.json?molecule_chembl_id={cid}&limit=20", f"mech:{name}")
    for x in (m or {}).get("mechanisms", []):
        mech.append([name, cid, x.get("mechanism_of_action"), x.get("action_type"), x.get("target_chembl_id"), x.get("direct_interaction"), x.get("max_phase")])
    # activities summary (potency types), aggregated
    agg = {}
    off = 0
    while True:
        a = get(f"https://www.ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id={cid}&standard_type__in=IC50,EC50,Ki,Kd,Potency&limit=1000&offset={off}", f"act:{name}")
        if not a: break
        for r in a.get("activities", []):
            if r.get("standard_value") is None or r.get("standard_units") != "nM" or r.get("standard_relation") not in ("=", None): continue
            k = (r.get("target_chembl_id"), r.get("target_pref_name"), r.get("standard_type"), r.get("assay_type"))
            agg.setdefault(k, []).append(float(r["standard_value"]))
        if a["page_meta"]["next"]: off += 1000
        else: break
    for (t, tn, ty, at), v in sorted(agg.items(), key=lambda kv: -len(kv[1])):
        v.sort(); act.append([name, cid, t, tn, ty, at, len(v), v[0], v[len(v)//2], v[-1]])
def w(fn, hdr, data):
    with (HERE / fn).open("w", newline="") as h: c = csv.writer(h, delimiter="\t"); c.writerow(hdr); c.writerows(data)
w("identity_it10_p21.tsv", ["compound", "branch", "chembl_id", "chembl_pref_name", "chembl_max_phase", "molecule_type", "prodrug_flag", "parent_chembl_id", "inchikey", "pubchem_cid", "mwt;alogp;psa;hba/hbd", "note"], rows)
w("chembl_mechanism_it10_p21.tsv", ["compound", "chembl_id", "mechanism_of_action", "action_type", "target_chembl_id", "direct_interaction", "max_phase"], mech)
w("chembl_potency_rows_it10_p21.tsv", ["compound", "chembl_id", "target_chembl_id", "target_name", "standard_type", "assay_type", "n_rows(relation '=', nM)", "min_nM", "median_nM", "max_nM"], act)
w("service_log_identity_it10_p21.tsv", ["date", "tag", "url", "http", "bytes", "sha256_or_error"], log)
print(len(rows), "compounds;", len(mech), "mechanism rows;", len(act), "potency groups;", len(log), "requests")
