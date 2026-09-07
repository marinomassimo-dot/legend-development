---
record: §13/§17 OPERATING-PRACTICE EVIDENCE — what the §5 per-edge schema could not hold
id: SCHEMA_GAPS_PER_EDGE_OUTPUT_SCIC_v1
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
status: NON-CANONICAL. Mutates nothing.
scope: measured against ONE adjudicated edge — CLAIM 016 <-> CLAIM 035. No second edge was
  adjudicated to produce this. No schema change is proposed.
---

# Five things that decided an edge, and had nowhere to go

> **Nothing here is medical advice.**

**This is not a graph contribution.** It is evidence about what a graph contribution has to contain,
measured the only way it can be measured: by adjudicating one edge to the bottom and recording what
fell through the form.

**The discipline that makes it citable rather than opinion:** every gap below is stated against a
*fact that actually decided something*. A schema critique unattached to a decision is design taste.
Each entry therefore carries the fact first and the missing shape second.

**Two prohibitions I am holding to.** §16 forbids inventing governed tokens, and the same logic
forbids inventing fields — so I name what the schema cannot hold and I do **not** name a field that
would hold it. Filling these is architecture and is not this run's authority. Where I describe the
shape of a homeless fact, that is a description of the fact, not a proposed slot.

**Failure kinds, distinguished throughout:**
`ABSENT` — no field addresses this at all ·
`WRONG-SHAPE` — a field exists, is asked for, and its shape forces the fact to be distorted or
dropped. The second kind is the more dangerous, because it returns a filled-in form.

---

## GAP 1 · The shared source is shared *bibliographically*, not *evidentially*

**Field that fails:** `PRIMARY SOURCE(S)` · **kind: `ABSENT`**

**The deciding fact.** Edge `016↔035` is a "shared evidential paper" edge — both claim records cite
`PAPER 056` (Wang 2012). Counted over the full JATS surface, 50,838 cleaned characters, tags
stripped to empty, positive control `GSK3` = 193:

```
seizure 0 · epilep 0 · convuls 0 · lithium 0 · LiCl 0 · PTZ 0 · ethosux 0
```

The shared paper **measures one endpoint and never the other.** (Counted first by Scientist A;
re-derived by me from the artifact rather than accepted from A.)

**Why this decided the edge.** The packet's own triage sorts edges by *"a shared evidential paper
already exists"* (§4B), and my dispatch treats that as the property that makes an edge tractable
first. It is not. **Two records citing one paper is a bibliographic fact.** Whether that paper
measured both endpoints is the evidential fact, and it is the one that determines whether the edge
can be typed from the shared source at all. Here it cannot: the mechanism paper contains no
phenotype endpoint, so nothing in it speaks to the relation.

**What had nowhere to go.** `PRIMARY SOURCE(S)` asks *which* sources; nothing asks *which endpoint
each source measures*. A Scientist filling the form correctly produces an edge that looks
well-sourced — one paper, both records, full text present, manifest-backed — while the single most
decisive property of that sourcing is unrecorded. **The form cannot distinguish a shared measurement
from a shared citation, and it is the distinction that decides the edge.**

---

## GAP 2 · The confound is external to both endpoints

**Field that fails:** `NEGATIVE / COUNTER-EVIDENCE` · **kind: `WRONG-SHAPE`**

**The deciding fact.** The strongest thing found against `CLAIM 016`'s core datum comes from
**neither endpoint of the edge.** `CLAIM 036` documents, in a systemic constitutive *Wwox* null at
P18: glucose 143.5 vs 250.6 mg/dL (`p=0.000131`), bicarbonate 14.50 vs 21.67 mEq/L, BUN 37.25 vs
17.67 mg/dL. Cheng's blot is at **P20**, in animals the paper says *"succumb to death by 4 weeks
postnatally"*, and reports **no systemic covariate whatsoever** (`blood glucose` 0 · `bicarbonate` 0
· `BUN` 0 case-sensitive · `serum` 0 · `body weight` 0, across 71,916 cleaned characters). Ser9
phosphorylation is the canonical insulin/IGF-1→PI3K→AKT output, so a hypoglycaemic, acidotic,
catabolic animal is predicted to show exactly the fall Figure 7c reports.

