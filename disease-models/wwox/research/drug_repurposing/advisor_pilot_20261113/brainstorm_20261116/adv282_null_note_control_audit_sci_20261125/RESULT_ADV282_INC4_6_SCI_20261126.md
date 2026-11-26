# RESULT, ADV-282 increments 4 to 6: null-note audit, queue ranks 25 to 48 (SCI, 2026-11-26)

Hypothesis level; reference genotype class; nothing here is medical advice. Session 7f7fcdaa (claude-sonnet-5-5, effort high, read back from the census: 89 of 89 turns). Frozen before any source of each increment was opened: `PREREG_ADV282_INC4_SCI_20261126.md` (sha256 ffdac3ce...), `PREREG_ADV282_INC5_SCI_20261126.md` (1a0734d3..., with an addendum written before any source), `PREREG_ADV282_INC6_SCI_20261126.md` (4511ed78...). First readings frozen before each blind report: `FIRST_READ_ADV282_INC4/5/6_SCI_20261126.tsv` (bb199685..., 3f976ba5..., 0b97de9f...). Blind readers (legend-delegate, sonnet, effort high stated in each dispatch, read back from each delegate transcript: inc 4 35 of 35 turns, inc 5 18 of 18, inc 6 10 of 10, all claude-sonnet-5-5 and effort high): reports verbatim in `BLIND_REPORT_ADV282_INC4/5/6_SCI_20261126.md`. Packets: the repository sentence plus the whole held source (`BLIND_SENTENCES_ADV282_INC4/5/6_SCI_20261126.md`). Files viewed with sha256: `FILES_VIEWED_ADV282_INC4_6_SCI_20261126.tsv`. Receipts are not written (targeted checks).

ADV's rule applied: **only blind-confirmed MUST CHANGE that I verified against the original are counted as MUST CHANGE**; strict, loose and ADD are labelled separately; first-reading counts are not results.

## 1. Population, deviations

