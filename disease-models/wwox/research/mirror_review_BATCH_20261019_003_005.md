# MIRROR review — BATCH_20261019_003, _004 and _005 (ex post, Annex C.2 format)

> Reviewer: ACTOR_ID `mirror` (not the producer). Scope: base `7b214f1c`, batch commits `7b8eaee7` (003), `70b874ce` (004), `f8bb7e9b` (005); reports `batch_report_BATCH_20261019_003.md` to `_005.md`; earlier review `mirror_review_BATCH_20261019_001.md`.
> Read-only toward every repository file except this one. A finding is a new task for the change's author, never a hold on a landed batch (LEGEND_CORE §21e). Not medical advice.

## Verdict

**CONFIRMED. No BLOCK-class defect. Eleven FINDINGs, none touching a claim Status, Type, Summary or baseline sentence.** CONFIRMED means no further defect found in the sampled evidence bundle, not "true". The sample is stated per item below; unsampled records were checked only mechanically.

Gates re-run by this reviewer on `main` at `f8bb7e9b` (HEAD equals it):

- `legend_lint.py .`: VERDICT WARN, 0 BLOCK (15 `WARN_BUT_PROCEED`, all `UNLINKED_SUPPORT` or `POSSIBLE_CONTRAST`; none names a record of these batches).
- `fulltext_receipts.py verify`: OK, 654 chained receipts, tail anchored.
- `growth_anchors.py check`: PASS (papers 389, corpus 376, literature 660, unread premises 0).
- `public_release_gate.py`: VERDICT PASS, 0 BLOCKS, 29 REVIEW lines. All 29 were checked line by line against `7b214f1c`: every flagged line is pre-existing (the 7 lines in files the three batches touched are unchanged text).

## STEELMAN

The three batches discharged a large registry debt (89 PAPER and 76 LIT records) with record-scoped edits and no `FULL_FALLBACK`. The Mirror repairs of batch 001 were taken up one by one and re-checked against the source rather than the review (the batch report even adds a defect the review missed: the VABAM cohorts were called "read in full" and are partial). The new records carry their earned negatives almost everywhere sampled: protocol with no results, abstract that overstates its own table, units and statistic inconsistencies, "no mitochondrial marker row", "WWOX occurs zero times". Every number in every new `Role` line was matched mechanically against the dossier, manifest or artefact (below) with no unexplained figure.

## Measured scope

- Item 1 diff: `claim_registry_current.md` and `working_model_current.md` from `7b214f1c` to HEAD, compared at word level.
- PAPER: all 89 new records (311-399) number-matched against dossier, manifest or full-text artefact; 33 read by eye (311-314, 316, 318, 322, 325-328, 333, 334, 338, 340, 356, 357, 361, 362, 367, 370, 383, 384, 387, 392, plus 324 and 363 in part); 15 existing records that received notes (005, 011, 015, 018, 021, 022, 023, 031, 061, 071, 093, 118, 129, 130, 204) read.
- LIT: all 76 new records checked mechanically against their PAPER record (PMID, evidence depth, receipt id): 0 mismatches. Only one (LIT-0640) was read in full, so "10 LIT records" is met mechanically and by one reading, not by ten readings. LIT-0561 read for the F3 repair.
- Leads: 17 of the 28 new leads read (DL-MECH-117, 121, 133, 136-139, 141-143, 145-148, 150, 153, 156, 158, 162) and the tag of all 28 listed.
- Primary-source spot checks: PAPER 361 (artefact HTML: 10 micromolar PMA, 30-minute co-localisation, release at 60-120 minutes), PAPER 356 (OR 3.735 and HR 1.621 print with three decimals; the record rounds), PAPER 367 numbers, PAPER 340 (56 to 22 percent), and the CLAIM 020 negatives against the PAPER 015 full text (zero hits for ketogenic, vigabatrin, steroid, ACTH, stimulation; seven antiseizure drugs listed; computed tomography at 35, video-EEG at 36; CNV analysis performed, outcome not reported).
- Privacy scan: 34,716 added lines in `disease-models`, `framework/state` and `ledger`.

## Per-item verdicts

| # | Item | Verdict |
|---|---|---|
| 1 | Claim Status, Type, Summary, baseline sentences | **OK**, one placement FINDING (M1) |
| 2 | Repair of 001: B1, F1-F6 | **OK** for B1, F1, F2, F3, F5, F6; **FINDING** F4 repaired only in part (M2) |
| 3 | 89 PAPER, 76 LIT, 28 leads, substitute labels, T3/T4 | **OK** on fidelity and labels; **FINDING** M3 (lead wording), M4 (mTOR premise), M5 (grades) |
| 4 | CLAIM 028 source line; CLAIM 009, 017, 020, 031 notes | 009, 017, 020, 031 **OK**; 028 **FINDING** M6 |
| 5 | Complement and Liu 2021 corrections; FT-090 | **OK**, lossless; one FINDING on wording (M7) |
| 6 | Public-edition privacy | **OK** on gate and individual linkage; **FINDING** M8 (report overstates) |
| 7 | Registry-scale deferral | **FINDING** M9: tell the operator now |

