# Final report — fifth autonomous run (2026-09-22)

**Actor:** Orchestrator · **Class:** non-canonical synthesis. READ-ONLY toward every canonical file.
**Nothing here is medical advice.** No molecule, dose, route or clinical framing. BLOCK-1 holds.
**Public edition:** the WWOX-DEE genotype class, never an individual.

---

# PART I — SCIENTIFIC REPORT

## 1 · `Q230P` — molecular state

**The state is and remains `MOLECULAR FATE UNRESOLVED`.** Nothing below converts *"no detectable
protein"* into a claim that Q230P protein exists.

| Axis | Status | Evidence |
|---|---|---|
| **RNA** | 🟢 **Transcript present.** Normal WWOX transcript by qRT-PCR in donor fibroblasts from two sisters homozygous at Gln230 | Johannsen 2018, `PMID 29808465` — `INHERITED` |
| **Nascent protein** | 🔴 **NEVER MEASURED, by anyone, in any WWOX allele.** No nascent-synthesis measurement exists | absence claim, §4 |
| **Soluble fraction** | 🟡 **One published negative, on an unclassifiable buffer.** Johannsen's Methods are `PREMISE: METHODS_INVISIBLE` (Springer-closed, no PMCID, three retrieval routes failed). On the repository's own buffer-licensing rule the negative is **not a C1 or C2 negative** and therefore **licenses nothing about solubility** | Scientist B §1.2 |
| **Insoluble fraction** | 🔴 **NOBODY HAS EVER LOOKED IN THE PELLET.** Zero WWOX abundance studies examined an insoluble pellet; zero reported a detection floor | census, `INHERITED` |
| **Degradation** | 🟡 **Unmeasured for this allele.** `Q230P`'s ΔΔG (+1.514) sits between `P47T` (+2.806, **normal protein**) and `P252A` (+1.298, **the only variant with demonstrated accelerated degradation**) ⇒ 🔴 **the predictor is inverted and carries no weight in either direction** | `INHERITED` |
| **Antibody uncertainty** | 🔴 **Decisive and documented.** A published rat *"no protein"* became *"present, faint, N-terminally intact"* at 46.2 kDa **by changing the antibody and nothing else** | Tochigi 2019, `PMID 31340538` |
| **Function** | 🔴 **Not addressed by any design.** `ABUNDANCE ≠ FUNCTION`, `SOLUBILITY ≠ FUNCTION`, `STABILITY ≠ FUNCTION` all hold. Lou 2018 (engineered SDR stabilisation → activity **lost** across the whole panel) is an adverse prior; Atanasov 2007 (pathogenic SDR missense functionally **rescued**) is a favourable one. **They disagree, and `Q230P`'s class is unmeasured** | `INHERITED` |

### 1.1 The best compressed experiment

**One matrix, five cells, minimum measurements:** ① RNA · ② two-epitope Puro-PLA (`S_N`, `S_C`, and
the ratio **ρ**) with **floor calibration** · ③ bafilomycin **and** MG-132, never one · ④ soluble /
pellet / total with the **`S+P ≈ T` arithmetic gate** · ⑤ decay of the pool that forms.

🥇 **The one genuinely new instrument: a two-epitope Puro-PLA ratio straddling residue 230.**
Puromycin terminates chains at whatever length the ribosome reached, so a Puro-PLA signal requires
the epitope to be **already synthesised in that truncated chain**. Epitope position is therefore a
**length gate, not an abundance gate**, and two epitopes straddling residue 230 turn the assay into
a **position report on where chains are being lost**. The N-versus-C comparison is not an invention:
it is **tom Dieck 2015's own specificity control**, repurposed as a measurement.

🔴 **The design's own two hardest limits, stated rather than buried:**
- **`D2`** — `ρ` reads **where**, never **by what machinery**. RQC-at-a-stall and post-exposure
  triage give the same sign and similar magnitude. Separating them needs a **collided-ribosome /
  disome** readout, which is a sequencing-scale experiment outside this matrix. **The matrix's
  principal blind spot.**
- **`D6`** — a fibroblast is not a neuron, and a **negative** in the pellet lane cannot close the
  insolubility branch for the disease-relevant cell type. 🟢 **Downgraded this run from `OUT OF
  SCOPE` to `ROUTE EXISTS, UNCOSTED`:** `PMID 40084072` is a published Puro-PLA protocol in **human
  iPSC-derived i3Neurons**. ⚠️ No i3Neuron carries a WWOX allele, and no WWOX-DEE iPSC line is
  established as available here.

