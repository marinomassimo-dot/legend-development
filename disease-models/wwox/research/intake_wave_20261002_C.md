# Intake wave 2026-10-02 — Scientist C

**ACTOR_ID** `scientist-c` · **Branch** `task/sci-C-20261002` · **Date** 2026-10-02
`context_policy: SOURCE_FIRST` — for every record, acquisition state, identity and the assigned
question were the only things known before opening; the model's claims were opened only after the
first pass was written down, and each dossier says where that line falls.
**Assigned questions:** (1) dose and safety of *increasing* WWOX; (2) biomarkers that measure WWOX,
under LEGEND_CORE §13.

**Not medical advice.** Nothing below describes any individual; patients appear only at the level
of allele class × zygosity × phenotype band.

---

## 1 · The six records

| PMID | Short | Verdict | Receipt | Manifest |
|---|---|---|---|---|
| 42395553 | Petrozziello 2026, WWOX in Huntington's — **bioRxiv preprint, not peer reviewed** | **INGEST** (research layer only) | `FTR-20261002-42395553-01` | `PMID42395553.json` ✅ strict PASS, 0 gaps, 9 locators |
| 37781246 | Kałuzińska-Kołat 2023, GBM molecular landscapes | **INGEST** | `FTR-20261002-37781246-01` | `PMID37781246.json` ✅ 0 gaps, 4 locators |
| 34204789 | Kałuzińska 2021, PLEK2/RRM2/GCSH triad | **INGEST as a rejected candidate** | `FTR-20261002-34204789-01` | `PMID34204789.json` ✅ 0 gaps, 4 locators |
| 33195192 | Chou 2020, Wwox-null mouse skin / ERK | **INGEST** | `FTR-20261002-33195192-01` | `PMID33195192.json` ✅ 0 gaps, 4 locators |
| 37897534 | Cheng 2023, senescence escape | **INGEST** | `FTR-20261002-37897534-01` | `PMID37897534.json` ✅ 0 gaps, 2 locators |
| 17679088 | Zhang & Freudenreich 2007, FRA16D Flex1 in yeast | **OFF-AXIS for the stated hypothesis; INGEST as a mechanistic precedent + one lead** | `FTR-20261002-17679088-01` | `PMID17679088.json` ✅ 0 gaps, 5 locators |

**Dedup:** all six are NEW. `registry_records.py get --pmid` returned no record for any of them, and
`fulltext_receipts.py status --pmid` exited 1 with `[]` for all six — no prior receipt, so every
reading is `first_read`. **No retraction, correction or expression of concern** on any of the six
(PubMed article types; the two JATS hits for the string "retract" are both inside reference lists).
No patient or family overlap exists to check: only one record (42395553) has human subjects at all,
a post-mortem HD cohort unrelated to WWOX-DEE.

**Acquisition:** four came straight from Europe PMC `fullTextXML`. Two needed the `find-fulltext`
cascade and both were resolved; neither was deferred. Full digests and routes are in the dossiers
and manifests.

⚠️ **Independence.** These six are **four** independent groups, not six: 37781246 and 34204789 are
the same Lodz department (Bednarek), and 33195192 and 37897534 are the same Tainan laboratory and
the same knockout mouse line (Hsu). Recorded in each manifest's `group_assessment`.

---

## 2 · Question 1 — dose and safety

### What each source actually did, exactly

