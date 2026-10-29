# CC-20261029-INTEGRATOR-IT6-REGISTRIES-01
- **Class:** ORDINARY, research-layer and registry-note batch. **No working-model statement changes, so no version bump: `target_wm_version` is `WM_v7.28` (preserved).** No claim created or reversed, no `Status`, `Type`, `Title` or `Summary` changed anywhere; no hypothesis promoted; no claim created from a hypothesis. Not medical advice; nothing here is a clinical recommendation.
- **Author:** ACTOR_ID `integrator` (Integrator worker for the orchestrator), mandate IT6, step registries, task branch `task/it6-batch`.
- **Source material (all independently verified and repaired, and already landed in the module; not re-enumerated here):** `drug_repurposing/wwox_data_census_it6_20261029.md` (P3), `drug_repurposing/mouse_wwox_p17_it6_p4_20261029/README.md` (P4), `drug_repurposing/wwox_function_reference_it6_20261029.md` (P5), `drug_repurposing/broad_recovery_it6_p6_20261029/README.md` (P6), `drug_repurposing/rescue_window_it6_20261029.md` (P7), `drug_repurposing/nmdar_pharmacology_it6_p9_20261029/README.md` (P9), `drug_repurposing/partial_benefit_it6_p10_20261029/README.md` (P10), `drug_repurposing/supplement_diet_it6_p11_20261029/README.md` (P11) and `drug_repurposing/priority_review_it6_20261029.md` (P2), with the verifier reports `locator_audits/2026-10-29_it6_p2_verifier.md` to `..._p11_verifier.md`. The 27 receipts these cycles produced were recorded earlier (22 events at ledger 907 and 5 events at ledger 912); this batch records none.

