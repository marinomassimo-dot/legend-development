"""Compare nominal probenecid assay scales and held WWOX purine RNA contrasts."""

import argparse
import csv
import hashlib
import json
from math import log2
from pathlib import Path
from statistics import mean
import sys

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent
sys.path.insert(0, str(RESEARCH / "ganaxolone_20261123"))
from analyze import assigned_nuclei, load_target, reference, tsv

MOLAR_MASS = 285.36
TRIAL_SHA256 = "18d7e00a4a666b5052303c2209b9ba25583c3c4a41f872a9330d981c5fcf822c"
MODELS = (
    ("GSE158682", "juvenile_neuronal_cortex", "CRTX_S_Ctrl_", "CRTX_S_KO_", 4, 3),
    ("GSE158681", "juvenile_neuronal_hippocampus", "S_Ctrl_", "S_KO_", 2, 3),
    ("GSE158681", "juvenile_neural_hippocampus", "N_Ctrl_", "N_KO_", 2, 2),
    ("GSE158681", "juvenile_global_hippocampus", "WT_", "KO_", 3, 2),
    ("GSE156243", "human_cerebral_organoid", "cwt", "cko", 2, 4),
)
GENES = ("Panx1", "Entpd1", "Nt5e", "Adora1", "P2ry1", "P2rx7", "Slc29a1", "Slc29a2",
         "Slc22a6", "Slc22a8", "Abcc4", "Wwox")


def verified(path, digest):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError(f"Public input digest differs for {path.name}")
    return data


def bulk(files, hashes):
    ensembl = next((files / "reference_ensembl_r92").glob("*.fa.gz"))
    verified(ensembl, hashes[ensembl.name])
    transcript_map, _ = reference(files)
    for accession, model, ctrl_prefix, ko_prefix, n_ctrl, n_ko in MODELS:
        human = accession == "GSE156243"
        unit = "CPM" if human else "TPM"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source = next((files / "geo" / accession).glob(pattern))
        verified(source, hashes[source.name])
        symbols = [name.upper() for name in GENES] if human else GENES
        names, values = load_target(source, set(symbols), None if human else transcript_map)
        ctrl = [i for i, name in enumerate(names) if name.startswith(ctrl_prefix)]
        ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
        assert (len(ctrl), len(ko)) == (n_ctrl, n_ko)
        for symbol in symbols:
            if symbol not in values:
                yield accession, model, symbol, unit, n_ctrl, n_ko, "unmapped", "NA", "NA", "NA", "NA", "NA"
                continue
            expression = [log2(1 + value) for value in values[symbol]]
            wt, mutant = (mean(expression[i] for i in arm) for arm in (ctrl, ko))
            bounds = [mutant - mean(expression[i] for i in ctrl if i != drop) for drop in ctrl]
            bounds.extend(mean(expression[i] for i in ko if i != drop) - wt for drop in ko)
            yield (accession, model, symbol, unit, n_ctrl, n_ko, "mapped",
                   *(f"{x:.6f}" for x in (wt, mutant, mutant - wt, min(bounds), max(bounds))))


def lineage_rows(files, hashes):
    symbols = ("Panx1", "Adora1", "Nt5e", "P2ry1", "P2rx7")
    folder = files / "geo" / "GSE158684"
    for arm in ("ctrl", "ko"):
        for suffix in ("features.tsv.gz", "matrix.mtx.gz"):
            path = folder / f"GSE158684_{arm}_filtered_{suffix}"
            verified(path, hashes[path.name])
    selected_classes = ("exc", "inh", "astro", "microglia")
    for arm, cell_class, depth, counts in assigned_nuclei(files, [], [], symbols):
        if cell_class in selected_classes:
            umi = int(depth.sum())
            for gene in symbols:
                if gene not in counts:
                    yield arm, cell_class, len(depth), umi, gene, "NA", "NA", "NA"
                    continue
                molecules = int(counts[gene].sum())
                detected = int((counts[gene] > 0).sum())
                yield arm, cell_class, len(depth), umi, gene, molecules, detected, f"{1e6 * molecules / umi:.6f}"


