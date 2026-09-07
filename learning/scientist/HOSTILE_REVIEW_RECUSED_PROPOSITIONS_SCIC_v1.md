---
record: PHASE IV (partial) — hostile review of the propositions Scientist B recused to me
id: HOSTILE_REVIEW_RECUSED_PROPOSITIONS_SCIC_v1
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
date: 2026-08-25
reviewed_object: SCIENTIST_TEAM_RECONCILIATION_PMID32000863_v1.md, commit af2f5e8 on lettore,
  sha256 e01636acb116d443f9a62a291d4887bcb24bb1d410d74a9e3e64e4b92a47d74a — verified by me
recusal_list: HOSTILE_SCIENTIFIC_REVIEW_PMID32000863_v1.md §1, commit 98d176d on lettore-b
status: NON-CANONICAL. Mutates nothing. No peer artifact edited.
---

# Hostile review of R-1 … R-7 — and the one that needed a figure, not an argument

> **Nothing here is medical advice.** Descriptive sections only; no governed verdict token is used.

---

## 1 · Recusals under my own symmetry rule, applied before anything else

I asked that the rule be symmetric and I am the first person it costs. Where a proposition B
originated was **co-originated with or adopted from me**, my attack is worth less than B's and I
flag rather than review.

| | Disposition |
|---|---|
| **R-3** — defect candidate 4, the `CLAIM 016`/`CLAIM 035` readout tension | 🔴 **RECUSED.** B's own list says *co-originator with C*. This is my Phase I D-4. I cannot be its hostile reviewer. |
| **R-4** — defect candidate 2, `CLAIM 016`'s `Summary`/`Type` contradiction | 🔴 **RECUSED.** B's list says *co-originator with C*. This is my D-2. |
| **R-2** — the 22-receipt class | **PARTIALLY RECUSED.** B originated the surfaces-disagree finding (§3.3) and I review that. The receipt-class layer on top is composite — the phrase *self-warranting set* is mine and the 23→22 cut is A's — and I do not review that layer. |
| **R-7** — `NOT_DIRECT` decidable for all twenty edges | **PARTIALLY RECUSED.** The *principle* — that `NOT_DIRECT` is decidable against the one published criterion — is my C1. The *extension to all twenty* is B's, and only the extension is reviewed below. |
| R-1, R-5, R-6 | Reviewed. |

🔴 **A correction to R-4's attribution that neither B nor the reconciliation carries.** B lists it as
co-originated by B and me. **Neither of us originated it.**
`disease-models/wwox/analysis/locator_contract_live_test.md`, tracked at 2026-08-04T20:32:01,
lines 384–387, states it with a drafted remedy: *"'Elevated' is the wrong word … GSK3β is
**dis-inhibited, not more abundant.** `CLAIM 016`'s Summary says *'GSK3β is elevated'*, which reads
as abundance. → commit candidate: correct to activation."* **The repository originated it, wrote the
fix, and did not apply it.** Two Scientists later re-derived it and both recorded it as a discovery.
That is a stronger finding than the defect: the system found this, solved it, and lost it.

---

## 2 · R-1 — the load-bearing one. The leg does not fall; it demotes, and B's self-attack understates it

**The proposition.** I-6's B row: *`CLAIM 035` declares WWOX's inhibition S9-independent and warns
pS9 gives a false negative; `CLAIM 016`'s principal molecular evidence is a pS9 western in that
setting.*

**B's stated self-attack**, which I was asked to judge: *the mismatch is between two claim* records*,
not two experiments; it establishes the canonical model is internally inconsistent, and nothing by
itself about what Cheng measured.*

**That is correct and it is not the strongest attack available. Here is the stronger one.**

### 2.1 New primary evidence — and only the panel could settle it

`CLAIM 035`'s warning is that a pS9 western gives a **false negative under WWOX loss**. I went to
Wang 2012 to find where pS9 was measured under loss.

The Results sentence reports pS9 inside the **retinoic-acid time-course**, where WWOX is *rising*:
*"We found that the phosphorylation levels of phospho-GSK3β S9 and phospho-β-catenin remained
normal."* The very next sentence introduces the knockdown: *"SH-SY5Y cells in which WWOX expression
was reduced by RNAi showed increased pTau S396 levels and notably decreased neurite outgrowth"* —
**pTau only. No pS9.**

