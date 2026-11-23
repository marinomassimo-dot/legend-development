"""Sensitivity of the incremental BHB response when initial exposure is nonzero."""
import csv
from pathlib import Path


def fraction(concentration, hill):
    return concentration**hill / (0.7**hill + concentration**hill)


def scenarios():
    # Pan et al., adult occipital tissue at baseline and day 3, in micromolar.
    for scale in [0.01, 0.1, 1]:
        low, high = 50 * scale, 980 * scale
        for hill in [0.7, 1, 1.5]:
            before, after = fraction(low,hill), fraction(high,hill)
            # At -60 mV Manville et al. report a maximal 3.5-fold current.
            rel = (1 + 2.5 * after)/(1 + 2.5 * before) - 1
            yield [scale,hill,low,high,round(100*before,3),round(100*after,3),
                   round(100*(after-before),3),round(100*rel,3)]


if __name__ == '__main__':
    with Path(__file__).with_name('saturation.tsv').open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow(['assumed_local_to_tissue_ratio','assumed_hill_slope','baseline_uM','higher_uM','baseline_pct_max_augmentation','higher_pct_max_augmentation','increment_pp','relative_current_increase_pct'])
        writer.writerows(scenarios())
