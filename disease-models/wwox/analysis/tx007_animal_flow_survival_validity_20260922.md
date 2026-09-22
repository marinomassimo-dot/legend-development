# `TX-007` — animal flow and survival validity: what happened to every animal, and what the survival data actually license

**Date:** 2026-09-22 · **Actor:** Scientist A · **Node:** `TX007_ANIMAL_FLOW_SURVIVAL_VALIDITY`
**Question dispatched:** *What exactly happened to every animal entering the TX-007 survival experiment,
and what survival conclusions are actually licensed by those data?*

**Primary source:** `PMID 42422765` / `PMC13343157` — Obeid M, Akkawi R, Repudi S, Singh PK, Abudiab B,
Jebara T, Berent A, Brennan T, Weiss Y, Shekh-Ahmad T, Aqeilan RI. *Neuron-specific WWOX gene therapy
produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy.*
**`Mol Ther Adv`** (*Molecular Therapy Advances*) 2026;34(3):201791.
DOI [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791).
**Predecessor:** `PMID 34747138` / `PMC8649866` — Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI.
*Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes.* *EMBO Mol Med* 2021;13(12):e14599.
DOI [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599).
**According to PubMed**, and both bodies retrieved from **PubMed Central** in this act.

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries,
> the receipt ledger, every queue and the state manifest. Nothing here changes a claim, a paper record, the
> working model or any queue. **No git operation was run by this node. No `BATCH_COMMIT`.**
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> 🔴 **BLOCK-1, stated once and binding over every line below.** **No molecule is named as a therapy, no
> dose is recommended, no route is recommended, no safety claim is made, no druggability score is given.**
> Every number below records **what a published experiment did to mice**, reconstructed so the experiment can
> be audited. **Reporting a dose a paper used is not recommending it.** *"No overt toxicity observed"* is
> never *"safety established"*. **Nothing here is medical advice**; it is material for discussion with a
> treating clinical team and for nobody else.

---

## 0 · Surfaces, and the provenance ceiling — declared before any number is used

| Surface | Code | How obtained | What it carries |
|---|---|---|---|
| **Obeid 2026 PMC served body, 48,780 chars** | **`S-body`** | 🟢 **fetched and read by me in-act**, `get_full_text_article(pmc_ids=["PMC13343157"])` | Introduction, 7 Results sections, Discussion, **complete Materials and methods**. 🔴 **No figure legends. `n =` → 0 occurrences (measured by me). No P values. Exponents deleted** (`1.23 × 10vg`) |
| **Repudi 2021 PMC served body** | **`S-2021`** | 🟢 **fetched and read by me in-act**, `get_full_text_article(pmc_ids=["PMC8649866"])` | Full text **including complete figure legends with `n`, exit counts and log-rank statements** — the 2026 paper's legends are absent from its own served surface while the 2021 paper's are present |
| Prior-session figure / caption renderings | **`A-fig`** | 🔴 **INHERITED ATTESTATION — I could not open any of them.** `files/` is **absent**, verified by me (`ls files` → no such file; `find / -name "mmc1.pdf"` → nothing) | Fig 3B pixel reads; per-arm `n`; the Fig 1, 3, 5 and 7 caption quotations; the S8 panel reads |
| Repository artefacts | **`A-repo`** | 🟢 read by me in-act | `tx007_per_arm_delivery_reconstruction_20260922.md` (638 ll.) · `tx007_saturation_hypothesis_20260922.md` · `CC-20260826-DOSE-ADJUDICATION-01.md` §§4,6,7 · `CC-20260826-DOSE-DECISION-TABLE-01.md` · `CC-20260922-TX007-DOSE-CHALLENGE-01.md` §9 · `PMID42422765_partial_locators.md` (889 ll.) |

🔴 **Every value marked `A-fig` is another actor's attestation that I could not verify. It is labelled as
such at every use and never relayed as my own read.** Where a conclusion of mine depends on an `A-fig`
value, that dependency is stated in the conclusion itself.

**Egress, attempted once by me and recorded once — not a scientific stop.**
`https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13343157/fullTextXML` → **`000`, blocked at CONNECT** ·
**control `https://example.com` → `000`, identically blocked.** ⇒ **allowlist, not a paper-specific block.**
The caption-bearing surface is unreachable from this deployment. Established first-hand, not retried.

🔴 **Exponent discipline.** Every dose below is in **E-notation**, the only exponent-safe form.
🆕 **One first-hand exponent recovery:** the Discussion of `S-body` contains the literal string **`(4E10)`**
— *"We also cannot exclude that the optimal dose was not achieved, as all vectors were tested at the same
titer (4E10)."* The authors themselves wrote E-notation there, so this one exponent **survived the parser**
and is now first-hand rather than inherited. Every other exponent in the paper is deleted on this surface.

---

## 1 · The answer, before the tables

> **What happened to every animal entering the TX-007 survival experiment?**

# 🔴 **It cannot be established. For no arm of the 2026 paper can a single animal be assigned an exit category from the paper's own text. `NOT RECONSTRUCTABLE`, per arm, for every arm.**

**The measured basis, first-hand on `S-body`, word-boundary counts by me in-act:**

| Token | Occurrences in 48,780 chars | Consequence |
|---|---|---|
| `censor*` | **0** | no censoring rule, no censoring statement, no sensitivity analysis |
| `euthan*` · `humane` · `moribund` · `sacrific*` · `harvest` | **0 each** | **no humane endpoint is defined anywhere**, and no word for a scheduled kill exists in the paper |
| `n =` / `n=` | **0** | no arm's enrolment is readable by me; Methods defer to *"the figure legends"* |
| `randomi*` · `allocat*` · `power` | **0 each** | no allocation rule, no randomisation, no power calculation |
| `lot` (word) · `batch` · `capsid` · `empty` · `endotoxin` · vector `purif*` · `dilut*` | **0 each** | the vector-prep chain is unreported end to end |
| `dam` / `dams` · `maternal` | **0 each** | the breeding variable the Methods create is never characterised |
| `at risk` · `follow-up` · `cohort size` | **0 each** | no numbers-at-risk table, no follow-up statement |

**And what the paper does contain, which makes the absence structural rather than incidental:**

> *"Exact sample sizes () and values are reported in the figure legends."* — Statistical analysis, `S-body`,
> read verbatim by me. **The parenthetical `(n)` and the word `p` are themselves deleted from that sentence.**

> *"**Data and code availability**: Not relevant."* — `S-body`, verbatim, read by me in-act. 🆕 **First-hand.**
> ⇒ **There is no deposited source data to request.** The animal-flow record, if it exists, exists only with
> the authors or the IACUC protocol.

🎯 **But three things ARE forced by the data, and they are the substance of this node:**

1. 🆕 **The paper's only acknowledgement that treated animals died is one clause**, and it also proves that
   post-mortem tissue entered the expression analysis: *"Notably, **mice from either treatment group that
   failed to survive** exhibited reduced WWOX expression, reinforcing the link between effective protein
   restoration and survival (A–S5D)."* (`S-body`, ~3-month paragraph, read verbatim by me.) **This is the
   whole of the paper's mortality reporting for the LD and HD arms.**
2. 🆕 **The Methods state a terminal procedure applied to the wild-type arm inside the survival window:**
   *"Mice (**WT**, KO, and KO injected mice) at different ages (**P10‑P180**) were deeply anesthetized using
   an overdose of ketamine and xylazine and then transcardially perfused using 4% paraformaldehyde
   (PFA)/PBS."* (`S-body`, Immunohistochemistry, verbatim.) **WT animals were killed for tissue between P10
   and P180 — and no rule says how they enter the Kaplan–Meier.**
3. 🆕 **Under any single analysis convention, the harvested animals cannot have been inside the survival
   denominators.** Derivation in §3.2. This is a *forced* result given two inherited pixel attestations, and
   it **corrects the repository's standing presumption** that harvest-plotted-as-death is the leading
   explanation of the WT+RI plateau.

---

## 2 · Per-arm reconstruction

### 2.0 · Arms as the paper defines them, and which figure carries each

| ID | Arm | Figure | Genotype | Vector | Transgene species | WPRE | Nominal dose |
|---|---|---|---|---|---|---|---|
| **A1** | EF1α | Fig 1 / S1 / S2 | KO | AAV9 | **human** (`hWWOX`) | ✅ **STATED** | `4E10` |
| **A2** | CMV | Fig 1 / S1 / S2 | KO | AAV9 | human | ✅ **STATED** | `4E10` |
| **A3** | CBA | Fig 1 / S2 | KO | AAV9 | human | 🔴 **ABSENT — see §2.4 T-1** | `4E10` |
| **A4** | MBP | Fig 1 / S1 / S2 | KO | AAV9 | human | ✅ **STATED** | `4E10` |
| **A5** | hSynI **+WPRE** | Fig 1 / S1 | KO | AAV9 | human | ✅ **STATED** | `4E10` |
| **B1** | hSynI **−WPRE** | Fig 2B / S3 | KO | AAV9 | human | ❌ **STATED absent** | `4E10` |
| **B2** | hSynI **+WPRE** | Fig 2B / S3 | KO | AAV9 | human | ✅ **STATED** | `4E10` |
| **B3** | hSynI **−WPRE** | Fig 2B / S3 | KO | AAV9 | human | ❌ **STATED absent** | `8E10` |
| **B-WT** | WT reference in Fig 2B | Fig 2B | WT | — | — | — | 🔴 **ABSENT** whether RI or nothing |
| **B-KO** | untreated / control KO in Fig 2B | Fig 2B | KO | — | — | — | 🔴 **ABSENT** |
| **C0** | **KO + RI** | Figs 3–7 | KO | vehicle | — | — | vehicle: *"PBS with 5% sorbitol and 0.001% pluronic F-68"* (**STATED**) |
| **C1 = LD** | KO + hSynI −WPRE | Figs 3–7, S4–S7 | KO | AAV9 | human | ❌ **STATED absent** | **`1.23E11` vg** |
| **C2 = HD** | KO + hSynI −WPRE | Figs 3–7, S4–S7 | KO | AAV9 | human | ❌ **STATED absent** | **`2.63E11` vg** |
| **C3** | **WT + RI** | Figs 3–7 | WT | vehicle | — | — | vehicle |
| **D1,D2,D3,D5** | window arms **shown** | S8 | KO | AAV9 | human | ❌ (HD vector) | `2.63E11` |
| **D0, D4** | window arms **stated but not shown** | — | KO | AAV9 | human | ❌ | `2.63E11` — 🔴 **see §2.4 T-5** |
| **D-WT / D-KO** | S8 controls | S8 | WT / KO | vehicle | — | — | vehicle |
| **E** | **fertility / breeding cohort** | S4C–S4E | KO **HD-treated**, WT, **Het** | AAV9 / — | human | ❌ | `2.63E11` |
| **F** | **ECoG cohort** | Fig 7 | WT, KO+RI, KO+AAV | AAV9 | human | ❌ presumed | 🔴 **dose ABSENT in Methods**; Results say *"HD"* |

