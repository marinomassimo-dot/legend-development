# `TX-007` — per-arm delivery-chain reconstruction: what differs between the LD and HD arms **beyond the nominal vg number**

**Date:** 2026-09-22 · **Actor:** Scientist T · **Node:** `TX007_PER_ARM_DELIVERY_RECONSTRUCTION`
**Primary source:** `PMID 42422765` / `PMC13343157` — Obeid M, Akkawi R, Repudi S, Singh PK, Abudiab B,
Jebara T, Berent A, Brennan T, Weiss Y, Shekh-Ahmad T, Aqeilan RI. *Neuron-specific WWOX gene therapy
produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy.*
**`Mol Ther Adv`** (*Molecular Therapy Advances*) 2026;34(3):201791.
DOI [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791). **According to PubMed**,
retrieved from **PubMed Central** in this act.

> ⚠️ **Journal name.** `OMTA` here expands to ***Molecular Therapy Advances***, **not** *Molecular Therapy —
> Methods & Clinical Development*. The repository previously mis-expanded it; the correct expansion is used
> throughout this file.

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries,
> the receipt ledger and the state manifest. Nothing here changes a claim, a paper record, the working model
> or any queue. No git operation was run by this node.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> 🔴 **BLOCK-1, stated once and binding over every line below.** **No molecule is named as a therapy, no dose
> is recommended, no route is recommended, no safety claim is made, no druggability score is given.** Every
> number below records **what a published experiment administered to mice**, reconstructed so the experiment
> can be audited. **Reporting a dose a paper used is not recommending it.** *"No overt toxicity observed"* is
> never *"safety established"*. **Nothing here is medical advice**; it is material for discussion with a
> treating clinical team and for nobody else.

---

## 0 · The closed question, restated once so it is not re-opened

The dose-unit audit is **finished** and is **not re-litigated anywhere in this file**:

- `HD/LD = 2.63/1.23 = **2.1382**` under every permitted reading; the unknown convention `u` **cancels**.
- The ambiguity is confined to the **absolute** axis, by exactly 2×: `LD ∈ [1.23, 2.46]×10¹¹ vg`,
  `HD ∈ [2.63, 5.26]×10¹¹ vg`. Classification `AMBIGUOUS BUT BOUNDED`.
- **The unit ambiguity does NOT explain the non-monotonicity.** Withdrawn as a category error.

Sources: [`tx007_dose_unit_forensics_20260922.md`](tx007_dose_unit_forensics_20260922.md) (read in full) ·
[`CC-20260922-TX007-DOSE-CHALLENGE-01.md`](../research/commit_candidates/CC-20260922-TX007-DOSE-CHALLENGE-01.md)
§10 (read in full). **This node takes both as settled and adds nothing to them.**

**The question this node answers instead:** *which variable differs between the LD and HD arms beyond the
nominal vg number, and which of those could explain survival and regional distribution?*

---

## 0.1 · Surfaces, declared before any number is used

| Surface | Code | How obtained | What it carries |
|---|---|---|---|
| **PMC served body, 48,780 chars** | **`S-body`** | 🟢 **fetched and read by me in-act**, `get_full_text_article(pmc_ids=["PMC13343157"])` | Introduction, 7 Results sections, Discussion, **complete Materials and methods**. 🔴 **No figure legends. No `n =` tokens (0, measured). No P values. Exponents deleted** (`1.23 × 10vg`) |
| Prior-session figure / caption renderings | **`A-fig`** | 🔴 **INHERITED ATTESTATION — I could not open any of them.** `files/` is gitignored and **absent from this worktree** (verified) | `gr1`–`gr7.jpg` at 104 ppi; `S_p09/S_p10_200dpi.png`; the ×4.5 Fig 3B and Fig 2B crops of `CC-20260826-DOSE-ADJUDICATION-01` |
| Repository artefacts | **`A-repo`** | 🟢 read in full by me | `PMID42422765_partial_locators.md` (889 ll.), `CC-20260826-DOSE-ADJUDICATION-01.md`, `CC-20260814-42422765-01.md`, `tx007_dose_unit_forensics_20260922.md`, `discovery_ledger_current.md` DL-MECH-009 |

🔴 **Every value marked `A-fig` is an attestation by a previous actor that I could not verify.** It is
labelled as such at every use and **never relayed as my own read**. Nothing in §3's ranking depends on an
`A-fig` value alone; where one is load-bearing it is said so explicitly.

**Egress, attempted once and recorded once (not a scientific stop):**
`europepmc …/PMC13343157/fullTextXML` → `CONNECT tunnel failed, 403` · `pmc.ncbi.nlm.nih.gov/articles/PMC13343157/`
→ `403` · **control `example.com` → `403`.** ⇒ allowlist, not a paper-specific block. **The caption-bearing
surface is unreachable from this deployment.** Established, not retried.

🔴 **Exponent discipline.** Every dose below is written in **E-notation**, the only exponent-safe form. The
served body renders all of them with the exponent **silently deleted** (`1.23 × 10vg`, `8 × 10vg`,
`4 × 10vg` — verified by me in-act). Exponents are supplied from the two `A-fig` renderings named in
`tx007_dose_unit_forensics_20260922.md` §3.1 and **not from memory**.

---

## 1 · The answer, before the tables

> **Which variable differs between LD and HD beyond the nominal vg number?**

# 🟢 **At the level of what the paper STATES: only the concentration of the prep. Nothing else.**
# 🔴 **At the level of what the paper does NOT state: almost the entire vector-prep chain, and the whole animal-allocation chain.**

**The forcing observation, from the Methods, read by me in-act:** the paper specifies **one injection
protocol, with one volume, applied to every arm** — *"The pup (KO or WT) was staged on the stereotaxic frame
for **AAV9-hWWOX or RI delivery**"* … *"delivering **2.0 μL/hemisphere**"* … *"**The procedure was repeated
for the contralateral hemisphere**."*

⇒ **Volume is a stated constant across arms.** Therefore, arithmetically and unavoidably:

# **HD was delivered as a MORE CONCENTRATED PREP, not as a larger volume.**

**This is a determination, and it kills one of the two candidate mechanisms outright:**

| Candidate mechanism | Prediction | Verdict from the text |
|---|---|---|
| HD spread further because a larger bolus filled more of the ventricular system | regional distribution should broaden with dose, especially to distal regions (cerebellum, spinal cord) | 🔴 **REFUSED.** Volume is stated identical. The CSF distribution volume is matched by construction |
| HD achieved a higher local vector concentration at the ependymal surface at a matched bolus | regional distribution should be **similar in shape** and differ in **magnitude** | 🟢 **The only stated mechanism remaining** |

⚠️ **And the paper's own data are the shape the surviving mechanism predicts**: the same four regions are
positive in both arms, and the LD→HD difference is one of magnitude — *"higher vDNA levels in HD-treated
mice than LD-treated mice **across regions**"* (`S-body`). Consistency is not proof; it is recorded as
consistency.

**But the stated chain stops there.** The paper never states the titre, never states how the two
concentrations were produced (dilution of one stock, or two independent preps), never assigns a lot or a
manufacturer to any arm, and states **nothing at all** about empty:full capsid ratio, purification route,
formulation buffer or endotoxin. **Every one of those is a variable that travels with concentration**, and
every one is `ABSENT`.

---

## 2 · The per-arm delivery chain

### 2.0 Arms as the paper defines them

