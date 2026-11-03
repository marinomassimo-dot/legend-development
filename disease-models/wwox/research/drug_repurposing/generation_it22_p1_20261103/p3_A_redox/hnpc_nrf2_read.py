#!/usr/bin/env python3
"""IT22 P3-A: descriptive read of NRF2-axis genes in the GSE126075 CAGE gene matrix (H9-derived hNSC and neurons, control vs WWOX-deleted; ONE library per arm).
Usage: python3 -I hnpc_nrf2_read.py <path to GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz>
Prints raw TPM, the uncentred KD/control ratio and a log2 ratio centred on the median log2 ratio of genes with TPM >= 1 in both arms.
The centring here is an approximation written for this package; it is NOT the module's derive_gene_values.py R_centred. n = 1 per arm: no test, no p value."""
import sys, gzip, csv, math, statistics as st
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
rows = list(csv.reader(gzip.open(sys.argv[1], "rt"), delimiter="\t"))
assert rows[0] == ["Gene", "hNSC", "Neurons", "hNSC_WWOX_del", "Neurons_WWOX_del"], rows[0]
d = {r[0]: [float(x) for x in r[1:]] for r in rows[1:]}
print("genes in matrix:", len(d))
med = {}
for name, (a, b) in {"hNSC": (0, 2), "Neurons": (1, 3)}.items():
    lr = [math.log2(v[b] / v[a]) for v in d.values() if v[a] >= 1 and v[b] >= 1]
    med[name] = st.median(lr); print(f"{name}: {len(lr)} genes with TPM>=1 in both arms, median log2 ratio {med[name]:.3f}")
print("gene\tTPM hNSC, Neurons, hNSC_del, Neurons_del\thNSC ratio\thNSC log2 centred\tNeurons ratio\tNeurons log2 centred")
for g in "NFE2L2 KEAP1 NQO1 HMOX1 G6PD SLC7A11 GCLM GCLC SRXN1 TXNRD1 GSR FTH1 FTL WWOX".split():
    v = d.get(g)
    if not v: print(g, "absent from the matrix"); continue
    out = []
    for name, (a, b) in {"hNSC": (0, 2), "Neurons": (1, 3)}.items():
        if v[a] > 0 and v[b] > 0:
            r = math.log2(v[b] / v[a]); out += ["%.2f" % (v[b] / v[a]), "%+.2f" % (r - med[name])]
        else: out += ["na", "na"]
    print(g + "\t" + ", ".join("%.2f" % x for x in v) + "\t" + "\t".join(out))
