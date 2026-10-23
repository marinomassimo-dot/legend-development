# Proof on the real corpus — the join run on the three live axes, 2026-10-23

Deliverable E of `harness_mandate_20261022.md`, task `PLAN-DRUGREPURPOSING-MODULE-20261022`, actor
`plan`. A measurement of what the module (`framework/scripts/repurposing_join.py`) found on this
repository's own evidence against what the hand-made cards in `cards/` and `cards_early/` carry,
stated in both directions. Nothing here is a candidate, a dose or a recommendation; every external
source named is **NOT WWOX EVIDENCE** and carries its retrieval date. Not medical advice.

## 1 · What was run

| Command | Result (2026-10-23) |
|---|---|
| `repurposing_join.py run --axis proteostasis --live` | 26 queries · 7 abstentions · 3 derived cards |
| `repurposing_join.py run --axis calcium --live` | 16 queries · 5 abstentions · 2 derived cards |
| `repurposing_join.py run --axis wnt --live` | 23 queries · 9 abstentions · 5 derived cards |
| `repurposing_join.py run` (whole corpus, cache reused) | 332 queries · 59 abstentions · 26 derived cards · 1,180 paper rows (769 complete reads, 351 partial, 57 without a receipt, 3 abstract-only) |
| `repurposing_join.py handoff --date 2026-10-23 --write …` | 26 assignment rows: 21 SELECT · 3 REPLICATE · 2 AUDIT (`research/repurposing_batch_selection_20261023_module.md`) |
| adapter cache after the runs | 60 responses: PubTator 3 13 MATCH / 26 NO_MATCH; ChEMBL 10 MATCH; openFDA 2 MATCH / 8 NO_MATCH; Open Targets 1 MATCH; 0 QUERY_ERROR after the ChEMBL URL-encoding fix |

The queries are derived, never typed: 47 from the claim registry, 219 from the discovery ledger,
26 from the mechanism-intervention map (its R-01…R-09 repurposing records and N-01…N-17 negative
translations, which are the only place a candidate NAME is taken from), 40 from the pathograph
export's relational propositions bound to claims. The candidate universe of the module is therefore
exactly the map's.

## 2 · What the module found that the hand-made cards did not

1. **The depth of the evidence behind each candidate, measured.** A hand-made card cites its
   sources as file paths and section numbers; none of the 21 carries a PMID in a locator, so none
   says how deep the reading behind it goes. The derived card carries, per paper, the strongest
   standing receipt, the manifest's locator count (`len(entries)`), the `contradicts_locator`
   verdicts with their auditor count, and the adjudication files naming the paper. Memantine
   (`Q-R-02`) rests on five complete reads and 139 locators; the AAV9 lever (`Q-R-01`) and the Wnt
   lever (`Q-R-03`) each rest on **one** complete read; the pannexin lever (`Q-N-16`) likewise.
2. **Contradiction audits, surfaced.** *(Corrected 2026-10-23: the first version of this item read the
   audit block one level too shallow and reported two candidates as standing on unaudited contradictions.
   All 301 declarations in the corpus carry an audit block; `Q-R-02` and `Q-N-17` each carry one auditor
   and a verdict, and the two AUDIT rows were an artefact. Repaired in `9c4dbe4d`.)* The join reads the
   auditor count and verdicts per declaration; the hand-made set has no field for this.
3. **Label lookups actually performed.** Every hand-made card declares `label_lookup: NOT_ATTEMPTED`.
   The derived cards carry a dated openFDA query for every map candidate: `MATCH_FOUND` for two
   (`Q-R-02`, `Q-R-04`), `NO_MATCH_FOUND` for eight class names (a class is not a product: the
   query is recorded, never read as absence), `NOT_ATTEMPTED` where no name could be searched.
4. **The route from a record to its papers, written down.** 60 queries inherit papers through a
   named `PAPER`, `CLAIM` or `DL-` record (`pmids_via_records`), which is how 146 abstentions became
   59 — and that number is the join's measured value: without the one-hop inheritance through the
   registries the module sees almost nothing, which is the operator's thesis that the join is the
   differentiator, measured.
