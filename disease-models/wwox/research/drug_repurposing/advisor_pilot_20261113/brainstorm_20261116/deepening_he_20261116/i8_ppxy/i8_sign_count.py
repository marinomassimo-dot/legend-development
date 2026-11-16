#!/usr/bin/env python3
"""I8 v3: expected directions per PY-motif candidate and sign variant, written down here BEFORE the count, and counted per independent feature group.

    python3 i8_sign_count.py --out <dir>        (deterministic; no files read; writes i8_sign_predictions.tsv, sign_fit_summary.tsv, sign_fit_by_group.tsv)

Features and groups (SCI's second reading of the held paper, Table 1): rest_conductance = resting potential and input resistance (two readouts of one change); deflection = sag and rebound (two readouts of one deep
hyperpolarising deflection); spike_amplitude = pyramidal AP amplitude and AP threshold (the amplitude is partly a consequence of a depolarised rest); interneuron_amplitude = interneuron AP amplitude (the one independent feature).
Observed (S-KO against control): RMP +1 (depolarised), Rin +1, sag +1, rebound +1, AP amplitude -1, threshold 0 (not different), interneuron AP amplitude -1.
M+ = surface level up, M- = down; M- directions are the exact opposite of M+ by construction. A channel-feature pair the channel cannot carry is `uninformative` (no direction is scored): Kcnh7 and Kcnt2 for rest_conductance
(ERG-type channels open positive to rest; Slack is Na+-activated; ASSUMED general physiology, SCI's reading). Not medical advice.
"""
import argparse, csv
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--out"); a = ap.parse_args()
if not a.out:
    ap.print_help(); raise SystemExit(0)
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
GROUP = {"pyr_RMP": "rest_conductance", "pyr_Rin": "rest_conductance", "pyr_sag": "deflection", "pyr_rebound": "deflection", "pyr_AP_amp": "spike_amplitude", "pyr_AP_threshold": "spike_amplitude", "int_AP_amp": "interneuron_amplitude"}
OBS = {"pyr_RMP": 1, "pyr_Rin": 1, "pyr_sag": 1, "pyr_rebound": 1, "pyr_AP_amp": -1, "pyr_AP_threshold": 0, "int_AP_amp": -1}
P = {  # M+ direction; "u" = uninformative
 "Scn1a (Nav1.1, PPSY 1983)": ({"pyr_AP_amp": 1, "pyr_AP_threshold": -1, "int_AP_amp": 1}, "more sodium channels: larger, lower-threshold spikes; Nav1.1 concentrated in interneurons (ASSUMED)"),
 "Scn2a (Nav1.2, PPSY 1973)": ({"pyr_AP_amp": 1, "pyr_AP_threshold": -1}, "more sodium channels in pyramidal neurons (ASSUMED)"),
 "Hcn1 (HCN1, PPVY 654)": ({"pyr_RMP": 1, "pyr_Rin": -1, "pyr_sag": 1, "pyr_rebound": 1}, "Ih open at rest: depolarises, lowers input resistance, raises sag and rebound (general physiology); sag in mV is not an Ih measurement here (SCI)"),
 "Kcnh7 (Kv11.3, PPAY 1067)": ({"pyr_RMP": "u", "pyr_Rin": "u"}, "ERG-type channels open positive to rest: uninformative for resting features (SCI; ASSUMED)"),
 "Kcnt2 (Slack-B, PPRY 12)": ({"pyr_RMP": "u", "pyr_Rin": "u"}, "Na+-activated K+ channel, active during firing: uninformative for resting features (SCI; ASSUMED)"),
 "Trpm3 (TRPM3, PPDY 573, PPTY 1515)": ({"pyr_RMP": 1, "pyr_Rin": -1}, "more non-selective cation conductance (ASSUMED)"),
}
rows = []
for c, (d, basis) in P.items():
    for sign, m in (("M+ adaptor (surface up)", 1), ("M- shield (surface down)", -1)):
        for f, v in d.items():
            pred = "uninformative" if v == "u" else v * m
            rows.append({"candidate": c, "sign_variant": sign, "feature": f, "independent_feature_group": GROUP[f], "predicted_direction": pred, "observed_direction": OBS[f], "basis": basis})
w = csv.DictWriter((out / "i8_sign_predictions.tsv").open("w", newline=""), list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)

def status(rr):
    inf = [r for r in rr if r["predicted_direction"] != "uninformative"]
    if not inf: return "uninformative"
    seen = [r for r in inf if r["observed_direction"] != 0]
    if not seen: return "predicted_change_not_seen"
    fit = sum(r["predicted_direction"] == r["observed_direction"] for r in seen); opp = sum(r["predicted_direction"] == -r["observed_direction"] for r in seen)
    return "fit" if fit == len(seen) else ("oppose" if opp == len(seen) else "mixed")
G = ["rest_conductance", "deflection", "spike_amplitude", "interneuron_amplitude"]
with open(out / "sign_fit_by_group.tsv", "w", newline="") as fh:
    wr = csv.writer(fh, delimiter="\t", lineterminator="\n"); wr.writerow(["candidate", "sign_variant"] + G + ["groups_fit", "groups_oppose", "groups_mixed"])
    for c in P:
        for sign in ("M+ adaptor (surface up)", "M- shield (surface down)"):
            st = [status([r for r in rows if r["candidate"] == c and r["sign_variant"] == sign and r["independent_feature_group"] == g]) for g in G]
            wr.writerow([c, sign] + st + [st.count("fit"), st.count("oppose"), st.count("mixed")])
with open(out / "sign_fit_summary.tsv", "w", newline="") as fh:    # per feature (v2 view), informative features only
    wr = csv.writer(fh, delimiter="\t", lineterminator="\n"); wr.writerow(["candidate", "sign_variant", "informative_features", "fit", "oppose", "predicted_change_not_seen"])
    for c in P:
        for sign in ("M+ adaptor (surface up)", "M- shield (surface down)"):
            rr = [r for r in rows if r["candidate"] == c and r["sign_variant"] == sign and r["predicted_direction"] != "uninformative"]
            wr.writerow([c, sign, len(rr), sum(r["observed_direction"] != 0 and r["predicted_direction"] == r["observed_direction"] for r in rr), sum(r["observed_direction"] != 0 and r["predicted_direction"] == -r["observed_direction"] for r in rr), sum(r["observed_direction"] == 0 for r in rr)])
print(open(out / "sign_fit_by_group.tsv").read())
