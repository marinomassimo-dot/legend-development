# Provisional, explainable, updatable ranking of the interventions (IT8 P9, 2026-10-29)

Non-canonical research material. Actor `scientist-a`, task `ORCH-ROADMAP-IT8-20261029`, package P9 (operator addition), worktree branch `task/it8-p9`.
**This is a research priority for VERIFICATION. It is not a validated prediction of clinical benefit, not a probability of success, not a therapeutic
recommendation and not medical advice.** No dose, preparation, route, schedule or individual recommendation is given. Association is not modulation,
modulation is not rescue. Nothing here changes the four scientific current files or the receipt ledger; the registry edits this work implies are
listed in section 9 for the batch path.

The ranking answers three questions and refuses a fourth:

1. **Which interventions deserve most further study for WWOX today, and why?** `selections.tsv`, `units.tsv`, the "Graduatoria" section of the view.
2. **Which evidence and counter-evidence support each position?** `unit_needs.tsv` (one row per intervention x need, with the card positions and the
   kind of link), the component fields of `units.tsv`, the per-unit detail in the view, and the cards themselves.
3. **Which new result could make each position rise, fall or leave the selection?** `could_rise`, `could_fall`, `could_leave` in `selections.tsv`, derived
   from the unmet criteria of the position rule and from the stored work-order statements; plus `triggers.tsv` for what makes the order be re-evaluated.
4. It does **not** answer "which one should be given to a patient": that question is outside the module and is not touched.

## 0. Files

| File | What it is |
|---|---|
| `ranking_it8.py` | the one script: `run`, `check`, `snapshot`, `diff`, `show`, `--help`; stdlib, offline, no clock, deterministic |
| `unit_map.tsv` | curated, reviewable: how the 36 cards form 27 ranked interventions and 3 excluded axes, with the reason for every merge |
| `uncarded_items.tsv` | curated, reviewable: 11 interventions identified (searched, abstained, opposed, excluded) that have no card, with source pointers |
| `units.tsv` | one row per intervention: class, depth, groups per view, the six components, access, members, merge reason |
| `unit_needs.tsv` | one row per intervention x need: position (per card, with conflicts), kind of link, opposed action, L1-L4 states |
| `unit_members.tsv` | every catalogue family (or tool compound) that belongs to an intervention, with roles, status, access, name twins not merged |
| `selections.tsv` | the general and the two per-objective selections, 15 fields per item |
| `inventory_families.tsv.gz` | **all 40,268 catalogue families** with class, depth, first-order group, need links, usable-by-method flags, unit membership |
| `deepening_queue.tsv` | the compounds to deepen first (a work queue, not a ranking of promise) |
| `triggers.tsv` | which novelties make an intervention be re-evaluated, and how each is detected |
| `unit_inputs.tsv` | per-intervention input digests (one per trigger) used by `diff` and `snapshot` |
| `ranking.json` | everything above in one document: the feed of the view |
| `snapshots/`, `changes.tsv` | dated versions of the unit table and the per-unit changes with their reason class |
| `test_ranking_it8.py` | 26 offline tests, including mutation tests |

Regenerate: `python3 -B disease-models/wwox/research/drug_repurposing/ranking_it8_p9_20261029/ranking_it8.py run` (needs `LEGEND_CATALOG_CACHE` for the
view only), then `python3 -B framework/scripts/repurposing_view.py run` and `... run --source shareable`. `check` exits 1 when a file differs from a
fresh regeneration.

## 1. What is being ranked, and how every compound stays traceable (requirement A)

**Start.** The catalogue (44,211 records, 40,268 families), the 36 cards, the coverage matrix and its 710 prioritised (family, need) pairs, the
join, the needs (22), the work order, the usable-compounds census of IT7 P2, the pharmacological comparison of IT7 P5 (9 records), the IT7 P3
result (exploratory information only) and the lead dispositions. Nothing was re-searched: the ranking reads what the module already holds.

