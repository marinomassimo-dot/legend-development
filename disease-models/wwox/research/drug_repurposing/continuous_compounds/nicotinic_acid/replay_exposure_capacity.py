"""Replay study-level PK comparisons and a synthetic NAPRT capacity check."""

from math import isclose


def row(comparison, observation, value, unit):
    print(f"{comparison}\t{observation}\t{value:.6g}\t{unit}")


def main():
    print("comparison\tobservation\tvalue\tunit")
    molar_mass = 123.11
    for formulation, concentration in (
        ("Neuvonen I rapid release", 7.4),
        ("Neuvonen II sustained release", 2.1),
        ("Neuvonen III sustained release", 0.08),
        ("Menon distinct extended release", 9.3),
    ):
        micromolar = concentration * 1000 / molar_mass
        row(formulation, "reported parent mean Cmax", micromolar, "umol/L")
        row(formulation, "100 umol/L culture input divided by serum or plasma peak",
            100 / micromolar, "fold")
    row("Neuvonen within-study comparison", "mean peak I divided by III", 7.4 / 0.08, "fold")
    row("Neuvonen within-study comparison", "mean peak I divided by II", 7.4 / 2.1, "fold")

    # Matched 17% oxygen groups, Ndufs4 model. Means within each tissue only.
    for tissue, treated, vehicle in (
        ("brainstem", 2.06, 1.26),
        ("cerebellum", 5.50, 4.33),
        ("cerebrum", 5.77, 3.96),
    ):
        row("Ndufs4 at 17% oxygen", tissue + " trough NAD increase",
            (treated / vehicle - 1) * 100, "percent")

    # J = a*S/(K+S), where a is capacity relative to control. S is expressed
    # in K units. These scenarios are assumptions, independent of measured RNA.
    residual_capacity = 0.5
    for target in (0.2, 0.5, 0.6):
        condition = f"reference flux {target:g} of control Vmax"
        baseline = target / (1 - target)
        row(condition, "control substrate at reference flux", baseline, "S/K")
        if residual_capacity <= target:
            row(condition, "finite substrate rescue exists", 0, "boolean")
            continue
        required = target / (residual_capacity - target)
        assert isclose(residual_capacity * required / (1 + required), target)
        row(condition, "finite substrate rescue exists", 1, "boolean")
        row(condition, "substrate required with half capacity", required, "S/K")
        row(condition, "required over baseline", required / baseline, "fold")


if __name__ == "__main__":
    main()
