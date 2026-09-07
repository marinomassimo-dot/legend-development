---
record: PHASE V — FINAL SCIENTIFIC SYNTHESIS · PMID 32000863, the GSK-3β / lithium neighbourhood
id: FINAL_SCIENTIFIC_SYNTHESIS_PMID32000863_v1
producer: worktree `lettore` (mapped scientist-a), designated by Orchestrator
actor_status: NOT ACTIVATED — roles/scientist.md is PROPOSED; DEC-20260822 returns
  ACTIVATION_NOT_CONFIRMED. Operator-directed analytical pilot.
inputs: Phase IV — B at `98d176d`, C at `cfc54c1`; Phase III (B); Phase II (A, B, C);
  Phase I (A, B, C); schema gaps (C)
status: NON-CANONICAL. No canonical file written. No relation type written. No token invented.
  No BATCH_COMMIT.
dissent: PRESERVED, not resolved. Forced consensus prohibited and none applied.
---

# Final synthesis — and the finding that cost me my own contribution

> **Nothing here is medical advice.** Public, disease-level, de-identified.

## 0 · The correction that reorganises this document

**Scientist C rendered Wang 2012 at 300 dpi and found that Figure 1d has no GSK-3β row.**
I re-derived it independently before writing a word of this synthesis, from
`files/fulltext/PMID22193544_Wang2012.pdf`, sha256
`8f994f9542a7a37470b5e6edb8ad72a32e87633e0aef59119d1a393b2035174a`, page 2 at 300 dpi:

| Wang panel | Direction of WWOX | Rows present |
|---|---|---|
| **Fig. 1b** — RA time-course | WWOX **rising** | βIII-tubulin · cyclin D1 · WWOX · pTau S422 · pTau S396 · pTau S404 · Tau · β-catenin · phospho-β-catenin · **GSK3β** · **GSK3β pS9** · Actin |
| **Fig. 1d** — siRNA knockdown | WWOX **lost** | WWOX · pTau S396 · Tau · actin — **no GSK3β row, no pS9 row** |

The caption is why text alone could not settle it: panel (b) lists its antibodies explicitly
*"…phospho-GSK3bS9, GSK3b, b-catenin, phospho-b-catenin and actin"*, while panel (d) says only
*"the resulting cell lysates were subjected to western blot analysis."* **A reader working from the
text cannot distinguish "not measured" from "measured and not discussed."** C rendered the page. I
had not.

### What this does to my own contribution

My observation stands: the **S9A** mutant behaves like wild type, so Ser9 is **not required** for
GSK-3β's output onto Tau. **What does not follow — and I asserted it — is that losing WWOX leaves
Ser9 unchanged.** Ser9 is set by upstream kinases whether or not it gates the effect on Tau. Wang
never tested that direction.

⇒ **The "readout mismatch" is not a measurement contradicting a measurement.** It is Cheng's
*measurement* (pS9 falls under WWOX loss) set against a *prediction about the same quantity that
was never tested in that direction* — and the composed account used the untested prediction to
discount the measurement. My reconciliation's sentence *"losing the WWOX brake predicts raised
GSK-3β activity with Ser9 unchanged"* is **withdrawn.**

🔴 **The caveat four lines below it was already more correct than the sentence above it**
(reconciliation §121–124: *"both explanations remain available and are not mutually exclusive"*).
**The sentence is corrected to the caveat, not the caveat to the sentence.**

### What it cost the actor who found it, recorded because C stated it against itself

Without the exclusion argument, **C's metabolic route stops being the explanation left standing and
becomes one of two, neither excluded.** C found the fact that demotes C's own strongest
contribution, and said so rather than let it be found. That is the single best piece of conduct in
this pilot and it is recorded here as a result, not as a compliment.

---

## A · PRIMARY OBSERVATIONS

Bound to fingerprinted artifacts. Independently derived by the actors named; scope labelled.

