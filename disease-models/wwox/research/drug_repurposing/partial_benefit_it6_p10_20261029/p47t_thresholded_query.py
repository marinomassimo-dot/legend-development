#!/usr/bin/env python3
"""Query the derived text of the P47T supplementary differential-expression sheets (PMID 36828035) for named genes.

The sheets list only genes beyond the thresholds (|log2 ratio| > 1, FDR < 0.05 stated for the forebrain regions; the cerebellum sheet carries smaller ratios, down to about 0.4, so its threshold differs and is not stated here), so a
gene that is ABSENT here was not above threshold; that is NOT a measurement that it did not change. A positive log ratio is
read as higher in the homozygote (the orientation is inferred from the matching counts, see manifest entry 67).
Usage: p47t_thresholded_query.py <Supplementary_data_all_sheets_derived.txt>   (read-only; TSV to stdout)"""
import csv, sys
GROUPS = {
 'pan-reactive astrocyte': 'Gfap Vim Serpina3n Serpina3g Serpina3h Lcn2 Steap4 Cd44 Timp1 Osmr Cp Hspb1 Nes Aspg Gbp2 Fbln5 Psmb8 H2-D1 H2-T23'.split(),
 'complement and A1-type': 'C3 C1qa C1qb C1qc C4b C3ar1 Srgn Amigo2 Fkbp5 Iigp1 Serping1'.split(),
 'homeostatic astrocyte': 'Slc1a2 Slc1a3 Kcnj10 Gja1 Aqp4 Glul Adk Gjb6 Aldh1l1 Slc4a4 Atp1a2 Aldoc Sparcl1'.split(),
 'microglia': 'Aif1 Cx3cr1 Tmem119 P2ry12 Trem2 Tyrobp Cd68 Itgax Clec7a Cst7 Apoe Lyz2 Hexb Csf1r Spp1 Lgals3 Ccl2 Ccl3 Ccl4 Ccl5 Cxcl10'.split(),
 'cytokine and inflammasome': 'Il1b Il1a Il1r1 Il1rn Tnf Il6 Nlrp3 Casp1 Il18 Ptgs2 Stat3 Socs3 Jak2 Cebpd Nfkbia Icam1 Tlr4'.split(),
 'interferon-stimulated': 'Oas1f Oas1a Oas2 Oas3 Ifit1 Ifit3 Isg15 Irf7 Stat1 Mx1 Mx2'.split(),
 'immediate-early': 'Fos Fosb Jun Junb Egr1 Egr2 Npas4 Arc Nr4a1'.split(),
 'redox (outside the glial thread; listed once for the record)': 'Nfe2l2 Hmox1 Nqo1 Gclm Gclc Sod1 Sod2 Gpx1 Gpx4 Txnrd1 Prdx1 Slc7a11 Gsta4 Sesn2 Fth1 Ftl1 Cybb Ncf1 Ncf2 Mt1 Mt2 Mt3'.split(),
 'oligodendrocyte lineage and myelin': 'Mbp Plp1 Mog Mag Cnp Olig1 Olig2 Sox10 Pdgfra Cspg4 Enpp6 Mobp Gpr17 Cldn11 St18'.split(),
}
if len(sys.argv) != 2 or sys.argv[1] in ('-h', '--help'):
    print(__doc__); sys.exit(0 if len(sys.argv) == 2 else 2)
by = {}
for r in csv.DictReader(open(sys.argv[1]), delimiter='\t'):
    try: by.setdefault(r['Symbol'].split(' ')[0], {})[r['sheet']] = round(float(r['Expr_Log_Ratio']), 2)
    except ValueError: pass
print('group\tgene\tabove_threshold_in\tlog_ratio_by_region')
for g, genes in GROUPS.items():
    for s in genes:
        if s in by: print(f"{g}\t{s}\t{','.join(by[s])}\t{by[s]}")
        else: print(f"{g}\t{s}\tNOT LISTED\t")
