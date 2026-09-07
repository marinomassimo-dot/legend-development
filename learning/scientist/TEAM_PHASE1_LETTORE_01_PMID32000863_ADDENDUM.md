# PHASE I ADDENDUM — PMID 32000863 · Figure 7c, layer partition, figure/text mismatches

**Actor:** Scientist A, worktree `lettore`, branch `lettore`.
**Relationship to the preserved first pass:** this is an **addendum**, not a revision.
`PILOT_PMID32000863_GSK3B_LITHIUM_ADJUDICATION_LETTORE_v1.md` is preserved byte-unchanged. Nothing
below reverses it; §1 and §3 close two dispatch questions it answered only in part, §4 adds two
figure/text findings it did not contain.
**Peer isolation:** Scientist B's pilot on this paper was **not** read — the Phase II gate is
closed on Scientist C (see artifact 00 §5). No peer scientific conclusion informed anything here.
**Status:** NON-CANONICAL. No canonical file written.
**Public, disease-level, de-identified. Nothing here is medical advice.**

---

## 0 · Coverage of the eight dispatch questions

| # | Question | Where answered |
|---|---|---|
| 1 | Lithium: nulls only, or controls too? | pilot §5 — **all three genotypes** |
| 2 | WWOX-specific rescue? | pilot §7 — **no** |
| 3 | GSK-3β established as the responsible target? | pilot §8 — **no** |
| 4 | What does Fig. 7c establish (total / Ser9 / genotype pattern / statistics)? | **§1–§2 here** — the pilot carried the densitometry but not the statistical adjudication |
| 5 | Ethosuximide genotype-restricted, distinct from lithium? | pilot §4 vs §5 — yes, and inverted from expectation |
| 6 | Causal edge licensed between Wwox loss / GSK-3β state / seizure phenotype? | pilot §9 + artifact 02 |
| 7 | Which propositions go to mechanism graph / pharmacological layer / hypothesis layer? | **§3 here** |
| 8 | Figure/text discrepancies material to the graph? | pilot §5, §11 + **§4 here** (two more) |

---

## 1 · Figure 7c — adjudicated from the panel

**Artifact.** `files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig7_HTML.png`,
sha256 `ced68a66c8d2ab69d7c61e7ec0af05f2eaa1566b7740a516593bcae519162542`, 1946×1627, read at
2× and 6× — never through a text conversion.

**Text artifact.** `files/fulltext/PMID32000863_Cheng2020_PMC.xml`, sha256
`792b5b296863674d0295a7dba918ee7c59ade8cdff64ee8ec9d8f01bd12f00f5`, JATS, abstract held
separate from body. Both hashes match the four `source_artifacts` declared in the canonical
deep-dive manifest.

### 1.1 What is on the panel

Four antibody rows — `pGSK3β (Ser9)`, `GSK3β`, `Wwox`, `β-actin` — over nine lanes, read at 6×:

```
Cerebellum          Hippocampus         Cortex
+/+   +/−   −/−     +/+   +/−   −/−     +/+   +/−   −/−
```

Densitometry printed beneath two of the four rows, and beneath those two only:

| Row | Cerebellum | Hippocampus | Cortex |
|---|---|---|---|
| `pGSK3β (Ser9)` | 2.7 · 3.1 · **1.3** | 3.6 · 3.5 · **2.0** | 3.9 · 3.8 · **2.5** |
| `GSK3β` (total) | 2.2 · 2.4 · **2.4** | 2.3 · 2.4 · **2.6** | 2.2 · 2.4 · **2.6** |
| `Wwox` | *no numbers* | *no numbers* | *no numbers* |
| `β-actin` | *no numbers* | *no numbers* | *no numbers* |

### 1.2 The legend, verbatim — and it is decisive

