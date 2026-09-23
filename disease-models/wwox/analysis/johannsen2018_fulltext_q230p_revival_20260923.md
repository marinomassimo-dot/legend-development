# `Q230P` REVIVAL — Johannsen 2018 (PMID 29808465) read at full-body depth

> **Discovery-space artefact.** `HYPOTHESIS ≠ CLAIM`. Nothing here is canonical; nothing is propagated.
> **Not medical advice.** Reasons about a reference WWOX-DEE genotype class, not about any person.
> **Public edition.** Bibliographic metadata retrieved from **PubMed**.
> Scores the predictions persisted in
> [`PREREG_johannsen2018_methods_20260922.md`](PREREG_johannsen2018_methods_20260922.md) §3,
> **using their persisted wording**, against the primary source acquired by the Operator on 2026-09-23.

---

## 0 · The revival trigger fired

`PREREG_johannsen2018_methods_20260922.md` §5.5 named one action: *"obtain Johannsen et al. 2018,
Neurogenetics 19(3):151–156, `doi:10.1007/s10048-018-0549-5`, and read **Methods**."* The Operator
supplied the publisher PDF. **The trigger is `HUMAN_REQUIRED` → discharged.**

**Identity verified two ways**, and they agree:

| Field | From the PDF itself | From PubMed |
|---|---|---|
| Authors | Jessika Johannsen, Fanny Kortüm, Georg Rosenberger, Kristin Bokelmann, Markus A. Schirmer, Jonas Denecke, René Santer | identical |
| Journal / citation | `Neurogenetics (2018) 19:151–156` | `Neurogenetics` 19(3):151-156 |
| DOI | `https://doi.org/10.1007/s10048-018-0549-5` | `10.1007/s10048-018-0549-5` |
| Received / accepted / online | 31 March 2018 / 17 May 2018 / 28 May 2018 | 2018-05-28 |

🟢 **No duplicate identity created.** One study, one artefact
(`files/fulltext/PMID29808465_Johannsen2018.pdf`, `sha256 0b2bce6f…8e49`).

🔴 **Extraction-instrument note, recorded because it nearly produced a false negative.** A first
search for the antibody catalogue number `sc-20528` returned **0**. The paper prints it as
**`sc20,528`** — the typesetter inserted a thousands comma into a catalogue number. The zero was an
instrument reading, not a finding. Positive controls (`WWOX` 72, `epileptic` 8) had already passed,
which is the only reason the zero was interrogated instead of quoted.

---

## 1 · THE FIVE PREREGISTERED PREDICTIONS, SCORED

Scoring rule fixed ex ante in `PREREG` §4: `SUPPORTED` / `REFUTED` / `AMBIGUOUS` / `UNTESTED`,
resolved **against each prediction's own stated falsifier**.

| # | Prediction (persisted wording) | Falsifier (persisted wording) | Score |
|---|---|---|---|
| **P1** | *"**No pellet / insoluble-fraction analysis** is reported. The post-spin pellet is discarded unexamined."* | *"Any resuspension, denaturing re-solubilisation or pellet blot is described."* | 🟢 **SUPPORTED** |
| **P2** | *"The lysis buffer is either **unnamed**, or named **without full detergent composition**; no SDS/urea/guanidine denaturing recovery step appears."* | *"A complete recipe with a strong denaturant is stated."* | 🟢 **SUPPORTED** |
| **P3** | *"The **immunoblot detection floor is not quantified** — no dilution series, no recombinant standard, no stated LOD."* | *"Any explicit sensitivity limit is reported."* | 🟢 **SUPPORTED** |
| **P4** | *"**No measurement of synthesis rate** — no pulse-label, no puromycin, no polysome fractionation. So 'impaired translation' is offered as an alternative the paper **did not test**."* | *"Any synthesis-rate measurement is present."* | 🟢 **SUPPORTED** |
| **P5** | *"The antibody is identified by **vendor at most**, with its **epitope region not stated**."* | *"The epitope or immunogen region is given."* | 🟡 **SUPPORTED on the falsifier — first clause over-performed** |

