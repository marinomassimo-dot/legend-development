"""Recalculate the published human crossover and digitize mouse brain plot means."""

import argparse
import hashlib
from pathlib import Path
from statistics import mean
from xml.etree import ElementTree

import pymupdf


FIGURE_DOCUMENT_SHA256 = "1d82a5c4a41b5245b9e5f248ee2287f9353cc54e506e85b01235642069b16b87"
GROUPS = ("WT", "WT_GGC", "APP_PS1", "APP_PS1_GGC")
PANELS = (
    ("brain_ATP", "Fig. 3", 28, 0, 2.5, 100, 298, 289.32, "nM/mg protein as printed"),
    ("brain_GSH", "Fig. 4C", 30, 0, 60, 100, 299, 289.32, "ug/mg protein"),
    ("brain_oxidized_to_reduced_ratio", "Fig. 4D", 30, 0, 100, 374, 565, 560.52, "percent"),
)


def normalized_text(node):
    return " ".join("".join(node.itertext()).split())


def human_delta_auc(xml_path):
    root = ElementTree.parse(xml_path)
    table, = (
        element for element in root.findall(".//table-wrap")
        if element.findtext("label") == "Table 2"
    )
    two_grams = {}
    four_grams = {}
    current = None
    for row in table.findall(".//tr"):
        cells = [normalized_text(child) for child in row]
        if any(text.startswith("2 g γ-GC") for text in cells):
            current = two_grams
        elif any(text.startswith("4 g γ-GC") for text in cells):
            current = four_grams
        elif current is not None and len(cells) == 8 and cells[0][:1].isdigit():
            current[cells[0]] = float(cells[6])
    if len(two_grams) != 5 or len(four_grams) != 4 or not four_grams.keys() <= two_grams.keys():
        raise ValueError("Unexpected rows in Zarka and Bridge Table 2")
    return two_grams, four_grams


def bar_heights(page, baseline):
    heights = {}
    for path in page.get_drawings():
        if path["fill"] != (0.0, 0.0, 0.0):
            continue
        for index, item in enumerate(path["items"]):
            if item[0] == "re":
                _, box, _ = item
                left, top, right, bottom = box
            elif item[0] == "l" and index + 1 < len(path["items"]):
                _, start, end = item
                following = path["items"][index + 1]
                if following[0] != "l" or following[1] != end or following[2].x != end.x or start.y != end.y:
                    continue
                left, top = start
                right, bottom = following[2]
            else:
                continue
            if 22 < right - left < 25 and 140 < left < 380 and abs(bottom - baseline) < 0.1:
                heights[round(left, 2)] = bottom - top
    if len(heights) != 4:
        raise ValueError(f"Expected four plotted bars on PDF page {page.number + 1} at {baseline}")
    return [heights[x] for x in sorted(heights)]


def panel_values(page, top_tick, bottom_tick, start, end, baseline):
    ticks = {}
    for word in page.get_text("words"):
        x0, y0, x1, y1, text = word[:5]
        mid = (y0 + y1) / 2
        if 90 < x0 < 112 and x1 < 112 and start <= mid <= end and text.replace(".", "", 1).isdigit():
            ticks[float(text)] = mid
    scale = (ticks[bottom_tick] - ticks[top_tick]) / (top_tick - bottom_tick)
    return [height / scale for height in bar_heights(page, baseline)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("human_xml", type=Path)
    parser.add_argument("mouse_pdf", type=Path)
    args = parser.parse_args()
    if hashlib.sha256(args.mouse_pdf.read_bytes()).hexdigest() != FIGURE_DOCUMENT_SHA256:
        raise ValueError("Unexpected Liu et al. accepted manuscript version")
    print("comparison\tmetric\tvalue\tunit\tlocator")

    def emit(comparison, metric, value, unit, locator):
        print(f"{comparison}\t{metric}\t{value:.6g}\t{unit}\t{locator}")

    two, four = human_delta_auc(args.human_xml)
    unit = "nmol*h/1e6 lymphocytes"
    paired_low = [two[key] for key in four]
    paired_high = list(four.values())
    differences = [high - low for low, high in zip(paired_low, paired_high)]
    omissions = [mean(differences[:index] + differences[index + 1:]) for index in range(len(differences))]
    estimates = (
        ("available_case_2g_mean", mean(two.values()), unit),
        ("available_case_4g_mean", mean(four.values()), unit),
        ("available_case_ratio_4g_to_2g", mean(four.values()) / mean(two.values()), "ratio"),
        ("paired_2g_mean", mean(paired_low), unit),
        ("paired_4g_mean", mean(paired_high), unit),
        ("paired_difference_4g_minus_2g", mean(differences), unit),
        ("paired_ratio_4g_to_2g", mean(paired_high) / mean(paired_low), "ratio"),
        ("paired_n", len(differences), "participants"),
        ("paired_positive_n", sum(value > 0 for value in differences), "participants"),
        ("one_omission_min_difference", min(omissions), unit),
        ("one_omission_max_difference", max(omissions), unit),
    )
    for metric, value, units in estimates:
        emit("human_lymphocyte_delta_AUC", metric, value, units, "Zarka and Bridge Table 2")

    with pymupdf.open(args.mouse_pdf) as document:
        for name, figure, page, low, high, start, end, baseline, units in PANELS:
            values = panel_values(document[page - 1], high, low, start, end, baseline)
            locator = f"Liu accepted PDF p. {page} {figure}, approximate plot read"
            for group, value in zip(GROUPS, values):
                emit(name, group, value, units, locator)
            wt, _, untreated, treated = values
            emit(name, "APP_PS1_treated_minus_untreated", treated - untreated, units, locator)
            emit(name, "APP_PS1_gap_to_untreated_WT_closed", (treated - untreated) / (wt - untreated), "fraction", locator)


if __name__ == "__main__":
    main()
