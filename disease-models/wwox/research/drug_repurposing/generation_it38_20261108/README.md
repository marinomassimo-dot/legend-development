# IT38: the MYC relations of NB-1 reach the generator (stage S14)

Non-canonical, not medical advice. This is a **consumption** change: knowledge already qualified in `nb1_myc_20261107/` now changes what the proposal generator writes. It is not a predictive result and no proposal changed rank, eligibility or hand-over.

## Four layers, kept apart

| Layer | What IT38 did there |
|---|---|
| need→intervention search | nothing (no new target or bridge: a context contrast, an uninformative result and an occupancy reading are not gene-to-gene precedents) |
| proposal generator | `run_generation_it21.py` reads `relation_use_it38.tsv`; each row names an investigation, ONE relation of a package by its evidence id, a `use` and optional chain/hypothesis filters; the limit text is built from the relation row itself (subject, relation, object, context, status) |
| qualification of proposals | the relation travels in `carried_limits` (the existing field; H8: an unresolved premise is a carried limit, never a veto) and in a new column `relation_use` that names which relation was used and how |
| cards, investigations, ranking, dashboard | unchanged by this link (the cards were corrected separately from their packets; see `p1_reconcile_it36_20261108/STATUS_IT38.md`) |

## The three relations, by source depth (checked in `nb1_myc_20261107/output/evidence.tsv`)

| Relation (evidence id) | Source depth in the package | Status label on the proposal | Use |
|---|---|---|---|
| sign contrast, MYC gain in tissue models versus the WWOX-knockout organoid (E11, E30, E01, E02) | E11 and E30: full text of the source (chick neural tube; mouse neurosphere), overexpression, culture and stage limits stated; E01 and E02: cited by identifier from a complete read (transcript, and a fraction of SOX2+ cells). The contrast itself is the package's inference. | INFERRED (not measured) | `context_limit`: no sign is carried from those contexts to the WWOX-deficient state |
| nocodazole result in another disease's MYC-lowering model (E27) | full text of the source; the package's audit marked its first wording an overshoot (a microtubule poison, not a G1 perturbation) | UNINFORMATIVE (another disease; neither support nor refutation) | `uninformative_not_negative`, only for the `H_PROTECT` arm: the result does not test the strategy and is not evidence against it |
| MYC binding lost at early-neuron gene promoters with MYC protein high (E80) | an auditor's reading of one figure, visual estimate, **no receipt** | EXPLORATORY (auditor's reading, no receipt) | `occupancy_not_amount`: MYC amount and occupancy at target genes are kept apart; a premise to verify, not a measurement |

## Before and after (S13 committed, S14 regenerated from the same recipe; `test_stage_it38.py`)

| | S13 | S14 |
|---|---|---|
| proposals / eligible / hand-overs | 994 / 220 / 15 | 994 / 220 / 15, same ids |
| `carried_limits` changed | , | 555 rows, exactly those whose premise is INV-17 (a change of MYC); 0 elsewhere |
| `relation_use` filled | , | 555 (context limit 555, occupancy 555, uninformative 241 of which all `H_PROTECT`) |
| selection columns (status, hypothesis, chain, z, eligibility, blocker) | , | identical |

Cases: (1) sign transfer, `DOT1L -P(+)-> MYC` (H_HARM): the limit now says the MYC direction is not carried over from tissue models; the eligibility is unchanged. (2) uninformative result: an `H_PROTECT` proposal (`BRD4 -P(-)-> MYC`) carries the three limits, the uninformative one only because of its hypothesis; nothing demotes it. (3) amount versus occupancy: the E80 limit is separate from the context limit, labelled exploratory. (4) control outside MYC: `HDAC5 -T(+)-> SLC2A1` and all 439 non-INV-17 proposals: carried limits byte-identical.

Execution: the stage was regenerated end to end (engine and propose, about 6 minutes, 4 GB cap, local catalogue cache) and the table was read by `run_generation_it21.py` at run time; `test_relation_use_it38.py` also runs in a public checkout.

**One change is not from this link.** `target_named_in_legend_material` turned `yes` for 10 rows whose main target is GSK3A. The corpus that column reads (cards, unit tables, need texts) changed between S13 and S14 (the GSK3 wording of IT36 and IT37 names GSK3A). It moves no eligibility or hand-over.

## Not shown

No improvement of prediction, selection or any ranking; no claim that MYC is a driver, a marker or a consequence (INV-17 stays open); DL-MECH-179 is an exploratory lead whose premise (occupancy at early-neuron genes across the knockout, the SCAR12-class line and the corrected line) is exactly the one the E80 limit marks as unverified. A compound is not promoted by this change.

Recipe: as `../generation_it30_p5_20261105/README.md` with `--out-dir generation_it38_20261108/results_s14`.
