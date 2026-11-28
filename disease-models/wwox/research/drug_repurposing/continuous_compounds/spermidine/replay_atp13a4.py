"""Replay van Veen et al. puncta, polyamine and miniature-current contrasts."""

import argparse
from collections import defaultdict
from pathlib import Path
from statistics import mean
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[6] / "framework" / "scripts"))
from xlsx_to_text import sheet_names


def load_figures(workbook):
    selected = ("Fig. 4c", "Fig. 4d", "Fig. 4f", "Fig. 5a-d", "Fig. 5e-g",
                "Suppl. Fig. 12a-g", "Fig. 5p", "Fig. 5r-s")
    with ZipFile(workbook) as archive:
        strings = ["".join(string.itertext())
                   for string in ET.fromstring(archive.read("xl/sharedStrings.xml"))]
        figures = {}
        for prefix in selected:
            member, = (member for title, member in sheet_names(archive) if title.startswith(prefix))
            cells = ET.fromstring(archive.read(member)).findall(".//{*}c")
            figures[prefix] = {
                cell.get("r"): strings[int(value)] if cell.get("t") == "s" else float(value)
                for cell in cells if (value := cell.findtext("{*}v")) is not None
            }
    return figures


def column(page, col, start, stop):
    return [page[f"{col}{row}"] for row in range(start, stop + 1) if f"{col}{row}" in page]


def wells(page, columns):
    assert [page[f"{col}8"] for col in columns] == ["N1", "N2", "N3"]
    values = [column(page, col, 9, 31) for col in columns]
    return [mean(group) for group in values], sum(map(len, values))


def electrical(page, id_col, value_col, start, stop):
    animals = defaultdict(list)
    for row in range(start, stop + 1):
        if (animal := page.get(f"{id_col}{row}")) is not None:
            animals[animal].append(page[f"{value_col}{row}"])
    assert set(animals) == {"Animal 1", "Animal 2", "Animal 3"}
    return [mean(values) for values in animals.values()], sum(map(len, animals.values()))


def row_values(page, columns, row):
    return [page[f"{col}{row}"] for col in columns]


def report(panel, endpoint, unit, ctrl, test, ctrl_obs, test_obs, group_unit, paired=False):
    ctrl_mean, test_mean = mean(ctrl), mean(test)
    change = test_mean - ctrl_mean
    if paired:
        differences = [treatment - baseline for baseline, treatment in zip(ctrl, test)]
        omissions = [mean(differences[:i] + differences[i + 1:]) for i in range(len(differences))]
    else:
        omissions = (
            [test_mean - mean(ctrl[:i] + ctrl[i + 1:]) for i in range(len(ctrl))]
            + [mean(test[:i] + test[i + 1:]) - ctrl_mean for i in range(len(test))]
        )
    record = (panel, endpoint, unit, group_unit, len(ctrl), len(test), ctrl_obs, test_obs,
              f"{ctrl_mean:.5g}", f"{test_mean:.5g}", f"{change:.5g}",
              f"{test_mean / ctrl_mean:.5g}", f"{min(omissions):.5g}", f"{max(omissions):.5g}")
    print("\t".join(map(str, record)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_workbook", type=Path)
    args = parser.parse_args()
    p = load_figures(args.source_workbook)
    print("panel\tcontrast\tunit\tanalysis_unit\tctrl_n\ttest_n\tctrl_observations\ttest_observations"
          "\tctrl_mean\ttest_mean\tdifference\tratio\tomit_min_difference\tomit_max_difference")

    for panel, name, base, treated in (
        ("Fig. 4c", "knockdown medium vs control medium", "EFG", "HIJ"),
        ("Fig. 4f", "10 nM spermidine vs vehicle", "BCD", "EFG"),
        ("Fig. 4f", "10 nM spermine vs vehicle", "BCD", "HIJ"),
    ):
        ctrl, ctrl_obs = wells(p[panel], base)
        test, test_obs = wells(p[panel], treated)
        report(panel, name, "colocalized puncta/image", ctrl, test, ctrl_obs, test_obs,
               "neuronal preparation", paired=True)

    for panel, name, unit, cols_ctrl, cols_test, ctrl_r, test_r, analysis_unit in (
        ("Fig. 4d", "knockdown medium vs control medium spermidine", "uM",
         "BCD", "BCD", 10, 11, "biological replicate"),
        ("Fig. 5a-d", "cortical spermidine KO vs WT", "nmol/g",
         "BCDEFGHIJKLM", "NOPQRSTUVWXY", 11, 11, "mouse"),
        ("Fig. 5e-g", "CSF spermidine KO vs WT", "uM",
         "BCDEFG", "HIJKLM", 9, 9, "sample incl. pools"),
        ("Suppl. Fig. 12a-g", "plasma spermidine KO vs WT", "uM",
         "BCDEFGHIJKLM", "NOPQRSTUVWXY", 11, 11, "mouse"),
    ):
        ctrl = row_values(p[panel], cols_ctrl, ctrl_r)
        test = row_values(p[panel], cols_test, test_r)
        report(panel, name, unit, ctrl, test, len(ctrl), len(test), analysis_unit)

    panel = "Fig. 5p"
    ctrl, test = (column(p[panel], col, 9, 22) for col in "BC")
    assert (len(ctrl), len(test)) == (14, 12)
    report(panel, "excitatory contacts KO vs WT", "colocalized puncta/image",
           ctrl, test, len(ctrl), len(test), "mouse")

    panel = "Fig. 5r-s"
    for kind, start, end in (("mEPSC", 8, 33), ("mIPSC", 38, 60)):
        for measure, unit, ids_values_wt, ids_values_ko in (
            ("frequency", "Hz", ("B", "D"), ("E", "G")),
            ("amplitude", "pA", ("I", "K"), ("L", "N")),
        ):
            ctrl, ctrl_obs = electrical(p[panel], *ids_values_wt, start, end)
            test, test_obs = electrical(p[panel], *ids_values_ko, start, end)
            source = panel if kind == "mEPSC" else "Suppl. Fig. 11p-q"
            report(source, f"{kind} {measure} KO vs WT", unit,
                   ctrl, test, ctrl_obs, test_obs, "mouse")


if __name__ == "__main__":
    main()
