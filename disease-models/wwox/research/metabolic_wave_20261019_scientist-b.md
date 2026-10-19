# Metabolic wave 2026-10-19 — Scientist B — group G2 (simple carbohydrates, fructose, glucose/HIF1A, ketogenic diet, hypoglycaemia)

Actor `scientist-b`, task `METAB-G2-B-20261019`, branch `task/METAB-G2-B-20261019`. Mode `PRIMARY_EVIDENCE_READ`, `context_policy` SOURCE_FIRST for every first read. Public disease-level record; nothing here is medical advice. Receipts are staged, not recorded (see the orchestration rule in the dispatch brief).

## 1 · Result in one table

| PMID | Paper | Tier | Depth (receipt as staged) | Manifest | Main finding |
|---|---|---|---|---|---|
| 33520443 | Baryla 2021, GDM leukocytes | 1 | partial (supplement raw XLS not opened) | PASS | WWOX and HIF1A transcripts uncorrelated; ratio arithmetic; Fig 6 contradicts text |
| 31145772 | Jamaspishvili 2019 (selection: "Permana") | 1 | complete | PASS | PubMed identity defect; rs17797882 null for T2D; nominal control-only traits |
| 40831798 | Hu 2025 KD in DEE review | 1 | complete | PASS | KD base rates across DEE; WWOX absent |
| 40659031 | Joshi 2025 in silico KD | 1 | partial | PASS | ketone rescue only upstream of acetyl-CoA; "primary" untested |
| 29481666 | Teslovich 2018 | 2 | PARKED | n/a | body unreachable lawfully, cascade below |
| 33854788 | Ouyang 2021 mGWAS | 2 | partial | PASS | WWOX-region SNP suggestive only; MR does not involve WWOX |
| 41007296 | Baryla 2025 TCGA ratio | 2 | partial | PASS | ratio not independent in six of seven models |
| 41830506 | Klepper 2026 Glut1DS KDT | 2 | partial | PASS | 39 percent not controlled; secondary failures; abstract EEG counts inverted |
| 42047543 | Pain 2026 decanoic acid iPSC | 2 | partial | PASS | one line, transcripts, mixed glycolytic direction |
| 39876842 | Kuang 2024 lactylation review | 2 | partial | PASS | speculative; one flagged reference |
| 36530994 | Chu 2022 ADI-PEG 20 | 3 | partial | PASS | GG advantage on 9 patients, lost on pooling |
| 33363507 | Fei 2020 metabolic control review | 3 | partial | PASS | two opposite therapeutic directions |
| 39997753 | Beltran-Velasco 2025 glycogen review | 3 | partial (screening depth) | PASS | no WWOX; GSK-3 beta once; glycogen not a tested buffer |
| 37907746 | Li 2023 KHK microglia | 3 | partial (screening depth) | PASS | db/db model; non-specific knockdown; methods error |
| 40500435 | Wang 2025 Nature fructose microglia | 3 | partial | PASS | brain lactate rises 2.7-fold with diet alone |
| 42171828 | Cornelio-Martinez 2026 HIF-1 alpha review | 3 | partial (screening depth) | PASS | HIF-1 alpha inhibitor sign reverses with timing |
| 24086726 | Sakai 2013 Japanese replication (extra item) | extra | partial | PASS | rs17797882 null; allele-convention conflict |

Fifteen readings from the selected sixteen plus one extra item; one parked. Dossiers: `fulltext_dossiers/PMID<PMID>.md`; manifests: `deepdive_manifests/`; receipts: `receipt_staging/scientist-b/`; commit candidates: `CC-20261019-SCIENTIST-B-G2-{HUMAN-AXIS,KD-PRIOR,FRUCTOSE}-01`.

## 2 · What the lot, read as a set, says (INTERNAL_EDGES the Orchestrator did not declare)

1. **One citation chain ends at a nominal number.** Ouyang 2021 says "WWOX is related to HOMA-beta" citing the Harbin paper (31145772); the Harbin HOMA-beta coefficient is p 0.014, controls only, about 64 uncorrected tests, an uninterpretable scale; the Japanese replication with Bonferroni correction (24086726) finds nothing (p 0.91). The three form one story: the human-genetics insulin-secretion pointer for WWOX is unsupported.
2. **The two papers on rs17797882 analyse opposite alleles.** The Harbin paper uses T (frequency about 0.24) as "risk allele", the Japanese paper uses C (about 0.79); with older controls the Japanese WWOX OR falls below 1. Neither paper notes it. The originating meta-analysis (not in this lot) would settle which allele is the effect allele.
3. **The WWOX/HIF1A ratio is the same defect in three guises.** In GDM leukocytes (Fig 4) WWOX and HIF1A are uncorrelated (rho -0.05) and the ratio's correlations with HIF1A targets are coupling to HIF1A; in TCGA glioma the favourable group has WWOX up and HIF1A down, the ratio is not independently prognostic (six of seven models), and the Conclusions assert HIF1 alpha stabilisation from mRNA alone; in the 2022 fibroblast and review papers of the same laboratory the arc is never measured in neural tissue. One laboratory, four papers, no independent confirmation.
4. **Metabolic intervention has no single sign.** Fei 2020 carries both "inhibit glycolysis" and "supply energy in hypometabolism"; Joshi 2025 models only energy sufficiency and cannot rank KD mechanisms; Klepper 2026 shows ketones fail in 39 percent of the cleanest fuel-defect epilepsy; Hu 2025 gives a wide base rate; Cornelio-Martinez 2026 shows the sign of a HIF1A intervention reverses with timing. A KD response in WOREE (CLAIM 042, denominator unstated) identifies no lesion in either direction.
5. **Lactate is not a clean readout.** Wang 2025: a diet exposure raises neonatal brain lactate 2.7-fold via a microglial transporter; Kuang 2024: lactate's signalling role is uncertain. The lactate-up readout in Wwox-null fibroblasts survives conditions, but a brain lactate rise in a knockout would be uninterpretable without matched diet and cell-type resolution.
6. **Two microglial fructose routes disagree** (Wang hexokinase and hypo-phagocytic neonates; Li KHK, NOX4 and activated adult microglia). Neither is WWOX; both are low priority.

