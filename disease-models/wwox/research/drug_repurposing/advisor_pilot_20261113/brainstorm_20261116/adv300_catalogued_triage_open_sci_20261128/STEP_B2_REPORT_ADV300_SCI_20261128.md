# ADV-300 step B batch 2 (records 3, 4) full-text reader; one response withheld by a safety classifier, as the report says

legend-delegate, claude-sonnet-5-5, effort high on 26 of 26 model turns read back. Model output, hypothesis level, not medical advice; saved verbatim.

---

ADV-300 full-text check, step B2 (public literature, hypothesis level, reference genotype class only; not medical advice).

**Process notice, read first.** Partway through, a safety classifier stopped one of my responses and withheld the rest. This happened right after I had read the record-4 supplementary PDF text. I did not reproduce the withheld content. I then continued with keyword searches, the two supplementary figure pages and this report, and I print no sequence material. Please weigh the report knowing that interruption happened.

**Result:** record 3 (29662317) has 0 counted data and one borderline item. Record 4 (28769061) has 2 counted data, the second weaker than the first.

Paths below are relative to /home/desktop/legend-development/.claude/worktrees/sci_aw_20261128/disease-models/wwox/ .

## Record 3, PMID 29662317

**(1) What it is.** A meta-analysis of published human case-control studies of three WWOX SNPs and malignant tumour risk. All studies are Asian except one Caucasian thyroid series. It generated no new genotypes and no cell data.
- rs3764340 C>G (the paper places it in exon 8): 8 comparisons, 6,177 cases and 6,606 controls. A control group shared by two studies is counted twice.
  - CG vs CC: OR 1.31 (1.12-1.53).
  - GG+CG vs CC: OR 1.31 (1.11-1.54).
  - G vs C: OR 1.28 (1.09-1.50).
  - GG vs CC: OR 1.36 (0.90-2.04), not significant.
- rs383362 and rs12918952 (4 studies each): no overall association. Some genotyping-method subgroups are positive.

**(2) Counted data:** none.

**(3) Uncounted data worth knowing**

(a) **Borderline, needs a check outside this paper.**
- The paper never names the protein change of rs3764340. From my background knowledge, not from the paper or any held file I searched, rs3764340 C>G is p.Pro282Ala (P282A). Please verify this before use.
- The held sentences it would touch are these.
  - research/therapeutic_hypotheses_ledger_current.md:440, "Lo stesso paziente porta **P282A**: stesso dominio SDR, **proteina stabile, nessun legame con HSC70** — e **completamente priva di funzione** (non inibisce crescita né invasione, in vitro e in vivo; perde il binding a POLE4)."
  - Same file, line 445: "Il paziente omozigote P252A+P282A **non aveva malattia neurologica**: sono **ipomorfi** [...]".
- If the identity holds, P282A is a common SNP, and a changed sentence would add: "P282A is the common SNP rs3764340; the G allele carries a pooled cancer OR of 1.28 in case-control data, and GG homozygotes occur among cancer-free controls."
- My arithmetic on the Table 1 rows, counting the shared Guo controls once: GG in 48 of 6,010 controls (0.80%), G allele frequency about 7.2%. These genotype counts come from the cited studies, not from this paper.
- I did not count it because the link to the held sentence depends on an identity the paper does not state.

(b) **rs12918952.**
- No overall susceptibility association: A vs G OR 1.12 (0.92-1.35). No prostate study is included.
- research/discovery_ledger_current.md:1469 (biochemical recurrence in prostate) and DL-MECH-158 at line 4324 (which allele GTEx calls "Alt") would read the same.
- A is the minor allele, roughly 5-7% in the four control groups. This does not answer the GTEx question.

(c) **Reliability problems in the paper itself** (relevant before anyone cites it):
- The "P" values printed beside the ORs (0.031, 0.014, 0.009) are heterogeneity P values. Table 2 heads them Ph, and Figure 2 prints "I2=54.7%, P=0.031". They are not association P values.
- Figure 2 lists "Cancemi" twice and "Guo" once, while Table 1 has one Cancemi row and two Guo rows. By my arithmetic the second "Cancemi" estimate (1.52) equals the Guo gastric counts.
- Table 1 gives Cheng as TaqMan, and the rs3764340 TaqMan subgroup size includes it. Figures 3 and 4 put Cheng in the PCR subgroup for the other two SNPs. The method-subgroup findings for those two SNPs therefore rest on an assignment that contradicts Table 1.
- Table 4 prints a confidence interval "0.62–0.768" for AA vs GG; Figure 4 shows 0.62-7.68.
- Guo controls deviate from Hardy-Weinberg equilibrium (P=0.025).

