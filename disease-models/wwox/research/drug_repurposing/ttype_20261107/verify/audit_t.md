# Blind verification audit, Package T (T-type thread in WWOX)

Verifier: independent blind verifier, 2026-11-07. Blind: nothing under `ttype_20261107/` other than this file was opened, and
the IT28 P9 compare README was not opened. Input: the items file only. Scratch files are in the session scratchpad
(`.../scratchpad/t_verify/w/`).

Sources reached: PMID 32000863 held full text (`PMID32000863_Cheng2020_PMC_r2.xml`) and Fig 7 images (full figure, panel b and
panel d crops, each viewed; the panel b bracket region enlarged to read the brackets); PubMed tool abstracts (42276303, 30189284,
22344687, 25099734, 26331302, 19666840, 37583441, 41510857); Europe PMC fullTextXML for 30189284 (PMC6200019) and 38605177
(PMC11143251); NCBI efetch PMC XML for 41489546 (PMC13080778; Europe PMC fullTextXML for it returned HTTP 500, so efetch was
used; the record is flagged not open access in Europe PMC, the efetch text was delivered); PubChem PUG REST; ChEMBL REST.
No access challenge was met. 42276303 is not open access and not in PMC (Europe PMC: isOpenAccess N, inEPMC N, inPMC N), so
the full text was not attempted; no publisher site was tried.

Depth labels: FT = full text read at the cited passage; FIG = figure image read; ABS = abstract only; DB = open database record.

## 1. Evidence rows

Verdicts: SUPPORTED, OVERSHOOT, UNDERSHOOT, NOT_IN_SOURCE, UNVERIFIABLE.