| Source | The intervention, precisely | Cells | Readout | Authors' conclusion | What they decline |
|---|---|---|---|---|---|
| 42395553 | **Recombinant human WWOX protein applied to the medium**, 1–500 ng/mL, 24/48 h | SH-SY5Y; **human ESC-derived cortical neurons, 65Q and isogenic 27Q** | MTT viability; γ-H2AX by ICC | *"maintaining appropriate WWOX levels may be important for cellular homeostasis"* | any therapeutic direction; any claim about HD causation |
| 42395553 | **Stable transgene** (PiggyBac EF1A>hWWOX-FLAG) | SH-SY5Y, RPE-1 — **not neurons** | γ-H2AX; CAG instability | raises γ-H2AX; **does not** alter repeat instability | that γ-H2AX equals double-strand breaks |
| 37781246 | **Lentiviral overexpression** | 4 GBM lines | proliferation (**carried from the prior paper**), CAGE-Seq | one line, DBTRG-05MG, proliferates *more* | that higher WWOX caused the worse patient outcome |
| 33195192 | none — **loss of function only** | mouse skin, HaCaT | — | *"A certain amount of WWOX expression may be necessary"* | — (the HT29 result is a citation, not their datum) |

### The answer

**Yes, three sources say that raising WWOX is not uniformly benign — and none of them transfers to
a neuron-targeted vector setting.** The strongest single datum, and the only one in neurons, is that
applied recombinant WWOX protein at 100 ng/mL reduced viability of human ESC-derived cortical
neurons **equally in the disease line and its isogenic control** (two-way ANOVA: treatment
F(1,28)=78.44, p<0.0001; **no interaction**, F=0.3129, p=0.5804). The transfer fails at four joints:

1. **Applied extracellular protein is not a transgene, and is not what a vector delivers.** WWOX is
   a ~46 kDa intracellular protein; by what route an applied preparation reaches the nucleus is
   neither measured nor discussed.
2. **The controls that would separate "WWOX" from "a commercial protein preparation" are absent** —
   no heat-denatured arm, no irrelevant-protein arm, no endotoxin assessment. An MTT fall at
   100–500 ng/mL of applied recombinant protein is exactly where that artefact lives.
3. **The transgene arms are not in neurons** — SH-SY5Y neuroblastoma and RPE-1 — and the only
   magnitude given anywhere is a Mann-Whitney statistic (U=1, p=0.0476).
4. **It is a preprint**, explicitly uncertified by peer review.

**Against the model's safety layer:** I compared only after writing the above. `CLAIM 011` and
`BLOCK 1 §4` reason about a **floor** — *"below 2.63 × 10¹¹ vg survival is not rescued at all"* —
and the corpus cross-query for any statement about *raising* WWOX returned **0 hits**.

🔴 **Does anything here bound a statement the model makes? Plainly: no.** No source has a vector, a
delivered dose, a neuron-targeted transgene or an in vivo endpoint, and Obeid 2026 reports ~80%
survival to 300 days at the high dose with no overexpression toxicity — a far stronger evidence
class. The model's dose positions stand unchanged.

**What this batch does establish is an absence, and the absence is worth writing down.** The corpus
has no ceiling datum and does not record that it has none. `CC-20261002-WWOX-DOSE-CEILING-01`
proposes exactly that — a `PREMISE_TAG` on `CLAIM 011` and one bullet in `BLOCK 1 §4` — written as
an open question and a revival trigger, never as a hazard.