**Why this decided the edge.** It supplies a *positive alternative* for the only measurement offered
as the bridge between the two endpoints — not a doubt, a competing mechanism that predicts the
observed direction.

**What had nowhere to go.** §5's `NEGATIVE / COUNTER-EVIDENCE` reads, in the dispatch's own words,
as *"evidence deliberately sought that could weaken the attractive interpretation"* — sought, by
construction, in the edge's own sources. `CLAIM 036` is a **third claim record**, about a different
mouse line, in an adjacent developmental window, that undermines one endpoint's datum without
mentioning either endpoint. It is not counter-evidence *from* the sources and not contradictory
evidence *between* them.

**The structural point, and it is the reason this is `WRONG-SHAPE` and not `ABSENT`:** a form scoped
to an edge's two endpoints and their shared sources **cannot see a three-body problem.** The
confound was reachable only by holding a claim that is on neither side of the edge. Note what
follows for the layer as a whole — `pathograph.py` assembles edges from declared wikilinks, and
`CLAIM 016` and `CLAIM 036` are mutually unlinked in both directions (positive control: `CLAIM 035`
appears 2× inside CLAIM 016's block, so the grep fires). **The strongest counter-evidence to an edge
sat one hop outside it, in a claim the graph does not connect to either endpoint.**

---

## GAP 3 · The bridging measurement is disqualified by the other endpoint's own paper

**Fields that fail:** `CAUSAL LIMIT` **and** `CONTRADICTORY EVIDENCE` · **kind: `WRONG-SHAPE`, both**

**The deciding fact.** Wang 2012, Results, Fig 5a/b, body-exact, verified by me from the primary
rather than accepted from Scientist A:

> *"Transfection with GFP–GSK3β WT and S9A notably decreased SH-SY5Y cell differentiation, whereas
> KD and R96A did not affect SH-SY5Y cell differentiation compared with the GFP control"*

A GSK-3β that **cannot be switched off at Ser9 behaves like wild type**; kinase-dead and the
substrate-binding mutant do not. Kinase activity is required and **the Ser9 switch is dispensable —
by design, with internal controls.** Wang separately reports pGSK3β-S9 *"remained normal"* while
output falls.

**Why this decided the edge.** `CLAIM 016`'s only molecular bridge to `CLAIM 035` is a Ser9 western.
Wang shows Ser9 is not the channel WWOX uses **and** is not required for GSK-3β's output. So Cheng
measures precisely the channel the mechanism paper excludes. The bridge is not weak — **it is
disqualified by the mechanism it is offered as evidence for.**

**What had nowhere to go.** `CAUSAL LIMIT` asks *what prevents a stronger interpretation*: it holds
"no interaction test", "one non-selective drug", "no target engagement". `CONTRADICTORY EVIDENCE`
asks whether evidence conflicts: here **nothing conflicts** — Wang's result and Cheng's result are
both real and are not in tension as observations. The relation between them is neither a limit nor a
contradiction. It is that **one endpoint's evidence removes the evidential standing of the
measurement the other endpoint offers as the join**, while leaving both observations intact.

Filed under `CAUSAL LIMIT` it reads as one caveat among four. Filed under `CONTRADICTORY EVIDENCE`
it is simply false. **Both available slots return a form that is filled in and wrong.**

---

## GAP 4 · `RELATION TYPE` presupposes the vocabulary is definable

**Field that fails:** `RELATION TYPE` · **kind: `WRONG-SHAPE` — the sharpest of the five**

**The deciding fact.** The governed vocabulary is `DIRECT · INDIRECT_UNKNOWN_INTERMEDIATES ·
ASSOCIATED · CONTROVERSIAL_OPEN`, published at `pathograph_inventory.md:131` as a bare list of
accepted values. **Three of the four carry no semantics anywhere in the governed surface.** The only
criterion published for any of them is an inline example at `pathograph.py:130` —
`(relation: DIRECT — the rescue measures both)`.

**Why this decided the edge.** Against the one published criterion the edge is decidable and I
decided it: **NOT `DIRECT`** — no experiment measures both endpoints (Gap 1 is the measurement).
Beyond that, *"does `ASSOCIATED` fit"* is not a hard question, it is **not a question**: there is
nothing to check a candidate against.

**What had nowhere to go.** §5 says *"Use only existing governed vocabulary. If no existing type
fits, say so."* That instruction assumes the failure mode is **no fit**. The actual failure mode is
**no criterion** — and the field offers no way to return it. A Scientist facing this slot has three
options and all three misreport: assign a token (asserts a fit that cannot be checked), leave it
blank (reads as work not done), or write prose (leaves the governed field empty while the content
lives somewhere a validator never reads — the exact failure the §5 free-text `Type` field already
produced on `CLAIM 016`, where the wrong word *abbondanza* survived three batches inside a slot no
tool inspects).

🔴 **The evidence that this is real and not my idiosyncrasy — two independent demonstrations.**

**(a) A and B each invented a definition, and neither cited one.** Scientist A glossed
`INDIRECT_UNKNOWN_INTERMEDIATES` as *"asserts a causal path with unspecified intermediates"*.
Scientist B, in a different document, rejected `ASSOCIATED` for other edges on the ground that it
*"asserts a biological association no source claims"*. **Both glosses are reasonable. Neither is
published.** The two Scientists then converged on `ASSOCIATED` for this edge and recorded the
disagreement as *resolved in A's favour*. **That convergence is two independent inventions that
happened to be compatible** — which is indistinguishable, from the outside, from two readings of a
shared definition, and is not the same thing at all.

**(b) B reached the same wall from the other side, and stated it at a different altitude.**
`PHASE1_PATHOGRAPH_EDGE_ADJUDICATION_SCIB_v1.md:236–240`:

> *"it is not that no governed type fits these eight edges — it is that **nobody can say whether any
> type fits any edge, because three of the four types mean nothing published.** The inventory's line
> 'Edges carrying a declared relation type: 0' reads as work not yet done; part of it is **undoable
> by construction** until the vocabulary is defined."*

B's *"part of the zero is undoable by construction"* and my *"the token has no published meaning"*
are **one finding at two altitudes** — B's is the property of the inventory's headline count, mine
is the property of the individual slot. I am recording the cross-reference rather than restating it
as a second finding, because counting it twice would inflate exactly the kind of tally this pilot
keeps warning about.

`VOCABULARY_INSUFFICIENCY_OBSERVED`, third instance, distinct kind. The two on record concern a
token that cannot **express** a proposition; this one concerns a token that has no published
**meaning**, which makes fit unanswerable rather than merely hard.

---

## GAP 5 · `MODEL / SYSTEM` is singular where the edge needs commensurability

**Field that fails:** `MODEL / SYSTEM` · **kind: `WRONG-SHAPE`**

*Forced by the same edge. No second adjudication was performed to reach it.*

**The deciding fact.** Scientist A's tabulation of the two endpoints, which I have checked against
both artifacts:

| | `PAPER 056` (Wang 2012) | `PAPER 019` (Cheng 2020) |
|---|---|---|
| Organism | **human** SH-SY5Y line + recombinant GST fusions + mouse brain extract | **mouse**, whole animal |
| Genotype | engineered point mutants (L404A, L311A; GSK3β WT/S9A/KD/R96A) — **no WWOX-DEE allele** | constitutive systemic null |
| Stage | not applicable (immortal line) | P20 |
| Condition | retinoic-acid differentiation; in-vitro kinase assay; pull-down | PTZ/pilocarpine challenge; drug-naive blot |

A's conclusion, which the table earns: **the two endpoints are never measured in the same animal.**

**Why this decided the edge.** The distance between the two systems is not context — it is the
quantity that determines whether a mechanism demonstrated in a differentiating human neuroblastoma
line licenses anything about seizure threshold in a P20 mouse. For this edge that distance is large
and it is load-bearing.

**What had nowhere to go.** §5's `MODEL / SYSTEM` asks for organism, cell type/tissue, genotype,
developmental stage, experimental condition — **one system, in the singular, as though an edge had
one.** An edge has two, and the scientifically decisive property is neither of them: it is their
**commensurability**. A Scientist can fill the field twice, once per endpoint, and the form will
look complete while the quantity that matters — the distance between them, and whether anything
bridges it — appears nowhere and is never asked for.

---

## Out of bounds, recorded rather than developed

**§5 has no shape for an edge that should exist and does not.** The whole schema opens with
`EDGE / TASK ID` and `CURRENT REPOSITORY ASSERTION`, both of which presuppose an existing declared
edge to type. `CLAIM 016 ↔ CLAIM 036` is the case in hand: the confound of Gap 2 and the claim it
constrains are mutually unlinked, and because `pathograph.py` assembles edges **from declared
wikilinks**, an edge nobody wrote is invisible to the layer by construction — it would not appear
among the inventory's 20 no matter how the evidence stood.

🔴 **Declared boundary:** this is forced by the **neighbourhood**, not by edge `016↔035`, so it sits
outside the "any fifth the same edge forces" bound. It required **no new adjudication** — it was
already recorded as E6 of my Phase II cross-review, before this was routed. I am naming it here
because it belongs with the other four and would be lost otherwise, and flagging its provenance so
it can be discounted if the bound is read strictly.

---

## What this cost, and what the right unit actually is

**AMENDED after the fact, and the amendment is against my own prediction.** I first wrote that one
edge was the right unit and that a second would yield no sixth gap. That was imprecise, and my own
sixth item is the reason: it was forced by the **neighbourhood**, not by the edge. Classifying all
six by what actually forced each one:

| | Gap | Forced by | Scope |
|---|---|---|---|
| 1 | `PRIMARY SOURCE(S)` | Wang's zero-count — Wang **is** an edge source | **EDGE** |
| 3 | `CAUSAL LIMIT` / `CONTRADICTORY EVIDENCE` | Wang's S9A — Wang **is** an edge source | **EDGE** |
| 5 | `MODEL / SYSTEM` | both endpoints' systems | **EDGE** |
| 2 | `NEGATIVE / COUNTER-EVIDENCE` | `CLAIM 036` — referenced by **neither** endpoint | **NEIGHBOURHOOD** |
| 6 | no shape for an absent edge | `CLAIM 016↔036` — referenced by **neither** endpoint | **NEIGHBOURHOOD** |
| 4 | `RELATION TYPE` | the vocabulary itself | **INSTRUMENT** — edge-independent |

Verified rather than asserted: `CLAIM 036` appears **0 times** in CLAIM 016's block and **0 times**
in CLAIM 035's body (positive control: `CLAIM 035` appears 2× in CLAIM 016's block). *A first count
returned 1 for the CLAIM 035 body; that was the `awk` range including its own terminator line. Caught
and corrected before it was used — the same off-by-one class this pilot keeps finding, and it would
have moved a gap from `NEIGHBOURHOOD` to `EDGE`.*

