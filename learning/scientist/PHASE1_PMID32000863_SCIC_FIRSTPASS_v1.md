---
artifact: SCIENTIST-C PHASE I FIRST-PASS — independent adjudication, PMID 32000863
actor_id: scientist-c
worktree: lettore-c
date: 2026-08-25
authority: OPERATOR-DIRECTED ANALYTICAL PILOT — the scientist role contract is PROPOSED, not binding
canonical_mutation: NONE. This is a work artifact. No canonical file is edited by this reading.
status: NON-CANONICAL
---

# PHASE I — SCIENTIST-C FIRST-PASS

## 0 · Authority actually held

`roles/scientist.md` front-matter, read this session, states:

```
status: PROPOSED — binding once Mirror hostile review passes and the operator approves
actor_id_status:
  scientist-c: PROPOSED — confirmed at its own registration (Annex I.2 step 7, PID-12)
```

`scientist-a` and `scientist-b` are `FIXED` on canonical execution of `CAND-20260818-SCIENTIST-AB-SPEC`.
**`scientist-c` is not.** The contract itself says so, and
`framework/protocols/scientist_reading_modes.md` is declared to leave `scientist-c` untouched.

Therefore, per the task's own IMPORTANT AUTHORITY CONDITION, and recorded explicitly:

- I did **not** self-activate the Scientist role contract. This prompt does not activate it and I
  have not treated it as activated.
- I hold **no** `ORCHESTRATOR_LEASE` and did not consult one as authority. `runtime/orchestrator_lease.md`
  shows the last five records all terminal (`STALE`/`RELEASED`/`EXPIRED`), none `ACTIVE`.
- I operate as an **Operator-directed analytical pilot**, within the authority the task grants:
  read primary evidence, adjudicate, record. Nothing else.
- No `TASK_ACK` / `TASK_CLAIM` was issued, because the Task Contract machinery belongs to the
  contract that is not yet binding. Recording this rather than performing a claim I am not
  authorized to make.

**Nothing here is medical advice.**

---

## 1 · Independence — declared honestly, including where it is imperfect

**What I did not read:** no artifact authored by `scientist-a` or `scientist-b`. I established by
filename only (never by content) what exists — see §3. `learning/scientist-b/SLR-scientist-b-0001.md`
exists on `refs/heads/lettore-b`; I did not open it, and it is a Session Learning Review, not a
PMID 32000863 pilot.

🔴 **ANCHORING HAZARD — DECLARED, NOT MINIMIZED.** I read
`disease-models/wwox/research/deepdive_manifests/PMID32000863.json` **before** forming my own
conclusions. I opened it to answer a logistics question — *are the primary artifacts reachable at
all, and under what paths and fingerprints* — and it turned out to contain a complete prior
adjudication of the very questions I was assigned, including the Figure 7d and Figure 7c readings.

This is a real contamination of my independence and I will not pretend otherwise:

- It is **not** another Scientist's Phase-I artifact. It is committed canonical repository state,
  present in all 57 refs, dated 2026-08-04 and audited 2026-08-10. §5 of the task *requires* me to
  record the current repository assertion, so reading it was mandated. But I read it earlier than
  I needed to, and I read the conclusions when I only needed the `source_artifacts` block.
- **Mitigation actually performed, not merely claimed:** every load-bearing observation below was
  re-derived from the primary artifacts at native resolution and is reported with my own measured
  values. Where I merely confirm the manifest, I say *confirms*. Where I found something it does
  not contain, I say *not in the manifest*. Readers should weight the confirmations lower than the
  novel findings, because the confirmations are the ones I could have been led to.
- **Process lesson, for §13:** a manifest that co-locates artifact fingerprints with adjudicated
  conclusions cannot be consulted for provenance without leaking conclusions. The
  `source_artifacts` block should be independently readable. Recorded as a contract finding.

---

## 2 · Workset — RE-MEASURED, and it does not exist

§4 directs me to the Pathograph inventory and says to re-measure rather than inherit the
"~20 edges / ~17 with a shared paper / ~3 without".

**Measured. The Pathograph is not present in this repository.**

| Surface searched | Denominator | Hits |
|---|---|---|
| Working tree, case-insensitive `pathograph`, excluding `.git` | 584 files | **1 file, 2 lines** |
| Filenames matching `pathograph` across every git ref | 57 refs | **0** |
| Commit messages, `git log --all -i --grep=pathograph` | all reachable commits | **0** |

The single file is `learning/scientist/PILOT_PMID33914858_FULLTEXT_DEEPDIVE_SCIC_v1.md` — my own
untracked work artifact — and both lines are passing mentions (a do-not-touch list; a note on
typing semantics). Neither is an inventory.

**Positive control for the ref sweep:** the identical loop searching for `roles/scientist.md`
returned **36 of 57 refs**. The sweep works; the zero is a real zero. (Loop written `"${r}"`, with
braces — the unbraced `"$r:path"` form silently applies zsh's `:r` modifier and returns a false
ABSENT on every ref.)

**Consequence, reported as a divergence per §4:** there is no canonical task packet, no edge
inventory, and therefore no edges to type. §4's priority list A–D is unexecutable as written. I did
not infer a workset from the prompt, because §4 forbids that where a canonical packet exists and is
silent on fabricating one where none does. **I executed §12 instead, which is fully specified and
whose evidence is present.**

