#!/usr/bin/env python3
"""Iteration 2 (scientist-d): one table of the informative signatures with compound identity, ChEMBL action, cell-line context (GSE92742/GSE70138 cell_info),
frequent-hitter flag. Reads derived/lincs_it2_compound_identity.json, derived/lincs_it2_frequent_hitters.json, tool_responses (no network).
Usage: lincs_it2_report_tables.py <dir holding the GEO gz files>   -> derived/lincs_it2_informative_signatures.tsv"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]) or len(_sys.argv) < 2:
    print(__doc__)
    raise SystemExit(0)
import csv, gzip, json
D = _sys.argv[1]
cells = {}
for fn in ("GSE70138_Broad_LINCS_cell_info_2017-04-28.txt.gz", "GSE92742_Broad_LINCS_cell_info.txt.gz"):
    for r in csv.DictReader(gzip.open(f"{D}/{fn}", "rt"), delimiter="\t"): cells[r["cell_id"]] = r
ident = json.load(open("derived/lincs_it2_compound_identity.json")); C = {k: v for k, v in ident["codes"].items() if not k.startswith("_")}
fh = json.load(open("derived/lincs_it2_frequent_hitters.json"))["S1_compound_to_null_rankings_containing_it_in_either_tail"]
def ctx(cell):
    r = cells.get(cell)
    if not r: return "NOT_IN_GSE92742/70138_cell_info"
    return f"{r['sample_type']}|{r['primary_site']}|{r['subtype']}|{r['cell_type']}"
rows = []
for h in ident["hits"]:
    src, tail, st, sig, brd, cell, tm, dose, val = h[:9]
    if src == "SigCom_S1_top100":
        keep = (not cell.startswith("MCLF")) or tail == "reversers" and h[9] in ("sildenafil", "nimodipine", "quiflapon") or brd in ("BRD-K09398529", "BRD-K52904470", "BRD-K55591206")
        if not keep: continue
        name = h[9]
    else: name = None
    o = C.get(brd, {}); ch = o.get("chembl")
    mech = "; ".join(ch["mechanisms"]) if isinstance(ch, dict) else (ch or "")
    nm = name or (o.get("inames") or [""])[0]
    tailkey = tail if src == "SigCom_S1_top100" else None
    hit_nulls = fh.get(tailkey, {}).get(nm, []) if tailkey else []
    rows.append([src, tail, sig, cell, tm, dose, val, brd, nm, "resolved" if o.get("resolved") else ("no-BRD-in-cmap_id" if not brd else "FAILED"), o.get("inchi_key", ""),
                 ch.get("id", "") if isinstance(ch, dict) else "", ch.get("max_phase", "") if isinstance(ch, dict) else "", mech, ctx(cell), ",".join(hit_nulls)])
with open("derived/lincs_it2_informative_signatures.tsv", "w") as f:
    w = csv.writer(f, delimiter="\t"); w.writerow(["source", "tail", "sig_or_rank", "cell", "time", "dose", "q_or_zsum", "brd", "name", "identity", "inchi_key", "chembl_id", "chembl_max_phase", "chembl_mechanisms", "cell_context_GSE92742_70138", "null_rankings_containing_name"])
    w.writerows(rows)
print(len(rows), "rows")