## What changes and why
1. **Gene addition is prevention or early-window in the mouse, not recovery of a manifested deficit (P7, with P5).** Every in-vivo genetic rescue treats the Wwox-null mouse at P0 to P5 in animals never measured before treatment; no treated-after-onset mouse arm exists; the only genetic add-back after a documented phenotype is organoid (week 10 on a phenotype seen at week 7, radial-glia abnormalities not corrected). The window-state wave notes sit on `CLAIM 004`, `CLAIM 011`, `CLAIM 040` and `CLAIM 002` (Titles and Statuses unchanged: the word 'rescue' is the authors' word for a measured change in a named endpoint), on `DL-MECH-011`, `DL-MOL-005` and `DL-MECH-007`, on the readings of the papers concerned, and in the map (CHAIN A boundary 5, the M1 cell, R-01). The cards C01 and C04 and the needs already carry the early-window wording (landed with the P5 and P7 consumers); the join output and the p5 tables, which still held the old card wording, are regenerated. Bulk protein does not track the survival step: the low dose already carries several-fold wild-type bulk protein in cortex and hippocampus.
2. **The d-APV result shows that the bursting needs NMDAR activity, not that NMDAR function is raised (P9, P11).** Three readings are unranked (NMDAR gain; permissive necessity with a depolarised resting potential and a halved inhibitory current; AMPAR-led drive). The wave note on `CLAIM 021`, the updates on `DL-MOL-001` and `HYP-20261027-01`, and the map (CHAIN B, R-02) say so; the map line that called the NMDAR node 'pharmacologically established with d-APV inside the WWOX system' is replaced in place by 'NMDAR ACTIVITY IS REQUIRED ... a RAISED NMDAR function is NOT shown'. The discriminating measurement is the isolated NMDAR current under voltage control (card F04). The incubation solution holds 1.3 mM Mg2+, the recording bath is not stated, the baseline burst rate is printed twice 2.7-fold apart.
3. **Extracellular magnesium as the physiological NMDAR gate is registered as a NEW hypothesis, `HYP-20261029-01` (P11).** Status `generated`, no ranking line, `IPOTESI`, a partial-benefit lever; the strongest counter-data (CSF unchanged after oral sulfate in the mouse, null seizure control in the one randomised infant trial with an oral phase, no deficiency premise) are in the record. No claim is created from it.
4. **The sign of the ISR transcript signal stays UNRESOLVED after a third system (P3, P4).** Mouse P17 brain with an unambiguous deletion: the ISR target set is inside its matched null in every contrast, no resolvable sign at about 0.3, Atf4 mRNA alone lower (an mRNA observation, not an ISR call). No public record measures protein, phospho-protein, translation or flux in a WWOX-deficient system. Updates on `DL-MECH-173`, `HYP-20261026-10`, `DL-MECH-020`, `DL-REPO-004`, `HYP-20260709-01`, `HYP-20261026-11` and the map (R-10, R-11).
5. **The glial change has no uniform sign (P10).** The rat deficit against the mouse excess, the organoid without a reactive programme, every mouse glial read after the first seizures: the lead stays an abstention. Wave note on `CLAIM 005`, updates on `DL-REPO-002` (whose heading 'direzione RISOLTA' is not edited and is superseded in effect by its own earlier CORRECTION and this update), `DL-MECH-012`, `HYP-20260705-02`, and the map (R-06).
6. **A wild-type function ruler is the first step before any abundance gain can be read as rescue (P5), and route blockade of a destabilised cytosolic enzyme returned protein of unequal worth (P6).** Updates on `DL-BIO-085`, `HYP-20260709-08` and the map (R-09). The premise (a route blocker or chaperone given to a WWOX missense system) is missing; no precedent separates stabilisation from a transcript effect.
7. **Reading updates** on 12 paper records and 11 literature-log records for the papers re-read in these cycles with a recorded receipt (question, depth, what the reading adds); each points to the claim wave note or ledger update where the content lives.

## What was deliberately NOT registered, and why
- **No working-model change.** Searched: `working_model_current.md` lines on AAV9, gene therapy, rescue, NMDAR and bursting. The statements that read as recovery language ('durable rescue', the Obeid and Steinberg bullets, the `011` and `002` rows of the claim table) already sit beside 'early postnatal window', 'early postnatal ICV delivery' and 'Treatment is at P0 ... post-natal dosing is declared future work', and no row's title, status or summary changes; the qualifier lives in the claim wave notes. The one working-model line left untouched on purpose is 'The therapeutic window is generally considered still open in early childhood; plasticity at age ~3 is plausible, not guaranteed' (an expert-sentiment sentence outside the mouse evidence; DL-MECH-011 and the dismissal `DIS-033` already say the window is not measured in either direction). A reviewer who wants the working model to carry 'prevention, not recovery' is asking for a separate MINOR candidate; this batch does not make it.
- **No identity records (PAPER or LIT) for the non-WWOX precedents read in these cycles**, as in the iteration-5 precedent: the cystathionine beta-synthase papers, the NQO1 chaperone paper (`FTR-20261029-37319242-01`, `-38051092-01`, `-39041895-01`, `-31605637-01`), the magnesium and infant-spasm papers and the physiology papers of P11 (`FTR-20261029-24614743-01`, `-31806980-01`, `-35222658-01`, `-36967744-01`), and the NMDAR class and GRIN papers of P9 (`FTR-20261029-29446949-01`, `-32106360-01`, `-41489401-01`, `-42201999-01`). They have receipts, no registry claim rests on them, and the registries' practice is identity records for papers a record cites. The mouse-side census deposits (the GEO series of P3 and P4) have no PubMed link and are not papers.
- **No new claim, no status change, no promotion.** The magnesium strand and the NMDAR classes are hypotheses; `CLAIM 030`, `CLAIM 031`, `CLAIM 036` and `CLAIM 037` are untouched although P4 and P10 touch their neighbourhood (the null at P17 is systemically ill, `CLAIM 036`, is already stated and only restated in the P4 limits).
- **Dismissal ledger: 0 ops.** `DIS-004` (phenylbutyrate, not reversed in iteration 5), `DIS-033` (the window cannot be bounded) and the others are consistent with the iteration-6 results and are not edited.
- **P8 capability trial and P12 resource comparison** (tool-level work: the ChEMBL adapter extension, the GluN2B comparison across four catalogues) state no registry-level fact; the tool-compound resolution that matters is in P9 and is carried by the F04 card.
- **P2 priority review** changes labels in the view and the coverage layer (already landed and regenerated); no registry or ledger record states a priority label, so nothing is registered.
- **Fly deposit observation of P3** (the head RNA deposits show no visible Wwox change in the deposited counts) has no receipt and is carried only inside the `DL-MECH-173` update, not in any paper record.
- **Receipt ledger untouched** (no receipt recorded here); `working_model_history.md` untouched; `experiment_ledger`, `disease_model.md` untouched.

## Version rule (prompt_batch_commit section 7)
No statement in `working_model_current.md` changes, so no bump: `WM_v7.28` is preserved, `last_wm_*` fields untouched and the working-model history gets no row, as in `BATCH_20261019_024` and `BATCH_20261019_026`. A claim wave note, paper reading updates and ledger bullets are not working-model changes.

## Op lists
`ops_parsed` is declared per file below, 29 record-scoped ops in all for the three registries that take them (working model 0, claim registry 6, paper registry 12, literature log 11), through `batch_commit.py propagate`, dry run then `--apply`. Written by `record_scoped_edit.py apply` because `batch_commit.py propagate` accepts only the four scientific current files: discovery ledger 10, hypotheses ledger 6 (each one `replace-within` on the addressed record that keeps its existing text and adds ONE dated UPDATE bullet after the record's final line, except where Position says otherwise). One further hypotheses-ledger change is not an op: the new record `HYP-20261029-01` is appended at the end of the file by a plain append, because `record_scoped_edit.py` refuses a level-3 record inserted into a level-2 run (`RESEGMENTATION`); every other byte of the file is the result of the record-scoped ops above (checked by diff).

### working_model_current.md (0 ops)
None.

### claim_registry_current.md (6 ops)
```json
[
 {
  "op": "replace-within",
  "id": "CLAIM 004",
  "old": "**Impact on Working Model:** strategic / trial-readiness support",
  "new": "**Impact on Working Model:** strategic / trial-readiness support\n**Wave note (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; research-layer reading, Status, Type and Summary unchanged):** read as a window statement, every endpoint of this study is PREVENTED or EARLY-WINDOW, none is RECOVERED: the vector was given at P0, the animals were never measured before treatment, every behavioural endpoint is compared with wild type only (the authors: they could not assess behaviour of Wwox-null mice because of their poor conditions and premature death), and adult recordings exist only for treated animals because the untreated nulls died within four weeks. The stated reason for treating at P0 is the null's limited life span, and the authors write that attempts to treat post-natal Wwox-null mice by a different route of AAV administration 'should and will be explored in the future'. 'Rescue' in the Title and Summary is the authors' word for a measured change in a named endpoint after neonatal treatment; it does not show that a deficit already manifested was undone and it does not license carrying the result to a later age. Source: `drug_repurposing/rescue_window_it6_20261029.md` section 2.1 (receipt `FTR-20261029-34747138-01`, `partial_fulltext_read`, question-driven), independently verified (`locator_audits/2026-10-29_it6_p7_verifier.md`, statement 1)."
 },
 {
  "op": "replace-within",
  "id": "CLAIM 011",
  "old": "S2 reports `n=5` on graph labels and `n=4` in its caption.",
  "new": "S2 reports `n=5` on graph labels and `n=4` in its caption.\n🔵 **Wave note (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; research-layer reading, Title, Status and Summary unchanged; nothing above is edited):** (1) **Window state.** The main cohorts were injected at P0 to P1 and the timing arms at P1 to P5 (S8), in animals never measured before injection; ECoG recording starts at about P14, which is a floor of observation and not an onset. Every endpoint of this claim is therefore PREVENTED or EARLY-WINDOW and none is RECOVERED. The S8 survival panels are small and not uniformly successful (P1, P2 and P5 arms at 100 percent to P40; a P3 arm, n = 3, at about 67 percent from about day 24; a P5 arm, n = 7, at 75 percent from about day 35 to day 300; the two panels are not obviously consistent for P5; no P0 arm and no P4 survival curve; treated arms are compared with wild type, so 'ns' is not equivalence), which the main-text sentence that delivery at any time point between P0 and P5 fully rescued the phenotype does not state. The authors write that rescue beyond this window 'was not explored' and that the inability to assess later intervention is not 'a definitive boundary for therapeutic responsiveness': P1-P5 is the set of ages tested, not a measured window. The only add-back after a documented phenotype in the corpus is organoid (see the note on `CLAIM 002`). (2) **Bulk protein does not track the survival step.** Low and high dose were not statistically resolved in vector DNA or mRNA (7 of 8 comparisons); protein at P30 shows an untested trend (cortex about 2-fold higher at the high dose, a reading of Fig 5I to L); the low dose already carries several-fold wild-type bulk protein in cortex and hippocampus, while the cerebellum stays below wild type at both doses. What carries the phenotype (a region, a cell type, a time, a peripheral tissue) is not what a per-lysate protein value reports, and a ruler built in one cell type does not transfer to a tissue dose-response. Sources: `drug_repurposing/rescue_window_it6_20261029.md` section 2.2 (receipt `FTR-20261029-42422765-01`); `drug_repurposing/wwox_function_reference_it6_20261029.md` section 4 row W12; verifiers `locator_audits/2026-10-29_it6_p7_verifier.md` (D1, D2) and `locator_audits/2026-10-29_it6_p5_verifier.md` (statements 8 to 11)."
 },
 {
  "op": "replace-within",
  "id": "CLAIM 040",
  "old": "**Non generalizzare a un altro allele, a un'altra età o a un'altra specie.**",
  "new": "**Non generalizzare a un altro allele, a un'altra età o a un'altra specie.** 🔵 **Wave note (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; research-layer reading, Status, Type and Summary unchanged):** window state. The vector was injected at P0 to P1 and recording began at about P14, so the fall of the spike-wave rate to a level not different from wild type is a PREVENTED or EARLY-WINDOW readout in animals never recorded before treatment (the recording start is a floor of observation, not an onset; glucose is already low at P10 and hypoglycaemia is stated from the second week); one vector level (the high dose) and no low-dose arm in this panel. A lower rate after neonatal treatment does not show that discharges already present were suppressed. Source: `drug_repurposing/rescue_window_it6_20261029.md` sections 2.2 and 4.1 (receipt `FTR-20261029-42422765-01`), independently verified."
 },
 {
  "op": "replace-within",
  "id": "CLAIM 002",
  "old": "**Impact on Working Model:** supports BLOCCO 1 and P7",
  "new": "**Impact on Working Model:** supports BLOCCO 1 and P7\n**Wave note (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; research-layer reading, Title, Status and Summary unchanged):** window state of the organoid add-backs. The stem-cell safe-harbour add-back (W-AAV) is present before differentiation, so it is PREVENTION by construction, and it is partial and supraphysiological; the lentiviral arm (day 35 of culture, 'week 6' in one legend) precedes the first excitability recording (week 7) by one to two weeks, so it is EARLY-WINDOW, while knockout DNA damage and astrocyte markers are already measured at week 6 (onset is unmeasured for excitability only; the panel n for W-AAV is given as 4 in most legends and as 3 from one batch in some, not reconciled). The only add-back after a documented phenotype in the corpus is the neuron-directed AAV9 arm of the 2026 organoid paper ([[paper_registry_current#PAPER 094]]): infection at week 10 on a hyperactivity seen at week 7 in a different organoid cohort, read at week 16, persistence unmeasured, hyperexcitability reduced to a level similar to wild type (not an equivalence test), layer markers up in one patient line and not the other, radial-glia abnormalities NOT corrected ('without correcting RG abnormalities'). 'Rescues organoid phenotype' in the Title therefore names a model result with these qualifiers, not recovery of a manifested deficit in general; organoid age is culture age, not gestational age. Sources: `drug_repurposing/rescue_window_it6_20261029.md` sections 2.3 and 2.4 (receipts `FTR-20261029-34268881-01`, `FTR-20261029-42397075-01`), independently verified."
 },
 {
  "op": "replace-within",
  "id": "CLAIM 021",
  "old": "**Impact on Working Model:** strengthens ACTIVE 1 / network hyperexcitability as core pathway; no BLOCCO 1 operational change",
  "new": "**Impact on Working Model:** strengthens ACTIVE 1 / network hyperexcitability as core pathway; no BLOCCO 1 operational change\n**Wave note (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; research-layer reading, Status, Type and Summary unchanged; the withdrawal of the gap-junction half stands):** what the d-APV arm shows and does not show. d-APV (50 uM, a complete competitive block; 51 bursts in 5 slices from 3 animals, no statistical test on that arm) shows that the bursting NEEDS NMDAR activity. It is not shown to be a raised NMDAR function. Three readings fit it, make different predictions and are NOT ranked here: (H1) NMDAR gain; (H2) permissive necessity in a network whose pyramidal neurons rest about 5.6 mV more depolarised (-73.62 against -79.25 mV, Table 1, no liquid-junction correction) and whose spontaneous inhibitory current amplitude is about half (57.3 against 27.5 pA, pooled controls); (H3) an AMPAR-led drive. No NMDAR-specific measurement exists in any Wwox system: the mEPSC increase is AMPAR-weighted (recorded at -70 mV in magnesium) and the decay time constant is unchanged (5.18 against 4.84 ms), which does not exclude an NMDAR change. The isolated NMDAR current under voltage control (card F04, step E1) is the measurement that decides between them. Two facts about the preparation: the incubation solution holds 1.3 mM Mg2+ while the recording bath is not stated (that the bursting occurs at physiological magnesium is an inference), and the baseline burst rate is printed twice, 2.7-fold apart (2.29 per minute in the text, 0.84 per minute in Table S1). An AMPAR antagonist is expected to stop an NMDAR-dependent burst whichever reading is true, so an antagonist result does not choose a drug class. Sources: `drug_repurposing/nmdar_pharmacology_it6_p9_20261029/README.md` sections 2, 3 and 7; `drug_repurposing/supplement_diet_it6_p11_20261029/README.md` (receipts `FTR-20261029-34634460-01`, `-04`, `-05`; independently verified)."
 },
 {
  "op": "replace-within",
  "id": "CLAIM 005",
  "old": "An earned null, recorded so the question is not re-asked of this paper.",
  "new": "An earned null, recorded so the question is not re-asked of this paper.\n**Wave note (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; research-layer reading, Status, Type and Summary unchanged):** the sign of the glial change is NOT uniform across the Wwox models, and this claim must not be read as a general direction. The rat lde/lde cortex shows LOWER GFAP-positive cell density (about half of wild type from PND 5, for example about 470 against 255 and about 1570 against 850 cells per mm2 at PND 21) and lower Iba1-positive density from PND 10 (not separated at PND 5), which its authors state to be the opposite of other models; the null mouse at P20 shows an excess (GFAP area about six-fold, Iba1 area about 1.7-fold; region not stated in the caption), as does the P47T knock-in in hippocampus; the human knockout organoid at week 15 shows no reactive-astrocyte or cytokine transcript programme (microglia absent from the tissue; four against two libraries). Species, allele, region, assay and age window are confounded. None of the two-week mice of this claim has a seizure measure, and a neuron-restricted deletion (astrocytes presumably keep Wwox) already shifts astrocyte-activation-type transcripts at P17 in a brain that seizes from P9, so the data fit a seizure-secondary or signal-mediated reactivity at least as well as an astrocyte-intrinsic cause and do not separate them. No Wwox is detected in rat microglia, and the astrocyte-specific deletion was scored for delay, weight and survival only, never for gliosis. Sources: `drug_repurposing/partial_benefit_it6_p10_20261029/README.md` sections 2 to 4 and 9 (receipts `FTR-20261029-31340538-01`, `FTR-20261029-42422765-02`, `FTR-20261029-30290271-01`, `FTR-20261029-33914858-01`, `FTR-20261029-36828035-01`), independently verified."
 }
]
```
### paper_registry_current.md (12 ops)
```json
[
 {
  "op": "replace-within",
  "id": "PAPER 011",
  "old": "422765-01`; count re-derived 2026-10-23 as `len(verbatim_locators['entries'])`).",
  "new": "422765-01`; count re-derived 2026-10-23 as `len(verbatim_locators['entries'])`).\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipts `FTR-20261029-42422765-01` (onset, comparator and follow-up of the P0-P5 arms; Figure S8 rendered at 300 dpi) and `FTR-20261029-42422765-02` (age and region of the glial excess; Figure S7 rendered), both `partial_fulltext_read`, question-driven. The study is a PREVENTED or EARLY-WINDOW study: main cohorts at P0-P1, timing arms at P1-P5 (S8: P3 arm n = 3 at about 67 percent from about day 24, P5 arm n = 7 at 75 percent from about day 35 to day 300, no P0 arm, no P4 survival curve, treated arms compared with wild type), recording from about P14, no treated-after-onset arm; the untreated glial excess at P20 is about six-fold for GFAP area and 1.7-fold for Iba1 area, region not stated in the caption. The record may carry early-window improvement of named endpoints and no recovery statement; see the wave note on `CLAIM 011`."
 },
 {
  "op": "replace-within",
  "id": "PAPER 005",
  "old": " verifica di metadati e contenuti-chiave, non una lettura integrale con locator.",
  "new": " verifica di metadati e contenuti-chiave, non una lettura integrale con locator.\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-34747138-01`, `partial_fulltext_read`, question-driven (onset statements, comparators, follow-up, stated reason for P0 treatment). Injection at P0; hypoglycaemia from the second week; every behavioural endpoint compared with wild type only, adult firing only wild type against treated; treatment at P0 is justified by the null's limited life span and later treatment is declared future work. PREVENTED or EARLY-WINDOW; nothing RECOVERED. See the wave note on `CLAIM 004`."
 },
 {
  "op": "replace-within",
  "id": "PAPER 094",
  "old": "397075-03`; count re-derived 2026-10-23 as `len(verbatim_locators['entries'])`).",
  "new": "397075-03`; count re-derived 2026-10-23 as `len(verbatim_locators['entries'])`).\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-42397075-01`, `partial_fulltext_read`, question-driven (infection time against the first recorded hyperexcitability; accepted-manuscript text layer, pages 12 to 17; no figure opened). AAV9-WWOX or AAV9-EGFP was given to week-10 organoids and read at week 16; the hyperactivity was seen at week 7 in a different organoid cohort (post-onset by about three weeks); reduced to a level similar to wild type (not an equivalence test); layer markers rose in WOREE and not in SCAR12; radial-glia abnormalities were not corrected; persistence beyond week 16 and a same-organoid baseline are unmeasured. The only genetic add-back after a documented phenotype in the corpus, RECOVERED in a model with these qualifiers."
 },
 {
  "op": "replace-within",
  "id": "PAPER 039",
  "old": "268881-03`; count re-derived 2026-10-23 as `len(verbatim_locators['entries'])`).",
  "new": "268881-03`; count re-derived 2026-10-23 as `len(verbatim_locators['entries'])`).\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-34268881-01`, `partial_fulltext_read`, question-driven (timing of the lentiviral and safe-harbour add-backs against the first measured phenotype; no figure opened). W-AAV is present in the stem-cell line before differentiation (prevention by construction, partial); the lentiviral arm is given at day 35 ('week 6' in a legend) and the first excitability recording is at week 7 (EARLY-WINDOW); knockout DNA damage and astrocyte markers are already measured at week 6; panel n for W-AAV is 4 in most legends and 3 from one batch in some, not reconciled. See the wave note on `CLAIM 002`."
 },
 {
  "op": "replace-within",
  "id": "PAPER 031",
  "old": "pth:** full text verificato (files/fulltext/PMID34634460_Breton2021.md, PMC MCP)",
  "new": "pth:** full text verificato (files/fulltext/PMID34634460_Breton2021.md, PMC MCP)\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipts `FTR-20261029-34634460-01` (window and washout of the d-APV arm), `FTR-20261029-34634460-04` (magnesium content of the medium, resting potentials; `queried_not_full_read`) and `FTR-20261029-34634460-05` (what an NMDAR experiment in this preparation must control), the first and third `partial_fulltext_read`, all question-driven. Slices are aged P13-P17 and the authors write that this age 'may mimic a late-stage disorder'; the d-APV effect is acute and reverses on washout; the incubation solution holds 1.3 mM MgSO4 and the recording bath is not stated; resting potential is -79.25 (wild type), -75.51 (heterozygote), -73.62 mV (knockout), without liquid-junction correction; the baseline burst rate is printed as 2.29 per minute in the text and 0.84 per minute in Table S1; d-APV shows that bursting needs NMDAR activity, not that NMDAR function is raised. See the wave note on `CLAIM 021`."
 },
 {
  "op": "replace-within",
  "id": "PAPER 019",
  "old": "-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's",
  "new": "-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-32000863-01`, `partial_fulltext_read`, question-driven (the onset sentence; the ethosuximide pre-treatment design). The onset sentence ('spontaneous epileptic seizures were commonly observed after postnatal day 12') is a lower bound from handling observations in this line, not a measured onset, and the allele differs from the rescue studies' line; ethosuximide before PTZ suppressed the provoked seizure in nulls (Figure 7b), age stated only as preweaning: an acute, symptom-level endpoint."
 },
 {
  "op": "replace-within",
  "id": "PAPER 021",
  "old": "-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's",
  "new": "-DEPTH-01` (BATCH_20260920_001) — the reading is the receipt's, not this batch's\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-31340538-01`, `partial_fulltext_read`, question-driven (readout, ages, region and n of the reduced glial measures; Figure 5 opened at native size). In the lde/lde rat cortex GFAP-positive cell density is about half of wild type at PND 5, 10, 15 and 21 and Iba1-positive density is lower from PND 10 (not separated at PND 5); the GFAP blot is lower at PND 15 only and the Iba1 blot at all ages, with the blot and the counts disagreeing in size at PND 10; Wwox is stained in neurons, astrocytes and oligodendrocytes and not in Iba1-positive microglia; the sound-evoked seizures after PND 16 are cited from earlier work not re-read, so the deficit precedes sound-evoked seizure competence and is not shown to precede any seizure (no EEG). The sign is the opposite of the mouse rows; see the wave note on `CLAIM 005`."
 },
 {
  "op": "replace-within",
  "id": "PAPER 006",
  "old": "status: complete_fulltext_read) — receipt `FTR-20260806-30290271-01`, 2026-08-06",
  "new": "status: complete_fulltext_read) — receipt `FTR-20260806-30290271-01`, 2026-08-06\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-30290271-01`, `queried_not_full_read`, question-driven (was seizure state recorded in the two-week mice in which the IBA1 and GFAP area fractions were read). No seizure measure is stated for those animals and the authors leave cause against consequence open. The earlier receipt's saved HTML path is not present on this host; the PMC r2 JATS (sha256 3672e629...) is the surface a verifier should use. See the wave note on `CLAIM 005`."
 },
 {
  "op": "replace-within",
  "id": "PAPER 004",
  "old": "rely went stale], validatore PASS), dossier `fulltext_dossiers/PMID33914858.md`.",
  "new": "rely went stale], validatore PASS), dossier `fulltext_dossiers/PMID33914858.md`.\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-33914858-01`, `queried_not_full_read`, question-driven (what was scored in the astrocyte-specific and oligodendrocyte-specific deletions). The GFAP-Cre and Olig2-Cre deletions were scored for delay, weight and survival at P17 (n 9 against 8 and 10 against 11): no abnormality; gliosis, EEG and seizures are not reported for the astrocyte-specific deletion, and the authors do not exclude a cell-autonomous astrocyte function. The neuron-restricted deletion shifts astrocyte-activation-type genes at P17 (Figure 3 legend; heat map not re-opened)."
 },
 {
  "op": "replace-within",
  "id": "PAPER 007",
  "old": "Earlier partial receipts `FTR-20260826-36828035-01` / `-02` stand in the ledger.",
  "new": "Earlier partial receipts `FTR-20260826-36828035-01` / `-02` stand in the ledger.\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-36828035-01`, `queried_not_full_read`, question-driven (do the canonical reactive-astrocyte, microglial and cytokine transcripts appear in the thresholded supplementary sheets). The forebrain sheets list genes with an absolute log2 ratio of at least 1 and the cerebellum sheet goes lower; Gfap, Aif1, Il1b, Tnf, Il6, Lcn2, Serpina3n, Nlrp3, Stat3 and Socs3 are not listed in any region (listed: Serpina3g, Serpina3h, Nes, C3 lower in hippocampus, and Oas1f up 6.0 to 7.3 in the forebrain regions, unexplained: a strain or passenger effect was not tested). Absence from a thresholded list is not a measurement of no change; it shows that the paper's regulator-level inflammatory inference does not rest on the canonical transcripts being beyond a two-fold threshold."
 },
 {
  "op": "replace-within",
  "id": "PAPER 434",
  "old": "ea`); unread or absent (receipt): supplementary `not_read`, tables `not_present`",
  "new": "ea`); unread or absent (receipt): supplementary `not_read`, tables `not_present`\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-33914734-02`, `partial_fulltext_read`, question-driven (class-level substitute for a WWOX route-blockade question; NOT WWOX EVIDENCE). Blocking the Hsp70/Hsp110 route accumulated C152W protein that was insoluble; in human cells the variant is found exclusively in the insoluble fraction; no enzyme activity could be measured, and the earlier studies the paper cites also found no residual activity in purified protein or extracts; bortezomib raised ubiquitinated C152W. Used as a negative precedent for route blockade (inert pellet protein); see the update on `HYP-20260709-08`."
 },
 {
  "op": "replace-within",
  "id": "CORPUS P318",
  "old": "rmed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.",
  "new": "rmed. Entry reserved for future promotion to PAPER 0NN on deep-dive integration.\n**Reading update (2026-10-29, `BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`):** receipt `FTR-20261029-25649963-01`, `partial_fulltext_read`, question-driven (stage and design of the mRNA rescue arm; Methods and Results in the JATS, no figure opened). The Methods describe the rescue as co-injection, at the single-cell stage with the morpholino or siRNA, of an RNA of the ADH-domain region (stated three times), while the Results say 'wwox mRNA'; if the ADH-domain-only RNA is what rescued, it escapes the siRNA (N-terminal WW domain) and the morpholino (start codon) and is the one organism-level rescue by a domain fragment found in this review; the rescue is shown by images, edema penetrance was 56 and 62 percent at 48 hpf, no dose. PREVENTED by simultaneous co-injection, non-neural endpoint."
 }
]
```
### literature_tracking_log_current.md (11 ops)
```json
[
 {
  "op": "replace-within",
  "id": "LIT-0011",
  "old": "**Flags:** preprint flag",
  "new": "**Flags:** preprint flag Reading update 2026-10-29 (`BATCH_20261019_027`): receipts `FTR-20261029-42422765-01`, `-02`; window state PREVENTED or EARLY-WINDOW, see the wave note on `CLAIM 011`. See [[paper_registry_current#PAPER 011]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0072",
  "old": "atal neuronal WWOX gene therapy rescues Wwox null phenotypes",
  "new": "atal neuronal WWOX gene therapy rescues Wwox null phenotypes Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-34747138-01`; window state PREVENTED or EARLY-WINDOW, see the wave note on `CLAIM 004`. See [[paper_registry_current#PAPER 005]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0417",
  "old": "xisting complete reading the entry its PAPER record links to",
  "new": "xisting complete reading the entry its PAPER record links to Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-42397075-01`; add-back at week 10 on a phenotype seen at week 7, radial glia not corrected. See [[paper_registry_current#PAPER 094]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0365",
  "old": "**Note:** Title: Modeling genetic epileptic encephalopathies using brain organoids",
  "new": "**Note:** Title: Modeling genetic epileptic encephalopathies using brain organoids Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-34268881-01`; timing of the add-backs against the first measured phenotype. See [[paper_registry_current#PAPER 039]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0021",
  "old": "**Note:** Key paper for structural substrate and GSK3β node.",
  "new": "**Note:** Key paper for structural substrate and GSK3β node. Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-32000863-01`; the onset sentence is a lower bound, not a measured onset. See [[paper_registry_current#PAPER 019]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0023",
  "old": "ote:** Key support for prenatal cortex hypomyelination axis.",
  "new": "ote:** Key support for prenatal cortex hypomyelination axis. Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-31340538-01`; rat glial density LOWER, the opposite sign to the mouse rows. See [[paper_registry_current#PAPER 021]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0318",
  "old": "in zebrafish embryos causes edema and alters Ca(2+) dynamics",
  "new": "in zebrafish embryos causes edema and alters Ca(2+) dynamics Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-25649963-01`; the rescue RNA is described in the Methods as the ADH-domain region. See [[paper_registry_current#CORPUS P318]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0706",
  "old": "**Note:** class-level record. Not medical advice.",
  "new": "**Note:** class-level record. Not medical advice. Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-33914734-02`; route blockade accumulated insoluble, inert protein (NOT WWOX EVIDENCE). See [[paper_registry_current#PAPER 434]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0110",
  "old": "ated with WOREE syndrome, causes epilepsy and myelin defects",
  "new": "ated with WOREE syndrome, causes epilepsy and myelin defects Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-33914858-01`; astrocyte-specific deletion scored for delay, weight and survival only. See [[paper_registry_current#PAPER 004]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-0077",
  "old": "ssive neuroinflammation, and cerebellar degeneration in mice",
  "new": "ssive neuroinflammation, and cerebellar degeneration in mice Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-36828035-01`; canonical reactive and cytokine transcripts absent from the thresholded sheets. See [[paper_registry_current#PAPER 007]]."
 },
 {
  "op": "replace-within",
  "id": "LIT-006",
  "old": "rtranslate as absolute GABA prohibition. Structured caution.",
  "new": "rtranslate as absolute GABA prohibition. Structured caution. Reading update 2026-10-29 (`BATCH_20261019_027`): receipt `FTR-20261029-30290271-01`; no seizure measure stated for the two-week mice. See [[paper_registry_current#PAPER 006]]."
 }
]
```

### discovery_ledger_current.md (10 ops, record_scoped_edit.py)
#### DL-MECH-011
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P7; EXPLORATORY; the Status `maturing`, the Causal statement and every earlier bullet are not edited).** The 'rescue' in the Causal statement is the authors' word for a measured change in a named endpoint, and the window state of every endpoint is now classified at the source: PREVENTED or EARLY-WINDOW for survival, growth, glucose, spike-wave discharges, motor score and gliosis (main cohorts P0-P1, timing arms P1-P5, animals never measured before injection; recording starts at about P14, a floor of observation and not an onset), RECOVERED for none in the mouse. The mouse timing arms are small and not uniformly successful (S8: a P3 arm, n = 3, at about 67 percent from about day 24; a P5 arm, n = 7, at 75 percent from about day 35 to day 300; no P0 arm and no P4 survival curve; treated arms compared with wild type, so 'ns' is not equivalence), which the main-text sentence that any time point between P0 and P5 fully rescues does not state. The only genetic add-back after a documented phenotype is organoid: neuron-directed AAV9-WWOX at week 10 on a hyperexcitability seen at week 7 (a different cohort), read at week 16, persistence unmeasured, radial-glia abnormalities not corrected (`paper_registry_current#PAPER 094`). The gap named in the title of this lead therefore stands, sharper: there is no post-onset mouse arm, and the model's life span (death at about three weeks) is why. Nothing here bounds the window in either direction (`DIS-033`). Sources: `drug_repurposing/rescue_window_it6_20261029.md`, independently verified; receipts `FTR-20261029-42422765-01`, `FTR-20261029-42397075-01`.

