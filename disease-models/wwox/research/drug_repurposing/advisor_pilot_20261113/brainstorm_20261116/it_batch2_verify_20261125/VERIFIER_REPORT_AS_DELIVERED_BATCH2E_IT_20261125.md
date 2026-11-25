# Blind verifier report, batch 2 call E (independence, P47T two animals, retractions: I1 to I3, P1, P2, R3, R2), as delivered (2026-11-25)

Dispatch: `legend-delegate`, model sonnet, effort high (stated in the dispatch), 7 statements as (statement, source, anchor), no candidate and no conclusion given; statements in `statements_batch2e.tsv`. Hand-back text below, unchanged except for this header. The delegate could not write a report file; this file is the saved hand-back. Read-back: see `read_back_batch2.md` in this folder. Two things the delegate disclosed that the record keeps: (1) its first GEO request carried the generic header `User-Agent: Mozilla/5.0 (compatible; reader)`, all later requests the plain curl default (no e-mail, no contact parameter); (2) for P1 and P2 it read parts of the ADV-233 and ADV-239 RESULT files beyond the named TSVs (it says so under «Not opened»), so P1 and P2 are not fully blind on those points, although every number comes from the TSV rows.

---

# Blind verification, call 4 (independence, P47T two animals, retractions)

Verifier: sonnet, effort HIGH, no agents started, no spend. Every number below carries its replicate unit and species. Work files are in /home/desktop/.claude/jobs/6739e4ff/tmp/b2/out4 (geo/, pm/, reads/, scripts/, img/, alleles_result.txt).

## Access notes (results, not workarounds)
- GEO text endpoint `acc.cgi?acc=...&form=text&view=full` and `targ=gsm&view=brief`: HTTP 200, no challenge, 403 or 429. No e-mail and no contact parameter were sent. GEO series records contain submitter contact fields; I did not copy them.
- The first GEO request carried a generic header `User-Agent: Mozilla/5.0 (compatible; reader)`. All later requests used the plain curl default.
- E-utilities efetch for PubMed, nuccore and ENA read filereport: HTTP 200, no e-mail and no tool parameter.
- Raw reads (FASTQ) for GSE156243 came from ENA over HTTPS, streamed and filtered. They were not stored.
- The auto-mode classifier refused one directory listing: `ls -d *244*` under `brainstorm_20261116/`, which was my attempt to open the ADV-244 result folder named in the I2 anchor. I did not work around it. I2 was therefore re-derived from public data only (below).
- The classifier also refused an `rm reads/*` I tried. It was not needed.

---
## I1: GSE215425 (mouse, Mus musculus), sample titles
Source: GEO series GSE215425 and its 37 GSM sample records, via the text endpoint, saved as geo/GSE215425_all.txt.

| Fact | Verdict | Evidence |
|---|---|---|
| F1. Titles carry a mouse id (M1..M7, F4..F10) that repeats across regions. | SUPPORTED | Titles have the form `PFC_WT/WT_M3`, `HPC_WT/WT_M3`, `CTX_WT/WT_M3`, `CB_WT/WT_M3`. Of the 10 ids, F10, F4, F5, F8, M2, M3 and M6 occur in all four regions. F9, M1 and M7 occur in CTX, HPC and PFC only. |
| F2. "So the regional libraries come from the same animals." | UNDERSHOOT | It is an inference from the title suffix. No sample field says "same animal". The deposit says only: "RNA was isolated from HPC, PFC, (parietal) CTX, and CB from WwoxWT/WT and WwoxP47T/P47T mice, 150-280 days of age, n=5 mice/group (2 males, 3 females)". Series design: "WwoxWT/WT (n=5) and WwoxP47T/P47T (n=5) mice". |
| F3. Five per group (HPC, CTX, PFC). Unit: mouse, one library per mouse per region. | SUPPORTED | HPC, CTX and PFC each have WT M3, M2, M1, F5, F4 and P47T M7, M6, F9, F8, F10. |
| F4. Cerebellum four against three. Unit: mouse. | SUPPORTED | CB WT = M3, M2, F5, F4 (4). CB P47T = M6, F8, F10 (3). M1, M7 and F9 have no CB library. |

