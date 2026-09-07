---
artifact: LEGEND scientific evaluation — HARD-CASE MINING for benchmark candidates
id: HARD_CASE_MINING_BENCHMARK_CANDIDATES_SCIC_v1
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
worktree: lettore-c · branch lettore-c · HEAD 5b1d6c2 (14 ahead of main, 0 behind)
date: 2026-08-25
scope: SCIENTIFIC ANALYSIS / EVALUATION PREPARATION. No governance, role-contract or
  architecture analysis is performed or proposed here.
status: NON-CANONICAL. Mutates nothing. No canonical file, manifest, receipt or ledger is edited.
canonical_mutation: NONE
---

# Hard cases that already exist in this corpus, and which of them can carry a gold standard

> **Nothing here is medical advice.** This document evaluates reasoning surfaces, not therapy.

---

## 0 · Provenance, before any case

**No case below is invented.** Every one is anchored to a paper this repository has opened, or to
a rejection this repository has already adjudicated. The mining surfaces were:

| Surface | Location | Count (object-derived, at `5b1d6c2`) |
|---|---|---|
| Full-text queue entries | `disease-models/wwox/research/full_text_queue_current.md` | **72** `FT-` entries |
| Deep-dive manifests | `.../research/deepdive_manifests/` | **64** JSON |
| Prose dossiers | `.../research/fulltext_dossiers/` | **33** |
| Claim registry | `.../registries/claim_registry_current.md` | **39** claims |
| Dismissal ledger | `.../research/dismissal_ledger_current.md` | 11 active rejections + 16 `DEFAULTS THAT BIT US` |
| Local full-text with figures | `files/fulltext/` in **this worktree** | **1** (Cheng 2020: JATS XML + 7 figure PNGs + 20.6 MB supplementary PDF) |

### 0.1 · The marker that runs through this document

Two actors have already read most of these papers, and a benchmark built by copying their findings
would inherit their errors along with their results. So each factual claim below carries one of:

- **✅ RE-DERIVED** — I measured it myself this session, from the primary artifact, and the command
  is reproducible.
- **◻ INHERITED** — it comes from a repository artifact (queue entry, ledger, manifest) and I did
  **not** re-verify it. It is a *candidate* fact. A benchmark built on it must re-verify it first.

Only **one** paper's primary surface exists in this worktree (`files/` is gitignored and per-worktree),
so the ✅ set is necessarily small and concentrated on Cheng 2020. **That is a limit of this run, not
a judgement that the ◻ set is weaker.** It is stated so nobody reads the asymmetry as evidence.

### 0.2 · What I re-derived, with the numbers

| Measurement | Value | How |
|---|---|---|
| Cheng 2020 JATS digest | `sha256 792b5b296863674d…` · 156,335 bytes | `hashlib` over `PMID32000863_Cheng2020_PMC.xml` |
| Cleaned body | **71,961** characters | strip tags → collapse whitespace |
| Term counts | `lithium` 9 · `LiCl` 4 · `GSK` 24 · `ethosuximide` 5 + `Ethosuximide` 2 · `ANOVA` 3 · `interaction` 2 | regex over cleaned body |
| Both `interaction` hits | **in the reference list**, not in Methods | context print, ±150 chars |
| Statistical analysis section | *"one-way analysis of variance (ANOVA) to compare the difference among groups… P values less than 0.05"* — **no post-hoc, no multiplicity correction, no interaction term** | verbatim extract |
| Figure 7 legend | defines **only** `n.s.` and `*** P < 0.001` | verbatim extract |
| Figure 7 image | 1946 × 1627 px | PIL |
| Panel 7d `+/−` | `****`, PTZ N=12 vs PTZ+LiCl N=12 | crop, native resolution |
| Panel 7d `−/−` | `****`, PTZ N=6 vs PTZ+LiCl N=7 | crop, native resolution |
| Panel 7b `−/−` | `***`, Control N=4 · PTZ N=6 · PTZ+ETS N=6 | crop, native resolution |

🔴 **Two honesty notes on my own numbers.**

1. **My cleaned-character count disagrees with my own earlier one.** `PHASE2_CROSS_REVIEW_SCIC_v1.md`
   records **71,916**; I measure **71,961**, a difference of 45 characters. Neither is wrong: the
   two whitespace-normalisation transforms differ. **The transform is part of the measurement**, and
   any benchmark that scores a *count* must publish the transform, not just the number.
2. **I did not re-verify the `+/+` panel of Figure 7d this session** — my crop cut its legend. Phase I
   recorded `****` with N=12 vs N=8. Two of three panels are ✅; the third stays ◻.

### 0.3 · The novelty check, run before claiming any finding

Three of the findings I re-derived felt like discoveries and were not. Before writing them up I
grepped the repository: the undefined `****` is already in my own `PHASE1 §411`; the
`Fig. 7b`/`7d` pointer defect is already in `PHASE1 §441–454`. **Both are re-derivations.**
They are still good benchmark items — a benchmark case does not need to be new, it needs to be
*true and re-checkable* — but calling them discoveries would have been the third instance of the
failure `OPERATING_PRACTICE_OBSERVED_SCIC_v1 §1` describes: an actor re-finding what the repository
wrote down and lost.

---

## 1 · Method and rubric

**Selection rule.** A case qualifies only if (a) a real published surface decides it, (b) a
competent careful reader could plausibly get it wrong, and (c) the wrong answer would propagate
into a claim rather than die immediately.

**Classification rubric**, applied uniformly:

| Class | Test it must pass |
|---|---|
| `HIGH_VALUE_BENCHMARK` | ground truth is recoverable from an obtainable surface; the failure mode is one a good reader actually commits; the correct answer discriminates overclaim from underclaim |
| `USEFUL_STRESS_CASE` | exercises a real capability, but ground truth is partly conventional, or the failure is easy to avoid once named |
| `TOO_AMBIGUOUS` | the record genuinely underdetermines the answer, and no verdict is defensible |
| `TOO_DEPENDENT_ON_UNRESOLVABLE_SURFACE` | the deciding surface cannot be obtained by any route open to this system |
| `LOW_VALUE` | true, but tests nothing a simpler case does not |

**Distribution of the 48 cases mined** (object-derived — count the `CLASS:` lines in this file):

| Class | Count |
|---|---|
| `HIGH_VALUE_BENCHMARK` | **37** (32 science · 3 provenance · 2 infrastructure) |
| `USEFUL_STRESS_CASE` | **6** |
| `TOO_DEPENDENT_ON_UNRESOLVABLE_SURFACE` | **1** + 1 dual-axis (`HC-I2`) |
| `TOO_AMBIGUOUS` | **1** |
| `LOW_VALUE` | **2** |

🔴 **The ratio is not a boast, and reading it as one would be the first error.** These 48 were mined
from surfaces where somebody had *already* found something hard — 72 queue entries and 11 adjudicated
rejections, all written by actors who record their own failures. **The population was pre-enriched for
difficulty**, so this distribution says nothing about the corpus at large, and a benchmark suite drawn
only from here would over-represent papers that have already been fought over.

🔴 **The prohibition I am holding to.** Where the correct answer is `UNRESOLVABLE` or the surface is
`UNVERIFIABLE`, I say so **in the `EXPECTED_EPISTEMIC_VERDICT` field itself** and do not manufacture
a graded answer. A case whose gold label is *"this cannot be decided"* is a legitimate and valuable
benchmark item — **but only if labelled that way.** Grading it as though it had a positive answer
would build a false gold standard, which is the one outcome the task forbids and the one this
corpus is most exposed to.

---

## 2 · The cases

### AXIS A — Abstract / text / figure disagreement

---

#### `HC-A1` — Does lithium suppression in Cheng 2020 apply only to *Wwox*-null mice?

- **SCIENTIFIC_QUESTION:** Is the lithium anticonvulsant effect genotype-restricted to `−/−`?
- **SOURCE:** PMID 32000863, Cheng et al. 2020, *Acta Neuropathol Commun* — Figure 7d + Results + Fig 7 caption. ✅ **RE-DERIVED**
- **WHY_DIFFICULT:** Results and caption both name only `Wwox−/−`. Both sentences are **true**. The panel marks the effect in all three genotypes at the same declared level. A text-only reader inherits a restriction the figure does not carry, and inherits it from sentences that are not false.
- **EXPECTED_CORRECT_REASONING:** Read 7d panel-by-panel. Record `+/+` N=12 vs 8, `+/−` 12 vs 12, `−/−` 6 vs 7, each bracketed `****`. Conclude the *text* is true-and-incomplete, and that the effect is present in controls. Then go one step further: check whether a genotype × treatment interaction was tested. ✅ It was not — Methods declare one-way ANOVA only, and both instances of the word `interaction` in the whole document are in the bibliography.
- **COMMON_FAILURE_MODE:** Extracting "lithium suppresses seizures in Wwox-null mice" as a genotype-specific rescue, and promoting it as mechanistic support for a GSK3β-targeted therapy.
- **MINIMUM_REQUIRED_EVIDENCE:** Figure 7d at native resolution, all three sub-panels + Methods *Statistical analysis*.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Figure 7b (ethosuximide) *is* genotype-restricted — `n.s.` in both controls, `***` in `−/−`. A reader who reports "all drug panels in this paper are non-specific" has over-generalised; 7b proves the paper *can* show restriction when it exists, and reported it when it did.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` that lithium suppresses PTZ seizures in all three genotypes. **`UNRESOLVABLE` whether the rescue is WWOX-specific** — the difference-of-differences was never computed.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** (a) "lithium specifically rescues the WWOX-null phenotype"; (b) equally, "lithium is non-specific" — that asserts an absence of interaction that was never tested.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Reporting only the text's null-restricted sentence; or flagging "figure may show more" without reading the panels.
- **BENCHMARK_VALUE:** Very high. It is the rare case where **both** directions are overclaims and the correct answer is a declared limit. It also discriminates readers who stop at "the figure says more than the text" from readers who then ask what test would settle it.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-A2` — What significance level does the lithium result carry?

