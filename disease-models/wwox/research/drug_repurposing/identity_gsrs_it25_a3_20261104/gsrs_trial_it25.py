#!/usr/bin/env python3
"""IT25 A3: G-SRS (FDA/NCATS) name -> UNII -> structure trial on the 22 rows left unresolved by the IT24 identity census (route R4).
Only the public compound name is sent; GET only; one request per name; >= 1.2 s apart; no key, no login, no e-mail address.
Usage: gsrs_trial_it25.py --run --cache DIR --catalog-cache DIR --out DIR     (network; raw responses go to --cache, outside git)
       gsrs_trial_it25.py --offline --cache DIR --catalog-cache DIR --out DIR (re-evaluate cached responses, no network)"""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help")):
    print(__doc__); raise SystemExit(0)
import argparse, csv, gzip, hashlib, json, re, time, urllib.parse, urllib.request
from pathlib import Path

H = Path(__file__).resolve().parent
DR = H.parent
ROUTES = DR / "identity_it24_p2_20261104/q248/identity_routes.tsv"
CATALOG = DR / "catalog/catalog.jsonl.gz"
URL = "https://gsrs.ncats.nih.gov/api/v1/substances/search?q={q}&top=20&view=full"


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def cache_path(cache, name):
    return Path(cache) / (hashlib.sha256(name.encode()).hexdigest()[:16] + ".json")


def fetch(name, cache):
    p = cache_path(cache, name)
    if p.exists():
        return json.loads(p.read_text())
    url = URL.format(q=urllib.parse.quote('"%s"' % name))
    req = urllib.request.Request(url, headers={"User-Agent": "legend-research-readonly/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read().decode()
    p.write_text(body)
    time.sleep(1.5)
    return json.loads(body)


def evaluate(name, resp, row_synonyms, row_chembl, unii2chembl, chembl2key):
    """Return a dict with verdict firm | weak | ambiguous | no_hit."""
    q = norm(name)
    cands = {}
    for rec in resp.get("content", []):
        if rec.get("substanceClass") != "chemical" or not rec.get("approvalID"):
            continue
        names = [rec.get("_name") or ""] + [n.get("name", "") for n in rec.get("names", [])]
        hit = [n for n in names if norm(n) == q]
        if hit:
            via = "preferred_name" if norm(rec.get("_name") or "") == q else "synonym"
            cands[rec["approvalID"]] = (rec, hit[0], via, names)
    out = dict(compound=name, verdict="no_hit", unii="", gsrs_name="", via="", n_candidates=len(cands), corroboration="",
               chembl_ids="", catalogue_inchikey="", smiles="", note="")
    if not cands:
        out["note"] = "no chemical record carries the name (total records returned: %s)" % resp.get("total")
        return out
    if len(cands) > 1:
        out.update(verdict="ambiguous", unii=";".join(sorted(cands)), note="two or more substances share the name; no family merged")
        return out
    unii, (rec, hit, via, names) = next(iter(cands.items()))
    nset = {norm(n) for n in names}
    corr = [s for s in row_synonyms if not re.match(r"^(IUPHAR|CHEMBL|DB\d|CHEBI)", s, re.I) and norm(s) in nset and norm(s) != q]
    chembl = sorted(unii2chembl.get(unii, []))
    contradiction = bool(row_chembl and chembl and row_chembl not in chembl)
    if row_chembl and row_chembl in chembl:
        corr.append("row ChEMBL id %s = UniChem(UNII)" % row_chembl)
    keys = sorted({chembl2key[c] for c in chembl if chembl2key.get(c)})
    out.update(unii=unii, gsrs_name=hit, via=via, corroboration=";".join(corr), chembl_ids=";".join(chembl),
               catalogue_inchikey=";".join(keys), smiles=(rec.get("structure") or {}).get("smiles", ""))
    if contradiction:
        out.update(verdict="ambiguous", note="row ChEMBL id not in UniChem(UNII): contradiction")
    elif corr:
        out["verdict"] = "firm"
    else:
        out.update(verdict="weak", note="single exact-name record, no independent identifier agrees")
    if out["verdict"] != "no_hit" and len(chembl) > 1:
        out["note"] = (out["note"] + " UNII maps to several ChEMBL ids; no catalogue key taken").strip()
        out["catalogue_inchikey"] = ""
    return out


def load_catalog():
    by_id, chembl2key = {}, {}
    with gzip.open(CATALOG, "rt") as f:
        for line in f:
            e = json.loads(line)
            by_id[e["id"]] = e
            c = e["ids"].get("chembl")
            if c and e["ids"].get("inchikey"):
                chembl2key[c] = e["ids"]["inchikey"]
    return by_id, chembl2key


def load_unii2chembl(cc):
    m = {}
    with gzip.open(Path(cc) / "unichem/src1src14.txt.gz", "rt") as f:
        next(f)
        for line in f:
            a, b = line.rstrip("\n").split("\t")
            m.setdefault(b, set()).add(a)
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", action="store_true"); ap.add_argument("--offline", action="store_true")
    ap.add_argument("--cache", required=True); ap.add_argument("--catalog-cache", required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    Path(a.cache).mkdir(parents=True, exist_ok=True)
    rows = [r for r in csv.DictReader(open(ROUTES), delimiter="\t") if r["route"] == "none_unresolved"]
    by_id, chembl2key = load_catalog()
    u2c = load_unii2chembl(a.catalog_cache)
    res = []
    for r in rows:
        name = r["compound"]
        if a.offline:
            p = cache_path(a.cache, name)
            resp = json.loads(p.read_text()) if p.exists() else {"content": [], "total": "not cached"}
        else:
            resp = fetch(name, a.cache)
        e = by_id.get(r["family_id"].replace("FAM:", ""), {})
        ids = e.get("ids", {})
        o = evaluate(name, resp, e.get("synonyms", []), ids.get("chembl"), u2c, chembl2key)
        o = dict(proposal_id=r["proposal_id"], family_id=r["family_id"], **o)
        res.append(o)
    cols = ["proposal_id", "family_id", "compound", "verdict", "unii", "gsrs_name", "via", "n_candidates", "corroboration", "chembl_ids", "catalogue_inchikey", "smiles", "note"]
    Path(a.out).mkdir(parents=True, exist_ok=True)
    with open(Path(a.out) / "gsrs_results.tsv", "w") as f:
        w = csv.DictWriter(f, cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(res)
    from collections import Counter
    print(dict(Counter(o["verdict"] for o in res)))


if __name__ == "__main__":
    main()