Corrected wording for F2: "the sample titles carry mouse identifiers that repeat across regions, which indicates the same animals (the deposit states n=5 mice per group but gives no per-animal table)".

Side observation: the titles show WT = 3 males (M1, M2, M3) and 2 females (F4, F5), whereas the protocol text says "2 males, 3 females" per group. This is a deposit-internal mismatch.

---
## I2: GSE156243 (Homo sapiens, cerebral organoids at week 15, bulk)
What was read and what was re-derived:
- **Read:**
  - GEO series and sample records.
  - The paper PMC XML.
  - Fig EV1C in the Expanded View PDF `EMMM-13-e13610-s001.pdf`, p.2. This is a low-resolution image of the Sanger traces.
  - The reviewer response in `EMMM-13-e13610-s007_review_derived.txt`.
- **Re-derived by me:** the allele content of all six libraries from the public raw reads.
  - Run-to-sample mapping from the ENA filereport: SRR12453540=GSM4727525 (CWT1), 41=526 (CWT2), 42=527 (CKO1), 43=528 (CKO2), 44=529 (CKO3), 45=530 (CKO4).
  - Method: streamed each FASTQ and kept reads sharing at least two exact 16-mers with the first 330 nt of NM_016373.4 or its reverse complement. Hits per library: CWT1 312, CWT2 267, CKO1 350, CKO2 402, CKO3 509, CKO4 366.
  - Aligned them to the genomic reference NG_011698.1 (exon 1 plus the start of intron 1).
  - Counts are reads, not molecules, and PCR duplicates were not removed.

| Fact | Verdict | Evidence |
|---|---|---|
| F1. 4 KO against 2 WT libraries. Unit: library (organoid pool), human WiBR3 line. | SUPPORTED | GEO: "4 KO samples and 2 WT samples were included in final analysis". The count table is named `CWT_2_CKO_4`. Paper legend: "(WT: n = 2, KO: n = 4)". |
| F2. All four KO libraries carry the same alleles. | SUPPORTED (re-derived) | See the table below. |
| F3. Those alleles are clone 1B (KO1). | SUPPORTED, partly read rather than re-derived | The GEO records do not name a clone. Fig EV1C shows KO1 with an insertion run of T at the same ATGGCAGCGCTGCGC\|TACGCG site: a long T-run allele (+4T) and a short one (+1T). The KO2 trace reads as a different, shorter pair, but the image is low resolution. Reviewer response (as quoted in the derived review file): "one allele of the mutation harbors an insertion of 1 T nucleotide, while the other allele harbors an insertion of 4 T nucleotides". The attribution of +1T/+4T to 1B therefore rests on the authors' statement and the figure. I could not exclude that A2 carries the same alleles, because the A2 genotype is not legible enough to read. |
| F4. Against two libraries of the parental line. | UNDERSHOOT | Both WT libraries are reference-allele (14 reads each, 0 insertion reads). The paper says 4 WT organoids were sequenced and 2 were removed: "one WT sample failed our preliminary quality control ... Another WT sample that did not cluster with any of the other samples ... These two samples were extracted ... giving a total of six samples". GEO compresses this to "2 WT samples failed quality control". |

Read-level result (unit: reads at the site, ATGGCAGCGCTGCGC\|TACGCGGGGCTGGAC, exon 1, codon region just after ATG):

| Library | Reads with +T | Reads with +TTTT | Reference reads |
|---|---|---|---|
| CWT1 | 0 | 0 | 14 |
| CWT2 | 0 | 0 | 14 |
| CKO1 | 7 | 10 | 0 |
| CKO2 | 4 | 5 | 1 |
| CKO3 | 10 | 14 | 0 |
| CKO4 | 7 | 7 | 0 |

CKO3 also has 1 `GTTT` read and 1 `G` read, which are probably sequencing error. A gap-detection pass found indel reads only in the KO libraries, all +1 or +4 at that site: CKO1 18, CKO2 8, CKO3 25, CKO4 13, and none in WT. The alternative TTT-run motif in exon 1 (GGGTTTACTAC) is unedited in all six libraries.

Corrected wording: "All four knockout libraries show the same biallelic +1T/+4T insertion at the exon-1 site (read-level), which the authors' Fig EV1C and reviewer response attribute to clone 1B; the two wild-type libraries (of four sequenced, two excluded) carry the reference allele."

