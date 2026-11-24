"""Per-library developmental GABRA3/GABRA1 comparison. Supply the laboratory files directory."""
import csv
import sys
from pathlib import Path
from statistics import mean

import numpy as np

here = Path(__file__).resolve().parent
repurposing = here.parents[1]
sys.path.insert(0, str(here.parent / "creatine"))
from assess import MODELS, load_target, reference

sys.path.insert(0, str(repurposing / "advisor_pilot_20261113" / "brainstorm_20261116" /
                      "expression_timecourse_adv088_sci_20261119"))
from mouse_timecourse import read_rows

files = Path(sys.argv[1])
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("accession", "group_or_KO_minus_WT", "n", "alpha3_mean_or_delta", "alpha1_mean_or_delta",
                 "pseudocount", "mean_log2_ratio_or_delta", "min_leave_one", "max_leave_one"))

def emit(accession, label, alpha3, alpha1, cases, controls=()):
    for pseudocount in (0.1, 1):
        ratio = np.log2((np.array(alpha3) + pseudocount) / (np.array(alpha1) + pseudocount))
        def estimate(values, omit=None):
            average = mean(float(values[i]) for i in cases if i != omit)
            if controls:
                average -= mean(float(values[i]) for i in controls if i != omit)
            return average
        omissions = [estimate(ratio, i) for i in (*cases, *controls)]
        writer.writerow((accession, label, len(cases)+len(controls), f"{estimate(alpha3):.4f}",
                         f"{estimate(alpha1):.4f}", pseudocount, f"{estimate(ratio):.4f}",
                         f"{min(omissions):.4f}", f"{max(omissions):.4f}"))

alpha3_id, alpha1_id = "ENSMUSG00000031343", "ENSMUSG00000010803"
names, rows = read_rows(files / "geo/E-MTAB-6798_mouse_timecourse/Mouse.RPKM.txt", {alpha3_id, alpha1_id})
for day in sorted({int(name.split(".")[1][1:]) for name in names}):
    cases = [i for i, name in enumerate(names) if name.split(".")[1] == f"P{day}"]
    emit("E-MTAB-6798", f"WT_P{day}", rows[alpha3_id], rows[alpha1_id], cases)

transcript_map, _ = reference(files)
for model, accession, wt_prefix, ko_prefix in MODELS:
    human = model == "human_organoid"
    genes = ("GABRA3", "GABRA1") if human else ("Gabra3", "Gabra1")
    source, = (files / "geo" / accession).glob("*count_table.txt.gz" if human else "*TPM_Table.txt.gz")
    names, rows = load_target(source, genes, None if human else transcript_map)
    cases = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
    controls = [i for i, name in enumerate(names) if name.startswith(wt_prefix)]
    emit(accession, model, rows[genes[0]], rows[genes[1]], cases, controls)
