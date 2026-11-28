"""Recreate felodipine contrasts from Siddiqi's deposited workbook and source anchors."""
import argparse
import csv
import hashlib
from pathlib import Path, PurePosixPath
from statistics import mean
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
WORKBOOK_SHA256 = "cd28955f0a0bc5b4f1c906f56ffddf4ebc67fbcae1764dbe62d864f2baa01887"


def worksheet(archive, name):
    links = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    targets = {entry.get("Id"): entry.get("Target") for entry in links}
    book = ET.fromstring(archive.read("xl/workbook.xml"))
    sheet, = [node for node in book.findall(".//{*}sheet") if node.get("name") == name]
    key = next(value for attribute, value in sheet.attrib.items() if attribute.endswith("}id"))
    path = PurePosixPath("xl", targets[key])
    root = ET.fromstring(archive.read(str(path).lstrip("/")))
    shared = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    texts = ["".join(t.text or "" for t in node.findall(".//{*}t")) for node in shared.findall("{*}si")]
    values = {}
    for cell in root.findall(".//{*}c"):
        value = cell.findtext("{*}v")
        kind = cell.get("t", "n")
        if value is not None and kind in ("n", "s"):
            values[cell.get("r")] = texts[int(value)] if kind == "s" else float(value)
    return values


def assay_contrasts(archive, out):
    def group(sheet, refs):
        return [sheet[ref] for ref in refs]

    def contrast(name, controls, treated, unit, locator, omit_batches=None):
        m0, m1 = mean(controls), mean(treated)
        effects = [100 * (mean(b) / mean(a) - 1) for a, b in omit_batches or ()]
        bounds = (f"{min(effects):.4f}", f"{max(effects):.4f}") if effects else ("", "")
        out.writerow([name, len(controls), len(treated), f"{m0:.4f}", f"{m1:.4f}",
                      f"{100*(m1/m0-1):.4f}", *bounds, unit, locator])

    def select(sheet, col, rows):
        return group(sheet, [f"{col}{row}" for row in rows])

    def omit(sheet, col, reference_batches, felodipine_batches):
        for excluded in range(3):
            selected = [batch for batch in range(3) if batch != excluded]
            flatten = lambda groups: [row for batch in selected for row in groups[batch]]
            yield select(sheet, col, flatten(reference_batches)), select(sheet, col, flatten(felodipine_batches))

    for panel, columns, group_rows, unit in [
        ("Fig4b", "DHL", (7, 10, 9), "normalized autolysosomes"),
        ("Fig4c", "LMN", (11, 14, 13), "normalized aggregate-positive neurons"),
    ]:
        sheet = worksheet(archive, panel)
        control, low, high = group_rows
        for nM, row in ((50, low), (100, high)):
            contrast(f"{panel}_{nM}nM", group(sheet, [f"{col}{control}" for col in columns]),
                     group(sheet, [f"{col}{row}" for col in columns]), unit, panel)

    for panel, cols, controls, treated, ctrl_batches, fel_batches, unit in [
        ("Fig4d", ("I",), range(6, 14), range(20, 26),
         ((6,), (7,), tuple(range(9, 14))), ((20,), (21, 22), (23, 24, 25)),
         "normalized cortical autolysosomes"),
        ("Fig4f", ("M", "N"), (5, 6, 8, 9, 11, 12, 13, 14, 15), range(20, 27),
         ((5, 6), (8, 9), tuple(range(11, 16))), ((20, 21), (22, 23), (24, 25, 26)),
         "normalized aggregate-positive cells per animal"),
    ]:
        sheet = worksheet(archive, panel)
        for col in cols:
            present = [row for row in controls if isinstance(sheet.get(f"{col}{row}"), float)]
            contrast(f"{panel}_{col}", select(sheet, col, present), select(sheet, col, treated), unit,
                     f"{panel} column {col}", omit(sheet, col, ctrl_batches, fel_batches))

    sheet = worksheet(archive, "Fig5c")
    for first_row in range(35, 42):
        original = tuple(sheet[f"{col}{first_row}"] for col in "DE")
        repeated = tuple(sheet[f"{col}{first_row+18}"] for col in "DE")
        if repeated != original:
            raise ValueError("The verified repeated cortex density cells have changed")
    for region, c1, c2, r1, r2 in [
        ("cortex_reported", "J", "K", range(35, 46), range(35, 46)),
        ("cortex_without_third_blot", "J", "K", range(35, 42), range(35, 43)),
        ("brainstem_reported", "AC", "AD", range(35, 46), range(35, 46)),
    ]:
        contrast(f"Fig5c_{region}", select(sheet, c1, r1), select(sheet, c2, r2),
                 "normalized insoluble alpha-synuclein / GAPDH", f"Fig5c {c1},{c2}")