(d) **Incidental, in held files, not from this paper.** research/therapeutic_hypotheses_ledger_current.md:440 and research/discovery_ledger_current.md:1164 still place P282A in the SDR domain. discovery_ledger_current.md:39 and :1143 correct this (only P252A falls inside residues 125-262).

## Record 4, PMID 28769061

**(1) What it measured.** A study of the human lncRNA PARTICLE and predicted RNA:DNA:DNA triplex sites.
- **In silico:** 14 predicted sites in human WWOX and 10 in mouse Wwox; about 1,600-7,200 human loci depending on the tool; a pathway analysis.
- **In vitro:** surface plasmon resonance (performed six times; shift 0.19 ± 0.04 nm against about 0.02 for controls) and gel shift with short oligos.
- **Transcript:** WWOX mRNA by TaqMan after PARTICLE knockdown (two siRNAs) or overexpression, n = 3 per the statistics.
- **Cells:** viability in MDA-MB-361 breast cancer cells; RNA FISH co-localisation in U2OS osteosarcoma cells after 0.25 Gy.
- **Not measured:** no WWOX protein, no neural cell, no WWOX variant.

**(2) Counted data**

**Datum 1: PARTICLE level moves WWOX mRNA in the opposite direction.**
- Locator: text section "PARTICLE influences WWOX transcript levels"; Figure 3A; Figure S2A (MOESM1 PDF page 7).
- Knockdown (97% and 96%) raises WWOX mRNA. The text says "0.7" and "0.8 fold increase"; the bars read about 1.9 and 2.0 against about 1.0.
- Overexpression (21-fold) lowers it; the bar reads about 0.2.
- Cell line: the Fig 3A and S2A legends say U2OS, the Discussion says MDA-MB-361, and the Results text names none.
- Held sentence, research/therapeutic_hypotheses_ledger_current.md:225: "tre leve indipendenti documentate su WWOX endogeno — miR-153 (repressore, 3'UTR), contesto **Kozak rs11545028** [...], sito **Sp1/Sp3 rs11644322** [...]. Tutte agiscono sul **trascritto endogeno, non allele-specificamente**."
- Changed sentence: "Four documented levers on endogenous WWOX: miR-153, the Kozak context rs11545028, the Sp1/Sp3 site rs11644322, and the lncRNA PARTICLE (knockdown raises WWOX mRNA about 1.7-2-fold and overexpression lowers it to about 0.2; human cancer cells, legends say U2OS; mRNA only, no protein)."

**Datum 2 (weaker, prediction level): a cluster of predicted PARTICLE sites in WWOX intron 8.**
- Locator: Table S2 (MOESM1, page 3); Figure 1B. Of the 14 predicted human sites, 11 are labelled intron 8, eight of them in tandem near 78.6386-78.6387 Mb (GRCh37).
- A probe just upstream (78,638,458-554) co-localises with PARTICLE on irradiated U2OS chromosome spreads, R = 0.91, against about 0.02 for a chr11 control (Fig 4I-L).
- Held sentence, research/discovery_ledger_current.md:3568 (DL-MECH-107): "**What sits in that one intron — four independent things.**" followed by items (1)-(4).
- Changed sentence: "Five things sit in that intron: the four listed, plus a tandem cluster of in-silico predicted triplex target sites for the lncRNA PARTICLE (PMID 28769061), with FISH co-localisation beside it in U2OS; binding at this cluster is not shown in vitro, and there are no allele or neural data."
- On the in-vitro limit: Table S4 describes the tested oligo as the antiparallel target site, while Table S2 marks the tandem cluster as parallel. That the cluster was not tested is my reading of those labels. Figure 2A does draw one cluster site as a predicted pairing.

**(3) Uncounted data worth knowing**
- **Radiation induces WWOX mRNA strongly and transiently. This is supplement-only (Fig S1, MOESM1 page 6) and the main text does not report it.** MDA-MB-361, relative to sham, approximate values read off a low-resolution image:

