# Independent verification of the needs table (iteration 3)

Auditor: scientist-c (did not produce the table). Date: 2026-10-28. Subject:
`disease-models/wwox/research/drug_repurposing/needs/needs.json` at main `1337d0de` (22 needs, 56 observations).
Status: non-canonical audit. Read-only toward every repository file except this report. No contact, registration or spend; no personal data.
Not medical advice.

Method. For each of eight needs, every observation was opened against its cited locator (manifest entry text and snippet,
repository document, card assertion, registry record via `registry_records.py`, never by grepping the two large registries).
Neighbouring manifest entries were read when the cited one is qualified by them. Verdict vocabulary per item:
SUPPORTED, OVERSHOOT (the table says more than the source), UNDERSHOOT (says less, or omits material counter-evidence that exists
in the record), NOT_IN_SOURCE (the cited locator does not contain it), UNVERIFIABLE (could not be checked here). Error and
uncertainty are kept apart: an item is an ERROR only where a source in the repository contradicts or does not contain the wording.

## 1. Recomputed counts (from the JSON)

| Quantity | Table claims | Recomputed |
|---|---|---|
| Needs | 22 | 22 |
| Observations | 56 | 56 |
| Intervention direction | uncertain 12 (needs.md) | uncertain 12, restore 5, down 3, up 2 (modulate 0) |
| Track | - | A 18, B 4 |
| Goal | - | partial_benefit 17, deep_recovery 5 |
| Track x goal | - | A/partial 17, B/deep 4, A/deep 1 (gene addition) |
| Need basis | - | observed 20, exploratory_question 2 (PTC read-through, GABA chloride gradient) |
| Observation scope | - | WWOX_EXPERIMENT_IN_DEE_SYSTEM 36, WWOX_BIOLOGY_OTHER_CONTEXT 10, COMPUTATIONAL_RESULT 8, UNVERIFIED_HYPOTHESIS 2, OTHER_DISEASE_PRECEDENT 0 |
| locator_status | - | MANIFEST 43, DOCUMENT 11, REGISTRY_ONLY 2 |

All stated counts reproduce. `check_needs.py` exits OK (it checks pointers and anchors, not support, as it declares).
Observation: no observation carries OTHER_DISEASE_PRECEDENT, yet four needs list it at need level (MISSENSE-PROTEIN-RESCUE,
ISR-ATTENUATION, EXCITATORY-GAIN, NEUROINFLAMMATION-GLIA); in the three I opened the precedent lives only in counter_evidence or
inferred as prose without a locator (see C5). UNVERIFIED_HYPOTHESIS is listed at need level for PDH-PYRUVATE-AXIS and
MTOR-AUTOPHAGY with no observation carrying it.

## 2. Needs audited (8 of 22) and why

| Need | Selection reason |
|---|---|
| NEED-WWOX-GENE-ADDITION | gene-replacement / restoration; only Track A + deep_recovery |
| NEED-WNT-BETA-CATENIN | required; also organoid and computational |
| NEED-MYC-PROGENITOR-PROLIFERATION | built from organoid analyses |
| NEED-ISR-ATTENUATION | direction uncertain; computational; other-disease precedent in counter-evidence |
| NEED-PDH-PYRUVATE-AXIS | direction uncertain; mixed scopes; PDK1/PDPK1 collision |
| NEED-GABA-CHLORIDE-GRADIENT | exploratory_question; computational |
| NEED-WWOX-PTC-READTHROUGH | exploratory_question; Track B |
| NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR | other-disease precedent (GRIN/memantine); perturbation-based direction |

## 3. Verdict per observation (22 observations in the 8 needs)

Tally: SUPPORTED 13, OVERSHOOT 8, UNDERSHOOT 1, NOT_IN_SOURCE 0 (as a whole-observation verdict; three sub-claims below),
UNVERIFIABLE 0 (as a whole-observation verdict; sub-claims below).