**Cheng 2020** — XML `792b5b29…f00f5`, Fig. 7 PNG `ced68a66…62542`, supplement `0acb771c…8f7f`.

| # | Observation | Derived by | Scope |
|---|---|---|---|
| A-1 | LiCl 60 mg/kg × 3 within 1 h suppresses PTZ-evoked Racine score with the panel's marker in **`+/+`, `+/−` and `−/−` alike**; N 12/8 · 12/12 · 6/7; **no saline arm** | A, B, C | `EDGE` |
| A-2 | `****` is **undefined** — legend defines only `n.s.` and `***P<0.001`; the string occurs **0×** in the XML | A, B, C | `EDGE` |
| A-3 | Fig. 7c: pGSK3β(Ser9) 2.7·3.1·**1.3** \| 3.6·3.5·**2.0** \| 3.9·3.8·**2.5**; total GSK3β 2.2·2.4·2.4 \| 2.3·2.4·2.6 \| 2.2·2.4·2.6 | A (6×), B, C (3×) — identical to the last digit | `EDGE` |
| A-4 | **Total GSK-3β is flat**; what falls is inhibitory **Ser9 phosphorylation** | A, B, C | `EDGE` |
| A-5 | **The heterozygote is not intermediate** — at or above wild-type on the phospho row in every region | A, B, C | `EDGE` |
| A-6 | Panel c carries **no statistics of any kind**. Legend: *"The representative results of four independent experiments are shown."* | A, B, C | `EDGE` |
| A-7 | Panel c's own **`Wwox` row**: protein absent in `−/−`, **visibly reduced in `+/−`** — dosage visible in WWOX protein, absent in pSer9. *(Qualitative: that row carries no densitometry.)* | C first; A at 4× | `EDGE` |
| A-8 | Ethosuximide: `***` in `−/−`, **`n.s.` in `+/+` and `+/−`** — with the **larger** N in the control arms | A, B, C | `EDGE` |
| A-9 | Dosing is **not exposure-matched**: ETS **one** dose 150 mg/kg at −45 min; LiCl **three** doses of 60 mg/kg = **180 mg/kg cumulative** | C first; A verbatim | `EDGE` |
| A-10 | Statistics in full: **one-way ANOVA**, no interaction term, no post-hoc named, repeated measures treated as independent | A, B, C | `EDGE` |
| A-11 | **GSK-3β was never measured in any lithium-treated animal** | C (two surfaces, denominators), A, B | `EDGE` |
| A-12 | Cheng reports **no systemic covariate**: `blood glucose` 0 · `bicarbonate` 0 · `BUN` 0 · `creatinine` 0 · `hypoglyc` 0 · `acidosis` 0 · `serum` 0 · `body weight` 0 | C first; A on an independently derived surface (70 057 v 71 916 chars) | `EDGE` |
| A-13 | Fig. 7d magnitudes: `+/+` peak Δ ≈ **0.3–1.0** stages, confined to ~5 of 60 min, traces interleaving after; `−/−` peak Δ ≈ **2.0**, sustained. *(Read off the plotted axis; the paper tabulates none.)* | **A alone**, native res. | `EDGE` |
| A-14 | Results states **no result** for Fig. 7c; the Fig. 7 **title** asserts *"leads to"* and no panel under it tests it | **A alone** | `EDGE` |

**Wang 2012** — JATS `eb6f568d…8268`; PDF `8f994f95…5174a`.

