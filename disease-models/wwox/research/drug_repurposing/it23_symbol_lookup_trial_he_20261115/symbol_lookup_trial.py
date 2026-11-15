"""Offline trial of the IT23 gene-symbol lookup (PRESIDIO-004 part A). Reads, never writes outside <out_dir>.

Usage: symbol_lookup_trial.py <repo_root> <geo_files_dir> <out_dir>

repo_root       the checkout that holds signature_it23_20261103/ and gse156243/ (read only)
geo_files_dir   files/geo, holding GSE156243/hgnc_complete_set_20261022.json, GSE150123/ and GSE92742/ (read only)
out_dir         receives the tables and trial_summary.json

No network, no install, no live query. The symbol logic is that of gse156243/validate_symbols.py (approved, previous
symbol, alias; ENSG kept); the flag definitions are those of signature_it23_20261103/reproduce_dseqr_cmap_comparison.py,
copied here so that neither committed file is imported, run or changed.
"""
import sys
if any(a in ("-h", "--help") for a in sys.argv[1:]) or len(sys.argv) != 4:
    print(__doc__); raise SystemExit(0)
import collections, csv, gzip, io, json, math, os, tarfile

REPO, GEO, OUT = sys.argv[1:4]
DR = f"{REPO}/disease-models/wwox/research/drug_repurposing"
G, IT = f"{DR}/gse156243", f"{DR}/signature_it23_20261103"
RHO_MIN = 0.6                                           # same constant as the reproduction script
os.makedirs(OUT, exist_ok=True)

def tsv(path): return list(csv.DictReader(open(path, encoding="utf-8"), delimiter="\t"))
def write_tsv(path, rows, cols):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows: f.write("\t".join(str(r.get(c, "")) for c in cols) + "\n")

# ---- inputs -------------------------------------------------------------------------------------------------------------------------------------------
docs = json.load(open(f"{GEO}/GSE156243/hgnc_complete_set_20261022.json"))["response"]["docs"]
approved = {d["symbol"]: d for d in docs}
prev, alias = collections.defaultdict(list), collections.defaultdict(list)
for d in docs:
    for p in d.get("prev_symbol", []): prev[p].append(d["symbol"])
    for a in d.get("alias_symbol", []): alias[a].append(d["symbol"])
AUTH = {r["symbol"]: r for r in tsv(f"{G}/derived/list_padj_le_0.05.tsv")}                    # the authors' list, keyed by ITS symbol
AUTH_BY_ENSG = collections.defaultdict(list)
for r in AUTH.values(): AUTH_BY_ENSG[r["ensg"]].append(r["symbol"])
S1 = json.load(open(f"{G}/derived/query_sets.json"))["S1"]
UP, DN = list(S1["up"]), list(S1["down"])
gi = list(csv.DictReader(gzip.open(f"{GEO}/GSE92742/GSE92742_Broad_LINCS_gene_info.txt.gz", "rt"), delimiter="\t"))
LM = {r["pr_gene_symbol"] for r in gi if r["pr_is_lm"] == "1"}
SPACE = {r["pr_gene_symbol"] for r in gi if r["pr_is_lm"] == "1" or r["pr_is_bing"] == "1"}
DECL_SYMBOLS = set()
for r in tsv(f"{G}/marker_sets_declared.tsv"): DECL_SYMBOLS |= set(r["genes"].split(","))
COMMITTED = {r["symbol"]: r for r in tsv(f"{IT}/composition_class.tsv")}