### 3.1 GENE-ADDITION (Track A, deep_recovery; direction restore)
- O1 survival: **OVERSHOOT** (one clause). Numbers (HD plateau 76-77 percent, WT 71-72, LD 0 percent at about day 77, LD better than untreated
  knockout p<0.0001) are exactly in manifest entries 40 and 46. But `direction_observed` says "threshold-like, not graded" and
  `counter_evidence` says "Survival is a threshold between two doses". Entry 40 states the opposite constraint: "'a step and not a gradient'
  is NOT read from this panel"; the panel shows a staircase decline at LD and a plateau at HD, two doses cannot tell a threshold from a
  steep gradient. The `limits` text is correct; the direction label and the counter-evidence line contradict it. Dose unit absent
  (entries 31, 33) and bilateral 2.0 uL ICV (entry 32) are consistent with the limit given.
- O2 spike-wave discharges: **SUPPORTED**. Means 0.635 / 0.13 / 0.03, **** KO-HD, ns WT-HD, no LD arm, n 5, P14 to P21 (entry 42 and
  reference scaffold row E1). Not carried but within the source: SWD are an absence-type correlate only (scaffold row E1).
- O3 neuron-specific deletion myelin: **SUPPORTED**. 180 versus 55 per field (3.3-fold) at P17, n 3 mice, flat negative for Olig2-Cre and
  GFAP-Cre (PMID 33914858 entries 0 and 29). Note for consumers: this is a cell-type deletion, not a rescue; it justifies the neuron
  as the restoration site, not efficacy of addition.
- Counter-evidence "motor coordination exceeds wild type on one panel": the sentence is in the rescue paper's text (map section for R-01 quotes it),
  but the panel-level count is unresolved in the record (map line 35 says three of eight panels exceed; line 435 says the count is
  unadjudicated). **UNVERIFIABLE** as "one panel". Wording fix below (C2). The "unmyelinated 52 versus 26" and "SATB2 about eleven-fold" lines are
  **SUPPORTED** (PMID 34747138 entry 9; PMID 42397075 entry 22).
- Track A (lesion-independent supply of a working copy) and goal deep_recovery (aim, with the separate basis that endpoints were measured): **SUPPORTED**.
  The basis correctly says Track A is not a statement about depth.
- Intervention direction restore: justified by neuron-restricted loss reproducing the phenotype plus neuron-restricted restoration rescue,
  not by reversal alone: **SUPPORTED**.

### 3.2 WNT-BETA-CATENIN (Track A, partial_benefit; direction uncertain)
- O1 deposited tables: **SUPPORTED** on every number (entry 31: NKD1 1.23, AXIN2 0.79, LEF1 1.00, TCF7L2 1.04, CTNNB1 0.56, WNT8B 3.17, padj at most 1.58E-2; 4 versus 2 libraries, 8 sequenced and 2 excluded per entry 40).
  Two field errors: (a) `age_stage` "culture weeks 8-15" is **NOT_IN_SOURCE** for the transcriptome and the qPCR: the paper (entries 40, 55, 59, 63) says week 15; weeks 8-15
  is the A51 treatment window of a different paper. (b) CTNNB1 and TCF7L2 are pathway members and WNT8B is a ligand; the statement calls all six "targets" (the manifest
  proposition does the same). Wording only.
- O2 rescue arm: **UNDERSHOOT**. The five genes brought toward wild type and the non-normalised effectors are right (entry 60: WNT1 4.1 to 1.35, WNT3 2.65 to 1.0, WNT3A 1.65 to 0.2,
  WNT5A 3.1 to 1.95, ROR2 2.65 to 1.15; LEF1 2.3 to 2.6, TCF7 1.85 to 2.7, TCF4 1.7 to 3.45; n 4/4/4 one batch, entry 64). The entry's own headline, repaired after a blind audit,
  also says WNT2B (1.25 to 1.85) and WNT8B (2.2 to 2.45) move further from wild type under rescue, and AXIN2 and CCND1 are unmoved. The observation omits these, which are counter-evidence to
  "ligands toward wild type". Also WNT3A at 0.2 is below wild type (overshoot of the rescue), not "toward".