| # | Observation | Derived by | Scope |
|---|---|---|---|
| A-15 | WWOX binds GSK-3β via an Axin-like motif at 388–407; **L404A abolishes binding**, L311A does not; interaction detectable between **endogenous proteins in mouse brain** | A (9/9 locators re-verified) | `EDGE` |
| A-16 | The **S9A** mutant decreases differentiation **exactly like wild type**; kinase-dead and R96A do not ⇒ Ser9 is **not required** for GSK-3β's output onto Tau | A first; **C verified at the source** | `EDGE` |
| A-17 | 🔴 **Fig. 1d (WWOX knockdown) carries no GSK-3β row and no pS9 row.** pSer9 is measured only in Fig. 1b, where WWOX **rises** | **C first**; A re-derived at 300 dpi | `EDGE` |
| A-18 | Wang contains **no seizure endpoint**: `seizure` 0 · `epilep` 0 · `convuls` 0 · `lithium` 0 · `LiCl` 0 across 49 334 non-abstract chars and the abstract | A first; **C verified at the source** | `EDGE` |

**Elsewhere in the model**

| # | Observation | Scope |
|---|---|---|
| A-19 | `CLAIM 036`: systemic constitutive null at **P18** — glucose 143.5 v 250.6 mg/dL (`p=0.000131`), bicarbonate 14.50 v 21.67 mEq/L (`p=0.006227`), BUN 37.25 v 17.67 mg/dL (`p=0.01086`), `n=3/3/4`, line EIIA-Cre `Wwox^ΔCre/ΔCre` | 🔴 `NEIGHBOURHOOD` |
| A-20 | `CLAIM 036` is referenced by **neither** endpoint of `016↔035`: 0 occurrences in `CLAIM 016`'s block, 0 in `CLAIM 035`'s body; positive control `CLAIM 035` appears 2× in `CLAIM 016` | 🔴 `NEIGHBOURHOOD` |

---

## B · AUTHOR INTERPRETATION

- Abstract: *"Inhibition of GSK3β by lithium ion significantly abolishes the onset of PTZ-induced
  seizure in Wwox−/− mice"* · *"targeting GSK3β with lithium ion ameliorates epilepsy."*
- Results, closing: *"these results suggest an important role of GSK3β in the hypersusceptibility to
  epileptic seizure induction due to Wwox loss in neuronal cells."*
- Discussion: *"its efficacy is better than the commonly used anticonvulsant drug ethosuximide"* —
  a cross-panel comparison for which no test is reported.
- Discussion, closing: *"**Future studies, as well as more evaluations, will be needed** to test
  whether GSK3β inhibitors may be promising candidates…"*

**The authors' own framing is weaker than the abstract's, and weaker than what downstream
representations have made of it.** Wang's authors claim neuronal differentiation and no disease.

---

## C · LEGEND LICENSED INTERPRETATION

**C-1 · `Wwox−/−` mice have a lowered seizure threshold.** `DATO`. Two convulsants, two strains,
spontaneous seizures from ~P12, status epilepticus in half the challenged nulls and in no control.

**C-2 · Lithium at 60 mg/kg × 3 raises the PTZ seizure threshold in mice.** `DATO`, all three
genotypes (A-1).

**C-3 · In `Wwox−/−` brain at P20, GSK-3β Ser9 phosphorylation is reduced while total GSK-3β is
flat.** `DATO`, with a declared statistical void (A-6). **The correct verb is *dis-inhibited*, not
*more abundant*.** Fairly stated, the abundance direction *is* upward by 9–18%, so *"elevated"* is
**unsupported and misdescribed, not disproven** — a correction all three of us converged on against
the team's collective lean.

**C-4 · WWOX is a direct, residue-mapped inhibitor of GSK-3β, and Ser9 is not required for that
output.** `DATO` **within Wang's system** (A-15, A-16), with *no WWOX-DEE allele tested* attached.

**C-5 · Genotype specificity is `NOT TESTABLE` in this design.** `INFERENZA`. Three verdicts, kept
distinct:

| | |
|---|---|
| **DEMONSTRATED?** | **No** — the discriminating test was not performed (A-10). |
| **CONTRADICTED?** | **No.** A-1 refutes only *"lithium acts only where WWOX is missing"*. It does **not** refute *"lithium acts more where WWOX is missing"*, and A-13 is visibly consistent with that. |
| **NOT TESTABLE?** | **Yes** — one-way ANOVA, no interaction term, repeated measures as independent, unequal N, no saline arm, floor in the control arms. |

