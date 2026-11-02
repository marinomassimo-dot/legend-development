# IT19 P5 — making the matching comparison evaluable (2026-11-02)

Non-canonical research material; not medical advice; pharmacological compatibility only, no benefit claim; no compound is proposed for use. Public edition, WWOX-DEE genotype class.

This is a **new dated subpackage**. The IT18 P4 pre-registration, locked answers, results, case tables and controls (`../matching_it18_p4_20261101/`) and the sealed IT17 freeze are read and **not modified**. The IT18 thresholds (the 40-determinate-row floor) belong to that experiment and are not reused here as a block on this one: this package does not test general superiority of any path, it measures whether the comparison can be adjudicated at all, and what one module decision gains from it.

## The question, and why IT18 could not answer it

IT18 evaluated 33 EVAL directed rows with 2 determinate GtoPdb references (8 of 76 directed rows determinate in total). 20 of the 31 uncovered EVAL rows were compounds with no GtoPdb ligand carrying a ChEMBL id, 11 were ligands with no interaction on the need's genes, and 72 of the 76 directed rows enter through ChEMBL records above single-protein level. The constraint was reference coverage at the resolution the needs are written in. This package builds that reference for a bounded, rule-selected set of unresolved pairs, from sources other than the GtoPdb join, and asks what it adjudicates.

## Step 1 — selection rule, committed before any new reference outcome was opened

[`SELECTION.md`](SELECTION.md) (commit `e1fe0b87`) holds the rule, the strata table, the required resolution per need, the source order, the dependency and error-attribution policy, and four written predictions. `select_pairs.py` applies it: of the 68 IT18 directed pairs with no determinate reference, **32 pairs over 25 compounds** in 12 strata (`selection.tsv`). Every stratum with data is represented; the strata that carry the attribution question whole (heterogeneous 26-component group blockers, both partial agonists, the single-protein glutamate records, the lone NMDA positive modulator) are taken entirely, and the homogeneous strata where more compounds repeat the same question are capped. Six of the 32 pairs carry an IT18 label of `opposite` or `indeterminable`, so the set is not a bag of easy confirmations.

## Step 2 — the reference

`reference_it19_p5.tsv`, one row per pair, with compound identity, the target **at the resolution actually measured**, action and context, measure type, source and locator, the dependency on the module's own construction sources, a resolution note and an error attribution. `check_reference.py` enforces the protocol (7 tests): a determinate label needs a measured target, a measure type and a locator; a binding-only measure can never carry a direction; an `unknown` row must say what is missing; the dependency vocabulary is closed.

| Reference state | Pairs |
|---|---|
| `compatible` | 13 |
| `opposite` | 4 |
| `indeterminable` (evidence exists, not at the required resolution, or binding only) | 9 |
| `unknown` (nothing found in the bounded search) | 6 |
| **usable (determinate) rows** | **17 of 32** — 11 from a functional measurement, 6 from a class-level attribution |

Dependency: 8 of the 17 determinate rows are independent of the module's own input; the rest are `partly_shared` (GtoPdb/ChEMBL/DrugCentral share part of their literature, or the document is one the ChEMBL mechanism cites). Agreement on a `partly_shared` row is not independent confirmation and is reported separately.

**Coverage before and after, on the same 32 pairs: 0 → 17 usable rows** (the pairs were selected precisely because the IT18 reference had none). Over the whole IT18 directed universe the determinate count rises from 8 of 76 to 25 of 76 (17 new, 11 of them on the EVAL split and 6 on DEV); over the 33 EVAL directed rows it rises from 2 to 13. Those wider figures are arithmetic on a non-random subset — the strata were chosen to discriminate, not to sample — so they describe this selection, not the universe.

### What the reference found about the group records

