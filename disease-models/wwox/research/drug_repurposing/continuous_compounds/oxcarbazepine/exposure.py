"""Recalculate group exposure shares from FDA study 2093-127, printed pages 53–56."""
import csv
import sys
rows = [
    ("plasma", 7, [164726,39034,7135], [16162,4039,1990]),
    ("CSF", 6, [86187,23996,2485], [7566,2146,448]),
]
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(["matrix","n","analyte","auc12_ng_h_ml","cmax_ng_ml","interval_mean_ng_ml","mass_auc_share_pct"])
for matrix,n,auc,peak in rows:
    for name,area,maximum in zip(["S-licarbazepine","R-licarbazepine","oxcarbazepine"],auc,peak):
        out.writerow([matrix,n,name,area,maximum,round(area/12,2),round(100*area/sum(auc),2)])
