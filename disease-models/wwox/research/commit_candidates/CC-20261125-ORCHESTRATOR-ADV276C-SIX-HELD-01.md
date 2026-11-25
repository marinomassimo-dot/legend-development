# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV276C-SIX-HELD-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (checkpoint 20, section 1) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the findings:** SCI's re-read of the six newly held papers, `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv276c_six_newly_held_sci_20261125/RESULT_ADV276_SIX_NEWLY_HELD_SCI_20261125.md` (sections 2, 5 and 7; SCI's own blind second reader, statements S1 to S9). SCI's message is peer content, not operator authority.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS (stated before any apply)
**MINOR.** One claim in observation (`CLAIM 027`) is narrowed in its Summary and gains one evidence-boundary paragraph. No claim is created, reversed or promoted; no status, grade or ranking row changes; `CLAIM 027` is not a consolidated baseline claim.

## 2 · CLAIM 027 (propagated by `BATCH_COMMIT`)
**Why.** The Summary said that nuclear accumulation of signaling complexes "is linked to context-dependent cell death output". Hsu 2017 (PMID 27845895) reports nuclear accumulation of endogenous proteins without apparent death and shows death only with introduced constructs. The repository's own audit of 2026-09-21 (`analysis/hyal2_wwox_smad4_audit_20260921.md`) already concluded this; the claim had not consumed it.
**Edit 1 (Summary).** Replace "Nuclear accumulation of signaling complexes is linked to context-dependent cell death output." with the sentence in the ops of the batch (cultured cells: nuclear accumulation of endogenous proteins reported without apparent death, not assayed; death with introduced constructs; rat brain injury without counts places Hyal-2/WWOX in apoptotic neuronal nuclei).
**Edit 2.** Append one dated evidence-boundary paragraph before the "Impact on Working Model" line.

## 3 · IT blind check of the CLAIM 027 statements
One verifier (`legend-delegate`, sonnet, effort high stated in the dispatch, read back `claude-sonnet-5-5` and high on every turn), nine statements, held bytes only (text, supplement, Figures 2, 7, 9, 10). Report as delivered: `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_adv276c_six_verify_20261125/VERIFIER_REPORT_AS_DELIVERED_HSU2017_IT_20261125.md`. Result: V1, V2, V3, V4, V5, V6, V8 supported with qualifications; **V7 WRONG** and **V9 UNDERSHOOT**.
* **V7 stays out.** "The boxed gold lies in cytoplasm beside the nucleus" (SCI's image reading, also its verifier's) is not carried: the second reader sees one arrowheaded cluster inside the nucleus at 3 h and gold scattered over the nucleus at 24 h. Two readers disagree on an image, so the claim states only what the authors report and that no counts are printed.
* **V9 repaired.** The replacement sentence names the HA trigger, the introduced constructs and the rat-injury result, which SCI's proposed wording left out.
* **V1 qualification carried.** The proteins that move differ by line (Smad3 not moved by HA in DU145), so the wording does not say "the endogenous complex".

## 4 · The five other consumers of the six papers
| Consumer | Route | State |
|---|---|---|
| `DL-MECH-119` (PMID 33854788), with SCI's amendment on the printed odds ratio | ordinary (discovery ledger) | applied 2026-11-25, one appended sentence; IT checked the OR sentence in the held XML and the SNP row in the held supplement |
| `DL-MECH-120` (PMID 33363507) | ordinary | applied 2026-11-25 |
| `DL-MECH-157` (PMID 34210081) | ordinary | applied 2026-11-25 |
| `RP-018` (PMID 39178853) and `RP-038` (PMID 27641496) | research portfolio, ADV's root-checkout upsert | exact rows sent to ADV 2026-11-25 with six rows of SCI's ADV-276 step 2 batch 2 |

## 5 · Registry lines of SCI's ADV-276b batch 1 (`RESULT_ADV276B_BATCH1_SCI_20261125.md`, sections 3 and 7)
**IT blind check.** A second verifier (`legend-delegate`, sonnet, effort high stated in the dispatch, read back high), eight statements on the held bytes of PMIDs 40500435, 24086726 and 41007296; report as delivered: `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_adv276c_six_verify_20261125/VERIFIER_REPORT_AS_DELIVERED_ADV276B_LINES_IT_20261125.md`. All eight supported; one needed a rewording (every group of Figure 3b, controls included, received the labelled fructose injection).

| Consumer | Change | Route |
|---|---|---|
| `PAPER 276` short title and Role; `LIT-0572` short title | the lactate values are after a labelled fructose injection in pups of fructose-fed or control dams; "a diet exposure alone" withdrawn | BATCH_COMMIT |
| `DL-MECH-123` title and causal statement | same correction | ordinary (discovery ledger), applied |
| `PAPER 264` short title, Model/species, Role; `LIT-0562` short title | 7,379 enrolled, adjusted model at most 6,969; the 42 percent power is at alpha 0.05 | BATCH_COMMIT |
| `PAPER 266` Role | the basal-like Cox row (HR 1.014, p 0.034) points to higher hazard against the text's "improved survival" | BATCH_COMMIT |
| `CC-20261019-SCIENTIST-B-G2-FRUCTOSE-01` and `-HUMAN-AXIS-01` | dated correction notes appended, entries left as written | ordinary, applied |

**One pointer of SCI's corrected:** SCI's section 5 names "the PAPER 118 record" for the Cox row. PMID 41007296 is `PAPER 266`; `PAPER 118` is a different paper (its own note says so). The note goes on `PAPER 266`.
**Not done here:** the `DL-MECH-057` author name (already corrected on 2026-11-25), the Santini optional precision, and the Kv7 lead (an open-question row, a later landing because a map edit owes the view trio).

## 6 · What this does NOT do
No claim, grade or ranking change beyond the narrowing above. No protein-level datum is created. Cho 2012 and Jamaspishvili 2019 were not re-opened. No receipt is added by IT: the reading of record is SCI's `queried_not_full_read` receipt.

## BATCH DISPOSITION — `BATCH_20261125_005` (2026-11-25, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED

`batch_commit.py propagate`, record-scoped, dry run then apply: `CLAIM 027` (Summary sentence and one evidence-boundary paragraph), `PAPER 276` (2 ops), `PAPER 264` (3 ops), `PAPER 266` (1 op), `LIT-0572` and `LIT-0562` (short titles). Ordinary-route edits of the same landing are listed in sections 4 and 5. **Change class restated: MINOR**, `WM_v7.29` preserved.
