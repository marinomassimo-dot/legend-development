"""IT24 P4 addendum D: extracted-ion-chromatogram re-quantification of MTBLS12344 (negative mode mzXML). numpy only.
Usage: python3 -I mtbls_eic.py qc <neg_dir> <maf> <outdir>   |   python3 -I mtbls_eic.py samples <neg_dir> <s_file> <outdir>"""
import sys, re, base64, math, json, csv, os
import numpy as np
mode, NEG, aux, OUT = sys.argv[1:5]
FEAT = {"L-Lactate": 89.0245, "Citrate": 191.0199, "2-Hydroxyglutarate": 147.0299, "Itaconate": 129.0194}
PPM = 5e-6
def scans(path):
    txt = open(path, encoding="latin-1").read()
    for m in re.finditer(r'<scan\b(.*?)</scan>', txt, re.S):
        blk = m.group(1)
        if 'msLevel="1"' not in blk or 'polarity="-"' not in blk: continue
        rt = float(re.search(r'retentionTime="PT([0-9.eE+-]+)S"', blk).group(1))
        b = re.search(r'<peaks[^>]*>([^<]+)</peaks>', blk).group(1).strip()
        a = np.frombuffer(base64.b64decode(b), dtype=">f8").reshape(-1, 2)
        yield rt, a
def eic(path):
    rts, tic = [], []; E = {k: [] for k in FEAT}
    for rt, a in scans(path):
        rts.append(rt); tic.append(a[:, 1].sum())
        for k, mz in FEAT.items():
            s = a[np.abs(a[:, 0] - mz) <= mz * PPM]
            E[k].append(s[:, 1].sum())
    return np.array(rts), np.array(tic), {k: np.array(v) for k, v in E.items()}
def area(rts, y, lo, hi):
    w = (rts >= lo) & (rts <= hi)
    return float(np.trapezoid(y[w], rts[w])) if w.sum() >= 2 else float("nan")