Related measurement, §5/§7: **no governed relation vocabulary exists either.** `relation_type`,
`edge_type`, `RELATION_VOCAB` return zero across all `*.md`, `*.py`, `*.json`. The governed
vocabularies that *do* exist are the linter's claim states —
`consolidated baseline · in observation · conflicting evidence · flagged for review · background only · archived`
— and the epistemic types `DATO / INFERENZA / IPOTESI`. §5 says: if no existing type fits, say so,
and do not invent one. **Accordingly I assign no relation type below.** I state the proposition, its
epistemic type, and the layer it belongs in, and leave typing to whoever governs the vocabulary.

---

## 3 · Phase gate — Phase II cannot open

§3 requires all three first-pass artifacts to be durably recorded before Phase II.

Swept `learning/` across all 57 refs:

| Actor | Durable artifacts in any ref |
|---|---|
| `scientist-a` | **none** — no `learning/scientist-a/` path in any ref |
| `scientist-b` | **one** — `learning/scientist-b/SLR-scientist-b-0001.md`, on `lettore-b` only; a Session Learning Review |
| `scientist-c` (me) | none tracked before this commit; three untracked files in my own worktree |

🔴 **§12's premise is not verifiable from any durable surface.** It states that Scientist-B has
already produced a pilot on PMID 32000863. **No such artifact exists in any of the 57 refs.** Two
readings are possible and I cannot distinguish them from here: it is untracked in `lettore-b`'s
working directory — invisible to git, unreadable by me under worktree confinement, and in any case
barred to me during Phase I — or the premise is mistaken. I report the measurement, not a verdict
on which.

**I therefore do not perform Phases II–V.** Cross-review of artifacts that do not exist would be
fabrication, and a "revised thesis" answering challenges nobody raised would be theatre. Phase I is
delivered complete; the gate is stated rather than stepped over.

---

## 4 · Primary evidence — identity verified before reading

`files/` is gitignored and absent from this worktree; the evidence lives in the shared checkout, as
the contract specifies. All four declared artifacts present, and **all four sha256 match the
manifest exactly** — so what I read is the blob that was adjudicated, not a same-named successor.

| Artifact | sha256 (measured = declared) |
|---|---|
| `PMID32000863_Cheng2020_PMC.xml` | `792b5b29…f00f5` |
| `PMID32000863_Cheng2020_supplementary.pdf` | `0acb771c…f8b7f` |
| `…_assets/40478_2020_883_Fig2_HTML.png` | `9e464859…7ae47d05` |
| `…_assets/40478_2020_883_Fig7_HTML.png` | `ced68a66…519162542` |

**Model system.** Mouse, two independently targeted constitutive systemic *Wwox* knockout strains
(exon-1-targeting `WD1` and exon-2/3/4-targeting `WD234`), built specifically to exclude an aberrant
product of the retained exon 1. Genotypes `+/+`, `+/−`, `−/−`. Figure 7c tissue: cerebellum,
hippocampus, cerebral cortex at **postnatal day 20**. Seizure models: pilocarpine 50 mg/kg i.p. and
PTZ 30 mg/kg i.p., scored 60 min on a modified Racine scale.

**Figures inspected as images at native resolution**, not from captions: Figure 7 at 1946×1627,
panel c re-read at 3×, all six treatment sub-panels of 7b and 7d re-read at 4×. Denominator stated:
**6 of 6** genotype×drug sub-panels inspected.

---

## 5 · Adjudication of the eight assigned questions

### Q1 — Is lithium suppression restricted to *Wwox*-null animals?

**No. It is present in all three genotypes, at the same declared significance level.**

Read directly from Figure 7d at 4×, per panel:

| Genotype | PTZ | PTZ + LiCl | Bracket |
|---|---|---|---|
| `+/+` | N=12 | N=8 | `****` |
| `+/−` | N=12 | N=12 | `****` |
| `−/−` | N=6 | N=7 | `****` |

The wild-type panel is marked exactly as strongly as the null panel. *Confirms* the manifest's
Figure 7d locator, re-derived independently.

The paper's text and caption assert only the null: *"Injection of a potent GSK3β inhibitor lithium
chloride significantly suppressed PTZ-induced epileptic seizure in Wwox−/− mice (Fig. 7 d)"*
(Results, GSK-3β section, final paragraph) and *"d Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg)
suppressed PTZ-induced seizure activity in Wwox−/− mice"* (Fig. 7 caption). Both statements are
**true and incomplete**. Incomplete is not false — but a knowledge graph built from the text alone
inherits a restriction the figure does not carry.

### Q2 — Does the experiment demonstrate a WWOX-specific rescue?

**No — and the reason is stronger than "it also works in controls".**

Two independent defeaters, and the second is the one that matters:

1. Suppression is significant in both control genotypes (Q1), with control-arm N equal to or larger
   than the null arm. This is not a power artefact in the controls.
2. 🔴 **No genotype × treatment interaction was ever tested.** Methods, *Statistical analysis*, in
   full: *"We performed statistical tests with one-way analysis of variance (ANOVA) to compare the
   difference among groups. The differences were considered significant when the P values were less
   than 0.05."* One-way ANOVA, no post-hoc named, no multiplicity correction named. Each genotype is
   analysed in its own panel. **The difference of differences — the only quantity that could
   establish genotype-specific rescue — is not computed anywhere in the paper.**

