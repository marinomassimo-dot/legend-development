"""Recompute lysine contrasts on existing negative-ion integrations, omitting each pool."""
import csv
import json
import math
from pathlib import Path
from statistics import mean
import sys

source = Path(__file__).resolve().parents[2] / "verification_it27_p2_20261104" / "results"
with (source / "v_areas_long.tsv").open() as fh:
    rows = [r for r in csv.DictReader(fh, delimiter="\t")
            if r["target"] == "lysine" and r["assay_name"].endswith("_KDExp")]
panel = json.loads((source / "v_panel_factors.json").read_text())["panel"]
out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
out.writerow(("background", "ppm", "normalization", "control_pools", "KD_pools",
              "KD_over_control", "omit_one_min", "omit_one_max"))
for background in ("LacZ", "AB42"):
    for ppm in ("5", "10"):
        selected = [r for r in rows if r["group_amyloid"] == background and r["ppm"] == ppm]
        for norm in ("raw", "TIC", "panel"):
            groups = {"RNAi Control": [], "Wwox RNAi": []}
            for r in selected:
                denominator = {"raw": 1, "TIC": float(r["tic"]), "panel": panel[r["file"]]}[norm]
                groups[r["group_wwox"]].append(math.log2(float(r["area"]) / denominator))
            ctrl, kd = groups["RNAi Control"], groups["Wwox RNAi"]
            if len(ctrl) != 5 or len(kd) != 5 or len({r["file"] for r in selected}) != 10:
                raise ValueError("Unexpected pool structure")
            ratio = 2 ** (mean(kd) - mean(ctrl))
            omit = [2 ** (mean(kd) - mean(ctrl[:i] + ctrl[i+1:])) for i in range(len(ctrl))]
            omit += [2 ** (mean(kd[:i] + kd[i+1:]) - mean(ctrl)) for i in range(len(kd))]
            out.writerow((background, ppm, norm, len(ctrl), len(kd), f"{ratio:.4f}",
                          f"{min(omit):.4f}", f"{max(omit):.4f}"))