A and B each first stated this too strongly and both withdrew; **C's formulation prevailed and is
adopted verbatim.**

**C-6 · Two live explanations of the Ser9 fall, neither excluded.** `INFERENZA`.
🔴 **This replaces the composed account of Phase III/reconciliation, which is withdrawn (§0).**

| | Explanation | Status |
|---|---|---|
| (i) | **WWOX-proximal** — loss of the docking-motif brake alters GSK-3β regulation, with Ser9 moving through some route | **Not excluded.** Wang never measured pSer9 under WWOX loss (A-17), so the prediction that Ser9 would stay put was never tested. |
| (ii) | **Systemic/metabolic** — Ser9 is the canonical insulin/IGF-1→PI3K→AKT output; the animal is hypoglycaemic, acidotic and uraemic in the same window (A-19) | **Not excluded**, untested, of high prior plausibility; different line and window (P14–P18 v P20). |

**What survives from the composition, and what does not:**

- ❌ **Leg A (S9A as exclusion)** — demoted. It shows Ser9 is *dispensable for the Tau output*, not
  that WWOX loss leaves Ser9 unchanged.
- ⚠️ **Leg B (readout mismatch)** — reclassified. It is a **registry-consistency observation**, not
  evidence about the mouse: `CLAIM 035` declares S9-independence and warns pS9 gives a false
  negative, while `CLAIM 016`'s principal molecular evidence *is* a pS9 western in that setting.
  Real, and about our model rather than about the biology.
- ✅ **Leg C (metabolic route)** — intact as an **alternative**, not as *the* explanation.
- ✅ **A-7 (dosage dissociation)** — intact and **independent of the S9A argument**: WWOX protein is
  dosage-graded, pSer9 is not. It constrains any stoichiometric model on its own evidence.

**C-7 · The bridge from `CLAIM 035` to `CLAIM 016` is a citation, not a measurement.** `INFERENZA`.
Cheng cites Wang and tests none of its mechanism; Wang measures no seizure endpoint (A-18).
**INFERENTIAL, not empirical.**

---

## D · NOT LICENSED

1. **A WWOX-specific pharmacological rescue.** Not demonstrated (C-5).
2. **GSK-3β as lithium's operative target here.** No target engagement was measured anywhere in the
   lithium arm (A-11); lithium is not selective; no second inhibitor and no genetic test was run.
3. **A mechanistic edge from GSK-3β state to the seizure phenotype.** Carried only by the lithium
   experiment, which is neither genotype-discriminating nor target-attributed.
4. **That the Ser9 fall is a WWOX-specific mechanistic signal.** Not excluded, not established
   (C-6).
5. 🔴 **That the Ser9 fall is *not* WWOX-proximal.** Equally not established. **This is the claim my
   own reconciliation came closest to making and it was not licensed.**
6. **Transfer to spontaneous seizures** — the phenotype that defines the human disorder, documented
   in this paper from P12 and never used as a drug endpoint.
7. **That ethosuximide is genotype-selective and lithium is not.** Confounded by exposure (A-9); the
   comparison is between panels with different control structures and was never tested.

---

## E · GRAPH CONTRIBUTIONS SUPPORTED

**None written to any registry. No token invented. No relation type applied.**

| Contribution | Basis | Scope |
|---|---|---|
| `CLAIM 016 ↔ CLAIM 035` is **`NOT_DIRECT`** — for this edge | the one published criterion, *"the same experiment measures both endpoints"*, fails by A-18 | `EDGE` |
| WWOX ⊣ GSK-3β, residue-mapped, Ser9-not-required | A-15, A-16, within Wang's system, *no WWOX-DEE allele tested* attached | `EDGE` |
| `Wwox` loss → seizure susceptibility | C-1 | `EDGE` |
| **No further token is assignable** to `016↔035` | three of four tokens have no published semantics | `INSTRUMENT` |
| The honest object is a **hypothesis**; the vocabulary has **no hypothesis tier**, so assigning nothing is *faithful*, not abstentive | C's residue, adopted | `INSTRUMENT` |

