"""Replay tissue ratios and mouse cortical lipid contrasts without equating scales."""
import argparse
import csv
import hashlib
import math
from statistics import correlation, mean
import sys
from xml.etree import ElementTree as ET
from zipfile import ZipFile

HASHES = (
    "04e751310826c3d744f7f2966f3366e6c8762ece0311bf7fed05933995bd2616",
    "1ea5c9bcedc71957a179fc529aeed943170080e93f509f2a1073258502fbd926",
    "fa773f83cec676ab22353730092b35190edcd1f59012f803e68b752fc71f0176",
)
FIELDS = ("tissue_or_feature", "comparison", "n_reference", "n_compared", "reference_mean",
          "compared_mean", "effect", "omit_min", "omit_max", "scale", "source")


def append_contrast(writer, label, comparison, reference, compared, scale, source, ratio=False):
    def effect(a, b):
        return b / a if ratio else b - a

    a, b = mean(reference), mean(compared)
    omissions = [effect(mean(reference[:i] + reference[i+1:]), b) for i in range(len(reference))]
    omissions += [effect(a, mean(compared[:i] + compared[i+1:])) for i in range(len(compared))]
    writer.writerow((label, comparison, len(reference), len(compared), f"{a:.6g}", f"{b:.6g}",
                     f"{effect(a,b):.6g}", f"{min(omissions):.6g}", f"{max(omissions):.6g}", scale, source))


def brites_table(path, writer):
    src = ET.parse(path)
    table = src.find(".//table-wrap[@id='pone-0028539-t001']")
    period = None
    for row in table.findall(".//tbody/tr"):
        when, tissue, control_wt, _, fed_wt, treated = (
            "".join(c.itertext()).strip() for c in row
        )
        if when:
            period = when
        if "±" not in treated:
            writer.writerow((tissue, f"{period}: treated Pex7-null", "", 6, "", "", "",
                             "", "", "below detection", "Brites Table 1"))
            continue
        n_fed = {"2 months": 6, "4 months": 3}[period]
        for comparator, n, text in (("control diet WT", 4, control_wt), ("same diet WT", n_fed, fed_wt)):
            if "±" not in text:
                continue
            reference, result = (float(x.split("±")[0]) for x in (text, treated))
            writer.writerow((tissue, f"{period}: treated Pex7-null vs {comparator}", n, n_fed,
                             reference, result, f"{100*result/reference:.6g}", "", "",
                             "% of comparator DMA ratio", "Brites Table 1"))


def cortex_untreated(path, writer):
    with open(path, newline="") as source:
        data = list(csv.DictReader(source))
    for chain in ("16:0", "18:0"):
        features = [key for key in data[0] if key.startswith(f"PE(P-{chain}-")]
        if len(features) != 17:
            raise ValueError(f"Unexpected column coverage for {chain}")
        groups = {}
        for row in data:
            groups.setdefault(row["Group"], []).append(sum(float(row[key]) for key in features))
        for period in ("D1", "D3", "D28"):
            append_contrast(writer, f"sum of PE P-{chain} features", f"untreated TBI-{period} vs Sham",
                            groups["Sham"], groups[f"TBI-{period}"], "ratio of mean deposited signals",
                            "Mendeley untreated CSV", ratio=True)


def cortex_treated(path, writer):
    with ZipFile(path) as archive:
        strings = ["".join(node.itertext()) for node in ET.fromstring(
            archive.read("xl/sharedStrings.xml")).findall("{*}si")]
        root = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
        table = []
        for row in root.findall(".//{*}row"):
            cells = {}
            for cell in row.findall("{*}c"):
                value = cell.findtext("{*}v")
                if value is not None:
                    column = cell.get("r").rstrip("0123456789")
                    cells[column] = strings[int(value)] if cell.get("t") == "s" else float(value)
            table.append(cells)
    header, *samples = table
    columns = ("T", "AQ", "AR", "X", "Y", "AB", "AE", "AF", "AG")
    groups = {"Sham d28" if s["B"] == "Sham" else "Sham d28+OAG" if s["B"] == "Sham+OAG" else s["B"]
              for s in samples}
    for column in columns:
        values = {g: [] for g in groups}
        for sample in samples:
            group = sample["B"]
            if group in ("Sham", "Sham+OAG"):
                if not sample["A"].startswith("Shamd28-"):
                    continue
                group = group.replace("Sham", "Sham d28")
            values[group].append(sample[column])
        observed = [len(values[g]) for g in ("Sham d28", "Sham d28+OAG", "TBI-d1", "TBI-d1+OAG",
                                            "TBI-d3", "TBI-d3+OAG", "TBI-d28", "TBI-d28+OAG")]
        if observed != [6, 6, 6, 5, 6, 6, 6, 6]:
            raise ValueError("Unexpected sample counts in time-matched groups")
        for group in ("Sham d28", "TBI-d1", "TBI-d3", "TBI-d28"):
            append_contrast(writer, header[column], f"{group}: OAG minus control", values[group],
                            values[group+"+OAG"], "difference in deposited transformed units", "Mendeley XLSX")
    total = max(abs(s["AR"]) for s in samples)
    anti = correlation([s["T"] for s in samples], [s["AQ"] for s in samples])
    writer.writerow(("ePL", "entire treatment matrix", len(samples), "", "", "", f"{total:.6g}", "", "",
                     "maximum absolute transformed value", "Mendeley XLSX"))
    writer.writerow(("ePC and ePE", "entire treatment matrix", len(samples), "", "", "", f"{anti:.6g}", "", "",
                     "Pearson r", "Mendeley XLSX"))
    if not math.isfinite(anti):
        raise ValueError("Non-finite aggregate diagnostic")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brites_xml")
    parser.add_argument("untreated_csv")
    parser.add_argument("treated_xlsx")
    args = parser.parse_args()
    files = (args.brites_xml, args.untreated_csv, args.treated_xlsx)
    for path, expected in zip(files, HASHES):
        with open(path, "rb") as source:
            if hashlib.sha256(source.read()).hexdigest() != expected:
                raise ValueError(f"Unexpected source bytes for {path}")
    output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    output.writerow(FIELDS)
    brites_table(files[0], output)
    cortex_untreated(files[1], output)
    cortex_treated(files[2], output)