- **SCIENTIFIC_QUESTION:** What P-threshold does `****` denote in Figure 7?
- **SOURCE:** PMID 32000863 — Figure 7 legend vs panel 7d. ✅ **RE-DERIVED**
- **WHY_DIFFICULT:** The legend defines exactly two tokens: `n.s., non-significant` and `*** P < 0.001`. Panel 7b uses `***` (defined). Panel 7d prints `****` (undefined). ✅ `****` occurs **zero** times in the cleaned text surface. The figure asserts a level the paper never defines, and the token *looks* self-explanatory.
- **EXPECTED_CORRECT_REASONING:** Note that four asterisks is a **convention**, not a definition; that GraphPad's common mapping (`****` = P<0.0001) is a property of the plotting software, not of this paper; and that the paper's own Methods declare only a single α = 0.05. Report the level as not recoverable from the published record.
- **COMMON_FAILURE_MODE:** Silently importing `P < 0.0001` from software convention and recording it as the paper's datum — a fabricated number with a real-looking provenance.
- **MINIMUM_REQUIRED_EVIDENCE:** Figure 7 legend verbatim + panel 7d image + a text search proving `****` is undefined in prose.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** `***` in panel 7b **is** defined by the same legend. A system that flags every asterisk as undefined has learned nothing; it must flag exactly the one the legend omits.
- **EXPECTED_EPISTEMIC_VERDICT:** **`UNRESOLVABLE`** — the significance level of the lithium comparison is not determinable from this record. The *direction* and the *presence* of an effect are `DATO`.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Recording `P < 0.0001`. Also: declaring the result invalid — an undefined token is not a refuted result.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Discarding panel 7d entirely for want of a defined threshold.
- **BENCHMARK_VALUE:** High, and unusually clean: a single binary — did the system import a convention as a datum?
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-A3` — Iacomino/Repudi 2020: progenitors or neurons?

- **SCIENTIFIC_QUESTION:** Does the migration defect reside in progenitors or in post-mitotic neurons?
- **SOURCE:** PMID 32581702, *Front Neurosci* — abstract vs panel; manifest `PMID32581702.json` entries[11]. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The abstract attributes to **progenitors** what the panel shows in **neurons**. The abstract is the surface most likely to be indexed, quoted and transferred.
- **EXPECTED_CORRECT_REASONING:** Identify the cell population actually labelled in the panel; treat the abstract's attribution as an authored summary, not an observation.
- **COMMON_FAILURE_MODE:** Building a progenitor-stage mechanistic model from an abstract sentence, then selecting stage-inappropriate experiments downstream.
- **MINIMUM_REQUIRED_EVIDENCE:** The panel + its marker legend; the abstract sentence verbatim.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** The same paper's BrdU experiment genuinely *is* a progenitor assay — a reader must not conclude "nothing in this paper concerns progenitors".
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` at the neuronal level; the progenitor attribution is `INFERENZA` of the authors, unsupported by the cited panel.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Recording a progenitor-autonomous migration defect.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Declaring the paper uninformative about cell type.
- **BENCHMARK_VALUE:** High — abstract-vs-panel with a clean cell-identity ground truth.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` *(re-verify the ◻ before use)*

---

#### `HC-A4` — Breton 2021: which synaptic arm changed more?

- **SCIENTIFIC_QUESTION:** In *Wwox*-KO neocortex, is the excitatory or the inhibitory change the larger effect?
- **SOURCE:** PMID 34634460, *Neurobiol Dis* — manifest entries[6],[7],[18]. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Excitatory +6% (23.3 → 24.7 pA) against inhibitory −52% (57.3 → 27.5). **The abstract lists them in the opposite order of magnitude.** Order of presentation reads as order of importance, and the numbers live in panels.
- **EXPECTED_CORRECT_REASONING:** Extract both magnitudes from the panels; rank by effect size, not by sentence order; report the inhibitory arm as dominant.
- **COMMON_FAILURE_MODE:** Reproducing the abstract's ordering into an E/I imbalance claim that inverts which arm carries the phenotype — with direct consequences for which drug class looks rational.
- **MINIMUM_REQUIRED_EVIDENCE:** Both amplitude panels with their axis values.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** A +6% change is not zero; a system must not round the excitatory arm away to make the story clean.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO`, inhibitory-dominant, with the excitatory change small and retained.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** "WWOX loss abolishes excitatory transmission"; or asserting a *ratio* the paper never computed.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** "E/I balance is altered" without direction — the direction is the actionable part.
- **BENCHMARK_VALUE:** High; tests whether magnitude beats narrative order.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` *(re-verify the ◻ before use)*

---

### AXIS B — Figure- and table-dependent claims

---

#### `HC-B1` — Wang 2012: does WWOX bind Tau?

- **SCIENTIFIC_QUESTION:** Does Supplementary Figure A establish that WWOX does not co-immunoprecipitate Tau?
- **SOURCE:** PMID 22193544, Wang et al. 2012 — Supplementary Figure A, its published legend, and the Results sentence. ◻ **INHERITED** (`dismissal_ledger` D-14 / DIS-010)
- **WHY_DIFFICULT:** This is the hardest case in the corpus. ◻ The main text says *"Tau was not co-immunoprecipitated… indicating that WWOX does not stably interact with Tau"*; the **published legend** says *"anti-Tau was used to detect endogenous Tau protein"*. **The image contains no Tau blot.** Its two panels are labelled **WWOX** and **GSK3β**, and the lower shows a faint *positive* band in the HA-IP lane. Text and caption **agree with each other**, and both are wrong — so cross-checking prose against prose cannot catch it. Only the raster does.
- **EXPECTED_CORRECT_REASONING:** Open the supplementary image. Read the panel labels. Observe no anti-Tau blot exists. Conclude the paper's only evidence for its negative is **absent from the displayed record**, and that it cannot be determined whether this is a swapped figure or mislabelled panels. Therefore: the negative is **not established**, and — critically — it is **not refuted either**.
- **COMMON_FAILURE_MODE:** Registering `conflicting evidence` against a live WWOX–Tau mechanism on caption authority. That fabricates a **false negative**: silent, permanent, self-reinforcing, and never retested.
- **MINIMUM_REQUIRED_EVIDENCE:** The supplementary figure **image**, at a resolution where panel labels are legible.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** **YES — decisive**
- **NEGATIVE_CONTROL:** The GSK3β co-IP in the same supplementary panel is genuine and *positive*, consistent with main-text Fig 2c. A reader must not discard the whole figure as unreliable.
- **EXPECTED_EPISTEMIC_VERDICT:** **`UNRESOLVABLE` / not evaluable.** The Tau arc of the mechanism is *intact and untested by this work*. Note that the opposing claim (Chang/Sze) rests on yeast two-hybrid — **neither side is solid.**
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** "WWOX does not bind Tau" (from text/caption). **Equally an overclaim:** "the figure proves WWOX binds Tau" — the faint band is a GSK3β lane.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Noting the discrepancy but still recording `conflicting evidence`; or omitting that the published record cannot distinguish swap from mislabel.
- **BENCHMARK_VALUE:** **The single most valuable case in this corpus.** It is the only one where prose-vs-prose consistency is a trap rather than a check, and where the correct answer is a refusal to grade.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` — with gold label `UNRESOLVABLE`

---

#### `HC-B2` — Aqeilan 2008: which bar is the knockout?

- **SCIENTIFIC_QUESTION:** In Figure 4B, which bar corresponds to `KO`?
- **SOURCE:** PMID 18487609, *WWOX is essential for postnatal survival and normal bone metabolism*. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Three bars per group, **two labels**: `WT HT` on light grey, `KO` on black, and an unlabelled dark-grey third box. **Read literally, the legend inverts the phenotype.** The true order (light = WT, black = HT, dark = KO) is recoverable only by crossing three directional statements in the running text.
- **EXPECTED_CORRECT_REASONING:** Detect that labels < bars. Refuse the literal reading. Reconstruct assignment from independent directional text statements, and declare the reconstruction as such.
- **COMMON_FAILURE_MODE:** Taking the legend at face value and recording a bone phenotype of inverted sign.
- **MINIMUM_REQUIRED_EVIDENCE:** Panel 4B image + the three directional sentences.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Figure 3B in the same paper is correctly labelled — the defect is local, not a property of the paper.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` **only after** cross-text reconstruction, and tagged as reconstructed.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Reporting either sign without declaring the reconstruction.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Discarding 4B as unreadable when the text does determine it.
- **BENCHMARK_VALUE:** High — tests whether a system can hold "the figure is defective **and** the fact is recoverable" simultaneously.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` *(re-verify the ◻)*

---

#### `HC-B3` — Breton 2021: the sign of the lag

- **SCIENTIFIC_QUESTION:** What is the sign of the cross-correlation lag in Figure 2C?
- **SOURCE:** PMID 34634460 — panel 2C axis. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The axis reads `100, 0, 100, 200` — **the minus sign is missing**, on the one panel that defines the sign of the lag, i.e. which region leads.
- **EXPECTED_CORRECT_REASONING:** Detect the non-monotonic axis; infer the intended `−100`; declare the direction as inferred from axis geometry, not printed.
- **COMMON_FAILURE_MODE:** Reading a symmetric axis and reporting the lead/lag relationship backwards, or reporting it without noting it was inferred.
- **MINIMUM_REQUIRED_EVIDENCE:** Panel 2C at a resolution where tick labels are legible.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Other axes in the paper print signs correctly.
- **EXPECTED_EPISTEMIC_VERDICT:** `INFERENZA` on the sign; `DATO` on the magnitude.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Stating which region leads as a measured fact.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Dropping the lag analysis altogether.
- **BENCHMARK_VALUE:** Moderate-high; a compact typographic-defect probe.
- **CLASS:** 🟡 `USEFUL_STRESS_CASE`

---

#### `HC-B4` — Breton 2021: caption says none, panel prints one

- **SCIENTIFIC_QUESTION:** Is the Figure 5D comparison significant?
- **SOURCE:** PMID 34634460 — Fig 5D caption vs panel. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Caption states *"No significance"*; the panel prints `p = 0.0312` **with an asterisk**. Direct caption/panel contradiction with a printed number on the panel side.
- **EXPECTED_CORRECT_REASONING:** Prefer the printed statistic; flag the caption as contradicted; note that `p = 0.0312` is marginal and unadjusted, and that the paper's multiplicity handling is undeclared.
- **COMMON_FAILURE_MODE:** Recording "no significance" from the caption, converting a marginal positive into a negative that nobody retests.
- **MINIMUM_REQUIRED_EVIDENCE:** Panel 5D image + caption verbatim.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Panel 5D's neighbours have captions that match their panels.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` marginal-positive, unadjusted; caption in error.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Treating `p = 0.0312` as an established effect without noting it is unadjusted and marginal.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Following the caption.
- **BENCHMARK_VALUE:** High — cheap, unambiguous, and it manufactures a false negative if failed.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-B5` — The figure a language model drew

- **SCIENTIFIC_QUESTION:** How many categories of neurodevelopmental fragile-site gene does the review define, and is GRID1 among them?
- **SOURCE:** PMID 42128308, Obeid/Aqeilan 2026, *Neurobiol Dis* — §1 text vs Figure 2 + its caption. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The text lists **six** categories including *glutamate receptor signaling (GRID1, GRM5)*. Figure 2 shows **five**: the category vanishes, **GRID1 appears nowhere**, GRM5 is relocated under *neuron projection development*. Caption and panel agree with each other and both diverge from the body. The caption's last sentence: *"This figure was prepared using Gemini."*
- **EXPECTED_CORRECT_REASONING:** Recognise that the panel-over-prose preference is a rule about **data panels**, where the panel is the observation. This panel is a *rendering downstream of the prose*, and its own caption declares the generator. Therefore the text wins here, and the discriminant is free — the caption names the tool.
- **COMMON_FAILURE_MODE:** Applying "figure beats text" mechanically and carrying away that GRM5 is a neuron-projection gene and GRID1 is not a neurodevelopmental fragile-site gene at all — **wrong twice**, with the text having been right.
- **MINIMUM_REQUIRED_EVIDENCE:** §1 text, Figure 2 panel, Figure 2 caption **including the generator sentence**.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** The same paper's other figures declare *FigureLabs*, *Biorender* — also non-data renderings. A system must distinguish "schematic" from "observation" generally, not special-case the word *Gemini*.
- **EXPECTED_EPISTEMIC_VERDICT:** Text `DATO`-as-reported; Figure 2 carries **no independent evidential weight**. The discrepancy is a production defect, not a scientific conflict.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Recording the five-category taxonomy, or recording a genuine contradiction in the field.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Refusing to use the review's §1 list because "the figure disagrees".
- **BENCHMARK_VALUE:** Very high, and increasingly so — it tests whether a system knows the *boundary condition* of its own figure-priority rule, on a class of artefact that is proliferating.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-B6` — Saadane 2021: the solid line

- **SCIENTIFIC_QUESTION:** Is WWOX a substrate of calpain?
- **SOURCE:** PMID 34214506 — text assertion + Figure 10 pathway diagram + its own legend convention. ◻ **INHERITED** (`DIS-008`)
- **WHY_DIFFICULT:** ◻ The paper asserts *"Wwox was identified as a substrate for calpain"* and Figure 10 draws calpain→WWOX as a **solid line**, which the figure's own legend defines as a *confirmed pathway*. The visual convention supplies an evidential claim the experiments do not.
- **EXPECTED_CORRECT_REASONING:** Ask what was measured. Only **abundance** (LFQ) and **transcript** (qRT-PCR) — no cleavage assay, no fragment, no molecular-weight shift. Then note the direction is wrong for a substrate: calpain rises **and WWOX rises**, and *mRNA* rises, which a protease cannot cause. A more parsimonious route is in the authors' own discussion: calpain → NF-κB → *transcription* of `Wwox`.
- **COMMON_FAILURE_MODE:** Adding calpain as a fourth WWOX turnover route on the strength of a sentence and a line style.
- **MINIMUM_REQUIRED_EVIDENCE:** The methods/results inventory of assays + Figure 10 legend convention.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES (the legend convention is the trap) · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** The proteomic hit itself is unbiased and therefore a **strong observation**; only the mechanistic label is weak. A system that rejects the whole paper has over-corrected.
- **EXPECTED_EPISTEMIC_VERDICT:** The **assertion** is rejected; the **possibility** stays open and untested. Observation strength and interpretation strength are weighed separately.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Recording calpain-mediated WWOX proteolysis.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Concluding calpain is irrelevant to WWOX — the abundance correlation is real.
- **BENCHMARK_VALUE:** High — separates rejecting a *claim* from rejecting a *hypothesis*, which is the distinction this corpus most often loses.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

### AXIS C — Ambiguous, absent, or self-contradictory statistics

---

#### `HC-C1` — Salah 2013: a paper with no statistics