**Unit of ranking = an intervention.** A catalogue family is a source-level unit (parent/child and identical InChIKey first block; source-only
records are never merged on name). A *ranked intervention* is what a physician or a laboratory would call the thing to study: the 36 cards form
**27 interventions** plus **3 excluded axes** (`unit_map.tsv`). Six sets of cards concern the same intervention and are counted once, so that the same
evidence cannot raise one intervention twice: gene addition (C01 and C04, endpoint families of the same dose-study experiments, two papers with a
shared senior author), dichloroacetate (E03 and I01), the ketogenic diet (E04 and EB-KD-01), vigabatrin with its sibling inactivators (EB-VGB-01 and
H02), the NMDAR/AMPAR class (F01 holds the one WWOX readout, obtained with a tool compound, and F04 the class), the read-through class (B01 and B02).
Per-need positions of each card are kept; when two cards of one intervention speak on the same need the merge never hides a counter position
(`MERGE_ORDER`: a contested or harm position stands above a weaker favourable one).

**Synonyms, salts, parents, name twins.** The catalogue family key is kept (parent link or identical InChIKey first block). Name twins are **not
merged** (ethosuximide is a ChEMBL family and a DGIdb-only family) and are listed in `unit_members.tsv` (`name_twins_not_merged`). For *display
counts only* `inventory_families.tsv.gz` carries `display_group` (case, punctuation and salt words removed; stereoisomers such as ketamine/esketamine
are NOT merged): 71 distinct display names for the 97 Q1 families. No position depends on a record or a family count: a test duplicates every member
family of every intervention and shows that no group, class or selection changes. Pharmacologically relevant formulation differences (a salt, a
prodrug, an ester) stay different families.

**Classification (exclusive; `units.tsv`, `class`):**

| Class | Rule (derived, not assigned by hand) | Count |
|---|---|---:|
| EVALUATED AND ORDERABLE | at least one linked need has a favourable position (F1, F2 or F3) after the card merge; the group says how strong | 10 |
| EVALUATED WITH WEAK PERTINENCE OR COUNTER-EVIDENCE | evaluated at card level, every position is counter-evidence (C1-C3) or a mechanism-only link (P3) | 5 |
| STILL INSUFFICIENTLY EVALUATED | every card is an abstention or names no step: a datum is missing before any test can be designed; **never placed at the bottom**, group GU lists the unit apart with the missing datum | 12 |
| EXCLUDED FROM A SPECIFIC COMPARISON WITH REASON | an endpoint axis with no candidate (developmental benefit, growth, pharmacodynamic anchor): not an intervention, nothing to order | 3 |

Interventions are also excluded from *specific comparisons* with the reason the module already states (`excluded_from_comparisons`, the IT7 P5
reasons: firewalled from the method comparison, not a compound question, outside the question asked). Gene addition, the diet, the oligonucleotide
and the magnesium ion are therefore ranked but have no place in a comparison of compounds by network or signature. **Eleven further interventions
have no card** (`uncarded_items.tsv`): seven nutrients searched and abstained (thiamine/lipoate/carnitine, NAD+ precursors, pyridoxine, omega-3,
vitamin D, taurine, creatine; title/abstract engines only), the NMDA-receptor agonists glycine and aspartic acid kept as a potentially OPPOSED effect,
adenosine and regadenoson excluded after the identity repair, pannexin-1 blockers (no catalogue compound), GCN2 modulators (genetic suppression in a
fly is not pharmacology). Each has a class, a depth and what would reopen it. A search that abstains has not shown the item unpromising.

**The broad catalogue** (`inventory_families.tsv.gz`, 40,268 families): every family is STILL INSUFFICIENTLY EVALUATED unless it belongs to a ranked
intervention (16 families do) or has an unresolved identity. A compound present only in a database has no WWOX rationale by default. First ordering uses
existing annotations only, with the depth declared:

| First-order group | Meaning | Families |
|---|---|---:|
| Q1 (E1c) | target listed with a **direction-consistent** documented action on a direction-evaluable need | 97 |
| Q2 (E1) | target listed on a need of uncertain direction or with an unresolved action (exploration list only) | 1,117 |
| Q3 (E1p) | pathway-member link only (counted apart) | 250 |
| Q4 (E0a) | documented target action, no need of the module | 14,411 |
| Q5 (E0) | database record only | 24,377 |
| UNIT (E3) | member of an already ordered intervention | 16 |

