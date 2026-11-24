"""Reproduce the adult plasma comparison and conditional receptor-mixture model."""
import argparse
import csv
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
NUMBERS = HERE.parents[1] / 'gabaa_subtype_adv004_20261114/output/numbers.tsv'
# Within a subtype: parent EC50, parent maximal response, metabolite EC50, metabolite maximal response.
models = {
    'Hammer': ('N041 N042 N049 N050', 'N043 N044 N051 N052'),
    'Ralvenius': ('N012 N013 N023 N024', 'N015 N016 N026 N027'),
}
with NUMBERS.open() as stream:
    source = {r['row_id']: r for r in csv.DictReader(stream, delimiter='\t')}

# VanLandingham Table 4. Each entry is (parent, metabolite), ordered day 1, day 33.
auc = [(2690, 18300), (2840, 48400)]
peak = [(330, 2060), (329, 4570)]
mw = (300.74, 286.71)  # g/mol
unbound = (.215, .275)  # FDA clinical pharmacology review, section 2.2.4.3

def to_free_molar(values):
    return [v * fraction / mass for v, fraction, mass in zip(values, unbound, mw)]

def parameters(study, ids, uncertainty):
    """Return possible values per parameter. Only the sensitivity table uses extremes."""
    choices = []
    for row_id in ids.split():
        row = source[row_id]
        center = float(row['value_as_printed'])
        dispersion = row['dispersion_type_and_value'].split()
        if row['unit'] == 'nM':
            center *= .001
            # The Hammer audit gives a standard error for minus log10 molar EC50.
            factor = 10 ** float(dispersion[3])
            limits = (center / factor, center * factor)
        else:
            if study == 'Hammer':
                center -= 100  # percent of control -> percent above control
            spread = float(dispersion[1])
            limits = (center - spread, center + spread)
        choices.append(limits if uncertainty else (center,))
    return list(product(*choices))

def response(parent, metabolite, parameters):
    kp, ep, km, em = parameters
    x, y = parent / kp, metabolite / km
    return (ep * x + em * y) / (1 + x + y)

def match_alpha1(target, ratio, parameters):
    kp, ep, km, em = parameters
    denominator = (ep - target) / kp + ratio * (em - target) / km
    if denominator <= 0:
        raise ValueError('Requested matched effect is unattainable')
    parent = target / denominator
    return parent, ratio * parent

def contrast(target, ratios, a1, a2):
    mixtures = [match_alpha1(target, ratio, a1) for ratio in ratios]
    assert all(abs(response(*pair, a1) - target) < 1e-8 for pair in mixtures)
    start, end = [response(*pair, a2) for pair in mixtures]
    return [*mixtures[0], *mixtures[1], start, end, end - start]

def table(mode):
    ratios = [m / p for p, m in map(to_free_molar, auc)]
    if mode == 'exposure':
        yield ['day', 'total_parent_AUC_ng_h_mL', 'total_met_AUC_ng_h_mL',
               'est_free_met_parent_molar_AUC_ratio', 'est_free_parent_Cmax_uM', 'est_free_met_Cmax_uM']
        for day, area, ratio, maxima in zip((1, 33), auc, ratios, peak):
            yield [day, *area, ratio, *to_free_molar(maxima)]
        return

    uncertainty = mode == 'corners'
    base = ['model', 'relative_partition', 'matched_alpha1_pct']
    yield base + (['corner_count', 'min_delta_alpha2_pp', 'max_delta_alpha2_pp'] if uncertainty else
                  ['parent_d1_uM', 'met_d1_uM', 'parent_d33_uM', 'met_d33_uM',
                   'alpha2_d1_pct', 'alpha2_d33_pct', 'delta_alpha2_pp'])
    for study, (ids1, ids2) in models.items():
        a1_values = parameters(study, ids1, uncertainty)
        a2_values = parameters(study, ids2, uncertainty)
        for partition, target in product((.25, 1, 4), (20, 40)):
            tissue_ratios = [r * partition for r in ratios]
            results = [contrast(target, tissue_ratios, a1, a2)
                       for a1, a2 in product(a1_values, a2_values)]
            deltas = [row[-1] for row in results]
            yield [study, partition, target, *([len(deltas), min(deltas), max(deltas)] if uncertainty else results[0])]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('table', choices=('exposure', 'mixture', 'corners'), default='mixture', nargs='?')
    for row in table(parser.parse_args().table):
        print(*(f'{x:.4f}' if isinstance(x, float) else x for x in row), sep='\t')
