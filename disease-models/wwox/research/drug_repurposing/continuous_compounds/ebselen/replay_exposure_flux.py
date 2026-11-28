"""Replay adult exposure scales and a steady-state transmitter identifiability check."""

from math import isclose, log


def row(comparison, endpoint, value, unit):
    print(f"{comparison}\t{endpoint}\t{value:.6g}\t{unit}")


def steady_state(supply, glutaminase, other_loss, glutamate_removal):
    glutamine = supply / (glutaminase + other_loss)
    labeled_flux_proxy = glutaminase * glutamine
    return glutamine, labeled_flux_proxy / glutamate_removal, labeled_flux_proxy


def main():
    print("comparison\tendpoint\tvalue\tunit")
    adult_peaks = (30.3 / 274.19, 83.4 / 274.19)  # Sponsor §2.5 and PubChem
    for name, peak in zip(("lowest reported group", "highest reported group"), adult_peaks):
        row(name, "total parent plasma peak", peak, "umol/L")
        for endpoint, reference in (
            ("IMPase IC50 divided by total peak", 1.5),
            ("GLS1 inactivation Ki divided by total peak", 0.014),
            ("TrxR apparent Km divided by total peak", 2.5),
        ):
            row(name, endpoint, reference / peak, "fold")
    row("purified GLS1", "saturating inactivation half-time at reported kinact", log(2) / 1.32, "h")

    # Apply the printed adult ACC MRS ratios to normalized, hypothetical pools.
    # Rate constants, their changes, and cell compartments are not fit to MRS.
    q_target = 3.37 / 3.60
    g_target = 11.34 / 11.66
    other_loss = 0.3
    baseline_gls, baseline_removal = 0.7, 0.7
    for name, supply, gls, removal in (
        ("baseline", 1.0, baseline_gls, baseline_removal),
        ("GLS inhibition alone", 1.0, 0.35, baseline_removal),
        ("same observed pools with unchanged GLS",
         q_target * (baseline_gls + other_loss), baseline_gls, baseline_gls * q_target / g_target),
        ("same observed pools with half GLS",
         q_target * (0.35 + other_loss), 0.35, 0.35 * q_target / g_target),
    ):
        q, g, flux = steady_state(supply, gls, other_loss, removal)
        if name.startswith("same observed"):
            assert isclose(q, q_target) and isclose(g, g_target)
        for endpoint, value in (
            ("glutamine pool", q), ("glutamate pool", g),
            ("glutamine supply", supply), ("glutaminase flux", flux),
            ("glutamate removal constant", removal),
        ):
            row(name, endpoint, value, "normalized")


if __name__ == "__main__":
    main()
