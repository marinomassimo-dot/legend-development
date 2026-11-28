"""Replay scoped digitization and exposure comparisons for olesoxime."""

import csv
import sys

output = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
output.writerow(("study", "condition", "measure", "value", "unit"))

# Su et al., Fig. 4C, 644 x 1461 image. Use tick and bar-line midpoints.
zero_y = 1395.5
one_y = 1144.5
for hours, wt_y, ko_y in ((12, 1242, 1193), (24, 1274, 1196), (48, 1307, 1198)):
    wt = (zero_y - wt_y) / (zero_y - one_y)
    ko = (zero_y - ko_y) / (zero_y - one_y)
    condition = f"{hours}h serum withdrawal"
    output.writerows((
        ("Su 2026 Fig. 4C", condition, "WT signal", f"{wt:.3f}", "fold of baseline"),
        ("Su 2026 Fig. 4C", condition, "KO signal", f"{ko:.3f}", "fold of baseline"),
        ("Su 2026 Fig. 4C", condition, "KO/WT baseline for equal raw signal",
         f"{wt / ko:.3f}", "ratio"),
    ))

# Wang et al., Results corresponding to Fig. 1. Compare within age and protocol.
for age, wt_n, ko_n, wt, ko in (("P9", 16, 19, 10.5, 20.6), ("P60", 18, 13, 14.3, 2.3)):
    output.writerows((
        ("Wang 2009 Fig. 1", age, "WT n", wt_n, "animals"),
        ("Wang 2009 Fig. 1", age, "KO n", ko_n, "animals"),
        ("Wang 2009 Fig. 1", age, "WT tissue loss", wt, "mm3"),
        ("Wang 2009 Fig. 1", age, "KO tissue loss", ko, "mm3"),
        ("Wang 2009 Fig. 1", age, "KO minus WT tissue loss", f"{ko - wt:.1f}", "mm3"),
        ("Wang 2009 Fig. 1", age, "KO/WT tissue loss", f"{ko / wt:.3f}", "ratio"),
    ))

# Bordet et al., Table 4. Labels identify rows of the animal experiment.
molar_mass_g_mol = 399.65
ocr_nominal_uM = 30.0
for days, row, plasma_ug_ml, brain_ug_g in (
    (7, "middle", 0.55, 0.19),
    (42, "middle", 0.47, 0.24),
    (7, "highest", 5.35, 1.23),
    (42, "highest", 5.85, 2.66),
):
    brain_umol_kg = 1000 * brain_ug_g / molar_mass_g_mol
    # A uniform tissue density of 1 kg/L is used only for this sensitivity example.
    required_fraction_ratio = ocr_nominal_uM / brain_umol_kg
    condition = f"Day {days}, {row} row"
    output.writerows((
        ("Bordet 2010 Table 4", condition, "Total brain", f"{brain_umol_kg:.3f}", "umol/kg"),
        ("Bordet 2010 Table 4", condition, "Total brain/plasma",
         f"{brain_ug_g / plasma_ug_ml:.3f}", "mL/g"),
        ("Bordet 2010 Table 4", condition, "Required brain/medium free fractions",
         f"{required_fraction_ratio:.2f}", "ratio"),
    ))
