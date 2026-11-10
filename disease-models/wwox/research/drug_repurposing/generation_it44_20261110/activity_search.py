#!/usr/bin/env python3
"""IT44 P2: a by-target ACTIVITY path for what the mechanism tables do not hold.
The mechanism path (action_search.py) reads curated mechanism rows and registry interactions; a compound with only measured activities on the target (azetukalner on KCNQ2 is the control found by SCI43) is invisible to it.
This path reads ChEMBL's public activity endpoint for the target records that carry a relation's gene symbols, caches every raw page in a gitignored cache with its SHA-256 and the completeness of the read,
and writes one row per measured activity plus one row per molecule. Principles kept apart (a measured activity is NOT an action):
  identity of the molecule (ChEMBL id, parent, name as served) | target record and organism | quantity as reported (type, relation, value, unit, assay type, assay text) | direction: never taken from the activity type | transfer to WWOX: always open.
Every molecule verdict is ACTIVITY_ONLY with named unknown fields; it can enter a comparison as a candidate for a primary-source read, never as a favourable compound. A truncated read is coverage TRUNCATED, never absence.
No third-party raw data is committed: the derived tables carry only values and ids; the raw pages stay in LEGEND_ACTIVITY_CACHE (default catalog/cache/chembl_activity).
  python3 activity_search.py --relations relations.tsv --out outdir [--types IC50,EC50,Ki,Kd,Potency] [--max-pages 5] [--refetch]"""
import argparse, csv, gzip, hashlib, json, os, re, sys, time, urllib.parse, urllib.request
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
API = "https://www.ebi.ac.uk/chembl/api/data/activity.json"
TYPES = ("IC50", "EC50", "Ki", "Kd", "Potency")
UNKNOWN_FIELDS = "direction;site;target_composition_in_assay;transfer_to_WWOX_context"

def cache_dir():
    d = Path(os.environ.get("LEGEND_ACTIVITY_CACHE", DR / "catalog/cache/chembl_activity")); d.mkdir(parents=True, exist_ok=True); return d

def target_index(cache_root):
    """gene symbol -> [(target_chembl_id, target_type, organism, n_components)] from the cached ChEMBL target file (human only)."""
    idx = defaultdict(list)
    with gzip.open(Path(cache_root) / "chembl/targets.jsonl.gz", "rt") as f:
        for line in f:
            t = json.loads(line)
            if t.get("organism") != "Homo sapiens": continue
            comps = t.get("target_components") or []
            for c in comps:
                for s in c.get("target_component_synonyms") or []:
                    if s.get("syn_type") == "GENE_SYMBOL": idx[s["component_synonym"].upper()].append((t["target_chembl_id"], t.get("target_type", ""), t.get("organism", ""), len(comps)))
    return {k: sorted(set(v)) for k, v in idx.items()}

def fetch(target, types, max_pages, refetch):
    """Raw pages for one target, cached; returns (rows, coverage, cache_files). coverage COMPLETE only when the last page had no next."""
    cd = cache_dir() / target; cd.mkdir(exist_ok=True); rows, files, cov = [], [], "COMPLETE"
    url = API + "?" + urllib.parse.urlencode({"target_chembl_id": target, "standard_type__in": ",".join(types), "limit": 1000, "offset": 0})
    for page in range(max_pages):
        fp = cd / f"p{page}.json"
        if fp.exists() and not refetch: raw = fp.read_bytes()
        else:
            req = urllib.request.Request(url, headers={"Accept": "application/json"})
            try:
                with urllib.request.urlopen(req, timeout=60) as r: raw = r.read()
            except Exception as e:
                return rows, f"READ_ERROR:{type(e).__name__}", files
            fp.write_bytes(raw); time.sleep(0.3)
        files.append((str(fp.relative_to(cache_dir())), hashlib.sha256(raw).hexdigest()))
        j = json.loads(raw); rows += j["activities"]; nxt = (j.get("page_meta") or {}).get("next")
        if not nxt: return rows, "COMPLETE", files
        url = "https://www.ebi.ac.uk" + nxt
    return rows, "TRUNCATED", files

