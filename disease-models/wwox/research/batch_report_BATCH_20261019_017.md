# BATCH COMMIT REPORT — BATCH_20261019_017

> **One job: verify the blind audit of the 2026-10-22 R1 repairs, then land the part of
> `CC-20261021-SCIENTIST-A-R1-PROTEOSTASIS-01` that was held back for want of it — proposal 2, the verdict
> annotations of the three historic `Q230P` dossiers.** Integrator: ACTOR_ID `integrator`, task
> `BATCH_20261019_017`. Everything landed is class-level **NOT WWOX EVIDENCE**, with no dose, no
> administration and no statement of suitability. **Not medical advice.**

## Summary

- Type: MANUAL, **MINOR**. Pre-flight LINT `WARN` (0 BLOCK); post-propagation LINT `WARN` (0 BLOCK).
- **WM version `WM_v7.27` PRESERVED**, carried forward as in batches 009 to 016: no claim, block, registry
  record, status, support or uncertainty was added or modified, so `state_manifest_current.md` § 2 and
  `prompt_batch_commit.md` § 4.6 preserve the version, the WM timestamps and the changelog rows.
- Commit candidates: **1 PROPAGATED** (`CC-20261021-SCIENTIST-A-R1-PROTEOSTASIS-01`, closing), with its
  `## BATCH DISPOSITION` block rewritten and its earlier disposition preserved below the new one.
- Snapshot `backup/20261024_batch017` (not committed); pre-batch commit
  `8050597d962f5881d4c16c0d7ff1d6f8fcc63d81`. No restore used.
- No append-only ledger was rewritten in place; no record-scoped op list was needed, because none of the
  four scientific current files is touched. `FULL_FALLBACK`: not applicable, **none**.

## The audit, verified before anything was landed

`disease-models/wwox/research/page_adjudications/locator_audit_R1_repairs_20261024.md` claims an exhaustive
blind re-judgement of the 21 `contradicts_locator` entries citing `locator_audit_R1_20261022.md` across six
manifests, 21 SUPPORTED, 0 adverse. The integrator checked it rather than taking it:

1. **Scope re-derived from the manifests, not from the audit.** Across all 101 deep-dive manifests, 343
   entries carry `contradicts_locator`; in the six declared manifests the counts are 3 (31402619), 4
   (32023956), 6 (38378758), 3 (38731820), 4 (42157447) and 1 (42875792) = **21**, and **every one of the
   21 cites `locator_audit_R1_20261022.md`**. The scope is exhaustive as declared, with no triple excluded
   from the denominator.
2. **Entry numbering reproduced.** The audit's entry ids are the zero-based numbering of
   `locator_audit.py --pmid <PMID> --triples 0`; the positional ids of the `contradicts_locator` entries
   reproduce the audit's lists exactly for all six manifests.
3. **Quote occurrence reproduced.** `locator_audit.py --pmid` over the six: one NOT FOUND, 31402619 entry 2,
   exactly as the audit's quote-occurrence note says. The quote **is** verbatim in its declared artefact,
   `files/supplement/PMID31402619/ACN3-6-1407-s009.docx` — confirmed by the integrator by reading the
   document — and the tool does not read `.docx`, so this is a limit of the checker. The other five
   manifests matched every text quote.
4. **Both figure corroborations re-read first-hand from the native rasters**, which carry the dimensions the
   audit declares (731 × 1511 and 771 × 599): 32023956 Figure 1B prints Pearson r **0.8771**, 95 percent
   interval 0.8381 to 0.9071, R squared **0.7692**, with panels A and C at 0.8729 / 0.7620 and
   0.7992 / 0.6388; 38731820 Figure 6C draws **six** animals at baseline whose mean and SEM recompute to
   15.583 and 5.014 against the body's 15.58 ± 4.987.
