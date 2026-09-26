# Session self-evaluation — `scientist-a` · `SCI-FT-A-001` · 2026-09-14

> Completed after the analysis and before takeaways. Public, disease-level, de-identified.

## Scope and executable verdict

- **Batch:** two papers, the never-dispatched lot of `SCIENCE-EXEC-20260914` step `OBJ_1_readings[0] R1` — PMID 31275852 (McBride 2019) and PMID 41090157 (Hussain 2025).
- **Receipts:** `FTR-20260914-31275852-01` and `FTR-20260914-41090157-01`, both `complete_fulltext_read`, both **written and NOT appended** by instruction; each passes `validate_receipt`, `validate_new_receipt` and `_strict_local_source` in-process.
- **Manifests:** both **strict PASS, 0 gaps** — 33 locators (25 body, 1 table, 7 figure) / 19 artefacts and 38 locators (27 body, 11 figure) / 31 artefacts, `--verify-artifacts --require-current-schema`. Counted from the files after writing them: my first prose draft said 34 and 29, which the files did not bear out.
- **Structural LINT:** `WARN` (one grandfathered LIT status, three INFO lines), baseline captured **before** any of my writes and unchanged by them.
- **`session_self_eval.py`:** `PASS` — every complete read has landed and every declared output resolves. Two standing `[RATCHET]` lines and the declared gaps it prints belong to other papers, none to these two.
- **Dependency screens:** `SCREENED_CLEAN` for both (59/61 and 70/74 screened; 0 flagged).

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full text, figures, tables, supplements | Every section of both papers in order. P1: 6 figures as native PDF rasters (up to 3551×1093) + 3 native-scale crops; 3 supplements as pixels; Table 1 as text. P2: 7 figures + visual abstract, Figures 5 and 6A re-rendered at 400 dpi from vector; all 15 supplement pages; both workbooks parsed row by row (213 CNV segments, 87 + 2355 DE rows). | strong | — |
| Main message and original contribution | P1: repair-pathway **choice** shifts without increased lesion load — an endpoint absent from this corpus (`microhomology` in 1 of 98 manifests, `class switch` in 0). P2: instability confined to tumours, with the AID mechanism failing its own test. | strong | — |
| Hidden gold beyond keywords/abstract | Nine findings exist only in pixels or deposited data: the 2.5-fold/6.5-fold mismatch, the "76 vs 77" caption error, the undeclared AID⁻/⁻ arm, the withheld p = 0.15, the PBP/PBL caption inversion, SBS85 absent from the hypermutated tumours, 31/87 immunoglobulin genes, *Wwox* down only 1.61 log₂, and Figure 7B's caption against its own segment counts. | strong | — |
| Source parity | Two B-cell oncology papers read at full depth for a CNS disease model; the most transferable datum turned out to be a negative-control lane (cerebellum Wwox-replete) and a gene-dose observation in heterozygotes the authors never analysed. | strong | — |
| Team type, field density, observation vs interpretation | Aldaz lab: primary for the gene (38/138) **and** publishes on the disease, while this output touches neither; the B-cell methods are McBride's (1 of 53 papers on WWOX) and the myeloma model is Chesi's under a declared royalty interest. Both recorded separately, as the validator requires. WWOX∩CSR = 1 paper in PubMed. | strong | — |
| DATO / INFERENZA / IPOTESI separation | Applied per proposition: "direct role" → INFERENZA; "Alt-NHEJ engagement" → author inference from a signature; B-cell intrinsicality → not established by the design; inflammation → IPA inference with no protein measured. | strong | — |
| Existing claims touched; conflicts/revival triggers | `CLAIM 029` only: one sentence proposed per paper, nothing retracted, **ATM leg untouched** (neither paper measures ATM). Refused to touch `CLAIM 006`/`CLAIM 025` with murine B-lineage inflammation data. Negatives carry premises and revival triggers in the dossiers. | strong | — |
| Multi-hop and corpus cross-query | 61 and 74 references enumerated from the fingerprinted ref-lists; 16 and 22 gene-direct; 15/16 and 22/22 present by identity; **10861292 absent from all of canon**. Reading depth stated per antecedent rather than assumed: `25331887` — `CLAIM 029`'s own primary — has **no complete receipt**. | strong | Debt routed in both candidates, not queued (this contract does not own the queue) |