- **terodiline** (P01-P02): the only calcium-channel measurements are **L-type** — block of cardiac L-type current, IC50 about 15 uM (PubMed:10482914), 33.5 uM (PubMed:9151306), human CACNA1C AC50 above 50 uM in ChEMBL. No Cav3 or native T-type measurement was found. The ChEMBL group record cites PubMed:10482914 **itself**: the annotation "voltage-gated calcium channel blocker" is legitimate in the source and becomes improper only through LEGEND's expansion onto CACNA1G/H/I.
- **suloctidil** (P03-P04): L-type radioligand binding only (Ki 152-510 nM, DRUGMATRIX panel in ChEMBL document CHEMBL1909046); described as a calcium antagonist. No T-type measurement. Same error attribution.
- **phloroglucinol** (P05-P06): the single reference the mechanism cites is a **clinical trial in diarrhoea-predominant irritable bowel syndrome** (PubMed:31917916). No calcium-channel measurement at any resolution was found. Here the group annotation is not supported by its own cited reference.
- **bepridil** (P07-P08): T-type block **is** documented — human recombinant Cav3.2, IC50 0.4 uM at -70 mV, voltage-dependent, no use-dependence (PubMed:15855830); native T-type block more potent than L-type at diastolic potentials (PubMed:1281221). The ChEMBL group record cites a troponin-C structure paper instead, so this reference is independent of the module's input. At the T-TYPE need (Cav3.1/3.2/3.3) the pair is determinate `compatible`; at the SEIZURE need, which lists CACNA1G alone, it stays `indeterminable` because no Cav3.1 value was found.
- **gabapentin** (P09-P10): the measured target is the **alpha2delta auxiliary subunit**, not a Cav3 pore-forming gene; no net direction on T-type current. The module already abstained here, and the abstention is right.
- **trimethadione** (P11-P12): no isoform-resolved measurement; a T-type **class** attribution with rodent in vivo pharmacology (PubMed:16171802, PubMed:17291698). Determinate at the T-type family level, indeterminable at CACNA1G alone. Family-level evidence is kept, not discarded: the T-TYPE need is written at that level.
- **apinocaltamide** (P13-P14) and **ABT-639** (P15): human Cav3.1/3.2/3.3 functional values (ChEMBL document CHEMBL4177680; GtoPdb targets 535/536/537) — subunit-level, determinate, including CACNA1G itself.

### Where the reference contradicted an abstention

**apimostinel and rapastinel** (P22-P23): ChEMBL curates PARTIAL AGONIST, and IT18's L rule abstained on that (`action_partial_or_unknown`). A 2025 review defines the stinels as **positive allosteric modulators** of NMDA receptor activity and states that the earlier partial-agonist descriptions were inconsistent and at times contradictory (PubMed:40005971). At receptor level the direction is an increase, which is **opposite** to the need. The abstention was conservative, not informative: a direction was available and an exclusion was missed. The source conflict is recorded, not resolved — this is a secondary source and no primary measurement was read.

## Step 3 — the module's answers, written and digested before the join

`module_answers.py` reads only the selection, the catalogue, the needs, the role table and the artefact table, and runs the **active path** (`framework/scripts/repurposing_search.py`). `module_answers_prefix.tsv` + `.digest.json` (guard off, the behaviour that produced the IT18 universe) were committed in `82690f75`, before `results_it19_p5.json` existed. The IT18 locked `L_v1`/`L_v2` labels travel unchanged in the same table.

**Declared prior knowledge, and the limits of a retrospective comparison.** One actor did both halves. When the reference was built, that actor had already read the IT18 README and the locked L labels (they are inputs to the selection rule), so this is **not** a blind evaluation: hiding the answers would not have made it prospective. Two things carry the weight instead: the resolution rule, the measure-type rule and the dependency policy were written and committed before any new reference outcome was opened, and the module's side is **machine-generated** from committed code and a digest, so it cannot have been nudged toward the reference. All sources are pre-existing curated data and literature; no prospective outcome is claimed.

## Step 4 — the module defect, in the ACTIVE path

IT18 found the transfer defect on DEV but repaired it only inside its own comparison script (`L_v2` in `matching_task.py`). The active path carried it: `Index` buckets a ChEMBL mechanism under **every** gene symbol of the record's components, so the 26-component `CHEMBL2363032` group record gave CACNA1G/H/I a BLOCKER direction and `consistency()` returned `consistent`. The row did carry a limit string saying the link "is not subunit-specific", but the label asserted a direction anyway.

Fix (`framework/scripts/repurposing_search.py`): `module_intervention_symbols(needs)` and `group_transfer_unresolved(src, t, module_symbols)`. A ChEMBL `PROTEIN FAMILY` or `PROTEIN COMPLEX GROUP` record whose components are **fewer than half** inside the module's intervention targets no longer resolves a direction to a member gene: the label becomes `direction_unresolved` with the reason naming the record and the component counts. The set is module-wide on purpose, so a need that lists one member of a family the module reasons about elsewhere (SEIZURE lists CACNA1G, T-TYPE lists all three) does not disqualify the family record. Single proteins and defined complexes are untouched; the row stays visible and the source's own action is never rewritten. `repurposing_coverage.py` passes the same set, so the coverage surface and the CLI agree. The two dated package scripts that call `associations_for_need` (`catalogue_funnel_it18_p2_20261101`, `usable_compounds_it7_p2_20261029`) do not pass it and keep their historical output on purpose.