🔴 **Arms `E` and `F` are cohorts the repository has never listed as arms.** They consumed animals, they are
not in any Kaplan–Meier, and their disposition is unstated. They are the reason §2.3's arithmetic does not
close.

---

### 2.1 · 🔴 The main survival arms (Fig 3B) — every field requested, cell by cell

**Legend:** `STATED` = printed in the paper on a surface named · `DERIVED` = arithmetic shown ·
`ABSENT` = the paper is silent · **`A-fig`** = inherited attestation, **not my read**.

| Field | **C3 · WT+RI** | **C0 · KO+RI** | **C1 · LD** | **C2 · HD** |
|---|---|---|---|---|
| **Genotype** | WT — **STATED** (`S-body`, Fig 3 text) | KO — **STATED** | KO — **STATED** | KO — **STATED** |
| **Vector** | vehicle (RI) — **STATED** | vehicle (RI) — **STATED**: *"KO mice injected with the reference item (RI)"* | AAV9 — **STATED** | AAV9 — **STATED** |
| **Transgene species** | — | — | **human `hWWOX`** — **STATED** (*"AAV9-hSynI-hWWOX"*) | **human** — **STATED** |
| **WPRE** | — | — | ❌ **absent — STATED**: *"we generated AAV9-hSynI-WWOX vectors **lacking the WPRE element**"*, the same sentence pair that introduces both doses | ❌ **absent — STATED, same sentence** |
| **Nominal dose** | — | — | **`1.23E11` vg — STATED**: *"an LD (1.23 × 10vg)"*, exponent from `A-fig` Fig 3A + S7I caption | **`2.63E11` vg — STATED**, same sentence; exponent `A-fig` |
| **Unit denominator** | — | — | 🔴 **ABSENT** — bare `vg`; `vg/` → **0**, `GC/` → **0**, `per animal` → **0** (measured by me) | 🔴 **ABSENT**, identically |
| **N enrolled** | 🔴 **ABSENT on `S-body`.** `A-fig`: **20** | 🔴 **ABSENT.** `A-fig`: **10** | 🔴 **ABSENT.** `A-fig`: **20** | 🔴 **ABSENT.** `A-fig`: **30** |
| **Sex** | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT as composition.** Two partial statements only: *"no significant sex-dependent differences observed"* (body weight) and *"both male and female HD-treated mice"* (behaviour) |
| **Maternal / breeding background** | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT — and the scheme guarantees it varies.** §6 | 🔴 **ABSENT — same.** §6 |
| **Age at treatment** | **`P0-P1` — STATED**: *"All preceding treatments were administered at P0‑P1"* | **`P0-P1` — STATED**, same sentence | **`P0-P1` — STATED.** Within-arm distribution **ABSENT** | **`P0-P1` — STATED.** Distribution **ABSENT** |
| **Route** | bilateral ICV, stereotaxic, `2.0 µL/hemisphere`, `1–1.5 µL/min`, 32G Hamilton, lambda-relative `±0.8 / 1.5 / −1.6 mm`, hypothermia anaesthesia — **STATED** in the one Methods paragraph covering *"AAV9-hWWOX **or RI** delivery"* | **identical — STATED by that same paragraph** | **identical — STATED** | **identical — STATED** |
| **Follow-up horizon** | Fig 3B x-axis to **300 d** — `A-fig` pixel, crop recipe declared in `CC-20260826` §1. 🔴 **ABSENT from the prose**; the only textual reference is *"By the study endpoint"*, undefined | same panel, same axis | same panel, same axis | same panel, same axis |
| **Scheduled tissue-harvest times** | **P10–P180 — STATED** (IHC Methods, terminal, names WT explicitly) | **P10–P180 — STATED** (same sentence names KO) | **P30 — DERIVED** from Fig 5A–5L (vDNA + mRNA + protein at P30, LD arm present). ~3 mo **DERIVED** from S5A–S5D via *"either treatment group that failed to survive"* | **P30 · ~3 mo · P180 · P240 · P300 — DERIVED** from Fig 5, S5A–S5D, S5E–S5G, S5J–S5K, S6B–S6D, plus **sciatic nerve** (S6E–S6G) and **liver** (S6H), all terminal |
| **Number harvested at each time** | 🔴 **ABSENT — every timepoint** | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT** |
| **Spontaneous deaths** | 🔴 **ABSENT.** No count, no statement | 🔴 **ABSENT as a count.** Discussion: untreated survival *"approximately three weeks"* | 🔴 **ABSENT as a count.** *"LD-treated mice did not survive to P90"* is a qualitative mortality statement | 🔴 **ABSENT as a count.** The only acknowledgement is *"mice from **either treatment group** that failed to survive"* |
| **Euthanised for humane endpoints** | 🔴 **ABSENT.** `humane` · `euthan*` · `moribund` → **0** each. **No humane endpoint is defined in this paper** | 🔴 **ABSENT** — and this is the arm where it matters most | 🔴 **ABSENT** | 🔴 **ABSENT** |
| **Number censored** | 🔴 **ABSENT.** `censor*` → **0** | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT** |
| **Number remaining at each horizon** | 🔴 **ABSENT as a count.** `A-fig` **fractions only**: 100% → ≈90% (~50 d) → **≈72%, flat to 300 d** | `A-fig`: **0% by ~18 d** | `A-fig`: declines from ~20 d, **0% by ~80 d**. Corroborated in prose, read by me: *"LD-treated mice did not survive to P90"* | `A-fig`: **≈78% at ~85 d, flat to 300 d** |
| **Denominator used** | 🔴 **ABSENT.** No numbers-at-risk row; `at risk` → 0 | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT** |
| **KM treatment of removed animals** | 🔴 **ABSENT — the central gap.** §3 | 🔴 **ABSENT** | 🔴 **ABSENT** | 🔴 **ABSENT** |
| **Statistical comparison performed** | **Kaplan–Meier + log-rank (Mantel–Cox) — STATED** (Statistical analysis, verbatim, read by me). **No sensitivity analysis, no competing-risks model, no censoring-independence statement** | same | same | same |
| **Comparator actually tested** | `A-fig` caption: **HD vs WT `p = 0.78`** | `A-fig` caption: **LD vs KO+RI `p < 0.0001`**; **HD vs KO+RI `p < 0.0001`** | 🟢 **vs KO+RI — STATED in prose and read by me**: *"LD treatment modestly, **though significantly**, extended lifespan relative to untreated-null controls"*. `A-fig` caption: **LD vs HD `p < 0.0001`** | 🔴 **no comparator in the prose** — *"whereas HD treatment produced a marked and sustained survival benefit (B)"* carries **no comparator and no statistic**. `A-fig` caption supplies all three |
| **Blinding** | 🟡 *"Data were analyzed in a blinded manner **when feasible**"* — **STATED, conditional** | same | same | same |

🟢 **One correction to the repository, discharged here.** The prompt's premise that *"nobody compared the two
vectors in either direction"* belongs to the **2021** paper (mWwox vs hWWOX; `CC-20260922-TX007-DOSE-CHALLENGE-01`
§9c, read by me). For **2026 LD vs HD**, the `A-fig` Fig 3 caption attestation *does* report a formal
comparison — **`p < 0.0001`, log-rank** — and the dossier records its own correction for having claimed
otherwise. **LD vs HD is `FORMALLY COMPARED`, on an inherited caption attestation.** §4 classifies it as such
and labels the provenance.

---

### 2.2 · The other arms — the fields that differ

| Arm | N enrolled | Age | Follow-up horizon | Survival as the paper renders it | Exit accounting |
|---|---|---|---|---|---|
| **A1 EF1α +WPRE** | `A-fig` Fig 1 caption: **n=5** | P0-P1 **STATED** | 🔴 **ABSENT in prose** | **STATED:** *"failed to rescue lethality, growth retardation, or hypoglycemia"* | 🔴 **ABSENT** |
| **A2 CMV +WPRE** | `A-fig`: **n=5** | P0-P1 | 🔴 ABSENT | **STATED:** *"supported early postnatal rescue … but this protection was not sustained at later stages"* | 🔴 ABSENT |
| **A3 CBA** | 🔴 **ABSENT — not in the Fig 1 caption list at all** (`A-fig`) | P0-P1 | 🔴 ABSENT | **STATED:** grouped with CMV in one sentence | 🔴 ABSENT |
| **A4 MBP +WPRE** | `A-fig`: **n=5** | P0-P1 | 🔴 ABSENT | **STATED:** *"weak expression and no phenotypic improvement"* | 🔴 ABSENT |
| **A5 hSynI +WPRE** | `A-fig`: **n=6** | P0-P1 | 🔴 ABSENT | **STATED:** *"the most robust and sustained rescue"* | 🔴 ABSENT |
| **B1 hSynI −WPRE `4E10`** | `A-fig`: **n=3** | P0-P1 | `A-fig`: **Fig 2B axis ends at 50 d** | **STATED:** *"exclusion of WPRE was insufficient to rescue lethality"* | 🟡 **the only partial accounting in the 2026 paper.** `A-fig` (`CC-20260826` §6): falls to ≈33% by ~20 d **with one animal censored at ~25 d** ⇒ 3 = 2 events + 1 censored, **which sums**. 🔴 But see §2.4 T-6 — two inherited reads disagree on **which** arm this is |
| **B2 hSynI +WPRE `4E10`** | `A-fig`: **n=3** | P0-P1 | 50 d | **STATED:** *"survival rates comparable to WT"* | 🔴 ABSENT |
| **B3 hSynI −WPRE `8E10`** | `A-fig`: **n=5** | P0-P1 | 50 d | **STATED:** *"improved outcomes, **including rescue of lethality**"* — ⚠️ on a **50-day axis**, see §7.1 | 🔴 ABSENT. `A-fig`: flat 100% to ~31 d |
| **D1 / D2 / D3 / D5 (S8)** | `A-fig`: **P1 n=6 · P2 n=6 · P3 n=3 · P5 n=7** = **22 DERIVED** | **P1–P5 STATED** | `A-fig`: **S8A to P40; S8B to P300**, and S8B plots **only P1 and P5** | **STATED:** *"a dramatic extension in survival, from approximately three weeks to **nearly one year**"* — ⇒ *"nearly one year"* **DERIVED ≈ the 300-day axis end** (`A-fig` S8B ~75% plateau to 300 d) | 🔴 ABSENT |
| **D-WT / D-KO (S8)** | `A-fig`: **WT+RI n=6 · KO+RI n=6** | P0–P5 | as above | **STATED:** *"WT littermates received identical injections to control for procedural effects"* | 🔴 ABSENT |
| **E · fertility / breeding** | **DERIVED ≥ 40 per group** — *"Fertility testing using **20 breeding cages per group**"* × *"**one male and one female of the same genotype** were housed together in an IVC cage"*, both **STATED** | ≥ breeding age | 🔴 ABSENT | **STATED:** *"HD-treated-null mice exhibited fertility rates and litter sizes comparable to WT and heterozygous controls"* | 🔴 **ABSENT — and never plotted anywhere.** §2.3 |
| **F · ECoG** | `A-fig`: **caption `n = 5 littermates per group`**; an earlier panel estimate said ~3 and the dossier records its own correction to `n=5` | **implant P14 — STATED**; treatment at **P0 — STATED** | **7 days of recording — STATED** | not a survival arm | 🔴 **ABSENT.** These animals carried a cranial ECoG transmitter *"kept outside of the body"*; **whether they re-enter any survival curve is unstated** |

