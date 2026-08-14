# Batch/full-text self-evaluation — Aqeilan three-study batch, 2026-08-14

## Scope and executable verdict

- **Batch/session:** three Aqeilan-group studies not previously backed by an adequate complete receipt.
- **Studies and receipt IDs:** PMID 42422765 — `FTR-20260814-42422765-06`, complete; PMID 25012504 — `FTR-20260814-25012504-01`, complete; PMID 34268881 — `FTR-20260814-34268881-03`, partial because Appendix Figures S1–S6 are unavailable.
- **`session_self_eval.py`:** PASS; 96 receipts, 44 complete events, 36 active complete reads, unread-premise ratchet tightened to 5/5.
- **Per-study manifests:** strict schema-v2 artifact/fingerprint/text verification PASS for all three PMIDs.
- **Receipt verification:** PASS; 96 chained events, tail anchored.
- **Structural LINT:** PASS; unbacked registry declarations improved to 16 from baseline 17.
- **Publication gate:** PASS, 0 blocks.
- **Release regressions:** last full runner verdict FAIL. Three batch-caused generated-state failures (coverage report, batch queue, reading state/unread-premise baseline) were regenerated/tightened and their targeted suites now PASS. Three ambient failures remain: an unrelated nested checkout under `.claude/worktrees/evidence-index` exposes missing paths to root-level tests, and `.claude/settings.local.json` is present while ignored.
- **Local verdict:** PASS for the two complete reads; PASS with declared residual source gap for Steinberg. All batch-owned targeted tests and gates pass.
- **Workspace/global verdict:** not fully green because of the three ambient release-regression failures above. Legacy self-eval gaps remain declared but non-blocking; no concurrent-writer failure occurred.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | Obeid: main + S1–S8 completed; Abu-Remaileh: structured article, 10-page PDF, 6 main figures/33 panels, 7-slide PPT/18 supplemental panels and 4-page legends; Steinberg: 20 pages, 11 figures/69 panels, 5 XLSX sheets, Expanded View, Appendix Table S1 and 47-page review file. | strong | Steinberg Appendix Figures S1–S6 absent from the official eight-file package; receipt remains partial. |
| Main message and original contribution | Obeid: early postnatal WWOX replacement can rescue severe null-mouse phenotypes, with long-term expression bounds. Abu-Remaileh: WWOX WW1 restrains normoxic HIF1α and glycolytic reprogramming. Steinberg: isogenic and patient-derived human organoids reproduce several WWOX-DEE phenotypes and show partial genetic rescue. | strong | Do not translate proof-of-concept rescue into a physiological dose/window/safety claim. |
| Hidden gold beyond keywords/abstract | Obeid S2 graph/caption `n` mismatch and S5 survivor-selected regional overexpression; Abu-Remaileh S5 GLUT1/PHD3 rather than PDK1/PHD3, `100 mg/kg` printed in both surfaces, and WT glucose movement; Steinberg peer-review outlier removal/inconclusive lineage claim plus five Excel auto-date gene-symbol corruptions. | strong | These findings required pixels, legacy binaries, raw spreadsheets or review history, not gene-keyword search. |
| Source parity: context, type and recency | All three are primary experimental studies and were weighted for measurements rather than journal/recency. The 2014 metabolism paper was read as seriously as the 2026 gene-therapy paper; the 2021 organoid paper was not promoted merely for phenotype proximity. | strong | None. |
| Team type, field density, observation vs interpretation | Aqeilan group: experimental lab, primary for WWOX and disease, PubMed count 137 total/65 WWOX at measured audit. Direct measurements remain high weight; GABA and translational interpretations were independently bounded. | strong | Group provenance does not validate its own causal interpretations. |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | Direct rescue, HIF1α assays, electrophysiology and marker changes are DATO. Depolarizing GABA, neural metabolic flux and physiological dose equivalence are IPOTESI/INFERENZA. Digoxin remains target validation, not a candidate. | strong | GABA needs E_GABA/NKCC1-KCC2/pharmacology; metabolism needs stage-matched flux. |
| Existing claims touched; conflicts/revival triggers | PAPER 039 full-read status, GABA wording, DL-MECH-034/094 metabolism, DL-MECH-020 and DL-MOL-009 digoxin wording, and Obeid timing/expression interpretations are all touched. Three commit candidates state exact corrections. | strong | Canonical application is deferred to lawful BATCH_COMMIT. |
| Multi-hop and corpus cross-query | Reference lists enumerated in manifests (Abu-Remaileh 48; Steinberg 91; Obeid manifest updated), direct antecedents deduped, and existing ledger claims audited against the new panels/tables. | strong | No new load-bearing unread premise introduced. |

## Persistence diagnosis

- **Durable ledger/registry IDs and wikilinks:** `DL-MECH-095`, `DL-MECH-098`, prior Obeid discovery lineage; receipt ledger entries for all three.
- **Reading queue/debt:** only PMID 34268881 retains debt, precisely Appendix Figures S1–S6. Its receipt and manifest state the missing surface; it was not mislabeled complete.
- **Dossiers and commit candidates:** `PMID25012504.md`, `PMID34268881.md`; `CC-20260814-42422765-01`, `CC-20260814-25012504-01`, `CC-20260814-34268881-01`.
- **Receipt source fingerprint, coverage and supplement state:** all receipts point to fingerprinted local full-text surfaces. Obeid and Abu-Remaileh are complete; Steinberg has every required main coverage slot read and supplementary marked unavailable because the cited Appendix figures are missing.
- **Future mechanical distinction:** `fulltext_receipts.py status --pmid` returns timestamp, fingerprint, per-section coverage, supplement state, prior receipt and reread reason; strict manifests resolve every locator to a fingerprinted artifact.

## Process and capability diagnosis

- **Skills/gates/patterns used:** LEGEND autopilot/deep-dive discipline, PDF render-and-inspect, Documents fallback for DOC/DOCX, Presentations for the legacy PPT, Spreadsheets for all XLSX rows, exact locator validator, receipt chain and publication gates.
- **Plausible skills deliberately declined:** image generation was irrelevant to evidence inspection; local PaperQA/RAG was not allowed to replace sequential source reading; browser automation was unnecessary after official package retrieval and direct publisher fallback both failed to expose the missing Appendix figures.
- **Failures/retries/extraction mismatches:** PMC proof-of-work initially accepted only PDFs and some requests returned 429/interstitials; the DOCX renderer lacked `pdf2image`; Poppler CLIs were absent; the first Steinberg manifest failed on exact punctuation and coupled-locator pointers; publisher fallback returned an HTML challenge; Appendix figures remained absent. New receipts also drifted three generated views/ratchets, which were regenerated and tightened. The full release runner exposed the unrelated nested-worktree and ignored-settings failures described above.
- **What caught each failure:** binary magic/MIME validation and retries; LibreOffice + PyMuPDF rendering; strict locator validation; explicit source-package inventory. No failure was converted into scientific absence or a complete receipt.
- **Disease-agnostic micro-upgrade shipped:** `pmc_pow_fetch.py` now validates PDF, legacy/current Office, XLSX, JPEG and PNG supplements by both declared MIME and file magic, while refusing HTML interstitials even under a binary MIME.
- **Regression/evidence:** six unit tests include legacy Office, XLSX, JPEG/PNG and hostile HTML cases.
- **Residual risk and next decisive action:** obtain Appendix Figures S1–S6 from the authors/editorial archive; then inspect them, append a new receipt and only then close PMID 34268881. At the next authorized BATCH_COMMIT, apply the three queued candidates atomically.