| ID | Arm | Figure | Vector | WPRE | Nominal dose as written |
|---|---|---|---|---|---|
| **A1** | KO + AAV9-EF1α-hWWOX | Fig 1 | AAV9 | ✅ present | `4E10` |
| **A2** | KO + AAV9-CMV-hWWOX | Fig 1 | AAV9 | ✅ present | `4E10` |
| **A3** | KO + AAV9-CBA-hWWOX | Fig 1 | AAV9 | 🔴 **ABSENT — see §2.3** | `4E10` |
| **A4** | KO + AAV9-MBP-hWWOX | Fig 1 | AAV9 | ✅ present | `4E10` |
| **A5** | KO + AAV9-hSynI-hWWOX | Fig 1 | AAV9 | ✅ present (`A-fig` caption) | `4E10` |
| **B1** | KO + AAV9-hSynI-hWWOX **−WPRE** | Fig 2 / S3 | AAV9 | ❌ absent | `4E10` |
| **B2** | KO + AAV9-hSynI-hWWOX **+WPRE** | Fig 2 / S3 | AAV9 | ✅ present | `4E10` |
| **B3** | KO + AAV9-hSynI-hWWOX **−WPRE** | Fig 2 / S3 | AAV9 | ❌ absent | `8E10` |
| **B4/B5** | ±WPRE protein columns | Fig 2E | AAV9 | both | `2E10` — 🔴 `A-fig` only; **no such token in `S-body`** |
| **C0** | KO + RI | Figs 3–7 | — (vehicle) | — | vehicle only |
| **C1 = LD** | KO + AAV9-hSynI-hWWOX **−WPRE** | Figs 3–7, S4–S7 | AAV9 | ❌ absent | `1.23E11` |
| **C2 = HD** | KO + AAV9-hSynI-hWWOX **−WPRE** | Figs 3–7, S4–S7 | AAV9 | ❌ absent | `2.63E11` |
| **C3** | WT + RI | Figs 3–7 | — (vehicle) | — | vehicle only |
| **D0–D5** | KO + HD vector at **P0, P1, P2, P3, P4, P5** | S8 | AAV9 | ❌ absent | `2.63E11` (HD) |
| **D-WT** | WT littermates, **identical injections** | S8 | — | — | — |

### 2.1 🔴 The main dose-response arms — the chain, link by link

**Every cell is `STATED` / `DERIVED` (arithmetic shown) / `ABSENT`, with its locator.**