| Dose | 2 h | 4 h | 24 h |
|---|---|---|---|
| 0.25 Gy | about 22 | about 11 | about 1 |
| 2.5 Gy | about 12 | about 15 | near baseline |
| 5 Gy | about 17 | about 12 | near baseline |
| 0.025 Gy | none | none | none |

  - I found no held sentence it would change. CLAIM 029 (registries/claim_registry_current.md:605) describes ubiquitination, nuclear accumulation and ATM interaction after DNA damage and would read the same. DL-MECH-126 (discovery_ledger_current.md:3958) concerns chronic replication stress in a non-cancer cell. It is the closest candidate if someone holds that the damage response is post-translational only.
  - In the same figure PARTICLE peaks at about 24-fold at 24 h (0.25 Gy), when WWOX is back to about 1. At 5 Gy WWOX rises without an early PARTICLE rise.
- PARTICLE overexpression raised and knockdown lowered the viable fraction (about 92% and 81% against about 88%). WWOX was not perturbed, so no WWOX link is shown.
- Mouse Wwox has 10 predicted sites (Table S3). No held sentence depends on this.
- The ERK 1/2 network placement of WWOX is a pathway-software output, not a measurement.
- Table S2 labels a site at 78,832,453 as intron 5, although the coordinate falls in the intron 8 span by the held exon positions (my inference).
- research/discovery_ledger_current.md:1449 (a predicted triplex axis with LINC01137, unrelated) and DL-BIO-006 at line 417 (KIRKOS, a different O'Leary paper, PMID 29108237) would read the same.

## (4) Searches run

**Files:** registries/claim_registry_current.md, registries/working_model_current.md, disease_model.md, research/discovery_ledger_current.md, research/therapeutic_hypotheses_ledger_current.md, the JSON in cards/ and cards_early/, research_portfolio.tsv, open_questions_map.tsv and the comparators TSVs. cards_early_it13_p22_20261031/ has no top-level JSON; I searched its regenerated/ JSON for the main terms. Every search excluded lines mentioning the barred PMID, and I never searched the repository recursively. Not every term below was run over every file: some follow-up terms covered only the five large files.

- **Record 3 terms:** rs3764340, rs12918952, rs383362, 29662317, meta-analysis, P282A, Pro282, polymorphism, cancer risk, susceptib, rs followed by 5+ digits, GWAS, exon 8, tumour risk / rischio, osteosarcoma, carrier or heterozygote or germline with cancer (English and Italian), common variant / SNP comuni; cancer / cancro / tumour / neoplas / oncolog in the working model and disease model.
- **Record 4 terms:** 28769061, PARTICLE, PARTICL-, triplex, triple helix, lncRNA, long non-coding, MAT2A, irradiat, radiation, U2OS, MDA-MB, intron 8, intron 5, antisense, non-coding / noncoding / non codificante, WWOX transcri, WWOX mRNA, ERK / MAPK, KIRKOS, 29108237, inducib, genotoxic, DNA damage, stress response, miR-153 / lever / repressor, upregulation of WWOX, damage-response phrases, transcriptional regulation.

## (5) What I read, did not read, and failures

- **Record 3:** the full text including all tables; Figures 1-4 (all panel images) and supplementary Figure S1 (s1.jpg). I did not open the .gif thumbnails or the .tif duplicate.
- **Record 4:** the full text; main Figures 1-5; MOESM1.txt in full; MOESM1 PDF pages 6-7 (Figs S1, S2).
- **Record 4 not read:**
  - The images of Figs S3-S5 (pages 8-10); I read their legends only.
  - The .gif thumbnails and the .doc.
  - MOESM2: I did not read it. I only counted matching lines for ten gene names (WWOX 2; GSK3B, GRIN2B, MBP and OLIG2 1 each; the other five 0). A held sentence that depends on a gene's presence in that list would have been missed.
- **Reference lists** were not in the supplied texts.
- **Failures:**
  - The safety-classifier stop described above.
  - Two shell calls arrived cut off and failed without running; I reran shorter versions.
  - A few regex searches exceeded the grep engine's limits; I redid them in Python.
- I wrote no file, did not create the scratch directory, and used no network. The worktree status is clean.

