# `TX-007` — dose-unit forensics: is the ~2.1× LD→HD step real, or an artefact of the unit convention?

**Date:** 2026-09-22 · **Actor:** Scientist O · **Node:** `TX007_DOSE_UNIT_FORENSICS`

> **Non-canonical analysis artefact.** READ-ONLY toward the four scientific current files, the registries,
> the receipt ledger and the state manifest. Nothing here changes a claim, a paper record, the working
> model or the tracking log.
>
> **Public edition.** Disease-level reasoning over the WWOX-DEE genotype class. No individual is described.
>
> 🔴 **BLOCK-1, stated once and binding over every line below.** **No molecule is named as a therapy, no
> dose is recommended, no route is recommended, no safety claim is made and no druggability score is
> given.** Every number below is **a dose that a published experiment administered to mice**, reconstructed
> so that the experiment can be audited. **Reporting a dose a paper used is not recommending it, and
> nothing here tells anyone to give, withhold or change any treatment.** *"No overt toxicity observed"* is
> never *"safety established"*. Nothing here is medical advice; it is material for discussion with a
> treating clinical team and for nobody else.

---

## 0 · Surfaces and read depth, declared before any number is used

| Source | Depth **reached in this act** | Measured size | Captions / figures |
|---|---|---|---|
| **`PMID 42422765`** (Obeid *et al.* 2026) | 🟢 **full body fetched and read in-act**, `get_full_text_article(pmc_ids=["PMC13343157"])` | **48,780 characters — measured, byte-identical to the prior wave's measurement** | 🔴 **none.** No figure, no caption, no supplementary panel reached me |
| **`PMID 42422765`** — PubMed **abstract** | 🟢 fetched in-act via `get_article_metadata` — **a different extraction route, not previously tested as a dose surface** | 2,022 chars | 🔴 **carries no dose number at all.** See §3.4 |
| **`PMID 34747138`** (Repudi *et al.* 2021) | 🟢 **full body + figure legends fetched and read in-act**, `get_full_text_article(pmc_ids=["PMC8649866"])` | whole article, legends included | legend text only; no panel seen |
| **`PMID 42128308`** (Obeid *et al.* 2026, review) | 🔴 **route closed, re-verified in-act.** `convert_article_ids(["42128308"])` returns `{"pmid":"42128308"}` and **no PMCID** | 0 bytes | — |
| LEGEND artefacts | `tx007_dose_challenge_20260922.md` (605 lines, **read in full**), `CC-20260922-TX007-DOSE-CHALLENGE-01.md` incl. §9, `CC-20260921-TX007-CEILING-AND-DOSE-CONTROL-01.md`, `PMID42422765_partial_locators.md` (889 lines), `PMID34747138_locators.md`, `PMID34747138_partial_locators.md`, `deepdive_manifests/PMID42422765.json`, `PMID34747138.json` | 🟢 **all read before any retrieval was run** | — |

### 0.1 🔴 Egress: ordered, attempted, measured — not skipped

**The rule is ORDER attempts, never SKIP.** Four routes to primary markup were attempted in this act and
every one failed, with the failure measured rather than presumed:

| Route attempted | Result, measured in-act |
|---|---|
| `WebFetch` → `pmc.ncbi.nlm.nih.gov/articles/PMC13343157/` | `EGRESS_BLOCKED` |
| `WebFetch` → `www.sciencedirect.com/…/S3117387X26001266` | `EGRESS_BLOCKED` |
| `curl` → `pmc.ncbi.nlm.nih.gov`, `doi.org`, `www.ebi.ac.uk/europepmc/…/fullTextXML` | **`CONNECT tunnel failed, response 403`** on all three, HTTP code `000` |
| `WebSearch` (open web, different channel) | ✅ **succeeded** — and its result is itself a finding, §3.3 |

⇒ **The raw JATS/XML and the publisher HTML — the surfaces that would carry `<sup>11</sup>` and settle
every exponent by direct inspection — are unreachable from this deployment.** Established once, recorded,
not retried. `files/` does not exist in this worktree, so **no local artefact of either paper could be
opened**; every figure-derived number below is inherited as a prior-session attestation and is labelled as
such.

### 0.2 🔴 The two-surface divergence, now characterised precisely

The repository holds quotations taken from an **88,241-character local HTML artefact**
(`PMID42422765_Obeid2026_PMC.html`, sha256 `00fadaf4…9bd3`). My route serves **48,780 characters**. The
difference is not merely size:

| | 88,241-char HTML surface (repository quotations) | 48,780-char served surface (this act) |
|---|---|---|
| Figure captions | ✅ **present** — Fig 1 caption quoted verbatim in the locator file | 🔴 **absent.** `Figure 3` → 0 hits; no `Figure N` string anywhere |
| Exponents | ✅ **preserved in flattened form**: `4 × 1010 vg`, `1.23x1011vg` | 🔴 **deleted**: `4 × 10vg`, `1.23 × 10vg` |
| `n =` tokens, P values | ✅ present (`n = 5`, `n = 6`) | 🔴 **zero** surviving |
| Superscript characters | — | 🔴 **zero** in 48,780 chars (measured) |

🔵 **This matters more than "two surfaces differ".** The flattened forms `1010` and `1011` on the HTML
surface are **exponent-bearing**: `1010` = 10¹⁰, `1011` = 10¹¹. The served surface deletes the digits
entirely. **So the repository's own quotations are a better exponent surface than live retrieval is**, and
a session that re-fetches and trusts the fetch over the archive will silently lose ten orders of magnitude.

---

## 1 · The direct answer, before the evidence

> **Primary question: is the ~2.1× LD→HD step robust, or could it be an artefact of an inconsistent
> dose-unit convention?**

# 🟢 **The step is ROBUST. It is not, and cannot be, a unit artefact.**

**The reason is arithmetic, not judgement, and it is the finding this node exists to produce:**

1. 🟢 **The unit ambiguity is a common-mode multiplier, so it cancels exactly in the ratio.** LD and HD are
   stated **in one sentence, in one unit token, for one experiment**, and the Methods deliver **the same
   2.0 μL/hemisphere, bilaterally, to every arm** (verified verbatim in-act, §3.2). Whatever the bare `vg`
   means — per hemisphere, per injection or total — **it means the same thing for both arms**. Therefore:

   **`HD / LD = 2.63 / 1.23 = 2.1382` under *every* permitted reading, identically.** §4.

