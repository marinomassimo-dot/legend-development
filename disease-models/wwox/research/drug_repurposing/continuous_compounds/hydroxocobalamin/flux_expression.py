"""Rank MMAA transcript and protein in two published fibroblast outliers against controls."""
import csv
from pathlib import Path
from statistics import correlation, median
import sys
from openpyxl import load_workbook

folder = Path(sys.argv[1]) / "deepening_downloads/hydroxocobalamin_loop_20261124"
phenos = load_workbook(folder / "forny_s4.xlsx", read_only=True, data_only=True)
header, *rows = phenos.active.values
controls = {r[0] for r in rows if r[header.index("case")] == 0}
paired = {r[0]: (r[header.index("OHCblMinus")], r[header.index("OHCblPlus")]) for r in rows
          if r[0] in controls and all(isinstance(r[header.index(k)], (int, float))
                                      for k in ("OHCblMinus", "OHCblPlus"))}
data = load_workbook(folder / "forny_s3.xlsx", read_only=True, data_only=True)
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("layer", "sample", "reported_value", "measured_controls", "control_min", "control_median",
                 "control_max", "controls_below_or_equal"))
for sheet, column, identifier in (("Source Data transcriptomics",0,"ENSG00000151611"),
                                  ("Source Data proteomics",2,"MMAA_HUMAN")):
    row_iter = data[sheet].values
    header = next(row_iter)
    target = next((r for r in row_iter if r[column] == identifier), None)
    if target is None:
        for sample in ("MMA206","MMA209"):
            writer.writerow((sheet, sample, "unrepresented", 0, "NA", "NA", "NA", "NA"))
        continue
    target = dict(zip(header, target))
    values = [target[c] for c in controls if isinstance(target.get(c), (int,float))]
    assert values
    for sample in ("MMA206","MMA209"):
        value = target.get(sample)
        valid = isinstance(value, (int,float))
        writer.writerow((sheet,sample,value if valid else "NA",len(values),min(values),median(values),max(values),
                         sum(x<=value for x in values) if valid else "NA"))

    if sheet == "Source Data transcriptomics":
        samples = sorted(c for c in paired if isinstance(target.get(c), (int, float)))
        with Path(sys.argv[2]).open("w") as stream:
            out = csv.writer(stream, delimiter="\t", lineterminator="\n")
            out.writerow(("measure", "controls_with_pairs_and_RNA", "rho", "omit_min", "omit_max"))
            for name in ("gain", "treated"):
                def association(keys):
                    x = [target[c] for c in keys]
                    y = [paired[c][1] - paired[c][0] if name == "gain" else paired[c][1] for c in keys]
                    return correlation(x, y, method="ranked")
                omissions = [association([c for c in samples if c != omitted]) for omitted in samples]
                out.writerow((name, len(samples), round(association(samples), 3),
                              round(min(omissions), 3), round(max(omissions), 3)))
