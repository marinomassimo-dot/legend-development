"""Translate oral population-PK reference concentrations and recount M2 assay comparisons."""
from math import comb
from pathlib import Path
from single_cells import write

OUT = Path(__file__).with_name('results')
# Parent only, molecular mass (g/mol) and CDD population-PK estimates (ng/mL).
MASS = 332.53
PK = [('2_to_under_6', 85, 247), ('6_to_under_12', 84, 269),
      ('12_to_under_18', 84, 293), ('adult', 84, 292)]


def fisher_upper(control, treated, n):
    total = control + treated
    return sum(comb(n, x) * comb(n, total - x) for x in range(treated, min(total, n) + 1)) / comb(2*n, total)


def main():
    rows = []
    for group, trough, peak in PK:
        for phase, level in [('trough', trough), ('peak', peak)]:
            for fraction in (0.001, 0.007, 0.010, 0.011):
                free = level * 1000 / MASS * fraction
                for target in (10, 20, 100):
                    for medium_fraction in (0.1, 0.5, 1):
                        required = target * medium_fraction / free
                        rows.append((group, phase, level, fraction, target, medium_fraction, free, required))
    write(OUT/'parent_exposure.tsv',
          'age_group phase total_parent_ng_per_mL plasma_free_fraction assay_nominal_nM '
          'assay_free_fraction plasma_unbound_nM required_unbound_brain_to_plasma_ratio'.split(), rows)
    # Aberrant metaphases inferred uniquely from the displayed percentages at n=300.
    conditions = {'4h_no_S9': (1, [(64,3,96),(128,5,68),(256,9,71),(333,6,51)]),
                  '4h_plus_S9': (2, [(64,1,85),(128,5,69),(256,13,49)]),
                  '21h_no_S9': (2, [(32,5,79),(64,5,56),(128,5,57)])}
    rows = []
    for condition, (ctrl, levels) in conditions.items():
        for concentration, case, mitotic_index in levels:
            rows.append((condition, concentration, ctrl, case, 300, mitotic_index,
                         100 * (case-ctrl)/300, fisher_upper(ctrl, case, 300)))
    write(OUT/'metabolite_aberrations.tsv',
          'condition M2_ug_per_mL control_aberrant treated_aberrant metaphases_per_group '
          'relative_mitotic_index_pct risk_difference_pp fisher_one_sided_descriptive'.split(), rows)


if __name__ == '__main__':
    main()