## Item 1 — what changed in the claim registry and the working model

Changed lines in `claim_registry_current.md`: the CLAIM 001 wave note (B1 repair), CLAIM 009 (a wave note appended), CLAIM 017, 020 and 031 (new evidence-boundary lines), CLAIM 028 (Source and Wikilinks lines), CLAIM 042 (CDKL5 and partial-depth additions). `Status`, `Type`, `Pathway`, `Transferability` and the baseline sentences of all 47 claims are byte-identical to `7b214f1c`. `working_model_current.md`: only the `Version` and `Last update` lines (WM_v7.21 to v7.24). The reports' statement "no Status, Type or Summary changed" is true.

**M1 — FINDING (placement).** The CLAIM 009 wave note was appended to the end of the `**Summary:**` line, not added as its own `**Evidence boundary:**` line. The baseline sentence is untouched and wave 13 already did the same, so this is not a change of claim, but a tool or reader that treats the Summary field as the claim now reads a 2026-10-20 evidence note inside it. Move the note to its own line.

## Item 2 — repair of the 001 findings

- **B1 (CLAIM 001, DL-MECH-133, Scientist D wave note): repaired.** The sentence now reads that both cohorts associate hormonal therapy with symptomatic VABAM and neither with the MRI finding alone, that they point the same way and are underpowered; the depth is corrected to partial; the correction is marked in place and the candidate body keeps the old sentence under a CORRECTION line. `conflicting evidence` unchanged. No live text still says the cohorts disagree.
- **F1 (CLAIM 042, DL-MECH-121): repaired.** CDKL5 0 of 10 now sits next to "47 to 100 percent", the range is called a range among responders, and the partial depth of PAPER 269 is named in the `PREMISE_TAG`.
- **F2 (PAPER 097): repaired.** The figure statement is marked "as of the earlier receipts only; superseded by the third receipt", and the currency of the textual negatives is declared unknown.
- **F3 (PAPER 263, LIT-0561): repaired.** The "2021" wording is replaced by what PubMed returns (2019, DOI of the other article); LIT-0561 now points to the identity note.
- **F4 (DL-MECH-117): repaired in part.** See M2.
- **F5 (PAPER 291, 289): repaired.** The support sentence in PAPER 291 is marked "proposed" and "parked"; PAPER 289 carries the parked marker.
- **F6 (scale ack count): repaired** in a new growth-anchor note; the anchor value is untouched.

**M2 — FINDING.** DL-MECH-117 is recast as a conditional "where WWOX and HIF1A transcripts are uncorrelated", which is the right shape. But the body still concludes "in these two data sets (one leukocyte series and one TCGA analysis) the ratio-based reading adds nothing". Only the leukocyte series is shown uncorrelated (rho -0.05 and -0.12); for TCGA the lead itself says the favourable group has WWOX up and HIF1A down, which is the opposite of uncorrelated. The arithmetic-coupling argument therefore covers one data set, not two. Restrict the sentence to the leukocyte series and state that the TCGA leg is not shown to meet the condition.

## Item 3 — records, leads and labels

Fidelity: the numbers of all 89 new `Role` lines were matched against dossier, manifest or artefact. The only unmatched figures were three-decimal values printed in the paper and rounded in the record (3.735 to 3.7, 1.621 to 1.62), a computed percentage and the paper's own reference numbers; none changes a conclusion. Every sampled record says less than or as much as its reading: it names the abstract-versus-table conflict (PAPER 311, 313, 316), the missing control (PAPER 318), the unmeasured compartment (PAPER 361, 362, 367), or the absence of the word WWOX (PAPER 328, 327, 387). Negatives are kept (PAPER 364 no data of its own, PAPER 369 no expression effect, PAPER 387 no loss-of-function datum). IPOTESI: 22 of the 27 new DL-MECH leads are IPOTESI (DL-METH-125 is a method rule); DL-MECH-136 and 139 INFERENZA, DL-MECH-137 and 146 ESPANSIONE, DL-MECH-147 DATO. The DATO tag on 147 is defensible (it restates a review's trial numbers and says "not a hypothesis").

Substitute labels: every new record that is not WWOX-direct carries "NOT WWOX EVIDENCE" (all of 311-355 and 370-399 except 324, 326, 383, 387). PAPER 326 (a Mendelian-randomisation gene list that names WWOX once) carries the label only through `clinical relevance: BACKGROUND — non-WWOX ... not WWOX evidence`, which is enough. The 14 records of batch 004 and PAPER 324, 383 and 387 are WWOX-direct and are not labelled substitutes, correctly.

