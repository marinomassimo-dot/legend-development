"""Replay published procysteine contrasts while keeping units and preparations separate."""

import csv
import sys


BRAIN_TISSUE = (
    ("control", 4, 1.22, 0.176, 3.76, 0.249),
    ("4 h after bolus", 3, 1.04, 0.392, 4.35, 0.275),
    ("6 h after bolus", 3, 1.05, 0.246, 4.16, 0.179),
    ("20 h infusion", 5, 1.51, 0.113, 3.93, 0.404),
)
BRAIN_ANALYTES = ("GSH", "cysteine", "taurine", "hypotaurine")
TISSUE_UNIT = "µmol/g tissue"
TISSUE_LOCATOR = "Gamcsik 2011 Table 1, rat brain extracts, group means"


def comparison():
    _, _, *control = BRAIN_TISSUE[0]
    for arm, n, *values in BRAIN_TISSUE:
        yield "rat brain extract", arm, "group size", n, "rats", TISSUE_LOCATOR
        for analyte, value, baseline in zip(BRAIN_ANALYTES, values, control):
            yield "rat brain extract", arm, f"{analyte} mean", value, TISSUE_UNIT, TISSUE_LOCATOR
            if arm != "control":
                yield "rat brain extract", arm, f"{analyte} change versus control", value - baseline, TISSUE_UNIT, TISSUE_LOCATOR
                yield "rat brain extract", arm, f"{analyte} ratio versus control", value / baseline, "ratio of means", TISSUE_LOCATOR

    bolus_enrichment = 0.0833
    gsh_infusion_enrichment = 0.348
    cys_infusion_enrichment = 0.434
    mrs_detection_scale = 0.2
    locator = "Gamcsik 2011 Results and Discussion, Fig. 2 and Fig. 3"
    yield "rat brain LC-MS enrichment", "bolus, 4.5 h", "GSH enrichment, one extract", bolus_enrichment * 100, "%", locator
    yield "rat brain LC-MS enrichment", "infusion, 20 h", "GSH enrichment, group mean", gsh_infusion_enrichment * 100, "%", locator
    yield "rat brain LC-MS enrichment", "infusion, 20 h", "cysteine enrichment, group mean", cys_infusion_enrichment * 100, "%", locator
    yield "MRS detection sensitivity", "published approximate scale", "detectable labeled metabolite", mrs_detection_scale, TISSUE_UNIT, locator
    for assumed_total in (1.0, 1.2):
        stock = assumed_total * bolus_enrichment
        condition = f"bolus at 4.5 h, assumed GSH {assumed_total:.1f} µmol/g"
        yield "MRS detection sensitivity", condition, "conditional labeled GSH", stock, TISSUE_UNIT, locator
        yield "MRS detection sensitivity", condition, "conditional fraction of MRS detection scale", stock / mrs_detection_scale, "ratio", locator

    stock = BRAIN_TISSUE[-1][2] * gsh_infusion_enrichment
    yield "MRS detection sensitivity", "infusion at 20 h", "illustrative labeled GSH, product of group means", stock, TISSUE_UNIT, locator
    yield "MRS detection sensitivity", "infusion at 20 h", "illustrative fraction of MRS detection scale", stock / mrs_detection_scale, "ratio", locator

    for analyte, before, after in (("cysteine", 0.37, 0.99), ("GSH", 8.7, 15.6)):
        yield "adult human lymphocytes", "2–3 h after oral parent", f"{analyte} ratio versus baseline", after / before, "ratio of means", "Porta 1991 primary abstract, nmol/mg protein"


def main():
    writer = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    writer.writerow(("preparation", "condition", "statistic", "value", "unit", "locator"))
    for preparation, condition, statistic, value, unit, locator in comparison():
        writer.writerow((preparation, condition, statistic, f"{value:.8g}", unit, locator))


if __name__ == "__main__":
    main()