🔵 **One delivery link is stated to differ, and only by age:** *"for P5 pups, the injection site was targeted
at ±1.0 mm, 1.0 mm, and −2.0 mm"* versus `±0.8 / 1.5 / −1.6` at P0-P1. **Volume, rate, needle and injection
count do not change with age** — so the window arms are delivery-matched to C1/C2 on every link but coordinate.

---

### 2.3 · 🆕 The animal-demand arithmetic — the HD survival denominator is smaller than the HD experiments require

**This is a first-hand derivation from `S-body` plus one inherited `n`. It is new to the repository.**

**Minimum HD-treated KO animals the paper's own experiments require.** Every panel below is a **terminal**
assay on `S-body`'s own Methods (snap-frozen brain for DNA/RNA/immunoblot; *"transcardially perfused"* for
IHC; *"non-perfused tissue"* for RNA ⇒ an IHC animal and an RNA animal **cannot be the same animal**):

| Requirement | Locator | Minimum HD animals |
|---|---|---|
| P30 vDNA + mRNA + protein, 4 regions | Fig 5A–5L (**STATED** in prose, read by me) | ≥3 |
| ~3 mo immunoblot | S5A–S5D | ≥3 |
| ~3 mo IHC (perfused ⇒ distinct animals) | S5H, S5I | ≥3 |
| P180 | S5E–S5G | ≥3 |
| P240 | S5J–S5K | ≥3 |
| P300 | S6B–S6D | ≥3 |
| ECoG cohort | Fig 7, `A-fig` `n=5` | ≥3 |
| **Fertility / breeding cohort** | **20 cages × 2 same-genotype animals — both STATED** | **≥40** |
| **Subtotal, distinct animals** | | **≥61** |
| **Floor if every molecular timepoint used only 2 animals and fertility is read as 20 animals** | | **≥35** |

**Against this: `A-fig` attests `KO+HD n = 30` in Fig 3B.**

# 🔴 **≥35 (floor) and ≥61 (nominal) both exceed 30. Under every reading, the Fig 3B HD arm is NOT the full set of HD-treated animals.**

**Three consequences, and none of them is a criticism of the experiment — they are limits on what the curve means:**

1. 🔴 **HD-treated animals exist outside the survival denominator, and the rule that decided which 30 went
   into the curve is `ABSENT`.** A survival curve over a subset selected by an unstated rule is not a survival
   curve over the treated population.
2. 🔴 **The load-bearing term is the fertility cohort**, and it is the one the Methods tie to the colony
   itself: *"Heterozygote **or KO rescued mice (KO injected with AAV9-hSynI-hWWOX) were used for breeding** to
   generate KO mice."* ⇒ **the treated KO breeders are the animals that produced this study's own KO litters.**
   They necessarily lived for months, in mixed-sex pairs, through pregnancies. **Whether any of them is among
   the 30 is unstated; whether their deaths were recorded anywhere is unstated.**
3. ⚠️ **Dependency declared.** The inequality rests on (i) the inherited `n = 30`, which I could not verify,
   and (ii) reading *"20 breeding cages per group"* with *"one male and one female of the same genotype"* — the
   only reading the Methods support. If either fails, the inequality weakens; **the floor calculation shows it
   does not vanish** unless the fertility cohort is far smaller than 20 animals.

⚪ **What this is NOT.** It is **not** evidence that the HD survival result is wrong. It is evidence that the
HD curve's **denominator is not the treated cohort**, which is exactly the fact a reader needs and does not have.

---

### 2.4 · Defects found in-act that the repository does not hold

**`T-1` (confirmed and extended).** The CBA construct is omitted from the Methods sentence that assigns WPRE —
*"Constructs driven by **EF1α, CMV, and MBP** included WPRE, whereas the **hSynI**-driven vector was generated
both with and without WPRE"* — and 🆕 **it is also absent from the Fig 1 caption's construct-and-`n` list**
(`A-fig`: EF1α n=5, CMV n=5, MBP n=5, hSynI n=6 — **no CBA**). It is additionally the only construct from a
different source (*"Custom-made AAV9-CBA-hWWOX … obtained from the Vector ELSC Core Facility"*). ⇒ **the CBA
arm has no stated WPRE status, no stated `n`, and a different manufacturer.** Everything drawn from the
*"CMV and CBA"* grouping inherits all three.

**`T-2` (confirmed, and now dated).** The breeding scheme makes maternal genotype/treatment a per-arm
variable and never reports its distribution. 🆕 **§6 shows this scheme is NEW in 2026**, verified first-hand
against `S-2021`.

**`T-3` 🆕 The Methods' account of what was done to the animals is demonstrably incomplete.** Blood glucose
Methods state *"Blood glucose was measured at **P10, P20, and P30**"* — yet `A-fig` attests a **P180 glucose
panel** (Fig 3H, WT+RI and KO+HD only). A procedure performed and plotted is missing from the Methods list.
⚪ Tail-nick glucose is non-terminal, so this does not change the animal flow; it is recorded because it
shows the Methods are **not** an exhaustive record of animal handling, which is the assumption a reader would
otherwise make about the harvest and censoring silences.

**`T-4` 🆕 The 2026 paper has no humane-endpoint definition at all.** `humane` · `euthan*` · `moribund` ·
`sacrific*` → **0 each**, measured by me. The only monitoring sentence is *"The pups were closely monitored
for growth rate, glucose levels, seizures, ataxia, and general condition to assess phenotypes"* — monitoring
**to assess phenotypes**, with no criterion attached to any action. ⇒ **`HUMANE_EUTHANASIA` cannot be
distinguished from `DEATH` anywhere in this paper**, in any arm, including the untreated KO arm whose animals
*"rapidly deteriorate … developing severe growth retardation, progressive weight loss, and frequent seizures"*.
In a model with that described course, an IACUC-approved study almost certainly applied humane endpoints —
and therefore **the KO+RI curve's *"0% by ~18 d"* is very likely a mixture of `DEATH` and `HUMANE_EUTHANASIA`
that the paper reports as one category.** 🔴 Recorded as an unresolvable category collapse, **not** as a
claim that any specific animal was euthanised.

**`T-5` 🆕 The S8 window arms as *stated* and as *shown* differ.** Prose: *"ICV injection … at daily
intervals **from P0 to P5**, with at least three littermates treated per time point"* (read by me). `A-fig`:
S8A plots **P1, P2, P3, P5** — **P0 and P4 are absent from the figure.** ⇒ either two treated groups exist
whose data are not shown, or the prose overstates the design. **Two groups of ≥3 animals are unaccounted for
under the first reading.**

**`T-6` 🆕 Two inherited reads of Fig 2B disagree on which arm is the censored one**, and the disagreement is
about the accounting, not the biology. `CC-20260826` §6 assigns *"≈33% by ~20 d with one animal censored at
~25 d"* to the **`4E10` WPRE-free** arm (which **agrees** with the prose). `PMID42422765_partial_locators.md`
assigns *"~33% to ~25 days"* to the **`4E10` WPRE-containing** arm (which **contradicts** the prose:
*"treatment with WPRE-containing vectors at the same dose resulted in survival rates comparable to WT"*). The
dossier **flagged its own Fig 2B read as unreliable** at 104 ppi. ⇒ **the higher-resolution read supersedes,
and the prose independently favours it.** Recorded so the superseded assignment is not re-found as live.

**`T-7` 🆕 Two distinct control cohorts are labelled the same way.** Fig 3B's controls are `A-fig`
**WT+RI n=20** and **KO+RI n=10**; S8's are `A-fig` **WT+RI n=6** and **KO+RI n=6**. ⇒ *"WT+RI"* and *"KO+RI"*
each denote **at least two different animal sets** in this paper. Any cross-figure control comparison is
therefore between cohorts, not within one.

---

## 3 · Exit-category ledger per arm — the six labels

**Labels, used exactly as specified:** `DEATH` · `HUMANE_EUTHANASIA` · `SCHEDULED_HARVEST` ·
`CENSORED_OTHER` · `UNKNOWN_EXIT` · `STILL_AT_RISK`.

🔴 **Rule applied without exception, per the dispatch:** *an animal's disappearance from a denominator is
`UNKNOWN_EXIT` until the text says otherwise.* Nowhere in the 2026 paper does the text say otherwise.

### 3.1 · The ledger — 2026 paper

