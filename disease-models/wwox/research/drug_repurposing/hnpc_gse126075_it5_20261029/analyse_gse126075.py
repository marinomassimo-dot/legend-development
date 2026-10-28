#!/usr/bin/env python3
"""GSE126075 descriptive analysis, exactly as declared in PRE_ANALYSIS.md (committed before any result).
Usage: python3 -I analyse_gse126075.py <geo_dir> <marker_sets_tsv> <out_dir> [matplotlib_dir]
geo_dir holds the two processed gz files and bed_streamed_tagcounts_and_sha256.tsv.
n = 1 library per arm: nothing here is a significance test."""
import sys, gzip, csv, json, hashlib, re, os
if len(sys.argv) > 4: sys.path.insert(0, sys.argv[4])   # optional dir holding matplotlib (not installed system-wide)
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

geo, markers, out = sys.argv[1:4]
SEED, NDRAW = 20261029, 10000
ARMS = ["hNSC", "Neurons", "hNSC_WWOX_del", "Neurons_WWOX_del"]   # column order of the deposited matrix
GSM = {"hNSC": "GSM3590948", "hNSC_WWOX_del": "GSM3590949", "Neurons": "GSM3590950", "Neurons_WWOX_del": "GSM3590951"}
F_MAT = "GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz"
F_TSS = "GSE126075_TSScoordinates_TPMexpression_all_samples_F5mapped.txt.gz"
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
N = {}
for l in open(f"{geo}/bed_streamed_tagcounts_and_sha256.tsv"):
    g, n, _ = l.split(); N[g] = int(n)
Ntags = {a: N[GSM[a]] for a in ARMS}

rows = list(csv.reader(gzip.open(f"{geo}/{F_MAT}", "rt"), delimiter="\t"))
assert rows[0] == ["Gene"] + ARMS, rows[0]
genes = [r[0] for r in rows[1:]]
TPM = np.array([[float(x) for x in r[1:]] for r in rows[1:]])
gi = {g: i for i, g in enumerate(genes)}
colsum = TPM.sum(0)
TPM_B = TPM / colsum * 1e6          # sensitivity B: renormalised to gene-matrix total
TAGS = TPM * np.array([Ntags[a] for a in ARMS]) / 1e6
col = {a: j for j, a in enumerate(ARMS)}

ALIAS = {"ATP5F1A": ["ATP5A1"], "ATP5F1B": ["ATP5B"], "ATP5F1C": ["ATP5C1"], "ATP5F1D": ["ATP5D"], "ATP5F1E": ["ATP5E"],
         "ATP5PB": ["ATP5F1"], "ATP5MC1": ["ATP5G1"], "ATP5MC2": ["ATP5G2"], "ATP5MC3": ["ATP5G3"], "ATP5PD": ["ATP5H"],
         "ATP5ME": ["ATP5I"], "ATP5MF": ["ATP5J2"], "ATP5MG": ["ATP5L"], "ATP5PF": ["ATP5J"], "ATP5PO": ["ATP5O"],
         "NDUFA4": [], "COX4I1": [], "UQCR10": ["UQCR11"], "UQCRQ": [], "MTRF1L": ["MTRF1L"], "SAMM50": ["SAMM50"],
         "TIMM17A": [], "PPP1R15A": [], "DNAJC19": []}
rng_sets = {}
rng_sets["ATF4_gene"] = ["ATF4"]
rng_sets["ISR_targets"] = "ASNS CHAC1 TRIB3 DDIT3 PHGDH PSAT1 PSPH SLC7A11 ATF5 PCK2 SESN2 GADD45A".split()
rng_sets["UPR_branches"] = "XBP1 HSPA5 HSP90B1 DNAJB9 EIF2AK3 EIF2AK4 EIF2S1 PPP1R15A".split()
ox = []
ox += [f"NDUFA{i}" for i in (1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13)] + ["NDUFAB1"]
ox += [f"NDUFB{i}" for i in range(1, 12)] + ["NDUFC1", "NDUFC2"] + [f"NDUFS{i}" for i in range(1, 9)] + [f"NDUFV{i}" for i in (1, 2, 3)]
ox += ["SDHA", "SDHB", "SDHC", "SDHD", "UQCRB", "UQCRC1", "UQCRC2", "UQCRFS1", "UQCRH", "UQCRQ", "UQCR10", "CYC1",
       "COX4I1", "COX5A", "COX5B", "COX6A1", "COX6B1", "COX6C", "COX7A2", "COX7B", "COX7C", "COX8A",
       "ATP5F1A", "ATP5F1B", "ATP5F1C", "ATP5F1D", "ATP5F1E", "ATP5PB", "ATP5MC1", "ATP5MC2", "ATP5MC3", "ATP5PD", "ATP5PF", "ATP5PO", "ATP5ME", "ATP5MF", "ATP5MG"]