#### DL-MOL-005
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P7 and P5; EXPLORATORY; Status `maturing`, the Belief, the Causal statement and the proposed experiment are not edited).** The `rescues` arrow of the Causal statement is early-window prevention in the null mouse, not recovery of a manifested deficit (see the update on `DL-MECH-011`). Two further cautions. (1) The dose arms are not separated by a resolved difference in vector DNA or mRNA (7 of 8 comparisons), protein at P30 shows an untested trend, and the LOW dose already carries several-fold wild-type bulk protein in cortex and hippocampus while the cerebellum stays below wild type at both doses: bulk lysate protein does not track the survival step, and the carrier of the phenotype (region, cell type, time, a peripheral tissue) is unidentified. (2) The add-back is regionally uneven and supraphysiological in survivors. The missing datum named in the proposed experiment (treatment after onset or in an older animal, in a hypomorphic model) is unchanged, and no inducible neural Wwox model is known (a bounded search, not proof of absence). Sources: `drug_repurposing/rescue_window_it6_20261029.md`, `drug_repurposing/wwox_function_reference_it6_20261029.md` (row W12); independently verified.

#### DL-MECH-007
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P7; EXPLORATORY; Status, Causal statement and earlier bullets are not edited).** 'Ectopic WWOX rescues the organoid phenotypes' covers three designs with different window states: the stem-cell safe-harbour knock-in (W-AAV, present before differentiation: PREVENTION by construction, partial and supraphysiological); the lentiviral arm of the 2021 paper (day 35 of culture, 'week 6' in a legend, first excitability recording at week 7: EARLY-WINDOW, while knockout DNA damage and astrocyte markers are already measured at week 6); and the neuron-directed AAV9 arm of the 2026 organoid paper (`paper_registry_current#PAPER 094`; week 10 on a hyperexcitability seen at week 7 in a different cohort, read at week 16, persistence unmeasured), the only add-back after a documented phenotype, which reduced hyperexcitability to a level similar to wild type and did not correct radial-glia abnormalities. Organoid age is culture age, not gestational age. The platform is the one place where a post-onset arm exists; its limits are one endpoint family, one time point and the missing same-organoid baseline. Sources: `drug_repurposing/rescue_window_it6_20261029.md` sections 2.3 and 2.4; receipts `FTR-20261029-34268881-01`, `FTR-20261029-42397075-01`.

