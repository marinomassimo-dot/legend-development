# CC-20261026-SCIENTIST-A-LUCASCLARKE-01

- **Class:** ORDINARY (research-layer; touches no consolidated baseline claim; every narrowing below is OWED a blind locator audit by someone other than the producer before it may touch a baseline claim).
- **target_wm_version:** none (no working-model change proposed).
- **Source:** `disease-models/wwox/research/fulltext_dossiers/PMID42909904.md`; manifest `PMID42909904.json` (104 locators); staged receipt `research/receipt_staging/scientist-a/FTR-20261026-42909904-01.json`.
- **All content is NOT WWOX EVIDENCE** in the sense of human disease: a *Drosophila* Alzheimer's-disease model, a different disease context from WWOX developmental and epileptic encephalopathy. Class-level; no dose, administration or suitability statement; not medical advice.

## Proposals

1. **Registry identity (paper and literature records):** the published article (PMID 42909904, DOI 10.1093/braincomms/fcag385, PMC13684411) is a record of its own, `complete_fulltext_read`, **not merged** with `PAPER 158` / `LIT-0447` (the bioRxiv preprint PPR1015434). Role: the only corpus source that moves *Wwox* in both directions in one model, now with the Ldh double-RNAi, Atf4, sima:GFP and metabolomics reported with statistics and supplementary tables.
2. **Correct `PAPER 158` / its dossier (the preprint reading), wording only:** (a) the preprint's "two independent UAS-RNAi constructs" is not carried into the published assay rows — the KK line (median 40 d; Abeta42 24 d) is absent and only the TRiP line remains; (b) the preprint's "upregulation reduces L-methionine" becomes, in the published text, "L-methionine decreased after overexpression in the LacZ background but unaltered in the presence of Abeta42", the interaction reflecting the absence of the fall under Abeta42 (Supp Fig 8: about 2.85e6 -> 0.9e6 in LacZ, about 1.5e6 vs 1.46e6 in Abeta42); (c) "lactate not restored" (preprint) is replaced by "without a reduction in Ldh or 2-hydroxyglutarate", and lactate is not a displayed OE panel: in that cohort Abeta42 itself did not raise lactate.
3. **`DL-MECH-020` annotation (HIF1A -> PDK -> PDH chain):** the published paper tests none of PDK or PDH or pyruvate or TCA flux; it reports a sima:GFP fluorescence null in one genotype pair (Abeta42 background, day 14, n 7-9, t 0.6623, P 0.5185) and states Atf4 "rather than" sima is "primarily" responsible for the Ldh rise. That is a reporter-level negative on HIF1alpha in a fly with transgenic amyloid; it is not a test of HIF1alpha activity or targets, and the reporter is described three ways (UAS-sima:GFP in Methods, "endogenously tagged" in Results, a PBac stock in Supp Table 1A). **`CLAIM 025` nuance wording:** the registry's "HIF1alpha-independent" is the registry's own phrase; the paper writes "rather than ... primarily". Narrowing, owed a blind audit.
4. **`DL-BIO-008` note:** lactate in this fly model is conditional: up only with Wwox reduction plus amyloid (interaction F 23.606, padj 0.0174; knockdown effect +1.30 log2 with Abeta42, -0.43 log2 without), so the paper neither supports nor contradicts the human MRS datum "extremely low".
5. **Leads (staged, numbered on `main`):** `lead_wwox_oe_glycolytic_transcripts.json` (Wwox OE lowers Gapdh1, Eno, Pgk, Pgi, Tpi, undiscussed) and `lead_fly_lactate_conditional.json`.
6. **`HYP-20260709-01` impact:** none; no ketone, PDH or oxidative-substrate manipulation is present.

## Owed

- Blind locator audit of the narrowing items (3) and the second half of (2) before any propagation.
- MetaboLights MTBLS12344 (pyruvate and PDH-adjacent rows) and the ArrayExpress deposits are not retrieved; if pyruvate or TCA intermediates are tested there, items 3 and 4 may need to be restated.
- The preprint has no manifest, so no persisted locator is contradicted by this reading.

---

## BATCH DISPOSITION

**Verdict:** PROPAGATED (registry and research layer; `WM_v7.27` preserved)
**Batch:** `BATCH_20261019_018` (2026-10-26, MINOR, MANUAL, ACTOR_ID `integrator`, task `BATCH_20261019_018`)

- **Proposal 1 landed:** `PAPER 567` and `LIT-0838`, a distinct identity for the published article, not merged with `PAPER 158` / `LIT-0447`; depth `complete_fulltext_read` and the coverage fields taken from `FTR-20261026-42909904-01`, locator count 104 re-derived from the manifest on disk.
- **Proposal 2 landed (wording only):** `PAPER 158` Genotype/model line (second RNAi construct), Note (L-methionine and lactate) and a pointer paragraph (sima reporter qualification), each with the superseded wording quoted per `prompt_batch_commit.md` 7.2; the preprint dossier `PPR1015434.md` annotated at the two lines that carried them. `LIT-0447` points to `LIT-0838`. The registry record of `PAPER 158` did not itself carry the words «two independent RNAi»; they lived in the preprint dossier it cites, and the record now says what the published assay rows support.
- **Proposal 3 landed:** `CLAIM 025` Nuance re-sourced to the paper's own text (the superseded wording quoted); the same correction in the mirror paragraph of `meta_metabolism_current.md`; `DL-MECH-020` qualification block. The integrator checked the quoted sentences against the Europe PMC JATS text (Discussion «Atf4, rather than the HIF1α orthologue sima, is primarily responsible … in this fly model»; Results sima:GFP; L-methionine sentence); the article contains no mouse experiment. `DL-MECH-023`: tension with Janczar 2017 (PERK unchanged) noted, not resolved.
- **Proposal 4 landed:** a dated note in `DL-BIO-008`.
- **Proposal 5 not landed here:** the two staged leads are not part of this batch. **Proposal 6 landed as a dated consequence note** in `HYP-20260709-01` and `HYP-20260709-05`, labelled exploratory; no score, status or ranking line was changed (no direct PDH support in the paper; the LDH/lactate branch logic is indirect).
- **Still owed:** the blind locator audit of the narrowing items, by someone other than the producer; MetaboLights MTBLS12344 retrieval. The `CLAIM 025` text is written in the paper's own words, with the audit state stated inside it, and its Status, Type and Summary are untouched.
- **Nothing else moved:** no ledger receipt, no working-model block; `WM_v7.27` is carried forward.