🔴 **Scope warning that must travel with these.** The argument that decided this edge depends on
`CLAIM 036`, which **neither endpoint references** (A-20). Since the layer assembles edges from
declared wikilinks, `CLAIM 036` is not one hop away *in the graph* — it is outside the graph's reach
from that edge entirely. **A reader arriving here through the graph cannot reconstruct the argument
that decided it.**

---

## F · GRAPH CONTRIBUTIONS NOT YET SUPPORTED

| Item | Why not |
|---|---|
| `GSK-3β state → seizure phenotype` as a mechanism edge | D-3 |
| `CLAIM 016 ↔ CLAIM 036` | Not an edge in the graph at all (A-20), while being load-bearing for both endpoints' interpretation |
| A causal type for `016 ↔ 035` | Requires F-1 (§I) — no existing evidence can supply it |
| 🔴 **`NOT_DIRECT` as a general result across the twenty edges** | **Refuted for at least three.** `PAPER 041` = PMID 29808465, registry `Evidence depth: abstract only — full text paywalled`, no PMCID, and it is the shared paper on exactly three edges — `019↔030`, `019↔032`, `030↔032` — verified by me from the export, with the 17/3 split reproducing at 17 of 20. **You cannot establish what a paper does not measure when you cannot read its experiments.** There `NOT_DIRECT` is **undetermined**, not decided-negative. C checked 3 of 17 and claims only that *"all twenty"* is false, which one counter-example settles. |

---

## G · THERAPEUTIC INTERPRETATION

🔴 **This node does not open a repurposing entry, and the reasons have strengthened.**

Track C requires four things to hold together: WWOX function, a **signed** pathway direction, a
proximal Tier 1/2 readout, and CNS/paediatric safety. **At least three fail.**

- **Direction is unsigned.** Target attribution failed (D-2), and after §0 the *sign* of the Ser9
  change relative to WWOX loss is itself contested (C-6).
- **No proximal readout exists.** GSK-3β was never measured in a treated animal (A-11), and the one
  molecular readout in the paper is the one under dispute.
- **The efficacy claim is smaller than it reads.** A-13: the wild-type effect is ~0.3–1.0 stages over
  five of sixty minutes. **A genuinely non-specific anticonvulsant effect is a *weaker* rationale
  than a specific one, not a stronger one.**
- **Safety.** Lithium in a paediatric DEE population carries a narrow therapeutic index and renal,
  thyroid and dehydration-interaction risk — and seizures cause dehydration.

**Nothing here is a candidate treatment, and nothing here is medical advice.** It remains a
hypothesis in the discovery and hypothesis ledgers, which is where the model already places it.

---

## H · CONTRADICTIONS / CAVEATS

1. **Text narrower than panel.** Legend and Results name only `Wwox−/−` for lithium; the panel marks
   all three genotypes.
2. **Text empty where the panel carries the evidence.** Results states no result for Fig. 7c (A-14).
3. **Title stronger than every panel.** *"…leads to…"* (A-14).
4. **Caption silent where it must be explicit.** Fig. 1d's caption lists no antibodies, so **the text
   cannot distinguish "not measured" from "measured and not discussed"** (§0). This is the caveat
   that changed the conclusion, and it was reachable only by rendering the page.
5. **A metric with no defined threshold.** `****` (A-2).
6. **A confound the paper does not mention.** No systemic covariate anywhere (A-12), in a model the
   paper itself says *"succumb[s] to death by 4 weeks."*
7. **Cross-panel comparison presented as a result.** *"its efficacy is better than… ethosuximide"*,
   untested, across arms differing in dose, schedule, N and control structure (A-9).

---

