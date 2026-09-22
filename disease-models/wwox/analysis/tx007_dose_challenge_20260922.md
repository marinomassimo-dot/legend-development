# `TX-007` — does the dose biology survive an independent challenge, and has anyone replicated it?

**Date:** 2026-09-22 · **Actor:** Scientist J · **Node:** `TX007_DOSE_CHALLENGE`

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries and
> every ledger. Nothing here changes a claim, a paper record, the working model or the tracking log.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> 🔴 **BLOCK-1, stated once and binding over every line below.** **No molecule is named as a therapy, no dose is
> recommended, no route is recommended, no safety claim is made and no druggability score is given.** Every
> number in §3 is **a dose that a published experiment administered to mice**, reported so that the experiment
> can be criticised. **Reporting a dose a paper used is not recommending it, and nothing here tells anyone to
> give, withhold or change any treatment.** Nothing here is medical advice; it is material for discussion with a
> treating clinical team and for nobody else.

---

## 0 · Read depth and surfaces, declared before any number is used

| Source | Depth **reached in this act** | Measured size | Figures / supplement |
|---|---|---|---|
| **`PMID 42422765`** (Obeid *et al.* 2026) | 🟢 **full body fetched and read in-act** via `get_full_text_article(pmc_ids=["PMC13343157"])` | **48,780 characters (measured exactly)** — byte-identical in length to the prior session's measurement | 🔴 **none.** No figure, caption or supplementary panel was seen by me |
| **`PMID 34747138`** (Repudi *et al.* 2021) | 🟢 **full body fetched and read in-act** via `get_full_text_article(pmc_ids=["PMC8649866"])` | **whole article + figure legends returned** | legend text only; **no panel seen** |
| **`PMID 34268881`** (Steinberg *et al.* 2021, organoids) | 🟡 **targeted string extraction in-act**, not a full read: delivery modality, promoter, locus, titration method. PMC body retrieved (81,107 chars) and **searched**, not read end to end. Declared as targeted, not as a reading | 81,107 chars retrieved | none |
| **`PMID 42397075`** (Steinberg/Zonca … 2026, *Brain*) | 🔴 **not fetchable, re-verified in-act.** `convert_article_ids(["42397075"])` returns **`{"pmid":"42397075"}` and nothing else — no PMCID exists.** Worked from LEGEND's dossier `PMID42397075_partial_locators.md` and manifest | **0 bytes** | none |
| `PMID 42128308` (Obeid *et al.* 2026, *Neurobiol Dis* **review**) | **metadata + abstract only** — `abstract-depth`. No PMCID in metadata | n/a | n/a |
| PubMed searches | 9 executed, all counts and translations in §7 | — | — |
| `mcp__Scholar_Gateway__semanticSearch` | executed once; **7 articles, all 2007–2012** | — | corpus gap, §7.4 |
| WebSearch | 3 executed; **snippet-depth only**, never treated as a read | — | §3.1 |
| LEGEND artefacts | `tx007_genotype_class_ceiling_20260921.md`, `denominator_audit_therapeutic_portfolio_20260922.md`, `CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01.md`, `PMID42422765_partial_locators.md` (889 lines), `deepdive_manifests/PMID42422765.json`, `PMID42397075.json`, `PMID42397075_partial_locators.md`, `discovery_ledger_current.md` → `DL-MOL-005`, `DL-MECH-009/010/011` | 🟢 **all read in full before any search was run** | — |

🔴 **Two egress routes are closed in this deployment and were measured, not assumed.** Direct HTTPS to
`eutils.ncbi.nlm.nih.gov`, `pmc.ncbi.nlm.nih.gov`, `europepmc.org` and `www.biorxiv.org` returns
`connect_rejected` / `EGRESS_BLOCKED` from the agent proxy. **Therefore the raw PMC XML — the one surface that
would carry `<sup>11</sup>` and settle every exponent by direct inspection — could not be reached at all.** This
is a measured route closure, not a silence: the proxy status endpoint names each refusal by host and timestamp.

🔴 **Parser defect reproduced independently, in-act, and extended.** Every vector-genome exponent is deleted from
the extracted body. Verbatim, from my own fetch:

> *"we evaluated two clinically applicable doses: an LD (1.23 × 10vg) and a higher dose (HD, 2.63 × 10vg)"*
> *"At a dose of 4 × 10vg, exclusion of WPRE was insufficient to rescue lethality"*
> *"Increasing the dose of the WPRE-lacking vector to 8 × 10vg"*

**Three new instances of the damage class, found this act:**

1. 🔴 **`n = ` and every P value are deleted wholesale.** In the 48,780-character body, `grep -c "n = "` → **0**;
   every `[Pp] ?[<=] ?0?\.[0-9]+` pattern → **0**; every asterisk/`∗` → **0**. The paper's own Statistical
   analysis section, quoted in-act, reads: *"Exact sample sizes () andvalues are reported in the figure
   legends."* — the parenthetical `(n)` and the word `p` are gone from that very sentence.