# ---- the conversion: query symbol -> the authors' list row, by two routes that must agree ---------------------------------------------------------------
def convert(sym):
    """Returns a record that keeps the original symbol, the ENSG and the reason for any non-conversion; nothing is guessed."""
    rec = {"query_symbol": sym, "hgnc_status": "", "hgnc_ensg": "", "authors_symbol": "", "authors_ensg": "", "route_symbol": "", "route_ensg": "", "status": "", "note": ""}
    d = approved.get(sym)
    if d is None:
        rec["hgnc_status"] = "previous_symbol->" + "|".join(prev[sym]) if sym in prev else ("alias->" + "|".join(alias[sym]) if sym in alias else "not_in_HGNC")
    else:
        rec["hgnc_status"] = "approved"; rec["hgnc_ensg"] = d.get("ensembl_gene_id", "")
    # route A: by symbol (the symbol itself, then every previous symbol and alias of the approved record)
    cand = []
    if sym in AUTH: cand.append((sym, "same_symbol"))
    if d is not None:
        for p in d.get("prev_symbol", []):
            if p in AUTH: cand.append((p, "previous_symbol"))
        for a in d.get("alias_symbol", []):
            if a in AUTH and a not in {c for c, _ in cand}: cand.append((a, "alias"))
    if sym in AUTH:                         # the symbol is already the authors' key: nothing to convert; an alias of this gene that is ANOTHER row of the list (GPNMB lists NMB) is noise, not a competitor
        others = sorted({c for c, _ in cand if c != sym})
        agree = bool(rec["hgnc_ensg"]) and AUTH[sym]["ensg"] == rec["hgnc_ensg"]
        rec.update(authors_symbol=sym, authors_ensg=AUTH[sym]["ensg"], route_symbol=sym + "(same_symbol)", route_ensg=";".join(sorted(AUTH_BY_ENSG.get(rec["hgnc_ensg"], []))) if rec["hgnc_ensg"] else "",
                   status="same_symbol" if agree else "same_symbol_ensg_not_confirmed",
                   note=("aliases/previous symbols that are other rows of the list were ignored: " + ",".join(others)) if others else ("" if agree else "HGNC ENSG differs from or is missing against the authors' ENSG"))
        return rec
    a_syms = sorted({c for c, _ in cand})
    # route B: by the stable identifier of the approved record
    b_syms = sorted(AUTH_BY_ENSG.get(rec["hgnc_ensg"], [])) if rec["hgnc_ensg"] else []
    rec["route_symbol"] = ";".join(f"{c}({how})" for c, how in cand)
    rec["route_ensg"] = ";".join(b_syms)
    if len(a_syms) == 1 and b_syms == a_syms:
        rec["authors_symbol"] = a_syms[0]; rec["authors_ensg"] = AUTH[a_syms[0]]["ensg"]
        rec["status"] = "same_symbol" if a_syms[0] == sym else "converted_two_routes_agree"
    elif not a_syms and not b_syms:
        rec["status"] = "unresolved"; rec["note"] = "no authors' row by symbol, previous symbol, alias or ENSG"
    elif len(a_syms) > 1 or len(b_syms) > 1:
        rec["status"] = "ambiguous"; rec["note"] = f"symbol route {a_syms}, ENSG route {b_syms}"
    else:
        rec["status"] = "routes_disagree"; rec["note"] = f"symbol route {a_syms}, ENSG route {b_syms}"
    return rec

