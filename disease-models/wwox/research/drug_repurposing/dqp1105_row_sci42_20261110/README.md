# SCI42 S5 — the DQP-1105 registry row resolved at its primary source (2026-11-10)

Non-canonical research material. Not medical advice; no dose, schedule or route. Reference genotype class only. One narrow package: one producer, one independent blind verifier, one recheck of the corrections. Task record `ledger/tasks/orchestrator/ORCH-SCI42-20261110.json`. It answers the question left open by `generation_it41_20261109/verify/VERDICTS.md` C2 (which subunit and measure the contested registry row belongs to). Labels DATO / INFERENZA / IPOTESI.

## Decision this changes

* **The contested row is resolved at source.** DATO: in the primary paper (21807990, Acker 2011, Mol Pharmacol), Table 1, row "1105 (19)", the fitted IC50 values of DQP-1105 are GluN2A no effect, GluN2B 113, GluN2C 7.0 and GluN2D 2.7 µM (rat cDNA, Xenopus oocytes, two-electrode voltage clamp, 100 µM glutamate plus 30 µM glycine, pH 7.4, 23 C, holding potential −40 mV; the mean ± SEM of Table 3 are 121 ± 32, 8.5 ± 1.2 and 2.7 ± 0.2 µM for GluN2B, GluN2C and GluN2D). The registry (GtoPdb 2026.3.1) holds 113.0, 7.0 and 2700.0 nM. **The GluN2B and GluN2C registry rows therefore carry micromolar values stored as nanomolar (a 1000-fold unit error: their pIC50 should read about 3.95 and 5.15, not 6.95 and 8.15); the GluN2D row is correct.** The numeric identity with Table 1 is DATO; that the cause is a unit slip is INFERENZA.
* **The 113 is a GluN2B measurement.** The "GluN2C" wording of the assay description on the GluN2B registry row is the registry's text, not the paper's. The IT41 statement "the subunit of the 6.95 is unresolved" is replaced by this resolution; the IT41 verifier's alternative readings (copied GluN2C text; value from the GluN2C assay) are both excluded by Table 1.
* **Role as a comparator: an exclusion for the GluN2B comparison, on the source's own numbers.** DQP-1105 is a GluN2C/GluN2D-preferring noncompetitive inhibitor (inhibition voltage-independent, p = 0.86, n = 5, and not overcome by glutamate or glycine). GluN2B is about 113–121 µM in rat oocytes, 206 ± 137 µM for human GluN2B, and shows no detectable effect in the BHK calcium-imaging assay. Scope limits kept: the GluN2B IC50 is a fitted value with complete inhibition assumed (the maximum at GluN2B is not reported), GluN2B was not assayed in the HEK patch configurations (where GluN2A selectivity is weak), and "no effect" means none at the concentrations evaluated. **Nothing here is a statement of benefit or harm for WWOX.**
* **Class lesson (for the integrator).** A value filed under a target can fail by unit as well as by subunit: two of the three DQP-1105 rows of one registry snapshot carry a unit slip. A registry affinity that disagrees with the source by a factor of 1000 is a reason to open the source, not to read the number.
* Nothing changes a rank, a card verdict or a work order.

## Status of the deliverables (nothing applied to a consumer)

| Layer | State |
|---|---|
| Sources read | 21807990 partial full text (Abstract, Introduction, Materials and Methods, Results through Table 3; the Table 1 image viewed; Figures 1–2, Discussion, Table 2 and later tables, supplement not read); 37566734 partial full text (Introduction, Table 2 as text, Methods, agonist-dependence Results; Table 1 image not viewed, 403) |
| Access, recorded | The PMC page of 21807990 answered the producer's and the Orchestrator's plain curl with a bot check (not retried by another route) and the verifier's plain curl with the article; the reading used the verifier's saved copy (SHA-256 `2aa970852b82bd4b66eb18103c074494bb2ec478b33d0d042c50e82a5c4b936a`), stated in the receipt. The hash identifies one saved copy, not the page: compare text, not hashes. The ChEMBL live query gave HTTP 200 with an empty list to the producer and HTTP 500 to the verifier, so "no ChEMBL document" is not claimed |
| Receipts | 2 staged in `output/receipts/` and `research/receipt_staging/sci42s5/` (suffix -92), validated, not recorded |
| Verifier | first pass on the abstract-level draft: 4 supported, 4 partly, 0 not supported; the draft had concluded "unresolved" because the producer's route was blocked; the verifier's own plain curl reached the paper and decided the row set. Recheck of the rewritten rows: 24 of 25 correct, 1 cosmetic (a quote carrying a reference number, fixed afterwards), 0 new errors; receipts' provenance statement judged defensible with stated limits |
| Delivered tables | `output/row_resolution.tsv` (8 rows), `decisive.tsv` (8), `evidence.tsv` (6), `queries.tsv` (10) |

## What the evidence does not give

The primary Discussion and most Figures were not read; the supplement of 37566734 (a re-measurement of DQP-1105 on GluN2D in HEK293: 1.4 µM at peak and 0.72 µM at steady state, same group, another system) was not read. The paper does not report a per-subunit maximum for DQP-1105. The registry cause (a unit slip in curation) is inferred from the numbers, not from any curation record.

## Provenance and distribution

The corrected values come from the paper, not from the registry: the registry-derived numbers appear here only as the object of the correction; they are share-alike and do not enter the shareable edition (the shareable view omits compound names and registry-derived values).