**5 / 5 falsifiers unmet. None dropped, none retrofitted.**

### 1.1 · The evidence behind each score, verbatim

**P1 · P2 — the whole lysis passage, quoted in full** (Methods, *"Biomaterial sampling for WWOX
expression analyses"*):

> *"The other pellet was resuspended in 100 μl ice-cold RIPA buffer supplemented with protease
> inhibitors and sonicated three times on ice. Upon 10 min centrifugation with 13.000 rpm at 4 °C,
> **the supernatant containing cellular proteins was collected.** An aliquot was used for
> quantification of total protein according to Bradford assay and the remaining material stored at
> −80 °C."*

- **P1:** the sentence ends at the supernatant. There is **no** resuspension of the post-spin pellet,
  **no** denaturing re-solubilisation, **no** pellet lane. 🔴 **The insoluble fraction was never
  loaded onto a gel.**
- **P2:** the buffer is **named and not specified** — no detergent identities, no percentages, no
  salt, no pH, no denaturant anywhere in the paper. This is a textbook instance of the rule this
  repository already recorded on 2026-09-23 (`5092de2`, *"A buffer named RIPA is not RIPA"*): the
  word `RIPA` covers formulations that differ by orders of magnitude in what they extract.
- ⚠️ **A misreading to avoid.** The same passage says the cells were *"divided in two fractions after
  centrifugation."* Those two fractions are **RNA vs protein**, not soluble vs insoluble. Read
  quickly, that phrase looks like fractionation evidence. It is not.

**P3 — no floor.** The blot is *"20–40 μg per sample on a 12% polyacrylamide gel"*, PVDF, ECL
(`Luminata Forte`), `ImageQuant LAS 4000 Mini`. Term census on the verified text layer:
`detection limit` **0**, `limit of detection` **0**, `sensitiv*` **1** (a reference title).
🟡 **The paper does hold a true negative control** — *"Three WWOX knock-out clones of PaTu-8988t …
catalogue number `sc-403070`"* — which establishes **specificity** of the ~46 kDa band. 🔴 **It does
not establish sensitivity.** A KO lane says the band is WWOX; it says nothing about how little WWOX
would still be seen.

**P4 — no synthesis measurement of any kind.** Census on the verified text layer:
`actinomycin` **0** · `cycloheximide` **0** · `MG132` **0** · `proteasom*` **0** · `half-life` **0** ·
`pulse` **0** · `puromycin` **0** · `polysome` **0** · `stabilit*` **0**.
The paper's own framing concedes the point: *"Transcription and translation were assessed by
quantitative real-time PCR and Western blotting"* — i.e. **translation was "assessed" via
steady-state protein**, which is the thing to be explained, not a measurement of synthesis.

**P5 — the nuance, recorded rather than smoothed.** The paper gives **more** than the prediction
allowed on identification, and **exactly** what it predicted on epitope:

> *"primary antibodies against WWOX (Santa Cruz Ref# `sc20,528`, Dallas, TX, USA) diluted 1:200 in
> TBST containing 5% (w/v) BSA or against actin (Acris, Chapel Hill, NC, USA) diluted 1:4000"*
> … secondary *"1:30,000 anti-goat IgG HRP or anti-rabbit IgG HRP"*.

A **catalogue number** is present (`sc-20528`), which P5's first clause did not expect — and a
catalogue number is *operationally better* than a prose epitope, because it can be looked up.
🔴 **But no immunogen, no epitope region, no clone, no aa range appears anywhere in the paper**, so
the stated falsifier is unmet. Scored `SUPPORTED`, with the over-performance declared rather than
hidden — which is the whole point of having written the falsifier down first.

🎯 **`DET-1` gains a name.** `q230p_true_frontier_20260922.md` row `DET-1` reads *"Which antibody
produced `Q230P`'s founding blot … `NOT ATTRIBUTABLE`. No vendor, no catalogue, no clone, no host,
no immunogen."* **Vendor, catalogue and host are now known** (Santa Cruz `sc-20528`, **goat** —
inferred from the anti-goat secondary, stated by the paper). The epitope remains unknown.
`DET-1` moves `NOT ATTRIBUTABLE` → **`ATTRIBUTED, EPITOPE UNKNOWN`**.

