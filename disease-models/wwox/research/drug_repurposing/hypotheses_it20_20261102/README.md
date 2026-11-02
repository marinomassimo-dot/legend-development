# IT20 P5 — WWOX-guided hypothesis generation and an operational order of the main investigations (2026-11-02)

**Ordine delle indagini da finanziare, non classifica di efficacia.** Every ordered list produced here ranks the value of
the next discriminating test — what its result would change, at what cost — and never the probability of benefit. Where a
need's direction is unresolved or a documented action pushes the other way, the row says so in its own decisive-uncertainty
field, and the position must not be read as support for a direction the evidence does not carry.

Non-canonical research material. Actor `scientist`, task `ORCH-ROADMAP-IT20-20261102`, package P5, branch `it20-hyp`,
baseline `main` = `4f8ff596`. **Nothing here is medical advice**; no dose, route, schedule or preparation is carried by any
file in this package, and a guard in the generator refuses a row that would introduce one. Association is not modulation,
modulation is not rescue. This is the public edition: the subject is the WWOX-DEE reference genotype class, never a person.
Nothing in this package changes the four scientific current files or the receipt ledger.

## 1. The observed problem, and which of its five possible causes are real

The operator's observation: the dashboard foregrounds interventions already known from the WWOX literature. The brief asked
which of five causes that depends on. Measured, on this date:

| Candidate cause | Verdict | The measurement |
|---|---|---|
| (a) real generation capacity | **CONFIRMED, and it is the main cause** | Over one identical usable universe, the WWOX-qualified arm selected 99 compound families and the external-only arm 622; the qualified set is a **strict subset** (`wwox_only` = 0). The qualification path cannot propose a candidate that a plain target-list search would not already return — it filters, it does not generate. |
| (b) which needs and which catalogue slice are queried | **CONFIRMED** | Only **3 of 23** needs can qualify any lever at all, and all three are in the excitability cluster the literature already worked. That is the mechanism by which the known threads dominate: they are the only needs with a qualifiable tool. |
| (c) qualification criteria | **CONFIRMED, and it is the binding constraint** | `consistent` requires both a resolved up/down need direction and an explicit coupling row. 10 needs are blocked by an unresolved direction, 6 by a `restore`-type direction that no catalogue action vocabulary matches, 4 by having no catalogue association at all. 291 of 3,331 associations are direction-coherent. |
| (d) ordering rules | **CONFIRMED as a contributing cause** | The existing group rule (G1…GU) is a function of WWOX-system evidence depth, so the order it produces necessarily favours what has already been tested in a WWOX system. It is a correct answer to its own question and the wrong answer to "what should we fund next". |
| (e) public-presentation limits | Real but **not** the cause | Already recorded in `../diagnosis_it20_20261102/README.md`; a presentation change alone would have left (a)–(d) untouched, which is what the brief warned against. |

## 2. The reference experiment: external-only versus WWOX-qualified, at equal usable universe

`compare_universe.py run` → `comparison_summary.json`, `comparison_arms.tsv`. This is question 3 of the IT20 diagnosis.

Both arms read **one** universe U: every (family, target, need) association the shipped search layer returns for the 23
needs, minus the rows that layer already excludes from counts. U = **3,331 associations, 2,002 families, 19 needs with any
reach**. Nothing was re-searched; no network call; no spend.

| | arm E (external-only) | arm W (WWOX-qualified) |
|---|---|---|
| rule | documented up/down action on a listed target, approved status preferred, ordered by targets and needs touched | the same U, keeping only an association whose documented action is direction-coherent with the need's stated direction |
| families selected | 622 | 99 (34 with an approved status) |
| needs reached | 19 | **3** |
| families the other arm misses | 523 | **0** |

**What emerges in both:** the excitability cluster — the T-type calcium axis, the glutamate-receptor axis and the
symptomatic seizure axis. These are exactly the threads the WWOX literature already names.

**What the qualification excludes or weakens:** 523 families, and 2 of arm E's top 10. Arm E's top 10 is also instructive
about the reflex it stands for: it is populated by promiscuity (four listed targets each) and by **duplicate family twins** —
the same compound served once by one source and once by another is counted twice. Both are artefacts of counting, which is
why this module refuses to classify compounds by how many pathways they cover.

**Which direction stays unresolved:** 10 needs, carrying 2,048 associations over 1,584 families. Neither arm can qualify a
lever on them, and this package does not. They are a named gap, not a negative finding.

**Which need has no adequate tool:** 20 of 23, for three distinguishable reasons (`needs_without_an_adequate_tool`): an
unresolved direction (10), a `restore`-type direction with no matching catalogue action vocabulary (6, including every
WWOX-restoration need and myelination), and no catalogue association at all (4, one of which carries no target because it is
an endpoint). This package did **not** separate catalogue-coverage limits from target-listing limits for the last group;
INV-11 is that work.

**Which next experiment discriminates:** for the generation deficit itself, INV-02 and INV-06 — a protein-level measurement
that resolves a need's direction converts the largest blocked slice of the catalogue into an orderable question, which no
compound test can do.

## 3. Generation: what the mechanism-driven search actually produced

Run over the qualified needs through the existing path (needs → targets → catalogue families → existing qualifications),
with the module's own card and table corpus checked by name for each proposal.

Of the 99 direction-coherent families, 69 are already named in the WWOX material. Of the remaining 30, the honest
classification is:

- **radioligands, tool compounds and research chemicals** — the large majority. Not usable as a therapeutic hypothesis; they
  stay visible as what they are.