rng_sets["OXPHOS_nuclear"] = ox
rng_sets["Mito_translation"] = sorted({g for g in genes if re.match(r"^MRP[LS]\d", g)}) + "TUFM TSFM GFM1 GFM2 MTIF2 MTIF3 MTRF1L".split()
rng_sets["Mito_import"] = "TOMM20 TOMM22 TOMM40 TOMM70 TIMM8A TIMM9 TIMM10 TIMM13 TIMM17A TIMM17B TIMM21 TIMM22 TIMM23 TIMM44 TIMM50 PAM16 DNAJC19 GRPEL1 HSPD1 HSPE1 PMPCA PMPCB SAMM50".split()
rng_sets["Glycolysis_lactate"] = "SLC2A1 HK2 PFKP ALDOA PGK1 ENO1 LDHA PKM BNIP3 LDHB".split()
rng_sets["PDK_family"] = ["PDK1", "PDK2", "PDK3", "PDK4"]
rng_sets["Lactate_transporters"] = ["SLC16A1", "SLC16A3"]
rng_sets["Ctl_cytosolic_ribosome"] = sorted(g for g in genes if re.match(r"^RP[LS]\d", g) and not g.startswith("RPLP"))
rng_sets["Ctl_housekeeping"] = "ACTB GAPDH TBP PPIA HPRT1 B2M TUBA1B EEF1A1 RPLP0 UBC YWHAZ GUSB".split()
mk = {}
for l in list(csv.reader(open(markers), delimiter="\t"))[1:]:
    mk["Mk_" + l[0]] = l[1].split(",")
SETS = {**rng_sets, **mk}
ROLE = {k: ("marker_confounder" if k.startswith("Mk_") else "control" if k.startswith("Ctl_") else "question") for k in SETS}

def resolve(sym):
    if sym in gi: return sym
    for a in ALIAS.get(sym, []):
        if a in gi: return a
    return None
resolved = {k: [(g, resolve(g)) for g in v] for k, v in SETS.items()}

def r_vec(mat, kd, ctl):
    return np.log2((mat[:, col[kd]] + .5) / (mat[:, col[ctl]] + .5))
CONTR = {"C_hNPC": ("hNSC_WWOX_del", "hNSC"), "C_neuron": ("Neurons_WWOX_del", "Neurons"),
         "S_ctrl": ("Neurons", "hNSC"), "S_kd": ("Neurons_WWOX_del", "hNSC_WWOX_del")}
def universe(kd, ctl): return (TAGS[:, col[kd]] >= 10) & (TAGS[:, col[ctl]] >= 10)

def centred(mat, kd, ctl, uni):
    r = r_vec(mat, kd, ctl); return r - np.median(r[uni])
DATA = {}
for c, (kd, ctl) in CONTR.items():
    u = universe(kd, ctl)
    DATA[c] = dict(uni=u, prim=centred(TPM, kd, ctl, u), unc=r_vec(TPM, kd, ctl), B=centred(TPM_B, kd, ctl, u),
                   mean_log10=np.log10((TAGS[:, col[kd]] + TAGS[:, col[ctl]]) / 2 + 1))
# stage-coupled residuals
for c in ("C_hNPC", "C_neuron", "S_kd"):
    u = DATA[c]["uni"] & DATA["S_ctrl"]["uni"]
    x, y = DATA["S_ctrl"]["prim"][u], DATA[c]["prim"][u]
    slope, icpt = np.polyfit(x, y, 1)
    res = np.full(len(genes), np.nan); res[u] = DATA[c]["prim"][u] - (slope * x + icpt)
    DATA[c]["res"] = res; DATA[c]["res_uni"] = u; DATA[c]["res_fit"] = (float(slope), float(icpt), float(np.corrcoef(x, y)[0, 1]), int(u.sum()))