### 1.2 · The pre-stated consequence fires

`PREREG` §4, written before the source existed:

> *"**If P1 ∧ P2 hold:** *protein not detected* **cannot discriminate H3 from H4** in this source.
> The canonical `MOLECULAR FATE UNRESOLVED` is then not merely cautious but **exactly right**, and it
> cannot be narrowed from this paper at all."*

**P1 and P2 both hold.** 🟢 **`MOLECULAR FATE UNRESOLVED` is confirmed as the correct canonical
status, on the paper's own method, and the confirmation was pre-committed and is therefore not a
retrofit.** This is the intended output of `preregister_prediction` and the first time in this
repository that a prediction set has been scored against a source that did not exist when it was
written.

---

## 2 · TWO INFERENCES THE PRE-REGISTRATION ITSELF MADE, NOW **REFUTED** BY THE SOURCE

`PREREG` §5.3 graded two indexer-assigned MeSH terms as `NEW DETAIL` and drew consequences from
them. The full text refutes both. Recording this is the obligation §4's scoring rule creates.

| MeSH term | What `PREREG` §5.3 inferred | What the paper shows | Verdict |
|---|---|---|---|
| **`HEK293 Cells`** | *"implies a **heterologous expression arm** — a second, independent measurement of `Q230P` protein in a non-patient context … it may be where a residual band would be visible if one exists anywhere"* | Fig. 3c legend: *"Model cell lines for pancreatic (PaTu-8988t) and colon (SW620) cancer **as well as HEK293 were employed as positive controls for WWOX protein expression**."* | 🔴 **REFUTED.** HEK293 is a **positive control for endogenous wild-type WWOX**. There is **no transfection, no construct, no `Q230P` expressed in any heterologous cell**. The word `transfect` does not occur |
| **`RNA Stability`** | *"implies transcript stability was assessed **as such**, not merely level — a finer measurement than 'qRT-PCR normal'"* | `stabilit*` = **0** in the full text. No actinomycin-D chase, no decay curve, no half-life | 🔴 **REFUTED.** The paper measured transcript **amount and length**. Nothing was measured about RNA **stability** |

🎯 **The transferable rule, and it is sharper than the one `PREREG` §5.3 wrote for itself.** That
section correctly bounded MeSH as *"indexer-assigned … a pointer, not a datum."* The bound was right
and the practice still went wrong: having written the caveat, it then reasoned **from** the pointer
for two paragraphs and graded the result `NEW DETAIL`. 🔴 **A caveat attached to an inference does
not weaken the inference; only refusing to draw it does.** Both MeSH-derived leads were wrong in the
same direction — both invented an *experiment* out of an *index term*.

🔴 **Consequence for `q230p_true_frontier_20260922.md` row `RNA-2`**, which currently reads
*"Has `Q230P` mRNA stability/decay been measured? **Unknown — and an experiment may exist** …
MeSH `RNA Stability` present."* → **`RESOLVED — answered in the negative`. No such experiment
exists. The row is no longer `SOURCE-DEPTH LIMITED`; it is closed.**

---

## 3 · 🎯 THE FINDING THE PRE-REGISTRATION DID NOT ANTICIPATE — the qRT-PCR is blind to exon 7

This was not predicted, was not looked for, and is the most consequential thing in the paper.

**The paper's own primer design** (Methods, *"Quantification of WWOX transcription"*):