Three regressions, `framework/scripts/test_repurposing_group_transfer.py` (verbosity=2, synthetic entries only):

1. **a case that previously received an improper attribution** — the 26-component group BLOCKER on CACNA1G: `consistent` before, `direction_unresolved` after, with `group_record_mostly_outside_module_targets` and "3 of 26 components" in the reason, still not excluded from the listing, source action unchanged;
2. **a correctly attributed case that must stay usable** — the three-component T-type family record under **both** calcium needs, the 7-component NMDA receptor group (4 of 7 inside), the defined GRIN1/GRIN2B complex and a single protein: all stay `consistent`;
3. **an unknown case that must stay unknown** — the same 26-component record with action MODULATOR: `direction_unresolved` before and after, and the reason stays the source's own ("the source states no up/down action"), because the guard never overwrites a reason that is already the honest one.

The 65 existing regressions in `test_repurposing_coverage.py` still pass.

## Step 5 — what the fix changed, measured

`join_it19_p5.py` → `results_it19_p5.json`, `cases_it19_p5.tsv`. An `unknown` or `indeterminable` reference is never scored as an error; a row the module does not direct is an abstention, not a mistake.

| Path | Directed assertions on a determinate row | Agree | Accuracy, Wilson 95 percent |
|---|---|---|---|
| Active path, guard off (pre-fix) | 13 | 13 | 1.00 [0.772, 1.000] |
| Active path, guard on (post-fix) | 12 | 12 | 1.00 [0.758, 1.000] |
| IT18 `L_v1` (locked labels, for comparison) | 15 | 15 | 1.00 [0.796, 1.000] |
| IT18 `L_v2` (locked labels) | 14 | 14 | 1.00 [0.785, 1.000] |

No disagreement with the reference was found on any path, on a selection built to find them: zero `asserted_and_disagrees` rows. With 12-15 assertions the lower bound sits near 0.76-0.80, so **no claim of general accuracy, and no claim of superiority of one path over another, is made or supported**. These are case series with intervals.

**Why the active path asserts less than IT18's L rule.** The active path requires an explicit coupling row in `coverage/target_roles.tsv` before it will call a row consistent or opposed. Three couplings the reference can score are `unresolved` there on purpose: CACNA1G under the SEIZURE need (demoted by an independent audit: nothing in that need's own sources measures a T-type effect), GRIA1-4 (the need says "possibly AMPAR"; no WWOX datum), and GRIN2D. So the active path abstains on P11, P13, P27, P29, P31 and on part of the NMDA group rows even where the reference holds a direction, and `abstained_reference_determinate` counts 4 rows before the fix and 5 after. Those abstentions are not the group-transfer defect; they are the WWOX side of the model declining to couple a target to the need's quantity, which is a different and documented decision.

**The decision that improved, and its price.** The fix changes exactly 4 of the 32 pairs, all at the T-TYPE need, all through the 26-component group record:

| Pair | Compound | Before | After | Reference | Verdict |
|---|---|---|---|---|---|
| P02 | terodiline | consistent | direction_unresolved | indeterminable (L-type only) | removed an unsupported attribution |
| P04 | suloctidil | consistent | direction_unresolved | indeterminable (L-type binding only) | removed an unsupported attribution |
| P06 | phloroglucinol | consistent | direction_unresolved | unknown (no channel measurement at all) | removed an unsupported attribution |
| P08 | bepridil | consistent | direction_unresolved | **compatible** (human Cav3.2, IC50 0.4 uM) | abstained although the reference holds a direction |

**3 of the 4 changes remove a direction the reference does not support; the fourth removes one it does.** That is the honest result and it is the tension the task names: a better abstention must not hide available information. It is reported, not smoothed. The information is not deleted — the bepridil row stays in the listing with its action, its record and the reason for the abstention — but the module now has no field in which a documented subunit-level measurement can re-license a direction the group record cannot carry. **Named capability gap: a per-compound, per-gene evidence override, sourced and receipted, that a group-record abstention can defer to.** Without it the guard is right 3 times in 4 on this selection and the fourth case needs a human to read the row.

Pharmacological relevance, research priority and biological benefit stay separate throughout. `compatible` here means only that a measured action has the direction the need states. It says nothing about benefit in WWOX deficiency, nothing about safety, and nothing about whether the need's direction is the beneficial one. Several of the selected compounds (bepridil, terodiline, suloctidil, trimethadione, phloroglucinol) are withdrawn, unmarketed or non-prescription agents in the catalogue's access field, and one selected pair (P19, memantine) is a compound the needs were written from — the IT18 construction-leakage control already flagged it, and it is kept and labelled rather than swapped.

