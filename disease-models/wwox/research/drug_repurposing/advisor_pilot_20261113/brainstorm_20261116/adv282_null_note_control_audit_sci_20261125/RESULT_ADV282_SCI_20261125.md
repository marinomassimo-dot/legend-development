# RESULT, ADV-282: positive-control audit of the queued null-wording card notes, increments 1 and 2 (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Session ae0002e7 (claude-sonnet-5-5, effort high, read back from the census). Rule and predictions: `PREREG_ADV282_INC1_SCI_20261125.md` and `PREREG_ADV282_INC2_SCI_20261125.md` (both written before any source of their rows was opened); ordered queue: `queue_ordered_adv282.tsv` from `step0_list_adv282.py`; first readings: `FIRST_READ_ADV282_INC1_SCI_20261125.tsv`, `FIRST_READ_ADV282_INC2_SCI_20261125.tsv`; blind readers (legend-delegate, sonnet 5.5, effort high, read back from each delegate's transcript; given only the verbatim sentence and the held-source paths): `BLIND_REPORT_ADV282_INC1_SCI_20261125.md`, `BLIND_REPORT_ADV282_INC2_SCI_20261125.md`; files viewed with hashes: `FILES_VIEWED_ADV282_INC1_2_SCI_20261125.tsv`. Parts (A) and (C) of the brief were done by the previous window (RESULT_ADV281 section 8, `equivalence_rows_adv281.tsv`).

## 1. Population, order and one deviation

* The 48 queued NULL rows of ADV-281 are all still on today's cards; no note text changed. One new route hit, DR-A02-001 (an ADV-279 rewording on an INCREASE row about weak measurement), is not a null result and is not added. Order: units that carry the row's study by HE's `consumer_count.py` (union over the PMIDs named in the row's `source`), then files naming the id, then id. Six rows of GSE156243 tie at 43 units.
* **Deviation: ranks 7 and 8 (DA-W2-011, DA-I01-006) were not audited.** A safety classifier stopped the session's response as the extraction of their source article (Obeid 2026, PMID 42422765) was starting. It was not retried, rephrased or handed to a peer; ADV agreed (message of 2026-11-25) and put it on the operator list. Both stay queued by id with the reason "classifier stop". No other row of the queue has that article as its only source.
* Audited: increment 1, ranks 1 to 6 (six rows of the deposit GSE156243); increment 2, ranks 9 to 16 (eight rows). 14 rows. The other 34 stay queued by id: DA-W2-011 and DA-I01-006, and ranks 17 to 48 of `queue_ordered_adv282.tsv`.

## 2. Classes (14 rows; first reader and blind reader shown)

Delegates: increment 1 blind reader, claude-sonnet-5-5, effort `high` on 23 of 23 turns, 59,704 output tokens, 2.80 million cache-read; increment 2 blind reader, claude-sonnet-5-5, effort `high` on 60 of 60 turns, 52,116 output tokens, 5.92 million cache-read (census of each delegate transcript). Each saw only the verbatim sentence and the held-source paths.

| id | first reader | blind reader | in-study check | sentence (blind) |
|---|---|---|---|---|
| DA-GSE-PDK-003 | PRESENT | PRESENT | yes | MUST CHANGE |
| DA-L01-003 | PRESENT | PRESENT | yes | MUST CHANGE |
| DA-W2-012 | PRESENT | PRESENT | yes | MUST CHANGE |
| DA-J01-007 | PRESENT | PRESENT | yes | MUST CHANGE |
| DA-K01-002 | PRESENT | PRESENT | yes | ADD |
| DA-I01-001 | PRESENT | PRESENT | yes | ADD |
| DA-J01-006 | PRESENT (weak) | PRESENT | yes | ADD |
| DA-K01-008 | PRESENT (manipulation) | NOT MATCHED for the knockdown, effect present, reporter responsiveness ABSENT | knockdown effect yes; reporter no | ADD |
| DA-M01-002 | PRESENT | PRESENT | yes | MUST CHANGE (blind; I viewed Fig 1F and confirm) |
| DA-W2-002 | PRESENT | NOT MATCHED (protein loss not in this paper; effect in the same cells) | effect yes; protein loss no | ADD |
| DA-J01-008 | PRESENT (the allele acts in one copy) | ABSENT for the heterozygote glia readout | no for the readout | STANDS (first reader: ADD) |
| DA-J01-002 | PRESENT (same-knockout effects) | NOT MATCHED | partial | ADD |
| DA-M01-007 | PRESENT (O-KO partial) | PRESENT | yes (representative images) | MUST CHANGE |
| DA-L01-001 | PRESENT | NOT MATCHED | partial | ADD |