## I · FALSIFIERS / NEXT EXPERIMENTS

**Adjudicated, not averaged.** B ranked F-3 first; C refused that and ranked F-1. **I rank F-1
first, and B's argument — correct in itself — does not promote F-3.**

### 🔴 F-1 · The L404A knock-in — first, and the only one neither confounded nor partial

Knock **L404A** — the allele Wang shows abolishes WWOX–GSK-3β binding (A-15) — into the mouse;
challenge with PTZ.

- Seizure-susceptible with total WWOX intact → the GSK-3β arm carries the phenotype, and the edge
  earns a causal type.
- Not susceptible → the seizure phenotype runs through something else in WWOX, and the edge is
  bibliographic.

**Why it ranks first, on a property neither alternative has:** it manipulates the *mechanism* rather
than measuring a correlate, and **an L404A knock-in with total WWOX intact need not be systemically
ill** — so it is untouched by the confound that compromises the other two. It uses the mechanism
paper's decisive reagent against the phenotype paper's endpoint: **the one experiment neither paper
could have run alone.** C's proposal; neither other actor reached it.

### F-2 · Reproduce the confound — sound in one direction only

Measure brain pGSK3β(Ser9) in a **non-`Wwox` model of comparable systemic illness at P20**.

- **Negative arm is sound:** Ser9 **holds** under matched illness ⇒ the systemic route is excluded.
- **Positive arm is not:** Ser9 falls there too ⇒ systemic illness is *sufficient*, which never
  establishes *attribution*. **B is right**, and C conceded that half — the over-strong wording was
  C's own. **Asymmetric, not invalid.**
- *This still supersedes the pair-fed design all three of us first proposed: reproducing a confound
  and seeing the effect is stronger than removing it and seeing nothing.*

### F-3 · The S9-independent substrate readout — demoted, and it was mine

Measure GSK-3β output by phospho-Tau S396/S404 — Wang's own substrate pair — in `Wwox−/−` brain.

🔴 **C's objection, which I accept:** pTau S396/S404 is reported to rise under hypothermia and
metabolic stress via PP2A inhibition, so a cachectic, hypoglycaemic P20 mouse is **predicted to read
as "the Wang mechanism operates in vivo"** whether or not it does. *I did not verify that literature
claim from a primary source and record it as C's, with C's own `PREMISE: DEFAULT_FROM_TEXTBOOK`
tag.* **The structural half I can adjudicate and it is sufficient on its own:** my selling point was
that it *"uses tissue the original study already collected"* — and that tissue comes from the
confounded animals, so **the design inherits the confound it was proposed to resolve.** An economy
argument, and the economy is the defect.

### F-4 · For genotype specificity

A PTZ + lithium arm with an **explicitly tested genotype × treatment interaction**; a structurally
unrelated GSK-3β inhibitor at **matched cumulative exposure and schedule**; a post-treatment
target-engagement western; a saline arm; endpoint **spontaneous** seizures on video-EEG.

### F-5 · For the exposure confound

ETS and LiCl at matched cumulative dose and schedule, in **one** experiment, one control arm.

---

## J · OPEN DISAGREEMENTS

**Preserved. None resolved by majority; none averaged.**

**J-1 · 🔴 Is the Ser9 fall WWOX-proximal or systemic? — OPEN, and it moved during this pilot.**
It entered as *"three findings point away from the WWOX-proximal reading"* and leaves as **two live
explanations, neither better evidenced than the other** (C-6). Per B and unrebutted: **L-1 moves.**
One decisive experiment exists (F-1); nobody has run it; **and the original study had the tissue.**

**J-2 · Does the ETS genotype restriction survive exposure matching? — UNTESTED.** C records this as
a standing disagreement with the **canonical evidence boundary**, *"which is not a peer and cannot
concede"*. Preserved in C's words.