| Arm | N enrolled | `DEATH` | `HUMANE_EUTHANASIA` | `SCHEDULED_HARVEST` | `CENSORED_OTHER` | `UNKNOWN_EXIT` | `STILL_AT_RISK` at 300 d | Does it sum? |
|---|---|---|---|---|---|---|---|---|
| **C3 WT+RI** | **20** (`A-fig`) | **0 stated** | **0 stated** (`T-4`: undefined) | **>0 STATED to have occurred, count ABSENT** — IHC Methods name WT at P10–P180 | **0 stated** | **≈5–6 — DERIVED** from `A-fig` 100%→≈72% × 20 | **≈14–15 — DERIVED** | 🔴 **NO.** 20 = 0+0+? +0+ ~5–6 + ~14–15. The harvested count is unknown and may overlap the unknown exits |
| **C0 KO+RI** | **10** (`A-fig`) | **0 stated as a count** | **0 stated**; `T-4` makes this category **indistinguishable from `DEATH`** | **>0 STATED to have occurred, count ABSENT** — IHC Methods name KO | **0 stated** | **10 — DERIVED** (`A-fig` 0% by ~18 d) | **0** | 🟡 **arithmetically yes, categorically no.** All 10 are events; **which category each is cannot be determined** |
| **C1 LD** | **20** (`A-fig`) | **>0 STATED qualitatively** — *"LD-treated mice did not survive to P90"*; *"mice from either treatment group that failed to survive"*. **Count ABSENT** | **0 stated** | **≥3 DERIVED** — Fig 5 requires LD brains at P30 | **0 stated.** 🔴 **And `A-fig`'s 0% endpoint makes >0 censoring impossible unless those animals were outside the 20** — §3.2 | **20 minus the harvested count — DERIVED** | **0 — DERIVED + corroborated in prose** | 🔴 **NO.** The 20 are all *events in the estimator*; the split between `DEATH` and `SCHEDULED_HARVEST`-scored-as-event is **NOT RECONSTRUCTABLE** |
| **C2 HD** | **30** (`A-fig`) | **>0 STATED qualitatively** — *"either treatment group that failed to survive"*. **Count ABSENT** | **0 stated** | **≥15 DERIVED** (§2.3, five timepoints × ≥3, IHC and immunoblot animals distinct) | **0 stated.** 🔴 §3.2 shows the harvests **must** have been censored **or** out-of-cohort | **≈6–7 — DERIVED** from `A-fig` 100%→≈78% × 30 | **≈23–24 — DERIVED** | 🔴 **NO**, and it cannot: **≥15 harvests + ≈6–7 exits + ≈23–24 survivors ≥ 44 > 30** |
| **B1 `4E10` −WPRE** | **3** (`A-fig`) | **2 — DERIVED** (≈33% of 3) | 0 stated | 0 stated | **1 — `A-fig` attests a censoring mark at ~25 d** | 0 | 0 at 50 d | 🟢 **YES — 3 = 2 + 1.** ⚠️ Subject to `T-6` |
| **B3 `8E10` −WPRE** | **5** (`A-fig`) | 0 | 0 | 0 stated | 0 stated | 0 | **5 at ~31 d — DERIVED** (flat at 100%) | 🟡 yes, trivially — nobody exited within the 50-day axis |
| **A1–A5 promoter arms** | **5/5/–/5/6** (`A-fig`; **CBA absent**) | 0 stated | 0 stated | 0 stated | 0 stated | **all — `UNKNOWN_EXIT`** | 🔴 **no horizon stated** | 🔴 **NO** |
| **D1/D2/D3/D5 window** | **6/6/3/7 = 22** (`A-fig`) | 0 stated | 0 stated | **>0 DERIVED** (S8E/S8F immunoblot + IHC) | 0 stated | **~25% of P1 and P5 — DERIVED** from `A-fig` ~75% plateau | **~75% of P1, P5 at 300 d** | 🔴 **NO.** P2, P3 have **no 300-day curve at all** |
| **D0, D4** | **≥3 each — STATED in prose, ABSENT from every figure** | — | — | — | — | **all — `UNKNOWN_EXIT`** | 🔴 unknown | 🔴 **NO** — `T-5` |
| **E fertility / breeding** | **≥40 — DERIVED** | 0 stated | 0 stated | 0 stated | 0 stated | **all — `UNKNOWN_EXIT`** | 🔴 **never plotted** | 🔴 **NO — this cohort has no survival record at all** |
| **F ECoG** | **5 per group** (`A-fig` caption) | 0 stated | 0 stated | 0 stated | 0 stated | **all — `UNKNOWN_EXIT`** after the 7-day recording | 🔴 unknown | 🔴 **NO** |

# 🔴 **Summary of the ledger: of thirteen arms, ONE (B1, n=3) sums — and that one sums only on an inherited attestation that two repository reads contradict each other about. No arm of the main dose experiment sums. Zero animals in the entire 2026 paper can be assigned an exit category from the paper's own text.**

### 3.2 · 🆕 What the two curve shapes force, jointly — and it corrects a repository presumption

**Premises, both inherited (`A-fig`, `CC-20260826` §4, pixel read at ×4.5 with a declared crop recipe):**

- **P-A:** the **HD** curve is **flat from ~85 d to 300 d** (≈78%, no further steps).
- **P-B:** the **LD** curve **reaches 0%** by ~80 d.

**Premises, first-hand on `S-body` (mine):**

- **P-C:** HD tissue was taken terminally at **~3 mo (≈P90), P180, P240 and P300** (S5, S6 panels).
- **P-D:** LD tissue was taken terminally at **P30** (Fig 5 includes the LD arm on all three molecular axes).

**Derivation:**

| If the convention was… | then in **HD** | and in **LD** | Verdict |
|---|---|---|---|
| **harvest scored as an EVENT** | the curve **must step down** at ≈P90, P180, P240, P300 | the curve **can** reach 0% ✅ | 🔴 **REFUSED by P-A** |
| **harvest CENSORED** | the curve **can** stay flat ✅ | a censored animal holds the estimator **above zero permanently** ⇒ the curve **cannot** reach 0% | 🔴 **REFUSED by P-B** |
| **harvested animals were never in the survival denominator** | flat ✅ | reaches 0% ✅ | 🟢 **the only convention consistent with BOTH curves** |

# 🟢 **⇒ Under a single uniform convention, the animals taken for tissue were not members of the Fig 3B denominators. This is independently corroborated by §2.3's arithmetic, which shows the HD experiments need more animals than the HD denominator holds.**

🔴 **The one alternative that survives, and it is not a small one:** the analysis is **internally inconsistent
across arms** — harvests scored as events in some arms and censored in others. **That alternative has direct
precedent in this laboratory**, verified first-hand by me on `S-2021` (§5.2). Under it, nothing is forced.

⚠️ **Correction to a repository position, stated as a correction.**
`tx007_per_arm_delivery_reconstruction_20260922.md` §4.3 and `tx007_saturation_hypothesis_20260922.md` §7.4
both record *"harvest plotted as death is the most economical explanation"* for the WT+RI plateau. **Given
P-A, that explanation cannot hold uniformly** — it is incompatible with the flatness of the HD curve over the
very interval in which HD animals were demonstrably being harvested. **It becomes the less favoured of the
two readings, not the leading one.** ⚠️ **This correction is conditional on P-A**, which is an inherited
pixel attestation I could not verify, and it is stated as conditional.

🟢 **And one prior inference is confirmed unchanged and for the right reason:** the removal accounting
**cannot manufacture the LD–HD gap**. Under the surviving convention the harvested animals are in neither
denominator, so removals bias neither arm. Under the inconsistent-convention alternative, the ≥P90 harvests
exist **only in HD**, so scoring them as events would **depress HD** and **compress** the gap. **In both
readings the LD–HD separation is not created by the removal accounting.** 🔴 **No direction of bias for the
LD–HD comparison is asserted here** — the previously withdrawn directional claim is not re-derived.

---

## 4 · The `WT+RI ≈72% at 300 days` anomaly

### 4.1 · First, reconcile two repository attestations that look like they disagree

| Locus | What it says about WT+RI |
|---|---|
| `PMID42422765_partial_locators.md`, Fig 3 entry | *"WT + reporter — **plateau at ~90%**"* |
| `CC-20260826-DOSE-ADJUDICATION-01` §4 (×4.5 crop, declared recipe) | *"`WT+RI n=20` — 100% → **≈90% (~50 d)** → **≈72%, flat to 300 d**"* |

🟢 **Not a contradiction.** The dossier read a **mid-curve** value; the higher-resolution read describes a
**two-step** curve whose first plateau is the dossier's ≈90%. **The two-step read supersedes and subsumes it.**
Recorded so the ≈90% is not re-found as a live conflict with the ≈72%.

### 4.2 · What is STATED, and it is more than the repository held

🆕 **First-hand, `S-body`, Immunohistochemistry, verbatim:**
> *"Mice (**WT**, KO, and KO injected mice) at different ages (**P10‑P180**) were deeply anesthetized using an
> overdose of ketamine and xylazine and then transcardially perfused using 4% paraformaldehyde (PFA)/PBS."*

⇒ **The paper STATES that wild-type animals were killed for tissue at ages inside the survival window.** The
repository previously treated WT harvesting as an inference. **It is stated.** What is absent is the count,
the exact ages, and whether those WT animals were among the 20 in Fig 3B.

🆕 **A cheap arithmetic discriminant nobody has named.** With `n = 20` and **no censoring**, a Kaplan–Meier
estimate can only take values `k/20` — i.e. multiples of **5%**. **≈72% is not a multiple of 5%** (70% = 14/20,
75% = 15/20). Likewise for HD at `n = 30`: multiples of **3.33%**, and **≈78%** falls between 76.7% (23/30)
and 80% (24/30). ⇒ **reading the plateau against the panel's own gridlines is a test for the presence of
censoring**: a plateau that lands **off** the `k/n` lattice requires censored observations; one that lands
**on** it does not. ⚠️ **I cannot run this test** — it needs the native-resolution panel — and the reported
values are explicitly approximate, so pixel error is a live alternative to censoring. **Recorded as a
discriminant, not as a result.**

### 4.3 · Verdict

# 🔴 **`NOT RECONSTRUCTABLE` as a fact. But the explanation space is now reduced to exactly two, and they are discriminable.**

| # | Reading | Support | Against |
|---|---|---|---|
| **R1** | **The ≈5–6 WT exits are real events** — `DEATH` and/or `HUMANE_EUTHANASIA` — in vehicle-injected WT, most plausibly **neonatal ICV procedure attrition** (bilateral 32G injection, hypothermia anaesthesia, 4.0 µL into a P0 pup) plus baseline mortality | 🟢 **Forced by §3.2 under a uniform convention.** 🟢 The curve's shape fits: both drops occur **early** (the first by ~50 d) and then **nothing for ~250 days** — that is procedure/early-life attrition, **not** an aging hazard, which would accrue late | 🔴 The paper never states a single WT death, and `T-4` means no humane-endpoint criterion exists to attribute them to |
| **R2** | **Terminal harvests were scored as events in the WT arm but censored (or excluded) in the HD arm** — an internally inconsistent analysis | 🟢 **Direct precedent in the same laboratory**, verified first-hand: §5.2 | 🔴 Incompatible with a single stated convention; the Methods describe **one** survival analysis |

🔴 **What is missing to decide, in order of cheapness:**
1. **Censoring tick marks on Fig 3B's WT and HD curves** at native resolution — their presence or absence
   decides `R1` vs `R2` almost by itself.
2. **The plateau's value against the gridlines** — on or off the `k/20` lattice (§4.2).
3. **The per-arm exit ledger** — which the same laboratory published in 2021 and did not publish in 2026 (§5.2).

⚪ **What must not be concluded.** The ≈72% is **not** by itself evidence of a toxicity, a procedural hazard
or a reporting fault. It is a number whose meaning depends on an accounting rule the paper does not state,
and `R1` — the reading §3.2 favours — describes an ordinary and expected cost of neonatal intracranial
surgery, **which the paper's own S8 design anticipates** by including WT littermates *"to control for
procedural effects."* 🔴 **That control exists and its result is never reported.**

---

## 5 · Every survival statement, classified

