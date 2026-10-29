#!/usr/bin/env python3
"""P4 (IT6): the iteration-5 gene sets measured in mouse P17 brain with Wwox deletion (GSE158681 hippocampus, GSE158682 cortex).
Same-set method of hnpc_gse126075_it5_20261029/p7_organoid_same_sets.py (per-arm mean, log2 ratio with 0.5 pseudocount, median centring,
expression-decile-matched random sets, 10,000 draws, seed 20261029), adapted to Salmon transcript TPM. Declared in PRE_ANALYSIS.md.
Usage: python3 -I p4_mouse_same_sets.py <hippo.txt.gz> <cortex.txt.gz> <Ensembl92 cdna.fa.gz> <it5 per_gene_in_sets.tsv> <out_dir>
Needs numpy only. Deterministic."""
import sys, gzip, csv, json, hashlib, re, os
import numpy as np

hippo, cortex, fasta, p6, out = sys.argv[1:6]
SEED, NDRAW = 20261029, 10000
THRESH = [1.0, 0.5, 2.0]          # first is primary
os.makedirs(out, exist_ok=True)

def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()

# ---- Ensembl 92 transcript -> gene key (primary assembly only) -------------------------------------------------------------------
tx2g, gsym, patch_tx = {}, {}, set()
for l in gzip.open(fasta, "rt"):
    if l[0] != ">": continue
    tid = l[1:].split(" ", 1)[0]
    gid = re.search(r"gene:(\S+)", l).group(1)
    s = re.search(r"gene_symbol:(\S+)", l)
    if "_PATCH" in l.split(" ", 3)[2]:
        patch_tx.add(tid); continue
    tx2g[tid] = gid
    gsym[gid] = s.group(1) if s else ""
up2ids = {}
for gid, s in gsym.items():
    if s: up2ids.setdefault(s.upper(), []).append(gid)

# ---- load TPM tables, sum to gene -------------------------------------------------------------------------------------------------
def load(path):
    f = gzip.open(path, "rt"); head = f.readline().rstrip("\n").split("\t")
    animals = head[3:]; ids, rows = [], []
    for l in f:
        p = l.rstrip("\n").split("\t"); ids.append(p[0]); rows.append(p[3:])
    return animals, ids, np.array(rows, dtype=float)

def to_gene(ids, M):
    gl = sorted(set(tx2g[i] for i in ids if i in tx2g))
    gi = {g: k for k, g in enumerate(gl)}
    G = np.zeros((len(gl), M.shape[1])); dropped = np.zeros(M.shape[1]); unk = 0
    for k, i in enumerate(ids):
        if i in tx2g: G[gi[tx2g[i]]] += M[k]
        elif i in patch_tx: dropped += M[k]
        else: unk += 1
    return gl, gi, G, dropped, unk

ha, hids, hM = load(hippo); ca, cids, cM = load(cortex)
hg, hgi, hG, hdrop, hunk = to_gene(hids, hM)
cg, cgi, cG, cdrop, cunk = to_gene(cids, cM)

# ---- ortholog rule and sets (PRE_ANALYSIS sections 4.6 and 5) ----------------------------------------------------------------------
ALIAS = {"ATP5F1A": "Atp5a1", "ATP5F1B": "Atp5b", "ATP5F1C": "Atp5c1", "ATP5F1D": "Atp5d", "ATP5F1E": "Atp5e", "ATP5PB": "Atp5f1",
         "ATP5MC1": "Atp5g1", "ATP5MC2": "Atp5g2", "ATP5MC3": "Atp5g3", "ATP5PD": "Atp5h", "ATP5PF": "Atp5j", "ATP5PO": "Atp5o",
         "ATP5ME": "Atp5i", "ATP5MF": "Atp5j2", "ATP5MG": "Atp5l", "TIMM8A": "Timm8a1", "HPRT1": "Hprt"}
def resolve(h):
    key = ALIAS.get(h, h).upper(); c = up2ids.get(key, [])
    return (c[0], "ok") if len(c) == 1 else (None, "absent" if not c else "ambiguous")

sets_h = {}
for r in csv.DictReader(open(p6), delimiter="\t"):
    if r["contrast"] == "C_hNPC": sets_h.setdefault(r["set"], []).append(r["symbol"])