5. **Spot checks of SUPPORTED propositions against the sources**: the 38378758 compound scope ("might only
   stabilize variants localized to the region or domain where the compound binds", the R42P UBL attribution),
   the 42875792 degradation attribution and its following sentence, the 42157447 butyrate range (7.4 % to
   17.8 %) and the Figure 7E dose language all occur as the audit reports them.

**One wording nuance, recorded and not adverse.** The audit says of 31402619's supplementary methods that
"no form of soluble/insoluble or pellet retention appears anywhere in it". The string *pellet* does occur
there, twice, but both times in an RNA precipitation, not a protein solubility fractionation — so the
substance of the note (no protein-pellet retention is described) holds, and the entry's restraint is
accurate.

**Verdict: the audit file is verified.** The debt the candidate declared is paid, and proposal 2 may land.

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_017.md` (this report).
- `ledger/tasks/integrator/BATCH_20261019_017.json` (task record, with `DEFAULTS_TAKEN` and `STOP_LOG`).
- `backup/20261024_batch017/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation |
|---|---|
| `research/vps_recovery_20260925/residue_q230p_20260922/q230p_fractionation_and_orthogonal_detection_20260922.md` | one annotation blockquote above the title: `PA-1` KEEP, `PA-2` INCONCLUSIVE, `PA-3` KEEP with its limit, `Premise 0` KEEP strengthened, plus the 32023956 printed-value resolution |
| `research/vps_recovery_20260925/residue_q230p_20260922/q230p_nascent_synthesis_discriminator_20260922.md` | one annotation blockquote above the title: `PB-1` KEEP, `PB-2` KEEP, `PB-3` INCONCLUSIVE, `PB-4` **INCONCLUSIVE for a protein-loss lesion** (was NARROW, withdrawn wording named as withdrawn), plus the 38731820 sample-size resolution |
| `research/vps_recovery_20260925/residue_q230p_20260922/systemic_rescue_mechanism_and_peripheral_panel_20260922.md` | one annotation blockquote above the title: `PC` INCONCLUSIVE, not addressable by the R1 lot |
| `research/commit_candidates/CC-20261021-SCIENTIST-A-R1-PROTEOSTASIS-01.md` | header hold marked RELEASED (not deleted), `## Owed` marked PAID, `## BATCH DISPOSITION` rewritten to **PROPAGATED** with the earlier disposition preserved verbatim beneath it |
| `framework/state/state_manifest_current.md`, `framework/state/state_history.md` | last-batch and last-LINT fields; `batch_20261019_017_scope` / `_candidates` at the top of § 4 |

## FILES UNCHANGED

All four scientific current files (`working_model_current.md`, `claim_registry_current.md`,
`paper_registry_current.md`, `literature_tracking_log_current.md`), `working_model_history.md`,
`disease_model.md`, every `meta_*`, research-line, biomarker, endpoint and therapeutics file, the discovery,
dismissal, hypothesis and experiment ledgers, the full-text queue, the receipt ledger, **every deep-dive
manifest** (nothing was stamped, repaired or re-judged by this batch), the DisMech sidecar and its seal, and
`growth_anchors.jsonl` (no countable growth event: no paper, literature record or claim was added).

## CHANGE LOG

1. **The annotations annotate; they do not promote.** Each is a blockquote placed between the recovered-record
   header and the dossier's own title. No sentence of any dossier was edited, and each block repeats that the
   `UNREAD_PREMISE` header still holds, that the verdicts are class-level and about experimental design rather
   than WWOX biology, and that nothing there is medical advice.
2. **Every row says how far the audit reaches.** `PA-1` and `PA-2` rest on PMIDs 33914734, 39216838 and
   30266908, which lie **outside the scope of both R1 audits**; `PB-2`'s quotation is 38378758 entry 5, which
   carries no `contradicts_locator` and so was not inside the repairs audit either, though its quote matches
   its artefact verbatim. Those rows say so instead of borrowing the audit's standing. `PA-3`, `PB-1`,
   `PB-4` and `Premise 0` name the audited entries that carry them.
3. **`PB-4` lands restated, with the withdrawal visible.** It is INCONCLUSIVE *for a protein-loss lesion*; the
   two withdrawn parts (that polysome profiling by itself cannot separate transcript from translational
   regulation, and that the lysate discards an insoluble pool) are named as withdrawn and are asserted
   nowhere. What survives is the audited absence of 31402619 entry 3, plus entry 1's regime separation.
4. **The two corroborations are carried where they bear.** For 32023956 the panel's r 0.8771 / R² 0.7692 is
   what `Premise 0`'s two-assay agreement rests on, the text's 0.9448 being the outlier — the arithmetic is
   given in the annotation. For 38731820 the annotation records that the figure's six animals, not the
   legend's "N = 3 female", is what any later use of that mouse seizure endpoint takes, and states plainly
   that **no verdict in the table rests on that sample size**.
5. **Nothing was held back.** Every part of proposal 2 enumerated in the mandate is landed. No part of it
   was found unsupported: the audit returned 0 of 21 adverse, so no repaired entry withdraws a verdict, and
   the verdicts resting on unaudited primaries are landed with their scope stated rather than suppressed.
   Proposal 3 carries nothing propagable — its own text routes the lead through `discovery_lead.py stage`
   and says it is not written in the candidate — so no lead was invented.

## DEFAULTS_TAKEN

1. **No WM bump** and no `current_state: IN_BATCH_COMMIT`: path-scoped landing, as batches 012 to 016.
2. **`Premise 0` was annotated**, although the mandate's enumeration named only `PA-1`/`PA-2`/`PA-3`,
   `PB-1`–`PB-4` and `PC`: it is part of proposal 2 in the candidate's own words ("Premise 0 KEEP
   strengthened"), and two audited entries (42157447 entry 8, 32023956 entry 4) carry it. It was placed in
   the fractionation dossier, the one whose § 4 argues that function comes after molecular state.
3. **Placement above the title rather than inside the dossier bodies.** The proposals `PA-1` … `PC` are
   Scientist A's labels for what the dossiers argue; they are not section ids inside the files, so there is
   no unambiguous in-body anchor for each one. One block per dossier keeps the historic text untouched.
4. **`growth_anchors.jsonl` was not appended to**: no claim, paper or literature record was created, so
   there is no growth event to record; `growth_anchors.py check` was run as a gate instead.
5. **No manifest entry was stamped** with the 2026-10-24 audit's verdicts (`audit_file`, `triple`,
   `audited_on`), although the producers have been stamping earlier audits. That is the readers' act, the
   mandate did not ask for it, and a parallel batch was working in the same window.
