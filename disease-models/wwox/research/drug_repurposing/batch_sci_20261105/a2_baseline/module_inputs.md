# Module inputs from the A2 baseline (proposals only; nothing here was applied)

Prepared by `sb-a2` for the Orchestrator, `ORCH-SCIBATCH-DR-20261105`, 2026-11-05; corrected 2026-11-06 after the adversarial review (`verify/review_A/`, statements A2-MI-INV10, A2-MI-CLAIM031, A2-MI-REG; answers in `RESPONSE.md`). Each proposal is written in the vocabulary of the file it would touch and names the `evidence_a2.tsv` rows it rests on, with the depth at which each cited source was read. Nothing was edited outside `a2_baseline/`. Not medical advice.

## 1. Investigation `INV-10`

File: `disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/ranking.json`, key `investigations`, entry `inv_id = INV-10`. The fields below are those of the entry.

* `question`: keep as written.
* `evidence_available`. Proposed addition: "Non-WWOX DEE baseline (batch_sci_20261105 `a2_baseline`):
  * In a prospective IESS cohort read at partial full-text depth, 72% of responders (126 of 175, computed from its Table 1) were below the developmental cut at 3 years. No genetic-aetiology child reached a favourable outcome: 0 of 49, a count over all genetic-aetiology children, not a responder rate.
  * In two randomised IESS trials (abstract level), arms that raised early spasm cessation by 15 to 19 points showed no demonstrated developmental difference, with about one chance in four of detecting the difference that full mediation would predict. In TSC, two randomised trials of pre-onset prevention changed seizure endpoints without changing development to 36 months; they test prevention before onset, not response after onset.
  * The person-level association (ICISS, abstract level: 15.9 VABS points higher with early cessation) is carried by unknown aetiology and a normal first neurological examination."

  Rows: A02, A08, B02, B03, B08, A09, B09, C01, C02, C03.
* `decisive_uncertainty`. Proposed rewording: "Whether the separation of symptomatic response and development seen in WWOX-DEE cases differs from the base rate of genetic and structural DEEs, in which a responder with poor development is the expected case (in unknown aetiology the two are coupled, so the base rate does not extend to DEE generally); and whether any WWOX-DEE case shows a change on a continuous developmental measure after a symptomatic response. The contradiction with the mechanism argument is explained, for genetic strata, by a developmental component independent of seizure control, as reported in STXBP1, Dravet and KCNQ2 cohorts." Rows: B03, B08, D01, D03, D05, D09, D12.
* `next_test`. Proposed refinement: "Read the A1 concordance counts against the stratum base rates in `a2_baseline/README.md` section 1.3. Only a WWOX-DEE responder rate with a favourable or improving developmental course clearly above the genetic-DEE base rate would be a WWOX finding. Where a source gives one, compare within-child continuous scores before and after response; a cut at 70 cannot discriminate." Rows: B01-B03, B09, C02, D01.
* `why_now`. The current sentence says the module holds a series in which response and development did not move together, "so the useful investigation is the separation itself". Proposed rewording: "The separation is the expected pattern in genetic and structural DEEs (`a2_baseline`), so it is not, by itself, a WWOX finding. The useful investigation is whether WWOX-DEE departs from that base rate, and whether any intervention moves development by a route other than seizure control." Rows: B02, B03, B08, D08, D11.
* `novelty_perimeter`. Proposed addition: "Non-WWOX DEE baseline queried: UKISS, ICISS, the National Infantile Spasms Consortium records (no developmental outcome endpoint), lead-time cohorts, EPISTOP and PREVeNT, STXBP1, Dravet and KCNQ2 cohorts, and an early-infantile DEE cohort with burst suppression (`a2_baseline/queries.tsv`)."
* Transfer conditions, proposed as a new line in the evidence text, since the entry has no dedicated field:
  * aetiology stratum (decoupling expected in genetic and structural strata, coupling in unknown aetiology; A03 and A05 at abstract level, B03 at partial full-text depth);
  * baseline neurological status at onset (B09, B04; partial full-text depth);
  * lead time from onset to effective treatment, confounded by aetiology (A06, A10, B10 at abstract level; B04 at partial full-text depth);
  * the developmental instrument (a cut at 70 hides change below it; C02, D01). The comparison with WWOX-DEE reports, which describe development without a scale, holds only as a binary.
  * The arm-level nulls are underpowered (about one chance in four for the mediated effect) and are not by themselves evidence of decoupling.

## 2. Work order `NEED-SEIZURE-CONTROL-SYMPTOMATIC`

File: `disease-models/wwox/research/drug_repurposing/view/work_order.json`, `entries`, `need = NEED-SEIZURE-CONTROL-SYMPTOMATIC`.

* `data`. Proposed addition: "For the case-level drugs, the base rate of 'responder with poor development' in genetic and structural DEEs (`a2_baseline/README.md` section 1.3) is the reference against which the vigabatrin and ketogenic-diet case-series denominators are read, as a binary comparison (favourable or not)."
* `would_change`. Proposed addition: "If the WWOX-DEE discordance rate does not exceed the genetic-DEE base rate, the discordance is recorded as a feature of genetic and structural DEEs, not a WWOX finding. The C2 judgement on the case series is decided by their denominators (package A1), not by this baseline." Rows: B02, B03, B08.
* No change proposed to the ethosuximide and lithium parts of the entry.