- **SCIENTIFIC_QUESTION:** Which comparisons in Salah 2013 are statistically supported?
- **SOURCE:** PMID 23370280, *Cell Death Dis*. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ **Zero statistics in the entire paper** — no statistics section, no P-value, no named test, no `n`. Bars carry `STDV`; panel 6d has no bars at all. And the text uses *"significantly"* **four times** for comparisons never tested.
- **EXPECTED_CORRECT_REASONING:** Enumerate the statistical apparatus and find it empty. Treat every *"significantly"* as an authorial adjective, not a test result. Grade the paper's directional observations as `DATO` (blots exist) while refusing all quantitative or significance language.
- **COMMON_FAILURE_MODE:** Ingesting *"significantly increased"* as a tested effect, because the word is a reliable signal in almost every other paper.
- **MINIMUM_REQUIRED_EVIDENCE:** A complete search for statistical vocabulary across the full text + panel inspection for error bars.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Absence of statistics is not absence of evidence; the co-IP directionality is still readable. A system must not zero the paper out.
- **EXPECTED_EPISTEMIC_VERDICT:** Qualitative `DATO`; **all** significance language `UNSUPPORTED`.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Any propagated significance or effect size.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Dismissing the paper — its central direction (WWOX antagonises ITCH on ΔNp63α) is visible in the blots.
- **BENCHMARK_VALUE:** High — tests whether the significance vocabulary is checked against apparatus rather than trusted.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-C2` — Breton 2021: the inverted asterisk ladder

- **SCIENTIFIC_QUESTION:** Which of `*` and `**` denotes the smaller P in Figure 3?
- **SOURCE:** PMID 34634460 — Fig 3 vs Fig 6. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ In Figure 3, `*` = 0.0036 and `**` = 0.0274 — **inverted**. In Figure 6 of the *same paper*, the convention is ordinary. A per-paper convention rule fails; a universal convention rule fails.
- **EXPECTED_CORRECT_REASONING:** Bind asterisks to their **printed numeric values per figure**, never to a global or per-paper convention.
- **COMMON_FAILURE_MODE:** Ranking findings by asterisk count and inverting the strength ordering of the paper's own results.
- **MINIMUM_REQUIRED_EVIDENCE:** Both figures' legends with numeric thresholds.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Figure 6 is ordinary — a system that flags the whole paper's asterisks as untrustworthy has over-flagged.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` with per-figure threshold binding.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Any cross-figure strength comparison by symbol.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Discarding Figure 3.
- **BENCHMARK_VALUE:** High; the scope of a convention is exactly what a reader assumes without checking.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-C3` — Abu-Odeh 2014: two P-values for one comparison

- **SCIENTIFIC_QUESTION:** What is the P-value of the comparison in Figure 2D?
- **SOURCE:** PMID 24550385, *J Biol Chem* — Methods vs panel 2D. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Methods declare `< 2.2E−18`; the panel prints `7.5591721538234e-12`. Both are in the paper, they disagree, and the panel's spurious 14-digit precision reads as authoritative.
- **EXPECTED_CORRECT_REASONING:** Record the conflict; prefer neither silently; note the panel value is machine output pasted unrounded, and that `< 2.2E−18` is R's floating-point floor rather than a computed value.
- **COMMON_FAILURE_MODE:** Recording whichever was read first, with no note that the other exists.
- **MINIMUM_REQUIRED_EVIDENCE:** Methods statistics paragraph + panel 2D.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** The direction of the effect is not in dispute at either value.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` on direction; the exact P is **`UNRESOLVABLE`** and both reported values should be carried.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Propagating a 14-digit P-value.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Reporting "significant" without recording that the record self-contradicts.
- **BENCHMARK_VALUE:** Moderate-high; tests precision hygiene and conflict retention.
- **CLASS:** 🟡 `USEFUL_STRESS_CASE`

---

#### `HC-C4` — Iacomino 2020: how many control fetuses?

- **SCIENTIFIC_QUESTION:** What is `n` for the controls in the paper's only human experiment?
- **SOURCE:** PMID 32581702 — Methods vs Results vs figure. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Methods say **one** fetus, Results say **three**, and the figure shows **one** Ctrl column per staining. Three surfaces, three readings, and the figure agrees with the smaller.
- **EXPECTED_CORRECT_REASONING:** Report the contradiction explicitly and treat the human arm as `n = 1`-supported at the level the figure displays, pending clarification.
- **COMMON_FAILURE_MODE:** Taking the Results number (larger, and in the section a reader trusts most).
- **MINIMUM_REQUIRED_EVIDENCE:** All three surfaces.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** The murine arm's `n` is consistent across surfaces.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` weak, `n` **`UNRESOLVABLE`**, human arm not promotable.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Citing `n = 3` human controls.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Deleting the human observation.
- **BENCHMARK_VALUE:** High — `n` is the most transferable and least re-checked quantity in the corpus.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

### AXIS D — Negative evidence

---

#### `HC-D1` — Do *Wwox*-null mice have epilepsy?

- **SCIENTIFIC_QUESTION:** Has epileptogenesis been measured in the *Wwox*-null mouse?
- **SOURCE:** PMID 30290271 (asserting) → PMID 19936220 (cited) → PMID 19500159 (terminal, incl. its Table 2). ◻ **INHERITED** (`DIS-011`)
- **WHY_DIFFICULT:** ◻ A two-hop citation chain, **never verified at either hop**, which entered `CLAIM 005`, the working-model changelog, a dossier, a session evaluation and `DL-MECH-072` — **five canonical surfaces, carried for months.** The terminal source contains no EEG, no seizure observation, no behavioural test and no brain histology; its only brain measurement is organ weight. And the decisive evidence is an **empty table cell**: Table 2's `Epilepsy` row is blank for both mouse models.
- **EXPECTED_CORRECT_REASONING:** Resolve the chain to its terminus. Distinguish "not measured" from "measured and negative". Here it is **stronger than absence**: the terminal source states in three places, and shows via an empty table row, that these mice have no reported epilepsy.
- **COMMON_FAILURE_MODE:** Accepting a citation as an attribution map; and treating an empty table cell as missing data rather than as a reported negative.
- **MINIMUM_REQUIRED_EVIDENCE:** All three papers, plus **Table 2 of the terminal source rendered**, not extracted as text — an empty cell is often lost in text extraction.
- **FULL_TEXT_REQUIRED:** YES (×3) · **FIGURE_OR_TABLE_REQUIRED:** YES — the table is decisive · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Human WWOX-DEE epilepsy is abundantly established. The rejection is about the **mouse model**, and a system that generalises it to the disease has failed the case in the opposite direction.
- **EXPECTED_EPISTEMIC_VERDICT:** Rejected **on contrary evidence**, not on absence.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Retaining epileptogenesis in the null mouse; or claiming the mouse is proven non-epileptic (unreported ≠ absent — the terminal source reports *no reported epilepsy*, which is a statement about the literature).
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Marking it "unverified" and leaving the claim standing in five files.
- **BENCHMARK_VALUE:** **Top-tier.** Multi-hop provenance, negative evidence, table-dependent, and a documented five-surface propagation cost.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-D2` — Aqeilan 2008: the untested null on osteoclasts

- **SCIENTIFIC_QUESTION:** Is osteoclast activity impaired in *Wwox*-KO?
- **SOURCE:** PMID 18487609 — Figure 3D + the sentence resting on it. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Fig 3D: RANKL moves `Wwox` from 1.00 → 0.77 (RAW264.7) and 2.23 → 1.67 (marrow) — **two systems, same direction**, error bars within the bar stroke, **no test named**. The text calls this *"did not result in significant changes"*, and on that null rests *"osteoclast activity is not impaired in vivo"*.
- **EXPECTED_CORRECT_REASONING:** Identify that no test was performed, so *"not significant"* is not a test result. Note the concordant direction across two independent systems is *positive* weak evidence, and that the downstream in-vivo claim inherits a null that was never computed.
- **COMMON_FAILURE_MODE:** Accepting the null, and with it the load-bearing in-vivo conclusion.
- **MINIMUM_REQUIRED_EVIDENCE:** Panel 3D with values + the absence of a named test.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** A ~23% change with tiny error bars may well be non-significant; the case is that it was **not tested**, not that it is significant.
- **EXPECTED_EPISTEMIC_VERDICT:** The null is `UNSUPPORTED`; the in-vivo claim is `PREMISE: DEFAULT_FROM_TEXTBOOK`.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Asserting osteoclast involvement.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Repeating "not significant" as the paper's finding.
- **BENCHMARK_VALUE:** High — the untested null is this corpus's most common silent error.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-D3` — The unchallenged oligodendrocyte readout

- **SCIENTIFIC_QUESTION:** Does oligodendrocyte-specific *Wwox* deletion produce a phenotype?
- **SOURCE:** `Olig2-Cre; O-KO`, reported via PMID 42128308 §. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ *"No major defects"* at baseline; defective **under cuprizone challenge**. A baseline-only readout returns a negative that is an artefact of the design.
- **EXPECTED_CORRECT_REASONING:** Treat an unchallenged readout in a compensable system as **uninformative**, not negative. State the challenge as a requirement for any future oligodendroglial null.
- **COMMON_FAILURE_MODE:** Recording "oligodendrocyte WWOX is dispensable".
- **MINIMUM_REQUIRED_EVIDENCE:** Both arms (baseline and challenge) from the primary, **not the review**.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** ◻ unknown
- **NEGATIVE_CONTROL:** Not every baseline negative is a design artefact; the argument requires a demonstrated challenge-revealed phenotype, which here exists.
- **EXPECTED_EPISTEMIC_VERDICT:** 🔴 **`IPOTESI`, not `DATO`** — I flagged during a prior run that I had called this "a false negative by construction" while its **only source is not peer-reviewed**. The shape of the finding holds; its support is weaker than I first stated.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Promoting the challenge requirement to a rule on this evidence.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Recording the baseline negative at face value.
- **BENCHMARK_VALUE:** Moderate — good concept, weak current substrate. **Use only after the primary is read.**
- **CLASS:** 🟡 `USEFUL_STRESS_CASE`

---

#### `HC-D4` — Abu-Odeh 2016: the text's "but not"

- **SCIENTIFIC_QUESTION:** Is K274R ubiquitinated in panel 4C?
- **SOURCE:** PMID 26675548 — panel 4C vs text. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The panel shows a **clear ubiquitination ladder** for K274R; the text says *"but not"*. Coherent with PMID 24550385's *predominant ≠ exclusive*, and here **better controlled** (equal anti-GST input across 12 lanes).
- **EXPECTED_CORRECT_REASONING:** Prefer the blot; reconcile with the earlier paper's "predominantly"; conclude K274 is the major but not sole site.
- **COMMON_FAILURE_MODE:** Recording an absolute site requirement, which then licenses a false design constraint on any K274-directed strategy.
- **MINIMUM_REQUIRED_EVIDENCE:** Panel 4C image + loading control lanes.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** PMID 24550385's own K274R lane. Two papers must agree on *predominant*, not on *exclusive*.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO`: K274 predominant, not exclusive.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** "K274 is the sole ubiquitination site."
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** "The site is undetermined."
- **BENCHMARK_VALUE:** High, and it is a two-paper case.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

### AXIS E — Causal claims supported only by association

---

#### `HC-E1` — Is GSK-3β the molecular target of the lithium rescue?

- **SCIENTIFIC_QUESTION:** Does Cheng 2020 demonstrate GSK-3β as the mediator of lithium's anticonvulsant effect?
- **SOURCE:** PMID 32000863 — Figures 7c and 7d, Methods, and the full-text distribution of `lithium`/`LiCl`. ✅ **RE-DERIVED**
- **WHY_DIFFICULT:** The paper is *organised* to imply the link. Figure 7c measures GSK3β (untreated mice); Figure 7d measures seizures (treated mice). **The two arms are never joined.** ✅ I enumerated all 13 occurrences of `lithium`/`LiCl` in 71,961 cleaned characters: abstract, an unrelated histology reagent (lithium carbonate in LFB staining), Methods dosing, the Fig 7d caption, one Results sentence, four Discussion sentences, the abbreviation list, and two reference titles. **No sentence and no panel reports any molecular measurement in a lithium-treated animal.**
- **EXPECTED_CORRECT_REASONING:** Four independent gaps, one decisive: (1) lithium is not a selective GSK-3β inhibitor; (2) no second, structurally unrelated inhibitor; (3) no genetic test — no *Gsk3b* knockdown or constitutively-active rescue; (4) **decisive** — no molecular readout in any treated animal.
- **COMMON_FAILURE_MODE:** Reading co-location within one figure as a causal chain, and promoting GSK3β to a validated target.
- **MINIMUM_REQUIRED_EVIDENCE:** Panels 7c and 7d + a complete enumeration of drug mentions across the full text.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO — but see the control below
- **NEGATIVE_CONTROL:** ✅ The supplementary PDF is the right place to check for a hidden treated-animal molecular arm. Prior work reported **zero** occurrences of `ithium`, `LiCl`, `GSK`, `thosuximide` in its 24 pages, and its nine figures are developmental/morphological per the XML's own additional-file listing. 🔴 **The denominator matters and was mis-stated once:** for a claim about what supplementary *figures* show, the relevant denominator is **nine figures**, not 17,570 extracted characters. Two surfaces agree: all GSK-3β and all pharmacology in this paper is Figure 7 alone.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO`: GSK3β Ser9 dephosphorylation in untreated nulls; `DATO`: lithium suppresses PTZ seizures. **`INFERENZA` unsupported** that the second acts through the first.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Recording GSK3β as a validated therapeutic target for WWOX-DEE on this paper.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Dismissing the GSK3β node — the abundance/phosphorylation observation is real and the residue-level mechanism is established elsewhere (PMID 22193544).
- **BENCHMARK_VALUE:** Very high — the archetypal "two arms, one figure, no bridge" error, on a locally verifiable surface.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-E2` — Abu-Odeh 2016: the ATR that was never measured

- **SCIENTIFIC_QUESTION:** Does the paper establish that WWOX modulates the **ATR**-mediated checkpoint?
- **SOURCE:** PMID 26675548, *Oncotarget* — title, antibody list, inhibitor identity, Figure 6 schematic. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The title asserts ATR. The antibody list (CHK1, p-CHK1 S296, p-H2AX, ATM, p-ATM S1981, KAP1, p-KAP1, p-H3, WWOX, GAPDH, HSP90, lamin) contains **no anti-ATR**. Zero occurrences of `p-ATR`, ATR inhibitor, or ATR knockdown. **The only inhibitor used is KU-55933, which is an ATM inhibitor.** Every ATR statement is p-CHK1 as proxy. And the paper's own Figure 6 schematic marks with a **`?`** precisely the WWOX→CHK1 arrow the title asserts.
- **EXPECTED_CORRECT_REASONING:** Inventory the measured entities against the claimed entity. Note the sole perturbation is ATM-directed and, worse, **depletes what should separate the two arms**: 48 h of ATM inhibitor zeroes p-ATM and p-KAP1, nearly zeroes ITCH and reduces WWOX — so "ATM-dependent signalling" and "chronic inhibition depleted the module" predict the same blot.
- **COMMON_FAILURE_MODE:** Taking the title as the finding; treating p-CHK1 as ATR-specific when ATM–CHK1 crosstalk is well documented.
- **MINIMUM_REQUIRED_EVIDENCE:** Methods antibody list + inhibitor identity + Figure 6 schematic.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES (the `?` is only in the panel) · **SUPPLEMENT_REQUIRED:** partly — see `HC-I5`
- **NEGATIVE_CONTROL:** The paper's cleanest result needs no proxy: **2.8 ± 1 vs 5.7 ± 1.7 breaks per cell**. A system must not discard the paper wholesale.
- **EXPECTED_EPISTEMIC_VERDICT:** ATR involvement **`UNSUPPORTED`**; a checkpoint phenotype is `DATO`; the responsible kinase is **`UNRESOLVED`**.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Recording WWOX as an ATR-pathway modulator.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Rejecting the DDR role of WWOX — which would also disturb `DIS-001`, whose argument against inhibiting ITCH rests on WWOX's DDR function.
- **BENCHMARK_VALUE:** Very high — title-vs-measurement, with a schematic that contradicts its own title.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-E3` — Obeid 2026: "restored"