**J-3 · Is the `INSTRUMENT` axis settled? — I DISAGREE WITH C.** C declared gap 4 settled. Measured
from the export the layer emits: `claim_node` carries `epistemic_type`; **`claim_edge` carries no
epistemic field at all** — the `review_packet` carries the *endpoints'* tiers, never the relation's,
so a relation asserted as `IPOTESI` and one asserted as `DATO` serialise identically. **This is not
gap 4** — gap 4 is definability, this is expressiveness, and a fully-defined vocabulary would still
be unable to hold the *"may"* in `CLAIM 016`'s own title. **The instrument has at least two
independent failure modes and was enumerated once.**

**J-4 · Breadth versus depth.** B eleven edges, A one at depth, C zero. Bounded by two facts: my
dispatch carries **no cap**, so my count is a declared unfinished task, not restraint; and volume
inside an unspecified instrument multiplies gap 4 rather than adding knowledge.

**J-5 · 🔴 UN-ATTACKED — no actor was positioned to review these.** B originated R-3 and R-4; C
recused under the symmetry rule; I am the synthesiser and putting me in the reviewer's seat one step
later would reproduce the routing defect B already found. **These two items have been reviewed by
nobody and are marked as such rather than folded into a reviewed layer.** An honest gap is a result;
a laundered one is the failure this run has spent itself cataloguing.

**J-6 · Recorded, not acted on — two recusal criteria that did not match.** B diagnosed my position
with a **having-been-corrected** criterion while recusing itself on a **having-originated** one. B
was corrected by C three times and by me twice. **C is explicitly not asking B to recuse further and
calls B's attacks on C among the best in the review.** The finding is about the record: two criteria,
each applied in the direction that favoured the actor choosing it, and nothing required them to
match. C's catch; it stands.

---

## K · CANONICAL DEFECTS DISCOVERED — NOT PROPAGATED

All require `BATCH_COMMIT` and the Operator. **No edit was performed.**