> *"**c** Increased activation of GSK3β was determined in the cerebellum, hippocampus and cerebral
> cortex of Wwox−/− mice at postnatal day 20, as evidenced by dephosphorylation of GSK3β at Ser9.
> β-actin was used as an internal control in western blotting. Quantitative densitometry of the
> immunoblots was performed, and the numbers depict the ratio of phosphorylated or total GSK3β to
> β-actin protein level in the brain tissues. **The representative results of four independent
> experiments are shown.**"*
> — Fig. 7 legend, panel c, BODY-EXACT against sha256 `792b5b29…f00f5`

Two things this settles that the pilot left open. **Both numbers are ratios to β-actin**, not to
each other — so total GSK3β is normalised the same way pGSK3β is, and the two rows are directly
comparable. And **n = four independent experiments, of which one representative is shown** — the
printed numbers are that one blot's densitometry, not a mean of four.

### 1.3 🔴 Statistical support: **none**

| What panel c carries | Present? |
|---|---|
| Error bars | ❌ |
| A dispersion statistic (SD / SEM) on any number | ❌ |
| A significance marker (`*`, `n.s.`, or any bracket) | ❌ |
| A stated statistical test for panel c | ❌ |
| A P value | ❌ |
| Per-replicate values for the declared n = 4 | ❌ |
| A stated n **in the panel** | ❌ (n = 4 appears only in the legend) |

The legend's statistics sentence — *"The results are expressed as means ± SEM. n.s.,
non-significant. \*\*\*P < 0.001"* — is the **last** sentence of the legend and follows panel
d's sentence. Panel c has no means and no SEM to express: a single representative blot has
neither. Read in order, that sentence governs the seizure time-series panels.

**Bounded search of the second surface.** The 24-page supplementary
(`PMID32000863_Cheng2020_supplementary.pdf`, sha256 `0acb771c…8f7f`, 17 844 characters of
extracted text, 9 supplementary figures, all legends read) contains **zero** occurrences of
`GSK`, `lithium`, `LiCl`, `Ser9`, `ethosuximide`, `ETS` or `PTZ`. The nine supplementary figures
are morphology, apoptosis and development; none is biochemistry or pharmacology. *Denominator
declared:* 24 pages of a PDF text layer plus the nine legends; individual figure panels of the
supplement were not adjudicated, so the absence is scoped to the text layer and the legends, not
asserted of the images.

⇒ **The whole GSK3β/pharmacology arm of this paper has no supplementary support of any kind, and
panel c carries no statistics anywhere in the article.**

### 1.4 The genotype pattern — and the heterozygote is the informative lane

Derived by me from the panel's own numbers (the paper computes no such ratio and attaches no
test to it; this is my arithmetic on its printed values, declared as such):

| Region | pS9/total, `+/+` | `+/−` | `−/−` | `−/−` ÷ `+/+` | `+/−` ÷ `+/+` |
|---|---|---|---|---|---|
| Cerebellum | 1.227 | 1.292 | 0.542 | **0.44** | 1.05 |
| Hippocampus | 1.565 | 1.458 | 0.769 | **0.49** | 0.93 |
| Cortex | 1.773 | 1.583 | 0.962 | **0.54** | 0.89 |

- **Ser9 phosphorylation falls in `−/−`**, in all three regions, by roughly half on the
  normalised ratio — consistent, sizeable, and the paper's real observation.
- **The heterozygote is not intermediate.** It sits at 1.05×, 0.93×, 0.89× of wild type — i.e. at
  wild type, and in cerebellum fractionally *above* it. **There is no gene-dosage gradient**,
  which is the pattern a graded mechanism would produce. One allele of *Wwox* is enough to hold
  the Ser9 state at wild-type level.
- **Total GSK3β is essentially flat, and what movement there is runs *upward* in the null**:
  1.09× · 1.13× · 1.18× of wild type. Between 9% and 18%, single lanes, no dispersion, no test.

### 1.5 🔴 What this does to the wording of `CLAIM 016`

`CLAIM 016`'s `Summary` (read from `main:disease-models/wwox/registries/claim_registry_current.md`)
states: *"In Wwox-null mice, **GSK3β is elevated** in cortex, hippocampus and cerebellum"*, and
its `Type` field opens `DATO (abbondanza, murino)`.