2. 🔴 **What the ambiguity *does* move is the absolute scale, by exactly 2×** — and only that. Under the
   per-hemisphere reading the animal receives **2.46 × 10¹¹ / 5.26 × 10¹¹ vg**; under the total reading,
   **1.23 × 10¹¹ / 2.63 × 10¹¹ vg**. **Every statement of the form "the threshold lies between 1.23 and
   2.63 × 10¹¹ vg" is uncertain by a factor of 2 in its endpoints and exact in its width.**

3. 🔴 **The prior wave's central framing is wrong, and this is the correction that matters most.**
   `tx007_dose_challenge_20260922.md` §1.5 and §4.1, and `CC-20260922-…-01` §4b, state: *"the
   per-hemisphere-vs-total ambiguity is a factor of **2**. The LD→HD step is **2.1×**. ⇒ **the ambiguity is
   the size of the effect**"*. 🆕 **A common-mode factor is not "the size of" a ratio it cancels out of.**
   The two numbers are numerically similar and **logically unrelated**: one is an uncertainty on the
   *level*, the other is the *separation*. §4.3.

4. **Classification: `AMBIGUOUS BUT BOUNDED`** — the convention is nowhere stated, but every permitted
   reading is bounded, and the bound on the ratio is **degenerate (a single value, 2.1382)**. §5.

5. 🔴 **The non-monotonicity SURVIVES, and the unit work SHARPENS it rather than dissolving it** — because
   the only unit-based escape required a per-figure convention switch, and the paper's own bridge sentence
   positively excludes that. §6. **But it survives on a 🟡 MEDIUM exponent, and the prior wave did not say
   so.** §6.3.

6. ⚪ **What is NOT claimed.** Nothing here says the therapy works or fails, nothing says any dose is safe
   or unsafe, nothing says any dose should be used. The finding is about **what was measured and on what
   scale**.

---

## 2 · Delta — what the prior wave already holds, stated before I add anything

**Read in full first. The following are theirs, not mine, and are not re-derived below.**

| Already held | Where |
|---|---|
| The exponent-deletion defect and the three verbatim `10vg` strings | prior wave §0 · `CC-…-01` §0 |
| LD `1.23 × 10¹¹` / HD `2.63 × 10¹¹`, the 2.1-fold separation, and its provenance in a raster read of `gr3.jpg` | `CLAIM 011` · locator file · prior wave §3.1 |
| The S7I caption as a second exponent surface (`1.23x1011vg`, 200 ppi) | locator file; **counted** by the prior wave §3.1 |
| `4E10` surviving extraction; E-notation as the only exponent-safe form | prior wave §3.1 |
| The 2026 Methods `2.0 μL/hemisphere` bilateral, and the 2021 `~1 µl` free-hand | prior wave §3.2 |
| The 2021 dose as `GC/hemisphere`, explicit | prior wave §3.1 |
| The text-vs-text non-monotonicity (8 × 10¹⁰ "rescue of lethality" vs "LD did not survive to P90") and its four candidate readings (a)–(d) | prior wave §4.2 |
| qPCR-only titration, no orthogonal method, no CV; four vendors and no arm assignment | prior wave §4.3 |
| The 2021 censoring (12/18 and 4/16), survivor conditioning per endpoint, the replication census (Q2 = 3, positive control 25), the `Mol Ther Adv` journal-name correction | prior wave §5, §7, §10 |

✅ **Everything above I treat as settled and do not restate as new.** **My additions are:** §3.2 (the
Methods verified in-act, and the discovery that the 2026 paper states **no dose in its Methods at all**);
§3.3 (the WebSearch surface fails as an exponent surface, contra the prior wave); §3.4 (the abstract route,
newly tested, carries no dose); §4 (**the invariance proof** — the arithmetic under every reading, computed
rather than asserted); §4.2 (**the cross-paper convergence test**, which is exactly symmetric and
adjudicates nothing); §4.3 (the common-mode correction); §6.1 (**the bridge sentence that excludes the
per-figure unit switch**); §6.3 (**the non-monotonicity rests on a 🟡 MEDIUM exponent — and the prior wave's
own "no figure is involved" claim is self-inconsistent**); §7 (the `LD` token overloaded within one paper;
`titer` used for a dose).

---

## 3 · Task 1 — the per-arm reconstruction

⚠️ **Read the BLOCK-1 notice at the head of this file before reading these tables.** These are doses that
published experiments administered to animals. **None is a recommendation of any kind.**

### 3.1 Exponent confidence, per figure

**Scale.** 🟢 **HIGH** = exponent seen on **≥2 independent non-extractor surfaces**. 🟡 **MEDIUM** = one.
🔴 **LOW** = none; inferred. **Every figure is 🔴 by default until a surface is named.**

