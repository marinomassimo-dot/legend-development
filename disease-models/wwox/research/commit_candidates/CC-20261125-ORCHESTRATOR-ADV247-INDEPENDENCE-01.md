# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV247-INDEPENDENCE-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-247) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the findings:** `advisor_pilot_20261113/brainstorm_20261116/adv247_independence_audit_sci_20261125/RESULT_ADV247_INDEPENDENCE_AUDIT_SCI_20261125.md` section 4 (SCI) and `independence_adv247.tsv`; organoid clone and batch from ADV-244 (SCI) and `it_adv244wording_20261125`.
**Status:** PROPOSED, for the next `BATCH_COMMIT` that the queue triggers. No registry file is edited by this act. Card and investigation wording was placed by the ordinary route and is not part of this candidate.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** Unit statements (what the n counts) on four claims. No conclusion, grade, status or number changes.

## 2 · Proposed sentences (English, one per claim)
| Claim | Sentence |
|---|---|
| `CLAIM 002` and `CLAIM 005` (organoid transcript statements) | "The organoid RNA-seq compares four knockout organoids of one CRISPR clone (1B) with two organoids of the parental line, apparently from one batch (authors' Methods: organoids from the same batch unless stated otherwise); a difference there is not shown to be independent of the clone." |
| `CLAIM 005` (P47T and hippocampal statements) | "The P47T region libraries come from the same mice, so agreement across regions is one set of animals seen several times, not replication; hippocampal bulk arms in the neuron-targeted deposit are 2 or 3 libraries with one mouse per library not stated." |
| `CLAIM 007` (P47T Wwox transcript) | "The four P47T region libraries come from the same mice (five per group; cerebellum four against three)." |
| `CLAIM 014` (shRNA contrast) | "One shRNA population per arm in one cell line; the two stages are not independent knockdowns." |

## 3 · What this does NOT do
No claim, grade or ranking change; no new measurement. The H1 neurosphere statement ("libraries not tied to individual pups") has only frozen seed tables as consumers and is carried in `it_adv247wording_20261125/WORDING_ADV247_IT_20261125.md`.

## 4 · Statements for the blind check at propagation time
1. GSE215425 sample titles carry a mouse identifier repeated across regions (SCI, ADV-247 table row T1 to T12).
2. The organoid deposit: ADV-244 reads (all four knockout libraries carry clone 1B's alleles) and the Methods sentence "For all analyses, organoids from the same batch were used, unless stated otherwise".
3. Each CLAIM named above exists with the cited statement; the exact text to be amended is read in place at propagation.