| id | verdict | what I checked | depth | reason |
|---|---|---|---|---|
| E01 | SUPPORTED | Results text of 32000863 and Fig 7b | FT + FIG | Quote verbatim. Ethosuximide arm significant in the null (*** bracket) and n.s. in +/+ and +/-; n per arm 6/6 (control 4) read from the figure. The Methods give one PTZ dose, 30 mg/kg, for all genotypes: "low dose" in the text is the authors' description of the response in +/+ and +/-, not a separate lower-dose arm. Age: abstract says "preweaning mice"; no test age given, as stated. |
| E02 | SUPPORTED | Methods "Induction of seizure" | FT | Quote verbatim: "Ethosuximide (i.p., 150 mg/kg), a T-type Ca2+ channel blocker that has anticonvulsant activity (Luszczki et al., 2005), was injected into mice 45 min before PTZ-induced clonic seizures." The T-type attribution is by citation only. The cited reference (reference list) is an isobolographic study of vigabatrin with conventional antiepileptics in PTZ seizures, so it supports "anticonvulsant in PTZ mice", not channel measurement. One injection is described (lithium is described as three). |
| E03 | SUPPORTED | Methods "Statistical analysis" | FT | Quote verbatim. No post hoc test is named although the figure prints pairwise brackets; no drug-by-genotype term; unit not stated. |
| E04 | SUPPORTED | Discussion; Fig 7d; Methods | FT + FIG | Quote verbatim ("...its efficacy is better than the commonly used anticonvulsant drug ethosuximide"). **** printed in all three genotype panels of 7d. Lithium "three times within 1 h", ethosuximide once. No head-to-head arm (my reading of 7b/7d: no panel holds both drugs). |
| E05 | SUPPORTED | Results text | FT + FIG | Quote verbatim. Fig 7d null: PTZ N=6, PTZ+LiCl N=7. |
| E06 | SUPPORTED (declared sample) | Results text | FT | Quote verbatim ("...commonly observed after postnatal day 12"); the text also states enhanced pilocarpine and PTZ susceptibility. |
| E07 | SUPPORTED | Fig 7 legend; panel 7d | FT + FIG | Legend verbatim "n.s., non-significant. ***P < 0.001"; no **** definition; panel 7d prints **** in all three. |
| E08 | SUPPORTED at abstract level | PubMed abstract | ABS | Quote verbatim. The abstract says OD/R raised firing without naming the preparation for that experiment, and "the same effect was observed in primary cortical neurons" is ambiguous about which effect (promoter activity or expression). Neither changes the row. |
| E09 | SUPPORTED at abstract level | PubMed abstract | ABS | Quote verbatim. |
| E10 | UNDERSHOOT (minor, wording only) | PubMed abstract | ABS | Quote verbatim, "putative" and the title "associated with" are right. But the limit text "wording bounds the claim to association" omits the abstract's closing sentence: "reveal a conserved hypoxia-responsive HIF1α-CaV3.2 pathway that promotes neuronal excitability across experimental models". The abstract names no CaV3.2 perturbation, so the claim is not data-backed, but the authors' own summary is causal and will be quoted that way. The chain status in L5 (not established) is unaffected. |
| E11 | SUPPORTED (declared sample) | PubMed abstract | ABS | Quote verbatim. |
| E12 | OVERSHOOT (minor) | Abstract and Results 3.3 of 30189284 | FT | Quote verbatim (abstract). The finding says "the only T-type channel ortholog": the paper never says "only" (it says "the worm cca-1 ortholog", "the T-type calcium channel-encoding cca-1 orthologue"). Drop "only" or source it separately. The finding also omits the regime: one saturating ethosuximide concentration (4 mg/ml, 2 h pre-incubation, PTZ 7 mg/ml for 15 min, unc-49(e407);cca-1(ad1650), three independent double-mutant lines, n = 13-15 per strain per condition, Kruskal-Wallis with Dunn's; "no difference" is p > 0.05, not an equivalence test). |
| E13 | SUPPORTED | Results 3.3 | FT | Quote verbatim; succinimide at 4 mg/ml gave no protection in unc-49 or unc-49;cca-1. |
| E14 | SUPPORTED | Discussion | FT | Quote verbatim; the 440 uM is an extrapolation from earlier accumulation data and a human dose-serum relation, not a measurement; the bath was 4 mg/ml, about 28 mM by my arithmetic (MW 141.2), not stated in the paper. |
| E15 | SUPPORTED | Discussion | FT | Quote verbatim, in the unc-43 (CAMKII) paragraph. |
| E16 | SUPPORTED | PubMed abstract | ABS | Quote verbatim. |
| E17 | SUPPORTED | PubMed abstract | ABS | Quote verbatim; no isoform values in the abstract. |
| E18 | SUPPORTED (quote hygiene note) | Results 1 and Table 2; Methods | FT | Source reads "Z944 inhibited CaV3.2 Ca2+ currents (ICa; IC50~ 265 nM, Fig.1A-C, Table 2)"; the stored quote has lost sub/superscripts and is not verbatim as stored. Table 2: Z944 Cav3.2 IC50 0.26 +/- 0.04 uM, Hill 0.82; ML218 0.0237 +/- 0.0025 uM. Human Cav3.2 (AF051946) in HEK293T, whole-cell, room temperature; external 10 or 20 mM CaCl2 (the paper does not say which for Cav3.2). |
| E19 | SUPPORTED (soft figure) | Results 2; Table 2 | FT | Quote supported. Table 2 gives Cav1.4 IC50 31.5 +/- 21 uM with Hill slope 0.22 +/- 0.04: a shallow, poorly constrained fit, so "about 100-fold" is a loose window. ML218: Cav1.4 2.1 +/- 0.51 uM, Cav1.2 37 +/- 6.5 uM. |
| E20 | SUPPORTED | Discussion | FT | Quote verbatim. Context: the caution is framed where Cav3 channels are upregulated in retina or pineal and the blockers could mislead; the same paragraph notes another group found Z944 (5 uM) increased Cav1.4 current in mouse cones. |
| E21 | SUPPORTED | Introduction | FT | Quote verbatim, cites Tringham 2012. PubChem IUPAC name is a piperidin-4-yl compound, so "piperazine" in the paper is loose, as the item says. |
| E22 | SUPPORTED | Introduction of 38605177 | FT | Quote verbatim; the next clause says Cav3.2 offers an opportunity to develop Cav3.2-selective molecules. Class statement, not a measurement. |
| E23 | SUPPORTED (text level) | Results | FT | Quote verbatim. The values are in Supplementary Table S4, which I did not read either. |
| E24 | SUPPORTED | Results | FT | Quote verbatim. "Share a chemotype" is a reasonable but loose gloss: PubChem shows ML218 carries a 3-azabicyclo[3.1.0]hexane amine, TTA-P2 a 4-fluoropiperidine, Z944 a piperidine; all three share the halogenated benzamide-methyl-amine pattern. |
| E25 | SUPPORTED | PubMed abstract | ABS | The quote is a background sentence of the abstract; the finding (promoter response for alpha1H not alpha1G; HRE at -1173; EMSA) is supported by other sentences of the abstract. Rat PASMC and PC12. |
| E26 | SUPPORTED | PubMed abstract | ABS | Quote verbatim; "required HIF-1alpha stabilization" and Ni2+ 50 uM are in the abstract. |
| E27 | SUPPORTED | PubMed abstract | ABS | Quote verbatim. The HIF-1alpha involvement rests on the CoCl2 mimic ("indicating ... HIF-1alpha is involved"), an author inference. |
| E28 | SUPPORTED | PubMed abstract | ABS | Quote verbatim. The abstract's own sentence about IGF-1 inhibition raising Cav3.2 is internally odd (likely a typo for activation); not used. |
| E29 | SUPPORTED | PubMed abstract of 41510857 | ABS | Quote verbatim. The list also contains an unspecified "CACNA1"; a gene list in a diagnostic cohort, no mechanism. |

Counts: 27 SUPPORTED (including 6 with a note), 1 OVERSHOOT (E12), 1 UNDERSHOOT (E10), 0 NOT_IN_SOURCE, 0 UNVERIFIABLE.
Decisive rows (E01, E02, E03, E04, E07, E08, E09, E10, E12, E15, E17, E18, E20, E21, E22): 13 SUPPORTED, E10 UNDERSHOOT, E12 OVERSHOOT.
Declared sample (E05, E06, E11): all SUPPORTED, so the sample does not extend the check; I checked E13, E14, E16, E19, E23-E28 as well.

## 2. Figure 7 (my own reading of the images)

General: the figure image shows, in panel b and d, brackets drawn as an outer bracket (control to the last arm) labelled ***, plus two inner brackets. The producer's reading lists only the inner ones. In 7b the outer *** appears in all three genotypes, including +/+ and +/-, where the inner PTZ v PTZ+ETS bracket is n.s. The outer bracket is either a three-group omnibus ANOVA or control v PTZ+ETS; the figure does not say. Either way, in the null the ethosuximide arm is not shown to reach control level.

| panel | my reading | agree with items.md? |
|---|---|---|
| 7a | +/+ (pilocarpine N=6, control 5) and +/- (N=8, control 5) rise to about stage 2 within 10 min and sit at about 2 to 2.5. Null (N=4, control 4): about 2 by 5 min, then 3 to 4, ending near 4, with large SEM bars, discrete steps (small n). No statistics printed, no drug arm. | Agree. |
| 7b +/+ | Control N=4, PTZ N=20, PTZ+ETS N=16. PTZ-alone peaks about 1.3 near min 15, decays to about 0.3. ETS arm is lower than PTZ by about 0.3 to 0.5 stage at min 5 to 17 and higher by about 0.3 to 0.5 at min 27 to 40: a crossover, not an exact overlap. Inner brackets: *** control v PTZ, n.s. PTZ v PTZ+ETS. Outer ***. | Agree on the reading and the floor (the whole response is about one stage, so a one-stage reduction cannot occur). The "overlaps" wording is simplified; the crossover should be stated. |
| 7b +/- | Control N=5, PTZ N=18, PTZ+ETS N=12. Both curves about 0.5 to 1 and interleaved; outer *** and inner *** / n.s. as above. | Agree. |
| 7b -/- | Control N=4, PTZ N=6, PTZ+ETS N=6. PTZ-alone about 1.5 to 2.5 up to min 12, about 1 to 1.5 for min 15 to 35, then rises to about 2.3 to 2.8 at min 40 to 52 and sits flat at 2.0 for min 53 to 60 (identical SEM bars: the tail looks carried forward or based on very few values; the cause is not stated). ETS arm about 1 to 2 early (peak about 1.8 near min 10 to 13), about 1.2 to 1.5 mid, about 0.5 to 1 after min 38, with a flat 0.5 segment at min 38 to 45. Early phase not different; the separation is in the second half and rests on the PTZ-alone late rise. Inner brackets *** and ***; outer ***. | Agree. SEM bars overlap for most minutes; with six animals per arm, a significant *** implies the test used pooled time points or the area; the unit is not stated (see below). |
| 7c | Blot lanes: cerebellum, hippocampus, cortex, each +/+, +/-, -/-. pGSK3B (Ser9) ratio to actin, per region as +/+, +/-, -/-: cerebellum 2.7, 3.1, 1.3; hippocampus 3.6, 3.5, 2.0; cortex 3.9, 3.8, 2.5; total GSK3B: cerebellum 2.2, 2.4, 2.4; hippocampus 2.3, 2.4, 2.6; cortex 2.2, 2.4, 2.6. Wwox band absent in -/-, reduced in +/-. | Agree on all values. Two additions: the ratios are to actin, not to total GSK3B (total/actin is flat, so the dephosphorylation reading holds); the legend says postnatal day 20 but the Methods Western paragraph says tissues "at postnatal day 14", an internal discrepancy in the paper that the producer did not list. |
| 7d +/+ | PTZ N=12, PTZ+LiCl N=8, no control arm. PTZ peaks about 1.2 in the first minute, about 0.3 by min 5 and onward; LiCl about 0.2 and about 0 throughout. **** printed. | Agree. A difference of about 0.1 to 0.3 stage confined to the first minutes with overlapping SEM bars, printed as ****, is hard to reconcile with an animal-level test with 12 and 8 animals; this is my inference that the unit may be time points (not stated in the paper). |
| 7d +/- | PTZ N=12, PTZ+LiCl N=12. PTZ about 0.5 to 1.1 up to min 13, lower later; LiCl about 0.1 to 0.4. **** printed. | Agree; same inference. |
| 7d -/- | PTZ N=6, PTZ+LiCl N=7. PTZ peaks about 3.5 at min 5 to 6, then about 1 to 1.8, small bump near min 50 to 55, about 0.3 to 0.5 in the last 3 min. LiCl peaks about 1.3 at min 5 to 8, near 0 after about min 20, and is flat 0 (no SEM) for most of the second half. **** printed. | Agree. Added: LiCl hits a floor (0) for most of the hour. The two null PTZ-alone curves differ (7b peak about 2.5 at min 8 to 11 and late rise; 7d peak about 3.5 at min 5 to 6 and no late rise); the 7b ETS arm after min 38 (about 0.5 to 1) is not far from the 7d PTZ-alone arm (about 1 to 1.7), so the ETS result depends on which PTZ-alone cohort is the comparator. |

## 3. Probes

| id | judgement |
|---|---|
| P1 | Identity confirmed (see H1). Measured values confirmed against 41489546: Cav3.2 IC50 0.26 +/- 0.04 uM (Hill 0.82), Cav1.4 31.5 +/- 21 uM (Hill 0.22), human clones in HEK293T, whole-cell, room temperature, external 10 or 20 mM CaCl2, internal NMDG/EGTA/Mg-ATP. Cav1.2 and Cav2.2 about 70 to 100-fold are cited from Tringham 2012 in the paper (not measured there). No class-to-isoform transfer: the paper measured Cav3.2 only; E22 and E21 stand. The statement "Z944 reaches Cav3.1" rests on the F956L mutant text in 38605177 (and the cryo-EM Z944-Cav3.1 structure it refers to). Exposure "not obtained" is accurate for the sources read. |
| P2 | Identity: PubChem CID 3291, ethosuximide, C7H11NO2, 3-ethyl-3-methylpyrrolidine-2,5-dione (I checked this; the probe said not re-resolved). Millimolar potency and ChEMBL values are IT28 reuse and could not be checked blind: UNVERIFIABLE here. Worm points confirmed (see H4). |
| P3 | Identity: PubChem CID 45115620 (3,5-dichloro-N-[[(1R,5S)-3-(3,3-dimethylbutyl)-3-azabicyclo[3.1.0]hexan-6-yl]methyl]benzamide), C19H26Cl2N2O. Values confirmed: Cav3.2 0.0237 uM (about 11-fold more potent than Z944), Cav1.4 2.1 +/- 0.51 uM, Cav1.2 37 +/- 6.5 uM; the "about 80-fold window" is derived (Table 2 gives about 89-fold). Monkey result stated in the introduction. |
| P4 | PubChem CID 24893979 (TTA-P2), 4-fluoropiperidine, C21H29Cl2FN2O2. Potency values are in Supplementary tables not read, as the probe says: remains open. |
| P5 | Design statement; no source to check. Not a measurement. |

No class-to-isoform transfer found in P1-P4. Watch item: the family statement "T-type blockers" in E22 is about the class, and E20 and E19 show non-Cav3 effects at micromolar levels.

## 4. Chain judgements

| id | judgement |
|---|---|
| L1 | Agree. Note the murine arm is HIF1A transcript, a weak activity marker; the human arm is protein. |
| L2 | Agree (gain of function; no loss of function in the abstract). |
| L3 | Agree: undetermined for neurons. The outside evidence (E25 HRE mutation and EMSA, E28 EMSA) is in rat PASMC/PC12 and spinal cord. |
| L4 | Label under-states: the abstract reports HIF1A overexpression raising network activity, which is an intervention, not only co-occurrence. What is not established is that CaV3.2 mediates it (L5), and HIF overexpression has many other targets. The label should separate "HIF gain of function raises firing in cultured neurons: supported at abstract level" from "through CaV3.2: not established". |
| L5 | Agree: NOT ESTABLISHED at abstract level. |
| L6 | Agree. |
| L7 | Partly UNVERIFIABLE (IT10 reuse, not readable blind). The cited evidence id E08 contains nothing on activity driving HIF. Also, "direction is not fixed by co-occurrence" is weaker than the abstract allows for the overexpression arm, where HIF is manipulated first; the alternative stays open for the hypoxia protocols and for epileptic tissue, not for the overexpression result. |
| L8 | Mostly right but the count is off: of E25-E28, Cav3.2 up with HIF involvement is three reports (E25, E26, E28), not four; E27 is Cav3.1 down (CoCl2-based HIF inference); E25 shows alpha1G promoter not responsive. Four only if the Bonn paper (E08) is added, which is not in L8's evidence ids. "Mixed" and "isoform not interchangeable" stand. Also E26 (Cav3.1 not altered) and E27 (Cav3.1 reduced) disagree within neonatal rat ventricular myocytes, which supports "protocol-dependent". |
| L9 | UNVERIFIABLE (repository-held, blind). |
| L10 | Agree for the PubMed side: my searches (section 5) give one hit, 41510857, a gene list. The IT28 clause on P17 transcripts is UNVERIFIABLE blind. |
| L11 | Agree: no link; ethosuximide is the only compound in Fig 7b, and the worm datum is an alternative, not proof of a non-T-type action in the mouse. |

## 5. H1-H4

**H1 (identity): CONFIRMED in two databases.** PubChem: name lookups for Z944, ulixacaltamide and PRAX-944 each return CID 44540045 only; formula C19H27ClFN3O2, InChIKey JOCLITFYIMJMNK-UHFFFAOYSA-N, IUPAC name N-[[1-[2-(tert-butylamino)-2-oxoethyl]piperidin-4-yl]methyl]-3-chloro-5-fluorobenzamide; synonyms include Z944, Ulixacaltamide, PRAX944, PRAX-944, CHEMBL3934636, QT2PJH89C3. ChEMBL CHEMBL3934636 (read by ID): pref_name ULIXACALTAMIDE, same InChIKey, same formula, synonyms Z944, Z-944, PRAX-944, PRAX944, Ulixacaltamide, NP-169944; max_phase 1.0 (read, not used). Not rerun: the producer's ChEMBL name-search route (I used the record by ID). The paper's "piperazine" is wrong; the structure is a piperidine.

**H2 (absence): holds for title/abstract/MeSH indexes; not shown for full text.** Route 1, PubMed tool (queries as typed):
1. `WWOX AND (CACNA1G OR CACNA1H OR CACNA1I)` -> 1 hit (41510857)
2. `WWOX AND CACNA1H` -> 1 hit (same)
3. `WWOX AND "T-type calcium channel"` -> 0
4. `(WWOX OR WOX1 OR "WW domain-containing oxidoreductase") AND ("Calcium Channels, T-Type"[MeSH Terms] OR "T-type" OR Cav3.1 OR Cav3.2 OR Cav3.3 OR Cacna1g OR Cacna1h OR Cacna1i OR "alpha1H")` -> 1 hit (same)
5. `(WWOX OR WOX1) AND "calcium channel"` -> 0
6. `(WWOX OR WOX1) AND (ethosuximide OR Z944 OR mibefradil OR "T-type")` -> 0
7. `(WWOX OR Wwox) AND (calcium[Title] OR "voltage-gated"[Title] OR "ion channel"[Title])` -> 1 hit (34214506, a diabetic retinopathy photoreceptor paper, not a WWOX-channel link; I read the title only)
What the PubMed tool does with OR and parentheses: it keeps the grouping. The returned `query_translation` shows `(A OR A' ) AND (B OR C OR D ...)` intact, each term wrapped as `"term"[All Fields]` with automatic term mapping (WWOX -> "wwox protein human"[Supplementary Concept]; Cav3.2 -> "cav3 2" plus the cacna1h supplementary concept). The OR query returned the same single hit as the single-gene query, so OR is not dropped or truncated. The index is title, abstract and MeSH only: query 6 returned 0 although Cheng 2020 (32000863) uses ethosuximide in Wwox null mice, because its abstract does not name the drug. So absence in this route does not cover full-text mentions.
Route 2, Europe PMC REST (full-text index for open-access papers):
- `WWOX AND (CACNA1G OR CACNA1H OR CACNA1I)` and the Cav3.x variant: hitCount 71 (full-text co-mentions: diagnostic panels, methylation, reviews)
- `(WWOX OR WOX1) AND ("T-type calcium" OR "T-type Ca" OR "T-type channel" OR "T-type channels")`: 4
- `(BODY:"WWOX" AND BODY:"T-type")`: 12
- `(TITLE_ABS:WWOX OR TITLE_ABS:Wwox OR TITLE_ABS:WOX1) AND (TITLE_ABS:"T-type" OR TITLE_ABS:Cacna1h OR TITLE_ABS:Cav3 OR TITLE_ABS:"calcium channel")`: 1 (41510857, same hit as PubMed)
Screen done: I fetched open-access full texts of 41135097, 32899411, 41898755, 42654085 and 41982212 and tested for a T-type or Cacna term within 500 characters of any WWOX mention: none (co-mention only); 35951482 returned HTTP 500 and was not read. The other roughly 65 of the 71 hits were not read.
Conclusion: no WWOX-to-T-type link in title/abstract in two routes; full-text absence is not established. The 1 PubMed hit is a gene list (E29).

**H3 (HIF paper): CONFIRMED at abstract depth.** The abstract shows: OD/R persistent increase in firing; murine slice hypoxia raising HIF1α and Cacna1h transcripts; human slice hypoxia raising protein; HIF1α overexpression raising Cacna1h in lines and primary cortical neurons; NS20Y promoter reporter increase; MEA network activity increase on overexpression. It names no CACNA1H knockdown, knockout, blocker, current recording or rescue. The authors do close with "reveal a conserved hypoxia-responsive HIF1α-CaV3.2 pathway that promotes neuronal excitability across experimental models" (see E10). Full text not reachable (not open access); an absence from the abstract is not an absence from the paper.

**H4 (worm datum): CONFIRMED, with the regime added.** Endpoint: proportion of worms with head-bobbing convulsions and mean head bobs per 30 s. Strain: unc-49(e407) (GABA-A subunit null) crossed to cca-1(ad1650) (2.5 kb deletion, null; single cca-1 mutant did not convulse on PTZ), three independently derived double lines, genetically verified. Regime: ethosuximide or succinimide 4 mg/ml (about 28 mM bath), 2 h pre-incubation, then PTZ 7 mg/ml for 15 min; young adults; n 13-15 per strain per condition pooled over three experiments; Kruskal-Wallis with Dunn's; ethosuximide differed from succinimide (p < 0.05) in every line and did not differ between lines (p > 0.05). The paper's own dose-response (in unc-49 only) reached complete abolition at 4 mg/ml, so the cca-1 test ran at a saturating dose, where a partial contribution of CCA-1 to a complete effect could be missed; no dose-response in the double mutant. The authors estimate about 440 uM internally by extrapolation. Authors: "we have not yet identified ethosuximide's molecular target"; ethosuximide also failed to rescue unc-43 null convulsions. What it does not show for the mouse: the worm PTZ model lacks the GABA-A subunit that PTZ is classically said to act on; there is no sodium channel in the worm genome; mouse Cav3 isoforms are not tested; it says nothing on whether ethosuximide acts on Cav3 in the Wwox null, only that a T-type-independent route to protection can exist.

## 6. Omitted decisive points (producer-side wording to repair)

1. Fig 7b/7d brackets: the outer *** is not described; in the null, ethosuximide's arm still differs from control (or the omnibus is significant).
2. Fig 7c: legend says P20, the Methods Western paragraph says P14.
3. E10: the abstract's closing causal sentence ("promotes neuronal excitability").
4. E12: "only" is not in the source; saturating single-dose regime; bath about 28 mM vs estimated internal 440 uM.
5. E19/P1: the Cav1.4 IC50 is 31.5 +/- 21 uM with Hill 0.22; Z944 raised Cav1.4 current in mouse cones in another report (cited in the paper).
6. L4 label under-states HIF gain of function; L8 counts three reports, not four, for Cav3.2 up and HIF-dependent.
7. Statistical unit in Cheng 2020: ****/*** with near-overlapping curves and 6-12 animals suggests time points or area as units (my inference; unstated). The ethosuximide contrast also depends on the PTZ-alone late rise, absent in the other null cohort.
8. H2: the PubMed route cannot see the full-text use of ethosuximide that already exists in the WWOX literature, so "absent in PubMed" is an index statement.

## 7. Not checked

- 42276303 full text (not open access; no publisher access tried). Abstract only for E08-E11, E25-E29 and L1-L6.
- Tringham 2012 full text and the Z944 Cav3.1/Cav3.3 values; 38605177 supplementary tables (S4); Cav3.2 vs Cav3.1 vs Cav3.3 isoform selectivity for Z944, ML218, TTA-P2: not obtained.
- Ethosuximide millimolar T-current potency and ChEMBL values (P2), IT28/IT10 reuse items (P2, P5, L7, L9, L10 second clause): blind, repository not read.
- The producer's ChEMBL name-search call and its queries.tsv Q06 (blind; I read the ChEMBL record by identifier instead).
- Roughly 65 Europe PMC full-text hits for WWOX plus Cacna terms; 35951482; non-open-access full text of any paper in the 71.
- Raw data behind Fig 7 (none in the supplement that I opened; the supplementary PDF was not opened); the statistical unit; the "carried forward" tails.
- Whether a mouse pup brain exposure for ethosuximide at 150 mg/kg or for Z944 exists: not searched.
- The 6 other Fig 7 images in the Fig directory (Figs 1-6): not opened.
