#!/usr/bin/env python3
"""PRESIDIO-004 part B: independent reference mapping of the 15 composition_class.tsv rows with blank log2fc.

Offline, read-only. Inputs: the authors' two gene lists and the HGNC file in files/geo/GSE156243,
and signature_it23_20261103/composition_class.tsv. Key: HGNC ensembl_gene_id -> authors' ENSG column;
the previous-symbol route is checked as a second, independent route. Usage:
  python3 -I build_reference_mapping.py <GSE156243_dir> <composition_class.tsv> <out_dir>
"""
import collections, csv, gzip, hashlib, json, os, sys

BLANK = "IRAG1 CCN2 DRC4 MNMIP1 POFUT4 MTCL2 ATOSB HDIP1 BBLN ADPRS CIRSR H1-2 H1-10 H4C15 ZNRD2".split()
FILES = {"down": "GSE156243_CKO_CWT_1021_downregulated_genes.txt.gz",
         "up": "GSE156243_CKO_CWT_1246_upregulated_genes.txt.gz"}
HGNC = "hgnc_complete_set_20261022.json"


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main(geo, comp, out):
    docs = json.load(open(os.path.join(geo, HGNC)))["response"]["docs"]
    by_sym = {d["symbol"]: d for d in docs}
    prev = collections.defaultdict(list)
    alias = collections.defaultdict(list)
    ens = collections.defaultdict(list)
    for d in docs:
        for p in d.get("prev_symbol") or []:
            prev[p].append(d["hgnc_id"])
        for p in d.get("alias_symbol") or []:
            alias[p].append(d["hgnc_id"])
        if d.get("ensembl_gene_id"):
            ens[d["ensembl_gene_id"]].append(d["hgnc_id"])
    auth = {}
    for lst, fn in FILES.items():
        for r in csv.DictReader(gzip.open(os.path.join(geo, fn), "rt"), delimiter="\t"):
            auth.setdefault(r["ensg"], []).append((lst, r))
    tsv = {r["symbol"]: r for r in csv.DictReader(open(comp), delimiter="\t")}
    cols = ["query_symbol", "hgnc_id", "ensg", "authors_symbol", "authors_list", "authors_direction",
            "log2fc", "padj", "entrez_hgnc", "entrez_authors", "authors_symbol_is_hgnc_previous",
            "previous_symbol_maps_to_one_hgnc_gene", "ensg_maps_to_one_hgnc_gene", "ensg_rows_in_authors_lists",
            "composition_class_direction", "direction_agrees", "ambiguity", "status"]
    rows = []
    for q in BLANK:
        d = by_sym[q]
        e = d["ensembl_gene_id"]
        hits = auth.get(e, [])
        if len(hits) != 1:
            rows.append([q, d["hgnc_id"], e, "", "", "", "", "", d.get("entrez_id", ""), "", "", "", str(len(ens[e]) == 1),
                         str(len(hits)), tsv[q]["ko_direction"], "", "no or several authors rows", "UNRESOLVED"])
            continue
        lst, r = hits[0]
        a = r["symbol"]
        is_prev = a in (d.get("prev_symbol") or [])
        one = len(set(prev.get(a, []))) == 1
        direction = "up" if float(r["log2FoldChange"]) > 0 else "down"
        amb = []
        for o in (d.get("alias_symbol") or []):
            if len(set(alias.get(o, []))) > 1:
                amb.append("alias %s shared by %d genes (not used)" % (o, len(set(alias[o]))))
        ok = (is_prev and one and len(ens[e]) == 1 and str(d.get("entrez_id")) == r["EntrezID"]
              and direction == tsv[q]["ko_direction"] and lst == direction)
        rows.append([q, d["hgnc_id"], e, a, lst, direction, r["log2FoldChange"], r["padj"], d.get("entrez_id", ""),
                     r["EntrezID"], str(is_prev), str(one), str(len(ens[e]) == 1), str(len(hits)),
                     tsv[q]["ko_direction"], str(direction == tsv[q]["ko_direction"]), "; ".join(amb) or "none",
                     "RESOLVED_UNIQUE" if ok else "CHECK"])
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "mapping_reference.tsv"), "w", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(cols)
        w.writerows(rows)
    with open(os.path.join(out, "input_digests.tsv"), "w") as f:
        f.write("file\tsha256\n")
        for fn in [HGNC] + list(FILES.values()):
            f.write("%s\t%s\n" % (fn, sha(os.path.join(geo, fn))))
        f.write("composition_class.tsv\t%s\n" % sha(comp))
    print("rows", len(rows), "RESOLVED_UNIQUE", sum(r[-1] == "RESOLVED_UNIQUE" for r in rows))


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2)
    main(*sys.argv[1:4])