- O3 single-cell stage contrast: **OVERSHOOT**. Entry 5: the panel is late versus early cells; Wnt higher in early cells is read correctly; entry 5 itself states "Nothing about WWOX follows from that panel".
  The observation is labelled WWOX_EXPERIMENT_IN_DEE_SYSTEM with `direction_observed` "knockout composition less mature". "Less mature" is an interpretation; the measurement is neurons about -2.4 log2FC and radial glia about +1.0
  in the engineered knockout (entry 2). The same entry 2 says SCAR12 and WOREE patient lines are within about 0.3 of wild type on both fractions, which is missing from the need's counter-evidence
  (Track A basis relies on patient-line relevance). The stage-contrast half should carry a non-WWOX label.
- O4 calibration and blind reanalysis: **SUPPORTED** (62 samples, 25 to 652 days, six lines; 15 labelings so minimum permutation p 1/15; verdict (c) cannot decide). Omitted but in the document:
  point estimates survive adjustment with 25 to 45 percent attenuation and the verdict has "a weak lean away from" composition fully explaining it. "Could not separate" is right; the lean is not stated.
- Identity: HGNC ids CTNNB1 2514, LEF1 6551, AXIN2 904, TNKS 11941, TNKS2 15677, DVL2 3086, TCF7L2 11641, TCF4 11634 agree with my knowledge of HGNC; GO:0016055 and GO:0060070 mean what is attributed.
  The HGNC snapshot is not in git, so these were checked from memory, **UNVERIFIABLE offline**. The TCF4/TCF7L2 guard is right to exist; but the plotted "TCF4" in the 2021 qPCR (entry 60, alongside TCF3 and TCF7) is assumed to be TCF7L2 and the source does not say which gene; flag as UNVERIFIABLE identity assumption.
- Direction uncertain with a stated rationale (confound, rescue does not normalise, Wnt builds tissue): **SUPPORTED**. Track A / partial_benefit: **SUPPORTED**.

### 3.3 MYC-PROGENITOR-PROLIFERATION (Track A, partial_benefit; uncertain)
- O1 radial glia: **OVERSHOOT**. MYC top upregulated gene: SUPPORTED (entry 0). "MYC correlates with S/G2M in the knockout (G1/G0 in wild type)": entry 6 proposition says so, but entry 6's own snippet reads
  Figure 4D as "MYC-phase correlation about +0.2 for S in KO, negative for M, and near zero across all phases in WT"; no G2M correlation and no G1/G0 correlation in wild type are in the snippet; Figure 4C has no error bars or significance markers and
  Figure 4A density curves are near-superimposed. The proposition and the snippet of the same entry disagree; the need inherits the stronger wording and drops the magnitude (about +0.2) and the missing statistics.
- O2 all three mutant lines: **SUPPORTED** for MYC (entry 37: SOX2+MYC+/SOX2+ about 60, 50, 55 versus 20 percent, ***, **, ****; week 16). Locator gap: the second clause "composition phenotype is almost entirely in the engineered knockout"
  is not in entry 37; it is entry 2, whose own text withdraws the unqualified headline and says Figure 5F shows both patient lines invert the early/late neuronal balance (and entry 25: MYC activation in radial glia is shared, logFC about 1.8, 1.65, 1.6). Add entry 2 and the Figure 5F qualifier. The `readout` "MYC nuclear co-localisation" is a fraction of SOX2+ cells MYC+.
- O3 A51: **OVERSHOOT**. SOX2+ 60 to 33 percent, ns versus wild type: SUPPORTED (entry 23; entry 17 for the 125 nM, weeks 8 to 15 and non-selectivity). "Does nothing for the layer markers" is stronger than the data: SATB2 0.35 to 0.7 percent and CTIP2 0.2 to 0.3 are non-significant with small groups,
  CTIP2 stays **** below wild type; "not shown to change" is the supportable wording. `readout_level` "functional" is wrong for immunostaining cell fractions (cellular/phenotypic). The NEUN+ rise (about 6 to 18 percent, significant) is omitted from the statement though it is in `direction_observed`'s neighbour entry.
- Direction uncertain: the rationale is reversal-only ("raised MYC suggests lowering it"), but it is declared uncertain and the do_not_assume clause blocks the reversal reading: acceptable. Track A and partial_benefit with separate bases: **SUPPORTED**. MYC HGNC:7553, SOX2 HGNC:11195, GO:0008283, GO:0021987: consistent with my knowledge (UNVERIFIABLE offline).