2. 🔴 **The extracted body contains no figure captions at all.** `grep -c "Figure 3"` → **0**. There is no
   `Figure N` string anywhere. ⇒ **the caption statistics the prior session quoted (`p = 0.78`, `p < 0.0001`,
   the per-arm n's) are NOT recoverable from this route.** They came from the **88,241-character local PMC HTML
   artefact** (`PMID42422765_Obeid2026_PMC.html`, sha256 `00fadaf4…9bd3`), which is **not present in this
   worktree** — `files/` does not exist here. Two surfaces of the same paper differ by ~39,000 characters and by
   the entire statistical apparatus. **Which surface a number came from now has to travel with the number.**
3. 🔴 **Chemical subscripts are deleted too**, found in the 2021 body: `CO₂` → **`CO`** (*"5% CO conditions"*),
   `H₂O₂` → **`HO`** (*"Endogenous peroxidase was blocked with 3% HOfor 15 min"*). ⇒ the damage class is not
   "exponents" — it is **every super/subscript numeral**, and it silently changes the identity of reagents as
   well as the magnitude of doses.

---

## 1 · The direct answer, before the evidence

**The dose biology does not survive the challenge, and the replication answer is the cleanest single finding of
this node: nobody outside one laboratory has ever performed the experiment, let alone replicated it.**

1. 🔴 **Replication: zero, with a working positive control.** `WWOX AND (AAV9 OR AAV OR adeno-associated)` →
   **`total_count: 3`**, translation properly expanded. The three are `42422765` (Obeid 2026, primary),
   `34747138` (Repudi 2021, primary) and `42128308` — **a review by the same authors**. Senior author on all
   three: **Aqeilan RI**. `Repudi S` is first author of the 2021 primary and third author of the 2026 primary.
   Positive control on the identical query form: `SCN1A AND (AAV9 OR AAV OR adeno-associated)` →
   **`total_count: 25`**. ⇒ **single laboratory, two primary studies, never replicated.**
2. 🔴 **And the replication negative is stronger than "a small field".** `Aldaz CM[Author] AND Wwox AND (mouse
   OR mice)` → **`total_count: 18`**. An independent laboratory has held WWOX mouse models for ~20 years,
   including the SCAR12 cerebellar work. **Its intersection with the three AAV records is empty.** The capability
   to replicate exists elsewhere and has not been used.
3. 🔴 **The dose axis is one experiment, not a literature.** `PMID 34747138` administers **a single dose** — no
   dose arm anywhere in its text. So every dose–response statement in `TX-007` rests on **`PMID 42422765`
   alone**, and inside it on **two figures**.
4. 🔴 **Threshold vs continuum: neither, as published — the paper's own prose is not monotone.** Two
   running-text sentences from my own fetch, same paper, same WPRE-lacking hSynI vector:
   *"Increasing the dose of the WPRE-lacking vector to 8 × 10[¹⁰] vg was associated with improved outcomes,
   including rescue of lethality"* — and — *"LD-treated mice did not survive to P90"* for **LD = 1.23 × 10¹¹
   vg**, i.e. a **1.5-fold higher** dose. If the two figures' dose units are the same, the dose–survival relation
   in this paper is **non-monotone**, which neither a threshold nor a continuum accommodates.
5. 🔴 **And the unit ambiguity is exactly the size of the effect.** The 2026 doses are written as bare `vg` with
   **no per-hemisphere/total qualifier** anywhere in the running text, while the Methods deliver **2.0 µL per
   hemisphere, bilaterally**, and the 2021 paper states its dose explicitly **per hemisphere**. A per-hemisphere
   vs total ambiguity is a factor of **2**. **The LD→HD step is 2.1×.** ⇒ the unresolved unit is the same
   magnitude as the entire dose separation the threshold is built on, and it is also what decides whether §1.4's
   non-monotonicity is real.
6. 🔴 **Survivor conditioning is worse in the 2021 paper than in the 2026 one, and nobody has said so.** The
   2021 survival curve on which the whole programme rests **censored 12 of 18 animals** in its main arm — the
   legend says so verbatim — with 6 spontaneous deaths. §5.
7. ✅ **The cerebellar signal is real, is a shortfall in one organ, and is kept in its own section (§6) with its
   own evidence.** It is **not** evidence about the dose ceiling and the ceiling is **not** evidence about it.
8. ⚪ **What is NOT claimed.** Nothing here says the therapy fails, nothing says any dose is unsafe, nothing
   says excess WWOX harms a neuron. The finding is about **what was measured and on what scale**.

---

## 2 · Delta — what the five named artefacts already contain, stated before I add anything

**Read in full first. The following are theirs, not mine, and are not re-derived below.**

| Already held | Where |
|---|---|
| The exponent-deletion defect, with the three verbatim `10vg` strings and the "ten orders of magnitude" framing | `tx007_genotype_class_ceiling_20260921.md` §0 · `CC-…-01` §0 and §3(d) |
| LD `1.23 × 10¹¹` / HD `2.63 × 10¹¹`, the 2.1-fold separation, and that they come from a **prior-session raster read of `gr3.jpg`** (sha256 `c63f930c…4997d`), not from extracted text | `CLAIM 011` · locator file · `CC-…-01` §0 |
| **The threshold reading, and that Figure 3B refuses the word "continuum"** — LD all dead by ~90 d, HD plateau ~80 % to 300 d; caption `p = 0.78` HD-vs-WT, `p < 0.0001` HD-vs-LD and LD-vs-KO+RI | locator file, Figure 3 entry **and its own correction** |
| The **four-point** survival series (4 × 10¹⁰ · 8 × 10¹⁰ · LD · HD) assembled across Figures 2 and 3 | locator file |
| **7 of 8 regional `ns`** on vector genomes and mRNA between the two doses, with opposite survival | locator file Figure 5 · manifest entry 12 · ceiling §5.2 |
| The survivor-conditioned explanation (*"mice … that failed to survive exhibited reduced WWOX expression"*) and that **S5 marks one HD and three LD animals dead** | locator file · ceiling §5.2 · denominator audit §2.1 |
| **The regional/scalar split, argued at length and with its own table**, incl. cerebellum 1.4× / 0.6× at P300, 0.2–0.7× at P30, and that raising dose is not the remedy | `CC-…-01` §1b-bis — the most complete treatment of it in the repository |
| WPRE as a dose-sparing booster, cerebellum the most boosted region (16.7×), and the design tension | `DL-MECH-009` |
| Neuronal (SynI) sufficiency; the P1–P5 window and that it is **not** a continuously sampled P0–P5 window; durable P300 rescue | `DL-MECH-010` · `DL-MECH-011` · `DL-MOL-005` · locator file S8 audit |
| `overexpress` = 0, `supraphysio` = 0, `apopto` = 0, `threshold` = 0, `toxicity` = 1, `tumor` = 3 in the 2026 body; the 2-record overexpression-toxicity census | ceiling §4.3 · `CC-…-01` §1c |
| The triply-qualified 2021 tumour non-finding, and that the 2026 study performs **no tumour surveillance** | ceiling §4.3 and §7 W3-C5 |
| That the promoter comparison is confounded by expression level, and the prior session's **two self-corrections** (the false Fig 1/Fig 2 discrepancy; the invalid "sub-threshold hierarchy") | locator file, both correction blocks |
| Genotype-class gradation refused for cause; isogenic confound; clone variance | ceiling §3 · `CC-…-01` §2 |
| TX-007's denominators are **reported** and the strategy still fails, for a different reason: the measured quantity does not track the endpoint | denominator audit §2, §3.1, §3.3 |

✅ **Everything in the list above I treat as settled and do not restate as new.** My additions are §3.1 (exponent
confidence per figure, from surfaces the repository had not counted as independent), §4.2 (the non-monotonicity,
which is text-vs-text and does not need a panel), §4.3 (titration and vendor), §5.2 (the 2021 censoring),
§5.3 (endpoints conditioned on survival *by design*), §6.3 (the human organoid arm has **no recorded dose at
all**), §7 (the replication census), and §10 (four repository assertions that do not hold).

---

## 3 · Task 1 — every dose arm in every WWOX gene-replacement study the repository holds

⚠️ **Read the BLOCK-1 notice at the head of this file before reading this table.** These are doses that
published experiments administered to animals or cells. **None is a recommendation of any kind.**

### 3.1 Exponent confidence, assigned per figure — the column the repository did not have

**Scale used.** 🟢 **HIGH** = exponent seen on **two or more independent non-extractor surfaces**.
🟡 **MEDIUM** = **one** non-extractor surface, **or** an E-notation token surviving in running text.
🔴 **LOW** = a single unreplicated attestation, or never seen outside extracted text.
**Every figure is 🔴 by default until a surface is named.**

| Dose as used in the paper | Figure / arm | Surfaces on which the **exponent** has been seen | Confidence | Unit |
|---|---|---|---|---|
| **1.23 × 10¹¹ vg** (LD) · **2.63 × 10¹¹ vg** (HD) | `42422765` Fig 3, Fig 5, Fig 4, Fig 6, Fig 7, S5, S7 | **(i)** prior-session raster read of Fig 3A, `gr3.jpg` sha256 `c63f930c…4997d`, 104 ppi; **(ii)** 🆕 **the S7I caption**, rendered from `mmc1.pdf` at **200 ppi** (`S_p09_200dpi.png`) and quoted in the locator file as *"KO+W LD (1.23x1011vg) and KO+W HD (2.63x1011vg)"* — a **flattened** superscript, `1011` = `10¹¹`, on a **different artefact by a different route** from (i); **(iii)** WebSearch snippet, in-act 2026-09-22, reporting `1.23 × 10¹¹` / `2.63 × 10¹¹` | 🟢 **HIGH** — three surfaces, two of them primary-document renderings. 🆕 **The repository had (i) only and stated the doses rest on a single raster read; (ii) is in its own locator file and was not counted** | 🔴 **UNRESOLVED.** Bare `vg` in running text, in the Fig 3A read, and in the S7I caption. **No `/hemisphere` or `total` anywhere.** See §4.1 |
| **4 × 10¹⁰ vg** | `42422765` Fig 1 (four promoters: EF1α, CMV, MBP, hSynI — **all +WPRE**) and Fig 2 low arm | **(i)** 🆕 **`4E10` in running text, read in-act** — *"all vectors were tested at the same titer (4E10)"*. **E-notation survives the extractor**; this is the only dose in the corpus that does; **(ii)** Fig 1 caption attestation *"(4 × 1010 vg, n = 5)"*, flattened `1010` = `10¹⁰` | 🟢 **HIGH** for the **Fig 1 promoter comparison**, 🟡 **MEDIUM** for the Fig 2 arm — the `4E10` sentence is about the promoter series, and transferring it to Fig 2 is the exact cross-figure move the prior session corrected itself for twice | ambiguous, same as above |
| **8 × 10¹⁰ vg** | `42422765` Fig 2, WPRE-lacking higher arm | **only** `8 × 10vg` (deleted, in-act) + a prior-session panel-colour read the prior session **itself declared unreliable** | 🔴 **LOW** | ambiguous |
| **2 × 10¹⁰ vg** | `42422765` Fig 2E protein columns | prior-session panel attestation only | 🔴 **LOW** | ambiguous |
| **2 × 10¹⁰ GC / hemisphere** | `34747138` — the **single** dose of the entire 2021 study (both mWwox and hWWOX vectors) | **(i)** in-act body: *"Viral particles (2 × 10/hemisphere)"* and *"Approximately 1 µl (2 × 10GC/hemisphere)"* — **exponent deleted**; **(ii)** WebSearch snippet in-act reporting `2 × 10¹⁰` | 🟡 **MEDIUM** — one snippet route, no primary rendering seen | 🟢 **EXPLICIT: per hemisphere**, and the unit **`GC`**, not `vg` |
| **not recorded** | `42397075` human organoid AAV9-hSynI-WWOX arm | 🔴 **no vg, no MOI, no titre appears anywhere in LEGEND's dossier or manifest for this paper** — the only "dose" in the whole record is `125 nM` of the A51 small molecule. Paper **not fetchable** (no PMCID, re-verified in-act) | 🔴 **NONE — there is no exponent to be confident about.** §6.3 | — |
| **no vector dose exists** | `34268881` organoid rescue arms | 🆕 in-act string extraction: the rescue line **`W-AAV` is not an AAV vector.** The paper's own legend: *"WWOX-KO WiBR3 hESCs were introduced with a plasmid containing WWOX coding sequence and targeting the safe harbor locus **AAVS1**. This resulted in hESCs **overexpressing WWOX under UBP promoter** from the AAVS1 locus (W-AAV)"* — `AAV` in `W-AAV` denotes **AAVS1, the safe-harbour locus**. Separately, the electrophysiology rescue used a **lentivirus**, whose *"titer was determined empirically by infecting 293T cells"*, applied at *"1:100 of virus-containing medium"* with polybrene at day 35 | 🔴 **not applicable** — a knock-in line and a functionally-titred lentivirus are not dose arms | — |

### 3.2 The full arm inventory, with what was measured in each

| Study · arm | Vector | Route | Dose (see §3.1 for exponent confidence) | n per arm | Age at dosing | Endpoint | Statistic |
|---|---|---|---|---|---|---|---|
| `42422765` Fig 1 | AAV9-**EF1α**/**CMV**/**MBP**/**hSynI**-hWWOX, **all +WPRE** (confirmed in-act from Methods: *"Constructs driven by EF1α, CMV, and MBP included WPRE, whereas the hSynI-driven vector was generated both with and without WPRE"*) | ICV, stereotaxic, bilateral | 4 × 10¹⁰ vg, **same titer for all four** | 5 / 5 / 5 / **6** — **caption attestation only; zero `n` tokens survive extraction** | P0–P5 window per Methods | survival; glucose P14; WWOX IF (panel M) | log-rank; t-test |
| `42422765` Fig 2 | AAV9-hSynI-hWWOX **± WPRE** | ICV | 4 × 10¹⁰ and 8 × 10¹⁰ (survival); 2 × 10¹⁰ and 4 × 10¹⁰ (protein, Fig 2E) | WT 5 · KO 4 · hWWOX 4E10 **3** · 8E10 5 · WPRE 4E10 **3** — panel attestation, and the prior session flagged its own Fig 2B colour read as unreliable | P0 | survival to ~50 d; growth; glucose; regional protein | log-rank |
| `42422765` **Fig 3 — the dose-ranging arm** | AAV9-hSynI-WWOX, **WPRE-lacking** | ICV | **LD 1.23 × 10¹¹ · HD 2.63 × 10¹¹** | WT+RI 20 · KO+RI 10 · **KO+LD 20 · KO+HD 30** — caption attestation | P0 | **Kaplan–Meier to 300 d**; glucose P10/P20/P30/P180 | log-rank Mantel–Cox; **HD vs WT p = 0.78**; HD vs LD and LD vs KO+RI **p < 0.0001** |
| `42422765` Fig 5 | same | ICV | LD vs HD | not recoverable | P0 | vector genomes, hWWOX mRNA, protein × 4 regions at P30 | unpaired two-tailed *t*; **7 of 8 `ns`** |
| `42422765` Fig 4 | same | ICV | **HD only** | WT+RI 9 · KO+W HD 10 | P0 | open field, EPM, rotarod at 3 months | *t*-test, **8 comparisons, no multiplicity correction declared** |
| `42422765` Fig 7 | same | ICV | **HD only** | **5 per group** (caption attestation corrects the earlier ~3 estimate) | P0; ECoG from P14, 7 days | interictal spikes (**printed `0.2000`**); SWD/h (`****`; WT-vs-HD `ns`) | *t*-test |
| `42422765` S8 | same | ICV | HD | P1 **6** · P2 **6** · P3 **3** · P5 **7** · KO+RI 6; **P4 absent**; the P300 panel plots **only P1 and P5** | **P1, P2, P3, P5** | survival to P40 and P300; weight/glucose P14 | log-rank; **no treated-vs-KO bracket drawn** |
| `34747138` Fig 1 | AAV9-hSynI-**mWwox**-IRES-EGFP | ICV, **free-hand**, ~1 µL/hemisphere, trypan-blue-traced | 2 × 10¹⁰ GC/hemisphere | **total 18 · spontaneously dead 6 · 12 removed for analysis**; AAV9-GFP 6; non-injected 8 | **P0** | Kaplan–Meier; weight (n=4/group) | log-rank, **p < 0.0001** |
| `34747138` Fig 2 | AAV9-hSynI-**hWWOX** | same | same | **total 16 · alive 6 · spontaneously dead 6 · 4 removed for analysis**; non-injected 8 | **P0** | Kaplan–Meier; weight (n=3/genotype) | log-rank, **p < 0.0001** |
| `34747138` Figs 3–5 | either | same | same | **n = 3 mice per group** throughout (30–60 neurons; 3 sections; ~300 axons) | P0 | firing rate P18-21 and 6 mo; GFAP/Iba1; EM g-ratio | *t*-test |
| `42397075` | AAV9-hSynI-WWOX (verbatim in LEGEND's dossier) | organoid infection | 🔴 **not recorded anywhere in LEGEND's record** | 🔴 not recorded | organoid age not recorded in the dossier extract | neuronal function, RG populations, protein 0.4×–7× WT across lines | brackets **WT-vs-EGFP** and **EGFP-vs-WWOX**; 🔴 **no bracket WT-vs-either-treated** |
| `34268881` | **(a)** AAVS1 knock-in, **UBP** promoter · **(b)** lentiviral WWOX cDNA | (a) germline edit (b) medium, day 35 | (a) **none** (b) functional titre, 1:100 | organoid-level n (8/8/4 from batches) | — | layering, GAD67 balance, PSD | Welch's *t* |

🆕 **Two route facts recovered in-act that the repository did not hold, and that bear directly on dose:**

- **`42422765` Methods, verbatim:** *"A Micro-4 nano-pump controller was used to ensure a steady injection rate
  of 1–1.5 μL/min, delivering **2.0 μL/hemisphere** … The procedure was repeated for the contralateral
  hemisphere."* Coordinates are given relative to **lambda** (±0.8 / 1.5 / −1.6 mm at P0–P1; ±1.0 / 1.0 / −2.0
  at P5). ⇒ **4.0 µL total, bilateral, stereotaxic.**
- **`34747138` Methods, verbatim:** *"**Free-hand** intracranial injections … Approximately 1 µl (2 × 10
  GC/hemisphere)"*, with *"Trypan blue 0.1% … added to the virus"*. ⇒ **2.0 µL total, free-hand.**
  🔴 **Between the two papers the injected volume per hemisphere doubled and the technique changed.** Volume and
  technique both change CSF distribution. **The two papers' doses are therefore not on a common scale even if
  their exponents and units were settled** — and settling the exponents would not fix it.

---

## 4 · 🔴 Task 2 — threshold or continuum? Verdict: **neither is established, and the paper's own prose is not monotone**

### 4.1 What exactly distinguishes the arms — and the unit that decides it

The LD and HD arms differ by **2.1-fold in nominal vector genomes** and, on the paper's own measurements, by
**nothing else that reached significance**: 7 of 8 regional comparisons of vector genomes and hWWOX mRNA are
`ns` (LEGEND's record; I did not see those panels). So the arms are distinguished by **a number on a syringe**,
and by survival.

🆕 🔴 **And that number has no unit.** From my own fetch, the defining sentence is *"an LD (1.23 × 10vg) and a
higher dose (HD, 2.63 × 10vg)"* — **bare `vg`**. The word `hemisphere` appears in the 2026 body **exactly
twice**, both in the Methods injection protocol, never attached to a dose. The 2021 paper, by contrast, writes
**`2 × 10 GC/hemisphere`** — unit explicit. The S7I caption, the one 200-ppi primary rendering the repository
holds, also reads bare: *"KO+W LD (1.23x1011vg)"*.

⇒ **The per-hemisphere-vs-total ambiguity is a factor of 2. The LD→HD step is 2.1×. The ambiguity is the size
of the effect.** Any statement of the form "the threshold lies between 1.23 and 2.63 × 10¹¹ vg" is a statement
whose two endpoints could each be off by the whole interval. **This is not pedantry about notation; it is the
reason the next item cannot be resolved.**

### 4.2 🔴🔴 The non-monotonicity — and it needs no figure at all

Two sentences, **both running text, both from my own in-act fetch of `PMC13343157`, both about the
WPRE-*lacking* hSynI vector** (the Fig 3 series is introduced as *"AAV9-hSynI-WWOX vectors **lacking the WPRE
element**"*):

> *"Increasing the dose of the WPRE-lacking vector to **8 × 10[¹⁰] vg** was associated with improved outcomes,
> **including rescue of lethality** and normalization of growth and glucose levels."*

> *"Behavioral testing could not be performed in untreated-null mice due to severe morbidity and early
> lethality, and **LD-treated mice did not survive to P90**; therefore, analyses were limited to WT and
> HD-treated groups."*  — LD = **1.23 × 10¹¹ vg**, i.e. **≈1.5× higher**.

**As written, a lower dose rescues lethality and a higher dose does not.** Four readings are open and this act
cannot choose between them:

| Reading | What would settle it |
|---|---|
| **(a) The two figures use different dose units** — one per hemisphere, one total. At 8 × 10¹⁰ *per hemisphere* = 1.6 × 10¹¹ total, the ordering reverses and monotonicity is restored | the unit, §4.1. **This is the single cheapest resolution and it is unavailable from the text** |
| **(b) "Rescue of lethality" names two different endpoints** — survival to the Fig 2 horizon (~50 d) vs survival to P90/P300. LEGEND's panel read has Fig 2 drawn to ~50 d and Fig 3 to 300 d | a stated follow-up duration for the Fig 2 arms. The word *"rescue"* is used for both |
| **(c) One of the two sentences is wrong.** The prior session independently recorded a Fig 2B panel read in which the `8E10` arm **died at ~17 days**, flatly contradicting the text — and honestly declined to assert it, having already made two colour-reading errors on this paper | a re-read of Fig 2B by an actor with panel access |
| **(d) Vector preparation differs between the arms** — §4.3 | a lot/vendor statement per arm |

🔵 **What is new here, and why it matters more than the earlier form of the observation.** The repository records
this tension **as a panel-reading uncertainty** — *"An apparent conflict at 8 × 10¹⁰ that I am NOT asserting …
I am not confident in my panel reading"*. 🆕 **The conflict does not depend on any panel.** Both sentences are
running text in the same fetch. **A conflict between two sentences cannot be dissolved by distrusting a
figure**, and the prior session's honest self-doubt had the side effect of parking a text-level contradiction as
an image-level one.

### 4.3 🆕 Two measurement facts that make "2.1-fold" softer than it reads

- 🔴 **Both papers titrate by qPCR, and only by qPCR.** `42422765`: *"Viral titers were determined by RT-qPCR
  using bGH primers."* `34747138`: *"Viral titer was measured by qRT–PCR using bGH primers."* No orthogonal
  method, no reference standard, no replicate titration is reported in either. **A 2.1-fold nominal separation
  is being asked to carry a qualitative survival difference, and the only instrument that defines it is a single
  qPCR assay against a plasmid-derived amplicon.** ⚠️ I make **no** claim about the size of that assay's error
  here — I state that **the paper reports none**, and that a dose axis with no titration-uncertainty statement
  cannot have a 2.1-fold step declared resolvable.
- 🔴 **Four vector sources appear in one Methods paragraph, and no arm is assigned to any of them.**
  Verbatim: *"These vectors were packaged into AAV9 serotypes (**Fujifilm Diosynth Biotechnologies** …;
  **Vector Biolabs** …; **Boston Institute of Biotechnology [BIB]** …). Custom-made AAV9-CBA-hWWOX and
  AAV9-hSynI-EGFP viral particles were obtained from the **Vector ELSC Core Facility** at the Hebrew
  University."* **The paper does not say which preparation produced the LD arm and which the HD arm, or whether
  they came from the same lot.** ⇒ I cannot exclude that the LD/HD comparison is partly a **preparation**
  comparison. **This is an "I could not verify", not an allegation** — and it is the kind of statement a
  dose-ranging study normally makes and this one does not.

### 4.4 Is the threshold supported by more than one comparison?

| Comparison | Independent of the LD-vs-HD pair? | Verdict |
|---|---|---|
| LD vs HD survival, `p < 0.0001` | no — it **is** the pair | the anchor |
| LD vs KO+RI, `p < 0.0001`; HD vs WT, `p = 0.78` | partly — they place LD and HD against **controls** | ✅ these are what make "LD improves but does not rescue" **the paper's own tested statement**, not an inference from a curve. Genuinely supportive |
| 4 × 10¹⁰ and 8 × 10¹⁰ arms (Fig 2) | 🔴 **no** — different construct family (±WPRE), different follow-up, **and §4.2** | ❌ **cannot be used to extend the series.** This is precisely the cross-figure move the prior session retracted, and the retraction was correct |
| Glucose at P20: `*` WT-vs-LD, `**` LD-vs-HD, `ns` WT-vs-HD | ✅ **a second endpoint separating the two arms in the same direction** | ✅ **the strongest corroboration that exists** — and it is a *metabolic* endpoint, not survival |
| GFAP at LD vs HD (S7H): LD `**` above WT, HD `ns` | ✅ third endpoint, same direction | ✅ supportive, supplementary-dependent |
| Expression (vector genomes, mRNA) | 🔴 **7 of 8 `ns`** | ❌ **the mechanism layer does not separate the arms at all** |

⇒ **VERDICT.** **A two-arm step with three concordant endpoints (survival, glucose, gliosis) and no expression
correlate, whose two arms are separated by a nominal 2.1× on an unstated unit with no titration-uncertainty
statement, and whose own paper asserts rescue at a lower dose.** That is **not a dose–response curve**, and it
is also **not a clean threshold**. The honest object is: **one ordered pair of doses, replicated across three
endpoints within one experiment, with the dose axis itself unresolved.** The repository's existing formulation —
*"a threshold, not a graded continuum"* — is **closer to right than the paper's "clear dose-response
relationship"**, and it is **still one word too confident**, because a threshold is a claim about a function and
two points do not define one.

🔴 **And the paper's own strongest sentence overreaches both.** Verbatim, in-act: *"we identified a clear
dose-response relationship, **providing strong mechanistic evidence of on-target activity and enabling
definition of an optimal therapeutic dose**."* The mechanistic layer (Fig 5) is **7 of 8 `ns`**. **"Mechanistic
evidence" is asserted on the one layer that failed to distinguish the arms.**

---

## 5 · 🔴 Task 3 — survivor conditioning, per arm, with numbers

**Rule applied literally: a denominator selected on the outcome is not a denominator.**

### 5.1 `42422765` — what is held, and what I could and could not re-verify

| Fact | Status in this act |
|---|---|
| **S5A–S5D label the last four treated animals "Dead" (one HD, three LD)** | 🔴 **NOT re-verifiable here.** The supplementary PDFs (`mmc1.pdf`, `mmc2.pdf`) are not in this worktree and every retrieval route is egress-blocked. It stands as a **prior-session figure attestation** and I neither confirm nor doubt it — I state its provenance |
| The words `dead`, `died`, `survivor`, `excluded` (of animals) | 🆕 **verified absent from the 48,780-char body**: `dead` → 0; `died` → 1 and it is the word *"stu**died**"*; `survivor` → 0. ⇒ **the animal deaths are recorded only in panel labels, nowhere in the paper's prose.** A reader of the text alone cannot know any treated animal died |
| *"mice from either treatment group that failed to survive exhibited reduced WWOX expression, reinforcing the link between effective protein restoration and survival"* | 🟢 **verified verbatim in-act.** 🔴 This is **the paper's mechanism sentence for its own central tension, and it is a comparison of survivors against non-survivors** — conditioned on the outcome it explains |

### 5.2 🆕 🔴 `34747138` — the censoring nobody has stated, and it is in the legend

**Verbatim, from the figure legends in my own in-act fetch (the extractor deleted every `n =`, so `total= 18`
reads for `total n = 18`):**

> Fig 1C: *"Kaplan–Meier survival graph indicates prolonged life span of knockout mice injected with
> AAV9-hSynI-mWwox [**total= 18, spontaneously dead= 6, mice taken out for
> electrophysiology/electron microscopy/analysis, are shown in yellow,= 12**] compared to mice injected with
> AAV9-hSynI-GFP (= 6) or the non-injected (= 8); < 0.0001, log-rank Mantel–Cox test."*

> Fig 2C: *"Kaplan–Meier survival graph indicates prolonged life span of knockout mice injected with
> AAV9-hWWOX [**total= 16, alive= 6, spontaneously dead= 6, 4 mice (shown in yellow) were taken out for
> analysis**) compared to the non-injected (= 8)]"*

| Arm | Total | Spontaneous deaths | **Removed by the investigators** | Remaining alive | Mortality among the non-removed |
|---|---|---|---|---|---|
| KO + AAV9-hSynI-**mWwox** | **18** | **6** | **12 (67 %)** | 0 stated | **6/6 = 100 %** of animals not removed |
| KO + AAV9-**hWWOX** | **16** | **6** | **4 (25 %)** | **6** | **6/12 = 50 %** |
| KO + AAV9-hSynI-GFP | 6 | — | — | — | control |
| non-injected KO | 8 | — | — | — | control |

🔴 **Consequences, and this is the largest single addition of this node.**

1. **The proof-of-concept survival curve for the entire programme is a curve in which the investigators removed
   two thirds of the animals in its main arm.** Animals removed for electrophysiology, EM and histology are
   removed **at scheduled times and in usable condition** — i.e. **plausibly informative censoring**, in the
   direction that flatters survival. The paper does not test that, and **neither do I**: I state that the
   censoring is 12/18, that its mechanism is non-random by construction, and that **no sensitivity analysis
   exists**.
2. **The two arms of the same experiment disagree on mortality among non-removed animals — 100 % vs 50 %** — and
   the paper's own conclusion is *"No difference was noted when using the murine or human WWOX vectors."* That
   sentence is about expression and phenotype; **applied to survival it is not supported by these two legends.**
3. 🔴 **The repository reads this legend as the clean case.** `denominator_audit_therapeutic_portfolio_20260922.md`
   §2 scores TX-007 *"🟢 **REPORTED.** Repudi 2021 gives the arms verbatim"* and §3.1 makes TX-007 **the
   out-of-sample case where the denominator IS reported**. 🆕 **The denominator is reported and it is
   survivor-shaped in the 2021 paper too — not only in the 2026 one.** The audit's own fourth case ("a reported
   denominator selected on the outcome") applies to **both** primaries, which strengthens the case it names and
   weakens the clean-example role it was given.

### 5.3 🆕 Which endpoints are conditioned on survival — per endpoint, as the task asks

| Endpoint | Conditioned on survival? | Basis |
|---|---|---|
| **Survival (Fig 3B, Fig 1C/2C 2021)** | ⚪ it **is** the outcome — but the 2021 curves are **censoring-conditioned**, §5.2 | legends, in-act |
| **Behaviour at 3 months (Fig 4)** | 🔴 **YES, and by design, in the authors' own words**: *"LD-treated mice did not survive to P90; therefore, analyses were limited to WT and HD-treated groups."* Methods confirm: *"Behavioral assessment was conducted on WT + RI and KO rescued mice (HD)"* | verbatim, in-act |
| **P180 glucose** | 🔴 **YES** — the LD arm is absent from the panel because, per Fig 3B, none survived | LEGEND panel read + the P90 sentence |
| **P240/P300 expression persistence (S5)** | 🔴 **YES** — measured in animals alive at P240/P300 | text: *"widespread, stable expression was maintained at P240 and P300"* |
| **The expression/survival link (S5A–S5D)** | 🔴 **YES, and doubly** — it is survivors **versus** non-survivors, i.e. the conditioning **is** the analysis | verbatim, in-act |
| **P30 vector genomes / mRNA / protein (Fig 5)** | 🟡 **partly** — P30 precedes the LD arm's ~90-day collapse, so LD animals are present; but any animal already dead by P30 is absent, and the panel labels are the only record of deaths | inference from Fig 3B; stated as inference |
| **ECoG at P14–P21 (Fig 7)** | 🟢 **NO** — before the survival divergence. n = 5/group | caption attestation |
| **Glucose at P10 / P20** | 🟢 **NO** — before the divergence. **This is why the P20 `*`/`**`/`ns` pattern is the most valuable corroboration of the dose step (§4.4): it is the one arm-separating endpoint that survival cannot have manufactured** | LEGEND panel read |
| **Fertility (20 breeding cages/group)** | 🔴 **YES, necessarily** — only surviving adults breed. And 🆕 the 2026 Methods state *"Heterozygote or **KO rescued mice (KO injected with AAV9-hSynI-hWWOX) were used for breeding** to generate KO mice"*, so treated survivors are also **parents of the cohorts** | verbatim, in-act |

⇒ **Of the endpoints that define `TX-007`'s efficacy, the two earliest (ECoG, P10/P20 glucose) are free of
survivor conditioning and the rest are not.** That is a **usable** result: the arm-separating evidence that
survives the objection is **metabolic and electrographic, measured before P30** — and those, not the behaviour
or the P300 expression, are where an independent replication would have to look.

---

## 6 · Task 4 — the regional (cerebellar) signal, kept strictly separate

🔴 **Separation rule, restated so it binds this section.** What follows is a **biodistribution observation about
one organ**. It is **not** a dose statement, **not** evidence about the ceiling, and **not** a claim that the
therapy fails or that ataxia will not respond. Conversely, **no dose number below may be read as regional
coverage.** `CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01` §1b-bis already argues this separation at length and
better than I could; I do not restate its table.

### 6.1 What the repository holds (theirs, not re-derived)

Cerebellar WWOX relative to WT: **1.4×** and **0.6×** on two P300 HD panels; **0.7 / 0.5 / 0.7** (LD) and
**0.7 / 0.5 / 0.2** (HD) on the P30 blot lanes; **0.1–0.4×** without WPRE at low dose; **6.2×** with WPRE at
4 × 10¹⁰. `DL-MECH-009`: WPRE boosted cerebellum **16.7×**, the largest of four regions — and WPRE was removed.
Cerebellum is **`ns`** on both vector genomes and mRNA between LD and HD (Fig 5, ≈320→≈730 and ≈37→≈95).

### 6.2 What I add, in-act, and only what is separable from dose

- 🟢 **Verified in-act:** `cerebell` occurs **7 times** in the 2026 body. **Every one is an expression,
  distribution or immunoblot mention. There is no cerebellar functional endpoint of any kind** — no
  cerebellum-specific behaviour, no Purkinje measure, no cerebellar histology quantification in the main text.
  ⇒ **the organ carrying the ataxic phenotype has an expression readout and no outcome readout.**
- 🟢 **Verified in-act, 2021 paper:** cerebellum appears there **only** as one of three regions in which
  transduced NeuN⁺WWOX⁺ cells were counted (*"cortex, hippocampus, and cerebellum"*, *"range between 60 and
  70 %"*) and as one of three regions with improved MBP staining. **Also no cerebellar functional endpoint.**
  ⇒ **across both primaries, over five years, no cerebellar outcome has ever been measured.**
- 🆕 **And this is the part that must not be merged with dose:** the 2026 transduction figure is **~40 % → 55–60 %
  of NeuN⁺ neurons** (*verified in-act*: *"rising from ∼40% to ∼55%–60% following treatment"*), against the 2021
  paper's **60–70 %**. **The later, higher-dose, stereotaxic study reports a *lower* neuronal transduction
  fraction than the earlier, lower-dose, free-hand one.** ⚠️ The two numbers are **not comparable** — different
  constructs (±WPRE), different quantification (the 2026 text says the WPRE signal was *"precluding
  quantification"*), different regions pooled. **I therefore assert nothing from the comparison** except that
  **"higher dose" and "more neurons reached" are not the same quantity in this corpus**, which is exactly the
  confusion §6's separation rule exists to prevent.

### 6.3 🆕 🔴 The human-cell arm — where the "no level control" evidence lives — has **no recorded dose at all**

The 0.4×–7× protein spread across rescued human lines, and the SATB2 overshoot to ~11×, come from
**`PMID 42397075`**. Searching LEGEND's entire record for that paper — the 368-line dossier and the manifest —
for `vg`, `MOI`, `titer`, `titre`, `dose`: **the only hit is `125 nM`, the A51 small molecule.** The paper is
**not fetchable** (no PMCID, re-verified in-act).

⇒ **The strongest evidence in the portfolio that AAV9-WWOX does not set an expression level is evidence whose
own dose is unknown to this repository.** The 17-fold spread across lines therefore **cannot be attributed to
dose, to line, or to anything else**, because one of the two variables is unrecorded. ⚠️ **I do not claim the
paper omits it** — only that LEGEND's record does, and that this is a **retrieval debt**, not a finding about
the paper.

---

## 7 · 🎯 Task 5 — replication. Every query, count, translation and control

### 7.1 The queries

| # | Query | `total_count` | Translation checked? | Reading |
|---|---|---|---|---|
| Q1 | `WWOX AND (gene therapy OR AAV OR adeno-associated OR gene replacement OR gene transfer)` | **78** | ✅ fully expanded — `"wwox"[All Fields]` OR the supplementary concept, AND the MeSH/all-fields expansions of each therapy term | the broad frame |
| Q2 | **`WWOX AND (AAV9 OR AAV OR adeno-associated)`** | 🔴 **3** | ✅ expanded, no punctuation, no bare number, no UID collapse | **`42422765` · `34747138` · `42128308`** — two primaries **and a review**, one laboratory |
| Q3 | `(WOREE OR SCAR12 OR "WWOX-related epileptic encephalopathy") AND (gene therapy OR AAV OR restoration OR rescue)` | **8** | ✅ expanded | `42422765` `42397075` `42128308` `41442931` `38161429` `34747138` `34268881` `32037574` — the last three of those are **a vigabatrin-MRI case report, a neuroimaging mini-review and a case report**, i.e. not therapy studies |
| Q4 | `WWOX AND (adenoviral OR adenovirus OR lentiviral OR lentivirus OR retroviral) AND (gene transfer OR transduction OR restoration OR overexpression)` | **17** | ✅ expanded | the **cancer-era** viral WWOX gene-transfer literature, 2005–2025. **A different disease axis, a different endpoint, and no nervous-system dose–response** |
| Q5 | `WWOX AND (neuron OR neuronal OR brain OR cortical OR hippocampal OR cerebellum) AND (gene transfer OR transduction OR ectopic expression OR restoration OR replacement)` | **25** | ✅ expanded | the neuro restoration frame; contains the same three Aqeilan items plus unrelated hits |
| Q6 | `Wwox AND (rat OR rats OR zebrafish OR Drosophila OR canine OR porcine OR nonhuman primate) AND (gene therapy OR AAV OR seizure OR epilepsy)` | **11** | ✅ expanded | **no gene-replacement study in any non-mouse species** |
| Q7 | **`Aldaz CM[Author] AND Wwox AND (mouse OR mice)`** | **18** | ✅ author index resolved (`aldaz, cm[Author]`) | **an independent laboratory with WWOX mouse models. Intersection with Q2 = ∅** |
| Q8 | `Aqeilan RI[Author] AND WWOX AND (gene therapy OR AAV OR organoid OR rescue OR restoration)` | **18** | ✅ | contains **all** of Q2 and both organoid papers |
| **PC1** | **`SCN1A AND (AAV9 OR AAV OR adeno-associated)`** | ✅ **25** | ✅ identical query **form** to Q2 | 🟢 **positive control passes: the form finds a gene-therapy literature when one exists.** Q2's `3` is a measurement, not a parser artefact |

### 7.2 🔴 The three ways a zero here would be meaningless — checked, one by one

| Failure mode | Checked how | Result |
|---|---|---|
| **(a) punctuation makes PubMed echo the query unexpanded** | I read `query_translation` for **every** query above | 🟢 **all nine expanded correctly** into MeSH + All-Fields alternations. No query was echoed raw. No count above is a punctuation artefact |
| **(b) a bare number becomes `[UID]`** | no query contains a bare number | 🟢 not applicable — and deliberately so: I used no numeric tokens |
| **(c) `[All Fields]` does not index Methods** | 🔴 **demonstrated live, on this exact paper** | 🔴 **`WWOX AND (clinical trial OR first-in-human OR investigational new drug OR intracerebroventricular)` → 10 records, and `42422765` and `34747138` are NOT among them** — although **both delivered their vector by ICV** and both use the word in their body (*"intracerebroventricular (ICV) delivery"*, verified in-act). **The two papers that unquestionably did the thing are invisible to a query for the thing, because the word lives in the Methods.** ⇒ **the bound on my negative is explicit: a replication that mentioned AAV-WWOX only in its Methods would not appear in Q2.** I judge that unlikely for a replication study, whose abstract would carry it — but it is a limit, not a certainty |

### 7.3 The answer

🔴 **No independent laboratory has replicated any part of the WWOX gene-replacement dose biology. Nobody has
replicated any part of WWOX gene replacement at all.**

| Claimed corroboration | What it actually is |
|---|---|
| `34747138` (2021) as "independent proof of concept" | 🔴 **not independent.** **Aqeilan RI is senior author of both primaries**; **Repudi S is first author of 2021 and third author of 2026**; both from *The Concern Foundation Laboratories … Hebrew University-Hadassah*, verified from PubMed author affiliations in-act. **Same laboratory, same senior author, overlapping first authors** |
| `42128308` (2026 review) | 🔴 **the same four authors reviewing their own two papers** (Obeid, Wang, Abudiab, Akkawi, Aqeilan). Its abstract states *"restoration of neuronal WWOX expression using AAV-based gene therapy rescues seizures, myelination defects, and survival in preclinical models"* — **a self-citation, at `abstract-depth`, which would double-count if read as support** |
| `42397075` and `34268881` (organoids) | 🔴 **same laboratory** (Aqeilan senior on both). Also **different modalities**: `34268881` uses an **AAVS1 knock-in under the UBP promoter** and a **lentivirus**, not AAV9. ⇒ **cannot corroborate AAV9 dose biology** |
| "mWwox ≈ hWWOX, replicated" (`DL-MOL-005`) | 🔴 **a within-study transgene-sequence control in one experiment**, not a replication — and §5.2 shows the two arms' survival denominators behave differently |
| The n = 1 human administration | 🔴 **the same programme**: three authors of `42422765` are **employed by Mahzi Therapeutics**, the senior author is **a consultant** for it, and the work **was supported by** it (verbatim in LEGEND's locator file; the 2021 paper declares **no** conflict). **A sponsor-funded first-in-human is the programme's next step, not an independent test of it** |

✅ **This is exactly the shape the task anticipated, and it is consistent with what the repository already found
about the rat seizure data.** A **well-evidenced "single laboratory, never replicated"** is the finding.

### 7.4 Two routes that returned nothing, with their causes named

- `mcp__Scholar_Gateway__semanticSearch`, asked directly whether any laboratory has independently replicated
  AAV9-WWOX dose-response rescue: **15 passages, 7 unique articles, publication range 2007-05-29 → 2012-12-18**
  — *Conditional inactivation of the mouse Wwox tumor suppressor gene…*, *WWOX: Its genomics, partners, and
  functions*, *WWOX hypomorphic mice display a higher incidence of B-cell lymphomas…* and four similar.
  ⇒ 🔴 **a corpus-coverage gap, not a field negative**: that corpus contains **no WWOX gene-therapy literature
  at all**. Recorded so nobody reads its silence as evidence.
- ⚠️ **A method caution worth one line.** A WebSearch for independent replication returned nine links — **every
  one of them the same two papers or their preprints** — and its AI-generated summary nonetheless concluded
  *"The search results show publications from multiple laboratories and confirm this is an active area of
  research."* **That sentence is false and was generated from a result set of one laboratory.** It is the
  cheapest available demonstration of why a summarizer's gloss is not a census, and why every count in §7.1
  carries its query.

---

## 8 · Task 6 — the one experiment that would settle the dose question

**Named, because the evidence does support naming one — and it is *not* the one the repository has queued.**
`CLAIM 011`'s `REVIVAL_TRIGGER` asks for **an intermediate dose arm between 1.23 and 2.63 × 10¹¹ vg**. That is
the right instinct and, after §4, it is **not yet the binding experiment**, because an intermediate arm placed
on an axis whose **unit is unstated (§4.1)**, whose **titration uncertainty is unreported (§4.3)** and whose
**own prose is non-monotone (§4.2)** would produce a third point on a ruler nobody has calibrated.

🎯 **The binding experiment, in one design.** A **single-lot, unit-declared, four-arm ICV dose series in the
`Wwox`-null mouse**, in which:

1. **one vector lot** is used for every arm, and the paper states the lot, the vendor and a **titration with two
   orthogonal methods** (e.g. qPCR **and** a droplet-digital or ELISA-based capsid/genome assay) with its
   coefficient of variation;
2. **the dose is reported both per hemisphere and as a total**, with the injected volume, in the same sentence;
3. arms span the **4 × 10¹⁰ → 2.63 × 10¹¹** range **at one fixed WPRE configuration** — at least four doses
   including 8 × 10¹⁰ and 1.23 × 10¹¹, which is the pair §4.2 says the literature currently contradicts itself
   on;
4. **survival is followed to a single pre-declared horizon in every arm** (the Fig 2 / Fig 3 horizon mismatch is
   the cheapest of the four candidate explanations in §4.2 and is fixed by protocol, not by analysis);
5. **every animal removed for tissue is pre-scheduled and pre-declared**, and the Kaplan–Meier is reported
   **twice — with and without censoring** (§5.2 is why);
6. the **arm-separating endpoints that survive survivor conditioning — ECoG at P14–P21 and glucose at P10/P20
   (§5.3) — are primary**, not survival, so the dose–effect relation is measured on quantities that survival
   cannot manufacture;
7. **achieved WWOX protein per region is reported per animal**, so the expression axis can be regressed on the
   dose axis instead of compared as group means (which is what produced 7 of 8 `ns`).

🔵 **And it should be done, at least once, by a laboratory that is not the originating one** — §7 is the reason.
An independent replication of items 6 and 7 alone, at two doses, would be more informative than a third dose arm
from the same group.

❌ **Explicitly not named as experiments:** anything involving a molecule, a route selection, a human dose, or a
safety endpoint framed as establishing safety. §9 and the header govern.

---

## 9 · What I could not verify

| Item | Why | What it would take |
|---|---|---|
| **Any exponent, by direct inspection of the primary markup** | 🔴 `eutils.ncbi.nlm.nih.gov`, `pmc.ncbi.nlm.nih.gov`, `europepmc.org`, `www.biorxiv.org` all `connect_rejected` / `EGRESS_BLOCKED` by the agent proxy. **Measured, with timestamps, not assumed** | one route to raw JATS XML or to the PDF |
| **Any figure or supplementary panel of `42422765`** | not in this worktree (`files/` absent); PMC PDF routes blocked | the shared evidence tree, or the `pmc_pow_fetch.py` route from a deployment with egress |
| **The "one HD and three LD animals Dead" labels in S5** | same | a re-read of `mmc1.pdf` p. — by an actor with the file |
| **`PMID 42397075` at any depth** | 🔴 **no PMCID exists**, re-verified in-act (`convert_article_ids` returns the PMID alone) | the local PDF in the shared tree |
| **Whether the 2021 vector contained WPRE** | 🔴 **the 2021 Methods do not mention WPRE at all** (verified in-act: *"Murine or human cDNA was cloned under the promoter of human in pAAV"*). The repository states WPRE was *"the configuration of the 2021 proof-of-concept"* — **that is an inference from Obeid 2026's framing (*"we generated … vectors lacking the WPRE element"*), not a statement in the 2021 paper** | the 2021 Appendix Fig 1 (vector map), unread |
| **Which vector preparation / lot produced the LD and HD arms** | 🔴 the paper names **four sources** and assigns none | the authors, or a lot statement |
| **Whether `vg` means per hemisphere or total** | 🔴 absent from running text, from the Fig 3A read and from the S7I caption | the Figure 3 legend at full resolution, or the Methods of the preprint |
| **Whether a replication exists that names AAV-WWOX only in its Methods** | 🔴 `[All Fields]` does not index Methods — **demonstrated live in §7.2(c)** | a full-text search engine with Methods indexing |
| **The 2026 review's content** | no PMCID; `abstract-depth` only | a non-PMC route |
| **`n` and `p` values for any 2026 arm** | 🆕 **zero `n = ` tokens and zero P-value tokens survive extraction, and the extracted body has no captions at all** | the 88,241-char HTML surface, or the PDF |

---

## 10 · 🔴 Findings that contradict a repository assertion

**Four, ordered by how load-bearing they are. Each names the file and what it says.**

**C-1 — The journal of `PMID 42422765` is wrong in three places, three different ways.**
PubMed metadata, retrieved in-act: journal **`Molecular therapy. Advances`**, ISO abbreviation **`Mol Ther Adv`**,
**vol 34, issue 3, page 201791**, PMCID `PMC13343157`, DOI `10.1016/j.omta.2026.201791`.
- `tx007_genotype_class_ceiling_20260921.md` §8 and `CC-20260921-…-01`: *"**Mol Ther Oncol**"* — wrong.
- `PMID42422765_partial_locators.md` header: *"**Mol Ther Methods Clin Dev**"* — wrong.
- `DL-MOL-005`: *"**OMTA (Mol Ther Methods Clin Dev)** vol 34"* — the volume is right, the expansion is wrong.
**The DOI is correct everywhere; only the journal name drifted, and it drifted into three mutually inconsistent
values.** ⚠️ Worth stating plainly because the repository's own near-miss note on this paper concerns **a DOI
reconstructed from memory of the journal**. The journal name was never corrected afterwards, and `omta` was
expanded from recall three times. **Same failure class, same paper, still live.**

**C-2 — `DL-MOL-005` calls the 2021 study independent. It is not.**
Verbatim: *"proof-of-concept 2021 **indipendente**"*, and in its evidence line *"proof-of-concept 2021
indipendente"* is listed under **supports**. From PubMed author records, in-act: **Aqeilan RI is the senior
author of both**; **Repudi S is first author of 2021 and third author of 2026**; same institution on both.
⇒ **the ledger's highest-belief therapeutic entry counts a same-laboratory predecessor as independent
corroboration.** This is the single most consequential correction in this file, because `DL-MOL-005`'s belief is
recorded as **`alto`** and its stated basis is *"convergenza multi-livello"*.

**C-3 — the 2021 survival denominators are censoring-conditioned, and the denominator audit uses them as its
clean case.** §5.2. `denominator_audit_therapeutic_portfolio_20260922.md` §3.1 makes TX-007 the **out-of-sample
case where the denominator IS reported** and concludes from it that *"a reported denominator is neither
necessary nor sufficient for soundness"*. That conclusion survives — but **the example is stronger than the
audit realised**: the 2021 legends report `total n = 18` **and** that **12 of the 18 were taken out for
analysis**. The audit quotes the legend string and does not read the censoring inside it.

**C-4 — the `8 × 10¹⁰` tension is a text-versus-text contradiction, not a panel-reading doubt.** §4.2. The
locator file records it as *"An apparent conflict at 8 × 10¹⁰ that I am NOT asserting … I am not confident in my
panel reading"*, with *"the presumption in favour of the text until someone looks again"*. 🔴 **Granting the
presumption to the text is what creates the contradiction**, because the other side of it is also text: *"LD-
treated mice did not survive to P90"*. **No figure is involved on either side.**

**Plus one smaller correction and one non-correction, both recorded so neither is re-found as new:**
- **C-5.** `tx007_genotype_class_ceiling_20260921.md` §0 cites *"its **30-locator** manifest"* and receipt
  `FTR-20260810-42397075-04` for `PMID 42397075`. The manifest on disk, `deepdive_manifests/PMID42397075.json`,
  carries **6** `verbatim_locators` and names receipt **`FTR-20260810-42397075-03`**. The 30 locators are
  plausibly in the 368-line dossier rather than the manifest; **the artefact named does not hold the count
  attributed to it**, and a reader following the citation finds 6.
- ⚪ **A suspicion I raised and then killed, recorded because killing it is the result.** Since `34268881`'s
  rescue line `W-AAV` is named after the **AAVS1 locus** and not after adeno-associated virus (§3.1), I checked
  whether LEGEND's `AAV9` attribution for `42397075` might be the same confusion. **It is not.** The dossier
  quotes the paper verbatim: *"neuron-targeted **AAV9-hSynI-WWOX** restoration effectively rescued neuronal…"*
  and *"the infection with **AAV9-WWOX** of WOREE organoids did not affect the RGs"*. 🟢 **The repository is
  right and my suspicion was wrong.** It is written down because a plausible cross-paper confusion that
  *doesn't* hold is worth as much as one that does.

---

## 11 · Reading debt declared

`python3 framework/scripts/growth_anchors.py check` before this file: `unread_premises=0`. **Every PMID named
above was checked against the full-text queue and the paper registry before being written**, and each is already
cleared by a persisted receipt, a registry record declaring the full text reviewed, or an existing `FT-` entry.
**No PMID was stripped to keep the ratchet at zero, and no new `FT-` number is claimed** — nothing in this file
cites an `FT-` identifier. Two PMIDs surfaced by §7's searches (`42190144`, `42135313`) are **deliberately not
named as premises** anywhere in this file, because they are not load-bearing for any statement in it; they are
search-result members only, and naming them would have opened a debt this node does not need.

---

## 12 · Source attribution

**According to PubMed**, and retrieved from **PubMed / PubMed Central** in this act.

| PMID | Citation | DOI |
|---|---|---|
| 42422765 | Obeid M, Akkawi R, Repudi S, Singh PK, Abudiab B, Jebara T, Berent A, Brennan T, Weiss Y, Shekh-Ahmad T, Aqeilan RI. Neuron-specific WWOX gene therapy produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy. *Molecular Therapy: Advances* 2026;34(3):201791. PMCID `PMC13343157` | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) |
| 34747138 | Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI. Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes. *EMBO Mol Med* 2021;13(12):e14599. PMCID `PMC8649866` | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |
| 42397075 | Steinberg DJ, Zonca A, Abdellatif D, *et al.*, Aqeilan RI. Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026. **No PMCID; not fetchable from this deployment** | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) |
| 34268881 | Steinberg DJ, Repudi S, Saleem A, *et al.*, Aqeilan RI. Modeling genetic epileptic encephalopathies using brain organoids. *EMBO Mol Med* 2021;13(8):e13610. PMCID `PMC8350905`. **Targeted string extraction only** | [10.15252/emmm.202013610](https://doi.org/10.15252/emmm.202013610) |
| 42128308 | Obeid M, Wang J, Abudiab B, Akkawi R, Aqeilan RI. WWOX in brain development and disease: Molecular mechanisms and therapeutic opportunities. *Neurobiol Dis* 2026;225:107446. **Review; same laboratory; abstract-depth** | [10.1016/j.nbd.2026.107446](https://doi.org/10.1016/j.nbd.2026.107446) |
| 36828035 | Aldaz-laboratory SCAR12 cerebellar work — cited in §7 only as a member of the `Aldaz CM[Author]` count, at metadata depth | via PubMed |
| 30290271 | Aldaz-laboratory WWOX mouse work — same, metadata depth | via PubMed |

Scholar Gateway · *Has any laboratory independently replicated … WWOX gene replacement dose-response …?* · 15 passages · 7 articles · 2007-05-29–2012-12-18. 🔴 **Gap stated plainly: that corpus contains no WWOX gene-therapy literature, so its silence is a coverage gap and carries no evidential weight.**

Web sources consulted at **snippet depth only**, never as a read: [PubMed 42422765](https://pubmed.ncbi.nlm.nih.gov/42422765/) · [PMC13343157](https://pmc.ncbi.nlm.nih.gov/articles/PMC13343157/) · [PMC8649866](https://pmc.ncbi.nlm.nih.gov/articles/PMC8649866/) · [EMBO Mol Med 2021](https://www.embopress.org/doi/full/10.15252/emmm.202114599).

---

**End.** Read-only toward every canonical file; nothing promoted, nothing committed. **No molecule, no dose
recommendation, no route recommendation, no safety claim, no druggability score.** *"No overt toxicity observed"*
appears in this file only as a quotation of what the authors wrote and is nowhere converted into safety.
**Not medical advice.**

---
Results retrieved by Scholar Gateway · Summary generated by AI — verify claims against source documents · Last corpus update: September 2026 · [Content coverage details](https://support.scholargateway.ai/s/article/Available-Content)
