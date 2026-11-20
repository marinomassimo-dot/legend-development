# ADV-123 producer A: report as delivered (legend-delegate, sonnet, effort medium, one round, no sub-delegation; delivered 2026-11-20; persisted verbatim by SCI from the subagent hand-back, which is the only place it lived; brief: PRODUCER_A_BRIEF_ARM_A_SCI_20261120.md). Producer output, NOT yet verified by SCI or a second reader: every number is a producer claim until adjudicated. Hypothesis level; no dose is a recommendation; not medical advice.

ADV-123 PRODUCER A REPORT, ARM (a): rescue studies with a myelin readout. SCI window S, 2026-11-20. Hypothesis level. No dose, schedule or recommendation; animal doses are findings of the sources. Reference genotype class only. Not medical advice.

Basis. According to PubMed (search and metadata tools; DOIs below) plus plain-HTTP Europe PMC REST, NCBI efetch (db=pmc) and held files under files/fulltext. No e-mail address or personal detail was sent anywhere. No gate, LINT or test was run. No repository file was edited. Scratch is in /home/desktop/.claude/jobs/53cd1e96/tmp/adv123/producer_a/ (downloads in dl/, quote check in verify.py).

Quote check. Every quote marked [Q] was verified by substring against bytes I fetched (verify.py: 36 of 36 found, whitespace and thin spaces normalised, tags stripped). A quote marked [LEDGER] comes from an existing receipt, not from my bytes.

Depth codes. FT = passage read in a full text I fetched or hold. AB = abstract only.

Routes tried:
- PMC page: reCAPTCHA, stopped for that route.
- jneurosci.org: Cloudflare 403.
- Europe PMC fullTextXML: HTTP 500 on retry for PMC3841446, PMC7065955, PMC3225598, PMC5546107, PMC4496262, PMC11081874 and PMC10731584.
- efetch: full text for PMC3225598, PMC7065955 and PMC10731584; publisher-restricted stub for PMC3841446 and PMC11081874.
- The PubMed full-text tool returned an empty full_text for PMC3841446.

TIMING codes are as in the pre-registration. Where a study measured myelin at one age only but function longitudinally, I give SAME_TIME and say so.

## 1. ADMITTED ROWS (10; 3 of them partly arm (b) in kind and marked so)

Row A01. Rett, Mecp2 restored in the oligodendrocyte lineage only (Nguyen 2013, J Neurosci, doi 10.1523/JNEUROSCI.2657-13.2013, PMID 24285883).
- Model and lesion: global Mecp2-null (Stop allele); the restoration is a germline cross with an oligodendrocyte-lineage Cre, so the lesion persists in neurons.
- Intervention: genetic restoration in OL-lineage cells. No restoration age is stated (germline cross; the ledger records this).
- Function (AB): "although only mildly prolonging their lifespan, significantly improved the locomotor deficits and hindlimb clasping phenotype, both in male and female mice, and fully restored the body weight in male mice".
- Myelin (AB): the level of some myelin-related proteins was impaired in null mice. Restoration only partially restored it.
- [LEDGER] FTR-20261105-24285883-24 (partial full text read 2026-11-05, bytes not saved): MBP "only partially restored to ~60%", PLP "remained aberrant"; an anxiety endpoint did not improve.
- TIMING: F_ONLY. Ages of readouts are not printed in what I could reach.
- Depth: AB for my reading; the ledger holds a partial full-text read.
- One-origin flag: none within the arm.
- Competing explanation: improvement from OL-lineage Mecp2 acting on non-myelin functions, or from Mecp2 in other NG2-Cre-expressing cells.
- Weakening: myelin proteins were not normalised, so function improved without myelin normalisation. The authors read the residual as non-cell-autonomous, from neurons or other cells outside the restored lineage.
- Locator and quote [Q]: Abstract, "Expression of MeCP2 in oligodendrocytes of these mice only partially restored their expression".