### 5.1 · The five classes, applied

`MEASURED` · `FORMALLY COMPARED` · `DESCRIPTIVELY DIFFERENT` · `NOT TESTED` · `NOT RECONSTRUCTABLE`

| # | Statement | Surface | Class | Why |
|---|---|---|---|---|
| 1 | *"LD treatment modestly, **though significantly**, extended lifespan relative to untreated-null controls (KO+RI)"* | 🟢 `S-body`, mine | 🟢 **`FORMALLY COMPARED`** | The prose itself asserts a test; `A-fig` caption supplies `p < 0.0001`, log-rank |
| 2 | *"HD treatment produced a marked and sustained survival benefit"* | 🟢 `S-body`, mine | 🔴 **`NOT TESTED` *as written*** | **No comparator and no statistic in the sentence.** It becomes `FORMALLY COMPARED` only via the `A-fig` caption |
| 3 | **HD vs WT+RI, `p = 0.78`** | 🔴 `A-fig` caption | 🟡 **`FORMALLY COMPARED` — on an inherited attestation** | A log-rank was run. ⚠️ **`p = 0.78` is a failure to reject, not equivalence.** With `n = 20` vs `30` and ~22% vs ~28% event rates, the study has **no stated power** to exclude a real difference (`power` → 0 occurrences) |
| 4 | **HD vs LD, `p < 0.0001`** | 🔴 `A-fig` caption | 🟡 **`FORMALLY COMPARED` — inherited** | 🟢 **This is the fact that licenses the dose claim.** It also discharges the *"nobody compared them"* concern **for the 2026 dose arms** |
| 5 | **LD vs KO+RI and HD vs KO+RI, `p < 0.0001`** | 🔴 `A-fig` caption | 🟡 **`FORMALLY COMPARED` — inherited** | both treated arms beat vehicle |
| 6 | *"LD-treated mice did not survive to P90"* | 🟢 `S-body`, mine | 🟢 **`MEASURED`** (as an endpoint claim) | A plain mortality statement in running text, **with no figure behind it** — it survives every figure-level doubt. 🔴 **But `T-4` + §3.1 mean it does not distinguish `DEATH` from `HUMANE_EUTHANASIA` from a harvest scored as an event** |
| 7 | *"Untreated-null mice … approximately three weeks"* | 🟢 `S-body`, mine | 🟢 **`MEASURED`**, qualitative | consistent with `A-fig` 0% by ~18 d |
| 8 | *"Increasing the dose of the WPRE-lacking vector to `8E10` was associated with improved outcomes, **including rescue of lethality**"* | 🟢 `S-body`, mine | 🟡 **`DESCRIPTIVELY DIFFERENT`** | **No statistic anywhere in the sentence.** And on `A-fig`'s 50-day axis *"rescue of lethality"* means **alive at ~31 d** — §7.1 |
| 9 | *"treatment with WPRE-containing vectors at the same dose resulted in **survival rates comparable to WT**"* | 🟢 `S-body`, mine | 🔴 **`NOT TESTED`** | *"comparable"* with **no test**, at `A-fig` `n = 3`, on a 50-day axis. **A comparability claim is exactly the claim a null result cannot carry** |
| 10 | *"a dramatic extension in survival, from approximately three weeks to **nearly one year**"* (S8 window) | 🟢 `S-body`, mine | 🟡 **`DESCRIPTIVELY DIFFERENT`** | 🆕 *"nearly one year"* **DERIVED ≈ 300 d**, the S8B axis end (`A-fig`) — it is the same horizon as Fig 3, **not a longer one**. `A-fig` gives `**p<0.001**` for S8B, so a test exists for **P1 and P5 only**; **P2 and P3 have no 300-day curve** |
| 11 | *"neuronal WWOX restoration using the high-dose vector **at any time point between P0 and P5** was sufficient to fully rescue"* | 🟢 `S-body`, mine | 🔴 **`NOT TESTED` as stated** | 🆕 `T-5`: **P0 and P4 are absent from S8**, and **P2/P3 are absent from the 300-day panel**. *"Any time point"* is asserted over a set the figure does not contain |
| 12 | *"mice from either treatment group that failed to survive exhibited reduced WWOX expression, reinforcing the link between effective protein restoration and survival"* | 🟢 `S-body`, mine | 🔴 **`NOT TESTED`, and structurally so** | 🆕 **Animals selected *on the outcome*, compared post hoc, with no statistic, no `n`, and no blinding statement for this comparison.** Reverse causation is unexcluded: a dying animal's brain protein falls for many reasons. ⚠️ **It is also the paper's *only* acknowledgement that treated animals died** |
| 13 | *"WT littermates received identical injections to control for procedural effects"* | 🟢 `S-body`, mine | 🔴 **`NOT RECONSTRUCTABLE`** | 🆕 **The control was run and its survival result is never reported.** This is the experiment that would settle §4 |
| 14 | *"By the study endpoint, body weights of HD-treated mice were nearly indistinguishable from WT littermates"* | 🟢 `S-body`, mine | 🟡 **`DESCRIPTIVELY DIFFERENT`** | *"the study endpoint"* is **never defined numerically** in the prose; `A-fig` puts it at 300 d |
| 15 | **Number of deaths, euthanasias, harvests or censorings in any arm** | — | 🔴 **`NOT RECONSTRUCTABLE`** | §3 |
| 16 | **Whether the Fig 3B denominators are the treated cohorts** | — | 🔴 **`NOT RECONSTRUCTABLE`**, and §2.3 shows the answer is probably **no** for HD | §2.3 |
| 17 | **`WT+RI ≈72% at 300 d`** | 🔴 `A-fig` | 🔴 **`NOT RECONSTRUCTABLE`** — two readings, both live | §4 |

### 5.2 · 🆕 The 2021 predecessor publishes exactly the record the 2026 paper omits — verified first-hand

**I fetched `PMC8649866` in this act. Unlike the 2026 paper, its served surface carries complete figure
legends.** Verbatim, read by me:

> **Fig 1C** — *"Kaplan–Meier survival graph indicates prolonged life span of knockout mice injected with
> AAV9‐hSynI‐mWwox [**total = 18, spontaneously dead = 6, mice taken out for
> electrophysiology/electron microscopy/analysis, are shown in yellow, = 12**] compared to mice injected with
> AAV9‐hSynI‐GFP (= 6) or the non‐injected (= 8); < 0.0001, log‐rank Mantel–Cox test."*

> **Fig 2C** — *"Kaplan–Meier survival graph indicates prolonged life span of knockout mice injected with
> AAV9‐hWWOX [**total = 16, alive = 6, spontaneously dead = 6, 4 mice (shown in yellow) were taken out for
> analysis**) compared to the non‐injected (= 8)] (< 0.0001, log‐rank Mantel–Cox test)."*

**Both ledgers sum exactly:** `18 = 6 + 12` and `16 = 6 + 6 + 4`. **And removed animals are visually marked.**

| | **Repudi 2021** | **Obeid 2026** |
|---|---|---|
| N per arm in the legend | 🟢 stated | 🔴 `A-fig` only; **0 `n =` tokens on the served body** |
| Spontaneous deaths | 🟢 **counted** | 🔴 **absent** |
| Animals removed for analysis | 🟢 **counted, and marked in yellow** | 🔴 **absent; `censor*` → 0** |
| Animals alive at write-up | 🟢 **counted** | 🔴 **absent** |
| Does the ledger sum? | 🟢 **yes, both arms** | 🔴 **no arm** |
| Humane-endpoint definition | 🔴 absent (both) | 🔴 absent (both) |
| Euthanasia method stated | 🟢 *"euthanized by CO₂ and transcardially perfused"* | 🟢 *"overdose of ketamine and xylazine … transcardially perfused"* |

# 🔴 **This is a reporting regression, not a data limitation. The same laboratory, five years earlier, reported the exact table this node needs — for two arms, summing, with censoring marked. The 2026 paper reports none of it for thirteen arms.**

🟢 **And it identifies the missing record precisely:** not a novel document, but **the 2026 equivalent of the
Fig 1C/Fig 2C bracket.** §9.

⚠️ **The documented 2021 inconsistency stands and is not softened.** `CC-20260826` §7: Fig 2C's legend says
`alive = 6` while the plotted curve reaches 0% — **a Kaplan–Meier with 6 animals at risk cannot terminate at
zero.** `EPISTEMIC_STATUS`: `UNRESOLVED`. ⇒ **the 2021 paper both publishes the ledger and contradicts it**,
which is why `R2` in §4.3 cannot be dismissed. 🟢 **Kaplan–Meier itself is not at fault in either paper: it
accommodates right-censoring correctly. What is at fault is the accounting handed to it.**

---

## 6 · Vector variables — each in exactly one of the four classes

`REPORTED SAME` · `REPORTED DIFFERENT` · `UNREPORTED` · `UNRESOLVED`

**Not re-derived (taken as settled by `A-repo`, `REPORTED SAME`):** injected volume (`2.0 µL/hemisphere`,
constant), injection count, rate, needle, coordinates, route, anaesthesia, WPRE within the compared dose
arms, FVB strain, housing. **Verified present in `S-body` by me in-act; not re-argued.**