| Link | **C1 · LD** | **C2 · HD** | Same or different? |
|---|---|---|---|
| **Nominal dose** | **`1.23E11` vg** — **STATED**, Results §"WWOX gene therapy improves survival…": *"we evaluated two clinically applicable doses: an LD (1.23 × 10vg) and a higher dose (HD, 2.63 × 10vg) (A)"* (`S-body`, exponent deleted; supplied `1.23E11` from Fig 3A + the S7I caption *"KO+W LD (1.23x1011vg)"*, `A-fig`) | **`2.63E11` vg** — **STATED**, same sentence; exponent from the same two `A-fig` renderings (*"KO+W HD (2.63x1011vg)"*) | 🔴 **DIFFERENT — 2.1382×** (closed, §0) |
| **Unit denominator (per hemisphere / total)** | 🔴 **ABSENT.** Bare `vg` on all three surfaces the repository holds; `hemisphere` occurs twice in `S-body`, both in Methods, never adjoining a dose | 🔴 **ABSENT**, identically | 🟢 same (common-mode) |
| **Titre (vg/µL)** | 🔴 **ABSENT as stated — never printed anywhere in the paper.** **DERIVED:** `1.23E11 / 4.0 µL = 3.075E10 vg/µL` (total reading) **or** `1.23E11 / 2.0 µL = 6.15E10 vg/µL` (per-hemisphere reading) | 🔴 **ABSENT as stated.** **DERIVED:** `2.63E11 / 4.0 = 6.575E10 vg/µL` **or** `2.63E11 / 2.0 = 1.315E11 vg/µL` | 🔴 **DIFFERENT — 2.1382× under both readings** (ratio invariant) |
| **Required stock titre (vg/mL)** | **DERIVED:** `3.075E13` or `6.15E13` | **DERIVED:** `6.575E13` or **`1.315E14`** | 🔴 different; **see §5.2 — this is a testable discriminant on the unit reading** |
| **Injected volume** | **`2.0 µL` per hemisphere — STATED**, Methods §ICV: *"delivering 2.0 μL/hemisphere through a Hamilton syringe with a 32G needle"* | **identical — STATED by the same sentence**, which covers *"AAV9-hWWOX or RI delivery"* | 🟢 **SAME — stated, not assumed** |
| **Total volume** | **`4.0 µL` — DERIVED:** `2.0 µL × 2 hemispheres`, from *"The procedure was repeated for the contralateral hemisphere"* (Methods, `S-body`) | **`4.0 µL` — DERIVED identically** | 🟢 SAME |
| **Number of injections** | **2 (one per hemisphere) — DERIVED** from the same two sentences | **2 — DERIVED** | 🟢 SAME |
| **Injection rate** | **`1–1.5 µL/min` — STATED**, Methods: *"A Micro-4 nano-pump controller was used to ensure a steady injection rate of 1–1.5 μL/min"* | **identical — STATED** | 🟢 SAME |
| **Needle / dwell / withdrawal** | **32G Hamilton; dwell `30-60 s`; withdrawal over `1 min` — STATED**: *"The needle was kept at the injection site for 30-60 s to allow proper diffusion and then removed slowly over 1 min"* | **identical — STATED** | 🟢 SAME |
| **Route** | **Bilateral ICV, stereotaxic — STATED**: *"conducted using stereotactic technique to ensure consistency by following a published protocol"*; coordinates relative to **lambda**, `±0.8 / 1.5 / −1.6 mm` at P0-P1 | **identical — STATED** | 🟢 SAME |
| **Anaesthesia** | **Hypothermia — STATED**: *"anesthetized by placing them on a dry, flat, cold surface"* | **identical — STATED** | 🟢 SAME |
| **Age at injection** | **`P0-P1` — STATED**: *"All preceding treatments were administered at P0‑P1"* (Results §"Early postnatal…"). 🔴 **The per-arm distribution inside that 2-day range is ABSENT** | **`P0-P1` — STATED by the same sentence.** Distribution **ABSENT** | 🟡 **bounded-same, not matched.** See §3.4 |
| **Anatomical distribution — vDNA, P30** | **STATED (4 regions measured, both arms):** *"we quantified viral DNA (vDNA) levels in brain tissue at P30 using qPCR. Analysis of the cortex, hippocampus, midbrain, and cerebellum revealed a clear dose-dependent pattern, with higher vDNA levels in HD-treated mice than LD-treated mice across regions, **with statistical significance in the hippocampus** (A–5D)"* — Fig 5A–5D | same sentence, same four regions | 🔴 **Significantly separated in 1 of 4 regions only — stated by the authors** |
| **WWOX mRNA per region, P30** | **STATED:** *"RT-qPCR analysis demonstrated robust, region-wide induction of WWOX transcripts in HD-treated mice, whereas LD-treated mice showed lower but readily detectable expression (E–5H)"* — Fig 5E–5H. 🔴 **No significance stated for any region** | same sentence | 🔴 **No stated significance on the transcript axis, either arm** |
| **WWOX protein per region, P30** | **STATED:** *"Immunoblot analyses at P30 revealed a marked dose-dependent increase in WWOX protein, most prominently in the cortex and to a lesser extent in the hippocampus, midbrain, and cerebellum, **with a trend toward higher expression** in HD-treated mice compared with LD-treated mice (I–5L)"* — Fig 5I–5L | same sentence | 🔴 **The authors' own word is "a trend"** — they do **not** claim significance |
| **Protein, ~3 months** | 🔴 **ABSENT — LD is not named.** *"At later stages (∼3 months) … **HD-treated mice** maintained elevated WWOX protein levels across all examined brain regions (A-S5D, S5H, S5I), a pattern also evident in the spinal cord"* | **STATED, HD only** | 🔴 **Asymmetric measurement begins here** |
| **Protein, P180 / P240 / P300** | 🔴 **ABSENT.** *"Robust WWOX protein levels persisted at P180 (E–S5G), and widespread, stable expression was maintained at P240 and P300 throughout the cortex, hippocampus, midbrain, cerebellum, and spinal cord following a single neonatal injection"* — **the arm is not named in this sentence**; that it must be HD is **DERIVED** from *"LD-treated mice did not survive to P90"* | **DERIVED = HD** | 🔴 asymmetric |
| **Sciatic nerve (PNS)** | 🔴 **ABSENT.** *"WWOX protein was also detected in the sciatic nerve of **HD-treated mice** (E–S6G)"* | **STATED, HD only** | 🔴 asymmetric |
| **Liver (negative control)** | 🟢 **STATED for BOTH:** *"no WWOX expression was detected in the liver following **either LD or HD** treatment (H and S6I)"* | same sentence | 🟢 **The ONE post-injection biodistribution statement that names both arms is the negative one** |
| **Myelination (MBP)** | **STATED, both arms:** *"HD treatment achieved near-complete rescue across affected regions, whereas **LD treatment produced only partial recovery** relative to HD (F;I)"* — Fig 6F, S7I. 🔴 `A-repo`: **Fig 6F, S7I and S8G are representative images with no quantification**; the only MBP quantification (Fig 6E) contains **WT and KO only** | same sentence | 🟡 stated as different, **quantification not located in any panel the repository has read** |
| **Neuroinflammation** | **STATED, both arms implicitly:** *"Neuronal WWOX restoration significantly reduced both astrocyte reactivity and microglial density **in a dose-responsive manner** (E–S7H)"*. `A-fig`: S7H **GFAP — LD significantly ABOVE WT (`**`), HD `ns`** | same sentence | 🔴 **the one axis where LD is stated/attested to be *worse than WT* while HD is not** |
| **Ataxia, P18** | **STATED, both arms:** *"LD treatment resulted in partial improvement and HD treatment achieved near-complete rescue"* (S4A–S4B) | same sentence | both measured |
| **Blood glucose, P10/P20/P30** | **STATED, both arms:** *"Beginning at postnatal day 10 (P10), both LD and HD treatments partially corrected hypoglycemia. By P20 … HD … fully normalized … whereas LD-treated mice showed an intermediate improvement. From P30 onward, glucose levels were normalized across all groups"* (Fig 3E–3H) | same sentence | both measured |
| **Behaviour, 3 months** | 🔴 **EXCLUDED — STATED:** *"Behavioral testing could not be performed in untreated-null mice due to severe morbidity and early lethality, and **LD-treated mice did not survive to P90**; therefore, analyses were limited to WT and HD-treated groups"* | **STATED, HD only** | 🔴 asymmetric **as a consequence of survival, stated as such** |
| **Fertility** | 🔴 **ABSENT.** *"Fertility testing using 20 breeding cages per group demonstrated that **HD-treated**-null mice exhibited fertility rates and litter sizes comparable to WT and heterozygous controls (C–S4E)"* | **STATED, HD only** | 🔴 asymmetric |
| **ECoG** | 🔴 **ABSENT.** The section names only *"**HD** WWOX gene therapy"* and *"using **HD** AAV-mediated gene delivery"*; Methods name the rescue group as *"WWOX-KO mice injected with AAV9-hSynI-hWWOX"* with no dose | **STATED, HD only** | 🔴 asymmetric |
| **Survival** | **STATED (qualitative):** *"LD treatment modestly, though significantly, extended lifespan relative to untreated-null controls"*; **STATED (hard):** *"LD-treated mice did not survive to P90"*. 🔴 `A-fig`: declines from ~20 d, **reaches 0% by ~80 d**, `n=20` | **STATED:** *"whereas HD treatment produced a marked and sustained survival benefit (B)"*. 🔴 `A-fig`: ≈78% at ~85 d, flat to 300 d, `n=30`; caption `p = 0.78` vs WT, `p < 0.0001` vs LD and vs KO+RI | 🔴 **categorically different** |
| **Follow-up horizon** | **Same panel as HD.** `A-fig` (pixel, crop recipe declared in `CC-20260826` §1): **Fig 3B x-axis runs to 300 days**; both arms plotted on it | same panel, same axis | 🟢 **SAME — see §4** |
| **n per arm** | 🔴 **ABSENT from every surface I read** (`n =` → **0 occurrences in 48,780 chars, measured**). `A-fig`: `n=20` | 🔴 **ABSENT.** `A-fig`: `n=30` | 🔴 **unequal allocation 20:30, unexplained** |
| **Sex composition** | 🔴 **ABSENT.** The only sex statements are *"with no significant sex-dependent differences observed"* (body weight) and *"both male and female **HD-treated** mice"* (behaviour) | 🔴 **ABSENT** (composition), partially stated for behaviour | 🔴 unstated |
| **Litter / dam / allocation** | 🔴 **ABSENT.** No litter statement for LD or HD. `randomi*` → **0 occurrences, measured** | 🔴 **ABSENT** | 🔴 unstated |
| **Background strain** | **FVB — STATED:** *"Mice were kept on an FVB (Friend leukemia Virus B) background"* | **identical — STATED** | 🟢 SAME |
| **Vector architecture / WPRE** | **−WPRE — STATED:** *"we generated AAV9-hSynI-WWOX vectors **lacking the WPRE element**"*, in the sentence pair that introduces both doses | **−WPRE — STATED by the same sentence** | 🟢 **SAME — the largest candidate confound is REFUSED** |
| **Titration method** | **RT-qPCR, bGH primers — STATED:** *"Viral titers were determined by RT-qPCR using bGH primers"*. 🔴 One method; **no orthogonal method, no CV, no replicate count** | **identical — STATED** | 🟢 method same; 🔴 **uncertainty unquantified for both** |
| **Manufacturer / lot** | 🔴 **ABSENT.** Four sources named collectively — *"Fujifilm Diosynth Biotechnologies … Vector Biolabs … Boston Institute of Biotechnology [BIB]"* plus *"the Vector ELSC Core Facility"* — with **only two constructs assigned** (AAV9-CBA-hWWOX and AAV9-hSynI-EGFP → ELSC). `lot`/`batch` → **0 occurrences, measured** | 🔴 **ABSENT** | 🔴 **unknown whether same lot** |
| **Empty:full capsid ratio** | 🔴 **ABSENT.** `capsid` → 0 · `empty` → 0, measured | 🔴 **ABSENT** | 🔴 unknown |
| **Purification route** | 🔴 **ABSENT.** `iodixanol` → 0 · `chromatog*` → 0 · `affinity` → 0 · vector `purif*` → 0, measured | 🔴 **ABSENT** | 🔴 unknown |
| **Formulation buffer of the vector** | 🔴 **ABSENT.** The **vehicle** is specified — *"reference item (RI; PBS with 5% sorbitol and 0.001% pluronic F-68)"* — but the **vector's own** formulation is never stated | 🔴 **ABSENT** | 🔴 unknown |
| **Endotoxin** | 🔴 **ABSENT.** `endotoxin` → 0, measured | 🔴 **ABSENT** | 🔴 unknown |
| **Blinding** | 🟡 **conditional — STATED:** *"Data were analyzed in a blinded manner **when feasible**"* | identical | 🟡 same, and weak |
| **Censoring rule** | 🔴 **ABSENT.** `censor*` → **0 occurrences, measured**. Methods state only *"Survival was analyzed using Kaplan-Meier curves with significance assessed by the log-rank (Mantel-Cox) test"* | 🔴 **ABSENT** | 🔴 **see §4.3 — this is the most damaging gap** |

### 2.2 The other arms — chain, abbreviated to the links that differ

**Every arm shares the identical delivery protocol** (2.0 µL/hemisphere, bilateral, 1–1.5 µL/min, 32G,
stereotaxic, lambda-relative, hypothermia), because the Methods state **one** protocol covering *"AAV9-hWWOX
or RI delivery"*. The links below are therefore the only ones that vary.

