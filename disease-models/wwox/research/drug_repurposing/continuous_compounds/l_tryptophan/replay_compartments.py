"""Reproduce source arithmetic and an illustrative two-source isotope balance."""

from math import isclose


def row(comparison, observation, value, unit):
    print(f"{comparison}\t{observation}\t{value:.6g}\t{unit}")


def main():
    print("comparison\tobservation\tvalue\tunit")
    # Orhan Table 2. Day 2 matched timing, 7–12 mL fraction. Group mean ratios.
    for analyte, csf, plasma in (
        ("tryptophan", 1.80, 73.98),
        ("kynurenine", 0.03, 2.06),
        ("kynurenate", 1.41, 39.95),
        ("quinolinate", 18.02, 608.0),
    ):
        row("fraction_over_plasma_mean", analyte, 100 * csf / plasma, "percent")

    # Hilmas Results, Figs. 6–7. A scale comparison, not predicted occupancy.
    kynurenate_baseline = 1.41 / 1000  # nM to µM
    row("receptor_scale", "NMDA IC50 shift with 10 µM added glycine", 238.9 / 15.4, "fold")
    row("receptor_scale", "no-added-glycine IC50 over CSF KYNA mean",
        15.4 / kynurenate_baseline, "fold")
    row("receptor_scale", "10 µM glycine IC50 over CSF KYNA mean",
        238.9 / kynurenate_baseline, "fold")

    # Identical input sum, disposal constant, and pool. Arbitrary units and
    # enrichment choices, with no fit to WWOX or to the gerbil study.
    clearance = 1.0
    for name, imported, local in (
        ("import-dominant", 0.8, 0.2),
        ("local-dominant", 0.2, 0.8),
    ):
        total_flux = imported + local
        row(name, "central KYN amount", total_flux / clearance, "normalized")
        for arm, blood_enrichment, local_enrichment in (
            ("shared precursor label", 0.5, 0.5),
            ("incoming KYN-specific label", 0.5, 0.0),
            ("local TRP-specific label", 0.0, 0.5),
        ):
            measured = (imported * blood_enrichment + local * local_enrichment) / total_flux
            row(name, arm, 100 * measured, "percent")
            if arm == "incoming KYN-specific label":
                recovered = (measured - local_enrichment) / (blood_enrichment - local_enrichment)
                assert isclose(recovered, imported / total_flux)


if __name__ == "__main__":
    main()
