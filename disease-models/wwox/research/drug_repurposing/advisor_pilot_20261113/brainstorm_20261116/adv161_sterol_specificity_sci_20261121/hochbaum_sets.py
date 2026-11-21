"""ADV-161: apply the pre-registered gene sets and decision rules to Hochbaum 2024 Supplementary Tables S1 (MMC1) and S2 (MMC2).
Usage: python3 -I hochbaum_sets.py <MMC1.xlsx> <MMC2.xlsx>   (reads only; prints a report)."""
import sys
import os
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import xlsx_min

A = "Hmgcs1 Hmgcr Mvk Pmvk Mvd Idi1 Fdps Fdft1 Sqle Lss Cyp51 Tm7sf2 Msmo1 Nsdhl Hsd17b7 Dhcr24 Ebp Sc5d Dhcr7".split()
B = "Srebf2 Scap Insig1 Ldlr Pcsk9 Stard4 Acat2".split()
C = "Mbp Plp1 Mog Mag Mobp Cnp Opalin Cldn11 Ugt8a Gpr37 Enpp6 Tcf7l2 Bcas1 Fyn".split()
T = "Hr Klf9 Dio3 Ier5".split()
NAMED = ["inferred_OPC", "inferred_Oligo.Enpp6_2", "inferred_Oligo.Opalin_2"]
OTHER_GLIA = ["inferred_Oligo.Opalin_1", "inferred_Oligo.Opalin_4", "inferred_Astro.Aqp4_Slc7a10", "inferred_Astro.Aqp4_Gfap"]


def main(p1, p2):
    rows = xlsx_min.read_rows(p1)
    ix = {k: i for i, k in enumerate(rows[0])}
    data = rows[1:]
    sets = {"A": A, "B": B, "C": C, "T": T}
    states = sorted({r[ix["cell_subtype"]] for r in data})
    print("rows", len(data), "states", len(states))
    # TRG per authors: adjP < 0.05 and |robScore_logFC| >= 0.5
    def trg(r):
        return r[ix["adj.P.Val"]] < 0.05 and abs(r[ix["robScore_logFC"]]) >= 0.5
    print("\n== per state: number of rows, TRG rows (adjP<0.05 and |rob|>=0.5), and set hits (all listed / TRG) ==")
    for s in states:
        rs = [r for r in data if r[ix["cell_subtype"]] == s]
        line = f"{s:32s} listed {len(rs):4d} TRG {sum(trg(r) for r in rs):4d}"
        for nm, g in sets.items():
            hit = [r for r in rs if r[ix["gene"]] in g]
            th = [r for r in hit if trg(r)]
            line += f" | {nm} {len(hit)}/{len(th)}"
        print(line)
    print("\n== set rows in named and comparison glial states (gene, logFC, adjP, robScore_logFC, pctExpr ctrl->T3, numCells) ==")
    for s in NAMED + OTHER_GLIA:
        print("--", s)
        for r in data:
            if r[ix["cell_subtype"]] != s:
                continue
            for nm, g in sets.items():
                if r[ix["gene"]] in g:
                    print(f"   {nm} {r[ix['gene']]:8s} logFC {r[ix['pseudocell_logFC']]:+.3f} adjP {r[ix['adj.P.Val']]:.2e} rob {r[ix['robScore_logFC']]:+.3f} pct {r[ix['pctExpr_Ctrl']]:.3f}->{r[ix['pctExpr_T3']]:.3f} cells {int(r[ix['numCells']])} TRG {trg(r)}")
    print("\n== sets A and B across ALL states (gene: states listed) ==")
    for g in A + B:
        st = [(r[ix['cell_subtype']].replace('inferred_', ''), round(r[ix['pseudocell_logFC']], 2)) for r in data if r[ix['gene']] == g]
        print(f"  {g:8s} {st}")
    # Table S2: sterol/cholesterol/lipid terms
    m2 = xlsx_min.read_rows(p2)
    h2 = {k: i for i, k in enumerate(m2[0])}
    print("\n== Table S2 terms matching sterol|cholesterol|lipid|steroid|myelin|oligodendro (state, term, padj, NES) ==")
    for r in m2[1:]:
        name = r[h2["pathway"]].lower()
        if any(k in name for k in ("sterol", "cholesterol", "lipid", "steroid", "myelin", "oligodendro", "gliogenesis", "glial")):
            print("  ", r[h2["cell_subtype"]], "|", r[h2["pathway"]], "| padj %.2e NES %.2f" % (r[h2["padj"]], r[h2["NES"]]))
    print("\nS2 terms per state:", collections.Counter(r[h2["cell_subtype"]] for r in m2[1:]))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
