# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV247-INDEPENDENCE-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-247) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the findings:** `advisor_pilot_20261113/brainstorm_20261116/adv247_independence_audit_sci_20261125/RESULT_ADV247_INDEPENDENCE_AUDIT_SCI_20261125.md` section 4 (SCI) and `independence_adv247.tsv`; organoid clone and batch from ADV-244 (SCI) and `it_adv244wording_20261125`.
**Status:** PROPAGATED (`BATCH_20261125_004`; see the BATCH DISPOSITION block at the foot). No registry file is edited by this act. Card and investigation wording was placed by the ordinary route and is not part of this candidate.

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

## 5 · Blind check and the wording that propagates (IT, batch 2, 2026-11-25)
One blind verifier (`legend-delegate`, sonnet, effort high stated; read back high), statements I1 to I3 in `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_batch2_verify_20261125/statements_batch2e.tsv`, report `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_batch2_verify_20261125/VERIFIER_REPORT_AS_DELIVERED_BATCH2E_IT_20261125.md`. **I1** (GSE215425, mouse): titles repeat mouse identifiers across regions (F10, F4, F5, F8, M2, M3, M6 in all four; F9, M1, M7 in three); «same animals» is an inference from the titles, the deposit gives no per-animal table; five per group in hippocampus, cortex and prefrontal cortex, cerebellum four against three. Side finding: the titles show three wild-type males and two females while the deposit's protocol text says 2 males and 3 females per group. **I2** (GSE156243, human organoids, week 15): re-derived from the public reads, all four knockout libraries carry the same +1T/+4T exon-1 insertion and the two wild-type libraries the reference allele; that those alleles are clone 1B rests on the authors' Fig EV1C and reviewer response (clone A2's genotype is not legible in the held figure); the paper sequenced four wild-type organoids and excluded two. **I3**: the Methods sentence is verbatim, but the Statistics section says experiments were performed on multiple batches unless stated otherwise and the RNA-seq legend states no batch, so one batch is not established. **Stays out (not checked):** the hippocampal-arms clause of the second row, the `CLAIM 014` row.
**Sentences that propagate:**
| Claim | Sentence |
|---|---|
| `CLAIM 002` and `CLAIM 005` (organoid transcript statements) | «The organoid RNA-seq (week 15, human) compares four knockout organoid libraries, all carrying the same biallelic exon-1 insertion (+1T and +4T; re-derived from the public reads), which the authors' Fig EV1C and reviewer response attribute to clone 1B, with two libraries of the parental line (four wild-type organoids were sequenced and two excluded after quality control); the batch of these libraries is not stated (Methods: organoids from the same batch unless stated otherwise; Statistics: multiple batches unless stated otherwise); a difference there is not shown to be independent of the clone.» |
| `CLAIM 005` (P47T statements) | «The P47T region libraries (mouse, GSE215425) carry mouse identifiers that repeat across regions, which indicates the same animals (the deposit states five mice per group and gives no per-animal table), so agreement across regions is one set of animals seen several times, not replication.» |
| `CLAIM 007` (P47T Wwox transcript) | «The four P47T region libraries come from the same mice by their sample titles (five per group in hippocampus, cortex and prefrontal cortex; cerebellum four against three).» |

## BATCH DISPOSITION — `BATCH_20261125_004` (2026-11-25, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED (verified remainder)

CLAIM 002, 005 and 007 paragraphs (same op list as ADV261). **Change class restated: MINOR.** **Blind check:** call E of batch 2 (`drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_batch2_verify_20261125/VERIFIER_REPORT_AS_DELIVERED_BATCH2E_IT_20261125.md`), statements I1 to I3: alleles of the four knockout libraries re-derived from the public reads; the clone 1B attribution rests on the authors' figure and reviewer response; one batch is not established. **Left out:** the hippocampal-arms clause and the `CLAIM 014` row (not checked).