#### DL-MOL-001
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P9 and P11; EXPLORATORY; the Status `maturing`, the Belief, the Causal statement and the proposed experiment are not edited).** The 'dipendenza NMDAR dimostrata' in Evidenza supports only that the bursting NEEDS NMDAR activity: d-APV is a complete competitive block (50 uM; 51 bursts, 5 slices, 3 animals; no test on that arm), and the dependence is not shown to be a raised NMDAR function. Three readings fit it and are not ranked: NMDAR gain; permissive necessity in a network whose pyramidal neurons rest about 5.6 mV more depolarised and whose spontaneous inhibitory current amplitude is about half; an AMPAR-led drive. The inferred arrow `NMDAR_antagonist —decreases→ bursting` is expected from an AMPAR antagonist too (AMPAR depolarisation relieves the magnesium block), so a drug effect on bursting does not discriminate. The class comparison (memantine, a GluN2B negative allosteric modulator, perampanel, competitive and glycine-site agents) is in card `F04_nmdar_intervention_class`, which supersedes the discriminator that card F01 pre-registered (memantine against perampanel; F01 is kept as the record of 2026-10-27): the discriminating measurement is the isolated NMDAR current under voltage control (E1), not a drug arm. In this preparation a pore blocker is a poor first discriminator (incubation solution 1.3 mM Mg2+, recording bath not stated, a GluN2D-containing interneuron effect would raise bursting). Extracellular magnesium as the physiological gate is carried separately as `HYP-20261029-01`. No receptor-level measurement exists in any Wwox system. Sources: `drug_repurposing/nmdar_pharmacology_it6_p9_20261029/README.md`, `drug_repurposing/supplement_diet_it6_p11_20261029/README.md`; independently verified. Not medical advice; no dose.