**M3 — FINDING (lead wording).** DL-MECH-145 says "Hypoxia rescued disease only where an electron-transport lesion lowers tissue oxygen use and raises tissue oxygen". PAPER 325 says hypoxia rescues "when" that holds. "Only where" turns a sufficient condition seen in two mouse models into a necessary one: a distortion built from two carried sentences, each correct alone. Replace "only where" by "where, in two mouse models". Same lead: the tag IPOTESI is right, the wording is not. DL-MECH-139 says lactate and respiration "stay impaired after epinephrine restored pressure"; PAPER 318 records that the design has no epinephrine-alone group and that the shock-only group was sampled at 15 minutes after dying, so "stay" implies a persistence the study cannot show. DL-METH-125 carries that caveat; DL-MECH-139 does not. Add it.

**M4 — FINDING (premise).** DL-MECH-148 predicts that fasting protection is intact in Wwox+/- animals "because mTORC1 sensing is not shown to be altered by WWOX loss". The paper registry itself holds a record in which WWOX co-immunoprecipitates with mTOR and raises phospho-mTOR and phospho-p70S6K (overexpression in cancer cells), and another that reads "mTOR/p70S6K" in a WWOX-manipulated line. Neither is a neuron or a null, but the premise as worded is false for the repository. Say "no record here measures mTORC1 signalling in a Wwox-deficient neuron; cancer-cell overexpression records report a WWOX-mTOR association". The prediction is fixed before data, which is the point of the lead, and stays.

**M5 — FINDING (transferability grades).** The batches took defaults and the defaults disagree with each other. Counts in the 89: T4 54, T3 35. Same class, different grade: Shin 2023 (WWOX-direct, non-neural, partial knockdown, one line) is T4; Hong 2009 (WWOX-direct, non-neural, overexpression, one cancer line) is T3; the 14 records of batch 004 (overexpression in leukaemia, lung and other lines) are all T3 "for every new record"; a paediatric enteral-refeeding cohort (PAPER 350) is T3 and a type-1-diabetes ketone study (PAPER 351) is T4. I found no definition of T3 and T4 in `framework/` or the registry header that would arbitrate. Either define the scale in one sentence where the grade is written and re-grade the 89, or stop grading class-level substitutes (the grade is meaningless for a record labelled "no datum transfers to ..."). No record's grade moves a claim, so this is a FINDING, not a block.

## Item 4 — claim notes

- **CLAIM 009 wave note: OK on content.** Verified against the artefacts: PAPER 361 (Jurkat, 10 micromolar PMA, one confocal field per time point, co-localisation visible at 30 minutes and released at 60-120) and PAPER 357 (the one mitochondrial sentence rests on a then-submitted paper). The note ends "the status and the INFERENZA type stand" and says nothing in the reading measures respiration, ROS, ATP or mitophagy. It does not overreach. Placement: M1.
- **CLAIM 017, 020, 031: OK.** CLAIM 020's negatives are text-verified (above), including the careful "CNV outcome not reported" rather than "no CNV analysis". CLAIM 031's definition note is tagged as the source review's statement of a consensus definition, with a revival trigger. CLAIM 017's survival-curve figures (about 0.62 against 0.26, overlapping bands, three-group log-rank) rest on a figure reading of PAPER 018 that this reviewer did not re-open; the other half of that note (n = 1 does not overturn a cohort rule) is arithmetic.
- **CLAIM 028 source line (Shin; PAPER 102, 113-115): FINDING M6.** The line adds PAPER 383 to Source and Wikilinks only, states the system gap (one line, partial knockdown, one stimulus), says it is "not a statement that WWOX loss is anti-inflammatory", and leaves Status (`flagged for review`) and Type unchanged. Good. But it asserts "a sign opposite to the lung, endothelial, B-cell and sepsis reports of partial loss" and PAPER 383 itself says the comparison was made "at registry-title level". The four comparators measure different things in different systems: lung neutrophilic inflammation (PAPER 102), endothelial knockdown in ventilator lung injury (PAPER 113), a heterozygous P47T mouse under LPS (PAPER 114), B-cell deletion on a MYC background with a tumour phenotype (PAPER 115). Against a keratinocyte poly(I:C)-induced phospho-p65 readout these are not one axis with two signs. The conclusion the claim needs, context dependence, survives; "opposite sign" does not at title level. Reword the claim line to "a different direction from the reports named in PAPER 383, compared at title level, readouts not commensurate", or open the four dossiers and compare readouts.

## Item 5 — corrections

