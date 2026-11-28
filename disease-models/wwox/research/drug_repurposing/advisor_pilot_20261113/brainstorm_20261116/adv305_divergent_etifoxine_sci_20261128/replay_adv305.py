"""ADV-305 step 1 replay: vehicle-normalised effects of five ligands in PMID 40561753 (JPET 2025), two readings.
Inputs are PRINTED means from sections 3.3 and 3.4 and vehicle baselines READ FROM PLOT (FIGURE_EXTRACT_...md). Usage: python3 replay_adv305.py"""
zf = {  # zebrafish Scn1Lab MEA, Fig 3: vehicle (DMSO) read from plot; treated printed
 'spikes': (818, dict(etifoxine=92.33, XBD173=12.71, PK11195=152.2, STP=26.25, Ro5=671)),
 'rate_Hz': (0.0231, dict(etifoxine=0.002236, XBD173=0.0003309, PK11195=0.004325, STP=0.0006836, Ro5=0.0174)),
}
cu = {  # rat cortical cultures under 4-AP, Fig 4, % of baseline: 4-AP alone printed for spikes, read for rate; treated printed
 'spikes': (410.5, dict(etifoxine=90.01, XBD173=222.2, PK11195=89.54, STP=29.04, Ro5=321.1)),
 'rate': (420.0, dict(etifoxine=53.85, XBD173=243.8, PK11195=92.92, STP=30.31, Ro5=292.0)),
}
def show(title, rows):
    print(title)
    for p, vals in rows.items():
        print(' ', p, '  '.join('%s %.3f' % (k, v) for k, v in vals.items()))
res_zf = {p: {k: v / veh for k, v in d.items()} for p, (veh, d) in zf.items()}
blk_zf = {p: {k: 1 - v for k, v in d.items()} for p, d in res_zf.items()}
blk_cu = {p: {k: (veh - v) / (veh - 100.0) for k, v in d.items()} for p, (veh, d) in cu.items()}
res_cu = {p: {k: 1 - v for k, v in d.items()} for p, d in blk_cu.items()}
show('zebrafish residual = treated/vehicle', res_zf); show('zebrafish share blocked', blk_zf)
show('culture share of 4-AP increase blocked', blk_cu); show('culture residual = 1 - blocked', res_cu)
print('sensitivity: zebrafish vehicle baseline +-25 percent moves residuals by x0.8 to x1.33 and no residual ratio between ligands.')