| Dose as written | Arm | Non-extractor surfaces carrying the **exponent** | Confidence | Unit as written |
|---|---|---|---|---|
| **4 × 10¹⁰ vg** | `42422765` **Fig 1**, four promoters, all +WPRE | **(i)** 🟢 **`4E10` in running text, re-verified by me in-act** — *"all vectors were tested at the same titer (4E10)"*; **E-notation is the only exponent form that survives extraction, and it is the only one in the entire 48,780-char body** (measured: regex for `\d+[eE]\d+` returns exactly one token). **(ii)** Fig 1 caption on the 88k HTML surface: *"AAV9-EF1a-hWWOX-WPRE (4 × 1010 vg, n = 5) … AAV9-hSynI-hWWOX-WPRE (4 × 1010 vg, n = 6)"* — `surface: body`, flattened `1010` | 🟢 **HIGH** | 🔴 bare `vg` |
| **4 × 10¹⁰ vg** | `42422765` **Fig 2 / S3** low arm (±WPRE) | prior-session panel-label read of `gr2.jpg` (`4E10` in the legend key). ⚠️ **The `4E10` sentence is about the Fig 1 promoter series; transferring it to Fig 2 is the exact cross-figure move the prior session corrected itself for twice** — I do not transfer it | 🟡 **MEDIUM** | 🔴 bare `vg` |
| **8 × 10¹⁰ vg** | `42422765` **Fig 2 / S3**, WPRE-lacking higher arm | **(i)** prior-session panel-label read of `gr2.jpg` (`8E10`). 🆕 **I part company with the prior wave's 🔴 LOW here:** the prior session declared its **Fig 2B survival-curve colour read** unreliable — *tracing a coloured curve to an arm*. **Reading a printed `8E10` label in a legend key is a different and far more robust operation**, and it was not what was retracted. **(ii)** parallel construction in-act: *"At a dose of 4 × 10vg … Increasing the dose … to 8 × 10vg"* and *"low expression … at 4 × 10vg … markedly higher levels at 8 × 10vg"* — same figure, same sentence pair, same token form as a 🟢 HIGH 10¹⁰ | 🟡 **MEDIUM** — one label surface + strong internal parallelism | 🔴 bare `vg` |
| **1.23 × 10¹¹ vg** (LD) · **2.63 × 10¹¹ vg** (HD) | `42422765` **Fig 3** (dose-ranging), and Figs 4–7, S5, S7 | **(i)** prior-session raster read of **Fig 3A**, `gr3.jpg` sha256 `c63f930c…4997d`, 104 ppi, `surface: figure`; **(ii)** the **S7I caption** rendered from `mmc1.pdf` at **200 ppi** (`S_p09_200dpi.png`, sha256 `5380be56…0501`): *"KO+W LD (1.23x1011vg) and KO+W HD (2.63x1011vg)"* — flattened `1011` = 10¹¹. **Two different artefacts, two different routes (PMC CDN figure JPG vs supplementary PDF page render), two different resolutions** | 🟢 **HIGH** — but see §3.3: **I could not re-verify either myself**, and the prior wave's third surface does not hold | 🔴 bare `vg` on **all three** surfaces |
| **2 × 10¹⁰ vg** | `42422765` Fig 2E protein columns | prior-session panel attestation only; **no such token exists in the served body** | 🔴 **LOW** | 🔴 bare |
| **2 × 10¹⁰ GC / hemisphere** | `34747138` — the **single** dose of the entire 2021 study, both vectors | **(i)** 🆕 **the repository's own 2021 locator file, taken from a local JATS XML** (`PMID34747138_Repudi2021_PMC.xml`, sha256 `7da156e8…988bb`, body 66,144 chars): *"Approximately 1 μl (2 × 1010 GC/hemisphere) virus was dispensed"* — **flattened exponent intact, `surface: body`**; **(ii)** prior-wave WebSearch snippet. 🆕 **Surface (i) is a primary-markup rendering the prior wave did not count — it rated this 🟡 MEDIUM with "no primary rendering seen". The repository held one in its own dossier.** My in-act fetch returns the same sentence with the exponent **deleted** (*"2 × 10GC/hemisphere"*), confirming the artefact is the extractor's, not the paper's | 🟢 **HIGH** — **upgraded from the prior wave's 🟡** | 🟢 **EXPLICIT: `/hemisphere`**, and the unit is **`GC`**, not `vg` |

🔴 **A property of the document, not of the extractor.** The 2026 doses are bare `vg` on **every surface the
repository holds** — the served body (7/7 occurrences, measured), the 88k HTML **figure caption**, and the
200-ppi **supplementary caption**. `hemisphere` occurs **exactly twice** in the 48,780-char body, both in the
Methods, **never attached to a dose**. `GC` → **0 occurrences**. `per animal` → **0**. `total dose` → **0**.
⇒ **The missing qualifier is not an extraction loss. The paper does not state it.**

### 3.2 🆕 The delivery protocol, verified verbatim in-act — and what it does *not* contain

**`42422765`, Materials and methods, quoted from my own fetch:**

> *"A Micro-4 nano-pump controller was used to ensure a steady injection rate of 1–1.5 μL/min, **delivering
> 2.0 μL/hemisphere** through a Hamilton syringe with a 32G needle (World Precision Instruments). The needle
> was kept at the injection site for 30-60 s to allow proper diffusion and then removed slowly over 1 min.
> **The procedure was repeated for the contralateral hemisphere.**"*

The same paragraph opens: *"The pup (KO or WT) was staged on the stereotaxic frame for **AAV9-hWWOX or RI
delivery**"* — i.e. **one protocol, applied to every arm**, with coordinates relative to **lambda**.

**`34747138`, Materials and methods, quoted from my own fetch:**

> *"**Free-hand** intracranial injections … Trypan blue 0.1% was added to the virus … **Approximately 1 µl
> (2 × 10\[¹⁰\] GC/hemisphere)** virus was dispensed using a NanoFil syringe with a 33G beveled needle …
> **The other hemisphere was injected in the same way.**"*
> *(exponent shown bracketed because my route deletes it; it is supplied from surface (i) of §3.1, not from memory)*

🆕 🔴 **The single most important structural finding of this node, and the repository does not hold it:**
**`PMID 42422765` states no dose anywhere in its Materials and methods.** Measured: all seven `vg` tokens
fall in Results and Discussion (character offsets 8,687–11,497); the Methods section begins at ~33,600 and
contains **volume, rate, coordinates, needle gauge, titration method and four vendors — and no dose value at
all**. ⇒ **The dose and the volume are never in the same sentence, never in the same section, and never in
the same figure.** That is the precise mechanism by which the unit was lost: not a typo, but a structural
separation between where the quantity is stated and where its denominator is defined.

### 3.3 🆕 🔴 The WebSearch surface fails as an exponent surface — contra the prior wave

The prior wave's §3.1 lists, as the **third** of three surfaces supporting the LD/HD exponents:
*"(iii) WebSearch snippet, in-act 2026-09-22, reporting `1.23 × 10¹¹` / `2.63 × 10¹¹`"*.

🆕 **I ran the same route in-act. It returned the exponent deleted.** The search summariser's own words:
*"a low dose (LD, **1.23 × 10 vg**)"*. **The open-web channel destroys the exponent exactly as the PMC
extractor does.**

⇒ **The LD/HD exponents rest on TWO surfaces, not three** — both prior-session renderings of primary
artefacts (`gr3.jpg`, `S_p09_200dpi.png`), **neither of which I could open**. By the stated scale that is
still 🟢 **HIGH** (two independent non-extractor surfaces, different artefacts, different routes). **But the
margin is one surface, not two**, and a reader should know the third was a mirage. ⚠️ This also generalises:
**a search-engine gloss is not an exponent surface**, and the prior wave separately demonstrated that such a
gloss can assert a flat falsehood (its §7.4).

### 3.4 🆕 The abstract route, newly tested — and empty

`get_article_metadata(["42422765"])` is a **different extraction path** from `get_full_text_article`, and
the prior wave did not test it as a dose surface. 🆕 **It carries no dose number whatsoever.** The abstract
says only *"An **optimal** AAV9-hSynI-WWOX **dose** restored survival, growth, metabolic function, behavior,
and fertility to near wild-type levels."* ⇒ **A reader at `abstract-depth` cannot learn any dose, any unit or
any ratio from this paper.** Recorded because it closes a route rather than leaving it untried, and because
it bounds what the companion review (`42128308`, no PMCID, route closed) could have been checked against.

