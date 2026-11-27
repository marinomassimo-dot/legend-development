"""Replay iron-handling RNA contrasts and separate reported clinical endpoints."""

import argparse
import csv
import hashlib
import json
from pathlib import Path
from statistics import mean
import sys

import numpy as np

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent.parent
sys.path.insert(0, str(RESEARCH / "ganaxolone_20261123"))
from analyze import load_target, reference, tsv

TRIAL = "NCT01741532"
TRIAL_SHA256 = "c32110390204258dffcc346b19454322c1ecba65929face71f4a4bd16aae731d"
MODELS = (
    ("GSE158682", "juvenile_neuronal_cortex", "CRTX_S_Ctrl_", "CRTX_S_KO_", 4, 3),
    ("GSE158681", "juvenile_neuronal_hippocampus", "S_Ctrl_", "S_KO_", 2, 3),
    ("GSE158681", "juvenile_neural_hippocampus", "N_Ctrl_", "N_KO_", 2, 2),
    ("GSE158681", "juvenile_global_hippocampus", "WT_", "KO_", 3, 2),
    ("GSE156243", "human_cerebral_organoid", "cwt", "cko", 2, 4),
)
GENES = ("Wwox", "Tfrc", "Slc11a2", "Slc40a1", "Fth1", "Ftl1", "Ncoa4",
         "Fxn", "Aco2", "Mbp", "Gpx4", "Acsl4")


def verified(path, digest):
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError(f"Public input digest differs for {path.name}")
    return data


def bulk_rows(files, hashes):
    ensembl = next((files / "reference_ensembl_r92").glob("*.fa.gz"))
    verified(ensembl, hashes[ensembl.name])
    transcript_map, _ = reference(files)
    for accession, model, ctrl_prefix, ko_prefix, n_ctrl, n_ko in MODELS:
        human = accession == "GSE156243"
        pattern = "*count_table.txt.gz" if human else "*TPM_Table.txt.gz"
        source = next((files / "geo" / accession).glob(pattern))
        verified(source, hashes[source.name])
        symbols = [name.upper() for name in GENES] if human else list(GENES)
        if human:
            symbols[symbols.index("FTL1")] = "FTL"
        names, values = load_target(source, set(symbols), None if human else transcript_map)
        ctrl = [i for i, name in enumerate(names) if name.startswith(ctrl_prefix)]
        ko = [i for i, name in enumerate(names) if name.startswith(ko_prefix)]
        assert (len(ctrl), len(ko)) == (n_ctrl, n_ko)
        for symbol in symbols:
            expression = np.log2(1 + values[symbol])
            ctrl_mean, ko_mean = mean(expression[ctrl]), mean(expression[ko])
            omitted_ctrl = [mean(expression[j] for j in ctrl if j != i) for i in ctrl]
            omitted_ko = [mean(expression[j] for j in ko if j != i) for i in ko]
            bounds = [ko_mean - value for value in omitted_ctrl]
            bounds.extend(value - ctrl_mean for value in omitted_ko)
            yield (accession, model, symbol, "CPM" if human else "TPM", n_ctrl, n_ko,
                   *(f"{x:.6f}" for x in (ctrl_mean, ko_mean, ko_mean - ctrl_mean,
                                         min(bounds), max(bounds))))


def clinical(files):
    snapshot = files / "deepening_downloads" / "deferiprone_20261127" / f"{TRIAL}.json"
    study = json.loads(verified(snapshot, TRIAL_SHA256))
    assert study["protocolSection"]["identificationModule"]["nctId"] == TRIAL
    result = study["resultsSection"]
    flow = result["participantFlowModule"]
    assert [group["title"] for group in flow["groups"]] == ["Deferiprone", "Placebo"]
    milestones = {m["type"]: [(x["groupId"], int(x["numSubjects"])) for x in m["achievements"]]
                  for m in flow["periods"][0]["milestones"]}
    for key, expected in (("STARTED", [59, 30]), ("Exposed", [58, 30]),
                          ("Provided Post-baseline Efficacy Data", [58, 28]),
                          ("COMPLETED", [49, 27])):
        assert milestones[key] == list(zip(("FG000", "FG001"), expected))
    outcomes = result["outcomeMeasuresModule"]["outcomeMeasures"]
    wanted = ("Change in Score on Barry-Albright Dystonia Scale",
              "Score on Patient Global Impression of Improvement at End of Study",
              "Change in Level of Brain Iron")
    for outcome in wanted:
        m = next(m for m in outcomes if m["title"] == outcome)
        n = {x["groupId"]: int(x["value"]) for x in m["denoms"][0]["counts"]}
        estimates = m["classes"][0]["categories"][0]["measurements"]
        values = {x["groupId"]: float(x["value"]) for x in estimates}
        assert [x["title"] for x in m["groups"]] == ["Deferiprone", "Placebo"]
        a, b = "OG000", "OG001"
        yield (TRIAL, outcome, m["timeFrame"], n[a], n[b], values[a], values[b],
               f"{values[a] - values[b]:.2f}", m["unitOfMeasure"])
    # FAIRPARK-II, Figure 1 and Table 2. Use reported ITT estimates and group counts.
    yield ("NCT02655315", "Total MDS-UPDRS change (ITT)", "Baseline to week 36",
           186, 186, 15.6, 6.3, f"{15.6 - 6.3:.2f}", "scale points")
    yield ("NCT02655315", "Withdrawal for symptoms requiring dopaminergic therapy", "Week 36",
           186, 186, f"{100 * 41 / 186:.2f}", f"{100 * 5 / 186:.2f}",
           f"{100 * (41 - 5) / 186:.2f}", "percent (difference in percentage points)")

    # Ayton et al., Figure 1, Figure 2B and Table 2. Higher cognitive scores are better.
    yield ("NCT03234686", "NTB cognitive composite change (ITT)", "Baseline to month 12",
           53, 28, -0.80, -0.30, f"{-0.80 - (-0.30):.2f}", "standardized scale points")
    yield ("NCT03234686", "Hippocampal QSM change (completed MRI)", "Baseline to month 12",
           18, 15, -0.36, 0.32, f"{-0.36 - 0.32:.2f}", "ppb")


def main(files, out):
    manifest = RESEARCH / "memantine_magnesium_20261123" / "inputs.tsv"
    with manifest.open() as stream:
        hashes = {row["input"]: row["sha256"] for row in csv.DictReader(stream, delimiter="\t")}
    out.mkdir(parents=True, exist_ok=True)
    tsv(out / "bulk_iron_handling.tsv",
        ("accession", "model", "gene", "input_unit", "n_WT", "n_KO",
         "WT_mean_log2_one_plus", "KO_mean_log2_one_plus", "delta_KO_minus_WT", "LOO_min", "LOO_max"),
        bulk_rows(files, hashes))
    tsv(out / "clinical_endpoints.tsv",
        ("trial", "endpoint", "time", "n_deferiprone", "n_placebo", "deferiprone",
         "placebo", "difference_DFP_minus_placebo", "units"), clinical(files))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("public_data_root", type=Path)
    parser.add_argument("--out", type=Path, default=HERE)
    args = parser.parse_args()
    main(args.public_data_root, args.out)