- **Complement wording: lossless.** The selection-file row quotes the old wording in the §7.2 form ("the model records microglial activation but nothing on complement") with date, actor and reason. The new statement ("only one WWOX-direct record") is honestly sourced to term queries.
- **Liu 2021 (Alzheimer's versus Parkinson's disease dementia): lossless.** The selection file quotes the old phrase; the registry records already carried the right disease.
- **FT-090: lossless.** The queue row's status changed from open to "read, complete reading" with the receipt, the route (Internet Archive capture, no figures or tables), the answer to the entry's question and the landing PAPER 364, which matches that paper's identifier. The old status text is not quoted, which is acceptable for a status transition.

**M7 — FINDING (low).** PAPER 387 says "This is the one WWOX-direct complement paper in the repository". The dossier says the same paper is restated in a read 2025 review, and the basis is a term query. Append "(by term query over the registry files)" so the record does not read as a literature statement.

## Item 6 — public-edition privacy

- E-mail strings in added lines: 0. Truncated digests: the four short-digest strings in PAPER 097 were in the base; none new. All new PAPER records print a full 64-character digest where an artefact is declared.
- Individual linkage to the reference genotype: none. Reference-genotype variant names occur only in the standard "no datum transfers to ..." transferability sentence.
- Parent-side wording: the added lines contain parent terms only for third-party published patients (a COL4A2 series, a published WWOX child, a published adult case). No pairing for the reference genotype; the gate passes.

**M8 — FINDING (report accuracy, low).** The 005 report states "No parent-side term is paired with a variant anywhere in the new text". That is true of the registry records and false of the files the batch rests on: a dossier says a COL4A2 variant was inherited from a mother without epilepsy, the Scientist A wave file repeats it ("maternal, mother without epilepsy"), and a WWOX dossier still records "both parents heterozygous" for a published child after the earlier repair of the CACNA1A sentence. None is the reference genotype's, none is blocked, but the gate's own wording is "read it before publishing". Soften the report to "in the registry records", and either strip the maternal wording from the wave file and the COL4A2 dossier or record that they are third-party facts retained on purpose.

Also low: the PAPER 015 `Evidence depth` line still reads "full text reviewed (PMC open access)", a declaration; the receipt-backed depth (complete) lives only in the new wave note. Add the receipt to the depth line.

## Item 7 — registry scale

Measured: the papers registry was 1,214,458 bytes at the base, 1,321,413 after 003, 1,376,877 after 004, 1,468,825 after 005 and now. The acknowledged anchor is 1,211,399 bytes and the re-raise point is anchor times 1.25, 1,514,249 bytes. The file is 1,468,825 bytes: 21.3 percent above the anchor, 45,424 bytes (about 3 percent) short of the trigger. The three batches added 107, 55 and 92 KB. Any one further batch of 40 or more PAPER records crosses the trigger.

**M9 — FINDING: tell the operator now.** The deferral itself remains defensible on correctness: three batches of record-scoped edits with no `FULL_FALLBACK`, and the editor writes bounded records. What is no longer defensible is leaving the decision to be raised by the tool after the crossing: the 001 acknowledgement reserved the sharding decision to the operator, and the next batch will cross it before any operator turn. Put the question in the next operator-facing hand-off, with these numbers, now. Two cautions: the `scale_ack` anchor covers the papers registry only, while the literature log (935 KB) and the discovery ledger (801 KB) grow in step and have no anchor; and the 005 report's "no new acknowledgement was recorded" is correct but means the 003 and 004 reports measured the margin only in prose.

## WHAT_WOULD_CHANGE_MY_MIND

- M2 would be dropped if the TCGA analysis reports a WWOX-HIF1A correlation near zero in the cohort used; the lead does not say so.
- M6 would be dropped if the four dossiers show the comparators measured an NF-kB-type readout on a comparable axis; the paper record says the comparison was made on titles.
- M4 would be dropped if the two repository records are shown not to concern mTORC1 signalling.
- The 17-of-28 lead sample and 33-of-89 hand-read PAPER sample leave 11 leads and 56 records checked only mechanically; the number match cannot see a sentence that is numerically right and logically too strong, which is exactly the form of M3.

## Repairs requested (new tasks for the author)

1. M1: give the CLAIM 009 note its own `Evidence boundary` line.
2. M2: limit DL-MECH-117's conclusion to the leukocyte series.
3. M3: DL-MECH-145 "only where" to "where, in two mouse models"; add the no-epinephrine-alone-control caveat to DL-MECH-139.
4. M4: reword the DL-MECH-148 premise.
5. M5: define T3 and T4 in one sentence or stop grading class-level substitutes; re-grade Shin, Hong and batch 004 consistently.
6. M6: reword the CLAIM 028 "opposite sign" phrase to title-level and non-commensurate readouts.
7. M7: add "by term query" to PAPER 387.
8. M8: soften the 005 report sentence; resolve the third-party maternal and paternal wording; add the receipt to the PAPER 015 depth line.
9. M9: put the sharding question to the operator now, with the byte counts above.