Row A02. Pitt-Hopkins (Tcf4+/-) mice carrying an MECP2 transgene (Mol Cell Neurosci 2026, doi 10.1016/j.mcn.2026.104094, PMID 41997465).
- Lesion: Tcf4 heterozygous (global). The lesion persists; MeCP2 is raised by transgene or viral vector.
- Function: "behavioral rescue also extends to a contextual fear learning task". Earlier behavioural rescue is cited in the abstract.
- Myelin: RNA-seq and protein expression of OL genes, "unchanged in the presence of an MECP2 transgene". No ultrastructure is mentioned.
- TIMING: F_ONLY. Ages are not stated in the abstract.
- Depth: AB only. Europe PMC says not in PMC and not open access. The publisher link resolves to a linking page with no text. The ledger has a matching abstract-only receipt (FTR-20261105-41997465-24).
- Competing explanation: myelin molecular markers too coarse, or the transgene acts on circuits independent of OL maturation.
- Weakening: the same abstract reports more Olig2 and Gfap co-expressing cells, suggesting a shift toward astrocytes.
- Quote [Q]: "OL gene expression and molecular phenotypes in Tcf4+/- animals are unchanged in the presence of an MECP2 transgene".
- This is a rescue of function with the neuronal lesion persisting and the OL readout not moving. Abstract level only, so it cannot meet a threshold alone.

Row A03. Angelman, Ube3a maternal-null mouse, ESR-beta agonist AC-186 (bioRxiv preprint 2026, PMC13228336, PMID 42239330; not peer reviewed). Arm (b) in kind.
- Lesion: neuronal and glial Ube3a loss, not corrected; AC-186 "did not modify UBE3A levels".
- Intervention: AC-186 10 mg/kg intraperitoneal daily from P13-14.
- Function: hindlimb clasping at P35, rotarod, contextual fear conditioning. Clasping and rotarod improved; contextual fear improved; cued fear was not different between groups.
- Myelin: OPC density and proliferation (PDGFRa and Ki67 in corpus callosum) and MBP and OL-lineage markers by immunofluorescence at P42 (Figs 7G, S11, S12). Printed as restored.
- TIMING: SAME_TIME. Behaviour at P35 to about P41 and histology at P42; no earlier myelin readout after treatment.
- Depth: FT (preprint text and legends; supplement figures embedded as images, not viewed).
- One-origin flag: single laboratory.
- Competing explanation: ESR-beta agonism acts on neurons or on LTP. The text states AC-186 did not rescue the neuronal plasticity marker in neurons alone (Fig S6B) but did in neuron-OPC co-culture.
- Weakening: bulk MBP and cell counts only, with no EM. n is 3 animals per group for the baseline Fig 7B quantification; n is 6 to 10 for 7G; n is 11 to 20 per group for the behaviour.
- Quotes [Q]: "it notably restored oligodendrocyte populations and myelination in AS mouse brains"; "AC-186 treatment significantly alleviated neurological symptoms in AS mice, enhancing their performance to wildtype levels without affecting wildtype mice".
- Weak and preprint. Counts as support only.

Row A04. Tsc1 Emx1-Cre forebrain deletion, rapamycin (Carson 2012, Neurobiol Dis, PMC3225598, PMID 21907282).
- Lesion: Tsc1 loss in forebrain neural progenitors (neurons and some glia).
- Intervention: rapamycin 3 mg/kg intraperitoneal, Monday to Friday, from P13-15 to P40.
- Function: survival. Treated KO n=12 all survived and had no seizures; vehicle KO "died by P25".
- Myelin: MBP immunostaining, reduced at P20 untreated. At P40-44 treated KO "approaching" control, a Sudan Black stain for the deficit.
- TIMING: SAME_TIME. Survival diverged by P25; the treated MBP reading is at P40-44 only; no two-age myelin series after treatment.
- Depth: FT (passages and legends).
- One-origin flag: none within the arm.
- Competing explanation: mTORC1 inhibition acts directly on oligodendrocytes (Emx1-Cre also deletes in some glia).
- Weakening: neuronal lamination was not corrected, which keeps the neuronal lesion in place. Rapamycin did not change myelination in control mice. Vehicle KO mice were dead by P25, so no treated-versus-untreated MBP comparison exists at P40.
- Quotes [Q]: "all rapamycin treated Tsc1Emx1-Cre CKO mice (n=12) thrived with this regimen with no mortality"; "exhibited increased cortical myelination approaching levels and patterns of MBP expression similar seen to those seen in control mice".

