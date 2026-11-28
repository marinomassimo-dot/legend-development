"""Transfer a prespecified myelin-challenge contrast to Wwox mouse expression profiles."""
import argparse
import csv
import gzip
import re
from pathlib import Path

import numpy as np


def tsv(path, header, rows):
    with path.open("w") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def reference(files):
    gene_for_transcript = {}
    sex_genes = {"Xist", "Tsix"}
    with gzip.open(next((files/"reference_ensembl_r92").glob("*.fa.gz")), "rt") as source:
        for line in source:
            if line.startswith(">"):
                match = re.search(r"gene_symbol:(\S+)", line)
                if match:
                    gene = match[1]
                    gene_for_transcript[line[1:].split(".")[0]] = gene
                    if re.search(r"chromosome:GRCm38:[XY]:", line):
                        sex_genes.add(gene)
    return gene_for_transcript, sex_genes


def source_matrix(path, excluded):
    genes = {}
    with gzip.open(path, "rt") as source:
        rows = csv.reader(source, delimiter="\t")
        samples = next(rows)[3:]
        for _, name, biotype, *values in rows:
            if (biotype == "protein_coding" and name not in excluded
                    and not re.match(r"^(mt-|Mrp[ls]|Rp[ls]\d|Rplp\d)", name, re.I)):
                genes[name] = genes.get(name, 0) + np.array(values, float)
    return samples, genes


def contrast_indices(samples, group, baseline):
    treated = [i for i, s in enumerate(samples) if s.startswith(group)]
    controls = [i for i, s in enumerate(samples) if s.startswith(baseline)]
    assert treated and controls
    return treated, controls


def train(samples, genes):
    case, ctrl = contrast_indices(samples, "E3_M_plus_", "E3_M_minus_")
    effects = {}
    for g, v in genes.items():
        if v[case + ctrl].mean() >= 1:
            y = np.log2(v + 1)
            effects[g] = y[case].mean() - y[ctrl].mean()
    up = sorted((g for g in effects if effects[g] >= .5), key=lambda g: (-effects[g], g))[:25]
    down = sorted((g for g in effects if effects[g] <= -.5), key=lambda g: (effects[g], g))[:25]
    assert up and down
    return up, down, effects


def load_target(path, wanted, transcript_map=None):
    counts = {}
    with gzip.open(path, "rt") as stream:
        rows = csv.reader(stream, delimiter="\t")
        offset = 3 if transcript_map is not None else 1
        samples = next(rows)[offset:]
        library = np.zeros(len(samples))
        for row in rows:
            g = transcript_map.get(row[0].split(".")[0]) if transcript_map is not None else row[0]
            if transcript_map is None:
                library += np.array(row[offset:], float)
            if g in wanted:
                counts[g] = counts.get(g, 0) + np.array(row[offset:], float)
    if transcript_map is None:
        counts = {g: 1e6 * v / library for g, v in counts.items()}
    return samples, counts


def score(log_expr, up, down):
    arms = [[g for g in group if g in log_expr] for group in [up, down]]
    avg = [np.mean([log_expr[g] for g in arm], axis=0) for arm in arms]
    return avg[0] - avg[1], [len(arm) for arm in arms]


def add_contrast(label, samples, expr, case, ctrl, up, down, rows, per_sample):
    values, sizes = score({g: np.log2(v + 1) for g, v in expr.items() if g in up or g in down}, up, down)
    a, b = contrast_indices(samples, case, ctrl)
    def effect(omit):
        return values[[i for i in a if i != omit]].mean() - values[[i for i in b if i != omit]].mean()
    loo = [effect(i) for i in a+b]
    rows.append([label, *sizes, len(a), len(b), effect(None), min(loo), max(loo)])
    per_sample.extend([label, samples[i], "case" if i in a else "control", values[i]] for i in a+b)


def assigned_nuclei(files, up, down, extra=(), *, exclude_markers=()):
    # The same marker assignment and 500-UMI filter as the LEGEND A2 classifier.
    markers = ["Slc17a7 Camk2a Satb2","Gad1 Gad2 Slc32a1","Aqp4 Aldh1l1 Slc1a2","Cx3cr1 P2ry12 Csf1r",
               "Pdgfra Cspg4 Cspg5 Pcdh15","Gpr17 Neu4 Bmp4 Vcan","Tcf7l2 Itpr2 Enpp6 Bcas1 Tmem2 Fyn Casr",
               "Mal Mog Opalin Serinc5 Mag","Klk6 Apod Pmp22 Slc5a11 Ermn Hapln2"]
    marker_sets = [
        [gene for gene in group.split() if gene not in exclude_markers]
        for group in markers
    ]
    if not all(marker_sets):
        raise ValueError("Each cell class must retain at least one marker")
    wanted = set(up + down + [gene for group in marker_sets for gene in group]) | set(extra)
    arms = []
    for arm in ["ctrl", "ko"]:
        prefix = str(files/f"geo/GSE158684/GSE158684_{arm}_filtered_")
        with gzip.open(prefix+"features.tsv.gz","rt") as f:
            indices = {i: row.split("\t")[1] for i,row in enumerate(f,1) if row.split("\t")[1] in wanted}
        with gzip.open(prefix+"matrix.mtx.gz","rt") as f:
            dims = next(row for row in f if not row.startswith("%"))
            n = int(dims.split()[1])
            matrix = np.fromstring(f.read(),dtype=np.int64,sep=" ").reshape(-1,3)
        library = np.bincount(matrix[:,1]-1,weights=matrix[:,2],minlength=n)
        keep = library>=500
        genes = {}
        selected = matrix[np.isin(matrix[:,0], list(indices))]
        for i,g in indices.items():
            items = selected[selected[:,0]==i]
            counts = np.bincount(items[:,1]-1,weights=items[:,2],minlength=n)[keep]
            genes[g] = genes.get(g,0) + counts
        log_expr = {g:np.log2(1+v*1e6/library[keep]) for g,v in genes.items()}
        classes = np.column_stack([np.mean([log_expr[g] for g in group],axis=0) for group in marker_sets])
        arms.append((arm, classes, genes, library[keep]))
    scale = np.percentile(np.concatenate([classes for _,classes,_,_ in arms]),99,axis=0)
    for arm, classes, genes, library in arms:
        norm = classes / scale
        names = ["exc","inh","astro","microglia","OPC","COP","NFOL","MFOL","MOL"]
        for i,name in enumerate(names):
            sel = (norm.argmax(1)==i) & (norm.max(1)>=.2)
            assert sel.any()
            yield arm, name, library[sel], {g:v[sel] for g,v in genes.items()}