> *"Transcription of WWOX was ascertained for the core (**exons 4–6**) and the 3′ region (**exons
> 8–9**). This was done to ensure complete WWOX transcription as exon 9 is located about 730 kbp
> distant from exon 8. Two primer pairs were designed according to PrimerBank … spanning either
> **exon 4–6** (forward 5′-CCAACCACCCGGCAAAGATA-3′, reverse 5′-AATGCTGCACGCTACGGAG-3′) or **exon
> 8–9** (forward 5′-ATGTACTCCAACATTCATCGCAG-3′, reverse 5′-GTCTCTTCGCTCTGAGCTTCT-3′) of the major
> WWOX transcript (`NM_016373.2`)."*

Amplicon lengths confirmed on gel (Fig. 3a): **277 bp** (core) and **200 bp** (3′).

**Now place the variant.** `q230p_structural_mechanism_20260922.md` §0.1 and
`missense_splice_reclassification_risk_20260921.md` §81 give the repository's exon map:

```
exon 6  c.517–c.605     exon 7  c.606–B     exon 8  c.B+1–1056     (754 ≤ B ≤ 843)
```

`Q230P` is **`c.689A>C`, in exon 7**.

> 🔴 **Neither amplicon contains exon 7.** The core assay stops at the end of exon 6 (`c.605`); the
> 3′ assay starts at the beginning of exon 8 (`≥ c.755`). **The two amplicons bracket the exon that
> carries the variant, and cover none of it.**

**Therefore — and this is `INFERENZA`, drawn from the paper's stated primer design plus the
repository's own exon map, not from any new measurement:**

- *"Normal levels of WWOX transcripts"* is established **for exons 4–6 and 8–9**. It is **not**
  established for exon 7.
- *"Normal … **length** of WWOX transcripts"* (Discussion) rests on two gel bands, **277 bp** and
  **200 bp**, neither of which spans exon 7. 🔴 **An exon-7 skipping event would leave both bands at
  exactly their expected size.** The length control is blind to it by construction.
- This is **precisely the failure mode `q230p_true_frontier` row `RNA-1` named in advance** as its
  remaining uncertainty: *"qPCR amplicon position `UNSTATED` — a single amplicon outside a skipped
  region returns 'normal transcript' and is blind."* 🎯 **The position is now STATED, and the
  blindness is confirmed rather than excluded.**

🟡 **What this does and does not license.**
- ✅ It **removes** `RNA-1` from `SOURCE-DEPTH LIMITED` — the amplicon geometry is known.
- ✅ It **keeps `RNA-4` (exon-7 `ESE` disruption → exon-7 skipping) fully open**, and shows the one
  published RNA experiment on this allele **could not have detected it**.
- ❌ It is **not** evidence that exon 7 *is* skipped. No one has looked. Splice-**site** disruption
  was already excluded on distance grounds (66–84 nt from any junction); `ESE`/`ESS` disruption was
  never assessed, and remains unassessed.
- ❌ It does **not** overturn `CLAIM 019`. The claim says transcripts are present at normal levels;
  that is what was measured. What changes is the **scope** the claim may be read at.

---

## 4 · WHAT JOHANNSEN NOW ESTABLISHES, AND WHAT IT STILL DOES NOT

### 4.1 · Established (all `DATO`, all first-hand from the full text)

