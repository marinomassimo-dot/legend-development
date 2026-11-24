"""Cross-matrix sensitivity calculations; no dose or efficacy prediction."""
import csv
import sys

# Values transcribed from the cited study's total plasma parent-CBD data.
exposures = [
    ('Brstilo_2023', 'trough_median', 48.2),
    ('Brstilo_2023', 'trough_range_low', 3.5),
    ('Brstilo_2023', 'trough_range_high', 366.3),
    ('Caceres_Guido_2020', 'serial_peak_median', 49.6),
    ('Caceres_Guido_2020', 'serial_peak_range_low', 14.4),
    ('Caceres_Guido_2020', 'serial_peak_range_high', 302.0),
    ('Wheless_2019', 'day10_peak_GM_lower_cohort', 91.0),
    ('Wheless_2019', 'day10_peak_GM_middle_cohort', 126.0),
    ('Wheless_2019', 'day10_peak_GM_higher_cohort', 314.5),
]
weight = 314.46  # CBD molecular weight in g/mol
transporter = 0.124  # nominal micromolar at half-maximal microglial adenosine influx inhibition
slice_bath = 10.0  # nominal micromolar in Hu, Fig. 3-9
out = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
out.writerow(('source', 'total_exposure_summary', 'ng_per_mL', 'assumed_plasma_free_fraction',
              'estimated_free_plasma_nM', 'nominal_microglia_IC50_over_estimate',
              'nominal_slice_bath_over_estimate'))
for source, measure, total in exposures:
    for fraction in (0.01, 0.05, 0.06):
        free = total * fraction / weight
        out.writerow((source, measure, total, fraction, f'{1000*free:.3f}',
                      f'{transporter/free:.2f}', f'{slice_bath/free:.1f}'))
