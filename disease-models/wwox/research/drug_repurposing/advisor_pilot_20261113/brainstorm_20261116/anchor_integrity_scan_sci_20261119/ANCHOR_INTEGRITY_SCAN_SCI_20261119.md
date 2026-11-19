# Anchor-integrity scan of the canonical claims: first slice of 20 consumed claims (SCI, 2026-11-19)

Non-canonical working note. Hypothesis level; no dose, schedule or recommendation for any agent in any person; not medical advice. Counting and reading only: no registry, card, need, arm table, candidate or receipt was edited or applied. ADV's assignment OBJ_ACCEPTED[31] of mandate ORCH-SCI-ADV065-DEEPEN-20261118. Method frozen before the first count in `PREREG_ANCHOR_SCAN_SCI_20261119.md` (sha256 in `SHA256SUMS_ANCHOR_SCAN_SCI_20261119.txt`); every change after the first run is a dated, post hoc amendment in `AMENDMENTS_ANCHOR_SCAN_SCI_20261119.md` (nine of them; the pre-registration file itself is not edited). Read at `origin/main` `357331aac` (merged into the task branch).

## 1. Answer first
1. **The CLAIM 025 pattern (a statement anchored to a placeholder record) is isolated among the consumed claims, not across the registry.** Of the 20 most consumed claims only CLAIM 025 has a CORPUS placeholder anchor. The same pattern sits in CLAIM 022, 024, 027 and 028, none of which a need, card or cell consumes except CLAIM 028 (one card). All 47 claims were scanned (the slice is the first 20 by consumption; 26 of the 47 are consumed at all).
2. **By reading depth, the slice is mostly sound; the only thin reading in it is CLAIM 001's safety anchor.** 10 of the 20 carry at least one anchor labelled below complete (F6), but the `partial` label mostly does not mean a thin reading: of 46 `partial` anchor rows in the whole registry, 42 have Results read in at least one surviving receipt (the 4 that do not are CLAIM 028 twice and CLAIM 043 and 044 through PAPER 141). In the slice, the one anchor thin in substance is Choi 2026 (PAPER 003, PMID 41442931), the vigabatrin MRI safety anchor of CLAIM 001 (`conflicting evidence`, 8 consumers): abstract only (`FTR-20261105-41442931-21`, every other section `unavailable`). The claim's own text says "abstract level, no denominator", so its wording matches its depth.
3. **A depth screen cannot see the 025 overshoot.** That overshoot was a wording problem found by reading sentences against the paper (ADV-081); a claim with all anchors complete can overshoot, and a claim with a partial anchor can be exactly worded. Section 5 therefore ranks AUDIT candidates by consumption and anchor weakness, and says which need a sentence-level reading.
4. **A tool defect surfaced and changes the numbers:** `trace_claim_foundation.py` (and so every consumer of its `claim_links` edge) counts a paper whose `Claim links` field says "none — … CLAIM 003 is untouched" as a link to CLAIM 003. 14 PAPER records, 21 false evidential edges, 14 claims affected (section 4). Not applied; for HE.
5. **Concentration, not depth, is the largest exposure:** 8 of the 20 slice claims rest on a single anchor; CLAIM 021 (138 consumers, of which 132 arm cells) rests on Breton 2021 alone, a `complete_strict` reading (one reading receipt, `FTR-20261019-34634460-01`). If that paper's reading is wrong, 132 cells move together.

## 2. What was counted, in one paragraph
Universe: the 47 claim records (cross-checked against `registry_records.py catalog`). Anchors: A1 = the paper's own `Claim links` affirming the claim, or a PMID in the claim's `Source`; A2 = a CORPUS record named in the claim's Source or Wikilinks (the tool omits these entirely; found before the freeze); A3 = wikilink only (shown, never counted); A4 = a `Claim links` field that names the claim only to refuse the link (shown, never counted). Depth: the deepest surviving receipt of the anchor's OWN study (`study_id`, not a PMID substring), `complete_strict` requiring Results read and abstract, introduction, methods, discussion each read or not present; plus the union of sections read across all surviving receipts of the study. Consumption: distinct needs (24 in `needs.json`), cards (`cards/`, `cards_early/`, and the 28 derived join cards) and arm cells (469 rows of `cells_v2_form.tsv`) whose structured fields name the claim: needs through `sources`, `counter_evidence`, `observed`, `inferred`; cards through `input`; cells through `source_locator`. Rank key = needs + cards + cells.