#### DL-BIO-085
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P5; EXPLORATORY; a DESIGN, nothing measured; Status `open` and earlier bullets are not edited).** The 'functional readout proximal to the gene' that this record says is missing has been specified from the published WWOX assays (`drug_repurposing/wwox_function_reference_it6_20261029.md`, independently verified): no assay in the record is a validated ruler of function per molecule. The enzymology paper's activity is a crude bacterial extract with no variant, no purification and no dead mutant (13 of 14 Km values below the lowest substrate concentration); the catalytic-triad mutants exist only as unpublished observations in a review; the nearest quantitative arm set (null cells, wild-type add-back, WW1 mutant, empty vector; glucose uptake, n = 3 per arm) reports the WW1-dependent axis only; the SDR-region binding probe L404A is a negative control for GSK3beta binding, Tau and neurite readouts only. The proposed ruler is a wild-type titration at measured per-cell protein in one isogenic null background, with the variant placed on that curve and a per-molecule binding-competence ratio beside it; a rise in abundance is read as rescue only when the compound arm moves along the variant's own curve with transcript flat and the null line unaffected, and a result on the Tier 1 curve is read as recovery of the WW1-dependent axis, not of SDR-domain function, unless an SDR-region readout agrees. No function per molecule has been measured for any WWOX allele. This is the design that the card A01 next-measurement field now carries.