- **further members of a class the module already holds** — several, including one approved agent on a receptor subunit of
  the glutamate axis. Useful, but the brief's distinction matters: this is *another member of a known class*, not a new
  relation.
- **one genuinely useful advance, and it is a probe, not a therapy**: two approved agents with *different isoform reach* on
  the T-type calcium axis. The module's own need file records that its single T-type result is complex-or-group level, with
  no isoform datum and no drug-by-genotype interaction test. An isoform-discriminating pair makes both gaps measurable
  without building a tool compound. That is INV-03.
- **one new relation rather than a new class member**: an endogenous ligand with a documented coherent action on the same
  axis. It carries no status statement and no WWOX context, so it is recorded as a lead inside INV-03's perimeter, not
  promoted to a row of its own.

**The limit that prevented more, stated plainly.** No sustainable *new* therapeutic relation emerged outside the excitability
cluster, and the reason is structural, not a shortage of effort: 20 of 23 needs cannot qualify a lever, so there was nothing
to generate from. The brief allows this outcome — "a null result or abstention is valid when the search was done and the
limit identified" — and the limit is cause (c) above. The three concrete repairs it implies are INV-02, INV-06 and INV-11.

## 4. The investigations order, and how it differs from the previous one

Generated by the existing generator: `ranking_it8.py run` → `ranking.json` key `investigations` and `investigations.tsv`
(contract for the dashboard actor), from the curated, reviewable
`../ranking_it8_p9_20261029/investigations_it20.tsv`. 11 rows, 6 rank positions, ties explicit, no filler.

Each row carries rank and tie group, intervention, question, why now, evidence available, **evidence depth as a separate
displayed field**, decisive uncertainty, next test, feasibility, `origin_class`, `novelty_perimeter`, `direction_state` and
`movement_reason`. Origin: 7 `known_in_wwox`, 4 `generated_by_legend`, 0 `external_transferred`.

`verify_order_change.tsv` compares the previous ordering (the group view) with the new one on the four contrasting cases the
brief required:

| Case | Row | Group view | Investigations | What the change shows |
|---|---|---|---|---|
| known thread | INV-01 gene addition | G1 | **1** | stays top, for a different reason: not because its evidence is deepest but because the post-onset arm it lacks would re-read every other row |
| proposal lacking a premise | INV-02 ISR direction | G4b | **1 (tie)** | rises to the top tie: the missing premise is the cheapest decisive measurement and blocks the largest slice of the catalogue. The row does **not** assert that attenuating the axis helps |
| proposal lacking a premise | INV-06 myelination premise | **GU** | **3** | a unit that is unorderable in the group view is not at the bottom here |
| qualified emerging hypothesis | INV-03 isoform discrimination | G4a (no unit of its own) | **2** | an emerging hypothesis outranks four units that beat it in the group view, for an explicit reason, while its limits stay on the row. It was **not** promoted to rank 1: nothing was forced to demonstrate change |
| weakened by counter-evidence | INV-09 | G2b | **5** | falls below rows it ties with in the group view, because its only pharmacology is non-selective and pushes against a second need of the same objective |

Movement in both directions, on explicit reasons, with no forced promotion. The unit ranking itself is **byte-identical** to
the committed one (`order_digest` unchanged, `units` unchanged): this package added a view, it did not re-rank the units.

## 5. What is not rewarded

Declared in the data (`investigations.summary.what_is_not_rewarded`) and tested: novelty for its own sake, publication
count, number of linked pathways or needs, ease of purchase or access category, and depth of existing evidence — carried
beside every row and never a gate. A row with no ranked unit is recorded as "no evaluation depth applies (this is not a
depth of zero)".

## 6. Files

| File | What it is |
|---|---|
| `compare_universe.py` | the reference experiment: both arms over one usable universe; `run`, safe `--help`, stdlib, offline |
| `comparison_summary.json`, `comparison_arms.tsv` | its outputs (arm E top 10 and the whole arm W, with the per-need no-tool reasons) |
| `verify_order_change.tsv` | previous (group view) versus new (investigations) order on the contrasting cases, with the reason per row |
| `test_compare_universe.py` | 15 tests: the arm rules on synthetic universes, plus the committed properties the conclusions rest on |
| `receipt_it20_p5.json` | the package receipt, handed back; **not** appended to the ledger |
| `../ranking_it8_p9_20261029/investigations_it20.tsv` | the curated input table (every judgement reviewable in one place) |
| `../ranking_it8_p9_20261029/test_investigations.py` | 30 tests: the contract, the depth-is-not-a-gate guarantee, movement, and the validator guards |

Regenerate: `python3 -B .../hypotheses_it20_20261102/compare_universe.py run` (about two minutes: it builds the universe
need by need), then `python3 -B .../ranking_it8_p9_20261029/ranking_it8.py run`.

## 7. Limits of this package

1. The comparison measures **selection**, not benefit. Neither arm's output is evidence about any compound.
2. Arm E is a *reference*, deliberately built to behave like the reflex this module refuses. It is not a recommended method
   and its top 10 should not be read as candidates.
3. The duplicate family twins in arm E were left visible rather than merged: merging them is a catalogue-identity question
   this package did not reopen.
4. `novelty_perimeter` records what this module queried on this date. It is never a claim about the literature at large, and
   the generator refuses a row that phrases it as one.
5. The isoform-discriminating proposal rests on catalogue-curated mechanism rows, not on a potency measurement read by
   LEGEND; no potency is carried. Whether the isoform claims hold at the relevant exposure is unverified here.
6. The engine branch (`it20-engine`) has not landed. Everything here was built against `main`; the association universe and
   therefore the three measured counts must be regenerated after that branch lands.
