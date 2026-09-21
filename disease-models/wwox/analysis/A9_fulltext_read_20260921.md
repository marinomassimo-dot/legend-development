# A9 — full-text read, PMID 35984507 (Carvalho et al. 2022, *Cell Mol Life Sci*)

**Status change: `EVIDENCE_BLOCKED` → `ACQUIRED` → `READ`.**
The operator supplied the publisher PDF **and** the supplementary bundle on 2026-09-21. Both were
extracted locally and read. This file is the read; the two
[`FULLTEXT_READ_RECEIPT`](../registries/fulltext_read_receipts.jsonl) events
`FTR-20260921-35984507-01` (main) and `FTR-20260921-35984507-02` (supplementary) fingerprint the
artefacts it rests on.

**Citation.** Carvalho C, Correia SC, Seiça R, Moreira PI. *WWOX inhibition by Zfra1-31 restores
mitochondrial homeostasis and viability of neuronal cells exposed to high glucose.*
Cell Mol Life Sci 2022;79(9):487. [DOI 10.1007/s00018-022-04508-7](https://doi.org/10.1007/s00018-022-04508-7).
Received 22 Mar 2022 / revised 26 Jul 2022 / accepted 27 Jul 2022 / online 19 Aug 2022.
Four authors, **all** University of Coimbra (CNC / CIBB / IIIUC / Institute of Physiology).
**Chang NS appears only in the reference list** (refs 16, 21, 22, 47) — never as an author. The
**group** is independent of NCKU; the **reagent and its specificity claim are not**.

**Nothing here is medical advice.**

---

## §1 Why this paper was queued, and what it was queued to answer

The [peptide intervention audit](peptide_intervention_audit_20260920.md) addendum of 2026-09-20
rested on this paper's **abstract** and said so in terms. It named exactly two questions that a
reading could settle, and filed the paper as acquisition item `A9` so that it would be *read* rather
than *cited*:

1. **Does a genetic WWOX arm exist alongside the peptide** — siRNA / shRNA / knockout — that would
   separate *"Zfra protects"* from *"less WWOX protects"*?
2. **Does total WWOX move, or only pTyr33-WWOX?**

Both are now answered. **The answer to the first is no. The answer to the second is that the question
cannot be answered from this paper, and the reason is itself a finding.**

---

## §2 Method of reading — and its one hard limit

This deployment has no PDF toolchain (`poppler`, `PyMuPDF`, `pypdf` all absent;
`pip install` fails at interpreter level). Text was recovered with
[`framework/scripts/pdf_text_extract.py`](../../../framework/scripts/pdf_text_extract.py), a
standard-library `zlib` + content-stream extractor written for this read.

🔴 **An extractor must be validated before any of its zeros is offered as evidence.** Positive
controls were run first and all returned non-zero: `SH-SY5Y` 3, `Zfra` 68, `Zfra1-31` 61,
`Seahorse` 4, `OCR` 21, `Western blot` 34, `WWOX` 76 distinct contexts. Only then were the negative
searches in §3 treated as readings of the paper rather than readings of the tool. All searches were
run hyphenation- and ligature-tolerant against a de-hyphenated, ligature-normalised rendering.

⚠️ **The limit, stated plainly: the figure *panels* were not inspected — only their legends, axis
mentions and the body text that reports them.** Per `D-14`, **no figure-asserted negative below is
adjudicated from the image**, and none is claimed to be. Every negative in §3 is a negative over
**body text, legends, methods and the supplementary**, which is what a text extractor can honestly
deliver.

---

## §3 What the paper actually contains

### 3.1 Design — verified

| Arm | What was done |
|---|---|
| **Cells** | Differentiated SH-SY5Y human neuroblastoma; 25 mM glucose, 48 h |
| **Peptide** | **20 µM Zfra1-31** (Genemed Synthesis, purity > 95 %), added **3 h** after glucose (**EI**, early intervention) or **24 h** after (**LI**, late intervention) |
| **Animals** | 6- and 12-month-old male **Goto-Kakizaki** rats vs **age-matched Wistar controls**; brain cortex and hippocampus homogenates. **Observational only** |
| **Readouts** | pWWOX(Tyr33), viability, ΔΨm, Seahorse respirometry (basal, maximal, proton leak, ATP-linked, coupling efficiency), mitochondrial ROS, carbonyls/nitrite/TBARS, fission–fusion proteins, MTCO1 / ND1 / VDAC, autophagy panel, Aβ, pTau, SNAP25 / PSD95 / synaptophysin, p53, caspase-3 |

### 3.2 🔴 The negatives — every one of them a text negative, all zero

Searched across the main article **and** the supplementary, hyphenation- and ligature-tolerant:

| Searched | Hits |
|---|---|
| `siRNA`, `shRNA`, `knockdown`, `knockout`, `CRISPR`, `silenc*` | **0** |
| `transfect*`, `lentivir*`, `vector` | **0** |
| `scrambl*`, `S8G`, `inactive peptide` | **0** |
| `bafilomycin`, `chloroquine`, `autophagic flux` (as a clamped measurement) | **0** |
| `total WWOX`, `WWOX expression`, any `pWWOX/WWOX` ratio string | **0** |

**There is no genetic WWOX perturbation of any kind in this paper. There is no scrambled or
inactive-peptide control. There is no vehicle-matched specificity control that is shown.**

### 3.3 🔴 The finding the abstract could not have given us: a total-WWOX antibody was bought and no total-WWOX result was reported

The methods antibody table lists **both**:

> `Anti-WWOX (phospho Y33) Abcam (ab193624)` **and** `WWOX Merck Millipore (ABN413)`

— i.e. a **total-WWOX** antibody was in hand. The methods also state the normalisation:

> *"β-actin was used as a loading control, and bands density was evaluated with the Quantity One
> Software (Bio-Rad)."*

and, separately, *"In some cases, membranes were re-probed instead of running and blotting multiple
gels, to maximize sample yield (e.g., loading control probes)."*

**No total-WWOX measurement is reported anywhere in the paper.** All 76 WWOX contexts report
*pWWOX (tyr33)* / *"activated WWOX"*. The quantified panels are labelled *"WWOX (tyr 33) levels"*
and *"WWOX activation levels"*. No pWWOX-over-total-WWOX ratio appears in any legend or sentence.

**Why that matters, and it is not a quibble.** A pTyr33 signal normalised to **β-actin** falls if
Tyr33 phosphorylation falls **or** if WWOX protein falls. The audit's own §3.6 finding is that
**zfration takes WWOX as a substrate** — i.e. the second possibility is the mechanistically expected
one. So the paper's central pharmacodynamic readout, the **~64 % reduction**, is *exactly* the
quantity that cannot distinguish *"Zfra inhibited WWOX"* from *"Zfra consumed WWOX"* — and the
antibody that would have distinguished them is listed in its own methods.

This does not overturn the paper. It means the paper's title verb — *inhibition* — is **not
established by the paper's own data**, and that the reading of it most consistent with the
originating lab's chemistry is the one the title does not use.

### 3.4 The quantities, attached to the arm they belong to

- The **~64 %** is the **LI (late-intervention)** arm, paired with **~16 %** viability:
  > *"We observed that Zfra1-31 diminished (~64%) the levels of activated WWOX (pWWOX tyr33)
  > (Fig. 3 A) and significantly increased cell viability (~16%; Fig. B)."*
- High glucose alone raised pWWOX(Tyr33) **~79 %** at 24 h (25 mM), maintained at 48 h; 10 mM gave
  **~60 %**, significant only at 48 h.
- Viability fell only **~15 %**, and only at 48 h — i.e. **WWOX activation precedes the damage**,
  which is the paper's genuine temporal result and is well supported.
- p53 **+58 %** and caspase-3 **+44 %** under high glucose, reduced by Zfra1-31 by
  ~34 (LI)–47 (EI) % and ~21 (LI)–50 (EI) % respectively.
- Proton leak normalised by **65–70 %**; coupling efficiency **~39 %**; other respiratory
  parameters improved **without reaching significance**.

### 3.5 The animal arm is better controlled than the abstract suggested — and non-monotonic

The abstract compares young GK to **older GK**, which reads as a weak comparison. The body text has
the comparison that matters:

> *"young animals (6-month-old) present increased levels of pWWOX (tyr33), **when compared to
> age-matched control rats** and to 12-month-old GK rats"*

Cortex **~+20 %**, hippocampus **~two-fold**, at 6 months vs age-matched Wistar. But at **12 months**
the cortical signal **falls ~20 %** and the hippocampal difference is **not significant**.

⚠️ **The age relation is non-monotonic, and the paper's framing ("early event") is a reading of that
shape, not a measurement of it.** Nothing in the animal arm tests whether lowering pWWOX helps an
animal: **no animal received Zfra**. Searches for animal-treatment patterns return zero. The GK arm
is purely observational.

### 3.6 Supplementary — read in full; it contains no Zfra experiment at all

Three items, and only three:

| Item | Content |
|---|---|
| **Table S.1** | Animal characterisation — body weight and occasional glycaemia, 6- and 12-month Control vs GK (GK ~20 % lighter, glucose ~85 % higher) |
| **Figure S.1** | High glucose alone: (A) ΔΨm, (B) mitochondrial ROS |
| **Figure S.2** | High glucose alone: (A) p53 levels, (B) representative blots, (C) caspase-3 activity |

**`Zfra` appears zero times in the supplementary. `WWOX` appears once, in a narrative sentence.**
The supplementary is a high-glucose time-course characterisation and contains **no intervention
arm**. The hope recorded in `HUMAN_ACTION_A9.md` — *"the blots that would show a genetic WWOX arm …
may exist only there"* — is closed: **they do not exist there either.**

⚠️ One epistemic note on the supplementary's own prose: it describes the study as proceeding
*"after establishing the veracity of our hypothesis 'brain WWOX alterations occur under T2D-brain
conditions'"*. That is a hypothesis reported as established within the same work — an instance of the
**interrogative-to-declarative re-voicing** this repository named on 2026-09-21. It is not cited
here as a finding.

### 3.7 🔴 The one genetic WWOX result in the paper belongs to someone else

> *"it was previously shown that inhibition of tyr33 phosphorylation by a **dominant-negative WWOX**
> was able to abolish apoptotic cell death in a MPP+ rat model for PD"* — **reference [18]**.

This is a **citation**, not this paper's data, and it is the same MPP+ line already held in the
audit as `PMID 18371080` / `FT-109`. **It must not be re-voiced as A9's genetic arm.** Under `D-15`,
a secondary source's attribution is not evidence for the attributed result; that line is carried by
its own primary receipt or not at all.

### 3.8 The specificity control the paper relies on is "data not shown"

> *"Zfra1-31, besides being effective against high glucose-induced mitochondrial defects, **does not
> affect mitochondria and cells function under control conditions (data not shown)**."*

This is the only control offered for peptide specificity, and it is not shown. Combined with §3.2
(no scrambled peptide) and §3.3 (no total WWOX), **the paper contains no shown control that
distinguishes a WWOX-mediated effect of Zfra1-31 from any other effect of a 20 µM covalent peptide.**

### 3.9 The authors' own stated limitation

> *"Due to the limited amount of rat brain samples, we were unable to perform key experiments done
> in neuronal cells."*

Recorded because it is the authors' own boundary and it travels with any use of the animal arm.

---

## §4 Verdict

**SUPPORTED — and it is real evidence, from an independent group, in differentiated human neuronal
cells.** 20 µM Zfra1-31 protects SH-SY5Y cells against 48 h of 25 mM glucose across a broad and
internally coherent panel — viability, ΔΨm, respirometry, oxidative damage, fission–fusion, MTCO1 /
ND1 / VDAC, autophagy markers, Aβ, pTau, synaptic proteins, p53, caspase-3 — and it reduces the
pTyr33-WWOX signal while doing so. The temporal claim (**WWOX activation precedes** mitochondrial
dysfunction and death) is supported by the paper's own time-course.

**NOT DEMONSTRATED — that genetic reduction or loss of WWOX is protective.** No genetic arm exists.

**NOT ESTABLISHED — that the protection is caused specifically by WWOX inhibition.** Three
independent reasons, any one of which would be sufficient:

1. **No orthogonal genetic WWOX perturbation** (§3.2).
2. **No inactive/scrambled peptide control**, and the only vehicle-specificity statement is *data not
   shown* (§3.2, §3.8).
3. 🔴 **Total WWOX was never reported** although the antibody was in hand, and the readout is
   normalised to β-actin — so *"Zfra inhibited WWOX"* and *"Zfra degraded WWOX"* are not
   distinguished by the measurement the conclusion rests on (§3.3).

**Canonical formulation, to travel wherever this paper is cited in this repository:**

> **Independent neuronal evidence that Zfra1-31 is protective while reducing the pY33-WWOX signal.
> Causal attribution of that protection to WWOX *inhibition* remains unresolved: no orthogonal
> genetic WWOX perturbation was performed, no inactive-peptide control is shown, and total WWOX was
> never measured — so the reduction in pY33 signal is not separable from a reduction in WWOX
> protein.**

---

## §5 What this does to the peptide audit — and what it does not

**It does not weaken the category objection; it changes which leg carries it.**

| Audit leg | Before this read | After |
|---|---|---|
| Zfra is directionally wrong in a WWOX-residual genotype because **zfration takes WWOX as a substrate** (audit § 3.6, Chang-lab chemistry) | Held on the originating lab's chemistry | **Unchanged, and now the load-bearing leg.** §3.3 shows A9 cannot exclude substrate consumption — so A9 is *consistent with* it, not a check on it |
| *"An independent lab confirms that inhibiting WWOX is protective in neurons"* | Asserted from the abstract | ⚠️ **Must be narrowed.** An independent lab confirms that **Zfra1-31 is protective in neurons and lowers pY33-WWOX**. Whether that is *inhibition* is the very thing the paper does not establish |
| Three-line convergence (peptide / C1q→WOX1 / Zfra) | Three lines | **Still three lines, but they are three lines about *reagents that antagonise the pTyr33 axis*, not three independent demonstrations that less WWOX is better.** Line 1 is a dominant-negative from one lab, line 2 is the authors' own extrapolation, line 3 is A9 with the caveat above |

**The therapeutic conclusion for the reference genotype is unchanged and, if anything, firmer.** Whether
Zfra1-31 *inhibits* WWOX or *consumes* it, **both** readings point the same way in a genotype whose
problem is too little functional WWOX. A reagent that lowers the pY33-WWOX signal by an unknown
mixture of dephosphorylation and degradation is **not** a candidate where residual WWOX protein is
the asset to protect. That remains a **category objection, not a dosing one**.

**What has changed is the honesty of the citation.** The addendum of 2026-09-20 rested on an
abstract and said so. It no longer has to: it now rests on the full text and the supplementary, and
the price of that is that one of its sentences was too strong.

---

## §6 Queue consequences

- **`A9` is closed.** No further acquisition is needed for this paper. `HUMAN_ACTION_A9.md` is
  discharged — the exact scientific question it posed is answered **no**.
- **No new claim is generated.** A9 supports no `CLAIM` in the registry on its own; it qualifies an
  existing audit conclusion and a hypothesis-ledger entry.
- **`HYP-20260705-05`** (*Zfra peptide: monitorare ma non promuovere*) keeps its status. Its
  falsifiable statement is untouched by this read, because the read shows the paper does not test it.
- **Nothing here reopens the Chang batch**, and nothing here is a registry↔ledger audit.

**REVIVAL_TRIGGER.** If any publication reports **total WWOX protein** alongside pTyr33-WWOX under
Zfra1-31 — or any genetic WWOX arm beside the peptide in a neuronal model — this file is revisited,
because that single measurement decides between the two readings in §3.3.

---

*Nothing in this document is medical advice. It concerns the reference genotype — a WWOX-DEE genotype
class — and contains no individual-level record.*