Q-groups are **not a ranking of promise**: they say how much of the module's own evidence a family already touches. The usable-by-method flags
(M-net 13,379 families; M-sig neural 931) are carried as columns and are *readiness for a computational follow-up*, not biology. Access categories of
the need-linked families (overlapping): prescription 42, OTC 3, supplement 16, experimental 173, unknown/unverified 1,339. The **deepening queue**
(34 compounds, `deepening_queue.tsv`) lists Q1 compounds on a need that has WWOX-system observations, with an approved status or a known access
category and no opposed action: they are siblings of the NMDAR/AMPAR class (20) or of the T-type calcium pair ethosuximide and apinocaltamide (13), plus
one on the seizure need; deepened, they would join an existing intervention, not create a new position. **No catalogue family outside the 27 is in a
selection**: that is a statement about depth of evaluation, not about the compounds.

**Depth of evaluation (declared for every item):** E4 card with WWOX-side assertions read beyond the abstract; E3 card with assertions; E2 card that
is an abstention; E1c/E1/E1p/E0a/E0 catalogue only, from most to least linked to the needs. A class-level pharmacology table (IT7 P5) is noted
beside the depth, not folded into it.

## 2. Method (requirements B and C): reuse, no score

The F/C/P position of every (card, need) pair is the existing rule (`priority_rules_it5_20261029.md`; re-derive with `repurposing_view.py positions`).
This work adds three small things and nothing else: the merge of cards into interventions, an objective-specific *group* built on the positions, and a
selection rule. No weight, no numeric score, no percentage read as a probability.

**Objectives.** Two views plus a general one. A need belongs to an objective by its own `goal` in the needs file (deep recovery: 5 needs;
partial benefit: 17). An intervention appears in the *broad, durable functional recovery* view if its card declares that objective or any of its linked
needs has that goal; the same for *partial or bridge benefit*. Its group in a view uses only the positions on that objective's needs, so a strong
symptom result does not erase interest in a broader-recovery hypothesis and vice versa: **gene addition is G1 for broad recovery and G3 for the
partial/bridge view** (its growth and glycaemia endpoints are contested). A declared objective with no linked need position is GU, not a verdict. The
general view takes the better of the two groups of an intervention and prints both. **Track A/B (variant or lesion dependence) is a separate field**
(`tracks`, filter "Track"): depth of benefit and genetic applicability are different dimensions and are never folded into the group.

**Groups (ordinal; within a group the order is alphabetical and means nothing: ties).** The lead position of an intervention in a view is the best
of its need positions in this order: F1, F2, C2, C1, F3, C3, P3, P2, P1 (a measured WWOX-system result, even contested, outranks a target hypothesis;
a target hypothesis outranks a mere counter-signal from outside WWOX).

| Group | Lead | Plain statement |
|---|---|---|
| G1 | F1 | favourable, read against an untreated same-genotype comparator, full or partial text, unflagged, no null/unfavourable/mixed WWOX-system row beside it; a reading-quality screen, not a size of effect |
| G2a | F2 | favourable WWOX-system readout with reading or design limits only (uncontrolled, graphical, one experiment), no null beside it |
| G2b | F2 + specificity flag | as G2a and the effect also occurs in wild type (`nonspecific_also_in_wild_type`) or comes from a tool compound |
| G3 | C2, C1 | WWOX-system results favourable and null/unfavourable side by side, or only null: the study is to learn which holds |
| G4a | F3 + coherent action | no test of the intervention in WWOX; favourable support outside; the need has WWOX observations; a documented catalogue action coherent with the need's direction |
| G4b | F3 | as G4a with no documented coherent action (uncertain-direction need, unresolved action, or no catalogue identity) |
| G5 | C3, P3 | harm or null signal outside WWOX with nothing favourable beside it, or a mechanism-only link |
| GU | P1, P2, or no position on the objective | premise missing: an abstention. **Not a finding that the intervention is unpromising** |

A lead of F plus a C position on another need of the same objective is flagged `contested` (the counter-evidence stays on the page and in the table;
it does not move the group, because the group describes the lead need). Linking more needs never raises a group (tested). The components below are
*displayed* with every item; the group is a function of the positions and of two flags, and `check` fails if a stored group differs from the rule.

**Components** (the dimensions the module already uses, clarified; none is weighted):

