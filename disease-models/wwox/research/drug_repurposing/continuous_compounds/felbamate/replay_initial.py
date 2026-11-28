"""Replay published felbamate exposure, pulse and recovery summaries."""

from math import exp

PARENT_MASS = 238.24


def late_current_ratio(nmda_um, felbamate_um):
    """Kuo et al. Eq. 3, steady-state open fraction relative to no drug."""
    agonist = nmda_um / 34
    closed = (1 + agonist) ** 2
    opened = 2.6 * agonist ** 2
    desensitised = 4 * opened
    closed_bound = closed * (1 + felbamate_um / 200)
    open_bound = opened * (1 + felbamate_um / 110)
    desensitised_bound = desensitised * (1 + felbamate_um / 55)
    drug_fraction = open_bound / (closed_bound + open_bound + desensitised_bound)
    control_fraction = opened / (closed + opened + desensitised)
    return drug_fraction / control_fraction


def recovery_fraction(delay_seconds, fast_fraction, fast_tau, slow_tau):
    """Published biexponential form. Constants are fits, not raw points."""
    fast_remaining = fast_fraction * exp(-delay_seconds / fast_tau)
    slow_remaining = (1 - fast_fraction) * exp(-delay_seconds / slow_tau)
    return 1 - fast_remaining - slow_remaining


def main():
    # DailyMed Felbatol pharmacokinetics, steady-state 4–12 years.
    rows = []
    for total_ug_ml in (17, 32, 49):
        total_um = total_ug_ml * 1000 / PARENT_MASS
        rows.extend([
            (f"label_{total_ug_ml}_parent_total", "uM", total_um),
            (f"label_{total_ug_ml}_parent_free_low", "uM", total_um * 0.75),
            (f"label_{total_ug_ml}_parent_free_high", "uM", total_um * 0.78),
        ])
    # Fig. 2B/C to Fig. 5B/C, at 100 µM felbamate. Contrast between groups.
    for glycine, isolated, conditioned in (
        (0.3, (0.96, 0.79), (0.88, 0.79)),
        (30, (0.97, 0.83), (0.90, 0.78)),
    ):
        for index, phase in enumerate(("peak", "late")):
            difference = 100 * (conditioned[index] - isolated[index])
            rows.append((f"conditioning_delta_at_glycine_{glycine:g}_{phase}", "percentage_points", difference))

    for agonist in (4, 10, 1000):
        rows.append((f"equation3_felbamate_100_nmda_{agonist}", "ratio", late_current_ratio(agonist, 100)))
    rows.append(("figure3_entorhinal_felbamate_100_frequency_change", "percent", 100 * (2.5 / 5.1 - 1)))
    for delay in (0.5, 1, 2, 5):
        control = recovery_fraction(delay, 0.77, 0.82, 14.4)
        drug = recovery_fraction(delay, 0.66, 0.93, 17.4)
        rows.extend([
            (f"figure8_{delay:g}s_control_recovery", "fraction", control),
            (f"figure8_{delay:g}s_felbamate_300_recovery", "fraction", drug),
            (f"figure8_{delay:g}s_recovery_difference", "percentage_points", 100 * (drug - control)),
        ])
    print("comparison\tunit\tvalue")
    for name, unit, value in rows:
        print(f"{name}\t{unit}\t{value:.4f}")


if __name__ == "__main__":
    main()