Rows A05 and A06 (one publication, one origin). Tsc1 Emx1-Cre with Raptor reduction (Nat Commun 2022, PMC9363483, PMID 35945201; I checked that a repository receipt exists as partial, 1 receipt).
- A05, genetic: Rptor heterozygous deletion.
  - Function: median survival of Tsc1-cKO from 18.5 to 24.5 postnatal days, and 26% of Raptor-cHet survived past P40.
  - Myelin: MBP at P14-15, "improved cortical myelination, resulting in an intermediate phenotype between WT and Tsc1-cKO".
  - TIMING: SAME_TIME (myelin at one age; survival to P40).
  - Weakening: homozygous Rptor loss gave near-normal survival but severely reduced cortex and no clear hippocampus.
  - Quotes [Q]: "loss of one copy of Rptor reduced cortical and hippocampal hypertrophy, ameliorated hippocampal lamination defects, and improved cortical myelination, resulting in an intermediate phenotype between WT and Tsc1-cKO mice"; "Heterozygous deletion of Rptor led to a significant shift in the median survival of Tsc1-cKO mice from 18.5 to 24.5 postnatal days".
- A06, postnatal: AAV9-shRptor injected at P0 (cortex and hippocampus).
  - Function: survival over the first 40 days and body weight improved.
  - Myelin: bulk cortical MBP at P16, n=6 per condition.
  - TIMING: SAME_TIME.
  - Weakening: the text says MBP rose "to near WT levels", yet the legend gives Tsc1-KO+shCtrl vs Tsc1-KO+shRptor p = 0.4833 (not significant), and Kruskal-Wallis p=0.0114. The text claim and the statistic disagree.
  - The authors attribute the MBP rise to a non-cell-autonomous effect of neuronal Raptor reduction (a hypothesis in the text).
  - Quotes [Q]: "We found that shRptor boosted bulk cortical MBP fluorescence in Tsc1-cKO mice to near WT levels"; legend "Tsc1-KO+shCtrl vs Tsc1-KO+shRptor, p = 0.4833".
  - Bulk marker, so weak.
- Depth: FT. Competing explanation for both: Emx1-Cre also deletes in some glia, so a direct oligodendrocyte effect cannot be separated.

Row A07. Tsc2+/- mouse, ENT1 inhibitor J4 (J Biomed Sci 2026, PMC13274077, PMID 42310739). Arm (b) in kind.
- Lesion: Tsc2 haploinsufficiency (global), uncorrected. J4 in drinking water 0.06 mg/ml for 10 weeks (about 10.2 mg/kg/day as estimated by the authors); methods give males aged 6 to 12 weeks.
- Function: open-field centre time and novel-object discrimination index, both improved in Tsc2+/- J4.
- Myelin: EM g-ratio and thickness versus axon diameter (corpus callosum), diffusion MRI, and MBP and PLP-NF co-staining in cortex and hippocampus.
- TIMING: SAME_TIME (end of the 10 weeks).
- Depth: FT.
- Competing explanation: J4 reduces neuronal hyperactivity (pS6 and cFos), which the authors discuss as an upstream route.
- Weakening: white-matter MBP staining showed no difference between genotypes. The deficit appears only by EM and MRI. Male only; mild phenotype.
- Quotes [Q]: "J4 treatment significantly increased the slope (F(1, 1660) = 13.97, p = 0.0002), restoring the myelin thickness-axon diameter relationship toward WT Veh control levels"; "the WM regions did not display any apparent differences in MBP staining when comparing the WT Veh, Tsc2+/– Veh, and Tsc2+/– J4 groups".
- Strongest ultrastructure among the non-Wwox rows. One origin.