The caption for the knockdown panel does not enumerate its blots — *"the resulting cell lysates were
subjected to western blot analysis"* — so **the text cannot settle whether pS9 was measured there
and merely not discussed.** I rendered the page from `PMID22193544_Wang2012.pdf` at 300 dpi and read
the panels:

| Panel | Condition | Rows blotted |
|---|---|---|
| **Fig 1b/1c** | RA time-course, **WWOX rising** (WWOX row rises across days 0–4; 1c plots it to ~8.5) | βIII-tubulin · cyclin D1 · WWOX · pTau S422 · pTau S396 · pTau S404 · Tau · β-catenin · phospho-β-catenin · **GSK3β** · **GSK3β pS9** · actin |
| **Fig 1d** | **WWOX knockdown** — mock, Si1+3, Si1, Si3 | WWOX · pTau S396 · Tau · actin — **no GSK3β row, no pS9 row** |

⇒ **Wang 2012 never measures pSer9 under WWOX loss.** pS9 is flat in the gain direction and is
**not blotted** in the loss direction.

### 2.2 What that does to the leg

`CLAIM 035`'s warning is therefore **an extrapolation from a gain-of-function time-course to a
loss-of-function prediction**, not a measured result. So the "mismatch" is not between two findings.
It is between:

- a **measurement** — Cheng's pS9 fall under *Wwox* loss, and
- a **prediction** — `CLAIM 035`'s warning about pS9 under WWOX loss,

**both concerning the same quantity, of which only Cheng has ever measured it.** The canonical model
uses the untested prediction to discount the measurement, and the prediction is the weaker object.

### 2.3 A's S9A result does not rescue the premise, and this is the part I expected to fail and did not

I-6's composed sentence is: *"losing the WWOX brake predicts raised GSK-3β activity **with Ser9
unchanged** (A). Cheng observed Ser9 changed. So the observed event is not the signature of the lost
brake (B)."*

A's O-14 establishes that **Ser9 is not required for GSK-3β's differentiation output** — S9A behaves
like wild type. That is a real, designed result and I verified it at the source myself.

**It is a different proposition from the one the composed sentence needs.** "Ser9 is not required for
GSK-3β's output" does not entail "losing WWOX leaves Ser9 unchanged". GSK-3β's Ser9 can be set by
other inputs — AKT among them — whether or not Ser9 gates its effect on Tau. **Nothing in either
paper licenses the premise in the loss direction.**

### 2.4 Answer to B's question — three legs or two?

**The B leg does not fall. It demotes, and its mechanistic force was never its own.**

- What survives of R-1 is a **registry-consistency observation**: two wikilinked canonical claims
  disagree about what the key measurement means. Real, and a finding about the model.
- The **mechanistic** force in I-6 comes from A's O-14, which is already a separate leg. It does not
  double.

⇒ **I-6 has two independent legs and one registry observation, not three independent legs.** And its
first clause rests on an untested extrapolation.

### 2.5 🔴 The cost falls on my own leg, and I would rather state it than have it found

If the "Ser9 should have been unchanged" premise is untested, then I-6's exclusion argument does not
run, and **my C leg stops being the explanation left standing after the alternatives are removed.**
It becomes one of two available explanations, neither excluded. My metabolic route is *weaker in its
role* after this attack than before it, and the attack is mine.

Note where that lands: A's own caveat at §121–124 — *"this does not refute the observation and does
not refute `CLAIM 016`. Both explanations remain available and are not mutually exclusive"* — is
**more correct than A's composed sentence four lines above it.** The caveat and the composition are
inconsistent, and the caveat is the one to keep.

---

## 3 · R-2, R-5, R-6, R-7

### R-2 — B's surfaces-disagree finding: the attack fails, B is right

I checked the half that is B's. `reading_state.md` returns **`partial_fulltext_read` for all four**
PMIDs (24369382 · 24456803 · 30361190 · 27495153) against a paper registry declaring
`full text reviewed`. **The surfaces do disagree. I found nothing to attack and record that.**

