"""Decompose the published PFC array summaries. Run with Python 3."""
import csv
import sys

# Huang et al., Fig. 3A/B and corresponding Results, PMID 16498613.
# Nominal bath µM, reported inhibition (%) of total amplitude, mean responsive sites.
ROWS = [(0, 0, 34), (3, 16.5, 28.5), (10, 47.5, 19.5), (30, 65.9, 9.5), (100, 87.9, 5)]


def main():
    writer = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    writer.writerow(['bath_uM', 'total_amplitude_inhibition_pct', 'mean_detected_sites',
                     'total_fraction', 'site_count_fraction', 'ratio_of_summaries_per_site'])
    for concentration, inhibition, count in ROWS:
        total = 1 - inhibition / 100
        sites = count / ROWS[0][2]
        writer.writerow([concentration, inhibition, count, f'{total:.5f}', f'{sites:.5f}',
                         f'{total / sites:.5f}'])


if __name__ == '__main__':
    main()