Row A08. Huntington, LacQ140 inducible mHtt lowering (Neurobiol Dis 2023, PMC10731584, PMID 37777020; preprint twin PMID 36747614 = same origin).
- Lesion: striatal-onset mHtt expression. Lowering by IPTG withdrawal at 2 or 8 months, or repression from conception; 38 to 52% cytoplasmic and synaptic mHTT lowering.
- Myelin: striatal white-matter lipids (ceramide, sphingomyelin, MGDG) and myelin-gene mRNA at 6, 9 and 12 months. A bulk lipid and transcript marker with no ultrastructure, so weak.
- Function: behaviour is not measured in this paper. It cites Marchionini 2022 (not read) and states that the 12-month biochemistry comes from the same animals as that longitudinal behaviour.
- Printed combination: "behavior was closer to normal at 6 and 9 months with early mHTT lowering, but the protective effect of lowering degraded by 12 months".
- TIMING: SAME_TIME at each of three ages. The lipid change at 9 months "disappeared at 12 months" even without lowering. That is a transient myelin-marker change, so a clean order is not available.
- Depth: FT (Abstract, Results and Discussion passages) for the myelin side; function side is secondary (cited only).
- Competing explanation: lipid normalisation reflects spontaneous repair, not lowering.
- Quotes [Q]: "Total striatal lipids were reduced in 9-month-old LacQ140 mice and preserved by mHtt lowering"; "the lipid differences in LacQ140 mice measured at 9 months disappeared at 12 months".

Row A09. Wwox-null, neuronal AAV9-hSynI-Wwox (Repudi 2021, EMBO Mol Med, PMC8649866, PMID 34747138; held full text read by me).
- Lesion: global Wwox null (WOREE-type).
- Intervention: one ICV injection at P0, 2 × 10^10 vg per hemisphere (the text prints "2 × 1010/hemisphere", the exponent being lost in text extraction) of murine or human construct. No other dose arm.
- Function: mice "indistinguishable from wild type by the age of 6 weeks"; survival extended (Kaplan-Meier, treated total n=18 versus 6 GFP and 8 non-injected); glucose normal; seizures and ataxia absent.
- Myelin: MBP immunofluorescence at P17; CC1 and PDGFRa counts in the corpus callosum (n=3 per group). EM at P17: more myelinated axons and higher g-ratio-based thickness versus KO. EM at 6 months: "similar number of myelinated axons in rescued mice ... compared to wild type", with a g-ratio difference (P = 0.011334 printed).
- TIMING: SAME_TIME at P17, with a second myelin age (6 months). F_FIRST is not supported by this paper because myelin had already changed at P17. A lag between function and myelin normalisation exists only as "partial at P17, similar to WT count at 6 months", with function normal in between.
- Depth: FT.
- Per animal or per field: the legend says "average number of myelinated axons in corpus callosum from WT (n = 3), KO (n = 3), or KO mice injected with AAV9-hSynI-mWwox (n = 3) per field of view (FOV)". It does not state whether the unit plotted is the mouse or the field. The g-ratio is pooled: "~300, 100 axons per mouse, n = 3 per genotype" in Methods, and the figure legend gives n = 350 axons per group.
- Premise check. The held ADV-120 measurement (not mine, one origin) reports for P17 WT 130.3, KO 45.7, treated 104.9 myelinated axons per FOV (ratio 0.70), and the unmyelinated count in treated 1.95 times WT. That is consistent with the text calling the P17 count improved but not normal. The premise in the pre-registration ("51.5 treated against 26.4 WT unmyelinated, n = 3, one dose, P17") matches that direction. I did not re-measure the bars.
- One-origin flag: same laboratory as A10.
- Competing explanation: ICV neuronal AAV9 may also transduce some glia, and global Wwox restoration includes the hypoglycaemia correction; seizure control may by itself feed myelination.
- Weakening: n = 3 per group in a single EM design; adult EM has no dose or order comparison.
- Quotes [Q]: "neuronal restoration of WWOX using AAV9‐hSynI‐mWwox increased the number of myelinated axons compared to KO at P17"; "similar number of myelinated axons in rescued mice (AAV9‐hSynI‐mWwox, n = 3) compared to wild type (n = 3) at the age of 6 months".

