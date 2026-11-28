"""Replay published felbamate state models and a fixed-state pulse sensitivity."""

from math import exp, sqrt

from replay_initial import late_current_ratio

RESTING_ON_PER_M_S = 187.5
RESTING_OFF_PER_S = 0.062
ACTIVE_ON_PER_M_S = 46000
ACTIVE_OFF_PER_S = 3.1


def step_occupancy(initial, duration_s, association, dissociation, parent_um):
    """Two-state ligand occupancy at a clamped receptor activation state."""
    on_rate = association * parent_um / 1_000_000
    rate = on_rate + dissociation
    equilibrium = on_rate / rate
    return equilibrium + (initial - equilibrium) * exp(-duration_s * rate)


def main():
    # Kuo Eq. 3, no fit to the external condition checks.
    open_relative_to_resting = 1 / 110 - 1 / 200
    desensitised_relative_to_open = 1 / 55 - 1 / 110
    pivot = sqrt(open_relative_to_resting / (desensitised_relative_to_open * 4 * 2.6))
    rows = [
        ("kuo_eq3_agonist_pivot", "uM", 34 * pivot / (1 - pivot)),
        ("kuo_eq3_ratio_felbamate_100_nmda_4", "ratio", late_current_ratio(4, 100)),
        ("kuo_eq3_ratio_felbamate_100_nmda_1000", "ratio", late_current_ratio(1000, 100)),
        ("chang_fig6_relative_peak_felbamate_100_nmda_4_fit", "ratio", 1.5),
        ("chang_fig5_representative_tau_felbamate_100", "ms", 105),
        ("chang_fig5_representative_tau_felbamate_1000", "ms", 23),
    ]

    # Harty and Rogawski, Table 1 mean individual fits and Fig. 2 pooled fit.
    for fit, params in (
        ("mean_cell_fits", (("2A", 2.55, 0.86), ("2B", 0.52, 0.70), ("2C", 2.40, 0.75))),
        ("pooled_curve", (("2A", 2.30, 0.78), ("2B", 0.60, 0.86), ("2C", 2.00, 0.78))),
    ):
        for subtype, midpoint_mm, slope in params:
            inhibition = 100 / (1 + (midpoint_mm / 0.1) ** slope)
            rows.append((f"harty_{fit}_GluN{subtype}_inhibition_at_100", "percent", inhibition))

    # Chang and Kuo 2007 between-condition sensitivity with published rates.
    for parent_um in (54, 100, 160, 300, 1000):
        resting_rate = RESTING_ON_PER_M_S * parent_um / 1_000_000 + RESTING_OFF_PER_S
        active_rate = ACTIVE_ON_PER_M_S * parent_um / 1_000_000 + ACTIVE_OFF_PER_S
        resting_occupancy = 1 - RESTING_OFF_PER_S / resting_rate
        rows.extend([
            (f"rest_equilibrium_occupancy_{parent_um}", "fraction", resting_occupancy),
            (f"rest_time_constant_{parent_um}", "s", 1 / resting_rate),
            (f"active_time_constant_{parent_um}", "ms", 1000 / active_rate),
        ])
        if parent_um == 1000:
            continue
        for duration_ms in (1, 10, 100, 1000):
            at_end = step_occupancy(
                resting_occupancy, duration_ms / 1000, ACTIVE_ON_PER_M_S, ACTIVE_OFF_PER_S, parent_um
            )
            rows.append((
                f"occupied_delta_{parent_um}_{duration_ms}ms",
                "percentage_points",
                100 * (at_end - resting_occupancy),
            ))

    # Extracellular proton paper, Fig. 1B. 300 µM, 1 mM NMDA, same reference within cells.
    for ph, early, late in ((6.4, 0.95, 0.78), (7.4, 0.93, 0.75), (8.4, 0.76, 0.70)):
        rows.append((f"ph_{ph:g}_extra_late_inhibition", "percentage_points", 100 * (early - late)))

    # Ritter et al. Table 2 and pediatric retrospective review; endpoints kept separate.
    rows.extend([
        ("lgs_atonic_diary_treatment_difference", "percentage_points", -34 - (-9)),
        ("lgs_video_eeg_treatment_difference", "percentage_points", -11 - 1),
        ("retrospective_retained_response", "percent", 100 * 37 / 73),
        ("retrospective_all_enrolled_if_missing_not_responding", "percent", 100 * 37 / 75),
    ])

    print("comparison\tunit\tvalue")
    for name, unit, value in rows:
        print(f"{name}\t{unit}\t{value:.4f}")


if __name__ == "__main__":
    main()