## 3. The slice (rank, consumers, anchors, flags)
Flags: **F1** no A1 anchor at `complete_strict`; **F2** a CORPUS record anchors the claim; **F6** an effective anchor below `complete_loose`; **F8** a partial or abstract anchor with no Results read in any receipt; none of the 20 has F4 (declared full text, attested below) or F7 (wikilink-only anchoring).

| Rank | Claim | Status | Needs / cards / cells | Anchors (A1+A2): strict / loose / partial / other | Flags |
|---|---|---|---|---|---|
| 1 | 021 | consolidated | 2 / 4 / 132 | 1 / 0 / 0 / 0 (+1 duplicate CORPUS record of the same study) | single anchor |
| 2 | 002 | consolidated | 1 / 4 / 22 | 1 / 0 / 1 / 1 (preprint, superseded) | F6 |
| 3 | 005 | consolidated | 2 / 1 / 22 | 4 / 0 / 2 / 0 | F6 |
| 4 | 031 | in observation | 2 / 16 / 0 | 3 / 0 / 0 / 0 | |
| 5 | 011 | flagged for review | 3 / 13 / 0 | 1 / 0 / 0 / 0 | single anchor |
| 6 | 019 | consolidated | 2 / 10 / 0 | 3 / 0 / 1 / 0 | F6 |
| 7 | 046 | in observation | 0 / 10 / 0 | 1 / 0 / 0 / 0 | single anchor |
| 8 | 001 | conflicting evidence | 3 / 5 / 0 | 4 / 0 / 4 / 1 (abstract only) | F6, F8 |
| 9 | 016 | in observation | 2 / 4 / 0 | 2 / 0 / 0 / 0 | |
| 10 | 036 | in observation | 4 / 2 / 0 | 4 / 0 / 0 / 0 | |
| 11 | 003 | consolidated | 2 / 3 / 0 | 0 / 0 / 1 / 0 | F1, F6, wording strong |
| 12 | 004 | consolidated | 2 / 3 / 0 | 1 / 0 / 0 / 0 | single anchor |
| 13 | 030 | in observation | 1 / 4 / 0 | 4 / 1 / 1 / 0 | F6 |
| 14 | 035 | in observation | 1 / 4 / 0 | 1 / 0 / 0 / 0 | single anchor |
| 15 | 042 | in observation | 1 / 4 / 0 | 0 / 1 / 2 / 0 | F1, F6 |
| 16 | 025 | in observation | 0 / 4 / 0 | 2 / 0 / 2 / 1 (placeholder) | F2, F6 |
| 17 | 032 | in observation | 1 / 2 / 0 | 16 / 0 / 5 / 0 | F6 |
| 18 | 040 | in observation | 0 / 3 / 0 | 1 / 0 / 0 / 0 | single anchor |
| 19 | 006 | consolidated | 1 / 1 / 0 | 1 / 0 / 0 / 0 | single anchor |
| 20 | 009 | in observation | 2 / 0 / 0 | 5 / 2 / 4 / 1 (no identifier) | F6 |

Ranks 19 to 21 tie at 2 (CLAIM 014 is rank 21). Full 47-row table: `claims_ranked_scan_sci_20261119.tsv`; one row per anchor (164 A1/A2 rows, 20 A3, 21 A4): `anchors_by_claim_scan_sci_20261119.tsv`; the numbers quoted here: `SCAN_SUMMARY_NUMBERS_SCI_20261119.txt`.

