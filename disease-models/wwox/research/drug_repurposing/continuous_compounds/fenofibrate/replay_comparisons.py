"""Compare reported concentrations and replay aggregate counts from published tables."""
import argparse
import csv
import hashlib
from pathlib import Path
import re
import subprocess


HERE = Path(__file__).resolve().parent
CLINICAL_PDF_SHA = "40b4ac2b1310e6aa838212cc19c94cae58f3977178459dc192110c05019777a8"


def published_totals(pdf):
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != CLINICAL_PDF_SHA:
        raise ValueError("Published clinical PDF has a different digest")
    raw = subprocess.check_output(["pdftotext", "-layout", str(pdf), "-"], text=True)
    diary_text = raw.split("Table 1. Effect of add-on fenofibrate treatment", 1)[1]
    diary_text = diary_text.split("Wilcoxon test", 1)[0]
    overnight = raw.split("Table 2. Effect of add-on fenofibrate treatment", 1)[1]
    overnight = overnight.split("Wilcoxon test", 1)[0]
    pattern = r"^\s*\d+/(?:AD)?NFLE\s+[MF]\s+(\d+)\s+(.+)$"
    diary = re.findall(pattern, diary_text, flags=re.M)
    recorded = re.findall(pattern, overnight, flags=re.M)
    assert len(diary) == len(recorded) == 11
    changes = [re.match(r"^\d+\s+\(\s*([^()]+)\)", row) for _, row in diary]
    count100 = sum(bool(item and re.fullmatch(r"[^\d]*100(?:\.0+)?", item.group(1)))
                   for item in changes)
    yield "Table1_diary_count_with_printed_percentage", sum(bool(x) for x in changes)
    yield "Table1_diary_count_printed_100_percent_reduction", count100
    ages = [int(age) for age, _ in recorded]
    yield "Table2_age_min_years", min(ages)
    yield "Table2_age_max_years", max(ages)
    counts = [list(map(int, row.split())) for _, row in recorded]
    assert all(len(row) == 6 for row in counts)
    for i, event in enumerate(("total", "major", "minor")):
        yield f"Table2_{event}_before_count", sum(row[2*i] for row in counts)
        yield f"Table2_{event}_after_count", sum(row[2*i+1] for row in counts)
        yield f"Table2_{event}_zero_after", sum(row[2*i+1] == 0 for row in counts)
    for offset, time in enumerate(("before", "after")):
        yield f"Table2_component_sum_mismatches_{time}", sum(
            row[offset] != row[2+offset] + row[4+offset] for row in counts)
    yield "Table2_any_event_after_n", sum(any(row[i] for i in (1,3,5)) for row in counts)


def chemistry(values):
    mw = values["acid_molecular_mass_g_mol"][1]
    benchmark = values["acid_PPAR_alpha_EC50_uM"][1]
    for day in (1, 8):
        brain = values[f"brain_acid_ug_g_day{day}"][1]
        plasma = values[f"plasma_acid_ug_mL_day{day}"][1]
        liver = values[f"liver_acid_ug_g_day{day}"][1]
        yield f"day{day}_brain_total_nmol_g", brain * 1000 / mw
        yield f"day{day}_plasma_total_uM", plasma * 1000 / mw
        yield f"day{day}_liver_total_nmol_g", liver * 1000 / mw
        yield f"day{day}_brain_plasma_total_mL_g", brain/plasma
        yield f"day{day}_plasma_volume_matching_brain_total_uL_g", 1000*brain/plasma
        yield f"day{day}_brain_total_vs_nominal_alpha_EC50_if_1g_per_mL", brain*1000/(mw*benchmark)
    for event in ("nicotine_spike_wave", "nicotine_severe_behavior"):
        ctrl, feno = values[event+"_events"]
        n_ctrl, n_feno = values[event+"_animals"]
        yield f"{event}_risk_change_percentage_points", 100*(feno/n_feno-ctrl/n_ctrl)
        yield f"{event}_risk_ratio", (feno/n_feno)/(ctrl/n_ctrl)
    ctrl, feno = values["frontal_OEA_pmol_g"]
    yield "frontal_OEA_case_over_control", feno/ctrl


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("published_pdf", type=Path)
    args = parser.parse_args()
    with (HERE / "source_inputs.tsv").open() as handle:
        rows = csv.DictReader(handle, delimiter="\t")
        values = {r["measure"]: [float(r[k]) if r[k] != "NA" else None
                                for k in ("control", "case")] for r in rows}
    print("measure\tvalue")
    for label, value in [*chemistry(values), *published_totals(args.published_pdf)]:
        print(f"{label}\t{value:.8g}")