* 24 rows (ranks 25 to 48, three increments of 8). Read: 22. Not read: **DR-L01-003** (Sheeni 2026; bytes not held, one Europe PMC fullTextXML request returned HTTP 503, a route result, NOT ASSESSABLE) and **DR-H02-005** (set aside: note blind-checked by ADV-287 on 2026-11-25). 24 minus 2 = 22 read (8 + 7 + 7).
* **Abstract rows.** 13 of the 24 were labelled abstract-only. Their abstracts (and one extra) were fetched once through NCBI efetch (plain request, no e-mail, no key) and saved with sha256 under `files/fulltext/adv282_abstracts_sci_20261126/`; two of the rows had held bytes the cards did not use (a full text of Wang 2026, a PMC page of Briggs 2014). An abstract's silence is NOT ASSESSABLE (a clause added to the frozen rule in PREREG 4, before any source).
* **Rule deviation in dispatch.** Readers 4 and 5 were dispatched with the PREREG wording (a dose-response of the same compound counts as an engagement readout); the reader of increment 6 got one clarifying phrase (an effect of the same compound on the study's own outcome endpoint is not an engagement check). Readers 4 and 5 mostly classed such rows PRESENT BUT NOT MATCHED or ABSENT on the stricter reading anyway (DR-H02-008, DR-W2-004), so the counts are close, but the three increments are not exactly one rule.
* Sealed or frozen material untouched; the Obeid 2026 article was not opened.

## 2. Classes (blind reader, main manipulation; first reading in brackets where it differs)

Increment 4:

| id | class | blind verdict | verified MUST CHANGE |
|---|---|---|---|
| DA-L01-005 | PRESENT for the knockout; **ABSENT for NAC** (no DHE group under NAC, Fig 6a; I viewed Fig 6) | ADD | no |
| DR-A02-010 | NOT MATCHED | ADD (first reading: MUST CHANGE) | no, held apart (3.2) |
| DR-A01-007 | **ABSENT** | MUST CHANGE | **yes** |
| DR-A02-006 | PRESENT | ADD (first: STANDS) | no |
| DR-A02-007 | NOT MATCHED | ADD | no |
| DR-B01-002 | PRESENT (FA-A, 24 h); NOT MATCHED for DEB and the FA-C micronuclei | MUST CHANGE | **yes** |
| DR-P9-009 | **ABSENT** | ADD | no |
| DR-E01-002 | NOT MATCHED (citation of the earlier phase 1B) | ADD (first: STANDS) | no |

Increment 5 (DR-L01-003 not read):

| id | class | blind verdict | verified MUST CHANGE |
|---|---|---|---|
| DR-E01-003 | PRESENT (abstract reports p-eIF2alpha; a proxy upstream of the target) | ADD | no |
| DR-W2-004 | NOT MATCHED (citation only for both drugs) | MUST CHANGE | **yes** |
| DR-H02-008 | NOT MATCHED (citation; first reading PRESENT on the dose-response) | MUST CHANGE | no, held apart (3.2) |
| DR-H02-023 | NOT ASSESSABLE (abstract) | MUST CHANGE | no, held apart (3.2) |
| DR-H02-024 | NOT ASSESSABLE (abstract) | ADD | no |
| DR-H02-036 | NOT ASSESSABLE (abstract) for the muscimol null; GABA-B arm PRESENT | MUST CHANGE | **yes** (one clause) |
| DR-H02-030 | NOT ASSESSABLE (abstract) | ADD | no |

Increment 6 (DR-H02-005 set aside):

| id | class | blind verdict | verified MUST CHANGE |
|---|---|---|---|
| DR-I01-006 | PRESENT (abstract: plasma clearance of DCA fell) | ADD | no |
| DR-I01-001 | NOT MATCHED (abstract does not give dose, cohort, tissue) (first: PRESENT) | ADD | no |
| DR-I01-002 | NOT MATCHED | ADD | no |
| DR-I01-004 | NOT MATCHED | ADD (the word 'only' is UNSETTLED) | no |
| DR-I01-014 | PRESENT | MUST CHANGE | **yes** |
| DA-K01-007 | PRESENT (Wwox transcript lower in all four contrasts; only about 3-fold with overlapping values in cortex) | ADD | no |
| DR-P9-010 | NOT ASSESSABLE (label) | ADD | no |

## 3. Scoring against the PREREGs (under the one rule, blind counts)

| | assessable | strict (ABSENT) | loose (ABSENT or NOT MATCHED) | blind MUST CHANGE | verified MUST CHANGE | ADD |
|---|---|---|---|---|---|---|
| inc 4 (8 rows) | 8 (predicted 6 to 7) | **2** (pred 1, range 0 to 3: within) | **5** (pred 3, range 1 to 5: top edge) | 2 (pred 2, 0 to 4: within) | 2 | 6 |
| inc 5 (7 read) | 3 (pred 3, 2 to 5: within) | **0** (pred 1, 0 to 3: within) | **2** (pred 2, 1 to 4: within) | 4 (pred 1, 0 to 3: **above**) | 2 | 3 |
| inc 6 (7 read) | 6 (pred 3, 1 to 5: above) | **0** (pred 1, 0 to 3: within) | **3** (pred 1, 0 to 3: top edge) | 1 (pred 1: within) | 1 | 6 |
| total 22 read | 17 | **2** | **10** | **7** | **5** | 15 |

* **Rejecting observation for increments 4 to 6** (blind MUST CHANGE 3 or fewer of the 22 read): **not met** (7 blind, 5 verified). The null-note wording class is still paying: 5 of 22 verified (23 percent), 7 of 22 blind (32 percent); across ADV-281 and ADV-282 the blind reader gave MUST CHANGE 2 of 13, 9 of 22 and 7 of 22 (18 of 57, 32 percent).
* Strict stays low (2 of 17 assessable) and both strict rows are rows with no engagement readout by construction (a butyrate comparator in HEK cells; a memantine clinical cohort). Loose (10 of 17) is driven by rows whose engagement is a citation, or an abstract that does not give dose and cohort.
* Error classes of the five verified MUST CHANGE: a wrong object of an attribution (DR-B01-002), a claim the held numbers cannot carry (DR-A01-007, a lower bound of 2 mM against 5 mM applied), a generalisation that a figure contradicts at one dose (DR-W2-004), an inference beyond two abstracts (DR-H02-036), and a statement made true of one readout and stretched to all (DR-I01-014).

### 3.1 Verified MUST CHANGE (each checked by me on the original; consumers named)

1. **DR-A01-007** (card A01; 3 study units; 3 files name the id). The note says butyrate 'does not engage HDAC6 at the applied level'. The only butyrate HDAC6 value held is `IC50 > 2,000,000 nM` (`missense_recovery_it5_p8_20261029/hdac_enzyme_potency_chembl_20261029.tsv`, row 25, CHEMBL1680140/CHEMBL1671826), against 5 mM applied (Guiberson 2018 Supp Fig 12a, HEK293T, n = 3, rendered and measured: G544D with sodium butyrate about 1.0 of control, unmarked; WT about 1.95, unmarked). A lower bound below the applied level says nothing about engagement at 5 mM. The paper has no HDAC or histone-acetylation readout (query 2026-11-26: 'HDAC|acetylat|butyrat' over the article and the supplement text: none beyond the screen list). Replace by: 'its HDAC6 potency is only known as above 2000 micromolar, below the 5 mM applied, so HDAC6 inhibition at that level is neither shown nor excluded; no HDAC engagement was measured in this paper'.
2. **DR-B01-002** (card B01; 2 units; 5 files). The last clause ('the effect that was seen is attributed ... to TBK1/IKKe inhibition, not read-through') names no effect. In Hristodor 2025 the effect so attributed is the p53 fall (about 40 percent, FA-A, Fig 2D, n = 10) and the pSTAT2 fall (about 50 percent, Fig 5C, n = 5), by the authors' hypothesis with no direct TBK1 readout; the FANCA full-length induction (under 5 percent to about 9 percent of control, FA-A, Fig 1C) is treated by the authors as read-through ('both ... should induce translational read-through'). The blind reader adds that the note never says the comparator ataluren did rescue (MMC survival, DEB aberrations, FANCC micronuclei minus 27 percent). Replacement (blind wording, checked against the held XML): amlexanox 25 micromolar induced full-length FANCA from under 5 to about 9 percent of control in FA-A cells (ataluren about 11 percent), not FANCF, and did not rescue FANCA mRNA; no improvement of MMC survival (n = 3), DEB aberrations (FA-A, up to 3 weeks) or FA-C micronuclei, whereas ataluren improved all three; p53 fell about 40 percent and pSTAT2 about 50 percent, which the authors attribute to TBK1/IKKe or NF-kB inhibition rather than read-through (hypothesis).
3. **DR-W2-004** (card F01; 2 units; 4 files). 'Memantine accelerated every seizure stage': Fig 3A (viewed): 5 and 25 mg/kg carry an asterisk on all four stages; 1 mg/kg on stages 1 and 2 only, none on stages 3 and 4; Fig 3B (stage 4): 5 mg/kg two stars, 25 mg/kg three stars, 1 mg/kg none. The paper's own text says 1 to 25 mg/kg shortened each stage; its figure does not. Replace by: 'memantine 5 and 25 mg/kg shortened latency to all four stages (stage 4 about 26 and 25 min against about 37 in controls, bar readings, n = 8 per group by the ANOVA df); 1 mg/kg stages 1 and 2 only'. From the blind report only (not checked by me): perampanel seizures still occurred in 7 of 8 at 1 mg/kg; the article has internal inconsistencies in n (14 in Methods, 8 implied by the df) and in the control data (listed in the blind report); no in-study engagement readout for either drug.
4. **DR-H02-036** (card H02; 2 units; 2 files). 'The axis therefore has opposite signs by receptor class' is not in either abstract: they report GABA-B agonism as positive and say none of the culture effects is mediated by the GABA-A agonist muscimol (no effect, not an opposite sign). Replace by: 'the two receptor classes differ (positive with the GABA-B agonist, no effect with muscimol in the purified-OPC culture); no opposite sign is reported in the abstracts'. The first clause ('did not reproduce the effect in the coculture study') is **UNSETTLED**, not verified: the abstract's 'None of these effects are mediated by the GABAAR agonist muscimol' can include the coculture effect; the full texts are not held.
5. **DR-I01-014** (card I01; 2 units; 0 files). 'The response to the PDK inhibitor depended on a pre-existing PDH defect': the abstract reports a shift of about 40 percent of carbon flow toward PDC in all cells, controls included, a 29 percent fall of average glycolysis only in patient cells (one splicing-mutation line excluded; five healthy subjects, six patient lines), and no change in lactate production or NTP/NDP in either cell type; no genotype-by-DCA interaction test is reported (blind reader). The endpoint line 'lactate production' with direction DECREASE is contradicted by the abstract. Replace by: 'DCA shifted flux toward PDC by about 40 percent in all cells, and decreased average glycolysis by 29 percent in patient cells (one line excluded) but not significantly in controls; lactate production did not change in either cell type; no interaction test'.

### 3.2 Held apart, not counted

* **DR-A02-010** (first reading MUST CHANGE, blind ADD). Both readers found the same two defects, which I checked in the original: 'low exposure' is 2.1 mg/kg/day for 7 days, about 14.7 mg/kg total, about equal to the 15 mg/kg over 24 hours that rescued S466L in Fig 1 (the rate is seven times lower); 'tolerated' is not shown for this arm (no weight, blood count or clinical record for low-dose carfilzomib). The Results say no significant change in tHcy or activity, the Discussion 'only a slight increase in liver CBS activity'. The blind reader graded this ADD. Sentence for IT, offered as ADD with these two facts.
* **DR-H02-008** (blind MUST CHANGE on the ambiguity of 'CPP-115 only, not vigabatrin', which the blind reader reads as possibly meaning vigabatrin did not reduce spasms; vigabatrin was not tested in this paper). The sentence is an ambiguity, not a false statement: ADD. Facts to add (held full text, PMC page): 0.1 to 1 mg/kg/day reduced spasms only transiently (PN5 to 7), 5 mg/kg/day was lethal, hippocampal sclerosis scores equal across groups (23 brains, P 0.69), no white-matter or myelin histology.
* **DR-H02-023** (blind MUST CHANGE on 'a negative in people who were not infants', since the note says ages are not stated). The PubMed record's MeSH list for 1940119 carries Child, Adolescent, Adult, Middle Aged, Aged and no Infant heading (checked in the XML); the claim has indexing support the note does not name. ADD: name the basis (MeSH, not the abstract text), the ten untreated comparison cases, and that the overlap of the five specimens with the 62 is not stated.
* **DR-H02-036 first clause**, **DR-I01-004 'only'** and 'the full text is closed': UNSETTLED (need a dated search or the full text).
* Own errors (in the first readings): DR-A02-010 graded MUST CHANGE where the blind reader graded ADD; DA-L01-005 missed that NAC lowered no measured ROS in the paper (the NAC check is ABSENT, blind finding, verified on Fig 6a); DR-A02-006, DR-E01-002 and DR-I01-001 graded too mildly or too generously in class (see the tables); I classed a dose-response on the study's own endpoint as an engagement check in DR-H02-008 and DR-W2-004 (the rule text allowed it; see section 1); my first reading called the muscimol 'coculture' clause MUST CHANGE where the abstract is ambiguous; the DA-K01-007 pseudocount (0.01) put the cortex Hif1a at -0.21, outside 'within 0.2' (0.1 gives -0.20).

## 4. Sentences for IT (card owner), ADD only (verified MUST CHANGE are in 3.1)

DA-L01-005 (L01, 4 units): the microarray is Wwox+/- against Wwox-/- (one column each, not wild type, no n or test; Supp Fig 8 PDF page 15), ROS is one representative DHE histogram per genotype without quantification, NAC was present from isolation (prevention) and no NAC group was measured for ROS. DR-A02-010 (A02): see 3.2. DR-A02-006 (A02): proteasome inhibition was confirmed in T191M (Fig 4D by text) and CBS protein rose, yet activity did not; the HEK gain (259 percent of vehicle, Mijatovic Fig 6b) is from an essentially zero baseline with signs of cell damage. DR-A02-007 (A02): the authors say the tHcy fall (345 to 179 micromolar against day 0, no vehicle arm) may be handling, the activity null may be assay sensitivity, one animal was moribund, a bimoclomol arm adds nothing. DR-P9-009 (F04; full text held, so 'abstract only' is stale): elderly adults with cognitive impairment, median age 63, patient-chosen add-on 10 mg/day, 24 weeks, 7 of 101 against 5 of 110 increased seizure frequency, baseline imbalances, no drug level. DR-E01-002 (E01): 'no evidence of slowing' (interval 0.83 to 1.32), engagement is the earlier trial's. DR-E01-003 (E01): 5xFAD, 10 mg/kg/day i.p., 23 days, donepezil arm, authors call the effects limited, p-eIF2alpha is upstream of the target. DR-H02-024 (H02): vigabatrin 500 and GABA 1000 nmol/ml (not equimolar), vigabatrin seemed slightly more toxic, degenerating fibres and gliosis in both, preliminary data. DR-H02-030 (H02): the 668 are those re-reviewed, children and adults together; infants 22 against 4 percent in the same study. DR-I01-006 (I01): DCA 12.5 mg/kg every 12 h blunted the postprandial lactate rise, ages 0.9 to 19 years, 11 PDH deficiency, 25 respiratory chain, 7 mtDNA. DR-I01-001, -002, -004 (I01): the PDH assays are in chronic-stage pilocarpine mice (dose and cohort not in the abstract), partial engagement; 50 and 100 mg/kg/day; drop or date 'the only'. DA-K01-007 (K01): n 2 to 4 per arm; Wwox falls 7- to 16-fold in the three hippocampal contrasts but only about 3-fold with overlapping values in cortex; say 'no consistent elevation' (Hk2 +0.15 and +0.35, Hif1a +0.06 in single contrasts); the sentence's numbers reproduce at pseudocount 0.1 on mean summed transcript TPM per symbol (`recompute_k01_007_adv282.py`, blind reader's own script). DR-P9-010 (F04): two studies (Study A parallel placebo-controlled, memantine 54 against placebo 53; Study B randomised withdrawal, 471 patients), the label also says the paediatric safety profile matched adults; the one label held is one of 75 openFDA records.

## 5. Limits

Gupta 2023 figure images and S1 File, Hristodor supplementary figures and the CPP-115 supplement are not held: statements resting on them are by text and legend only. Abstract-level rows (13) give NOT ASSESSABLE unless the abstract reports a readout, so the class counts for those rows are weaker than the full-text rows. One blind reader per increment, not recomputed by a second one except where a number is quoted above as mine. DR-L01-003 and DR-H02-005 not read. No note was edited; card edits are IT's.

## 6. Carry forward (EMPATHY)

* A figure can contradict the paper's own text at one dose (DR-W2-004): when a note generalises over doses, read the per-dose marks, not the text.
* A lower-bound potency ('> 2 mM') cannot support 'does not engage' at a higher applied level.
* An attribution needs its object named ('the effect that was seen').
* Abstract-level null notes are mostly faithful to their abstracts and fail by omission (15 ADD) and by inference (the 'opposite signs' and 'depended on' clauses).
* Next in the queue: none of ranks 25 to 48 remains except DR-L01-003 (retry the Europe PMC route once later) and DR-H02-005 (set aside). H02/A01 second random 20 (ADV-287) is next.
