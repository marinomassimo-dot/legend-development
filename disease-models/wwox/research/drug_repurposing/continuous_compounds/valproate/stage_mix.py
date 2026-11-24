"""Recalculate the fractions of assigned oligodendroglial nuclei in each stage."""
import csv
from pathlib import Path
import sys

source = Path(__file__).resolve().parents[1] / "creatine/nuclei.tsv"
with source.open() as stream:
    rows = [r for r in csv.DictReader(stream, delimiter="\t") if r["gene"] == "Gamt"]
stages = ("OPC", "COP", "NFOL", "MFOL", "MOL")
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(("pool","stage","nuclei","classified_lineage_nuclei","percent"))
for pool in ("ctrl", "ko"):
    counts = {r["class"]: int(r["nuclei"]) for r in rows if r["pool"] == pool}
    total = sum(counts[stage] for stage in stages)
    for stage in stages:
        out.writerow((pool,stage,counts[stage],total,f"{100*counts[stage]/total:.2f}"))