| | |
|---|---|
| **Cell system** | Dermal fibroblasts from a **forearm punch biopsy of patient 2**, DMEM + 10% FCS, harvested by trypsinisation at confluency, within **five passages**, at **two independent time points** |
| **Genotype** | Homozygous `c.689A>C` / `p.Gln230Pro` in two girls, **cousins from two related consanguineous families**; both parents heterozygous carriers; REVEL **0.729**, CADD **23.1**, M-CAP **0.059** (*"possibly pathogenic"*) |
| **Transcript** | Detectable, **expected length**, at *"almost identical transcript level"* vs three reference lines, for **exons 4–6** and **exons 8–9**, normalised to `HPRT1` + `UBC`, referenced to PaTu-8988t = 100%. `−RT` controls clean ⇒ no gDNA carry-over |
| **Protein** | *"Western blotting, however, did not elicit any detectable WWOX protein in the fibroblast line of the index patient."* Replicated on a **second harvest several days later** |
| **Controls** | 🟢 **Positive:** PaTu-8988t, SW620, **HEK293** — all endogenous wild-type WWOX. 🟢 **Negative:** three CRISPR/Cas9 `WWOX` knock-out PaTu-8988t clones (`sc-403070`) |
| **Reagents** | anti-WWOX **Santa Cruz `sc-20528`, 1:200** (goat; anti-goat HRP secondary) · anti-actin **Acris 1:4000** · 12% SDS-PAGE, 20–40 μg · PVDF 0.45 μm · ECL Luminata Forte · ImageQuant LAS 4000 Mini · bands at **WWOX ~46 kDa, actin ~42 kDa** |
| **Author interpretation** | *"These results may point towards an impaired protein translation or, **more likely, premature degradation of the misfolded protein after transcription due to quality control mechanisms in the endoplasmic reticulum (ER)**"* |

### 4.2 · NOT established — and the list is longer than the abstract suggests

🔴 The paper does **not** measure, anywhere: translation rate · cotranslational disposal · protein
half-life · proteasomal degradation · lysosomal or autophagic degradation · **ERAD or any ER
process** · insoluble sequestration · aggregation · nascent-chain labelling · transcript
**stability** · exon-7 inclusion · a detection floor · an antibody epitope.

🎯 **One author inference deserves its own line, because it is mechanistically specific and carries
zero measurement.** The Discussion attributes the loss to **ER quality control**, and repeats it in
the conclusion (*"the complete elimination of proteins, e.g., by ER quality control mechanisms"*).
**No ER experiment was performed** — no ER marker, no ERAD inhibitor, no glycosylation, no
fractionation. The citation offered is a general review, not a WWOX result. 🔴 **`AUTHOR
INTERPRETATION ≠ MEASURED MECHANISM`, and here the interpretation is not merely unmeasured but
unusually specific** — it names a compartment and a pathway. The repository should carry the
authors' disjunction *(impaired translation | premature degradation)* as the authors' own, and
should **not** inherit the ER attribution at any strength.

### 4.3 · Two internal inconsistencies in the source, recorded so they are not propagated

1. 🔴 **The paper mis-states its own variant once.** Discussion: *"homozygosity for the missense
   variant `c.689A>C` predicting a change of **glycine** 230 into proline."* The abstract, Results
   and Fig. 3 all say **`Gln230`** (glutamine), and `c.689A>C` in a `CAA/CAG` codon gives
   Gln→Pro. **`Gln230Pro` is correct; "glycine 230" is a typographical error in the source.**
2. 🟡 **Two different total-protein assays are named.** Methods §*Biomaterial sampling* says
   **Bradford**; Methods §*Assessment of WWOX protein* says **bicinchoninic acid (BCA)**. Both
   appear; the paper does not reconcile them. Low consequence, but it is the number that sets the
   20–40 μg load, so it is recorded.
3. 🟡 **"Patient 2" vs "the index patient."** Methods say fibroblasts came from **patient 2**;
   Fig. 3 legend and Results say *"the index patient."* Same cells; inconsistent label.

---

## 5 · UPDATED MOLECULAR-FATE FRONTIER

Assessed strictly against what this source can and cannot see. **No winner is forced.**

> 🔴 **AMENDED 2026-09-23 — `H1` is split, because one label was doing two jobs.** The original row read
> *"H1 reduced RNA — REFUTED within the measured window"*. That is too coarse: it bundles a question about
> **abundance** (answered) with a question about **architecture** (never asked). A reader carrying the
> single label forward would take "RNA is fine" from a measurement that never looked at the exon the
> variant is in. The two are now separate hypotheses with separate statuses.

