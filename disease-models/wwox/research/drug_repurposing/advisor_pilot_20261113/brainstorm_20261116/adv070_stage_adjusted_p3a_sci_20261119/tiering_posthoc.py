"""ADV-070 POST-HOC reading (not pre-registered): tiers built from out/stage_adjusted_by_contrast.tsv and out/stage_scores_per_animal.tsv.
    python3 tiering_posthoc.py run <adv070_dir>
Tier A: C_S label STANDS and, in at least two of the three hippocampal contrasts, |delta| >= 0.5 with the genotype term c keeping the sign of delta and |c| >= 0.3.
Tier B: C_S label STANDS but fewer than two hippocampal contrasts retain. Tier C: C_S NO_SHIFT (hippocampal retention shown). Tier D: C_S UNSTABLE.
Also prints the stage-score separation between arms per contrast (the leverage of the covariate)."""
import sys
if len(sys.argv) != 3 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv
from pathlib import Path
D = Path(sys.argv[2])
rows = list(csv.DictReader(open(D / "out/stage_adjusted_by_contrast.tsv"), delimiter="\t"))
sc = list(csv.DictReader(open(D / "out/stage_scores_per_animal.tsv"), delimiter="\t"))
lev = {}
for r in sc:
    lev.setdefault(r["contrast"], {}).setdefault(r["arm"], []).append(float(r["stage_score_full_covariate"]))
with open(D / "out/stage_score_separation.tsv", "w") as f:
    f.write("contrast\tcase_mean\tcontrol_mean\tseparation_case_minus_control\tn_case\tn_control\n")
    for c, d in lev.items():
        m = lambda v: sum(v) / len(v)
        f.write(f"{c}\t{m(d['case']):.3f}\t{m(d['control']):.3f}\t{m(d['case'])-m(d['control']):.3f}\t{len(d['case'])}\t{len(d['control'])}\n")
        print(c, round(m(d['case']), 3), round(m(d['control']), 3), round(m(d['case']) - m(d['control']), 3))
by = {}
for r in rows:
    by.setdefault(r["item"], {})[r["contrast"]] = r
out = []
for item, d in by.items():
    cs = d.get("C_S")
    if not cs or cs["status"] != "measured":
        continue
    kept = []
    for k in ("H_S", "H_N", "H_null"):
        r = d.get(k)
        if r and r["status"] == "measured" and r["raw_delta_log2"] != "":
            dl, c = float(r["raw_delta_log2"]), float(r["genotype_term_c"])
            kept.append(abs(dl) >= 0.5 and dl * c > 0 and abs(c) >= 0.3)
    n_kept = sum(kept)
    lab = cs["label"]
    tier = {"STANDS": "A" if n_kept >= 2 else "B", "NO_SHIFT": "C", "UNSTABLE": "D"}.get(lab, "?")
    out.append((tier, item, cs["category"], cs["raw_delta_log2"], cs["genotype_term_c"], cs["background_flag_p3a_gt_0.25"], n_kept))
out.sort()
with open(D / "out/tiered_reading_posthoc.tsv", "w") as f:
    f.write("tier\titem\tcategory\tC_S_delta\tC_S_c\tbackground_flag_p3a\thippocampal_contrasts_retaining_of_3\n")
    for o in out:
        f.write("\t".join(str(x) for x in o) + "\n")
for o in out:
    print("\t".join(str(x) for x in o))
