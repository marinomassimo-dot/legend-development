context_policy: SOURCE_FIRST

# Intake wave 6 — 2026-10-03 — Scientist A: can WWOX loss be measured outside the WOREE patient record?

- **Actor:** ACTOR_ID `scientist` (Scientist A), branch `task/sci-A-20261003w6`, dispatched by the Orchestrator under the standing authorisation of 2026-09-28.
- **Papers (6):** PMID 40507943 · PMID 40377402 · PMID 40524961 · PMID 36291747 · PMID 34852950 · PMID 42135313.
- **Method:**
  - All six sources were acquired as JATS XML: five from Europe PMC, and one (PMID 34852950) from NCBI efetch after Europe PMC returned HTTP 500.
  - Figures and supplements came from the PMC Article Datasets open-data bucket. This route worked where the PMC page served a reCAPTCHA and the publisher and Europe PMC binary endpoints returned 403. PMID 34852950's figures and supplements came via `pmc_pow_fetch`.
  - First-pass notes were written before any registry record about a paper was opened. **Declared exposure:** for PMID 34852950 the record ids `CORPUS-STUB-033` / `LIT-0059` were seen before reading; their contents were not.
  - `FIRST-PASS OBSERVATIONS COMPLETE → PRIOR KNOWLEDGE ADMITTED FOR COMPARISON` — admitted: `registry_records.py get` for the six PMIDs and their cited primaries; `CLAIM 027`, `DL-MOL-003`, `FT-180`, `FT-164`, `FT-169`, `CORPUS-STUB-132`, `LIT-0151`.
- **Procedure note:** a safety-classifier stop interrupted the first attempt to write the manifests in one generator. Per the Orchestrator's instruction, the write-up was redone paper by paper, and each locator was chosen from a span printed by a search over the validator's own text surface. No passage was skipped.
- **Not medical advice.**

## 1 · Question assigned

> What does each source add to, or limit in, the claim that WWOX loss has consequences measurable outside the WOREE patient record — in a non-cancer in-vivo tissue, in a human dose-response design, and in the Dvl/Wnt and HYAL-2/SMAD4 axes — and for each, is WWOX *measured* in a neural or whole-animal system, or carried over from an epithelial one?

## 2 · Per paper

| PMID | Verdict | WWOX measured where? | What is new versus held | Receipt (prepared) | Candidates |
|---|---|---|---|---|---|
| 36291747 (rat glaucoma) | INGEST | **Yes — rat retina in vivo, mRNA** | First record of Wwox mRNA falling in a non-genetic CNS injury. Microarray "0.864" is a log-scale ratio (≈0.47 linear) that fails FDR (0.187). qPCR 0.24-fold, n 3–4 | `sciA_36291747_1.json` (complete) | REGISTRY-01 |
| 34852950 (autopsy genetics) | INGEST | No — association only | Locus-wide (not genome-wide) signals for LATE-NC, HS and arteriolosclerosis. LATE-NC eQTL points to MAF. Deposited Suppl. Table 6 repeats NACC values in all columns | `sciA_34852950_1.json` (complete) | REGISTRY-01 (LIT-0059 corrected) |
| 42135313 (PD dementia) | INGEST | No — association only | "Dose" = number of loci carried. WWOX SNP HR null in biomarker cohorts; unreported design heterogeneity; not independent of its discovery study | `sciA_42135313_1.json` (complete) | REGISTRY-01 |
| 40377402 (Wnt review) | ABSTRACT-SUFFICIENT | No — one table row citing a cancer-cell paper | Adds nothing independent of Bouteille 2009 (FT-180) | `sciA_40377402_1.json` (partial: FT-180 unread) | WNT-01, REGISTRY-01 |
| 40524961 (DVL2/sterol) | OFF-AXIS for WWOX; INGEST for the inference check | No WWOX measurement; DVL2 measured in NSCs and mouse cortex | Nuclear DVL2 with **inhibited** TCF/LEF signalling. WWOX link is one citation (Celebi 2020) | `sciA_40524961_1.json` (partial: Figs 1–6 by legend; Celebi unread) | WNT-01, REGISTRY-01 |
| 40507943 (HA review) | INGEST (background) | No — DU145 over-expression only | Nervous-system section has no WWOX. AD-risk sentence cites five non-AD papers | `sciA_40507943_1.json` (complete) | HYAL2-01, REGISTRY-01 |