- **SCIENTIFIC_QUESTION:** Does gene therapy restore SATB2/CTIP2 to wild-type levels?
- **SOURCE:** PMID 42128308 §10.4, reviewing PMID 42397075. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The review writes *"restored"*; the primary's own panels show **SATB2 ≈ 10× wild type** and **CTIP2 ≈ 3×**. The word survives because **the WT-vs-treated bracket is not drawn** — the comparison that would falsify it is absent from the figure, so nothing in the visual record contradicts the word.
- **EXPECTED_CORRECT_REASONING:** Compare treated against **WT**, not against untreated. Recognise ~10× as overshoot, which is a different and safety-relevant phenomenon from restoration.
- **COMMON_FAILURE_MODE:** Reading "restored" as normalisation; and, structurally, only checking comparisons the figure chose to draw.
- **MINIMUM_REQUIRED_EVIDENCE:** The primary's quantification panels including the WT arm.
- **FULL_TEXT_REQUIRED:** YES (both) · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** ◻ possibly
- **NEGATIVE_CONTROL:** Overshoot is not failure; the intervention does move the readout. Both must be held.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO`: marker levels rise above WT. *"Restored"* is `UNSUPPORTED`.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Recording normalisation to WT; or asserting overshoot is harmful without evidence.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Recording "markers increased" without the WT comparator.
- **BENCHMARK_VALUE:** High — tests whether the system supplies the comparison the figure omitted. **Note the preprint caveat in `HC-H1`.**
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

### AXIS F — Conflicting papers and multi-paper adjudication

---

#### `HC-F1` — ITCH and WWOX: which stabilises what?

- **SCIENTIFIC_QUESTION:** Does ITCH stabilise WWOX, or does WWOX block ITCH from degrading a third protein?
- **SOURCE:** PMID 23370280 (Salah 2013) + PMID 24550385 (Abu-Odeh 2014) + PMID 26675548. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ A commit candidate in this repository cites Salah 2013 for *"direct ITCH/proteasomal stabilization"*. Salah 2013 shows **WWOX antagonises ITCH** and stabilises **ΔNp63α**. **Substrate, stabiliser and direction all inverted.** Measured absences make it certain, not probable: `K63` zero occurrences, `Lys-63` zero, no sentence describes WWOX as ubiquitinated. Meanwhile Abu-Odeh 2014 independently shows ITCH ubiquitinates **WWOX** on K63 *independent of degradation*, lengthening its half-life (CHX chase; `Itch⁻/⁻` MEFs, 0.36 vs 1).

| | substrate | chain | outcome |
|---|---|---|---|
| 24550385 · 26675548 | **WWOX** | **K63** | stabilisation, degradation-**independent** |
| 23370280 | **ΔNp63α** | proteasome | degradation, **blocked by WWOX** |

- **EXPECTED_CORRECT_REASONING:** Both are true and not in conflict, and the reconciling frame is the authors' own: WWOX **competes** with other WW-domain proteins (YAP, ITCH) for shared targets via WW1/PY, while itself being an ITCH substrate on a non-degradative chain. Then the therapeutic inference that neither paper yields alone: **raising ITCH activity to stabilise WWOX would simultaneously increase ITCH-mediated degradation of its other substrates** — ΔNp63α here, p73 in Fig 7 of 24550385. **An ITCH lever is not WWOX-selective.**
- **COMMON_FAILURE_MODE:** Collapsing "proteasomal" and "K63, degradation-independent" into one mechanism because both are "ubiquitination".
- **MINIMUM_REQUIRED_EVIDENCE:** All three full texts; the CHX chase and `Itch⁻/⁻` panels; the competition sentences.
- **FULL_TEXT_REQUIRED:** YES (×3) · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** The two papers do **not** contradict each other. A system that records `conflicting evidence` has failed in the opposite direction from the original error.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` on both arcs; the composite non-selectivity conclusion is `INFERENZA`, explicitly cross-paper.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** The original *"direct ITCH/proteasomal stabilization"*; or proposing ITCH agonism as a therapeutic route.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Filing them as conflicting and dropping both.
- **BENCHMARK_VALUE:** **Top-tier.** Direction, substrate and chain-type must all be tracked, across three papers, with a therapeutic consequence that exists in none of them individually.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-F2` — Is there an intermediate genotype class?

- **SCIENTIFIC_QUESTION:** Does `null/missense` constitute an intermediate-severity class in WWOX-related disorders?
- **SOURCE:** PMID 36779245 (Oliver 2023, *Epilepsia*) vs PMID 42128308 (Obeid 2026 review). ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The three-class scheme **is Oliver's own** — *"classified into three genotypic classes… (1) null/null, (2) null/missense, (3) missense/missense"*. And Oliver's conclusion is: *"We found no difference between individuals with one or two missense variants and therefore no evidence to support an 'intermediate' phenotype."* The 2026 review presents class 2 as *"associated with intermediate phenotypes"* and then offers counterexamples to a framework **whose own source denies a third of it.** The data are binary on one axis only: n=75 (45/15/15); **time to death** p = .0085 log-rank, 5-year survival <50% vs >75%, 10-year 25% vs >60%; **time to seizure onset** p = .65. The paper itself groups the two missense classes as *"the other two, presumably less severe, genetic groups"*.
- **EXPECTED_CORRECT_REASONING:** Return to the framework's source before accepting a review's rendering of it. Report a **binary** split (double-null vs ≥1 missense) on **survival only**, and no genotype effect on seizure onset.
- **COMMON_FAILURE_MODE:** Inheriting the three-class scheme from the review, then treating counterexamples as anomalies within a valid framework rather than as evidence the class was never supported.
- **MINIMUM_REQUIRED_EVIDENCE:** Oliver 2023 §2.4, §3.6–3.7, **Table 3**, and the corresponding discussion.
- **FULL_TEXT_REQUIRED:** YES (both) · **FIGURE_OR_TABLE_REQUIRED:** YES — Table 3 and the survival curves · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Genotype **does** stratify survival. A system that concludes "genotype does not predict severity" has over-corrected on the strength of the seizure-onset null.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO`: binary survival stratification. The **intermediate class is `UNSUPPORTED` by its own source.**
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Using the three-class scheme; or "missense ⇒ residual function ⇒ milder" — falsified by a homozygous missense (p.Ser304Tyr) fatal in early infancy.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Declaring genotype uninformative.
- **BENCHMARK_VALUE:** **Top-tier.** It attacks a premise sitting under much of this repository's hypomorph and ASO reasoning, and the ground truth is a single quoted sentence in the framework's own source.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-F3` — Vigabatrin in WWOX-DEE

- **SCIENTIFIC_QUESTION:** What is the defensible position on vigabatrin?
- **SOURCE:** `CLAIM 001` — Choi 2026 (VABAM, n=2) · Shaukat 2018 (n=2, *"the spasms resolved"* in WWOX-null) · You 2024 · Chong 2023 · Gao 2025. ✅ registry text re-read; ◻ primaries not re-verified
- **WHY_DIFFICULT:** Genuinely conflicting small-n clinical evidence on **two different axes** — efficacy on spasms versus MRI toxicity — that do not exclude each other. Additionally, the mechanistic rationale from organoids (*depolarising GABA in immature neurons ⇒ GABAergic drugs underperform*) **does not predict these clinical outcomes**: vigabatrin resolved spasms in a WWOX-null.
- **EXPECTED_CORRECT_REASONING:** Hold both arms. Keep `conflicting evidence`, and be explicit that the mechanism remains valid *as a mechanism* while failing *as a predictor of clinical response*.
- **COMMON_FAILURE_MODE:** Resolving the conflict by mechanism — the most seductive move available, and the one the record forbids here.
- **MINIMUM_REQUIRED_EVIDENCE:** All five reports; MRI follow-up status per case.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** NO · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** You 2024 reports seizure reduction **without MRI follow-up** — absence of reported VABAM there is absence of *looking*, not of the event.
- **EXPECTED_EPISTEMIC_VERDICT:** `conflicting evidence`, sustained, on two non-exclusive axes. **Not medical advice.**
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** "Vigabatrin is contraindicated in WWOX-DEE"; or "vigabatrin is effective in WWOX-DEE".
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Collapsing to "insufficient evidence" without stating that both an efficacy signal and a toxicity signal exist.
- **BENCHMARK_VALUE:** High — tests resistance to mechanism-driven resolution of a clinical conflict, in the one domain where being wrong carries real-world weight.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` *(handle under the no-medical-advice rule)*

---

#### `HC-F4` — Which reference does the clause belong to?

- **SCIENTIFIC_QUESTION:** Which primary supports *"different, with some overlapping, tau residues"*?
- **SOURCE:** Review PMC3139124, citing `[75, 76]`; refs = Mukai 2002 (PMID 12065620) and Saeki 2011. ◻ **INHERITED** (`D-15`)
- **WHY_DIFFICULT:** ◻ A compound statement with a bracketed pair. The claim was attributed to ref 76 (Saeki 2011); Saeki measures **one site only, Ser396**, and never addresses site selectivity. The clause belongs to ref 75, **still unread**. **A bracketed citation range is not an attribution map.**
- **EXPECTED_CORRECT_REASONING:** Do not split a compound claim across a citation pair. Resolve each primary before propagating any clause.
- **COMMON_FAILURE_MODE:** Attaching the nearest reference to the nearest clause — plausible, cheap, and wrong roughly half the time by construction.
- **MINIMUM_REQUIRED_EVIDENCE:** Both primaries.
- **FULL_TEXT_REQUIRED:** YES (×2) · **FIGURE_OR_TABLE_REQUIRED:** NO · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Saeki 2011 genuinely supports the *other* clause (weaker GSK-3β2–tau interaction). Neither reference is spurious.
- **EXPECTED_EPISTEMIC_VERDICT:** Attribution **`UNRESOLVED`** until ref 75 is read; the clause must not be propagated with a source attached.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Citing Saeki for site selectivity.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Discarding the clause.
- **BENCHMARK_VALUE:** High, and highly generalisable — bracketed multi-citations are ubiquitous.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

### AXIS G — Model-, stage- and genotype-dependence

---

#### `HC-G1` — Does *Wwox* loss raise or lower Runx2?

- **SCIENTIFIC_QUESTION:** What is the sign of the RUNX2 change in *Wwox*-KO?
- **SOURCE:** PMID 18487609 — Fig 5A (in vivo) vs Fig 6C (isolated calvarial osteoblasts) vs the Discussion. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ **In vivo +50% femur / +39% calvaria; ex vivo isolated osteoblasts −70%. Same knockout, same paper.** The Discussion writes *"an indirect effect that leads to decreased RUNX2 expression **in bone** and in isolated osteoblasts"* — the *"in bone"* half is contradicted by its own Fig 5A, and 400 words earlier the same Discussion says *"slightly increased in both calvarial and femoral bone"*.
- **EXPECTED_CORRECT_REASONING:** Record **two signs, one per preparation**. Do not average, do not pick, do not let the summary sentence override the panels. State the constraint: a node that changes sign between tissue and isolated cell **cannot carry a repositioning hypothesis**.
- **COMMON_FAILURE_MODE:** Extracting the Discussion's single-sign summary, and inheriting a downstream direction that is wrong in half of all preparations.
- **MINIMUM_REQUIRED_EVIDENCE:** Fig 5A and Fig 6C quantifications + both Discussion sentences.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Not every in-vivo/ex-vivo difference is a sign flip; magnitude differences are ordinary. The case is the **reversal**.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` × 2, preparation-indexed. A single unqualified sign is `UNSUPPORTED`.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Any unqualified "WWOX loss decreases/increases RUNX2".
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** "Results are inconsistent" without recording that each preparation is internally consistent.
- **BENCHMARK_VALUE:** **Top-tier.** Model-dependence with a within-paper contradiction and an explicit downstream constraint.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-G2` — Is WWOX protein abundance a readout of WWOX function?