Stated fairly: the abundance direction in the panel **is** upward, so the wording is not
fabricated. But it selects the *smaller and noisier* of the two effects and drops the larger one.
The abundance change is 9–18% on unreplicated single lanes with no statistics; the Ser9 change
is a ~2× fall on the same lanes. Calling the finding *"GSK3β is elevated"* and tagging it
`DATO (abbondanza)` puts the load on the weakest quantity the panel produced.

The same claim record already contains its own correction, in the `Meccanismo aggiunto` block:
*"L'affermazione causale si sposta quindi da «GSK3β è elevata» (osservazione di abbondanza) a
«GSK3β è de-repressa» (perdita di un freno fisico)."* **The correction was written and the
`Summary` and `Type` lines it corrects were never updated.** The record therefore says two
different things about the same panel, and a graph materialiser reading the `Title`, `Summary` or
`Type` field — the fields a graph actually reads — gets the superseded one.

Classification: candidate for lawful later integration via `BATCH_COMMIT`, change class
**MINOR** — wording alignment inside one record, no status change, no conclusion reversal;
`CLAIM 016` stays `in observation`. **I performed no edit.**

### 1.6 Page-adjudication recipe — published as a recipe, never as the image

`CLAUDE.md` §5e. Source `40478_2020_883_Fig7_HTML.png`, sha256 `ced68a66…62542`. PIL 11.3.0,
`Image.crop(box)` then `resize(w*s, h*s, Image.LANCZOS)`, saved PNG. Crops written to the session
scratchpad, **outside the repository**; the reproduction is not shipped.

| id | crop box (L,U,R,Lo) px | scale | sha256 of crop |
|---|---|---|---|
| `c_full` | 820, 0, 1946, 500 | 2× | `257f721699baa206032437ea1b1d63ee9b2c99d92e4e3d7abf38fb7642996a47` |
| `c_lanelabels` | 1440, 105, 1880, 155 | 6× | `d6e2775a8244166a671033a006938cd043a016cb1d41d320074d20a698ec65ac` |
| `c_pgsk_nums` | 1440, 225, 1880, 270 | 6× | `9a0b8246c33a6ae1a4cf64b85ebdc0b0a9315f321cd3524a036f7c0a85c7b405` |
| `c_tot_nums` | 1440, 320, 1880, 365 | 6× | `45a233d9b206e9750f12368e4798512d422c422086d4a447add3e4177bece49b` |

**Re-executed after recording: all four regenerate byte-identically.** The first pair of boxes I
wrote missed the number rows vertically and were discarded rather than described — a recipe is
published only after the crop it names has been looked at and contains the span it claims to
adjudicate. `c_lanelabels` exists so the genotype↔number mapping is verifiable independently of
my reading of it.

---

## 2 · Answer to dispatch question 4, stated flat

**Total GSK-3β:** essentially unchanged. Normalised to β-actin, `−/−` reads 1.09× · 1.13× · 1.18×
of `+/+` across cerebellum, hippocampus and cortex — a small upward drift on single lanes with no
replicate values, no dispersion and no test. The panel does **not** establish an abundance change.

**Ser9 phosphorylation:** reduced in `−/−` in all three regions; on the pS9/total ratio the fall
is to 0.44× · 0.49× · 0.54× of wild type. This is the panel's real signal.

**Genotype pattern:** `−/−` separates from both other genotypes; `+/−` is **not intermediate** but
at wild-type level (1.05× · 0.93× · 0.89×), with no dosage gradient.

**Statistical support:** **none.** Four independent experiments are declared in the legend; one
representative blot is shown; no mean, no SD, no SEM, no test, no P value and no significance
marker is attached to panel c anywhere in the article or its supplement.

**What panel c therefore establishes:** that in drug-naive `Wwox−/−` mouse brain at P20, the
inhibitory Ser9 phosphorylation of GSK3β is lower than in littermate controls, in three regions,
on one representative of four blots, without statistics — while total GSK3β abundance is
approximately unchanged. It establishes an **association measured in untreated animals**. It
establishes nothing about seizures, nothing about lithium, and nothing about causal direction.

