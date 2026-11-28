"""Replay exposure benchmarks for hypothetical direct acrolein capture."""
import csv
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def capture_fraction(rate, auc_molar_seconds):
    return -math.expm1(-rate * auc_molar_seconds)


def main():
    with (HERE / "exposure_inputs.tsv").open() as table:
        inputs = {row["key"]: float(row["value"]) for row in csv.DictReader(table, delimiter="\t")}

    anserine = inputs["anserine_acrolein_rate"]
    carnosine = inputs["carnosine_acrolein_rate"]
    gsh_rate = inputs["gsh_acrolein_rate"]
    csf_parent = inputs["csf_dual_detection_mean"] * 1e-9
    print("measure\tcondition\tvalue\tunit")

    def emit(measure, condition, value, unit):
        print(f"{measure}\t{condition}\t{value:.8g}\t{unit}")

    for arm in ("low", "middle", "high"):
        auc = inputs[f"pure_auc_{arm}"]
        emit("no_competitor_capture", f"adult plasma mean AUC {arm} arm",
             100 * capture_fraction(anserine, auc * 60e-6), "percent")
    emit("required_intact_auc", "10 percent capture of pre-existing trace acrolein",
         -math.log(0.9) / anserine / 0.0036, "uM h")
    emit("break_even_auc_ratio", "anserine versus carnosine in same compartment",
         carnosine / anserine, "ratio")
    emit("matched_serum_rate_ratio", "anserine versus carnosine at 50 uM",
         inputs["anserine_serum_hydrolysis_rate"] / inputs["carnosine_serum_hydrolysis_rate"], "ratio")
    emit("no_competitor_capture", "one hour at baseline CSF paired-detection mean",
         100 * capture_fraction(anserine, csf_parent * 3600), "percent")

    for factor in (1.0, 0.1):
        # The GSH concentration and the reduced rate are sensitivity scenarios.
        gsh_clearance = gsh_rate * factor * 1e-6
        parent_clearance = anserine * csf_parent
        emit("two_sink_first_capture_share", f"CSF parent mean and 1 uM GSH, GSH rate x{factor:g}",
             100 * parent_clearance / (parent_clearance + gsh_clearance), "percent")


if __name__ == "__main__":
    main()
