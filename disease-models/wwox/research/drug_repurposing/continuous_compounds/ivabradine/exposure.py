"""Sensitivity of the reported recombinant HCN curves to two rat concentration estimates."""
import csv
from math import isclose
from pathlib import Path

# Bucchi et al., Figure 1C: half-block in micromolar and dimensionless Hill factor.
PARAMETERS = {'mouse_HCN1': (0.94,1.2), 'human_HCN4': (2.0,0.8)}
# Iacone et al., Figure 1D (2 h; unbound brain, nM); other rows are assay landmarks.
SAMPLES = [('rat_parent_alone',4.7),('rat_combination_comparator',184),
           ('published_trace_concentration',300),('one_micromolar',1000)]


def block(concentration, half, slope):
    odds = (concentration / half)**slope
    return odds / (1 + odds)


def run(output):
    k1,h1 = PARAMETERS['mouse_HCN1']
    k4,h4 = PARAMETERS['human_HCN4']
    cross = (k1**h1 / k4**h4)**(1 / (h1-h4))
    assert isclose(block(cross,k1,h1), block(cross,k4,h4))
    with output.open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow(['scenario','concentration_nM','channel','reported_curve_block_percent','unit_slope_sensitivity_percent'])
        for name,nm in [*SAMPLES,('positive_curve_crossing',1000*cross)]:
            for channel,(half,slope) in PARAMETERS.items():
                concentration=nm/1000
                writer.writerow([name,round(nm,3),channel,round(100*block(concentration,half,slope),3),
                                 round(100*block(concentration,half,1),3)])


if __name__ == '__main__':
    run(Path(__file__).with_name('exposure.tsv'))