Where the readers differ (five rows of increment 2), the cause is the ADV-281 rule again: the first reader counted an effect of the same manipulation in the same preparation as the check (PREREG); the blind reader asked for loss of the target or a matched positive control and graded NOT MATCHED when loss is shown only in another paper (Breton 2021, Hussain 2019), at another age (Lucas-Clarke Supp Fig 1) or not at all. The in-study column agrees everywhere except DA-J01-008 and the reporter of DA-K01-008, which is the robust column. **For the six deposit rows the check is present on both readings**: protein loss in the same lines' organoids at weeks 6, 10 and 24 (Fig EV1B, Fig 1A-B, Fig EV2A-B; I viewed the rendered Fig EV1 page, ev1.png in the files-viewed table; Fig 1A-B and EV1E are named in the Results), plus 2,267 other differentially expressed genes in the sequenced week-15 libraries; the sequenced libraries themselves are not checked and the WWOX transcript is not lower (1.39 times; an exon-1 frameshift), so the deposit cannot show the loss by transcript.

## 3. Scoring against the PREREGs

Increment 1 (six rows):

* P1 strict, predicted 1 of 8, range 0 to 2: **0 of 6** (both readers). Within.
* P2 loose, predicted 2 of 8, range 1 to 4: **0 of 6** (both readers). Just below the range (scaled to six rows: 1.5, range 0.75 to 3).
* P3 blind MUST CHANGE, predicted 1 of 8, range 0 to 3: **4 of 6**. Above the range.
* P4 MUST CHANGE or ADD, predicted 6 of 8, range 4 to 8: **6 of 6**. At the top.
* P5 deposit rows with a printed statement that does not reproduce, predicted 1 of 6, range 0 to 3: first reader 2 (DA-L01-003, DA-J01-007); blind reader 3 to 4 (adds the P 0.22 of DA-GSE-PDK-003, which the blind reader could not reproduce from an unnamed set and which I reproduce with the repository's own script, and "nominally" for PDGFRA). Within on the first reading.

Increment 2 (eight rows):

* P1 strict: first reader **0 of 8**, blind reader **1 of 8** (DA-J01-008, the heterozygote glia readout); range 0 to 2. Within.
* P2 loose: first reader **0 of 8**, blind reader **5 of 8** (DA-K01-008, DA-W2-002, DA-J01-008, DA-J01-002, DA-L01-001); predicted 2, range 1 to 4. The two readers bracket the range.
* P3 blind MUST CHANGE, predicted 2 of 8, range 0 to 4: **2 of 8** (DA-M01-002, DA-M01-007). Within.
* P4 MUST CHANGE or ADD: **7 of 8**, predicted 6, range 4 to 8. Within.
* P5 not assessable: 0. Within.

**Rejecting observation** (loose 3 of 14 or fewer over the two increments: genetic and transcript nulls are mostly checked): first reader loose 0 of 14, **met**; blind reader loose 5 of 14, **not met**. It depends on the matching rule. The robust reading: an effect of the same manipulation in the same preparation is present in 13 of 14 rows (all but DA-J01-008, whose readout has no held data); loss of the target is shown in the same paper and preparation in the six deposit rows and in DA-M01-007, DA-M01-002 and DA-K01-008 (at another age), and is not shown in the paper for DA-W2-002, DA-J01-002 and DA-L01-001. Consequence for IT's card-template decision: a single "positive control" field would not discriminate among these; if a field is added, the useful one is **where the target-loss or engagement check sits** (same preparation and time / same paper, other time / another paper / none), which splits exactly these cases.

Over both assignments (ADV-281 and ADV-282), sentences judged by a blind reader: MUST CHANGE 2 of 13 and 6 of 14 (8 of 27); MUST CHANGE or ADD 12 of 13 and 13 of 14 (25 of 27). The null-note wording is a real defect class in the genetic and transcript rows too, even where the knockout check is present: the errors were in the compressed description of the source, not in the check.

## 4. Sentences for IT (card owner): verified errors first

Wording (replacement or added clause) is in each blind report under the id and in the first-reading tables; the ones that matter most:

1. **DA-L01-003.** "Only NFE2L2 is in the authors' DE list" is false: **G6PD is in the deposited down list (p 3.15E-04, adjusted p 7.15E-03, log2FC -0.42)**, and so are GSTP1 (4.38E-03) and PRDX1 (2.44E-02), both lower. The lists are cut at nominal P below 0.01 and fold change above 1.2 (maximum adjusted p 0.0684), which is why NFE2L2 (adjusted p 1.43E-02) is in them above the stated alpha of 0.01. "No cytokine-expressing compartment" says more than the counts show (IL1B, IL6, TNF 0 to 11 counts, but TGFB1, MIF, IL33, CSF1 are expressed and AIF1 and CD68 are detectable; I confirmed on the table). HMOX1, SRXN1 and GSR are higher on group means in 3 of 4 knockout libraries, not 4 of 4. The sentence names no criterion for "no coherent NRF2 signature".
2. **DA-J01-007.** "Of seven reactive-pan genes above 5 CPM" is false for SERPINA3 (0.95 and 2.34 CPM) and C3 (4.56 and 3.50); the panel has ten genes, two not informative, and the declared rule (all four knockout beyond both wild type and at least 1.5-fold) leaves STAT3 (1.46 times, higher in all four, **in the authors' up list, adjusted p 5.74E-03**) as "not separated" only by the fold cut. TMEM119 (3.83 times) and AIF1 (7.6 CPM) are not named; GFAP RNA is not raised (0.88) while the article's own GFAP immunofluorescence is. "VIM and CD44 radial-glia or progenitor associated" has no held source; the blind reader's direction check, not recomputed by me, in an unperturbed spheroid time course (GSE150123, other laboratory) has CD44 rising with culture age (rho +0.92), not checked by me.
3. **DA-M01-007.** "The Synapsin-Cre survival age is not stated" is false: the Results (both held copies) and the abstract say S-KO die by 3 to 4 weeks (Fig 1I, S-KO n = 15). "Oligodendrocyte and astrocyte deletion do not [reproduce seizures]" has no data: only delay, weight and survival (and hind-limb clasping for O-KO) were measured; the authors write "no phenotype abnormalities". Olig2-Cre deletion is partial in the single image shown (Supp Fig 1E).
4. **DA-M01-002.** "SCAR12 is the clean dissociation case" does not hold: **Fig 1F (week 7, immunofluorescence) shows SCAR12 SOX2+ cells up (median about 48 against about 13 percent) and SATB2+ cells down (three stars)**, which I viewed on page 32 of the accepted manuscript; the wild-type-like fractions are the week-16 scRNA-seq and CTIP2/SATB2. "Overlaps the wild-type lower tail" is reversed (SCAR12's lower whisker reaches into the wild-type upper half); the plotted points outnumber the organoids (n 7, 5, 8, 11) and the unit is not stated.
5. **DA-W2-012.** "PDGFRA nominally higher" understates it: higher in all four knockout libraries (8.8 times) and in the authors' up list (adjusted p 6.55E-03); MBP (1.79 times, up list) and PLP1 (1.88 times) are also higher, so "counts are very low" is not true of the lineage; "a week-15 organoid has no compact myelin" has no held source.
6. **DA-GSE-PDK-003 and DA-I01-001.** The two PDK1 values reconcile: -0.34 is log2 of (mean CPM + 1), -0.39 is the median-of-ratios-normalised ratio (the blind reader reproduced both). The "LDH-to-PDH ratio not shifted" is the log2 of (LDHA+LDHB) over (PDHA1+PDHB+DLAT+DLD), KO minus WT -0.138 (I reproduced it with the repository script) but it depends on the pairing (LDHA over PDHA1: three of four knockout libraries below both wild types); PDHA1 (2.02 times, adjusted p 5.75E-10), LDHA (1.70) and **PDK3 (1.55 times, all four knockout above both wild type, nominal P 7.39E-03, adjusted p 5.65E-02)** are higher and the set mean (+0.17, P 0.2265 on rerun of the repository's own set test, printed 0.22; the blind reader's sets gave 0.48 to 0.55, the set is not named in the sentence) averages them away from PDK1. "No support for a raised PDK" is therefore not a statement about PDK3.
7. **ADD only:** DA-J01-006 (species: the microglia clause is the wild-type rat, the astrocyte deletion the mouse; the n of 8 and 9 belongs to the weight and appearance panels; the authors' "not excluded" is "in other neurological disorders"); DA-K01-008 (P 0.5185 fits 7 plus 9 brains at 14 df; the genotype table shows no UAS element, so "driver-expressed" rests on the Methods name; four ROIs of about 415 square micrometres per brain; no control shows the reporter can move; the authors say Atf4 "could be" the mechanism); DA-W2-002 (the heterozygote already differs from wild type in amplitude, KS p 1.98e-04, and frequency, p 0.0018, so the knockout-against-wild-type frequency difference is not a knockout effect; isolation of mEPSCs is TTX only); DA-J01-002 and DA-L01-001 (the figure readings 1.48 and 1.85 times cannot be checked: **the figure image is not held** (folders empty on 2026-11-25; PMC open-data bucket lists no figure; Europe PMC image route 403, NCBI route 404) and they sit slightly against the text's "more than 1.5 fold" for both); DA-J01-008 (STANDS; the heterozygote's age, n and metric are not given); DA-K01-002 and DA-I01-001 (normalisation labels).

Consumers that lean on these notes (leads, not a complete list): DA-L01-003 and DA-L01-001: `L01_nrf2_axis.packet.json`, `nrf2_it11_p23_20261031/README.md` and `l01_corrections_proposal.md` (the origin of "only NFE2L2" is item 5 of that proposal and README line 32, which searched NFE2L2, NQO1, HMOX1, KEAP1, IL6, IL1B and TNF and did not search G6PD); DA-J01-007, -006, -008, -002: the J01 card and packet; DA-M01-007: `M01_neurogenic_output_myc_window.packet.json` and `COVERAGE_MATRIX_EEG_BY_AGE_IT_20261125.md` (also names DA-J01-006 and DA-W2-002); DA-GSE-PDK-003: `knowledge_contribution_trial_20261027/answer_b.md`; DA-I01-001 and DA-K01-008: their READMEs and `build_packet_k01.py`.

## 5. Not done, and limits

* DA-W2-011 and DA-I01-006 (classifier stop, above) and ranks 17 to 48 of the queue are not audited; they stay queued by id in `queue_ordered_adv282.tsv`.
* Hussain 2019 Fig 4E (DA-J01-002, DA-L01-001) and Fig 6D: the image is not held; the Il6 and Tnf-a readings remain by-eye readings of a figure no longer in the files folder.
* The class column reflects two readers who disagree on a rule; both are shown. The blind readers saw only their paths, but the first reading came first and fixed my own sentences before they returned (frozen files, hashes in the folder's commit).
* GSE150123 comparisons are the blind reader's, one reader, not recomputed by me. Receipts are not written: targeted checks, not completed reads.

## 6. Carry forward (EMPATHY)

* A knockout-against-wild-type null can have its check present and its sentence still wrong: all four hard errors of increment 1 were descriptions of what a list contains or what a threshold selects, repeated from an earlier reading without searching the list again (the G6PD miss came from a search keyed to the genes of the question).
* When a sentence names membership in "the authors' list", search every gene the sentence mentions against the deposited list and say what the list's cut was (nominal P, fold, adjusted p).
* A figure that was read by eye once may no longer be held; record the hash or say the image is gone.
* Candidate direction (queued, not run): the PDK isoform pattern (PDK1 down, PDK3 up) in the other WWOX-deficient neural transcript datasets, against the dichloroacetate isozyme potencies in HE's batch 8 sheet (one assay: PDK1 1.03, PDK2 0.50, PDK3 5.56 mM); prior art: `adv095_selection_sci_20261119/out/gene_values.tsv` (PDK3 row of an organoid dataset, different values and transform, not reconciled here) and `case_it9_p6_hif_axis_20261030`. Rejecting observation: PDK3 not higher in a second independent WWOX-deficient neural dataset. Consumers: cards E03 and I01 and HE's dichloroacetate sheet.

## 7. Addendum (2026-11-25, after ADV's reading of this result)

* **The yield is MUST CHANGE**: 4 of 6 and 2 of 8 here (6 of 14), 2 of 13 in ADV-281; about a third of the audited null-note sentences need a change. "MUST CHANGE or ADD 25 of 27" in section 3 is reported but is not a yield: ADD fires on almost every sentence.
* **Matching rule.** The loose rate depended on the rule (0 of 14 by the first reading, 5 of 14 by the blind reader). The next audit defines one rule in its PREREG before any reading and gives both readers' counts under it only.
* **Unit and n of the PDK3 1.55 times (checked before the next strand starts).** Ratio of the mean CPM of the four knockout libraries (10.47) to the mean CPM of the two wild-type libraries (6.77), human WiBR3 cerebral organoids at week 15, one library per replicate. Raw counts: knockout 425, 394, 455, 322; wild type 263, 194; library totals 38.73, 41.15, 38.21, 34.21, 37.26 and 29.98 million. All four knockout libraries are above both wild-type libraries; the deposited list gives nominal P 7.39E-03, adjusted p 5.65E-02, log2FC 0.55. Two wild-type libraries only, so no rank test can reach P below 0.133 two-sided. For the same libraries: PDK1 0.78 (533, 673, 478, 521 against 659, 579 raw), PDK2 0.91, PDK4 1.37 (overlapping).

## 8. Increment 3 (ranks 17 to 24; 2026-11-25; one frozen matching rule, both counts under it only)

Frozen before any source: `PREREG_ADV282_INC3_SCI_20261125.md` (hash fd68e9d948ba5a1e, 21:03:41Z). First reading frozen before the blind report: `FIRST_READ_ADV282_INC3_SCI_20261125.tsv` (hash 6051da14aa5cec46). Blind reader: sonnet, effort high (read back from the census: 51 turns, effort high, model claude-sonnet-5-5, no mid-run change), report `BLIND_REPORT_ADV282_INC3_SCI_20261125.md`. No row was skipped for being Obeid-only: none of the eight has the Obeid article as its only source.

### 8.1 Classes under the one rule

| id | first reading | blind reader | in-study check | other effect (separate column) |
|---|---|---|---|---|
| DA-I01-002 (PDK1 CAGE, Kosla 2019) | PRESENT (progenitor Western, Supp Fig 1) | PRESENT in progenitors; NOT MATCHED for the neuron stage | yes | yes |
| DA-K01-005 (cytoplasmic HIF1alpha, Baryla 2022) | PRESENT | PRESENT | yes | yes |
| DA-K01-006 (nuclear HIF1alpha) | PRESENT in 3 of 4 conditions | PRESENT in 3 of 4 | yes | yes |
| DA-I01-004 (PDH, Baryla 2022) | PRESENT | PRESENT (hypoxia hyperglycaemia inconsistent across assays) | yes | yes |
| DR-W2-002 (memantine, GoF) | NOT MATCHED | NOT MATCHED | variant function yes; patient exposure no | yes |
| DR-W2-003 (memantine, LoF) | NOT MATCHED | NOT MATCHED | as above | yes |
| DR-W2-007 (adult WWOX-DEE, antiseizure drugs) | ABSENT (query 2026-11-25: serum, level, dose, plasma, concentration, held XML) | ABSENT (regex, zero hits) | no | no |
| DR-K01-006 (HIF axis, four PMIDs) | held paper 34021541 PRESENT; three PMIDs NOT ASSESSABLE (not in files/fulltext) | same | yes (held paper) | yes |

**Counts, both readers under this rule only (denominator 8; DR-K01-006 on its one held source):** strict (ABSENT) 1 of 8; loose (ABSENT or NOT MATCHED) 3 of 8 (DR-W2-002, DR-W2-003, DR-W2-007). The two readers agree on every class and every in-study entry. Predictions in the PREREG: strict 3 (range 1 to 5), loose 5 (range 3 to 7): both landed at the bottom edge of the range. The rejecting observation (loose 2 of 8 or fewer) was not met. Loose across the 22 assessable rows of increments 1 to 3 under the same rule: increments 1 and 2 were 0 of 14 (first reading) or 5 of 14 (blind reader); with this increment 3 of 22 or 8 of 22. It rests on what the matching rule counts, as before.

### 8.2 Yield (MUST CHANGE is the yield; MUST CHANGE or ADD is reported but is not the yield)

| | MUST CHANGE | ADD | STANDS |
|---|---|---|---|
| first reading | 1 (DR-W2-002) | 6 | 1 (DR-W2-007) |
| blind reader | **3** (DA-I01-002, DR-W2-002, DR-W2-003) | 5 | 0 |

Blind MUST CHANGE 3 of 8 (prediction 2, range 0 to 4: within). Over all three increments the blind reader gives MUST CHANGE 9 of 22; ADV-281 gave 2 of 13. The first reading missed two of the three (DA-I01-002 and DR-W2-003): it graded the facts, not the sentence (see 8.4).

### 8.3 What I verified myself before accepting each MUST CHANGE

* **DR-W2-002.** The text of the held article puts "Fisher exact test, P = .0698" on the 9 angstrom distance classification scored per individual (only sustained effects counted as positive) and P = .0210 on the variant-level version; the card puts 0.0698 on "variant level counting sustained effect only". The other Fisher values reproduce (14/19 against 3/15 P = .0049; behaviour .006; development .0261; seizures 7/18 against 2/10 P = .417). Worsened: #10, #25, #32 (increased seizure frequency). Both readers agree.
* **DR-W2-003.** Re-read from Table S1 (`..._supp_S2_clinical.xlsx`, one column per individual, 34 individuals): ACMG class VUS in five individuals (#8, #19, #28, #29, #31), and the VCEP row has four VUS and one likely benign (#28); the card says "4 non-pathogenic". The comparator group of 15 is ten loss-of-function, indeterminate or no-effect carriers plus these five. Both seizure reductions in the comparator (2 of 10) are #28 (seizure free except for one) and #29 (reduction), whose variants were "not tested" for function and rated "no effect" by the authors; no carrier with a tested loss-of-function or indeterminate variant had a seizure reduction in the sheet. "Parent-reported only" is slightly narrow (#23 is also reported by the kindergarten; blind finding, not rechecked by me). The article text says "five VUS and one likely benign", which disagrees with its own table by one: the sentence should carry the table's count and say so.
* **DA-I01-002.** The sentence's own numbers contradict its wording: -0.67 with a Poisson half-width of 0.45 gives [-1.12, -0.22], which excludes zero (arithmetic, mine). From the deposit I recomputed the library-size-normalised shifts of PDK1: progenitors 3.558/5.156 gives -0.535, neurons 1.571/3.304 gives -1.072, both negative; the column totals (summed TPM 89,581 for the knockdown neuron library against 264,496 for its control, 609,160 for the progenitor control against 606,894 for the progenitor knockdown, recomputed by me from the deposit; the blind reader's cluster-level sums, 619,266 and 616,711, are another sum and are not used here) mean the sign at the neuron stage depends on the normalisation. The -0.67, +0.44 and p about 0.49 do not reproduce from the deposit under library-size normalisation (the blind reader's median re-centred values are -0.74 and +0.38). The median gene ratio in the neuron pair is 0.350 with my filter (control TPM at least 1); my first reading wrote 0.357. The progenitor CAGE WWOX signal is 1.154 times control (the shRNA acts after transcription), so the knockdown rests on the Western alone there; at the neuron stage the CAGE WWOX signal is 0.203 of control (0.60 after the column-total ratio 0.339).
* **ADD points checked:** Baryla fractions were cultured 6 h (Methods); the blind reader reports 48 h in the Figure 6 caption (not checked by me). The Results' immunocytochemistry (Figure 8) shows higher total HIF1alpha in the knockout in normoxia (normo- and hyperglycaemia, p < 0.01), which the DA-K01-005 and -006 sentences omit; in DA-K01-006 the normoxia-normoglycaemia nuclear fraction has no nuclear WWOX loss, the blind reader reads the nuclear HIF1alpha mean there as about 5.4 times higher in the knockout with a large SEM (not rechecked by me). For DR-K01-006 the held paper is a miR-485 agomir in ICR mice, and the in vivo causal evidence is reversal of the agomir effect by overexpression of HDAC5, HIF1alpha or PFKFB3, not "lowering the three together"; figure images are not held. DR-W2-007: the paper gives the current regimen (valproate 1,000 mg, levetiracetam 2,000 mg, perampanel 6 mg per day) and "sustained", so "exposure unknown" is too strong and transient benefit is not excluded.

### 8.4 Sentences for IT (card owner), verified errors first

1. **DR-W2-002 (16 consumer files; MUST CHANGE).** Put P = 0.0698 on the individual-level 9 angstrom classification, P = 0.0210 on the variant-level one, and state that neither tests the 14 of 19.
2. **DR-W2-003 (16 files; MUST CHANGE).** "Group of 15 includes 5 non-pathogenic variants (Table S1; the text says five VUS and one likely benign)"; add that both seizure reductions of the comparator (2 of 10) come from two carriers of untested VUS rated "no effect", and none from a tested loss-of-function or indeterminate carrier.
3. **DA-I01-002 (3 files; MUST CHANGE).** Replace "the interval spans zero" (false at -0.67 with half-width 0.45) by: "library-size-normalised shifts -0.54 (progenitors) and -1.07 (neurons), both decreases; the neuron column is on another scale (summed TPM 89,581 against 264,496), the sign flips after median re-centring (-0.74, +0.38); n = 1 library per arm; no decrease is demonstrated; WWOX knockdown is shown by Western blot in progenitors only (Supp Fig 1), and the CAGE WWOX signal is not lower there". The -0.67, +0.44 and p about 0.49 should be marked "normalisation not stated, not reproduced from the deposit".
4. **ADD (do not change the null):** DA-K01-005 and -006 (2 files each): add the immunocytochemistry increase and the 6 h fraction timing; DA-K01-006 notes no nuclear WWOX loss in normoxia-normoglycaemia. DA-I01-004 (3 files): hexokinase, LDH and lactate are higher only in some conditions (lactate in all four); the hypoxia-hyperglycaemia "no effect" coincides with no WWOX reduction by mRNA and immunofluorescence; WWOX overexpression lowers PDH activity, so the assay can move; keep the unresolved "PDK" wording. DR-W2-007 (17 files): current doses and "sustained". DR-K01-006 (18 files): the cascade was tested node by node; three of the four named PMIDs are not held and stay abstract level; the "abstract level" tag is out of date for the held paper.

### 8.5 Not done, limits

DR-K01-006: PMIDs 24889205, 36655171 and 42276303 are not held (NOT ASSESSABLE; not fetched, as the row has a consumer count that would justify it only if IT asks). The Baryla supplementary .tif figures and Kosla Data_Sheet_3 were not opened by either reader; Karnstedt's Tables S1 and S4 (docx) were not read in full by the blind reader. Ranks 25 to 48 and the two classifier-stop rows are untouched.