### 3.5 The per-arm reconstruction table

**All 2026 arms: single administration at P0 (or P1–P5 for the window arms), bilateral ICV, 2 injections
(one per hemisphere), 2.0 μL each, 4.0 μL total. All 2021 arms: single administration at P0, bilateral ICV,
2 injections, ~1 μL each, ~2.0 μL total.**

| Study · arm | Reported value, **exactly as written** | Surface I read it on | Per injection / hemisphere / total? | **Evidence establishing which** | Vol/hemi | Hemi | Inj. | Conc. (vg/μL) | **Total vg per animal** |
|---|---|---|---|---|---|---|---|---|---|
| `42422765` **Fig 3 LD** | `1.23 × 10vg` (served) · `1.23x1011vg` (S7I caption, prior session) · `1.23 × 10¹¹ vg` (Fig 3A, prior session) | served body **in-act**; two prior-session figure renderings | 🔴 **UNSTATED** | 🔴 **none.** Bare `vg` on all 3 surfaces; `hemisphere` never adjoins a dose; no dose in Methods | 2.0 μL | 2 | 1 per hemi | **6.15 × 10¹⁰** (per-hemi reading) or **3.08 × 10¹⁰** (total reading) — *derived, not stated* | **2.46 × 10¹¹** or **1.23 × 10¹¹** |
| `42422765` **Fig 3 HD** | `2.63 × 10vg` · `2.63x1011vg` · `2.63 × 10¹¹ vg` | same | 🔴 **UNSTATED** | 🔴 none | 2.0 μL | 2 | 1 per hemi | **1.32 × 10¹¹** or **6.58 × 10¹⁰** | **5.26 × 10¹¹** or **2.63 × 10¹¹** |
| `42422765` **Fig 2 −WPRE high** | `8 × 10vg` (served) | served body **in-act** | 🔴 **UNSTATED** | 🔴 none | 2.0 μL | 2 | 1 per hemi | 4.00 × 10¹⁰ or 2.00 × 10¹⁰ | **1.60 × 10¹¹** or **8.00 × 10¹⁰** |
| `42422765` **Fig 2 ±WPRE low** | `4 × 10vg` (served) | served body **in-act** | 🔴 **UNSTATED** | 🔴 none | 2.0 μL | 2 | 1 per hemi | 2.00 × 10¹⁰ or 1.00 × 10¹⁰ | **8.00 × 10¹⁰** or **4.00 × 10¹⁰** |
| `42422765` **Fig 1**, 4 promoters, all +WPRE | `4E10` (served, running text) · `4 × 1010 vg` (Fig 1 caption, 88k HTML) | served body **in-act**; caption via repository | 🔴 **UNSTATED** — 🆕 **and the paper calls it a *"titer"***, §7.2 | 🔴 none | 2.0 μL | 2 | 1 per hemi | 2.00 × 10¹⁰ or 1.00 × 10¹⁰ | **8.00 × 10¹⁰** or **4.00 × 10¹⁰** |
| `42422765` Fig 2E protein cols | `2 × 10¹⁰` — **prior-session panel attestation only; absent from served body** | 🔴 none in-act | 🔴 UNSTATED | 🔴 none | 2.0 μL | 2 | 1 per hemi | — | **4.00 × 10¹⁰** or **2.00 × 10¹⁰** |
| `34747138` **all arms** (mWwox, hWWOX, EGFP) | `2 × 10\[¹⁰\] GC/hemisphere` (Methods) · `2 × 10\[¹⁰\]` **bare** (Figs 1D, 1F, 2A, 2D–F legends) | Methods + legends **in-act**; exponent from repository JATS quote | 🟢 **PER HEMISPHERE** | 🟢 **stated explicitly in the Methods and once in Results** (*"Viral particles (2 × 10\[¹⁰\]/hemisphere)"*) | ~1.0 μL | 2 | 1 per hemi | **2.00 × 10¹⁰** | **4.00 × 10¹⁰ GC** |

🆕 🔵 **The 2021 paper establishes this laboratory's house style, and it cuts against the total reading.**
In `34747138` the **figure legends write the dose bare** — *"injected with AAV9‐hSynI‐mWwox (2 × 10\[¹⁰\])"*,
*"KO injected with AAV‐hWWOX (2 × 10\[¹⁰\]) at P19"*, four such instances, verified in-act — while **only the
Methods and one Results sentence carry the `/hemisphere` qualifier.** ⇒ **When this laboratory writes a bare
dose, the qualifier it omits is `/hemisphere`.** `42422765` is the same laboratory (Aqeilan senior author of
both; Repudi first author of 2021 and third of 2026, per PubMed author records read in-act), and it **omits
the qualifier everywhere, including in the Methods**. ⚠️ **This is an inference about authorial convention,
not a measurement, and I do not promote it to a determination** — §4.2 shows an equally strong arithmetic
argument pointing the other way.

---

## 4 · Task 2 — `HD / LD` under every interpretation the Methods permit. The arithmetic, shown.

### 4.1 The three permitted readings, and the invariance

The Methods permit exactly three readings of a bare `vg`, and two of them coincide because the protocol
delivers **one injection per hemisphere**:

| Reading | LD total | HD total | **HD / LD** |
|---|---|---|---|
| **(A)** `vg` = **per hemisphere** | 1.23 × 10¹¹ × 2 = **2.460 × 10¹¹** | 2.63 × 10¹¹ × 2 = **5.260 × 10¹¹** | 5.260/2.460 = **2.1382** |
| **(B)** `vg` = **total per animal** | **1.230 × 10¹¹** | **2.630 × 10¹¹** | 2.630/1.230 = **2.1382** |
| **(C)** `vg` = **per injection** (≡ per hemisphere, 1 injection per hemisphere) | **2.460 × 10¹¹** | **5.260 × 10¹¹** | **2.1382** |

# 🟢 `HD / LD = 2.63 / 1.23 = 2.1382` — identical under all three readings.

**Why, stated as a proof rather than a coincidence.** Let *u* be the unknown multiplier converting the
written `vg` to total delivered vg per animal (*u* = 2 under A and C, *u* = 1 under B). The Methods fix
**one** injection protocol — *"2.0 μL/hemisphere … repeated for the contralateral hemisphere"*, applied to
*"AAV9-hWWOX or RI delivery"* — so **the same *u* applies to both arms**. Then

