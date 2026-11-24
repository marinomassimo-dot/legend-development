"""Compare NMNAT2 to five neuronal markers in the same pooled mouse nuclei."""
import csv
from pathlib import Path
import sys
import tempfile

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "thiamine"))
from cell_types import run

markers = "Stmn2 Tubb3 Nefl Gap43 Snap25".split()
with tempfile.TemporaryDirectory() as scratch:
    path = Path(scratch)
    run(Path(sys.argv[1]), genes=["Nmnat2", *markers], output_dir=path)
    with (path / "cell_types.tsv").open() as handle:
        counts = {(r["pool"], r["class"], r["gene"]): int(r["gene_UMI"])
                  for r in csv.DictReader(handle, delimiter="\t")}
writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
writer.writerow(("cell", "denominator", "WT_Nmnat2", "KO_Nmnat2", "WT_marker", "KO_marker", "ratio_of_ratios"))
for cell in ("exc", "inh"):
    wt, ko = (counts[arm, cell, "Nmnat2"] for arm in ("ctrl", "ko"))
    for gene in markers:
        ref_wt, ref_ko = (counts[arm, cell, gene] for arm in ("ctrl", "ko"))
        ratio = round(ko * ref_wt / (wt * ref_ko), 4) if min(wt, ko, ref_wt, ref_ko) > 0 else "NA"
        writer.writerow((cell, gene, wt, ko, ref_wt, ref_ko, ratio))