| Component | Field | What it shows |
|---|---|---|
| WWOX evidence | `W_wwox_evidence` | WWOX-system and case-report assertions with their signs, reading depth, L4 technical comparisons, replication (distinct papers; independence of the groups is **not** established by a count) |
| Mechanistic coherence | `M_mechanism` | catalogue families, L2 states over the (family, need) cells, opposed needs; modality and no-identity cases say "not evaluable here" (UNKNOWN, not zero) |
| Transferability | `T_transferability` | track, species and genotype of the WWOX-side assertions, the cards' stated transfer limits and window notes |
| Pharmacology | `P_pharmacology` | the IT7 P5 class table where it exists (potency with assay context, human exposure, brain penetration) and always "potency in a WWOX system UNKNOWN"; the IT8 P3 qualification of nine cases (`pharmacological_qualification_it8_p3_20261029/comparison.tsv`, read when present: measures by assay type, never aggregated, with exposure, nervous-system data and contrary/unknown signals) is shown beside it for the ten interventions it covers; **IT7 P3/P2 information is carried as exploratory information only and never moves a position** |
| Counter-evidence | `X_counter_evidence` | WWOX-system null/harm/mixed assertions, outside-WWOX null/harm assertions, need-level counter items (items of the need record, not of the intervention), opposed-action needs |
| Uncertainty | `U_uncertainty` | of N linked needs: measured / hypothesised / mechanism-only / premise missing; plus the always-unknown items |

**Feasibility of the next experiment is separate** from biological promise: it is carried in the item's `next` fields (the work-order kind and its
stated feasibility), never in the group. **Access** (prescription, OTC, supplement, experimental) is descriptive listing evidence with source,
jurisdiction and date (openFDA NDC identifier match; NIH DSLD name-only match; ChEMBL status statement); it says nothing about efficacy, safety or
availability.

**Source independence.** An assertion is counted once however many records cite it (preprint, publication, database row, citing paper). The two AAV9
cards are one intervention. Distinct-paper counts are shown, and the text says that they do not establish independence of the groups.

## 3. Selections (requirement E)

A selection lists at most ten interventions from G1, G2a, G2b, G3 and G4a, **only when the evaluation supports them; never padded**; ties stay whole.
G4b, G5 and GU are listed *apart* with their group and objective (they are not "at the bottom"). Current state (data of 2026-10-29, rules R1):

| View | Items | Detail |
|---|---:|---|
| General | 8 | AAV9 gene addition (G1, broad); ethosuximide (G2a); lithium, NMDAR/AMPAR class (G2b); A51, ketogenic diet, vigabatrin and GABA-AT inactivators (G3); apinocaltamide (G4a) |
| Broad, durable functional recovery | 1 | AAV9 gene addition (G1). The next in line, **not selected**, are the 4-phenylbutyrate/bile-acid chaperone class and the proteasome-inhibitor class (G4b, Track B hypotheses whose decisive premise, where the missense protein is lost, is missing); the oligonucleotide, CRISPRa, pharmacological and ER-proteostasis chaperones, HSP70 axis, Wnt-lowering agents and the amlexanox/read-through class are GU or G5 |
| Partial or bridge benefit | 8 | ethosuximide (G2a); lithium, NMDAR/AMPAR class (G2b); A51, gene addition (growth/glycaemia endpoints), ketogenic diet, vigabatrin (G3); apinocaltamide (G4a). Apart: ISR modulators, LDH inhibition, dichloroacetate (G4b), magnesium (G5) and seven GU |

Each item carries compound, access category, context, objective and applicability (track), group, main reason, best relevant evidence and main limit,
needs and pathways, next experiment or useful control, what could change its position (rise / fall / leave), sources, date and depth
(`selections.tsv`; in the view the same fields, in Italian field labels, scientific text as stored).

**The questions that could change the top positions** (full statements per item in `could_rise` / `could_fall` / `could_leave`):

* **Gene addition (G1, broad):** the day-of-injection baseline and a treated-after-onset arm with a same-age untreated comparator (every mouse endpoint is
  prevention or early window); an intermediate vector level (threshold versus gradient); quantified myelination; a replication outside the source
  laboratory. A null on the growth or glycaemia endpoints is already counted (G3 in the partial view). Track A in design; missense lesions with
  residual function unmeasured.
