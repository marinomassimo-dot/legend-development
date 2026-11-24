"""Recompute a passive baseline from the held WWOX means and published IPSC contrasts."""
import csv
import math
import sys
from pathlib import Path

# Breton et al., Table 1, juvenile layer II/III putative pyramidal neurons.
TAU_MS = {'WT': 18.55, 'HT': 18.79, 'KO': 21.25}
# PMID, location, readout, nominal micromolar, baseline and exposed group summary, unit.
EVENTS = [
    ('19776733', 'CA1', 'sIPSC frequency', 100, 2.64, 4.69, 'Hz'),
    ('19776733', 'CA1', 'mIPSC frequency', 100, 0.19, 0.17, 'Hz'),
    ('27455251', 'CA1', 'sIPSC frequency', 100, 6.43, 2.58, 'Hz'),
    ('27455251', 'CA1', 'mIPSC frequency', 100, 1.95, 1.81, 'Hz'),
    ('27455251', 'DG', 'sIPSC frequency', 100, 1.20, 0.52, 'Hz'),
    ('27455251', 'DG', 'mIPSC frequency', 100, 0.32, 0.31, 'Hz'),
    ('34948401', 'CA1', 'sIPSC frequency', 50, 1.91, 1.94, 'Hz'),
    ('34948401', 'CA3c', 'sIPSC frequency', 50, 7.05, 4.05, 'Hz'),
]


# Rambeck et al., Table 3B. Unit is µg/mL parent in corrected cortical extracellular
# fluid. Keep the two extrema and the number of probes within each participant.
CORTICAL = [(1, 1, 1.06, 1.06), (3, 1, 0.77, 0.77), (8, 2, 0.59, 0.62),
            (13, 4, 0.57, 1.80), (21, 4, 0.59, 0.92)]
PARENT_MW = 256.09


def exposure_comparison(output):
    with (output/'exposure.tsv').open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['study_case', 'catheters', 'min_ug_ml', 'max_ug_ml',
                         'min_uM', 'max_uM'])
        for case, n, low, high in CORTICAL:
            writer.writerow([case, n, low, high, f'{1000*low/PARENT_MW:.4f}',
                             f'{1000*high/PARENT_MW:.4f}'])
    bounds = (min(row[2] for row in CORTICAL), max(row[3] for row in CORTICAL))
    with (output/'sodium.tsv').open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['exposure_uM', 'assumed_Ki_uM', 'duration_s', 'inactivated_eq_fraction',
                         'inactivated_bound_from_zero_fraction', 'resting_eq_upper_fraction'])
        for bound in bounds:
            concentration = bound*1000/PARENT_MW
            for ki in (7, 9):
                equilibrium = concentration/(concentration+ki)
                # Same-state two-rate illustration using the published association rate.
                rate = 10000*(concentration+ki)*1e-6
                for duration in (0.1, 1, 10):
                    occupied = equilibrium * -math.expm1(-rate*duration)
                    writer.writerow([f'{concentration:.4f}', ki, duration, f'{equilibrium:.6f}',
                                     f'{occupied:.6f}', f'{concentration/(1400+concentration):.6f}'])


def run(output):
    exposure_comparison(output)
    with (output/'passive.tsv').open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['genotype', 'tau_ms', 'Hz', 'interval_ms', 'fifth_over_first'])
        for genotype, tau in TAU_MS.items():
            for hz in (5, 10, 20, 40):
                interval = 1000/hz
                ratio = sum(math.exp(-n*interval/tau) for n in range(5))
                writer.writerow([genotype, tau, hz, interval, f'{ratio:.8f}'])
    with (output/'inhibition.tsv').open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(['PMID', 'region', 'readout', 'LTG_uM', 'before', 'after', 'units', 'change_pct_of_baseline'])
        for row in EVENTS:
            before, after = row[4:6]
            writer.writerow([*row, f'{100*(after/before-1):.2f}'])


if __name__ == '__main__':
    run(Path(sys.argv[1]))
