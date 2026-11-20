"""ADV-121: merge the raw outputs of measure_bars.py for Fig S7B and S7D into measurements_adv121/figS7B_D.json,
adding a second calibration (B2: two-endpoint tick scale, first and last tick) next to the all-tick fit (A).
The 200 ppi panels have no label-centre calibration (small mode), so B2 replaces it.
Usage: python3 -I make_s7bd_json.py"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
out = {'source': 'Obeid 2026 supplement Fig S7B (Iba1) and S7D (GFAP), P20 knockout against wild type, percent area; mmc2.pdf page 26 at 200 ppi; '
                 'crops 300x340+1200+100 (B) and 300x340+1200+430 (D); ADV-120 measure_bars.py with crop B (288, 50) and crop D (281, 57), minh 12, small mode',
       'legend': 'percentage of area in KO compared to WT; error bars mean +/- SD; n not printed'}
for nm, f, ticks in (('S7B_Iba1', 'figS7B.json', [0, 2, 4, 6, 8, 10]), ('S7D_GFAP', 'figS7D.json', [0, 10, 20, 30])):
    d = json.load(open(os.path.join(HERE, 'measurements_adv121', f)))
    yt = d['y_ticks_px_found']              # top tick first (largest value), bottom tick last (value 0)
    scale = (ticks[-1] - ticks[0]) / (yt[-1] - yt[0])     # units per pixel, positive
    bars = []
    for b in d['bars_left_to_right']:
        vB2 = ticks[0] + (yt[-1] - b['top_row']) * scale
        bars.append({'colour': b['colour'], 'value_A': b['value_A'], 'value_B2_endpoint_scale': round(vB2, 2),
                     'cap_minus_top_A': b['cap_minus_top_A']})
    out[nm] = {'ticks_px': yt, 'bars': bars}
json.dump(out, open(os.path.join(HERE, 'measurements_adv121', 'figS7B_D.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in out.items() if k.startswith('S7')}, indent=1))