**This sharpens the existing canonical boundary rather than merely repeating it.** The canonical
text argues from "the same suppression in the two control genotypes". That slightly overstates what
the panels license: they show suppression is *significant* in controls, not that its *magnitude*
equals the null's. Baselines differ greatly — PTZ drives controls to roughly stage 0.5–1.5 and nulls
to roughly stage 2–3.5 — so a real interaction could exist and remain undetected. The defensible
position is therefore not *"lithium is non-specific"* but:

> **The experiment cannot distinguish specific from non-specific rescue, because the test that
> would separate them was not performed, and every marginal significance it does report is
> identical.**

That is weaker than "non-specific" and much harder to overturn. Recorded as my position, and as a
divergence from the canonical wording.

### Q3 — Does it demonstrate GSK-3β is the molecular target responsible?

**No. Four independent gaps, one of them decisive.**

1. **Lithium is not a selective GSK-3β inhibitor.** The paper calls it *"a potent GSK3β inhibitor"*.
   It is also an inositol monophosphatase inhibitor and has multiple documented CNS actions.
2. **No second, structurally unrelated GSK-3β inhibitor was tested.** One drug, one conclusion.
3. **No genetic test.** No *Gsk3b* knockdown, knockout, or constitutively-active rescue.
4. 🔴 **DECISIVE — the pharmacological arm and the molecular arm are never joined.** I enumerated
   every occurrence of `lithium`/`LiCl` across the full cleaned XML (searched surface: 71,916
   characters). They appear in the abstract, an unrelated histology reagent (lithium carbonate in
   LFB staining), Methods dosing, the Fig 7d caption, one Results sentence, four Discussion
   sentences, the abbreviation list, and two reference titles. **No panel and no sentence reports
   any molecular measurement in a lithium-treated animal.** Figure 7c is untreated mice; Figure 7d
   is treated mice with no molecular readout. Nothing in this paper shows that lithium changed
   GSK-3β Ser9 phosphorylation, or anything else, in these brains.

   Confirmed on the second surface: the supplementary PDF (24 pages, 17,570 extracted characters)
   contains **zero** occurrences of `ithium`, `LiCl`, `GSK`, or `thosuximide`, and its nine figures
   S1–S9 are all developmental/morphological per the XML's own Additional-file listing. Two
   independent surfaces agree: **all GSK-3β and all pharmacology in this paper is Figure 7 alone.**

   > 🔴 **ANNOTATION 2026-08-25, at closure — THE DENOMINATOR ABOVE DESCRIBES THE WRONG POPULATION.**
   > *Left standing; correction here. The conclusion is unchanged and the warrant under it moves.*
   >
   > *"24 pages, 17,570 extracted characters, zero occurrences"* invites the reader to weigh the
   > negative against 17,570 characters. **For a claim about what the supplementary figures show, that
   > is not the denominator.** Measured per page:
   >
   > ```
   > pages carrying a figure-image (≥20,000 px²)   7 of 24   holding 23 figure-images
   > text on those seven pages                     1,012 characters  ≈ 5.7% of the document
   > e.g. p21  54 chars = "Supplementary Figure 8 +/+ -/- H&E (postnatal day 20)"
   >      p11  42 chars · p13 76 · p9 103 · p23 161 · p15 272 · p7 304
   > ```
   >
   > The other ~94% is Supplementary Methods and legend prose on pages that carry no figure at all.
   > **So the text negative covers the legends and does not cover the panels** — anything rendered
   > inside those 23 raster images is invisible to text extraction, and I have not OCR'd them.
   > Quoting 17,570 makes the negative look roughly seventeen times stronger than it is for the
   > question actually asked.
   >
   > **What carries the conclusion is therefore the *other* surface**, not this one: the XML's
   > Additional-file listing names S1–S9 by title and every one is developmental or morphological,
   > which is a listing of what the figures *are*, from a different artifact, unaffected by raster
   > text. The conclusion stands on that. **This sentence should never have been the co-equal second
   > leg it is written as.**
   >
   > My `OBSERVATION_SCOPE` already said this negative was *"weaker than the XML negatives"* and that
   > pypdf can miss vector-rendered text — **that caveat was correct and it was in the wrong place**,
   > four sections away from the number it qualifies, where a reader taking the Q3 sentence alone
   > would never meet it. *A caveat that does not travel with its claim has not been made.*
   >
   > Found while testing whether Scientist A's boundary around its own supplement claim also held for
   > mine. It did not. Ninth instance in this run of a denominator describing a different population
   > than the claim it supports, and the fourth that is mine.

🔴 **Counter-evidence from the paper's own bibliography, sought deliberately.** The Discussion cites
reference [10] — *Bahremand et al. 2011, "Additive anticonvulsant effects of agmatine and lithium
chloride on pentylenetetrazole-induced clonic seizure in mice: involvement of α2-adrenoceptor",
PMID 21651904* — for the statement that *"Administration of lithium in mice has been demonstrated to
attenuate PTZ-induced clonic seizure"*. That reference establishes lithium's anticonvulsant action
against PTZ **in ordinary mice**, and attributes it to the **α2-adrenoceptor, not GSK-3β**. The
paper cites, in its own Discussion, a genotype-independent and GSK-3β-independent mechanism for the
exact effect it attributes to GSK-3β inhibition. *Not in the manifest.*

### Q4 — What exactly does Figure 7c establish?

Densitometry read at 3× from the native image, all nine lanes:

