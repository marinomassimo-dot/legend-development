"""IT55: independent re-derivation of the QF_minus_broad_maturation membership change (PRESIDIO-004 part C). Standard library only; offline.
Inputs: committed composition_class.tsv (declared-marker flags and the committed broad flags), the authors' raw GEO lists, GSE150123 counts and series matrix.
The 15 old symbols come from SCI's reference table (mapping_reference.tsv, hand-read), not from HE's output. Usage: python3 -I rederive_qf.py <repo_root>"""
import csv, gzip, io, math, sys, tarfile
R = sys.argv[1]; DR = f"{R}/disease-models/wwox/research/drug_repurposing"; GEO = f"{R}/files/geo"
OLD = {"IRAG1": "MRVI1", "CCN2": "CTGF", "DRC4": "GAS8", "MNMIP1": "SH3D21", "POFUT4": "FUT11", "MTCL2": "SOGA1", "ATOSB": "FAM214B", "HDIP1": "C16orf87",
       "BBLN": "C9orf16", "ADPRS": "ADPRHL2", "CIRSR": "CIR1", "H1-2": "HIST1H1C", "H1-10": "H1FX", "H4C15": "HIST2H4B", "ZNRD2": "SSSCA1"}
ens = {}
for f in ("GSE156243_CKO_CWT_1246_upregulated_genes.txt.gz", "GSE156243_CKO_CWT_1021_downregulated_genes.txt.gz"):
    for r in csv.DictReader(io.TextIOWrapper(gzip.open(f"{GEO}/GSE156243/{f}"), "utf-8"), delimiter="\t"): ens[r["symbol"]] = r["ensg"]
tab = list(csv.DictReader(open(f"{DR}/signature_it23_20261103/composition_class.tsv"), delimiter="\t"))
meta = gzip.open(f"{GEO}/GSE150123/GSE150123_series_matrix.txt.gz", "rt").read().splitlines()
gsm = next(l for l in meta if l.startswith("!Sample_geo_accession")).split("\t")[1:]
day = next(l for l in meta if "differentiation day" in l).split("\t")[1:]
day = {g.strip('"'): float(d.strip('"').split(": ")[1]) for g, d in zip(gsm, day)}
cols = {}
for m in (tf := tarfile.open(f"{GEO}/GSE150123/GSE150123_RAW.tar")).getmembers():
    rows = list(csv.reader(io.TextIOWrapper(gzip.open(tf.extractfile(m), "r"), "utf-8")))[1:]
    cols[m.name.split("_")[0]] = {r[0]: float(r[1]) for r in rows}
S = sorted(cols); tot = {s: sum(cols[s].values()) for s in S}
def rk(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]: j += 1
        for k in range(i, j + 1): r[o[k]] = (i + j) / 2 + 1
        i = j + 1
    return r
def sp(x, y):
    a, b = rk(x), rk(y); ma, mb = sum(a) / len(a), sum(b) / len(b)
    sa = math.sqrt(sum((u - ma) ** 2 for u in a)); sb = math.sqrt(sum((u - mb) ** 2 for u in b))
    return sum((u - ma) * (v - mb) for u, v in zip(a, b)) / (sa * sb) if sa and sb else 0.0
def rho(e):
    if not e or any(e not in cols[s] for s in S) or sum(cols[s][e] for s in S) / len(S) < 5: return None
    return sp([math.log10(day[s]) for s in S], [math.log2(cols[s][e] / tot[s] * 1e6 + 1) for s in S])
changed = []; up = dn = 0; mism = 0
for r in tab:
    g = r["symbol"]; e = ens.get(OLD.get(g, g)); x = rho(e)
    broad = int(r["in_declared_markers"] == "1" or (x is not None and abs(x) >= 0.4))
    if r["rho_vs_log10_day"] and x is not None and abs(float(r["rho_vs_log10_day"]) - x) > 5e-4: mism += 1
    if broad != int(r["broad_class_abs_rho_ge_0.4"]): changed.append((g, OLD.get(g, ""), r["ko_direction"], r["broad_class_abs_rho_ge_0.4"], broad, None if x is None else round(x, 3)))
    if not broad: (up := up + 1) if r["ko_direction"] == "up" else (dn := dn + 1)
print("my QF up/down", up, dn, "| committed 365/260 | rho mismatches vs committed rows with a value:", mism)
print("rows whose broad flag differs from the committed table:"); [print(" ", c) for c in changed]
print("rho of the 15:", {g: (None if rho(ens.get(o)) is None else round(rho(ens.get(o)), 3)) for g, o in OLD.items()})
