#!/usr/bin/env python3
"""IT10 P2.1, premise (a): can culture time / maturity markers / organoid-stress state account for the size of the
KO-versus-WT shift of HIF-axis, glycolysis, hypoxia-response and organoid-stress genes in GSE156243 (4 KO v 2 WT libraries)?

Question (declared before running): for each gene g, (1) what is the KO/WT log2 shift, (2) what shift would the observed
KO/WT shift of the progenitor and neuronal marker panels predict, using the coupling slope of log2 g on log2 marker
within iPSC line in GSE150123 (WWOX-unperturbed cortical spheroids, 25-652 days), and (3) is the gene time-confounded.
Reuses (does not modify) gse156243/maturation_calibration.py for the pinned inputs. Transcript level only; no flux, no protein.
Run: python3 -I maturity_stress_check_it10_p21.py   (reads files/geo of the main checkout; writes TSVs next to this script)
"""
import csv, gzip, importlib.util, math, statistics, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MC = HERE.parent / "gse156243" / "maturation_calibration.py"
spec = importlib.util.spec_from_file_location("mc", MC); mc = importlib.util.module_from_spec(spec); spec.loader.exec_module(mc)

GROUPS = {
 "HIF_axis": ["HIF1A", "EPAS1", "ARNT", "EGLN1", "EGLN2", "EGLN3", "VHL"],
 "glycolysis_HIF_targets": ["SLC2A1", "HK2", "LDHA", "LDHB", "PGK1", "ALDOA", "ENO1", "PFKP", "PKM", "BNIP3", "PDK1"],
 "hypoxia_response_other": ["VEGFA", "ADM", "NDRG1", "ANKRD37", "BHLHE40", "P4HA1", "DDIT4", "ERO1A", "CA9", "ENO2"],
 "organoid_stress_Bhaduri": ["PGK1", "ARCN1", "GORASP2", "HSPA5", "DDIT3", "ATF4", "XBP1"],
 "astro_oligo_composition": ["GFAP", "AQP4", "S100B", "SLC1A3", "ALDH1L1", "OLIG2", "MBP"],
 "MYC_axis": ["MYC", "MYCN"],
}
PROG = ["VIM", "NES", "SOX9", "SOX2", "PAX6", "HES1"]
NEUR = ["STMN2", "MAP2", "SYT1", "RBFOX3", "TUBB3", "SNAP25"]

def deposited_padj():
    """Authors' deposited DESeq2 up/down lists (padj<=0.05 only) as carried in gse156243/derived; absence from the list is not 'no change'."""
    t = {}
    with (HERE.parent / "gse156243" / "derived" / "list_padj_le_0.05.tsv").open(encoding="utf-8") as h:
        for r in csv.DictReader(h, delimiter="\t"): t[r["symbol"]] = (float(r["padj"]), float(r["log2FoldChange"]))
    return t

