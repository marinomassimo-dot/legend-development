"""Recompute M+0 contrasts from Parker et al., Nature Communications (2021)."""
import argparse
import hashlib
from pathlib import Path
from statistics import mean, stdev
from xml.etree import ElementTree
from zipfile import ZipFile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("workbook", type=Path)
workbook = parser.parse_args().workbook
expected = "32d9908b5e01e5a0e301760043276713286b65ddc1137c83c9006df351047bbf"
if hashlib.sha256(workbook.read_bytes()).hexdigest() != expected:
    raise ValueError("Source Data workbook differs from the archived version")

# Each group has three biological replicates. The matched vehicle is specific to
# the oxygen condition or sample compartment. Group contrasts use unpaired means.
with ZipFile(workbook) as archive:
    print("panel\tcell\tpool_condition\tanalyte\tvehicle_M0_pct\tvehicle_SD_pp\tAKG_M0_pct\tAKG_SD_pp\tdifference_pp")
    for sheet, panel, cell, condition, analyte, row, controls, treated in (
        (10, "5e", "8988T", "cell_normoxia", "AKG", 34, "LMN", "OPQ"),
        (10, "5e", "8988T", "cell_anoxia", "AKG", 34, "RST", "UVW"),
        (10, "5e", "8988T", "cell_normoxia", "succinate", 25, "LMN", "OPQ"),
        (10, "5e", "8988T", "cell_anoxia", "succinate", 25, "RST", "UVW"),
        (12, "6d", "HuPT4", "intracellular", "succinate", 4, "CDE", "FGH"),
        (12, "6d", "HuPT4", "medium", "succinate", 11, "CDE", "FGH"),
    ):
        root = ElementTree.fromstring(archive.read(f"xl/worksheets/sheet{sheet}.xml"))
        values = {c.get("r"): c.findtext("{*}v") for c in root.findall(".//{*}c")}
        vehicle = [100 * float(values[f"{col}{row}"]) for col in controls]
        akg = [100 * float(values[f"{col}{row}"]) for col in treated]
        stats = mean(vehicle), stdev(vehicle), mean(akg), stdev(akg), mean(akg) - mean(vehicle)
        print(panel, cell, condition, analyte, *(f"{v:.2f}" for v in stats), sep="\t")
