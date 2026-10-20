# MIRROR review — BATCH_20261019_001 (ex post, Annex C.2 format)

> Reviewer: ACTOR_ID `mirror` (not the producer). Scope: commits `99a9f400..db4f3d63` plus `a9db41b0`, base `d956ded7`.
> Read-only toward every repository file except this one. A finding is a new task for the change's author, never a hold on the landed batch. Not medical advice.

## Verdict

**CONFIRMED with one BLOCK-class repair (B1) and six FINDINGs.** CONFIRMED means no further defect found in the sampled evidence bundle, not "true". No claim `Status`, `Type` or `Summary` and no baseline sentence changed. The batch's own gates were re-run by this reviewer:

- `legend_lint.py .`: verdict WARN, 0 BLOCK.
- `fulltext_receipts.py verify`: OK, 542 chained receipts, tail anchored.
- `growth_anchors.py check`: PASS (8 candidates on disk with no disposition; a decision is due).
- `test_build_evidence_index.py`: 11 tests OK.

## STEELMAN

The batch discharged a real registry debt (23 orphan complete reads) with record-scoped ops, no `FULL_FALLBACK`, and the earned negatives are carried in nearly every sampled record: the nominal/uncorrected status of the GWAS papers, the tumour-cell-line limits of the oleate paper, the absence of recorded seizures in recessive ELOVL1 disease with its basis stated, and the "do not cite" label on the review whose conclusion its own body contradicts. The sampled numbers match their dossiers digit for digit.

## Measured scope

- Diff of `claim_registry_current.md` and `working_model_current.md` from `d956ded7`: the only changed lines are the `CLAIM 042` evidence-boundary line, the `CLAIM 001` additional-observations line, and the WM `Version` and `Last update` lines. No Status, Type, Summary or baseline sentence moved.
- Sampled 17 of 64 PAPER records (250, 254, 261, 262, 263, 265, 267, 268, 269, 278, 291, 294, 295, 296, 299, 302 and 310), 6 LIT records (0549, 0561, 0565, 0575, 0590, 0603) and all 22 new leads, against the dossiers and, for PAPER 263, a live PubMed metadata query.
- Scan of 15,909 added lines in `disease-models` and `framework/state`: 0 e-mail strings, 0 parent-of-origin or pedigree-allele attributions about the reference genotype (the only family terms are sibling and consanguinity facts of third-party published case reports), and no new truncated digest. The four `sha256 xxxxxxxx…` truncations in PAPER 097 were already in `d956ded7` and are quoted history.

## Findings

### B1 — BLOCK-class (repair as new task): CLAIM 001 wave note invents a conflict between the two VABAM cohorts

Where: `claim_registry_current.md` CLAIM 001 wave note ("The two cohorts disagree on whether hormonal therapy relates to the MRI finding"), `DL-MECH-133` ("The two non-WWOX cohorts disagree on whether hormonal therapy relates to the MRI finding"), and the Scientist D wave note.

Measured: the note's own figures show agreement, not disagreement.

- Sathe: hormonal therapy accompanied 11 of 11 symptomatic cases, and the asymptomatic comparison showed no hormonal difference (4 of 6 vs 17 of 39).
- Stevering: hormonal therapy was not associated with the MRI finding (RR 0.94) but was associated with symptoms (RR 9.00, eight exposed).
- Both therefore point the same way: hormonal therapy tracks symptoms, not the presence of the MRI change.

Sathe never tested hormonal therapy against the MRI finding as such. The sentence creates a "conflict" on a claim whose status is `conflicting evidence`, which a later reader will count as evidence. Repair: restate as "both cohorts associate hormonal therapy with symptomatic VABAM and neither with the MRI finding alone; both are underpowered and neither isolates a mechanism". Status stays.

### F1 — FINDING: CLAIM 042 base-rate paragraph drops a landed negative and does not say one source is partial

- "Roughly 47 to 100 percent" omits CDKL5 0 of 10 in the same gene-level study, which PAPER 268 and its dossier record. The 47 to 100 range is built only from the responders in that table. The same range is repeated in `DL-MECH-121`. Add the CDKL5 0 of 10 to both.
- PAPER 269 is `partial_fulltext_read` (Figure 2 and 4 legends only), yet the paragraph's `PREMISE_TAG` says "rests on the two cited readings (DATO as printed)" without saying one is partial. Name the partial depth.
- The paragraph does not overreach otherwise: it says "not distinguishable" and "does not identify an energy lesion in either direction". It does not assert that the diet works or fails in WOREE, and the Q230P statement is untouched.

### F2 — FINDING: PAPER 097 depth raise leaves the old figure statement unqualified

Raising `PAPER 097`, `136` and `147` to complete is lossless: receipt `FTR-20261019-35984507-03` exists with every coverage field `read`, and the earlier receipts are kept in the same line. But PAPER 097 still reads "**`figures: captions_only` in entrambe: nessun pannello ispezionato** ... tutti i negativi sotto sono negativi **testuali**" with no marker that this was superseded. A reader of the Evidence-depth line sees "complete" and "no panel inspected" together. Add "(as of the earlier receipts; superseded by -03)". The body negatives were not re-examined against the closing read, so the "textual only" qualifier now has unknown currency.

