"""Reproduce the contrasts defined in prediction.md using the GEO deposit tables."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path
import re

import numpy as np


PANELS = {
    "primary": ["CCNG2", "CDKN1B", "RBL2", "GADD45A"],
    "comparator": ["CDKN1A", "BCL2L11", "CAT", "SOD2", "EIF4EBP1"],
    "cycling": ["MKI67", "PCNA", "MCM2", "TOP2A"],
    "differentiation": ["DCX", "MAP2", "TUBB3", "RBFOX3"],
}
GENES = set().union(*PANELS.values())
DATA = {
    "GSE156243": "*count_table.txt.gz",
    "GSE126075": "*all_genes_all_samples_merged.txt.gz",
    "GSE158682": "*TPM_Table.txt.gz",
    "GSE158681": "*TPM_Table.txt.gz",
}
GROUPS = {
    "organoid": ("GSE156243", ["cko1", "cko2", "cko3", "cko4"], ["cwt1", "cwt2"]),
    "precursor": ("GSE126075", ["hNSC_WWOX_del"], ["hNSC"]),
    "differentiated": ("GSE126075", ["Neurons_WWOX_del"], ["Neurons"]),
    "cortex": ("GSE158682", [f"CRTX_S_KO_{i}" for i in range(1, 4)], [f"CRTX_S_Ctrl_{i}" for i in range(1, 5)]),
    "hippocampus": ("GSE158681", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"]),
}


def transcript_symbols(path):
    names = {}
    with gzip.open(path, "rt") as source:
        for line in source:
            if line.startswith(">"):
                match = re.search(r" gene_symbol:(\S+)", line)
                if match and match[1].upper() in GENES:
                    names[line[1:].split(".", 1)[0]] = match[1].upper()
    return names


def matrix(path, cohort, symbols):
    mouse = cohort in {"GSE158681", "GSE158682"}
    start = 3 if mouse else 1
    with gzip.open(path, "rt") as src:
        reader = csv.reader(src, delimiter="\t")
        samples = next(reader)[start:]
        totals = np.zeros(len(samples))
        rows = {}
        for row in reader:
            gene = symbols.get(row[0].split(".", 1)[0]) if mouse else row[0]
            if gene in GENES or cohort == "GSE156243":
                values = np.asarray(row[start:], dtype=float)
                if not np.all(np.isfinite(values)) or np.any(values < 0):
                    raise ValueError(f"Invalid values for {row[0]}")
                if cohort == "GSE156243":
                    totals += values
                if gene in GENES:
                    rows[gene] = rows.get(gene, 0) + values
    if cohort == "GSE156243":
        rows = {g: v * 1e6 / totals for g, v in rows.items()}
    return samples, rows


def effect(values, case, ctrl):
    return float(np.mean(values[case]) - np.mean(values[ctrl]))


def limits(values):
    return [min(values), max(values)] if values else ["NA", "NA"]


def write_tsv(path, header, rows):
    with path.open("w") as out:
        writer = csv.writer(out, delimiter="\t", lineterminator="\n")
        writer.writerow(header.split())
        for row in rows:
            writer.writerow(f"{v:.6f}" if isinstance(v, (float, np.floating)) else v for v in row)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True, parents=True)
    ref = args.files / "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz"
    files = {}
    for cohort, pattern in DATA.items():
        files[cohort], = (args.files / "geo" / cohort).glob(pattern)
    with (args.out / "inputs.sha256").open("w") as out:
        for path in [ref, *files.values()]:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            print(digest, path.relative_to(args.files), sep="  ", file=out)
    symbols = transcript_symbols(ref)
    matrices = {k: matrix(p, k, symbols) for k, p in files.items()}
    panels, genes, libraries, changes = [], [], [], {}
    for model, (cohort, cases, controls) in GROUPS.items():
        samples, expression = matrices[cohort]
        case, ctrl = [[samples.index(s) for s in group] for group in (cases, controls)]
        log_expr = {g: np.log2(1 + x) for g, x in expression.items()}
        scores = {}
        for name, members in PANELS.items():
            present = [g for g in members if g in log_expr]
            if len(present) >= len(members) - 1:
                scores[name] = np.mean([log_expr[g] for g in present], axis=0)
            for gene in members:
                if gene not in present:
                    genes.append([model, name, gene, "missing", "NA", "NA", "NA", "NA"])
                    continue
                x = expression[gene]
                genes.append([model, name, gene, "present", np.mean(x[case]), np.mean(x[ctrl]),
                              int(np.sum(x[case+ctrl] < 1)), effect(log_expr[gene], case, ctrl)])
        if "primary" in scores and "comparator" in scores:
            scores["primary_minus_comparator"] = scores["primary"] - scores["comparator"]
        for name in [*PANELS, "primary_minus_comparator"]:
            if name not in scores:
                panels.append([model, name, len(case), len(ctrl), *(["NA"] * 5)])
        for name, values in scores.items():
            changes[model, name] = effect(values, case, ctrl)
            loo = []
            if min(len(case), len(ctrl)) >= 2:
                for i in case + ctrl:
                    loo.append(effect(values, [j for j in case if i != j], [j for j in ctrl if i != j]))
            gene_loo = []
            if name in PANELS:
                present = [g for g in PANELS[name] if g in log_expr]
                for omitted in present:
                    score = np.mean([log_expr[g] for g in present if g != omitted], axis=0)
                    gene_loo.append(effect(score, case, ctrl))
            panels.append([model, name, len(case), len(ctrl), changes[model, name], *limits(loo), *limits(gene_loo)])
            for i in case + ctrl:
                libraries.append([model, samples[i], "WWOX_loss" if i in case else "control", name, values[i]])
    write_tsv(args.out / "panels.tsv", "model panel case_n control_n delta loo_library_min loo_library_max loo_gene_min loo_gene_max", panels)
    write_tsv(args.out / "genes.tsv", "model panel gene coverage case_mean control_mean libraries_below_1 delta_log2p1", genes)
    write_tsv(args.out / "libraries.tsv", "model library group panel score", libraries)
    write_tsv(args.out / "stage_interaction.tsv", "panel differentiated_delta_minus_precursor_delta",
              [(p, changes["differentiated", p] - changes["precursor", p]
                if ("differentiated", p) in changes and ("precursor", p) in changes else "NA")
               for p in [*PANELS, "primary_minus_comparator"]])


if __name__ == "__main__":
    main()