⚠️ One adjacent observation: `PAPER 082` (Fabbri 2005, *"WWOX gene restoration prevents lung cancer
growth"*), which my dependency screen independently re-flagged through PMID 33195192's bibliography,
is one of the citations behind the general belief that restoring WWOX is benign — and it stands
under `PUBLICATION_INTEGRITY_HOLD`. The model already records this correctly: scope narrow (one
β-actin panel), not a retraction, linked to no claim. It changes nothing; it is a reason not to
treat that belief as more heavily evidenced than it is.

**What would change the model if true:** a neuron-targeted vector arm above the Obeid high dose with
a toxicity endpoint. **What would falsify this batch's contribution:** a heat-denatured-rWWOX control
reproducing the neuronal viability loss.

---

## 3 · Question 2 — biomarkers that measure WWOX

Eight candidate readouts across four sources. **All eight fail §13**, and the scoring, the premises
and the revival triggers are in `CC-20261002-BIOMARKER-REJECTIONS-01` (proposed entries DIS-026 to
DIS-029 — renumbered from 022–025 on 2026-10-02 to yield to Scientist A's
`CC-20261002-DOSE-GAIN-DISMISSAL-01`, which claimed the same four numbers first and is cited by
`CC-20261002-INTAKE-A-REGISTRY-01`; this candidate's numbers had no downstream citation, so it is
the cheaper side to move). The summary:

| Candidate | Dependence shown by | System | Type | Patient-samplable | §13 |
|---|---|---|---|---|---|
| PLEK2, RRM2, GCSH | **no perturbation at all** — expression cut-point + Spearman ρ | bulk TCGA glioma | transcript | tumour tissue only | ❌ not a biomarker, not an endpoint |
| pERK Thr202/Tyr204 | constitutive knockout vs littermates | mouse epidermis, IHC | phospho-protein | **skin biopsy yes**, brain no | ❌ fails specificity; retained as a possible *pharmacodynamic* readout |
| γ-H2AX | knockout, knockdown, overexpression, applied protein | MEFs, HEK293T, SH-SY5Y, RPE-1 | phospho-protein | no | ❌ **non-monotonic** |
| SA-β-gal, p16/p21/p27, MSI | knockout + knockdown | fibroblasts | mixed | no | ❌ generic / culture artefact |

### The two findings worth carrying

🔴 **"WWOX-dependent" in PMID 34204789 means a rank correlation, not a perturbation.** No knockdown,
no overexpression, no protein measurement appears anywhere in that study; patients were split on a
WWOX expression cut-point of 222.6 and genes ranked by Spearman ρ (|R| 0.42–0.44). Every reported
AUC discriminates a tumour grade, never a WWOX state. The authors themselves say the triad's
usefulness *"is yet to be confirmed"*. This is written as a **rejected candidate with its reason**
so that the next session does not re-triage it hopefully from the title.

🔴 **γ-H2AX is non-monotonic in WWOX, and no single paper in the batch could show that.** It rises
when WWOX is lost (Cheng 2023) and rises when WWOX is added (Petrozziello 2026). Neither cites the
other. A readout that moves the same way under opposite perturbations cannot report the direction
of the quantity it measures — which disqualifies it independently of tier. **This is the batch's
one genuinely emergent result**, and it exists only because the two papers were read against each
other.

---

## 4 · The yeast paper — an earned null, and one lead

**PMID 17679088 does not support the hypothesis it was assigned for, and the gap is not the species.**
The brief offered it as a mechanistic basis for exon-scale **germline** deletions in WWOX-DEE. Every
measurement in it is **somatic**, mitotic, in *S. cerevisiae*, often in `rad52Δ`/`rad50Δ` backgrounds
with hydroxyurea, and the authors' own prediction terminates in *"cancer-causing rearrangements"*.
"WWOX" occurs **9 times in 189,143 bytes**; no WWOX protein, transcript or function is measured.

What transfers is a **mechanistic precedent** — FRA16D carries a characterised, specific
replication-barrier element (Flex1; Flex4 and Flex5-p do **not** increase fragility) — and that is
a real, non-trivial reason this locus is rearrangement-prone at all. What does not transfer is any
statement about why a particular allele class is deleted.

🔴 **And the paper never states which WWOX intron or exon Flex1 lies in.** That is the fact the
hypothesis would turn on, and it is absent from the body.

### LEAD-C1 — Flex1 AT-repeat length as a candidate genomic covariate · `IPOTESI`

- **Causal statement:** the Flex1 perfect AT repeat is polymorphic in the general population
  (*"97% heterozygosity … alleles varying between 11–88 AT repeats, and alleles of 34 repeats or
  greater are quite common"*), longer alleles stall replication forks more strongly in yeast, and the
  authors predict longer alleles *"could predispose to cancer-causing rearrangements in the FRA16D
  region"*. **If** that extends to the germline, Flex1 length would be a modifier of the probability
  that a WWOX deletion arises — **genotypable from blood DNA**.
- **§13:** **neither biomarker nor endpoint.** It is a constitutional sequence feature, not a measure
  of WWOX function. Deliberately not entered in the biomarker ledger in either direction.
- **Counter-evidence, from the source itself:** *"Although a relationship between AT length and
  fragility could not be documented in the Finnis et al. study, a comparison of fragility rates of
  the different alleles in our assay suggests that the effect may be subtle."* And the (AT)34 allele's
  own breakage rate **could not be measured**, because the structure appears to block the assay's
  recovery step — the authors say so.
- **Falsifier:** Flex1 AT-repeat lengths in WWOX deletion carriers and parents showing no shift
  against population controls.
- **Blocking acquisition:** **Finnis et al. 2005** — it holds both the allele distribution and the
  position of Flex1 within WWOX. Queued, not read. Nothing may be asserted about whether Flex1 falls
  inside or near the intervals deleted in WWOX-DEE allele classes until it is.

### LEAD-C2 — NAC rescue in a Wwox-null system · `IPOTESI`

N-acetyl-L-cysteine prevented microsatellite instability and restored senescence induction in
late-passage `Wwox−/−` MEFs (PMID 37897534). Adjacent to `CLAIM 009` (redox, *in observation*) and
`CLAIM 034` (counter-direction); **resolves neither**, because it is a fibroblast-culture result
with no neural and no in vivo arm. **Not promoted, and no commit candidate touches it.** Falsifier:
a neural or in vivo Wwox-deficient system where NAC does not move the phenotype.

---

## 5 · Where each paper stops saying anything about WWOX

| PMID | Stops at |
|---|---|
| 42395553 | WWOX is central, but every WWOX reagent is bought in and the group's whole WWOX output is this preprint |
| 37781246 | At causation — every patient-level statement is an association, and the authors say so |
| 34204789 | At perturbation — WWOX is a stratifying variable, never a manipulated one |
| 33195192 | At the brain — keratinocytes, hair follicles, dermis and fat; no neural tissue |
| 37897534 | At the brain, and at *in vivo* — MEFs, HEK293T and dermal fibroblasts only |
| 17679088 | **At the gene.** It is a paper about a DNA sequence; WWOX is the name of what the sequence sits in |

---

## 6 · Anything in the brief that was wrong

- The brief expected the bioRxiv **HTML** route to work and the PDF to be blocked. **The reverse was
  true**: `.full` and `.source.xml` returned Cloudflare 429 persistently, and `.full.pdf` returned a
  valid 39-page PDF. Worth correcting in `find-fulltext`'s bioRxiv note.
- The brief allowed `DEFER` for both hard acquisitions. **Neither was deferred**; both resolved.
- For PMID 17679088 the brief's framing ("candidate mechanistic basis for why exon-scale deletions
  are so prominent") presumes a germline reading the paper does not support. Noted, not followed.
- ⚠️ A method note for the next reader: the PMC reader HTML for PMC2144737 served a reCAPTCHA page on
  one request and the full article on a later one, **same URL, same session**. A single refusal is
  not evidence that a paper is unavailable.
- ⚠️ A measurement-hygiene note: `pdftotext -layout` alone emits U+000C page breaks, which
  `deepdive_manifest.py` correctly refuses as an unverifiable text surface; `-nopgbrk` re-derives it
  cleanly. The same derivation renders **γ as a Latin `g`**, which every quote from it must carry.

## 7 · Gates, and the one suite that is red

| Gate | Result |
|---|---|
| `legend_lint.py .` | exit 0, **0** `BLOCK_BATCH_COMMIT` / `BLOCK_SYSTEM` |
| `fulltext_receipts.py verify` | exit 0 — `OK: 267 chained receipt(s), tail anchored` |
| `growth_anchors.py check` | exit 0 — **PASS**; backlog 5 → 7, which is this wave's two candidates and is expected |
| `scripts/public_release_gate.py` | exit 0 — **VERDICT: PASS**, 0 `[BLOCK]`, and **0** `[REVIEW]` lines touching any file of this wave |
| `test_section_references.py` · `test_link_targets.py` · `test_fresh_clone_reader_journey.py` · `test_pathograph.py` | all exit 0, OK |
| `candidate_tree_freshness.py` | exit 0 — **VERDICT: FRESH** |
| `pathograph.py --verify` | **CURRENT** after regeneration with the generator |
| `scripts/run_release_regressions.py` | **exit 1 — one suite red:** `test_manifest_receipt_provenance.py` |

### The red suite, diagnosed to its cause

`test_the_declared_ceiling_is_the_measured_count` asserts `BASELINE_DEFECTS == 15` and measured
**21**. The six extra are exactly this wave's six manifests, all class **`UNKNOWN_EVENT`** — *"the
declared receipt is not in the ledger"*.

🟢 **That is the brief's own instruction, not a defect in the work.** The receipts are prepared and
deliberately **not** recorded, because the ledger is hash-chained and three scientists are writing
in parallel; the Orchestrator trial-records them in a scratch clone and appends them in event-ID
order. Between landing and that append, the suite must read 21.

**It closes on append, and that was verified rather than assumed** — the six pending receipts were
loaded alongside the live 267-event ledger and the module's own `assess()` re-run over every
manifest:

```
BEFORE append  total defects = 21 (ceiling 15) | my six: all UNKNOWN_EVENT
AFTER  append  total defects = 15 (ceiling 15) | my six: all CONFORMS
```

🔴 **One repair this check forced, and it would have been a silent defect.** The receipt JSONs
originally carried no `outputs` field. Appending them in that shape would have moved the six from
`UNKNOWN_EVENT` to **`UNCHECKABLE`** — *"no same-study event names this manifest among its
outputs"* — which is not a defect class the ceiling counts and would therefore have passed the
suite while leaving six manifests permanently unattributable. Each receipt now names its manifest,
its dossier and this note in `outputs`, which is what makes the simulated result `CONFORMS`.

**The ceiling was not raised.** The module says *"re-measure and lower it when the tail is repaired
— never raise it"*, and the 15 pre-existing defects (13 `NOT_THE_PRODUCER`, 2 `UNNAMED`) are
untouched by this wave.

**Action for the Orchestrator:** append the six `sciC_<pmid>_1.json` receipts, then re-run
`python3 framework/scripts/test_manifest_receipt_provenance.py` and expect exit 0.

## 8 · Candidates produced

| ID | Class | Targets | Triples |
|---|---|---|---|
| `CC-20261002-WWOX-DOSE-CEILING-01` | **MINOR** | `CLAIM 011` (append a `PREMISE_TAG`), `BLOCK 1 §4` (append one bullet) | 13 |
| `CC-20261002-BIOMARKER-REJECTIONS-01` | **MINOR** | `dismissal_ledger_current.md` (append DIS-026 … DIS-029) | 9 |

⚠️ **Numbering collision, resolved in this actor's own work rather than left for the integrator.**
Scientist A's `CC-20261002-DOSE-GAIN-DISMISSAL-01` proposes `DIS-022`–`DIS-025` in the same file and
in the same wave, and A's `CC-20261002-INTAKE-A-REGISTRY-01` already cites three of those ids in
`PAPER` records. This candidate's ids were cited by nothing, so it is the cheaper side to move and
it moved: **`DIS-022`–`DIS-025` → `DIS-026`–`DIS-029`.** Both candidates anchor their insert on
`DIS-020`'s last line; whichever lands second appends after the other's block, and neither op
depends on being first.

Neither narrows nor reverses a `consolidated baseline` claim. No canonical scientific current file
is edited by the second candidate at all.
