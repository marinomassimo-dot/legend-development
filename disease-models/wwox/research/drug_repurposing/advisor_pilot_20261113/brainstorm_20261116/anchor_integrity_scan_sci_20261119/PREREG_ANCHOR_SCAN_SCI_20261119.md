# Pre-registration: anchor-integrity scan of the canonical claims (SCI, 2026-11-19; method frozen before any claim-level count)

Non-canonical working note. Hypothesis level; no dose; not medical advice. Reading and counting only: nothing in any registry, card, need, arm table or candidate is edited or applied. Written under ADV's assignment OBJ_ACCEPTED[31] of mandate ORCH-SCI-ADV065-DEEPEN-20261118. This file is hashed (SHA256SUMS_ANCHOR_SCAN_SCI_20261119.txt) before the analysis script is written; every later change is a dated section, not an edit.

## 0. What was looked at before this freeze (stated so the freeze is honest)
* `registry_records.py catalog --source claim_registry_current --column Status`: 47 claims, with their status. No claim-level count of anchors, depths or consumers had been produced.
* A `git grep -c` of claim-id strings over `drug_repurposing/` showed which FILES mention claim ids (the top ones are `join/queries.json`, the two arm-cell tables, `join/evidence.json`, `join/cards.json`, `needs/needs.json`, `cards/` and `cards_early/`). That told me where consumers live, not which claim is consumed most.
* `trace_claim_foundation.py` (via its `Foundation` class) was read for how it builds anchors. **Pre-freeze finding that shapes the method:** its `papers` universe holds only `PAPER` records (559 of them), and its claim-to-paper edges are `claim_links` and `source_field` (evidential) and `wikilink_only` (not). A claim anchored to a `CORPUS P###` placeholder (for example CLAIM 028, whose Source field names corpus 207, 218, 206, 214) is therefore SHOWN WITHOUT its placeholder anchors. A scan that used the tool alone would miss exactly the placeholder category ADV asked about. The method below adds the CORPUS anchors from the claim's own text.

## 1. Question
For each canonical claim: which records anchor it, and at what attested reading depth; which claims rest only on placeholders, abstract-level or partial readings while their wording is stronger; ranked by how many cards, needs or arm cells consume the claim. First slice: the 20 most consumed claims. Side question ADV named: is the CLAIM 025 case (a statement anchored to a placeholder or to a partial reading, with wording stronger than the paper) isolated?

## 2. Universe
The 47 records of `claim_registry_current.md`, enumerated with the `Foundation` splitter AND cross-checked against the count of `registry_records.py catalog` (47). (A suite that shares a tool's splitter cannot verify that tool; the catalog is the second route for the count only.)

## 3. Anchors (three classes, kept apart)
* **A1, PAPER anchors:** a `PAPER nnn` record that (a) lists the claim in its own `Claim links`, or (b) carries a PMID named in the claim's `Source` field. These are the tool's evidential edges.
* **A2, placeholder anchors:** a `CORPUS P###` record named in the claim's `Source` or `Wikilinks` field (regex `CORPUS P\d+`), or whose own `Claim links` field names the claim. Also counted as a placeholder: any anchor whose Identifier is `PENDING` or carries no PMID and no DOI.
* **A3, cross-references:** a `PAPER nnn` that appears only in the claim's `Wikilinks`. Listed, never counted as an anchor (the tool's own rule, `wikilink_only`).

## 4. Depth (attested versus declared, never merged)
* **Attested depth** = the deepest surviving receipt for the anchor's OWN study (`study_id.pmid` or `study_id.doi` in the receipt ledger, through `fulltext_receipts.receipt_depth_index`; a PMID that merely appears inside another receipt does not count). Levels, strongest first: `complete_strict` (receipt `complete_fulltext_read` and `coverage.results` = read and each of abstract, introduction, methods, discussion is `read` or `not_present`); `complete_loose` (receipt complete, strict test failed); `partial`; `abstract_only`; `not_read` (`queried_not_full_read`, `retrieved_not_read`); `none` (no receipt); `placeholder` (class A2 or no identifier).
* **Declared depth** = `coverage_report.classify_depth` on the registry entry (what the registry says about itself). A mismatch where the declared depth is `full_text` and the attested level is below `complete_*` is flagged `DECLARED_NOT_ATTESTED`.
* Cross-check: the PMID in the receipt's event id (`FTR-<date>-<PMID>-<NN>`) must equal `study_id.pmid`; disagreements are listed.

## 5. Consumption (distinct units that name the claim id; regex `CLAIM 0nn`)
* **needs:** distinct need ids in `needs/needs.json` whose record text names the claim.
* **cards:** distinct cards: `cards/*.card.json` and `cards_early/*.card.json` by file stem, and `join/cards.json` by card id. Not counted as separate cards: `*.packet.json` (the same card), `cards_early_it13_p22_20261031/regenerated/` (a regeneration).
* **arm cells:** rows of `matrix_v2_cells_sci_20261116/output/cells_v2_form.tsv` (the current cell table, 469 rows) in any field. The older `aed_matrix_sci_20261116/output/*.tsv` tables are not counted (superseded; double counting).
* **context, not in the key:** distinct query ids in `join/queries.json` that name the claim (mechanically derived from the claims, so a claim with a lead always has some).
* **Rank key** = needs + cards + arm cells; ties by claim number. The first slice is the top 20 with key > 0. All 47 are written to the TSV.

## 6. Screens (flags; they do not test the claim's wording against the paper)
* **F1 THIN:** no A1 anchor at `complete_strict`.
* **F2 PLACEHOLDER:** at least one A2 anchor; **F2a PLACEHOLDER_ONLY:** every anchor is A2 or `none`.
* **F3 WORDING_VS_DEPTH:** status `consolidated baseline` with F1 = strong; status `in observation` with deepest anchor at `abstract_only` or lower (or no anchor) = medium; other statuses are not scored.
* **F4 DECLARED_NOT_ATTESTED** (section 4).
* **F5 SOURCE_PMID_UNANCHORED:** a PMID in the claim's `Source` field that no `PAPER` record carries.

## 7. What this scan cannot say, and the second layer
A flag says the anchor depth is thin; it does NOT say the claim overshoots its source. The CLAIM 025 overshoot was found only by reading the sentences of the Abstract, Results and Discussion against the proposition. So: a **second layer by reading** is applied to at most the five highest-ranked claims in the slice that carry F1 together with a strong or medium F3 (or F2a), and reported separately, each with the claim sentence, the anchor, the receipt's coverage and my reading, marked "read by SCI, not audited". Whether CLAIM 025's pattern is isolated is answered at two levels: (screen) how many slice claims share F1 with the 025 pattern F2 or partial-only anchors, and (reading) what the second layer finds in those five.

## 8. Verification
A seeded spot-check (seed 20261119) of 10 anchor rows from the output, redone by a SEPARATE script that does not import the three tool modules (raw ledger lines by event id; raw registry text by regex), reported with the match rate and with the byte origin each route shared. A blind delegate is used only if the spot-check disagrees or if ADV asks.

## 9. Not done here
No registry edit; no card, need or cell change; no new receipt; no reading of a supply-path paper (L); no grep of the two large registries (they are parsed by the tools' splitters, which read them whole into memory once).
