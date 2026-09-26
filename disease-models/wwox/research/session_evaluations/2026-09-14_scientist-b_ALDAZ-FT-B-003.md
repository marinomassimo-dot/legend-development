# Session self-evaluation — `scientist-b` · `ALDAZ-FT-B-003` · 2026-09-14

> Completed after the analysis and before takeaways. Public, disease-level, de-identified.

## Scope and executable verdict

- **Batch/session:** one paper, PMID 30285739 (Bonin 2018, VOPP1–WWOX), named authorisation under `ALDAZ-EXEC-20260913`.
- **Receipt:** `FTR-20260914-30285739-01` — `complete_fulltext_read`.
- **Manifest:** `deepdive_manifests/PMID30285739.json` — strict PASS, **0 gaps**, 41 locators, 23 artefacts, `--verify-artifacts --require-current-schema`.
- **Receipt verification:** chain OK, tail anchored in the state manifest.
- **Structural LINT:** PASS (baseline PASS captured before any edit).
- **Release gate:** PASS, 0 BLOCKS (baseline captured before any edit).

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full text, figures, tables, supplements | Every section in order; all 7 figures inspected as native rasters (1183×1724–1949×2373); all 7 supplements retrieved and inspected as pixels. No `<table-wrap>` exists — tables are supplementary images. | strong | — |
| Main message and original contribution | Stated in dossier §2–3 and M4b §B: three-route co-association plus **mutation-tested** WW1 and PPPY165 dependence, with the binding-deficient mutant used as a functional control throughout. | strong | — |
| Hidden gold beyond keywords/abstract | Five findings exist only in the pixels/supplements: Y157A partial loss, Figure 4e's undeclared NIH3T3 system, two incompatible WWOX cut-offs, `P=0.09` whole-cohort, A549 death below baseline. | strong | — |
| Source parity | Breast-oncology paper read at full depth for a CNS disease model; the gold was in a figure lane. | strong | — |
| Team type, field density, observation vs interpretation | Institut Curie breast group: primary for neither gene nor disease (6/51 on WWOX). Clinical half weighs strong, binding half competent-but-borrowed (Y33R premise imported), "sequester" typed as interpretation. WWOX∩VOPP1 = **2 papers in all of PubMed**. | strong | — |
| DATO / INFERENZA / IPOTESI separation | Applied per proposition; "sequester" → INFERENZA, Y33R→WW1 → imported premise, directness → not established by anything. | strong | — |
| Existing claims touched; conflicts/revival triggers | `CLAIM 026`: one sentence **added**, nothing retracted, directness negative preserved. REVIVAL_TRIGGER recorded (purified/recombinant or biophysical measurement; or neural material / disease allele). | strong | — |
| Multi-hop and corpus cross-query | 53 refs enumerated from the fingerprinted ref-list; 32 WWOX-direct + 5 VOPP1-direct; 32 resolved by identity, 11 with receipts, **5 VOPP1 antecedents unread and in no registry** — named and routed. Cross-query: VOPP1 in 1 of 94 manifests; "two-hybrid" and MDA-MB-468 in **zero**. | strong | 5 antecedents queued to the orchestrator, not silently dropped |

## Persistence diagnosis

- **Durable IDs:** `FTR-20260914-30285739-01`, `CC-20260914-30285739-01`, manifest, dossier, M4b note, this evaluation.
- **Reading debt:** 5 VOPP1 antecedents named with reasons in `CC` §6 (20571887 is the load-bearing one; 21519330 and 15735698 propose competing mechanisms).
- **Receipt fingerprint/coverage:** bound to the efetch JATS sha256; `figures: read` and `supplementary: read` are honest — images were opened, not captions trusted; `tables: not_present` because the article has none; `limitations: not_present`.
- **Can a future run distinguish full text from abstract only?** Yes: 41 locators across body, figure and supplement surfaces, each bound to a fingerprinted artefact, plus acquisition recipes for replay.

## Process and capability diagnosis

- **Skills used/declined:** `find-fulltext` used inline (cascade recorded); 5 declined with reasons in the manifest.
- **Failures and retries caught before an overclaim:**
  1. **PMC `/bin/` served 21.4 kB HTML stubs disguised as `.jpg` and `.tif`** for Figures 2–6 and all 7 supplements, returning **HTTP 200**. A size/`file`-type assertion caught it; a naive downloader would have declared `figures: read` over HTML. Recovered via the `pmc.../instance/` and publisher static-content routes.
  2. I downloaded PMC figure JPGs, then inspected the **higher-resolution PDF-extracted** rasters instead. Rather than declare artefacts I had not viewed, I **deleted the un-inspected duplicates** so the evidence tree contains only inspected surfaces.
  3. Every body snippet was sliced programmatically between explicit endpoints out of the normalized XML and asserted unique and non-abstract **before** the validator ran — zero quote-verification failures on the first strict run.
- **What the corpus expectation could have cost:** the contract warned that expectation must not shape the report. The live risk here was the opposite of the usual one — the corpus expected *less* (Hussain's "VOPP1 has no pull-down") and the paper delivers *more*. Had I read to confirm the corpus's framing, I would have under-reported mutation-tested WW1/PPPY dependence and an endogenous co-IP.
- **Residual risk:** the `Y157A partially impairs binding` reading is a densitometric judgement on one blot lane; I recorded it as `panel_only` with the band described, not as a quantified claim.
- **Next decisive action:** read `20571887` — VOPP1's lysosomal identity is imported from it and this paper's compartment argument inherits that premise.

## Micro-upgrade shipped

**Finding, disease-agnostic:** `[RATCHET] retraction_check.dependencies: not declared` and the `declaration-is-not-attestation` ratchet both police *unbacked declarations*. This session hit the **mirror-image defect**: a paper named in three working documents as the only independent support for a live claim existed in canon as `not_processed` with `Claim links: none` — **real support with no registry record**, which no current ratchet can see. Recorded in `CC` §2 as a flag for the orchestrator rather than implemented here, because the counter would live in `growth_anchors.py`, which this contract does not own. Stated so it is not lost: the measurable form is *"working documents assert support from a PMID whose registry record is a placeholder with no claim link"*.
