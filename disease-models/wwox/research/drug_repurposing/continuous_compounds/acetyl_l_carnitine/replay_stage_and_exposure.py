"""Replay the oral plasma scale comparison and check the held glial UMI coverage."""

import argparse
import csv
from pathlib import Path


HERE = Path(__file__).resolve().parent
GLIAL_STAGES = ("OPC", "COP", "NFOL", "MFOL", "MOL")
MIN_UMI_PER_ARM = 20


def rows_from(name):
    with (HERE / name).open() as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def oral_exposure():
    print("pmid\tlocator\toral_input\treported_dose_g\tplasma_analyte\tsummary\tn_sampled_later\ttime_h"
          "\tlater_uM\tdelta_uM\tratio_later_pre\tbath100_over_later\tbath2000_over_later")
    for row in rows_from("oral_plasma_inputs.tsv"):
        before, after = float(row["pre_uM"]), float(row["later_uM"])
        columns = [value for key, value in row.items() if key not in ("pre_uM", "later_q3_uM")]
        columns.extend((f"{after - before:.2f}", f"{after / before:.2f}"))
        if row["plasma_analyte"] == "C2":
            columns.extend((f"{100 / after:.2f}", f"{2000 / after:.2f}"))
        else:
            columns.extend((".", "."))
        print("\t".join(columns))


def glial_coverage():
    selected = {(row["cell_class"], row["gene"], row["pool"]): row
                for row in rows_from("nuclei.tsv")}
    print("stage\tgene\tctrl_nuclei\tko_nuclei\tctrl_gene_UMI\tko_gene_UMI\tctrl_CPM\tko_CPM\tpasses_floor")
    for stage in GLIAL_STAGES:
        for gene in ("CRAT", "SLC22A5", "ACSS1", "CROT"):
            ctrl = selected[stage, gene, "ctrl"]
            ko = selected[stage, gene, "ko"]
            adequate = min(int(ctrl["gene_UMI"]), int(ko["gene_UMI"])) >= MIN_UMI_PER_ARM
            print("\t".join((stage, gene, ctrl["nuclei"], ko["nuclei"], ctrl["gene_UMI"],
                             ko["gene_UMI"], ctrl["CPM"], ko["CPM"], "yes" if adequate else "no")))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("comparison", choices=("oral", "glia"))
    args = parser.parse_args()
    if args.comparison == "oral":
        oral_exposure()
    else:
        glial_coverage()
