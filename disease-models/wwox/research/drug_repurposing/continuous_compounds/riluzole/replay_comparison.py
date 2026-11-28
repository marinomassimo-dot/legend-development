"""Replay exposure arithmetic and a synthetic fixed-input glutamate comparison."""

from math import exp, isclose


def print_exposure():
    molecular_mass = 234.20  # Riluzole, g/mol
    pediatric_peak = 359 / molecular_mass  # Abbara et al., Table 2, mean total Cmax
    pediatric_free_guess = pediatric_peak * 0.04  # TIGLUTIK label, population binding
    adult_csf_measurement = 3.9 / molecular_mass  # Sarkar et al., one post-injury sample
    print("endpoint\tcondition\tvalue\tunit")
    for condition, exposure in (
        ("pediatric SMA mean total plasma peak", pediatric_peak),
        ("pediatric SMA total plasma peak SD", 234 / molecular_mass),
        ("pediatric SMA mean peak arithmetic free plasma at 96% binding", pediatric_free_guess),
        ("pediatric SMA mean peak arithmetic free plasma at 98% binding", pediatric_peak * 0.02),
        ("pediatric OCD week-24 total serum median", 76 / molecular_mass),
        ("pediatric OCD week-24 total serum IQR lower", 53 / molecular_mass),
        ("pediatric OCD week-24 total serum IQR upper", 172 / molecular_mass),
        ("historical adult ALS total serum median peak", 183 / molecular_mass),
        ("adult spinal-injury CSF single total concentration", adult_csf_measurement),
    ):
        print(f"exposure\t{condition}\t{exposure:.5f}\tumol/L")
    for concentration in (0.1, 1.0, 3.0, 100.0):
        ratio = concentration / pediatric_free_guess
        print(f"nominal_bath_over_arithmetic_free_plasma\t{concentration:g} umol/L bath\t{ratio:.2f}\tratio")
    local_stock_amount_nmol = 7 * 200 / 1000  # Human slice Fig. 3
    print(f"local_application_amount\tHuman slice Fig. 3\t{local_stock_amount_nmol:.2f}\tnmol")


def concentration(time, initial, clearance, secondary_release):
    direct = initial * exp(-clearance * time)
    delay, release_rate = 0.12, 3.0  # s, s^-1; synthetic values only
    elapsed = time - delay
    if elapsed <= 0 or not secondary_release:
        return direct
    released = secondary_release * release_rate / (clearance - release_rate)
    return direct + released * (exp(-release_rate * elapsed) - exp(-clearance * elapsed))


def integrate(initial, clearance, secondary_release, start=0):
    step = 0.0005
    value = 0.5 * concentration(start, initial, clearance, secondary_release)
    stop = 8
    for k in range(1, round((stop - start) / step)):
        value += concentration(start + k * step, initial, clearance, secondary_release)
    value += 0.5 * concentration(stop, initial, clearance, secondary_release)
    return value * step


def print_glutamate_comparison():
    for stimulus in ("evoked", "fixed"):
        suppressed_release = 0.70 if stimulus == "evoked" else 1.0
        scenarios = (
            ("baseline", 1.0, 5.0, 0.0),
            ("uptake", 1.0, 7.5, 0.0),
            ("neuronal_release_reduction", suppressed_release, 5.0, 0.0),
            ("uptake_and_delayed_glial_release", 1.0, 7.5, 0.60),
        )
        for mechanism, initial, clearance, secondary in scenarios:
            label = f"{stimulus} {mechanism}"
            area = (initial + secondary) / clearance
            assert isclose(area, integrate(initial, clearance, secondary), abs_tol=1e-6)
            for endpoint, value, unit in (
                ("initial_Glu", initial, "normalized concentration"),
                ("early_Glu_50ms", concentration(0.05, initial, clearance, secondary), "normalized concentration"),
                ("total_Glu_area", area, "normalized concentration*s"),
                ("late_Glu_area_after_200ms", integrate(initial, clearance, secondary, 0.20), "normalized concentration*s"),
            ):
                print(f"{endpoint}\t{label}\t{value:.5f}\t{unit}")


if __name__ == "__main__":
    print_exposure()
    print_glutamate_comparison()