| | Hypothesis | Status after the full text | Why |
|---|---|---|---|
| **H1a** | **Reduced abundance of the ASSAYED WWOX transcript regions** (exons 4–6, exons 8–9) | 🟢 **REFUTED in patient-2 fibroblasts under this assay** | Both regions *"expressed to a similar extent"* and at *"almost identical transcript level"* vs three reference lines, normalised to `HPRT1`+`UBC`, with clean `−RT`. 🔴 Scope: **one cell type, one donor, duplicate wells, no statistical test reported** |
| **H1b** ⭐ | **Abnormal transcript architecture involving EXON 7** | 🔴 **UNTESTED** | `c.689A>C` is in exon 7. The core amplicon ends at exon 6 (`c.605`); the 3′ amplicon begins at exon 8. **Neither interrogates exon 7**, and an exon-7 event would leave both gel bands at expected size. 🔴 **This does NOT license inferring exon-7 skipping — and equally does NOT license inferring a normal exon-7 junction. Both are unknown.** A newly *sharpened* experimental gap, not a new suspicion |
| **H2** | Impaired translation / nascent production | 🔴 **UNTESTED** | Author-offered; `P4` confirms zero synthesis measurement |
| **H3** | Cotranslational / immediate post-translational disposal | 🔴 **UNTESTED** | No chase, no inhibitor, no nascent label |
| **H4** | Rapid degradation after synthesis | 🔴 **UNTESTED — and author-*preferred*, which is not evidence** | No `MG132`, no `CHX`, no bafilomycin, no `t½` |
| **H5** | Insoluble sequestration | 🔴 **NOT EXCLUDED — and structurally un-interrogable from this source** | `P1`: the pellet was discarded. 🎯 **This is the only hypothesis the method could not have seen even in principle** |
| **H6** | Detection artefact / mixed state | 🔴 **NOT EXCLUDED** | `P3`: no floor, so *"not detected"* has no magnitude. `P5`: unknown epitope, so a fold-dependent epitope loss in the SDR domain — where residue 230 sits — is unexcluded |

**Net movement, restated after the split: the branch count did not fall — it was re-partitioned.**
Before today, `H1`–`H6` were six live branches resting on an abstract. After today there are **seven**
(`H1a`, `H1b`, `H2`–`H6`), of which exactly **one — `H1a` — is retired**, and its retirement is scoped to
one assay, one cell type and one donor. `H5` and `H6` are shown to be *specifically enabled by two named
method gaps*; `H1b` is newly *visible* rather than newly *open* — it was always open and was previously
hidden inside a label that implied it had been answered.

🔴 **`MOLECULAR FATE UNRESOLVED` stands**, and the honest summary is narrower than "one of six refuted":
**the only thing measured about this allele's RNA is the abundance of two regions that exclude the exon
carrying the variant.**

### 5.0 · The reconstructed post-Johannsen fate model, one line per layer

| Layer | Status after the full text |
|---|---|
| **RNA abundance** (assayed regions) | 🟢 **Narrowed substantially** — comparable to three control lines on both amplicons |
| **RNA architecture** (exon 7) | 🔴 **Unresolved — and never interrogated** |
| **Protein production / translation rate** | 🔴 **Unresolved** — not measured, offered by the authors as an alternative they did not test |
| **Soluble protein** | 🟢 **Measured: undetectable under Johannsen's RIPA-supernatant conditions**, replicated at two harvests |
| **Insoluble protein** | 🔴 **Not examined** — the pellet was discarded. The one branch the method could not see even in principle |
| **Post-synthetic turnover** | 🔴 **Not measured** — no chase, no inhibitor, no `t½` |
| **Cotranslational loss** | 🔴 **Not measured** |
| **Detection artefact** | 🔴 **Not excluded** — no quantified floor, unknown epitope |
| **Function** | 🔴 **Not measurable until a protein population can be established.** A function assay with no detectable substrate measures the assay |