### 3.4 ISR-ATTENUATION (Track A, partial_benefit; uncertain)
- O1 fly Atf4: **SUPPORTED** (entries 57, 58, 59: 1.0 versus 1.28, N 6, U=0 P=0.0022, y axis from 0.5; no change without amyloid, t=0.0894). Day-14 age from the card (not in the cited entries): consistent.
- O2 organoid ISR set: **SUPPORTED** (document RESULT: 12 targets, mean -0.288, P 0.0005 lower, CHAC1 -0.70, TRIB3 -0.64, PHGDH -0.32, ATF4/ATF5/DDIT3/ASNS ns, ATF4 flat, UPR branches P 0.43). Two omissions from the same document: SESN2 (-0.35, padj 0.03) is also individually down;
  and the document discloses CHAC1/TRIB3/PHGDH had been seen before the sets were fixed, so their per-gene direction is not a blind result. The "uncorrected across nine set tests" line is correct and matches the document's Bonferroni note.
- Counter-evidence on the paediatric dataset: **UNDERSHOOT**. "A paediatric tolerability dataset exists only in vanishing white matter" omits what the card (DR-E01-004, abstract-level) records: serious adverse events in about three quarters of 33 children, hallucinations in over half, severe constipation in three; and that the agent tested there (guanabenz) is not an eIF2B activator
  while the need's targets are eIF2B subunits. As written, "tolerability dataset" could be read as reassuring. The ALS lines (target engagement in the phase 1b abstract, ratio 1.04 with credible interval 0.83 to 1.32 at 24 weeks) are **SUPPORTED** but abstract-level; the PERK/pancreas line was not found in the card I opened: **UNVERIFIABLE**.
- Scope: OTHER_DISEASE_PRECEDENT is listed at need level but no observation carries it; the positive 2BAct mouse datum (DR-E01-003) is not mentioned anywhere in the need.
- Direction uncertain, with the explicit statement that no WWOX-dependent ISR increase is seen in a human system: **SUPPORTED** and well separated from reversal. HGNC ids (ATF4 786, EIF2AK3 3255, EIF2S1 3265, EIF2B1-5 3257-3261, DDIT3 2726) and GO:0034976, GO:0006446 agree with my knowledge; GO:0034976 is ER stress, a proxy for the integrated stress response (no ISR-specific GO term used).

### 3.5 PDH-PYRUVATE-AXIS (Track A, partial_benefit; uncertain)
- O1 Wwox-null MEFs: **OVERSHOOT** on the scope label only. Entries 4, 2, 1, 5 support each clause (HIF1alpha detected in KO, higher Pdk1, reduced oxygen consumption, no HIF1alpha difference under hypoxia). But mouse embryonic fibroblasts are non-neural and the observation's own `limits` says "not a DEE-specific system", yet it is labelled
  WWOX_EXPERIMENT_IN_DEE_SYSTEM, while the human non-neural fibroblast line in O2 is labelled WWOX_BIOLOGY_OTHER_CONTEXT (the vocabulary puts "non-neural cell line" there). The two labels are inconsistent; O1 should be WWOX_BIOLOGY_OTHER_CONTEXT. "PDK1 is raised at transcript level": the entry 2 sentence says "higher levels of Pdk1" without naming the level in the snippet: readout level unverified (UNVERIFIABLE).
- O2 human fibroblast line: **SUPPORTED** (entry 7: PDH activity no KO bracket in any condition; lactate higher in all four conditions; entry 8: no PDK activity or protein measured; the loss arm is a roughly three-fold mRNA reduction in a polyclonal population, entry 0 of that manifest, i.e. a knockdown as the need says).
- O3 organoid transcripts: **SUPPORTED** (SLC2A1 +1.40, HK2 +2.18, LDHA +0.75, PDK1 -0.34, PDHA1 +1.00, oxidative panel flat; glycolytic genes also fall with culture time).
- Missing counter-evidence (need level): **UNDERSHOOT**. The same human fibroblast paper reports cytoplasmic HIF1alpha DECREASED in the knockout in two of four conditions (2-fold in normoxia normoglycaemia; nearly 2-fold in hypoxia normoglycaemia; manifest 35328751 entries 9 and 11), with equal or higher values in the other two. That is the opposite sign to the MEF observation (O1 "HIF1alpha up") that anchors the chain, and it is not in the need (a search of the need for a cytoplasmic or decreased HIF1alpha statement found none).
  Also absent: the re-supply arm raises rather than lowers lactate in two conditions (entry 2), so lactate is not dose-faithful.
