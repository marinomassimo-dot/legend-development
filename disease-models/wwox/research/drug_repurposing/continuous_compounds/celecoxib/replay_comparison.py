"""Reproduce separate exposure comparisons and held WWOX bulk RNA sensitivities."""

import argparse
import csv
import gzip
import hashlib
import sys
from pathlib import Path
from statistics import mean

import numpy as np

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent
sys.path.insert(0, str(RESEARCH / "ganaxolone_20261123"))
sys.path.insert(0, str(RESEARCH / "perampanel_kainate_20261123"))
from analyze import load_target, reference
from p47t_analysis import contrast

GENES = ("Ptgs2", "Ptgs1", "Ptges", "Ptger2")
DATASETS = (
    ("neuronal_cortex", "GSE158682", "CRTX_S_Ctrl_", "CRTX_S_KO_"),
    ("neuronal_hippocampus", "GSE158681", "S_Ctrl_", "S_KO_"),
    ("neural_hippocampus", "GSE158681", "N_Ctrl_", "N_KO_"),
    ("global_hippocampus", "GSE158681", "WT_", "KO_"),
    ("human_organoid", "GSE156243", "cwt", "cko"),
)
ADULT_REGIONS = ("PFC", "CTX", "HPC")
# Held ADV-231/233 activity-high animals selected before this gene comparison.
ADULT_ACTIVITY_HIGH = {"M6", "F8"}


def write_tsv(path, header, rows):
    with path.open("w", newline="") as stream:
        out = csv.writer(stream, delimiter="\t", lineterminator="\n")
        out.writerow(header)
        for row in rows:
            out.writerow(f"{value:.6f}" if isinstance(value, float) else value for value in row)


def exposure_comparisons():
    molecular_mass = 381.372  # NIST C169590425, g/mol
    to_nm = 1000 / molecular_mass
    adult_peak = 2.4  # Dembo Results, Fig. 2, ng/mL
    for measure, ng_ml in (
        ("adult_observed_pk_csf_peak_mean", adult_peak),
        ("adult_observed_pk_csf_peak_sd", 2.2),
        ("adult_observed_pk_free_plasma_peak_mean", 1.4),
        ("adult_observed_pk_csf_quantification_limit", 0.5),
        ("pediatric_model_wild_type_csf_steady_state_mean", 1.7),
        ("pediatric_model_cyp2c9star3_csf_steady_state_mean", 2.5),
        ("analgesia_fit_csf_ce50", 1.46),
    ):
        yield (measure, "nmol/L", ng_ml * to_nm)
    yield ("expressed_cox2_ic50_over_adult_mean_peak", "ratio", 15 / adult_peak)
    yield ("fibroblast_pge2_ic50_over_adult_mean_peak", "ratio", 91 / (adult_peak * to_nm))
    yield ("rat_slice_nominal_10uM_over_adult_mean_peak", "ratio", 10000 / (adult_peak * to_nm))
    yield ("rat_nonresponders_during_celecoxib_over_vehicle", "ratio", 6.46 / 7.68)
    yield ("rat_nonresponders_after_phenobarbital_over_celecoxib_period", "ratio", 2.20 / 6.46)


def verify(path, expected):
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if actual != expected[path.name]:
        raise ValueError(f"Unexpected source digest for {path.name}")


def juvenile_and_organoid(files, expected):
    verify(next((files / "reference_ensembl_r92").glob("*.fa.gz")), expected)
    gene_map, _ = reference(files)
    for model, accession, control, case in DATASETS:
        human = model == "human_organoid"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source = next((files / "geo" / accession).glob(pattern))
        verify(source, expected)
        genes = [gene.upper() if human else gene for gene in GENES]
        labels, counts = load_target(source, genes, None if human else gene_map)
        wt = [i for i, name in enumerate(labels) if name.startswith(control)]
        mutant = [i for i, name in enumerate(labels) if name.startswith(case)]
        assert min(len(wt), len(mutant)) >= 2
        for gene in genes:
            y = np.log2(1 + counts[gene])

            def change(omitted):
                return mean(y[i] for i in mutant if i != omitted) - mean(y[i] for i in wt if i != omitted)

            sensitivity = [change(i) for i in wt + mutant]
            yield (accession, model, gene, "CPM" if human else "TPM", len(wt), len(mutant),
                   change(None), min(sensitivity), max(sensitivity), "NA")


def adult_p47t(files, expected):
    source = files / "deepening_downloads/gse215425/GSE215425_processed_data.csv.gz"
    verify(source, expected)
    with gzip.open(source, "rt") as stream:
        rows = csv.reader(stream, delimiter="\t")
        labels = next(rows)[2:]
        totals = np.zeros(len(labels))
        counts = {gene: np.zeros(len(labels)) for gene in GENES}
        for _, name, *values in rows:
            v = np.array(values, int)
            totals += v
            if name in counts:
                counts[name] += v
    for region in ADULT_REGIONS:
        indices = [i for i, name in enumerate(labels) if name.startswith(f"{region}_")]
        groups = [(labels[i].split("_")[1].split("/")[0], labels[i].split("_")[2][0])
                  for i in indices]
        wt = sum(genotype == "WT" for genotype, _ in groups)
        mutant = sum(genotype == "P47T" for genotype, _ in groups)
        assert (wt, mutant) == (5, 5)
        retained = [j for j, i in enumerate(indices)
                    if labels[i].split("_")[2] not in ADULT_ACTIVITY_HIGH]
        assert len(retained) == 8
        for gene in GENES:
            y = np.log2(1 + 1e6 * counts[gene][indices] / totals[indices])
            estimate, _, _, omit_min, omit_max = contrast(y, groups)
            without_activity_high = mean(
                mean(y[j] for j in retained if groups[j] == ("P47T", sex))
                - mean(y[j] for j in retained if groups[j] == ("WT", sex))
                for sex in ("F", "M")
            )
            yield ("GSE215425", f"P47T_{region}", gene, "CPM", wt, mutant, estimate,
                   omit_min, omit_max, without_activity_high)


def main(files, out):
    input_manifest = RESEARCH / "memantine_magnesium_20261123" / "inputs.tsv"
    with input_manifest.open() as stream:
        expected = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    out.mkdir(parents=True, exist_ok=True)
    write_tsv(out / "exposure.tsv", ("comparison", "unit", "value"), exposure_comparisons())
    write_tsv(out / "bulk_rna.tsv",
              ("accession", "model", "gene", "input_unit", "n_WT", "n_mutant",
               "delta_log2_one_plus", "LOO_min", "LOO_max", "omit_held_activity_high"),
              (*juvenile_and_organoid(files, expected), *adult_p47t(files, expected)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_data_root", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    main(args.public_data_root, args.out)
