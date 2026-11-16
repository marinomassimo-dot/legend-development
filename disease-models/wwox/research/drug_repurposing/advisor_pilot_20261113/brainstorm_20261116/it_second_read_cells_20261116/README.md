# Second read of 25 of SCI's 244 frozen cells (IT; non-canonical; not medical advice)

Written for: SCI (corrections as a dated line, never an edit of the frozen files) and ADV. Reference genotype class only. Mechanism and evidence only; no clinical outcome table used (A1, aed_compare, INV-10 were forbidden to the reader; the reader reports it saw some adjacent rows incidentally and did not use them).

Sample: stratified by script from `aed_matrix_sci_20261116/output/cells_form.tsv` at SCI's freeze f5b71a3f4345: 4 aggravation (all that exist: T12, T16, T17 x2), 5 top-set class, 5 tier-3 or genotype-contrast, 11 random non-zero tier (seeds 56 and 5656). Reader: one legend-delegate (sonnet-5-5, effort high; read back: 30 turns, output 32,907, cache written 115,700, cache read 1,858,185). One reader, not blind to the cells' claims; IT verified two of its claims (below).

## Counts (25 cells)
Thread statement: says_it 21, says_less 3 (T12, T16, T7), locator_wrong 1 (T14), says_more 0, not_openable 0. Evidence tier: ok 23, too low 2. Directness: ok 24, too low 1. 25 cells rest on 10 locators; Breton 2021 (PMID 34634460) decides 17 of them (T1 x10, T2 x4, T13 x6 via CLAIM 021 and the INV-05 README), so the sample carries far fewer than 25 independent checks.

## Cells that would change
* T14-ampa_antagonist-seizure-later_unspecified: tier 2 to 3; T15-valproate_type-seizure-later_unspecified: tier 2 to 3. Both because the data are knockout versus control (a genotype contrast per the rubric as written, and the cells' own has_genotype_contrast flag says yes). If tier 3 is meant to require a functional readout, tier 2 stands and the flag should be reconciled instead.
* T2-sodium_channel-seizure-P13-P15: directness 0 to 1 (low confidence): T12 scores the same class against the same deficit as 1 with sign unknown, so a neutral sign beside a plausible link of unknown direction reads as unknown used as neutral.
* T14 locator wrong: the cell cites PMID 42397075 (PAPER 094); IT checked the held surface of that paper (the partial-locators dossier) and found no GAD or GABRB mention; the statement is carried by CLAIM 002 and the mechanism map line 101, and the GAD-up/GABRB-down data are in PMID 34268881 (PAPER 039). The held dossier of 42397075 is partial, so this says the held surface does not contain it, not that the paper does not.

## Other readings (not tier changes)
T12 says_less: the source gives the reduced-inhibition premise only; nothing about sodium-channel dependence or aggravation. T16 says_less: held text is the Ikonomidou 1999 abstract only (NMDAR blockade, late fetal or early neonatal period); it names neither pore blockers nor P6-P8; the aggravation sign has a source statement. T7 says_less: the two second-reader READMEs cover K2P tool pharmacology only. Match signs for several cells are class expectation or a registry sentence ("expected to stop"), not a measurement: the source tool is d-APV and no NMDAR modulator has been tested in any WWOX model. `later_unspecified` extends Breton (P13-P17 only). Breton 'increased firing' means more spikes at the same current; the F-I slope did not differ (p 0.3669), so depolarisation explains part. Sign handling (unknown never neutral; no aggravation without a source statement) held in the cells read.

## Limits
Not read in the original: Ikonomidou 1999 (abstract quote only), Mierau 2004 and the O'Connell and Kang papers (through second-reader notes). Locator paths for `analysis/mechanism_intervention_map.md` and the dossiers omit their `disease-models/wwox/` or `research/fulltext_dossiers/` prefix (path style, not content). A PubMed lookup by the reader was blocked by the permission classifier and not worked around. 25 of 244 cells is 10%; this is not an audit of the matrix.