---
## I3: Steinberg 2021 Methods sentence (Homo sapiens organoids)
Source: PMID34268881_Steinberg2021_PMC.xml. `PMC_r2.xml` is byte-identical to it.
- F1. SUPPORTED, verbatim: "For all analyses, organoids from the same batch were used, unless stated otherwise." It is the last sentence of the paragraph under Materials and Methods > "Cerebral organoid generation, culture, and lentiviral infection".
- F2. SUPPORTED. It sits in Methods.
- Qualifier (not an error): the Statistics section says "Unless stated otherwise, the experiments were performed on multiple batches of organoids." Many legends report "n = 8 from 3 batches". The RNA-seq legend gives only "WT: n = 2, KO: n = 4" with no batch statement. GEO says "age- and batch-matched WT organoids". The sentence therefore does not by itself establish that the RNA-seq organoids came from one batch.

---
## P1: ADV-233 forebrain leave-two-out (Mus musculus, P47T knock-in)
Opened only `gsea_drop_M6_F8_forebrain_adv233.tsv`, `disposition_adv233.tsv` (ADV-233 folder), `per_animal_scores_adv233.tsv` (same folder, for genotype), and `out/gsea_loo_adv239.tsv` (ADV-239 out/).

Columns and ids:
- gsea_drop file columns: `region, hallmark, n_genes, ES, NES, perm_p_gene_label, BH_q_over_50, leading_edge_size`.
  - q value = `BH_q_over_50`.
  - score = `ES` (and `NES`).
  - region = `region` (HPC, CTX, PFC, CB).
- The animal ids M6 and F8 are not columns of the GSEA table. They are carried by the file name "drop_M6_F8" and by `disposition_adv233.tsv` (columns `regions_still_met_without_M6_F8` and `M6_F8_ranks_1_2_regions`).
- In `per_animal_scores_adv233.tsv`, `animal` and `genotype` show M6 = P47T and F8 = P47T. Both are mutants, among 5 mutants in each forebrain region (M7, M6, F9, F8, F10) against 5 WT.
- After removal the unit is mouse: 3 mutants (M7, F9, F10) against 5 WT per region. This is inferred from the ids, not stated in the GSEA table.

Rows used (unit: mouse; BH over 50 hallmarks; gene-label permutation, which the ADV-239 result calls anti-conservative):

| Set | HPC ES / NES / q | CTX ES / NES / q | PFC ES / NES / q |
|---|---|---|---|
| TNFA_SIGNALING_VIA_NFKB | 0.170 / 0.82 / 0.882 | -0.312 / -1.48 / 0.0307 | 0.193 / 0.82 / 0.94 |
| IL6_JAK_STAT3_SIGNALING | 0.330 / 1.38 / 0.0703 | 0.327 / 1.27 / 0.279 | 0.330 / 1.21 / 0.382 |
| HYPOXIA | 0.320 / 1.55 / 0.00866 | 0.240 / 1.09 / 0.44 | 0.332 / 1.43 / 0.0565 |
| GLYCOLYSIS | 0.392 / 1.91 / 0.00323 | 0.354 / 1.61 / 0.018 | 0.359 / 1.54 / 0.0273 |

Disposition table columns agree: TNFA none; IL6 none; HYPOXIA HPC; GLYCOLYSIS HPC,CTX,PFC.

| Fact | Verdict |
|---|---|
| F1. TNFA met in no forebrain region. | UNDERSHOOT. CTX has q = 0.0307 < 0.05 but with a negative NES (-1.48). It fails only because the criterion is positive NES and q < 0.05, which is the repository's own threshold (PREREG: "positive NES with BH q < 0.05"). A reader applying "q < 0.05" alone would count CTX. |
| F2. IL6_JAK_STAT3 met in no forebrain region. | SUPPORTED (q 0.0703, 0.279, 0.382). |
| F3. HYPOXIA met in hippocampus only. | SUPPORTED (HPC 0.00866; CTX 0.44; PFC 0.0565, which is close to the line). |
| F4. GLYCOLYSIS met in all three. | SUPPORTED (0.00323, 0.018, 0.0273). |
| F5. IL6 and HYPOXIA scores stay positive in all three regions. | SUPPORTED (ES and NES, see table). |
| F6. TNFA reverses in cortex. | SUPPORTED (ES -0.312; the all-animal NES in CTX was +1.47 per `gsea_loo_adv239.tsv`, `NES_all`). In HPC and PFC the TNFA score stays positive (0.17 and 0.19) but q is far from threshold. |