> `HD_total / LD_total = (u · 2.63 × 10¹¹) / (u · 1.23 × 10¹¹) = 2.63/1.23`, **and *u* cancels.**

**A common-mode multiplier cannot change a ratio.** The only way the unit could corrupt the step is if *u*
differed between the LD and HD arms — i.e. if the paper switched convention **within one sentence, one
figure and one experiment**. It does not: both doses appear in the same sentence, in the same token form, in
the same figure, under one Methods protocol.

⇒ **The ~2.1× step is not an artefact of the dose-unit convention. It survives the audit intact.**

**The same invariance holds for the four-point series** (total vg per animal):

| Reading | 4 × 10¹⁰ | 8 × 10¹⁰ | LD | HD | span |
|---|---|---|---|---|---|
| **(A/C) per hemisphere** | 8.00 × 10¹⁰ | 1.60 × 10¹¹ | 2.46 × 10¹¹ | 5.26 × 10¹¹ | **6.58×** |
| **(B) total** | 4.00 × 10¹⁰ | 8.00 × 10¹⁰ | 1.23 × 10¹¹ | 2.63 × 10¹¹ | **6.58×** |

⇒ **Every ratio in this paper is invariant to the unit convention. Only the absolute level moves, and it
moves by exactly 2×.**

### 4.2 🆕 The cross-paper convergence test — and it is exactly symmetric

The 2021 paper gives a fully specified dose (2 × 10¹⁰ GC/hemisphere, ~1 μL/hemisphere, bilateral), so two
quantities can be compared against the 2026 lowest arm (4 × 10¹⁰ vg, 2.0 μL/hemisphere, bilateral):

| Quantity | 2021 (fully specified) | 2026 under **(A) per hemisphere** | 2026 under **(B) total** |
|---|---|---|---|
| **Total per animal** | **4.00 × 10¹⁰ GC** | 8.00 × 10¹⁰ — **2.00×** the 2021 total | 4.00 × 10¹⁰ — 🎯 **1.00×, exact match** |
| **Concentration** | **2.00 × 10¹⁰ GC/μL** | 2.00 × 10¹⁰ — 🎯 **1.00×, exact match** | 1.00 × 10¹⁰ — **0.50×** the 2021 conc. |

🔵 **Each reading reproduces the 2021 experiment exactly on one of the two derivable quantities, and misses
by exactly 2× on the other.** The per-hemisphere reading says the 2026 study **reused the 2021 vector
concentration** and doubled the volume; the total reading says it **reused the 2021 total dose** and halved
the concentration. **Both are coherent experimental narratives. Neither is stated. The convergence test is
exactly symmetric and therefore adjudicates nothing.**

⚠️ **This is a negative result and is reported as one.** It is the strongest arithmetic lever available
without the primary markup, and it does not decide the question. ⚠️ It also **must not be read as evidence
that the two papers are on a common scale**: they are not — the 2021 study injected **~1 μL/hemisphere
free-hand**, the 2026 study **2.0 μL/hemisphere stereotaxically**. Volume and technique both change CSF
distribution, so the *delivered* exposure is not comparable even when the *nominal* numbers are. The prior
wave established this and I do not re-derive it.

### 4.3 🆕 🔴 Why "the ambiguity is the size of the effect" is a category error

The prior wave's load-bearing sentence — repeated in `CC-20260922-…-01` §4b and in its §1.5 — is:

> *"A per-hemisphere vs total ambiguity is a factor of **2**. **The LD→HD step is 2.1×.** ⇒ the unresolved
> unit is **the same magnitude as the entire dose separation** the threshold is built on."*

🔴 **The two numbers are numerically adjacent and logically unrelated, and §4.1 is why.** The factor of 2 is
a **common-mode uncertainty on the level**; the 2.1× is a **within-experiment separation**. A common-mode
multiplier **cancels** out of a ratio — it cannot corrupt the quantity it is being compared to. Setting them
side by side and inferring that one threatens the other is the error, and it is the error on which the prior
wave's §4.1 verdict (*"the ambiguity is the size of the effect"*) and its §4.2 reading **(a)** both rest.

**What the ambiguity does and does not do, stated exactly:**

| Quantity | Affected by the unit ambiguity? |
|---|---|
| **HD/LD ratio (2.1382×)** | 🟢 **NO** — invariant, exactly |
| Four-point span (6.58×) | 🟢 **NO** — invariant, exactly |
| Any within-paper dose ratio | 🟢 **NO** |
| **Absolute dose per animal** | 🔴 **YES — exactly 2×** |
| **Where a "threshold" sits on an absolute axis** | 🔴 **YES — exactly 2×** |
| Comparability to the 2021 study | 🔴 **YES** — and independently broken by volume/technique (§4.2) |
| **Any statement that leaves this corpus carrying an absolute vg number** | 🔴 **YES — 2×** |

⇒ **The correct formulation, which I offer to replace the current one:** *the dose-unit defect does not
threaten the internal dose–response structure of `PMID 42422765`; it threatens every absolute dose number
exported from it, by a factor of 2.*

---

## 5 · Classification

# `AMBIGUOUS BUT BOUNDED`

**Assigned against the three definitions, explicitly:**

- ❌ **not `UNAMBIGUOUS`** — the Methods do **not** fix the convention. The paper states **no dose in its
  Methods at all** (§3.2), and the dose is bare `vg` on every one of the three surfaces the repository
  holds (§3.1). The evidence establishing per-hemisphere-vs-total is, in one word, **absent**.
- ✅ **`AMBIGUOUS BUT BOUNDED`** — the convention is unstated, and **every permitted reading yields a ratio
  within a stated range: the range is the single point `2.1382`** (§4.1). The absolute dose is bounded to a
  closed interval of width exactly 2: **LD ∈ [1.23, 2.46] × 10¹¹ vg**, **HD ∈ [2.63, 5.26] × 10¹¹ vg**.
- ❌ **not `INTERNALLY INCONSISTENT`** — this was tested, not assumed. No two statements in the paper imply
  **mutually incompatible unit conventions**. One Methods, one injection protocol, one volume, one token
  form throughout, and a bridge sentence that **requires** a shared scale across figures (§6.1). ⚠️ The
  paper **is** internally inconsistent in its **nomenclature** (§7) — the token `LD` denotes two different
  doses, and a dose is called a *"titer"* — **but nomenclature inconsistency is not unit inconsistency**,
  and the classification asks about the latter. I record the former in §7 rather than letting it inflate
  the verdict.

