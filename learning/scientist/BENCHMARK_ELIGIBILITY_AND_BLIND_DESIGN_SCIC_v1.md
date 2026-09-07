---
artifact: LEGEND scientific evaluation — BENCHMARK ELIGIBILITY, CONTAMINATION AND BLIND DESIGN
id: BENCHMARK_ELIGIBILITY_AND_BLIND_DESIGN_SCIC_v1
class: evaluation-preparation input for a controlled benchmark, in the vocabulary of
  `framework/protocols/controlled_benchmark_ab.md` (CONTROLLED_BENCHMARK_AB) and of
  `framework/eval/benchmarks/BENCH-AB-001/` (`surface_spec.json` · `benchmark_manifest.json` ·
  `instructions/ASSIGNMENT.*.md` · `population/evidence_units.json`). It proposes an input set.
  It is NOT a benchmark manifest and authorizes no run.
continues: HARD_CASE_MINING_BENCHMARK_CANDIDATES_SCIC_v1 (48 cases)
actor: scientist-c (NOT ACTIVATED — operator-directed analytical pilot)
worktree: lettore-c · branch lettore-c · HEAD 5b1d6c2
date: 2026-08-26
scope: EVALUATION DESIGN. No governance, role-contract or architecture change is performed or
  proposed. No schema, field or rule is proposed.
status: NON-CANONICAL. Mutates nothing. No canonical file, manifest, receipt or ledger is edited.
canonical_mutation: NONE
---

# Which of the 48 hard cases can carry a gold standard, and which of those can be run blind

> **Nothing here is medical advice.** This document evaluates reasoning surfaces, not therapy.

---

## 0 · What I measured this session, before classifying anything

The prior artifact carries roughly four fifths of its factual content as ◻ **INHERITED** and says so.
A classification built on top of that inheritance would rank cases by how confidently they were
written down, not by how well they hold. So the first act of this session was measurement, and the
markers carry through:

- ✅ **RE-DERIVED** — measured this session from the primary artifact, command reproducible.
- ◻ **INHERITED** — from a repository artifact, not re-verified here.

### 0.1 · Primary re-derivations, with digests

| # | What | Result | Artifact |
|---|---|---|---|
| 1 | Wang 2012 **Supplementary Figure A** image | Two panels, labelled **WWOX** and **GSK3β**. **No anti-Tau blot exists.** Lanes: INPUT · IP:IgG · IP:HA | `cdd2011188x1.tif` 630×565, `sha256 4e4fc936ddad189f…`, from `PMID22193544_Wang2012_supplement.zip` `sha256 af2faa04f85d5219…` |
| 2 | Densitometry of that figure | **WWOX panel:** band row 211; INPUT 59.8, IgG 204.2, HA 42.6 → clean co-IP positive, INPUT and HA dark at the **same** row. **GSK3β panel:** INPUT band centred y≈384 (min 124.8 vs 172–177 baseline); IgG flat; **HA lane has no minimum at row 384** — it darkens monotonically to 113 at y≈432, the panel's bottom edge, ~48 rows below the INPUT band | same file, PIL/numpy row-and-column profiles |
| 3 | Wang 2012 **published supplementary legend** | *"Supplementary Figure A. **WWOX does not associate with Tau.** … Immunoprecipitated WWOX was recognised by antibodies against HA. **Anti-Tau was used to detect endogenous Tau protein.**"* | `cdd2011188x4.doc`, printable-run extraction |
| 4 | Wang 2012 **Results / Discussion** | *"…although WWOX–HA can be immunoprecipitated with anti-HA antibodies, **Tau was not co-immunoprecipitated** in the complex (Supplementary Figure A), indicating that WWOX does not stably interact with Tau in SH-SY5Y cells."* · *"…we were not able to detect a Tau–WWOX complex … the inconsistency in results may due to the different expression systems used."* · `anti-Tau` occurs **0** times in the body | `PMID22193544_Wang2012_PMC_JATS.xml` `sha256 eb6f568d046f8df8…`, 49,976 extracted chars |
| 5 | Wang 2012 **Supplementary Figure C** | GS-1 phosphorylation (% total): `−` ≈100 · `GST` ≈93 · **`GST-WWOX wt` ≈19** · `GST-WWOX L404A` ≈87. Condition row reads `GSK3β/Tau +` for all four bars | `cdd2011188x3.tif` 630×531, `sha256 25b2823dfc15dfcd…` |
| 6 | Suzuki 2009 **Table 2**, rendered | Three columns (`*Wwox−/−` mice · `†Wwox^gt/gt` mice · `lde/lde` rats). **`Epilepsy` row: blank · blank · "Wild running and tonic−clonic convulsion"**. `Vacuolization` row identically shaped. Footnote: *"\*Data from Aqeilan et al. 2007, 2008, and 2009"* | `PMID19500159_Suzuki2009.pdf` `sha256 e1a0a87dc7faac00…`, page 9, PyMuPDF 1.26.5, `Matrix(400/72)`, clip from the `Table 2:` anchor rect; render `sha256 73f4b280f8d91bee…` |
| 7 | The same table, **as text** | `page.get_text()` yields `Epilepsy\nWild running and tonic–clonic convulsion` — **one value, no column marker.** The two empty mouse cells vanish without trace | same PDF, PyMuPDF default mode |
| 8 | Oliver 2023 decisive sentences | *"…classified into three genotypic classes: (1) null/null, (2) null/missense, (3) missense/missense"* (Methods) · *"**We found no difference between individuals with one or two missense variants and therefore no evidence to support an 'intermediate' phenotype**"* (Discussion) · *"all 75 cases … null/null (n = 45), null/missense (n = 15), missense/missense (n = 15)"* · death p = **.0085** log-rank, 5-y <50% vs >75%, 10-y 25% vs >60% · seizure onset p = **.65** log-rank | `PMID36779245_Oliver2023_PMC.xml` `sha256 3aff9ecb9e62b4a9…`, 60,639 extracted chars |
| 9 | The `WWOX ‐DEE` fabricated space | **Does not reproduce.** Current extractor yields `WWOX‐DEE` ×**35** and `WWOX ‐DEE` ×**0** on the same file | `deepdive_manifest._artifact_text`, `XML_INLINE_TAGS` (24 tags) present |
| 10 | Caption-in-body census, whole corpus | 41 XML parsed: **29** all-in-body · **2** some-outside · **7** all-outside · 3 no figures · 1 with no `<body>`. Salah 2013 **0/6**; **Wang 2012 also 0/6** | `framework/scripts/caption_census.py <REPO_ROOT>`, run 2026-08-26 |
| 11 | Provenance/adjudication co-location | 64 manifests · **60** carry both `source_artifacts` and `verbatim_locators.entries` in one file · of those, **38** carry adjudicative language in the propositions | `disease-models/wwox/research/deepdive_manifests/*.json`, regex named in §4.2 |
| 12 | Figure-artifact provenance | **333** figure artifacts declared across **58** papers. The receipt ledger carries **3** of those digests, all for one paper (PMID 42397075). **57 of 58 papers have zero figure provenance outside an adjudicating file** | ledger + manifests, digest membership test |
| 13 | Discipline-file leakage | See §4.3 — measured over a fixed 12-file mandatory set with a positive control | `grep -l` over an explicit array, 21 PMIDs + 35 content patterns |

### 0.2 · Corrections these measurements force on the prior artifact

Three of them change a case's eligibility, so they are stated before the tables and not buried.