| # | Object | Defect | Class |
|---|---|---|---|
| K-1 | `CLAIM 016`, Evidence boundary | cites **Fig. 7b** for a **Fig. 7d** result — *"the pointer routes a verifier to the refutation of the claim it anchors"* (C's formulation). Read charitably so 7b governs only the ethosuximide clause, **the lithium assertion is left with no figure locator at all.** Defective either way | MINOR |
| K-2 | `CLAIM 016`, `Summary` + `Type` | *"GSK3β è elevata"* / `DATO (abbondanza)` contradicted by the same record's later block; a graph materialiser reads the superseded field | MINOR |
| K-3 | `CLAIM 016` ↔ `CLAIM 036` | do not reference each other, though `CLAIM 036` is a declared cross-cutting design constraint on exactly the window and model `CLAIM 016`'s datum comes from — **and it is now load-bearing for both live explanations** | MINOR |
| K-4 | `CLAIM 016` ↔ `CLAIM 035` | hold an unresolved readout tension with no comment | MINOR |
| K-5 | `fulltext_read_receipts.jsonl` | **22 of 128** legacy reconstructions whose `evidence_basis`, `source_locator` **and** `outputs` are all one registry line, `source_fingerprint: null`, `evidence_depth: partial_fulltext_read` — **each contradicts the registry it appears to corroborate.** *(Not 23: `FTR-20260806-23446842-02` is a `receipt_invalidation` whose locator points at the registry because the registry entry is what it makes a statement about; counting it files a repair as a defect. Four further null-fingerprint receipts are honest contemporaneous records.)* | **MAJOR candidate** |
| K-6 | `deepdive_manifests/PMID32000863.json` entry `[0]` | declares `surface: body` for a proposition its quoted caption does not contain | hygiene |

### 🔴 K-2's provenance is the finding, and both B's list and my reconciliation had it wrong

Verified: `disease-models/wwox/analysis/locator_contract_live_test.md:387`, tracked since
**2026-08-04T20:32:01+02:00** (`3cfd451`):

> *"GSK3β is **dis-inhibited, not more abundant.** CLAIM 016's Summary says "GSK3β is elevated",
> which reads as abundance. **→ commit candidate: correct to *activation*.**"*

**Neither B nor C originated it. Neither did I.** The system found the defect, wrote the remedy,
and lost it — **and three weeks later two Scientists recorded it as a discovery, and a third
reconciled it as one.** The attribution is corrected here.

**The provenance is worth more than the defect.** A written, correct, actionable commit candidate
sat in a tracked file for three weeks and reached nobody. That is not a reading failure and not a
discipline failure; it is a **propagation** failure, and it is the same class as K-3 — a fact
correctly recorded in a place from which nothing carries it to where it is needed.

---

## THE DELTA — the row the form could not hold

My reconciliation's delta table has rows for `RETRACTED`, `WEAKENED`, `STRENGTHENED`,
`REFORMULATED`, `CORRECTED` and `STRUCK`. **The word `attribution` occurs 0 times in it.** C's R-6
is right, and its diagnosis is right too: this is not concealment. **The table has rows for
measurement errors and for position changes and no row for attribution**, so B's voluntarily
disclosed fifth error had nowhere to go. **Same shape as C's own gap 2 — a fact with nowhere to go
in the form built to hold it.** Being *"different in kind"* is exactly why the table could not hold
it.

**ATTRIBUTION — added**

| Item | Recorded as | Actually | Disclosed by |
|---|---|---|---|
| The *"elevated → activation"* commit candidate | a B and C discovery; carried as such in my reconciliation | **originated by the repository itself**, `3cfd451`, 2026-08-04 | Orchestrator; verified here |
| B's own attribution error | omitted from B's four-item error record | B's fifth error | **B, voluntarily** — and it was dropped by the form, not by B |
| A-7, A-9, A-12, A-17, F-1, F-2 | — | **C's**, and A-17 and F-1 are the two that most changed this synthesis | C |
| A-13, A-14, A-16 | — | **A's**, single-actor, un-re-derived by any peer | A |
| The readout mismatch | — | **B's**, and now reclassified from evidence to registry-consistency | B |

### What this pilot changed, in one line

It entered with a composed three-legged account that made the metabolic route the explanation left
standing. **It leaves with two live explanations, neither excluded, one decisive experiment that
nobody has run, and the tissue for a weaker version of it sitting in a 2020 study.** The account got
smaller and the reason for it got harder to overturn.

---

## OBSERVATION_SCOPE

- Phase IV halves read in full (B `98d176d`, C `cfc54c1`), plus all Phase I–III artifacts.
- **Wang 2012 page 2 re-rendered by me at 300 dpi** from PDF `8f994f95…5174a` before accepting A-17.
  Crop recipes, all re-executable: `fig1d` (480,2250,1250,2680) ×2 →
  `d113be760a3940711a9c24cc18cc2b55c34171e0f7a02f02ecdacedbeb547b36`; `fig1b_rows`
  (1250,1000,1950,1760) ×2 → `86a23c9249479fc39e007e330fe59af121e5363dece2f93b32c9e0c975484499`.
  Crops written outside the repository — derivation published, reproduction not shipped.
- Wang artifacts read from the **shared checkout**; they are absent from this worktree.
- Every peer claim adopted here was re-derived or re-verified by me first; each says which.
- **Not verified by me:** the pTau/PP2A/hypothermia literature behind C's objection to F-3. Recorded
  as C's, with C's tag. The structural half of that objection I did adjudicate.
- R-3 and R-4 are `UN-ATTACKED` and are marked, not folded (J-5).
- Nineteen of twenty edges remain unadjudicated; twelve are adjudicable today. **A task, not a scope
  boundary.**
- No canonical file written. No relation type. No token invented. No `BATCH_COMMIT`.

---

*Non-canonical. Nothing here is medical advice. This synthesis is not canonical until the
applicable review and integration workflow accepts it.*
