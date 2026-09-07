---
record: TEAM RECONCILIATION — PMID 32000863 · the GSK-3β / lithium neighbourhood
id: SCIENTIST_TEAM_RECONCILIATION_PMID32000863_v1
producer: worktree `lettore` (mapped scientist-a), designated by Orchestrator
actor_status: NOT ACTIVATED — roles/scientist.md is PROPOSED;
  DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE returns ACTIVATION_NOT_CONFIRMED
date: 2026-08-25
status: NON-CANONICAL. No canonical file written. No relation type written to any registry.
  No token invented. No peer artifact edited. No BATCH_COMMIT.
inputs: A (5 artifacts), B (Phase I pilot + addendum + edge adjudication + Phase II + Phase III),
  C (Phase I first pass + Phase II + schema gaps)
forced_consensus: PROHIBITED. Surviving disagreement is recorded as a result.
---

# Reconciliation — three readings of one experiment

> **Nothing here is medical advice.** Public, disease-level, de-identified.

**Producer's declared conflict.** I am the most contaminated of the three by the tracked tree —
most of my Phase I was recognition, not derivation (§0.2 of my cross-review) — and I published a
false routing fact about a peer. I hold the lowest stake in the surviving disagreements only
because **both of my contested positions were withdrawn**, not because I was careful. Where this
document preserves dissent against a position I once held, that is the cheapest kind of fairness
and should be discounted accordingly.

**Scope discipline used throughout.** Every finding is labelled by the scope at which it was
obtained — `EDGE`, `NEIGHBOURHOOD`, or `INSTRUMENT` — using C's taxonomy. **A finding reachable
only at neighbourhood scope, recorded against an edge, reads to a later reader as an edge-scope
finding and will not reproduce.** Two of the load-bearing findings here are `NEIGHBOURHOOD`.

---

## LAYER 1 · CONSENSUS OBSERVATIONS

Only propositions **all three accept** *and* that bind to primary evidence. "Nobody objected" was
not sufficient for entry; each line names who derived it independently.

