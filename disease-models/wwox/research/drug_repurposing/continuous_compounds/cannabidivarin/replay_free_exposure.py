"""Replay the conditional parent exposure comparison without estimating pediatric brain PK."""
import csv
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
PLASMA_FREE_SCENARIOS = (0.01, 0.10, 0.232, 1.00)
TARGETS = (
    ("Husni Table 1", "recombinant human CB2 GTPgammaS", 0.003, "reported estimate"),
    ("Zagzoog Table 2", "recombinant human CB2 cAMP inhibition", 0.005, "reported estimate"),
    ("Zagzoog Table 3", "recombinant human CB2 beta-arrestin2 recruitment", 10.0, "strict lower bound"),
    ("De Petrocellis Table 1", "recombinant rat TRPA1 activation", 0.42, "reported estimate"),
    ("De Petrocellis Table 3", "recombinant human TRPV1 activation", 3.6, "reported estimate"),
    ("De Petrocellis Table 3", "recombinant human TRPV1 desensitization", 10.0, "reported estimate"),
    ("Iannotti Fig 7", "rat CA1 native-slice duration comparison", 10.0, "tested concentration"),
)


def main():
    with (HERE / "clinical_checkpoint.tsv").open() as source:
        matched, = (row for row in csv.DictReader(source, delimiter="\t")
                    if row["comparison"] == "first-exposure parent Cmax"
                    and row["units"] == "micromolar total plasma")
    cmax = float(matched["value"])
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("source", "readout", "nominal_uM", "nominal_quantity", "assumed_fup",
                  "scenario_free_plasma_nM", "required_kpuu_over_fu_assay"))
    for source, readout, benchmark, quantity in TARGETS:
        for fup in PLASMA_FREE_SCENARIOS:
            free_plasma = cmax * fup
            out.writerow((source, readout, benchmark, quantity, fup,
                          f"{1000 * free_plasma:.6f}", f"{benchmark / free_plasma:.6f}"))


if __name__ == "__main__":
    main()