🔴 **And a specification defect that stops two prior designs dead.** The lysis census §4 requires
*"a **C-terminal SDR** antibody (immunogen C-terminal to Q230)."* Across **17 censused anti-WWOX
primaries**, every epitope-documented reagent is **N-terminal** (aa 32–110; 12–94; exons 1–5 ⇒
1–172) or **spans 230** (full-length 1–414; exons 1–7 ⇒ 1–≈280). **The C-terminal-only class is
empty.** Those designs are **unexecutable as written**, not merely unfunded. The proposed
substitute is a **flanking PRM pair** — N-arm `VVVVTGANSGIGFETAK` (126–142), C-arm `VIVVSSESHR`
(255–264) — whose proteotypicity is **`UNVERIFIED` and unverifiable here** (`HUMAN_REQUIRED`).

### 1.2 Implication for a chaperone / proteostasis strategy

🔴 **No branch is selected, and selecting one now would be the error the decision tree exists to
prevent.** The tree is entered only through the `S+P ≈ T` arithmetic gate: **if wild-type mass is
not recovered across the fractions, no blank lane may be read and the tree is void.**

**The therapeutic sign is still unreadable, and that is the finding.** The non-allele-specific
upregulation axis reopened earlier in this session series onto (a) **an empty shelf** — ten agents
with a measured direction, **all oncology, none in a neuron, none in a WWOX-DEE genotype**, and
abundance **never once tied to function** — and (b) **an unreadable sign**: degradation ⇒ a chaperone
route is coherent; **insolubility ⇒ a boost is actively dangerous**, and nobody can exclude it
*because nobody has looked in the pellet.* **The proteotoxic flag stands on both alleles.**

## 2 · Systemic rescue

| | |
|---|---|
| **Historical peripheral abnormalities** | Hypoglycaemia, metabolic acidosis (total CO₂ `14.50` vs `21.67`, `p=0.006`), uraemia (BUN `37.25` vs `17.67`), hypocalcaemia, leukopenia, splenic atrophy (`0.21%` vs `0.53%`, `p=0.0015`), thinned thymic cortex — **all at `n≈4`, at a single P18 timepoint** |
| **Treatment measurements** | 🔴 **Every peripheral WWOX measurement ever made in a treated animal is a PROTEIN BLOT. Transduction was never measured outside the brain at all.** A promoter-restricted construct can deposit vector genomes in a tissue and express nothing there, so *"no WWOX protein in liver"* bounds **expression** and says nothing about **vector arrival** — and the two have been used interchangeably |
| 🔴 **The most important unmeasured endpoint** | **The ANION GAP.** It separates `R1`/renal-tubular (**normal** gap) from `R3`/catabolic-ketotic-lactic (**raised** gap) — the two readings of the same low bicarbonate — **for the price of three electrolytes a panel runs anyway.** The repository currently holds bicarbonate with **no pH and no anion gap**, which is why the field's own death hypothesis has never been testable |
| **Competing hypotheses** | `R1` central control 🟢 **strongly favoured** for growth + metabolic limb · `R2` survival without normalisation 🟡 **fully live for six unmeasured families** · `R3` nutritional/catabolic 🟡 supported, **not separable by the panel alone** · `R4` off-CNS vector 🟡 **under-bounded, not excluded** · `R5` developmental prevention 🔴 **refuted for glucose** · `R6` survivor selection 🟡 live, cuts both ways · `R7` the attribution was never a measurement 🟢 **largely adjudicated** |
| **Minimal existing-sample experiment** | 🥇 **The untreated-null TIME COURSE at P3/P7/P10/P14/P18 — no treated animal, no vector, no therapeutic arm.** Untreated nulls are a by-product of every breeding scheme and die anyway. It is the **only** route to `R5`; it converts the baseline from a **point** into a **distribution** (`±3.5` at `n=4` is equally a shifted mean and a **mixture of two populations**, and no rescue is scorable against a mixture); and it orders the derangements in time **without** the survivor conditioning that contaminates every P18-only measurement. 🔴 **Run it BEFORE the treated panel.** |

🔴 **The structural finding.** The organs carrying the **unrescued** phenotypes — bone, spleen,
thymus, marrow — and the organs ever **assayed** in a treated animal — liver, pancreas, kidney,
testis, ovary, sciatic nerve — **do not overlap at all. The intersection is empty.** And the one
non-CNS tissue added after the original five came back **positive**, so *"restoration is brain-only"*
is an **extrapolation** contradicted at the first organ appended to the list.

## 3 · Purkinje

