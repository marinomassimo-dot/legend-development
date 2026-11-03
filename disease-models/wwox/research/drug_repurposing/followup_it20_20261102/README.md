# IT20 follow-up — the six "restore-type" needs are a correct abstention, and the stated cause was wrong (2026-11-03)

**Result: nothing to fix in the engine or in the qualification data. One documentation defect, corrected by pointer.**

Non-canonical research material. Actor `scientist`, branch `it20-follow`, baseline `main` = `e7f00f13`. Read-only toward
the four scientific current files, the registries and the receipt ledger; no coverage figure changes, so no generator was
re-run. **Nothing here is medical advice**; no dose, route, schedule or preparation appears in this package. Public
edition: the subject is the WWOX-DEE reference genotype class, never a person. This package does not rewrite IT17–IT19 or
any earlier IT20 dated result — the hypotheses package keeps its findings and receives one correction pointer.

## 1. What was claimed, and what the code does

`hypotheses_it20_20261102/README.md` § 1 and § 2 attribute 6 of the 20 unqualifiable needs to "a `restore`-type direction
with no matching catalogue action vocabulary". **That attribution is false.** The search layer already normalises
`restore` into the up/down vocabulary before any compatibility test:

`framework/scripts/repurposing_search.py`, in `consistency()`:

```python
want = {"up": "up", "down": "down", "restore": "up"}[nd]
```

A `restore` need is therefore treated exactly as an `up` need, and four of the five WWOX-restoration needs additionally
carry a registered coupling row (`coverage/target_roles.tsv`, coupling `same`, basis "the need restores or raises WWOX
protein or transcript: more functional WWOX = up"). There is no vocabulary gap to close: the mapping row the brief
hypothesised as the smallest possible fix **already exists and already fires**. Nor do these six needs share one cause;
they fail at three different, later guards, each of which the record asks for.

The machine-readable field was already accurate. `comparison_summary.json` says, for all six, "associations exist but none
carries a documented action coherent with the stated direction" — a statement about the *catalogue rows*, not about the
need's direction word. The prose compressed that into a vocabulary claim and inverted where the abstention happens.

## 2. The six needs, one by one

Judged against the brief's test — (a) could a compound-target action legitimately be compatible, or (b) is there no
target-level direction to be compatible with.

| Need | Direction / certainty | Evaluable targets | Where it actually abstains | Verdict |
|---|---|---|---|---|
| `NEED-WWOX-GENE-ADDITION` | `restore`; supported_in_WWOX_mouse_model | WWOX (`disease_gene_product`), coupling `same` | `action_not_stated` | **(b) correct** |
| `NEED-WWOX-SPLICE-CORRECTION` | `restore`; inferred, conditional on the unresolved cryptic-site outcome | WWOX, coupling `same` | `action_not_stated` | **(b) correct** |
| `NEED-WWOX-ENDOGENOUS-BOOST` | `up`; context_dependent | WWOX, coupling `same` | `action_not_stated` | **(b) correct** |
| `NEED-WWOX-MISSENSE-PROTEIN-RESCUE` | `up`; inferred | WWOX, coupling `same`; chaperone/UPR symbols are `pathway_member` | `action_not_stated` on WWOX; `not_an_intervention_target` on HSPA8 / HSPA1A / HSPA1B / XBP1 / ERN1 | **(b) correct** |
| `NEED-WWOX-PTC-READTHROUGH` | `restore`; **unknown** | WWOX, coupling **`unresolved`** | `coupling_not_measured` | **(b) correct** |
| `NEED-MYELINATION` | `restore`; "unknown for any pharmacological route" | CHRM1 (`intervention_target`); five `readout_marker` symbols | `no_coupling_row` on CHRM1 | **(b) correct, and it is the one that could change** |

**The three WWOX-level needs and the missense need.** The entire catalogue reach on the WWOX gene product is four DGIdb
rows: Sorafenib, Gemcitabine, a recombinant TNF-family protein, and a literal `NULL` placeholder the loader already
discards. None states an up/down action on WWOX, so each is `action_not_stated`. There is no agonist/antagonist action
to be coherent *with* — the abstention is the engine declining to invent one, which is the rule the module exists to
enforce. Granting these a direction would mean asserting that an oncology kinase inhibitor and a nucleoside analogue
raise WWOX protein, which no source in the module says.

**Why the chaperone route does not rescue the missense need.** HSPA8, HSPA1A, HSPA1B, XBP1 and ERN1 *do* carry stated
down-actions from catalogue compounds, so this is the shape the brief flagged as a possible defect: a stability modulator
with a stated direction on a named target. It is nonetheless a correct abstention twice over. Those symbols are declared
`target_kind: pathway_member`, i.e. members named by the card, not intervention targets of this need — and the need's own
`do_not_assume` holds the route unresolved in terms the engine must not overrule: chemical chaperones were judged to act
in the wrong compartment (an objection IT5 P8 narrowed but did not settle, with no enzyme and no WWOX system tested), and
HSP70 co-induction carries a stated hypothesis of harm. Promoting these to `intervention_target` would convert a
documented *caution* into a qualified lever.

**`NEED-WWOX-PTC-READTHROUGH` is the clearest case not to touch.** Its coupling row exists and reads `unresolved`,
explicitly demoted from `same` by the independent audit of 2026-10-28 because "the need's only evidence scope is an
unverified hypothesis". The one-character data edit that would make it usable is precisely the edit an audit already made
in the other direction. The need's own certainty field reads `unknown`.

**`NEED-MYELINATION` is the only need where a compound action is directionally real.** CHRM1 is an `intervention_target`
and the catalogue states 51 up-actions and 108 down-actions on it; the need carries 318 associations, by far the largest
blocked slice. It abstains because `target_roles.tsv` holds **no row at all** for this need — not an unresolved row, no
row. Adding one would mean asserting the sign that links muscarinic activity to myelin formation in this disease, and the
need's record refuses exactly that: certainty is "unknown for any pharmacological route", and `do_not_assume` warns that
the axonal signal may be absent and that a pro-myelinating agent may be unable to act if the neuron does not signal.
Abstention is therefore correct **today**, and this is the single need among the six whose status a measurement could
legitimately flip: one WWOX-system datum fixing the sign of a muscarinic-class effect on myelination would convert 318
associations into an orderable question, with no code change at all. That is a measurement result, not a vocabulary row,
and it belongs to the INV-02 / INV-06 class the hypotheses package already names.

## 3. Before and after

No code and no qualification data changed, so every figure is unchanged by construction, and the three regressions the
brief asked for are already the module's own: `test_repurposing_coverage.py` holds a newly-usable case (the
direction-evaluable excitability needs), an abstained case that must stay abstained, and an unknown that stays unknown.

