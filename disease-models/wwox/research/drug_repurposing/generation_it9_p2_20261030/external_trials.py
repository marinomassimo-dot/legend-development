#!/usr/bin/env python3
"""Contained trials of external resources for the seed engine (IT9 P2). Sends HTTP requests carrying only gene symbols / Ensembl ids from the seed tables (no e-mail, no identity, no key).

  external_trials.py --seeds-dir DIR [--extra FILE] --actions DIR --out FILE.tsv
Trial 1 (Open Targets Platform GraphQL, public, no key): for every seed gene, the drugs/clinical candidates the platform lists against it, compared with the catalogue's
direct (any-action) hits on the same gene. Trial 2: availability headers of the SigCom LINCS metadata API and the HuggingFace MATRIX scores dataset (licence field, revision).
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, csv, glob, gzip, json, os, urllib.request, collections

ap = argparse.ArgumentParser(); ap.add_argument("--seeds-dir", required=True); ap.add_argument("--extra", action="append", default=[]); ap.add_argument("--actions", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args()
genes = collections.OrderedDict()
for f in sorted(glob.glob(os.path.join(a.seeds_dir, "*.tsv"))) + a.extra:
    if f.endswith("manifest.tsv"): continue
    for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
        for g in ([x for x in r["members"].split(";") if x] if r["kind"] == "process" else [r["gene"]]):
            genes.setdefault(g.upper(), set()).add(os.path.basename(f)[:-4])
def gql(q):
    req = urllib.request.Request("https://api.platform.opentargets.org/api/v4/graphql", data=json.dumps({"query": q}).encode(), headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=40))
anyt = collections.defaultdict(set)
for r in csv.DictReader(gzip.open(os.path.join(a.actions, "family_targets_any.tsv.gz"), "rt"), delimiter="\t"):
    anyt[r["target_symbol"].upper()].add(r["family_id"])
rows = []
for g, sets in genes.items():
    try:
        h = gql('{search(queryString:"%s", entityNames:["target"], page:{index:0,size:1}){hits{id name}}}' % g)["data"]["search"]["hits"]
        if not h or h[0]["name"].upper() != g:
            rows.append([g, "", "NO_EXACT_SYMBOL_HIT", "", "", len(anyt.get(g, ()))]); continue
        eid = h[0]["id"]
        t = gql('{target(ensemblId:"%s"){drugAndClinicalCandidates{count rows{maxClinicalStage drug{id name}}}}}' % eid)["data"]["target"]["drugAndClinicalCandidates"]
        ot = {x["drug"]["id"] for x in t["rows"] if x.get("drug")}
        cat = {f for f in anyt.get(g, ())}
        cat_chembl = {f.split("FAM:CAT:")[-1] for f in cat if f.startswith("FAM:CAT:CHEMBL")}
        rows.append([g, eid, "OK", len(ot), len(ot & cat_chembl), len(cat)])
    except Exception as e:
        rows.append([g, "", "ERROR " + type(e).__name__, "", "", len(anyt.get(g, ()))])
with open(a.out, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n")
    w.writerow(["seed_gene", "ensembl_id", "state", "open_targets_drug_candidates", "of_which_chembl_id_equals_a_catalogue_family_hitting_the_gene", "catalogue_families_with_any_action_on_gene"]); w.writerows(rows)
print(len(rows), "genes ->", a.out)
for nm, url in (("sigcom_lincs_metadata_api", "https://maayanlab.cloud/sigcom-lincs/metadata-api/"), ("hf_matrix_scores", "https://huggingface.co/api/datasets/everycure/matrix-scores")):
    try:
        r = urllib.request.urlopen(url, timeout=30); b = r.read(4000).decode("utf-8", "ignore")
        print(nm, r.status, (json.loads(b).get("sha") if nm.startswith("hf") and b.startswith("{") else b[:120].replace("\n", " ")))
    except Exception as e:
        print(nm, "ERROR", type(e).__name__, e)
