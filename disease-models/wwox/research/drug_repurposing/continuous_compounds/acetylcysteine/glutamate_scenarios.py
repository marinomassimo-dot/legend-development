"""Illustrate ambiguity in predicted tonic glutamate under linear, unsaturated clearance."""
import csv
from pathlib import Path
from statistics import mean

HERE = Path(__file__).parent

def read(name):
    with (HERE/name).open() as f:
        return list(csv.DictReader(f, delimiter='\t'))

def main():
    rows = []
    def add(model, omit, export, clearance):
        crossover = (1 - clearance) / (1 - export) if export != 1 else ''
        for fraction in (0, 0.25, 0.5, 0.75, 1):
            fold = (1 + fraction*(export-1)) / clearance
            rows.append([model,omit,export,clearance,fraction,fold,crossover])
    records = read('libraries.tsv')
    for model in sorted({r['model'] for r in records}):
        matched = [r for r in records if r['model']==model]
        def ratio(gene, omit):
            def avg(arm):
                return mean(float(r['expression']) for r in matched if r['gene']==gene and r['arm']==arm and r['library']!=omit)
            return avg('KO') / avg('WT')
        for omit in ['none']+sorted({r['library'] for r in matched}):
            add(model,omit,ratio('SLC7A11',omit),ratio('SLC1A2',omit))
    nuclei = read('nuclei.tsv')
    for group in ('astro','Aqp4_and_Aldh1l1'):
        rates = {(r['pool'],r['gene']):float(r['CPM']) for r in nuclei if r['subset']==group}
        add(group,'none',rates['ko','Slc7a11']/rates['ctrl','Slc7a11'],rates['ko','Slc1a2']/rates['ctrl','Slc1a2'])
    with (HERE/'glutamate_scenarios.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t',lineterminator='\n')
        w.writerow(['model','omitted_library','export_proxy_ratio','clearance_proxy_ratio','baseline_exchange_fraction','hypothetical_glutamate_fold','crossing_fraction'])
        w.writerows(rows)

if __name__ == '__main__':
    main()