| Arm | Nominal | Derived titre (vg/µL), total ‖ per-hemi reading | Age | Survival, as the paper renders it | Follow-up horizon |
|---|---|---|---|---|---|
| **A1 EF1α +WPRE** | `4E10` | `1.00E10` ‖ `2.00E10` | P0-P1 (STATED) | **STATED:** *"failed to rescue lethality, growth retardation, or hypoglycemia"* | 🔴 ABSENT in text. `A-fig`: curves to ~25–45 d |
| **A2 CMV +WPRE** | `4E10` | `1.00E10` ‖ `2.00E10` | P0-P1 | **STATED:** *"supported early postnatal rescue of survival and glycemic defects … but this protection was not sustained at later stages"* | 🔴 ABSENT in text |
| **A3 CBA** | `4E10` | `1.00E10` ‖ `2.00E10` | P0-P1 | **STATED:** grouped with CMV in the same sentence | 🔴 ABSENT in text |
| **A4 MBP +WPRE** | `4E10` | `1.00E10` ‖ `2.00E10` | P0-P1 | **STATED:** *"weak expression and no phenotypic improvement"* | 🔴 ABSENT in text |
| **A5 hSynI +WPRE** | `4E10` | `1.00E10` ‖ `2.00E10` | P0-P1 | **STATED:** *"the most robust and sustained rescue"* | 🔴 ABSENT in text |
| **B1 hSynI −WPRE** | `4E10` | `1.00E10` ‖ `2.00E10` | P0-P1 | **STATED:** *"exclusion of WPRE was insufficient to rescue lethality in KO mice"* | 🔴 ABSENT in text. `A-fig` (pixel): **Fig 2B x-axis ends at 50 d**; this arm `n=3`, falls to ≈33% by ~20 d, **one animal censored at ~25 d** |
| **B2 hSynI +WPRE** | `4E10` | `1.00E10` ‖ `2.00E10` | P0-P1 | **STATED:** *"treatment with WPRE-containing vectors at the same dose resulted in survival rates comparable to WT (B)"* | same panel, 50 d |
| **B3 hSynI −WPRE** | `8E10` | `2.00E10` ‖ `4.00E10` | P0-P1 | **STATED:** *"Increasing the dose of the WPRE-lacking vector to 8 × 10vg was associated with improved outcomes, **including rescue of lethality** and normalization of growth and glucose levels"* | 🔴 **ABSENT in text.** `A-fig` (pixel): `n=5`, **flat at 100% to ~31 d**, on a **50-day axis** |
| **C0 KO+RI** | vehicle | — | P0-P1 | **STATED (Discussion):** untreated survival *"approximately three weeks"* | Fig 3B, 300 d |
| **C3 WT+RI** | vehicle | — | P0-P1 | 🔴 `A-fig`: **≈72% at 300 d — the vehicle-injected WT arm is NOT 100%** | Fig 3B, 300 d |
| **D0–D5 window, HD** | `2.63E11` | `6.575E10` ‖ `1.315E11` | **P0, P1, P2, P3, P4, P5 — STATED:** *"ICV injection … at daily intervals from P0 to P5, with **at least three littermates treated per time point**"* | **STATED:** *"a dramatic extension in survival, from approximately three weeks to **nearly one year**"* | `A-fig`: **S8A to P40; S8B to P300 and plots only P1 and P5** |
| **D-WT** | — | — | P0–P5 | **STATED:** *"WT littermates received identical injections to control for procedural effects"* | — |

🔵 **Coordinate adjustment is the one delivery link that is stated to differ by age, and only by age:**
*"for P5 pups, the injection site was targeted at ±1.0 mm, 1.0 mm, and −2.0 mm"* versus `±0.8 / 1.5 / −1.6`
at P0-P1. **Volume, rate, needle and injection count do not change with age.** ⇒ the window arms are
delivery-matched to the LD/HD arms on every link except stereotaxic coordinate.

### 2.3 🆕 Two chain defects found in-act that the repository does not hold