rng = np.random.default_rng(SEED)
def null_test(values, uni, members, mean_log10):
    """members: indices measurable. returns obs mean, null mean, lo, hi, two-sided rank p"""
    idx = np.where(uni)[0]
    dec = np.digitize(mean_log10[idx], np.quantile(mean_log10[idx], np.linspace(0, 1, 11)[1:-1]))
    mem = np.array(members)
    mdec = np.digitize(mean_log10[mem], np.quantile(mean_log10[idx], np.linspace(0, 1, 11)[1:-1]))
    pools = {d: idx[(dec == d) & ~np.isin(idx, mem)] for d in range(10)}
    need = {d: int((mdec == d).sum()) for d in range(10)}
    obs = float(values[mem].mean())
    nulls = np.empty(NDRAW)
    for i in range(NDRAW):
        pick = [rng.choice(pools[d], size=k, replace=False) for d, k in need.items() if k > 0]
        nulls[i] = values[np.concatenate(pick)].mean()
    pl, pg = (nulls <= obs).mean(), (nulls >= obs).mean()
    return obs, float(nulls.mean()), float(np.quantile(nulls, .025)), float(np.quantile(nulls, .975)), float(min(1, 2 * min(pl, pg)))

pergene, summ = [], []
for setname, pairs in resolved.items():
    for c in CONTR:
        D = DATA[c]; uni = D["uni"]
        mem = [gi[r] for _, r in pairs if r is not None and uni[gi[r]]]
        notm = [s for s, r in pairs if r is None or not uni[gi[r]]]
        row = dict(set=setname, role=ROLE[setname], contrast=c, n_declared=len(pairs), n_measurable=len(mem),
                   not_measurable=";".join(notm) if len(notm) < 40 else f"{len(notm)} genes")
        if len(mem) >= 3:
            for key, uni_, label in (("prim", uni, "primary"), ("unc", uni, "A_uncentred"), ("B", uni, "B_renorm")):
                o, nm, lo, hi, p = null_test(D[key], uni_, mem, D["mean_log10"])
                row[f"mean_{label}"] = round(o, 3)
                if label == "primary": row.update(null_mean=round(nm, 3), null_lo=round(lo, 3), null_hi=round(hi, 3), rank_two_sided=round(p, 4))
                else: row[f"null_{label}_95"] = f"[{lo:.2f},{hi:.2f}]"
            if c != "S_ctrl":
                ru = D["res_uni"]; memr = [m for m in mem if ru[m]]
                if len(memr) >= 3:
                    o, nm, lo, hi, p = null_test(D["res"], ru, memr, D["mean_log10"])
                    row.update(mean_residual=round(o, 3), res_null_95=f"[{lo:.2f},{hi:.2f}]", res_rank=round(p, 4))
        summ.append(row)
        for s, r in pairs:
            if r is None: continue
            i = gi[r]; a, b = TAGS[i, col[CONTR[c][0]]], TAGS[i, col[CONTR[c][1]]]
            se = (1 / max(a, .5) + 1 / max(b, .5)) ** .5 / np.log(2) * 1.96
            pergene.append(dict(set=setname, contrast=c, symbol=s, matrix_symbol=r, measurable=bool(uni[i]),
                tpm_kd=round(TPM[i, col[CONTR[c][0]]], 2), tpm_ctl=round(TPM[i, col[CONTR[c][1]]], 2),
                tags_kd=round(a, 1), tags_ctl=round(b, 1), R_centred=round(D["prim"][i], 3), R_uncentred=round(D["unc"][i], 3),
                poisson95_halfwidth=round(se, 3)))

# decision rule for question and marker sets
def get(setname, c): return next(r for r in summ if r["set"] == setname and r["contrast"] == c)
def outside(r): return "mean_primary" in r and (r["mean_primary"] < r["null_lo"] or r["mean_primary"] > r["null_hi"])
decision = {}
# WWOX control
wi = gi.get("WWOX")
wwox = {}
tss = list(csv.reader(gzip.open(f"{geo}/{F_TSS}", "rt")))
th = tss[0]
ix = {h: i for i, h in enumerate(th)}
nm = ix["TSS_F5.name"]
wt = [r for r in tss[1:] if re.search(r"@WWOX(,|$)", r[nm]) or r[nm].split("@")[-1].split(",")[0] == "WWOX"]
wwox["tss_clusters"] = [dict(name=r[nm], chr=r[ix["TSS_F5.seqnames"]], start=r[ix["TSS_F5.start"]], strand=r[ix["TSS_F5.strand"]],
    **{a: float(r[ix[a]]) for a in ("hNSC", "hNSC_WWOX_del", "neurons", "neurons_WWOX_del")}) for r in wt]