5. **A dependence per candidate and the act that splits it** (`measure_next`), derived from the
   table rather than written: three REPLICATE rows carrying real PMIDs, two AUDIT rows naming the
   manifests, twenty-one SELECT rows.

## 3 · What the module missed that the hand-made cards have

1. **Drug assertions with direction and context.** The hand-made cards carry 30 drug assertions
   (A01 five, EB-VGB-01 eleven, EB-ETX-01 three, …) each with target, endpoint, direction and the
   five context dimensions; one of them (`C01`) reaches `OPPOSES_DISEASE_CHANGE`. The derived cards
   carry **none**: the join binds papers, depth and audit status, not the assertion inside the
   paper, so every derived card is `UNRESOLVED` with `NO_DRUG_ASSERTIONS_SUPPLIED`. The diff on
   `Q-R-01` vs `C01_aav9_wwox` says exactly this: 42 fields differ, among them `directional_summary`
   (UNRESOLVED vs OPPOSES_DISEASE_CHANGE) and `assessment`. Extracting a typed assertion from a
   locator is a Scientist's reading act, and the module does not pretend to do it.
2. **The early-benefit axis.** *(Corrected 2026-10-23: three of the nine, not none, have map records:
   `R-05`, `N-04`, `N-15`.)* Nine `cards_early/` candidates (ethosuximide, vigabatrin, the
   ketogenic diet, cannabidiol, the hormonal axis, …) mostly have no counterpart because the mechanism map
   names few early-benefit records; the calcium axis therefore produced two derived cards and neither
   is the T-type blocker the hand-made set qualified. The candidate universe is the map's, and the
   map's gap is now visible as the module's gap.
3. **Abstention cards with a named missing datum.** Seven hand-made abstentions name the datum
   that is missing and the search that failed to find it (`abstention_card.missing_datum`,
   `search_record`); the derived abstention named only the dependence class. *(Closed 2026-10-23: every
   derived abstention now carries `LINKAGE_GAP` or `NO_PAPER` and its missing datum.)*
4. **Twenty-one map records (`R-04`..`R-09`, `N-01`..`N-15`) cite nothing the join can follow; 19 of
   them cite no paper at all, and only `R-04` cites author-year prose** *(corrected 2026-10-23; the
   first version said twenty records cite author-year prose)*, so the join finds no PMID
   behind them and abstains (`Q-N-01`…`Q-N-15`, `Q-R-04`…`Q-R-09`). The hand-made cards for the
   same levers were written from the manifests directly. The fix is in the record, not in the tool:
   the SELECT rows ask the selector to resolve those citations, and once a map record names a
   `PAPER` id the join inherits its papers on the next run.

## 4 · Where both agree

`Q-R-03` vs `D02_wnt_tankyrase`: same `directional_summary` (UNRESOLVED), same abstention, 33
fields identical; the only load-bearing difference is the label lookup the module performed. Both
sets keep every candidate `IPOTESI`, `canonical: false`, with no score and no rank.

## 5 · Honest summary

The module's value on this corpus is the **join itself** — depth, audit status and the route to the
papers, per candidate, re-derivable in one command — and the **steering** it produces (26 rows for
the next batch, two of them audits that nobody had scheduled). Its blind spot is the **content of
a reading**: direction, endpoint and context stay with the Scientists, and a derived card without
their assertions is a dependence report, not a comparison. The two sets are complementary; the
derived card cannot drift from the manifests, the hand-made card cannot be regenerated.

## 6 · Licences and sources used in this proof

Open Targets (CC0), ChEMBL (CC BY-SA 3.0), PubTator 3 (public domain, 3 req/s), openFDA (CC0;
"Data provided by the U.S. Food and Drug Administration"), Orphadata (CC BY 4.0), iLINCS (CC BY):
read from each source's own terms page on 2026-10-23, quoted in each adapter's `INFO`, and
acknowledged in [`ACKNOWLEDGEMENTS.md`](ACKNOWLEDGEMENTS.md). Nothing was declined in this stage
beyond the sources already declined in the survey (`tool_survey_20261022.md` § 2).