**T-1 · The CBA construct's WPRE status is `ABSENT`, and the Methods sentence that looks like it settles it
does not.** Methods, verbatim: *"Constructs driven by **EF1α, CMV, and MBP** included WPRE, whereas the
**hSynI**-driven vector was generated both with and without WPRE."* **CBA is not in that list**, and CBA is
one of the five promoters in Fig 1 (*"Ubiquitous promoters (EF1α, CMV, and **CBA**)"*). The one place CBA
appears in the Methods is *"Custom-made **AAV9-CBA-hWWOX** and AAV9-hSynI-EGFP viral particles were obtained
from the Vector ELSC Core Facility"* — a **different manufacturer from every other construct**, with **no
cassette description**. ⇒ **The CBA arm differs from its own comparators on two links at once — WPRE status
and manufacturer — and neither is stated.** Anything drawn from the CMV/CBA grouping (*"Stronger ubiquitous
promoters (CMV and CBA) supported early postnatal rescue"*) inherits both.

**T-2 · 🔴 The breeding scheme puts a maternal variable into every arm, and its per-arm distribution is
`ABSENT`.** Methods, verbatim: *"**Heterozygote or KO rescued mice (KO injected with AAV9-hSynI-hWWOX) were
used for breeding** to generate KO mice."* ⇒ **some KO pups are born to an AAV-treated KO dam and others to
an untreated heterozygous dam.** The paper never states which dams produced the LD cohort and which produced
the HD cohort. **This is not a cosmetic gap:** the study's principal systemic endpoint is **blood glucose**,
and *"profound hypoglycemia"* is the dam's phenotype as well as the pup's. A treated-KO dam and a Het dam
are different intrauterine and lactational environments for a metabolic readout. **Neither the repository nor
the prior forensics node holds this.** It is recorded as a **confound**, not as a criticism of the breeding
scheme, which is the only practical way to generate these litters.

---

## 3 · Confound inventory — each candidate confirmed, refused or declared unstated

**Scope note, stated once:** *confirmed* means the paper states the arms differ; *refused* means the paper
states they match; *unstated* means the paper is silent and the value is `ABSENT` — **which is never 0 and
never "same as the other arm."**

### 3.1 Volume and titre — **ADJUDICATED**

| Sub-question | Verdict | Verbatim evidence |
|---|---|---|
| Was HD a **larger volume**? | 🟢 **REFUSED** | *"delivering **2.0 μL/hemisphere**"* + *"The procedure was repeated for the contralateral hemisphere"*, in the single Methods paragraph covering *"AAV9-hWWOX or RI delivery"* (`S-body`) |
| Was HD a **more concentrated prep**? | 🟢 **CONFIRMED by arithmetic**, `ABSENT` as a stated value | **DERIVED:** at fixed 4.0 µL, `2.63E11 / 1.23E11 = 2.1382×` concentration. The paper prints **no titre for any arm** |
| Both? | 🟢 **NO — concentration only** | follows from the two rows above |

🔵 **Why this matters mechanistically, and it is the substantive result of this section.** A fixed 4.0 µL
bolus into the neonatal lateral ventricles delivers the **same distribution volume** in both arms. The two
arms therefore differ in the **concentration gradient driving transduction**, not in the **anatomical
territory reached**. **Prediction that follows:** regional distribution should be *the same set of regions,
different magnitude* — which is what the authors report (*"higher vDNA levels in HD-treated mice than
LD-treated mice **across regions**"*). ⚠️ Consistency, not proof: no arm-by-arm spatial map exists.

### 3.2 Vector prep — **the largest block of `ABSENT`**

| Variable | Verdict | Evidence |
|---|---|---|
| **WPRE** | 🟢 **REFUSED as a LD-vs-HD confound.** Both arms are **−WPRE** | *"we generated AAV9-hSynI-WWOX vectors **lacking the WPRE element** … we evaluated two clinically applicable doses: an LD … and a higher dose (HD …)"* — one sentence pair, `S-body` |
| **WPRE, across figures** | 🔴 **CONFIRMED as a confound for Fig 1/Fig 2 vs Fig 3** | Methods: EF1α/CMV/MBP **+WPRE**; hSynI **both**. `A-repo` DL-MECH-009, S3E: WPRE raises WWOX **cortex 3.0× · hippocampus 3.0× · midbrain 5.5× · cerebellum 16.7×**. 🔴 **A 3–16.7× regional factor dwarfs a 2.14× dose factor** — so **no dose comparison may cross the ±WPRE line** |
| **Same lot?** | 🔴 **UNSTATED.** `lot` / `batch` → 0 occurrences, measured | — |
| **Same manufacturer?** | 🔴 **UNSTATED for the LD/HD vector.** Three commercial packagers listed collectively; only CBA-hWWOX and hSynI-EGFP assigned (to the HUJI ELSC core) | *"These vectors were packaged into AAV9 serotypes (Fujifilm Diosynth Biotechnologies …; Vector Biolabs …; Boston Institute of Biotechnology [BIB] …)"* |
| **Same purification?** | 🔴 **UNSTATED.** 0 occurrences of any purification term | — |
| **Empty:full capsid ratio** | 🔴 **UNSTATED.** `capsid` → 0, `empty` → 0 | — |
| **Formulation buffer** | 🔴 **UNSTATED** for the vector; **STATED** for the vehicle only | *"reference item (RI; PBS with 5% sorbitol and 0.001% pluronic F-68)"* |
| **Endotoxin** | 🔴 **UNSTATED.** 0 occurrences | — |
| **Titration** | 🟢 **method matched, uncertainty unquantified** | *"Viral titers were determined by RT-qPCR using bGH primers"* — one method, no orthogonal, no CV, no replicate count |

🔴 **The consequence, stated plainly.** If LD and HD were **two independent preps**, they differ on every row
above and the 2.1382× nominal separation is the *only* difference anyone has measured. If LD was a
**dilution of the HD stock**, the rows collapse to near-identity and the nominal separation is nearly the
whole story — **but the excipient concentration would then also differ 2.14×, and the empty-capsid burden
would scale with it.** **The paper does not say which, and the two cases have different predictions.** This
is the single largest unresolved variable in the chain.

### 3.3 Age at injection — **bounded, not matched**

🟢 **STATED:** *"All preceding treatments were administered at **P0‑P1**."* (Results §"Early postnatal…") —
this sentence covers Figs 1–7, i.e. **both the Fig 2 arms and the Fig 3 LD/HD arms**.
🔴 **`ABSENT`:** the distribution of P0 versus P1 **within** the LD arm and **within** the HD arm.

⚠️ **The S8 window result cannot be used to dismiss this, and the reason is a transfer rule.** S8 shows
*"neuronal WWOX restoration using **the high-dose vector** at any time point between P0 and P5 was sufficient
to fully rescue"* — **HD only.** There is **no low-dose window experiment.** ⇒ **A 1-day age spread is
demonstrably immaterial at HD and is untested at LD.** If LD sits near a delivery threshold, a
developmental day could matter there and not at HD. Rated **live but low-magnitude** in §3.7.

### 3.4 Follow-up horizon — **see §4, answered in full**

### 3.5 `n` per arm — **`ABSENT` from every surface I read**

🔴 **Measured:** `n =` and `n=` → **0 occurrences in 48,780 characters.** The Methods say *"Exact sample
sizes () and values are reported in the figure legends"* — **and the legends are the surface this deployment
cannot reach.**

**Inherited (`A-fig`, not my read):** Fig 3B `WT+RI n=20 · KO+RI n=10 · KO+LD n=20 · KO+HD n=30`;
Fig 2B `4E10 n=3 · 8E10 n=5`; Fig 7 caption `n = 5 littermates per group`; Fig 4 `WT+RI n=9 · KO+W HD n=10`.

🔴 **The `n=5` / `n=4` disagreement the repository records is real and is recorded here as inherited, not
re-found:** `CC-20260814-42422765-01` and `paper_registry_current.md#PAPER 011` — *"In S2 le etichette del
grafico indicano `n=5`, la didascalia `n=4`"* (graph labels `n=5`, caption `n=4`). **Both are preserved; neither
is silently chosen.** ⚠️ **It concerns Supplementary Figure S2, which belongs to the Fig 1 promoter series —
it is NOT an LD/HD arm**, and must not be transferred there.

🔴 **The unequal 20:30 allocation is itself unexplained.** No allocation rule, no power calculation, no
randomisation statement (`randomi*` → 0 occurrences). An unequal allocation favouring the arm that succeeds
is not evidence of anything by itself, but it is **exactly the shape that a non-randomised, sequentially
enrolled study produces**, and the paper gives nothing that excludes it.

### 3.6 Litter, sex, background strain

| Variable | Verdict | Evidence |
|---|---|---|
| **Background strain** | 🟢 **REFUSED as a confound — matched and stated** | *"Mice were kept on an FVB (Friend leukemia Virus B) background"* |
| **Litter structure, LD vs HD** | 🔴 **UNSTATED.** No litter statement anywhere for Figs 3–7 | — (contrast: the S8 window arms **do** state *"at least three littermates treated per time point"* and *"WT littermates received identical injections"*) |
| **Sex composition per arm** | 🔴 **UNSTATED.** Two partial statements only | *"with no significant sex-dependent differences observed"* (body weight, Fig 3D) · *"both male and female HD-treated mice"* (behaviour, 3 mo) |
| **Maternal genotype / treatment status** | 🔴 **UNSTATED per arm, and the scheme guarantees it varies** — **T-2, §2.3** | *"Heterozygote or KO rescued mice (KO injected with AAV9-hSynI-hWWOX) were used for breeding to generate KO mice"* |
| **Housing** | 🟢 matched and stated | *"individual ventilated cages (IVC) … specific pathogen-free (SPF) facility under a 12-h light/dark cycle"* |

### 3.7 🔴 Which confounds are LIVE, ranked by how much of the apparent non-monotonicity each could account for

⚠️ **First, the question must be split, because the paper contains two different phenomena and only one of
them is a non-monotonicity.**

- **`N1` — the real one:** Fig 2's `8E10` arm *"rescue of lethality"* versus Fig 3's LD `1.23E11` *"did not
  survive to P90"*. A **1.5375× higher** dose appearing to do worse. **This is the non-monotonicity.**
- **`N2` — not a non-monotonicity at all:** the LD→HD survival step **within** Fig 3. It is **monotonic** and
  in the expected direction; what is anomalous is that it is **categorical** while the measured delivery and
  expression differences behind it are **not significant** in 3 of 4 regions and are called *"a trend"* by
  the authors on the protein axis. **That is an effect-size mismatch, not a monotonicity failure**, and
  conflating the two is the error this section exists to prevent.

#### Ranking for `N1` (the non-monotonicity)

| # | Confound | Could it account for `N1`? | Status |
|---|---|---|---|
| **1** | 🟢 **Follow-up-horizon mismatch** | ✅ **YES — ENTIRELY.** See §4.2 | 🟢 **CONFIRMED and sufficient.** `N1` **dissolves** |
| 2 | The `8E10` exponent is 🟡 MEDIUM (`8E11` would erase it) | yes, entirely — but **moot**, since #1 already dissolves it under either exponent | open, no longer load-bearing |
| 3 | Vector prep / lot (Fig 2 arms vs Fig 3 arms, different experiments, months apart) | yes, partly | 🔴 unstated |
| 4 | `n=5` (Fig 2 `8E10`) vs `n=20` (Fig 3 LD) | yes, partly — 5 animals to ~31 d is a weak basis for *"rescue of lethality"* | 🔴 inherited `A-fig` only |

#### Ranking for `N2` (the effect-size mismatch inside Fig 3)

| # | Confound | Share of `N2` it could account for | Status | Why |
|---|---|---|---|---|
| **1** | 🔴 **Vector prep identity — lot, empty:full, purification, formulation, true delivered titre** | **up to all of it** | 🔴 **UNSTATED, every row** (§3.2) | The nominal 2.1382× is a **label**, not a measurement of what entered the ventricle. Two independent preps can differ several-fold in **infectious** units at matched vg, and empty capsids compete for receptor. **Nothing in the paper constrains this** |
| **2** | 🔴 **Animal allocation — 20:30 unequal, no randomisation, no litter structure, maternal treatment status (T-2)** | **substantial** | 🔴 **UNSTATED** (§3.5, §3.6, §2.3) | A survival difference of this size is reachable by litter- or dam-confounding alone in a model whose untreated lifespan is ~3 weeks and whose primary systemic readout is glycaemia |
| **3** | 🔴 **Censoring / harvest-vs-death — no rule stated** | **bounds both curves; see §4.3** | 🔴 **UNSTATED**, `censor*` → 0 | **Direction matters:** harvest-as-event would depress **HD** (the arm harvested at P180/P240/P300), so it would **compress** the LD–HD gap, not create it. It therefore **cannot explain** `N2` — it can only mean the true gap is **larger** |
| **4** | 🟡 **Titration uncertainty — one qPCR, no CV, no orthogonal method** | **resizes, does not reverse** | 🟡 stated method, unquantified error | A nominal 2.1382× could be a true 1.3× or 3×. It moves where the threshold sits; it does not remove the categorical outcome difference |
| **5** | 🟡 **Age spread inside P0-P1 per arm** | **small** | 🔴 **UNSTATED**; bounded to 1 day (§3.3) | S8 shows P0–P5 is immaterial **at HD**; that result cannot be transferred to LD, so it is bounded-small rather than excluded |
| **6** | 🟢 **Volume / spread** | **none** | 🟢 **REFUSED — stated identical** | §3.1 |
| **7** | 🟢 **WPRE** | **none** | 🟢 **REFUSED — both arms −WPRE, stated** | §3.2 |
| **8** | 🟢 **Strain, route, technique, needle, rate, anaesthesia, housing, titration method** | **none** | 🟢 **REFUSED — stated identical** | §2.1 |
| **9** | 🟡 **Sex composition** | **unquantifiable** | 🔴 **UNSTATED** | the only sex statement is a null on body weight |

🔴 **The ranking's own conclusion, stated because it is a finding and not a shrug:** **the confounds do NOT
explain `N2`.** Every confound that is *stated* is *matched*; every confound that could plausibly carry the
effect is *unstated*. The two live candidates — prep identity and allocation — are live **precisely because
the paper reports nothing about them**, so their magnitude is unbounded in both directions. ⇒ **`N2` is not
explained away, and it is also not evidence of biology.** It is an **unresolvable-from-this-paper** effect-
size mismatch, and the honest label is exactly that.

⚪ **And what `N2` is NOT.** It is **not** a biological non-monotonicity and this file does not infer one.
LD→HD survival is monotonic and in the expected direction.

---

## 4 · The follow-up-horizon test, answered explicitly

### 4.1 For **LD versus HD** (`N2`) — 🟢 **the horizon is MATCHED, and a horizon mismatch is EXCLUDED**

**Q1 · Were LD and HD animals observed to the same endpoint date?**

# 🟢 **YES — by construction, and the construction is the proof.**

LD and HD are **two arms of one Kaplan–Meier panel**, Figure 3B. `A-fig`, pixel-level, with a declared crop
recipe (`CC-20260826-DOSE-ADJUDICATION-01` §1: `gr3.jpg`, crop `(436, 0, 726, 297)`, ×4.5): **the x-axis runs
to 300 days and both arms are plotted on it.** A single KM panel cannot give its arms different horizons.

**And the stronger argument, which does not need the panel at all:** 🔴 **the LD curve reaches 0%.** A
Kaplan–Meier estimator cannot reach zero while any animal is censored — censored animals hold the curve
above zero permanently. ⇒ **the LD arm is fully observed, every animal an event, no truncation.**

🟢 **Independently corroborated in running text, with no figure involved:** *"**LD-treated mice did not
survive to P90**; therefore, analyses were limited to WT and HD-treated groups."* That is a plain mortality
statement in the Results, read by me in-act on `S-body`.

⇒ # 🔴 **A follow-up-horizon mismatch CANNOT explain the LD–HD survival difference. The test is answered NO.**

**Q2 · Were survivors censored differently between LD and HD?**

🔴 **`ABSENT` — and the absence is total.** `censor*` → **0 occurrences in 48,780 characters, measured.** The
Methods give the test and nothing else: *"Survival was analyzed using Kaplan-Meier curves with significance
assessed by the log-rank (Mantel-Cox) test."* **No censoring rule, no humane endpoint, no
removal-for-analysis statement, no per-arm animal flow.** See §4.3 for why this still matters even though
Q1 is answered.

⚠️ **What the asymmetry after P90 is, and what it is not.** LD is absent from behaviour (3 mo), fertility,
ECoG, sciatic nerve, and every expression timepoint ≥3 months. **That asymmetry is a CONSEQUENCE of the
survival difference, stated as such by the authors** — *"LD-treated mice did not survive to P90; therefore,
analyses were limited to WT and HD-treated groups."* **Direction of causation: survival → missing LD data,
not missing LD data → apparent survival difference.** It is a real and severe limit on what can be said about
LD at any late endpoint, and it is **not** a horizon artefact.

### 4.2 For the actual non-monotonicity `N1` — 🟢 **a horizon mismatch is CONFIRMED, and it is sufficient**

**The two sentences, both read by me in-act on `S-body`:**

> *"Increasing the dose of the WPRE-lacking vector to **8 × 10vg** was associated with improved outcomes,
> **including rescue of lethality** and normalization of growth and glucose levels."* — Fig 2

> *"**LD-treated mice did not survive to P90**"* — Fig 3, LD = `1.23E11`

`1.23E11 / 8E10 = **1.5375**` — a 1.54× higher dose apparently failing where a lower one rescued.

🟢 **The horizons are NOT the same, and the repository already holds the pixel-level measurement.**
`CC-20260826-DOSE-ADJUDICATION-01` §6, with the crop recipe declared in its §1:

> 🔴 *"Read at pixels, **Figure 2B's x-axis ends at 50 days**. The `8 × 10¹⁰` arm (n = 5, magenta) is flat at
> 100 % to ~31 d; the `4 × 10¹⁰` arm (n = 3, yellow) falls to ≈33 % by ~20 d with one animal censored at
> ~25 d; untreated KO reaches 0 % at ~19 d."*
>
> *"⇒ **'Rescue of lethality' in Figure 2 means 'alive at about 31 days'.** In Figure 3, followed to 300 days,
> the same word means 'alive at 300 days'. **`NOMENCLATURE_CONFLICT`, not a true contradiction.**"*

**The arithmetic that closes it.** Untreated KO die by ~18–19 d. The Fig 3 LD arm *"declines from ~20 d,
reaches 0% by ~80 d"* (`A-fig`) — **so at 31 days the LD arm is still substantially alive.** ⇒ **placed on
Figure 2's 50-day axis, the LD arm would also read as "rescue of lethality."**

# 🟢 **`N1` DISSOLVES. The two sentences are both true, describe different observation windows, and do not conflict. There is no dose inversion.**

🔵 **And this is why the exponent question is moot.** The prior forensics node rated the `8E10` exponent
🟡 MEDIUM and noted that `8E11` would erase the tension. **Under the horizon reading the tension is erased at
either exponent**, so `N1` no longer rests on that exponent at all. The exponent remains worth closing for
the *dose-series* record; it is no longer load-bearing for the contradiction.

### 4.3 🔴 What the missing censoring rule still costs, even though §4.1 answers the test

The paper harvests tissue from **treated animals** at **P30, ~3 months, P180, P240 and P300** (Fig 5, S5,
S6 — all read by me on `S-body`). Those animals leave the colony. **The paper states no rule for how they
enter the survival analysis.** `censor*` → 0.

🔴 **This is not hypothetical for this laboratory.** `CC-20260826-DOSE-ADJUDICATION-01` §7 documents the
predecessor paper (`PMID 34747138`, Repudi 2021, same senior author) plotting a Kaplan–Meier whose **legend
states 6 animals alive and 4 removed for analysis while the curve reaches 0%** — i.e. **censored animals
plotted as events**, an internal inconsistency the repository classifies `UNRESOLVED`.

**Three consequences, stated with their directions so none is over-read:**

1. 🟡 **It may explain the WT+RI arm.** `A-fig` reports vehicle-injected **WT at ≈72% by 300 d** — wild-type
   mice are not dying at 28% by ten months. **Harvest plotted as death is the most economical explanation**,
   and the alternative — real procedure-attributable mortality in WT — would be a serious finding in its own
   right. **The paper distinguishes neither.**
2. 🟢 **It cannot manufacture the LD–HD gap.** The harvested timepoints ≥P90 exist **only in HD**. Harvest-as-
   event therefore depresses **HD**, compressing the gap. ⇒ **if this artefact is present, the true LD–HD
   separation is LARGER than plotted, not smaller.** `N2` is not rescued by it.
3. 🔴 **It does bound the LD curve's *shape*.** Whether LD's decline from ~20 d is pure mortality or partly
   P30 harvest (Fig 5's vDNA/mRNA/protein panels require LD brains at P30) **cannot be determined**. ⚠️ **But
   the threshold reading does not depend on the shape:** *"LD-treated mice did not survive to P90"* is a
   running-text mortality statement with no figure behind it. **The endpoint survives; the curve's
   intermediate shape does not.**

---

## 5 · What is `ABSENT` from the paper entirely, and the single record that would supply it

### 5.1 The absence inventory

| # | Absent item | Measured basis | Blocks what |
|---|---|---|---|
| 1 | **Titre (vg/µL or vg/mL) for any arm** | no titre value anywhere in `S-body` | any statement about delivered concentration; any cross-study transfer |
| 2 | **Dose unit denominator** | bare `vg`, 7/7 occurrences; `GC`/`per animal`/`total dose` → 0 | the absolute axis, ±2× (closed, §0) |
| 3 | **Any dose at all in the Methods** | all 7 `vg` tokens in Results/Discussion; Methods carry volume, rate, coordinates, needle, titration, four vendors — and no dose | is the structural cause of #1 and #2 |
| 4 | **Vector lot / manufacturer per arm** | `lot`, `batch` → 0; four sources listed, two constructs assigned | whether LD and HD are the same material |
| 5 | **Empty:full capsid ratio** | `capsid`, `empty` → 0 | total capsid dose; receptor competition |
| 6 | **Purification route, formulation buffer, endotoxin** | `purif`(vector), `iodixanol`, `chromatog`, `affinity`, `endotoxin` → 0 | prep equivalence |
| 7 | **Whether LD is a dilution of HD or an independent prep** | never stated | which of #4–#6 even apply |
| 8 | **Titration uncertainty (CV, replicates, orthogonal method)** | one method stated, no error | whether 2.1382× is 1.3× or 3× |
| 9 | **`n` per arm** | `n =` → **0 occurrences**; Methods defer to *"the figure legends"* | every effect size; the 20:30 imbalance |
| 10 | **Allocation / randomisation rule** | `randomi*` → 0 | whether LD/HD assignment is confounded with litter or dam |
| 11 | **Censoring rule; harvest-vs-death accounting** | `censor*` → 0 | the shape of every KM curve, incl. WT+RI at ≈72% |
| 12 | **Litter and dam identity per arm; maternal treatment status (T-2)** | no statement for Figs 3–7 | the metabolic endpoints above all |
| 13 | **Sex composition per arm** | two partial statements only | any sex-stratified reading |
| 14 | **Age distribution inside P0-P1 per arm** | range stated, distribution not | a bounded developmental confound |
| 15 | **A low-dose window experiment** | S8 is **HD only** — *"using the high-dose vector"* | whether the P0–P5 window is dose-dependent |
| 16 | **An intermediate dose arm between `1.23E11` and `2.63E11`** | none exists | where the threshold sits |
| 17 | **Follow-up horizon for the Fig 1 and Fig 2 arms, in text** | no duration statement in either passage | recovered from pixels only (`A-fig`), never from the paper's prose |
| 18 | **WPRE status of the CBA construct (T-1)** | the Methods list omits CBA | the CMV/CBA grouping in Fig 1 |

### 5.2 The single record that would supply the most

**If only one record can be obtained: the per-arm animal-flow and censoring table** — n enrolled, n injected,
n dead by date, n harvested by date, n censored, litter and dam of origin, sex, exact injection day, per arm.
🔵 **Reason it outranks the vector CoA:** it decides whether the survival observation is an **observation** at
all (#9, #10, #11, #12, #13, #14, and the WT+RI ≈72% anomaly). **Establishing a mechanism for an artefact is
wasted work**, so the record that tests whether the phenomenon is real must come first.

**Second, and the one that would decide the mechanism: the Certificate of Analysis for the LD and HD
material** — titre by two orthogonal methods with CV, empty:full by AUC or cryo-EM, purification route,
formulation buffer, endotoxin, lot identity, and **whether LD is a dilution of the HD stock**. This supplies
#1, #4, #5, #6, #7 and #8 in one document.

🔵 **A CoA would also settle the closed unit question as a free by-product, and this is a discriminant nobody
has named.** The derived stock titres required are: **total reading — LD `3.075E13`, HD `6.575E13` vg/mL;
per-hemisphere reading — LD `6.15E13`, HD `1.315E14` vg/mL.** A single printed stock titre on a CoA picks one
pair and therefore fixes `u`. ⚪ **No claim is made here about which is achievable** — that is exactly the
point: the CoA would answer it by measurement rather than by anyone's recollection of manufacturing limits.

**Third, figure-level, if no record can be had: the Figure 3 legend at native resolution** (n per arm, the
P values, and any censoring tick marks) — this is the surface every `A-fig` value in this file came from and
the one this deployment cannot reach.

### 5.3 🆕 A cross-study test run here, and it is negative — which is the result

**The repository's `VG_DOSE_ALONE_IS_NOT_TRANSFERABLE` finding** (`CC-20260826` §5) rests on total vg. I
tested whether **concentration** is the transferable quantity instead, since §3.1 shows concentration is what
actually differs between arms at fixed volume.

`PMID 34747138` (Repudi 2021, same laboratory, same FVB background, same AAV9-hSynI-hWWOX architecture,
**WPRE-free**, same qPCR/bGH titration): `2E10 GC/hemisphere` in ~1 µL ⇒ **`2.0E10 GC/µL`**, `4.0E10` total.

| Comparison | total reading | per-hemisphere reading |
|---|---|---|
| Obeid **LD** vs Repudi — **total** | **3.075×** higher | **6.15×** higher |
| Obeid **LD** vs Repudi — **concentration** | **1.538×** higher | **3.075×** higher |
| Obeid **HD** vs Repudi — **total** | 6.575× | 13.15× |
| Obeid **HD** vs Repudi — **concentration** | 3.288× | 6.575× |

**Outcome:** Repudi ≈93% at 270 d (`A-repo`, pixel); Obeid LD **0% by ~80 d**.

# 🔴 **Obeid's LD exceeds Repudi's dose on BOTH total vg AND vg/µL, under BOTH unit readings, and performs far worse.**

⇒ **Concentration is no more transferable than total vg.** The `VG_DOSE_ALONE_IS_NOT_TRANSFERABLE` finding
**extends to vg/µL** and is strengthened, not weakened, by the volume analysis. ⚠️ **And this comparison is
not a non-monotonicity claim:** the two studies differ on **injection technique** (free-hand vs stereotaxic),
**volume** (1 vs 2 µL/hemisphere), **prep** and **year**, all unmatched. It is recorded as a **negative result
about transferability**, which is what it is.

---

## 6 · What I could not establish

| Item | Why | What would close it |
|---|---|---|
| **Any figure legend, `n`, or P value by my own read** | 🔴 `S-body` carries **zero** `n =` tokens and no legends; `files/` absent from this worktree; all four egress routes 403 (control also 403) | the shared `files/` tree, or one open route to JATS/publisher markup |
| **Whether LD and HD are the same lot** | 🔴 unstated; 0 occurrences of `lot`/`batch` | vector CoA, or the authors |
| **Whether LD is a dilution of HD** | 🔴 unstated | vector CoA |
| **Empty:full, purification, endotoxin, formulation** | 🔴 0 occurrences each | vector CoA |
| **Whether Fig 3B's curves are mortality or mortality + harvest** | 🔴 no censoring rule; the predecessor paper has a documented censored-as-event inconsistency (`CC-20260826` §7) | per-arm animal-flow table |
| **Why WT+RI sits at ≈72% at 300 d** | 🔴 `A-fig` only; no text statement; no censoring rule to interpret it against | same table |
| **Per-arm sex, litter, dam, exact injection day** | 🔴 unstated | same table |
| **The `8E10` exponent (🟡 MEDIUM)** | 🔴 `gr2.jpg` unreachable to me | a native-resolution Fig 2 read — **but §4.2 makes it non-load-bearing** |
| **The `n=5` vs `n=4` S2 discrepancy** | 🔴 inherited; I could not open S2. It belongs to the **Fig 1 series**, not LD/HD | the S2 caption at full resolution |
| **The WPRE status of the CBA construct (T-1)** | 🔴 the Methods list omits CBA and gives no cassette map | Fig 1A / S1 vector maps |
| **Whether the 3-in-4 `ns` vDNA result reflects true equivalence or low power** | 🔴 no per-region `n`, no variance, no power statement | Fig 5 legend + source data |
| **Whether the LD arm's P30 tissue harvest removed animals from its survival curve** | 🔴 Fig 5 requires LD brains at P30; no accounting given | per-arm animal-flow table |

---

## 7 · Findings this node adds, and one process note

**T-1** — `CBA` is omitted from the Methods sentence that assigns WPRE, and is the only construct sourced
from a different manufacturer. **Its WPRE status is `ABSENT`, not "same as the other ubiquitous promoters."** (§2.3)

**T-2** — 🔴 **The breeding scheme makes maternal genotype/treatment status a per-arm variable, and the paper
never reports its distribution.** *"Heterozygote or KO rescued mice (KO injected with AAV9-hSynI-hWWOX) were
used for breeding."* In a study whose principal systemic endpoint is **blood glucose**, that is a live
metabolic confound. **Not held by the repository or by the prior forensics node.** (§2.3, §3.7)

**T-3** — 🟢 **Volume is a stated constant, so HD is a concentration difference and not a spread difference.**
This **refuses** one of the two candidate mechanisms outright and is a determination, not an inference. (§1, §3.1)

**T-4** — 🟢 **The follow-up-horizon test is answered in both directions:** matched for LD vs HD (one KM panel;
the LD curve reaches 0%, which censoring forbids), and **confirmed as the full explanation of `N1`** (Fig 2's
axis ends at 50 d; *"rescue of lethality"* there means *alive at ~31 d*). (§4)

**T-5** — 🔴 **No censoring rule exists, the paper harvests treated animals at five timepoints, and the
predecessor paper has a documented censored-as-event inconsistency.** Direction established: this **cannot
create** the LD–HD gap and **can only compress** it. (§4.3)

**T-6** — 🔴 **Concentration is not transferable across studies either.** Obeid LD exceeds Repudi on both
total vg and vg/µL under both unit readings and performs far worse. (§5.3)

**T-7** — ⚪ **Process note, recorded because the repository names this failure class itself.**
`tx007_dose_unit_forensics_20260922.md` §6.2 lists the follow-up-horizon mismatch as *"now the leading
explanation"* and §8 records the Fig 2 horizon as **unverified** — *"the ~50 d figure is a prior-session panel
read"*. But `CC-20260826-DOSE-ADJUDICATION-01` §6, dated **2026-08-26**, already carried that measurement at
pixel level **with a declared, reproducible crop recipe**, and drew the `NOMENCLATURE_CONFLICT` conclusion in
full. **The repository held the answer for four weeks while a later node re-opened it as unknown.** Same class
as the repository's own `O-4` and the S8 episode: *an artefact declared unavailable while another actor held
it.* **The remedy that would have worked here is cheap: search the commit-candidate queue for the figure
number before declaring a figure-level question open.**

**T-8** — ⚪ **A superseded panel read, reconciled rather than left contradicting.**
`PMID42422765_partial_locators.md` records the Fig 2B `8E10` arm as *"dead ~17 days"* — and **flags its own
read as unreliable** (*"the 2B legend has five arms in similar colours at 104 ppi, and I have already made two
colour-and-label errors on this paper … logged as to re-verify, with the presumption in favour of the text"*).
`CC-20260826` §6 re-read the same panel at **×4.5 with a declared crop** and found the `8E10` arm **flat at
100% to ~31 d**, which **agrees with the running text**. ⇒ **the higher-resolution read supersedes; the
dossier's own caveat was correct and is now discharged.** Recorded so the superseded value is not re-found as
a live contradiction.

---

## 8 · Reading debt and scope declaration

**No new PMID is introduced as a premise.** Every PMID named — `42422765`, `34747138` — is already a premise
of `tx007_dose_challenge_20260922.md` and `CC-20260826-DOSE-ADJUDICATION-01`, and is already covered by an
existing registry record and receipt. **No `FT-` identifier is cited in this file**, so no manifest crosscheck
is opened. **No new reading debt.**

🔴 **Outstanding debt this node did not pay and does not claim to have paid:** every figure legend, every `n`,
every P value in `PMID 42422765` remains unread **by me**; all such values in this file are labelled `A-fig`
and are another actor's attestation. **The `files/` evidence tree is absent from this worktree and every
egress route is closed**, so the debt is recorded rather than discharged.

**No researcher email or contact detail appears anywhere in this file. No individual-level record appears
anywhere in this file.**

---

## 9 · Source attribution

**According to PubMed**, and retrieved from **PubMed / PubMed Central** in this act.

| PMID | Citation | DOI |
|---|---|---|
| **42422765** | Obeid M, Akkawi R, Repudi S, Singh PK, Abudiab B, Jebara T, Berent A, Brennan T, Weiss Y, Shekh-Ahmad T, Aqeilan RI. *Neuron-specific WWOX gene therapy produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy.* **Molecular Therapy Advances** (`Mol Ther Adv`) 2026;34(3):201791. PMCID `PMC13343157`. **Full body (48,780 chars) fetched and read in-act; no figures, no legends** | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) |
| **34747138** | Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI. *Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes.* *EMBO Mol Med* 2021;13(12):e14599. PMCID `PMC8649866`. **Not re-fetched in this act; used only through repository attestations, and labelled as such** | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |

**Repository artefacts read in full and cited above:**
[`tx007_dose_unit_forensics_20260922.md`](tx007_dose_unit_forensics_20260922.md) ·
[`CC-20260922-TX007-DOSE-CHALLENGE-01.md`](../research/commit_candidates/CC-20260922-TX007-DOSE-CHALLENGE-01.md) §10 ·
[`CC-20260826-DOSE-ADJUDICATION-01.md`](../research/commit_candidates/CC-20260826-DOSE-ADJUDICATION-01.md) §§1,4,6,7 ·
[`CC-20260814-42422765-01.md`](../research/commit_candidates/CC-20260814-42422765-01.md) ·
[`PMID42422765_partial_locators.md`](../research/fulltext_dossiers/PMID42422765_partial_locators.md) ·
[`discovery_ledger_current.md`](../research/discovery_ledger_current.md) `DL-MECH-009`.

---

**End of file — complete run.** Read-only toward every canonical file, every registry, the receipt ledger and
the state manifest. Nothing promoted, nothing committed, no git operation run, no BATCH_COMMIT. **No molecule,
no dose recommendation, no route recommendation, no safety claim, no druggability score.** Every dose recorded
above is what a published experiment administered to mice. **Not medical advice.**