#### DL-REPO-002
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P10; EXPLORATORY; the heading 'direzione RISOLTA' and the earlier bullets are not edited; read the CORRECTION of 2026-09-26 (`B3`) together with this update as the current state).** The direction of the glial change is NOT resolved across the Wwox models, and the lead stays an abstention (card `J01_glial_reactivity_modulation`; no WWOX assertion for any compound): the rat lde/lde cortex shows LOWER GFAP-positive and Iba1-positive cell density from PND 5 to 21 (by its authors' account opposite to the other models); the null mouse (P20) and the P47T knock-in show an excess; the human knockout organoid at week 15 shows no reactive-astrocyte or cytokine transcript programme (microglia absent; four against two libraries; transcript level); the P47T thresholded sheets do not list the canonical reactive or cytokine transcripts. Species, allele, region, assay and age window are confounded. Every glial read in the mouse is after the first seizures (spontaneous seizures reported from P9 in the neuron-restricted deletion), a neuron-restricted deletion already shifts astrocyte-activation-type transcripts at P17, no Wwox is detected in rat microglia and the astrocyte-specific deletion was never scored for gliosis, so no glial compartment can be assigned as cause. The compound precedents found (anakinra and tocilizumab in acute immune-triggered syndromes, minocycline, a caspase-1 inhibitor, STAT3 work in neonatal injury) are abstract level, uncontrolled or uninformative for long-term outcome and none is a WWOX-system datum; the catalogue holds no WWOX context for any of the 642 non-excluded intervention-target rows, and IL1R1 and CASP1 were added to the need because the two IL-1-axis agents with epilepsy exposure were unreachable from it. The discriminating experiment is a within-species time course of glial density before and after the first spike (P5 to P17, both readouts in cortex and hippocampus, animal as unit). Sources: `drug_repurposing/partial_benefit_it6_p10_20261029/README.md`, independently verified. Not medical advice; no dose.

#### DL-MECH-012
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P10; EXPLORATORY; nothing above is edited).** 'In all tissues loss of WWOX increases inflammation' meets a counter-sign in the brain: the rat lde/lde cortex shows lower GFAP-positive and Iba1-positive cell density from PND 5, the human knockout organoid shows no reactive programme at week 15, and the neuron-restricted rescue that lowers GFAP in the null mouse also stops seizures and restores survival, so the fall does not say which route it used. See the update on `DL-REPO-002` for the full reading and the discriminating time course.

#### DL-MECH-173
Position: before the closing "Not medical advice" bullet of the record.

> - **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P3 and P4; EXPLORATORY; COMPUTATIONAL_RESULT at transcript level, never eIF2 alpha phosphorylation, ATF4 protein, translation or flux; the Status `open`, the Causal statement and the earlier updates are not edited).** The sign of the human ISR transcript signal stays UNRESOLVED after a third system. In the mouse P17 deposit with an unambiguous deletion (hippocampus: neuron-targeted, neural-stem-and-progenitor-targeted and germline-null; cortex: neuron-targeted; 2 to 4 animals per arm; summed Wwox TPM 85, 94, 91 and 68 percent lower) the pre-declared ISR target set sits inside its matched null in every contrast (centred means +0.135, -0.134, -0.019, +0.051; none animal-separated), so the mouse sides with neither the organoid (lower) nor the shRNA deposit (higher). The defensible statement is 'no resolvable sign at about 0.3': at animal level an organoid-sized fall is excluded at about 2.5 SE (neuron-targeted hippocampus), about 5 SE (null) and about 4.7 SE (cortex) but NOT in the neural-stem-and-progenitor-targeted contrast (2 against 2 animals), and Chac1 is a few TPM, Sesn2 5 to 8 TPM and Trib3 below 1 TPM in this tissue, so the three-gene organoid set is not evaluable. Atf4 mRNA is lower in all four contrasts (uncentred log2 -0.55, -0.97, -0.60, -0.71; animal-separated in two): an mRNA observation, not an ISR call (ATF4 is translationally controlled) and not support for either human system. The positive control passes (myelin and oligodendrocyte transcripts -0.8 to -1.8 in all four contrasts); the germline-null contrast is exposed to a wild-type against Cre-line control difference (transcriptome-wide IQR about +-0.35 to 0.41, against +-0.13 between the two Cre-line control groups); sex is not balanced; the Cre drivers, the control genotype and the allele are not stated by the deposit. A census of public records found none that measures, in a WWOX-deficient system, a proteome or phospho-proteome, translation, eIF2 alpha phosphorylation or PERK/GCN2 activation, ATF4 protein or an enzyme and flux readout (OCR, ECAR, PDH, NAD(H)); the fly head metabolomics deposit is still not public, and the fly head RNA deposits show no visible Wwox change in the deposited counts, so they offer no check of perturbation depth. Which measurement to do first is a judgement: a matched protein and phospho-protein measurement with target mRNA is less likely to be superseded than another transcript re-analysis. Sources: `drug_repurposing/wwox_data_census_it6_20261029.md`, `drug_repurposing/mouse_wwox_p17_it6_p4_20261029/README.md`; independent rerun byte-identical, nine wording defects repaired.