| # | Observation | Primary locator | Derived independently by | Scope |
|---|---|---|---|---|
| O-1 | Lithium (LiCl 60 mg/kg i.p. × 3 within 1 h) suppresses PTZ-evoked Racine score with the panel's significance marker in **`Wwox+/+`, `Wwox+/−` and `Wwox−/−` alike** | Fig. 7d, three sub-panels; PNG `ced68a66…62542` | A (native res.), B, C | `EDGE` |
| O-2 | N in Fig. 7d: `+/+` 12 vs 8 · `+/−` 12 vs 12 · `−/−` 6 vs 7; **no saline arm in any sub-panel** | Fig. 7d | A, B, C | `EDGE` |
| O-3 | `****` is **undefined**: the legend defines only `n.s.` and `***P < 0.001`; the literal string occurs **0 times** in the XML | Fig. 7 legend; XML `792b5b29…f00f5` | A, B, C | `EDGE` |
| O-4 | Fig. 7c densitometry, all nine lanes: pGSK3β(Ser9) 2.7·3.1·**1.3** \| 3.6·3.5·**2.0** \| 3.9·3.8·**2.5**; total GSK3β 2.2·2.4·2.4 \| 2.3·2.4·2.6 \| 2.2·2.4·2.6 | Fig. 7c, read at 3–6× | A (6×), B, C (3×) — **identical to the last digit** | `EDGE` |
| O-5 | **Total GSK-3β is flat** (all nine lanes 2.2–2.6, null marginally higher); what falls is **inhibitory Ser9 phosphorylation** | Fig. 7c | A, B, C | `EDGE` |
| O-6 | **The heterozygote is not intermediate** on the phospho row — at or above wild-type in every region (3.1 v 2.7; 3.5 v 3.6; 3.8 v 3.9) | Fig. 7c | A, B, C | `EDGE` |
| O-7 | Panel c carries **no statistical support whatever**: no error bars, no SD/SEM, no marker, no test, no P value, no per-lane n. Legend: *"The representative results of four independent experiments are shown."* | Fig. 7 legend, panel c | A, B, C | `EDGE` |
| O-8 | Ethosuximide suppression is `***` in `−/−` and **`n.s.` in `+/+` and `+/−`** — with the **larger** N in the control arms | Fig. 7b | A, B, C | `EDGE` |
| O-9 | **GSK-3β was never measured in any lithium-treated animal**; no molecular readout exists anywhere in the lithium arm | whole XML + 24-pp supplement, denominators declared | C (two surfaces), A, B | `EDGE` |
| O-10 | Statistics, in full: *"We performed statistical tests with one-way analysis of variance (ANOVA)… P values… less than 0.05."* **No interaction term, no post-hoc named, no multiplicity correction, repeated measures treated as independent** | Methods, Statistical analysis | A, B, C | `EDGE` |
| O-11 | Dosing is **not exposure-matched**: ethosuximide **one** dose of 150 mg/kg at −45 min; LiCl **three** doses of 60 mg/kg within 1 h = **180 mg/kg cumulative** | Methods, BODY-EXACT | C first; A verified verbatim | `EDGE` |
| O-12 | Panel c's own `Wwox` row shows protein **absent** in `−/−` and **visibly reduced** in `+/−` — gene dosage visible in WWOX protein, **absent** in pSer9 | Fig. 7c, Wwox row at 4× (qualitative — that row carries **no densitometry**) | C first; A verified at 4× | `EDGE` |
| O-13 | Wang 2012 contains **no seizure endpoint at all**: `seizure` 0 · `epilep` 0 · `convuls` 0 · `lithium` 0 · `LiCl` 0 across 49 334 non-abstract characters and the abstract | Wang JATS `eb6f568d…8268` | A first; **C verified at the source, not from A** | `EDGE` |
| O-14 | Wang's **S9A mutant** — a GSK-3β that cannot be inhibited at Ser9 — decreases SH-SY5Y differentiation **exactly like wild type**, while kinase-dead and R96A do not | Wang, Results / Fig. 5a–b | A first; **C verified at the source** | `EDGE` |
| O-15 | Cheng reports **no systemic covariate**: `blood glucose` 0 · `bicarbonate` 0 · `BUN` 0 · `creatinine` 0 · `hypoglyc` 0 · `acidosis` 0 · `serum` 0 · `body weight` 0 | whole cleaned XML | C first; A re-ran on an independently derived surface (70 057 chars vs C's 71 916) | `EDGE` |
| O-16 | `CLAIM 036` documents the systemic constitutive null at **P18**: glucose 143.5 v 250.6 mg/dL (`p=0.000131`), bicarbonate 14.50 v 21.67 mEq/L (`p=0.006227`), BUN 37.25 v 17.67 mg/dL (`p=0.01086`), `n=3/3/4` | `claim_registry_current.md`, `main` | C first; A verified verbatim | 🔴 `NEIGHBOURHOOD` |
| O-17 | `CLAIM 016` cites **Fig. 7b** for a **Fig. 7d** result | `claim_registry_current.md` | A, B, C | `EDGE` |
| O-18 | The Results text states **no result** for Fig. 7c — method and figure citation only, then *"Together, these results suggest…"* | Results, GSK-3β section | **A alone** | `EDGE` |
| O-19 | The Fig. 7 **title** asserts causation — *"Increased GSK3β activity … **leads to** hypersusceptibility"* — and no panel under it tests it | Fig. 7 title | **A alone** | `EDGE` |
| O-20 | Fig. 7d magnitudes: `+/+` peak Δ ≈ **0.3–1.0** stages, confined to ~5 of 60 min, traces interleaving thereafter; `−/−` peak Δ ≈ **2.0**, sustained | Fig. 7d at 3×; read off the plotted axis — the paper tabulates none | **A alone**, native resolution | `EDGE` |

**O-18, O-19 and O-20 are single-actor observations.** They are recorded as consensus *observations*
only in the sense that neither peer disputes them and both had the same artifact; **no peer
independently re-derived them.** Weight them below O-1…O-17 accordingly. Marking this is the point
of the layer.

---

## LAYER 2 · CONSENSUS INTERPRETATIONS

**Explicitly interpretation, not observation.** All three hold each; each is defeasible.

**I-1 · The paper demonstrates no WWOX-specific pharmacological rescue.** `EDGE`.
Held by all three from Phase I onward and unchanged by peer interaction.

**I-2 · GSK-3β is not established as lithium's operative target here.** `EDGE`.
No target engagement was measured (O-9); lithium is not selective; no second inhibitor and no
genetic test was run. The paper's own Discussion supplies the alternatives it does not exclude.

**I-3 · GSK-3β is *dis-inhibited*, not *more abundant*.** `EDGE`. From O-4/O-5.
🔴 **All three converged on the further point that *"elevated"* is *unsupported and misdescribed*,
not *disproven***: the abundance direction really is upward by 9–18%. B wrote *"disproven"* and
retracted it after A and C objected independently. **Recorded because the correction ran against
the direction the team was collectively leaning.**

**I-4 · Genotype specificity is `NOT TESTABLE` in this design — neither demonstrated nor
contradicted.** `EDGE`. The three verdicts, kept distinct as required:

| | |
|---|---|
| **DEMONSTRATED?** | **No.** The test that would separate specific from non-specific rescue was not performed (O-10). |
| **CONTRADICTED?** | **No.** O-1 refutes only the strongest form — *"lithium acts only where WWOX is missing"*. It does **not** refute *"lithium acts more where WWOX is missing"*, and O-20 is visibly consistent with that. |
| **NOT TESTABLE?** | **Yes.** One-way ANOVA, no interaction term, repeated measures as independent, unequal N, no saline arm in 7d, floor in the control arms. |

**A and B both first stated this too strongly and both withdrew.** C's formulation prevailed and is
adopted verbatim: *"the experiment cannot distinguish specific from non-specific rescue, because the
test that would separate them was not performed."*

**I-5 · The ETS-versus-lithium specificity contrast is confounded by exposure and cannot carry
weight.** `EDGE`, from O-11. All three had quoted the dosing sentence; only C drew the consequence.
**The confound has a direction:** higher cumulative exposure makes lithium *more* likely to clear
significance in exactly the low-ceiling control arms where ETS did not — so it is a competing
explanation for the observed pattern, not a symmetric caveat.
*Scope of the concession:* this removes a **rhetorical** argument all three of us used. It does not
touch O-1, which is within-panel and within-drug.

**I-6 · The composed account — the substantive scientific output, and no single first pass contains
it.** 🔴 `NEIGHBOURHOOD`.

| Contributor | Objection | What it establishes |
|---|---|---|
| **B** | `CLAIM 035` declares WWOX's inhibition S9-independent and warns pS9 gives a false negative; `CLAIM 016`'s principal molecular evidence *is* a pS9 western in that setting | The two wikilinked claims disagree about what the key measurement means |
| **A** | O-14 — the S9A mutant behaves like wild type, with internal controls | The Ser9 axis is **dispensable by design**, not merely unengaged. B's mismatch becomes a designed result rather than an inference |
| **C** | O-15 + O-16 — Ser9 is the canonical AKT output; the animal is hypoglycaemic, acidotic and uraemic in the same window | A **complete alternative cause**: right direction, right readout, no WWOX–GSK-3β mechanism required |

**Composed:** losing the WWOX brake predicts raised GSK-3β activity *with Ser9 unchanged* (A). Cheng
observed Ser9 *changed*. So the observed event is not the signature of the lost brake (B) — and
there is a standing, quantified, same-window explanation that predicts exactly it (C).
**O-12 closes the loop:** WWOX protein is dosage-graded, pSer9 is not. *That is what a systemically
driven readout looks like and what a WWOX-proximal one does not.*

🔴 **Held at its proper strength, and this is the sentence to carry forward:** this **does not
refute** the observation and **does not refute `CLAIM 016`**. Both explanations remain available and
are not mutually exclusive. C's confound is *untested, of high prior plausibility, not demonstrated*
— different line (EIIA-Cre `Wwox^ΔCre/ΔCre`), different window (P14–P18 v P20).
**What the composition removes is not the observation. It is the observation's right to be read as a
WWOX-specific mechanistic signal until a metabolically-controlled measurement exists.**

**I-7 · The bridge from `CLAIM 035` to `CLAIM 016` is a *citation*, not a measurement.** `EDGE`.
Cheng cites Wang (reference list carries `WangHY… Cell Death Differ 2012 19 1049`) and runs no
experiment testing Wang's mechanism; Wang measures nothing on Cheng's side (O-13).
**INFERENTIAL, not empirical** — the answer to the question the dispatch posed.

**I-8 · `CLAIM 016 ↔ CLAIM 035` is `NOT_DIRECT`, and no further token is assignable.** `INSTRUMENT`.
Decided against the only published criterion — *"the same experiment measures both endpoints"* — by
O-13. Beyond that exclusion nothing is assignable, because three of four tokens have no published
semantics. **A and B each first assigned a token and both withdrew.**
*C's residue, adopted:* the endpoints also share an **entailment** — Wang's mechanism entails
de-repressed GSK-3β in WWOX-null neurons — which makes the honest object a **hypothesis**. The
vocabulary has **no hypothesis tier**, so assigning nothing is the *faithful* move, **not an
abstention**.

---

## LAYER 3 · LIVE DISAGREEMENTS

Preserved. **Forced consensus is prohibited and none was applied.** Two items that were live at the
close of Phase III are now closed — recorded as closed, not deleted.

**L-1 · Is the Ser9 fall WWOX-proximal or systemic? — UNRESOLVED, and it is the scientific centre.**
Three findings point away from the WWOX-proximal reading (O-12, O-14, O-15+O-16) and **none refutes
it.** Both explanations predict the same panel, and they are not exclusive. All three actors hold
this open. **This is a legitimate surviving disagreement with the canonical model, not among us.**

**L-2 · Does the ethosuximide genotype restriction survive exposure matching? — UNTESTED.** `EDGE`.
C records it as a standing disagreement with the **canonical evidence boundary**, *"which is not a
peer and cannot concede"*. Correct, and the formulation is preserved.

**L-3 · 🔴 Is the `INSTRUMENT` axis settled? — I DISAGREE WITH C, and I hold the falsifier C
invited.** `INSTRUMENT`.

C published a falsifiable prediction, measured it, broke it and amended its own artifact — which is
the conduct that makes this checkable. C's restated position: *"`INSTRUMENT` (gap 4) will recur on
every edge. Re-testing it adds nothing; **it is settled**."*

**Measured, from the export the layer actually emits** (`pathograph_export.jsonl`, 371 records):

```
claim_node fields : biological_scale, claim_link_degree, clinical_relevance,
                    cross_reference_papers, epistemic_type, evidential_papers,
                    genotype_model_relevance, id, kind, mirror_title, pathway,
                    status, title, transferability
claim_edge fields : declaring_fields, directions_declared, edge_id, endpoints,
                    kind, reciprocal, relation_type, relation_type_basis,
                    review_packet, review_state
```

🔴 **Nodes carry `epistemic_type`. Edges carry none.** The `review_packet` carries the *endpoints'*
`endpoint_type` — the nodes' tiers — and the edge itself has no epistemic field of any kind. **A
relation asserted as `IPOTESI` and one asserted as `DATO` serialise identically.**

This is **not** C's gap 4. Gap 4 is about *definability* — three tokens lacking semantics. This is
about *expressiveness*: a fully-defined four-token vocabulary would still be unable to distinguish
*"contributes to"* from *"**may** contribute to"*, which is the exact wording of `CLAIM 016`'s own
title and the single most important word in it.

⇒ **The `INSTRUMENT` axis has at least two independent failure modes and was enumerated once and
declared closed.** *"Settled"* is premature. I record this as a disagreement rather than an
extension because C's word was *settled*, and the difference between *"this recurs"* and *"this is
the only one"* is what decides whether anyone looks again.

**L-4 · Breadth versus depth — UNRESOLVED and correctly not ours.** B adjudicated eleven edges, A
one at greater depth, C zero. §15 puts it with Orchestrator. Two facts now bound it: my dispatch
carries **no cap**, so my count of one is a choice I declared as unfinished work and not restraint;
and C's measurement shows volume inside an unspecified instrument multiplies gap 4 rather than
adding knowledge.

**L-5 — CLOSED.** B's dissent trail item 5 (*"C concluded the Pathograph does not exist … not
conceded by C"*): **C has since withdrawn it** in its Phase II D1. Closed by concession.

**L-6 — CLOSED.** B's dissent trail item 6 (*"A declared the Phase II gate closed on C … not
conceded by A"*): **A has since conceded it**, in Phase II §0.3 and in correction blocks placed
above the false text in both Phase I artifacts. Closed by concession.

🔴 **B's Phase III carries the caveat that *"only one third of Phase II has happened"*. That caveat
is now stale** — all three cross-reviews exist, and both one-sided items closed in the direction B
predicted. Recorded here because a stale caveat in a durable artifact misdirects a later reader
exactly as a stale measurement does.

**L-7 · Producer's conflict, left open rather than adjudicated by the producer.** Every position I
held that was contested is now withdrawn, which makes preserving dissent costless for me. **Whether
this document under-preserves dissent *against C* — whose argument prevailed, and on whom neither
B nor I now disagree except at L-3 — is a question I am not positioned to answer about my own
writing.** It belongs to Phase IV.

---

## LAYER 4 · FALSIFIERS / NEXT EXPERIMENTS

Ordered by what each settles, not by cost.

**F-1 · 🔴 C's L404A knock-in — the best falsifier the pilot produced, and neither other actor
proposed it.** Knock the **L404A** allele — which Wang shows abolishes WWOX–GSK-3β binding — into
the mouse, then challenge with PTZ.
- Seizure-susceptible with total WWOX intact → the GSK-3β arm carries the phenotype and the edge
  earns a causal type.
- Not susceptible → the seizure phenotype runs through something else in WWOX and the edge is
  bibliographic.
**It uses the mechanism paper's decisive reagent against the phenotype paper's endpoint — the one
experiment neither paper could have run alone.** It is the only proposal that would make
`016 ↔ 035` *typable* rather than arguable.

**F-2 · 🔴 C's sharpened confound test — reproduce the confound, do not remove it.** Measure brain
pGSK3β(Ser9) in a **non-*Wwox* model of comparable systemic illness at P20** — any genotype rendered
hypoglycaemic, acidotic and cachectic to a matched degree.
- Ser9 falls there too → the Cheng observation is a readout of terminal illness; `CLAIM 016`'s core
  datum loses its mechanistic reading.
- Ser9 holds → the systemic route is excluded, and the WWOX-proximal reading survives while still
  owing an explanation of why the dispensable channel is the one that moved.
**This is a positive control for the confound, which pair-feeding is not.** Removing a confound and
seeing nothing is weak; reproducing a confound and seeing the effect is decisive. *This supersedes
the pair-fed/glucose-clamped design that A, B and C all first proposed — the earlier form remains
valid and is strictly weaker.*

**F-3 · A's S9-independent substrate readout — the cheapest discriminator.** The metabolic route acts
**through Ser9**; the Wang mechanism is **S9-independent**. Measure GSK-3β output by a substrate that
does not use Ser9 — phospho-Tau S396/S404, Wang's own pair — in `Wwox−/−` brain. Raised output with
Ser9 held constant → the Wang mechanism operates in vivo. Output tracking Ser9 alone → the metabolic
route explains the panel. **Uses only tissue the original study already collected.**

**F-4 · For genotype specificity.** A PTZ + lithium arm with an **explicitly tested genotype ×
treatment interaction**; a structurally unrelated GSK-3β inhibitor at **matched cumulative exposure
and matched schedule**; a post-treatment target-engagement western; a saline arm in the lithium
panel; and the endpoint that matters — **spontaneous** seizures on video-EEG, documented from P12 and
never used.

**F-5 · For the exposure confound.** Ethosuximide and LiCl at matched cumulative dose and schedule,
in **one** experiment with a shared control arm.

---

## THE SCIENTIFIC DELTA — what peer interaction changed, and by whose evidence

The measurement this pilot exists to produce.

### RETRACTED

| Actor | Position | Retracted on | Whose evidence |
|---|---|---|---|
| **B** | Wang 2012 manifest locators are **2/9** strict; a legacy-manifest defect class is confirmed on a second paper | Withdrawn outright | **A** — re-derivation with tags stripped to empty gives **9/9**; B's own substitution inserted the whitespace it then diagnosed |
| **A** | Genotype-specific rescue is **REFUTED** by the panel | Withdrawn; replaced by `NOT TESTABLE` | **B + C** independently; and A's own native-resolution re-read (O-20), which A had declined in Phase I |
| **A** | Edge type `ASSOCIATED` | Withdrawn entirely | **C** — first the criterion (three tokens undefined), then the substance: A's own O-14 composed with C's confound dissolves the shared-referent premise |
| **B** | Edge type `INDIRECT_UNKNOWN_INTERMEDIATES` | Withdrawn → `ASSOCIATED` → then that too | **A**, then **C** |
| **C** | *"The Pathograph is not present in this repository"* | Withdrawn | **A + B** — the object is untracked in the shared checkout; C's sweep was worktree-confined |
| **C** | *"No governed relation vocabulary exists"* | Withdrawn | same cause, not a second error |
| **C** | *"A second edge would force no sixth schema gap"* | Withdrawn **by C's own measurement**, and C amended its durable artifact rather than only replying | **C** on itself |

### WEAKENED

| Position | Weakened to | Whose evidence |
|---|---|---|
| B: *"elevated"* is **disproven** | *"unsupported and misdescribed"* — the abundance direction really is upward by 9–18% | **A + C**, independently, against the team's collective lean |
| A + B: lithium raises threshold *"irrespective of genotype"* | *"the experiment cannot distinguish specific from non-specific rescue"* | **C** — weaker and much harder to overturn |
| All three: *"ETS is specific, lithium is not"* | Confounded by exposure; withdrawn as an argument | **C** (O-11) |
| B: the working-model mirror *"is already corrected"* | *"half-corrected"* — *"not merely elevated abundance"* still presupposes elevated abundance | **C** |
| A: *"the vocabulary question is unresolvable as posed"* | Partly decidable: `NOT_DIRECT` is a decided result | **C** — an undecidable framing was hiding the answerable half |

### STRENGTHENED

| Position | By what | Whose evidence |
|---|---|---|
| B's pS9 readout mismatch — an **inference** | Became a **designed result** with internal controls | **A**'s O-14 (S9A). C states this **changed** its position rather than supplementing it |
| A's *"CLAIM 036 is a standing confound"* — a **name** | Became a **mechanism** predicting the observed direction and readout | **C** |
| C's *"no target engagement"* — an **assertion** | Became a **measured absence** across two surfaces with denominators | **C** |
| A's *"shared evidence is bibliographic, not evidential"* — a **generalisation** | Became an **instance with a count** on the edge that matters | **A**; C verified it at the source rather than from A |
| A's four-surface receipt finding | Verified as a **class**, not an instance — see below | **B**, extended by **A** |

### REFORMULATED

- A's *"the four papers' inputs are gone"* → **the surfaces never agreed on what was read** (B).
- C's *"one edge is the right unit"* → **`edge + one hop`**, after C's own scope classification.
- The confound test: *remove the confound* (all three) → **reproduce it in a non-`Wwox` model** (C).

### 🔴 CORRECTED HERE — the receipt class is **22**, not 23

Re-measured by me over all 128 receipts:

| | |
|---|---|
| Total receipts | **128** (chain verifies; the chain validates hashes, not semantics) |
| `source_fingerprint: null` | **27** |
| `source_locator` → `paper_registry_current.md#PAPER nnn` | **23** |
| …of which `record_kind: legacy_reconstruction` | **22** |
| …of which `record_kind: receipt_invalidation` | **1** |

**`FTR-20260806-23446842-02` must be excluded.** It is a `receipt_invalidation` whose
`evidence_basis` reads *"Identity audit on 2026-08-06: PAPER 032 owns PMID 30619736, not PMID
23446842; the legacy reconstruction cannot establish reading depth"*. **Its locator points at the
registry because the registry entry is precisely what it makes a statement about.** Counting it
would file a **repair** as a defect.

Likewise the other **4** null-fingerprint receipts are `contemporaneous_receipt` with honest depths
(`abstract_only`, `queried_not_full_read`, `partial_fulltext_read`) and real external locators — a
null fingerprint is *correct* where no local artifact exists.

⇒ **The defect class is 22 of 128:** legacy reconstructions whose `evidence_basis`, `source_locator`
**and** `outputs` are all the same registry line, `source_fingerprint: null`, `evidence_depth:
partial_fulltext_read` — **so each contradicts the registry it cites while appearing to corroborate
it.** The null fingerprint also means none of the 22 could ever have satisfied the fail-closed
artifact gate, which **explains** the missing artifacts rather than deepening the mystery.
Recorded as a canonical defect candidate. **Not propagated. Operator's call.**

### STRUCK, not reworded

**B's convergence-map line *"Edge type for `016 ↔ 035` … resolved in A's favour"* is struck.** It
records an outcome that no longer exists: A withdrew the token, B had already withdrawn its own, and
C never assigned one. Rewording it would preserve the shape of a resolution where there is none.

---

## GRAPH CONTRIBUTIONS — with the scope at which each was obtained

**None written to any registry. No token invented. No relation type applied.**

| Contribution | Disposition | 🔴 Scope obtained at |
|---|---|---|
| `016 ↔ 035` is **`NOT_DIRECT`** | decided against the only published criterion | `EDGE` |
| Any further token for `016 ↔ 035` | **not assignable** — no criterion exists to check against | `INSTRUMENT` |
| The honest object is a **hypothesis** | the vocabulary has no hypothesis tier; assigning nothing is faithful, not abstentive | `INSTRUMENT` |
| WWOX ⊣ GSK-3β, residue-mapped, S9-independent | strongly evidenced **within Wang's system**, with *no WWOX-DEE allele tested* attached | `EDGE` |
| GSK-3β state → seizure phenotype | **unsupported** as a mechanism edge | `EDGE` |
| The metabolic alternative (I-6, O-16) | load-bearing, and **reachable only by holding `CLAIM 036`** | 🔴 `NEIGHBOURHOOD` |
| Nodes carry `epistemic_type`; **edges carry none** | a second `INSTRUMENT` failure mode (L-3) | `INSTRUMENT` |

🔴 **The two findings that jointly dissolved `ASSOCIATED` are a three-body argument in a two-body
form.** `CLAIM 036` is referenced by **neither** endpoint — verified: 0 occurrences in `CLAIM 016`'s
block, 0 in `CLAIM 035`'s body, positive control `CLAIM 035` appears 2× in `CLAIM 016`'s block. Since
the layer assembles edges from declared wikilinks, `CLAIM 036` is not one hop away *in the graph*; it
is **outside the graph's reach from that edge entirely.** A reader who arrives at this edge through
the graph cannot reconstruct the argument that decided it.

**The minimum unit that exposes this schema is `edge + one hop`, not `edge`.** Two of six schema
gaps were invisible at edge scope. C's amended prediction, carried forward for testing:
`INSTRUMENT` recurs on every edge — **and is *not* settled (L-3)**; `EDGE` holds, and a second edge
at depth should expose nothing further of that kind; `NEIGHBOURHOOD` may force more, because what
is reachable one hop out is a property of which claims surround an edge, not of the schema.

---

## WHAT THIS RECONCILIATION IS NOT

- **Not hostile-reviewed.** Phase IV is B's, and the items that most need adversarial attention are
  the two I depend on and did not derive — C's AKT route — and the one I did derive and that now
  carries the composed account, O-14.
- **Not canonical.** Five defect candidates stand and all require `BATCH_COMMIT` and the Operator:
  the Fig. 7b/7d pointer (O-17); `CLAIM 016`'s `Summary`/`Type` contradicting its own later block;
  `CLAIM 016` and `CLAIM 036` not referencing each other; `CLAIM 016`/`CLAIM 035` holding an
  unresolved readout tension with no comment; and the **22-receipt** class.
- **Not a settlement of the science.** The decisive experiments in Layer 4 have been done by nobody,
  and the field is five papers wide — `WWOX AND GSK3` returns five records in all of PubMed.
- **Not an adjudication of the remaining edges.** Nineteen unadjudicated, twelve adjudicable today.
  **That is a task, not a scope boundary**, and it stays a task.

---

*Non-canonical. Nothing here is medical advice. No canonical file was modified in producing it.*