### R-5 — L-5 / L-6, closed by concession

I have no evidence-based attack. One structural note, offered as an observation rather than a
finding: §9 of the dispatch says *do not erase the dissent trail*, and two dissent items closed by
concession are the case where erasure is most tempting and least visible, because nobody objects.
**I did not read B's Phase III trail in full and I am not scoring this.**

### R-6 — B's own error record is incomplete, and the reason is structural rather than evasive

The delta table's B rows carry four errors: the 2/9 retraction, `INDIRECT_…` → `ASSOCIATED` → also
withdrawn, *"disproven"* → *"unsupported"*, *"already corrected"* → *"half-corrected"*.

**A fifth is missing.** B published a causal explanation of *why I missed its pilot* — that my sweep
predated its commit — without running the commands that would settle it. Grepped the reconciliation
for it: **0 occurrences.**

🔴 **This is not B concealing it — B disclosed it voluntarily and asked for a ruling on the timing.**
The finding is that it **did not reach the durable record**, and the reason is that the delta table
has rows for *measurement* errors and *position* changes and **no row for an attribution error**.

That is the same shape as my own gap 2: **a fact with nowhere to go in the form that was supposed to
hold it.** A voluntarily disclosed error fell out of the record because the record had no category
for its kind. The Orchestrator recorded it separately and called it *"different in kind"*, which is
exactly the diagnosis — and being different in kind is precisely why the table could not hold it.

### R-7 — `NOT_DIRECT` decidable for all twenty edges: **refuted for at least three**

Reviewing the extension only; the principle is mine and recused.

The one published criterion is `DIRECT — the same experiment measures both endpoints`. Deciding
`NOT_DIRECT` therefore requires establishing that **no single experiment measures both** — which for
an edge with a shared paper means reading that paper for both endpoints, exactly the zero-count work
A did on Wang for one edge.

Measured from the export, `review_packet.shared_evidential_papers`:

```
edges with no shared paper   3   -> NOT_DIRECT decidable trivially
edges with a shared paper   17   -> requires reading that paper for BOTH endpoints
```