| | |
|---|---|
| **What is known** | `PREMISE: NOBODY_LOOKED`. Nothing shows Purkinje cells are poorly transduced; **nobody has measured it.** `MAB377` = clone **A60** ⇒ NeuN excludes Purkinje **and** basket cells, so every cerebellar percentage in the programme is a **granule-cell** measurement — a convention inherited across **five years and two papers**, not one paper's defect |
| **What remains invisible** | Cerebellum-resolved **functional** physiology, anywhere. The one slice study **discards the cerebellum at dissection** (*"placed caudal-side down"*). TX-007's archive has **two secondaries, ever**, so four rabbit primaries compete for one channel — a **reagent** gate that makes the archive marker-blind to Purkinje cells |
| **Cheapest existing-material next step** | 🔴 **Mostly "nothing further", and that is the honest answer.** The TX-007 whole-slide scans are `NEW ANALYSIS ONLY` **and `BLOCKED — HOLDER-ONLY`** (*"Data and code availability: Not relevant"*). The 2021 archive holds **in-vivo EGFP reporter material**, a **bicistronic EGFP** therapeutic vector and a **confocal** chain — and **no lysates and no extracted nucleic acid at all**. 🥇 The one item that is neither blocked nor new-cohort is **μCT of archived limbs**, which belongs to the *peripheral* axis and converts an **unquantified visual comparison** (*"cortical bones were of comparable size and thickness to WT"*, Appendix Fig S4B, **unquantified, untested, panel never opened**) into BV/TV |

---

# PART II — DISCOVERY-METHOD REPORT

## 4 · Recursive re-reads

| | OLD PAPER | NEW QUESTION | NEW OBSERVATION | NEW CONSEQUENCE |
|---|---|---|---|---|
| **Cycle 3** | Suzuki 2007, `PMID 17803050` — read 2026-08-06 for **seizures and ataxia** | What unit does Table 2 actually **print**? | 🔴 The token is **`TRANSCRIBED FAITHFULLY AND UNADJUDICATED`** — neither *"we mistranscribed"* (refuted: the locator holds `mg/ml`) nor *"the source misprints it"* (not established: the layer is `SUSPECT`, 34 C0 controls, ~145 substitutions, `q → ±` documented **on the BUN row itself**). **The render that would settle it was made, verified and digested — and it reported the values and never named a unit.** The needle resolving the row was **made of the character in doubt** | Candidate 7. A cross-model numeric comparison is **blocked**; direction and significance **untouched**; a ~2-minute `HUMAN_REQUIRED` render settles it |
| **Cycle 4** | Ludes-Meyers 2009, `PMID 19936220` — read for **systemic/skeletal phenotype** | Are the two models' chemistries **commensurable**? | 🔴 **Creatinine was never measured in the mouse.** Table 3 carries glucose, total CO₂, BUN, calcium, WBC — **no creatinine row.** By the repository's own rule (*adjudicable only if measured in BOTH models*) it is **`UNDETERMINED`** | `CLAIM 038`'s **title** asserts recurrence for a one-model analyte. **Independent of the unit question.** 🟢 Reached the same day by Scientist C, which did not read this re-read |

**Grades:** 2 `REDISCOVERY` · 6 `NEW DETAIL`/`NEW CONNECTION` · 1 claim-changing. The mixture is the
honest result.

## 5 · 🎯 §25 — one COMPLETE iterative-knowledge-growth loop, closed in this run

```
NEW READING (earlier 2026-09-22) — peripheral denominator audit establishes that the mouse
    prints mg/dL and the rat prints mg/ml, and that nothing downstream flags it
        ↓  UPDATED KNOWLEDGE — the two models' chemistries may not be comparable at all
NEW QUESTION ABOUT AN OLD PAPER — Suzuki 2007, read six weeks earlier for a completely
    different purpose (seizures, ataxia): what does it actually PRINT?
        ↓  OLD PAPER RE-READ (pre-registered at 3d0a558, before any locator was opened)
NEW OBSERVATION — the token is unadjudicated, and the instrument that could have adjudicated
    it was pointed at the row and reported everything except the answer
        ↓  CHANGED HYPOTHESIS — the defect is not "wrong unit" but "unverified character",
           which has a different repair: QUALIFY, never correct
TRIGGERS ANOTHER TARGETED SEARCH — sweep the mouse surfaces for creatinine
        ↓
NEW OBSERVATION #2 — creatinine was never measured in the mouse (and \bCRE\b matches Cre
    recombinase at 100% false-positive rate: a new tool trap)
        ↓
CHANGES A CANONICAL TITLE — and the loop hands the next actor a ~2-minute experiment
```

🟢 **The loop is complete and every arrow is documented in a committed file.** The question that
re-opened a six-week-old paper **did not exist** when that paper was read; it was **created by a
different reading, of a different paper, on a different axis.**

## 6 · V0 primitives — shadow-mode verdicts