6. **Phase 8.1 not performed**: `legend_activity_log.md` does not ship in this edition; the snapshot path
   and the pre-batch SHA are recorded here and in `batch_20261019_017_scope`.

## STOP_LOG

Empty. No STOP condition arose: no URGENT cat-1, no baseline reversal, no paid service, no `§21d`
reservation touched.

## Verification

| Check | Result |
|---|---|
| `legend_lint.py .` (pre and post) | `WARN`, **0 BLOCK** both times |
| `growth_anchors.py check` | PASS |
| `scripts/public_release_gate.py` | PASS |
| `fulltext_receipts.py verify` | OK, chain intact |
| `candidate_tree_freshness.py` | derived surfaces fresh |
| `locator_count_crosscheck.py --sweep` | run **last**, after merging `main` (which brought `BATCH_20261019_016` in): 250 assertions reached, agrees 188, **disagrees 0** against a ceiling of 0, manifest absent 0, unparsed 5 (declared 5) — AT OR BELOW BASELINE; `test_locator_count_crosscheck.py` 26 tests OK |

## Recommended next actions

- The 21 re-judged entries now have a second reader's verdict; stamping `audit_file` / `triple` /
  `audited_on` onto them belongs to their producers, and `repurposing_join.py` counts a condemned entry
  whose repair nobody re-judged as its own state, so the join will keep reporting them until they are stamped.
- `CC-20261021-SCIENTIST-C-R3-A51-ATTRIBUTION-01` remains deferred and is untouched by this batch.
