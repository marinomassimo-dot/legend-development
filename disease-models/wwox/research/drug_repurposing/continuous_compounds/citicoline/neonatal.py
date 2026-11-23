"""Recalculate the two binary seizure comparisons in the neonatal HIE study (Table 4)."""
import csv
from math import comb, erfc, sqrt
from pathlib import Path

def evaluate(events_a, n_a, events_b, n_b):
    total_events = events_a + events_b
    total = n_a + n_b
    risk_difference = events_a / n_a - events_b / n_b
    pooled = total_events / total
    chi_p = erfc(abs(risk_difference) / sqrt(2 * pooled * (1-pooled) * (1/n_a+1/n_b)))
    def numerator(x):
        return comb(n_a, x) * comb(n_b, total_events - x)
    support = range(max(0, total_events-n_b), min(total_events,n_a)+1)
    observed = numerator(events_a)
    fisher_p = sum(numerator(x) for x in support if numerator(x) <= observed) / comb(total, total_events)
    return 100*risk_difference, chi_p, fisher_p

if __name__ == '__main__':
    with Path(__file__).with_name('neonatal.tsv').open('w') as stream:
        writer=csv.writer(stream,delimiter='\t',lineterminator='\n')
        writer.writerow(['outcome','citicoline_events','citicoline_n','control_events','control_n','published_p','risk_difference_pp','pearson_two_sided_p','fisher_two_sided_p'])
        for outcome,a,b,p in [('during_treatment',8,15,0.04),('after_discharge',2,11,0.006)]:
            writer.writerow([outcome,a,40,b,40,p,*[round(x,6) for x in evaluate(a,40,b,40)]])
