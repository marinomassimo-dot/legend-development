"""Replay chemical-species exposure comparisons and juvenile WWOX bulk RNA."""

import argparse
import csv
from hashlib import sha256
from pathlib import Path
from statistics import mean
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent
sys.path.insert(0, str(RESEARCH / "ganaxolone_20261123"))
from analyze import load_target, reference

GENES = ("Rhoa", "Rock1", "Rock2", "Ppp1r12a", "Myl9", "Myl12a", "Adgrg1")
MODELS = (
    ("GSE158682", "neuronal_cortex", "CRTX_S_Ctrl_", "CRTX_S_KO_", 4, 3),
    ("GSE158681", "neuronal_hippocampus", "S_Ctrl_", "S_KO_", 2, 3),
    ("GSE158681", "neural_hippocampus", "N_Ctrl_", "N_KO_", 2, 2),
    ("GSE158681", "global_hippocampus", "WT_", "KO_", 3, 2),
    ("GSE156243", "human_organoid", "cwt", "cko", 2, 4),
)


def exposure():
    # Koch et al. Results p. 1141; hydroxyfasudil mass from PubChem CID 3064778.
    for arm, csf, sd in (("lower_exposure_arm", 5.8, 2.0), ("higher_exposure_arm", 9.4, 4.5)):
        mean_nm = csf * 1000 / 307.37
        yield arm, "adult_day26_hydroxyfasudil_csf_mean", "nM", mean_nm
        yield arm, "adult_day26_hydroxyfasudil_csf_sd", "nM", sd * 1000 / 307.37
        # Rikitake et al. Results, molecule-matched enzyme benchmarks.
        yield arm, "hydroxyfasudil_ROCK1_ic50_over_csf_mean", "ratio", 730 / mean_nm
        yield arm, "hydroxyfasudil_ROCK2_ic50_over_csf_mean", "ratio", 720 / mean_nm
    # Syed et al. 5 µM O4 response and Pedraza et al. 100 µM pMYPT1 assay.
    # Compare nominal parent concentrations only with parent enzyme values.
    for assay, nominal in (("parent_opc_O4", 5), ("parent_mNphOPC_pMYPT1", 100)):
        yield assay, "parent_ROCK1_ic50_scale", "ratio", nominal / 1.2
        yield assay, "parent_ROCK2_ic50_scale", "ratio", nominal / 0.82


def verify(path, expected):
    if sha256(path.read_bytes()).hexdigest() != expected[path.name]:
        raise ValueError(f"Public input hash differs for {path.name}")


def abundance(files, expected):
    verify(next((files / "reference_ensembl_r92").glob("*.fa.gz")), expected)
    gene_map, _ = reference(files)
    for geo, model, normal, deletion, n_normal, n_deletion in MODELS:
        human = geo == "GSE156243"
        name = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        path = next((files / "geo" / geo).glob(name))
        verify(path, expected)
        genes = [gene.upper() if human else gene for gene in GENES]
        labels, raw = load_target(path, genes, None if human else gene_map)
        normal_indices = [i for i, name in enumerate(labels) if name.startswith(normal)]
        deletion_indices = [i for i, name in enumerate(labels) if name.startswith(deletion)]
        assert (len(normal_indices), len(deletion_indices)) == (n_normal, n_deletion)
        for gene in genes:
            y = np.log2(1 + raw[gene])

            def delta(omitted):
                return (mean(y[i] for i in deletion_indices if i != omitted)
                        - mean(y[i] for i in normal_indices if i != omitted))

            sensitivities = [delta(i) for i in normal_indices + deletion_indices]
            yield (geo, model, gene, "CPM" if human else "TPM", n_normal, n_deletion,
                   delta(None), min(sensitivities), max(sensitivities))


def tsv(path, header, rows):
    with path.open("w", newline="") as f:
        writer = csv.writer(f, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        for row in rows:
            writer.writerow(f"{x:.6f}" if isinstance(x, float) else x for x in row)


def main(files, out):
    with (RESEARCH / "memantine_magnesium_20261123" / "inputs.tsv").open() as f:
        hashes = {r["input"]: r["sha256"] for r in csv.DictReader(f, delimiter="\t")}
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "exposure.tsv", ("arm_or_assay", "comparison", "unit", "value"), exposure())
    tsv(out / "wwox_bulk_rock.tsv", ("accession", "model", "gene", "input_unit", "n_WT", "n_KO",
                                    "delta_log2_one_plus", "LOO_min", "LOO_max"),
        abundance(files, hashes))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_data_root", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    opts = parser.parse_args()
    main(opts.public_data_root, opts.out)
