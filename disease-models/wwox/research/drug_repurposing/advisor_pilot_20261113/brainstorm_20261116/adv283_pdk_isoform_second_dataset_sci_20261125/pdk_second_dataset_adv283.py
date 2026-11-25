#!/usr/bin/env python3
"""ADV-283: PDK1-4 in held WWOX-deficient datasets, rules frozen in PREREG_ADV283_SCI_20261125.md.
Usage (python3 -I -P -E): pdk_second_dataset_adv283.py <files_root> <outdir>
files_root is the root checkout's files/ folder. Reads held tables only."""
import gzip, sys, re, os, csv
root, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
SYM = {"Pdk1": "Pdk1", "Pdk2": "Pdk2", "Pdk3": "Pdk3", "Pdk4": "Pdk4"}
# mouse transcript -> gene symbol from Ensembl GRCm38 r92 cdna headers (names only)
t2s = {}
with gzip.open(f"{root}/reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz", "rt", errors="replace") as h:
    for l in h:
        if l[0] != ">":
            continue
        m = re.match(r">(\S+?)(?:\.\d+)?\s.*?gene_symbol:(\S+)", l)
        if m:
            t2s[m.group(1)] = m.group(2)

def tpm_table(path, arms):
    """arms: {arm: [column names]}; returns gene sums per column for Pdk1-4 and mapping stats."""
    with gzip.open(path, "rt", errors="replace") as h:
        hdr = h.readline().rstrip("\n").split("\t")
        idx = {c: i for i, c in enumerate(hdr)}
        sums = {g: {c: 0.0 for a in arms.values() for c in a} for g in SYM}
        n_tx = {g: 0 for g in SYM}
        unmapped = 0
        rows = 0
        for l in h:
            f = l.rstrip("\n").split("\t")
            rows += 1
            t = re.sub(r"\.\d+$", "", f[0])
            s = t2s.get(t)
            if s is None:
                unmapped += 1
                continue
            if s in SYM:
                n_tx[s] += 1
                for a in arms.values():
                    for c in a:
                        sums[s][c] += float(f[idx[c]])
    return sums, n_tx, unmapped, rows

def verdict(g, d_cols, c_cols, sums):
    d = [sums[g][c] for c in d_cols]; c = [sums[g][c] for c in c_cols]
    md, mc = sum(d) / len(d), sum(c) / len(c)
    detected = max(md, mc) >= 1.0
    ratio = md / mc if mc > 0 else None
    above = min(d) > max(c); below = max(d) < min(c)
    if len(d) < 2 or len(c) < 2 or not detected:
        v = "CANNOT TEST"
    elif g == "Pdk3":
        v = "SUPPORTS" if (ratio is not None and ratio >= 1.2 and above) else "FAILS TO SUPPORT"
    elif g == "Pdk1":
        v = "SUPPORTS" if (ratio is not None and ratio <= 1 / 1.2 and below) else "FAILS TO SUPPORT"
    else:
        v = "no prediction"
    return md, mc, ratio, above, below, detected, v, d, c

DATA = [
 ("D2 GSE158681 hippocampus P17 mouse", f"{root}/geo/GSE158681/GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz",
  {"KO v WT (primary, global null)": (["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"]),
   "S KO v S Ctrl (secondary, Synapsin-Cre)": (["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"]),
   "N KO v N Ctrl (secondary, nestin-Cre)": (["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"])}),
 ("D3 GSE158682 cortex P17 mouse", f"{root}/geo/GSE158682/GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz",
  {"S KO v S Ctrl (primary)": (["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"])}),
]
rows_out = []
for name, path, comps in DATA:
    cols = sorted({c for d, k in comps.values() for c in d + k})
    sums, n_tx, unm, nrows = tpm_table(path, {"all": cols})
    print(f"## {name}: table rows {nrows}, unmapped transcripts {unm}, transcripts summed per gene {n_tx}")
    for cname, (d, k) in comps.items():
        for g in ["Pdk1", "Pdk2", "Pdk3", "Pdk4"]:
            md, mc, r, ab, be, det, v, dv, cv = verdict(g, d, k, sums)
            rows_out.append([name, cname, g, f"{len(d)} v {len(k)}", f"{md:.3f}", f"{mc:.3f}", "" if r is None else f"{r:.3f}",
                             "all deficient above all control" if ab else ("all deficient below all control" if be else "overlap"),
                             "yes" if det else "no", v,
                             " ".join(f"{x:.2f}" for x in dv), " ".join(f"{x:.2f}" for x in cv)])
            print(rows_out[-1][1:])
