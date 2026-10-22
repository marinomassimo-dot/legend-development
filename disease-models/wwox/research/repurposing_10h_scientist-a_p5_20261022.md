# Roadmap P5: two comparisons as visible dimensions, no score

> **Actor** `scientist-a` · **Task** `REPURP-10H-P5-A-20261022` · 2026-10-22. Non-canonical research record; touches none of the four scientific current files, `disease_model.md`, `cards/`, `cards_early/`, the roadmap copies or `repurposing_bridge.py`. **Not medical advice.** No score, rank, probability, index, dose, route, schedule or paediatric suitability. Adjacent sources are NOT WWOX EVIDENCE. No paper read, no receipt.

The deliverable and its reasoning are in [`drug_repurposing/p5/p5_comparison.md`](drug_repurposing/p5/p5_comparison.md) (start there) with per-row tables beside it. In brief:

* **RECUPERO_PROFONDO (12 rows)** — non-dominated set: P4-A-01, P4-A-02, P4-B-01, P4-C-01, P4-D-01 (all five): nine pairs incomparable by endpoint and genotype class, one pair (A01-A02) comparable and undecided. Seven of twelve rows rest on **one** Q230P measurement.
* **BENEFICIO_PRECOCE (9 rows)** — non-dominated set: EB-KD-01, EB-VGB-01, EB-ETX-01 (all three): two pairs incomparable, one undecided; the diet and vigabatrin cards share the Chong series.
* **Plain lookup** (Monarch/DGIdb, status INCOMPLETE): reaches only rows with no WWOX-system measurement and none of the five rows that have one.
* **Next experiment**: the cards change nothing in the choice; they attach one fate-of-the-variant assay to five deep rows and one series acquisition to three early rows. Lithium is a row in neither path.
* **Roadmap criterion**: INCONCLUSIVE for choosing a candidate (context dominates); KEEP for choosing what to measure or acquire.

## DEFAULTS_TAKEN

| Condition | Default | Why safe |
|---|---|---|
| "Non-dominated" needs a comparability rule the roadmap does not give | same endpoint and same genotype class, fixed before reading the pairs; a sensitivity stated for the one borderline pair | the alternative (dominance across endpoints) would force an order the cards cannot support |
| Abstentions have no evaluable cell | rows in the tables, not called non-dominated | vacuous truth would read as a result |
| Cells must be the card's own value | extracted verbatim by code, cut at a sentence and marked, full value in `cells.json` | a paraphrase would be a new claim |
| Shared origin is not a card field | computed by hand, labelled a reader's derivation, OWED audit | refusing to count would double-count |
| The A51 exposure statement arrived by relay | kept outside the verbatim cells, marked superseded and unaudited, no dose reproduced | a card frozen at one moment cannot be edited here |
| The lookup is live and the raw packet is 7.8 MB | summary and digest committed, raw left in scratch | rerunnable; no unique material lost |
| Early cards sit in different field containers | explicit field map in `build_p5.py` | the mapping is inspectable |

## STOP_LOG

Empty. No act reserved to the operator was needed; no external spend; no push.

## OWED

* Blind audit by someone other than the author of the reader's derivations: origin counts (§ 1.1, § 2.1), the comparability calls, the eight staleness flags, the reading of the lookup and the "inversion".
* A one-line update to the D01 packet by its author (superseded exposure sentence).
* The Harness decision on the eight gaps (G1-G8).
* A card for lithium in one of the paths, or an explicit decision not to.