Receipt files are in the Orchestrator's scratch `receipts_pending_w6/`; none is appended to the real ledger. Each was dry-recorded into a throwaway copy of the ledger together with a copy of the state manifest taken from `main`: all six exited 0, and `verify` on the copy was OK.

## 3 · Patients counted once

No patient-level record is in any of the six sources: one rat study, two adult association studies and three reviews or cell papers. Nothing is added to any WWOX-DEE patient census.

## 4 · Answer to the question, with its limits

- **Non-cancer in-vivo tissue:** one source (36291747) measures Wwox in a whole animal's CNS tissue (rat retina), at mRNA level only. The array signal does not survive FDR; the qPCR is significant with n = 3–4. The injury is immune-mediated, not genetic, and the study says nothing about the direction of causality.
- **Human dose-response:** no WWOX dose-response exists in this set. The "dose" in 42135313 is a count of loci, and its WWOX SNP is a common variant whose effect is absent in the largest cohort class. In 34852950 the loss-of-function axis is absent altogether: common non-coding variants are labelled "WWOX" by position, and the LATE-NC eQTL points to MAF.
- **Dvl/Wnt axis:** both 2025 sources only re-cite unread cancer-cell primaries. The one measurement in the set (40524961) shows nuclear DVL2 occurring *with inhibited* canonical Wnt signalling. That weakens, rather than supports, the inferred step "WWOX loss → nuclear DVL2 → Wnt hyperactivation" behind `DL-MOL-003`.
- **HYAL-2/SMAD4 axis:** the review that states the neural claim (40507943) carries only DU145 over-expression data from one laboratory; it gives no neural measurement.
- **Limits:**
  - Two readings are partial (40377402 and 40524961).
  - The three cancer-cell primaries behind the Dvl direction (PMIDs 19465938, 23030478 and 32368285) remain unread.
  - The rat retinal finding is n = 3–4 and mRNA only.

## 5 · What would change the model, and what would falsify it

- **Would change it:**
  - nuclear β-catenin or a TCF/LEF readout measured in WOREE organoids or Wwox-null neural tissue (the experiment already proposed in `DL-MOL-003`);
  - WWOX protein measured in an acquired CNS injury with cell-type resolution;
  - a full read of Bouteille 2009 (FT-180) to establish the evidence class behind the Dvl direction.
- **Would falsify "WWOX loss → canonical Wnt hyperactivation" in neural context:** a WWOX-null neural system showing nuclear DVL2 without TCF/LEF activation, or with reduced activation, which is the pattern 40524961 shows under a different perturbation.

## 6 · Corrections to LEGEND found after the first pass

- `LIT-0059` (PMID 34852950): identity fields empty and clinical relevance HIGH → corrected to LOW with the identity filled in (`CC-20261003W6-A-REGISTRY-01`).
- `DL-MOL-003`: "tre studi indipendenti" rests on three primaries with no receipt; the 2025 restatements are not independent; the inference step is not automatic (`CC-20261003W6-A-WNT-01`).
- `CLAIM 027`: the newest source for the axis adds no CNS evidence (`CC-20261003W6-A-HYAL2-01`).
- Minor and not proposed as edits: `FT-073` says LEGEND has "no object" for PMID 27845895, but a partial receipt `FTR-20260921-27845895-01` exists — noted only, because `FT-073` is another actor's record.

## 7 · Brief premises found wrong

- A3 is not the "experimental counterpart" to A2: they cite different WWOX primaries (Celebi 2020 vs Bouteille 2009).
- The DVL2–p53 relation in A3 is a STRING network plus one unquantified co-IP, not co-localisation.
- A1's "neural" WWOX claim has no neural datum behind it. Its "63 body hits" counts the XML including references; the text layer holds 55.
- A6's "dose-response" is a count of loci, not WWOX allele dose.
- A5: "independently of ADNC" cannot be checked from the deposited supplement.