---

## 3 · Answer to dispatch question 7 — the layer partition

The dispatch requires ENTITY / OBSERVATION / RELATION / HYPOTHESIS / INTERVENTION / PHENOTYPE to
be held apart rather than compressed into one node type. Every proposition this paper licenses,
placed:

### 3.1 Disease-mechanism graph — what may become a mechanism edge

| Proposition | Layer | Type | Note |
|---|---|---|---|
| WWOX loss of function ⟷ reduced GSK3β Ser9 phosphorylation in brain, P20, three regions | RELATION over ENTITY(WWOX) → ENTITY(GSK3β state) | `ASSOCIATED` | drug-naive, cross-sectional, unstatisticized, no dosage gradient |
| `Wwox−/−` mice show a lowered threshold to chemoconvulsants and spontaneous seizures from ~P12 | PHENOTYPE | `DATO` | a phenotype of the genotype, not a relation between two molecules |

🔴 **Nothing in this paper licenses a mechanism edge from GSK3β state to the seizure phenotype.**
That edge exists only through the lithium experiment, and the lithium experiment is neither
genotype-specific nor target-attributed (pilot §7, §8). Placing it in the mechanism graph would
put a pharmacological inference into the layer reserved for measured mechanism.

### 3.2 Pharmacological observation layer

| Proposition | Layer | Type |
|---|---|---|
| LiCl 60 mg/kg i.p. ×3 within 1 h reduces PTZ-evoked Racine score — **in `+/+`, `+/−` and `−/−` alike** | INTERVENTION → PHENOTYPE | `DATO`, genotype-nonspecific |
| Ethosuximide 150 mg/kg 45 min pre-PTZ reduces PTZ-evoked score significantly in `−/−`, `n.s.` in `+/+` and `+/−` | INTERVENTION → PHENOTYPE | `DATO`, with a floor confound and no interaction test |
| GSK3β activity was **not** measured in any lithium-treated animal | *evidence boundary* | the absence that blocks target attribution |

This layer must be typed as pharmacology and **must not inherit the mechanistic node's name**.
The failure mode is precise: an edge labelled *"GSK-3β inhibition suppresses seizures"* reads as
mechanism while resting entirely on an intervention whose target was never verified.

### 3.3 Hypothesis layer

| Proposition | Type |
|---|---|
| GSK3β de-repression contributes causally to seizure susceptibility in WWOX deficiency | `IPOTESI` — the composite `CLAIM 016` asserts; not carried by this paper |
| Lithium's anticonvulsant effect here runs through GSK3β rather than through inositol monophosphatase or Wnt/β-catenin | `IPOTESI` — untested; the paper's own Discussion lists the alternatives |
| GSK3β is an amplifier of an already-misassembled network rather than a standalone driver | `INFERENZA` — already carried in `CLAIM 016`; Fig. 7d is arguably better evidence for this than for the target-specific reading |

**Decisive next evidence, unchanged from the pilot:** a selective GSK3β inhibitor, or a
conditional *Gsk3b* manipulation, in all three genotypes, with an explicit genotype × treatment
interaction test, against **spontaneous** seizures on video-EEG.

---

## 4 · Answer to dispatch question 8 — two further figure/text mismatches

The pilot recorded two (the lithium panel's selective silence; the `CLAIM 016` Fig. 7b/7d pointer
defect). Two more, both material to graph typing:

### 4.1 🔴 The Results text reports no result for Fig. 7c

The entire Results treatment of panel c, BODY-EXACT:

> *"To investigate whether the enhanced epileptogenesis in Wwox−/− mice is due to increased GSK3β
> activation in neuronal cells, we determined dephosphorylation of GSK3β at Ser9 (active GSK3β)
> in Wwox−/− mouse cerebellum, hippocampus and brain cortex by western blotting (Fig. 7c).
> Injection of a potent GSK3β inhibitor lithium chloride significantly suppressed PTZ-induced
> epileptic seizure in Wwox−/− mice (Fig. 7d). Together, these results suggest an important role
> of GSK3β in the hypersusceptibility to epileptic seizure induction due to Wwox loss in neuronal
> cells."*