if mode == "qc":
    r = list(csv.reader(open(aux), delimiter="\t")); h = r[0]
    pools = ["pooled_2_04", "pooled_2_05", "pooled_2_06", "pooled_2_07", "pooled_2_08", "pooled_2_09", "pooled_7", "pooled_8", "pooled_9", "pooled_10", "pooled_11", "pooled_12"]
    D = {p: eic(os.path.join(NEG, p + ".mzXML")) for p in pools}
    win = {}
    for k in FEAT:
        rts = np.arange(0.0, 1500.0, 0.5); stack = np.mean([np.interp(rts, D[p][0], D[p][2][k]) for p in pools], axis=0)
        m = [x for x in r[1:] if x[4] == k][0]; rt_maf = float(m[9])
        near = (rts > rt_maf - 60) & (rts < rt_maf + 60); apex = float(rts[near][np.argmax(stack[near])])
        win[k] = {"maf_rt": rt_maf, "apex_rt_from_pools": apex, "lo": apex - 15, "hi": apex + 15, "mz": FEAT[k]}
    json.dump(win, open(os.path.join(OUT, "mtbls_windows.json"), "w"), indent=1)
    # QC control: rank correlation of my pooled areas with deposited MAF pooled values; pool column order unknown, so test both labelings
    # MAF column <- raw file, from the assay sheet column pair "MS Assay Name" / "Raw Spectral Data File" (attempt 1 assumed an order and was wrong)
    MAFCOL = {"pooled_7": "Pool1_1", "pooled_8": "Pool1_2", "pooled_9": "Pool1_3", "pooled_10": "Pool1_4", "pooled_11": "Pool1_5", "pooled_12": "Pool1_6",
              "pooled_2_05": "Pool2_1", "pooled_2_06": "Pool2_2", "pooled_2_07": "Pool2_3", "pooled_2_08": "Pool2_4", "pooled_2_09": "Pool2_5", "pooled_2_04": "Pool2_6"}
    cols_a = [MAFCOL[p] for p in pools]
    out = {}
    for k in FEAT:
        mine = np.array([area(D[p][0], D[p][2][k], win[k]["lo"], win[k]["hi"]) for p in pools])
        row = [x for x in r[1:] if x[4] == k][0]
        dep = np.array([float(row[h.index(c)]) for c in cols_a])
        def rank(x): return np.argsort(np.argsort(x)).astype(float)
        best = None
        out[k] = {"mine": mine.tolist(), "deposited_in_Pool_column_order": dep.tolist(),
                  "spearman_same_order": float(np.corrcoef(rank(mine), rank(dep))[0, 1]),
                  "median_ratio_mine_over_deposited": float(np.median(np.sort(mine) / np.sort(dep))),
                  "spearman_sorted_values_trivial": 1.0, "cv_mine": float(mine.std(ddof=1) / mine.mean()), "cv_deposited": float(dep.std(ddof=1) / dep.mean())}
    blanks = {b: eic(os.path.join(NEG, b + ".mzXML")) for b in ["matrix_blank_1", "matrix_blank_2"]}
    for k in FEAT:
        bl = np.mean([area(blanks[b][0], blanks[b][2][k], win[k]["lo"], win[k]["hi"]) for b in blanks])
        mine = np.array(out[k]["mine"]); dep = np.array(out[k]["deposited_in_Pool_column_order"])
        def rank(x): return np.argsort(np.argsort(x)).astype(float)
        out[k]["blank_mean_area"] = float(bl); out[k]["mine_blank_subtracted"] = (mine - bl).tolist()
        out[k]["spearman_blank_subtracted"] = float(np.corrcoef(rank(mine - bl), rank(dep))[0, 1])
        out[k]["gate_raw_pass"] = bool(out[k]["spearman_same_order"] >= 0.7); out[k]["gate_blanksub_pass"] = bool(out[k]["spearman_blank_subtracted"] >= 0.7)
        out[k].pop("spearman_sorted_values_trivial", None)
    json.dump(out, open(os.path.join(OUT, "mtbls_qc_control.json"), "w"), indent=1)
    print(json.dumps({k: (v["spearman_same_order"], v["median_ratio_mine_over_deposited"], v["cv_mine"], v["cv_deposited"]) for k, v in out.items()}, indent=1))
else:
    win = json.load(open(os.path.join(OUT, "mtbls_windows.json")))
    qc = json.load(open(os.path.join(OUT, "mtbls_qc_control.json")))
    FEAT = {k: v for k, v in FEAT.items() if qc[k]["gate_raw_pass"] or qc[k]["gate_blanksub_pass"]}   # declared gate: failing features are not analysed
    s = list(csv.reader(open(aux), delimiter="\t")); sh = s[0]
    names = {x[sh.index("Sample Name")][:2]: (x[sh.index("Factor Value[Wwox manipulation]")], x[sh.index("Factor Value[Amyloid]")]) for x in s[1:] if x[sh.index("Characteristics[Sample type]")] == "experimental sample" and "KDExp" in x[sh.index("Sample Name")]}
    with open(os.path.join(OUT, "mtbls_sample_areas.tsv"), "w") as f:
        f.write("sample\tgroup\tamyloid\tTIC_total\t" + "\t".join(f"{k}_area" for k in FEAT) + "\t" + "\t".join(f"{k}_area_over_TIC" for k in FEAT) + "\n")
        for sid, (grp, amy) in sorted(names.items()):
            rts, tic, E = eic(os.path.join(NEG, sid + ".mzXML"))
            ar = {k: area(rts, E[k], win[k]["lo"], win[k]["hi"]) for k in FEAT}
            f.write(f"{sid}\t{grp}\t{amy}\t{tic.sum():.6g}\t" + "\t".join(f"{ar[k]:.6g}" for k in FEAT) + "\t" + "\t".join(f"{ar[k]/tic.sum():.6g}" for k in FEAT) + "\n")
    print("samples done")