## Persistence diagnosis

- **Durable IDs:** two manifests, two dossiers, two commit candidates, two receipt files, this evaluation, and `ledger/tasks/scientist-a/SCI-FT-A-001.json`.
- **Coverage honesty:** `figures: read` and `supplementary: read` are literal — images were opened, never captions trusted. `tables: read` for P1 (one real `<table-wrap>`), `tables: not_present` for P2 (zero), `limitations: not_present` for both.
- **Can a future run distinguish full text from abstract only?** Yes: 71 locators across body, table and figure surfaces, each bound to a fingerprinted artefact, plus acquisition recipes that name the route actually used — including the routes that **failed**.

## Process and capability diagnosis

- **Acquisition was adversarial and is recorded as measured, not as assumed.** Europe PMC `fullTextXML` returned **HTTP 503** for both PMCIDs, contradicting the dispatch brief's own measurement from earlier today; PMC `/bin/` served an NCBI 404 page for one paper and a **reCAPTCHA interstitial under HTTP 200** for the other; `ars.els-cdn.com` refused every path with HTTP 400 and ScienceDirect with 403. Recovery came from `efetch`, the publisher PDF, the **PMC Open Access S3 bucket** and the Europe PMC `supplementaryFiles` zip. A downloader that trusted status codes would have declared eleven figures "read" over 21 kB of HTML each.
- **Three failures I caught before they became claims:**
  1. **My snippet checker reported the opposite of the truth.** It said every quote failed and Methods sentences were "in the abstract" — I had mis-ordered `_xml_surfaces`'s two return values. Had I reported that verdict, I would have declared 22 sound locators broken. Fixed to identify the body surface empirically, then 21/22 passed (the 22nd was my own "Naive" for the paper's "Naïve").
  2. **A near-miss contradiction against paper 2.** On the deposited 642-px oncoplot I read *no* mutated knockout-marrow column and was about to record a contradiction of the text's "1 Wwox KO-BM". Re-rendering the PDF's vector artwork at 400 dpi showed *Kmt2c* in the last knockout column — **the text was right and my surface was too coarse.** The finding that survives is about resolution, not about the paper.
  3. **I mis-measured the corpus and corrected it in the manifests.** `wc -l` and `grep -c` gave "173 events / 121 complete"; the event-level truth is **175 events, 104 complete over 87 PMIDs**. Both `corpus_crossquery` fields now state the measured numbers and why the first pass was discarded.
- **What the parallel-reader constraint cost and preserved:** nothing was appended to the receipt ledger, so both readings are complete but **not yet persisted** — the honest state is `ANALYSIS_DONE_RECEIPT_NOT_PERSISTED` until the orchestrator appends. Reported rather than worked around.
- **Residual risk:** the 6.5-fold reading of Figure 6C is a densitometric judgement on printed bar heights; it is recorded as an attestation with the axis ticks described and as an **unresolved ambiguity**, never as a corrected fold change.
- **Next decisive action:** read **25331887**. A consolidated-adjacent claim whose own primary source has never been read is a worse gap than either paper I just read.

## Micro-upgrade shipped

**Finding, disease-agnostic:** the repository has a ratchet for *registry declarations with no receipt behind them* (`UNBACKED_FULLTEXT_DECLARATION`) and one for *manifests missing a dependency screen*. It has **none for a claim whose cited primary source has no complete receipt**. `CLAIM 029` is the live instance: `Source: PMID 25331887`, `Wikilinks: PAPER 030`, and `fulltext_receipts.py status --pmid 25331887` exits non-zero. The measurable form, stated so it is not lost: *for every claim in `claim_registry_current.md`, resolve the PMIDs named in `Source`/`Wikilinks` and count those with no active complete receipt.* On today's state that query returns at least one claim, and it is a claim two of my locators now bear on. Recorded in both commit candidates as a flag for the orchestrator rather than implemented here, because the counter would live in `growth_anchors.py`, which this contract does not own.
