# Verdicts (sources A, B, C only; line numbers are file lines from grep -n of A and C)

## P1 — PARTLY
Quotes (A):
- L446-447: "...and two subclones (JH-iPS11 WKO-1C and WKO-2C) were established." (L445: "WWOX was knocked out in this line using CRISPR/Cas9")
- L694-695: "To further validate this observation, we used our previously described WWOX-KO WiBR3 human embryonic stem cell (hESC) system23 to generate unguided organoids" (Suppl. Fig. 4E-F)
- L953-954: "Taking advantage of our hESCs WWOX WT and KO system23, we treated WWOX-WKO cerebral organoids with a submaximal dose of A51 drug"
- L710 and L912: NSCs from "the latter described hESCs-WWOX-KO system"; ChIP-seq "in hESC-derived WWOX-KO and WT"
- L1221-1223: "multiple independent models, including the previously reported hESC-WWOX KO, WOREE and SCAR12 lines23, newly generated wildtype and WWOX-KO JH-iPS11 lines, and compound heterozygous WOREE patient-derived lines"
Panel B (Fig 1A): KO line labelled "JH-IPS11 KO"; WT "JH-iPS11 WT".
Comment: The JH-iPS11 CRISPR KO (clones WKO-1C, WKO-2C) and its role as the main Fig 1 system are supported. The source does NOT say WiBR3 is "only" a separate validation: besides the validation of the MYC finding (Suppl. Fig 4E-F), the WiBR3 hESC system is also used for the A51 drug treatment, NSC derivation and ChIP-seq, and is described as one of several independent models. "Main" is my reading of Fig 1 and the text, not a phrase in the source. Also "WiBR3 WT ... excepted" from the two-clones rule (L387-388).

## P2 — PARTLY (first half SUPPORTED; second half only by inference from C)
A, L1827-1829 (ref 23): "Steinberg DJ, Repudi S, Saleem A, et al. Modeling genetic epileptic encephalopathies using brain organoids. EMBO Molecular Medicine. 2021;13(8):e13610."
C, article-title: "Modeling genetic epileptic encephalopathies using brain organoids" (same title, same journal/volume/e-number as the matching reference) -> first half supported.
C (line 131): "generating WWOX knockout (KO) clones of the WiBR3 hESC line using the CRISPR/Cas9 system (Abdeen et al, 2018)"; Fig 4 legend (line 146): "RNA sequencing (RNA-seq) of week 15 COs and transcriptome analysis (WT: n = 2, KO: ..." ; Methods (line 158): "WiBR3 hES cell line and the generated iPS cell lines were maintained...".
Comment: C never mentions JH-iPS11 in the lines I checked (grep for JH-iPS11 not run on C; I only grepped WiBR3 etc.), and the KO comparison in C is described as WiBR3 KO vs WT. But C also contains iPSC lines (WSM, patient lines) and its Methods say "at least two hPSC lines used for each genotype (with the exception of the WiBR3 WT line)"; the sentence the RNA-seq legend gives does not itself say in the excerpt I read which cell lines fed the RNA-seq, only WT vs KO with n. So "from WiBR3 KO derivatives" is the natural reading of C but is not stated verbatim for the RNA-seq panel; a 2021 paper cannot contain JH-iPS11 (newly generated in 2026 per A L1222 "newly generated ... JH-iPS11").

## P3 — PARTLY (pattern SUPPORTED; ordering of the two patient groups not resolved)
A, L521-526: "At week 7, immunofluorescence analysis revealed a significant reduction in SATB2-positive cells concurrent with an expansion of the SOX2-positive population in WWOX-mutant organoids compared to controls (Fig. 1E-F) ... The severity of this neurogenic disruption demonstrated a genotype-dependent gradient, with WWOX knockout organoids exhibiting the most pronounced" [text continues on next line; not quoted].
B, panel F "SOX2+/nuclei count" (y: percentage of cells): WT lowest, KO highest, SCAR12 and WOREE in between.
HAND READINGS of medians from panel F (approximate, read from the image, not from data; +-5 points):
- WT ~13%
- WWOX-KO ~77% (box ~65-83%, only about 8 points)
- SCAR12 ~48%
- WOREE ~43%
Comment: SCAR12 vs WOREE are not clearly different (WOREE box wider, 35-71%, median marginally lower or equal), so the source does not support a SCAR12 < WOREE ordering; the gradient claim in the text is about KO being most severe. Panel F shows significance brackets (KO vs WT ****, KO vs SCAR12 and KO vs WOREE one star each as I read them; WT vs patient groups ****), consistent with the above but hand-read. Panel F SATB2 shows the converse (WT median ~7%, others ~0-1%).