def main():
    mc.verify_inputs()
    dep = deposited_padj()
    genes = sorted({g for v in GROUPS.values() for g in v} | set(PROG) | set(NEUR) | {"WWOX"})
    # KO v WT (GSE156243)
    with gzip.open(mc.KO_COUNTS, "rt", encoding="utf-8") as h:
        r = csv.reader(h, delimiter="\t"); next(r); rows = {x[0]: [float(v) for v in x[1:]] for x in r}
    tot = [sum(rows[g][i] for g in rows) for i in range(6)]
    ko = {}
    for g in genes:
        if g not in rows: ko[g] = None; continue
        cpm = [rows[g][i] / tot[i] * 1e6 for i in range(6)]
        k, w = statistics.fmean(cpm[:4]), statistics.fmean(cpm[4:])
        ko[g] = dict(ko_cpm=k, wt_cpm=w, shift=math.log2((k + 1) / (w + 1)), min_raw=min(rows[g]), raw_wt=rows[g][4:], raw_ko=rows[g][:4],
                     separated=(min(cpm[:4]) > max(cpm[4:])) or (max(cpm[:4]) < min(cpm[4:])))
    # coupling and time slopes (GSE150123)
    s2e = mc.symbol_to_ensg(); wanted = {g: s2e[g] for g in genes if g in s2e}
    meta, data = mc.calibration_matrix(wanted)
    titles = sorted(data)
    lines = [meta[t]["iPSc line"] for t in titles]
    days = [float(meta[t]["differentiation day"]) for t in titles]; logd = [math.log10(d) for d in days]
    def l2(t, g): return math.log2(data[t]["genes"].get(g, 0.0) / data[t]["total"] * 1e6 + 1)
    y = {g: [l2(t, g) for t in titles] for g in wanted}
    mean_count = {g: statistics.fmean(data[t]["genes"].get(g, 0.0) for t in titles) for g in wanted}
    d_marker = {m: ko[m]["shift"] for m in PROG + NEUR if ko.get(m)}
    out = []
    for grp, gl in GROUPS.items():
        for g in gl:
            if g not in wanted or ko.get(g) is None:
                out.append([grp, g, "ABSENT_FROM_TABLE", "", "", "", "", "", "", "", ""]); continue
            sl = mc._line_slopes(lines, logd, y[g]); k = len(sl)
            if k >= 3:
                m_ = statistics.fmean(sl.values()); sd = statistics.stdev(sl.values()); half = mc._T975.get(k - 1, 1.96) * sd / math.sqrt(k)
                tslope = f"{m_:+.2f} [{m_-half:+.2f},{m_+half:+.2f}]"; tconf = (m_ - half > 0) or (m_ + half < 0)
            else: tslope, tconf = "NA", False
            preds = []
            for m, dm in d_marker.items():
                if m == g: continue
                b = mc._pooled(lines, y[m], y[g]) if statistics.pstdev(y[m]) > 0 else None
                if b is not None: preds.append((m, b * dm))
            pv = sorted(p for _, p in preds)
            med = statistics.median(pv) if pv else float("nan")
            out.append([grp, g, f"{ko[g]['shift']:+.2f}", f"{ko[g]['ko_cpm']:.1f}/{ko[g]['wt_cpm']:.1f}", f"{ko[g]['min_raw']:.0f}",
                        "yes" if ko[g]["separated"] else "no", tslope, "yes" if tconf else "no",
                        f"{med:+.2f} [{pv[0]:+.2f},{pv[-1]:+.2f}]" if pv else "NA", f"{mean_count[g]:.0f}",
                        (f"{dep[g][0]:.2g} / {dep[g][1]:+.2f}" if g in dep else "not on the padj<=0.05 list")])
    hdr = ["group", "gene", "KO_vs_WT_log2_shift_GSE156243", "meanCPM_KO/WT", "min_raw_count_any_library", "all4KO_beyond_both_WT", "culture_time_slope_per_log10day_GSE150123_[between-line_95pct]", "time_confounded_(interval_excludes_0)", "marker_predicted_shift_median_[min,max]_over_12_markers", "mean_raw_count_GSE150123", "deposited_DESeq2_padj_(list_padj<=0.05_only)_and_log2FC"]
    with (HERE / "maturity_stress_check_it10_p21.tsv").open("w", newline="") as h:
        w = csv.writer(h, delimiter="\t"); w.writerow(hdr); w.writerows(out)
    mk = [["marker", "panel", "KO_vs_WT_log2_shift_GSE156243"]] + [[m, "progenitor" if m in PROG else "neuronal", f"{d:+.2f}"] for m, d in d_marker.items()]
    with (HERE / "maturity_markers_it10_p21.tsv").open("w", newline="") as h:
        csv.writer(h, delimiter="\t").writerows(mk)
    print("\t".join(hdr)); [print("\t".join(map(str, r))) for r in out]; print(); [print("\t".join(r)) for r in mk]
    print("informative lines:", len(set(lines)), "samples:", len(titles))
main()