The Results sentence names the **method** and the **figure** and states **no finding** — no
direction, no magnitude, no comparison. The result exists only in the legend and in the panel.
The two sentences are then joined by *"Together, these results suggest…"*, and the joint sits on
one measurement whose outcome the running text never states.

**Why it is material.** Any curation pipeline that extracts from Results — the conventional
surface — extracts *nothing* from panel c and then meets a summary sentence asserting an
important role for GSK3β. The evidence and the conclusion are on different surfaces. This is the
same structural hazard the pilot found on the DisMech side, where the node's evidence snippet was
abstract-sourced: **the qualification and the claim keep landing on surfaces that are not read
together.**

### 4.2 🔴 The figure's own title is the strongest causal claim in the paper

> *"Increased GSK3β activity in the brain tissues **leads to** hypersusceptibility to drug-induced
> seizure in Wwox knockout mice."* — Fig. 7 title, BODY-EXACT

*"Leads to"* is a causal assertion. The figure it titles contains: an unstatisticized
representative blot in **untreated** animals (c), and a drug experiment that works in
**wild-type** animals (d). No panel measures GSK3β activity and seizure susceptibility in the
same animal, and no panel manipulates GSK3β specifically. **The title asserts the edge; no panel
under it tests the edge.**

This matters for graph work more than for reading: figure titles are short, declarative and
causally phrased, which makes them the most extractable and the least evidenced sentences in a
paper.

### 4.3 Summary of figure/text mismatches material to the graph

| # | Mismatch | Direction | Where recorded |
|---|---|---|---|
| 1 | Legend and Results name only `Wwox−/−` for lithium; the panel marks all three genotypes | text **narrower** than panel | pilot §5 |
| 2 | `CLAIM 016` cites Fig. 7b for a lithium finding that is in Fig. 7d | canonical pointer sends the verifier to the panel that appears to refute the claim | pilot §11 |
| 3 | Results states no result for Fig. 7c; the finding exists only in legend + panel | text **empty** where the panel carries the evidence | §4.1 here |
| 4 | Fig. 7 title asserts *"leads to"*; no panel under it tests causation | text **stronger** than every panel | §4.2 here |
| 5 | `CLAIM 016` `Summary`/`Type` say "elevated"/"abbondanza"; the same record's later block says that wording is wrong | canonical record internally inconsistent | §1.5 here |

---

## 5 · Negative evidence sought against my own reading

The attractive interpretation *for me* — having found the wild-type lithium response — is that
this paper's GSK3β story is weak throughout. That reading was tested against the panel and it is
**too strong in one place**, so it is corrected here rather than carried:

- **The Ser9 observation is a real and sizeable effect.** ~2× on the normalised ratio, in the same
  direction, in three independently dissected regions, consistent with a declared n = 4. Absence
  of statistics is a reporting failure, not evidence of absence — the effect size and the
  three-region concordance are what a real finding looks like. My §1.3 says the panel carries no
  statistical support; it does **not** say the observation is false, and the distinction is the
  whole point.
- **The abundance direction really is upward.** 9–18%. `CLAIM 016`'s "elevated" is weak, not
  invented. Calling it invented would be over-correction — the same error with the sign reversed.
- **The heterozygote result cuts against a mechanism I might have preferred.** If loss of WWOX
  de-repressed GSK3β proportionally, `+/−` should sit between. It does not. That is evidence
  against a simple dose-dependent WWOX→GSK3β mechanism, and it is recorded because it weakens a
  reading I find attractive, not one I find inconvenient.
- **Searched and not found:** any statistical treatment of panel c anywhere in the article or its
  24-page supplement; any measurement of GSK3β in a lithium-treated animal; any supplementary
  figure bearing on GSK3β, lithium or seizures. Three targeted absences, each scoped to the
  surface searched.

---

*Non-canonical. Nothing here is medical advice. No canonical file was modified in producing it.*