- **SCIENTIFIC_QUESTION:** Can protein level be used as a functional readout?
- **SOURCE:** P47T (WT-level protein, severe phenotype) and SCAR12 organoids (minimal protein, near-normal phenotype), via PMID 42128308. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The premise is falsified from **both directions** in the same review, and it is the tacit premise under most western-blot-based reasoning in this field.
- **EXPECTED_CORRECT_REASONING:** Decouple abundance from function. Note the companion measurement hazard from `CLAIM 035`: because WWOX's GSK3β inhibition is **S9-independent**, any WWOX-DEE study using phospho-S9 as a GSK3β activity readout produces a **false negative by construction**.
- **COMMON_FAILURE_MODE:** Ranking alleles by residual protein and inferring severity.
- **MINIMUM_REQUIRED_EVIDENCE:** Both primaries (not the review) + the S9-independence datum from PMID 22193544.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Johannsen's *normal transcript / protein not detected* is a genuine and load-bearing abundance datum — abundance is not meaningless, it is **not sufficient**.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` that abundance and function dissociate; abundance-as-severity-proxy is `PREMISE: DEFAULT_FROM_TEXTBOOK`, **false in this system**.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Predicting severity from residual protein.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Discarding abundance measurements entirely.
- **BENCHMARK_VALUE:** Very high — a premise, not a fact, and premises are what this corpus most needs tested.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-G3` — Developmental stage as a confound

- **SCIENTIFIC_QUESTION:** Is the OXPHOS↓/glycolysis↑ signature a metabolic phenotype or a differentiation-stage artefact?
- **SOURCE:** PMID 34268881, Steinberg 2021, *EMBO Mol Med* — RNA-seq subsection. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The signature is **confounded with the differentiation defect the paper declares in the title of the very section the datum comes from**. Metabolic and maturational signatures are collinear in developing tissue.
- **EXPECTED_CORRECT_REASONING:** Refuse to read the signature as an independent metabolic phenotype. State the operational consequence: **a Seahorse assay on KO vs WT at the same culture week would reproduce the confound**; the experiment must be paired by **differentiation stage**, not by age.
- **COMMON_FAILURE_MODE:** Recording a metabolic phenotype and designing the age-matched experiment that cannot distinguish the two.
- **MINIMUM_REQUIRED_EVIDENCE:** The RNA-seq subsection with its section heading + any staging data.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** ◻ nine supplementary items unretrieved
- **NEGATIVE_CONTROL:** A stage-matched comparison, if the paper contains one, would settle it. ◻ Not established that it does.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO` on the transcriptional signature; metabolic interpretation **`CONFOUNDED`**.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** A WWOX-specific metabolic rationale (this touches the ketogenic-diet rationale).
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Discarding the signature.
- **BENCHMARK_VALUE:** High — the confound is *named in the section heading*, so ground truth is unusually clean for a confounding case.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-G4` — Are heterozygotes normal?

- **SCIENTIFIC_QUESTION:** Do `Wwox` heterozygotes show a phenotype?
- **SOURCE:** PMID 34634460 (17% of slices vs 86%; Discussion: *"manifested similarly"*) and PMID 18487609 (organism-level silent; **−50% connectivity density, −54% bone surface** at tissue level, non-overlapping bars, and **the paper says so**). ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Two papers, opposite handling of the same question. Breton's Discussion flattens a **5-fold** difference into *"similarly"*; Aqeilan 2008 **correctly declares** its heterozygote tissue phenotype — a negative control that came back negative *for the paper*.
- **EXPECTED_CORRECT_REASONING:** Read the level of observation. Heterozygotes can be silent at organism level and affected at tissue level; "similar" at one level is not "similar" at another.
- **COMMON_FAILURE_MODE:** Adopting *"manifested similarly"* and losing the dosage gradient — which matters directly for carrier interpretation and for any dose-dependent therapeutic reasoning.
- **MINIMUM_REQUIRED_EVIDENCE:** Both papers' heterozygote panels with numbers.
- **FULL_TEXT_REQUIRED:** YES (×2) · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** Aqeilan 2008 is the built-in control: the same question, handled correctly, in the same corpus.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO`: level-dependent heterozygote phenotype. *"Manifested similarly"* is `UNSUPPORTED` at the slice level.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** "Heterozygotes are affected" without naming the level.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** "Heterozygotes are normal."
- **BENCHMARK_VALUE:** High, and it is a paired case — one paper fails, one succeeds, on the same question.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

### AXIS H — Preprint → publication

---

#### `HC-H1` — Which version of Steinberg was adjudicated?

- **SCIENTIFIC_QUESTION:** Do claims attributed to *"Steinberg et al. 2024"* describe the preprint or the accepted manuscript?
- **SOURCE:** PMID 42128308 cites `10.1101/2024.12.22.630016` (preprint); the accepted version is PMID 42397075, *Brain*. Likewise *"Obeid et al. 2026"* preprint → PMID 42422765. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The review cites **expired preprint DOIs for papers that are published**. The panels adjudicated in this repository at 258 ppi come from the *accepted* manuscript. So the *"restored"* contradiction of `HC-E3` is between **the review's reading of the preprint** and **a reading of the accepted manuscript** — two different objects.
- **EXPECTED_CORRECT_REASONING:** Resolve preprint DOIs to their published records before comparing. Where both versions are not held, **name the version each claim describes** and decline to call the difference a contradiction until the versions are compared.
- **COMMON_FAILURE_MODE:** Treating preprint and publication as one object, so that a version difference is scored as a scientific disagreement — or vice versa.
- **MINIMUM_REQUIRED_EVIDENCE:** **Both versions.** The preprint is not currently held.
- **FULL_TEXT_REQUIRED:** YES (×2 versions) · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** YES (supplementary panels are where such changes concentrate)
- **NEGATIVE_CONTROL:** The published version is what the field will cite; a version difference does not dissolve the `HC-E3` finding, it re-scopes it.
- **EXPECTED_EPISTEMIC_VERDICT:** **`UNRESOLVED` pending preprint retrieval.** The `HC-E3` overshoot finding stands **for the accepted manuscript**.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Asserting the review misread the primary, without holding the version it read.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Withdrawing `HC-E3` — the accepted manuscript was read directly.
- **BENCHMARK_VALUE:** Moderate-high **as an identity-resolution case**; low as a science case until both versions are held. Retrieving the bioRxiv version would convert it to `HIGH`.
- **CLASS:** 🟡 `USEFUL_STRESS_CASE` — becomes `HIGH_VALUE_BENCHMARK` once the preprint is acquired

---

### AXIS I — Locator, provenance, and surface traps

---

#### `HC-I1` — The italic that breaks every locator

- **SCIENTIFIC_QUESTION:** Why do 13 of 20 verbatim locators fail to verify against their own source?
- **SOURCE:** PMID 36779245 JATS + the extractor's normalisation. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The XML contains `<italic>WWOX</italic>‐DEE` **30 times**; the extractor joins every text node with a space, producing `WWOX ‐DEE` — **a space the author never wrote, fabricated at the markup boundary.** Verification: **7/20** as the validator stands; 9/20 with Unicode punctuation folding; 7/20 with space-free inline joining; **16/20 with both**. The remaining 4 fail late, on a citation marker — a **third distinct cause**, probably `<xref>` content. And because gene names are italicised in every journal, **`WWOX-DEE` is the token most likely to break a locator in the corpus built around that gene.**
- **EXPECTED_CORRECT_REASONING:** Diagnose the failure as a property of the **normaliser**, not of the readings. Measure each hypothesised cause separately and refuse to attribute the residual to a cause already tested.
- **COMMON_FAILURE_MODE:** Reading a low verification rate as evidence that readings were sloppy, and re-reading papers that were read correctly. ◻ A first hypothesis blaming Unicode punctuation alone recovers only 2 of 13 — it was **tested**, not asserted, which is why the second cause was found.
- **MINIMUM_REQUIRED_EVIDENCE:** Raw XML + extractor output + a per-hypothesis verification count.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** NO · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** 🔴 **A control that came back clean for the wrong reason, and must be stated as such.** 90 text locators across six manifests carried **zero** fabricated spaces — but those captures were verified *against the extractor itself*, so a fabricated space would have entered the snippet and **passed**. The protection was accidental, not designed.
- **EXPECTED_EPISTEMIC_VERDICT:** The readings are sound; the tooling is defective. Corpus-wide "not found" counts must be re-read in this light.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Declaring the corpus's locator health good on a fixed normaliser without re-measuring; **or** aggressive normalisation that would mask exactly the printable substitutions the surface sentinel exists to find.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Attributing failures to reader error.
- **BENCHMARK_VALUE:** **Top-tier for infrastructure.** It is the only case where the *measurement apparatus* is the defect, and where the naive fix would break a different guarantee.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-I2` — 92% of the corruptions are printable

- **SCIENTIFIC_QUESTION:** Is the Aqeilan 2005 text layer usable for verbatim locators?
- **SOURCE:** PMID 16061658 PDF, `sha256 075fdbbcd1e17c3b…`, 9 pages. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ **Suspicion by absence**: zero occurrences of `< > ≤ ≥ ± × − µ α β Δ` across 44,465 characters, in a paper that says *"significan"* six times and reports plasmid quantities throughout. Character-level damage: `63\x01` for `63×` (×1); `(6.0 Ag)` for **µg** (×16); `p73h` for **p73β** and `h-dystroglycan` (×7). **25 corruptions, 23 printable — 92%**, against the ~80% the governing rule estimates. **A control-character scan finds 2 of 25 and declares the surface clean.** And `p73h` is an **isoform name corrupted silently** — it reads as a plausible token.
- **EXPECTED_CORRECT_REASONING:** Screen by **expected-symbol absence**, not only by control characters. Refuse the surface rather than repair it — a hand correction at 16 points is indistinguishable from a rewrite and verifiable by nothing. Route to page adjudication (digest, page, rectangle in points, dpi, image SHA-256, published as a **recipe**, never as an image).
- **COMMON_FAILURE_MODE:** Passing a clean control-character scan and extracting locators containing silently wrong glyphs.
- **MINIMUM_REQUIRED_EVIDENCE:** The PDF + a symbol-absence screen + rendered pages.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES (page rendering) · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** ◻ Reported and negative, which is what makes the screen a screen: the `P 5 0.05` signature of another paper does **not** appear here, and the nine isolated `D` characters are genuine (FRA16D, panel D, cyclin D1) — **not** corrupted `Δ`.
- **EXPECTED_EPISTEMIC_VERDICT:** Text layer **`UNVERIFIABLE_SURFACE`**. Content is recoverable **only** by page adjudication. ◻ This was subsequently done under explicit operator authorisation.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Any verbatim text locator from this surface; or calling the paper irretrievable.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Declaring the paper unusable when page adjudication is available.
- **BENCHMARK_VALUE:** **Top-tier for surface screening**, and it carries a quantified refutation of the governing rule's own 80% estimate.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` (surface-screening axis) · 🔴 `TOO_DEPENDENT_ON_UNRESOLVABLE_SURFACE` (text-locator axis)

---

#### `HC-I3` — Six figures, none inside the body