## 3 · Effect on the disease model and research lines

- **RL-003 (metabolic/lipid line):** no claim is reversed; three readings narrow the human-genetics and ratio support (items 1 to 3), and CLAIM 042 gains a base-rate boundary (commit candidate KD-PRIOR). Change class MINOR throughout; the legend-locator-audit trigger is not met. Triples are in the candidates for a later blind audit.
- **Negative results kept, with revival triggers** (in each dossier section 6): Harbin HOMA-beta signal; WWOX-HIF1A ratio as biomarker; fructose/KHK as WWOX-DEE mechanism; glycogen buffer; WWOX-ASS1-arginine as therapeutic predictor.
- **Questions of the selection file** — 1: no human or neural measurement of the glycolytic shift exists in this lot (GDM leukocytes mRNA only); 2: insulin secretion loses its only nominal support, amino-acid handling rests on a rare suggestive SNP; 3: a better prior is Hu 2025 plus Klepper 2026, and Joshi 2025 cannot adjudicate energy repletion against Warburg reversal; 4: glycogen/GSK3B buffer untested in any source; 5: fructose is a diet-exposure question with a developmental window, not a WWOX mechanism.

## 4 · Defects found in sources and metadata (for the Orchestrator)

- **PubMed record for PMID 31145772 is a hybrid**: title and abstract of the 2019 Harbin article with the authors, DOI and pages of a 2021 Brawijaya article. The staged receipt and manifest carry the DOI PubMed stores (as the brief requires); the artefact is the article under DOI 10.18388/abp.2018_2632. An `identity_correction` may be warranted at integration. The mismatching 2021 PDF (1,979,803 bytes, sha256 0d1d2ed323fe4cdbf74dd5a7ceac15664469c4b23bb5afc730792d80f96e9694) was fetched and discarded; the digest is recorded in the manifest.
- Figure-versus-text mismatches: Baryla 2021 Fig 6C and 6E; Klepper 2026 abstract EEG counts; Chu 2022 text P 0.025 against log-rank 0.020 (different tests, not an error).
- Arithmetic and method slips in sources: Ouyang 2021 MR OR 0.004 with CI 1.001 to 1.006 and a repeated OR line for two metabolites; Li 2023 human-genome mapping for mouse RNA-seq; Beltran-Velasco 2025 synthase-inhibitor sentence; Klepper 2026 "23 percent of non-responders".
- PMC figure file numbering is reversed in three papers (Klepper 2026, Pain 2026, Ouyang 2021); declared in the manifests.
- Integrity: one flagged reference in Kuang 2024 (declared citation-only).

## 5 · Parked and the cascade run

**PMID 29481666 (Teslovich 2018, PMC5905595), tier 2, parked.** Europe PMC `fullTextXML` HTTP 500; Europe PMC render and OUP publisher PDF behind Cloudflare (403); PMC HTML and PDF paths served the reCAPTCHA page under no-User-Agent, curl and identified-agent policies; PMC efetch XML returned 21 kB of front matter only (outside the open-access subset); PMC OA S3 bucket listing empty; OpenAlex and Semantic Scholar resolve only to the same PMC page; Europe PMC supplementary files returned an error bean. No lawful body reached; abstract is not a read. Revival: operator-supplied PDF, or a lawful route to the NIH author manuscript. Reserve rule applied: the lot was otherwise exhausted, so the extra self-chosen search was run (WWOX with glucose, insulin, diabetes, ketogenic, fructose, glycolysis, HIF1A, lactate, glycogen; 51 hits; deduped by `paper_packet.py` and the receipt ledger); 24086726 qualified and was read; 35984507 already holds two partial receipts (a resume belongs to its owner); 26390919 is group G3 territory.

## 6 · Method deviations and DEFAULTS_TAKEN

See the task contract `ledger/tasks/scientist-b/METAB-G2-B-20261019.json` (`DEFAULTS_TAKEN`, `STOP_LOG`). In brief: committed under `LEGEND_STALE_SURFACES_BECAUSE` because manifests and staged receipts stale five derived surfaces that only the Orchestrator regenerates; validated each staged receipt against a scratch copy of the ledger and state manifest (the real ledger and state manifest untouched, one accidental write to the worktree state manifest restored from `HEAD` content); no discovery-ledger writer exists, so leads travel inside commit candidates; screening depth for four readings (three reviews and one mouse paper) is declared in each receipt and loc_note, not hidden.
