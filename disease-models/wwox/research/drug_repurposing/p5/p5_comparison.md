# P5 — two comparisons, visible dimensions, no score

> Actor `scientist-a`, task `REPURP-10H-P5-A-20261022`, 2026-10-22. Non-canonical research record.
> **Nothing here is medical advice**; it supports a discussion with a treating clinical team and never
> substitutes for one. Public, disease-level. No score, ordinal rank, probability, weighted or blended
> index, dose, route, schedule or paediatric suitability appears. Every adjacent source is **NOT WWOX
> EVIDENCE**. No paper was read for this task and no receipt exists or is staged.
>
> **Status of everything below that is not a verbatim cell: reader's derivation by one actor, UNAUDITED
> and OWED a blind audit by someone else** (the origin counts, the comparability calls, the
> staleness flags, the reading of the lookup). The cells themselves are verbatim pieces of the stored
> cards (`p5_check.py` proves it); the cards are themselves unaudited after repair (8 of 9 early and 8 of 12 deep
> carried a defect at the first blind audit, the repairs are not re-audited), so **each cell is a claim to
> be read against its packet, not a fact**.

Files: per-row cells [`tables_deep.md`](tables_deep.md) · [`tables_early.md`](tables_early.md) (machine form
[`cells.json`](cells.json)) · where a cell carries content [`matrix.md`](matrix.md) · the plain lookup
[`lookup_summary.json`](lookup_summary.json).

## 0 · Rules used (DEFAULTS, stated so they can be contested)

