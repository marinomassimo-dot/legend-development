"""SCI47 package B: values of a gene list by cluster type from the HPA single-nuclei brain table, plus the raw value of the same genes in the local GSE73721 human table.
  python3 -I hpa_cluster_extract.py <rna_single_nuclei_cluster_type.tsv.zip> <GSE73721_Human_and_mouse_table.csv.gz> <out dir> [GENE ...]
Writes hpa_cluster_values.tsv (gene, cluster_type, nCPM or 'not in table'), gse73721_raw_neuron.tsv (raw cells of the neuron, astrocyte and whole-cortex columns) and input hashes. No statistics: one pooled value per cluster type; the loader attributes no biological meaning."""
import sys, zipfile, io, csv, gzip, hashlib, os
if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 4:
    print(__doc__); sys.exit(0)
zp, hp, out = sys.argv[1:4]
GENES = [g.upper() for g in sys.argv[4:]] or ["KCNQ2","KCNQ3","KCNQ5","SNAP25","RBFOX3","SLC17A7","GAD1","GFAP","AQP4","P2RY12","MBP","PDGFRA"]
z = zipfile.ZipFile(zp); name = z.namelist()[0]
rd = csv.reader(io.TextIOWrapper(z.open(name), encoding="utf-8"), delimiter="\t"); hdr = next(rd)
gi, ni, ci, vi = hdr.index("Gene name"), hdr.index("Gene name"), hdr.index("Cluster type"), hdr.index("nCPM")
types = set(); vals = {}
for r in rd:
    types.add(r[ci])
    if r[gi].upper() in GENES: vals[(r[gi].upper(), r[ci])] = r[vi]
sha = hashlib.sha256(open(zp, "rb").read()).hexdigest()
with open(os.path.join(out, "hpa_cluster_values.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "cluster_type", "nCPM", "input_sha256"])
    for g in GENES:
        present = any(k[0] == g for k in vals)
        for t in sorted(types):
            w.writerow([g, t, vals.get((g, t), "0 (row absent for this gene and type)" if present else "gene not in table"), sha])
hs = hashlib.sha256(open(hp, "rb").read()).hexdigest()
r2 = csv.reader(gzip.open(hp, "rt", encoding="latin1")); h2 = next(r2)
cols = [i for i, h in enumerate(h2) if i and (h.strip().endswith("neuron") or "whole cortex" in h or h.strip().endswith("astro") or h.strip().endswith("oligo") or h.strip().endswith("myeloid"))]
with open(os.path.join(out, "gse73721_raw_cells.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "column_header", "raw_cell", "input_sha256"])
    for r in r2:
        if r[0].upper() in GENES:
            for i in cols: w.writerow([r[0].upper(), h2[i].strip(), r[i], hs])
print("hpa types", len(types), "input sha", sha[:12], "human sha", hs[:12])