- **SCIENTIFIC_QUESTION:** How many figures does Salah 2013 have, and will a reader see their captions?
- **SOURCE:** PMID 23370280 JATS, `sha256 d6d46a8c7a2d8ee9…`. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ **6 figures, 0 inside `<body>`.** A reader whose renderer clips to `<body>` sees **no caption at all and is not told**. ◻ Corpus-wide: **62 structured surfaces, 14 with figures outside the body, 8 with all of them outside.** Compounding it, the panel census **rejects on all six** — the captions are not where the parser looks — and separately this depositor uses **lowercase** panel letters while the matcher seeks `[A-J]`.
- **EXPECTED_CORRECT_REASONING:** Verify figure/caption recovery **against the whole article**, not the body, and treat a zero-caption result as a surface diagnostic rather than a paper property.
- **COMMON_FAILURE_MODE:** Silent, complete loss of the figure layer with no error raised — the panel budget then reads as satisfied because the denominator is zero.
- **MINIMUM_REQUIRED_EVIDENCE:** A caption census over the full XML tree, plus a figure-count cross-check.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** ◻ 29 of 41 analysable surfaces have captions inside the body — the defect is a class, not the norm.
- **EXPECTED_EPISTEMIC_VERDICT:** A surface property; no scientific verdict. Any reading of this paper that reports `figures: read` without captions is **`INVALID`**.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Declaring panel coverage complete.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Declaring the paper unreadable.
- **BENCHMARK_VALUE:** High — a silent-zero failure, the hardest kind to notice.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` (infrastructure)

---

#### `HC-I4` — The recipe that does not rebuild the artefact

- **SCIENTIFIC_QUESTION:** Can the declared text surface of PMID 42397075 be regenerated from its declared method?
- **SOURCE:** Receipt records *"PyMuPDF 1.26.5 page.get_text() default mode, pages joined in order"*; artefact `sha256 9c48aa0934…`. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The artefact is intact and the PDF digest still matches. But re-running the declared method yields `''.join` → `bab5bc5d…`, `'\n'.join` → `f2f053fd…`, `'\f'.join` → `76943b7b…` — **none match**, byte counts differ by 942. *"Pages joined in order"* leaves the separator unstated. **A derivation recorded only in prose decays silently; one a command runs cannot.**
- **EXPECTED_CORRECT_REASONING:** Distinguish **artefact integrity** (fine) from **recipe reproducibility** (absent). Retract nothing; record that a third party cannot rebuild the surface.
- **COMMON_FAILURE_MODE:** Treating a matching artefact digest as proof the method is reproducible; or retracting sound locators because the recipe fails.
- **MINIMUM_REQUIRED_EVIDENCE:** The PDF, the declared method, and ≥3 candidate join implementations.
- **FULL_TEXT_REQUIRED:** NO · **FIGURE_OR_TABLE_REQUIRED:** NO · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** 🔴 The same preflight produced a **false positive** worth keeping: an initial screen found zero `P\s*[<>=]\s*0?\.\d+` in 90,000 characters — the classic suspicion-by-absence signature — plus two `q`-between-digits hits. Both were artefacts of the probe: the paper writes thresholds with **`≤` (16 occurrences)**, and the `q` hits are `16q21-q23`, a cytogenetic locus. **The regex was incomplete, not the PDF.**
- **EXPECTED_EPISTEMIC_VERDICT:** Locators **valid**; provenance recipe **`NOT_REPRODUCIBLE`**.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Declaring the surface reproducible; or declaring the locators void.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Ignoring the recipe failure because the digest matches.
- **BENCHMARK_VALUE:** High for provenance, and it ships its own negative-control lesson.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` (provenance)

---

#### `HC-I5` — The supplement that decides the claim, behind a challenge

- **SCIENTIFIC_QUESTION:** Does K274 carry a signalling function beyond stability?
- **SOURCE:** PMID 26675548 — **Figure S4**, in `oncotarget-07-4344-s001.pdf`, behind a PMC proof-of-work challenge. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Panel 2C shows K274R expressed **less** than WT, so its failure to rescue is confounded by expression. **Figure S4 is the control that removes the confound** — and it is the only support for the claim that K274 carries signalling function beyond stability, i.e. exactly what decides whether a therapeutic lever is *"more protein"* or *"restore a specific modification"*. **The hole is load-bearing.**
- **EXPECTED_CORRECT_REASONING:** Identify that the decisive control is unread; declare the claim unadjudicated; **do not circumvent the challenge**; record the route as the next action.
- **COMMON_FAILURE_MODE:** Adjudicating on the main figures and inheriting the expression confound.
- **MINIMUM_REQUIRED_EVIDENCE:** Figure S4.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** **YES — decisive and not held**
- **NEGATIVE_CONTROL:** The main-text expression panel 2C *shows* the confound — the paper is not hiding it.
- **EXPECTED_EPISTEMIC_VERDICT:** **`UNRESOLVED — SUPPLEMENT_NOT_HELD`**, with the specific missing object named.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Concluding either way on K274 signalling function.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Omitting that a single named figure would settle it.
- **BENCHMARK_VALUE:** High — tests whether the system can name the exact missing object rather than gesture at incompleteness.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` — gold label is a **declared, addressed gap**

---

#### `HC-I6` — The claim whose source does not exist

- **SCIENTIFIC_QUESTION:** What paper supports `CLAIM 023` (Tyr33 effect)?
- **SOURCE:** `CLAIM 023` → `paper 206`; `CORPUS P206` carries `Identifier: PENDING` and the note *"likely overlaps PAPER 026 (PMID 32185845); verify before merge"*. **PAPER 026 is abstract-only and gives the opposite direction for Tyr33.** ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ The claim is `consolidated baseline` / `DATO`. Its content is faithful to a real paper; **its chain of custody does not exist.** A dedup against the wrong record would import a direction reversal into a baseline claim.
- **EXPECTED_CORRECT_REASONING:** Resolve the identifier before any merge. Note that the claim's *content* is not impeached by its *custody* defect, and that these must be reported separately.
- **COMMON_FAILURE_MODE:** Merging on title similarity, silently adopting the abstract-only opposite direction.
- **MINIMUM_REQUIRED_EVIDENCE:** Resolution of `P206`; full text of PMID 32185845.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** NO · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** ◻ PMID 15070730 was read on 2026-08-14 and its content matches the claim — so the claim is probably right and merely unsourced.
- **EXPECTED_EPISTEMIC_VERDICT:** Content `DATO`; provenance **`UNRESOLVED`**; the reconciliation is a canonical write and belongs to the operator.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Merging `P206` into `PAPER 026`.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Downgrading the claim for a custody defect alone.
- **BENCHMARK_VALUE:** Moderate-high — separates content validity from custody validity.
- **CLASS:** 🟡 `USEFUL_STRESS_CASE`

---

#### `HC-I7` — The pointer that routes to the disconfirming panel

- **SCIENTIFIC_QUESTION:** Which panel supports the statement that lithium suppressed seizures in all three genotypes?
- **SOURCE:** `CLAIM 016` evidence-boundary note says **`Fig. 7b`**; the deep-dive manifest says **7d**, twice. ✅ **RE-DERIVED** (registry text read; caption and panels verified against the local figure)
- **WHY_DIFFICULT:** ✅ Figure 7b is the **ethosuximide** panel, whose controls read `n.s.` — so a verifier following the canonical pointer lands on the panel that **disconfirms the sentence it was sent to check**, and would reasonably conclude the sentence is wrong. The sentence is right; the pointer is wrong.
- **EXPECTED_CORRECT_REASONING:** Verify the pointer against the caption before accepting or rejecting the claim. ✅ Caption: *"b … Pretreatment of ethosuximide (ETS, 150 mg/kg)…"* / *"d Pretreatment of a GSK3β inhibitor LiCl (60 mg/kg)…"*.
- **COMMON_FAILURE_MODE:** Following the pointer, finding `n.s.` controls, and retracting a correct claim — a **fabricated retraction**, which is worse than an uncorrected error because it destroys a true statement.
- **MINIMUM_REQUIRED_EVIDENCE:** Figure 7 caption + panels 7b and 7d.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** ✅ Under the most charitable reading — that `Fig. 7b` was meant to govern the ethosuximide clause of the same sentence — the pointer would be correct for the clause it precedes. That reading must be tested and stated, not assumed away.
- **EXPECTED_EPISTEMIC_VERDICT:** Claim content `DATO`; pointer **defective**; the two reported separately.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Retracting the claim.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Fixing the pointer without recording that it routed a verifier to disconfirming evidence.
- **BENCHMARK_VALUE:** High — the failure mode is a *false retraction*, which this corpus has no other case of.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-I8` — Counting panels with a parser

- **SCIENTIFIC_QUESTION:** How many panels does a figure have?
- **SOURCE:** PMID 34268881 (**69** panels, counter said 17); PMID 26675548 (**16**, census said 10 and **lost panel A in all five figures that "passed"**); PMID 18487609 (**32**, census printed `A,B,C,E` and returned 27 without protesting); PMID 24550385 (**39**; three ad-hoc scripts gave 7, then 9, then 6). ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ Every failure returns **a small, plausible number and no error.** EMBO marks panels as `<list-item>`, not letters; one depositor uses lowercase; one caption writes *"higher magnifications in D showing"* without the punctuation the regex requires.
- **EXPECTED_CORRECT_REASONING:** Derive the panel budget by **reading captions**. Treat any parser output as a lower bound, never as a denominator. **A count that cannot look wrong is not a count.**
- **COMMON_FAILURE_MODE:** Declaring full panel coverage against a denominator that is 25–75% of the truth.
- **MINIMUM_REQUIRED_EVIDENCE:** Captions read by a human/model, not matched by regex.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** ◻ Rejection *does* fire when zero panels are found — so the tool catches the zero and misses the systematic loss. The control distinguishes the two failure modes.
- **EXPECTED_EPISTEMIC_VERDICT:** Coverage claims against parser denominators are **`UNSUPPORTED`**.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** `panels: N/N` on a parser count.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Refusing to state a budget at all.
- **BENCHMARK_VALUE:** High, with **four independent instances** — rare enough to support a real measurement rather than an anecdote.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` (infrastructure)

---

#### `HC-I9` — An `<Id>` in the response is not an `<Id>` to your question

- **SCIENTIFIC_QUESTION:** Is Havali 2021 deposited in PMC?
- **SOURCE:** PMID 34034642 — `elink`, `esummary`, Europe PMC, Unpaywall. ◻ **INHERITED**
- **WHY_DIFFICULT:** ◻ `elink` returned three `<Id>` values. Read **without the `LinkName`**, they say a PMC deposit exists. They are `pubmed_pmc_refs` — articles that *cite* this one. Four routes agree the paper is closed.
- **EXPECTED_CORRECT_REASONING:** Read the `LinkName`, not the payload shape. Record *"not retrievable by these routes"*, **never** *"irrecoverable"* — the institutional, ILL and author-deposit routes stay open.
- **COMMON_FAILURE_MODE:** Concluding a deposit exists; **or** the mirror-image error of recording a retrieval failure as a **property of the artefact**, which is exactly how ◻ two retractions came to rest on a false premise.
- **MINIMUM_REQUIRED_EVIDENCE:** The four route responses, verbatim, with `LinkName` preserved.
- **FULL_TEXT_REQUIRED:** NO · **FIGURE_OR_TABLE_REQUIRED:** NO · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** A paper with a genuine `pubmed_pmc` linkset must be distinguished — otherwise the fix rejects real deposits.
- **EXPECTED_EPISTEMIC_VERDICT:** **`NOT_RETRIEVABLE_BY_THESE_ROUTES`**, routes enumerated.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** "A PMC deposit exists"; or "the paper is irrecoverable".
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Recording "not found" without naming the routes tried.
- **BENCHMARK_VALUE:** High — tests the difference between a property of an object and a property of an attempt.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` (provenance)

---

#### `HC-I10` — A `200` is not a body, and a PMCID is not a surface

- **SCIENTIFIC_QUESTION:** Has the full text been retrieved?
- **SOURCE:** ◻ Three `pdf_only` records with valid PMCIDs return `200` from `efetch` with **8,781 / 7,406 / 7,159 bytes and no `<body>`** — metadata dressed as full text. Same shape as PMID 18487609 and 42395553.
- **WHY_DIFFICULT:** ◻ A pipeline checking only status code, or only non-emptiness, files these as *"full text retrieved"*. 🔴 And the **inverse** error occurred on the same PMID: it was reported that 18487609 *"returns 200 with no `<body>`"*, while the file actually on disk **has** a `<body>`, eight `<figure>` blocks, and full sections. **Whoever measured it measured a different object** — a different fetch, or the interstitial. A measurement on a fetch that is not the file on disk is not a measurement of the surface.
- **EXPECTED_CORRECT_REASONING:** Validate on **structure** (`<body>` present, sections present, plausible length), measured **on the artefact on disk**, not on a live response.
- **COMMON_FAILURE_MODE:** Both directions — accepting metadata as full text, and rejecting a good local surface on a stale or misaimed probe.
- **MINIMUM_REQUIRED_EVIDENCE:** The file on disk, its digest, and a structural assertion.
- **FULL_TEXT_REQUIRED:** NO · **FIGURE_OR_TABLE_REQUIRED:** NO · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** PMID 18487609 itself is the control: it passes the structural test, so a screen that rejects it is over-strict.
- **EXPECTED_EPISTEMIC_VERDICT:** Surface class is a **measured property of a named file**, never of a route.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** `structured` on a `200`.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** `pdf_only` on a paper whose clean XML is already on disk — ◻ and this exact stale record kept PMID 15070730 closed for two years of corpus, because **a surface declared `SUSPECT` is a surface nobody opens.**
- **BENCHMARK_VALUE:** High, bidirectional, with a documented two-year cost.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK` (provenance)

---

### AXIS J — Evidence-transfer overreach

---

#### `HC-J1` — The paper about the wrong domain

- **SCIENTIFIC_QUESTION:** Does PMID 25703206 provide a rationale for an SDR-domain stabiliser?
- **SOURCE:** PMID 25703206. ◻ **INHERITED** (`DIS-005`)
- **WHY_DIFFICULT:** ◻ Title and abstract promise *"allostery + conformational switch in WWOX"*. The paper concerns **residues 1–91 entirely** — the WW1–WW2 modules. **The SDR is not even in the constructs.** The relevance prediction was made from the abstract and treated as background rather than as a premise.
- **EXPECTED_CORRECT_REASONING:** Treat a relevance prediction as a **premise requiring verification against the text**. The right rejection comes *after* reading, never in its place.
- **COMMON_FAILURE_MODE:** Triaging by title/abstract and importing a rationale from the wrong structural domain.
- **MINIMUM_REQUIRED_EVIDENCE:** The Methods construct definitions.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** NO · **SUPPLEMENT_REQUIRED:** NO
- **NEGATIVE_CONTROL:** ◻ The paper still yielded something better than what was sought — the `D-04` design constraint (**stability is bought with occlusion, and occlusion is anti-function**; P282A is stable and completely inert). A system that files it as irrelevant loses that.
- **EXPECTED_EPISTEMIC_VERDICT:** Rejected for the SDR question; **retained** for the design constraint.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Citing it for SDR allostery.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Discarding it as irrelevant.
- **BENCHMARK_VALUE:** High — tests whether a wrong-domain rejection still harvests what the paper does contain.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-J2` — Is a WWOX-mimetic safer than lithium?

