"""Screen held WWOX profiles for matrix transcripts and PV-lineage context."""

import argparse
import csv
from math import log2
from pathlib import Path
from statistics import mean
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("files", type=Path)
args = parser.parse_args()
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "creatine"))
from assess import MODELS, load_target, reference

genes = (
    "Mmp9", "Mmp2", "Timp1", "Timp2", "Acan", "Bcan", "Hapln1", "Tnr",
    "Pvalb", "Gad1", "Gad2", "Slc32a1",
)
gene_map, _ = reference(args.files)
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("model", "gene", "wt_n", "ko_n", "wt_present", "ko_present", "wt_mean",
                 "ko_mean", "mean_log2_difference", "loo_min", "loo_max"))
for model, accession, wt_prefix, ko_prefix in MODELS:
    human = model == "human_organoid"
    species_genes = [gene.upper() if human else gene for gene in genes]
    source, = (args.files / "geo" / accession).glob("*count_table.txt.gz" if human else "*TPM_Table.txt.gz")
    names, measured = load_target(source, species_genes, None if human else gene_map)
    wild = [i for i, name in enumerate(names) if name.startswith(wt_prefix)]
    knockout = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
    for gene in species_genes:
        if gene not in measured:
            writer.writerow((model, gene.upper(), len(wild), len(knockout), *("NA",) * 7))
            continue
        wt, ko = ([float(measured[gene][i]) for i in group] for group in (wild, knockout))
        wt_log, ko_log = ([log2(1 + x) for x in group] for group in (wt, ko))
        delta = mean(ko_log) - mean(wt_log)
        omissions = [
            *(mean(ko_log) - mean(wt_log[:i] + wt_log[i+1:]) for i in range(len(wt_log))),
            *(mean(ko_log[:i] + ko_log[i+1:]) - mean(wt_log) for i in range(len(ko_log))),
        ]
        vals = (mean(wt), mean(ko), delta, min(omissions), max(omissions))
        writer.writerow((model, gene.upper(), len(wt), len(ko), sum(v > 0 for v in wt),
                         sum(v > 0 for v in ko), *(f"{v:.5g}" for v in vals)))
