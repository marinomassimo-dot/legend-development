# Source verification of two blunt-instrument audit verdicts — `CLAIM 039` and `CLAIM 014`

**Date:** 2026-09-20 · **Actor:** Scientist A · **File class:** non-canonical analysis.
**Upstream:** `disease-models/wwox/analysis/blunt_instrument_claim_audit_20260920.md` (read in full
before any work here; not redone).

> 🔴 **Read-only. No canonical file was touched.** Nothing under `disease-models/wwox/registries/`,
> `disease-models/wwox/therapeutics/` or `framework/` was edited, no commit candidate was created,
> no claim text, status or tag was changed, and nothing was committed. Wording changes below are
> **proposed as text, not applied**.
> `fulltext_receipts.py verify` at the time of writing → **OK: 168 chained receipt(s), tail anchored**.

## 0 · Why this file exists

The blunt-instrument audit screened all 39 canonical claims for *"an apparently normal phenotype
under a coarse endpoint becomes abnormal under a sensitive one"*, returning `SOUND` 12 · `BLIND` 4 ·
`OVERSTATED` 4 · `CANNOT ASSESS` 4. Two of its verdicts were reached by reasoning **about claim
text** rather than from the claims' sources. This file tests those two against the sources, so that
any commit candidate rests on evidence rather than on inference.

---

## 1 · Read depth per source

| Source | What was read, and how | Depth |
|---|---|---|
| **PMID 17803050** (Suzuki 2007, *Comp Med* 57(4):360–369) — source of `CLAIM 039` | 🔴 **Not re-read in this session, and it cannot be.** PubMed metadata retrieved 2026-09-20 returns `identifiers: {pmid only}` — **no DOI, no PMCID**, confirming the record's standing statement and the manifest's Europe PMC probe (`inEPMC=N, hasPDF=N`, 2026-08-07). The PMC open-access route cannot reach it; no PDF tooling exists here. Worked instead from **LEGEND's own complete-read receipt** `FTR-20260806-17803050-01` — `deepdive_manifests/PMID17803050.json`, schema v2, **all 32 verbatim locators enumerated individually**, plus `fulltext_dossiers/PMID17803050.md` read end to end | **receipt-mediated**, not an independent read — declared as such at every use below |
| **PMID 31340538** (Tochigi 2019, *Int J Mol Sci* 20:3596) — `doi:10.3390/ijms20143596`, PMC6678113 | **Full text retrieved and read in this session** via the PubMed MCP full-text route, Introduction → Results → Discussion → Materials and Methods; cross-read against `deepdive_manifests/PMID31340538.json` (11 locators, `FTR-20260806-31340538-01`) | **complete full text, this session** |
| **PMID 32581702** (Iacomino 2020, *Front Neurosci* 14:644) — `doi:10.3389/fnins.2020.00644`, PMC7300205 | **Full text retrieved and read in this session** by the same route, including the rat Methods and the rat Results section in full; cross-read against `deepdive_manifests/PMID32581702.json` (21 locators, `FTR-20260810-32581702-01`) | **complete full text, this session** |
| `CLAIM 039`, `CLAIM 014`, `PAPER 059`, `PAPER 020`, `PAPER 021`, `CLAIM 037` | `registry_records.py get --id … --hops 1` | full records |
| `working_model_current.md` BLOCK 2 row 039 | read in place | one row |

🔴 **`paper_registry_current.md` and `literature_tracking_log_current.md` were never grepped and
never opened directly** — every record above came through `registry_records.py`.

🔴 **No figure panel was inspected.** There is no PDF tooling and no figure-image route in this
deployment. Every panel-level question below is marked **unresolved**, never answered.

