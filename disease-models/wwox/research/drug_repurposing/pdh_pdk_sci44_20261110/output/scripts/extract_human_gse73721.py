"""Extract gene rows from the GSE73721 human and mouse table (Zhang 2016) and group columns by cell class. usage: python3 -I extract_human_gse73721.py <csv.gz> <out_tsv>
No network. Reads local files given as arguments.
"""
import sys
if "--help" in sys.argv or "-h" in sys.argv:
    print(__doc__)
    sys.exit(0)
import sys, gzip, csv, hashlib
src, out = sys.argv[1:3]
sha = hashlib.sha256(open(src, "rb").read()).hexdigest()
genes = ["PDK1","PDK2","PDK3","PDK4","PDP1","PDP2","PDHA1","PDHB","DLAT","PDHX","PDPR","LDHA","MPC1","MPC2","GFAP","SNAP25","STMN2","SLC17A7","GAD1","MBP","AIF1","CX3CR1","CLDN5","PECAM1","PDGFRA","PPARGC1A"]
rd = csv.reader(gzip.open(src, "rt", encoding="latin1"))
hdr = next(rd)
groups = {}
for i, h in enumerate(hdr[1:], start=1):
    h2 = h.strip()
    if h2.endswith("tumor periphery astro") or "tumor core astro" in h2: g = "astro_tumor"
    elif "Hippocampus astro" in h2: g = "astro_hippocampus_epilepsy_region"
    elif h2.startswith("Fetal"): g = "astro_fetal_ctx"
    elif "ctx" in h2 and h2.endswith("astro"): g = "astro_mature_ctx"
    elif h2.endswith("neuron"): g = "neuron_ctx"
    elif h2.endswith("oligo"): g = "oligo_ctx"
    elif h2.endswith("myeloid"): g = "myeloid_ctx"
    elif h2.endswith("endo"): g = "endo_ctx"
    elif "whole cortex" in h2: g = "whole_cortex"
    elif h2.startswith("Mouse"): g = "mouse_astro"
    else: g = "other"
    groups.setdefault(g, []).append((i, h2))
with open(out, "w") as f:
    f.write("gene\tgroup\tn_columns\tmean_fpkm\tvalues\tcolumn_labels\tinput_sha256\n")
    for r in rd:
        if r[0].upper() in genes:
            for g, cols in groups.items():
                vals = [float(r[i]) for i, _ in cols]
                f.write("\t".join([r[0].upper(), g, str(len(vals)), "%.2f" % (sum(vals)/len(vals)), ";".join(str(v) for v in vals), ";".join(h for _, h in cols), sha]) + "\n")
print({g: len(c) for g, c in groups.items()})