extra = {"ISR_targets": ["SLC7A11"], "UPR_branches": ["PPP1R15A"], "Glycolysis_lactate": ["PKM"], "PDK_family": ["PDK4"],
         "Lactate_transporters": ["SLC16A3"], "Mito_import": ["TOMM70", "TIMM23"], "OXPHOS_nuclear": ["NDUFA11"]}
for k, v in extra.items(): sets_h[k] = sorted(set(sets_h.get(k, [])) | set(v))
del sets_h["Ctl_cytosolic_ribosome"]   # replaced by the mouse regex below
sets_h["Glycolysis_19"] = sorted(set(sets_h["Glycolysis_lactate"]) | {"SLC2A3", "SLC16A3", "HK1", "GPI", "TPI1", "GAPDH", "PGAM1", "PFKL", "ENO2"})
sets_h["Prog_core4"] = ["SOX2", "PAX6", "HES1", "HES5"]
sets_h["Prog_9"] = list(sets_h["Mk_radial_glia_progenitor"])
sets_h["Prog_NESVIM"] = ["NES", "VIM"]
sets_h["Neuro_5"] = list(sets_h["Mk_neuronal_pan"])
sets_h["Neuro_10"] = ["TUBB3", "MAP2", "DCX", "STMN2", "SYT1", "RBFOX3", "NEUROD2", "NEUROD6", "SNAP25", "NEFL"]
sets_h["ISR_core5"] = ["CHAC1", "TRIB3", "PSAT1", "SESN2", "ATF5"]
sets_h["ISR_org3"] = ["CHAC1", "TRIB3", "SESN2"]
sets_h["Myelin_OL"] = ["MBP", "PLP1", "MOG", "MAG", "MOBP", "CLDN11", "CNP", "MAL", "OPALIN", "UGT8A"]
sets_h["ATF4_gene"] = ["ATF4"]
RIB = re.compile(r"^Rp[ls][0-9]+[a-z]?[0-9]?$")
rib_ids = sorted(g for g, s in gsym.items() if RIB.match(s) and s not in ("Rps4y1", "Rps4y2"))
ORDER = ["ATF4_gene", "ISR_targets", "ISR_core5", "ISR_org3", "UPR_branches", "OXPHOS_nuclear", "Mito_translation", "Mito_import",
         "Glycolysis_lactate", "Glycolysis_19", "PDK_family", "Lactate_transporters", "Prog_core4", "Prog_9", "Prog_NESVIM", "Neuro_5",
         "Neuro_10", "Myelin_OL", "Mk_cell_cycle_proliferation", "Mk_glutamatergic", "Mk_GABAergic", "Mk_astrocyte_glia",
         "Mk_regional_patterning_non_cortical", "Mk_wnt_pathway", "Ctl_housekeeping", "Ctl_cytosolic_ribosome"]
sets_ids, resolution = {}, []
for s in ORDER:
    if s == "Ctl_cytosolic_ribosome":
        sets_ids[s] = rib_ids; resolution.append((s, "regex", len(rib_ids), "ok")); continue
    ids = []
    for h in sets_h[s]:
        g, st = resolve(h); resolution.append((s, h, g or "", st))
        if g: ids.append(g)
    sets_ids[s] = ids
with open(f"{out}/set_member_resolution.tsv", "w") as f:
    f.write("set\thuman_symbol\tensembl_gene_or_n\tstatus\n")
    for r in resolution: f.write("\t".join(map(str, r)) + "\n")

# ---- contrasts --------------------------------------------------------------------------------------------------------------------
def cols(animals, names): return [animals.index(n) for n in names]
CONTR = [
 ("H_S", "hippo", ["S_KO_1", "S_KO_2", "S_KO_3"], ["S_Ctrl_1", "S_Ctrl_2"], True),
 ("H_N", "hippo", ["N_KO_1", "N_KO_2"], ["N_Ctrl_1", "N_Ctrl_2"], True),
 ("H_null", "hippo", ["KO_1", "KO_2"], ["WT_1", "WT_2", "WT_3"], True),
 ("C_S", "cortex", ["CRTX_S_KO_1", "CRTX_S_KO_2", "CRTX_S_KO_3"], ["CRTX_S_Ctrl_1", "CRTX_S_Ctrl_2", "CRTX_S_Ctrl_3", "CRTX_S_Ctrl_4"], True),
 ("CC_SW", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], False),
 ("CC_NW", "hippo", ["N_Ctrl_1", "N_Ctrl_2"], ["WT_1", "WT_2", "WT_3"], False),
 ("CC_SN", "hippo", ["S_Ctrl_1", "S_Ctrl_2"], ["N_Ctrl_1", "N_Ctrl_2"], False),
]
DATA = {"hippo": (ha, hg, hgi, hG), "cortex": (ca, cg, cgi, cG)}
wwox_id = [g for g, s in gsym.items() if s == "Wwox"]; assert len(wwox_id) == 1; wwox_id = wwox_id[0]