#### DL-MECH-020
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P4; EXPLORATORY; COMPUTATIONAL_RESULT at transcript level; Status `open` and the Statement causale are not edited).** One more neural system without transcript support for the middle link: in mouse P17 brain with Wwox deletion (four contrasts, 2 to 4 animals per arm) Pdk1 has no consistent sign (-0.20, +0.32, +0.13, cortex -0.10) and the four-gene PDK family signs differ between contrasts (+0.39, +0.19, -0.30, +0.08), all inside their matched nulls; Hif1a is slightly higher in sign in the three hippocampal contrasts (+0.22 to +0.28; a per-gene row, not a call). The finding stays the absence of support at PDK1, not a demonstrated decrease; the glycolysis sets are not extended to the mouse (see the 2026-10-29 update on the LDH-lowering lead). Source: `drug_repurposing/mouse_wwox_p17_it6_p4_20261029/README.md` sections 4 and 5. Association is not modulation is not rescue. Not medical advice.

#### DL-REPO-004
Position: before the closing "Not medical advice" bullet of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P4; EXPLORATORY; COMPUTATIONAL_RESULT; Status `open` and the potency statements are not edited).** 'LDHA and the HIF-type glycolysis set are higher in both human neural systems' is not extended to the mouse: in P17 mouse brain with Wwox deletion the 10-gene lactate set is -0.09 and -0.19 and the 19-gene panel -0.07 and -0.09 in the two cell-targeted hippocampal contrasts, nothing outside the null there (the germline-null contrast, -0.18 and -0.21, is the one exposed to the wild-type against Cre-line control difference, and only the 19-gene panel leaves its null there). The human statement stays set-dependent and two-system; this is not a refutation (different species, tissue and composition). Lactate, ECAR and LDH activity remain unmeasured in any WWOX neural system. Transcript is not flux; the falsifying experiment above is unchanged.

### therapeutic_hypotheses_ledger_current.md (6 ops, record_scoped_edit.py, addressed by the exact heading of each hypothesis; plus the appended record)
#### HYP-20260709-01
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P4; EXPLORATORY; transcript level; the Status, the ranking line and the score are unchanged).** The CURRENT READING stands with one more system without PDK1 support: mouse P17 brain with Wwox deletion shows no consistent Pdk1 sign (-0.20, +0.32, +0.13, cortex -0.10), inside the null; absence of support, not a demonstrated decrease (see `DL-MECH-020`). Not medical advice.

#### HYP-20261026-10
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P3 and P4; EXPLORATORY; COMPUTATIONAL_RESULT; the Status `generated`, the absence of a ranking line and the reopening condition are unchanged).** A third system does not break the tie: in mouse P17 brain with an unambiguous deletion (four contrasts, 2 to 4 animals per arm) the ISR target set is inside its matched null in every contrast with no resolvable sign at about 0.3 (an organoid-sized fall is not excluded in the 2 against 2 stem-and-progenitor-targeted contrast; Chac1, Trib3 and Sesn2 are at or below a few TPM), while Atf4 mRNA alone is lower in all four (an mRNA observation, not an ISR call). A census of public records found no proteome, phospho-proteome, translation, eIF2 alpha phosphorylation, ATF4 protein or flux record in any WWOX-deficient system, so the first experiment stays the matched protein and phospho-protein measurement with target mRNA, not another transcript re-analysis. Details in the update on `DL-MECH-173`. Association is not modulation is not rescue. Not medical advice.

#### HYP-20261026-11
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P4; EXPLORATORY; COMPUTATIONAL_RESULT; Status `generated`, no ranking line and the reopening condition are unchanged).** The LDHA and glycolysis rise is seen in two human neural transcript systems only; it is not extended to mouse P17 brain with Wwox deletion (10-gene set -0.09 and -0.19 in the cell-targeted hippocampal contrasts, 19-gene panel -0.07 and -0.09; nothing outside the null there). Set-dependent, two-system, transcript level; the falsifying experiment is unchanged (see `DL-REPO-004`). Not medical advice.

#### HYP-20260709-08
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P5 and P6; EXPLORATORY; NOT WWOX EVIDENCE for every external item; Status, tags and the minimal falsifying experiment are unchanged).** (1) Order of work: the wild-type function ruler first (see the update on `DL-BIO-085`), then the three-fraction fate experiment, then the lever panel; the ruler is what converts a fold gain in protein into a function number. (2) Route blockade of a destabilised cytosolic enzyme returned protein of unequal worth in the best-resolved precedent, cystathionine beta-synthase (a PLP tetramer; NOT WWOX EVIDENCE): stabilisation sufficed for a regulatory-domain allele in mouse liver, improved three catalytic-domain alleles and failed for one; an ERAD arm raised the activity of one allele without a change in its half-life while another gained both; the better drug did not track proteasome inhibition; effective exposure was toxic and tolerated exposure gave no significant activity gain for the allele that had rescued at high exposure; wild type rose alongside. In ASPA C152W (`paper_registry_current#PAPER 434`) blocking the Hsp70/Hsp110 route accumulated insoluble, inert protein. Whether a stabilised Q230P-class protein is active is predicted by neither: if it behaves like a catalytic-domain allele stabilisation alone is expected to be insufficient, and the repository red-team record expects a lysosomal route, which would make a proteasome arm the wrong lever; both expectations are unranked. (3) No experiment gave a route blocker, chaperone or proteostasis modulator to a WWOX missense system beyond the P252A route arms (searches screened by title, not proof of absence), and no precedent separates stabilisation from a transcript effect (transgene mRNA under treatment is absent from all four CBS papers). The prediction fails if a stabilised Q230P-class protein is active on the ruler. Card A02 was revised; A05 stays an abstention. Sources: `drug_repurposing/wwox_function_reference_it6_20261029.md`, `drug_repurposing/broad_recovery_it6_p6_20261029/README.md`; independently verified; receipts `FTR-20261029-37319242-01`, `FTR-20261029-38051092-01`, `FTR-20261029-39041895-01`, `FTR-20261029-31605637-01`, `FTR-20261029-33914734-02`. Not medical advice.

#### HYP-20261027-01
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P9 and P11; EXPLORATORY; Status `generated`, no ranking line and the reopening condition are unchanged; the minimal falsifying experiment above is superseded as DISCRIMINATOR by card `F04_nmdar_intervention_class`, and F01 stays as the record of the registration of 2026-10-27).** Three readings of the d-APV datum are unranked (NMDAR gain; permissive necessity with a depolarised resting potential and a halved inhibitory current; AMPAR-led drive), and neither memantine nor perampanel discriminates them in this preparation: an AMPAR antagonist is expected to stop an NMDAR-dependent burst whichever reading is true, and a pore blocker is state-dependent (incubation solution 1.3 mM Mg2+, recording bath not stated, block of GluN2A rises with intracellular Ca2+, an interneuron GluN2D effect would raise bursting). The first measurement is the isolated NMDAR current under voltage control, with resting potential and input resistance in the same cells, in knockout, heterozygote and wild type, animal as unit. A GluN2B-selective negative allosteric modulator is the first drug arm (a ceiling below complete block gives a fraction F* that is defined only if bursts are abolished at the plateau), with a wild-type slice made to burst as the positive control and a time-matched vehicle; memantine is the translation probe afterwards, with Mg2+ and voltage stated. The baseline burst rate is printed twice, 2.7-fold apart (2.29 against 0.84 per minute), and must be resolved before counting time is set. What would close the strand: an isolated current that is not raised with F* near complete, or a generic response in wild-type slices made to burst, means a symptom tool without a window and the mechanism-matched levers upstream. Chronic NMDAR block in a developing brain carries a developmental signal (abstract level) and burst control is not benefit. Extracellular magnesium is carried separately as `HYP-20261029-01`. Not medical advice; no dose.

#### HYP-20260705-02
Position: after the final line of the record.

> - 🔵 **UPDATE 2026-10-29 (`BATCH_20261019_027`, `CC-20261029-INTEGRATOR-IT6-REGISTRIES-01`; IT6 P10; EXPLORATORY; Status `flagged` and the ranking line are unchanged).** The glial premise of this bridge has a counter-sign: the rat lde/lde cortex shows lower GFAP-positive and Iba1-positive cell density, the human knockout organoid shows no reactive programme at week 15, and no WWOX-system pSTAT3 or pJAK2 measurement exists; see the updates on `DL-REPO-002` and `DL-MECH-012`. Not medical advice.