def exposure_contrasts(out):
    with (HERE / "source_inputs.tsv").open(newline="") as source:
        rows = {row["id"]: float(row["value"]) for row in csv.DictReader(source, delimiter="\t")}
    mw = rows["molecular_weight"]
    for key in ("ip_mouse_plasma_peak", "pk_mouse_d10_plasma", "pk_mouse_d28_plasma",
                "phenotype_mouse_d28_plasma", "phenotype_mouse_d28_plasma_min", "phenotype_mouse_d28_plasma_max"):
        value = rows[key] * 1000 / mw
        out.writerow([key, "", "", "", f"{value:.4f}", "", "", "", "nM total plasma", "source_inputs.tsv"])
    for reference in ("elder_adult_peak", "young_adult_er_peak"):
        value = rows["phenotype_mouse_d28_plasma"] * 1000 / (mw * rows[reference])
        out.writerow([f"phenotype_mouse_over_{reference}", "", "", "", f"{value:.4f}", "", "", "",
                      "ratio of total plasma means across studies", "source_inputs.tsv"])
    upper = rows["young_adult_er_peak"] * rows["young_adult_unbound_ceiling"]
    out.writerow(["young_adult_free_peak_ceiling", "", "", "", f"{upper:.4f}", "", "", "",
                  "nM plasma, upper bound under label binding", "source_inputs.tsv"])
    n = rows["pk_mouse_d28_brain_total_n"]
    detected_sum = rows["pk_mouse_d28_brain_detected_sum"]
    bounds = (detected_sum / n, (detected_sum + rows["pk_mouse_d28_brain_censor_limit"]
                                * rows["pk_mouse_d28_brain_censored_n"]) / n)
    out.writerow(["pk_mouse_d28_brain_censor_bounds", "", int(n), "", "", "",
                  *(f"{value:.4f}" for value in bounds), "ng/g total homogenate mean", "Siddiqi Table 5"])
    for name, num, den in [
        ("aed_peak", "aed_exposed_peak", "aed_control_peak"),
        ("aed_auc", "aed_exposed_auc", "aed_control_auc"),
        ("fell_attributable_ae", "fell_related_ae", "fell_mitt"),
        ("fell_attributable_sae", "fell_related_sae", "fell_mitt"),
        ("pediatric_blinded_completion", "pediatric_blinded_completed", "pediatric_randomized"),
    ]:
        fraction = rows[num] / rows[den]
        out.writerow([name, "", "", "", f"{100*fraction:.4f}", "", "", "", "%", "source_inputs.tsv"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    args = parser.parse_args()
    if hashlib.sha256(args.workbook.read_bytes()).hexdigest() != WORKBOOK_SHA256:
        raise ValueError("Workbook does not match the verified Siddiqi source")
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["contrast", "n_reference", "n_felodipine", "reference", "felodipine_or_summary",
                  "change_pct", "lower_check", "upper_check", "unit", "locator"])
    with ZipFile(args.workbook) as archive:
        assay_contrasts(archive, out)
    exposure_contrasts(out)