* **Ethosuximide (G2a):** a drug-by-genotype test and a second experiment; a T-type measurement in the model (none exists); the discriminating compound
  apinocaltamide on the same need.
* **Lithium (G2b):** a drug-by-genotype interaction (the effect is also present in wild type and heterozygote); it rises only if specificity appears.
* **NMDAR/AMPAR class (G2b):** the isolated NMDAR current in the knockout (the discriminator between NMDAR gain, permissive necessity and AMPAR-led
  drive) and a pore blocker as a translation probe with Mg2+ and holding potential stated; the one readout is a tool compound (d-APV).
* **A51, ketogenic diet, vigabatrin (G3):** whether the null rows (same-organoid null, case-report nulls) are real; a controlled readout would lift them.
* **Apinocaltamide (G4a):** its first WWOX-system readout against an untreated comparator.

## 4. Pathways and needs (requirement D)

For each intervention and each linked need the table `unit_needs.tsv` states **which kind of link** it is, in this order of strength: *effect observed in
the relevant system* / *documented action directionally compatible with the need* / *documented association (target listed)* / *other-disease precedent
only* / *card inference by mechanism, no catalogue row*. A **computational prediction** is "none" everywhere: the IT7 P3 comparison excluded the carded
families on purpose, was exploratory, did not detect its effect and cannot drive a position. Opposed actions are flagged per need (`opposed_action`) and
the opposed-direction catalogue compounds without a card are in `uncarded_items.tsv` (glycine and aspartic acid). Overlaps are shown as "needs shared with
other interventions" in the view. Every count carries its denominator ("k of 22 needs linked"), is a count of links, not a share of the disease
treated, and does not raise a group. Uncertain links stay "uncertain" (12 of the 22 needs have an uncertain direction, so the sign of a favourable
intervention is not known there).

## 5. Evolution (requirement F)

* **Versions.** `ranking_it8.py snapshot --reason CLASS` writes `snapshots/units_<date>_<digest>.json|tsv` (the group per view and the input digests of
  each intervention) and appends one row per change to `changes.tsv`. It does nothing when nothing changed (idempotent). A group that moved needs a
  reason class: `new_evidence`, `counter_evidence`, `identity_correction`, `better_pharmacological_qualification`, `context_change`, `method_revision`.
  **Entry of a new compound (`new_entry`) and resolution of a tie (`tie_resolution`) are recorded as such and are never counted as a change of
  assessment.**
* **What triggers a re-evaluation** (`triggers.tsv`, `ranking_it8.py diff`): T1 a card or packet of the intervention changes; T2 a pertinence row is
  added or changed; T3 a new fulltext read receipt on a PMID the intervention cites (read-only count from the ledger: the digest raises a flag, a reader
  decides); T4 a need observation, counter item, direction or work-order statement of a linked need changes; T5 the pharmacological comparison row
  changes (P3 qualification); T6 the catalogue families, cells or L2/L3 states of the intervention change; T7 the rules change (`RULES_VERSION`); T8 the
  existing daily radar reports a changed source, after which `repurposing_coverage.py run` and `ranking_it8.py run` are run. `diff` prints, for each
  moved intervention, the inputs that changed and the suggested reason class.
* **Demonstrated on this data.** Snapshot 1 (rules R1) enters the 30 entries as `new_entry`. After the IT8 P3 qualification was read, `diff` reported
  10 interventions with changed pharmacology input (T5) and no group moved; snapshot 2 records them as `input_change_without_order_change` with reason
  class `better_pharmacological_qualification` (P3 itself states that no F/C/P position changed). Only the P3 comparison table is read from that branch;
  its card and work-order edits reach this ranking when the branch is integrated: re-running `run`, `diff` then shows T1/T4 changes and the groups are
  re-derived.
* **No new information, no change.** `check` regenerates in memory and compares byte by byte; the tests assert it. There is no scheduler, no agent
  role and no gate: the daily scout already exists, and a person runs the three commands (coverage, ranking, view) after a trigger.
* **Link to the view.** The view reads `ranking.json`, validates it against the cards and needs at build time (an inconsistency is a build error) and
  shows the as-of date, the rules version, the order digest and the snapshot history.

## 6. Integration and verification (requirement G)