| Measure | Before | After |
|---|---|---|
| needs with no adequate tool | 20 of 23 | 20 of 23 |
| direction-coherent associations | 208 of 3,331 | 208 of 3,331 |
| needs usable for qualification | 3 | 3 |
| compounds entering a ranked unit | unchanged | unchanged |
| queue | unchanged | unchanged |

The only change in the repository is this note plus a one-line correction pointer in the hypotheses package, where the
false cause was stated.

## 4. What this says about the method

The brief's own framing — judge first whether an abstention is a defect — is what kept a plausible one-row "fix" out of
the data. Three of the six needs had a coupling row ready to use and failed later, for reasons each need's record states
in its own words; two were held by an explicit audit or an explicit caution; one is waiting on a measurement. A session
that had trusted the package's prose would have looked for a vocabulary mapping, found one already present, and been
tempted to loosen a guard to produce the change it came to produce.

The transferable lesson is narrower than "read the code": **a package's prose cause and its machine-readable cause can
diverge, and the JSON was right.** `why_no_tool` named the catalogue rows; the README named the direction word. The
abstention-class vocabulary (`action_not_stated`, `no_coupling_row`, `coupling_not_measured`,
`not_an_intervention_target`) is precise enough to separate four distinct causes inside one group of six — and the
grouping in the prose, by direction word, destroyed exactly that distinction. Where a closed abstention vocabulary
already exists, a summary should quote it rather than paraphrase it.