1. **Columns are the dimensions the cards actually carry**: benefit (the ONE endpoint; symptomatic versus
   modifying, as the card's own `expected_contribution`), evidence (state; functional evidence), risk (class level, as the card
   carries it), BLOCK-1 status, time to ACCESS, time to BENEFIT (two columns, never merged), feasibility
   (the card's `next_measurement`/`next_measure`). *Shared origin* is not a card field: it is computed below as a reader's derivation.
2. **UNKNOWN is never zero and never favourable**, and a cell holding a harm or a negative is "carries a value", not "bad".
   BLOCK-1: no card except the A51 card carries a BLOCK-1 statement, so every other row reads UNKNOWN there. **UNKNOWN is not a pass.**
3. **Comparability gate.** Two candidates are comparable only if they pursue the **same endpoint in the same genotype class**.
   Otherwise they are *incomparable* and no order is forced, in either direction.
4. **Dominance.** X dominates Y iff they are comparable and, on every dimension where *both* cells are evaluable, X is
   at least as good, and on at least one clearly better. An UNKNOWN cell takes no part (it is not a point for X
   and not a point against Y).
5. **Abstentions are rows, not candidates.** They have no evaluable benefit, evidence or risk cell, so they can neither dominate nor be
   dominated; "non-dominated" would be vacuously true of them and misleading, so it is **not** said of them. They stay in the
   tables with the missing datum and the measurement that would end them.
6. **"Non-dominated" is not "worth pursuing".** It only says no comparable candidate is clearly better on the evaluable cells.

## 1 · RECUPERO_PROFONDO (12 rows: 5 candidates, 7 abstentions)

Cells: [`tables_deep.md`](tables_deep.md). Compressed reading of what each candidate row's *endpoint* is (verbatim cells are in the table):

| Row | Endpoint family (genotype class) | Class of benefit the card allows | Evidence the card allows |
|---|---|---|---|
| P4-A-01 4-PBA / bile-acid class | recovered soluble functional protein (Q230P-class missense) | function recovery only; "compensation, symptom and protection are not claimed" | state: inconclusive, rationale withdrawn not refuted; adjacent proteins only (no WWOX test) |
| P4-A-02 proteasome-inhibitor class | recovered Q230P protein from an undetectable baseline (same class) | recovery only if lost at the proteasome | "not verified for this disease"; its own closest precedent carries a toxicity-bounded window |
| P4-B-01 amlexanox | full-length protein from a premature-stop allele (PTC alleles only) | none stated for the missense class | not verified for WWOX; one independent comparator-controlled negative on phenotypic rescue elsewhere |
| P4-C-01 AAV9-WWOX | spike-wave discharge rate (Wwox-null mouse) | recovery of function by replacement; nothing stated for clinical benefit | the only measured rescue in the corpus, WWOX-direct, one laboratory, unreplicated, transfer to missense not established |
| P4-D-01 A51 | cortical neurogenesis in a knockout organoid | compensation of a downstream signal, "not recovery of WWOX function" | split: progenitor identity moved, layer-neuron production did not; one organoid experiment, receipt None |

Time to access / time to benefit: UNKNOWN on all five (C01 carries two separate facts beside its UNKNOWN: a gene-therapy programme recorded at grant level
and no registered WOREE interventional study on that registry on that date, with the census's own caution; and, in the null mouse only, the interval in which the discharge effect was recorded).
Feasibility is the measurement each card names (verbatim in the table).

**A51 exposure statement: card field superseded.** The D01 card's own pharmacokinetic sentence ("very few measurements at two levels … supports neither
dose proportionality nor its absence") has been overtaken by scientist-c's later recomputation, entry 21 of the 40665325 reading (commit `c9aff6a2`), **UNAUDITED**: the
later-day exposure measure is about proportional over the middle of the range and looks supralinear at the bottom only because of one patient; the first-day measure is above
proportional over the same middle range; across the top two cohorts a two-fold step gives a 1.27-fold rise; N per cohort 1, 1, 3, 3, 3, 8, 5; CVs 4.1 to 79 percent; one first-day cell blank. So "dose-proportional"
is reproduced neither exactly nor in one direction. The packet stored on `main` at `edc1299d`, which this table reads, still carries the older sentence (the coordinator's relay says the 1.27 wording was
added earlier; it is not in the stored packet, so it lives on a branch or is not yet landed). Marked in the A51 block of the table as "card field superseded by a later unaudited
recomputation, see 40665325 entry 21". The card needs a one-line packet update, to be made by its author (gap G5 below).

### 1.1 Evidence counted by origin (reader's derivation, UNAUDITED)

| Origin | Rows that rest on it | Counts as |
|---|---|---|
| The single Q230P protein measurement behind CLAIM 019 (PAPER 041: one single-laboratory study, one patient fibroblast line, "transcript comparable, protein not detected") | the disease assertion of A01, A02, A03, A04, A05, B01, C03 (seven of twelve rows, byte-identical `disease_assertion.source`) | **ONE** premise, not seven |
| Intervention side of A01 | five R1 readings, of which the rescue-with-function precedent is two papers of one target family (the card's own words) | one target family for the rescue; non-rescues and the wild-type rise are additional readings, not replications |
| Intervention side of A02 | four readings; the card puts the two library studies in one assertion and the card's own text names two ASPA sources | one recessive-missense iPSC precedent (no replication recorded), two library readings in one assertion, one non-rescue |
| B01 | the originating NMD-screen paper and one independent Fanconi-anaemia head-to-head | two origins that disagree on the NMD arm; neither is WWOX |
| C01 | "two mouse papers, one laboratory"; `DR-C01-001` is "same study, same panel" as CLAIM 011 | **ONE** origin; support is intra-study |
| D01 | one organoid experiment, one laboratory, `DL-THER-089`; assertions carry receipt `None` and depth UNKNOWN | **ONE** origin, and the one least verifiable from the card (the card says its panel values cannot be re-audited) |
| D02 | organoid differential-expression tables read cell-wise | one origin; the lithium experiment named in its `not_known` is the Cheng 2020 experiment also used by the early ETX card |

### 1.2 Pair by pair (10 pairs among the five candidates)

| Pair | Comparable? | Relation on evaluable cells |
|---|---|---|
| A01 – A02 | **yes** (same endpoint family, same genotype class) | **Undecided; neither dominates.** Benefit equal. Evidence not orderable: A01 has an allele-specific rescue with protein and function read together in one adjacent protein, against a wild-type rise and a non-rescue; A02's precedent matches the "normal mRNA, protein absent" premise best but returns only a fraction, with a window toxic to controls. Risk: A02 carries an observed class-level bound, A01 carries UNKNOWN, so the cell is not evaluable on both sides. Feasibility: the same fate-of-the-variant design family. Both rest on the same single Q230P measurement |
| A01 – B01, A02 – B01 | no | the endpoint is full-length protein from a premature-stop allele, not the missense class (the B01 card says its mechanism is "structurally inapplicable" to the reference missense) |
| A01 – C01, A02 – C01, B01 – C01 | no | endpoint (spike-wave rate in a null mouse) and genotype class (null) differ; the C01 card says transfer to a missense context is not established |
| A01 – D01, A02 – D01, B01 – D01, C01 – D01 | no | endpoint (organoid neurogenesis) and class (engineered knockout) differ; D01 is also a downstream compensation, not recovery |

**Non-dominated set, RECUPERO_PROFONDO: P4-A-01, P4-A-02, P4-B-01, P4-C-01, P4-D-01 — all five, because the dominance relation is empty over
the evaluable cells** (nine incomparable pairs and one undecided pair). That is the result, not an omission: the criterion removes nothing on this evidence, and
the information is in the incomparability. A single dimension does separate the rows without dominating: **only C01 has a WWOX-system rescue and only D01 has a WWOX-system pharmacological
intervention; A01, A02 and B01 have none**, which makes them candidates whose every evidence cell is adjacent literature. That is not an ordering, because the rows differ in endpoint and class.

## 2 · BENEFICIO_PRECOCE (9 rows: 3 candidates, 6 abstentions)

Cells: [`tables_early.md`](tables_early.md). Three of the abstention rows (growth, development, pharmacodynamic anchor) are **endpoint axes, not interventions**; they are rows because
the roadmap asks for abstentions as rows and because they bound what any candidate row can claim.

| Row | Endpoint | Class of benefit | Evidence |
|---|---|---|---|
| EB-KD-01 ketogenic diet | clinician-reported seizure control (human WOREE) | symptom; "Not disease modification" | inconclusive; one uncontrolled five-child series, no denominator, development unchanged in every column, two of three responders had died, reference genotype class has no diet entry |
| EB-VGB-01 vigabatrin | clinical cessation of epileptic spasms (human WWOX-DEE, single-patient reports) | symptom; "Not disease modification (CLAIM 031)" | partial plus an exposure limit; CLAIM 001 is "conflicting evidence" (efficacy n = 2 and n = 1 against MRI toxicity n = 2) |
| EB-ETX-01 ethosuximide (T-type contrast) | late-phase provoked seizure score in the Wwox-null mouse; no human endpoint | symptom; "Not disease modification" | one experiment, one laboratory; the R2 narrowing is proposed and unaudited |

Time to access and time to benefit: UNKNOWN on all three, separately. Risk: VGB carries an observed class-level exposure limit in WWOX-DEE; KD carries "Adverse effects: UNKNOWN";
ETX's cell is UNKNOWN-led with a class-level in-vitro signal for T-type blockers (research compounds; ethosuximide untested) that the card marks hypothesis-generating.

### 2.1 Evidence counted by origin (reader's derivation, UNAUDITED)

* **One series, many rows.** The Chong 2023 series is the origin of the whole diet card, of `A-VGB-10` and `A-VGB-11` on the vigabatrin card, and (through CLAIM 042, Table 1) of the growth and development axes. It counts **once**.
  Inside it two of the five children are "previously published" and which two is an inference from Table 1, so a pooled count across series may double-count them.
* **Shaukat 2018** is one report describing two children: one origin, two patients. Its development row is also the source of `A-VGB-9`.
* **Cheng 2020** (one figure, one experiment) is the origin of the ethosuximide card **and** of the lithium specificity negative that the ETX card cites; ethosuximide and lithium are one experiment, not two.
* The hormonal-regimen "six responders" are one column of one curation; cannabidiol's "4 of 4 continued" is one cohort.

### 2.2 Pair by pair (3 pairs)

| Pair | Comparable? | Relation |
|---|---|---|
| KD – VGB | **no on the strict gate** (seizure control, all types, versus cessation of epileptic spasms; different defined endpoints). *Sensitivity: treated as comparable*, the result is the same | **Undecided; neither dominates.** Both are symptomatic, uncontrolled, human, without latency; VGB carries an observed exposure limit and KD an UNKNOWN adverse-effect cell, so risk is not evaluable on both sides; they also share the Chong series |
| KD – ETX, VGB – ETX | no | a provoked seizure score in a null mouse versus a human clinical endpoint |

**Non-dominated set, BENEFICIO_PRECOCE: EB-KD-01, EB-VGB-01, EB-ETX-01 — all three** (two incomparable pairs, one undecided pair), for the same reason as above. None of the three
has any datum in the reference genotype class (no missense responder in the diet series; VGB's reports are mostly predicted-null; the mouse is a constitutive null).
Nothing in the table licenses an order, "protection", or a reading of seizure control as slowing of disease (CLAIM 031).

## 3 · Convergence: agreeing algorithms are not independent origins

* **No LINCS, signature-reversal or other virtual-perturbation output sits in any card**, and none was run for P5. The roadmap's warning that two LINCS-based tools are not two votes is therefore
  not exercised here; it is carried forward unchanged for the later (P6/P7) comparison.
* **Within the cards**, apparent agreement is mostly a shared premise. Seven of the twelve deep rows hang on **one** Q230P measurement; their agreement that "the first thing to place is the fate of the variant" is
  one dependence, not seven confirmations. In the early path the Chong series and the Cheng 2020 experiment each feed several rows.
* **Between the plain lookup and the cards** (§ 4), the lookup and the cards name the *same drug class* for a few rows (proteasome inhibitors, mTOR inhibitors, amlexanox, a read-through agent, arimoclomol,
  corticosteroids/phenobarbital). Two routes agree on a name. Their origins are not WWOX evidence on either side: the lookup's edge is an interaction database (519 of the 524 neighbour edges have BioGRID as primary source) and the drug sits on the
  neighbour, not on WWOX; the cards' origins are adjacent-disease papers or repository notes. Independence of the *selection* of the card candidates from database-style reasoning is not established here,
  so the agreement is **counted as zero WWOX evidence and not as a second vote**.

## 4 · The plain target-to-drug lookup

Command, read-only: `kg_thin_slice.py WWOX --limit 2000 --raw-dir <scratch> [--json]` (the Monarch/DGIdb slice), run 2026-10-22; summary in [`lookup_summary.json`](lookup_summary.json); raw packet 7.8 MB kept in the session scratchpad, SHA-256
`0f09f09789772cebd36d6dc3feac1e886263670eff3915473445f64885dbeb03`, not committed (live APIs may differ on rerun).

* **Coverage states, unmerged.** Monarch: `OK`, all 825 associations read, not truncated. DGIdb: `INCOMPLETE`, 328 of 461 requested symbols returned, 133 `UNMATCHED` (unmatched is not "no drugs"); the packet's top-level `interaction_coverage` is `UNKNOWN`, so whether any per-gene interaction list was cut is not stated by the tool. 196 of the 328 returned symbols have at least one interaction. Overall status `INCOMPLETE`.
* **What it returns.** 521 gene neighbours and 3 pathway nodes (never sent to DGIdb); **WWOX itself has three direct drug entries** (two oncology/pharmacogenomic entries and a recombinant TNF-family protein), none a WWOX-function datum. Everything else is a drug on a *neighbour* gene, ordered by how much the neighbour has been studied.
* **Which card rows it touches, only through a neighbour gene:** A02 (proteasome subunits as neighbours: bortezomib, carfilzomib, ixazomib), B01 (amlexanox via a metabolic-enzyme neighbour), B02 (ataluren via two ribosomal-protein neighbours; gentamicin via two others), A05 (arimoclomol via HSPA1A, the candidate the repository withdrew the same day), A01 only as butyrate salts/esters, not 4-phenylbutyrate or bile acids, EB-MTOR (sirolimus/everolimus via MTOR and others), EB-HORM (corticosteroids, phenobarbital), plus valproate and lithium cation, which no card carries.
* **Which rows it does not touch:** vigabatrin, ethosuximide, cannabidiol, the ketogenic diet, A51, AAV9, the WWOX splice ASO, CRISPRa, Wnt/tankyrase agents (a hit is not an absence: coverage is incomplete).
* **The inversion this shows (reader's derivation, UNAUDITED):** every row that has *any* measurement in a WWOX system (C01, D01, ETX, KD, VGB) is invisible to the lookup; the rows the lookup does reach (A02, B01, B02, A05, MTOR, HORM) are those with none. A lookup-first choice would therefore have pointed at the rows with the least WWOX-specific data and away from the rows with the most.

## 5 · Against the pre-existing records, and what the cards change in the next experiment

Pre-existing choices of "the cheapest next observation" (known-roads note § 6, early-benefit note § 4, the deep-card note's closing question):
(a) a drug-by-genotype ethosuximide comparison; (b) one junction-spanning RT-PCR with an NMD block for a WWOX splice allele; (c) a function measurement for any read-through; (d) acquire a native surface of the one WOREE series; (e) the Q230P fate design implied by CLAIM 019/030/032.

* **Which experiment is next: the cards change nothing.** Each pre-existing choice is reproduced by a card's own `next_measurement`. No card proposes an experiment absent from the notes.
* **What they change is the attachment of the experiment to the rows.** (i) The fate-of-the-variant design (three fractions, an inhibitor arm, a chase, on the exact variant, with a function readout) is the named next measurement of A01, A02, A04, C03 and, as a chase paired with a chaperone perturbation, A05: five of twelve deep rows
  wait on one assay on one allele, and two more (A03 needs a ligand and a stability measurement; B01/B02 need a PTC enumeration) wait on others. (ii) The acquisition of the native surface of the Chong series is the named next step of KD and GROWTH and also informs VGB's two Chong observations: one act, three rows. (iii) For ethosuximide the *specification* changes (late-phase restriction, an interaction test, a same-day control), not the choice.
* **A row neither path carries.** Lithium (a measured relevant negative on specificity in the same experiment as ethosuximide, and the only GSK3-inhibitor datum in a Wwox-null mouse) is a row in neither table: it appears only inside the D02 abstention's `not_known` and the ETX card's text. "Not carded" is not "discarded" (the deep-card note said it was a natural card for the other path).
* **The deep-card note's "if one card were brought to a clinician first, P4-C-01 is the candidate"** is a single-candidate preference expressed in prose; P5 does not adopt it. Consistently with it, C01 is the only row with a WWOX-system rescue and it is not dominated by anything, because nothing is comparable to it.

**Roadmap criterion.** KEEP if the comparison adds interpretable information; INCONCLUSIVE if the context problem dominates. Split, because the two uses differ:
* **For choosing a candidate, INCONCLUSIVE.** The context problem dominates: more than half of the cells that matter are UNKNOWN, the candidates sit in different endpoint and genotype cells, and no row has a datum in the reference genotype class. The dominance statement is empty by construction.
* **For choosing what to measure or acquire next, KEEP.** The tables add three interpretable facts the cards alone did not: the seven-to-one collapse of the Q230P premise, the shared gating assay across five rows, and the lookup's inversion.

## 6 · Fields that look stale (reader's reading, UNAUDITED; no card was edited)

| # | Card | Looks stale because |
|---|---|---|
| S1 | cards/D01_a51 | its pharmacokinetic sentence is overtaken by the later recomputation (see § 1); the stored packet does not even hold the earlier 1.27 repair. A card frozen at one moment cannot see a repair that lands after it |
| S2 | cards_early/EB-VGB-01 | its prose says two reports were "reported ineffective" (`A-VGB-5`, `A-VGB-6`) while both assertions are encoded UNKNOWN, although `NO_CHANGE` has existed since the bridge change `b96e4cd9` and `A-VGB-10` uses it |
| S3 | cards_early/README.md | still lists as open "no sign for no change" and "translation hard-coded UNKNOWN", which the deep set records as closed by `b96e4cd9`; its translation blocks in the cards still print plain UNKNOWN |
| S4 | cards/D02_wnt_tankyrase | `novelty_for_woree` says "NON_TROVATO … as a test" while its own `not_known` records a GSK3 inhibitor given to Wwox-null mice with a seizure endpoint; the abstention sits on a measured relevant negative that has no row |
| S5 | cards_early/EB-KD-01 | its README says the diet quote is matched "on secondary surfaces only" and was not re-sourced to the primary report |
| S6 | cards/D01_a51 | both assertions carry receipt `None` and depth UNKNOWN; the evidence cell cannot be verified from the card |
| S7 | cards_early/README.md | "time to access and time to benefit are UNKNOWN on every card" while three axis cards say "Not applicable" |
| S8 | cards_early/EB-MTOR-AX-01 | sits in the early set although its own text assigns the pathway rationale to the deep path; tabulated here where the card puts it |

## 7 · What the bridge cannot represent (gap list for the Harness agent; `repurposing_bridge.py` not touched)

* **G1 evidence origin.** No origin identifier on an assertion, so shared origin across assertions and across cards cannot be computed by a tool; § 1.1 and § 2.1 were done by hand.
* **G2 BLOCK-1.** No typed status; it is a free-text clause in one card. "UNKNOWN is not a pass" has no place to live.
* **G3 comparability.** No typed endpoint family or genotype class, so "incomparable" cannot be stated by a tool; this gate was applied by hand.
* **G4 one disease assertion per packet (the old open G-2).** It prevented tabulating C01's five endpoint families and D01's two without going back to the prose.
* **G5 staleness.** A card carries no pointer that says a source reading was later repaired (`superseded_by`), so S1 is invisible to any check. The D01 packet needs a one-line update by its author.
* **G6 two card layouts.** Deep cards keep P4 fields under `p4_card`, early cards under `p4_roadmap_fields`, with different key names (`next_measurement`/`next_measure`, `state_of_known_roads`/`known_roads_state`); a tabulator needs a mapping, a shared schema would not.
* **G7 null encoding.** `NO_CHANGE` is used by some assertions and not by others for the same kind of report (S2).
* **G8 lookup tool.** `interaction_coverage` is `UNKNOWN` at top level beside a per-batch `INCOMPLETE`; a drug listed under a neighbour gene is not flagged in the packet as "not on the seed".

## 8 · One question, never advice

*In the Q230P-class variant itself, in a cell that makes it from its own promoter, where is the protein lost: never made, made and cleared by the proteasome or the lysosome, or made and insoluble, as read from soluble, pellet and total fractions with and without inhibitors, and does whatever is recovered carry a WWOX function readout?*
One answer would turn five deep rows from abstentions or probes into cards or retire them, and would say whether the only WWOX-system rescue (a null-mouse replacement) bears on a missense context at all. The runner-up is the denominator in the one WOREE series (how many children, which counts, over what interval, on what co-medication); it would change three early rows.
