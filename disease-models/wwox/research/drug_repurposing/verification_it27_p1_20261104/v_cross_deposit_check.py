"""IT27 verifier: do the genes called in 4 of 4 deletion contrasts (GSE158681/2) move in P47T (GSE215425)? Direction check only, not a test.
Usage: python3 -I v_cross_deposit_check.py <p1b_genes_called_in_ge3_of_4...tsv> <p1a_all_regions_own_results.tsv.gz> <out.json> <pylib>"""
import sys, csv, json
sys.path.insert(0, sys.argv[4])
import pandas as pd, numpy as np
g = pd.read_csv(sys.argv[1], sep="\t"); g = g[(g.n_contrasts_called == 4) & (g.direction_consistency == "same")]
g["dir"] = g.iloc[:, 5].str[0].map({"+": 1, "-": -1}); g["sym"] = g.symbol
p = pd.read_csv(sys.argv[2], sep="\t")
out = {"n_convergent_4of4_same_dir": int(len(g)), "n_down": int((g.dir < 0).sum()), "n_up": int((g.dir > 0).sum())}
for reg in ["PFC", "CTX", "HPC", "CB"]:
    q = p[p.region == reg].drop_duplicates("symbol").set_index("symbol"); j = g.set_index("sym").join(q[["log2FoldChange", "padj"]], how="inner")
    j = j[~j.index.duplicated()]
    for d, nm in [(-1, "down_in_deletion"), (1, "up_in_deletion")]:
        s = j[j.dir == d]
        out[f"{reg}_{nm}"] = dict(n_found=int(len(s)), P47T_same_direction=int((np.sign(s.log2FoldChange) == d).sum()), same_dir_and_padj_lt10=int(((np.sign(s.log2FoldChange) == d) & (s.padj < .10)).sum()), median_lfc=float(s.log2FoldChange.median()) if len(s) else None)
mk = ["Mbp", "Plp1", "Mog", "Mobp", "Mag", "Cldn11", "Cnp", "Opalin", "Enpp6", "Fa2h", "Gal3st1", "Gjb1", "Gjc2", "Ugt8a"]
for reg in ["PFC", "CTX", "HPC", "CB"]:
    q = p[p.region == reg].drop_duplicates("symbol").set_index("symbol"); out[f"{reg}_myelin_lfc_padj"] = {s: [round(float(q.log2FoldChange[s]), 2), float(f"{q.padj[s]:.2g}")] for s in mk if s in q.index}
json.dump(out, open(sys.argv[3], "w"), indent=1); print(json.dumps(out, indent=1))
