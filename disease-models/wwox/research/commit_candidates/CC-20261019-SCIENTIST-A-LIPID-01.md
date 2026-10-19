# CC-20261019-SCIENTIST-A-LIPID-01 — human-genetics lipid sources of group G1

`context_policy: QUESTION_DRIVEN` (the selection file's lipid questions were held; no prior dossier). **Author:** ACTOR_ID `scientist-a`, metabolic batch G1, 2026-10-19, task `METAB-G1-A-20261019`.
**Status:** `PROPOSED — NOT PROPAGATED`. **Change class: MINOR** (identity records and one registry-note correction; no baseline claim is reversed). `target_wm_version`: next MINOR after the integrator's current value; no working-model line is edited here.
**Nothing here is medical advice.** PAPER, LIT and CORPUS-STUB numbers are provisional and are renumbered by the integrator from `registry_records.py catalog`.

## 1 · Landings and notes, per source (this file grows by section as the lot proceeds)

| # | Source | Receipt (staged) | Landing proposed |
|---|---|---|---|
| 1 | PMID 20942981 (Saez 2010, BMC Med Genet, 801 Spanish adults, WWOX region vs HDL-C / TG) | `FTR-20261019-20942981-01` | Promote `CORPUS P288` / `LIT-0288` from "screened — corpus placeholder" to a full `PAPER` record, depth `complete_fulltext_read`, transferability T3, relevance LOW |

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
