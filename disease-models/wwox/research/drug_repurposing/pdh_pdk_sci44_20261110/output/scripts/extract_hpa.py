"""Extract the nine PDH-complex genes from three unzipped HPA downloads (single-nuclei brain clusters, single cell types, normal IHC). usage: python3 -I extract_hpa.py <hpa_dir> <out_dir>
No network. Reads local files given as arguments.
"""
import sys
if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)
import sys, os, hashlib
d, out = sys.argv[1:3]
genes = ["PDK1","PDK2","PDK3","PDK4","PDP1","PDP2","PDHA1","PDHB","DLAT"]
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def rows(p):
    with open(p, encoding="utf-8") as f:
        h = f.readline().rstrip("\n").split("\t")
        for l in f:
            yield dict(zip(h, l.rstrip("\n").split("\t")))
nuc = os.path.join(d, "rna_single_nuclei_cluster_type.tsv")
sc = os.path.join(d, "rna_single_cell_type.tsv")
ihc = os.path.join(d, "normal_ihc_data.tsv")
keepn = {"upper-layer intratelencephalic","deep-layer intratelencephalic","deep-layer near-projecting","deep-layer corticothalamic and 6b","MGE interneuron","CGE interneuron","LAMP5-LHX6 and Chandelier","astrocyte","oligodendrocyte","oligodendrocyte precursor cell","committed oligodendrocyte precursor","central nervous system macrophage","endothelial cell","pericyte","Bergmann glia"}
keeps = {"brain excitatory neurons","brain inhibitory neurons","other brain neurons","astrocytes","oligodendrocyte progenitor cells","oligodendrocytes","microglia","vascular endothelial cells","pericytes","hofbauer cells"}
with open(os.path.join(out, "hpa_snRNA_brain.tsv"), "w") as f:
    f.write("gene\tcluster_type\tnCPM\tinput_sha256\n"); s = sha(nuc)
    for r in rows(nuc):
        if r["Gene name"] in genes and r["Cluster type"] in keepn:
            f.write("\t".join([r["Gene name"], r["Cluster type"], r["nCPM"], s]) + "\n")
with open(os.path.join(out, "hpa_scRNA_celltype.tsv"), "w") as f:
    f.write("gene\tcell_type\tnCPM\tinput_sha256\n"); s = sha(sc)
    for r in rows(sc):
        if r["Gene name"] in genes and r["Cell type"] in keeps:
            f.write("\t".join([r["Gene name"], r["Cell type"], r["nCPM"], s]) + "\n")
with open(os.path.join(out, "hpa_ihc_brain.tsv"), "w") as f:
    f.write("gene\ttissue\tcell_type\tlevel\treliability\tinput_sha256\n"); s = sha(ihc)
    for r in rows(ihc):
        if r["Gene name"] in genes and r["Tissue"] in ("Cerebral cortex","Hippocampus"):
            f.write("\t".join([r["Gene name"], r["Tissue"], r["Cell type"], r["Level"], r["Reliability"], s]) + "\n")