if wi is not None:
    for c in ("C_hNPC", "C_neuron"):
        D = DATA[c]; u = D["uni"]
        rk = float((D["prim"][u] < D["prim"][wi]).mean()) if u[wi] else None
        a, b = TAGS[wi, col[CONTR[c][0]]], TAGS[wi, col[CONTR[c][1]]]
        wwox[c] = dict(tpm_kd=TPM[wi, col[CONTR[c][0]]], tpm_ctl=TPM[wi, col[CONTR[c][1]]], tags_kd=a, tags_ctl=b,
                       R_centred=float(D["prim"][wi]), R_uncentred=float(D["unc"][wi]), R_B=float(D["B"][wi]),
                       fraction_of_measurable_genes_lower=rk, measurable=bool(u[wi]))
wwox_ok = bool(wi is not None and all(wwox[c]["R_centred"] < 0 and wwox[c]["R_uncentred"] < 0 and wwox[c]["R_B"] < 0 for c in ("C_hNPC", "C_neuron")))
pos = {k: get(k, "S_ctrl").get("mean_primary") for k in ("Mk_neuronal_pan", "Mk_radial_glia_progenitor", "Mk_cell_cycle_proliferation")}
pos_ok = bool(pos["Mk_neuronal_pan"] is not None and pos["Mk_neuronal_pan"] > 0 and pos["Mk_radial_glia_progenitor"] < 0 and pos["Mk_cell_cycle_proliferation"] < 0)
for s in SETS:
    a, b = get(s, "C_hNPC"), get(s, "C_neuron")
    if "mean_primary" not in a or "mean_primary" not in b: decision[s] = "too few measurable members"; continue
    same = np.sign(a["mean_primary"]) == np.sign(b["mean_primary"])
    i_ = outside(a) and outside(b) and same
    ii = all(np.sign(r["mean_primary"]) == np.sign(r["mean_" + k]) for r in (a, b) for k in ("A_uncentred", "B_renorm"))
    def resout(r):
        if "mean_residual" not in r: return None
        lo, hi = [float(x) for x in r["res_null_95"].strip("[]").split(",")]
        return r["mean_residual"] < lo or r["mean_residual"] > hi
    iii = all(resout(r) and np.sign(r["mean_residual"]) == np.sign(r["mean_primary"]) for r in (a, b)) if i_ else None
    if i_ and ii and iii and wwox_ok: decision[s] = "descriptive signal worth carrying"
    elif outside(a) or outside(b): decision[s] = "inconsistent or confounded (outside the matched null in %s; criteria i-iii: %s/%s/%s)" % (
        "one or both stages", i_, ii, iii)
    else: decision[s] = "not distinguishable from matched random sets (not evidence of absence)"

# global distribution
glob = {c: dict(n_measurable=int(DATA[c]["uni"].sum()), median_uncentred_R=float(np.median(DATA[c]["unc"][DATA[c]["uni"]])),
                sd_centred_R=float(DATA[c]["prim"][DATA[c]["uni"]].std()),
                frac_abs_centred_R_ge_1=float((np.abs(DATA[c]["prim"][DATA[c]["uni"]]) >= 1).mean())) for c in CONTR}
for c in ("C_hNPC", "C_neuron", "S_kd"): glob[c]["stage_fit_slope_intercept_r_n"] = DATA[c]["res_fit"]

os.makedirs(out, exist_ok=True)
def wtsv(name, recs):
    keys = list(dict.fromkeys(k for r in recs for k in r))
    with open(f"{out}/{name}", "w") as f:
        f.write("\t".join(keys) + "\n")
        for r in recs: f.write("\t".join(str(r.get(k, "")) for k in keys) + "\n")
wtsv("set_summary.tsv", summ); wtsv("per_gene_in_sets.tsv", pergene)
params = dict(seed=SEED, ndraw=NDRAW, inputs={F_MAT: sha(f"{geo}/{F_MAT}"), F_TSS: sha(f"{geo}/{F_TSS}"), "markers": sha(markers)},
              library_tags=Ntags, matrix_colsum=dict(zip(ARMS, colsum.tolist())), n_genes_matrix=len(genes),
              WWOX_control=wwox, WWOX_silenced_all_three_normalisations_both_stages=wwox_ok, stage_positive_control=pos, stage_positive_control_ok=pos_ok,
              global_distribution=glob, decisions=decision,
              unresolved_symbols={k: [s for s, r in v if r is None] for k, v in resolved.items() if any(r is None for _, r in v)})