🔴 **No winner is chosen, and none is available.**

### 5.1 · Row-level deltas owed to `q230p_true_frontier_20260922.md`

| Row | Was | Becomes | Driver |
|---|---|---|---|
| `RNA-1` | `SOURCE-DEPTH LIMITED` (amplicon position unstated) | 🟢 **RESOLVED for `H1a`, with a declared scope limit** — positions known; **exon 7 uncovered** | §3 |
| `RNA-1b` 🆕 | *(did not exist — was hidden inside `RNA-1`)* | 🔴 **OPEN: exon-7 architecture, `UNTESTED`** — see `H1b` | §3, §5 |
| `RNA-2` | `SOURCE-DEPTH LIMITED` (MeSH suggests a decay chase) | 🟢 **RESOLVED — negative. No stability experiment exists** | §2 |
| `RNA-4` | `EXPERIMENT PROPOSED BUT UNRUN` | 🔴 **UNCHANGED, and now shown un-addressable by the existing data** | §3 |
| `SOL-1` | `HUMAN_REQUIRED` — eleven targets `METHODS_INVISIBLE` | 🟢 **DISCHARGED** — buffer, spin, pellet handling, antibody, load, detection all now quoted | §1.1, §4.1 |
| `SOL-2` | `SOURCE-DEPTH LIMITED` | 🟢 **RESOLVED** — *"not detected"* means **not detected in the RIPA-soluble supernatant**, explicitly | §1.1 |
| `SOL-3` ⭐ | `EXPERIMENT PROPOSED BUT UNRUN` | 🔴 **UNCHANGED — and now positively confirmed that nobody looked** | `P1` |
| `DET-1` ⭐ | `NOT ATTRIBUTABLE` | 🟡 **ATTRIBUTED, EPITOPE UNKNOWN** — Santa Cruz `sc-20528`, goat, 1:200 | `P5` |
| `DET-4` | `EXPERIMENT PROPOSED BUT UNRUN` (no floor anywhere) | 🔴 **UNCHANGED, confirmed at source** | `P3` |
| `PROD-1` | `TRUE EXPERIMENTAL GAP` | 🔴 **UNCHANGED, confirmed at source** | `P4` |

🔴 **A `HEK293` correction is owed to `SOL-1`**, whose extraction list included *"whether the
MeSH-indexed **HEK293 arm** exists."* **It does not.** See §2.

---

## 6 · THE SINGLE HIGHEST-INFORMATION-GAIN EXPERIMENT

The three gaps this paper created (`P1` pellet, `P3` floor, `P5` epitope) are **not three
experiments. They are three lanes and one calibration on one gel.**

> ### 🎯 One denaturing-resolubilised S/P/T blot on `Q230P` fibroblasts, with a dilution-series LOD and two epitope-flanking antibodies.
>
> - **Fractions.** From one lysate at **equal cell-equivalents**: `S` (RIPA-soluble supernatant —
>   reproduces Johannsen exactly), `P` (the discarded pellet, **resolubilised in SDS or urea**),
>   `T` (no-spin total). **`S + P ≈ T` in the wild-type lane is the design's own validity control**
>   (`q230p_true_frontier` `SOL-4`, falsifier `F1`).
> - **Floor.** A ≥5-point dilution series of a WWOX standard **on the same membrane**. Report
>   *"below X ng, N = 3"* — never *"absent"* (`DET-4`).
> - **Epitope.** Blot in parallel with an antibody whose immunogen lies **N-terminal to residue 230**
>   and one that **spans it**, and **score by band size, not signal alone** (`DET-2`/`DET-3`).
>   🎯 **The reagents are already enumerated in this repository**:
>   `wwox_antibody_epitope_census_20260922.md` rows `A5` (ProteinTech, exons 1–7, **spans 230**) and
>   `A6` (Abcam, exons 1–5, **stops 58 residues before 230**), plus `HPA050992` (aa 32–110), *"printed
>   in a peer-reviewed Methods section."* **Add `sc-20528` to that census as a new row** — the
>   antibody that produced the founding result, catalogue number now known, **epitope still to be
>   looked up.**
>
> **Why this one and not another.** It is the only design that can **move H5 and H6 simultaneously**,
> it re-uses the exact cell type and buffer of the original so a negative is directly commensurable,
> and every reagent is already identified in files this repository holds. 🔴 **It does not touch H2,
> H3 or H4** — those need a chase, and `q230p_minimum_discriminator_20260922.md` §4.2 already ruled
> a chase out as the *second* experiment, on the stated ground that *"you cannot chase a band you
> cannot see."* **This experiment is the one that decides whether there is a band to chase.**

