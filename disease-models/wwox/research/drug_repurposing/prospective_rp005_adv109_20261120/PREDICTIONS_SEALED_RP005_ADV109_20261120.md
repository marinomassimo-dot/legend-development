# RP-005 / ADV-109: SEALED prediction sets of all arms (IT, 2026-11-20). Not committed until SCI's truth table is on main; its SHA-256 is committed in the scorer sheet. Arm A = baseline as frozen in commit 0270ce710 (primary); A' = the rule-faithful baseline (rule R3 gives the 'not measured / not tested' option for T1-S4 and T2-S3, where the frozen instantiation wrote A and B): reported as a sensitivity.

## Slot-level predictions
| Slot | A baseline (frozen) | A' rule-faithful | B generator | C abstract-only |
|---|---|---|---|---|
| T1-S1 | A | A | A | A |
| T1-S2 | A | A | B | A |
| T1-S3 | B | B | B | B |
| T1-S4 | A | C | C | C |
| T1-S5 | B | B | B | B |
| T1-S6 | A | A | A | A |
| T1-S7 | A | A | A | A |
| T1-S8 | A | A | A | A |
| T1-S9 | A | A | A | A |
| T2-S1 | A | A | A | A |
| T2-S2 | B | B | B | B |
| T2-S3 | B | C | B | C |
| T2-S4 | A | A | A | A |
| T2-S5 | B | B | B | B |
| T2-S6 | A | A | A | A |
| T2-S7 | C | C | C | C |
| T2-S8 | B | B | A | B |
| T2-S9 | A | A | A | A |
| T2-S10 | B | B | B | B |
| T3-S1 | B | B | C | B |
| T3-S2 | B | B | B | B |
| T3-S3 | A | A | A | A |
| T3-S4 | B | B | B | B |
| T3-S5 | B | B | B | B |
| T3-S6 | B | B | B | B |
| T3-S7 | B | B | B | B |
| T3-S8 | A | A | A | A |
| T3-S9 | A | A | A | A |

## Arm B reasons as delivered (three delegates, one per text)

## Arm B, T1 (sonnet, effort high self-reported; tools: Read x3 of the three manifest files; recalls the paper body: partly, faint memory, S1, S3 and S9 close to blind)
| Slot | Option | Reason | Confidence |
|---|---|---|---|
| T1-S1 | A | BATCH10 gives no answer (brain not named in the abstract, full text not read); general knowledge: a mouse tissue-distribution panel usually includes brain with numeric values, lipophilic compound, high fat uptake | low |
| T1-S2 | B | BATCH10 reports eight metabolites without structures; general knowledge: thiazolidinone, LC-MS only, tentative phase I assignments more likely than conjugates | medium |
| T1-S3 | B | BATCH10 gives cell IC50 about 35 to 60 micromolar (MDA-MB-231, MDA-MB-468, P493-6), no DU145 or PC-3 row; literature 20 to 100 micromolar | low |
| T1-S4 | C | general knowledge: a 2009 PK paper of this type usually does not measure protein binding; BATCH10 mentions none | medium |
| T1-S5 | B | BATCH10 gives no age; general knowledge: xenograft studies in SCID or nude mice usually state 6 to 8 weeks | medium |
| T1-S6 | A | BATCH10 gives no vehicle; general knowledge: poorly soluble, typically DMSO stock diluted | medium |
| T1-S7 | A | BATCH10 records no significant tumour inhibition at two doses; implies doses well tolerated; earlier 10058-F4 efficacy report stated no toxicity at 20 and 30 mg/kg | medium |
| T1-S8 | A | BATCH10 lists tissues in the order fat, lung, liver, kidney (may reflect descending concentration); lipophilic compound accumulates in fat | medium |
| T1-S9 | A | BATCH10 gives peak tumour at least tenfold below plasma, no per-line values; similar vascularity, one compound | low |

## Arm B, T2 (sonnet, effort high self-reported; tools: Read x4 = slot table plus the three manifest files; recalls the paper body: no)
| Slot | Option | Reason | Confidence |
|---|---|---|---|
| T2-S1 | A | general knowledge: TTA-P2 usually i.p. in rodents; the manifest gives only the doses, no route (TTYPE comparison) | medium |
| T2-S2 | B | general knowledge: about 30 min before a PTZ challenge; manifest gives no interval | low |
| T2-S3 | B | general knowledge: a drug-alone locomotor control is likely; manifest names no TTA-P2 sedation figure; related TTA-P2 pain work reports no motor effect at effective doses; coin flip against C | low |
| T2-S4 | A | general knowledge: chronic intermittent ethanol vapour with pyrazole is typical; manifest says only 'ethanol-withdrawal plus PTZ model' | medium |
| T2-S5 | B | general knowledge: about 3 to 4 withdrawal cycles; manifest silent | low |
| T2-S6 | A | general knowledge: Racine-type or modified Racine for PTZ | medium |
| T2-S7 | C | manifest (TTYPE comparison section 1; BATCH11 second correction) quotes only '20 and 40 mg/kg protective' and no 10 mg/kg naive arm; points to the lower dose used only in withdrawal | low |
| T2-S8 | A | general knowledge: PTZ 40 mg/kg i.p. sub-lethal or marginal in naive mice, expect vehicle mortality under 25 percent (if zero deaths and the paper states no mortality, D) | low |
| T2-S9 | A | general knowledge: ordinal scores, Kruskal-Wallis or Mann-Whitney | low |
| T2-S10 | B | general knowledge: adult mice 8 to 16 weeks; manifest says only 'mice' | medium |