json.dump(params, open(f"{out}/results.json", "w"), indent=1, default=float)

# figures
fig, ax = plt.subplots(1, 2, figsize=(11, 4.6))
u = DATA["C_hNPC"]["uni"] & DATA["C_neuron"]["uni"]
ax[0].scatter(DATA["C_hNPC"]["prim"][u], DATA["C_neuron"]["prim"][u], s=2, c="#bbbbbb", rasterized=True)
cols = {"ISR_targets": "#d62728", "OXPHOS_nuclear": "#1f77b4", "Mito_translation": "#2ca02c", "Glycolysis_lactate": "#ff7f0e", "PDK_family": "#9467bd"}
for s, c_ in cols.items():
    m = [gi[r] for _, r in resolved[s] if r is not None and u[gi[r]]]
    ax[0].scatter(DATA["C_hNPC"]["prim"][m], DATA["C_neuron"]["prim"][m], s=14, c=c_, label=s)
if wi is not None and u[wi]: ax[0].scatter(*[DATA[c]["prim"][wi] for c in ("C_hNPC", "C_neuron")], marker="*", s=160, c="k", label="WWOX")
ax[0].axhline(0, c="k", lw=.5); ax[0].axvline(0, c="k", lw=.5); ax[0].set_xlim(-6, 6); ax[0].set_ylim(-6, 6)
ax[0].set_xlabel("shWWOX vs control, hNPC: centred log2 ratio"); ax[0].set_ylabel("shWWOX vs control, neurons: centred log2 ratio")
ax[0].set_title("Single libraries per arm (n = 1): descriptive"); ax[0].legend(fontsize=7, markerscale=1)
names = [s for s in SETS if ROLE[s] != "marker_confounder" or True]
names = [s for s in names if "mean_primary" in get(s, "C_hNPC") and "mean_primary" in get(s, "C_neuron")]
y = np.arange(len(names))
for k, (c, off, colr) in enumerate((("C_hNPC", -.18, "#1f77b4"), ("C_neuron", .18, "#d62728"))):
    ax[1].errorbar([get(s, c)["mean_primary"] for s in names], y + off,
        xerr=None, fmt="o", c=colr, label=c, ms=4)
    for yy, s in zip(y, names):
        r = get(s, c); ax[1].plot([r["null_lo"], r["null_hi"]], [yy + off] * 2, c=colr, alpha=.35, lw=4, solid_capstyle="butt")
ax[1].axvline(0, c="k", lw=.5); ax[1].set_yticks(y); ax[1].set_yticklabels(names, fontsize=6); ax[1].invert_yaxis()
ax[1].set_xlabel("set mean centred log2 ratio (dot) and central 95% of matched random sets (bar)"); ax[1].legend(fontsize=7)
ax[1].set_title("Sets against matched random sets")
plt.tight_layout(); plt.savefig(f"{out}/fig1_sets_vs_matched_null.png", dpi=110); plt.close()

fig, ax = plt.subplots(figsize=(6, 4.2))
mks = [s for s in SETS if s.startswith("Mk_") and "mean_primary" in get(s, "S_ctrl")]
x = np.arange(len(mks))
ax.bar(x - .2, [get(s, "S_ctrl")["mean_primary"] for s in mks], .4, label="control line, neurons vs hNPC", color="#7f7f7f")
ax.bar(x + .2, [get(s, "S_kd")["mean_primary"] for s in mks], .4, label="shWWOX line, neurons vs hNPC", color="#d62728")
ax.set_xticks(x); ax.set_xticklabels([s[3:] for s in mks], rotation=40, ha="right", fontsize=7); ax.axhline(0, c="k", lw=.5)
ax.set_ylabel("set mean centred log2 ratio (stage)"); ax.legend(fontsize=7); ax.set_title("Differentiation progress: marker sets, by line")
plt.tight_layout(); plt.savefig(f"{out}/fig2_stage_markers.png", dpi=110); plt.close()
print(json.dumps({k: params[k] for k in ("WWOX_silenced_all_three_normalisations_both_stages", "stage_positive_control_ok")}))