## 4. The tool defect (negated links)
`Foundation.supporting_papers` finds claim numbers with `\b(\d{3})\b` anywhere in a paper's `Claim links` field. Fourteen PAPER records have a field that starts with "none" and names claims to refuse them: PAPER 082 and 083 ("deliberately none … CLAIM 002 and CLAIM 004 must NOT be linked"), 112, 122, 125, 126, 127, 129, 130, 132, 171, 176, 189, 289. Naive reading: 167 edges; strict reading (field not starting "none", backticks, parentheses and text after a spaced dash ignored): 146; in every other field the two agree. The 21 false edges (13 `complete_strict`, 7 `partial`, 1 `complete_loose`) sit on 14 claims. Effect on this scan: CLAIM 003 looked like three anchors with a complete one and was ONE (PAPER 004, partial); CLAIM 002 looked like three complete anchors and has one (`complete_strict`) plus a partial and a superseded preprint; CLAIM 011 lost one anchor. The same defect type exists in CORPUS records, which the tool does not read: CORPUS P261 and P268 say "none — the reading adds … and creates no link", and my first A2 builder counted them as two anchors of CLAIM 036 (now four anchors, all A1). Any other consumer of the tool's `evidential` edges (the `support_linkage.py` script has the same input) inherits the error. Proposed fix for HE, not applied: refuse a `Claim links` field that begins "none".

## 5. Second layer by reading: the four consolidated-baseline claims with a weak anchor, and the audit candidates
Rule (amendment 3): consolidated baseline, in the slice, with F6, by consumption: CLAIM 002, 005, 019, 003 (CLAIM 021 left the set when its CORPUS record proved to duplicate the complete PAPER 031). Read by SCI at the level of "does the claim's sentence depend on the weak anchor, and what do the study's receipts cover"; **not** an audit of the wording against the papers.

