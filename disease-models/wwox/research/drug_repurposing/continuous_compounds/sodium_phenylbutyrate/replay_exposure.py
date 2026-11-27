"""Replay published aggregate exposure, nitrogen recovery and PDK2 scenarios."""

PBA_MG_PER_MMOL = 164.20
PAA_MG_PER_MMOL = 136.15
PAGN_MG_PER_MMOL = 264.28
N_MG_PER_MMOL = 14.007
PDK2_KI_MM = 0.33


def pdk2_inhibition_pct(concentration_mm, substrate_over_km):
    """Competitive initial-rate equation, with input treated as free inhibitor."""
    apparent_ic50 = PDK2_KI_MM * (1 + substrate_over_km)
    return 100 * concentration_mm / (apparent_ic50 + concentration_mm)


def main():
    # Smith Fig. B and Mokhtarani Table 2, NaPBA periods only.
    younger_pba = 483 / 24 / PBA_MG_PER_MMOL
    younger_paa = 1458 / 24 / PAA_MG_PER_MMOL
    older_pba = 236 / 24 / PBA_MG_PER_MMOL
    older_paa = 773 / 24 / PAA_MG_PER_MMOL
    older_pba_peak = 37.4 / PBA_MG_PER_MMOL
    older_paa_peak = 75.1 / PAA_MG_PER_MMOL
    urinary_pagn_mmol = 12500 / PAGN_MG_PER_MMOL
    rows = [
        ("young_ucd_pba_time_average", "mM", younger_pba),
        ("young_ucd_paa_time_average", "mM", younger_paa),
        ("young_ucd_paa_over_pba_molar_auc", "ratio", younger_paa / younger_pba),
        ("older_ucd_pba_time_average", "mM", older_pba),
        ("older_ucd_paa_time_average", "mM", older_paa),
        ("older_ucd_pba_observed_peak_mean", "mM", older_pba_peak),
        ("older_ucd_paa_observed_peak_mean", "mM", older_paa_peak),
        ("older_ucd_paa_over_pba_molar_auc", "ratio", older_paa / older_pba),
        ("older_ucd_pagn_glutamine_conjugated", "mmol/24h", urinary_pagn_mmol),
        ("older_ucd_nitrogen_in_pagn", "g/24h", urinary_pagn_mmol * 2 * N_MG_PER_MMOL / 1000),
        ("healthy_adult_fast_glutamine_change", "percent", 100 * (380 / 514 - 1)),
        ("e1_alpha_range_low_from_method", "uM", 0.5 / 47000 / 50 * 1e6),
        ("e1_alpha_range_high_from_method", "uM", 8 / 47000 / 50 * 1e6),
    ]
    for label, parent in (
        ("young_24h_mean", younger_pba),
        ("older_24h_mean", older_pba),
        ("older_peak", older_pba_peak),
    ):
        rows.append((f"pba_over_apparent_pdk2_ki_{label}", "ratio", parent / PDK2_KI_MM))
        for substrate_over_km in (0.1, 1, 10):
            scenario = f"pdk2_inhibition_if_free_{label}_s_over_km_{substrate_over_km:g}"
            rows.append((scenario, "percent", pdk2_inhibition_pct(parent, substrate_over_km)))

    print("comparison\tunit\tvalue")
    for label, unit, value in rows:
        print(f"{label}\t{unit}\t{value:.4f}")


if __name__ == "__main__":
    main()
