#!/usr/bin/env python3
"""HE44 H1/H3: for the genes of given relations files, the ChEMBL human targets a cached-index lookup finds against the exact targets by UniProt accession.
The cached index is the one `activity_search.py` (IT44) builds from catalog/cache/chembl/targets.jsonl.gz, which holds only targets linked to a curated mechanism.
  LEGEND_CATALOG_CACHE=<cache> python3 symbol_coverage.py <relations.tsv> [more.tsv] --out symbol_coverage.tsv --cache <adapter cache dir>"""
import argparse, collections, csv, gzip, json, os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts")); sys.path.insert(0, str(HERE.parents[4] / "framework"))
import compound_catalog as cc, target_activity as ta  # noqa: E402
from adapters import _http, chembl  # noqa: E402

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("relations", nargs="+"); ap.add_argument("--out", required=True); ap.add_argument("--cache", default=None)
    a = ap.parse_args()
    genes = collections.defaultdict(set)
    for f in a.relations:
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter="\t"):
            for s in r["target_symbols"].replace(":down", "").replace(":up", "").split(";"):
                if s.strip(): genes[s.split(":")[0].strip().upper()].add(r["relation_id"])
    root = Path(os.environ.get("LEGEND_CATALOG_CACHE") or HERE.parent / "catalog/cache")
    idx = collections.defaultdict(set)
    with gzip.open(root / "chembl/targets.jsonl.gz", "rt") as f:
        for line in f:
            t = json.loads(line)
            if t.get("organism") != "Homo sapiens": continue
            for c in t.get("target_components") or []:
                for s in c.get("target_component_synonyms") or []:
                    if s.get("syn_type") == "GENE_SYMBOL": idx[s["component_synonym"].upper()].add(t["target_chembl_id"])
    path, digest = cc.cache_file("gtopdb/targets_and_families.csv"); tbl = ta.load_gtopdb_targets(path)
    fetch = _http.make_fetch(a.cache) if a.cache else _http.make_fetch(); q = lambda r: chembl.query(r, fetch=fetch)  # noqa: E731
    rows = []
    for g in sorted(genes):
        rt = ta.resolve_targets(g, q, tbl); cached = idx.get(g, set()); exact = {t["target_chembl_id"]: t["target_type"] for t in rt["targets"]}
        miss = sorted(set(exact) - cached)
        rows.append([g, ";".join(sorted(genes[g])), rt["state"], rt["accession"] or "", len(cached), len(exact), len(miss), sum(1 for m in miss if exact[m] == "SINGLE PROTEIN"), ";".join(miss), rt.get("source_version") or ""])
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["gene", "relations", "state", "accession", "targets_in_cached_index", "exact_human_targets", "missing_from_index", "missing_single_protein", "missing_ids", "chembl_release"]); w.writerows(rows)
    z = sum(1 for r in rows if r[4] == 0 and r[5] > 0)
    print(f"{len(rows)} genes; {z} with no target in the cached index but at least one exact target; {sum(r[6] for r in rows)} exact targets missing from the index, {sum(r[7] for r in rows)} of them single protein")
if __name__ == "__main__": main()