**Attribution.** Full texts for PMID 31340538 and PMID 32581702 were obtained from **PubMed / PubMed
Central**: [10.3390/ijms20143596](https://doi.org/10.3390/ijms20143596) and
[10.3389/fnins.2020.00644](https://doi.org/10.3389/fnins.2020.00644). Metadata for PMID 17803050
also from PubMed (no DOI registered).

---

## 2 · TASK 1 — `CLAIM 039`, the *"not cerebellar"* limb

### 2.1 · What the claim says and what it names

`CLAIM 039` (`claim_registry_current.md:716`, `record_digest=9bcaf1c22e62`), **Status:** `in
observation`, **Type:** `DATO`, **Transferability:** T3, **clinical relevance:** INDIRECT.

> **Title:** *"Ataxic gait is the most penetrant phenotype of the rat `lde/lde` model — 95% versus
> 0% — **and it is not cerebellar**"*

> **Summary:** *"**95%** dei mutanti mostra andatura atassica contro **0%** dei normali. È più
> penetrante delle crisi spontanee (~34%) e più penetrante di qualunque altro fenotipo neurologico
> del modello. Gli autori esaminano il cervelletto e **non trovano alterazioni patologiche
> marcate**, in contrasto esplicito con il topo *ataxia and male sterility* (AMS)."*

> **Evidence boundary:** *"L'atassia **non ha spiegazione strutturale** in questo paper: il
> cervelletto è istologicamente indenne e nessun'altra regione, oltre a ippocampo e amigdala,
> mostra alterazioni **al microscopio ottico**. **Non sono stati eseguiti test motori quantitativi
> (rotarod, footprint, analisi cinematica): la valutazione è osservazionale e non in cieco.**
> Nessun dato su progressione temporale."*

**Source named:** `[[paper_registry_current#PAPER 059]]` — **Suzuki H, Takenaka M, Suzuki K. 2007,
PMID 17803050**, receipt `FTR-20260806-17803050-01`. A **single** source; no co-source.

**Working-model mirror**, `working_model_current.md:189`, reproduced verbatim:

> `| 039 | Ataxic gait is the most penetrant phenotype of the rat lde/lde model — 95% versus 0% — and it is not cerebellar | DATO | P1 neurodevelopment / motor function | T3 | in observation | PAPER 059 (Suzuki 2007) |`

🔴 **The audit's mirror observation is confirmed exactly.** The mirror row carries the title's
mechanistic exclusion with **no endpoint column, no evidence boundary and no `🔴` qualifier marker**
— the marker the mirror already uses on row 011 for precisely this purpose. A reader who consults
BLOCK 2 instead of the registry receives *"it is not cerebellar"* as a bare fact.

### 2.2 · What the source measured

From the 32 verified locators of `FTR-20260806-17803050-01` and the dossier:

| Question | Answer, from the receipt |
|---|---|
| **Gait — what was measured** | Presence/absence of ataxic gait, scored **observationally**. Locator 12: *"95% of the mutant rats but none of the normal rats had ataxic gait"* — anchored to **Results, 'Observation of epilepsy', page 2** |
| **Gait — how many animals, what age** | Locator 12 anchor: *"assessed in **19 female and 20 male mutants** against **14 female and 12 male normals** at **21 days**"* |
| **Gait — quantification** | **None.** A binary categorical descriptor, reported as a percentage. No latency, no distance, no stride, no kinematic variable, no score scale |
| **Gait — blinding** | **Not declared anywhere in the receipt.** Genotype was visually obvious in this strain — the mutants are severely dwarfed (≈56% of normal weight at 21 d) — so genotype-blind observational scoring was not achievable even in principle |
| **Cerebellum — what was measured** | Light-microscopy histology, reported as an absence. Locator 23, **Discussion, page 8** |
| **Cerebellum — n, age, stain, quantification** | 🔴 **Not recorded in any of the 32 locators.** The histology cohort is the 28-day cohort per the paper's own framing, but **no cerebellar n, no stain, no section plane, no counting method and no statistic exists in LEGEND's read of this paper.** Since the paper cannot be reopened, this gap **cannot be closed from here** and is declared rather than guessed |
| **Cerebellum — blinding** | **Not declared.** Same structural obstacle as the gait scoring |
| **Stereology / cell counts anywhere in the cerebellum** | **None** in any locator |

### 2.3 · Is there a quantitative motor or coordination test anywhere in the source?

**No. None exists.** Stated plainly, as the task requires, rather than quoted — because there is
nothing to quote.

The receipt enumerates the paper's sectioning through its locator anchors: Materials and methods
*'Determination of the mode of inheritance'*; Results *'Growth and survival'*, *'Observation of
epilepsy'*, *'Blood examination and urinalysis'*, *'Histologic examinations'*; Discussion; Tables
1–3; Figures 3, 5, 6. **Not one of the 32 locators names rotarod, footprint or gait analysis, beam
walk, ledge test, catwalk, grip strength, open field, or any other motor or coordination assay**,
and no such section exists to hold one. The gait finding is lodged inside the section on **seizure
observation**, where animals were watched *">6 h per day until death"* (locator 10 anchor) — an
observational husbandry protocol, not a motor assay. PubMed's own MeSH indexing of the record
carries **`Lameness, Animal`** — a categorical observational descriptor — and no motor-testing term.

The claim's own evidence boundary already says this in as many words (*"Non sono stati eseguiti test
motori quantitativi (rotarod, footprint, analisi cinematica): la valutazione è osservazionale e non
in cieco"*). **The audit did not have to infer it and neither did I: it is declared canon.** The
source-level check confirms the declaration is accurate.

**The audit is not corrected on this point. `CLAIM 039` names no motor test, and there is none.**

### 2.4 · The one quote the exclusion actually rests on

Locator 23, receipt `FTR-20260806-17803050-01`, **Discussion, page 8** — **PMID 17803050**:

> *"in contrast with the ataxia and male sterility (AMS) mouse,¹⁰ **we did not detect any marked
> pathologic changes in the cerebella of `lde/lde` rats**"*

That single sentence is the entire evidentiary basis for the five words *"and it is not cerebellar"*
in a canonical claim title and in the BLOCK 2 mirror.

### 2.5 · What the source can actually exclude

The sentence is a **negative observation on unblinded light microscopy, of unrecorded n, at an
unrecorded age, with no quantification** — and the authors hedge it themselves with *"marked"*.

**It can exclude:** gross, qualitatively obvious cerebellar histopathology at the magnifications
used — frank atrophy, overt layer disruption, visible vacuolation of the kind the same paper *did*
find and report in CA1 and the amygdala.

**It cannot exclude a cerebellar contribution to the ataxia.** Everything that would test that is
absent from the source: Purkinje-cell stereology or calbindin counts, molecular-layer thickness,
granule-layer density, climbing-fibre refinement, dendritic arborisation, synaptic density,
cerebellar or vestibular electrophysiology, deep-nuclei output timing, and any quantitative
kinematic measure of the gait itself. A cerebellum with a normal complement of Purkinje cells that
fire abnormally is, under light microscopy, an unremarkable cerebellum.

This is structurally the **NeuN instance** the audit identified in §0 of its own table: the cells are
present and look right; how they are wired and whether they fire is never measured. **"No visible
cerebellar histopathology on light microscopy" and "the phenotype is not cerebellar" are not the
same statement, and the claim's title asserts the second on evidence for the first.**

### 2.6 · 🔴 A finding the audit did not have: corpus-internal counter-evidence, in the same species and the same strain

The audit wrote: *"**MORE SENSITIVE EVIDENCE → none in the corpus, in either direction.** No
cerebellar electrophysiology, no Purkinje counts, no DTI and no quantitative gait analysis exists for
the `lde` rat."*

**That is wrong, and this is the substantive correction this file returns.** A cerebellar abnormality
in the `lde/lde` rat is already in LEGEND's corpus, in a paper with a persisted complete-read receipt
that is **canonically linked to `CLAIM 014` and `CLAIM 015`** — PMID 32581702, `PAPER 020`, the
Iacomino 2020 paper that is the subject of Task 2 below. Read this session, Results, *"Abnormal
Neural Migration and Cortical Layer Formation in lde/lde Rats"*:

> *"In addition, **the development of cerebellum was delayed in [`lde/lde`] as shown by reduced
> number of foliation** (Figure 3, arrowheads)."* — **PMID 32581702**,
> [10.3389/fnins.2020.00644](https://doi.org/10.3389/fnins.2020.00644)

and in the Figure 3 caption:

> *"**Arrowheads indicate delayed foliation in [`lde/lde`] cerebellum.**"* — **PMID 32581702**

This is **not** a cross-species splice. It is the **same `lde/lde` rat strain, maintained in the same
colony, reported by the same laboratory** — Iacomino 2020's Methods place the rat arm at Nippon
Veterinary and Life Science University under protocol #2019K-28, and Suzuki H is an author of both
this paper and Suzuki 2007. The `MECHANISM_TRANSFER_FIREWALL` that `therapeutic_repair_candidates.md`
correctly invoked to keep the **mouse** `Wwox⁻/⁻` foliation/Purkinje lesion (PMID 32000863) away from
`CLAIM 039` **does not apply here**, because no species boundary is crossed.

**Four limits on this counter-evidence, stated before it is used for anything:**

1. **It is one sentence, in passing.** The cerebellum is not this paper's subject; the finding is
   reported with **no count, no measurement and no statistic** — *"reduced number of foliation"* and
   an arrowhead.
2. 🔴 **The panel cannot be checked here.** The evidence is arrowheads in Figure 3. There is no
   figure-image route in this deployment, so **whether the arrowheads support the sentence is
   UNRESOLVED and is left unresolved.** For an audit about instrument sensitivity that is itself a
   finding: the only cerebellar datum for this rat is one whose verification requires the one
   instrument this session does not have.
3. **n = 3 per genotype, unblinded.** Manifest entry 17: *"Data from each 3 [+/+] and [`lde/lde`]
   rats genotyped by PCR were used for statistical analysis"*, stated once in Methods and nowhere in
   Results. The word *"blind"* does not occur anywhere in the full text.
4. **The ages do not overlap.** Iacomino measures **P1**; Suzuki 2007's histology is on the ~28-day
   cohort. A *delay* in foliation at P1 is not the same assertion as a *lesion* at 4 weeks, and
   could in principle resolve. The two observations are **compatible as measurements** — and that is
   exactly the point: the P1 abnormality is invisible to the 28-day light-microscopy endpoint, so the
   28-day endpoint's silence was never evidence of cerebellar normality.

Convergent but **not** load-bearing, and kept outside the rat chain: the same paper's human WOREE
fetus was diagnosed with **cerebellar vermis hypoplasia** on prenatal imaging, and the proband's MRI
showed *"hypoplasia of the corpus callosum and inferior cerebellar vermis"*. Human, different
allele, different instrument — recorded as context only.

🔴 **Neither the cerebellar sentence nor the Figure 3 caption appears in any of the 21 locators of
`deepdive_manifests/PMID32581702.json`, and the string "foliation" appears nowhere in
`disease-models/` except in entries about the *mouse* (PMID 32000863).** The rat cerebellar finding
was read and never landed. That is a second-order finding about the reading, not about the biology.

### 2.7 · Verdict on the audit's `BLIND`

> ### **HOLDS.**

The audit's verdict is correct and its reasoning is confirmed at source: the title's mechanistic
exclusion rests on one hedged sentence of unblinded light-microscopy histology, with no n, no age,
no quantification and no motor test anywhere in the paper. The audit **understated** its own case in
one respect — it reported no corpus-internal counter-evidence, and there is some, in the same species
and strain, in a paper LEGEND has already read in full (§2.6). That strengthens the verdict; it does
not change it.

**Closing line — the exact wording change I would propose, as text, not as an edit:**

> Retitle `CLAIM 039` to: **"Ataxic gait is the most penetrant phenotype of the rat `lde/lde` model
> — 95% versus 0% — and it has no gross cerebellar histopathology on light microscopy; the anatomical
> substrate is unresolved."** Leave the 95%-vs-0% finding, the `Status: in observation` and the
> `DATO` type untouched. Append to the existing evidence boundary: *"Il negativo cerebellare è una
> singola frase di istologia in microscopia ottica non in cieco (**«we did not detect any marked
> pathologic changes in the cerebella of `lde/lde` rats»**, PMID 17803050, Discussione p. 8), senza n
> dichiarato, senza età dichiarata, senza colorazione dichiarata e senza quantificazione: **non
> esclude un contributo cerebellare** (conta delle cellule di Purkinje, spessore dello strato
> molecolare, elettrofisiologia e cinematica quantitativa dell'andatura non sono stati misurati).
> 🔴 **Contro-evidenza intra-corpus, stessa specie e stesso ceppo:** PMID 32581702 riporta nel ratto
> `lde/lde` a P1 «the development of cerebellum was delayed … as shown by reduced number of
> foliation» — una frase sola, n=3 per genotipo, non in cieco, non quantificata, e il pannello non è
> verificabile con la strumentazione di questo deployment. Età non sovrapposte (P1 contro ~28 giorni):
> le due osservazioni sono compatibili come misure, ed è precisamente per questo che il silenzio
> dell'endpoint a 28 giorni non è mai stato prova di normalità cerebellare."*
> Propagate the narrowed title into BLOCK 2 row 039 and attach the `🔴` marker the mirror already uses
> on row 011. Precedent for the method: `CLAIM 023`, `BATCH_20260909_001`.

---

## 3 · TASK 2 — `CLAIM 014`, the migration evidence boundary

### 3.1 · What the claim currently says, and what boundary it already carries

`CLAIM 014` (`claim_registry_current.md:256`, `record_digest=161de4b129de`), **Status:**
`consolidated baseline`, **Type:** `DATO`, **T2**, **clinical relevance:** HIGH.

> **Title:** *"WWOX loss perturbs prenatal cortical development, neuronal migration and cortical
> maturation across species"*

> **Summary:** *"Across fetal human tissue, rat `lde/lde` and human neural progenitor models, WWOX
> loss is associated with impaired neuronal migration, altered cortical layering, dysregulated
> cytoskeleton-related developmental programs, and defective cortical maturation with downstream
> hypomyelination/glial-development abnormalities."*

> **Evidence boundary (BATCH_20260806_002):** *"the multi-paper convergence is retained, but **PMID
> 31340538 (Tochigi) contributes early postnatal maturation and hypomyelination at PND5–21 — not
> prenatal migration, not cortical layering, and no directly observed prenatal assembly.** It
> measures no prenatal time point. Its record previously carried an invented title naming
> *lissencephaly*, which had been steering it toward a migration/layering reading the study does not
> make. The prenatal component of this claim therefore rests on Iacomino and Kośla, not on this
> paper."*

**Sources:** Iacomino 2020 (`PAPER 020`, PMID 32581702) · Tochigi 2019 (`PAPER 021`, PMID 31340538) ·
Kośla 2019 (`PAPER 022`).

**So the boundary already fences Tochigi off from the prenatal/layering limb of the claim** — on
grounds of *time point*. What it does **not** say is that Tochigi's Discussion contains a general
negative conclusion about migration, or what happened to that conclusion afterwards.

### 3.2 · The two quotes, verbatim

Neither PMID is cached under `files/fulltext/PMID31340538_*` or `PMID32581702_*` — that directory
holds twelve files and neither of these (checked with `ls` before fetching anything, as instructed).
Both were therefore retrieved this session through the PubMed MCP full-text route from PMC.

**(a) PMID 31340538 — Tochigi 2019, Discussion:**

> *"Although Wwox localized to the cell bodies of neurons in the cerebral cortices of [`lde/lde`]
> rats, **the normal density and distribution of NeuN-positive neurons and the normal level of
> expression of NeuN** in the cerebral cortices of [`lde/lde`] rats **during early postnatal period**
> indicated that **Wwox is not required for proliferation and migration of immature neurons**."*
> — [10.3390/ijms20143596](https://doi.org/10.3390/ijms20143596)

with the underlying result, Tochigi Results §2.2:

> *"Immunohistochemistry using an antibody against a neuronal specific nuclear protein, NeuN did not
> show any significant difference of neuron number between [`+/+`] and [`lde/lde`] rats, and these
> results were also confirmed by western blot analysis. In consistent with these findings, there is
> no significant difference between [`+/+`] and [`lde/lde`] rats in the thickness of cerebral
> cortices at all ages **and in neuron number in each cortical layer at PND21**."* — PMID 31340538

**(b) PMID 32581702 — Iacomino 2020, Results, closing sentence of the rat section:**

> *"**These results indicate that Wwox deficiency impairs prenatal neuronal migration which is
> required for normal cortical layer formation at birth in rats.**"*
> — [10.3389/fnins.2020.00644](https://doi.org/10.3389/fnins.2020.00644)

with its two supporting results in the same paragraph:

> *"There was no significant difference between `+/+` and [`lde/lde`] in the distribution of Tbr1-
> positive cells, whereas **the density of Satb2-positive cells was significantly decreased in the
> surface layer of [`lde/lde`] cortical plate** (area number 1 corresponding to cortical layer II).
> This defect was accompanied by increase in Satb2-positive cells of the bottom layer in [`lde/lde`]
> cerebral wall (area number 7 corresponding to intermediate zone)."* — PMID 32581702

> *"When BrdU-incorporated cells were traced to P1, **we found altered distribution of BrdU-positive
> cells in [`lde/lde`] cerebral walls, revealing delayed migration of late-born neurons**."*
> — PMID 32581702

**Same investigators:** confirmed at source. Tochigi Y is first author of PMID 31340538 and third
author of PMID 32581702; Suzuki H is senior author of both; both papers' rat work is at Nippon
Veterinary and Life Science University. **The audit is right on this.**

### 3.3 · Do the two statements address the same thing? Reversal, or narrowing?

They must be taken **limb by limb**, because the 2019 conclusion is a conjunction of two and only one
limb is touched.

| Limb of the 2019 conclusion | What the 2020 paper does to it | Reading |
|---|---|---|
| *"…not required for **proliferation**…"* | **Nothing.** Iacomino 2020 runs **no proliferation assay** — no Ki67, no phospho-histone-H3, no total neuron count, no VZ/SVZ progenitor quantification. Its E16.5 BrdU is a **birth-dating pulse read at P1**, which measures where cells born on one day ended up, not how many were born. Its only convergent measurement, *"no significant difference between `+/+` and [`lde/lde`] in the thickness of cortical wall"*, is **consistent** with Tochigi | 🔴 **NOT reversed, and not even tested** |
| *"…not required for **migration** of immature neurons"* | **Directly contradicted as an unqualified statement**, by a layer-identity and birth-dating design the 2019 paper did not run, at a time point the 2019 paper did not measure | **Reversed as a conclusion, not as a measurement** |

**The two sets of measurements are compatible; only the 2019 *conclusion sentence* is not.** Nothing
in Iacomino 2020 says Tochigi's NeuN counts were wrong, and nothing needs to: a cortex can hold the
normal number of neurons distributed across morphologically normal-looking bands while the cells that
should be in layer II sit in the intermediate zone. **Neuron *number* is normal; laminar *placement*
is not.** The audit's own one-line summary of the substance is exactly right.

**Three reasons the honest label is *narrowed*, not *reversed*, and one reason it is not purely
narrowing either:**

1. **The time windows do not overlap.** Tochigi measures **PND5, 10, 15 and 21**; Iacomino measures
   **E16.5→P1**. Tochigi's own sentence attaches *"during early postnatal period"* to the **evidence**
   — but leaves the **conclusion** unqualified. The 2020 paper fills a window the 2019 paper never
   entered, and Iacomino's own word is *"**delayed** migration", a defect that may partly resolve by
   the ages Tochigi examined.
2. **The instruments differ in kind, not only in resolution.** Tochigi's layer analysis divided the
   cortex into five bands *"based on specific morphology of NeuN-positive cells"* (Methods §4.4) and
   then counted NeuN⁺ cells within them. Iacomino used **molecular layer-identity markers** — Satb2
   (layers II–IV) and Tbr1 (layers V/VI) — plus **E16.5 BrdU birth-dating**. A misplaced neuron
   retains its molecular identity and its birth date; it does not retain a position that a
   NeuN-morphology band would flag. 🔴 **Worse, the 2019 design is close to circular for this
   question**: the layer boundaries are drawn *from* the cytoarchitecture whose disturbance is the
   phenotype. Iacomino found at P1 that *"boundary between II-IV and V/VI was unclear in [`lde/lde`]
   cortical plate due to irregular cell distribution"* — if a boundary is blurred, drawing it by eye
   from NeuN morphology and then counting inside it cannot detect the blurring.
3. **The 2019 paper was never making a migration argument.** Migration appears once, in a Discussion
   inference; the paper's subject, title and every positive result concern **neurite maturation,
   myelination and glia at PND5–21**. The sentence is a by-product, not a finding.
4. **But it is not pure narrowing either.** The 2019 sentence as written is unqualified in its
   conclusion clause, it entered the literature as a general negative about Wwox and migration, and
   the 2020 paper's closing sentence asserts the opposite in the same species and the same strain.
   **For the migration limb, and only that limb, this is a genuine self-reversal of a stated
   conclusion.**

**Therefore, in one sentence:** *the 2020 paper **narrowed the 2019 paper's evidence and reversed one
limb of its conclusion** — the migration limb, as an unqualified statement — while leaving the
proliferation limb untested and the 2019 measurements standing.*

### 3.4 · Where the audit needs correcting

🔴 **The audit's stated endpoint for the 2019 negative — "bulk NeuN counts" — is inaccurate, and it
matters.** Tochigi 2019 ran **three** NeuN readouts, not one:

1. bulk NeuN density by immunohistochemistry (bulk);
2. NeuN expression level by western blot (**genuinely bulk** — no spatial information at all);
3. 🔴 **NeuN⁺ neuron number in each of five cortical layers at PND21** (**layer-resolved**).

The third is a lamination-adjacent endpoint, and calling the whole thing "bulk" concedes the 2019
authors less than they measured. The right criticism is not *"they only counted in bulk"* — it is
*"their layer-resolved count used layer boundaries defined by the very cytoarchitecture under test,
at a single late age, in males only, n ≥ 3, with uncorrected t-tests and no declared blinding, and it
therefore could not have seen a marker-identity misplacement."* That criticism is stronger, and it is
the one that survives contact with the Methods.

**Both papers are unblinded.** The string *"blind"* occurs **nowhere** in either full text. Both use
Student's t-tests with no multiplicity correction. Tochigi: males only, at least three affected and
three normal per experiment per age, with litters culled to <5 pups at ~PND5 to improve `lde/lde`
survival. Iacomino: n = 3 per genotype, both sexes, stated once in Methods and never in Results.

**Unresolved and left unresolved:** the Satb2/BrdU effect sizes live in Figure 3 panels G and J, and
the asterisk-level adjudication in `deepdive_manifests/PMID32581702.json` (entries 3 and 4) is a prior
reader's panel inspection. **I could not inspect those panels** — no figure-image route exists here —
so I neither confirm nor rely on them. The text carries the direction and the significance; it
carries **no number** for the BrdU result (manifest entry 2 flags exactly this: *"the strongest
quantitative result in the paper is reported in the text as the phrase 'altered distribution', with
no number and no count"*).

### 3.5 · Verdict on the audit's item 4

> ### **NEEDS NARROWING.**

The substance is right and the sources support it: the same lab, one year apart, published a general
negative about Wwox and neuronal migration and then a positive prenatal migration defect in the same
strain, and `CLAIM 014` should carry that. Two corrections are required before it is committed:

- the 2019 endpoint was **not only bulk NeuN** — it included a layer-resolved NeuN count at PND21,
  and the boundary text must say so or it will misdescribe a source LEGEND has read in full;
- **"self-reversal" over-states it.** The proliferation limb is untouched and untested; the
  measurements are mutually compatible; the reversal is confined to the migration limb **as a stated
  conclusion**, across non-overlapping ages. Committing the audit's wording as it stands would put a
  **false contradiction** into the registry — the outcome the task warned against.

**Closing line — the exact wording change I would propose, as text, not as an edit:**

> Append to `CLAIM 014`'s existing evidence boundary, leaving `Status: consolidated baseline`, the
> title and the summary untouched: *"🔴 **Auto-restringimento dello stesso gruppo, a un anno di
> distanza.** PMID 31340538 conclude, in Discussione, che «**Wwox is not required for proliferation
> and migration of immature neurons**», sulla base di densità NeuN normale, espressione NeuN normale
> al western blot **e conta di neuroni NeuN⁺ per singolo strato corticale a PND21** — con gli strati
> delimitati «based on specific morphology of NeuN-positive cells», cioè dalla stessa
> citoarchitettura che costituisce il fenotipo. PMID 32581702 — **stessi investigatori (Tochigi primo
> autore del 2019 e terzo del 2020; Suzuki senior su entrambi), stesso ceppo `lde/lde`, stessa
> colonia** — conclude che «**Wwox deficiency impairs prenatal neuronal migration which is required
> for normal cortical layer formation at birth in rats**», con marcatori di identità laminare
> (densità Satb2 ridotta nello strato II e aumentata nella zona intermedia; distribuzione Tbr1
> invariata) e birth-dating BrdU a E16.5 letto a P1. ⚠️ **Non è una smentita delle misure, ed è una
> reversione di una sola delle due proposizioni:** il numero dei neuroni resta normale e il ramo
> «proliferation» non è mai stato testato da PMID 32581702 (nessun Ki67, nessuna conta totale;
> spessore della parete corticale non significativo, coerente col 2019); a essere rovesciato è il
> ramo «migration» **come conclusione non qualificata**. Le finestre temporali **non si sovrappongono**
> — PND5–21 contro E16.5→P1 — e il difetto è dichiarato «**delayed**». **Il numero dei neuroni era
> normale; la collocazione laminare no**: un endpoint che conta cellule dentro bande definite dalla
> morfologia NeuN non può vedere uno sfasamento di identità molecolare. Entrambi gli studi sono **non
> in cieco**, con t-test di Student senza correzione per confronti multipli e n = 3 per genotipo
> (PMID 31340538: soli maschi; PMID 32581702: entrambi i sessi). ⚠️ Le dimensioni d'effetto Satb2/BrdU
> risiedono nei pannelli di Figura 3 e **non sono verificabili con la strumentazione di questo
> deployment**; il testo del 2020 riporta il risultato BrdU come «altered distribution», senza numero.
> Il confine `BATCH_20260806_002` resta valido e invariato: PMID 31340538 continua a non contribuire
> al ramo prenatale di questa claim."*

---

## 4 · Summary

| Task | Audit verdict | This file | Decisive quote |
|---|---|---|---|
| **1** — `CLAIM 039`, *"not cerebellar"* | `BLIND` | **HOLDS** (and is understated) | *"we did not detect any marked pathologic changes in the cerebella of `lde/lde` rats"* — PMID 17803050, Discussion p. 8. **No quantitative motor test exists anywhere in the source.** Counter-evidence found in the same strain: *"the development of cerebellum was delayed in [`lde/lde`] as shown by reduced number of foliation"* — PMID 32581702 |
| **2** — `CLAIM 014`, migration boundary | reversal to be added | **NEEDS NARROWING** | *"Wwox is not required for proliferation and migration of immature neurons"* (PMID 31340538) versus *"Wwox deficiency impairs prenatal neuronal migration which is required for normal cortical layer formation at birth in rats"* (PMID 32581702). **Migration limb reversed as a conclusion; proliferation limb untested; measurements compatible; ages disjoint.** |

## 5 · What could not be obtained

| Item | Status | Why it matters |
|---|---|---|
| **PMID 17803050 full text, independently re-read** | 🔴 **Permanently unobtainable here.** No DOI, no PMCID, no PMC deposit (PubMed metadata, 2026-09-20; Europe PMC `inEPMC=N`, 2026-08-07). Task 1 rests on LEGEND's own 32-locator receipt, declared at every use | The only source of a canonical claim title cannot be re-opened by this deployment. Any future challenge to `CLAIM 039` must go through the operator's PDF |
| **Suzuki 2007 cerebellar histology: n, age, stain, section plane** | 🔴 **Unrecorded in all 32 locators, and uncloseable from here** | The exclusion's endpoint is not merely coarse — its sample size and age are **unknown to LEGEND**. That is a stronger statement than the audit made |
| **Figure 3 panels of PMID 32581702** — cerebellar arrowheads, Satb2 panel G, BrdU panel J | 🔴 **Unresolved.** No PDF tooling, no figure-image route. No panel was inspected and none is claimed | The rat's only cerebellar datum, and the effect sizes of Task 2's positive result, both sit in panels this session cannot open. For an audit about instrument sensitivity, **the missing instrument is the point** |
| Purkinje counts, cerebellar electrophysiology, DTI or quantitative gait analysis for the `lde` rat | **Confirmed absent from the corpus**, as the audit said | The anatomical substrate of the most penetrant phenotype in the model is genuinely unmeasured |