- **SCIENTIFIC_QUESTION:** Is WWOX's inhibition of GSK3β substrate-selective, and would a mimetic therefore be safer?
- **SOURCE:** PMID 22193544 — main Fig 1b/1c vs **Supplementary Figure C**. ◻ **INHERITED** (`DIS-009`)
- **WHY_DIFFICULT:** ◻ The main figures are genuinely attractive: WWOX lowers pTau S396/S404 **without touching** β-catenin or phospho-β-catenin — which reads as targeted where lithium is global. **Supplementary Figure C refutes it**: WWOX inhibits GSK3β-dependent phosphorylation of **GS-1**, a glycogen-synthase-derived peptide unrelated to Tau, to ~18% of control (L404A ~87%). The interaction is a **generic docking-site block** (Axin/FRAT/GSKIP), not substrate selectivity. The cellular β-catenin sparing is more parsimoniously explained by **pool segregation** or sub-saturating endogenous stoichiometry — **never measured** in the work.
- **EXPECTED_CORRECT_REASONING:** Read the supplement before converting a cellular observation into a biochemical property. Reject the **safety argument** while preserving the **mechanistic strengthening** (a physical brake is lost, not merely a level).
- **COMMON_FAILURE_MODE:** Generalising cellular selectivity to interaction selectivity — and doing it in a **safety** argument, where the error is most costly.
- **MINIMUM_REQUIRED_EVIDENCE:** Supplementary Figure C with its quantification.
- **FULL_TEXT_REQUIRED:** YES · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** **YES — decisive**
- **NEGATIVE_CONTROL:** L404A at ~87% is the built-in specificity control: the effect is real and motif-dependent, so the case is about *scope*, not artefact.
- **EXPECTED_EPISTEMIC_VERDICT:** Substrate selectivity **refuted**. A pool-selective molecule remains **possible and untested**. ◻ And a distinct claim — **isoform** selectivity via Axin-site occupancy (GSK-3β2) — opened separately and legitimately when a revival trigger fired.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** "A WWOX-mimetic is a safer lithium."
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Concluding the mechanism is worthless — the rationale strengthens even as the safety argument dies.
- **BENCHMARK_VALUE:** **Top-tier.** Supplement-decisive, safety-relevant, and it requires distinguishing *which claim died* from *which is merely different*.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

#### `HC-J3` — Elevated, or de-repressed?

- **SCIENTIFIC_QUESTION:** Is GSK3β *more abundant* or *dis-inhibited* in WWOX deficiency?
- **SOURCE:** `CLAIM 016` Summary (*"GSK3β is elevated"*) vs `CLAIM 035` (direct physical inhibition via the Axin-like motif 388–407/L404, **S9-independent**). ✅ registry re-read
- **WHY_DIFFICULT:** *"Elevated"* reads as abundance. The mechanism is **loss of a physical brake**. ✅ `CLAIM 016` itself carries the `PREMISE_TAG` that *abundance reports activity* is `DEFAULT_FROM_TEXTBOOK` and false here — abundance and activity are dissociable in this system. 🔴 And `locator_contract_live_test.md`, tracked since 2026-08-04, **already stated the correction and drafted the remedy** — *"'Elevated' is the wrong word … GSK3β is dis-inhibited, not more abundant"*. ◻ Two Scientists later re-derived it independently and each recorded it as a discovery. **The system found this, solved it, and lost it.**
- **EXPECTED_CORRECT_REASONING:** Separate abundance from activity; state the measurement consequence — a **phospho-S9 western produces a false negative** for this mechanism.
- **COMMON_FAILURE_MODE:** Designing or accepting a pS9-based activity readout; and, at the system level, re-deriving a fix that already exists in an untracked-by-nobody file.
- **MINIMUM_REQUIRED_EVIDENCE:** PMID 22193544 residue-level assays + PMID 32000863 abundance panels.
- **FULL_TEXT_REQUIRED:** YES (×2) · **FIGURE_OR_TABLE_REQUIRED:** YES · **SUPPLEMENT_REQUIRED:** YES (see `HC-J2`)
- **NEGATIVE_CONTROL:** The abundance datum is real. The correction is about the *word*, not the *observation*.
- **EXPECTED_EPISTEMIC_VERDICT:** `DATO`: de-repression. *"Elevated"* is imprecise, not false.
- **WHAT_WOULD_COUNT_AS_OVERCLAIM:** Predicting a total-GSK3β increase.
- **WHAT_WOULD_COUNT_AS_UNDERCLAIM:** Keeping "elevated" as though the distinction were cosmetic — it determines which assay is valid.
- **BENCHMARK_VALUE:** High as science; **higher as a retention benchmark** — it is the corpus's cleanest instance of a solved problem being lost.
- **CLASS:** 🟢 `HIGH_VALUE_BENCHMARK`

---

### Cases recorded and NOT recommended as gold standards

---

#### `HC-X1` — Johannsen 2018: load-bearing and unobtainable

- **SOURCE:** PMID 29808465. ◻ **INHERITED**
- **THE PROBLEM:** ◻ The paper **holds 47 citations across 7 canonical files** and is closed on every route tried (Europe PMC `pmcid: null`, NCBI idconv *"not found in PMC"*, Unpaywall `is_oa: false`, absent locally). **The datum entered from the abstract, which is where it lives** — so the 47 citations are nobody's inattention: the paper was never available to those citing it.
- **WHY NOT A GOLD STANDARD:** The deciding surface cannot be obtained. Any graded answer would be scored against an abstract, not the evidence.
- 🔴 **What is nonetheless valuable, and it cuts in the system's favour:** ◻ the canonical state handled this **better** than the alarm raised about it. `disease_model.md` records a MAJOR reversal `WM v2.1 → v3.0` retracting the equation *normal mRNA + absent protein = degradation*; the cause is carried as **not discriminated**; and it is annotated that western-blot absence is *"a sensitivity limit, not an absolute zero"* and that *"a fibroblast is not a neuron"*. The underdetermination (impaired translation **or** premature degradation **or** insolubility) is correctly preserved.
- **EXPECTED_EPISTEMIC_VERDICT:** **`UNVERIFIABLE_SURFACE`.** Usable only as a *declare-the-limit* case: the correct output is an explicit statement that the claim rests on an abstract and that the mechanism is undiscriminated.
- **CLASS:** 🔴 `TOO_DEPENDENT_ON_UNRESOLVABLE_SURFACE` — valuable as a **limit-declaration** probe, never as a science gold standard

---

#### `HC-X2` — The Europe PMC / efetch body-size disagreement

- **SOURCE:** ◻ PMID 30356099: Europe PMC body **45,559** chars vs efetch **35,239**. PMID 31543760: **56,746** vs **40,700**. PMID 39952983: **40,456** vs **26,299** — and here efetch returns *more total bytes* (137,703 vs 116,460) with *less body*. Figures are inside the body in **both** routes in all three cases, so **it is not the captions.**
- **WHY NOT A GOLD STANDARD:** ◻ **What those ~10,000 characters are has never been adjudicated.** Three of five structured surfaces show the same gap, so it is a property of the two routes, not of an article — but until someone diffs them, there is no ground truth to score against.
- **EXPECTED_EPISTEMIC_VERDICT:** **`UNRESOLVED — OPEN QUESTION`.** Europe PMC is declared for being the larger surface; that is a policy, not a finding.
- **BENCHMARK_VALUE:** High **as a research task**, zero as a gold standard today. **Diffing one pair once would convert this into a benchmark and settle a corpus-wide question.**
- **CLASS:** 🔴 `TOO_AMBIGUOUS` *(today)* — high-value **next measurement**

---

#### `HC-X3` — The distance that was a covalent bond

- **SOURCE:** ◻ `DIS-007` / `D-12`. C299R was called *"3.4 Å from the catalytic triad"* → a catalytic lesion and *"the cheapest and most discriminating test we have"*. The measurement was **minimum atom–atom distance of any kind**, which for sequence-adjacent residues returns backbone — or, at 1.3 Å, a **covalent bond**. True side-chain distance: **9.4 Å**. Collaterally, *"P282A at 1.3 Å"* → **4.9 Å**. And a correction **against** the author: the lid helix is not 6.8 Å from the triad but **3.5 Å**, making the `D-04` design constraint **stricter**.
- **WHY NOT A LITERATURE GOLD STANDARD:** It is a computational-measurement artefact, not a reading task. It belongs to a different benchmark family.
- **WHY IT MATTERS ANYWAY:** An entire two-route model was built on it, and it was found by a **parallel session**, not by its author. It is the corpus's best evidence that independent re-measurement catches what review does not.
- **EXPECTED_EPISTEMIC_VERDICT:** Withdrawn on measurement error; the human `DATO` under it survives.
- **CLASS:** 🟡 `USEFUL_STRESS_CASE` — for a **computational-method** benchmark, not a reading one

---

#### `HC-X4` — Low-value: the published placeholder

- **SOURCE:** ◻ PMID 34634460, panel showing `ch?` — an unresolved placeholder in the published figure.
- **WHY LOW VALUE:** Real, but it tests nothing beyond "look at the panel", which `HC-B4` and `HC-C2` already test on the same paper with actual scientific stakes.
- **CLASS:** ⚪ `LOW_VALUE`

---

#### `HC-X5` — Low-value: the motif tree that does not sum

- **SOURCE:** ◻ PMID 24550385 — motif-tree leaves sum to **563** and **355** over declared sets of **240** and **144**.
- **WHY LOW VALUE:** An arithmetic inconsistency with no downstream claim resting on it. Worth recording; not worth benchmarking.
- **CLASS:** ⚪ `LOW_VALUE`

---

## 3 · Closing analysis

### TOP_10_BENCHMARK_CANDIDATES

Ranked by *(ground-truth solidity) × (failure realism) × (cost of the failure)*.

| # | Case | Why it ranks here |
|---|---|---|
| **1** | `HC-B1` — Wang 2012 Supplementary Figure A | The only case where text and caption **agree with each other and both are wrong**. Prose-vs-prose checking cannot catch it; only the raster can. Gold label is `UNRESOLVABLE`, which tests the rarest capability of all: refusing to grade. |
| **2** | `HC-F1` — ITCH direction, substrate and chain | Three papers; substrate, stabiliser and direction all invertible; two papers that *look* contradictory and are not; and a therapeutic non-selectivity conclusion present in neither alone. |
| **3** | `HC-D1` — *Wwox*-null epileptogenesis | Two-hop citation chain, unverified at both hops, propagated to **five canonical surfaces for months**, and decided by an **empty table cell**. |
| **4** | `HC-A1` — lithium genotype scope | Both directions are overclaims; the correct answer is a declared limit. ✅ Locally verifiable end-to-end. |
| **5** | `HC-F2` — the intermediate genotype class | The framework's **own source denies a third of it**, in one quotable sentence. Sits under this repository's hypomorph and ASO reasoning. |
| **6** | `HC-G1` — Runx2 sign flip | Same knockout, same paper, **opposite signs** by preparation, with the Discussion contradicting its own figure twice in 400 words. |
| **7** | `HC-E2` — the ATR never measured | Title asserts a kinase for which no antibody, no inhibitor and no knockdown exists — and the paper's own schematic marks the asserted arrow with `?`. |
| **8** | `HC-J2` — the WWOX-mimetic safety argument | Supplement-decisive refutation of a **safety** claim; requires distinguishing the claim that died from the one that is merely different. |
| **9** | `HC-I1` — the fabricated space | The measurement apparatus is itself the defect, the naive fix breaks a different guarantee, and it silently degrades locator verification corpus-wide. |
| **10** | `HC-B5` — the Gemini figure | Tests the **boundary condition of the figure-priority rule** on a class of artefact that is proliferating; the discriminant is free and printed in the caption. |

### TOP_FAILURE_MODES

Ordered by frequency across the ~35 cases, with the count of cases exhibiting each.