| Row | Cerebellum `+/+ +/− −/−` | Hippocampus | Cortex |
|---|---|---|---|
| pGSK3β (Ser9) | 2.7 · 3.1 · **1.3** | 3.6 · 3.5 · **2.0** | 3.9 · 3.8 · **2.5** |
| total GSK3β | 2.2 · 2.4 · 2.4 | 2.3 · 2.4 · 2.6 | 2.2 · 2.4 · 2.6 |

- **Total GSK-3β:** essentially unchanged — every one of the nine values lies in 2.2–2.6. The null
  is marginally *higher*, by 0.2–0.4 units, with no statistics attached. **There is no abundance
  increase.** *Confirms* the manifest.
- **Ser9 phosphorylation:** clearly reduced in `−/−` in all three regions. GSK-3β is
  **dis-inhibited, not more abundant** — which is what the paper itself says: *"as evidenced by
  dephosphorylation of GSK3β at Ser9"*.
- **Genotype pattern:** the heterozygote is **not intermediate**. On the phospho row it sits at or
  above wild-type in every region (3.1 vs 2.7; 3.5 vs 3.6; 3.8 vs 3.9). *Confirms* the manifest's
  corrected values.
- 🔴 **Statistical support: NONE.** *Not in the manifest, and it is the answer to the sub-question
  actually asked.* Panel c carries no error bars, no per-lane n, no significance marker, and no
  P-value. The caption offers *"The representative results of four independent experiments are
  shown"* and *"the numbers depict the ratio of phosphorylated or total GSK3β to β-actin protein
  level"*. These are point densitometry values from one representative blot. **The paper's central
  molecular claim rests on nine unreplicated numbers with no dispersion and no test.**
- **Robustness check I ran, which the paper did not.** Both rows are normalised to β-actin
  separately; the biologically meaningful pSer9/total ratio is never computed. Computing it from the
  printed values: cerebellum 1.23 · 1.29 · 0.54; hippocampus 1.57 · 1.46 · 0.77; cortex
  1.77 · 1.58 · 0.96. The direction and the non-intermediate heterozygote both survive the
  renormalisation. **The qualitative conclusion is robust to normalisation choice** — worth stating,
  since it is the one thing about panel c that *is* solid.
- **An internal dissociation, *not in the manifest*.** The panel's own Wwox row shows protein absent
  in `−/−` and visibly reduced in `+/−` versus `+/+`. So gene dosage is plainly visible at the level
  of WWOX protein and **entirely absent at the level of pSer9**. Half the WWOX protein yields full
  Ser9 phosphorylation. That argues against a simple stoichiometric WWOX ⊣ GSK-3β relationship in
  vivo and is a constraint any mechanistic model must satisfy.

### Q5 — Does ethosuximide show a genotype-restricted pattern distinct from lithium?

**Yes.** Figure 7b at 4×, PTZ vs PTZ+ETS within genotype:

| Genotype | Control | PTZ | PTZ + ETS | PTZ vs PTZ+ETS |
|---|---|---|---|---|
| `+/+` | N=4 | N=20 | N=16 | **n.s.** |
| `+/−` | N=5 | N=18 | N=12 | **n.s.** |
| `−/−` | N=4 | N=6 | N=6 | `***` |

The control genotypes carry the **larger** samples and still show nothing, so the negative is not a
power artefact. The comparator drug has exactly the genotype restriction the favoured drug lacks.

🔴 **Two limits on how far this can be pushed, and I hold to both.**

- **Not exposure-matched.** Methods: ethosuximide is a **single** 150 mg/kg dose at −45 min; LiCl is
  *"pretreated three times within 1 h before PTZ injection"* at 60 mg/kg — a cumulative 180 mg/kg
  across three administrations. The two arms differ in dose, schedule and number of administrations.
  **A specificity contrast between them is confounded by exposure.** *Not in the manifest.*
- **Different experiments.** 7b and 7d have different control arms and different N. "ETS is
  specific, LiCl is not" is a between-panel comparison, never tested.

### Q6 — What causal edge does this paper license between *Wwox* loss, GSK-3β state, and seizure?

Separating the three links, because they are not equally supported:

| Link | What the evidence licenses |
|---|---|
| *Wwox* loss → seizure susceptibility | **Well supported.** Two independent KO strains, two convulsant models, spontaneous seizures after P12, SE in half the nulls and in no control. Epistemic type: `DATO`. |
| *Wwox* loss → reduced GSK-3β Ser9 phosphorylation | **Observed, unreplicated, untested, and confounded** (see the confound below). Correlational and cross-sectional. Epistemic type: `DATO` with a declared statistical void. |
| GSK-3β state → seizure susceptibility | 🔴 **Not licensed.** This is the link the paper needs and the one it never measures. It rests entirely on one non-selective drug, with no molecular confirmation that the drug engaged the target in these animals, no second inhibitor, no genetic test, and no interaction test. Epistemic type: `IPOTESI`. |

So the licensed edge is a **two-arm structure, not a chain**: *Wwox* loss → seizures, and *Wwox*
loss → altered GSK-3β phosphorylation state, **with the join between them unmeasured**. Any
graph that renders `Wwox loss → GSK-3β activation → seizure` as a mechanistic path asserts a link
this paper does not carry.