#### HYP-20261029-01 (new record, plain append at the end of the file)
> The record is the text of `therapeutic_hypotheses_ledger_current.md` from the heading `### HYP-20261029-01` to the end of the file: Track A, route BENEFICIO_PRECOCE, tag IPOTESI, status `generated`, no ranking line, card `P11_magnesium_nmdar_gate`, the falsifiable statement, the Wwox evidence PRO, the counter-evidence and limits, the safety line (unassessed), the minimal falsifying experiment and the reopening condition. It is not reproduced here to keep one source of the wording.

### dismissal_ledger_current.md (0 ops)
None.

## Normal edits (files that are not scientific current files or ledgers)
| File | Edit |
|---|---|
| `disease-models/wwox/analysis/mechanism_intervention_map.md` | M1 cell qualified; CHAIN A boundary 5 (prevention, not recovery); CHAIN B node line replaced in place ('NMDAR ACTIVITY IS REQUIRED ...') and an update paragraph; R-01 WWOX_DIRECT_EVIDENCE cell qualified; R-02, R-06, R-09, R-10, R-11 update paragraphs (ledger ids deliberately not named in R-09, R-10 and R-11, whose SOURCE_IDS are curated so that the join does not inherit unrelated families of papers) |
| `framework/scripts/test_repurposing_join.py` | new class `SupersededWordingGoneIT6` (6 tests, positive checks plus the exact old strings replaced in place) |
| regenerated | `join/*`, `coverage/coverage_matrix.json`, `p5/cells.json`, `p5/tables_deep.md`, `view/index.html`, `view/index_shareable.html`, `view/shareable_package`, `research/repurposing_batch_selection_20261029_module.md`, `analysis/pathograph_inventory.md`, `analysis/data/pathograph_export.jsonl` |

## Proof that the consumers use the corrected wording
`framework/scripts/test_repurposing_join.py::SupersededWordingGoneIT6`: the map no longer calls the NMDAR node 'pharmacologically established with d-APV inside the WWOX system' and states that NMDAR activity is required while a raised NMDAR function is not shown; the map, the cards C01 and C04, the needs, the p5 tables, the join output, both views and the handoff no longer contain 'R-class demonstrated' or 'would act in humans at the stage a patient is treated' and say early-window and 'would recover a manifested deficit'; the six claims carry the wave note and keep their Status; the ledgers carry the dated UPDATE bullets while their earlier headings and wording are still there (append-only); the magnesium hypothesis exists with Status `generated`; every receipt a paper reading update names is recorded in the ledger; the working model keeps its version and does not name this batch. A mutation of the replaced map string is caught.

## Needs a verifier
The ledger bullets and wave notes restate independently verified material and add no new reading. Owed to a later actor: the choice of which records receive a note is the integrator's (the reviewer may ask for `CLAIM 030`, `CLAIM 036` or the working-model line named above); the P5 verifier's open items (Figure 3b fold values, the 78 to 89 percent arithmetic, P282A against P252A) are not carried into any registry text.

## BATCH DISPOSITION

**Verdict:** PROPAGATED (research layer and registry notes; working model `WM_v7.28` preserved, no bump)
**Batch:** `BATCH_20261019_027` (2026-10-29, MANUAL, ACTOR_ID `integrator`, task `ORCH-ROADMAP-IT6-20261029`, registries step)

- **Gene addition as prevention or early-window; organoid add-back qualifiers:** propagated to `CLAIM 004`, `CLAIM 011`, `CLAIM 040`, `CLAIM 002` (wave notes), `DL-MECH-011`, `DL-MOL-005`, `DL-MECH-007`, `PAPER 011`, `PAPER 005`, `PAPER 094`, `PAPER 039`, `PAPER 019`, `CORPUS P318`, the matching literature-log records, and the map.
- **NMDAR dependence versus gain; magnesium gate:** propagated to `CLAIM 021` (wave note), `DL-MOL-001`, `HYP-20261027-01`, the new `HYP-20261029-01`, `PAPER 031`, and the map.
- **ISR sign, census, PDK1 and glycolysis in the mouse:** propagated to `DL-MECH-173`, `HYP-20261026-10`, `DL-MECH-020`, `DL-REPO-004`, `HYP-20260709-01`, `HYP-20261026-11`, and the map.
- **Glial sign conflict:** propagated to `CLAIM 005` (wave note), `DL-REPO-002`, `DL-MECH-012`, `HYP-20260705-02`, `PAPER 021`, `PAPER 006`, `PAPER 004`, `PAPER 007`, and the map.
- **Function ruler and route blockade:** propagated to `DL-BIO-085`, `HYP-20260709-08`, `PAPER 434`, and the map.
- **Unchanged:** every `Status`, `Type`, `Title` and `Summary`; the working model; the dismissal ledger; the receipt ledger; the Status and ranking of every hypothesis touched.

## Addendum 2026-10-29 (repair after the independent adversarial review; same batch, see the batch record `ADDENDUM_REPAIR_20261029`)
The review (`research/locator_audits/2026-10-29_it6_batch_review.md`, no HIGH) found D1 to D13; D2 to D13 are wording repairs of this batch's own notes (each re-checked against the cycle verifier reports first), made as record-scoped `replace-within` edits of the batch's own text (earlier ledger wording untouched): 3 claim notes (`CLAIM 011`, `CLAIM 002`, `CLAIM 021`), 3 paper updates (`PAPER 094`, `PAPER 434`, `CORPUS P318`), `LIT-0706`, 4 discovery-ledger bullets (`DL-MECH-011`, `DL-MECH-007`, `DL-MOL-001`, `DL-REPO-002`), the `HYP-20260709-08` and `HYP-20261027-01` updates and the new `HYP-20261029-01`, and the map. The statement above that the working model is left unchanged is SUPERSEDED by D1: the working-model wording is filed and applied as the separate MINOR candidate `CC-20261029-INTEGRATOR-IT6-WM-01` (`BATCH_20261019_028`, `WM_v7.29`).
- D2: motor score stated as partial and not normalised, gliosis at the high dose only (map boundary 5, `DL-MECH-011`).
- D3: 'inert' replaced by 'insoluble pellet protein with no measurable activity (yeast and U2OS; earlier reports also found no residual activity)' (map R-09, `HYP-20260709-08`, `PAPER 434`, `LIT-0706`).
- D4: the `HYP-20261029-01` falsifier compares with wild-type slices made to burst by raised K+ or 4-aminopyridine, not by lowered Mg2+.
- D5: arithmetic stated as 'the reachable rise may fall short' (about +42 percent for a cortical-type slope against +31 percent in healthy mice); uncorrected liquid-junction potential and the shared burst incidence added to the limits.
- D6: d-APV described as observed (50 uM eliminated the bursting; a competitive antagonist; no test on that arm) in `CLAIM 021`, `DL-MOL-001`, the map and `HYP-20261029-01`.
- D7: the stale 'actionable node NMDAR/gap-junction' summary lines of the map (M2 row, key-unknown 2, the programme table) restated.
- D8: the negative-existence claim on `CORPUS P318` reworded to 'the only such rescue noted in the readings of this batch'.
- D9: radial-glia wording restricted to the knockout lines, with the abstract's neuronal description of the patient-line impairment.
- D10: 'in the corpus' replaced by 'read in this corpus' with the bounded search stated.
- D11: F* and the closing criteria stated as exploratory proposals to be time-stamped before unblinding.
- D12: 'first drug arm' and 'order of work' stated as proposals, not rankings; `Lever: 3 (repurposing, nutrient class)`; `INFERENZA` dropped as a tag.
- D13: the `DL-REPO-002` heading stated as superseded in effect; the 642-row statement labelled 'by the catalogue's own fields'.
