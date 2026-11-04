"""IT27 verifier: compare my P1a results with the producer's tables (run AFTER my own tables existed).
Usage: python3 -I v_compare_with_producer.py <my p1a_all_regions_own_results.tsv.gz> <producer p47t_all_regions_tested_genes.tsv.gz> <out.json>"""
import sys, json, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0, sys.argv[4]) if len(sys.argv) > 4 else None
import numpy as np, pandas as pd
from scipy import stats
mine = pd.read_csv(sys.argv[1], sep="\t"); prod = pd.read_csv(sys.argv[2], sep="\t")
out = {}
for reg in ["PFC", "CTX", "HPC", "CB"]:
    m = mine[mine.region == reg].set_index("ensembl"); p = prod[prod.region == reg].set_index("ensembl_id")
    j = m.join(p, how="inner", rsuffix="_prod"); S = dict(n_mine=len(m), n_prod=len(p), n_shared=len(j))
    S["spearman_lfc_deseq_vs_prod_centred"] = float(stats.spearmanr(j.log2FoldChange, j.log2FC_centred).correlation)
    S["spearman_lfc_myols_vs_prod"] = float(stats.spearmanr(j.ols_lfc, j.log2FC_centred).correlation)
    S["spearman_p_myols_vs_prod"] = float(stats.spearmanr(j.ols_p, j.p).correlation)
    S["slope_prod_on_deseq"] = float(np.polyfit(j.log2FoldChange - j.log2FoldChange.median(), j.log2FC_centred, 1)[0])
    pc = set(j.index[j.FDR_with_sex < .10]); dc = set(j.index[j.padj < .10]); oc = set(j.index[j.ols_fdr < .10])
    S["FDR10"] = dict(prod=len(pc), deseq2=len(dc), my_ols=len(oc), prod_and_deseq2=len(pc & dc), prod_and_myols=len(pc & oc),
                      prod_only_not_deseq2=len(pc - dc), deseq2_only_not_prod=len(dc - pc),
                      prod_calls_with_same_sign_in_deseq2_when_both=int(sum(np.sign(j.log2FoldChange[g]) == np.sign(j.log2FC_centred[g]) for g in pc & dc)))
    ps = set(j.index[(j.FDR_with_sex < .05) & (j.log2FC_centred.abs() >= 1)]); ds = set(j.index[(j.padj < .05) & (j.log2FoldChange.abs() >= 1)])
    S["FDR05_2x"] = dict(prod=len(ps), deseq2=len(ds), both=len(ps & ds), prod_calls_deseq2_padj_lt10=int(sum(j.padj[g] < .10 for g in ps)))
    # producer's genes not tested by producer but tested by me (low expression), and called by DESeq2
    extra = m.index.difference(p.index); S["tested_by_me_not_producer"] = int(len(extra)); S["of_which_deseq2_padj10"] = int((m.loc[extra, "padj"] < .10).sum())
    # producer 'tested' definition vs mine: mean normalised count of genes only in mine
    out[reg] = S
json.dump(out, open(sys.argv[3], "w"), indent=1); print(json.dumps(out, indent=1))