Row A10. Wwox-null, neuronal AAV9-hSynI-hWWOX, two doses (Obeid 2026, Mol Ther Adv, PMC13343157, PMID 42422765; held full text read by me).
- Doses: low (LD) 1.23 × 10^11 vg; high (HD) 2.63 × 10^11 vg; P0-P1 ICV. The text prints exponents in the usual way.
- Function: survival (HD comparable to WT; LD "modestly" extended); glucose normal by P20 in HD and across groups from P30; clasping at P18 "LD treatment resulted in partial improvement and HD treatment achieved near-complete rescue"; HD behaviour tested at 3 months (open field, plus maze, rotarod); LD mice did not survive to P90.
- Myelin: MBP immunostaining at P18 in corpus callosum, cortex, striatum and anterior commissure. HD "near-complete rescue across affected regions", LD "only partial recovery relative to HD". The treated bars are images, so no numbers are in the text (consistent with ADV-120).
- TIMING: SAME_TIME. MBP and clasping were both read at P18; later ages carry function only (survival, 3-month behaviour). Myelin was not re-read later in this paper.
- Depth: FT.
- One-origin flag: same laboratory as A09; a joint count of one.
- Weakening: bulk MBP intensity, no ultrastructure; the text calls the rescue "near-complete" while the P17 EM count in A09 was not normal.
- Quote [Q]: "HD treatment achieved near-complete rescue across affected regions, whereas LD treatment produced only partial recovery relative to HD".

Counts by origin and depth. Independent origins: Mecp2 OL-lineage restoration (1, AB, with a partial ledger read), PTHS-MECP2 (1, AB), AS preprint (1, FT, preprint), Tsc1 rapamycin (1, FT), Tsc1-Raptor (1 publication, FT), Tsc2 J4 (1, FT), HD LacQ140 (1, FT on myelin side, function secondary), Wwox (1 laboratory, 2 papers, FT). Total: 8 origins, 10 rows; 6 of the 8 origins at FT depth. No ultrastructure-level rescue row outside Wwox and J4.

## 2. LESION-LOCALISATION AND BOUNDARY NOTE (lack one readout, or no rescue)
- Rett, OL-lineage Mecp2 deletion (same Nguyen 2013): mice "more active and developed severe hindlimb clasping"; no myelin readout in the abstract, no rescue. Lesion-localisation only.
- PMID 32015540 (Phan 2020, Nat Neurosci, doi 10.1038/s41593-019-0578-x, PMC7065955; full text read): Pitt-Hopkins models show cell-autonomous reductions in OL numbers and myelination; Olig2-Cre Tcf4+/flox phenocopies the OL defect. No rescue and no functional readout. Localisation only.
- PMID 37068912 (clemastine in Tcf4 mutants): ledger partial read, 2026-11-13; arm (b) belongs to another producer. Held leads: Tcf4 callosal conduction improved while total myelinated-axon density was not restored. Not re-read.
- Angelman PMID 39726042 (Mol Autism 2024, PMC11670556; full text read): myelination delay from loss of neuronal UBE3A, not oligodendrocyte haploinsufficiency; no mouse functional readout and no reinstatement. Localisation only.
- Angelman PMID 28663201 (Judson 2017, AB): reduced axon caliber and slowed conduction in white matter; no rescue.
- Angelman PMID 26028516 (AB): myelin proteins normalised by a maternal higher-fat diet; no functional readout.
- PMID 28183733 (CTGF/CCN2, Tsc1 neuron deletion, PMC5339668): neuronal Ctgf deletion improved MBP and MAG and the myelinated-axon count; no functional readout (full text read; grep for seizure, survival, behaviour found none). Not admitted.
- PMID 38429929 (SCA3 ASO, Mol Ther 2024, AB; publisher restricted): OL maturation "transcriptionally, biochemically, and functionally rescued"; I could not reach the text to see whether "functionally" is organismal. Not admitted.
- PMID 36674969 (Rett IEG paper), 22334035 (CNPase down in Mecp2-null), 34117744 (MECP2 mutant monkeys, white-matter imaging), 28687309 (axon diameter in peripheral nerve): deficits only, no rescue.
- PMID 27126634 (YAC128 and BACHD myelination deficits), 32348987 (Fmr1 knockout white-matter alterations): deficits only.
- PMID 38983872 (GCDH gene therapy, glutaric aciduria): metabolic primary lesion; excluded by the inclusion rule.
- Obeid MBP-promoter hWWOX arm: "no phenotypic improvement"; the OL-restricted arm printed no myelin readout. Lesion-localisation only.

## 3. TWO LINES PER ITEM
Item 1, Rett/MECP2. Answers: the only restoration row is OL-lineage-only restoration (A01, AB) and the Tcf4/MECP2 transgene row (A02, AB); both show function improving with myelin not normalised. Missing: no Mecp2 reactivation, AAV9-MECP2 or ASO study with a myelin readout was found. Routes: PubMed Title/Abstract queries (Mecp2 with myelin, oligodendrocyte or white matter; with reactivation, restoration, gene therapy, AAV9 returned one record, A01); repository receipts and files/fulltext (no Rett or Mecp2 file; ledger holds A01 and A02 only); one external route (Europe PMC and efetch, restricted text).

