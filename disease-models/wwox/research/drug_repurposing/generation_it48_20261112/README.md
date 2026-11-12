# IT48: from verified deliveries to consumers (Strategic Advisor pilot container)

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. No rank, sign, tier or qualification of any candidate was changed by this work.

## Increment 1 (SCI43 reopened rows) — `../sci43_reopen_it48_20261112/`
Eight rows that stood producer-read only were reread by a distinct verifier against the original full texts: **5 SUPPORTED (D01, D04, D07, D08, D13), 3 PARTLY (D02, D03, D11), 0 NOT_SUPPORTED** (the first hand-back and the first consumer clauses said 4 supported by omitting D13; corrected 2026-11-12 in the verdicts file, KH1, INV-18, the SCI43 README and the five-language passage). The 23 percent figure survives as printed arithmetic but is a one-dose Ba2+ increment in P28-P42 auditory cortex, not a Kir2 share; no row measures a juvenile layer II/III Ba2+ share. Consumers: KH1 premise, INV-18 next_test, SCI43 README, open question IT48-Q01 (open).

## Increment 2 (SCI48 comparator package) — dispositions of `../nrf2_comparator_sci48_20261112/consumer_delta.md`
| Row | Disposition | Where |
|---|---|---|
| 1 IT46-Q06 | applied: CONCLUDED (not met as printed; comparator for a survivor set); new OPEN IT48-Q02 (supplement; needs a route the operator authorises) | `open_questions_map.tsv` |
| 2 IT46-Q09 | applied: CONCLUDED for existence and role only; new IT48-Q03 (acute verified loss; wet laboratory) and IT48-Q04 (abstract-only readings; literature) stay OPEN | same |
| 3 V19 | applied: RA839 added to the name list with its limits (myeloid only, identity from the paper, catalogue id not reconciled); counter clause: comparator not probe, system and endpoint kept, previous abstract-depth sentence replaced; open_premise clause (protein and mRNA at the endpoint time); public text uses descriptors, not catalogue names (shareable audit) | `compound_view.tsv`, five-language passages |
| 4 INV-08 X1-X3 | applied: dated clause (loss as protein and mRNA at the endpoint, the electrophile inside the loss arm, loss-alone and reagent-alone arms, matched exposures, inactive analogue control) | `investigations*.tsv` |
| 5 engine rows N01-N13 | applied: package registered (`hypothesis_packages.tsv`, role pharmacological_comparison, INV-08); engine rerun, see below | `compound_decisions_inv08_it44.tsv` |
| 6 aliases | applied for `ra839`, `sulforaphane`, `cddo-me` (same ester as bardoxolone methyl); **`sfn` not aliased**; no numbered aliases; an alias finds a mention, it does not merge chemical identities (stereochemistry, the inactive analogues RA889 and RA912 and ambiguous abbreviations stay distinct) | `comparison_engine.py` |
| 7 identity declarations | not applicable: the declarations file maps card ids to ChEMBL ids and RA839 has none; identity stays in V19 as "not reconciled" until a lookup succeeds | — |
| 8, 10 | already applied by SCI48 (dated lines in its own earlier folder) | — |
| 9 receipts | applied: 37 recorded through `record_staged_receipts.py` after a trial (producer first); three `prior_receipt` lineages were declared at integration (two verifier receipts point to the producer receipt of the same study; the Winkel producer receipt points to the earlier abstract-only receipt); ledger 1,855; registries regenerated | ledger, registries |

## Before and after, by running the engine (INV-08)
Before (IT47 tree): sulforaphane NONE (no proposition named it); RA839 absent; bardoxolone methyl ABSTRACT (one row). After: sulforaphane PRIMARY with three counted propositions (N05, N07, N11); RA839 PRIMARY (SCI46 D20 plus N01); bardoxolone methyl ABSTRACT with two rows and no potency pair; new measurements M-N1..M-N4 reach the binder, the electrophile and the new reagent.
**An error the run exposed:** the engine derives the role "probe" for sulforaphane and for RA839 because its tier rule reads depth and class, not meaning; the package states both as comparators (germline or unverified loss; RA839 myeloid only). The engine has no comparator role. The label is therefore disclosed next to the display (V19 counter) and handed to Harness as an engine gap; it was not patched here. The SCI46 row D20 (RA839 at abstract depth) is still counted by the engine next to N01; its sentence is superseded in the text, not in the loader.

## Limits
Consumption by the generator and the view was shown by running them; a better prediction was not shown. Translations are the assistant's. SCI47 package B inferences (OPC contribution, the low held human KCNQ2 value, the provenance of the second human table) are still not independently verified and are public in five languages (a dated clause says so).

## Pilot limit recorded (IT48 A2)
Stage A #2 could not read the SCI48 package: the checkout it read (commit 54b985c7) did not yet contain it, although the brief stated it as delivered on main. The assessment is kept as saved and was not rerun; Harness has a separate task for the input-availability problem.
