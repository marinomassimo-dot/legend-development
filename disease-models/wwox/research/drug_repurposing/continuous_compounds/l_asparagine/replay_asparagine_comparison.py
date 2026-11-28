"""Replay stage-separated WWOX asparagine-pathway expression and exposure checks."""

import argparse
import csv
import gzip
import hashlib
from math import log2
from pathlib import Path
from statistics import mean
import sys

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent
sys.path.insert(0, str(RESEARCH / "ganaxolone_20261123"))
from analyze import assigned_nuclei, load_target, reference, tsv

CAGE_SHA256 = "7e51e3cffa7491a7778a23516fd6e8bbe601b62cb5223536885a401219a392c2"
MODELS = (
    ("GSE158682", "juvenile_neuronal_cortex", "CRTX_S_Ctrl_", "CRTX_S_KO_", 4, 3),
    ("GSE158681", "juvenile_neuronal_hippocampus", "S_Ctrl_", "S_KO_", 2, 3),
    ("GSE158681", "juvenile_neural_hippocampus", "N_Ctrl_", "N_KO_", 2, 2),
    ("GSE158681", "juvenile_global_hippocampus", "WT_", "KO_", 3, 2),
    ("GSE156243", "human_cerebral_organoid", "cwt", "cko", 2, 4),
)
GENES = ("Asns", "Nars", "Pc", "Got1", "Got2", "Glul", "Gls", "Slc1a3", "Slc1a5", "Slc38a2",
         "Slc7a5", "Slc7a8", "Eif2ak4", "Eif2ak1", "Atf4", "Wwox")


def verify(path, digest):
    if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
        raise ValueError(f"Public input digest differs for {path.name}")


def bulk_rows(files, hashes):
    ensembl = next((files / "reference_ensembl_r92").glob("*.fa.gz"))
    verify(ensembl, hashes[ensembl.name])
    transcripts, _ = reference(files)
    for accession, model, ctrl_prefix, ko_prefix, n_ctrl, n_ko in MODELS:
        human = accession == "GSE156243"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source = next((files / "geo" / accession).glob(pattern))
        verify(source, hashes[source.name])
        symbols = [name.upper() for name in GENES] if human else [
            "Pcx" if name == "Pc" else name for name in GENES
        ]
        names, values = load_target(source, set(symbols), None if human else transcripts)
        ctrl = [i for i, name in enumerate(names) if name.startswith(ctrl_prefix)]
        ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
        assert (len(ctrl), len(ko)) == (n_ctrl, n_ko)
        for symbol in symbols:
            if symbol not in values:
                yield accession, model, symbol, "CPM" if human else "TPM", n_ctrl, n_ko, "unmapped", "NA", "NA", "NA", "NA", "NA"
                continue
            expression = [log2(1 + value) for value in values[symbol]]
            mean_ctrl = mean(expression[i] for i in ctrl)
            mean_ko = mean(expression[i] for i in ko)
            bounds = [mean_ko - mean(expression[i] for i in ctrl if i != drop) for drop in ctrl]
            bounds.extend(mean(expression[i] for i in ko if i != drop) - mean_ctrl for drop in ko)
            yield (accession, model, symbol, "CPM" if human else "TPM", n_ctrl, n_ko, "mapped",
                   *(f"{val:.6f}" for val in (mean_ctrl, mean_ko, mean_ko - mean_ctrl, min(bounds), max(bounds))))


def cage_rows(files):
    source = files / "geo" / "GSE126075" / "GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz"
    verify(source, CAGE_SHA256)
    wanted = {name.upper() for name in GENES}
    with gzip.open(source, "rt") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        relevant = {row["Gene"]: row for row in reader if row["Gene"] in wanted}
    designs = (("hNSC", "hNSC_WWOX_del"), ("Neurons", "Neurons_WWOX_del"))
    for control, knockdown in designs:
        for symbol in sorted(wanted):
            row = relevant.get(symbol)
            if row is None:
                yield control, symbol, 1, 1, "unmapped", "NA", "NA", "NA"
                continue
            wt, kd = float(row[control]), float(row[knockdown])
            yield control, symbol, 1, 1, "mapped", f"{wt:.6f}", f"{kd:.6f}", f"{log2(1 + kd) - log2(1 + wt):.6f}"


def lineage_coverage(files, hashes):
    symbols = ("Pcx", "Asns", "Got2", "Nars")
    folder = files / "geo" / "GSE158684"
    for arm in ("ctrl", "ko"):
        for suffix in ("features.tsv.gz", "matrix.mtx.gz"):
            path = folder / f"GSE158684_{arm}_filtered_{suffix}"
            verify(path, hashes[path.name])
    for arm, cell_class, depth, counts in assigned_nuclei(files, [], [], symbols):
        if cell_class in ("exc", "inh", "astro"):
            umi = int(depth.sum())
            for gene in symbols:
                molecules = int(counts[gene].sum())
                detected = int((counts[gene] > 0).sum())
                yield arm, cell_class, len(depth), umi, gene, molecules, detected, f"{1e6 * molecules / umi:.6f}"


def exposure_checks():
    for month, value in ((0, 3.0), (6, 5.3), (12, 4.4), (18, 3.5)):
        yield ("Sprute_2019", "serum", f"month_{month}", f"{value:.3f}", "reported in one of two cases")
    yield ("Sprute_2019", "CSF", "baseline", "2.910", "post-exposure CSF unavailable")
    yield ("Cui_2026", "RPE_and_cancer_cell_medium", "added", "100.000", "nominal bath increment")
    for form, mass in (("anhydrous", 132.12), ("monohydrate", 150.13)):
        yield ("NARS1_2026", "HEK293T_medium", f"added_if_{form}", f"{200_000 / mass:.3f}",
               "200 mg/L converted with stated hydration assumption")


def main(files, out):
    with (RESEARCH / "memantine_magnesium_20261123" / "inputs.tsv").open() as stream:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "bulk_synthesis_and_charging.tsv",
        ("accession", "model", "gene", "input_unit", "n_WT", "n_KO", "coverage",
         "WT_mean_log2_one_plus", "KO_mean_log2_one_plus", "delta_KO_minus_WT", "LOO_min", "LOO_max"),
        bulk_rows(files, hashes))
    tsv(out / "cage_stage_sensitivity.tsv",
        ("stage", "gene", "n_control", "n_knockdown", "coverage", "control_TPM",
         "knockdown_TPM", "delta_log2_one_plus"), cage_rows(files))

    tsv(out / "hippocampal_lineage_coverage.tsv",
        ("condition_pool", "assigned_class", "n_nuclei", "total_UMI", "gene",
         "gene_UMI", "detected_nuclei", "gene_CPM"), lineage_coverage(files, hashes))

    tsv(out / "reported_exposure_scales.tsv",
        ("source", "matrix", "measure", "asparagine_uM", "interpretation"),
        exposure_checks())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_data_root", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    main(args.public_data_root, args.out)