### F3 — FINDING: PAPER 263 identity correction is right, with two loose ends

Verified against PubMed: PMID 31145772 now returns the title and abstract of the East Asian type-2-diabetes GWAS article together with authors of a different group (Permana et al.), DOI `10.18388/abp.2020_5563` and pages 679-686. The correction (cite the DOI printed on the article, do not rewrite the PubMed fact) is sound and the numbers in the record match the dossier.

- `LIT-0561` says "see Note", but its Note is the generic class-level line. The `identity_correction` lives only in PAPER 263.
- The record calls the other article "a 2021 article". The PubMed return shows a 2019 date and a 2020-style DOI, so "2021" is not supported by what this reviewer could measure. Drop the year or source it.

### F4 — FINDING: DL-MECH-117 states more than two series support

"A ratio-based reading adds no information about WWOX loss beyond HIF1A alone" is a universal derived from one leukocyte series (WWOX and HIF1A uncorrelated) and one TCGA analysis. Coupling is real for those data, and the falsifier is stated, but the tag INFERENZA covers a conditional: where the two transcripts are uncorrelated, the ratio is dominated by the denominator. Restate it as that conditional.

### F5 — FINDING: records cite claim support that was parked

`PAPER 291` says it is "PAPER-level support for the context principle in CLAIM 034, MINOR" and `PAPER 289` addresses CLAIM 010, while both carry `Claim links: none`, and Scientist C's CLAIM 034 and CLAIM 010 support mentions were parked. Parking was right (see item 8). But the record text now asserts a support relation the claim registry does not carry. Either mark the sentence "proposed, parked at BATCH_20261019_001" or land the support mentions. `legend_lint` will eventually warn `UNLINKED_SUPPORT`, as it already does for 8 older claim-to-paper pairs.

### F6 — FINDING: scale acknowledgement note has a stale count

The `scale_ack` note says "the 63 PAPER records ... took the papers registry from under to 1183 KB". The batch landed 64, and the file is now 1,214,458 bytes (about 1186 KB). The anchor binds to 1,211,399 bytes, so the +25 percent expiry arithmetic is unaffected.

## Per-item verdicts

| # | Item | Verdict |
|---|---|---|
| 1 | Claim STATUS and baseline sentences | OK. No status, type, summary or baseline line changed; only the two evidence-boundary notes and the WM version and last-update lines. |
| 2 | 17 PAPER and 6 LIT records and 22 leads | OK with F1, F3 and F4. All 22 leads carry a tag. Leads 125-135 and the three METH leads are IPOTESI. "Not WWOX evidence" substitutes are labelled in the sampled records: PAPER 254's seizure absence rests on one "-" in a summary table and is worded as "recorded" and "conditional", and PAPER 261 is labelled do-not-cite. |
| 3 | CLAIM 042 base rate and CLAIM 001 VABAM note | CLAIM 042: FINDING F1. CLAIM 001: BLOCK-class B1. |
| 4 | PAPER 263 identity correction | OK, verified live; F3 loose ends. |
| 5 | Sze 2015 to PAPER 310; CORPUS-STUB-157 retitle; PAPER 097, 136 and 147 | Lossless. The stub retitle quotes the superseded wording and cross-links PAPER 249. PAPER 310 is correctly labelled as a self-commentary, counted once. The 097/136/147 raises are backed by receipts; F2 on stale wording. |
| 6 | Integrator edits: `build_evidence_index` 4 decimals; scale ack "stay on canonical Markdown" | OK. The 4-decimal change is correct (the share now prints 99.6 percent, not 100 percent) and its 11 tests pass. The ack is a recorded deferral, the sharding decision is left to the operator, and it is the first ack of this registry; only F6. |
| 7 | Individual linkage, pedigree-parent allele attribution, e-mail, truncated digest | OK. None found. |
| 8 | Parked ops (CLAIM 034 and 010 support mentions, PAPER 084 sentence, PAPER 003 description) | Parking was right: no op text, and they edit claim support sets that no landed status depends on. The consequence is F5. |

## WHAT_WOULD_CHANGE_MY_MIND

- B1 would drop to a wording FINDING if Sathe tested hormonal therapy against the MRI finding itself, not against symptoms. The dossier does not show that.
- F1: sight of the CDKL5 0 of 10 in the claim paragraph, or a reason it is excluded.
- The sample is 17 of 64 PAPER records and 6 of 55 LIT records. Unsampled records were checked only by LINT and by the grep scans above.

## Repairs requested (new tasks for the author)

1. B1: rewrite the CLAIM 001 wave note sentence, `DL-MECH-133` and the D wave note.
2. F1: add CDKL5 0 of 10 and the partial depth of PAPER 269 to the CLAIM 042 paragraph and `DL-MECH-121`.
3. F2: mark the PAPER 097 figure statement as superseded.
4. F3: fix the LIT-0561 note pointer and the "2021" wording.
5. F4: recast DL-MECH-117 as a conditional.
6. F5: mark or land the parked support sentences in PAPER 291 and 289.
7. F6: correct the count in the ack note, in a new note.