1. 🔴 **`HC-B1`'s negative control is falsified.** The prior artifact states *"The GSK3β co-IP in the
   same supplementary panel is genuine and **positive**"* and, elsewhere, that the lower panel
   *"shows a faint positive band in the HA-IP lane"*. Measured (§0.1 #2): the HA lane carries **no
   density minimum at the INPUT band's migration row**. Its darkest point is at the panel's bottom
   edge, ~48 rows below. The WWOX panel above it is the internal positive control for the method —
   there INPUT and HA are dark at the *same* row. **The case cannot be scored until its negative
   control is rewritten**, because a grader would mark a correct reader wrong.
2. 🔴 **`HC-J2`'s attractive claim is misattributed.** The prior artifact says the main figures show
   *"WWOX lowers pTau S396/S404 **without touching β-catenin or phospho-β-catenin**"*. The paper
   measures β-catenin sparing under **retinoic acid treatment**, not under WWOX: *"we also examined
   whether the phosphorylation level of GSK3β and its downstream target, β-catenin, are affected by
   **RA treatment**. We found that the phosphorylation levels of phospho-GSK3β S9 and
   phospho-β-catenin remained normal."* The paper's own specificity control for WWOX is **Tau
   S422** — *"which is phosphorylated by MKK4 kinase in vivo"*, i.e. **not a GSK3β site at all**.
   The case survives and gets sharper: Supplementary Figure C is the *first* within-GSK3β
   selectivity test in the paper, and it comes out negative for selectivity.
3. 🔴 **`HC-I1` no longer reproduces.** The fabricated space was repaired on 2026-08-10; the fix
   (`XML_INLINE_TAGS`) and the full diagnosis both sit in `deepdive_manifest.py`, which every
   participant must run. Measured: 35 correct tokens, 0 fabricated. The case is **EXCLUDE** for a
   live run and cannot be revived without pinning a pre-fix revision of the tool.

### 0.3 · The novelty check, run before claiming anything

Two findings below are **re-derivations, not discoveries**, and the prior run's §0.3 exists because
this corpus loses its own conclusions. `provenance-and-conclusions-must-not-share-a-file` is already
recorded; §4 does not announce it, it **measures** it and gives it a denominator. The `HC-B1`
text-and-caption-agree finding is already in `fulltext_read_receipt.md`; §4.3 does not re-find it,
it observes that its being written **there** is what disqualifies the case.

What is new here, as far as `git grep` at `5b1d6c2` shows: the 289/333 figure-provenance count, the
`fulltext_read_receipt.md` / `deepdive_manifest.py` leak into the participant surface, the falsified
`HC-B1` control, the `HC-J2` misattribution, and the `HC-I1` non-reproduction.

---

## 1 · The rubric — observable criteria, applied uniformly

**A case is not GOLD_ELIGIBLE because the repository has adjudicated it.** The repository's
adjudication is exactly the thing under test. Four conditions, all four required:

| # | Condition | How it is checked |
|---|---|---|
| **E-1** | **Surface reachable.** The deciding artifact is held locally, or obtainable by a named route that does not require circumventing an access control | listing + digest, or a named acquisition route |
| **E-2** | **Answer determinate.** Exactly one final epistemic verdict is defensible on that surface — where *"the record does not decide"* counts as a verdict about the record | the verdict is stated as a proposition that could be false |
| **E-3** | **Independently recoverable.** A reader with the surface and no LEGEND output reaches the verdict | the derivation cites only the primary |
| **E-4** | **Failure realistic and costly.** At least one wrong answer is one a competent careful reader commits, and it propagates rather than dying | a named failure mode, and where it would land |

**Primary statuses.** Exactly one per case.

| Status | Test |
|---|---|
| `GOLD_ELIGIBLE` | E-1…E-4 hold and the gold is a **positive determinate proposition** |
| `GOLD_WITH_MULTIPLE_ACCEPTABLE_OUTCOMES` | E-1, E-3, E-4 hold; **E-2 fails in a bounded way** — more than one final verdict is defensible on the same evidence, and the acceptable set can be enumerated |
| `STRESS_ONLY` | exercises a real capability, but the correct answer is **partly a convention of this repository** rather than a property of the source, or the deciding evidence is repository state rather than a published surface |
| `UNRESOLVABLE` | E-1…E-4 hold **and the gold answer is that the published record does not decide the question**. A legitimate benchmark item, and the rarest capability it tests is the refusal to grade |
| `UNVERIFIABLE_SURFACE` | **E-1 fails**: the deciding surface cannot be obtained, or cannot be quoted (corrupt text layer, closed access, un-held version) |
| `EXCLUDE` | subsumed by a stronger case on the same paper; or the defect no longer exists; or it belongs to a different benchmark family; or no ground truth exists yet |

🔴 **`UNRESOLVABLE` and `UNVERIFIABLE_SURFACE` are not the same failure.** In the first, the record
is complete and still does not decide — that is a **finding**. In the second, the record would
decide and we do not hold it — that is a **debt**. Scoring them together would reward a system for
saying *"cannot be determined"* when the honest answer is *"go and get the file"*.

---

## 2 · Benchmark eligibility — all 48 cases

`RD` = `GOLD_FACTS_REDERIVED` (§3). `CONT` = contamination after an allowlist surface build (§4).

### 2.1 · `GOLD_ELIGIBLE` — 29

| Case | Question in one line | Why it passes E-1…E-4 | RD | CONT |
|---|---|---|---|---|
| `HC-A1` | Is the lithium effect genotype-restricted? | Surface held; verdict determinate (present in all three genotypes, interaction never computed); both directions are named overclaims | ◻→✅ *partial* | 🔴 FULL |
| `HC-A3` | Progenitors or neurons? | XML held; cell identity is readable from a panel; abstract carries the error | ◻ NO | 🟡 PART |
| `HC-A4` | Which synaptic arm changed more? | XML held; two magnitudes, ranking is arithmetic | ◻ NO | ✅ CLEAN |
| `HC-B2` | Which bar is the knockout? | HTML + PDF held; labels < bars is observable; the text determines the assignment | ◻ NO | ✅ CLEAN |
| `HC-B4` | Is Fig 5D significant? | XML held; caption and printed statistic disagree, both quotable | ◻ NO | ✅ CLEAN |
| `HC-B5` | Six categories or five? | PDF + fitz text + assets held; discriminant printed in the caption | ◻ NO | ✅ CLEAN |
| `HC-B6` | Is WWOX a calpain substrate? | PDF held; the assay inventory is enumerable and empty of cleavage assays | ◻ NO | ✅ CLEAN |
| `HC-C1` | Which comparisons are supported? | XML held; the statistical apparatus is enumerable and empty | ◻ NO | ✅ CLEAN |
| `HC-C2` | Which of `*` / `**` is smaller? | XML held; both legends print numbers | ◻ NO | ✅ CLEAN |
| `HC-D1` | Do *Wwox*-null mice have epilepsy? | **✅ decisive surface rendered this session**; empty cell visible at 400 dpi and invisible in text | ✅ **YES** | ✅ CLEAN |
| `HC-D2` | Is osteoclast activity impaired? | HTML + PDF held; absence of a named test is checkable | ◻ NO | ✅ CLEAN |
| `HC-D4` | Is K274R ubiquitinated? | XML + assets held; the ladder is in the panel | ◻ NO | ✅ CLEAN |
| `HC-E1` | Is GSK-3β the target of the rescue? | XML + supplement held; the two arms and the absence of a bridge are enumerable | ✅ *by prior run* | 🟡 PART |
| `HC-E2` | Does the paper support its title? | XML + PDF held; measured entities vs claimed entity is an inventory | ◻ NO | ✅ CLEAN |
| `HC-E3` | Does gene therapy *restore*? | PDF + assets held; the WT comparator is in the panel | ◻ NO | ✅ CLEAN |
| `HC-F1` | ITCH: which stabilises what? | three surfaces held; substrate/chain/direction each quotable | ◻ NO | 🟡 PART |
| `HC-F2` | Is there an intermediate class? | **✅ re-derived this session**; the denial is one sentence in the framework's own source | ✅ **YES** | 🟡 PART |
| `HC-G1` | Runx2: which sign? | HTML + PDF held; two quantifications, one Discussion contradicting both | ◻ NO | ✅ CLEAN |
| `HC-G3` | Metabolic phenotype or stage artefact? | XML held; the confound is named in the section heading | ◻ NO | ✅ CLEAN |
| `HC-G4` | Are heterozygotes normal? | both XML held; level-of-observation is explicit in both | ◻ NO | ✅ CLEAN |
| `HC-I2` | Is the text layer usable? *(screening axis)* | PDF held; symbol-absence screen is a command; 25 corruptions countable | ◻ NO *(the screen is described in the prior artifact and was **not** re-run here)* | 🟡 PART |
| `HC-I3` | Will a reader see the captions? | **✅ re-measured this session** — 0/6 on Salah, corpus totals in §0.1 #10 | ✅ **YES** | 🟡 PART |
| `HC-I4` | Does the recipe rebuild the artefact? | PDF + receipt held; three join implementations, three digests, none matching | ◻ NO | 🟡 PART |
| `HC-I7` | Which panel supports the sentence? | figure held; caption settles the pointer | ✅ *by prior run* | 🔴 FULL |
| `HC-I8` | How many panels does a figure have? | four papers held; captions readable; parser output comparable | ◻ NO | 🟡 PART |
| `HC-I9` | Is Havali 2021 in PMC? | four route responses; `LinkName` decides — **requires the responses frozen as fixtures** | ◻ NO | 🟡 PART |
| `HC-I10` | Has the full text been retrieved? | files on disk + digests; structural assertion is a command | ◻ NO | 🟡 PART |
| `HC-J2` | Is a WWOX-mimetic safer? | **✅ re-derived this session**; Supplementary Figure C decisive and held | ✅ **YES** | ✅ CLEAN |
| `HC-J3` | Elevated, or de-repressed? | both surfaces held; the assay consequence follows from the mechanism | ✅ *registry* | 🔴 FULL |

### 2.2 · `GOLD_WITH_MULTIPLE_ACCEPTABLE_OUTCOMES` — 2

| Case | Why E-2 fails in a bounded way | The acceptable set |
|---|---|---|
| `HC-C3` | Two P-values for one comparison, **both printed in the paper**. Preferring the panel (machine output, unrounded) and preferring the Methods (`< 2.2E−18`, R's floating-point floor) are *both* defensible; what is not defensible is silence about the other | (a) both carried, exact P declared not recoverable; (b) panel value carried **with** the Methods value recorded as conflicting; (c) Methods value carried **with** the panel value recorded as conflicting. **Rejected:** either value alone |
| `HC-F3` | Genuinely conflicting small-*n* clinical evidence on **two non-exclusive axes** (efficacy on spasms · MRI toxicity). The literature does not resolve it, and several defensible summaries exist | (a) `conflicting evidence` sustained, both axes named; (b) same, plus the explicit note that the organoid mechanism fails *as a predictor* while remaining valid *as a mechanism*. **Rejected:** any resolution in either direction, and any collapse to *"insufficient evidence"* that drops one of the two signals. **Handle under the no-medical-advice rule** |

🔴 **`HC-F3` must never be scored by a harness that rewards a resolution.** Its whole content is
that resolving is the error. A rubric that gives partial credit for *"probably contraindicated"*
trains exactly the failure the case exists to catch, in the one domain where being wrong has
real-world weight.

### 2.3 · `STRESS_ONLY` — 4

| Case | Which condition fails |
|---|---|
| `HC-B3` | E-4 weak. The missing minus sign is a typographic defect; once *"check the axis is monotonic"* is named, the failure stops being one a careful reader commits. It is a probe, not a discriminator |
| `HC-D3` | E-1/E-3. Its only source is a review that is **not peer-reviewed**; the prior artifact records this as its own prior overstatement. The `Olig2-Cre` primary must be read before any verdict exists |
| `HC-G2` | E-1. The case requires *"both primaries (not the review)"* and **names no PMID for either** (P47T, SCAR12 organoids). The surface cannot even be enumerated, so it cannot be checked for reachability |
| `HC-I6` | E-3. The deciding evidence is repository state (`CORPUS P206`, `Identifier: PENDING`), not a published surface. Real and worth testing — but it tests custody hygiene, not reading |

### 2.4 · `UNRESOLVABLE` *(gold = the record does not decide)* — 4

| Case | What is not decided, and why the record is nonetheless complete |
|---|---|
| `HC-A2` | The P-threshold behind `****`. The legend defines `n.s.` and `*** P < 0.001` and nothing else; `****` occurs zero times in prose; Methods declare a single α = 0.05. Every surface exists and none defines the token |
| `HC-B1` | Whether WWOX binds Tau **on this evidence**. The text and the published legend both assert a Tau blot; **the image contains none** (✅ measured). Whether this is a swapped figure or a mislabelled panel cannot be distinguished. Not established — and **not refuted** |
| `HC-C4` | `n` for the human controls. Methods say one fetus, Results say three, the figure shows one Ctrl column. Three surfaces, three readings, all present |
| `HC-F4` | Which of `[75, 76]` supports *"different, with some overlapping, tau residues"*. Saeki measures one site (Ser396) and never addresses selectivity; ref 75 is unread. **Convertible to `GOLD_ELIGIBLE` by reading Mukai 2002 (PMID 12065620)** |

### 2.5 · `UNVERIFIABLE_SURFACE` — 4

| Case | The surface, and the route that would close it |
|---|---|
| `HC-H1` | The **bioRxiv preprint** `10.1101/2024.12.22.630016` is not held, so no version *difference* is measurable. Its other axis — resolving an expired preprint DOI to its published record — **is decidable today and must be split into its own case ID before either is scored** |
| `HC-I5` | **Figure S4** in `oncotarget-07-4344-s001.pdf`, behind a PMC proof-of-work challenge. **Not circumvented, and must not be.** The gold is a declared, addressed gap naming the exact missing object |
| `HC-J1` | PMID 25703206 is **absent from the local corpus** (verified: no matching file under `files/fulltext/` in the main checkout; no row in `surface_census.md`). Acquire, then it becomes `GOLD_ELIGIBLE` |
| `HC-X1` | Johannsen 2018 (PMID 29808465): closed on all four routes tried. **47 citations across 7 canonical files rest on an abstract.** Usable only as a limit-declaration probe, never as a science gold standard |

### 2.6 · `EXCLUDE` — 5

| Case | Why |
|---|---|
| `HC-I1` | ✅ **The defect no longer reproduces** (§0.1 #9). Its diagnosis *and* its fix are in `deepdive_manifest.py`, which the participant must run. Every participant would pass, and pass for the wrong reason |
| `HC-X2` | **No ground truth exists.** The ~10,000-character Europe PMC / efetch body gap has never been adjudicated. Diffing **one** pair once would convert it — and would settle a corpus-wide question. High value as a *measurement*, zero as a gold standard today |
| `HC-X3` | Different benchmark family — a computational-measurement artefact (atom–atom distance), not a reading task |
| `HC-X4` | Subsumed. The `ch?` placeholder tests *"look at the panel"*, which `HC-B4` and `HC-C2` already test on the same paper with scientific stakes |
| `HC-X5` | Subsumed. A motif-tree arithmetic inconsistency with no downstream claim resting on it |

---

## 3 · Re-derivation status

**The rule, stated before the table:** *if the decisive fact is inherited and no primary surface is
available, it cannot silently become a gold label.* Applied strictly, that disqualifies nothing
here — the two cases whose surfaces are unavailable (`HC-J1`, `HC-X1`) are already
`UNVERIFIABLE_SURFACE`. What it does force is the third column below.

| `GOLD_FACTS_REDERIVED` | Cases | Consequence |
|---|---|---|
**Denominator: the 35 potential gold cases** — `GOLD_ELIGIBLE` (29) + `GOLD_WITH_MULTIPLE` (2) +
`UNRESOLVABLE` (4). The other 13 are `STRESS_ONLY`, `UNVERIFIABLE_SURFACE` or `EXCLUDE` and carry no
gold label to re-derive.

| `GOLD_FACTS_REDERIVED` | n | Cases | Consequence |
|---|---:|---|---|
| **YES** | **4** | `HC-D1` · `HC-F2` · `HC-I3` · `HC-J2` | Gold facts stand on a digest I produced. **Gold *label* still requires independent adjudication** (§6) — re-deriving a fact is not adjudicating a verdict |
| **PARTIAL** | **6** | `HC-B1` (all three surfaces ✅, but its negative control is **falsified** and unrepaired) · `HC-A1` (Fig 7d `+/−` and `−/−` ✅ by the prior run, `+/+` still ◻) · `HC-A2`, `HC-E1`, `HC-I7`, `HC-J3` (✅ by the prior run, not re-checked here) | Usable only with the missing half named in the case file. `HC-B1` is **blocked** until its control is rewritten |
| **NO** | **25** | the remainder of the 35 | **Each must be re-derived from the primary before it is scored against anything.** Otherwise the benchmark inherits the errors of the readings it was built to test |

🔴 **Two of the four YES rows produced a correction to the case they confirmed** (`HC-J2`'s
misattributed β-catenin claim; `HC-B1`'s falsified control). That is a **50% correction rate on
re-derivation** of cases the prior artifact ranked #1 and #8. It is a small denominator and I will
not build a rate on it — but it is the strongest available argument that the `NO` rows are not a
formality.

---

## 4 · Contamination — measured, not asserted

### 4.1 · The two questions, kept apart

A case can be contaminated in two different places, and conflating them produces either false alarm
or false comfort:

- **CONTAMINATION_IN_PLACE** — the case is run inside a LEGEND checkout. Then the corpus itself is
  the leak: 40 tracked files name PMID 32000863, 52 name PMID 22193544, 48 name PMID 19500159.
  **Every case in this set is `FULLY_CONTAMINATED` in place.** This is not a finding about any
  case; it is the reason `controlled_benchmark_ab.md` §2.1 builds the surface *outside* every
  checkout, and that document already says it: *the blinding problem is a property of the corpus,
  not of this paper.*
- **CONTAMINATION_AFTER_ALLOWLIST_BUILD** — the case is run on a BENCH-AB-001-style surface, built
  by allowlist into a standalone repository. This is the only design under which any of these cases
  can be blind, so it is the classification the tables in §2 carry.

### 4.2 · The explicit PMID 32000863 test the task asks for

**Claim under test:** the manifest a participant is required to open co-locates provenance with
adjudication.

**Measurement.** `disease-models/wwox/research/deepdive_manifests/PMID32000863.json`, 28,279 bytes,
schema_version 2. Its `source_artifacts` key holds four records — the XML, the supplementary PDF,
and **two figure PNGs including `40478_2020_883_Fig7_HTML.png`** — each with `path` + `sha256`. Its
`verbatim_locators.entries` key holds **25 entries**, of which **4** open with the literal string
`READ FROM THE IMAGE`. Entry 0, verbatim:

> *"READ FROM THE IMAGE, NOT THE TEXT: lithium suppressed PTZ-induced seizures in ALL THREE
> genotypes, including wild-type — so the experiment does not establish a Wwox-specific rescue."*

That is `HC-A1`'s gold answer. Entry 1 is `HC-A1`'s **negative control** (ethosuximide is
genotype-specific). Entries 2 and 23 are `HC-J3`'s gold answer (*"dis-inhibited, not more
abundant"*). Entry 22 restates entry 0. Entry 9 is a fifth adjudication (`+/−` Tc-MEP latency).

**Verdict: co-location CONFIRMED.** Opening this file for the artifact paths and digests puts the
reader in the same JSON object as five adjudications, two of which are gold answers in this set.

**And now the half the prior framing got wrong.** *Required by whom?*

| Role | Must open the manifest? | Route |
|---|---|---|
| Participant re-reading the paper and filing a receipt | **No** | `fulltext_read_receipts.jsonl` carries `source_locator`, `source_fingerprint` and `prior_receipt` for this paper **with no adjudication**. Measured: the row for `FTR-20260804-32000863-01` contains a coverage map, a digest and a workflow note, and no verdict |
| Participant needing **figure** artifact provenance | **No, but only because they must not use it** — `controlled_benchmark_ab.md` §2.3 *excludes* prior renders from the surface precisely because *"their selection encodes a prior reader's attention"*. The participant renders and hashes its own | own render |
| Participant asked to verify a canonical pointer (`HC-I7`) | **Yes** | the question *is* the manifest |
| **Dispatcher / surface builder** | **Yes** | nothing else enumerates what artifacts exist for the paper |

**Documented contamination path**, then, in the order it actually runs:

```
dispatcher needs "which artifacts exist for PMID 32000863"
   → deepdive_manifests/PMID32000863.json is the only tracked file that answers it
      → the same file's entries[0] states HC-A1's answer
         → if dispatcher == participant, the case is spent before the reading starts
         → if dispatcher ≠ participant, the contamination is contained in the evaluator role
```

**Containment is therefore a personnel constraint, not a file constraint**, and
`controlled_benchmark_ab.md` §2.2 already imposes it: *one writer per surface, transferred once.*

### 4.3 · The leak that no allowlist can remove

The BENCH-AB-001 surface must contain the discipline documents — they define the output the
participant produces. I swept a fixed 12-file mandatory set with a positive control:

```bash
MAND=(roles/scientist.md framework/instruction/epistemic_discipline.md \
      framework/instruction/LEGEND_CORE.md framework/master/gold_is_in_the_details.md \
      framework/master/designed_for_growth.md framework/protocols/fulltext_read_receipt.md \
      framework/protocols/scientist_reading_modes.md framework/eval/failure_taxonomy.md \
      framework/scripts/deepdive_manifest.py framework/scripts/corpus_firewall.py \
      CLAUDE.md framework/scripts/locator_audit.py)          # 12/12 present, verified
grep -l -i -E "<pattern>" "${MAND[@]}"                        # array form: zsh does NOT word-split
```
*(Positive control: `22193544` → 1 hit in `fulltext_read_receipt.md`, as it must. Denominator: 21
PMIDs and 35 content patterns swept. The array form is mandatory — an unquoted `$MAND` in zsh
returns a silent zero on every pattern.)*

| Leaking file | What leaks | Cases hit |
|---|---|---|
| `framework/protocols/fulltext_read_receipt.md` §`captions_only` | *"Wang 2012 (PMID 22193544) describes its Supplementary Figure A, in **both** the main text **and** the published legend, as the co-IP proving 'WWOX does not associate with Tau' — while the image contains **no Tau blot at all**, its two panels being labelled WWOX and GSK3β."* — **the complete gold answer**, with the reasoning | **`HC-B1`** 🔴 FULL |
| `framework/scripts/deepdive_manifest.py` L96–103 | *"PMID 32000863 entry 0, where the caption says lithium suppressed seizures in Wwox−/− mice — true — and the panel shows the same suppression in +/+ and +/−"* — **the complete gold answer** | **`HC-A1`** 🔴 FULL |
| same, same block | *"PMID 36779245 entry 0, where the text says one versus two missense variants make no difference and Figure 4A orders null/missense ABOVE missense/missense"* — the **premise** `HC-F2`'s answer rests on, on a different question | **`HC-F2`** 🟡 PART |
| same, L340–349 | the fabricated-space diagnosis in full, **and the fix beside it** | **`HC-I1`** 🔴 FULL (already `EXCLUDE`) |
| `framework/instruction/epistemic_discipline.md` L22, L39 | *"K48 chains commonly support proteasomal turnover, whereas K63 chains have several context-dependent roles"* — generic, naming neither WWOX nor ITCH, but it **hands the reader the exact discriminating concept** `HC-F1` turns on | **`HC-F1`** 🟡 PART |

Measured **absent** from the mandatory set (case-sensitive where it matters): `RUNX2` · `Olig2` ·
`K274` · `GS-1` · `Gemini` · `calpain` · `\bATR\b` · `\bITCH\b` · `null/missense` · `Epilepsy row` ·
`epileptogenesis` · `Ludes-Meyers` · `Oliver` · `Breton` · `Salah` · `Abu-Odeh` · `Cheng` ·
`Steinberg` · `Saeki` · `Mukai` · `vigabatrin` · `Johannsen` · `SATB2` · `CTIP2` · `KU-55933` ·
`GRID1` · `Havali` · `LinkName`. 🔴 Two apparent hits were false positives and are recorded as such:
case-insensitive `atr` matches *"matrix"*; case-insensitive `itch` matches *"stitched"* and
*"switched"*. Both were checked with `\b…\b` case-sensitive and returned **0**.

🔴 **`HC-B1` and `HC-A1` cannot be made blind.** Removing the passage from
`fulltext_read_receipt.md` would remove the rule the reading is graded against; redacting the
comment in `deepdive_manifest.py` would change the bytes of the validator both readers must run and
break parity. These are the prior artifact's **#1 and #4** ranked candidates.

### 4.3.1 · The full assignment, so the summary counts are auditable

Every one of the 48, after an allowlist build. The 29 `GOLD_ELIGIBLE` carry their value in §2.1; the
other 19 are assigned here, all by the same sweep.

| Status | n | Cases |
|---|---:|---|
| 🔴 `FULLY_CONTAMINATED` | **6** | `A1` `B1` `I1` (discipline-file leak, irremediable) · `I6` `I7` `J3` (the question **is** repository state — contaminated by construction, not by accident) |
| 🟡 `PARTIALLY_CONTAMINATED` | **11** | `A2` (manifest gives the observation, no verdict) · `A3` `E1` `I2` `I3` `I4` `I8` `I9` `I10` (infrastructure and provenance cases where the tool under test is the tool the participant runs) · `F1` (`epistemic_discipline.md` supplies the K48/K63 discriminant) · `F2` (`deepdive_manifest.py` supplies the premise) |
| ✅ `CLEAN_BLIND` | **31** | the remaining 31: `A4` `B2` `B3` `B4` `B5` `B6` `C1` `C2` `C3` `C4` `D1` `D2` `D3` `D4` `E2` `E3` `F3` `F4` `G1` `G2` `G3` `G4` `H1` `I5` `J1` `J2` `X1` `X2` `X3` `X4` `X5` |
| `UNKNOWN` | **0** | every case's distinctive identifier or content was named in one of the three sweeps |

🔴 **`UNKNOWN: 0` is a claim about a fixed 12-file set and 56 named patterns, not about the
universe.** A leak phrased in words I did not think to grep for would not appear. The sweep is
reproducible and its patterns are listed above precisely so someone can extend it and find one.

### 4.4 · The general form, with its denominator

The PMID 32000863 co-location is not an accident of one file. Measured across
`deepdive_manifests/*.json` at `5b1d6c2`:

| Measurement | Value |
|---|---|
| Manifests | **64** |
| Carrying `source_artifacts` | 60 |
| Carrying `verbatim_locators.entries` | 63 |
| **Carrying both — provenance and adjudication in one file** | **60** |
| …of those, entries carrying adjudicative language *(regex: `READ FROM THE IMAGE\|not established\|unsupported\|contradict\|refut\|overclaim\|does not support\|never (measured\|tested)\|no …(blot\|test\|antibody)\|is not \|cannot be`)* | **38** |
| Distinct **figure**-artifact digests declared | **333**, across **58** papers |
| …also present in the receipt ledger (the non-adjudicating surface) | **3**, all for PMID 42397075 |
| **Papers whose figure provenance exists nowhere outside an adjudicating file** | **57 of 58** |
| Non-manifest tracked files carrying any figure digest | 8 — the ledger, three `*_locators.md` dossiers, four `page_adjudications/` files |

The regex is a **screen, not a classification**; I read PMID 32000863's 25 entries directly to
confirm it fires on real adjudication. Seven of the eight non-manifest holders are themselves
adjudication artifacts, by name.

**Reproduction note.** These sweeps run against `HEAD` (`5b1d6c2`), where this file is untracked. If
this artifact is committed, every PMID and every quoted verdict in it enters the population and the
counts move. Re-run with `-- . ':!learning/'` or the numbers will describe a corpus that now
includes its own audit.

---

## 5 · Benchmark axes

Fifteen axes, assigned per case. **They are not summed.** A system that reads panels well and
resolves provenance badly should show two numbers, not one average that hides both.

| Axis | Cases |
|---|---|
| `TEXT_EXTRACTION` | `I1`(ex) `I2` `I3` `I4` `I10` `D1` |
| `VISUAL_PDF_ADJUDICATION` | `A1` `A2` `B1` `B2` `B3` `B4` `C1` `D1` `D2` `D4` `E2` `E3` `G1` `I2` `I7` `I8` `J2` |
| `STATISTICS` | `A2` `C1` `C2` `C3` `C4` `D2` `B4` `F2` |
| `NEGATIVE_EVIDENCE` | `B1` `D1` `D2` `D3` `B4` `C1` `J2` `A1` `I2` `I4` |
| `CAUSALITY` | `E1` `E2` `E3` `B6` `G3` |
| `MULTI_PAPER_REASONING` | `F1` `F2` `F4` `D1` `D4` `G2` `G4` `J3` `E3`+`H1` |
| `PROVENANCE` | `D1` `F4` `I4` `I6` `I9` `I10` `X1` `H1` |
| `SOURCE_IDENTITY` | `H1` `I6` `I9` |
| `LOCATOR` | `I1`(ex) `I2` `I7` `I4` |
| `TRANSFER_DISTANCE` | `J1` `J2` `G2` `G3` `D3` |
| `CONTRADICTION_RESOLUTION` | `F1` `F3` `G1` `C3` `B4` `C4` |
| `UNRESOLVABILITY_RECOGNITION` | `B1` `A2` `C4` `F4` `I5` `X1` `A1` `C3` |
| `ABSTRACT_VS_FULLTEXT` | `A3` `A4` `J1` `X1` `E2` |
| `SUPPLEMENT_DEPENDENCY` | `B1` `I5` `J2` `E1` `G3` |
| `PREPRINT_VS_PUBLICATION` | `H1` `E3` |

**Coverage after eligibility filtering.** Every axis retains at least one `GOLD_ELIGIBLE`,
`GOLD_WITH_MULTIPLE` or `UNRESOLVABLE` case **except one**: 🔴 `PREPRINT_VS_PUBLICATION` is carried
by `H1` (`UNVERIFIABLE_SURFACE`) and `E3` (whose preprint axis is `H1`). **The axis has no runnable
case until the bioRxiv version is retrieved.** `LOCATOR` is down to `I2`/`I7`/`I4` now that `I1` is
excluded, and `I7` is `FULLY_CONTAMINATED` — so that axis is thin, not absent.

---

## 6 · Gold specifications

Full field set for the strongest candidates. **`NEEDS_INDEPENDENT_ADJUDICATION: YES` everywhere
below** — a re-derived fact is not an adjudicated verdict, and no final gold label is created here.

---

### `GOLD-01` ← `HC-D1` — the epileptogenesis chain

- **CASE_ID:** `GOLD-01` · status `GOLD_ELIGIBLE` · RD **YES**
- **QUESTION:** Has epileptogenesis been measured in the *Wwox*-null **mouse**?
- **ALLOWED_SOURCE_SURFACES:** PMID 30290271 (asserting) · PMID 19936220 (cited) · PMID 19500159 (terminal). Nothing else.
- **REQUIRED_SOURCE_SURFACES:** **Table 2 of PMID 19500159 rendered as an image.** Text extraction of that table returns `Epilepsy` followed by one value and no column marker (✅ measured) — the decisive evidence does not survive it.
- **EXPECTED_OBSERVATIONS:** three columns (`Wwox−/−` mice · `Wwox^gt/gt` mice · `lde/lde` rats); the `Epilepsy` row **blank under both mouse columns**; `Vacuolization` identically shaped; footnote attributing the mouse columns to Aqeilan 2007/2008/2009; the running text on the same page reporting seizures in **33% spontaneous / 95% audiogenic `lde/lde` rats**.
- **ACCEPTABLE_INFERENCES:** the chain terminates in **contrary** evidence, not absent evidence; the epilepsy phenotype in this literature is a **rat** phenotype; an empty table cell here is a *reported* negative, not missing data.
- **FORBIDDEN_OVERCLAIMS:** retaining epileptogenesis in the null mouse; **and equally** asserting the mouse is *proven* non-epileptic — the terminal source reports *no reported epilepsy*, a statement about the literature.
- **FORBIDDEN_UNDERCLAIMS:** marking the claim *"unverified"* and leaving it standing; generalising the rejection to human WWOX-DEE, where epilepsy is abundantly established.
- **EXPECTED_EPISTEMIC_STATUS:** rejected **on contrary evidence**.
- **WHAT_MAKES_IT_UNRESOLVABLE:** nothing — but note what *is* open: whether the mouse lacks the phenotype or dies before expressing it. Earliest rat seizure onset (day 16) exceeds the entire lifespan of the mouse null.
- **SCORING_DIMENSIONS:** `PROVENANCE` (chain walked to terminus, both hops) · `NEGATIVE_EVIDENCE` (not-measured vs measured-and-negative) · `VISUAL_PDF_ADJUDICATION` (empty cell read) · `TRANSFER_DISTANCE` (rat ≠ mouse; mouse ≠ human).
- **CONTAMINATION_CHECK:** ✅ `CLEAN_BLIND` after allowlist build. Mandatory set: `epileptogenesis`, `Ludes-Meyers`, `Table 2`, `no reported epilepsy` → 0 hits. 🔴 In place: `claim_registry_current.md` states the full verdict including *"a Table 2 whose `Epilepsy` row is **empty for both mouse models**"*, and `DIS-011` restates it. 48 tracked files name PMID 19500159.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES**

---

### `GOLD-02` ← `HC-F2` — the intermediate genotype class

- **CASE_ID:** `GOLD-02` · status `GOLD_ELIGIBLE` · RD **YES**
- **QUESTION:** Does `null/missense` constitute an intermediate-severity class in WWOX-related disorders?
- **ALLOWED_SOURCE_SURFACES:** PMID 42128308 (the review, which presents class 2 as intermediate) · PMID 36779245 (Oliver 2023, the framework's source).
- **REQUIRED_SOURCE_SURFACES:** Oliver 2023 §2.4, §3.6–3.7, Table 3, Figure 4A/4B and the Discussion.
- **EXPECTED_OBSERVATIONS (✅ all re-derived):** the three-class scheme is **Oliver's own** (Methods, verbatim); 75 cases, 45/15/15; time-to-death **p = .0085** log-rank, 5-y <50% vs >75%, 10-y 25% vs >60%; time-to-seizure-onset **p = .65**; the paper groups the two missense classes as *"the other two, presumably less severe, genetic groups"*; and the Discussion states *"**We found no difference between individuals with one or two missense variants and therefore no evidence to support an 'intermediate' phenotype**"*.
- **ACCEPTABLE_INFERENCES:** a **binary** split (double-null vs ≥1 missense) on **survival only**; no genotype effect on seizure onset; the review's three-class rendering is denied by its own source.
- **FORBIDDEN_OVERCLAIMS:** using the three-class scheme as a severity framework; *"missense ⇒ residual function ⇒ milder"* — falsified by a homozygous missense (p.Ser304Tyr) fatal in early infancy.
- **FORBIDDEN_UNDERCLAIMS:** *"genotype does not predict severity"* — it stratifies survival at p = .0085.
- **EXPECTED_EPISTEMIC_STATUS:** `DATO` binary survival stratification; the intermediate class **`UNSUPPORTED` by its own source**.
- **WHAT_MAKES_IT_UNRESOLVABLE:** n/a.
- **SCORING_DIMENSIONS:** `MULTI_PAPER_REASONING` · `STATISTICS` (two log-rank tests, opposite outcomes) · `SOURCE_IDENTITY` (review vs primary).
- **CONTAMINATION_CHECK:** 🟡 `PARTIALLY_CONTAMINATED` — `deepdive_manifest.py` L98 tells the participant *"the text says one versus two missense variants make no difference"*. That is the premise, on a question about Figure 4A. **The verdict is not leaked; the key fact is.** 29 tracked files name PMID 36779245.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES**

---

### `GOLD-03` ← `HC-J2` — the WWOX-mimetic safety argument

- **CASE_ID:** `GOLD-03` · status `GOLD_ELIGIBLE` · RD **YES**
- **QUESTION:** Is WWOX's inhibition of GSK3β substrate-selective, and would a WWOX-mimetic therefore be safer than lithium?
- **ALLOWED_SOURCE_SURFACES:** PMID 22193544 — JATS body, main Figures 1b/c and 4b/c, **and the supplement archive**.
- **REQUIRED_SOURCE_SURFACES:** **Supplementary Figure C** (`cdd2011188x3.tif`) with its quantification, and the supplementary legends file.
- **EXPECTED_OBSERVATIONS (✅ re-derived):** GS-1 phosphorylation `−` ≈100 · `GST` ≈93 · `GST-WWOX wt` ≈**19** · `L404A` ≈**87**; the body sentence *"WT but not mutant WWOX inhibits GSK3β phosphorylation of GS-1 (Supplementary Figure C)"*; the body's own specificity control is **Tau S422**, *"which is phosphorylated by MKK4 kinase in vivo"*; and 🔴 the β-catenin sparing sentence is scoped to **RA treatment**, not to WWOX.
- **ACCEPTABLE_INFERENCES:** GS-1 is a genuine GSK3β substrate unrelated to Tau, so the inhibition is a **generic docking-site block**, not substrate selectivity; S422 is a weak specificity control because it is not a GSK3β site; the **safety** argument dies while the **mechanistic** claim (a physical brake is lost, not merely a level) strengthens; a *pool*-selective molecule remains possible and untested.
- **FORBIDDEN_OVERCLAIMS:** *"a WWOX-mimetic is a safer lithium"*; asserting pool segregation as the explanation — it was never measured.
- **FORBIDDEN_UNDERCLAIMS:** concluding the mechanism is worthless; and 🔴 **repeating the β-catenin framing as a WWOX result** — that is the error the case now also tests.
- **EXPECTED_EPISTEMIC_STATUS:** substrate selectivity **refuted**; the mechanism retained.
- **WHAT_MAKES_IT_UNRESOLVABLE:** n/a for selectivity. Pool-selectivity is `UNTESTED`, and must be reported as such rather than as refuted.
- **SCORING_DIMENSIONS:** `SUPPLEMENT_DEPENDENCY` (decisive) · `TRANSFER_DISTANCE` (cellular observation → biochemical property) · `NEGATIVE_EVIDENCE` · `CAUSALITY`.
- **CONTAMINATION_CHECK:** ✅ `CLEAN_BLIND` after allowlist build — `GS-1`, `glycogen synthase`, `L404A` all 0 hits in the mandatory set. 🔴 **But the paper is Wang 2012**, whose *other* supplementary figure is spelled out in `fulltext_read_receipt.md`. A participant given this paper reads that passage and learns that its supplement repays inspection. **Not the answer, but a strong prompt** — so if `GOLD-03` and `GOLD-08` (`HC-B1`) are ever run together, the second is spent.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES**

---

### `GOLD-04` ← `HC-G1` — the Runx2 sign flip

- **CASE_ID:** `GOLD-04` · status `GOLD_ELIGIBLE` · RD **NO**
- **QUESTION:** What is the sign of the RUNX2 change in *Wwox*-KO?
- **ALLOWED_SOURCE_SURFACES:** PMID 18487609 — `_PMC.html` and the PDF.
- **REQUIRED_SOURCE_SURFACES:** Figure 5A and Figure 6C quantifications; both Discussion sentences.
- **EXPECTED_OBSERVATIONS:** ◻ in vivo **+50%** femur / **+39%** calvaria; ex vivo isolated calvarial osteoblasts **−70%**; a Discussion that writes *"decreased RUNX2 expression in bone and in isolated osteoblasts"* and, 400 words earlier, *"slightly increased in both calvarial and femoral bone"*.
- **ACCEPTABLE_INFERENCES:** two signs, one per preparation, each internally consistent; a node that reverses sign between tissue and isolated cell **cannot carry a repositioning hypothesis**.
- **FORBIDDEN_OVERCLAIMS:** any unqualified single sign; averaging the two.
- **FORBIDDEN_UNDERCLAIMS:** *"results are inconsistent"* without recording that each preparation is internally consistent.
- **EXPECTED_EPISTEMIC_STATUS:** `DATO` × 2, preparation-indexed; a single unqualified sign `UNSUPPORTED`.
- **WHAT_MAKES_IT_UNRESOLVABLE:** n/a.
- **SCORING_DIMENSIONS:** `VISUAL_PDF_ADJUDICATION` · `CONTRADICTION_RESOLUTION` (within one paper) · `TRANSFER_DISTANCE` (tissue ↔ isolated cell).
- **CONTAMINATION_CHECK:** ✅ `CLEAN_BLIND` — `RUNX2`, `Aqeilan`, `osteoclast`, `RANKL` → 0 hits in the mandatory set. 38 tracked files name the PMID; `PMID18487609.json` carries 23 entries with 12 adjudicative hits and **15 figure artifacts** whose digests exist nowhere else.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES** — and the ◻ facts must be re-derived first.

---

### `GOLD-05` ← `HC-F1` — ITCH direction, substrate and chain

- **CASE_ID:** `GOLD-05` · status `GOLD_ELIGIBLE` · RD **NO**
- **QUESTION:** Does ITCH stabilise WWOX, or does WWOX block ITCH from degrading a third protein?
- **ALLOWED_SOURCE_SURFACES:** PMID 23370280 · PMID 24550385 · PMID 26675548.
- **REQUIRED_SOURCE_SURFACES:** the CHX chase and `Itch⁻/⁻` MEF panels of 24550385; the ΔNp63α blots of 23370280; the WW-domain competition sentences. 🔴 **Salah 2013's captions are 0/6 inside `<body>`** (✅ re-measured) — a body-clipped route silently returns no caption at all.
- **EXPECTED_OBSERVATIONS:** ◻ 24550385/26675548 — substrate **WWOX**, chain **K63**, outcome stabilisation, degradation-**independent** (0.36 vs 1 in `Itch⁻/⁻`); 23370280 — substrate **ΔNp63α**, proteasomal, degradation **blocked by WWOX**; `K63` and `Lys-63` occur **zero** times in 23370280.
- **ACCEPTABLE_INFERENCES:** the two are **compatible**, not contradictory; WWOX competes with other WW-domain proteins for shared targets while itself being an ITCH substrate on a non-degradative chain; therefore — present in neither paper alone — **raising ITCH activity to stabilise WWOX would simultaneously increase ITCH-mediated degradation of its other substrates. An ITCH lever is not WWOX-selective.**
- **FORBIDDEN_OVERCLAIMS:** *"direct ITCH/proteasomal stabilization"* (the original error, substrate + stabiliser + direction all inverted); proposing ITCH agonism as a therapeutic route.
- **FORBIDDEN_UNDERCLAIMS:** filing the two as `conflicting evidence` and dropping both.
- **EXPECTED_EPISTEMIC_STATUS:** `DATO` on both arcs; the composite non-selectivity conclusion `INFERENZA`, explicitly cross-paper.
- **WHAT_MAKES_IT_UNRESOLVABLE:** n/a.
- **SCORING_DIMENSIONS:** `MULTI_PAPER_REASONING` · `CONTRADICTION_RESOLUTION` (a non-contradiction correctly identified) · `TEXT_EXTRACTION` (the caption trap) · `TRANSFER_DISTANCE`.
- **CONTAMINATION_CHECK:** 🟡 `PARTIALLY_CONTAMINATED` — `\bITCH\b` is absent from the mandatory set, but `epistemic_discipline.md` supplies the discriminating concept (*"K48 … proteasomal turnover, whereas K63 … context-dependent roles"*) as a generic premise example. The reader is handed the key without being handed the lock.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES**

---

### `GOLD-06` ← `HC-E2` — the ATR that was never measured

- **CASE_ID:** `GOLD-06` · status `GOLD_ELIGIBLE` · RD **NO**
- **QUESTION:** Does PMID 26675548 establish that WWOX modulates the **ATR**-mediated checkpoint?
- **ALLOWED_SOURCE_SURFACES:** PMID 26675548 XML + PDF + assets. 🔴 **Not** the supplement (`Figure S4` is `GOLD-11`/`HC-I5`, a different question behind a challenge).
- **REQUIRED_SOURCE_SURFACES:** the Methods antibody list; the inhibitor identity; **Figure 6's schematic**.
- **EXPECTED_OBSERVATIONS:** ◻ antibody list (CHK1, p-CHK1 S296, p-H2AX, ATM, p-ATM S1981, KAP1, p-KAP1, p-H3, WWOX, GAPDH, HSP90, lamin) contains **no anti-ATR**; zero `p-ATR`, no ATR inhibitor, no ATR knockdown; the sole inhibitor is **KU-55933, an ATM inhibitor**; Figure 6 marks the asserted WWOX→CHK1 arrow with **`?`**.
- **ACCEPTABLE_INFERENCES:** every ATR statement rests on p-CHK1 as proxy, and ATM–CHK1 crosstalk is documented; worse, 48 h of ATM inhibitor **depletes the module that should separate the two arms** — zeroing p-ATM and p-KAP1, nearly zeroing ITCH, reducing WWOX — so *"ATM-dependent signalling"* and *"chronic inhibition depleted the module"* predict the same blot.
- **FORBIDDEN_OVERCLAIMS:** recording WWOX as an ATR-pathway modulator.
- **FORBIDDEN_UNDERCLAIMS:** rejecting the DDR role of WWOX — which would also disturb `DIS-001`, whose argument against inhibiting ITCH rests on it. The cleanest result needs no proxy: **2.8 ± 1 vs 5.7 ± 1.7 breaks per cell**.
- **EXPECTED_EPISTEMIC_STATUS:** ATR involvement **`UNSUPPORTED`**; a checkpoint phenotype `DATO`; the responsible kinase **`UNRESOLVED`**.
- **WHAT_MAKES_IT_UNRESOLVABLE:** the kinase identity — the one perturbation available cannot separate the hypotheses.
- **SCORING_DIMENSIONS:** `CAUSALITY` · `VISUAL_PDF_ADJUDICATION` (the `?` exists only in the panel) · `ABSTRACT_VS_FULLTEXT` (title vs measurement).
- **CONTAMINATION_CHECK:** ✅ `CLEAN_BLIND` — `\bATR\b`, `KU-55933`, `CHK1`, `Abu-Odeh` → 0 hits in the mandatory set (case-insensitive `atr` matches *"matrix"* and was excluded).
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES**

---

### `GOLD-07` ← `HC-B5` — the figure a language model drew

- **CASE_ID:** `GOLD-07` · status `GOLD_ELIGIBLE` · RD **NO**
- **QUESTION:** How many categories of neurodevelopmental fragile-site gene does the review define, and is GRID1 among them?
- **ALLOWED_SOURCE_SURFACES:** PMID 42128308 PDF + fitz text + figure assets.
- **REQUIRED_SOURCE_SURFACES:** §1 text, Figure 2 panel, **Figure 2 caption including its final sentence**.
- **EXPECTED_OBSERVATIONS:** ◻ text lists **six** categories including *glutamate receptor signaling (GRID1, GRM5)*; the figure shows **five**; GRID1 appears nowhere; GRM5 is relocated under *neuron projection development*; caption and panel agree with each other; the caption ends *"This figure was prepared using Gemini."*
- **ACCEPTABLE_INFERENCES:** the panel-over-prose rule is about **data panels**, where the panel is the observation; this panel is a **rendering downstream of the prose**, so the text wins, and the discriminant is free — the caption names the generator.
- **FORBIDDEN_OVERCLAIMS:** recording the five-category taxonomy; recording a genuine contradiction in the field.
- **FORBIDDEN_UNDERCLAIMS:** refusing the review's §1 list because *"the figure disagrees"*.
- **EXPECTED_EPISTEMIC_STATUS:** text `DATO`-as-reported; Figure 2 carries **no independent evidential weight**; the discrepancy is a production defect.
- **WHAT_MAKES_IT_UNRESOLVABLE:** n/a.
- **SCORING_DIMENSIONS:** `VISUAL_PDF_ADJUDICATION` · `CONTRADICTION_RESOLUTION` · `SOURCE_IDENTITY` (schematic vs observation).
- **CONTAMINATION_CHECK:** ✅ `CLEAN_BLIND` — `Gemini`, `GRID1`, `GRM5`, `Obeid` → 0 hits in the mandatory set.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES**. **Negative control that must ship with it:** the same paper's other figures declare *FigureLabs* and *Biorender*. A system must distinguish schematic from observation **generally**, not special-case the word *Gemini*.

---

### `GOLD-08` ← `HC-B1` — Wang 2012 Supplementary Figure A

- **CASE_ID:** `GOLD-08` · status **`UNRESOLVABLE`** · RD **PARTIAL** *(all three surfaces ✅; the case's negative control is falsified and unrepaired)*
- **QUESTION:** Does Supplementary Figure A establish that WWOX does not co-immunoprecipitate Tau?
- **ALLOWED_SOURCE_SURFACES:** PMID 22193544 JATS body · the supplement archive (images + legends `.doc`).
- **REQUIRED_SOURCE_SURFACES:** **`cdd2011188x1.tif` at a resolution where panel labels are legible**, and `cdd2011188x4.doc`.
- **EXPECTED_OBSERVATIONS (✅ all re-derived):** body — *"Tau was not co-immunoprecipitated in the complex (Supplementary Figure A), indicating that WWOX does not stably interact with Tau"*; legend — *"WWOX does not associate with Tau … **Anti-Tau was used to detect endogenous Tau protein**"*; image — **two panels, labelled WWOX and GSK3β; no anti-Tau blot**; `anti-Tau` occurs **0** times in the body.
- **ACCEPTABLE_INFERENCES:** the paper's only evidence for its negative is **absent from the displayed record**; the legend describes two detections (anti-HA, anti-Tau) and the image has two panels, so the *count* matches and the *identity* of the second does not; **swap and mislabel cannot be distinguished**; the negative is not established **and not refuted**; the Tau arc is intact and untested by this work. The paper itself flags the tension with prior work: *"the inconsistency in results may due to the different expression systems used."*
- **FORBIDDEN_OVERCLAIMS:** *"WWOX does not bind Tau"* (from text or caption). **Equally:** *"the figure proves WWOX binds Tau"*.
- **FORBIDDEN_UNDERCLAIMS:** noting the discrepancy and still recording `conflicting evidence`; omitting that the record cannot distinguish swap from mislabel.
- **EXPECTED_EPISTEMIC_STATUS:** **`UNRESOLVABLE` / not evaluable.** The opposing claim (Chang/Sze) rests on yeast two-hybrid — **neither side is solid**.
- **WHAT_MAKES_IT_UNRESOLVABLE:** the decisive blot is not in the published figure, and no route recovers what the authors ran.
- **SCORING_DIMENSIONS:** `UNRESOLVABILITY_RECOGNITION` (primary) · `VISUAL_PDF_ADJUDICATION` · `NEGATIVE_EVIDENCE` · `SUPPLEMENT_DEPENDENCY`.
- **CONTAMINATION_CHECK:** 🔴 **`FULLY_CONTAMINATED`, irremediably.** `framework/protocols/fulltext_read_receipt.md` §`captions_only` states the answer and its reasoning, and that file is normative for the reading the participant is asked to produce. It cannot be withheld.
- 🔴 **BLOCKER, beyond contamination.** The case's published negative control — *"the GSK3β co-IP in the same supplementary panel is genuine and positive"* — is **falsified by measurement** (§0.1 #2). Under the corrected reading, the lower panel would score a careful reader as wrong. **Do not score this case until the control is rewritten and independently adjudicated.**
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES — and it is the highest-priority adjudication in this set.**

---

### `GOLD-09` ← `HC-A1` + `HC-A2` — Cheng 2020 Figure 7

- **CASE_ID:** `GOLD-09` · status `GOLD_ELIGIBLE` (`A1`) + `UNRESOLVABLE` (`A2`) · RD **PARTIAL**
- **QUESTION (A1):** Is the lithium anticonvulsant effect genotype-restricted to `Wwox−/−`? **(A2):** What P-threshold does `****` denote?
- **ALLOWED_SOURCE_SURFACES:** `PMID32000863_Cheng2020_PMC.xml` · the figure assets · the supplementary PDF.
- **REQUIRED_SOURCE_SURFACES:** Figure 7d at native resolution, **all three sub-panels**; the Figure 7 legend verbatim; Methods *Statistical analysis*.
- **EXPECTED_OBSERVATIONS:** `+/+` N=12 vs 8 ◻ · `+/−` 12 vs 12 ✅ · `−/−` 6 vs 7 ✅, each bracketed `****`; the legend defines **only** `n.s.` and `*** P < 0.001`; `****` occurs **zero** times in prose; Methods declare one-way ANOVA, no post-hoc, no multiplicity correction, no interaction term; both instances of `interaction` in the whole document are in the **bibliography**.
- **ACCEPTABLE_INFERENCES:** the text is true-and-incomplete; the effect is present in controls; the genotype × treatment interaction **was never computed**; four asterisks is a **convention**, and GraphPad's mapping is a property of the plotting software, not of this paper.
- **FORBIDDEN_OVERCLAIMS:** *"lithium specifically rescues the WWOX-null phenotype"*; **equally** *"lithium is non-specific"* — that asserts an absence of interaction never tested; recording `P < 0.0001`; declaring panel 7d invalid.
- **FORBIDDEN_UNDERCLAIMS:** reporting only the text's null-restricted sentence; flagging *"the figure may show more"* without reading the panels; discarding 7d for want of a defined threshold.
- **EXPECTED_EPISTEMIC_STATUS:** `DATO` suppression in all three genotypes · **`UNRESOLVABLE`** whether the rescue is WWOX-specific · **`UNRESOLVABLE`** what level `****` denotes.
- **SCORING_DIMENSIONS:** `VISUAL_PDF_ADJUDICATION` · `STATISTICS` · `UNRESOLVABILITY_RECOGNITION` · `NEGATIVE_EVIDENCE`.
- **CONTAMINATION_CHECK:** 🔴 **`FULLY_CONTAMINATED`, irremediably** for `A1`: `deepdive_manifest.py` L96–103 states the answer, and the file is the validator both readers run. 🟡 `PARTIALLY` for `A2`: the manifest hands over the *observation* (*"each carries its own **** significance bracket"*) but no verdict, and no `0.0001` appears anywhere in it.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES** — and the `+/+` panel is still ◻; the prior run's crop cut its legend.
- **Negative control that must ship with it:** Figure 7b (ethosuximide) **is** genotype-restricted — `n.s.` in both controls, `***` in `−/−`. A reader reporting *"all drug panels in this paper are non-specific"* has over-generalised; 7b proves the paper reports restriction when it exists.

---

### `GOLD-10` ← `HC-I3` — six figures, none inside the body

- **CASE_ID:** `GOLD-10` · status `GOLD_ELIGIBLE` (infrastructure) · RD **YES**
- **QUESTION:** How many figures does Salah 2013 have, and will a reader see their captions?
- **ALLOWED_SOURCE_SURFACES:** `PMID23370280_Salah2013_PMC.xml` and the corpus of structured surfaces.
- **REQUIRED_SOURCE_SURFACES:** a caption census over the **whole article tree**, not the `<body>`.
- **EXPECTED_OBSERVATIONS (✅ re-measured 2026-08-26):** Salah 2013 **0/6 captions inside `<body>`**. Corpus: 41 XML parsed — 29 all-in-body, 2 some-outside, **7 all-outside**, 3 no figures, 1 with no `<body>` at all. Also 0/6: **Wang 2012**. Additionally ◻ this depositor uses **lowercase** panel letters while the matcher seeks `[A-J]`.
- **ACCEPTABLE_INFERENCES:** a zero-caption result is a **surface diagnostic**, not a paper property; the panel budget then reads as satisfied because the denominator is zero.
- **FORBIDDEN_OVERCLAIMS:** declaring panel coverage complete; declaring the defect the norm — 29 of 41 are clean.
- **FORBIDDEN_UNDERCLAIMS:** declaring the paper unreadable.
- **EXPECTED_EPISTEMIC_STATUS:** a surface property, no scientific verdict. Any reading reporting `figures: read` without captions is **`INVALID`**.
- **SCORING_DIMENSIONS:** `TEXT_EXTRACTION` · `PROVENANCE`.
- **CONTAMINATION_CHECK:** 🟡 `PARTIALLY_CONTAMINATED` by construction — the tool under test is the tool the participant runs. Mitigation: hand the participant the XML and the question, **not** `caption_census.py`.
- 🔴 **Denominator warning.** The prior artifact records *"62 structured surfaces, 14 with figures outside the body, 8 with all of them outside"*; I measure 41 XML parsed (HTML counted separately by the current tool) with 9 and 7. **Neither is wrong — the populations differ.** Any figure of this kind decays and must be re-run with its date and its command, never quoted forward.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES**

---

### `GOLD-11` ← `HC-I5` — the supplement that decides the claim

- **CASE_ID:** `GOLD-11` · status **`UNVERIFIABLE_SURFACE`** · RD **NO**
- **QUESTION:** Does K274 carry a signalling function beyond stability?
- **REQUIRED_SOURCE_SURFACES:** **Figure S4**, in `oncotarget-07-4344-s001.pdf`, behind a PMC proof-of-work challenge. **Not held. Not circumvented.**
- **EXPECTED_OBSERVATIONS:** ◻ panel 2C shows K274R expressed **less** than WT, so its failure to rescue is confounded by expression; Figure S4 is the control that removes the confound and the only support for the claim.
- **EXPECTED_EPISTEMIC_STATUS:** **`UNRESOLVED — SUPPLEMENT_NOT_HELD`**, with the specific missing object named.
- **FORBIDDEN_OVERCLAIMS:** concluding either way on K274 signalling function.
- **FORBIDDEN_UNDERCLAIMS:** omitting that a **single named figure** would settle it.
- **WHAT_MAKES_IT_UNRESOLVABLE:** nothing intrinsic — this is a **debt, not a finding**. The hole is load-bearing: it decides whether a therapeutic lever is *"more protein"* or *"restore a specific modification"*.
- **SCORING_DIMENSIONS:** `SUPPLEMENT_DEPENDENCY` · `UNRESOLVABILITY_RECOGNITION` (naming the exact missing object, not gesturing at incompleteness) · `PROVENANCE`.
- **CONTAMINATION_CHECK:** ✅ `CLEAN_BLIND` — `K274`, `pmc_pow`, `proof-of-work` → 0 hits in the mandatory set.
- **NEEDS_INDEPENDENT_ADJUDICATION:** **YES**

---

## 7 · The blind replication candidate set

**Requested:** 3 moderate · 3 difficult · 2 multi-paper · 2 visual/PDF · 2 unresolvability. **Cases
may satisfy more than one category; the overlap is made explicit rather than padded around.**

🔴 **The pool is smaller than the request, and the reason is measured, not estimated.** Of the six
cases the prior artifact ranked highest, **three are disqualified by leakage into files the
participant must hold** (`HC-B1`, `HC-A1`, `HC-I1`) and one carries a falsified control (`HC-B1`
again). **I select 9 distinct cases, not 12, and the shortfall is entirely in the
`UNRESOLVABILITY_RECOGNITION` and `VISUAL_PDF_ADJUDICATION` categories**, which is exactly where the
leaks landed.

| Slot | Case | WHY_SELECTED | CONTAMINATION_STATUS | EXPECTED_AXIS | EXPECTED_FAILURE_MODE | CORPUS_BOUNDARY |
|---|---|---|---|---|---|---|
| **Moderate 1** | `GOLD-07` `HC-B5` | Free discriminant printed in the caption; one paper; no supplement | ✅ CLEAN_BLIND | `VISUAL_PDF_ADJUDICATION` · `SOURCE_IDENTITY` | Applies *"figure beats text"* mechanically and carries away that GRM5 is a neuron-projection gene and GRID1 is not a fragile-site gene — **wrong twice, with the text right** | PMID 42128308 only |
| **Moderate 2** | `GOLD-04` `HC-G1` | One paper, two panels, one self-contradicting Discussion; single question | ✅ CLEAN_BLIND | `CONTRADICTION_RESOLUTION` · `VISUAL_PDF_ADJUDICATION` | Extracts the Discussion's single-sign summary and inherits a direction wrong in half of all preparations | PMID 18487609 only |
| **Moderate 3** | `HC-C1` | The statistical apparatus is enumerable and empty; the trap is one word used four times | ✅ CLEAN_BLIND | `STATISTICS` · `NEGATIVE_EVIDENCE` | Ingests *"significantly increased"* as a tested effect, because the word is reliable in almost every other paper | PMID 23370280 only. 🔴 **Its captions are 0/6 in `<body>`** — a body-clipped route returns no caption and no error |
| **Difficult 1** | `GOLD-06` `HC-E2` | Title asserts a kinase with no antibody, no inhibitor, no knockdown; the schematic marks the arrow `?` | ✅ CLEAN_BLIND | `CAUSALITY` · `ABSTRACT_VS_FULLTEXT` | Takes the title as the finding; treats p-CHK1 as ATR-specific | PMID 26675548 main text only — **the supplement is out of bounds** (that is `GOLD-11`) |
| **Difficult 2** | `GOLD-03` `HC-J2` | Supplement-decisive refutation of a **safety** claim; requires separating the claim that died from the one merely different | ✅ CLEAN_BLIND *(see the prompt caveat in §6)* | `SUPPLEMENT_DEPENDENCY` · `TRANSFER_DISTANCE` | Generalises a cellular observation to a biochemical property, in a safety argument | PMID 22193544 + its supplement. 🔴 **Must not be scheduled alongside `GOLD-08`** |
| **Difficult 3** | `GOLD-02` `HC-F2` | The framework's own source denies a third of it in one sentence; sits under this repository's hypomorph and ASO reasoning | 🟡 PARTIALLY | `MULTI_PAPER_REASONING` · `STATISTICS` | Inherits the three-class scheme from the review, then treats counterexamples as anomalies inside a valid framework | PMID 42128308 + PMID 36779245 |
| **Multi-paper 1** | `GOLD-05` `HC-F1` | Substrate, chain and direction all invertible across three papers; the therapeutic conclusion exists in none alone | 🟡 PARTIALLY | `MULTI_PAPER_REASONING` · `CONTRADICTION_RESOLUTION` | Collapses *"proteasomal"* and *"K63, degradation-independent"* into one mechanism because both are *"ubiquitination"* | PMIDs 23370280 + 24550385 + 26675548 |
| **Multi-paper 2** *(also Visual 1, also Unresolvability-adjacent)* | `GOLD-01` `HC-D1` | Two-hop chain, decided by an **empty table cell** that text extraction destroys; five canonical surfaces carried the error for months | ✅ CLEAN_BLIND | `PROVENANCE` · `NEGATIVE_EVIDENCE` · `VISUAL_PDF_ADJUDICATION` | Accepts a citation as an attribution map; reads an empty cell as missing data | PMIDs 30290271 → 19936220 → 19500159 |
| **Visual 2** | `HC-B2` | Three bars, two labels; **read literally the legend inverts the phenotype**; recoverable only by crossing three text statements | ✅ CLEAN_BLIND | `VISUAL_PDF_ADJUDICATION` | Takes the legend at face value and records a bone phenotype of inverted sign | PMID 18487609 Figure 4B. 🔴 **Overlaps `GOLD-04`'s paper — schedule in different sessions or the second is not blind** |
| **Unresolvability 1** | `GOLD-11` `HC-I5` | Correct answer is a **declared, addressed gap** naming one figure | ✅ CLEAN_BLIND | `UNRESOLVABILITY_RECOGNITION` · `SUPPLEMENT_DEPENDENCY` | Adjudicates on the main figures and inherits the expression confound | PMID 26675548 main text + the challenge response. **Overlaps `GOLD-06`'s paper — same scheduling constraint** |
| **Unresolvability 2** | *(vacant)* | — | — | — | — | — |

### 7.1 · Overlaps, stated rather than avoided

| Overlap | Consequence |
|---|---|
| `GOLD-04` and `HC-B2` are the **same paper** (PMID 18487609) | Whichever runs second is not blind. Assign to different actors, or accept the second as a `PARTIALLY_CONTAMINATED` re-read and say so |
| `GOLD-06` and `GOLD-11` are the **same paper** (PMID 26675548), split at the supplement boundary | The boundary is the experiment. If a participant crosses it, both results are void — hence the explicit `CORPUS_BOUNDARY` and the `STOP_CONDITION` in §10 |
| `GOLD-03` and `GOLD-08` are the **same paper** (PMID 22193544) | And `GOLD-08` is already unrunnable. Running `GOLD-03` first is the correct order |
| `GOLD-01` counts in three categories | Deliberate: it is the only case in the set that is simultaneously multi-paper, visual, and a negative-evidence discrimination |
| `GOLD-02` and `GOLD-07` share PMID 42128308 | `GOLD-07` uses §1 + Figure 2; `GOLD-02` uses §10-era framing. Different sections, same PDF — treat as an overlap, not a separation |

### 7.2 · The vacant slot

🔴 **I am not filling it.** The natural candidates were `HC-B1` (irremediably leaked *and* carrying a
falsified control), `HC-A2` (partially leaked, and on the same figure as `GOLD-09`, which is itself
leaked), `HC-C4` and `HC-F4` (both `UNRESOLVABLE` and both `NO` on re-derivation — neither has been
checked against its primary this session, and `HC-F4`'s terminal reference is unread). Promoting any
of them would create the second unresolvability case by decree rather than by evidence, which is the
one failure mode a benchmark of unresolvability recognition cannot afford.

**The cheapest route to a second unresolvability case** is `HC-F4`: read Mukai 2002 (PMID 12065620,
5 tracked mentions, ✅ 0 hits in the mandatory set). If ref 75 supports the clause, the case converts
to `GOLD_ELIGIBLE`; if it does not, it becomes a genuine `UNRESOLVABLE` with a re-derived basis.
Either outcome fills the slot honestly.

---

## 8 · The three test anchors

The task asks what each **evaluates** — and warns against assuming they are gold-ready. Two of the
three are not.

### 8.A · Wang 2012 Supplementary Figure A — which capability does it test?

**All three, and they are separable — which is why the case must be scored on three dimensions, not
one.**

| Candidate | Does it apply? | Evidence |
|---|---|---|
| **Visual adjudication** | **Yes, and it is the gate.** Nothing else opens the case | ✅ The image has two panels labelled WWOX and GSK3β. `anti-Tau` occurs **0** times in the body. No prose route reaches this |
| **Contradiction between image and prose** | **Yes, but of an unusual kind.** The contradiction is *image vs (text **and** caption jointly)* | ✅ Body: *"Tau was not co-immunoprecipitated"*. Legend: *"Anti-Tau was used to detect endogenous Tau protein."* **The two prose surfaces agree with each other and both are wrong.** Prose-vs-prose cross-checking — the cheap check — returns clean |
| **Recognition of unresolvability** | **Yes, and it is the gold label.** Swap and mislabel are not distinguishable | ✅ The legend describes exactly two detections; the image has exactly two panels. The *count* matches, the *identity* does not. Both hypotheses survive |

🔴 **A fourth thing it tests, which the prior framing had backwards.** Under the *mislabel*
hypothesis, the lower panel would BE the Tau blot — and my densitometry shows its HA-IP lane carries
**no band aligned with the INPUT band**, which would make it a *negative* Tau co-IP consistent with
the text. **That reading is live and cannot be excluded**, and it strengthens `UNRESOLVABLE` rather
than weakening it. It also **falsifies the case's published negative control**, which asserted the
GSK3β co-IP is *"genuine and positive"*.

**Verdict: NOT gold-ready.** Two independent blockers — irremediable leakage into
`fulltext_read_receipt.md` (§4.3), and a negative control that would mark a correct reader wrong.

### 8.B · The ITCH multi-paper set — which inference needs the pair, and what stays outside it?

**Requires cross-paper reconciliation** — none of these is derivable from one paper:

1. That the two mechanisms are **compatible**. 23370280 (WWOX blocks ITCH-mediated degradation of
   ΔNp63α) and 24550385 (ITCH ubiquitinates WWOX on K63, non-degradatively) *look* contradictory
   and are not. **The reconciling frame is the authors' own** — competition among WW-domain
   proteins for shared PY targets.
2. That the substrate differs between them (**ΔNp63α** vs **WWOX**), which is what the original
   error inverted.
3. That the chain type differs (**proteasomal** vs **K63, degradation-independent**), and that the
   word *"ubiquitination"* covers both.
4. The therapeutic conclusion present in neither: **an ITCH lever is not WWOX-selective**, because
   raising ITCH to stabilise WWOX raises degradation of ITCH's other substrates — ΔNp63α in
   23370280, p73 in Figure 7 of 24550385.

**Remains outside the pair, and must be scored as `UNRESOLVED` rather than inferred:**

| Fact | Why it is outside |
|---|---|
| Whether WWOX is ever **K48**-ubiquitinated by ITCH | ◻ `K63`/`Lys-63` occur zero times in 23370280 and no sentence describes WWOX as ubiquitinated there; the K63 result is 24550385's alone, and neither paper tests K48 |
| The **stoichiometry** of the competition | Neither measures it; the frame is qualitative |
| Whether the ΔNp63α arc holds in neurons | Both are non-neuronal systems |
| Whether **K274** carries signalling function beyond stability | Decided by `Figure S4` of 26675548 — behind a challenge, `GOLD-11`, **not held** |
| Whether the third paper (26675548) belongs in the pair at all | Its ATR framing is `UNSUPPORTED` (`GOLD-06`); it contributes the K274R data and nothing about the kinase |

🔴 **A surface hazard that governs this set:** ✅ Salah 2013's captions are **0/6 inside `<body>`**.
A reader routing through the body sees no caption for any of six figures **and is told nothing.**

**Verdict: gold-*eligible*, not gold-*ready*.** `GOLD_FACTS_REDERIVED: NO` on every one of the four
inferences; and `epistemic_discipline.md` pre-supplies the K48/K63 discriminant (§4.3).

### 8.C · WWOX-null epileptogenesis — which cell, and which surfaces inherited it?

**The exact evidence gap, ✅ measured this session at 400 dpi:**

`Table 2` of PMID 19500159, *"Phenotypic comparison in the WWOX mutated animals"*, page 9. Three
columns: `*Wwox−/−` (mice) · `†Wwox^gt/gt` (mice) · `lde/lde` (rats). The row:

```
Epilepsy      [blank]      [blank]      Wild running and tonic−clonic convulsion
```

**The generating mechanism, also measured.** `page.get_text()` on the same page returns:

```
Epilepsy
Wild running and tonic–clonic convulsion
```

— one value, **no column marker**. In a table titled *"Phenotypic comparison in the WWOX mutated
animals"*, a text-only reader sees an epilepsy phenotype attached to nothing in particular. **The
two empty mouse cells do not survive extraction, and their emptiness is the evidence.** The same
page's running text confirms the attribution: *"We observed spontaneous epileptic seizures in only
33% of `lde/lde` rats … 95% of `lde/lde` rats experienced at least one epileptic seizure during
exposure to sound stimulation."* The mouse columns are sourced from *"Aqeilan et al. 2007, 2008, and
2009"*, and the epilepsy cell is empty there.

**Canonical surfaces that inherited the claim** — ◻ as recorded, five: `CLAIM 005`, the working-model
changelog, a dossier, a session evaluation, and `DL-MECH-072`. Carried for months across a two-hop
citation chain never verified at either hop.

**Verdict: the strongest gold candidate in the set** — `GOLD_FACTS_REDERIVED: YES`, `CLEAN_BLIND`
after an allowlist build, and the failure mode has a documented five-surface propagation cost.
Still `NEEDS_INDEPENDENT_ADJUDICATION: YES`: I re-derived the *facts*; nobody has adjudicated the
*label*.

---

## 9 · Sampling bias, formalized

### 9.1 · The bias

The 48 cases were mined from: 72 full-text queue entries, 64 deep-dive manifests, 33 prose dossiers,
a 39-claim registry, and a dismissal ledger of 11 active rejections plus 16 recorded defaults.
**Every one of those surfaces exists because somebody already found something hard there.** A queue
entry is a declaration of reading debt. A dismissal-ledger row is an adjudicated rejection. A
manifest with 25 verbatim locators is the residue of a reading that went deep enough to produce 25.

So the sampling frame is not the corpus. It is **the subset of the corpus that has already been
fought over**, and it was assembled by actors who record their own failures — a second enrichment,
in the same direction.

### 9.2 · Why the observed distribution cannot estimate corpus-wide failure rates

Four independent reasons, any one of which is sufficient:

1. **Selection on the outcome.** A case entered the set *because* a defect was found. `P(defect |
   in sample) ≈ 1` by construction. That number carries no information about `P(defect | random
   paper)`.
2. **No denominator.** The mining never enumerated papers-examined-and-found-clean. **The count of
   the clean is missing entirely**, so not even a crude ratio exists.
3. **Depth is confounded with difficulty.** The papers with the richest manifests are the papers
   read hardest. A defect rate computed over them measures *how hard we looked*, not *how often
   defects occur* — and the two vary together across the corpus by an order of magnitude (from
   1-entry manifests to 32-entry ones).
4. **The adjudicators are the mined.** The dismissal ledger is a record of errors this laboratory
   caught. Errors it did **not** catch are, by definition, absent from the frame. This truncates
   precisely the tail a failure-rate estimate is for. 🔴 And the asymmetry runs one way: a false
   positive gets tested and dies; **a false negative is never retested.**

**Consequence, stated plainly:** the 37/48 `HIGH_VALUE` ratio in the prior artifact, and every
per-axis count in §5 of this one, describe **this sample**. Neither is an estimate of anything about
the corpus, and neither may be quoted as one.

### 9.3 · A future unbiased sampling design

**Designed, not executed.**

| Field | Specification |
|---|---|
| `SAMPLING_FRAME` | The **paper registry** at a named commit — every paper the laboratory has ever admitted, whether or not it was read, queued, dossiered or adjudicated. 🔴 Not `full_text_queue_current.md` (debt-enriched), not the manifests (depth-enriched), not the dismissal ledger (outcome-enriched). Frame size must be **enumerated and published before any draw**, and the enumeration command recorded beside it |
| `RANDOMIZATION_OR_SYSTEMATIC_SELECTION` | **Systematic with a published seed.** Sort the frame by a stable key (PMID ascending), draw every *k*-th record from a seeded random start. Reason for systematic over simple random: the frame is small enough that a bad simple-random draw is likely, and a published seed makes the draw **re-executable by a third party** — which a benchmark about provenance has to be |
| `EXCLUSION_RULES` | Applied **after** the draw, each recorded with its count so the exclusion rate is itself a measurement: (a) no obtainable surface after the named acquisition cascade — excluded, **counted separately**, and reported as a retrieval statistic not a reading one; (b) surface class `SUSPECT` on the sentinel — routed to page adjudication, **not excluded**; (c) already read by the assigned actor — reassigned, not dropped; (d) retracted or withdrawn — excluded and counted. 🔴 **No exclusion for "looks uninteresting".** That would rebuild the bias the design exists to remove |
| `BLINDNESS` | Each drawn paper gets its own allowlisted surface (BENCH-AB-001 §2.1–2.3), built by a dispatcher who is not the reader. 🔴 **And the discipline files must be screened per draw** with the §4.3 sweep — the two leaks I measured were both in files nobody suspected. A leak found at build time re-routes the paper to a different actor; a leak found afterwards voids that reading |
| `MINIMUM_SAMPLE` | 🔴 **REQUIRES DESIGN WORK — and the blocker is the estimand, not the arithmetic.** *"Failure rate"* is undefined until the **unit of observation** is fixed: per paper? per claim? per verbatim locator? per figure panel? These give different denominators and different rates from the same readings, and the corpus currently supports all four. **Once the unit is fixed**, the arithmetic is ordinary: for a binomial proportion near p ≈ 0.3, a 95% Wilson interval of half-width ≤ 0.10 needs **n ≈ 81**; half-width ≤ 0.15 needs **n ≈ 36**. Both assume independence between units, which is **false across panels within a paper** and probably false across claims within a reading — so a per-panel or per-claim estimand needs a clustered design and a larger *n* than those figures. **No sample size is proposed here.** Fixing the estimand is the next design act |
| `WHAT_RATE_COULD_BE_ESTIMATED` | With the frame, the draw and a fixed unit: **the rate at which a first reading, under the current discipline, produces a defect of a named class on a randomly drawn corpus paper.** That is the number worth having. It would NOT estimate: the rate in the published literature at large (the frame is a WWOX corpus); the rate for a different actor or a different model; or the rate of **undetected** defects — which needs a second independent reading per paper, i.e. **doubling the sample cost**, and is the only design that reaches the false negatives §9.2 #4 truncates |

`SAMPLING_BIAS_STATUS`: **FORMALIZED, NOT CORRECTED.** The design above is written and unexecuted;
the 48-case set remains a convenience sample of a pre-enriched frame and is labelled as such
wherever its counts appear.

---

## 10 · Participant-facing handoff

**Six fields only. No adjudication, no expected answer, no gold label, no failure mode, no axis.**
Everything in §2–§9 is evaluator information and stays there.

🔴 **One field in the requested set is itself a disclosure, and I am flagging it rather than
silently altering it.** Telling a participant `CONTAMINATION_STATUS: PARTIALLY_CONTAMINATED` tells
them prior work on this paper exists and that some of it may have reached them — which changes how
they read. `CLEAN_BLIND` is harmless. **Below, the field carries the value; at dispatch it should be
rendered as the surface constraint it implies**, per this mapping, and the raw value kept with the
evaluator:

```
CLEAN_BLIND             → "This surface is complete. Do not seek material outside it."
PARTIALLY_CONTAMINATED  → "This surface is complete. Some material you hold was written by
                           readers of other papers; treat any statement about THIS paper found
                           outside the source files as untrusted and record that you saw it."
FULLY_CONTAMINATED      → not dispatched.
```

---

```
CASE_ID:              GOLD-01
QUESTION:             Has epileptogenesis been measured in the Wwox-null mouse?
CORPUS_BOUNDARY:      PMID 30290271, PMID 19936220, PMID 19500159 — these three only.
ALLOWED_SURFACES:     the three full texts as supplied, including page renders you make
                      yourself. Tables must be adjudicated from a render, not from extracted
                      text; state the dpi and the digest of every render you rely on.
CONTAMINATION_STATUS: CLEAN_BLIND
STOP_CONDITION:       stop when you can state, for each of the three papers, what was measured
                      in it — or record that the chain does not terminate and name what is
                      missing. Do not consult any LEGEND registry, ledger, manifest or dossier.
```
```
CASE_ID:              GOLD-02
QUESTION:             Does null/missense constitute an intermediate-severity class in
                      WWOX-related disorders?
CORPUS_BOUNDARY:      PMID 42128308 and PMID 36779245 — these two only.
ALLOWED_SURFACES:     both full texts as supplied, with tables and figures.
CONTAMINATION_STATUS: PARTIALLY_CONTAMINATED
STOP_CONDITION:       stop when you can say what each paper claims about the class and on what
                      evidence, or record that they disagree and which surface decides.
```
```
CASE_ID:              GOLD-03
QUESTION:             Is WWOX's inhibition of GSK3-beta substrate-selective?
CORPUS_BOUNDARY:      PMID 22193544 and its supplementary archive — this paper only.
ALLOWED_SURFACES:     the JATS body, the supplementary images, the supplementary legends file.
                      Inspect images; a caption is not its figure.
CONTAMINATION_STATUS: CLEAN_BLIND
STOP_CONDITION:       stop when you can state what was measured, in what system, against what
                      comparator — or record that the record does not decide and say why.
```
```
CASE_ID:              GOLD-04
QUESTION:             What is the sign of the RUNX2 change in Wwox-KO?
CORPUS_BOUNDARY:      PMID 18487609 — this paper only.
ALLOWED_SURFACES:     the full text with all figures, at a resolution where axis values are
                      legible. State the dpi of any crop you rely on.
CONTAMINATION_STATUS: CLEAN_BLIND
STOP_CONDITION:       stop when you can state the sign, with the preparation it applies to,
                      or record that the paper does not support a single sign.
```
```
CASE_ID:              GOLD-05
QUESTION:             Does ITCH stabilise WWOX, or does WWOX block ITCH from degrading a third
                      protein?
CORPUS_BOUNDARY:      PMID 23370280, PMID 24550385, PMID 26675548 — these three only.
ALLOWED_SURFACES:     all three full texts with figures. Verify your figure/caption recovery
                      against the whole article, not only its body, and report what you found.
CONTAMINATION_STATUS: PARTIALLY_CONTAMINATED
STOP_CONDITION:       stop when you can state, for each paper, the substrate, the chain type
                      and the direction — or record which of those the record leaves open.
```
```
CASE_ID:              GOLD-06
QUESTION:             Does this paper support its title?
CORPUS_BOUNDARY:      PMID 26675548 MAIN TEXT ONLY. The supplementary material is OUT OF BOUNDS
                      for this case. If you open it, say so and stop.
ALLOWED_SURFACES:     the main full text with figures and the Methods in full.
CONTAMINATION_STATUS: CLEAN_BLIND
STOP_CONDITION:       stop when you can list what entities were measured and compare that list
                      against what the title asserts.
```
```
CASE_ID:              GOLD-07
QUESTION:             How many categories of neurodevelopmental fragile-site gene does this
                      review define, and which genes fall in each?
CORPUS_BOUNDARY:      PMID 42128308 — this paper only.
ALLOWED_SURFACES:     the full text, its figures, and every figure caption in full.
CONTAMINATION_STATUS: CLEAN_BLIND
STOP_CONDITION:       stop when you can state the taxonomy and say which surface you took it
                      from and why that surface governs.
```
```
CASE_ID:              GOLD-11
QUESTION:             Does K274 carry a signalling function beyond stability?
CORPUS_BOUNDARY:      PMID 26675548 — this paper only, main text and whatever supplementary
                      material you can lawfully obtain.
ALLOWED_SURFACES:     the main full text with figures. If a surface is behind an access
                      control, DO NOT circumvent it — record the route and the refusal.
CONTAMINATION_STATUS: CLEAN_BLIND
STOP_CONDITION:       stop when you can answer the question, or when you can name the exact
                      object that would answer it and state that you do not hold it.
```
```
CASE_ID:              HC-B2      (no gold spec written; participant-ready)
QUESTION:             In Figure 4B, which bar corresponds to KO?
CORPUS_BOUNDARY:      PMID 18487609 — this paper only.
ALLOWED_SURFACES:     the full text with Figure 4B at a resolution where the legend keys are
                      legible.
CONTAMINATION_STATUS: CLEAN_BLIND
STOP_CONDITION:       stop when you can assign each bar, and state how you assigned it.
```
```
CASE_ID:              HC-C1      (no gold spec written; participant-ready)
QUESTION:             Which comparisons in this paper are statistically supported?
CORPUS_BOUNDARY:      PMID 23370280 — this paper only.
ALLOWED_SURFACES:     the full text with all figures and captions. Verify caption recovery
                      against the whole article, not only its body.
CONTAMINATION_STATUS: CLEAN_BLIND
STOP_CONDITION:       stop when you have enumerated the paper's statistical apparatus and can
                      say which statements rest on it.
```

**Not dispatched:** `GOLD-08` (`HC-B1`) and `GOLD-09` (`HC-A1`/`HC-A2`) — irremediably leaked
(§4.3); `GOLD-08` additionally blocked on its falsified control (§0.2).

---

## 11 · What this document does not claim

- **It proposes no schema, field, rule or governance change.** Where §4.4 describes provenance and
  adjudication sharing a file, that is a **measurement of the current state**, not a proposed slot,
  a proposed split, or a proposed protocol amendment.
- **It creates no gold label.** Every case in §6 carries `NEEDS_INDEPENDENT_ADJUDICATION: YES`,
  including the four whose facts I re-derived myself. Re-deriving a fact is not adjudicating a
  verdict, and the actor who re-derived it is the wrong actor to adjudicate it.
- **It authorizes no run.** `controlled_benchmark_ab.md` §1 lists seven preconditions, **none of
  which this file satisfies or lifts**. This is an input proposal.
- **It does not re-verify the ◻ set.** 21 of the 29 `GOLD_ELIGIBLE` cases are `NO` on re-derivation.
  Each must be re-derived from its primary before being scored against anything — and §3 records
  that re-derivation corrected two of the four cases it touched.
- **Its counts describe this sample.** §9 says why they cannot describe the corpus.
- **Nothing here is medical advice.**

---

## 12 · Summary

```
TOTAL_CASES:                        48

GOLD_ELIGIBLE:                      29
GOLD_MULTIPLE_OUTCOMES:              2   HC-C3 · HC-F3
STRESS_ONLY:                         4   HC-B3 · HC-D3 · HC-G2 · HC-I6
UNRESOLVABLE:                        4   HC-A2 · HC-B1 · HC-C4 · HC-F4
UNVERIFIABLE_SURFACE:                4   HC-H1 · HC-I5 · HC-J1 · HC-X1
EXCLUDED:                            5   HC-I1 · HC-X2 · HC-X3 · HC-X4 · HC-X5
                                    ---
                                     48

CONTAMINATION (after an allowlist surface build; in place, all 48 are FULLY):
CLEAN_BLIND:                        31
PARTIALLY_CONTAMINATED:             11   HC-A2 A3 E1 F1 F2 I2 I3 I4 I8 I9 I10
FULLY_CONTAMINATED:                  6   HC-A1 · HC-B1 · HC-I1 · HC-I6 · HC-I7 · HC-J3
UNKNOWN:                             0   (21 PMIDs + 35 content patterns swept over a fixed
                                    ---   12-file mandatory set, with a positive control)
                                     48

  of which IRREMEDIABLE (leak is in a file the participant must hold):
                                     3   HC-B1 (fulltext_read_receipt.md)
                                         HC-A1, HC-I1 (deepdive_manifest.py)

PROPOSED_BLIND_REPLICATION_CASES:   10 distinct cases filling 11 of the 12 requested slots
                                     moderate 3 · difficult 3 · multi-paper 2 · visual 2
                                     (HC-D1 counted in both multi-paper and visual) ·
                                     unresolvability 1 of 2
                                     1 SLOT VACANT — not filled by decree; the named route to
                                     fill it is reading PMID 12065620 for HC-F4

CASES_NEEDING_INDEPENDENT_ADJUDICATION:
                                    35   every GOLD_ELIGIBLE (29) + GOLD_MULTIPLE (2) +
                                         UNRESOLVABLE (4). No exceptions, including the four
                                         re-derived this session.

  GOLD_FACTS_REDERIVED  YES:         4   HC-D1 · HC-F2 · HC-I3 · HC-J2
                        PARTIAL:     6   HC-A1 · HC-A2 · HC-B1 · HC-E1 · HC-I7 · HC-J3
                        NO:         25   the remainder of the 35

BENCHMARK_AXIS_COVERAGE:            14 of 15 axes retain ≥1 runnable case
                                     PREPRINT_VS_PUBLICATION: 0 — no runnable case until the
                                       bioRxiv version of Steinberg is retrieved
                                     LOCATOR: thin — 3 cases, 1 excluded, 1 fully contaminated

SAMPLING_BIAS_STATUS:               FORMALIZED, NOT CORRECTED. Frame, draw, exclusion rules and
                                     blinding designed; MINIMUM_SAMPLE requires design work,
                                     blocked on fixing the unit of observation, not on arithmetic.

PARTICIPANT_HANDOFF_READY:          YES — 10 cases, six fields each, no adjudication,
                                     no expected answer, no gold label.
                                     Conditional on one personnel constraint that is not a
                                     property of any case: the dispatcher who builds the surface
                                     must not be the participant who reads it (§4.2).
```

🔴 **The one line to carry out of this document.** Of the six cases the prior artifact ranked
highest, **three are unrunnable** — two because their answers are written into files the participant
must hold, one because the defect it tests has already been repaired in the tool under test. The
benchmark's hardest constraint is not finding hard cases. It is that **this laboratory writes down
what it learns in exactly the places a blind reader is required to look.**
