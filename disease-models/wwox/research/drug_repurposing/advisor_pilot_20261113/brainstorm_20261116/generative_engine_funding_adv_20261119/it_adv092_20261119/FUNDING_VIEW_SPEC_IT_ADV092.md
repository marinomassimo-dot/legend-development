# Ordinal funding view: specification, build state and the first map (IT, 2026-11-19, ADV-092 items 2 and 3)

Hypothesis level. Reference genotype class only. No dose, schedule or recommendation for any agent in any person. Not medical advice. No personal or individual-level information is used or recorded.

**Current scope, operator clarification of 2026-11-19.** This is a study-preparation diagnostic, not a scientific candidate ranking or funding decision. The legacy file and command names are retained for compatibility. Apply [Scientific selection before laboratory work](../../../../roadmap_current.md#scientific-selection-before-laboratory-work) and the [team continuation brief](../SCIENTIFIC_SELECTION_BRIEF_ADV_20261119.md). Costs are optional context, never an input required to select a candidate. Earlier sections below record the original implementation; their stronger funding claims, universal L1/L2-only assay limit and operator dependencies are superseded within this scope. The display now makes these limits explicit. No research order or scientific source row is changed by this correction.

**First line of the view: funding order is not research order.** The view orders nothing by cost, probability or score.

## 1. What was built (small, read-only, tested)
| Piece | File | State |
|---|---|---|
| The view generator | `framework/scripts/funding_view.py` (`run`, `check`) | built; one self-contained HTML, no script, English; refuses a malformed input instead of repairing it |
| Its tests | `framework/scripts/test_funding_view.py` (10 tests) | green; includes "cost changes no ordering", "bad cost row refused", "the committed preview is current", "no write path to the cost file" |
| The map (item 3) | `opportunities.tsv` (10 rows) | first pass; classes are the row author's reading of cited sources, not a re-audit |
| The operator's cost input | `cost_ranges.tsv` (columns item, low, high, currency, source, date) | **header only**, default `not supplied`; no agent writes a row |
| The rendered preview | `FUNDING_VIEW_PREVIEW_IT_ADV092.html` | generated; `funding_view.py check` exits 1 when stale |
| The dossier template | `DECISION_DOSSIER_TEMPLATE_IT_ADV092.md` | item 1 (with SCI's outcome-to-decision table and interpretable-null control; the "would we do anything different" check for every candidate whose item 3 names no decision) |

## 2. The rules the view keeps (each is a test or a refusal)
1. **Components stay separate columns** (L1 target engaged, L2 direction, L3 phenotype relevance, L4 transfer to variant and age), each with an evidence class; never summed.
2. **Unknown is printed as unknown** and is the lowest class. The classes, low to high: unknown, ESPANSIONE, IPOTESI, INFERENZA, DATO-adjacent (another system or stage, or abstract level), DATO-matching (the system the study would use). The weakest link is the lowest class, ties all marked; `n/a` is for an assay that is not a candidate.
3. **Sensitivity strip: three declared orderings, lexicographic (key tuples), not weighted sums**; equal keys share a rank; the range of ranks is shown. A: decision named, null control, weakest link resolved, assay sharing. B: weakest link resolved first. C: assay sharing first. The keys contain no benefit, safety or cost, so rank 1 is not a verdict.
4. **Information value only as a sensitivity**: a fourth table appears only when at least two candidates carry a dossier count of outcome rows that change a decision (`rows_that_change_decision`); today it prints "not available: 0 of 10".
5. **Shares an assay** is a flag per candidate and a table; **PAIR table**: every ambitious and conservative pair, listed by id, never ordered.
6. **Cost** is read only from `cost_ranges.tsv`, shown as its own column and a flag ("supplied / not supplied"), a pair cost only when both ranges are supplied in one currency; never a sort key (a test changes the cost and asserts all rankings equal), never inside any ordering. The view reads no ranking: `next_priority` stays cost-blind and its digest (ff38fcaa61295a5a) is untouched.

## 3. Decision taken: not a tab of `repurposing_view.py` yet (DEFAULTS_TAKEN)
The request said "as a tab beside the others"; the view is a standalone page instead. **Why:** the public page is built from shareable sources only, in five languages with a committed translation inventory and a shareable audit that proves no non-allowlisted value is in its bytes; a new section needs translated strings in all five and an allowlist entry for every cell, and its content (readiness of candidates, and operator costs once supplied) is not content the operator has decided to publish. **What would be different:** embedding is a bounded follow-up once the operator says the view may appear on the public page (and which fields): the renderer's tables are plain `data-table` blocks and move without change. **Revert:** none needed; nothing in the public build changed. This is reserved to no one but is the operator's to overrule.

## 4. First map: what the 10 rows show (read with the table; not a ranking)
| Observation | Rows |
|---|---|
| The study resolves the weakest link | OPP-01, 04, 05, 06 |
| The study does NOT resolve the weakest link (it stays open after the best outcome) | OPP-02 (L4 then L3), OPP-03 (L3) |
| Weakest link or decision cannot be stated from what was read | OPP-08, 09, 10 (partial or card-only reading); OPP-07 is an assay (`n/a`) |
| **No decision named** (fails the dossier's item 3: goes to the person who can say "we would not do anything different") | OPP-08 ketogenic card, OPP-09 rescue window, OPP-10 clinical series |
| Shared preparations | SLICE-PREP: OPP-01, 02, 05; PUP-SERIES: OPP-03, 04, 06, 08, 09; SLICE-ANIMAL-TISSUE: OPP-07; CLINICAL-SERIES: OPP-10 |
| Not on the ordering page | OPP-05 (Kv7, IT46 P4 audit) and OPP-09 (rescue window); the page's measurement rows 1, 8, 9, 10, 11, 12, 14 are not mapped as candidates (they are measurements or constraints; row 11 is the prerequisite of row 6 of the map's OPP-06) |

**Three flags for ADV and SCI (kept side by side, not resolved here):**
1. *Shared assay and ethosuximide.* ADV-091 and the brainstorm reply say the matched-block slice preparation serves "ethosuximide with the wild-type age series"; the ordering page puts ethosuximide in the in vivo pup series (row 3, stage 2), and the slice package S2 lists no ethosuximide slice arm. The map therefore tags OPP-03 to PUP-SERIES and OPP-05 (Kv7, an R5a slice design in the IT46 audit) to SLICE-PREP. If a slice ethosuximide arm is meant, it is an addition to S2, not a shared existing arm.
2. *"Paediatric safety already known" for the conservative cluster* (meeting record) against the held labels: ethosuximide not established below 3 years (INV-04 D11), lithium from age 7 (INV-09 D05). The map places lithium (OPP-04) with the ambitious cluster, following the record's own list; IT's first reply had it conservative. SCI to reconcile the sentence.
3. *OPP-09 and OPP-08 and OPP-10 are thinly read* (read_state says so per row); they are in the table so the Foundation sees that the readiness question is open for them, not because they are ready.

**Named, not mapped (no chain could be written from what was read):** the isolated NMDAR current under voltage control (CLAIM 021 F06; card F04 step E1); the myelin-promoting arm (needs the conduction re-measurement first: ordering rows 8 and 9); heterozygote carrier latency (row 10, one source).

## 5. How a dossier feeds the view
A dossier (template) becomes one row: its field 1 gives L1 to L4 with classes; field 3's outcome table gives `decision_named`, `decision_text`, `null_control` and `rows_that_change_decision`; field 6 gives `assay_id`; field 7 gives `blind_check`. SCI's pilot dossier on the slice panel (ADV-091) should replace the rows of OPP-01, 02 and 05 when it lands; until then those rows are the map's reading.

## 6. Reserved to the operator (unchanged)
The cost ranges per type of study (from the laboratories' own quotes), the choice of any laboratory or clinical channel, the human supply of the clinical series, whether the view appears on the public page, and the final choice of what to fund.

## 7. Dated line 2026-11-19 (after ADV accepted ADV-092 and resolved the three flags)
ADV: ethosuximide belongs to the PUP series, not the slice preparation (the earlier wording was the error; the map already tags it so); "paediatric safety already known" is overstated, so lithium stays ambitious and **safety gets its own cell per agent and age**; the dossier names the "would we do anything different" reader, the operator for the first cases. Applied: template field `check_reader` and field 2b (safety cell); `opportunities.tsv` column `safety_cell` (filled for OPP-03 and OPP-04 from the held label rows, `unknown` elsewhere); the view prints it as its own column and no ordering reads it.

## 8. Dated line 2026-11-19 (SCI's pilot dossier applied)
SCI's ADV-091 pilot dossier rows replace OPP-01, OPP-02 and OPP-05 in `opportunities.tsv` (source: `adv091_pilot_dossier_hindcast_sci_20261119/dossier_rows_for_opportunities_adv091.tsv`): null control named for OPP-01 and OPP-02, `rows_that_change_decision` = 2 for each, so the information-value sensitivity table now appears (3 of 10 rows carry a value; it is a sensitivity, not an ordering of merit). The `safety_cell` column, which SCI's layout does not carry, is kept from this file (unknown for these three). OPP-10's chain note now points to SCI's cluster-2 note for the safety wording. The dossier itself says it is not ready for L2 in the template's sense (a cheaper route is untried: the per-slice data and supplement of the preparation paper are not held). A blind check of its fields 1 to 3 is ADV-094 item 1.

## 9. Dated line 2026-11-19 (after ADV-094, ADV's decision)
The view now says, in a second boxed line under the first, that the case for funding a study rests on its dossier (the decisive uncertainty and the outcome-to-decision table), not on any score or on the sensitivity orderings, because a blind hindcast of the four components showed no separation of known successes from known failures in a contaminated run (`adv094_it_20261119/ADV094_RESULT_IT_20261119.md`). ADV closed the hindcast as a diagnostic with that result; no re-freeze.

## 10. Dated line 2026-11-19 (correction of section 4 and of the view's column, found while reading ADV's draft proposal)
The column "Study resolves the weakest link(s)?" printed "yes" when the study resolves at least ONE of the tied weakest links. Section 4 of this spec ("The study resolves the weakest link: OPP-01, 04, 05, 06") therefore said more than the map supports. The view now prints yes only when the study resolves ALL tied weakest links, "partly" when it resolves some: **yes** OPP-01 (E_GABA); **partly** OPP-04 (lithium: L1 resolved, L4 open), OPP-05 (Kv7: L2 resolved, L3 and L4 open and tied lowest), OPP-06 (glucose timing: L3 resolved, L4 open); **no** OPP-02 (L4, then L3) and OPP-03 (L3); unknown for OPP-08, 09, 10; n/a for OPP-07. The earlier text of section 4 is not edited.