🔵 **The bound is unusually tight for an ambiguity of this kind, and that is the substantive result:** the
defect is real, it is a genuine retrieval/reporting failure, and it is **confined to the absolute axis**.

---

## 6 · 🔴 Carried forward: does the unit resolution dissolve the non-monotonicity?

## Answer: **NO. It SHARPENS it** — and then §6.3 partly blunts it again, for a different reason.

### 6.1 🆕 The bridge sentence excludes the per-figure unit switch

The prior wave's reading **(a)** — *"the two figures use different dose units; at 8 × 10¹⁰ per hemisphere =
1.6 × 10¹¹ total, the ordering reverses and monotonicity is restored"* — was called *"the single cheapest
resolution"*. My arithmetic confirms it **works**: 8 × 10¹⁰/hemisphere = 1.60 × 10¹¹ total against LD
1.23 × 10¹¹ total, a **1.30× reversal**.

🆕 **But the paper positively excludes it.** The sentence that closes the Figure 2 section and opens the
Figure 3 section, verified verbatim in-act:

> *"However, this reduction in expression **necessitates the use of higher vector doses** to achieve
> comparable therapeutic outcomes."*
>
> — immediately followed by: *"Building on our optimization studies (;), we generated AAV9-hSynI-WWOX
> vectors lacking the WPRE element … we evaluated two clinically applicable doses: an LD (1.23 × 10\[¹¹\]vg)
> and a higher dose (HD, 2.63 × 10\[¹¹\]vg)"*

🔵 **This sentence is a magnitude comparison *across* Figure 2 and Figure 3.** It asserts that the Figure 3
doses are **higher** than the Figure 2 doses, and offers that as the reason they were chosen. **For that
assertion to be meaningful, the two figures must be on the same scale.** A paper cannot say "we therefore
used higher doses" while silently changing what the number counts.

**Three further facts point the same way:** one Materials-and-methods injection protocol covering all arms;
one volume (2.0 μL/hemisphere) for every arm; one token form (`N × 10ᵉ vg`) across all seven occurrences.

⇒ **Reading (a) requires an unstated, undeclared, per-figure convention switch inside a paper whose own
prose compares the two figures' magnitudes. It is not merely unevidenced — it is contradicted.** 🆕 **The
cheapest explanation for the non-monotonicity has been removed, which is the opposite of dissolving it.**

### 6.2 The tension restated, with the arithmetic

Both sentences are running text, both from my own in-act fetch, both about the **WPRE-lacking hSynI vector**
(the Fig 3 series is introduced as *"vectors **lacking the WPRE element**"*, verified in-act):

> *"Increasing the dose of the WPRE-lacking vector to **8 × 10\[¹⁰\] vg** was associated with improved
> outcomes, **including rescue of lethality** and normalization of growth and glucose levels."*

> *"Behavioral testing could not be performed in untreated-null mice due to severe morbidity and early
> lethality, and **LD-treated mice did not survive to P90**; therefore, analyses were limited to WT and
> HD-treated groups."* — LD = **1.23 × 10¹¹ vg**.

| Scenario | Arithmetic | Outcome |
|---|---|---|
| **Single convention** (what §6.1 supports) | LD / 8 × 10¹⁰ = **1.5375** | 🔴 **a 1.54× HIGHER dose fails where a lower one rescued. Contradiction STANDS.** |
| Fig 2 per-hemi, Fig 3 total *(reading (a))* | 1.60 × 10¹¹ vs 1.23 × 10¹¹ = **1.30** | contradiction dissolves — **but §6.1 contradicts this reading** |
| Fig 2 total, Fig 3 per-hemi | 2.46 × 10¹¹ vs 8.00 × 10¹⁰ = **3.075** | 🔴 contradiction **sharpens** to 3.1× |

**Surviving explanations, now that (a) is excluded — and all are cheaper than biology:**

| Reading | Status after this act |
|---|---|
| **(b) "rescue of lethality" names two different endpoints / follow-up horizons** — Fig 2 drawn to ~50 d, Fig 3 to 300 d (repository panel read) | 🔵 **now the leading explanation.** Untreated KO die by ~15–20 d; **at a ~50-day horizon an LD animal (dead by ~90 d) would also read as "rescued"**. The two sentences are then both literally true and simply not comparable. **The served text states no follow-up duration for the Fig 2 arms** (verified: no horizon statement in that passage) |
| **(c) one of the two sentences is wrong** — the prior session's Fig 2B panel read has the `8E10` arm dead at ~17 d, which contradicts *"rescue of lethality"* **at any horizon** | 🔴 still open; needs panel access |
| **(d) vector preparation / lot differs between arms** — four vendors named, no arm assigned | 🔴 still open; the paper states no lot |
| **(e) 🆕 the `8 × 10` exponent is wrong** | 🔴 **newly raised, and it is the one that would erase the tension entirely.** §6.3 |

### 6.3 🆕 🔴 The non-monotonicity rests on a 🟡 MEDIUM exponent — and the prior wave's own framing is self-inconsistent

The prior wave's §4.2 and §10 C-4 assert:

> *"**The conflict does not depend on any panel.** Both sentences are running text in the same fetch. **A
> conflict between two sentences cannot be dissolved by distrusting a figure.**"* · *"**No figure is
> involved on either side.**"*

🔴 **That is not correct, and the prior wave's own §3.1 table says so.** In the served text the two
sentences read *"8 × **10vg**"* and — for LD — *"1.23 × **10vg**"*. **Neither exponent exists in the text.**
The quantities that make this a contradiction are figure-derived on **both** sides:

| Side | Predicate — from text | **Exponent — from where** |
|---|---|---|
| 8 × 10¹⁰ arm | *"rescue of lethality"* 🟢 text | **`gr2.jpg` panel label**, prior session. Prior wave rated it **🔴 LOW**; I rate it **🟡 MEDIUM** (§3.1) |
| LD arm | *"did not survive to P90"* 🟢 text | **`gr3.jpg` Fig 3A + S7I caption**, prior session. 🟢 HIGH |

⇒ **The contradiction is text-versus-text in its *predicates* and figure-versus-figure in its *quantities*.**
The prior wave rated the `8 × 10¹⁰` exponent **🔴 LOW in its own §3.1 table** and then, two sections later,
built on it a conflict it declared independent of figures. **Those two statements cannot both stand.**