def catalogue_by_chembl():
    """ChEMBL id -> (catalogue name, status class, origin) from the tracked catalogue; the join is by id, never by name."""
    out = {}
    with gzip.open(DR / "catalog/catalog.jsonl.gz", "rt") as f:
        for line in f:
            r = json.loads(line)
            for sr in r.get("source_records", []):
                if sr.get("source") == "chembl": out[sr["id"]] = (r.get("name") or "", r.get("status_class") or "", r.get("origin") or "")
    return out

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--relations", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--types", default=",".join(TYPES)); ap.add_argument("--max-pages", type=int, default=5); ap.add_argument("--refetch", action="store_true")
    a = ap.parse_args(); out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    croot = Path(os.environ.get("LEGEND_CATALOG_CACHE", DR / "catalog/cache")); idx = target_index(croot); types = tuple(a.types.split(","))
    rels = list(csv.DictReader(open(a.relations, encoding="utf-8"), delimiter="\t")); act_rows, manifest = [], {}
    for r in rels:
        for sym in sorted({s.split(":")[0].strip().upper() for s in r["target_symbols"].replace(":down", "").replace(":up", "").split(";") if s.strip()}):
            for tid, ttype, org, ncomp in idx.get(sym, []):
                if ttype not in ("SINGLE PROTEIN", "PROTEIN COMPLEX", "PROTEIN FAMILY"): continue
                rows, cov, files = fetch(tid, types, a.max_pages, a.refetch); manifest[tid] = {"coverage": cov, "files": files, "rows": len(rows)}
                gran = "single_protein" if ncomp == 1 and ttype == "SINGLE PROTEIN" else "complex_or_family_record"
                for x in rows:
                    act_rows.append(dict(relation_id=r["relation_id"], target_symbol=sym, target_chembl_id=tid, target_granularity=gran, molecule_chembl_id=x.get("molecule_chembl_id") or "",
                        parent_chembl_id=x.get("parent_molecule_chembl_id") or x.get("molecule_chembl_id") or "", name=x.get("molecule_pref_name") or "", type=x.get("standard_type") or "", relation=x.get("standard_relation") or "",
                        value=x.get("standard_value") or "", units=x.get("standard_units") or "", assay_type=x.get("assay_type") or "", assay_organism=x.get("assay_organism") or "", validity=x.get("data_validity_comment") or "",
                        assay_description=(x.get("assay_description") or "")[:160].replace("\t", " ").replace("\n", " "), document=x.get("document_chembl_id") or "", pubmed=x.get("pubmed_id") or "", coverage=cov))
    if not act_rows: print("no activity rows"); return 1
    with open(out / "activity_rows.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(act_rows[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(act_rows)
    cat = catalogue_by_chembl(); mol = defaultdict(list)
    for x in act_rows: mol[(x["relation_id"], x["parent_chembl_id"])].append(x)
    mrows = []
    per_rel = defaultdict(set)
    for (rid, par) in mol: per_rel[rid].add(par)
    DEPOSIT = 200   # a document that measures more molecules than this on the relation's targets is a screening deposit: its molecules are pointers to the screen, not candidates
    doc_mols = defaultdict(set)
    for (rid, par), xs in mol.items():
        for x in xs: doc_mols[(rid, x["document"])].add(par)
    for (rid, par), xs in sorted(mol.items()):
        nm = sorted({x["name"] for x in xs if x["name"]}); fun = [x for x in xs if x["assay_type"] == "F"]
        cn, cs, co = cat.get(par, ("", "", ""))
        mrows.append(dict(relation_id=rid, parent_chembl_id=par, name=" | ".join(nm)[:80], catalogue_name=cn[:60], catalogue_status=cs or ("none" if not cn else "unstated"), catalogue_origin=co, n_documents=len({x["document"] for x in xs if x["document"]}), n_activities=len(xs), n_functional=len(fun), types=";".join(sorted({x["type"] for x in xs})), organisms=";".join(sorted({x["assay_organism"] for x in xs if x["assay_organism"]}))[:80],
            targets=";".join(sorted({x["target_symbol"] for x in xs})), n_flagged_validity=sum(1 for x in xs if x["validity"]), unit_variants=";".join(sorted({x["units"] for x in xs if x["units"]}))[:40],
            coverage=";".join(sorted({x["coverage"] for x in xs})), read_state=("TRUNCATED" if any(x["coverage"] != "COMPLETE" for x in xs) else "SCREEN_DEPOSIT" if all(len(doc_mols[(rid, x["document"])]) > DEPOSIT for x in xs) else "OK"), verdict="ACTIVITY_ONLY", unknown_fields=UNKNOWN_FIELDS))
    with open(out / "activity_molecules.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(mrows[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(mrows)
    json.dump(manifest, open(out / "activity_manifest.json", "w"), indent=1)
    print(len(act_rows), "activity rows;", len(mrows), "molecule x relation rows;", {k: v["coverage"] for k, v in manifest.items()})
    return 0
if __name__ == "__main__": sys.exit(main())