| # | Failure mode | Cases | The shape of it |
|---|---|---|---|
| **1** | **Caption/summary authority over the panel** | `B1 B2 B4 B5 B6 C1 D2 D4 G1 A3 A4` (11) | A caption, an abstract or a Discussion sentence is authored prose; a panel is data. When they disagree the prose usually wins in extraction, because prose is what extractors index. |
| **2** | **Provenance accepted without resolution** | `D1 F4 I6 I9 I10 X1` (6) | A citation, a `<Id>`, a `200`, a `PENDING` identifier or a bracketed pair is treated as an attribution. **A reference in the response is not a reference to the question you asked.** |
| **3** | **Untested null read as a tested negative** | `D2 D3 C1 B4` (4) | *"Not significant"*, *"no major defects"*, *"did not result in changes"* — with no test named, no challenge applied, or no statistics section anywhere. The resulting false negative is silent, permanent and self-reinforcing. |
| **4** | **Tool output as ground truth** | `I1 I3 I8 I10 X3` (5) | Panel counters, extractors, distance metrics and status codes return **small plausible numbers with no error**. A count that cannot look wrong is not a count. |
| **5** | **Scope silently narrowed or widened** | `A1 A3 F2 E3 G4 J1` (6) | Text restricts what the figure leaves broad (`A1`); a review narrows what its source left open (`F2`); *"restored"* survives because the falsifying bracket was never drawn (`E3`). |
| **6** | **Association read as causation** | `E1 E2 B6 E3` (4) | Two arms in one figure, never joined; a proxy readout standing for an unmeasured entity; a solid line in a schematic. |
| **7** | **Abundance/level substituted for function** | `G2 J3 X1` (3) | The tacit premise under most western-blot reasoning here — and false in **both** directions in this system. |
| **8** | **Surface class asserted, not measured** | `I2 I3 I10` (3) | `SUSPECT` and `structured` recorded as properties of a route rather than of a named file with a digest. A stale `SUSPECT` kept one paper closed for two years of corpus. |
| **9** | **Convention imported as datum** | `A2 C2 C3` (3) | `****`, asterisk ladders, 14-digit P-values — software output read as the paper's measurement. |
| **10** | **A solved problem lost** | `J3` and, structurally, `X1` (2) | The repository states the fix, drafts the remedy, does not apply it, and later actors re-derive it and record it as discovery. **A conclusion never written has no address, so no measurement is ever pointed at it.** |

### CASES_REQUIRING_VISUAL_PDF_ADJUDICATION

Cases where a text layer **cannot** decide, and the page or panel image must be rendered.

| Case | What only the image shows |
|---|---|
| `HC-B1` | That no anti-Tau blot exists — text and caption both claim it does |
| `HC-B2` | Three bars, two labels; the literal legend inverts the phenotype |
| `HC-B3` | The missing minus on the axis that defines the sign of the lag |
| `HC-B4` | `p = 0.0312` printed on a panel whose caption says *"No significance"* |
| `HC-A2` | `****` printed in the panel and absent from all prose |
| `HC-A1` | Per-genotype brackets and N in Figure 7d |
| `HC-D2` | Error bars inside the bar stroke, with no test named |
| `HC-D4` | The ubiquitination ladder the text denies |
| `HC-E2` | The `?` on the schematic's WWOX→CHK1 arrow |
| `HC-I2` | The only route to content: page adjudication, the text layer being refused |
| `HC-D1` | The **empty `Epilepsy` row** in Table 2 — routinely lost in text extraction |
| `HC-I3` | That six captions exist at all, outside the `<body>` |

🔴 **Two resolution lessons that belong with this list, both from within the corpus.** ◻ At 101 ppi a reader attributed to CBX a frequency change that is the **opposite** of the result, and the crop corrected it. ◻ At full-figure scale another reader saw a smear in Fig 5G that **is not there**, and the crop corrected it in the opposite direction. **Resolution is part of the observation**, and both directions of error occur. Additionally: on one paper the **local PDF was the better figure surface by a factor of 2** (173–203 ppi vs 84–102 from the CDN) — *"a structured surface was found"* does not imply *"the best figure surface was found"*.

### CASES_REQUIRING_MULTI_PAPER_REASONING

| Case | Papers | What only the combination decides |
|---|---|---|
| `HC-F1` | 23370280 + 24550385 + 26675548 | That the two mechanisms are **compatible**, and that an ITCH lever is therefore not WWOX-selective |
| `HC-D1` | 30290271 → 19936220 → 19500159 | That the chain terminates in **contrary** evidence, not absent evidence |
| `HC-F2` | 36779245 + 42128308 | That a review's framework is denied by its own source |
| `HC-F4` | PMC3139124 + Mukai 2002 + Saeki 2011 | Which clause of a compound statement belongs to which reference |
| `HC-E3` + `HC-H1` | 42128308 + 42397075 (+ preprint) | Whether *"restored"* is a misreading, a version difference, or both |
| `HC-G2` | P47T + SCAR12 primaries + 22193544 | That abundance and function dissociate in **both** directions |
| `HC-G4` | 34634460 + 18487609 | That a heterozygote phenotype is level-dependent — one paper handles it correctly, one does not |
| `HC-D4` | 26675548 + 24550385 | *Predominant* versus *exclusive* site usage |
| `HC-J3` | 32000863 + 22193544 | That *"elevated"* should read *"de-repressed"*, and that pS9 is therefore an invalid assay |

### CASES_REQUIRING_NEGATIVE_EVIDENCE_HANDLING

Ordered by how badly a naive reading damages the model.

| Case | The negative | Correct handling |
|---|---|---|
| `HC-B1` | *"WWOX does not bind Tau"* | **Not evaluable.** The evidence does not exist in the record. Registering `conflicting evidence` here fabricates the worst class of false negative. |
| `HC-D1` | *"Wwox-null mice show epileptogenesis"* | Rejected on **contrary** evidence — but *no reported epilepsy* is a statement about the literature, not proof of absence. |
| `HC-D2` | *"Osteoclast activity is not impaired"* | The null was never computed; the direction is concordant across two systems. |
| `HC-D3` | *"No major defects"* (Olig2 KO) | An **unchallenged readout in a compensable system** is uninformative, not negative. Support is `IPOTESI`. |
| `HC-B4` | Caption *"No significance"* | Contradicted by the panel's own printed `p`. |
| `HC-C1` | Four uses of *"significantly"* | No test exists anywhere in the paper. |
| `HC-J2` | *"β-catenin untouched ⇒ selective"* | A negative in one cellular readout is not a biochemical property; the supplement refutes it. |
| `HC-A1` | Text silent on control genotypes | Silence is not a reported negative — but neither is the panel a tested interaction. |
| `HC-I2` | Symbol absence across 44k characters | Absence **as a positive signal** of surface corruption. Its own negative control was run and reported. |
| `HC-I4` | Zero `P<0.05` matches | A **false** absence signal — the regex was incomplete, the paper used `≤`. |

🔴 **The asymmetry that orders this whole list**, stated by the ledger itself: a false positive gets tested and dies; **a false negative is never retested.** It makes no noise, it is permanent, and it is self-reinforcing. Six of the ten above would, if mishandled, close a door silently.

### CASES_UNSUITABLE_FOR_GOLD_STANDARD

Declared explicitly, because turning any of these into a graded answer would build a false standard.

| Case | Class | Why, precisely |
|---|---|---|
| `HC-X1` Johannsen 2018 | `TOO_DEPENDENT_ON_UNRESOLVABLE_SURFACE` | Closed on all four routes; 47 citations rest on an abstract. **Usable only as a limit-declaration probe.** |
| `HC-X2` EPMC/efetch gap | `TOO_AMBIGUOUS` | ~10,000 characters of difference, three times over, **never adjudicated**. No ground truth exists yet. |
| `HC-I2` (text-locator axis) | `TOO_DEPENDENT_ON_UNRESOLVABLE_SURFACE` | 92% printable corruption; the text layer is refused, not repaired. The **surface-screening** axis of the same case is `HIGH`. |
| `HC-H1` **version-comparison axis only** | `TOO_AMBIGUOUS` **today** | The preprint is not held, so no version *difference* can be graded. Its other axis — resolving an expired preprint DOI to its published record — is decidable now and stays `USEFUL_STRESS_CASE`. **The two axes must not be scored together.** |
| `HC-I5` Figure S4 | usable **only** with `UNRESOLVED` as the gold label | The decisive control is behind a challenge and was **not circumvented**. |
| `HC-D3` Olig2 challenge | weak substrate | Its only source is not peer-reviewed. **This is my own prior overstatement, corrected here.** |
| `HC-X3` distance artefact | wrong family | Computational measurement, not a reading task. |
| `HC-X4`, `HC-X5` | `LOW_VALUE` | True, but subsumed by stronger cases on the same papers. |

🔴 **And one boundary that applies across the set:** `HC-F3` (vigabatrin) is a legitimate benchmark **only** under the no-medical-advice constraint. Its correct answer is a sustained conflict on two non-exclusive axes; any harness that rewards a resolution will train exactly the error the case exists to catch.

### RECOMMENDED_NEXT_BLIND_REPLICATION_CASES

Selected so that (a) the deciding surface is held or cheaply obtainable, (b) the answer is checkable against an artefact rather than against a peer, and (c) each exercises a **different** failure mode. Ordered by readiness.

| # | Case | Surface status | Blinding protocol | What it would establish |
|---|---|---|---|---|
| **1** | `HC-A1` + `HC-A2` — Cheng 2020 Figure 7d | ✅ **Held in this worktree**: XML, 7 figure PNGs, 20.6 MB supplement | Give the reader the **figure only**, then the **text only**, in separate sessions; compare. Withhold `CLAIM 016` and both manifests — ◻ `deepdive_manifests/PMID32000863.json` contains a **complete prior adjudication** of exactly these questions, and `locator_contract_live_test.md` states the Fig 7d result in prose. **Both must be withheld or the run is contaminated.** | Whether text-first and figure-first readings converge, and whether either reports the untested interaction |
| **2** | `HC-B1` — Wang 2012 Supplementary Figure A | ◻ Supplementary image needed | Supply text + caption + image; ask *"is the negative established?"*. **Do not** hint that a discrepancy exists | Whether the reader inspects the raster at all — the single highest-leverage habit in the corpus |
| **3** | `HC-F2` — the intermediate class | ◻ PMID 36779245 XML on disk (183,753 bytes) | Give the **review's** framing first, then the primary. Ask whether class 2 is supported | Whether a review's framework is checked against its own source |
| **4** | `HC-G1` — Runx2 sign | ◻ `PMID18487609_Aqeilan2008_PMC.html` + PDF on disk, surface verified clean | Ask a single question: *"what is the sign of the RUNX2 change?"* | Whether a single-sign summary sentence overrides two panels |
| **5** | `HC-I1` — the fabricated space | ◻ XML on disk | Hand the reader 20 locators and the raw XML; ask why 13 fail | Whether the reader diagnoses the **normaliser** rather than the readings — and resists the over-aggressive fix |
| **6** | `HC-E2` — the unmeasured ATR | ◻ XML + PDF on disk, preflight complete | Ask *"does this paper support its title?"* | Whether claimed entities are inventoried against measured entities |
| **7** | `HC-D1` — the epileptogenesis chain | ◻ Terminal source needs Table 2 **rendered** | Give the citing sentence only; ask for the primary evidence | Whether a two-hop chain is walked to its terminus, and whether an empty table cell is read |
| **8** | `HC-B5` — the Gemini figure | ◻ PDF + fitz text on disk | Give text and figure with **caption intact**; ask which is authoritative | Whether the figure-priority rule's boundary is known, and whether the free discriminant is used |

🔴 **The contamination hazard that governs every entry above, and it is structural rather than incidental.** ◻ It has already been recorded that `deepdive_manifests/PMID32000863.json` had to be opened for artefact paths and fingerprints — a read the protocol **mandates** — and that the same file also contains a complete prior adjudication of the assigned questions. **Provenance and conclusions are co-located.** Any blind replication on a previously-read paper must be handed *fingerprints and paths only*, extracted by a third party, or the independence is spent before the reading starts. ◻ On the one prior attempt, measured against all 581 tracked files, **five of nine first-pass findings pre-existed in the repository** — and three actors independently "found" what the repository had already written down.

---

## 4 · What this document does not claim

- **It proposes no schema, no field, no rule and no governance change.** Where a case names something the current grammar cannot hold — a cross-paper `contradicts` pointer, a version-of-record field, a `figure_kind: schematic|data` distinction — that is a **description of the fact**, not a proposed slot.
- **It applies no verdict token to any canonical claim.** Every `EXPECTED_EPISTEMIC_VERDICT` above is the answer a *benchmark* should score against, not an adjudication of the registry.
- **It does not re-verify the ◻ set.** Roughly four fifths of the factual content is inherited from repository artefacts and marked as such. **A benchmark built from this document must re-derive each ◻ fact from the primary before scoring anything against it** — otherwise it inherits the errors of the readings it was built to test, which is precisely the failure `HC-J3` records.
- **Nothing here is medical advice.**
