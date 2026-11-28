"""Replay adult exposure benchmarks and descriptive WWOX nucleus coverage."""

import argparse
import csv
import hashlib
from pathlib import Path
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent
sys.path.insert(0, str(RESEARCH / "ganaxolone_20261123"))
from analyze import assigned_nuclei, tsv

MOLAR_MASS = 230.31  # g/mol, PubChem CID 3671
MAX_FREE_FRACTION = 0.05  # Sanftner et al., human binding >=95%
GENES = ("Pde4b", "Pde4d", "Mif", "Cd74", "Cd44", "Cxcr2", "Cxcr4", "Tlr4",
         "Il1b", "Il6", "Tnf", "Il10", "C1qa", "Ccl2", "P2ry12")
CLASSES = ("exc", "inh", "astro", "microglia", "OPC", "NFOL", "MFOL")


def plasma():
    # Rolan et al., Table 2 geometric means. This converts aggregate values.
    samples = (("day_1_peak", 14, 32.0),
               ("day_6_peak", 10, 59.9),
               ("day_6_trough", 10, 27.5),
               ("day_16_peak", 10, 59.9),
               ("day_16_trough", 10, 22.1))
    for time, n, total_mass in samples:
        total_nm = 1000 * total_mass / MOLAR_MASS
        yield (time, n, total_mass, f"{total_nm:.3f}", MAX_FREE_FRACTION,
               f"{total_nm * MAX_FREE_FRACTION:.3f}")


def compare_assays():
    # Cho et al., Figs. 1A and 2A. Takuma et al., primary abstract.
    value_and_context = (
        ("MIF-stimulated PBMC migration", "significant at nominal 10 nM", 10),
        ("MIF tautomerase", "K_i", 30_900),
        ("MIF fluorescence binding", "K_d", 55_100),
        ("H2O2-challenged rat astrocyte viability", "lowest reported effective nominal level", 10_000),
    )
    ceiling = 1000 * 59.9 / MOLAR_MASS * MAX_FREE_FRACTION
    for endpoint, parameter, nm in value_and_context:
        yield (endpoint, parameter, nm, f"{ceiling:.3f}", f"{nm / ceiling:.3f}")


def sample_coverage(files):
    manifest = RESEARCH / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as stream:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    folder = files / "geo" / "GSE158684"
    for arm in ("ctrl", "ko"):
        for suffix in ("features.tsv.gz", "matrix.mtx.gz"):
            path = folder / f"GSE158684_{arm}_filtered_{suffix}"
            if hashlib.sha256(path.read_bytes()).hexdigest() != hashes[path.name]:
                raise ValueError(f"Public input digest differs for {path.name}")
    for arm, cell_class, depth, counts in assigned_nuclei(files, [], [], GENES):
        if cell_class not in CLASSES:
            continue
        umi = int(depth.sum())
        for gene in GENES:
            if gene not in counts:
                yield arm, cell_class, len(depth), umi, gene, "unmapped", "", "", ""
                continue
            total = int(counts[gene].sum())
            detected = int(np.count_nonzero(counts[gene]))
            yield (arm, cell_class, len(depth), umi, gene, "mapped", total, detected,
                   f"{1e6 * total / umi:.3f}")


def main(files, out):
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "plasma_exposure.tsv",
        ("time", "n", "total_ng_ml", "total_nM", "assumed_max_free_fraction",
         "estimated_unbound_upper_nM"), plasma())
    tsv(out / "assay_concentration_scales.tsv",
        ("endpoint", "parameter", "assay_nM", "estimated_adult_unbound_plasma_peak_upper_nM",
         "assay_to_plasma_upper_ratio"), compare_assays())
    tsv(out / "pooled_nuclei_target_coverage.tsv",
        ("condition_pool", "assigned_class", "n_nuclei", "total_UMI", "gene", "mapping",
         "gene_UMI", "detected_nuclei", "gene_CPM"), sample_coverage(files))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_data_root", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    main(args.public_data_root, args.out)