🔴 **ALTERNATIVE EXPLANATION — the strongest one, and it is not recorded anywhere in the canonical
model.** Figure 7c is measured at **postnatal day 20**. This paper's own Introduction states that
*"Wwox-deficient mice are significantly reduced in size, exhibit abnormalities of bone metabolism
and succumb to death by 4 weeks postnatally"*, and its Results record *"reduction in brain size and
weight … at postnatal day 20"*. So the westerns are run on runted, microcephalic animals inside the
terminal decline.

Cheng 2020 reports **no systemic covariate at all**. Searched surface, full cleaned XML, 71,916
characters: `blood glucose` 0 · `bicarbonate` 0 · `BUN` 0 (case-sensitive) · `creatinine` 0 ·
`hypoglyc*` 0 · `acidosis` 0 · `serum` 0 · `body weight` 0. The two `glucose` hits are an
Introduction sentence about HIF1α and a reference title.

Meanwhile `claim_registry_current.md` **CLAIM 036** documents, in a systemic constitutive *Wwox*
null at **P18**: glucose 143.5 vs 250.6 mg/dL (`p=0.000131`), total bicarbonate 14.50 vs 21.67 mEq/L
(`p=0.006227`), BUN 37.25 vs 17.67 mg/dL (`p=0.01086`) — and concludes that any brain phenotype
measured in that window *"rende impossibile per costruzione separare la perdita neuronale
cell-autonoma di Wwox dal danno metabolico secondario"*.

**GSK-3β Ser9 phosphorylation is the canonical output of insulin/IGF-1 → PI3K → AKT signalling.
Hypoglycaemia and a catabolic, acidotic state reduce AKT activity and therefore reduce Ser9
phosphorylation — precisely the direction and precisely the readout Figure 7c reports.** The
observation is fully predicted by systemic metabolic decompensation with no WWOX–GSK-3β mechanism
required.

**Held to its proper strength, not overstated.** CLAIM 036's window is P14–P18 and its source is a
*different* line (Ludes-Meyers 2009, EIIA-Cre `Wwox^ΔCre/ΔCre`); Cheng's strains are his own and the
timepoint is P20. So this is **an untested confound of high prior plausibility, not a demonstrated
one.** It does not refute the observation. It removes its right to be read as a WWOX-specific
mechanistic signal until a metabolically-controlled measurement exists.

**Decisive next test (falsifier).** Measure brain pGSK3β(Ser9) in *Wwox*-null mice against
littermate controls **pair-fed or glucose-clamped**, or in a **brain-restricted conditional** null
that is not systemically ill — the `Wwox^flox` allele CLAIM 036 notes was built and never used in
this direction. If the pSer9 drop survives metabolic normalisation, the mechanistic reading stands.
If it does not, CLAIM 016's core datum is a readout of terminal illness.

Secondary falsifier for the pharmacology: a PTZ + lithium arm with an **explicit, tested**
genotype × treatment interaction, plus a structurally unrelated GSK-3β inhibitor at matched
exposure, plus a post-treatment pSer9 western demonstrating target engagement.

### Q7 — Layer assignment

| Layer | Propositions |
|---|---|
| **Disease mechanism** | *Wwox* loss → increased susceptibility to convulsant-induced and spontaneous seizure (two strains, two convulsants). Structural substrate: holoprosencephaly-to-microcephaly range, cortical heterotopia, CA1 disorganisation, cerebellar vermian fusion with Purkinje loss. |
| **Pharmacological observation** | LiCl 3×60 mg/kg suppresses PTZ seizure activity in `+/+`, `+/−` **and** `−/−` (`****` each). Ethosuximide 150 mg/kg suppresses in `−/−` only (`***`; n.s. in both controls). **Both belong here and neither belongs in the mechanism layer** — they are drug-effect observations in a seizure model, not demonstrations of a WWOX pathway. |
| **Molecular observation** | pGSK3β(Ser9) reduced in `−/−` across three regions; total GSK-3β unchanged; heterozygote not intermediate; WWOX protein absent in `−/−`, reduced in `+/−`. Carries an explicit statistical void and an untested systemic confound. |
| **Hypothesis** | GSK-3β de-repression is a *causal contributor* to the seizure phenotype. Lithium's benefit is *mediated by* GSK-3β. The tension between S9-dependence here and CLAIM 035's S9-independence (below). |
| **Not licensed at any layer** | "Targeting GSK3β with lithium ion ameliorates epilepsy" as a mechanistic statement; any WWOX-genotype-specific pharmacological claim. |

### Q8 — Figure/text discrepancies material to the graph

**Four. The third is the sharpest and the fourth is canonical, not authorial.**

1. **Lithium's control-genotype result is omitted from every text surface.** Panel 7d marks `****`
   in `+/+` and `+/−`; abstract, Results and caption name only `−/−`. A text-only extractor —
   human or machine — curates a genotype-restricted edge the figure does not support. This is
   exactly the failure class `DISMECH_INTEGRATION.md` §23 already names as its worked example.
2. 🔴 **`****` is used but never defined.** The Figure 7 legend declares only *"n.s.,
   non-significant. *** P < 0.001"*. Panel d's three brackets are all four-asterisk. I searched the
   full cleaned XML: **`****` occurs 0 times**; it exists only inside the image. **The significance
   level of the paper's central pharmacological result is undefined in the paper.** *Not in the
   manifest.*