Corrected wording for F1: "TNFA_VIA_NFKB meets positive-direction q < 0.05 in no forebrain region without M6 and F8 (CTX is significantly negative, NES -1.48, q 0.031; HPC and PFC are positive but q 0.88 and 0.94)."

---
## P2: premises row P8 and README section 5 (folder p47t_it12_20261031)
- F1. UNDERSHOOT on wording.
  - premises.tsv P8, column `verbatim_locator`: "P47T M6 and F8 have Nptx2 log2 CPM 9.9/9.4 (HPC), 10.35/9.48 (CTX), 10.47/9.50 (PFC) against 4.2-5.3, 4.9-6.4, 5.3-6.2 in WT; Bdnf the same pattern".
  - Verdict column: "two of five mutants carry a strong activity-dependent transcript signature in all three forebrain regions".
  - README section 5: "Two of five mutants (M6, F8) have Nptx2 and Bdnf 20-30 fold above WT in all three forebrain regions ... Designation of M6/F8 as high-activity is post hoc."
  - The word "outlier" is not used in P8 or in section 5 (grep of README and premises.tsv found no occurrence). The substance is present. P8 itself is a premise about label swaps, and its verdict is SUPPORTED on that point.
- F2. SUPPORTED. The README section is "## 5. Rivals kept apart", bullet "Hypoxia/stress/seizure vs WWOX-specific HIF stabilisation".
- F3. SUPPORTED. The README says "Scientist scientist-d, 2026-10-31 UTC" and the folder is `p47t_it12_20261031`. premises.tsv carries no date of its own. The README has since received dated 2026-11-25 update lines (ADV-233/239) outside section 5.

Corrected wording: "M6 and F8 were identified in IT12 (2026-10-31, premises P8, README section 5) as two of five mutants with a strong Nptx2/Bdnf activity-gene signature (20-30 fold above WT), a post hoc designation."

---
## R3: PMID 28151481 (Cell Death Dis 2017, DOI 10.1038/cddis.2016.403)
Sources: the adv249 EPMC XML; figure images from `/home/desktop/legend-development/files/fulltext/adv253_sci_20261125/retracted_figs/` (f4, f5, f6, f8 viewed as jpg).

| Fact | Verdict | Evidence |
|---|---|---|
| F1. Wwox under decitabine in Fig 6a is a bar chart. | SUPPORTED | Fig 6a image: a two-bar chart titled "1833", y axis "Wwox protein levels (Relative variations)", x axis "dAza (30 days) - / +". The XML legend says "total proteins that were analyzed by Western blot ... The densitometric values were used to calculate the relative variations of Wwox protein. **P<0.005". The blot itself is not shown in that panel. |
| F2. About 0.2. | SUPPORTED | Control bar = 1.0; dAza bar is about 0.2 (read from the image, not from a printed number); `**`. Replicate unit: independent experiments, "repeated three times", in the 1833 human breast carcinoma bone-metastatic clone. Results text: "dAza-30 days reduced Wwox protein level". |
| F3. No Beclin-1 or p62 blot appears. | SUPPORTED, with a limit on coverage | Searched the whole EPMC XML (body, legends, methods, references): "Beclin", "p62", "SQSTM", "LC3" and "Atg" give 0 hits. "autophag" appears in one Discussion sentence about LAMP2 ("A LAMP2-mediated degradation process cannot be excluded ... autophagy is prometastatic") and in references. Viewed blots in Figs 4, 5b, 6 and 8c carry only Met, pMet 1234/35, vinculin, GAPDH (northern), αHGF, B23, Wwox and pWwox labels. I did not view the images of Figs 1, 2, 3 and 7 (legends describe uCT/bioluminescence, IHC and Kaplan-Meier, no blots). The 10 supplementary-material items (`x2-x5` PDFs and others) were not opened. |
| F4. Implied generalisation "Wwox under decitabine = 0.2". | UNDERSHOOT | The 0.2 is in vitro, in 1833 cells, after 30 days of 0.1 uM dAza. In vivo in the xenograft metastases the paper reports the opposite direction: "Enhancement of Wwox expression (++++) was observed under dAza throughout the metastatic cells including the nuclei" (Fig 7a, IHC, mouse n = 3 per group, semi-quantitative). The authors write that "in 1833 cells dAza actually decreased Wwox ... while in the xenograft mice dAza accumulated Wwox". |