## Receipts

13 abstract-level `FULLTEXT_READ_RECEIPT` JSONs in [`receipts/`](receipts/), one per literature source used for a reference label, each validated with `fulltext_receipts.py record --dry-run` (all 13 "DRY RUN OK"). **They were not appended to the ledger by this package** and are handed back for the integrator to append in event-ID order. Depth is `abstract_only` with `source_kind: abstract`: no full text was retrieved, and every label states its measure type, so a class attribution is recorded as `determinate_class_level` and never as a functional measurement. No reading claims an experimental detail its abstract does not report.

## Limits, stated plainly

1. 32 pairs, 17 usable references, 12-15 scoreable assertions per path. Every figure is a case series with an interval; no general superiority is claimed for the contextual path, the active path or the target-only listing, and none is excluded.
2. The selection is deliberately non-random: it was built to discriminate attribution kinds, so its agreement rates are not estimates of universe-wide accuracy.
3. Retrospective and single-actor on the reference side (see step 3). The module side is machine-generated and digested; the reference side is not blind.
4. 6 of the 17 determinate rows rest on a **class-level** attribution (a review, a clinical endpoint, in vivo pharmacology), not on a functional measurement at the target. They are counted separately and never merged with the functional rows.
5. 9 of the 17 determinate rows are `partly_shared` with the module's own construction sources; agreement there is not independent confirmation.
6. 6 pairs stay `unknown`. Unknown is not negative: the bounded search (GtoPdb cache, ChEMBL activity and assay records, DrugCentral, PubMed) found nothing, which is a statement about the search, not about the compound.
7. The fix is a guard, not a resolver. It removes unsupported directions and, on this selection, also removed one supported direction (P08). The capability gap named above is the repair route.
8. Nothing here changes any canonical file, the IT18 package, or the IT17 freeze.

## Reproduce

```bash
cd disease-models/wwox/research/drug_repurposing
P=matching_it19_p5_20261102
python3 $P/select_pairs.py --answers matching_it18_p4_20261101/answers.tsv \
  --it18-eval-ref matching_it18_p4_20261101/reference.tsv \
  --it18-dev-determinate matching_it18_p4_20261101/controls_it18_20261101/controls_result.json \
  --catalog catalog/catalog.jsonl.gz --needs needs/needs.json --out $P/selection.tsv
python3 $P/check_reference.py --selection $P/selection.tsv --reference $P/reference_it19_p5.tsv --json
python3 $P/module_answers.py --selection $P/selection.tsv --catalog catalog/catalog.jsonl.gz \
  --needs needs/needs.json --out $P/module_answers_prefix.tsv --digest $P/module_answers_prefix.digest.json
python3 $P/module_answers.py --selection $P/selection.tsv --catalog catalog/catalog.jsonl.gz \
  --needs needs/needs.json --guard --out $P/module_answers_guarded.tsv --digest $P/module_answers_guarded.digest.json
python3 $P/join_it19_p5.py --selection $P/selection.tsv --reference $P/reference_it19_p5.tsv \
  --prefix $P/module_answers_prefix.tsv --guarded $P/module_answers_guarded.tsv \
  --out $P/results_it19_p5.json --out-tsv $P/cases_it19_p5.tsv
python3 $P/test_select_pairs.py && python3 $P/test_check_reference.py && python3 $P/test_join_it19_p5.py
python3 -B ../../../../framework/scripts/test_repurposing_group_transfer.py
python3 -B ../../../../framework/scripts/test_repurposing_coverage.py
```

Third-party data: identifiers, coarse classes, short locators and the compound names only. The DrugCentral TSV, the UniChem map and the ChEMBL activity pull used for this package live in the gitignored `files/drug_repurposing_it19/matching_it19_p5_20261102/cache/` (5.6 MB; digests in `cache_SHA256SUMS.txt`, which is committed); no raw third-party table is committed. Public GETs only (ChEMBL REST, DrugCentral download, PubMed metadata), zero spend, no registration, no account, no contact address sent to any service, no new terms accepted. ChEMBL content is CC BY-SA 3.0, GtoPdb CC BY-SA 4.0, DrugCentral CC BY-SA 4.0; PubMed metadata and abstracts are cited by PMID and DOI in `reference_it19_p5.tsv` and the receipts.