def contrast_stats(cname, region, kon, ctn, thr, rng, want_animal=True):
    animals, genes, gi, G = DATA[region]
    ko, ct = cols(animals, kon), cols(animals, ctn)
    mk, mc = G[:, ko].mean(1), G[:, ct].mean(1)
    uni = (mk >= thr) & (mc >= thr)
    R = np.log2((mk + .5) / (mc + .5)); Rc = R - np.median(R[uni])
    ml = np.log10((mk + mc) / 2 + 1)
    idx = np.where(uni)[0]; qs = np.quantile(ml[idx], np.linspace(0, 1, 11)[1:-1]); dec = np.digitize(ml[idx], qs)
    L = np.log2(G + .5); med = np.array([np.median(L[uni, a]) for a in range(G.shape[1])])
    res = {}
    for s in ORDER:
        mem = [gi[g] for g in sets_ids[s] if g in gi]
        m = np.array([i for i in mem if uni[i]], dtype=int)
        row = dict(n_declared=len(sets_h.get(s, [])) or len(sets_ids[s]), n_resolved=len(mem), n_measurable=len(m), mean=None)
        if len(m) >= 3:
            md = np.digitize(ml[m], qs); pools = {d: idx[(dec == d) & ~np.isin(idx, m)] for d in range(10)}
            need = {d: int((md == d).sum()) for d in range(10)}
            obs = float(Rc[m].mean())
            nul = np.array([Rc[np.concatenate([rng.choice(pools[d], k, replace=False) for d, k in need.items() if k])].mean() for _ in range(NDRAW)])
            lo, hi = float(np.quantile(nul, .025)), float(np.quantile(nul, .975))
            sc = (L[m].mean(0) - med)
            ks, cs = sc[ko], sc[ct]
            sep = bool((ks.min() > cs.max()) if obs > 0 else (ks.max() < cs.min())) if obs != 0 else False
            loo = []
            for a in ko + ct:
                k2 = [x for x in ko if x != a]; c2 = [x for x in ct if x != a]
                R2 = np.log2((G[:, k2].mean(1) + .5) / (G[:, c2].mean(1) + .5)); R2 = R2 - np.median(R2[uni])
                loo.append(float(R2[m].mean()))
            row.update(mean=obs, null_lo=lo, null_hi=hi, outside=bool(obs < lo or obs > hi),
                       rank_two_sided=float(min(1, 2 * min((nul <= obs).mean(), (nul >= obs).mean()))),
                       mean_uncentred=float(R[m].mean()), separated=sep,
                       animal_scores_ko=[round(float(x), 3) for x in ks], animal_scores_ctl=[round(float(x), 3) for x in cs],
                       loo_signs="".join("+" if x > 0 else "-" for x in loo), loo_all_same_sign=bool(all((x > 0) == (obs > 0) for x in loo)))
        res[s] = row
    return dict(sets=res, n_universe=int(uni.sum()), median_uncentred_R=float(np.median(R[uni])),
                iqr_centred_R=[float(np.quantile(Rc[uni], .25)), float(np.quantile(Rc[uni], .75))], Rc=Rc, uni=uni, R=R, mk=mk, mc=mc, ko=ko, ct=ct)

RES = {}   # (contrast, thr) -> stats
for cname, region, kon, ctn, counted in CONTR:
    for thr in THRESH:
        rng = np.random.default_rng(SEED)
        RES[(cname, thr)] = contrast_stats(cname, region, kon, ctn, thr, rng)