def microglia(files, up, down):
    for arm, name, library, genes in assigned_nuclei(files, up, down):
        total = library.sum()
        summed = {g:int(v.sum()) for g,v in genes.items()}
        pseudo = {g:np.log2(1+v*1e6/total) for g,v in summed.items()}
        value, sizes = score(pseudo, up, down)
        yield arm, name, len(library), int(total), sizes, value, summed



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files",type=Path)
    parser.add_argument("training_matrix",type=Path)
    parser.add_argument("out",type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True,parents=True)
    tx, sex = reference(args.files)
    sample, expr = source_matrix(args.training_matrix, sex | set("Mbp Plp1 Mobp Mag Mog Cnp".split()))
    up,down,effects = train(sample,expr)
    tsv(args.out/"signature.tsv",["gene","direction","training_delta"],[[g,d,effects[g]] for d,arm in [("up",up),("down",down)] for g in arm])
    rows, indiv = [], []
    for genotype in ("E3","E4","WT"):
        add_contrast(genotype, sample,expr,genotype+"_M_plus_",genotype+"_M_minus_",up,down,rows,indiv)
    for geo,case,ctrl in [("GSE158682","CRTX_S_KO_","CRTX_S_Ctrl_"),("GSE158681","S_KO_","S_Ctrl_")]:
        p, = (args.files/"geo"/geo).glob("*TPM_Table.txt.gz")
        add_contrast(geo,*load_target(p,set(up+down),tx),case,ctrl,up,down,rows,indiv)
    p = args.files/"deepening_downloads/gse319769/counts_fixed.tsv.gz"
    add_contrast("GSE319769_day14",*load_target(p,set(up+down)),"iaka14_","iasl14_",up,down,rows,indiv)
    tsv(args.out/"contrasts.tsv","context up_mapped down_mapped cases controls difference loo_min loo_max".split(),rows)
    tsv(args.out/"samples.tsv","context sample group score".split(),indiv)
    profiles = list(microglia(args.files,up,down))
    tsv(args.out/"microglia.tsv","pool assigned_nuclei up_mapped down_mapped pseudobulk_score".split(),
        [[arm,n,*sizes,v] for arm,c,n,tot,sizes,v,summed in profiles if c=="microglia"])
    # Post hoc: cell classes, dropout/low-count sensitivity and leave-one-gene-out.
    checks = []
    for c in sorted({p[1] for p in profiles}):
        ctrl,ko = [p for p in profiles if p[1]==c]
        delta = {g:np.log2(1+ko[6][g]*1e6/ko[3])-np.log2(1+ctrl[6][g]*1e6/ctrl[3])
                 for g in up+down if g in ctrl[6] and g in ko[6]}
        strong = {g:v for g,v in delta.items() if min(ctrl[6][g],ko[6][g]) >= 10}
        if set(up)&strong.keys() and set(down)&strong.keys():
            robust, kept = score(strong,up,down)
        else:
            robust, kept = "NA",[len(set(up)&strong.keys()),len(set(down)&strong.keys())]
        loo = [score({k:v for k,v in delta.items() if k!=g},up,down)[0] for g in delta]
        checks.append([c,ctrl[2],ko[2],ctrl[3],ko[3],ko[5]-ctrl[5],min(loo),max(loo),*kept,robust])
    tsv(args.out/"cell_sensitivity.tsv",
        "class ctrl_n ko_n ctrl_umi ko_umi delta loo_gene_min loo_gene_max retained_up retained_down delta_min10".split(),checks)

    mg = [p for p in profiles if p[1] == "microglia"]
    genes = sorted((set(up+down) & mg[0][6].keys()) & mg[1][6].keys())
    depth = min(p[3] for p in mg)
    rng = np.random.default_rng(20261123)
    draws = []
    for _,_,_,total,_,_,summed in mg:
        counts = [summed[g] for g in genes]
        counts.append(total - sum(counts))
        subsampled = rng.multivariate_hypergeometric(counts, depth, size=250)
        logged = np.log2(1 + 1e6*subsampled/depth)
        draws.append(np.array([score(dict(zip(genes,row)),up,down)[0] for row in logged]))
    change = draws[1] - draws[0]
    tsv(args.out/"microglia_depth.tsv",["matched_umi","draws","delta_min","delta_median","delta_max"],
        [[depth,len(change),change.min(),np.median(change),change.max()]])



if __name__ == "__main__":
    main()