- Stated counter-evidence lines checked against the map and registry: PDK1 down, PDH unchanged, normal human metabolic screens with the count disputed (N-06), DCA nerve signal (N-08), digoxin (N-07), ketogenic diet listed among ineffective interventions in a severe case (DL-MOL-007): **SUPPORTED**.
- Identity: PDK1 HGNC:8809 with the PDPK1 alias collision recorded as a guard (the collision is real); PDK2-4 8810-8812, PDHA1 8806, PDHB 8808, SLC2A1 11005, HK2 4923, HIF1A 4910; HK2's listed aliases are genes that carry HK2 as an alias (KCNA5, HOOK2, KIF2A), correctly worded. GO:0006096 is named "glycolytic process" in GO; the label "glycolysis" differs (cosmetic).
- Direction uncertain (middle link has no human observation): **SUPPORTED**.

### 3.6 GABA-CHLORIDE-GRADIENT (exploratory_question; Track A, partial_benefit; uncertain)
- O1 placeholder: **OVERSHOOT** (scope of the negative). "No WWOX system has a measurement of E_GABA, intracellular chloride, NKCC1/KCC2 or a GABA response" is a universal negative; the cited entries (1 and 8 of the 2021 organoid paper) support only that this paper does not measure it and invokes depolarizing GABA from developmental literature. No search record is cited for the rest of the WWOX literature. Reword to "in the sources read for this table". The "default from textbook" label is justified.
- O2 NKCC1/KCC2 ratio and GABRB2/3: **SUPPORTED** on figures: from `organoid_panel_cpm.tsv` the ratio is 0.24, 0.29, 0.13, 0.14 in knockouts and 0.29, 0.30 in wild types (recomputed), GABRB2 about a quarter and GABRB3 about half of wild type. "No signed direction" is defensible given confounding, but the table omits that the ratio is not higher in any knockout (no hint of a more depolarising gradient) and that GAD1 differs about ten-fold (composition); both are in card DA-W2-020. Wording suggestion only.
- Basis exploratory_question: **SUPPORTED** (the need itself says a textbook premise is held to prevent its use as observed). Counter-evidence (amplitude hypofunction as competing account) is carried. SLC12A2 10911, SLC12A5 13818 agree with my knowledge; GO:0007214 is correct.