# D4 GSE126075 CAGE, gene symbols, n=1 per arm: descriptive
with gzip.open(f"{root}/geo/GSE126075/GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz", "rt", errors="replace") as h:
    hdr = h.readline().rstrip("\n").split("\t")
    want = {g.upper(): g for g in SYM}
    for l in h:
        f = l.rstrip("\n").split("\t")
        if f[0].upper() in want:
            v = dict(zip(hdr[1:], map(float, f[1:])))
            for ctrl, dele, lab in [("hNSC", "hNSC_WWOX_del", "hNSC"), ("Neurons", "Neurons_WWOX_del", "neurons")]:
                r = v[dele] / v[ctrl] if v[ctrl] > 0 else None
                det = max(v[ctrl], v[dele]) >= 1.0
                rows_out.append(["D4 GSE126075 human CAGE (descriptive)", lab + " WWOX-del v control", want[f[0].upper()], "1 v 1",
                                 f"{v[dele]:.3f}", f"{v[ctrl]:.3f}", "" if r is None else f"{r:.3f}", "n of 1: no ordering", "yes" if det else "no",
                                 "DESCRIPTIVE" if det else "CANNOT TEST", f"{v[dele]:.2f}", f"{v[ctrl]:.2f}"])
                print(rows_out[-1][1:])
# D5 GSE158684 snRNA: coverage only
import collections
for lib in ("ctrl", "ko"):
    feats = []
    with gzip.open(f"{root}/geo/GSE158684/GSE158684_{lib}_filtered_features.tsv.gz", "rt") as h:
        for l in h:
            f = l.rstrip("\n").split("\t"); feats.append(f[1] if len(f) > 1 else f[0])
    gi = {i + 1: s for i, s in enumerate(feats) if s in SYM}
    tot = collections.Counter(); nz = collections.Counter(); ncell = 0
    with gzip.open(f"{root}/geo/GSE158684/GSE158684_{lib}_filtered_matrix.mtx.gz", "rt") as h:
        hdr_done = False
        for l in h:
            if l[0] == "%":
                continue
            a = l.split()
            if not hdr_done:
                ncell = int(a[1]); hdr_done = True; continue
            gidx = int(a[0])
            if gidx in gi:
                tot[gi[gidx]] += int(float(a[2])); nz[gi[gidx]] += 1
    for g in ["Pdk1", "Pdk2", "Pdk3", "Pdk4"]:
        rows_out.append([f"D5 GSE158684 snRNA mouse hippocampal nuclei (coverage only)", lib, g, f"1 library, {ncell} nuclei",
                         f"{tot[g]}", f"{nz[g]}", "", "", "yes" if nz[g] else "no", "COVERAGE ONLY", "", ""])
        print(rows_out[-1][1:])
with open(f"{out}/pdk_second_dataset_adv283.tsv", "w", newline="") as h:
    w = csv.writer(h, delimiter="\t")
    w.writerow(["dataset", "comparison", "gene", "n_deficient_v_control", "mean_TPM_deficient_or_total_UMI", "mean_TPM_control_or_nuclei_nonzero", "ratio",
                "ordering", "detected_mean_TPM_ge_1", "verdict", "deficient_libraries_TPM", "control_libraries_TPM"])
    w.writerows(rows_out)
