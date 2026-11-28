"""Compare copper handling RNA and complex IV subunit RNA in held WWOX matrices."""

import argparse
import csv
import hashlib
from pathlib import Path
from statistics import mean
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent
sys.path.insert(0, str(RESEARCH / "ganaxolone_20261123"))
from analyze import assigned_nuclei, load_target, reference

MODELS = (
    ("GSE158682", "juvenile_neuronal_cortex", "CRTX_S_Ctrl_", "CRTX_S_KO_", 4, 3),
    ("GSE158681", "juvenile_neuronal_hippocampus", "S_Ctrl_", "S_KO_", 2, 3),
    ("GSE158681", "juvenile_neural_hippocampus", "N_Ctrl_", "N_KO_", 2, 2),
    ("GSE158681", "juvenile_global_hippocampus", "WT_", "KO_", 3, 2),
    ("GSE156243", "human_cerebral_organoid", "cwt", "cko", 2, 4),
)
DELIVERY = ("Cox17", "Sco1", "Sco2", "Coa6", "Cox11")
STRUCTURAL = ("Cox4i1", "Cox5a", "Cox5b")
GENES = ("Wwox", "Slc31a1", "Atp7a", "Atp7b", *DELIVERY, *STRUCTURAL)
SCORE = "delivery_minus_structural_mean_log"


def verify(path, hashes):
    if hashlib.sha256(path.read_bytes()).hexdigest() != hashes[path.name]:
        raise ValueError(f"Public input digest differs for {path.name}")


def pathways(files, hashes):
    verify(next((files / "reference_ensembl_r92").glob("*.fa.gz")), hashes)
    transcript_map, _ = reference(files)
    for accession, model, control_prefix, case_prefix, n_control, n_case in MODELS:
        human = accession == "GSE156243"
        source_name = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source = next((files / "geo" / accession).glob(source_name))
        verify(source, hashes)
        symbols = {name: name.upper() if human else name for name in GENES}
        inputs, g = load_target(source, symbols.values(), None if human else transcript_map)
        control = [i for i, label in enumerate(inputs) if label.startswith(control_prefix)]
        case = [i for i, label in enumerate(inputs) if label.startswith(case_prefix)]
        assert (len(control), len(case)) == (n_control, n_case)
        arrays = {name: np.log2(1 + g[symbol]) for name, symbol in symbols.items()}
        delivery_score = np.mean([arrays[name] for name in DELIVERY], axis=0)
        structural_score = np.mean([arrays[name] for name in STRUCTURAL], axis=0)
        arrays[SCORE] = delivery_score - structural_score
        symbols[SCORE] = SCORE
        for measure, y in arrays.items():
            def difference(omit):
                return mean(y[i] for i in case if i != omit) - mean(y[i] for i in control if i != omit)

            omitted = [difference(i) for i in control + case]
            yield (accession, model, symbols[measure], "CPM" if human else "TPM", n_control, n_case,
                   difference(None), min(omitted), max(omitted))


def nuclei(files, hashes):
    prefix = files / "geo" / "GSE158684"
    for arm in ("ctrl", "ko"):
        for suffix in ("features.tsv.gz", "matrix.mtx.gz"):
            verify(prefix / f"GSE158684_{arm}_filtered_{suffix}", hashes)
    rows = []
    for arm, cell_class, depth, counts in assigned_nuclei(files, [], [], ["Slc31a1"]):
        umi = int(depth.sum())
        target = int(counts["Slc31a1"].sum())
        rows.append((arm, cell_class, len(depth), umi, target, 1e6 * target / umi))
    rates = {(row[0], row[1]): (row[2], row[3], row[5]) for row in rows}
    classes = sorted({row[1] for row in rows})
    common_classes = [cell for cell in classes
                      if min(rates[arm, cell][0] for arm in ("ctrl", "ko")) >= 100]
    contrasts = [(group, measure, value)
                 for group, keep in (("all_assigned", classes), ("min_100_nuclei", common_classes))
                 for measure, value in decompose(rates, keep)]
    return rows, contrasts


def decompose(rates, classes):
    totals = {arm: sum(rates[arm, cell][1] for cell in classes) for arm in ("ctrl", "ko")}
    wt_weights = np.array([rates["ctrl", cell][1] / totals["ctrl"] for cell in classes])
    ko_weights = np.array([rates["ko", cell][1] / totals["ko"] for cell in classes])
    wt_rates = np.array([rates["ctrl", cell][2] for cell in classes])
    ko_rates = np.array([rates["ko", cell][2] for cell in classes])
    raw = float(ko_weights @ ko_rates - wt_weights @ wt_rates)
    within = float((ko_rates - wt_rates) @ ((ko_weights + wt_weights) / 2))
    class_mix = float((ko_weights - wt_weights) @ ((ko_rates + wt_rates) / 2))
    assert abs(raw - within - class_mix) < 1e-10
    return (
        ("control_observed", float(wt_weights @ wt_rates)),
        ("knockout_observed", float(ko_weights @ ko_rates)),
        ("knockout_minus_control", raw),
        ("within_assigned_class", within),
        ("assigned_class_composition", class_mix),
    )


def write_rows(path, header, rows):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        for row in rows:
            writer.writerow(f"{v:.6f}" if isinstance(v, float) else v for v in row)


def survival():
    # FDA ZYCUBO Drug Trials Snapshot, Tables 2 and 3. Data-cutoff status.
    for comparison, n_exposed, alive_exposed, n_external, alive_external, overlap, hr, low, high in (
        ("early", 31, 16, 17, 2, 16, 0.22, 0.10, 0.49),
        ("late", 35, 12, 16, 2, 16, 0.27, 0.12, 0.57),
    ):
        yield (comparison, n_exposed, alive_exposed, alive_exposed / n_exposed, n_external,
               alive_external, alive_external / n_external, overlap, hr, low, high)


def main(files, out):
    manifest = RESEARCH / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as stream:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    out.mkdir(parents=True, exist_ok=True)
    write_rows(out / "bulk_delivery.tsv",
               ("accession", "model", "measure", "input_unit", "n_WT", "n_KO",
                "delta_log2_one_plus", "LOO_min", "LOO_max"),
               pathways(files, hashes))
    write_rows(out / "menkes_comparators.tsv",
               ("comparison", "treated_n", "treated_alive_n", "treated_alive_fraction",
                "external_n", "external_alive_n", "external_alive_fraction",
                "external_n_shared_between_comparisons", "reported_HR", "reported_CI_low", "reported_CI_high"),
               survival())

    composition, decomposition = nuclei(files, hashes)
    write_rows(out / "nuclei_slc31a1.tsv",
               ("condition_pool", "assigned_class", "n_nuclei", "total_UMI", "Slc31a1_UMI", "Slc31a1_CPM"),
               composition)
    write_rows(out / "nuclei_decomposition.tsv", ("subset", "assigned_class_contrast", "Slc31a1_CPM"),
               decomposition)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_data_root", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    main(args.public_data_root, args.out)