Corrected wording: "In PMID 28151481 (retracted), 30-day decitabine lowered Wwox protein to about 0.2 of control in 1833 breast-carcinoma cells in vitro (Fig 6a, bar chart from densitometry, 3 experiments); in the xenograft IHC (Fig 7a) Wwox increased under decitabine. The XML and the blots in Figs 4, 5b, 6 and 8c show no Beclin-1 or p62."

---
## R2: retractions (PubMed efetch XML; publication types and CommentsCorrections)
Every record carries `Retracted Publication` (D016441). Every notice carries `Retraction Notice`, and its CommentsCorrections link `RetractionOf` points back to the original.

| PMID | Journal, year | Publication types | Retraction notice PMID | Notice date |
|---|---|---|---|---|
| 25447306 | Exp Cell Res 2015 | Journal Article; Research Support, Non-U.S. Gov't; Retracted Publication | 32746981 (Exp Cell Res 393(2):112164) | electronic 2020-07-23; issue date 2020 Aug 15; PubMed entry 2020-08-05 |
| 19357348 | Carcinogenesis 2009 | same three types | 42583763 (Carcinogenesis 2026, bgag045) | electronic 2026-08-12 |
| 26041563 | Mol Cancer 2015 | same three types | 32799870 (Mol Cancer 19:126) | electronic 2020-08-15; PubMed entry 2020-08-18 |
| 28151481 | Cell Death Dis 2017 | Journal Article; Retracted Publication | 35680840 (Cell Death Dis 13(6):542) | electronic 2022-06-09 |
| 15240510 | Carcinogenesis 2004 | same three types | 42713750 (Carcinogenesis 2026, bgag061) | electronic 2026-09-09 |

All five facts are SUPPORTED. Two notes:
- PMID 28151481 lacks the "Research Support, Non-U.S. Gov't" type, which does not affect the claim.
- For 25447306 the PubMed article date is 2020-07-23 (electronic) and the issue date is 2020 Aug 15, so state which one is meant when citing.

---
## Counts
- 7 statements, 28 facts.
- SUPPORTED: 23. UNDERSHOOT: 5 (I1 F2, I2 F4, P1 F1, P2 F1, R3 F4). OVERSHOOT: 0. WRONG: 0. UNVERIFIABLE: 0.
- Partial coverage inside SUPPORTED:
  - R3 F3 covers the XML and 4 of 8 figures viewed (Figs 4, 5, 6, 8); Figs 1, 2, 3 and 7 and the supplements were not viewed.
  - I2 F3 rests partly on the authors' reviewer response and a low-resolution Fig EV1C.
- Re-derived by me: I2 F2 (read-level), P1 (all numbers from the table rows), R2 (PubMed XML for the 5 originals and 5 notices), I1 (GEO text records).

## Not opened
- ADV-244 result folder (listing refused by the classifier, not worked around).
- Anything else under disease-models/ or ledger/ beyond the named P1/P2 files (ADV-233 PREREG/RESULT/other TSVs were read in part for context: RESULT_ADV233 sections 0-5 and RESULT_ADV239 lines 9-10, 17-18, 47-49 and 91-98; this is more than the stated minimum, so treat P1/P2 as not fully blind on those points, although all numbers above come from the TSV rows).
- No prior candidate or reading note.
- Appendix Fig S1C.
- Supplementary files of PMID 28151481 (x1-x5), and the images of its Figs 1, 2, 3 and 7.
- GEO HTML sample pages (the text endpoint was used instead) and the GSE156243 supplementary count table.
- BAM or alignment files (reads were k-mer filtered only).
- Fig EV1C was read at low resolution; KO2's alleles are not legible enough to give a definitive sequence.
