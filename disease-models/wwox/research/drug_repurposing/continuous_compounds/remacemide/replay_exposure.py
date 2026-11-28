"""Replay adult total-plasma scale and enantiomer selection scenarios."""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    with (HERE / "exposure_inputs.tsv").open() as source:
        values = {x["key"]: float(x["value"]) for x in csv.DictReader(source, delimiter="\t")}

    print("measure\tcondition\tvalue\tunit")

    def emit(measure, condition, value, unit):
        print(f"{measure}\t{condition}\t{value:.6g}\t{unit}")

    for background in ("cbz", "pht", "vpa", "vpa_completer"):
        peak = values[f"{background}_dgr_cmax"]
        for basis in ("base", "hcl"):
            total = peak / values[f"dgr_{basis}_mw"]
            name = f"{background} {basis} mass basis"
            emit("total_DGR_plasma_Cmax", name, total, "uM")
            emit("slice_nominal_to_total_plasma", name, values["dgr_slice_nominal"] / total, "ratio")
            emit("S_NMDA_nominal_IC50_to_total_plasma", name, values["dgr_s_nmda_ic50"] / total, "ratio")
            if background != "vpa_completer":
                total_parent = values[f"{background}_parent_cmax"] / values[f"parent_{basis}_mw"]
                emit("total_parent_plasma_Cmax", name, total_parent, "uM")

    nmda_r_s = values["dgr_r_nmda_ic50"] / values["dgr_s_nmda_ic50"]
    firing_s_r = values["dgr_s_firing_ic50"] / values["dgr_r_firing_ic50"]
    emit("nominal_NMDA_IC50_R_over_S", "cultured rat hippocampal voltage clamp", nmda_r_s, "ratio")
    emit("nominal_firing_IC50_S_over_R", "adult rat CA1 sustained repetitive firing", firing_s_r, "ratio")
    emit("nominal_NMDA_exposure_index_S_over_R", "illustrative matched firing index",
         nmda_r_s * firing_s_r, "ratio")
    emit("DGR_AUC_with_over_without_phenobarbital", "healthy adult comparison",
         values["dgr_auc_with_inducer"] / values["dgr_auc_without_inducer"], "ratio")


if __name__ == "__main__":
    main()