def exposure_rows():
    # Clark Fig. 3B and Results. Rat parent data are from Nagata p. 1042.
    for h, csf, serum, reported_pair_pct in ((24, 5.4, 75.4, 7.33), (48, 6.2, 75.1, 7.64), (72, 4.6, 52.9, 10.16)):
        ratio = 100 * csf / serum
        yield ("Clark_TBI_Pro_NAC", h, "CSF", "measured_total", 7, csf, f"{1000 * csf / MOLAR_MASS:.3f}",
               f"{ratio:.3f}", reported_pair_pct)
        yield ("Clark_TBI_Pro_NAC", h, "serum", "measured_total", 7, serum, f"{1000 * serum / MOLAR_MASS:.3f}",
               "NA", "NA")
    yield ("Nagata_rat_infusion", 3, "CSF", "measured_total", "NA", "NA", "57.300", "NA", "NA")
    yield ("Nagata_rat_infusion", 3, "plasma", "measured_unbound", "NA", "NA", "154.000", "NA", "NA")


def assay_rows():
    references = (
        ("Silverman_Fig2", "pannexin-1 oocyte current", "IC50", 150),
        ("Ma_Fig5_Table1", "pannexin-1 recombinant whole-cell current", "IC50", 350),
        ("Bhaskaracharya_Fig2", "human P2X7 dye uptake stimulated with 200 uM ATP", "IC50", 203),
        ("Bhaskaracharya_Fig2", "human P2X7 dye uptake stimulated with 1000 uM ATP", "IC50", 1300),
        ("Lopatar_Fig4", "rat hippocampal ATP and burst suppression", "nominal bath", 1000),
    )
    peak = 1000 * 6.2 / MOLAR_MASS
    for source, endpoint, parameter, value in references:
        yield source, endpoint, parameter, value, f"{peak:.3f}", f"{value / peak:.3f}", f"{value / 57.3:.3f}"


def trial_row(files):
    source = files / "deepening_downloads" / "probenecid_20261127" / "NCT07318870.json"
    trial = json.loads(verified(source, TRIAL_SHA256))
    section = trial["protocolSection"]
    outcomes = section["outcomesModule"]["primaryOutcomes"]
    assert len(outcomes) == 1
    a = section["eligibilityModule"]
    status = section["statusModule"]
    design = section["designModule"]
    yield (section["identificationModule"]["nctId"], status["lastUpdatePostDateStruct"]["date"],
           status["overallStatus"], a["minimumAge"], a["maximumAge"], design["designInfo"]["allocation"],
           design["enrollmentInfo"]["count"], design["enrollmentInfo"]["type"],
           outcomes[0]["description"], str(trial["hasResults"]).lower())


def main(files, out):
    manifest = RESEARCH / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as stream:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "bulk_purine_pathway.tsv",
        ("accession", "model", "gene", "input_unit", "n_WT", "n_KO", "coverage",
         "WT_mean_log2_one_plus", "KO_mean_log2_one_plus", "delta_KO_minus_WT", "LOO_min", "LOO_max"),
        bulk(files, hashes))
    tsv(out / "pooled_purine_coverage.tsv",
        ("condition_pool", "assigned_class", "n_nuclei", "total_UMI", "gene",
         "gene_UMI", "detected_nuclei", "gene_CPM"), lineage_rows(files, hashes))
    tsv(out / "exposure.tsv", ("source", "time_h", "matrix", "statistic", "n",
                              "parent_ug_ml", "parent_uM", "ratio_of_group_means_pct",
                              "study_reported_concurrent_CSF_serum_pct"), exposure_rows())
    tsv(out / "assay_scales.tsv", ("source", "endpoint", "parameter", "assay_uM",
                                  "Clark_48h_total_CSF_uM", "assay_to_Clark_CSF_ratio",
                                  "assay_to_Nagata_rat_CSF_ratio"), assay_rows())
    tsv(out / "clinical_registry.tsv", ("NCT", "last_posted", "recruitment_state", "min_age",
                                      "max_age", "allocation", "enrollment_n", "enrollment_kind",
                                      "primary_outcome_description", "has_results"), trial_row(files))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_data_root", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    main(args.public_data_root, args.out)