| primitive | evidence for | evidence against / failures | independent useful instances | **VERDICT** |
|---|---|---|---|---|
| `verify_the_omitted_clause` | Hobson's adjacent sentence **validating** the design its headline appeared to kill; our own adjudication naming values and never the unit | ⚠️ **Half its headline count is delegate-facing**, which measures hand-back compression, not the literature | **8 total — but the number that supports adoption is the SOURCE-SIDE 4**, which doubled this run with no new delegate correction | 🟢 **KEEP** |
| `gate_is_not_quantity` | Puro-PLA **destroys the molecule it counts**; an adjudication reports only the characters its locators were about | never observed to fail; the risk of using it to dismiss any disliked number is **untested** | **7**, six domains | 🟢 **KEEP** |
| `enumerate_baseline_before_scoring` | 🟢 **Second success, first on the Orchestrator** — two findings demoted to `REDISCOVERY` **before** publication, with no delegate involved | **three of five instances are failures** | **5** (3 failures, 2 successes), four actors | 🟢 **KEEP** |
| `preregister_prediction` | **`P1` refuted, and the refutation IS the finding** — written afterwards it would have reported something false | untested against the case where a prediction is so specific it blinds the reader | **3** | 🟢 **KEEP** |
| `diverge_hypotheses` | produced the **third** branch that two others had blocked themselves between | not yet observed to fail | **3** | 🟢 **KEEP** |
| `connect_domains` | Puro-PLA imported from synaptic neuroscience with the `DOES NOT TRANSFER` half carried | the known severe failure — an analogy imported without its `DOES NOT` half becomes a premise | **3** | 🟢 **KEEP** |
| `recursive_reread` | two rounds, different questions, both outcome-changing | **yield per re-read is low**; 3 of 5 returns in round 1 were already held | **2** | 🟢 **KEEP** (promoted) |
| `outcome_distribution_width` | 🎯 **first PROSPECTIVE test of the revised `WIDTH × DISCRIMINATION` rule, and it fired to REJECT** the endpoint most tempting to promote (platelets: never counted in any WWOX animal ⇒ maximally wide; `WIDE × LOW ⇒ LOW`) | 🔴 **one recorded failure**, by misapplication | **2** + 1 failure | 🟡 **REFINE** — the repair now has a prospective confirmation |
| `compress_experiment` | one matrix, eight patterns, six named degeneracies each mapped to the measurement that breaks it | single instance, single actor, single day | **1** | 🟠 **MORE DATA** |
| `adversarial_verify` | — | 🔴 `legend-locator-audit` already ships a **blind** version that is strictly stronger | **0** | 🟠 **MORE DATA — `PROVISIONAL, SUSPECTED DUPLICATE`** |

🔴 **The missing instrument is still missing.** No primitive has been run **deliberately on a case
where it should not help**, with the null recorded. Five rows carry zero failures and are
***untested against failure***, not clean.

## 7 · The two questions, answered explicitly

> ### Did iterative re-reading of existing literature produce genuinely new scientific value in this run?

🟢 **Yes, and the strongest instance is not in a paper at all.** Re-reading Suzuki 2007 under a
question invented six weeks after it was read produced a finding **about our own evidence chain**:
a page adjudication that certified a table row's values and never certified its unit, resolved by a
needle built from the very character in doubt. That changed a commit candidate from *"correct the
unit"* to *"qualify it, and here is the two-minute act that settles it"* — a different edit, with a
different risk profile, reached only because the paper was opened a second time with a question its
first reader had no reason to ask.

⚠️ **And the honest half.** Two of this run's re-read findings were **`REDISCOVERY`**, caught before
publication only because baseline enumeration ran first. **Re-reading generates candidate novelty at
a rate the repository cannot adjudicate without an enumeration step in front of it.** The two
primitives are not independent: `recursive_reread` is only safe downstream of
`enumerate_baseline_before_scoring`.

> ### Which scientific result would probably not have been generated under a conventional one-pass literature review?

🥇 **The two-epitope Puro-PLA ratio.**

A one-pass review of the WWOX literature returns *"normal transcript, no detectable protein,
impaired translation or premature degradation"* and stops, because **that is what the corpus says**.
Reaching the ratio required four things no single pass produces:
1. an accumulated state in which **a published WWOX *"absent protein"* is already known to have
   reversed on an antibody change** — so *epitope position* was a live variable rather than a
   technicality;
2. a **cross-domain import** from synaptic neuroscience, a field with no WWOX literature at all;
3. reading the paper that **refutes** that method closely enough to find the adjacent sentence
   affirming the one claim the design needs — the headline alone would have closed the route; and
4. knowing the repository **already owns** an N-terminal epitope-stated antibody, which sits in an
   **Italian-language bullet** in a canonical ledger and is invisible to anyone reading only the
   obvious files.

🔴 **Runner-up, and it is a negative:** *the flanking antibody pair two prior designs specify cannot
be built.* A one-pass review produces the design; only an **enumeration of every reagent the corpus
actually documents** shows that the design's second half has no reagent in it. **A one-pass review
is structurally incapable of finding that its own recommendation is unexecutable.**