**So one third of the findings were invisible at edge scope.** Gaps 2 and 6 were reachable only by
holding a claim that neither endpoint references — and, since `pathograph.py` assembles edges from
declared wikilinks, that claim is one the graph does not connect to either side.

> 🔴 **ANNOTATION 2026-08-25, after Phase III — THE WORD "SETTLED" BELOW IS WRONG. DO NOT ACT ON IT.**
>
> *The text underneath is left exactly as written, per the precedent B set in its own Phase I: a
> finding annotated rather than revised, because erasing it erases the cause. The current version of
> this section lives in Scientist A's reconciliation, `af2f5e8` on `lettore`.*
>
> **What is wrong.** I measured **one** instrument failure — definability — and wrote that the
> `INSTRUMENT` axis was settled. That is a completeness claim and I measured nothing about
> completeness. **"Settled" is an instruction to stop looking**, sitting in a durable file, and a
> reader who reaches this artifact without also reaching `af2f5e8` receives the stop instruction and
> nothing else.
>
> **There are at least three independent instrument failures, not one:**
>
> | Axis | Failure | Found by |
> |---|---|---|
> | **Definability** | 3 of 4 relation tokens have no published semantics, so "does it fit" is unanswerable | this artifact, gap 4 |
> | **Expressiveness** | a fully-defined vocabulary still could not carry the hedge **"may"** in `claim_registry_current.md:289` — *"GSK3β hyperactivation **may** contribute to seizure susceptibility"* | Scientist A |
> | **Enforcement** | `pathograph.py:152–155` publishes a *negative* rule — an `ASSOCIATIVE` connective does not make an edge `ASSOCIATED` — re-emitted at `inventory:295` and unenforced, because validation is membership-only | Scientist B |
>
> Defining `ASSOCIATED` perfectly would not create an axis for hedging, and neither would enforce a
> prohibition the validator was never built to read. **The three are independent.**
>
> **And the expressiveness failure is a floor, not an asymmetry.** A framed it as edges lacking what
> nodes have. Measured across the export, `epistemic_type` is **absent from the schema** — the key
> is not present-and-empty, it does not exist — in every record kind but one:
>
> ```
> claim_node              n= 39   epistemic_type key present  39   non-empty  39
> relational_proposition  n=302   epistemic_type key present   0
> claim_edge              n= 20   epistemic_type key present   0
> claim_to_record_link    n=  8   epistemic_type key present   0
> ```
>
> The 302 relational propositions are the **candidate-edge population** — the raw material every
> future edge is drawn from. So typing the 20 current edges would not touch the 302 behind them:
> **the pipeline downstream of the node layer is epistemically flat.**
>
> **Why this error is worth more than its content.** It is the second completeness claim I published
> in this artifact, four paragraphs from the first — the amended edge-unit prediction directly above.
> I argued to the Orchestrator that an imprecise falsifiable claim in a durable file is expensive
> *because it directs someone else's work*, and then wrote "settled" in the same document. Once is an
> error. Twice is a habit, and it is not a habit about scope — **it is about asserting closure over a
> set I had enumerated myself.** That is the same shape as sweeping `^learning/`, as sweeping my own
> worktree, and as the `awk` terminator: **letting my own instrument define the population.**
>
> *(A footnote in the same key: verifying the table above, I first queried `record_kind` and got
> `n=0` for every kind, because these rows key it as `kind`. Both spellings exist in the export's
> namespace. I enumerated the key set and re-ran — the third time today I queried a value before
> enumerating the field, and the second time the false answer was a clean-looking zero.)*

