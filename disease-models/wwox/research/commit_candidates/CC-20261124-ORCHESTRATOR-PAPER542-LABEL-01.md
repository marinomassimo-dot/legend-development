# COMMIT CANDIDATE — CC-20261124-ORCHESTRATOR-PAPER542-LABEL-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-208 item 5, queued at ADV's word of 2026-11-24) · **Date:** 2026-11-24 · **target_wm_version:** `WM_v7.29` (unchanged)
**Paper:** PMID 42523332 (Aragon-Ramirez et al. 2026, bioRxiv preprint, PMC13405132; `PAPER 542`, `LIT-0814`)
**Origin of the findings:** SCI's ADV-205 result, `advisor_pilot_20261113/brainstorm_20261116/adv205_paper542_golgi_wwox_scope_sci_20261123/RESULT_ADV205_PAPER542_GOLGI_WWOX_SCOPE_SCI_20261123.md` (pre-registered five-point control checklist, disposition b, receipt `FTR-20261123-42523332-01`, preprint v3 only). The wording below is IT's, taken from that result and from ADV's wording line; it has NOT been audited separately.
**Status:** PROPOSED, for the next `BATCH_COMMIT` that the queue triggers (five candidates or the weekly trigger). Neither registry is edited by this act, and no standalone batch is run for it (ADV, 2026-11-24).

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice.

## 1 · CHANGE CLASS (stated before any apply)
**MINOR.** The records' `Status`, identity, receipt and `Evidence depth` fields are untouched, and no claim is created, reversed or promoted. Only the two fields that carry the registration-time label change: `Transferability` and `Next action` on `PAPER 542` and the mirrored two on `LIT-0814`. The grade stays T4 and the record stays background (`clinical relevance: BACKGROUND (non-WWOX)` is not touched). No ranking, compound or causal-model consequence (ADV-205: nothing for a ranking row, a compound, RP-017 or the neural ITGB1 branch).

## 2 · Why the label is wrong in both directions
The label was written at registration (`BATCH_20261019_012`) from the subject of the paper and "the research note that read it"; the record itself says the WWOX count was not re-measured and asks for a re-grade "if a re-read finds WWOX measured". ADV-205 re-read it. The text is neither "WWOX is not the subject" nor a demonstrated WWOX mechanism: one siRNA (verified at mRNA only, two repeats) in hTERT-RPE1 cells was followed by higher plasma-membrane HPA and GNL binding, lower COPB2 and GALNT2 colocalisation and a slightly smaller Golgi area, n = 30 cells per panel; no second siRNA or knockout, no rescue, the control is labelled "CTRL" without stated identity, unit = cells. Disposition (b): perturbation present, required controls missing, ambiguity kept visible; disposition (c), an incidental mention, is rejected; disposition (a), direct controlled evidence, is not met.

## 3 · Proposed wording (record-scoped `replace-within`; every other byte of both records unchanged)

### `PAPER 542` — field `Transferability`
Old (verbatim): `T4 — 🔴 **NOT WWOX EVIDENCE: WWOX is not the subject of the article.** The read artefact is not on the checkout this record was authored on, so the WWOX count was **not re-measured at registration** and the grade rests on the subject of the paper and on the research note that read it; re-grade if a re-read finds WWOX measured`
New: `T4 — 🔴 **WWOX perturbation present (one siRNA, hTERT-RPE1 cells, unit = cells, no rescue or second reagent); controls missing; ambiguity kept visible.** Not an incidental mention and not a demonstrated WWOX-dependent mechanism: the abstract's regulator wording is stronger than these controls. Re-read 2026-11-23 (SCI ADV-205, disposition b; receipt FTR-20261123-42523332-01; preprint v3 only; locator advisor_pilot_20261113/brainstorm_20261116/adv205_paper542_golgi_wwox_scope_sci_20261123/). Nothing about a neural cell type. [Replaces the registration-time label 'NOT WWOX EVIDENCE: WWOX is not the subject of the article', which was not re-measured at registration.]`