## 3. CLAIM 031

File: `disease-models/wwox/registries/claim_registry_current.md`, `## CLAIM 031`.

* `Genotype/model relevance` now reads "umano — null biallelici; il principio è atteso indipendente dal genotipo". **Proposed narrowing:** the principle is expected in genetic and structural strata, not independent of aetiology. In unknown aetiology, symptomatic response and development are coupled:
  * in randomised data read at abstract level: the 14-month and 4-year reports of one trial (UKISS), in infants with no identified aetiology, VABS +9.3 at 14 months and median +14 at 4 years in the arm with better early control;
  * in cohort data: ICISS person-level, abstract level; Jonsson 2024, partial full-text depth.

  Rows: A03, A05, A09, B07. Quote for the narrowing, from the UKISS 14-month abstract (abstract level): "In infants with no identified underlying aetiology, the mean VABS score was higher in those allocated hormone treatment than in those allocated vigabatrin".
* **Proposed evidence-boundary line:** "Baseline (`a2_baseline`): in genetic-aetiology DEEs a responder with poor development is the expected case.
  * In a prospective IESS cohort (Jang 2026, read at partial full-text depth) none of 49 genetic-aetiology children was favourable at 3 years. The count is over all 49; the number of responders among them is not in the text read.
  * In a population cohort (Jonsson 2024, partial full-text depth) all genetic IESS infants had global delay 'despite good seizure control in the majority'.
  * In STXBP1-DEE (Balagura 2022, partial full-text depth) development did not track age at seizure remission.

  The observation therefore supports 'seizure control is not protection of development' for the genetic class, and does not distinguish WWOX-DEE from other genetic DEEs. The comparison holds only as a binary (favourable or not), because the WWOX reports describe development without a scale." Rows: B03, B08, D01. The qualifier "in some of these cases" stays unresolved here; this package did not read the primary.
* `Clinical meaning` ("Il controllo delle crisi non va contato come protezione dello sviluppo cognitivo"): consistent with the baseline for genetic and structural strata (A02, A08 at abstract level; C01-C03 module-held complete reads; these arm-level nulls are underpowered undemonstrated differences, not shown absences). Proposed addition: "In genetic DEEs treated with a channel-matched drug, development has been linked to treatment timing beyond seizure control (KCNQ2: an abstract-level assertion in a 282-child cohort, and a prompt-diagnosis comparison read at partial full-text depth), so 'no antiseizure drug modifies development' is not shown as a general rule." Rows: D10, D11. No status change proposed.

## 4. `proposed_registry_changes` (plain statements; nothing was changed)

1. PAPER and LIT identity records for the eight sources read beyond the abstract at partial full-text depth (receipts `partial_fulltext_read`), which have no registry identity now: PMID 42730593, 34623615, 38785332, 35655584, 24225340, 38229878, 42081271, 31929713. Each would carry its receipt `FTR-20261105-<PMID>-22` once recorded, its depth as `partial_fulltext_read` (no source was read to complete depth), and the note "NOT WWOX EVIDENCE: non-WWOX DEE baseline". These are the same kind of identity records that `BATCH_20261019_012` created for receipts without identity.
2. PAPER and LIT identity records, abstract level, for the 16 abstract-only receipts (PMID 15541450, 16239177, 20457702, 21668442, 27838190, 30236380, 36621063, 22689735, 23740534, 15009227, 17201726, 19369101, 42610455, 37099824, 29750338, 25880994), if the Orchestrator records those receipts. The guideline and the Cochrane review should be marked as pointers, not primary units.
3. Cross-link PAPER 498 (EPISTOP), PAPER 514 (PREVeNT) and PAPER 515 (PREVeNT neurodevelopment) to `INV-10` and to `NEED-SEIZURE-CONTROL-SYMPTOMATIC` as the randomised genetic-and-structural-stratum evidence of the baseline (rows C01-C04). Their identity records now name only trial-design precedents.
4. Correction for the batch record. The statement "Nothing on this baseline was read at full-text level by the module" is not accurate: PAPER 498, 514 and 515 are complete reads (receipts `FTR-20261021-33180985-01`, `FTR-20261021-37638552-01`, `FTR-20261021-41061327-01`). They were reused here from their manifests, not re-read.
5. Full-text queue candidates, for any later open route: PMID 30236380 (ICISS 18 months) and PMID 31418851 (ICISS aetiology). They hold the one dataset that would discriminate marker from cause by aetiology stratum, and both are subscription only today.
6. PMID 42190144 (Riccardi 2026, 110-child early-infantile DEE cohort with burst-suppression EEG), added 2026-11-06 at the review's request (row D14). Its abstract names WWOX among the novel gene associations of the cohort, so it is relevant to package A1's WWOX counts as well as to this baseline. The module already holds the abstract in discovery ledger entries DL-MECH-001, DL-MOL-001 and DL-REPO-001, and DL-REPO-001 already asks for the full text. Proposed: a full-text queue entry (no PMC record; not reachable by an open route today), and a PAPER and LIT identity record at abstract level. No receipt is staged here, because this package read only the PubMed record.