🔴 **And the stake is total: if the deleted exponent is 11 rather than 10, `8 × 10¹¹` is 6.5× *higher* than
LD and the non-monotonicity vanishes completely.** I judge 10 the better reading — the parallel construction
with a 🟢 HIGH `4 × 10¹⁰` in the same sentence pair, plus the panel label — but **that is 🟡 MEDIUM, and a
🟡 MEDIUM exponent cannot carry a claim of biological non-monotonicity.**

### 6.4 Verdict on the non-monotonicity

| Question | Answer |
|---|---|
| Does the unit resolution **dissolve** it? | 🔴 **No.** Under the single convention the Methods support, LD is **1.54× higher** and the tension is intact |
| Does it **leave** it? | 🔴 **No — it sharpens it**, by positively excluding reading (a), the cheapest escape (§6.1) |
| Should biological non-monotonicity now be inferred? | 🔴 **NO — and more firmly than before.** Three cheaper explanations remain unexcluded: **(b)** a follow-up-horizon mismatch, now the leading candidate; **(c)** an erroneous sentence; **(e)** 🆕 **a 🟡 MEDIUM exponent on one side, which if wrong erases the tension outright.** **A unit convention was the cheapest explanation and it is now excluded; three cheaper-than-biology explanations took its place.** |

⚪ **Stated plainly so it cannot be misread:** this node **does not** assert that a lower dose rescues where
a higher one fails. It asserts that **the paper's prose says so, that units do not explain it, and that
three non-biological explanations remain open.**

---

## 7 · 🆕 Two nomenclature defects found in-act, recorded separately from the classification

**Neither creates incompatible unit conventions (§5), and both are traps for a downstream reader.**

**7.1 🔴 The token `LD` denotes two different doses in one paper, ~1,000 characters apart.**

> @10,499 (Fig 2 / S3 passage): *"increasing the vector dose in the absence of WPRE failed to recapitulate
> the expression levels achieved with **lower dose (LD) containing WPRE**"* — context fixes this **LD** as
> **4 × 10¹⁰ vg WITH WPRE**.

> @11,483 (Fig 3 passage): *"we evaluated two clinically applicable doses: **an LD (1.23 × 10\[¹¹\]vg)**"* —
> **1.23 × 10¹¹ vg WITHOUT WPRE**.

⇒ **A 3.1-fold difference and an opposite WPRE configuration behind one two-letter token.** Any downstream
reader who matches on `LD` across the paper will conflate them. ⚠️ **Surface caveat:** the repository's
locator file quotes this sentence from the 88k HTML surface **without** the `(LD)` parenthesis. Either the
surfaces differ again, or the repository quoted the S3F caption and I am reading the parallel running-text
sentence. **I cannot tell which from here, and I flag it rather than resolve it.**

**7.2 🔴 A dose is called a "titer".** *"all vectors were tested at the same **titer** (4E10)"* — a titre is a
**concentration**; `4E10` is used everywhere else in this paper as a **dose in vg**. ⇒ **The one place the
paper uses an exponent-safe notation is also the one place it names the wrong physical quantity.** This is
the same class of defect as the missing `/hemisphere`: **the number is stated, its denominator is not.**

---

## 8 · What I could not verify

| Item | Why | What it would take |
|---|---|---|
| **Whether `vg` means per hemisphere or total** | 🔴 **Unstated in the paper.** Bare on all 3 surfaces; no dose in Methods; `GC`/`per animal`/`total dose` → 0 occurrences | the Figure 3 legend at full resolution, the journal's supplementary methods, or the authors |
| **Any exponent by direct inspection of primary markup** | 🔴 4 routes attempted, all blocked; **measured** (§0.1) | one route to raw JATS XML or the publisher PDF |
| **`gr2.jpg`, `gr3.jpg`, `S_p09_200dpi.png`** — the artefacts carrying every 2026 exponent | 🔴 `files/` absent from this worktree; all fetch routes blocked | the shared evidence tree |
| **The `8 × 10` exponent** | 🟡 one prior-session panel-label surface + internal parallelism; **I could not open the panel** | a re-read of `gr2.jpg` |
| **The Fig 2 follow-up horizon** — which would settle explanation (b) | 🔴 **no duration statement in the served text**; the ~50 d figure is a prior-session panel read | a re-read of Fig 2B, or a stated horizon |
| **Whether §7.1's `(LD)` discrepancy is a surface difference or two different sentences** | 🔴 the 88k HTML surface is unreachable | that surface |
| **Which vector lot produced which arm** | 🔴 four vendors named, **none assigned** | a lot statement, or the authors |
| **Titration uncertainty** | 🔴 both papers titrate by qPCR/bGH **only**; **neither reports a CV, a replicate or an orthogonal method** (re-verified in-act) | an orthogonal titration |
| **`42128308` (the 2026 review)** at any depth | 🔴 **no PMCID**, re-verified in-act | a non-PMC route |

---

## 9 · 🔴 Findings that contradict or correct a repository assertion

**Ordered by how load-bearing they are. Each names the file and what it says.**

**O-1 — "the ambiguity is the size of the effect" is a category error, and it is the prior wave's
load-bearing sentence.** `tx007_dose_challenge_20260922.md` §1.5, §4.1 and `CC-20260922-TX007-DOSE-CHALLENGE-01.md`
§4b. The unit ambiguity is **common-mode** and **cancels exactly** from `HD/LD`; the ratio is **2.1382 under
every permitted reading** (§4.1). The defect is real but confined to the **absolute** axis, where it is
**exactly 2×**. ⇒ **the ~2.1× step is robust, and `TX-007`'s internal dose–response structure was never
threatened by the unit.** This is the single most consequential correction here, because the prior wave's
§4.1 verdict and its §4.2 reading (a) both rest on the conflation.

**O-2 — reading (a) is not merely unavailable, it is contradicted.** Prior wave §4.2 calls a per-figure
unit switch *"the single cheapest resolution … unavailable from the text"*. 🆕 **The text does bear on it,
and against it:** *"this reduction in expression **necessitates the use of higher vector doses**"* is an
explicit cross-figure magnitude comparison, and it requires one scale (§6.1). ⇒ **the non-monotonicity is
sharpened, not left open.**

**O-3 — "no figure is involved on either side" does not hold, and conflicts with the prior wave's own
table.** Prior wave §4.2 and §10 C-4. **Both exponents in that contradiction are figure-derived**; the
served text reads `10vg` on both sides (§6.3). The prior wave rated the `8 × 10¹⁰` exponent **🔴 LOW in its
§3.1** and then built on it a conflict declared **independent of figures**. **Those two cannot both stand**,
and the stake is total: at `8 × 10¹¹` the tension vanishes.

