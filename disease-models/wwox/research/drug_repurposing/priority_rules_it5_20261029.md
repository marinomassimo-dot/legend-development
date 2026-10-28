# Research-priority positions: revised rules (IT5 P11, 2026-10-29)

Scope: the physician view (`framework/scripts/repurposing_view.py`, `view/assets/curated.*`). No score, no probability, no new framework.
The old rule (groups G1 to G4) was the builder's own and unverified. It ranked by proximity of evidence and gave a card the best group seen in any of its needs. Both are dropped.

Re-derive everything with `python3 -B framework/scripts/repurposing_view.py positions` (one TSV line per card x need: WWOX result, depth class, position, criteria not met). The rule is one function, `assign_need_position()`, fed by `classify_rows()`; both have their own tests in `test_repurposing_view.py`.

## 1. What a position is

One position per card AND per need. A position names the REASON a next study is interesting, in three visibly different families (different label, colour, border, `kind` field):

| id | family | label | reason |
|---|---|---|---|
| F1 | favourable hypothesis | controlled WWOX readout | favourable WWOX-system result, controlled, deep enough, unflagged, no null/unfavourable/mixed WWOX-system row beside it (outside-WWOX rows are NOT part of this test; they appear as a tag) |
| F2 | favourable hypothesis | thin WWOX readout | favourable WWOX-system result, but uncontrolled, depth-limited or flagged; study to learn whether the signal is real |
| F3 | favourable hypothesis | from the target, intervention not tested in WWOX | no WWOX-system result; favourable support exists outside WWOX and the need has WWOX-system observations |
| C1 | counter-evidence to clarify | null or unfavourable WWOX result | the only signed WWOX-system result is null or harmful; study to learn whether it is real |
| C2 | counter-evidence to clarify | mixed WWOX result | favourable and null/unfavourable/mixed WWOX results stand side by side; study to learn which holds |
| C3 | counter-evidence to clarify | harm or null signal from outside WWOX | no signed WWOX result; what exists outside WWOX is harm or null with no favourable signal |
| P1 | premise missing | abstention | the card names the missing datum instead of a test |
| P2 | premise missing | no next step named | nothing to put forward |
| P3 | premise missing | nothing favourable recorded for this intervention on this need, or no WWOX observation on the need | the card links the need by mechanism only |

The order of the list is a grouping by kind of reason, not a ranking. Inside a position: alphabetical, meaningless. Nothing is added across positions.

## 2. The rule (first match wins), in plain words

Inputs per card x need are the pertinence rows (`coverage/assertion_pertinence.tsv`: evidence kind, sign, comparator, flags), the reading depth of the assertion in the card, the card's abstention and next step, and whether the need has a WWOX-system observation.

1. Card is an abstention: **P1**. 2. No next step named: **P2**.
3. WWOX-side rows = readout in a WWOX system, WWOX clinical case report, genotype comparison vs wild type. A row flagged `not_a_recovery_comparison` (wild-type-only comparison) is listed and counts neither way. Signs: favourable = benefit, partial benefit, normalised vs wild type; null; unfavourable = harm; mixed. "Not normalised vs wild type" (a low-dose arm) is listed but counts neither way; unresolved/unquantified are listed, not counted.
   - favourable only: **F1** if one and the same favourable readout in a WWOX system has an untreated same-genotype comparator (or before/after washout), a full or partial text reading, and none of the weakening flags (tool compound, reading depth unknown/queried, nonspecific also in wild type, graphical reading, one experiment, case level, micrographs only, partial read, no instrument, no knockout arm, abstract only); otherwise **F2**.
   - null or unfavourable only: **C1**. Any favourable (or "mixed") together with a null, unfavourable or mixed row: **C2**. A favourable result never hides a null one.
4. No signed WWOX-side row: outside-WWOX rows (other disease, safety, label) with harm/null and no favourable other-disease readout: **C3**. Else **F3** if favourable support is recorded on this need (other-disease readout or target-engagement benefit) and the need has a WWOX-system observation; else **P3**.