| Claim | Weak anchor and what its receipts cover | The claim's dependence | Reading |
|---|---|---|---|
| 002 (rank 2, 27 consumers) | PAPER 039 Steinberg 2021 (PMID 34268881): `partial`, 14 receipts, union = every section including the supplement (one receipt `…-07` read all; partial only because Appendix Figures S1 to S6 are absent). PAPER 001: the 2024 preprint, no identifier, Status `superseded` by PAPER 094 (`complete_fulltext_read`, `FTR-20260810-42397075-04`; its declared bytes are absent from every checkout, so that level is the receipt's attestation) | the organoid marker and firing-rate sentences; the E/I inference leans on Breton 2021 (PAPER 031, complete) | no depth finding; the claim's evidence boundary already scopes the rescue as marker-selective |
| 005 (rank 3, 25) | PAPER 004 (12 receipts; union Results, Discussion, supplement, tables) and PAPER 039 (as above) | headline anchor is Hussain 2019 (PAPER 006, complete); the NPY sentence rests on the PAPER 039 re-read `…-07` (all sections) with a blind locator audit named in the claim | no depth finding |
| 019 (rank 6, 12) | PAPER 025 Weisz-Hubshman 2019 (PMID 30853297): `partial`, 3 receipts, union abstract, introduction, methods, results, discussion, figures, tables; the registry DECLARES only "abstract" and the claim Source says "abstract-supported" | Q230P in severe compound context; PAPER 040 and 041 and 042 are complete | the registry understates the reading (declared below attested); no depth finding |
| 003 (rank 11, 5) | PAPER 004 Repudi 2021 *Brain* (PMID 33914858), the ONLY anchor: `partial`, 12 receipts; the index shows a methods-and-supplement receipt, but `…-03` and `…-01` read Results, Discussion, Introduction, figures and tables | "neuronal WWOX deletion induces non-cell-autonomous hypomyelination" | reading adequate for Results; the twin 2021 *EMBO Mol Med* paper (PAPER 005, complete) is named in the claim's evidence boundary but its own `Claim links` field says only "004": a declaration gap |

**Audit candidates, ranked (each needs a sentence-level reading, as ADV-081 did; none started):**
1. CLAIM 002, headline sentences against PAPER 039 Results and PAPER 094 (27 consumers incl. 22 cells; depth is clean, the wording was never audited).
2. CLAIM 005 NPY and PV sentences against PAPER 039 and PAPER 006 (25 consumers incl. 22 cells).
3. CLAIM 021 against Breton 2021 alone (138 consumers; a single-source concentration, its reading attested once).
4. CLAIM 001: obtain Choi 2026 full text (PMID 41442931) — the one substance-thin anchor in the slice; supply is the operator's, like the L list; I started no reading.
Also outside the slice: CLAIM 017 and CLAIM 020 (consolidated baseline, no consumer) are anchored by author-year `Source` text and wikilinks only; no paper record names them back (a declaration gap, not a reading gap: the wikilinked papers are complete for CLAIM 020, and for CLAIM 017 except PAPER 025, which is partial with Results read). CLAIM 018 (consolidated baseline, 1 consumer) has two `partial` anchors and no complete one.

## 6. Other counts
* Consolidated baseline: 18 claims; 10 consumed; 9 with F6; 5 with F1 (003, 017, 018, 020, 022); 2 wikilink-only (017, 020).
* Declared depth against attested depth, 164 anchor rows: equal 125, declared above attested 12, declared below attested 27 (registry text older than later receipts, the safe direction). `DECLARED_NOT_ATTESTED` (declared full text, attested partial): PAPER 014 (CLAIM 013) and PAPER 028 (CLAIM 028, with no Results read in any receipt); neither claim is in the slice.
* Anchor levels, 164 A1/A2 rows: `complete_strict` 101, `complete_loose` 4, `partial` 46, `abstract_only` 1, `none` 2, `placeholder` 7, `no_identifier` 3. Source PMIDs in a claim's `Source` field that no PAPER record carries (F5): none.
* Receipt ledger: 2,201 events; no event id disagrees with its own `study_id.pmid` among the anchors.

## 7. Verification and limits
* **Seeded spot-check** (seed 20261119, 10 of 164 A1/A2 rows) redone by `spotcheck_independent_sci_20261119.py`, which imports none of the three tool modules (raw registry text and raw ledger lines): 10 of 10 match on level and on link affirmation. The two routes share their byte origin (the same registry files and ledger); they differ in code only.
* **Consumption cross-check by raw grep and a separate JSON dump:** cells for CLAIM 021, 002, 005 = 132, 22, 22 (exact); CLAIM 031 cards = 12 files + 4 join cards = 16; CLAIM 011 = 11 + 2 = 13; needs for 036, 011, 031, 005 = 4, 3, 2, 2 (exact).
* No blind delegate was used (the pre-registration reserved one for a spot-check disagreement or ADV's request). No model run, no external call, no new receipt.
* **A "mention" in a structured field is the consumption proxy**; it does not say the card's conclusion depends on the claim. The join queries (one per claim) are context, not in the key. The older `aed_matrix` cell tables are not counted (superseded; double counting).
* The F-flags are label-based screens; F3 (wording against depth) uses the registry's status word, not the claim's sentences. The second layer covers four claims, depth only.
* Amendments 5 to 9 were made after seeing results (an A2 over-reach of my own script, negated links, partial-label union, superseded and promoted records, a PENDING string match); each is dated and states the numbers it moved. The first run (frozen method) is recorded in the amendments file with its numbers (171 A1 and 18 A2 anchors; CLAIM 017 and CLAIM 020 with zero anchors; CLAIM 021 with a placeholder); the script as shipped runs the amended method only.

## 8. Files
`PREREG_ANCHOR_SCAN_SCI_20261119.md`, `AMENDMENTS_ANCHOR_SCAN_SCI_20261119.md`, `anchor_integrity_scan_sci_20261119.py` (run `python3 -I <script> <repository root>`; writes the three TSV/JSON files and the log), `spotcheck_independent_sci_20261119.py`, `summarise_scan_sci_20261119.py`, `claims_ranked_scan_sci_20261119.tsv`, `anchors_by_claim_scan_sci_20261119.tsv`, `consumption_field_paths_scan_sci_20261119.tsv`, `scan_log_sci_20261119.json`, `SCAN_SUMMARY_NUMBERS_SCI_20261119.txt`, `SHA256SUMS_ANCHOR_SCAN_SCI_20261119.txt`.

## 9. What I propose (nothing applied)
* **HE:** treat a `Claim links` field that begins "none" as no link in `trace_claim_foundation.py` (and check `support_linkage.py`); the recipe row "anchor depth is the receipt of the anchor's own study, with union coverage, not the index receipt alone".
* **IT:** the 8 consolidated-baseline claims with no consumer and the 8 single-anchor slice claims as the next map items; the declaration gap of CLAIM 017, 020 and 003's twin paper is a registry-side change for the batch route.
* **ADV:** pick which audit candidate follows (section 5; I would take CLAIM 002 then CLAIM 005, because they carry 22 cells each and have never had a sentence-level audit), and whether Choi 2026 joins the L supply list. B (PV population, RP-019) stays next unless you say otherwise.
