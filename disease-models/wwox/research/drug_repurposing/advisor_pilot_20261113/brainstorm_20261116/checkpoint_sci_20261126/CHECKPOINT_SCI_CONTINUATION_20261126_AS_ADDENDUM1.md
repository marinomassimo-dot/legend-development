# Checkpoint AS, addendum 1 (SCI, 2026-11-26, after the landing of ADV-292; read together with AS, which is not edited)

Hypothesis level; not medical advice. Three items from ADV's message of the direction round after AS was hashed.

## 1. ADV-292 is landed

`development/main` `c8ae8a5ec34d803b75032107e49d2562a6468174` (safe_push PUBLISHED, gate PASS, verified by ls-remote; before it a first push was refused on a stale repurposing view after the receipts, regenerated and committed, then published). IT 6f4e0008 and ADV were told. AS itself (sha256 `62b07db4e728fa043ef1312df4853c07997897139da783d3c3ea86aa531e3332`) is on that sha.

## 2. Errors in my sentence files, reported by ADV from IT's first blind check; the successor verifies each on the sources and corrects the files after IT's second check reports

I have not re-read the sources for these in this window; they are listed as reported, to be checked before editing.

* **ADV-289 (`adv289_breton_s3c_dapv_block_sci_20261125/RESULT_ADV289_SCI_20261125.md` section 7) V1:** my sentence says "'At least one half' is therefore at the ceiling d-APV reached in that figure, not below it". By my own numbers in the same sentence the block was about 0.6 of the measured amplitude, which is above one half, so one half is not at the ceiling. Wrong as written (checked by arithmetic on my own sentence, not yet on the figure).
* **ADV-289/290 V4 and V6:** the Table S1 value 0.66 s is the pooled baseline of 119 bursts, not the carbenoxolone group's own baseline. Reported by IT, not yet re-read by me.
* **ADV-291 headline (`adv291_breton_s4_s12_sci_20261126/RESULT_ADV291_SCI_20261126.md` and `ADDENDUM1_CLOSURE_ADV291_SCI_20261126.md`) and AR section 1:** "the dossier sentence 'animal-level significance in 8 of 9 for delta' is reversed" is not right as a headline. The paper's Results say "For the delta range, 8/9 subjects showed significant coupling" by the authors' own criterion; the S1G animal-level rho is positive in 8 animals with p < 0.05 in 2 of 9. ADV's corrected label (my headline and ADV's meeting entry both said reversed): "ambiguous: the authors' criterion versus the S1G animal-level p < 0.05 in 2 of 9; label which statistic is which". The successor edits the ADV-291 RESULT and ADDENDUM1 wording (and any sentence I proposed for CLAIM 021 or the dossier line) to carry both statistics with their labels; claim_registry only through BATCH_COMMIT.

## 3. Do not resend the four sentence sets to IT

They went by path in one message to IT 6f4e0008 (and ADV-292 by `PROPOSED_SENTENCES_ADV292_SCI_20261126.md`). After IT's second check, send IT the corrected versions of V1, V4, V6 and the ADV-291 relabelling.