### `PAPER 542` — field `Next action`
Old (verbatim): `none — registered for identity; re-grade the transferability if a re-read finds WWOX measured`
New: `none now; revival condition (ADV-205): a second independent siRNA or a knockout with the lectin readout in independent experiments, a rescue, or a published version adding them would move this to direct controlled WWOX perturbation evidence in a non-neural context`

### `LIT-0814` — fields `Transferability` and `Next action`
Old `Transferability` (verbatim): `T4 — NOT WWOX EVIDENCE`
New: `T4 — WWOX perturbation present (one siRNA, hTERT-RPE1 cells, unit = cells, no rescue or second reagent); controls missing; ambiguity kept visible (SCI ADV-205; see [[paper_registry_current#PAPER 542]])`
Old `Next action` (verbatim): `none — registered for identity; re-grade the transferability if a re-read finds WWOX measured`
New: the same sentence as the new `PAPER 542` `Next action`.

## 4 · What this does NOT do, and the consumers
* No claim, working-model sentence, ranking row, compound card or portfolio row changes; `Status: processed`, the receipt line of `Evidence depth` and the `LIT link` are untouched (the newer receipt `FTR-20261123-42523332-01` is already in the ledger and in the derived coverage and reading-state surfaces).
* The depth-queue row (`generation_it59_20261119/queue_start_here_with_depth_it59.tsv`) is generated by `reading_debt_reconcile_it59.py` from `batch_queue.py`; it carries no label and is not hand-edited.
* Consumers checked by IT on 2026-11-24: the open-questions map, `investigations_it20.tsv`, the README and the portfolio state no premise about PAPER 542 as live; nothing to propagate beyond the two registries.

## 5 · Statements for the blind check at propagation time, with anchors (surface: the held Europe PMC XML and figure images; SCI's result)
1. One siRNA, no second reagent or knockout: Results, Fig 5 section; Methods (absence); the string "siRNA" occurs three times in the whole XML.
2. Depletion verified at mRNA only, two repeats: Supplementary Fig 4C legend; no protein-level verification.
3. n = 30 cells per panel and unit = cells, independent experiments not stated: Fig 5C legend; Supplementary Fig 4E and G.
4. No rescue (myc-WWOX used for localisation only): Results; Methods (absence).
5. The abstract's wording "establishes WWOX as a previously unrecognized regulator of Golgi homeostasis and glycosylation": abstract of PMID 42523332.
Figure-read values are approximate and stay out of the registry wording.

## 6 · Order of work
(1) blind check of section 5 against the held text (fresh delegate, statements and anchors only, effort stated in the dispatch) at the time a batch is triggered; (2) one MINOR `BATCH_COMMIT` through `batch_commit.py propagate`, the four edits as record-scoped `replace-within` operations together with the other queued candidates; (3) regenerate the derived surfaces in the documented sequence (the depth-queue row follows by itself).

**Not medical advice.**

## BATCH DISPOSITION — `BATCH_20261124_001` (2026-11-24, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED

4 record-scoped `replace-within` ops: `PAPER 542` `Transferability` and `Next action` (2 ops, paper registry) and `LIT-0814` `Transferability` and `Next action` (2 ops, literature tracking log); the new `Next action` sentence is the same in both. **Change class restated: MINOR** (no Status, identity, receipt, Evidence depth or LIT link changed; the grade stays T4; no claim, ranking or compound consequence). Blind check of section 5 by one fresh `legend-delegate` (sonnet, effort high, statements and anchors only, held XML, Figure 5 image and supplement): all five statements SUPPORTED. Caveats it returned, none of which enters the registry wording: (1) the paper does not say whether the siRNA is one oligo or a pool and gives no sequence (it cites an earlier paper for it); (3) 'n = 30 cells' appears only in the Fig 5 quantification legend and Supplementary Fig 4E and 4G, other panels give a different n or none, so 'per panel' in section 5 statement 3 was too broad; the registry wording says only 'unit = cells', which is supported. The numbers in the new text are the ones the candidate already carried; no figure-read value was added.
