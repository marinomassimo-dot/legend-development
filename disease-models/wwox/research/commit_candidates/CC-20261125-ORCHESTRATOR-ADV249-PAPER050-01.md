# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV249-PAPER050-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-249 wording) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the finding:** `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv249_unread_lead_primaries_sci_20261125/RESULT_ADV249_UNREAD_LEAD_PRIMARIES_SCI_20261125.md` (SCI's reading of PMID 26857392; receipt `FTR-20261125-26857392-01`, partial: main text and three tables, figures from captions only, supplements and references not read).
**Status:** PROPOSED, for the next `BATCH_COMMIT` that the queue triggers. No registry file is edited by this act.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** Two corrections to `PAPER 050`. No claim is linked to this record, and no claim, status, ranking or working-model line changes.

## 2 · Proposed changes
**A. `Evidence depth`.** The line says "full text reviewed (coverage_status: complete_fulltext_read; supplementary non recuperati)". The ledger does not attest a complete read: `FTR-20260726-26857392-01` is a reconstruction with every section `unknown_legacy`, and `FTR-20261125-26857392-01` is partial. Proposed value (English):
"partial full-text read (`FTR-20261125-26857392-01`: main text and three tables; figures from captions only; supplements not opened). The earlier 'complete' declaration is not attested by a receipt (`FTR-20260726-26857392-01`: all sections unknown_legacy)."

**B. `Note`, append (the existing text is kept):**
"Correction 2026-11-25 (ADV-249): this is a junction-versus-core RT-qPCR used in lymphoblastoid lines; it is not validated for detecting exon 9 loss. Alternative 3' ends in intron 8 are cited from databases, not measured by the authors. The paper does not try the assay on a splice-altering variant (no search for later use was run), and the assay does not separate exon skipping, intron retention, a cryptic site or alternative termination; the exon 8-9 to core ratio (mean 67 %) was measured in 88 of 89 lines. The words 'pubblicato e validato' above overstate."

## 3 · What this does NOT do
No change to `Status`, `Role`, `clinical relevance`, wikilinks or the literature tracking log. The note's other sentences (including the ACMG-criterion remark) were not re-assessed. The corpus table row elsewhere that reads "full text" is not touched.

## 4 · Statements for the blind check at propagation time
1. The authors analysed 89 lymphoblastoid cell lines; the exon 8-9 versus exon 4-6 transcript comparison reports 88 lines (reverse transcription failed in one).
2. The mean transcription rate of exon 8-9 relative to the core coding region is 67 %, with intra-line correlation r = 0.68.
3. The alternative transcripts ending within intron 8 are attributed in the text to GenBank database entries.
4. No splice-altering variant is assayed with the junction amplicon in this paper.

Statements 1 to 3 were located by IT in the held Europe PMC XML on 2026-11-25; statement 4 rests on SCI's reading and was not checked by IT. None has had a blind check.

## 5 · Applied outside the registries (ordinary route, same day)
Dated corrections on `DL-BIO-003`, `DL-MECH-032` and `DL-MECH-025` (discovery ledger), on the TX-001 experiment decision packet § B.3 and on `HYP-20260709-06`.

Wording fix 2026-11-25 (ADV-263, same author): the earlier clause 'was never tried' stated a negative about all later use without a search; it is now bounded to the paper.