Every position prints on the page which of these criteria are met and which are not ("Criteria" line, plus the six or seven facts behind it: result in WWOX, depth and quality with comparators and row flags, outside WWOX, counter-evidence, decisive premise, next step, feasibility). Feasibility is shown and never assumed ("not known" when no access evidence was obtained) and is not used to place a card; the rule does not judge what a next step would reveal, it shows the step so the reader can.

## 3. Global presentation

There is no global position. The card profile lists one position per need; the overview chip row and the card list show the SET of need-level positions (`positions` field, e.g. `F1 + C2`); the "to study next" panels list `card (need)` entries under each position. Tiles count card-need links, never cards. The old `group` field on a card is gone; `links[need].group` now holds the position id.

## 4. Representative cases (from the cards; old = the G1..G4 rule it replaces)

Result = sign of the WWOX-side rows; depth = firm / limited (WWOX rows present but not firm) / none.

| case | need | result in WWOX | depth | position | reason | old |
|---|---|---|---|---|---|---|
| C01 AAV9 | gene addition | favourable (1 row, high dose, n=5) | controlled (untreated same genotype, full text) | F1 | carried by DR-C01-001 alone (spike-wave discharges, one high-dose arm, n=5); flags high_dose_only, n=5 printed | G1 |
| C04 AAV9 families | gene addition | favourable (5 counted; 2 wild-type-only rows neither way) | controlled | F1 | carried by DR-AAV-GFAP-P5HD only (GFAP cells, high dose, vs untreated same genotype); survival and motor rows have no stated comparator. Qualifier tag: beside the not-normalised low-dose arm DR-AAV-GFAPAREA-LD | G1 |
| C04 AAV9 families | systemic glycaemia/growth | mixed (2 fav, 2 null, 1 mixed) | limited | C2 | glucose endpoints null in both doses beside body-weight benefit | G1 |
| D01 A51 | MYC / progenitor | null (the normalised-vs-WT row DR-D01-001 is flagged not a recovery comparison and counts neither way) | limited (reading depth UNKNOWN) | C1 | the only real signed result is the null DR-D01-002 | G1 |
| D01 A51 | Wnt/beta-catenin | none | none | P3 | no row of A51 on this need | G3 |
| EB-ETX-01 ethosuximide | seizure control; T-type calcium | favourable (1 experiment, graphical) | limited | F2 | controlled, but one experiment, graphical reading, late phase; also an outside harm row (progenitor viability, in vitro) | G1 |
| G01 lithium | seizure control | favourable (1 row) | limited | F2 | flag "nonspecific also in wild type"; two further rows are drug effects in wild-type arms and do not count | G1 |
| G01 lithium | GSK3beta de-repression | none | none | P3 | no assertion on this need (target pharmacology is not recorded as an assertion) | G3 |
| EB-KD-01 ketogenic diet | seizure control | favourable (1 case report, no instrument) | limited (uncontrolled case) | F2 | partial read, uncontrolled | G2 |
| EB-KD-01 | pyruvate entry | none | none | P3 | nothing recorded | G3 |
| EB-VGB-01 vigabatrin | seizure control | mixed (2 benefit, 1 partial, 3 null in WWOX case reports) | limited (queried, not full read) | C2 | reported nulls stand beside reported benefits; outside rows add a brain-MRI harm signal | G2 |
| H01 apinocaltamide | T-type calcium (ETX sensitivity) | none | none | F3 | other-disease benefit (GAERS rat, abstract only) beside a null; no WWOX readout | G3 |
| H01 | seizure control | none | none | P3 | no row on this need | G3 |
| H02 GABA-AT inactivator | hypomyelination | none | none | C3 | seven harm rows (rat/dog toxicology, label, WWOX case-level) and no favourable signal; study = does it apply | G3 |
| H02 | seizure control | none | none | F3 | two other-disease benefits (n=1, concurrent vigabatrin) | G3 |
| A01 PBA class | misfolded-protein rescue | none | none | F3 | other-disease: 3 benefit, 2 null, class level | G3 |
| B02 readthrough class | PTC read-through | none | none | P1 | abstention; missing datum named | G4 |
| E02 LDH inhibition | lactate/LDH | none | none | F3 | target-engagement and tool-compound assays only, fly model | G3 |
| E03 PDK inhibition (DCA) | PDH/pyruvate axis | none | none | F3 | enzyme assays and tool compounds | G3 |
| F01 glutamate node | excitatory gain | favourable (d-APV, before/after washout) | limited (flag tool_compound) | F2 | tool compound, not a candidate drug: tagged; outside rows include null and harm: tagged | G1 |