### 3.7 WWOX-PTC-READTHROUGH (exploratory_question; Track B, deep_recovery; direction restore)
- O1: **OVERSHOOT** in one clause. "No read-through experiment" is **SUPPORTED** by the card's bounded abstention record (zero hits in WWOX literature bodies; PubMed title/abstract query not re-runnable offline, so the zero is **UNVERIFIABLE** here but declared as bounded).
  "No enumeration of nonsense alleles in the record" is contradicted by the record in two places: discovery ledger DL-MOL-007 (a severe WOREE compound-heterozygote case carrying a stop-gain allele plus an exon-6 deletion, cited by the PDH need but not by this one), and the card's own search record, which says
  `analysis/ft116_cohort_triage_20260921.md` calls p.(Arg264Ter) a read-through candidate and a therapeutic-class census carries a read-through class row. Neither is a read-through measurement, but both are nonsense-allele entries in the record. The supportable statement is "no systematic count of nonsense alleles with stop-codon identity and +4 nucleotide" (the card's own wording). `counter_evidence` ("No WWOX read-through datum exists in either direction") is acceptable once the first clause is narrowed, and the in-repo candidate flag should be listed as non-evidence.
- The reference-genotype clause ("carries no premature stop in the stated analysis") is **SUPPORTED** by the w2 README line.
- Track B (allele-class specific) and deep_recovery with separate bases: **SUPPORTED**. Direction restore with rationale "conditional, nothing observed": **SUPPORTED**. GO:0006412 (translation) is correct but generic; a termination-specific term (translational termination) would map the read-through mechanism better (suggestion).

### 3.8 EXCITATORY-GAIN-GLUTAMATE-RECEPTOR (Track A, partial_benefit; direction down)
- O1 bursting: **SUPPORTED** (36/42, 4/23, 0/11; entry 0; the one-sixth heterozygote limit is stated).
- O2 d-APV: **SUPPORTED** (n 5 slices, 3 animals per the w2 README; "eliminated bursting" per the card; entry 25 for the delayed evoked response). Note: in the figure entry the d-APV bar is absent, so "zero" rests on the text sentence, and the delayed response overshoots baseline at washout (about 1.3); neither changes the statement.
- O3 EPSC amplitudes: **OVERSHOOT**. sEPSC 23.3 +/- 12.0 versus 24.7 +/- 13.6 pA: SUPPORTED (entry 6). "mEPSC amplitude is raised in the knockout" cites only the card, which reads the paper's text; but manifest entry 18 (same paper) states that in the mEPSC panel (B) and the sEPSC panel (F-f1) "the curves run almost on top of one another and separate by a sliver, each marked with a single asterisk",
  and no mEPSC amplitude values are given in the table. The statement and direction ("sEPSC small; mEPSC up") present an asymmetry that entry 18 does not support: both are slight. Also the KS test on pooled events (10 cells per genotype) inflates significance; this is in `limits` but not in the direction label.
- O4 pannexin-1 blocker: **SUPPORTED** on the numbers (entry 2: about 2.55 under BB-FCF, no marker; CBX about 0.15 with one asterisk, no washout reversal). "The only **selective** pannexin-1 blocker" is **NOT_IN_SOURCE**: the manifest calls it a pannexin blocker and the Discussion lists carbenoxolone's off-target actions, not BB-FCF's selectivity; from general pharmacology, brilliant blue FCF is also a P2X7 antagonist, so "selective" should be dropped.
- Direction down with rationale "a perturbation result, not a reversal inference" (d-APV abolishes bursts): the rationale is stated and is not reversal: **SUPPORTED**. The inferred memantine series (14 of 19 gain-of-function versus 3 of 15 loss-of-function/indeterminate) matches the card (DR-W2-002/003); the card adds that the 15 include 4 variants the authors call non-pathogenic, which the need omits (minor UNDERSHOOT). The OTHER_DISEASE_PRECEDENT lives only in `inferred` and counter-evidence with no observation or locator record.
- Track A (allele-blind network lever; Track B unmeasured) and partial_benefit (network state, burst control is not recovery): **SUPPORTED**. HGNC ids for GRIN1 4584, GRIN2A 4585, GRIN2B 4586, GRIA1-4 4571-4574, PANX1 8599, GJA1 4274 agree with my knowledge; the GRIN1/GPRIN1 alias collision is real; GO ids correct.

## 4. Track and goal across the eight needs

All eight (Track, goal) pairs are correct in kind and carry separate bases: gene addition A/deep; PTC read-through B/deep; the six others A/partial. No case was found where a Track B claim was made from a Track A observation or the reverse.
Two bases worth tightening: PDH's Track A basis cites preservation of the WW1 route in an SDR missense allele, an allele-class argument that belongs to a Track B discussion and is inference (it is labelled so); ISR's basis mentions "Q230P class", an allele-class term that the public edition otherwise avoids in favour of "reference genotype class".

## 5. Corrections needed (precise, not applied)

| # | Location | Correction |
|---|---|---|
| C1 | GENE-ADDITION O1 `direction_observed`; counter_evidence line 3 | Replace "threshold-like, not graded" and "Survival is a threshold between two doses" with: progressive extinction at the low dose, plateau at the high dose; threshold versus steep gradient not distinguishable with two doses (manifest entry 40). |
| C2 | GENE-ADDITION counter_evidence line 1 | "motor coordination exceeds wild type on one panel": say the source text asserts an exceedance (Figure 4K) and the panel-level count is unresolved in the record (map lines 35 versus 435). |
| C3 | WNT O1 `age_stage` (and any "8-15" on O2) | "culture week 15" (RNA-seq and qPCR). Weeks 8-15 is the A51 window in the 2026 paper. Optional: call WNT8B a ligand and CTNNB1/TCF7L2 pathway members, not targets. |
| C4 | WNT O2 | Add: WNT2B and WNT8B move further from wild type under rescue; AXIN2 and CCND1 unmoved; WNT3A falls below wild type (manifest entry 60). |
| C5 | WNT O3 | Relabel the stage-contrast half as non-WWOX evidence (entry 5: "Nothing about WWOX follows"); replace "knockout composition less mature" by the measured fractions; add to counter_evidence that SCAR12 and WOREE lines sit within about 0.3 of wild type on composition (PMID 42397075 entry 2). Add the reanalysis lean (25 to 45 percent attenuation, weak lean away from composition explaining all). |
| C6 | MYC O1 | Drop "G1/G0 in wild type"; state MYC-phase correlation about +0.2 for S in the knockout, near zero in wild type, no error bars or markers on Figure 4C, near-superimposed density curves. |
| C7 | MYC O2 | Add locator entry 2 (and its Figure 5F qualifier, plus entry 25) for the composition clause. |
| C8 | MYC O3 | "does nothing for the layer markers" to "no significant change in SATB2 or CTIP2 (n small; CTIP2 remains below wild type)"; `readout_level` "functional" to a cellular readout; add NEUN+ rise (about 6 to 18 percent). |
| C9 | ISR counter_evidence line 3 | State the adverse-event burden in the vanishing-white-matter dataset (serious adverse events in about three quarters of 33 children, hallucinations in over half) and that guanabenz is not an eIF2B activator; add the PERK/pancreas locator or mark abstract-level/unlocated. |
| C10 | ISR / MISSENSE / EXCITATORY / NEUROINFLAMMATION | Either add an OTHER_DISEASE_PRECEDENT observation with locator for each precedent the need relies on, or drop the scope from the need-level list; same for UNVERIFIED_HYPOTHESIS on PDH and MTOR (document the premise as an observation or remove it). |
| C11 | ISR O2 | Add SESN2 down; add that three per-gene directions had been seen before the sets were fixed. |
| C12 | PDH O1 `evidence_scope` | WWOX_BIOLOGY_OTHER_CONTEXT (consistent with O2 and its own limits). |
| C13 | PDH counter_evidence | Add: in the human fibroblast knockdown line cytoplasmic HIF1alpha is decreased in two of four conditions (manifest 35328751 entries 9, 11), opposite to the MEF sign; re-supply raises lactate in two conditions (entry 2). |
| C14 | GABA O1 | Narrow the universal negative to "in the sources read for this table" or cite a bounded search. |
| C15 | GABA O2 | Add the ratio values (0.13-0.29 versus 0.29-0.30) and that no knockout is higher; GAD1 about ten-fold different. |
| C16 | PTC O1 `statement` | Replace "no enumeration of nonsense alleles in the record" by "no systematic enumeration with stop-codon identity and +4 nucleotide"; list the stop-gain allele in the severe case (DL-MOL-007) and the in-repo read-through-candidate remarks as non-evidence. |
| C17 | EXCITATORY O3 | Remove the sEPSC-small/mEPSC-up asymmetry or give the mEPSC values; cite manifest entry 18 (both panels separate by a sliver, one asterisk each) and the pooled-event test. |
| C18 | EXCITATORY O4 | Delete "selective" for the pannexin-1 blocker. |
| C19 | EXCITATORY inferred | Add that 4 of the 15 comparator variants are called non-pathogenic by the authors. |
| C20 | PDH targets pathways | Cosmetic: GO:0006096 label "glycolytic process". |

## 6. Limits of this audit

- 8 of 22 needs opened; 14 not audited, including the other gene-restoration needs (splice, missense, endogenous boost), so no claim is made about them.
- HGNC and GO identities were checked against my own knowledge, not against the HGNC snapshot (not in git) or QuickGO (no network use here): UNVERIFIABLE offline rather than confirmed.
- Figure readings are those attested in the manifests (some of which were themselves blind-audited); I did not re-render source figures.
- Abstract-level other-disease precedents were checked against the cards, not against the papers.
- The negative searches (no read-through experiment; no E_GABA measurement) cannot be re-run offline.
