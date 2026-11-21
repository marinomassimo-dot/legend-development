# ADV-147 pre-registration: WWOX transcript detection by lineage in human fetal cortex single-cell atlases (SCI window X, 2026-11-21; hypothesis level; no dose; reference genotype class only; donor data at class level only; not medical advice)

Assignment: ADV-147 (message from ADV 2026-11-21; the assignment file lands with ADV's next push). Question proposed by me in the ADV-146 close and registered by ADV with two edits (below).

## Disclosure: what I had already seen
`analysis/wwox_subfield_celltype_expression_20260922.md` (opened before this registration): in MOUSE ADULT, by a review of DropViz (Aldaz and Hussain 2020; second-hand), `Wwox` interneurons are at or above excitatory neurons (Pvalb-positive basket cells top in cerebellum; a Gad2 cluster top in hippocampus); its source block records that the Human Protein Atlas, Allen API, Hipposeq and GTEx per-cell routes were EGRESS_BLOCKED then, so human, fetal and inhibitory-lineage data were never reached. GTEx adult bulk (cerebellum 12.1, frontal cortex 6.9 TPM) and the Human Brain Transcriptome regional course are region-level only. `analysis/wwox_postnatal_svz_expression_20260922.md` D1 asks for the Nascimento 2023 postnatal object (not reached). `expression_timecourse_adv088_sci_20261119` covers marker timecourses in unaffected tissue, not WWOX by cell type. The Brain 2026 paper uses the Polioudakis 2019 atlas for annotation. **Nothing from any fetal atlas has been opened.** This step covers only what that note could not reach: human, fetal, MGE- and CGE-derived inhibitory lineage and progenitors.

## Question
In public human fetal cortex single-cell atlases, what fraction of cells in each lineage (progenitors and radial glia, intermediate progenitors, excitatory neurons by layer, MGE- and CGE-derived inhibitory lineage and interneurons, glia) has detectable WWOX transcript, compared with matched-abundance control genes?

## Binding scope limits (from ADV)
(a) Report "WWOX transcript detection in the lineage" and nothing stronger: expression in a lineage does not establish, and a lower detection fraction does not reject, a cell-autonomous function. (b) A result below half the excitatory detection after matching is a CONFLICT with the mouse adult map and with the AES 1.019 statement that inhibitory-neuron loss of Wwox is sufficient (a prediction check on a class-level, unverifiable sentence), not a rejection of a cell-autonomous function. (c) Access: plain clients and processed matrices only; a challenge, captcha, rate limit or egress block is a dated route result, never bypassed; absence needs two routes; report donor data at class level.

## Matched-abundance control (fixed now, before any value)
Pool of 20 genes of ordinary moderate expression: HPRT1, TBP, POLR2A, YWHAZ, PPIA, UBE2D3, CSNK2B, PSMB4, ARF1, TMEM59, SDHA, GUSB, TFRC, HMBS, PGK1, RAB7A, VCP, EEF2, NACA, SNRPD1. For each atlas, controls = pool members whose dataset-wide detection fraction is within plus or minus 25 percent (relative) of WWOX's. If fewer than 3 qualify, the atlas is reported as UNMATCHED and no zero or low detection in it is interpreted. Verdict compares WWOX's per-lineage detection fraction, as a ratio to the median of its matched controls in the same lineage, between inhibitory lineage and excitatory neurons.

## Routes (in this order; each outcome recorded as a dated route result)
1. CZ CELLxGENE Discover processed-summary API (gene by cell type by tissue; fetal brain datasets), plain HTTP client.
2. UCSC Cell Browser public datasets (cortex-dev, Nowakowski 2017; Polioudakis 2019 if listed), plain HTTP, cluster-level gene summaries.
3. Publisher or Europe PMC supplementary tables of the two papers (cluster marker tables) as a second route for absence claims only.

## Predictions (written before any access)
* P1 (70 percent): at least one processed route is reachable by a plain client and returns WWOX values per cell type.
* P2 (70 percent): WWOX is detected in MGE- or CGE-derived inhibitory lineage clusters, with a detection ratio against matched controls at least half that of excitatory neurons.
* P3 (50 percent): WWOX detection in radial glia and progenitors is at least equal to that in excitatory neurons.
* P4 (80 percent): per-cell detection is modest everywhere (no cluster above half of cells) so that any zero would be uninterpretable.
* P5 (60 percent): the matched-control step is feasible in at least one atlas (3 or more qualifying controls).

## Verdict rows (blind check on these)
V1 route reached (which, which not, dated). V2 inhibitory-lineage detection against excitatory (ratio with matched controls). V3 progenitors and radial glia against neurons. V4 consistency with the mouse adult map and what remains unreachable.

## Rules
MADE / VISUAL / NOT PRINTED / UNREADABLE for any printed figure; computed values stay labelled COMPUTED with their inputs; no third-party matrix is committed (digests and the query, not raw data); no individual-level information; blind recomputation of V2 by a different delegate from the saved query outputs only; close with a CHOICE (next verifiable question, rejecting observation, what unblocks).