Totals before the fix over the 43 card-need links (old -> new): G1 8 -> F1 3 (C01, C04 and, before the fix, F01), F2 3, C2 2 (before the fix; after: F01 F2, D01 MYC C1); G2 2 -> F2 1, C2 1; G3 16 -> F3 7, P3 8, C3 1; G4 17 -> P1 16, P3 1.

## 5. Where old and new disagree, and why the new one is right

| case | old | new | why |
|---|---|---|---|
| D01 A51, MYC | G1 ("intervention read out in a WWOX system") | C1 | the only readout with an untreated same-genotype comparator is null and depth UNKNOWN; the favourable row compares with wild type only and is flagged not a recovery comparison, so it counts neither way. Proximity of evidence is not a favourable result. The study of interest is whether the null is real. |
| C04 AAV9 families | G1 for the whole card (best of needs) | F1 for gene addition, C2 for glycaemia/growth | the card's glucose endpoints are null in both doses; best-of-needs hid them. |
| EB-VGB-01 | G2 (best of G2/G3/G3) | C2 on seizures; P3 on two needs | the case reports include three nulls; "case reports" is not "favourable". Hypomyelination and inhibitory drive have no vigabatrin assertion at all. |
| G01 lithium, ETX | G1 (same as C01) | F2 | a single graphical or nonspecific (also in wild type) experiment is not the same footing as a controlled, deep, unflagged one. |
| H02 | G3 (all needs) | F3 / C3 / P3 | hypomyelination has seven harm rows and no benefit; filing it with "target altered, not yet tested" with the seizure need hid that the reason to study it is a safety question. |
| G01 GSK3, EB-KD-01 pyruvate, D01 Wnt, H01 seizure | G3 | P3 | no assertion of the intervention on the need: nothing favourable is recorded. G3 implied a hypothesis the card does not state. |
| EB-KD-01 seizure | G2 (below G1) | F2 | the order G1 above G2 is dropped; uncontrolled and thin are the same F2 reason. |

## 6. Limits

- Signs and flags come from `assertion_pertinence.tsv` as it stands; a wrong sign there propagates. P4 (identity) and P8/P9 (new cards) are not in this branch; positions will move when their rows land, by rule, not by hand.
- "Firm" is a reading-quality screen (comparator, depth, flags). It is not a verdict on effect size or benefit; tool compounds are only recognised through the pertinence flag `tool_compound` (capped at F2 and tagged).
- The information a next step would give, and its feasibility, are shown (card text, access evidence) but not scored; most cards have no access evidence, so feasibility is mostly "not known".
- Catalogue-stated target actions do not enter the rule (sparse, source statements, identities under reconciliation).
- Alpha order inside a position and the grouped listing order carry no meaning.

## 7. Verification fixes (p11fix)

After the independent verification of 12affd39: (1) `tool_compound` is a weakening flag (F01 d-APV: F1 -> F2) and the position carries the tag "tool compound, not a candidate drug"; (2) F positions carry a tag with the number of counter-evidence rows outside WWOX (H01 T-type, A01, E01, ETX T-type, F01), and the F1 definition says its "no counter-result" test covers WWOX-system rows only; (3) a wild-type-only comparison row flagged `not_a_recovery_comparison` counts neither way and is tagged (D01 MYC C2 -> C1; C04 glycaemia stays C2 on benefit, mixed and two null rows); (4) F1 is renamed "controlled WWOX readout" and the page names the carrying row ("carried by ..."); (5) the F1 criterion is split into comparator / text reading / no weakening flag (flags found are named) / one readout meeting all three, so an F2 shows which part failed. A F1 beside a "not normalised vs wild type" arm shows that arm as a tag (C04 gene addition: DR-AAV-GFAPAREA-LD). Result after the fix: F1 = C01, C04 gene addition; F01 is F2; D01 MYC is C1.