# ---- depth control ------------------------------------------------------------------------------------------------------------------
depth = {}
with open(f"{out}/wwox_depth.tsv", "w") as f:
    f.write("contrast\tregion\tanimal\tarm\twwox_sum_tpm\n")
    for cname, region, kon, ctn, counted in CONTR:
        animals, genes, gi, G = DATA[region]
        for arm, names in (("KO", kon), ("ctl", ctn)):
            for n in names: f.write(f"{cname}\t{region}\t{n}\t{arm}\t{G[gi[wwox_id], animals.index(n)]:.3f}\n")
        mk = np.mean([G[gi[wwox_id], animals.index(n)] for n in kon]); mc = np.mean([G[gi[wwox_id], animals.index(n)] for n in ctn])
        depth[cname] = dict(ko_mean=float(mk), ctl_mean=float(mc), reduction=float(1 - mk / mc), ok=bool(1 - mk / mc >= .5), counted=counted)
        f.write(f"{cname}\t{region}\tMEAN\tKO/ctl\t{mk:.3f}/{mc:.3f}\n")

# ---- tables -------------------------------------------------------------------------------------------------------------------------
keys = ["n_declared", "n_resolved", "n_measurable", "mean", "null_lo", "null_hi", "outside", "rank_two_sided", "mean_uncentred", "separated",
        "loo_signs", "loo_all_same_sign", "animal_scores_ko", "animal_scores_ctl"]
def fmt(v): return "" if v is None else (f"{v:.3f}" if isinstance(v, float) else str(v))
with open(f"{out}/set_summary.tsv", "w") as f:
    f.write("contrast\tuniverse_thr_tpm\tset\t" + "\t".join(keys) + "\n")
    for (cname, thr), r in RES.items():
        for s in ORDER: f.write(f"{cname}\t{thr}\t{s}\t" + "\t".join(fmt(r['sets'][s].get(k)) for k in keys) + "\n")

KEYG = ["Wwox", "Atf4", "Asns", "Chac1", "Trib3", "Ddit3", "Phgdh", "Psat1", "Psph", "Slc7a11", "Atf5", "Pck2", "Sesn2", "Gadd45a",
        "Eif2ak1", "Eif2ak2", "Eif2ak3", "Eif2ak4", "Ppp1r15a", "Hif1a", "Ldha", "Ldhb", "Hk1", "Hk2", "Slc2a1", "Slc2a3", "Pdk1", "Pdk2", "Pdk3",
        "Pdk4", "Pdha1", "Slc16a1", "Slc16a3", "Sox2", "Pax6", "Hes1", "Hes5", "Nes", "Vim", "Fabp7", "Mbp", "Plp1", "Mog", "Xist", "Ddx3y",
        "Kdm5d", "Eif2s3y"]
with open(f"{out}/key_genes.tsv", "w") as f:
    f.write("contrast\tgene\tmeasurable\tmean_tpm_KO\tmean_tpm_ctl\tR_centred\tR_uncentred\ttpm_KO_animals\ttpm_ctl_animals\tanimal_separated\n")
    for cname, region, kon, ctn, counted in CONTR:
        animals, genes, gi, G = DATA[region]; r = RES[(cname, 1.0)]
        for sym in KEYG:
            c = up2ids.get(sym.upper(), [])
            if len(c) != 1 or c[0] not in gi: f.write(f"{cname}\t{sym}\tunresolved\t\t\t\t\t\t\t\n"); continue
            i = gi[c[0]]; kv, cv = G[i, r['ko']], G[i, r['ct']]
            sep = bool(kv.min() > cv.max() or kv.max() < cv.min())
            f.write(f"{cname}\t{sym}\t{bool(r['uni'][i])}\t{kv.mean():.3f}\t{cv.mean():.3f}\t{r['Rc'][i]:.3f}\t{r['R'][i]:.3f}\t"
                    f"{';'.join(f'{x:.3f}' for x in kv)}\t{';'.join(f'{x:.3f}' for x in cv)}\t{sep}\n")

with open(f"{out}/isr_leave_one_gene_out.tsv", "w") as f:
    f.write("contrast\tdropped_gene\tmean_centred_R_of_remaining\tn\n")
    for cname, region, kon, ctn, counted in CONTR:
        animals, genes, gi, G = DATA[region]; r = RES[(cname, 1.0)]
        mem = [gi[g] for g in sets_ids["ISR_targets"] if g in gi and r["uni"][gi[g]]]
        for i in mem:
            rest = [j for j in mem if j != i]
            f.write(f"{cname}\t{gsym[genes[i]]}\t{r['Rc'][rest].mean():.3f}\t{len(rest)}\n")