# ---- flags, with the reproduction script's own definitions, keyed either as stored (before) or through the conversion (after) ----------------------------
def spearman(x, y):
    def rk(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
        while i < len(o):
            j = i
            while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]: j += 1
            for k in range(i, j + 1): r[o[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    a, b = rk(x), rk(y); ma, mb = sum(a) / len(a), sum(b) / len(b)
    sa = math.sqrt(sum((u - ma) ** 2 for u in a)); sb = math.sqrt(sum((u - mb) ** 2 for u in b))
    return sum((u - ma) * (v - mb) for u, v in zip(a, b)) / (sa * sb) if sa and sb else 0.0

meta = gzip.open(f"{GEO}/GSE150123/GSE150123_series_matrix.txt.gz", "rt").read().splitlines()
gsm = next(l for l in meta if l.startswith("!Sample_geo_accession")).split("\t")[1:]
day = next(l for l in meta if "differentiation day" in l).split("\t")[1:]
day = {g.strip('"'): float(d.strip('"').split(": ")[1]) for g, d in zip(gsm, day)}
cols = {}
tf = tarfile.open(f"{GEO}/GSE150123/GSE150123_RAW.tar")
for m in tf.getmembers():
    g = m.name.split("_")[0]
    rows = list(csv.reader(io.TextIOWrapper(gzip.open(tf.extractfile(m), "r"), "utf-8")))[1:]
    cols[g] = {r[0]: float(r[1]) for r in rows}
samples = sorted(cols); tot = {s: sum(cols[s].values()) for s in samples}

def rho_for(ensg):
    if not ensg or any(ensg not in cols[s] for s in samples): return None
    if sum(cols[s][ensg] for s in samples) / len(samples) < 5: return None
    y = [math.log2(cols[s][ensg] / tot[s] * 1e6 + 1) for s in samples]
    return spearman([math.log10(day[s]) for s in samples], y)

def flags(keyer, label):
    """keyer(query_symbol) -> (authors_symbol or None). Returns per-symbol facts and the five query sets, by the reproduction script's rules."""
    out = {}
    for g in UP + DN:
        k = keyer(g)
        row = AUTH.get(k) if k else None
        out[g] = {"log2fc": float(row["log2FoldChange"]) if row else None, "ensg": row["ensg"] if row else "", "rho": rho_for(row["ensg"]) if row else None,
                  "in_space": (k in SPACE) if k else False, "landmark": (k in LM) if k else False, "auth_dir": row["direction"] if row else ""}
    decl = {g for g in UP + DN if g in DECL_SYMBOLS or (keyer(g) in DECL_SYMBOLS)} if label == "after" else {g for g in UP + DN if g in DECL_SYMBOLS}
    mat = {g for g, v in out.items() if v["rho"] is not None and abs(v["rho"]) >= RHO_MIN and ((g in UP and v["rho"] < 0) or (g in DN and v["rho"] > 0))}
    comp = decl | mat
    broad = decl | {g for g, v in out.items() if v["rho"] is not None and abs(v["rho"]) >= 0.4}
    q = {"QA_all": (UP, DN),
         "QC_minus_declared": ([g for g in UP if g not in decl], [g for g in DN if g not in decl]),
         "QD_minus_composition": ([g for g in UP if g not in comp], [g for g in DN if g not in comp]),
         "QF_minus_broad_maturation": ([g for g in UP if g not in broad], [g for g in DN if g not in broad]),
         "QE_composition_flipped": ([g for g in UP if g not in comp] + [g for g in DN if g in comp], [g for g in DN if g not in comp] + [g for g in UP if g in comp])}
    return out, decl, mat, comp, broad, q

CONV = {g: convert(g) for g in UP + DN}
COMMITTED_BLANK = {g for g, r in COMMITTED.items() if r["log2fc"] == ""}
before = flags(lambda g: g if g in AUTH else None, "before")                      # the lookup as the package ran it: the query symbol itself is the key
after = flags(lambda g: CONV[g]["authors_symbol"] or None, "after")               # the key is the authors' symbol reached by two agreeing routes, else nothing

# ---- check: does the stored-key reproduction give the committed table? (otherwise "before" would not be the package's before) ------------------------------
o_b = before[0]
mismatch = []
for g in UP + DN:
    c = COMMITTED[g]; v = o_b[g]
    got = (f"{v['log2fc']}" if v["log2fc"] is not None else "") == (c["log2fc"] if c["log2fc"] == "" else f"{float(c['log2fc'])}")
    got &= (f"{v['rho']:.3f}" if v["rho"] is not None else "") == c["rho_vs_log10_day"]
    got &= int(g in before[3]) == int(c["composition_class"]) and int(g in before[4]) == int(c["broad_class_abs_rho_ge_0.4"]) and int(g in before[1]) == int(c["in_declared_markers"])
    got &= int(v["in_space"]) == int(c["in_L1000_12328_space"]) and int(v["landmark"]) == int(c["landmark_978"])
    got &= (g in UP) == (c["ko_direction"] == "up")
    if not got: mismatch.append(g)

# ---- outputs ------------------------------------------------------------------------------------------------------------------------------------------
map_cols = ["query_symbol", "ko_direction", "hgnc_status", "hgnc_ensg", "authors_symbol", "authors_ensg", "route_symbol", "route_ensg", "status", "note"]
write_tsv(f"{OUT}/symbol_mapping_834.tsv", [{**CONV[g], "ko_direction": "up" if g in UP else "down"} for g in UP + DN], map_cols)

changed_rows = [g for g in UP + DN if CONV[g]["status"] != "same_symbol" or g in COMMITTED_BLANK]
cols_ba = ["query_symbol", "ko_direction", "conversion_status", "authors_symbol", "ensg", "authors_list_direction", "direction_agrees", "log2fc_before", "log2fc_after", "rho_before", "rho_after",
           "declared_before", "declared_after", "composition_before", "composition_after", "broad_before", "broad_after", "in_L1000_space_before", "in_L1000_space_after", "landmark_before", "landmark_after"]
def fmt(x, nd=3): return "" if x is None else f"{x:.{nd}f}"
rows_ba = []
for g in changed_rows:
    b, a = before[0][g], after[0][g]; kd = "up" if g in UP else "down"
    rows_ba.append({"query_symbol": g, "ko_direction": kd, "conversion_status": CONV[g]["status"], "authors_symbol": CONV[g]["authors_symbol"], "ensg": CONV[g]["authors_ensg"] or CONV[g]["hgnc_ensg"],
                    "authors_list_direction": a["auth_dir"], "direction_agrees": ("" if not a["auth_dir"] else int(a["auth_dir"] == kd)),
                    "log2fc_before": fmt(b["log2fc"], 2), "log2fc_after": fmt(a["log2fc"], 2), "rho_before": fmt(b["rho"]), "rho_after": fmt(a["rho"]),
                    "declared_before": int(g in before[1]), "declared_after": int(g in after[1]), "composition_before": int(g in before[3]), "composition_after": int(g in after[3]),
                    "broad_before": int(g in before[4]), "broad_after": int(g in after[4]), "in_L1000_space_before": int(b["in_space"]), "in_L1000_space_after": int(a["in_space"]),
                    "landmark_before": int(b["landmark"]), "landmark_after": int(a["landmark"])})
write_tsv(f"{OUT}/before_after_converted_rows.tsv", rows_ba, cols_ba)

facts = json.load(open(f"{IT}/run_facts.json"))
chg = []
for name in before[5]:
    bu, bd = before[5][name]; au, ad = after[5][name]
    add_u, rem_u, add_d, rem_d = sorted(set(au) - set(bu)), sorted(set(bu) - set(au)), sorted(set(ad) - set(bd)), sorted(set(bd) - set(ad))
    chg.append({"query": name, "up_before": len(bu), "up_after": len(au), "down_before": len(bd), "down_after": len(ad), "membership_changed": int(bool(add_u or rem_u or add_d or rem_d)),
                "genes_added_up": ",".join(add_u), "genes_removed_up": ",".join(rem_u), "genes_added_down": ",".join(add_d), "genes_removed_down": ",".join(rem_d),
                "stored_response_present": int(name in facts["responses"]), "to_repeat_if_adopted": int(bool(add_u or rem_u or add_d or rem_d))})
write_tsv(f"{OUT}/query_membership_changes.tsv", chg, list(chg[0]))

summary = {"rows": len(UP + DN), "up": len(UP), "down": len(DN), "status_counts": dict(collections.Counter(c["status"] for c in CONV.values())),
           "before_reproduces_committed_table": {"mismatching_rows": len(mismatch), "rows": mismatch},
           "rows_with_blank_log2fc_committed": sum(1 for r in COMMITTED.values() if r["log2fc"] == ""),
           "converted_rows": [g for g in UP + DN if CONV[g]["status"] == "converted_two_routes_agree"],
           "non_converted_unresolved_or_ambiguous": [g for g in UP + DN if CONV[g]["status"] in ("unresolved", "ambiguous", "routes_disagree", "same_symbol_ensg_not_confirmed")],
           "same_symbol_rows_with_ignored_alias_hits": [g for g in UP + DN if CONV[g]["status"] == "same_symbol" and CONV[g]["note"]],
           "rows_whose_composition_or_broad_flag_changed": [g for g in UP + DN if (g in before[3]) != (g in after[3]) or (g in before[4]) != (g in after[4]) or (g in before[1]) != (g in after[1])],
           "queries_with_changed_membership": [c["query"] for c in chg if c["membership_changed"]],
           "live_queries_run": 0, "hgnc_file": "files/geo/GSE156243/hgnc_complete_set_20261022.json", "samples_in_maturation_series": len(samples)}
json.dump(summary, open(f"{OUT}/trial_summary.json", "w"), indent=1, sort_keys=True)
print(json.dumps(summary, indent=1, sort_keys=True))