**A cheap second, newly justified by §3 and costing one qPCR plate:** a third amplicon **spanning
exon 7** (or exon 6→8 junction-spanning), run on the same cDNA. It tests `RNA-4` directly and would
close the one window Johannsen's design left open. 🟡 **Requires `Q230P` patient RNA, which this
repository does not hold** — so it is `HUMAN_ASSET`, not a bench task.

---

## 7 · THERAPEUTIC CONSEQUENCE — conservatively

**Does the full text change the qualification of pharmacological-chaperone / proteostasis
strategies (`TX-003`, `HYP-20260709-02`)? 🔴 No. It sharpens why they remain conditional.**

- ❌ **The negative Western must NOT be read as `NO TARGET PROTEIN EXISTS`.** Only the
  **RIPA-soluble supernatant** was assayed (`P1`), with **no quantified floor** (`P3`), with an
  antibody of **unknown epitope** (`P5`), and **no turnover or synthesis measurement** (`P4`).
- ❌ **Equally, nothing here supports `A STABILISABLE POOL EXISTS`.** No pellet was examined, so its
  contents are unknown in both directions. 🔴 **Absence of a look is not a look that found something.**
- 🟢 **Correct state: `MOLECULAR FATE UNRESOLVED`, with materially narrower uncertainty** — the
  ambiguity is now localised to four named, individually testable gaps rather than to an unread
  Methods section.
- 🔴 **The therapeutic sign still hinges on `SOL-3`**, exactly as `q230p_structural_mechanism` §9
  already stated: on the clearance branch a proteostasis boost is coherent; on the insolubility
  branch it is *"actively dangerous."* **Today's reading does not select the branch. It confirms
  that the one experiment which would select it has never been run, and names the gel that runs it.**

🔴 **Nothing in this section is medical advice.** No dose, route, schedule or clinical framing is
proposed for any genotype.

---

## 8 · DECLARED LIMITS OF THIS FILE

- Read from the **text layer** of the publisher PDF via `framework/scripts/pdf_text_extract.py`, with
  positive controls passed (`WWOX` 72, `epileptic` 8). 🔴 **Figure *images* were not inspected** —
  Fig. 3c's band pattern is taken from the legend and Results prose, not from the panel. A
  figure-asserted negative would need the image.
- The exon map used in §3 (`exon 7 = c.606–B`, `754 ≤ B ≤ 843`) is the **repository's own**, carried
  from `missense_splice_reclassification_risk_20260921.md` §81, which itself declares the exon 7/8
  boundary `UNKNOWN` within a 90-nt window. 🟢 **The conclusion is insensitive to `B`:** exon 7
  begins at `c.606`, the core amplicon ends at `c.605`, and the 3′ amplicon begins at `c.B+1` — so
  exon 7 is excluded from both for **every** admissible `B`.
- **No canonical file, registry, queue, ledger or the state manifest was modified by this reading.**
  `CLAIM 019`, `CLAIM 030`, `CLAIM 033` and the six Operator-gated candidates are **untouched**.
