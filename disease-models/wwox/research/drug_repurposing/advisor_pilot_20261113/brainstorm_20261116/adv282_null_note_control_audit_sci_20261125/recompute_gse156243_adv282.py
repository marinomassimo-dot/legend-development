"""ADV-282 increment 1: per-library recount of the named genes in the GSE156243 count table and deposited lists. Args: folder, then set:GENE,GENE ... Run with python3 -I -P -E."""
import csv, gzip, io, math, sys
base = sys.argv[1]
def rd(n):
    return list(csv.reader(io.TextIOWrapper(gzip.open(f"{base}/{n}"), "utf-8", errors="replace"), delimiter="\t"))
t = rd("GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz")
cols = t[0][1:]
raw = {r[0]: [float(x) for x in r[1:]] for r in t[1:]}
lib = [sum(v[i] for v in raw.values()) for i in range(len(cols))]
print("columns", cols, "library totals", [round(x/1e6, 2) for x in lib])
de = {}
for n, d in (("GSE156243_CKO_CWT_1246_upregulated_genes.txt.gz", "UP"), ("GSE156243_CKO_CWT_1021_downregulated_genes.txt.gz", "DOWN")):
    rows = rd(n); h = rows[0]
    for r in rows[1:]:
        x = dict(zip(h, r)); de[x["symbol"]] = (d, x.get("log2FoldChange"), x.get("padj"))
ko = [i for i, c in enumerate(cols) if c.startswith("cko")]; wt = [i for i, c in enumerate(cols) if c.startswith("cwt")]
def show(g):
    v = raw.get(g)
    if v is None: print(f"{g}\tNOT IN TABLE"); return
    cpm = [v[i]/lib[i]*1e6 for i in range(len(cols))]
    mk = sum(cpm[i] for i in ko)/4; mw = sum(cpm[i] for i in wt)/2
    ratio = mk/mw if mw else float("nan")
    sep = "all KO above both WT" if min(cpm[i] for i in ko) > max(cpm[i] for i in wt) else ("all KO below both WT" if max(cpm[i] for i in ko) < min(cpm[i] for i in wt) else "overlap")
    lg = math.log2(ratio) if ratio and ratio > 0 else float("nan")
    print(f"{g}\traw {','.join(str(int(round(v[i]))) for i in range(len(cols)))}\tCPM ko {mk:.2f} wt {mw:.2f}\tratio {ratio:.2f}\tlog2 {lg:+.2f}\t{sep}\tDE {de.get(g, 'none')}")
for grp in sys.argv[2:]:
    name, genes = grp.split(":")
    print("##", name)
    for g in genes.split(","): show(g)
print("DE list sizes", sum(1 for v in de.values() if v[0]=="UP"), sum(1 for v in de.values() if v[0]=="DOWN"))