Item 2, Angelman/UBE3A. Answers: no genetic or ASO Ube3a reinstatement with myelin was found; the one rescue is a drug (A03, preprint). Missing: Ube3a reinstatement with MBP or EM. Routes: PubMed Ube3a/Angelman with myelin, OL, white matter (26 records read by title, the four relevant ones by abstract); ledger and files/fulltext empty for these PMIDs; Europe PMC full text for PMC11670556 and PMC13228336.

Item 3, other neuronal lesions. Answers: Tsc1/Tsc2 give four rows with both readouts (A04 to A07); HD gives one with a weak myelin marker (A08); Pitt-Hopkins gives A02 and boundary leads. Missing: Fmr1, Cdkl5 (PubMed Title/Abstract returned no rescue study with a myelin readout) and an ASO or gene-restoration study with both readouts. Routes: PubMed per disorder; ledger and files/fulltext (no Fmr1, Cdkl5 or Huntington file); Europe PMC and efetch.

Item 4, Wwox. Answers: A09 and A10 above, with the per-field and n statement. Missing: the exact P17 and 6-month counts as printed numbers (the text gives only the direction; the figure values come from the ADV-120 measurement); the P18 MBP treated bars are images. Routes: held XML for PMIDs 34747138 and 42422765, read by me.

Item 5, timing. Answers: no row shows myelin changing before function. Rows with two or more myelin ages: A09 (P17 then 6 months; improved at the first age) and A08 (6, 9, 12 months; transient). All other rows are SAME_TIME or F_ONLY. A01 and A02 are F_ONLY. Missing: a study measuring myelin before and after a function change in the same animals; none found.

## 4. CONFLICTS BETWEEN SOURCES
1. Cell of origin of the Ube3a myelin phenotype: the 2024 Mol Autism paper says delay "is caused by the loss of UBE3A in neurons rather than UBE3A haploinsufficiency in oligodendrocytes" (quote verified in the abstract); the 2026 preprint says OL-lineage UBE3A depletion "was sufficient to reduce myelin marker intensity" and reports an intrinsic requirement. Different models and readouts, not reconciled.
2. Ube3a ultrastructure: Judson 2017 reports small-caliber axons; the 2024 paper says "Our earlier studies suggested a decrease in axon size [21]. However, in this study, we did not see any significant reduction" and the myelination delay normalises by P30 (verified in the full text).
3. Raptor shRptor MBP: text "near WT levels" versus legend p = 0.4833 for KO+shCtrl versus KO+shRptor.
4. Wwox: text calls myelination improved and the 6-month count similar to WT, but the g-ratio differs (P = 0.011334 printed), and Repudi's discussion itself says "there are still some differences between rescued and WT mice"; Obeid says "near-complete rescue" at P18 by bulk MBP.
5. Pitt-Hopkins: Phan 2020 says OL defects are cell-autonomous; the clemastine paper (held) says conduction improved but myelinated density was not restored.

## 5. WHERE THE DATA ARE THINNEST
1. Rett restoration: no genetic reactivation, AAV or ASO study with a myelin readout reached; the two Mecp2-axis rows are abstract-level (A01 partial ledger read only).
2. Angelman: no Ube3a reinstatement with myelin; the only rescue is one preprint with bulk MBP.
3. Timing: only A08 and A09 have more than one age for myelin, and A09 has n = 3 per group with a per-field unit; no row separates myelin-first from function-first.
4. Myelin measures: seven of ten rows use bulk MBP, lipids or marker expression; ultrastructure appears only in A07, A09 (n = 3) and A04 (Sudan Black only).
5. Neuronal lesion correction versus persistence: Emx1-Cre and global models make it hard to exclude direct glial effects (A04 to A06, A09); function in A08 comes from a paper I did not read.

Files: scratch only, /home/desktop/.claude/jobs/53cd1e96/tmp/adv123/producer_a/ (dl/*.txt text conversions; verify.py; titles.py; abs.py).