**O-4 — the 2021 dose exponent is 🟢 HIGH, not 🟡 MEDIUM; the repository already held the surface it said it
lacked.** Prior wave §3.1 rates `2 × 10¹⁰ GC/hemisphere` **🟡 MEDIUM — "one snippet route, no primary
rendering seen"**. 🆕 **`PMID34747138_locators.md` quotes it from a local JATS XML** (sha256 `7da156e8…988bb`,
`surface: body`) as *"Approximately 1 μl (**2 × 1010 GC/hemisphere**) virus was dispensed"* — a
primary-markup rendering with the exponent intact, **in the repository's own dossier, cited by the prior
wave for other purposes.** Same failure class the prior wave itself named (an artefact declared unavailable
while another actor held it).

**O-5 — the prior wave's third LD/HD exponent surface does not survive re-testing.** Prior wave §3.1 counts
*"(iii) WebSearch snippet … reporting 1.23 × 10¹¹ / 2.63 × 10¹¹"*. 🆕 **I ran that route in-act and the
exponent came back deleted** — *"a low dose (LD, 1.23 × 10 vg)"* (§3.3). The doses remain 🟢 HIGH on two
primary-artefact renderings, but **the margin is one surface, not two**, and **a search-engine gloss is not
an exponent surface.**

**O-6 — a structural fact the repository does not hold: `PMID 42422765` states no dose in its Methods at
all.** All seven `vg` tokens are in Results/Discussion; the Methods carry volume, rate, coordinates, needle,
titration method and four vendors, and **no dose value** (§3.2, measured by character offset). ⇒ **the
dose and its volume are never in the same sentence or section** — the precise mechanism by which the unit
was lost.

**Plus two smaller items, recorded so neither is re-found as new:**
- **O-7.** The token `LD` denotes 4 × 10¹⁰ (+WPRE) in one passage and 1.23 × 10¹¹ (−WPRE) in another (§7.1);
  and a dose is called a *"titer"* (§7.2).
- ⚪ **O-8 — a suspicion raised and then killed, recorded because killing it is the result.** I tested
  whether the paper might be **internally inconsistent** in its unit convention (the third classification),
  which would have been the most damaging finding available. **It is not.** One Methods, one protocol, one
  volume, one token form, and a bridge sentence requiring a shared scale. **The paper is consistently
  silent, not inconsistently specified** — and that distinction is what makes the ratio recoverable and the
  absolute dose not.

---

## 10 · Reading debt declared

`python3 framework/scripts/growth_anchors.py check` **before** this file:
`structural: claims=40 · papers=87 · corpus=361 · literature=398 | registry_only=13 | unread_premises=0` ·
`VERDICT: PASS`.

**Every PMID named in this file — `42422765`, `34747138`, `42128308`, `42397075`, `34268881` — was already a
named premise of `tx007_dose_challenge_20260922.md` and is already cleared by a persisted receipt, a
registry record or an existing queue entry. No new PMID is introduced as a premise, no PMID was stripped to
keep the ratchet at zero, and nothing in this file cites an `FT-` identifier** — so
`manifest_queue_id_crosscheck.py --prose` has no `FT-` number to resolve here. No new `FT-` entry is
required, because no new reading debt was opened. **No researcher email or contact detail appears
anywhere in this file.**

---

## 11 · Source attribution

**According to PubMed**, and retrieved from **PubMed / PubMed Central** in this act.

| PMID | Citation | DOI |
|---|---|---|
| 42422765 | Obeid M, Akkawi R, Repudi S, Singh PK, Abudiab B, Jebara T, Berent A, Brennan T, Weiss Y, Shekh-Ahmad T, Aqeilan RI. Neuron-specific WWOX gene therapy produces dose-dependent, durable rescue in a model of WWOX-related epileptic encephalopathy. *Molecular therapy. Advances* (`Mol Ther Adv`) 2026;34(3):201791. PMCID `PMC13343157`. **Full body read in-act (48,780 chars); no figures, no captions** | [10.1016/j.omta.2026.201791](https://doi.org/10.1016/j.omta.2026.201791) |
| 34747138 | Repudi S, Kustanovich I, Abu-Swai S, Stern S, Aqeilan RI. Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes. *EMBO Mol Med* 2021;13(12):e14599. PMCID `PMC8649866`. **Full body + legends read in-act** | [10.15252/emmm.202114599](https://doi.org/10.15252/emmm.202114599) |
| 42128308 | Obeid M, Wang J, Abudiab B, Akkawi R, Aqeilan RI. WWOX in brain development and disease. *Neurobiol Dis* 2026;225:107446. **Review, same laboratory. No PMCID — route closed, re-verified in-act. Not read.** | [10.1016/j.nbd.2026.107446](https://doi.org/10.1016/j.nbd.2026.107446) |
| 42397075 | Steinberg DJ, Zonca A, Abdellatif D, *et al.*, Aqeilan RI. Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids. *Brain* 2026. **No PMCID; named only as a repository cross-reference, not read in this act** | [10.1093/brain/awag239](https://doi.org/10.1093/brain/awag239) |
| 34268881 | Steinberg DJ, Repudi S, Saleem A, *et al.*, Aqeilan RI. Modeling genetic epileptic encephalopathies using brain organoids. *EMBO Mol Med* 2021;13(8):e13610. PMCID `PMC8350905`. **Named only as a repository cross-reference; not read in this act** | [10.15252/emmm.202013610](https://doi.org/10.15252/emmm.202013610) |

**Web route consulted at snippet depth only, never as a read, and reported in §3.3 as a *failed* exponent
surface:** [PubMed 42422765](https://pubmed.ncbi.nlm.nih.gov/42422765/) ·
[PMC13343157](https://pmc.ncbi.nlm.nih.gov/articles/PMC13343157/) ·
[PMC8649866](https://pmc.ncbi.nlm.nih.gov/articles/PMC8649866/) ·
[ScienceDirect S3117387X26001266](https://www.sciencedirect.com/science/article/pii/S3117387X26001266).

---

**End.** Read-only toward every canonical file, the registries, the receipt ledger and the state manifest;
nothing promoted, nothing committed. **No molecule, no dose recommendation, no route recommendation, no
safety claim, no druggability score.** Every dose above is a record of what an experiment administered to
mice. **Not medical advice.**