**Restated, and this is the version to check:**

- **`INSTRUMENT` (gap 4) will recur on every edge.** Re-testing it adds nothing; it is settled.
- **`EDGE` (gaps 1, 3, 5) — my original prediction holds for these**, and only these: a second edge
  at the same depth should expose no further schema-shape gap of this kind.
- **`NEIGHBOURHOOD` (gaps 2, 6) — my original prediction was wrong.** A fresh neighbourhood may well
  force further gaps, because what is reachable one hop out is a property of *which* claims surround
  the edge, not of the schema's shape.

⇒ **The minimum unit that exposes this schema is `edge + one hop`, not `edge`.** A stress test scoped
to the edge alone would have returned four of six.

One consequence worth stating because it cuts in the Orchestrator's favour and against my own
framing: the cap was routed at *"the 016-035-036 neighbourhood"*, not at *"one edge"*. **That was the
right unit, and my argument for it named the wrong one.** I defended the cap on the ground that one
edge fully exposes the shape; the measurement says the neighbourhood does, and the routing already
had the neighbourhood.

What survives unchanged is the argument that mattered for declining the twelve: **volume inside an
unspecified instrument accumulates instances, not knowledge.** Twelve edges would multiply gap 4
twelvefold and add nothing to it.

**No schema change proposed. No field named. No token invented. No canonical file touched.**
