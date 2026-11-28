"""Replay matched RNA contrasts, recombinant affinity and selected source arithmetic."""
import argparse
import csv
from pathlib import Path
import sys

import numpy as np


def write_source_comparisons(output):
    receptor_source = "Busnelli 2013 Table 1, native ligand and recombinant mouse receptors"
    macaque_source = "Lee 2020 Table 1, reported tissue mass and Methods extracellular-volume scenario"
    pws_source = "Tauber 2026 OTBB3 week-4 Results; active minus placebo, descriptive"
    fxs_source = "Chavez 2026 preprint Results and Fig. 2B,E, early treatment"
    rows = []
    for receptor, ki_nm in (("OXTR", 0.83), ("AVPR1A", 20.38), ("AVPR1B", 36.32)):
        rows.append((f"{receptor} Ki", f"{ki_nm:.2f}", "nM", receptor_source))
        for concentration in (1, 10, 100):
            fraction = concentration / (concentration + ki_nm)
            rows.append((f"{receptor} at {concentration} nM",
                         f"{100 * fraction:.3f}", "%, one-site scenario with Ki used as Kd",
                         receptor_source))
    density_g_ml = 1.05
    mw = 1012
    for organ, pg_mg in (("Orbitofrontal cortex", 2.04), ("Striatum", 2.41)):
        mass_density_nm = 1000 * pg_mg * density_g_ml / mw
        rows.append((f"{organ} whole-tissue equivalent", f"{mass_density_nm:.3f}", "nM", macaque_source))
        for ecf in (0.15, 0.20, 0.25):
            rows.append((f"{organ} if all analyte assigned to {ecf:.0%} extracellular volume",
                         f"{mass_density_nm / ecf:.3f}", "nM, scenario", macaque_source))
    rows.extend([
        ("Infant NOMAS responder difference", f"{100 * (5 / 26 - 5 / 26):.2f}",
         "percentage points", pws_source),
        ("Infant VFSS selected-subscore responder difference",
         f"{100 * (8 / 15 - 2 / 12):.2f}", "percentage points", pws_source),
        ("Infant paired-VFSS any improvement difference",
         f"{100 * (11 / 18 - 5 / 20):.2f}", "percentage points", pws_source),
    ])
    for sex, control, exposed in (("Male", 2.40, 0.57), ("Female", 0.78, 0.74)):
        rows.append((f"{sex} Fmr1-KO severity score change", f"{exposed - control:.2f}",
                     "ordinal score points, descriptive", fxs_source))
    with output.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(("comparison", "value", "unit", "basis"))
        writer.writerows(rows)


def write_chloride_balance(drug_repurposing, files, output):
    shared = drug_repurposing / "continuous_compounds" / "creatine"
    sys.path.insert(0, str(shared))
    from assess import MODELS, load_target, reference, tsv

    # replay_expression.py verifies these same held inputs against the original manifest first.
    transcripts, _ = reference(files)
    rows = []
    for model, accession, control_prefix, ko_prefix in MODELS:
        human = model == "human_organoid"
        genes = ("SLC12A5", "SLC12A2") if human else ("Slc12a5", "Slc12a2")
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source, = (files / "geo" / accession).glob(pattern)
        names, panel = load_target(source, genes, None if human else transcripts)
        control = np.array([i for i, name in enumerate(names) if name.startswith(control_prefix)])
        ko = np.array([i for i, name in enumerate(names) if name.startswith(ko_prefix)])
        balance = np.log2(1 + panel[genes[0]]) - np.log2(1 + panel[genes[1]])
        difference = balance[ko].mean() - balance[control].mean()
        omitted = [
            balance[ko[ko != i]].mean() - balance[control[control != i]].mean()
            for i in np.r_[control, ko]
        ]
        rows.append((model, accession, len(control), len(ko), f"{difference:.5f}",
                     f"{min(omitted):.5f}", f"{max(omitted):.5f}"))
    tsv(output, "model accession control_n ko_n delta_log2_balance omit_min omit_max".split(), rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("drug_repurposing", type=Path)
    parser.add_argument("files", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    write_chloride_balance(args.drug_repurposing, args.files, args.output / "chloride_balance.tsv")
    write_source_comparisons(args.output / "source_comparisons.tsv")


if __name__ == "__main__":
    main()
