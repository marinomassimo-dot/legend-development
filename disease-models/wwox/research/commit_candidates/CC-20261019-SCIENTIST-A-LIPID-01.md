# CC-20261019-SCIENTIST-A-LIPID-01 — human-genetics lipid sources of group G1

`context_policy: QUESTION_DRIVEN` (the selection file's lipid questions were held; no prior dossier). **Author:** ACTOR_ID `scientist-a`, metabolic batch G1, 2026-10-19, task `METAB-G1-A-20261019`.
**Status:** `PROPOSED — NOT PROPAGATED`. **Change class: MINOR** (identity records and one registry-note correction; no baseline claim is reversed). `target_wm_version`: next MINOR after the integrator's current value; no working-model line is edited here.
**Nothing here is medical advice.** PAPER, LIT and CORPUS-STUB numbers are provisional and are renumbered by the integrator from `registry_records.py catalog`.

## 1 · Landings and notes, per source (this file grows by section as the lot proceeds)

| # | Source | Receipt (staged) | Landing proposed |
|---|---|---|---|
| 1 | PMID 20942981 (Saez 2010, BMC Med Genet, 801 Spanish adults, WWOX region vs HDL-C / TG) | `FTR-20261019-20942981-01` | Promote `CORPUS P288` / `LIT-0288` from "screened — corpus placeholder" to a full `PAPER` record, depth `complete_fulltext_read`, transferability T3, relevance LOW |
| 2 | PMID 21444760 (Leduc 2011, J Lipid Res, mouse QTL map and human HDL GWA) | `FTR-20261019-21444760-01` | New `PAPER` record (none exists; queue entry `FT-019` only), depth `complete_fulltext_read`, T3, relevance LOW; close `FT-019` |
| 3 | PMID 35559044 (Liu 2022, Front Genet, EHBP1/TUBB/WWOX SNPs, CAD and ischemic stroke) | `FTR-20261019-35559044-01` | Promote `CORPUS-STUB-157` / `LIT-0174` to a full `PAPER` record; correct the stub title (it reads "... and Hypertension"; the article says "... and Ischemic Stroke") |

## 2 · Required content of the PAPER record for source 1

One sentence of what it measures: a common-variant association scan of the WWOX region in 801 unrelated Spanish adults (1045 SNPs, 894 imputed, no multiple-testing correction), with the strongest triglyceride signal at the 5' end (rs11645006, P 0.0002, imputed) and the strongest HDL signal in intron 8 (rs2047927, P 0.003); the originally reported HDL SNP was not replicated (P 0.299).

Note text to carry (the negative, in the style of PAPER 156 and CORPUS-STUB-109):
🔴 **DO_NOT_CITE as support for a WWOX dose effect or a heterozygous-loss lipid phenotype.** Common non-coding variants in one population, no loss-of-function allele, no carrier phenotype, no expression assay; no multiple-comparison correction (smallest P in Tables S2-S4 is 2.4e-4, against a 1045-test Bonferroni line near 4.8e-5); the headline SNPs are imputed (rs11645006 Rsq 0.8756); no intron-8 region is associated with HDL in the haplotype test; the lead HDL SNPs carry opposite signs in different regions; Table S2 betas (2.67 and 2.81) differ from the body text (0.96 and 1.03) for rs4888865 and rs4145518 with no unit stated. Nominal-hit counts (script-derived on the strings surface of Tables S2-S4, not a locator): 39, 46 and 46 of 1045 SNPs below P 0.05 for HDL, TG and TG/HDL, i.e. no excess over the 5 percent chance expectation (LD makes this descriptive, not a test).

## 3 · What must NOT be written

- No statement that WWOX heterozygous loss lowers HDL-C or raises triglycerides.
- No claim link; no change to CLAIM 045 or to the metabolic branch of the working model.
- No individual-level content (none exists in the source).

## 4 · Known registry statements to re-check at integration

`CORPUS P288` and `LIT-0288` say "Claim links: none — triage only" and "Primary pathway: P5" — consistent; only status and depth change. `PAPER 084` (Lee 2008) could carry one added sentence: the Saez 2010 attempt in a Spanish sample did not replicate the lead variant rs2548861 (P 0.299, imputed) and reports other intron-8 and 5' SNPs.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The authors applied no multiple-comparison correction | We have not applied multiple comparison correction because we consider it over-conservative for the replication of a previously described gene specially given that most genotypes analysed in this report are derived from a small number of observed genotypes; a p value under 0.05 is interpreted as significant. | Methods, Statistical analysis, `files/fulltext/PMID20942981_Saez2010_PMC.xml`
2. The lead HDL variant of the earlier study was not replicated | In our study, we failed to replicate the association of the rs2548861 with HDL. | Discussion, paragraph 5, same artefact
3. No intron-8 region is associated with HDL in the haplotype analysis | Moreover, none of the intron 8 regions are associated with HDL in the haplotypic analysis, although region 2 shows a trend for association (p = 0.07). | Discussion, paragraph 1, same artefact
4. The top triglyceride SNP is an imputed genotype | rs11645006 76710658 G A 0.33 -13.81 -21.16 -6.47 2.4E-04 1.8E-04 Imputed | Additional file 9 (Table S3), `files/fulltext/PMID20942981_Saez2010_supplement/1471-2350-11-148-S9.strings.txt`
5. Table S2 beta differs from the body text for rs4888865 | rs4888865 77434919 C A 0.18 2.67 0.79 4.55 0.006 0.006 Imputed | Additional file 8 (Table S2), `.../1471-2350-11-148-S8.strings.txt` (body text, Results HDL region 2: beta 0.96)

## 5 · Source 2 (PMID 21444760, Leduc 2011): record content

What it measures: re-analysis of a published human HDL GWA meta-analysis against the mouse HDL QTL map; for Wwox, a B6xCAST QTL overlap, one predicted-functional missense change (V186M, SIFT only, not conserved), no liver expression difference by real-time PCR, wild-type inbred strains, no knockout, no brain or myelin data.

Note text to carry:
🔴 **No WWOX loss-of-function evidence and no brain or myelin evidence.** The queue rationale ("via brain cholesterol, for the myelin axis") is not in the paper. The Wwox conclusion rests on V186M "may affect" function; V186M does not segregate in the second cross; the B6xCAST interval holds 184 candidate genes after haplotype filtering. Supplementary Table S10 prints one Wwox probe set at +2.14 and +2.28 fold (P below 0.001, both sexes) between the high- and low-HDL strains while the Results report no expression difference and the footnote explains only a different probe set; the Discussion nevertheless says the mouse "confirms" cis-regulation of WWOX. The Discussion's statement that the Wwox knockout mouse is hypercholesterolemic cites the 2007 deletion paper, which reports serum lipids only as "data not shown" (rendered-page check); the companion paper Saez 2010 describes the same mouse as hypocholesterolemic and hypotriglyceridemic, citing the 2008 paper (not re-verified here).

## 6 · Registry statements to re-check at integration (source 2)

`FT-019` ("abstract read, full text NOT read") becomes closed. `LIT-0402` carries a declared reading debt naming this PMID; the debt is discharged. Any registry sentence that relays "Wwox knockout is hypercholesterolemic" or "hypocholesterolemic" should be traced to its primary source before reuse (two secondary descriptions disagree).

### LOCATOR TRIPLES FOR BLIND AUDIT (source 2)

6. Wwox liver expression did not differ by qPCR | For Wwox, we performed real-time PCR between B6 and CAST on chow in males and females but did not find any difference in expression (P > 0.05) (Table 1). | Results, Galnt2, Wwox, Cdh13, `files/fulltext/PMID21444760_Leduc2011_PMC.html`
7. Wwox conclusion rests on a possible functional change | because V186M may affect the function or structure of WWOX, we think that Wwox is a QTL gene for the B6xCAST cross. | same
8. V186M does not segregate in the second cross | The polymorphism segregated between B6 and CAST but not between B6 and CASA. | same
9. Probe set 1416334_at differs between the strains in both sexes | 1416334_at B6xCAST C M F +2.14 (<0.001) +2.28 (<0.001) 1431960_at B6xCAST C M F +1.38 (0.001) +1.12 (0.261) | Supplementary Table S10, `files/fulltext/PMID21444760_Leduc2011_supplement/supp_M009175_jlr.M009175-1.strings_S4_S10_S12.txt`
10. The Discussion states hypercholesterolemia for the Wwox knockout, citing ref 39 | For instance, the Wwox knockout mouse has previously been shown to exhibit hypercholesterolemia (39); HDL was not measured, but hypercholesterolemia in a chow-fed mouse would indicate increased HDL because 80% to 90% of cholesterol in a chow-fed mouse is HDL. | Discussion, paragraph 3

## 7 · Source 3 (PMID 35559044, Liu 2022): record content

What it measures: two common WWOX SNPs (rs2222896, rs2278075) among six in a hospital-based Han case-control study (622 CAD, 593 stroke, 638 controls). No loss-of-function allele, no expression, no WWOX disease subject.

Note text to carry:
🔴 **DO_NOT_CITE as evidence of a WWOX lipid or vascular dose effect.** (a) Common SNPs only. (b) The one WWOX hit, rs2278075, has a control T frequency of 14.6 percent against 21.2 and 22.9 in the case groups, while the paper's own quoted reference frequency is 22.0: the controls are the outlier. (c) Lipid-by-genotype results (all six SNPs altering nearly every trait in 638 controls; t up to 15.2 for one genotype term on triglyceride; betas outside their own intervals) are not plausible as common-SNP effects. (d) The authors' deposited genotype spreadsheet reproduces Table 2 exactly but its CAD and stroke columns are laid out in a few contiguous blocks in file order, so joint genotypes cannot be relied on for the haplotype and interaction analyses; it carries no covariates. (e) The reference list does not match the in-text citations: a WWOX lipid statement cites a WWOX epileptic-encephalopathy case report; a genome-wide P value cites an epidemiology review; the WWOX HDL paper is cited for alcohol.

## 8 · Registry statements to re-check at integration (source 3)

`CORPUS-STUB-157` title. `CORPUS-STUB-109` (Liu 2021, same group) may share the deposit layout: not checked here. `CORPUS P383` (Johannsen 2018, WWOX SDR missense case report, an unread primary named in the standing brief) is cited by this paper for a statement it does not contain; no change to that record.

### LOCATOR TRIPLES FOR BLIND AUDIT (source 3)

11. The control group's T frequency is below the quoted reference | rs2278075AA 68.3%, AT 19.5%, TT 12.2%, and T 22.0% | Discussion, paragraph 3, `files/fulltext/PMID35559044_Liu2022_PMC.xml` (controls: Table 2, rs2278075, T 186 of 1276 chromosomes)
12. A lipid statement is cited to a WWOX case report | The correlation between the WWOX rs2222896AA genotype and LDL-C was two times that of the rs2222896AG or rs2222896 GG genotypes (Johannsen et al., 2018). | Introduction, paragraph 2
13. Reference 16 is the case report | A Novel Missense Variant in the SDR Domain of the WWOX Gene Leads to Complete Loss of WWOX Protein with Early-Onset Epileptic Encephalopathy and Severe Developmental Delay. | Reference 16
14. A printed beta lies outside its own interval | rs2222896 AA AG −0.647 −11.274 <0.0004 −1.053 −0.741 | Table 4, TG block
15. CAD genotype column layout in the deposit | RUNS CAD rs2278075: 5 runs; A/T x30, T/T x14, A/A x386, T/T x14, A/T x178 | `files/fulltext/PMID35559044_Liu2022_supplement/Table1_aggregate_derivation.txt` (aggregate derivation of the authors' Table1.XLSX)