3. 🔴 **Asymmetric reporting of control-genotype outcomes, within one figure.** For ethosuximide the
   text states the control result explicitly and negatively: *"although ethosuximide pretreatment
   had no effects on the behavior changes in Wwox+/+ and Wwox+/− mice"*. For lithium — same figure,
   same design, same three genotypes — the control result is a **positive** finding and the text is
   silent. **The authors demonstrably knew how to report control-genotype outcomes and did so for
   the drug where the result was negative, and not for the drug where it was positive.** That is a
   materially different, and much more precise, statement than "the text is incomplete". *Not in the
   manifest.*
4. **The Discussion asserts an untested head-to-head comparison:** *"Administration of GSK3β
   inhibitor lithium chloride effectively ameliorated the seizure susceptibility in Wwox−/− mice,
   and its efficacy is better than the commonly used anticonvulsant drug ethosuximide."* No
   statistical comparison of LiCl vs ETS is reported anywhere; they sit in different panels with
   different N, different control arms and non-matched exposure (Q5). **"Efficacy is better" is an
   eyeball comparison across panels presented as a result.** *Not in the manifest.*

---

## 6 · Defects found in canonical state — RECORDED, NOT FIXED

§16 forbids canonical mutation. I have edited nothing. Each is stated with its locator so an
authorized batch can act.

### D-1 — `claim_registry_current.md` mis-cites the panel, onto the panel that appears to refute it

`disease-models/wwox/registries/claim_registry_current.md` line 300 is the *Evidence boundary* added
by `BATCH_20260810_005`. It contains exactly **one** `Fig. 7` citation and it reads **`Fig. 7b`**:

> *"…registra che **il litio ha soppresso le crisi da PTZ in TUTTI E TRE i genotipi, wild-type
> incluso** (Fig. 7b; per l'etosuccimide il testo dichiara `n.s.` …)"*

**The lithium experiment is Figure 7d.** Figure 7b is ethosuximide. The manifest it cites says
"Figure 7d" in both of its lithium locators; I verified from the image that lithium is panel d.

Why this is material and not pedantic: a reader who follows the canonical pointer to check
*"lithium suppressed seizures in all three genotypes"* lands on the **ethosuximide** panel, where
the control genotypes are marked **n.s.** — evidence that appears to *contradict* the sentence it
was cited to support. **The pointer routes a verifier to the refutation of the claim it anchors.**

Under the most charitable alternative reading — that `Fig. 7b` was meant to govern the ethosuximide
clause after the semicolon — the lithium assertion is then left with **no figure locator at all**,
in the one sentence that constitutes its evidence boundary. Defective either way.

### D-2 — the same propagation failure the same batch diagnosed, left unrepaired one line above

CLAIM 016 currently asserts, verbatim:

- `**Title:**` *"GSK3β **hyperactivation** may contribute to seizure susceptibility in WWOX deficiency"*
- `**Type:**` *"**DATO (abbondanza**, murino)"*
- `**Summary:**` *"In Wwox-null mice, **GSK3β is elevated** in cortex, hippocampus and cerebellum…"*

**Figure 7c shows total GSK-3β is not elevated.** All nine lanes fall in 2.2–2.6. What changes is
Ser9 phosphorylation. The paper never claims elevated abundance; it claims increased *activation*
evidenced by *dephosphorylation*. The canonical record has converted a phosphorylation-state
observation into an abundance observation, and typed the claim's datum accordingly.

**The conclusion survives; the stated evidence does not.** GSK-3β activity is plausibly increased —
the pSer9 data support that. So this is a **misdescribed premise**, not a reversed conclusion, and
it should be corrected without disturbing the claim's status.

🔴 **What makes this worth escalating:** line 297 (`BATCH_20260726_001`) already reframed the claim
*"da «GSK3β è elevata» (osservazione di abbondanza) a «GSK3β è de-repressa»"*, and line 298 attached
a `PREMISE_TAG` to *"che l'abbondanza di proteina GSK3β riporti l'attività di GSK3β"*. **That
`PREMISE_TAG` guards a premise the primary never instantiated** — there is no abundance observation
to question. Two batches built qualifications on top of a base sentence that misstates the
measurement, and neither corrected the sentence.

And the manifest recorded it correctly on day one: *"total GSK3-beta protein is essentially
unchanged… GSK3-beta is dis-inhibited, not more abundant."* `BATCH_20260810_005` closed the lithium
locator's propagation gap and wrote its own diagnosis — *"Il locator esisteva dal giorno della
lettura e non era mai arrivato fin qui: è un difetto di propagazione, non di lettura"* — while a
second instance of the identical class, sitting in the same manifest and contradicting the same
claim's `Summary`, was left in place. **The repair fixed the instance and not the class.** The
working-model mirror carries the residue too: line 164 reads *"not merely elevated abundance"*,
which still presupposes abundance is elevated.

### D-3 — CLAIM 016 and CLAIM 036 do not know about each other

The confounded claim and the claim that documents the confound are **mutually unlinked in both
directions**. CLAIM 016's `Wikilinks` are `PAPER 019 · PAPER 056 · CLAIM 035`; CLAIM 036's are
`PAPER 057 · CLAIM 005 · CLAIM 038`. Grep for `CLAIM 036` inside CLAIM 016's block: **0**. Grep for
`CLAIM 016` inside CLAIM 036's block: **0**. (Positive control: `CLAIM 035` appears **2×** inside
CLAIM 016's block, so the grep fires.)

CLAIM 036 explicitly declares itself *"un vincolo di disegno trasversale"* — a cross-cutting design
constraint — and names P1, P2 and P6 as the pathways it crosses. **CLAIM 016's primary datum is a
brain measurement in a systemic constitutive null in the immediately adjacent window, and it is not
among the claims the constraint reaches.** A cross-cutting constraint that has to be wikilinked by
hand to each claim it constrains will keep missing claims.

### D-4 — an unresolved tension between CLAIM 016 and CLAIM 035, currently held without comment

- **CLAIM 035** (Wang 2012, PMID 22193544): WWOX inhibits GSK-3β via the SDR 388–407/L404 docking
  motif, the inhibition is **S9-independent**, and the canonical text warns that WWOX-loss-driven
  de-repression *"sarebbe **invisibile a un western anti-fosfo-S9**, che è il saggio standard —
  qualunque studio WWOX-DEE che usi pS9 come readout di attività GSK3β produrrà un **falso
  negativo**"*.
- **CLAIM 016** (Cheng 2020): a phospho-S9 western in WWOX-null brain returns a **positive** result.

The canonical model asserts that the assay will produce a false negative, and holds alongside it a
positive result from that assay, with no note connecting them. Both cannot be read naively. Either
the pSer9 drop is driven by something other than direct WWOX→GSK-3β de-repression — the P20 systemic
confound of §Q6 is a concrete candidate — or Wang's S9-independence does not generalise to brain in
vivo. **This is a genuine scientific question the model is currently positioned to answer and has
not asked.** It is also, independently, a reason the confound in Q6 deserves priority: the two
findings point at the same resolution.

---

## 7 · Graph recommendations

Using §5's semantic outcomes. No governed relation token is assigned, per §2.

| Proposition | Recommendation |
|---|---|
| *Wwox* loss → seizure susceptibility (mouse, two strains, two convulsants) | **carry existing relation** |
| *Wwox* loss → reduced pGSK3β(Ser9) in brain at P20 | **carry with qualification** — flag the statistical void (no error bars, no n, no test) and the untested systemic confound |
| *Wwox* loss → increased GSK-3β **abundance** | **relation unsupported** — contradicted by the primary's own panel; see D-2 |
| GSK-3β state → seizure susceptibility | **relation should remain hypothesis rather than established edge** |
| Lithium → seizure suppression **specifically in WWOX deficiency** | **relation unsupported** |
| Lithium → seizure suppression (genotype-independent, PTZ model) | **carry with qualification** — pharmacological observation layer only; `****` undefined |
| Ethosuximide → seizure suppression restricted to `−/−` | **carry with qualification** — real, but not exposure-matched to the lithium arm |
| Lithium acts *via* GSK-3β in this model | **additional source required** — needs target engagement, a second inhibitor, and a genetic test |
| Lithium efficacy > ethosuximide efficacy | **relation unsupported** — asserted in Discussion, never tested |
| CLAIM 016 ↔ CLAIM 035 S9-dependence | **relation unresolved** — preserve the disagreement |

**Architecture-sensitive:** the pharmacological observations must not sit in the disease-mechanism
layer. A graph that cannot distinguish *"drug X suppresses seizures in a model that has seizures"*
from *"drug X corrects the disease mechanism"* will convert every anticonvulsant into a
pathway-specific therapeutic rationale. This paper is a clean worked example of that failure mode,
and its closing sentence — *"Future studies … will be needed to test whether GSK3β inhibitors may be
promising candidates"* — is appropriately hedged in the source and is exactly what downstream
synthesis tends to un-hedge.

---

## 8 · Decomposition candidates (§7 — evidence for Plan, not authorization)

**DC-1 — CLAIM 016.**
Exact title: *"GSK3β hyperactivation may contribute to seizure susceptibility in WWOX deficiency"*.
Latent source: WWOX loss. Latent relation: contributes-to (hedged). Latent target: seizure
susceptibility. Latent mediator, compressed and invisible: GSK-3β hyperactivation.
Why materialization is impaired: the title compresses a **three-node mediated path** into one node
label, and the mediation is precisely the link the evidence does not license (Q6). Any edge derived
from this title inherits an asserted mechanism.
Would decomposition change scientific meaning? **Yes — beneficially.** Splitting it into the two
supported arms plus one hypothesis-layer mediator would let the graph carry what is known without
asserting the join. But it would also split a claim whose status, sources and premise tags are
currently unitary, so it is Plan's call, not mine.

**DC-2 — the claim `Type` field mixes epistemic type with evidence kind.**
CLAIM 016's `Type:` reads *"DATO (abbondanza, murino) + DATO meccanicistico risolto a livello di
residuo (biochimica, PAPER 056) + INFERENZA prudente (trasferimento clinico)"* — three epistemic
types, two sources, one organism annotation and one transferability judgement in a single free-text
field. D-2 was able to hide inside it: the wrong word *abbondanza* sits in a slot no validator
reads. **A structured field would have caught it.**

---

## 9 · Operating-practice observations (§13)

**WHAT HELPED SCIENTIFIC QUALITY**
- Verifying artifact sha256 against the manifest **before** reading. Cheap, and it converts "I read
  the paper" into "I read *this blob*".
- Inspecting panels as images at 3–4×. Every one of my four novel findings (undefined `****`, the
  reporting asymmetry, the absent statistics on 7c, the WWOX-dosage/pSer9 dissociation) came from
  the image or from cross-reading the image against the text. None was reachable from captions.
- Stating the searched surface **and its denominator** for every negative. "`****` occurs 0 times in
  71,916 characters of cleaned XML" is auditable; "the paper doesn't define it" is not.
- Running a **positive control** on every sweep. The 57-ref Pathograph zero is only trustworthy
  because the same loop returned 36 for a string that had to be there.
- Recomputing the pSer9/total ratio the paper never computed — a two-minute robustness check that
  told me which part of panel c is solid.
- Reading the paper's **own bibliography** as counter-evidence. Reference [10] undercuts the
  paper's mechanistic framing, and it is sitting in the Discussion.

**WHAT CREATED WASTE**
- Consulting the deepdive manifest for artifact paths and receiving a full adjudication (§1).
  Provenance and conclusions should not share a file.
- Searching for a Pathograph that does not exist. A canonical inventory pointer would have cost one
  read instead of four sweeps.

**WHAT SHOULD BE MANDATORY**
- Artifact fingerprint verification before a reading counts.
- Denominator-and-positive-control for every negative claim.
- Figure inspection as image, at native resolution, with the sub-panel denominator declared
  (*6 of 6*, not "figures inspected").
- **A statistics field per figure panel** — test, n, dispersion, and whether the significance
  notation used is actually defined in the legend. D-2 and the undefined `****` are both instances
  of "nobody had a slot for this".

**WHAT SHOULD REMAIN TASK-MODE SPECIFIC**
- Multi-hop reference enumeration; corpus cross-query; group assessment. Valuable, and not needed to
  adjudicate a specific relation.

**WHAT SHOULD BE A REUSABLE SKILL**
- *Panel-vs-text divergence sweep*: for each figure, extract every text/caption assertion, read the
  panel, and emit `text_only | text_confirmed_by_panel | panel_only | text_contradicted_by_panel`.
  The manifest already has this vocabulary and already found it insufficient — it notes three times
  that it has "neither a value for [qualification] nor a way to point at what is qualified". **A
  fifth value, `text_incomplete_vs_panel`, with a pointer to the specific clause qualified, is the
  missing token.** All four of my Q8 discrepancies are that shape.
- *Locator propagation audit*: diff every manifest locator against the canonical claim text it
  landed in. D-1 and D-2 are both propagation defects and both are mechanically detectable.

**WHAT SHOULD NOT BE IN THE SCIENTIST CONTRACT**
- Canonical mutation, vocabulary creation, actor activation, lease handling. Confirmed comfortable:
  I found four canonical defects and repairing none of them cost me nothing scientifically.

**WHAT REQUIRED ANOTHER SCIENTIST**
- Nothing yet, and that is the finding: Phase I is genuinely single-actor work. The independence
  requirement only becomes load-bearing at Phase II, which cannot open (§3).

**WHAT REQUIRED MIRROR RATHER THAN SCIENTIST**
- The §1 anchoring hazard. I can declare the contamination; I cannot certify my own independence.
- Whether D-1/D-2 indicate a systemic propagation-gate weakness rather than two incidents.
- Whether §12's unverifiable premise about a Scientist-B pilot is a frame-contamination event.

**WHAT REQUIRED ORCHESTRATOR**
- The Pathograph workset (§2). A scientist cannot conjure a canonical packet.
- Authorization to propagate D-1–D-4 into canonical state.
- Opening a peer review, per the contract's routing rule.

**WHAT, IF ANYTHING, JUSTIFIES A FUTURE NEW ACTOR**
- **Nothing here does.** D-1 through D-4 are all *propagation* defects — manifest to canonical text
  — and every one is mechanically detectable by a validator. That argues for a **check in the commit
  gate**, not a new actor. Recorded explicitly because "we found defects, therefore we need a
  reviewer role" is the tempting and wrong inference: an actor that reads prose is exactly what
  already failed here, four times, across three batches.

---

## 10 · OBSERVATION_SCOPE

- **Adjudicated:** PMID 32000863 only, against the four fingerprinted artifacts named in §4.
- **Read in full:** the JATS XML body — Methods (seizure induction, statistics, western blotting),
  the complete GSK-3β Results section, the Figure 7 caption, the Discussion's lithium paragraph,
  the Additional-file listing. Figure 7 inspected as an image at native 1946×1627, panel c at 3×,
  all six treatment sub-panels of 7b/7d at 4×.
- **Not read:** Figures 1, 3, 4, 5, 6 as images (not load-bearing for the assigned questions).
  Figure 2 was fingerprint-verified but not re-inspected — the Tc-MEP heterozygote finding is
  outside Q1–Q8 and I did not re-derive it. The supplementary PDF was searched by extracted text
  (24 pages, 17,570 chars), **not** inspected panel by panel; pypdf extraction can miss
  vector-rendered text, so that negative is weaker than the XML negatives. Its corroboration is the
  XML's own S1–S9 listing, an independent surface.
- **Not read, deliberately:** any artifact authored by `scientist-a` or `scientist-b`.
- **Not attempted:** live PubMed / Europe PMC. The connector is unauthorized in this session, so no
  retraction re-check and no field-density measurement. The manifest's 2026-08-04 retraction check
  against the local PMC XML article-meta is inherited, **not re-verified**, and is declared as
  inherited.
- **Not performed:** Phases II–V (§3 gate); any canonical mutation (§16); any relation typing (§2).
