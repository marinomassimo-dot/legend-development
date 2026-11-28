"""Replay figure calibration, exposure units and specimen-size sensitivity."""
import csv
import sys


CALCITRIOL_G_MOL = 416.64
XUAN_INPUT_G = 0.1
XUAN_DETECTION_PG_G = 2.5
XUAN_LOW_QC_PG_G = 10
JONES_ORAL_PEAK_NM = 0.116


def main():
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(("source", "comparison", "value", "unit", "basis"))

    for label, px_y in (("vehicle", 143), ("10nM", 129), ("50nM", 102), ("100nM", 86)):
        fraction = 60 * (215 - px_y) / (215 - 47)
        out.writerow(("de la Fuente Fig. 3B", label, f"{fraction:.1f}", "%_MBP_positive_Olig2",
                      f"plot y={px_y}; percent axis 0@215, 60@47; approximate pixel reading"))

    for label, px_y in (("WT_DRG_WT_OPC", 665), ("KO_DRG_WT_OPC", 712)):
        fraction = 70 * (790 - px_y) / (790 - 595)
        out.writerow(("Repudi Fig. 6D", label, f"{fraction:.1f}", "%_myelinating_OL_morphology",
                      f"box median y={px_y}; percent axis 0@790, 70@595; PDF p.12 scaled to 1500px"))

    for in_vitro in (10, 50, 100):
        out.writerow(("de la Fuente Fig. 3B / Jones oral Cmax", str(in_vitro),
                      f"{in_vitro / JONES_ORAL_PEAK_NM:.1f}", "nominal_to_total_ratio",
                      "nominal cell medium nM / 0.116 nM total pediatric serum"))
    out.writerow(("FDA Table 9 Klaus", "historical serum peak", f"{125 / CALCITRIOL_G_MOL:.3f}", "nM_total",
                  "125 pg/mL / molecular weight; separate pediatric CKD study"))

    brain = (("anterior_watershed", 30.7), ("middle_temporal", 19.2), ("cerebellum", 18.5))
    for label, pg_g in brain:
        out.writerow(("Xuan Fig. 2", label, f"{pg_g * 1000 / CALCITRIOL_G_MOL:.1f}", "pM_total_equivalent",
                      f"{pg_g} pg/g wet tissue; assumes 1 kg/L solely for unit comparison"))

    lod_pg = XUAN_INPUT_G * XUAN_DETECTION_PG_G
    qc_pg = XUAN_INPUT_G * XUAN_LOW_QC_PG_G
    for mass_mg in (5, 10, 20, 50, 100):
        grams = mass_mg / 1000
        out.writerow(("Xuan input scenarios", f"{mass_mg}mg detection equivalent", f"{lod_pg / grams:.1f}",
                      "pg_per_g", "same absolute input mass at detection as original; constant assay recovery"))
        out.writerow(("Xuan input scenarios", f"{mass_mg}mg lowest QC equivalent", f"{qc_pg / grams:.1f}",
                      "pg_per_g", "same absolute mass as lowest reported QC; not a validated LLOQ"))

    mass_per_ml_g = 0.15
    stack_ml = 0.4
    standard_limit_pg_ml = 12.5
    stack_pg = standard_limit_pg_ml * stack_ml
    for mass_mg in (10, 20, 50, 60):
        available_g = min(mass_per_ml_g * stack_ml, mass_mg / 1000)
        out.writerow(("Stephenson Table 3", f"{mass_mg}mg fixed 400uL stack",
                      f"{stack_pg / available_g:.1f}", "pg_per_g",
                      "ideal 100% recovery, original extraction ratio, no extra diluent beyond filling stack"))


if __name__ == "__main__":
    main()
