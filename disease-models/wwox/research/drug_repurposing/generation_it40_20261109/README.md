# IT40: physiological hypotheses and mechanism-first search reach generation, comparison and the dashboard

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Nothing here is a predictive result: the proof is of **functional capacity and traceability**, and no independent data exist to test prediction.

## P4 baseline: where the current path stops (S16 = S17)

The generator was regenerated end to end once with IT40 inputs (S17: same recipe as S15/S16, about 6 minutes, 4 GB cap). Result: **994 proposals, 220 eligible, 15 hand-overs, every column of every row identical to S16.** The path for gene-graph hypotheses is unchanged, as intended.

| Case | Stopping point of the current path | Evidence |
|---|---|---|
| Physiological hypothesis with no proven gene pair (membrane MH1) | **representation**: no proposal has a GRIN/GRIA/GRIK/HCN/KCNQ/GABR/SLC12A/GJD2/PANX target (0 of 994); the hypothesis reached consumers as two free-text cells | `measure_it40.tsv` case 1 |
| AMPA/NMDA with competing explanations (BH1–3) | **composition and propagation**: the prediction matrix (17 arms × 7 explanations) had no consumer; rivals were reachable only as words | case 2 |
| Premise already correctly consumed (HIF1A→HK2, ISRIB) | none | case 3: S16 versus S17 identical |
| Abstain (Kv7 / resting K+ conductance) | **selection**: a symbol lookup offers 7 molecules including 2 openers; nothing says why not | case 4 |

## What was added (all through existing paths; no new registry, gate or catalogue)

* `conditional_proposals.py` reads each linked hypothesis in place (Harness `framework/scripts/hypothesis_package.py`) and writes `conditional_proposals_it40.tsv`: starting observation and chain, context, competing explanations (the hypothesis's own text **and** the linked alternatives with their matrix column), premise and pharmacological action, source and limits, expected result per arm and explanation (untruncated, with the arms' own "does not separate" note and the INFERENZA label), the measure that changes the decision, experiments, the compound or probe the package names (named, not ranked) and an explicit **nomination state**: MH1 and MH3 ABSTAIN. A `corrections_it40` column carries what the independent verifier found. No gene–gene arc is made; `gene_arc` is always false.
* `../mechsearch_it40_20261109/`: a search that starts from six action–context–benefit relations (R1 GluN2B-directed, R2 GluN2A, R3 AMPA/kainate, R4 Ih, R5 Kv7, R6 connexin/pannexin) and only then lists what the catalogue holds: distinct parent molecules, direction (a raiser is not an antagonist), the **granularity of the catalogue target record** (one protein, a two-gene assembly, a family record with the subunit unresolved) and phase and access as recorded. `identity_check.tsv` checks, for the 15 tools the packages name, whether the record found by name carries the intended target.
* The 19 membrane and AMPA/NMDA proposals were applied (see `../consume_it40_20261109/RECONCILIATION.md`); six conditional hypotheses are in the dashboard under INV-05 and INV-18 (`reader_view.tsv`, five languages, no compound name, in both editions).

## P7 measure (same cases; `measure_it40.tsv`)

| | Current path | Simple baseline | New path |
|---|---|---|---|
| Hypotheses with representation | 0 | free text | 6 records, 7 fields each |
| Arm × explanation cells readable | 0 | 0 | 119 distinct (an arm shared by hypotheses is counted once) |
| Molecules for the symbol GRIN2B | | 24 | 24 listed, **4** with a GluN1/GluN2B assembly record (all phase ≤ 2, none approved), 20 with a family record (subunit unresolved), 3 raisers flagged |
| AMPA/kainate antagonism | | 74 rows | 15 molecules, 9 antagonists |
| Kv7 | | 7 molecules, 2 openers offered | 0 nominated, reason stated |
| Tools with a record carrying the intended target | | 14 of 15 found by name | 11 confirmed, 4 not (1 absent, 2 record without the target, 1 name mismatch) |
| Premise already consumed | identical | | identical (0 columns changed) |

Ablation on the same inputs: without the package link the six rows have no expected-result cell and fewer competing explanations (`conditional_proposals_nolink.tsv`); the effect is from the link, not from the new sources.

**What this shows.** Relevant knowledge that no consumer could read (a prediction matrix, rival explanations, tool identities) is now consumed and can change an abstention (Kv7), a comparison (a GluN2B arm must be read against a measured NMDA-receptor current, and only four catalogue molecules carry a GluN1/GluN2B record, none approved) and an experiment order (`next_investigations_it40.md`). **What it does not show:** a better prediction, a new favourable compound, or a change in the generator's selection. The catalogue gene count is a record granularity, not a selectivity (the verifier overturned the first reading).

## Verification

An independent sonnet/high delegate (verify/VERDICTS.md) checked seven questions against the originals. It overturned first versions on: d-APV (present in the catalogue as D-Ap5), the "subunit-specific" rule (a record granularity, not selectivity), row counts (distinct molecules: R3 74 rows are 15 molecules, R5 36 rows are 7), truncated cells, dropped rivals and qualifiers, standard-error multiples not reproduced (about 1.1–1.4 against the quoted 3.9 and 2.9) and a "sufficient" step that rests on a culture result. All were corrected before closing; the original verdict text is kept.

## Limits

* The package tables are checked for consistency with the consumer texts, not against the primary papers (nobody re-read them here).
* Reader summaries (`reader_view.tsv`) are one-or-two-sentence condensations written for the dashboard; each cites its source rows; translations are mine, unreviewed by a native speaker.
* Relations beyond NB-1: only `nb1_myc_20261107/output/generator_relations.tsv` exists; there is nothing else to consume yet.
* HIF1A→BNIP3 (three proposals, no investigation): not started; it needs its own literature question, not a recycled HK2 row.
* The catalogue holds no ifenprodil or Ro 25-6981 GluN2B mechanism row and no Brilliant Blue FCF record (a catalogue gap, not a statement about the molecules).