## Arm B, T3 (sonnet, effort high self-reported; tools: Read x3 = slot table plus the two manifest files; recalls the paper body: partly, recognises it by title, no numbers)
| Slot | Option | Reason | Confidence |
|---|---|---|---|
| T3-S1 | C | general knowledge: GABA analogue, probably saturable transport; the abstract giving only the two lower ratios suggests the highest dose differs, most plausibly lower; BATCH5 has no body data | low |
| T3-S2 | B | general knowledge: brain-to-plasma ratio low, roughly dose-independent; a hedge against S1 | low |
| T3-S3 | A | general knowledge: whole-eye homogenate; BATCH5 shows retina-specific work is a later 2021 paper (PMID 33385945) | medium |
| T3-S4 | B | BATCH5 gives the title (tissue distribution and metabolic correlations): biochemical readouts only | medium |
| T3-S5 | B | general knowledge: 'metabolic correlations' means tissue VGB against GABA and metabolites, not an enzyme assay; BATCH5 lists only literature GABA-T values | low |
| T3-S6 | B | general knowledge: short dosing, weight did not differ | low |
| T3-S7 | B | general knowledge: adult mice 8 to 16 weeks | low |
| T3-S8 | A | general knowledge: chiral derivatisation (Marfey-type) with achiral LC-MS/MS is the common route; not sure | low |
| T3-S9 | A | general knowledge: racemate, liver S/R near plasma; enrichment more likely in retina (BATCH5, PMID 33385945, title only) | low |
Delegate's remark: BATCH5 lists only the title of the paper; the V3_1 file was irrelevant for T3.


## Arm C reasons as delivered (three delegates, one per text)

## Arm C, T1 (sonnet, effort high self-reported; tools: none; recalls the paper body: partly, in general terms)
| Slot | Option | Reason | Confidence |
|---|---|---|---|
| T1-S1 | A | typical mouse tissue panels include brain with a likely low numeric value | low |
| T1-S2 | A | eight metabolites, ethylbenzylidene: de-ethylation or oxidation plus conjugates | low |
| T1-S3 | B | in vitro IC50 reported around 20-60 micromolar | medium |
| T1-S4 | C | abstract does not mention binding | medium |
| T1-S5 | B | SCID xenograft mice typically 6-8 weeks | medium |
| T1-S6 | A | poorly soluble; DMSO with a co-solvent | medium |
| T1-S7 | A | probably states mice tolerated it, since it explains lack of efficacy by PK | medium |
| T1-S8 | A | lipophilic compound accumulates in fat, listed first | medium |
| T1-S9 | A | both xenografts at least tenfold below plasma; similar penetration | medium |

## Arm C, T2 (sonnet, effort high self-reported; tools: none; recalls the paper body: no)
| Slot | Option | Reason | Confidence |
|---|---|---|---|
| T2-S1 | A | TTA-P2 routinely i.p. in mouse seizure studies; prior ETX work from the group also i.p. | medium |
| T2-S2 | B | typical pretreatment about 30 min | low |
| T2-S3 | C | the abstract mentions no motor or sedation control; probably not reported | low |
| T2-S4 | A | vapour chamber with pyrazole is the standard model for this group | medium |
| T2-S5 | B | usually three or four cycles | low |
| T2-S6 | A | Racine or modified Racine | medium |
| T2-S7 | C | the abstract names 20 and 40 mg/kg against PTZ 40, so 10 mg/kg probably not tested in non-withdrawal mice | medium |
| T2-S8 | B | vehicle mortality at PTZ 40 mg/kg in DBA/2J likely partial, 25 to 75 percent | low |
| T2-S9 | A | ordinal scores, Kruskal-Wallis or Mann-Whitney | medium |
| T2-S10 | B | adult DBA/2J mice commonly 8 to 12 weeks | low |

## Arm C, T3 (sonnet, effort high self-reported; tools: none; recalls the paper body: no; the abstract was given with the S/R symbols restored by IT, which the source text had lost)
| Slot | Option | Reason | Confidence |
|---|---|---|---|
| T3-S1 | B | passive non-saturating accumulation, ratio near constant | medium |
| T3-S2 | B | brain ratio roughly dose-independent | medium |
| T3-S3 | A | 'eye' listed as one tissue, whole-eye homogenate | medium |
| T3-S4 | B | only mass-spectrometry biochemical endpoints in the abstract | high |
| T3-S5 | B | no enzyme assay mentioned | high |
| T3-S6 | B | 12-day infusion, weights usually unaffected | low |
| T3-S7 | B | adult C57BL/6 8 to 16 weeks | low |
| T3-S8 | A | Marfey-type derivatisation then LC-MS/MS is common; same lab's earlier VGB work | medium |
| T3-S9 | A | plasma S/R 0.74, liver probably similar | low |

