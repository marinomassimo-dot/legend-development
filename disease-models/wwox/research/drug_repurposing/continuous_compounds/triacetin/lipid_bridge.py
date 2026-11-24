"""Recalculate the triacetin study contrasts from its original open-access JATS table."""
import csv
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def main(article):
    doc = ET.parse(article)
    assert doc.findtext('.//article-id[@pub-id-type="pmid"]') == '20464498'
    table = next(t for t in doc.findall('.//table-wrap') if t.findtext('label', '').split() == ['Table', '3'])
    gc = next(row for row in table.findall('.//tr') if row[0].text == 'GC*')
    groups = []
    for cell in gc[1:]:
        numbers = ''.join(cell.itertext()).replace(',', '').split('±')
        groups.append(tuple(float(n) for n in numbers))
    (wt, _), (treated, sem_t), (untreated, sem_u) = groups
    difference = treated - untreated
    ratio = treated / untreated
    output = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    output.writerow(['comparison', 'value', 'unit'])
    def emit(label, value, unit):
        output.writerow([label, f'{value:.5f}', unit])
    emit('female_GC_mean_difference', difference, 'reported normalized intensity units')
    emit('female_GC_treated_over_untreated', ratio, 'ratio')
    emit('female_GC_change_over_WT_minus_untreated', difference / (wt - untreated), 'fraction of group mean gap')
    emit('total_spot_signal_if_GC_and_protein_fixed', 1 / ratio, 'hypothetical treated/control ratio')
    emit('unpaired_difference_over_SE', difference / math.hypot(sem_t, sem_u), 'SE units')
    # Two-sided t cutoff at 0.05, assuming all n observations are true pairs.
    for n, critical in [(4, 3.182446), (5, 2.776445)]:
        rho = (sem_t**2 + sem_u**2 - (difference/critical)**2) / (2*sem_t*sem_u)
        emit(f'minimum_correlation_under_{n}_true_pairs', rho, 'correlation')
    # Results, Rotarod treadmill performance, female group means in seconds.
    normal, supplied, unsupplied = 157, 76, 27
    emit('female_motor_treated_over_untreated', supplied / unsupplied, 'ratio')
    emit('female_motor_change_over_WT_minus_untreated', (supplied-unsupplied)/(normal-unsupplied), 'fraction of group mean gap')
    # Madhavarao et al. PMID 15784740 Table 1, genotype contrast without treatment.
    emit('ASPA_null_over_WT_new_myelin_lipid_label', 18991/26946, 'ratio of cpm/mg myelin protein')
    emit('ASPA_null_over_WT_liver_lipid_label', 60499/60056, 'ratio of cpm/mg tissue protein')


if __name__ == '__main__':
    main(Path(sys.argv[1]))