The view has a new section "Graduatoria" (nav entry, route `#ranking`): a Italian orientation text, the group legend, filters (view, class, group,
track, need/pathway, access category, quality of the WWOX evidence, free text), the selection of the chosen view, the **full list** of all 30 entries
with a collapsible component/pathway detail for each, the inventory with denominators, the uncarded interventions, the evolution block and the
triggers. Export: TSV of the visible rows and JSON of the whole list (client-side, no network). Print: `#section=rankingprint` is the **one-page
A4** synthesis (the three selections), `#section=ranking` prints the whole section. The shareable build (`--source shareable`) embeds no catalogue
member name, no status class, no potency or exposure text and only class-A access statements per compound; the other access categories survive as
counts; catalogue-only uncarded items have their names withheld. `repurposing_shareable_audit.py` has rules for the new subtree.

Checks run (all green at the last commit): `test_ranking_it8.py` (26), `test_repurposing_view.py`, `test_repurposing_coverage.py`,
`test_repurposing_join.py`, `repurposing_view.py check`, `repurposing_view.py audit-shareable` (and `--dynamic` where Chromium exists),
`check_cards.py`, `check_needs.py`, the three release tests, the closed-world guard, `scripts/test_tool_routing.py`, `scripts/public_release_gate.py`.
Mutation tests: a damaged position moves the group; a damaged flag moves G2a to G2b; a damaged F1 moves G1 to G2a; a damaged pertinence sign changes
exactly that intervention's input digest; an unmapped or doubly mapped card is refused; a duplicated family changes nothing.

## 7. Declared coverage

* **Selectable (G1-G4a): 8 interventions** (5 of class EVALUATED AND ORDERABLE: gene addition, ethosuximide, lithium, the NMDAR/AMPAR class,
  apinocaltamide; 3 of class WEAK PERTINENCE OR COUNTER-EVIDENCE but in G3: A51, the ketogenic diet, vigabatrin with its sibling inactivators). **Ordered
  but not selected (G4b/G5): 7** (the 4-phenylbutyrate class, proteasome inhibitors, ISR modulators, LDH inhibition, dichloroacetate; magnesium and
  the amlexanox/read-through class). **Still insufficiently evaluated (GU): 12.** **Excluded: 3 axes.** Total 27 + 3. **Catalogue families not in any
  intervention: 40,252**, all insufficiently evaluated, 1,464 of them need-linked (Q1-Q3).
* **What the data do not support:** a broad-recovery list longer than one intervention (no WWOX-system result exists for any other broad-recovery
  intervention; the nearest are Track B hypotheses whose decisive premise is missing); any statement about which intervention a given patient
  should receive; any comparison by potency (no card has potency in a WWOX system); any role for the IT7 P3 result.
* **Still to qualify** (the reason each is in a group other than the selection): 12 abstentions (a datum is missing), the 7 G4b/G5 interventions, 11
  uncarded interventions, and the 97 Q1 families (the deepening queue).

## 8. Limits and UNVERIFIED

* The group rule is mine and is stated here; the positions it reads are the module's own and were independently reviewed in IT6 (P2 review). The
  specificity split (G2a/G2b) reads two flags (`nonspecific_also_in_wild_type`, `tool_compound*`) from the pertinence table; other specificity limits
  (for example a multi-kinase compound) do not move a group.
* The G4a/G4b split reads the coverage cells: it is as good as the catalogue's action statements (class-B/C sources, stale DGIdb export, no potency).
* Counts of PMIDs and receipts are counts of identifiers, not independence.
* The T3 trigger counts receipts per cited PMID; it does not know whether a receipt concerns the claim the ranking rests on.
* The pharmacological table (IT7 P5) has potency values with assay contexts that were not re-verified here; they are displayed, not used.
* UNVERIFIED by this work: the scientific premises of the top positions at the sources are left to the independent verifier; this work re-derives
  them from the module's cards and pertinence rows, not from the papers.

## 9. Registry and ledger items for the batch path (not edited here)

None of the four current files is changed. If the Orchestrator decides to record this work: a commit candidate noting the ranking as a non-canonical
research record (rules R1, 27 interventions, selections), and, only if the verifier confirms them, the G1/G2 premises as `CLAIM` updates through
`BATCH_COMMIT`. No receipt is needed for this work (no source was newly read).