| Variable | Class | Evidence, and the measurement behind it |
|---|---|---|
| **Nominal dose, LD vs HD** | 🔴 **`REPORTED DIFFERENT`** | `1.23E11` vs `2.63E11` — **STATED**. Ratio `2.1382×` |
| **Prep concentration** | 🔴 **`REPORTED DIFFERENT` by arithmetic; `UNREPORTED` as a value** | Volume is a stated constant, so HD is **a more concentrated prep, not a larger one**. 🔴 **No titre is printed anywhere**: `vg/` → 0, `GC/` → 0, measured by me. 🔴 **"HD spread further" is REFUSED by the text** — the CSF distribution volume is matched by construction |
| **Titration method** | 🟢 **`REPORTED SAME`** | *"Viral titers were determined by RT-qPCR using bGH primers"* — one method, both arms |
| **Titration uncertainty (CV, replicates, orthogonal method)** | 🔴 **`UNREPORTED`** | no error term stated for any titre |
| **Lot identity** | 🔴 **`UNREPORTED`** | `lot` (word-boundary) → **0**, `batch` → **0**, measured by me |
| **Manufacturing source** | 🔴 **`UNREPORTED` for the LD/HD vector** | Four sources named **collectively** — *"Fujifilm Diosynth Biotechnologies … Vector Biolabs … Boston Institute of Biotechnology [BIB]"* plus *"the Vector ELSC Core Facility"* — with **only two constructs assigned** (AAV9-CBA-hWWOX, AAV9-hSynI-EGFP → ELSC). The hSynI-hWWOX −WPRE vector is assigned to **none of them** |
| **Purification route** | 🔴 **`UNREPORTED`** | `iodixanol` → 0 · `chromatog*` → 0 · vector `purif*` → 0 (the single `purif` hit is *"elution of purified DNA"*), measured by me |
| **Empty:full capsid ratio** | 🔴 **`UNREPORTED`** | `capsid` → **0** · `empty` → **0**, measured by me |
| **Formulation buffer of the vector** | 🔴 **`UNREPORTED`** | the **vehicle** is fully specified — *"RI; PBS with 5% sorbitol and 0.001% pluronic F-68"* — the **vector's own** formulation is never stated |
| **Endotoxin** | 🔴 **`UNREPORTED`** | `endotoxin` → **0**, measured by me |
| **Whether LD is a dilution of HD or independent manufacturing** | 🔴 **`UNRESOLVED`** — 🎯 **the single largest open vector variable** | `dilut*` → **0**, measured by me. 🔵 **The two cases have different predictions and the paper does not say which obtains:** a dilution collapses lot / purification / empty:full to near-identity **but makes the excipient and empty-capsid burden differ 2.14× as well**; two independent preps make every row above a live difference |
| **WPRE, within the compared dose arms** | 🟢 **`REPORTED SAME`** (both −WPRE, one sentence) | not re-derived |
| **WPRE, across figures (Fig 1/2 vs Fig 3)** | 🔴 **`REPORTED DIFFERENT`** | Methods: EF1α/CMV/MBP **+WPRE**; hSynI **both**. `A-repo`: a **3–16.7× regional expression factor** for WPRE **dwarfs** the 2.14× dose factor ⇒ **no dose comparison may cross the ±WPRE line** |
| **WPRE status of the CBA construct** | 🔴 **`UNREPORTED`** — `T-1` | the Methods WPRE list **omits CBA**, and 🆕 the Fig 1 caption's construct list omits it too (`A-fig`) |
| **ECoG-arm dose** | 🔴 **`UNREPORTED` in Methods** | Methods name only *"WWOX-KO mice injected with AAV9-hSynI-hWWOX"* with **no dose**; the Results say *"HD"*. 🟡 `UNRESOLVED` overall |

🔴 **Stated once and binding: `UNREPORTED` is a finding about the paper, NOT evidence that the arms differed.**
No vector-quality difference is inferred anywhere in this file from the absence of metadata. What the
absences establish is that **the nominal `2.1382×` is a label on a syringe, not a measurement of what entered
the ventricle**, and that its uncertainty is **unbounded in both directions** from the published record.

---

## 7 · What is closed, and what is not

### 7.1 · Closed — not reopened here

🟢 **The "dose non-monotonicity" premise is CLOSED** as an artefact of incompatible survival horizons.
`CC-20260826-DOSE-ADJUDICATION-01` §6, read by me: **Fig 2B's x-axis ends at 50 days**; the `8E10` arm is
flat at 100% to ~31 d. At 31 d the Fig 3 LD arm is still substantially alive (it declines from ~20 d and
reaches 0% by ~80 d), **so on Fig 2's axis LD would also read as "rescue of lethality."**
⇒ *"rescue of lethality"* means **alive at ~31 d** in Fig 2 and **alive at 300 d** in Fig 3.
**`NOMENCLATURE_CONFLICT`, not a contradiction.** **This node does not investigate "why the higher dose
performed worse", because that phenomenon is not established.** 🟢 **And the exponent question is moot under
this reading** — the tension is erased at either `8E10` or `8E11`.

🟢 **The LD→HD step is MONOTONIC** and in the expected direction. What is anomalous is an **effect-size
mismatch**, not a monotonicity failure. Conflating the two is the error this section exists to prevent.

🟢 **Not re-derived:** the previously WITHDRAWN claim that late scheduled removals necessarily biased the
comparison in a specific direction. §3.2 establishes that under the surviving convention removals bias
**neither** arm, and under the alternative they would **compress** the LD–HD gap. **No direction is asserted.**
🟢 **Also not re-derived:** *"HD spread further"* — refused by the constant `2.0 µL/hemisphere`.

### 7.2 · Does the live question survive the animal-flow reconstruction?

> **Why does a relatively modest change in measured regional WWOX expression appear associated with a large
> change in long-horizon survival?**

**Both halves, assembled from what I read first-hand:**

| Half | What the paper states, verbatim (`S-body`, mine) | Class |
|---|---|---|
| *"modest expression change"* | vDNA: *"higher vDNA levels in HD-treated mice than LD-treated mice across regions, **with statistical significance in the hippocampus**"* — **1 of 4 regions** · mRNA: *"robust, region-wide induction … whereas LD-treated mice showed lower but readily detectable expression"* — **no significance stated for any region** · protein: *"**with a trend toward** higher expression in HD-treated mice"* — **the authors' own word is "a trend"** | 🟡 `MEASURED`, with **`NOT TESTED`** on the mRNA axis and **the authors declining significance** on the protein axis |
| *"large survival change"* | LD *"did not survive to P90"* vs HD *"marked and sustained"*; `A-fig` caption **`p < 0.0001`** | 🟢 `FORMALLY COMPARED` (on an inherited caption) |

# 🟡 **The question survives — but as a mismatch between two differently-powered measurements, not as an established biological fact.**

🔴 **Why it cannot be promoted past that.** Three separate reasons, each independently sufficient:

1. **The expression side has no power.** No `n`, no variance, no power statement is available to me
   (`power` → 0; `n =` → 0). *"`ns` in 3 of 4 regions"* with the enormous error bars `A-repo` attests
   (*"in panel C the high-dose interval runs from about 2 000 to 15 000"*) is **equally consistent with a real
   2× difference the study could not detect.** **An underpowered null is not a small effect.**
2. **The survival side's denominators are of unknown composition** (§2.3, §3), and **allocation was not
   randomised** (`randomi*` → 0) with an **unexplained 20:30 imbalance** favouring the successful arm.
3. **The two sides are not measured on the same animals or at the same horizon** — expression at P30 in a
   handful of animals, survival over 300 d in twenty and thirty.

⇒ # 🔴 **The correct answer to the live question, from this paper alone, is `NOT RECONSTRUCTABLE` — not "biological".** §8 ranks candidate explanations as hypotheses only, in obedience to that verdict.

---

## 8 · What survival conclusions the data actually license — **the deliverable**

### 8.1 · 🟢 LICENSED

| # | Conclusion | On what |
|---|---|---|
| **L1** | **Untreated `Wwox`-null mice on FVB die at approximately three weeks.** | 🟢 `MEASURED`, prose + `A-fig` 0% by ~18 d, and consistent with the 2021 paper and the conditional-KO literature the Introduction cites. ⚠️ `DEATH` and `HUMANE_EUTHANASIA` are **not separable** (`T-4`) |
| **L2** | **A single neonatal bilateral ICV injection of AAV9-hSynI-hWWOX (−WPRE) at `2.63E11` vg extends survival relative to vehicle, and the extension is large and durable to the 300-day observation limit.** | 🟢 log-rank vs KO+RI, `p < 0.0001` (`A-fig` caption); corroborated by two independent prose statements and by S8's separate cohort |
| **L3** | **At `1.23E11` vg the same vector also extends survival relative to vehicle — and does not rescue it.** | 🟢 **both halves formally supported:** LD vs KO+RI `p < 0.0001` (`A-fig`) **and** *"LD-treated mice did not survive to P90"* (`S-body`, mine). 🎯 **This is the study's most robust single finding, because the failure half rests on running text with no figure behind it** |
| **L4** | **The `1.23E11` and `2.63E11` arms differ in survival, and the difference was formally tested.** | 🟡 log-rank **`p < 0.0001`** — `A-fig` Fig 3 caption. ⚠️ **Inherited attestation; label it as such at every use.** ⚪ The difference is **between two arms of one study**, not between two doses in general |
| **L5** | **A survival benefit at `2.63E11` is reproducible across two separate cohorts in the same paper.** | 🟡 Fig 3B (`A-fig` n=30) and S8B (`A-fig` P1 n=6, P5 n=7, ~75% to 300 d, `p<0.001`) are **different animals** — `T-7`. Weak but genuine internal replication |

### 8.2 · 🔴 NOT LICENSED — with what each would need