# ---- decision rule (PRE_ANALYSIS section 7) ---------------------------------------------------------------------------------------
COUNTED = ["H_S", "H_N", "H_null"]; CCs = ["CC_SW", "CC_NW", "CC_SN"]
def verdict(s):
    P = {c: RES[(c, 1.0)]["sets"][s] for c, *_ in CONTR}
    ok = [c for c in COUNTED if depth[c]["ok"]]
    if any(P[c]["mean"] is None for c in ok): return "NOT EVALUABLE (fewer than 3 measurable members)", ""
    sign = lambda c: 1 if P[c]["mean"] > 0 else -1
    outs = [c for c in ok if P[c]["outside"]]
    notes = [f"{c}:{P[c]['mean']:+.2f}{'*' if P[c]['outside'] else ''}{'s' if P[c]['separated'] else ''}" for c in ok]
    for sg in (1, -1):
        grp = [c for c in outs if sign(c) == sg]
        if len(grp) >= 2:
            reasons = []
            opp = [c for c in ok if c not in grp and P[c]["outside"] and sign(c) != sg]
            if opp: reasons.append("opposite-sign contrast outside null: " + ",".join(opp))
            ns = [c for c in grp if not P[c]["separated"]]
            if ns: reasons.append("not animal-separated: " + ",".join(ns))
            cc = [c for c in CCs if RES[(c, 1.0)]["sets"][s]["outside"]]
            if cc: reasons.append("outside null in control-vs-control: " + ",".join(cc))
            thr_bad = [t for t in (0.5, 2.0) for c in grp if RES[(c, t)]["sets"][s]["mean"] is None or (RES[(c, t)]["sets"][s]["mean"] > 0) != (sg > 0)]
            if thr_bad: reasons.append("sign not stable across universe thresholds")
            rb = [c for c in grp if RES[(c, 1.0)]["sets"]["Ctl_cytosolic_ribosome"]["outside"] and (RES[(c, 1.0)]["sets"]["Ctl_cytosolic_ribosome"]["mean"] > 0) == (sg > 0)]
            word = "higher" if sg > 0 else "lower"
            if rb: reasons.append("cytosolic-ribosome control outside null with same sign: " + ",".join(rb)); 
            if reasons:
                lab = "NON-SPECIFIC" if (rb and len(reasons) == 1) else "NOT MOVED (criterion a met for %s, but %s)" % (word, "; ".join(reasons))
                return lab, " ".join(notes)
            cs = P["C_S"]
            rep = "replicated in cortex" if (cs["outside"] and cs["mean"] is not None and (cs["mean"] > 0) == (sg > 0)) else "not replicated in cortex"
            return f"MOVED {word} ({rep})", " ".join(notes)
    return f"NOT MOVED (outside null in {len(outs)} of {len(ok)} counted contrasts)", " ".join(notes)

with open(f"{out}/verdicts.tsv", "w") as f:
    f.write("set\tverdict\tcounted_contrasts_centredR(*=outside null; s=animal-separated)\tC_S_cortex\n")
    for s in ORDER:
        v, n = verdict(s); c = RES[("C_S", 1.0)]["sets"][s]
        f.write(f"{s}\t{v}\t{n}\t{fmt(c.get('mean'))}{'*' if c.get('outside') else ''}{'s' if c.get('separated') else ''}\n")

json.dump(dict(seed=SEED, ndraw=NDRAW, thresholds_tpm=THRESH, inputs_sha256=dict(hippo=sha(hippo), cortex=sha(cortex), ensembl92_cdna=sha(fasta), it5_set_table=sha(p6)),
               n_genes=dict(hippo=len(hg), cortex=len(cg)), patch_transcript_tpm_share_dropped_hippo_mean=float(hdrop.mean() / 1e6),
               unknown_transcripts=dict(hippo=hunk, cortex=cunk), n_universe={c: RES[(c, 1.0)]["n_universe"] for c, *_ in CONTR},
               median_uncentred_R={c: RES[(c, 1.0)]["median_uncentred_R"] for c, *_ in CONTR},
               iqr_centred_R={c: RES[(c, 1.0)]["iqr_centred_R"] for c, *_ in CONTR}, wwox_gene=wwox_id, depth=depth, n_ribosome_ctl_genes=len(rib_ids)),
          open(f"{out}/results.json", "w"), indent=1)
print(open(f"{out}/verdicts.tsv").read())
