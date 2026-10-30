#!/usr/bin/env python3
"""Collect tests_<label>.json files of the engine into one TSV (one row per seed set) for the README.

  summarize_tests.py --dir results --out results/tests_summary.tsv
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, csv, glob, json, os
ap = argparse.ArgumentParser(); ap.add_argument("--dir", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
cols = ["label", "seed_units", "defined", "uncertain", "examined", "nonzero_families_rawQ", "T1_PASS", "T2_PASS", "T2a_rho_median", "T2a_top100_overlap_median", "T2b_shuffle_rho_median",
        "T2c_decoy_rho", "T2_Z_rho_median", "T2_Z_top100_overlap_median", "families_absz_gt3", "T3_identity_PASS", "T3_norm_ingraph_rho", "T3_probes_examined", "T3_probes_with_own_target_seed",
        "T3_probes_flagged", "T4_rho_netind_direct", "T4_n_direct_any", "T4_rawQ_new", "T4_rawQ_new_specific", "T4_rawQ_outcome", "T4_Z_new", "T4_Z_new_specific", "T4_Z_outcome", "T5_PASS"]
rows = []
for f in sorted(glob.glob(os.path.join(a.dir, "tests_*.json"))):
    d = json.load(open(f)); t1, t2, t3, t4, t5 = d["T1"], d["T2"], d["T3"], d["T4"], d["T5"]
    rows.append([d["label"], d["n_seed_units"], d["n_defined"], d["n_uncertain"], d["examined_families"], t2["a_families_nonzero"], t1["PASS"], t2["PASS"],
                 round(t2["a_spearman_real_vs_null_median"], 3), t2["a_top100_overlap_median"],
                 "NA" if t2["b_sign_shuffle_median_spearman"] is None else round(t2["b_sign_shuffle_median_spearman"], 3), round(t2["c_decoy_spearman_with_real"], 3),
                 round(t2["z_spearman_real_vs_null_median"], 3), t2["z_top100_overlap_median"], t2["a_families_abs_z_gt3"], t3["PASS_identity"],
                 round(t3["b_norm_all_targets_vs_ingraph_only_spearman"], 5), t3["c_probes_examined"], t3["c_probes_with_own_target_seed"], t3["c_probes_flagged"],
                 round(t4["spearman_NETIND_vs_DIRECT_examined"], 4), t4["n_direct_any_action_families"], t4["raw_Q_top100"]["n_new"], t4["raw_Q_top100"]["n_new_and_seed_specific_z_gt3"],
                 t4["raw_Q_outcome"], t4["Z_top100"]["n_new"], t4["Z_top100"]["n_new_and_seed_specific_z_gt3"], t4["Z_outcome"], t5["PASS"]])
with open(a.out, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(cols); w.writerows(rows)
print(len(rows), "sets ->", a.out)