| # | Not licensed | Why | What would license it |
|---|---|---|---|
| **N1** | *"HD survival is equivalent to wild type."* | **`p = 0.78` is a failure to reject.** No power statement exists, and the WT arm itself sits at `A-fig` **≈72%**, so the comparison is against a **depleted** reference whose depletion is unexplained (§4) | a stated non-inferiority margin, a power calculation, and the WT arm's exit ledger |
| **N2** | *"The dose–response is a continuum: a lower, safer dose would still help proportionally."* | **`A-fig` Fig 3B refuses it for survival** — LD reaches 0%, HD plateaus. The paper's own vocabulary (*"dose-dependent"*, *"graded improvement"*, *"a clear dose-response relationship"*) describes a continuum the survival panel does not show | an **intermediate-dose arm** between `1.23E11` and `2.63E11`, which is the single most informative experiment this paper implies |
| **N3** | *"A threshold lies between `1.23E11` and `2.63E11` vg."* | 🟡 **Licensed only as a threshold for *this* vector, *this* prep, *this* delivery, *this* colony.** Not transferable: `A-repo` shows the same laboratory's 2021 vector at **3–6× lower dose** reached ≈93% at 270 d | delivered vector-genome copies per brain region, by one assay, in two studies |
| **N4** | *"`8E10` −WPRE rescues lethality."* | **`DESCRIPTIVELY DIFFERENT` at `A-fig` n=5 on a 50-day axis** — *"rescue of lethality"* there means **alive at ~31 d** (§7.1) | the `8E10` arm carried to 300 days |
| **N5** | *"Treatment at any time from P0 to P5 rescues survival."* | 🆕 `T-5`: **P0 and P4 are absent from S8**; **P2 and P3 have no 300-day curve** | the missing groups, or a restatement covering only P1 and P5 at 300 d |
| **N6** | *"WPRE-containing vector at `4E10` gives WT-like survival."* | **`NOT TESTED`**, `A-fig` n=3, 50-day axis | a test, a larger n, and the full horizon |
| **N7** | *"Reduced WWOX expression caused the deaths of the treated animals that died."* | **`NOT TESTED`**, outcome-selected, reverse causation unexcluded (§5.1 #12) | prospective expression measurement before death, or a landmark analysis |
| **N8** | *"Vehicle-injected WT survival was ~72% because harvests were plotted as deaths."* | 🔴 **§3.2 makes this the LESS favoured reading.** It is one of two, both live | Fig 3B's censoring marks; the exit ledger |
| **N9** | **Any statement about how many animals died, were euthanised, were harvested or were censored, in any 2026 arm.** | **`NOT RECONSTRUCTABLE`** (§3) | the exit ledger |
| **N10** | *"The Fig 3B curves describe the survival of the treated cohorts."* | 🆕 §2.3 — the HD experiments require **more** HD-treated animals than the HD denominator holds | the enrolment and allocation record |

### 8.3 · 🎯 The one-line deliverable

> 🟢 **The data license: a large, formally tested, twice-observed survival benefit at `2.63E11` vg of this
> −WPRE AAV9-hSynI-hWWOX vector in this colony, and a formally tested partial benefit at `1.23E11` vg that
> does not reach rescue.**
> 🔴 **The data do NOT license: equivalence to wild type, a continuous dose–response, a transferable dose
> threshold, any statement about the fate of individual animals, or any inference from the ≈72% wild-type
> plateau — and they do not license treating the Fig 3B denominators as the treated cohorts.**
> ⚪ **The direction and existence of the LD–HD difference are not in question here. Its interpretation is.**

---

## 9 · The maternal / breeding confound — and it is dated to 2026

🔴 **Methods, verbatim, `S-body`, read by me in-act:**
> *"**Heterozygote or KO rescued mice (KO injected with AAV9-hSynI-hWWOX) were used for breeding** to
> generate KO mice."*

⇒ **Some KO pups in this study have an AAV-treated KO dam; others have an untreated heterozygous dam. The
per-arm distribution is never stated** (`dam`/`dams`/`maternal` → **0 occurrences**, measured by me;
`litter` occurs 4 times and **never** in connection with Figs 3–7).

🆕 **And the scheme is NEW in 2026. Verified first-hand against `S-2021`:**

| | **Repudi 2021** (`S-2021`, verbatim) | **Obeid 2026** (`S-body`, verbatim) |
|---|---|---|
| Breeding | *"**Heterozygote mice were used for breeding** to get the-null mice."* | *"**Heterozygote or KO rescued mice (KO injected with AAV9-hSynI-hWWOX) were used for breeding**"* |
| Maternal variable | 🟢 **uniform** — Het dams only | 🔴 **two dam classes, distribution unstated** |

**Why this is a confound and not a quibble — four reasons, each from the paper's own design:**

1. 🔴 **The study's principal systemic endpoint is blood glucose**, and *"profound hypoglycemia"* is the
   **dam's** phenotype as well as the pup's. A treated-KO dam and a Het dam are **different intrauterine and
   lactational metabolic environments** for the paper's headline metabolic readout (Fig 3E–3H).
2. 🔴 **A treated-KO dam is itself a treated animal** — she carries neuronal hWWOX from a neonatal ICV
   injection, and the paper reports her as fertile with *"litter sizes comparable to WT"* (S4C–S4E). Litter
   size, maternal care and milk supply all feed directly into pup growth (Fig 3C–3D) and survival.
3. 🔴 **It is entangled with §2.3.** The treated-KO breeders **are** the fertility cohort — the same animals.
   So the arm whose disposition is least documented is the arm that determines the maternal background of the
   pups in every other arm.
4. 🔴 **It is also an unmatched variable BETWEEN the two studies**, and this bears on the repository's
   `VG_DOSE_ALONE_IS_NOT_TRANSFERABLE` finding: Repudi's better-performing low dose was delivered to pups of
   **uniformly heterozygous dams**; Obeid's LD was delivered to pups of a **mixed dam population**. 🆕 **The
   repository's cross-study comparison did not hold this variable.** It is added to the unmatched list
   alongside injection technique (free-hand vs stereotaxic), volume (1 vs 2 µL/hemisphere), prep and year.

⚪ **This is not a criticism of the breeding scheme**, which is the only practical way to generate these
litters once a rescued animal is fertile — and its fertility is one of the paper's findings. **It is a
criticism of the reporting:** one column in a supplementary table (dam genotype and treatment status per
animal) would remove it entirely.

⚠️ **No effect size is assigned to this confound.** Its magnitude is **unbounded** from the published record,
which is exactly why it ranks where it does in §10.

---

## 10 · 🟡 `IPOTESI` — ranked explanatory classes for the live question

**Every entry below is a HYPOTHESIS. None is a conclusion. The verdict of §7.2 stands over all of them: from
this paper alone the answer is `NOT RECONSTRUCTABLE`.** They are ranked by **how much of the mismatch each
could account for given what the paper reports**, not by biological plausibility.

| Rank | Class | `IPOTESI` | Share it could account for | What would test it, cheapest first |
|---|---|---|---|---|
| **1** | 🟡 **Statistical / power artefact on the EXPRESSION side** | 🟡 `IPOTESI` — **there is no "modest" expression change to explain.** The expression difference may be as large as the dose difference and simply undetected: 3-of-4 `ns` with the attested error bars, no `n`, no power statement, and *"a trend"* is the authors' own hedge | **up to all of it** | Fig 5 legend `n` and variance; a power calculation; **per-region source data** |
| **2** | 🟡 **Denominator / accounting artefact on the SURVIVAL side** | 🟡 `IPOTESI` — the Fig 3B denominators are selected subsets of larger treated cohorts (§2.3) under an unstated rule, with a **20:30 non-randomised imbalance** favouring the successful arm | **substantial; unbounded** | **the per-arm exit and enrolment ledger** |
| **3** | 🟡 **Vector / preparation difference** | 🟡 `IPOTESI` — the nominal `2.1382×` is a label. Two independent preps can differ several-fold in **infectious** units at matched vg, and empty capsids compete for receptor. **Whether LD is a dilution of HD is `UNRESOLVED`** | **up to all of it** | **Certificate of Analysis** for both materials — titre by two orthogonal methods with CV, empty:full, purification, buffer, endotoxin, lot, and dilution-or-not |
| **4** | 🟡 **Breeding / maternal effect** | 🟡 `IPOTESI` — §9. A metabolic phenotype read out in pups of two different dam classes, distribution unstated | **substantial; unbounded** | one column: dam genotype + treatment status per animal |
| **5** | 🟡 **Threshold effect (true non-linearity)** | 🟡 `IPOTESI` — a genuinely step-like survival response to a smoothly graded input. 🔵 **This is the paper's own implied reading**, and it is a hypothesis, not a result: it requires the expression measurement to be **right**, which #1 denies we know | large, if #1 and #3 are excluded | **an intermediate-dose arm specified as a FRACTION of HD, never in absolute vg** |
| **6** | 🟡 **Per-cell vs per-tissue expression (coverage vs output)** | 🟡 `IPOTESI` — tissue-level vDNA and immunoblot cannot separate *more transduced cells* from *more protein per cell*, and survival may depend on the fraction of cells above a per-cell threshold | large | 🔴 **per-region % NeuN⁺WWOX⁺ at LD and at HD — never measured.** `A-repo`: S3C exists only in the `4E10` +WPRE arm. **The single measurement that would decide** |
| **7** | 🟡 **Critical cell population** | 🟡 `IPOTESI` — survival may hinge on a population the four homogenised regions do not resolve. 🔴 `A-repo`: **Purkinje cells are never resolved**; the cerebellum is one homogenate throughout | moderate | cell-type-resolved expression in the surviving vs non-surviving animals |
| **8** | 🟡 **Unmeasured region or systemic effect** | 🟡 `IPOTESI` — 🔴 `A-repo`: **the hypothalamus is never assayed for WWOX**, in a paper whose central systemic phenotype is **hypoglycaemia**; striatum, thalamus, brainstem also unassayed | moderate | hypothalamic expression at LD and HD |
| **9** | 🟡 **Developmental timing** | 🟡 `IPOTESI` — the P0-vs-P1 distribution **within** each arm is `ABSENT`. ⚠️ **S8 shows P0–P5 is immaterial at HD and there is NO low-dose window experiment**, so this is bounded-small at HD and **untested at LD** | small, bounded to 1 day | per-animal injection day |
| **10** | 🟡 **Biological variability** | 🟡 `IPOTESI` — with n=20 and n=30 and `p<0.0001`, chance alone is a poor fit for the survival separation, but variability interacts with #1 and #2 | small alone | replication in an independent laboratory — 🔴 `A-repo`: **replication count is zero** |
| **11** | 🟡 **Regional distribution shape** | 🔵 **Partly refused already.** Volume is a stated constant, so the anatomical territory reached is matched by construction and the arms differ in **concentration**, not **spread**. The authors' *"higher vDNA … across regions"* is the shape this predicts | small | an arm-by-arm spatial map — none exists |

🔵 **The two cheapest tests in the whole table are #1's Fig 5 legend and #6's per-arm transduction fraction.
Neither requires a new animal.** #6 is the only one that would *decide* between saturation and coverage.

---

## 11 · What I could not establish, and the single record that would supply most

| Item | Why | What would close it |
|---|---|---|
| **Any figure legend, any `n`, any P value, by my own read** | 🔴 `S-body` carries **zero** `n =` tokens and **no legends**; `files/` verified **absent**; europepmc → **`000` at CONNECT**, control `example.com` → **`000`** | the shared `files/` tree, or one open route to JATS / publisher markup |
| **Number of deaths, euthanasias, harvests, censorings — any arm** | 🔴 `censor*` · `euthan*` · `humane` · `moribund` · `harvest` → **0 each** | **the per-arm exit ledger** |
| **Whether Fig 3B carries censoring tick marks** | 🔴 the panel is unreachable to me; `A-fig` reports a censoring mark in **Fig 2B** but says nothing about Fig 3B | a native-resolution Fig 3B |
| **Whether the WT+RI ≈72% plateau lands on the `k/20` lattice** | 🔴 same; and the attested value is explicitly approximate | same panel, read against its gridlines (§4.2) |
| **Whether the Fig 3B denominators are the full treated cohorts** | 🆕 §2.3 shows probably **not** for HD, on an inequality that rests on one inherited `n` | the enrolment / allocation record |
| **The disposition of the fertility-and-breeding cohort (≥40 animals)** | 🔴 never plotted, never counted, and it doubles as the colony's breeding stock | same |
| **The disposition of the ECoG cohort after recording** | 🔴 unstated; these animals carried cranial implants | same |
| **Whether the S8 P0 and P4 groups exist** | 🆕 `T-5` — stated in prose, absent from the figure | S8 at native resolution, or the authors |
| **Per-arm sex, litter, dam genotype and treatment status, exact injection day** | 🔴 all `ABSENT`; `randomi*` · `allocat*` → 0 | same |
| **A humane-endpoint criterion** | 🔴 `T-4` — the paper defines none | the **HU-IACUC protocol**, which by regulation contains one |
| **Whether LD is a dilution of HD** | 🔴 `dilut*` → 0 | vector **CoA** |
| **Empty:full, purification, endotoxin, formulation, lot** | 🔴 0 occurrences each | vector **CoA** |
| **Whether the 3-of-4 `ns` vDNA result is equivalence or low power** | 🔴 no per-region `n`, no variance, no power statement | Fig 5 legend + source data |
| **Any deposited source data** | 🆕 🔴 **STATED impossible:** *"Data and code availability: Not relevant."* | **the authors, or the IACUC record — there is no repository to query** |

### 11.1 · 🎯 The single record that would supply the most

# **The 2026 equivalent of the Repudi 2021 Figure 1C / Figure 2C bracket: a per-arm animal-flow table — `total` · `alive` · `spontaneously dead` · `taken out for analysis` (with date and reason) · `euthanised at humane endpoint` — plus, per animal, litter, dam genotype and treatment status, sex and exact injection day.**

🔵 **Four reasons it outranks the vector CoA, in this order:**

1. 🟢 **It exists, and the same laboratory has published its own version of it.** §5.2 verifies the 2021
   legends first-hand: two arms, both summing, censored animals marked. **This is not a request for new work
   — it is a request for a table the authors demonstrably keep.**
2. 🟢 **It decides whether the survival observation is an observation at all** — it closes §3 (the whole exit
   ledger), §4 (the ≈72% anomaly, both readings at once), §2.3 (the denominator inequality) and ranks #2 and
   #4 of §10.
3. 🟢 **It is a prerequisite for the mechanism question.** **Establishing a mechanism for an artefact is
   wasted work**, so the record that tests whether the phenomenon is real must come first.
4. 🟢 **It is the cheapest record in the list** — no assay, no animal, no instrument.

**Second, and the one that would decide the mechanism: the Certificate of Analysis for the LD and HD
material** — titre by two orthogonal methods with CV, empty:full by AUC or cryo-EM, purification route,
formulation buffer, endotoxin, lot identity, and **whether LD is a dilution of the HD stock.**

**Third, figure-level, if no record can be had: Figure 3 and Figure 5 at native resolution** — the per-arm
`n`, the P values, the censoring marks and the plateau-against-gridline read of §4.2. **This is the surface
every `A-fig` value in this file came from and the one this deployment cannot reach.**

---

## 12 · Findings this node adds

| ID | Finding | Provenance |
|---|---|---|
| **A-1** | 🆕 **The paper's only acknowledgement that treated animals died is one clause** — *"mice from either treatment group that failed to survive exhibited reduced WWOX expression"* — which also proves post-mortem tissue entered the expression analysis, and is itself an **outcome-selected, untested** comparison | 🟢 **first-hand `S-body`** |
| **A-2** | 🆕 **The Methods STATE a terminal procedure on wild-type animals inside the survival window** (IHC, WT named, P10–P180, anaesthetic overdose + perfusion). The repository previously treated WT harvesting as an inference | 🟢 **first-hand `S-body`** |
| **A-3** | 🆕 🎯 **Under a single uniform convention, the harvested animals were not in the Fig 3B denominators** — forced jointly by HD's flatness after ~85 d and LD's arrival at 0%. **This makes "harvest plotted as death" the LESS favoured reading of the WT plateau, correcting two repository files** | 🟡 derivation mine; **premises `A-fig`** |
| **A-4** | 🆕 🎯 **The HD experiments require ≥35 (floor) to ≥61 (nominal) HD-treated KO animals against an attested denominator of 30** ⇒ the Fig 3B HD arm is **not** the treated cohort. The load-bearing term is the **fertility/breeding cohort (≥40)**, which doubles as the colony's breeding stock and is never plotted | 🟡 derivation mine from **first-hand** Methods + one `A-fig` `n` |
| **A-5** | 🆕 **A `k/n`-lattice test for censoring:** with no censoring a KM estimate can only take multiples of `1/n`. ≈72% is not a multiple of 1/20; ≈78% is not a multiple of 1/30. **Reading the plateau against the gridlines tests for censoring without any new data** | 🟢 arithmetic mine |
| **A-6** | 🆕 🎯 **The breeding scheme CHANGED between 2021 and 2026** — *"Heterozygote mice"* → *"Heterozygote **or KO rescued mice**"*. The maternal confound is **new in 2026**, and is a further **unmatched variable between the two studies**, which the repository's cross-study dose comparison did not hold | 🟢 **first-hand, both bodies** |
| **A-7** | 🆕 🎯 **The 2021 predecessor publishes the exact exit ledger the 2026 paper omits** — `total = 18, spontaneously dead = 6, taken out for analysis = 12`; `total = 16, alive = 6, spontaneously dead = 6, 4 taken out`; **both sum, censored animals marked in yellow.** ⇒ **a reporting regression, and the precise identity of the missing record** | 🟢 **first-hand `S-2021` legends** |
| **A-8** | 🆕 **`Data and code availability: Not relevant.`** There is no deposited source data to request; the record exists only with the authors or the IACUC | 🟢 **first-hand `S-body`** |
| **A-9** | 🆕 **No humane-endpoint criterion exists anywhere in the 2026 paper** (`humane`/`euthan*`/`moribund`/`sacrific*` → 0) ⇒ **`DEATH` and `HUMANE_EUTHANASIA` are collapsed into one category in every arm**, most consequentially in KO+RI | 🟢 **first-hand `S-body`** |
| **A-10** | 🆕 **The Discussion contains the literal string `(4E10)`** — the authors' own E-notation, the one exponent that survived the parser. First-hand confirmation of the Fig 1 / Fig 2 base dose | 🟢 **first-hand `S-body`** |
| **A-11** | 🆕 **The Methods' glucose timepoint list (P10, P20, P30) omits the attested P180 panel** ⇒ **the Methods are not an exhaustive record of animal handling**, which is the assumption a reader would otherwise apply to the harvest and censoring silences | 🟢 first-hand + `A-fig` |
| **A-12** | 🆕 **`T-5`: S8 shows P1, P2, P3, P5 only — P0 and P4 are absent** — while the prose claims *"daily intervals from P0 to P5"*; and **P2/P3 have no 300-day curve.** *"Any time point between P0 and P5"* is asserted over a set the figure does not contain | 🟢 first-hand prose + `A-fig` panels |
| **A-13** | 🆕 **`T-7`: "WT+RI" and "KO+RI" each denote at least two different animal sets** (Fig 3B n=20/10 vs S8 n=6/6) ⇒ no cross-figure control comparison is within-cohort | `A-fig` |
| **A-14** | 🆕 **`T-1` extended: CBA is absent from the Fig 1 caption's construct-and-`n` list as well as from the Methods' WPRE list** ⇒ no `n`, no WPRE status, different manufacturer | first-hand Methods + `A-fig` caption |
| **A-15** | 🆕 **Two repository attestations of the WT plateau (≈90% vs ≈72%) are reconciled**, not left contradicting: the ≈90% is the mid-curve value of a two-step curve. The two-step read supersedes | `A-repo`, mine |
| **A-16** | 🆕 **`T-6`: two inherited reads of Fig 2B disagree on which arm carries the censoring mark**; the higher-resolution read agrees with the prose and supersedes | `A-repo`, mine |
| **A-17** | 🆕 **`Kaplan–Meier itself is exonerated in both papers.** It accommodates right-censoring correctly; what is defective is the accounting handed to it — absent in 2026, published-but-internally-contradicted in 2021 | mine |

---

## 13 · Reading debt and scope declaration

**No new PMID is introduced as a premise.** Both PMIDs named — `42422765` and `34747138` — are existing
premises of `tx007_dose_challenge_20260922.md` and `CC-20260826-DOSE-ADJUDICATION-01`, already covered by
registry records and receipts. **No `FT-` identifier is cited**, so no manifest crosscheck is opened.
🟢 **One reading debt is partly DISCHARGED:** `PMC8649866`'s **figure legends** were read first-hand in this
act (§5.2, §9), where the repository previously held them only as attestations through `CC-20260826` §7.

🔴 **Outstanding debt this node did not pay and does not claim to have paid:** every figure legend, every `n`
and every P value of `PMID 42422765` remains **unread by me**. Every such value above is labelled `A-fig` and
is another actor's attestation. The `files/` tree is absent and every egress route is closed (verified
first-hand, with control), so the debt is **recorded rather than discharged**.

**No researcher email or contact detail appears anywhere in this file. No individual-level record appears
anywhere in this file. No registry, queue, ledger, receipt, manifest or canonical file was read for writing
or modified. No git command was run.**

---

## 14 · Source attribution

**According to PubMed**, and retrieved from **PubMed / PubMed Central** in this act.

| PMID | Citation | DOI |
|---|---|---|
| **42422765** | Obeid M, Akkawi R, Repudi S, Singh PK, Abudiab B, Jebara T, Berent A, Brennan T, Weiss Y, Shekh-Ahmad T, Aqeilan RI. *Neuron-specific WWOX gene therapy produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy.* **Molecular Therapy Advances** (`Mol Ther Adv`) 2026;34(3):201791. PMCID `PMC13343157`. **Full body (48,780 chars) fetched and read in-act; no figures, no legends** | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) |
| **34747138** | Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI. *Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes.* *EMBO Mol Med* 2021;13(12):e14599. PMCID `PMC8649866`. **Full body fetched and read in-act, INCLUDING complete figure legends** | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |

**Repository artefacts read by me and cited above:**
[`tx007_per_arm_delivery_reconstruction_20260922.md`](tx007_per_arm_delivery_reconstruction_20260922.md) ·
[`tx007_saturation_hypothesis_20260922.md`](tx007_saturation_hypothesis_20260922.md) ·
[`tx007_regional_wwox_forebrain_cerebellum_20260922.md`](tx007_regional_wwox_forebrain_cerebellum_20260922.md) ·
[`tx007_dose_challenge_20260922.md`](tx007_dose_challenge_20260922.md) ·
[`CC-20260826-DOSE-ADJUDICATION-01.md`](../research/commit_candidates/CC-20260826-DOSE-ADJUDICATION-01.md) §§4,6,7 ·
[`CC-20260826-DOSE-DECISION-TABLE-01.md`](../research/commit_candidates/CC-20260826-DOSE-DECISION-TABLE-01.md) ·
[`CC-20260922-TX007-DOSE-CHALLENGE-01.md`](../research/commit_candidates/CC-20260922-TX007-DOSE-CHALLENGE-01.md) §9 ·
[`PMID42422765_partial_locators.md`](../research/fulltext_dossiers/PMID42422765_partial_locators.md).

---

**End of file — complete run.** Read-only toward every canonical file, every registry, every queue, the
receipt ledger and the state manifest. Nothing promoted, nothing committed, no git operation run, no
`BATCH_COMMIT`, no registry or ledger touched. **No molecule, no dose recommendation, no route
recommendation, no safety claim, no druggability score.** Every dose recorded above is what a published
experiment administered to mice. **Not medical advice.**