*(17/3 independently reproduces the packet's expected split.)*

🔴 **`PAPER 041` is the shared evidential paper for three of the seventeen** — `019↔030`, `019↔032`,
`030↔032` — and the registry records its `Evidence depth` as **`abstract only — full text
paywalled`**.

**You cannot establish that a paper does not measure both endpoints when you cannot read its
experiments.** For those three edges `NOT_DIRECT` is not decided — it is **undetermined**, which is a
different state, and it is the same distinction this pilot has enforced throughout: *no criterion* is
not *no fit*, and *not readable* is not *decided negative*.

The extension is refuted for at least three of twenty. I did not check the remaining fourteen and do
not claim they are decidable either; **I claim only that "all twenty" is false**, which one
counter-example settles.

---

## 4 · Is B's line drawn too narrow? — yes, by B's own mechanism

B recused what it **originated** and said recusing from everything it touched would empty the review.
As a bright line that is defensible, and B drew it wide within it.

🔴 **But B applied a different criterion to A than to itself.** B's §4, answering L-7, diagnoses A:

> *"The mechanism is routing, not care. … **An actor corrected by C three times is the worst-placed
> actor to challenge C's fourth claim.**"*

That criterion is **having been corrected**, not **having originated**. Applied to B: B was corrected
by me on the exposure confound (accepted, *"C is right"*), on the Q1/Q2 formulation (adopted mine),
and on *"already corrected"* → *"half-corrected"*; and by A on the 2/9 retraction and the edge type.
**By B's own mechanism, B is poorly placed to challenge propositions originating with A and with
me** — and B challenged several, including two of mine.

**I am not asking B to recuse further.** B is right that it would empty the review, and B's attacks
on my propositions are among the best in it. The finding is narrower and it is about the record:
**B used the favourable criterion for itself and the unfavourable one for A, and nothing in the
process required the two to match.** Whichever criterion is right, it should be one criterion.

---

## 5 · Answering B's attacks on my own propositions

Outside my assigned scope; the Orchestrator asked me to answer them and they are aimed at me.

### 5.1 F-2 demoted below F-3 — I concede half, and the other half is a defect in F-3

**Conceded.** B: *"a positive control demonstrates sufficiency, never attribution."* My positive arm
read *"Ser9 falls there too → the Cheng observation is a readout of terminal illness; `CLAIM 016`'s
core datum loses its mechanistic reading."* **That does not follow.** Sufficiency in a sick non-*Wwox*
animal leaves WWOX-proximal de-repression free to operate additionally in the null. My arm assumed
an exclusivity I-6 explicitly disclaims. B is right and the wording was mine.

**Not conceded: the whole design.** F-2 is **asymmetric, not invalid.**

- **Negative arm — sound.** Ser9 *holds* under matched systemic illness ⇒ systemic illness is not
  sufficient ⇒ the route is excluded. Necessity fails, and exclusion follows.
- **Positive arm — over-read**, exactly as B says.

So F-2 is informative when it returns negative and over-claimed when it returns positive. **B
discards the design; the correct repair keeps the arm that works and rewrites the one that does
not.** That is a smaller correction than a demotion and it preserves a test nothing else supplies.

**And F-3 has a defect B did not weigh.** F-3 reads GSK-3β output through pTau S396/S404 in
`Wwox−/−` brain, and its discriminating arm is *"substrate output raised with Ser9 held constant"*.

1. **In Cheng's animals Ser9 is not held constant — it falls.** The clean arm's condition does not
   obtain in the tissue F-3 proposes to use.
2. 🔴 **pTau S396/S404 is not a clean readout in a systemically ill animal.** Tau phosphorylation at
   those sites rises under hypothermia, anaesthesia and metabolic stress, largely through PP2A
   inhibition, and is also driven by CDK5. A cachectic, hypoglycaemic P20 mouse is predicted to show
   raised pTau **for reasons that have nothing to do with WWOX** — which F-3 would read as *"the Wang
   mechanism operates in vivo"*. **F-3's discriminating arm is confounded by the very systemic
   illness it is meant to discriminate against.**
   *`PREMISE: DEFAULT_FROM_TEXTBOOK` — this is general biochemistry, not something I measured in
   either paper. Tagged, per §5.2 below.*
3. *"Uses only tissue the original study already collected"* is an economy argument, not an
   inferential one — and that tissue comes from the confounded animals, so reusing it **inherits**
   the confound.

**My position:** F-3 is cheaper and is not cleaner. F-2's negative arm and F-3 are both confounded or
partial; **F-1, the L404A knock-in, is the only proposal on the table that is neither**, and B
explicitly declined to touch its ranking. I do not contest F-3 rising above F-2 as stated — my stated
F-2 deserved the demotion — but the ranking should record that F-3 is confounded rather than
"decides the central claim".

### 5.2 B §2.8 — conceded without qualification

*"Ser9 is the canonical output of insulin/IGF-1 → PI3K → AKT"* is mine, it is textbook physiology
imported to license a causal route in specific animals, neither paper measures AKT or insulin, and I
did not tag it. **The repository has `PREMISE: DEFAULT_FROM_TEXTBOOK` and applies it to weaker
premises than this one.** It should carry the tag. B found it; I had reached the same conclusion
while testing F-3 above, which is why the F-3 objection is tagged — and reaching it independently is
not a mitigation, because I published the untagged version first.

---

## 6 · What I did not examine

- I did not read B's Phase III dissent trail in full; R-5 is unscored, not cleared.
- I did not check 14 of the 17 shared-paper edges for R-7. I claim only that "all twenty" is false.
- Fig 1b's pS9 row was read as **present/absent and flat**, from the 300 dpi page render; I did not
  densitometrically quantify it, and 1c's plotted line is the paper's own quantification, not mine.
- R-3 and R-4 are recused, so the two defect candidates most closely tied to my own Phase I work are
  **un-attacked by anyone**. That is a real hole and it is the price of the symmetry rule. It should
  be routed to A or recorded as un-attacked rather than left looking reviewed.
