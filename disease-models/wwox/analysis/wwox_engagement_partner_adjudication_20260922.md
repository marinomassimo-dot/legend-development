# The `POLE4` label gate, resolved — and the WWOX engagement-partner adjudication

**Actor:** Scientist E · **Date:** 2026-09-22 · **Node:** `MECHANISM_WWOX_SDR_FUNCTION_AND_MISSENSE_RESCUE`
**Task:** resolve the one unresolved gate in
[`function_per_molecule_assay_design_20260922.md`](function_per_molecule_assay_design_20260922.md)
(Scientist D), then adjudicate the partner choice on its merits.
**Status:** NON-CANONICAL analysis file. No registry, queue, ledger, receipt chain, state manifest or
`*_current.md` was read-modified-written. No `BATCH_COMMIT`. No git command was run: no commit, no
stage, no push. **Nothing here is medical advice.** No molecule, dose or route for any person
appears. The reference genotype is a WWOX-DEE genotype class; no individual-level record is
reintroduced.

---

## VERDICT UP FRONT

> ## 🎯 **The label is `P282A`. It is not a reconstruction any more — the panel legend itself was recovered.**
>
> Figure 5F's own legend, verbatim from a rendering that preserves superscript markup:
> *"F) Co‐IP analysis shows the interaction of WWOX and POLE4. HEK293T cells were co‐transfected with
> Flag‐tagged wild‐type (**WWOX^WT^**) or mutant (**WWOX^P282A^**) vector and HA‐tagged POLE4 vector."*
>
> And the Results sentence whose superscript the PMC extractor deleted, restored:
> *"However, the **WWOX^P282A^** mutant appeared to lose its interaction with POLE4 (Figure 5F). The
> interaction between POLE4 and the **WWOX^P252A^** mutant was also markedly reduced, likely due to
> the low abundance of the unstable **WWOX^P252A^** mutant (Figure S9, Supporting Information)."*
>
> 🟢 **Scientist D's reconstruction was correct. Falsifier #1 does NOT fire.** The primary numerator
> keeps its abundance-independent credential and **does not have to switch on label grounds.**
> `PREMISE: UNVERIFIED` → **`VERIFIED`** at the label level, on the panel label, the Results prose,
> the Discussion, the abstract and the docking summary — five places, two independent surfaces.
>
> 🔵 **A second load-bearing premise was carrying the same risk silently, and I resolved it too.**
> *"`P282A` is stable"* rested on the same superscript-deleted sentences. Restored:
> *"the protein expression of **WWOX^P252A^** mutant was much lower than the expression of wild-type
> WWOX and **WWOX^P282A^** mutant proteins"* and *"the **WWOX^P252A^** mutant exhibited significantly
> enhanced protein degradation, compared to its wild-type counterpart and the **WWOX^P282A^**
> mutant."* **Both poles of the `P252A`/`P282A` dissociation are now label-verified.**
>
> 🟠 **But the merits verdict is NOT "keep POLE4 and stop".** On criterion (a) — SDR-dependence —
> `POLE4` is the **weakest** mapped partner in the inventory, not the strongest: **the paper never
> names the domain** (`SDR`, `short-chain`, `dehydrogenase` = **zero occurrences**, verified
> case-sensitively), no fragment or deletion mapping exists, and no WW-domain control was run.
> `POLE4`'s binding site on WWOX is **unmapped**. `PREMISE: NOBODY_LOOKED`.
>
> ## 🟢 **RECOMMENDED: `POLE4` and `GSK3β` as CO-PRIMARY numerators on one plate — not primary-and-fallback. `BRCA1` (WW1) as the negative control. `HSC70` added as a third, inverse-sign channel. `tau` REMOVED from the design.**
>
> They are complements, not alternatives, and the reason is exact: **`POLE4` supplies the one
> credential `GSK3β` lacks (a demonstrated loss of engagement in a missense protein with no measured
> stability defect — criterion C6), and `GSK3β` supplies the one credential `POLE4` lacks
> (residue-level SDR-span mapping, five orthogonal assays, a ready-made loss-of-binding control, and
> the only non-oncological material of origin in the entire inventory).** Either alone leaves a
> criterion unmet. Scientist D's file already holds a slot for both — §3.3's *"secondary/confirmatory
> SDR numerator"* — and **my adjudication is that the slot should be promoted to co-primary, and that
> `tau` should be struck from it.**
>
> 🔴 **Three new blocking constraints the design did not carry, all found in the body:**
> **(1)** every WWOX–`POLE4` measurement in existence was made **after UV irradiation** — a ±UV arm
> is now mandatory and it collides with the abundance-raising arms; **(2)** the `P282A`
> co-IP panel (5F) contains **only WT and `P282A`** — `P252A`'s `POLE4` result lives in
> **Figure S9, Supporting Information**, which nobody here has seen; **(3)** the authors themselves
> write that *"the precise molecular mechanism underlying the loss-of-function of the WWOX P282A
> variant is still unknown"* — so the POLE4 attribution is **their suggestion, docking-supported**,
> not their conclusion.

---

## 0 · Read depth and provenance, declared before any finding

**Bibliographic source of the new literature content below: PubMed** (records retrieved by me in
this act) and **Scholar Gateway** (full-text passages retrieved by me in this act).

| Source | Depth reached by **me**, in this act |
|---|---|
| `PMID 41124647` / `PMC12767083` (Zhang 2025, *Adv Sci* 13(1):e07602, [DOI](https://doi.org/10.1002/advs.202507602)) | 🟢 **Body fetched and searched by me, twice, on two independent renderings.** PMC route: 68 491 characters measured, superscripts **deleted**. Scholar Gateway route: 12 + 8 passages, superscripts **preserved as `^…^` markup**, including four figure legends. This is the paper the gate is about |
| `PMID 22193544` (Wang 2012, GSK3β; `PAPER 056`) | 🔵 **Repository-held at `complete_fulltext_read` depth** (`FTR-20260726-22193544-01/02/03`), nine verbatim locators in `deepdive_manifests/PMID22193544.json`, **variant labels intact** (`L404A`, `L311A`, `388–407`, `Δ286`, `Δ389`). Read by me **as that actor's attestation**, not re-fetched |
| `PMID 27869163` (Schrock 2016, BRCA1/WW1, `Y293F`) | 🔵 **Repository-held at `partial_fulltext_read`** (`FTR-20260921-27869163-01`), with its audit `wwox_brca1_transferability_audit_20260921.md`. Another actor's attestation; labels intact |
| `PMID 27551439`, `25650666`, `26355344`, `32764489` (Chang/NCKU: TRAPPC6AΔ, tau, Zfra, p-WWOX) | 🔵 **Repository-held at `partial_fulltext_read`** (receipts `FTR-20260920-*`), with the 2026-09-21 adversarial re-read of `25650666`. Another actor's attestation |
| `PMID 29808465` (the only `Q230P` paper) | 🔴 **`abstract_only`** (`FTR-20260810-29808465-01`). Unchanged by me |
| `PMID 21476439` (the only WWOX enzymology paper) | 🔴 **NOT READ BY ANYONE HERE.** `PREMISE: UNREAD_PRIMARY` — owed a reading, not doubted. Unchanged by me |
| `advs.202507602` **Figures S9, S10, S11** (the `P252A` POLE4 co-IP; the CASTp pocket analysis; the docking) | 🔴 **NOT SEEN.** Supporting Information was not retrieved by any route available here. `PREMISE: UNREAD_PRIMARY` on the supplement |
| Every figure **image** | 🔴 **NOT INSPECTED.** Per `D-14`, nothing asserted only by a panel image is adjudicated. **What I resolved is the panel's *legend text*, which is prose, not the panel's *image*** — and that distinction is exactly what the gate needed, because the gate was about a *label*, not about a band |

🔴 **A prediction is never a measurement.** The paper's PyMOL/CASTp/docking results are
**predictions**, and I use them below **only** as evidence of *what the authors attributed to which
variant* — never as evidence that the attribution is true. `ΔΔG`, `pLDDT`, `SASA` likewise.

🔴 **No cross-variant generalisation.** `Q230P` ≠ `P252A` ≠ `P282A` ≠ `P47T` ≠ `P47R` ≠ `G372R` ≠
`L404A` ≠ `Y293F` ≠ `L239R` ≠ `A141T` ≠ `G372R`. Every row below carries its allele.

**Before declaring any defect I ran the required order** — `FIND ISSUE` → `SEARCH EXISTING CLAIMS`
(`CLAIM 016`, `030`, `035`) → `SEARCH EXISTING CANDIDATES` (`RC-013`) → `SEARCH DISCOVERY LEDGER`
(`DL-MECH-008`, `DL-MECH-019` + its 2026-07-26 upgrade, `DL-MECH-029`, `DL-BIO-004`, `DL-MOL-006`) →
and only then proposed. **Two of my four substantive conclusions turned out to be already held by
this repository** and are cited to it rather than claimed as new: that the `tau` arc is
`INDETERMINATO` (`DIS-010`, `D-14`) and that a `Q230P` loss of GSK3β binding would report global
fold collapse rather than a local interface lesion (`DL-MECH-019` upgrade). **That is the
rediscovery failure mode working as intended — caught by the search, not by luck.**

---

## 1 · Every route attempted for the label, and what each returned

Ordered as attempted. **Eight routes, four blocked, two negative, two decisive.**

| # | Route | Mechanism | Result |
|---|---|---|---|
| **R-1** | **The repository's own held artefact** — `files/fulltext/PMID41124647_PMC_MCPtext.txt`, named as `source_locator` in receipt `FTR-20260921-41124647-01` | Re-read the byte-identical artefact the earlier reading used | 🔴 **ABSENT FROM THIS CHECKOUT.** `files/` does not exist; `find -iname "*41124647*"` returns nothing. **The artefact behind the receipt is not in the working tree.** Not a defect in the receipt — the tree is a different checkout — but it means *the label could not be re-checked against the artefact the receipt fingerprints*, and the route had to be rebuilt from the network |
| **R-2** | **PubMed abstract** via `get_article_metadata` | A *different* extraction pipeline (efetch abstract XML) from the PMC body route | 🔴 **NEGATIVE, and informatively so.** The abstract on this surface reads *"but not with the **WWOXmutant**"*, *"both **WWOXand WWOXmutants**"*, *"The **WWOXmutant** undergo accelerated degradation"*. **The superscripts are deleted on the abstract surface too** — so the defect is not specific to the full-text route, and Scientist D's §0 assessment of the extractor is confirmed on a second surface. `"WWOXand WWOXmutants"` is itself the fingerprint of **two** deleted labels fused |
| **R-3** | **PMC full text** via `get_full_text_article(["PMC12767083"])` | The canonical open-access body | 🟡 **PARTIAL — and it is the route that produced the gate.** 68 491 characters. Every superscript variant label on a protein name is gone. **But it is not a total loss, and this is the finding that reopened the gate:** the *docking* sentences carry their labels in **roman** type and therefore survived — *"The **P282A** mutation in the WWOX protein reduced the binding energy for POLE4, compared to the wild-type WWOX"* and *"the **P252A** mutation enhances WWOX binding to HSC70, whereas the **P282A** mutation reduces its affinity for POLE4."* **The paper's own mechanistic assignment of POLE4 to `P282A` was legible all along, in a sentence nobody had queried.** ⚠️ It is a *docking* sentence — a prediction — so it establishes the authors' attribution, not the measurement |
| **R-4** | **Internal logic of the two surviving co-IP sentences** | Reconstruction from roman-type context | 🟡 **CONSISTENT, and I record it as reasoning, not as evidence.** *"the WWOX[?]mutant appeared to lose its interaction with POLE4. The interaction between POLE4 and the WWOX[?]mutant was **also** markedly reduced, likely due to the low abundance of the **unstable** WWOX[?]mutant."* *"also"* forces the second sentence onto a **different** mutant; *"unstable"* identifies it as the degraded one; the repository independently holds that the degraded one is `P252A` ⇒ the first is `P282A`. **Sound, but it is an inference chained onto another file's attestation. It would not have closed the gate on its own and I did not stop here** |
| **R-5** | **Europe PMC `fullTextXML`; NCBI `efetch` (db=pmc); PMC and pmc.ncbi HTML; Wiley DOI landing; a third-party index** — via `curl` **and** via `WebFetch` | JATS XML and rendered HTML both retain `<sup>` | 🔴 **BLOCKED, all of them.** `curl`: `CONNECT tunnel failed, response 403` for `www.ebi.ac.uk`, `eutils.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov`, `pmc.ncbi.nlm.nih.gov`. **Control run as required: `example.com` also 403** — so this is a closed allowlist, not a property of the paper. `WebFetch`: `EGRESS_BLOCKED` for `pmc.ncbi.nlm.nih.gov`, `www.ebi.ac.uk`, `europepmc.org`, `advanced.onlinelibrary.wiley.com`, `lacuna.tiptreesystems.com`. `TOOL_BLOCKED → PARK ROUTE → CONTINUE`; each host tried **once** |
| **R-6** | **Web search, two independent queries** | A rendered surface read by a summarising model | 🟡 **POSITIVE BUT WEAK EVIDENCE, and I refused to close on it.** Query 1 returned *"but not with the **WWOX^P282A^** mutant"*; query 2, differently worded, returned *"the **WWOX^P282A^** mutant appeared to lose its interaction with POLE4"* — the exact Results sentence, restored. Two queries agreeing, and the second reproducing the PMC wording word-for-word apart from the superscript, is real corroboration. 🔴 **But the answer text is generated by a model reading the page, not the page. For a question that is entirely about four characters, that is not a surface I will call verified.** Carried as corroboration only |
| **R-7** ⭐ | **Scholar Gateway `semanticSearch` — a DIFFERENT EXTRACTION OF THE SAME BODY** | Publisher-side full text, chunked, with **superscripts preserved as `^…^` markup** and figure legends retained | 🟢 🎯 **DECISIVE. This is the route.** 12 passages, 1 article, the same DOI. It returns the **Figure 5F legend**, the **Results** sentences, the **Discussion** and the **abstract**, all with labels intact — see §2. **The brief's instruction was "use an alternative rendering or route when a label is missing rather than reconstructing it." This is that route, and it existed the whole time** |
| **R-8** | **Second Scholar Gateway query, aimed at the *other* premise** (which mutant is degraded) | Same route, different question, to test the route rather than trust it | 🟢 **CONFIRMS AND EXTENDS.** 8 passages. Returns Figure 4B/C/D/E/F/G/H/I/J legends and the turnover Results with every label intact, resolving *"`P282A` is stable"* on the same footing. **A route that answers a second, independently-checkable question correctly is a route, not a coincidence** |

### 1.1 Routes deliberately NOT taken, and why

- **ClinVar / UniProt annotation of either variant's reported consequence.** The brief lists this as a
  candidate route. 🔴 **I judge it incapable of answering this question and did not spend on it**, and
  the reason is not access: `rest.uniprot.org` and `files.rcsb.org` are on the blocked list
  (recorded in the proxy's own failure log), **but even with access it would not help.** A ClinVar or
  UniProt record states a variant's *clinical or functional annotation*; **neither database records
  which panel of which figure of which paper a co-IP band came from.** `P282A` is `rs3764340`, a
  common SNP with cancer-association literature; `P252A` is novel to this paper. An annotation
  lookup would return two variant records and **no information about the `POLE4` panel** — i.e. it
  would produce a confident-looking non-answer. Parked as *incapable*, not as *blocked*.
- **`find-fulltext`'s tiered cascade.** Its tiers are PMC / Unpaywall / Europe PMC / OpenAlex /
  Semantic Scholar / preprint / Scholar / CORE / publisher — **every one of which resolves to a host
  the egress proxy refuses** (R-5 tested five of them directly, plus the control). Running the
  cascade would have produced nine refusals and no body. Parked.
- **A citing paper that restates the attribution.** The paper is eleven months old
  (published 2025-10-22). I did not pursue this route because R-7 closed the question at the source;
  had R-7 failed it would have been next. Noted as unspent.

### 1.2 🔴 Two extraction traps hit and cleared in this act — both were on the brief's list

1. **Case-sensitive false positive.** A naive case-insensitive search of the body for `ADH` returns
   **6 hits**. All six are **`cadherin`** (`E-cadherin`, in the EMT section). A case-sensitive
   word-boundary search returns **0**. Had I counted the naive hits I would have concluded the paper
   names the ADH/SDR domain six times; **it never names it at all.** Verified both ways and reported
   both numbers, because the naive number is exactly the kind that becomes a citation.
2. **Informative zeros, verified case-sensitively.** In the body: `SDR` **0**, `short-chain` **0**,
   `dehydrogenase` **0**, `oxidoreductase` **1**, `seizure` **0**, `neuron` **0**, `without UV` /
   `no UV` / `untreated` / `mock` **0 each**, `WOREE` **7**. These are roman-type words, so the
   zeros are informative. **Three of them are load-bearing below** (§3.1, §3.4, §5.2).

---

## 2 · THE LABEL VERDICT

> ## 🎯 **`P282A`. Not `P252A`. Not `NOT DETERMINABLE`.**
>
> **Confidence: as high as this repository's evidence standards permit for a textual fact —
> the panel's own legend, read on a rendering that preserves the markup the other rendering deleted,
> agreeing with four other statements in the same body and with the prose that survived on the
> defective rendering.**

### 2.1 The evidence, in the order that closes the question

**(i) 🔴 THE PANEL LABEL ITSELF — this is the item Scientist D flagged as "never verified".**
Figure 5F legend, verbatim (Scholar Gateway rendering of `10.1002/advs.202507602`, chunk 13):

> *"F) Co‐IP analysis shows the interaction of WWOX and POLE4. HEK293T cells were co‐transfected with
> Flag‐tagged wild‐type (**WWOX^WT^**) or mutant (**WWOX^P282A^**) vector and HA‐tagged POLE4 vector.
> After UV exposure, cell lysates were immunoprecipitated with anti‐FLAG antibody, followed by a
> western blot for POLE4 (HA‐tagged)."*

**(ii) The Results sentence pair, both labels restored** (chunk 14):

> *"However, the **WWOX^P282A^** mutant appeared to lose its interaction with POLE4 (Figure 5F). The
> interaction between POLE4 and the **WWOX^P252A^** mutant was also markedly reduced, likely due to
> the low abundance of the unstable **WWOX^P252A^** mutant (Figure S9, Supporting Information)."*

**(iii) The abstract** (chunk 0): *"POLE4, is identified to interact with WWOX, but not with the
**WWOX^P282A^** mutant."*

**(iv) The Discussion, twice** (chunk 21): *"we found a novel WWOX interaction partner, POLE4, but the
**WWOX^P282A^** mutant protein was not able to bind to POLE4"* · *"But the **WWOX^P282A^** mutant
protein fails to bind to POLE4, preventing the accurate repair of DNA breaks."*

**(v) The docking summary — and this one survived even the defective extraction, in roman type:**
*"the molecular docking results suggest that the **P252A** mutation enhances WWOX binding to HSC70,
whereas the **P282A** mutation reduces its affinity for POLE4."*

**Five statements, two independent renderings, one figure legend. They do not disagree.**

### 2.2 The second premise, resolved in the same act — `P282A`'s stability

Scientist D's design rests on `P282A` being **stable and dead**. That claim came from sentences with
the **same** deleted superscripts, so it carried the **same** unverified risk — and nobody had
flagged it. Restored (chunks 8, 10, 9):

- *"western blot and IHC analyses showed that the protein expression of **WWOX^P252A^** mutant was
  much lower than the expression of wild‐type WWOX and **WWOX^P282A^** mutant proteins."*
- *"the **WWOX^P252A^** mutant exhibited significantly enhanced protein degradation, compared to its
  wild‐type counterpart and the **WWOX^P282A^** mutant (Figure 4B)."*
- *"MG132 treatment did not induce the accumulation of **WWOX^WT^**, **WWOX^P252A^**, and
  **WWOX^P282A^** proteins"* · *"chloroquine (CQ) and NH₄Cl treatment, restored **WWOX^P252A^**
  protein level"* · *"co-IP revealed an interaction between HSC70 and **WWOX^P252A^** mutant protein,
  **but not wild-type WWOX protein and WWOX^P282A^ mutant protein**."*

🟢 **`P252A` = low abundance, rapidly degraded, K63-polyubiquitinated, HSC70-positive,
lysosome-dependent, CQ/NH₄Cl-rescuable, proteasome-independent, 3-MA-independent.
`P282A` = none of that, on every one of those panels.** Both poles label-verified.

### 2.3 🔴 What the verdict does NOT establish — four bounds that ride with it

1. **A label is not a band.** I verified the **legend text** of Figure 5F. I did **not** see the
   image. Per `D-14` I do not adjudicate the blot. What is now certain is *which variant the panel is
   of*; what the panel shows remains the authors' reported result, at `partial_fulltext_read` depth.
2. ⚠️ **The Results wording remains the bound, exactly as Scientist D said.** Abstract: *"but not
   with"*; Results: *"**appeared to** lose"*. The label verdict does not upgrade the strength of the
   claim — it only fixes whose claim it is.
3. 🔴 **"No stability defect" is a NEGATIVE with an unmeasured floor.** `P282A`'s stability is
   *"not significantly different from wild type"* by CHX-chase western densitometry, ImageJ,
   GAPDH-normalised, **n = 3, Student's t-test, no half-life value stated anywhere**
   (`half-life` appears only in the Methods sentence declaring the intent). `PREMISE: DETECTION_FLOOR`
   applies to the negative as much as to `Q230P`'s *"protein not detected"*. **"Stable" here means
   "no defect large enough for n = 3 densitometry to see", not "wild-type turnover".**
4. 🔴 **The authors do not claim the mechanism.** Discussion, verbatim: *"Nevertheless, the precise
   molecular mechanism underlying the loss-of-function of the **WWOX** P282A variant is **still
   unknown**."* The `POLE4` loss is offered as the novel observation and supported by **docking**;
   **no NER assay is performed**, and *"the functional relevance of WWOX‐POLE4 interaction in
   nucleotide excision repair remains to be elucidated."* ⇒ `D-04` stands at full strength: this is
   **engagement**, not demonstrated function.

---

## 3 · Partner inventory, scored on (a) SDR-dependence, (b) titration compatibility, (c) body-read status

**Scoring.** `✅` met · `🟡` partly met · `🔴` failed · `—` not assessable.
**Material of origin is carried in every row, as required** — and the inventory's single most
important structural fact is that **every partner except one comes from oncology.**

| Partner | Size | **(a) SDR-dependence** | **(b) Titration / saturation compatibility** | **(c) Body read + labels intact** | **Material of origin** | Verdict |
|---|---|---|---|---|---|---|
| 🥇 **`POLE4`** (POLE4, DNA pol ε accessory subunit) | **117 aa** | 🟡 **WEAKEST MAPPING IN THE TABLE, and this is the correction to §3.3.** One substitution, `P282A`, inside the SDR span **by external coordinates only — the paper names no domain (`SDR` 0, `dehydrogenase` 0, verified case-sensitively)**. No fragment mapping, no deletion series, no WW-domain control, no triad control. The binding site on WWOX is **unmapped**: `PREMISE: NOBODY_LOOKED`. Docking "reduced binding energy for POLE4" is a **prediction**. Fails the `PMID 28540421` standard outright | ✅ **BEST IN TABLE.** 117 aa → a HaloTag/NanoLuc acceptor fusion is trivial. 🔴 **But one hard new constraint: every WWOX–`POLE4` measurement in existence was made AFTER UV** (`without UV`/`no UV`/`untreated`/`mock` = **0** in the body). Whether the engagement exists in unstressed cells is **untested** ⇒ a ±UV arm is mandatory, and UV itself perturbs abundance and autophagic flux, colliding with the CQ and 30 °C arms | ✅ **`partial_fulltext_read`** (`FTR-20260921-41124647-01`) **+ labels now VERIFIED by me on a second rendering, including the panel legend.** 🔴 `P252A`'s POLE4 co-IP is in **Figure S9, Supporting Information — not seen by anyone here** | 🔴 **Oncological.** CAL-62 anaplastic thyroid carcinoma, BCPAP papillary thyroid carcinoma, HEK293T; nude-mouse xenografts. `neuron` 0, `seizure` 0 | 🥇 **CO-PRIMARY.** Holds the **only** C6 credential in the literature; holds the **weakest** (a) |
| 🥇 **`GSK3β`** (GSK3B) | **420 aa** | ✅ **STRONGEST MAPPING IN THE TABLE, by a wide margin.** Residue-resolved: **aa 388–407** required; **`L404A` completely abolishes binding** in GST pull-down *and* cellular co-IP; **`L311A` does not** (in-plane negative); truncations **Δ286** and **Δ389** do not bind; the motif is the conserved `FXXXLI/VXRLE` GSK3β-docking motif homologous to `GSKIP₁₁₅₋₁₃₉`, `Axin₃₈₁₋₄₀₅`, `FRAT₂₀₅₋₂₂₉`. **Five orthogonal assays, one point mutation.** 🟢 **And — unlike `POLE4`'s paper,
which never names the domain — the SDR attribution here is the AUTHORS' OWN, in their own abstract:**
*"We demonstrated biochemically that WWOX can bind directly to GSK3β through its **short-chain
alcohol dehydrogenase/reductase domain**"* (retrieved from PubMed by me in this act). **So for
`GSK3β`, "SDR-dependent" is the source's claim; for `POLE4` it is the reader's arithmetic. That
asymmetry is the core of criterion (a) in this table.** ⚠️ **But one premise is unverified and it is
the one that matters here:** 388–407 sits at the extreme C-terminal end of the span, and **whether presentation of that motif requires the SDR CORE fold has never been measured.** A linear docking motif near a terminus may survive core misfolding. 🔴 **And no WWOX-DEE allele has ever been tested against it** (`CLAIM 035`, explicit) | ✅ **GOOD.** 420 aa → tractable acceptor. Published formats: GST pull-down, cellular co-IP, **and co-IP between ENDOGENOUS proteins in mouse brain extract**. 🟡 No luminescent-proximity format has ever been built for this pair | ✅ **BEST IN TABLE. `complete_fulltext_read`** (`FTR-20260726-22193544-01/02/03`), nine verbatim locators held in `deepdive_manifests/PMID22193544.json`, **every variant label intact** (`L404A`, `L311A`, `Δ286`, `Δ389`, `388–407`, `Y293F` n/a) | 🟢 **THE ONLY NON-ONCOLOGICAL ROW.** SH-SY5Y neuroblastoma under RA differentiation, recombinant protein, **and endogenous co-IP from mouse brain**. The closest material to the disease in the whole inventory | 🥇 **CO-PRIMARY — promote from Scientist D's "secondary/confirmatory".** Supplies (a) and (c) at a level `POLE4` cannot reach |
| 🥉 **`HSC70`** (HSPA8) | 646 aa | 🟡 **INVERSE SIGN — and that is its value, not its flaw.** `P252A` **gains** HSC70 binding; WT and `P282A` do **not**. So it reports *exposure of a degron-adjacent surface*, i.e. **misfolding**, not function. The `KFERQ`-like motif (`LRSVQ`, aa 187–191) is **identified by sequence inspection and NEVER MUTATED**; `LAMP2A` is neither knocked down nor overexpressed nor mentioned. So the *route* is lysosome-dependent/proteasome-independent; **calling it CMA is the authors' own "we speculated"** | ✅ **COMPATIBLE**, same co-IP architecture, and 🟢 **it is the one channel that already has BOTH POLES ON ONE FIGURE** (4I: WT-negative, `P252A`-positive, `P282A`-negative) | ✅ Same body, same receipt, **labels now verified by me** | 🔴 **Oncological** (CAL-62, HEK293T) | 🥉 **ADD AS A THIRD, INVERSE-SIGN CHANNEL — NOT a numerator.** §4.3 |
| **`TRAPPC6AΔ`** (TPC6AΔ) | ~half of TRAPPC6A | 🟡 **THE ONLY MAPPED REGION THAT ACTUALLY CONTAINS RESIDUE 230** — binds the C-terminal tail D3 / SDR span **aa 120–414**, **not** the WW domains (aa 1–95), mapped by FRET (`DL-MECH-019`). 🔴 But that is **fragment-level, and the fragment is "everything that is not WW"** — a WW-exclusion, not a domain-dependence demonstration. No residue resolution, no missense allele ever tested | 🟡 🟢 **Uniquely, a proximity format ALREADY EXISTS for this pair — the mapping was done by FRET.** That is a real (b) advantage nothing else in the table has. 🔴 Offset by the aggregation-prone nature of the ligand: TPC6AΔ is an **aggregating** species, which is a poor acceptor for a saturation curve | 🟡 `partial_fulltext_read` (`FTR-20260920-27551439-01`, `-26355344-01`), labels intact — **but single-laboratory (Chang/NCKU) and, on this repository's own record, "biologia di TPC6AΔ quasi esclusiva di questo gruppo, non replicata indipendentemente"**, with `DL-BIO-004`'s belief downgraded to **BASSO** on 2026-09-21 after an adversarial re-read found the human arm confounded (controls ~21 y younger, no blinding) | 🟡 **Mixed — neural.** AD post-mortem hippocampus/cortex, `Wwox`-KO mouse brain, plus cell lines. Neural material, but the human arm is confounded | 🟡 **HOLD as a ranked-third SDR candidate.** Its FRET precedent is genuinely valuable; its single-lab, non-replicated, belief-`BASSO` status disqualifies it as a numerator today |
| **`tau`** (MAPT) | 441 aa | 🔴 **FAILS.** Status in this repository is **`INDETERMINATO`** (`DL-MECH-019` upgrade 2026-07-26). Chang/Sze assert SDR-mediated tau binding from **yeast two-hybrid**; **Wang 2012 states in its text that WWOX does not bind Tau — and its Supplementary Figure contains NO Tau blot** (panels labelled WWOX and GSK3β), so **the negative is unevaluable** (`DIS-010`, `D-14`). 🔴 **Neither side is solid and they contradict each other** | 🟡 Tractable size | 🔴 **The affirmative side rests on a two-hybrid result in a single-lab body; the negative side rests on a figure that does not exist.** Criterion (c) unmet in both directions | Mixed (SH-SY5Y; AD brain) | 🔴 **REJECT AS A NUMERATOR — and STRIKE IT FROM THE DESIGN.** This is a direct correction to Scientist D's proposed fallback *"tau / GSK3β"*: **the fallback should have been GSK3β alone.** ⚠️ **tau keeps a different, legitimate role: as the DOWNSTREAM EFFECTOR readout** (pTau S396/S404) of the GSK3β arc, where `PMID 22193544` places it with epistasis — not as a binding partner |
| **`BRCA1`** | **1863 aa** | 🔴 **WW1-DEPENDENT — and that is exactly why it is here.** Residue-resolved: *"the WW domain fragment with mutated WW1 (**W44F/P47A**) … did not bind HA-Brca1 (lane 4)"*; *"a **GST-fused SDR fragment did not bind HA-Brca1 (lane 6)** and does not contain either WW domain"*; and the functional dissociation *"the SDR mutant Wwox-expressing cells are sensitive to radiation because they retain a WW1 domain"* vs *"without a functional WW1 domain, Wwox does not sensitize cells to radiation"* — i.e. **`Y293F` (SDR catalytic) RETAINS it, `W44F/P47A` (WW1) ABOLISHES it** | 🔴 **WORST IN TABLE.** 1863 aa is a poor BRET acceptor. 🟡 Workarounds: tag a BRCA1 fragment, or keep this control in the published co-IP format on the same lysates. **No BRET-format WW1 control has ever been built for WWOX** | ✅ **`partial_fulltext_read`** (`FTR-20260921-27869163-01`) with its dedicated audit; **labels intact** (`W44F/P47A`, `Y293F`) | 🔴 **Oncological.** MDA-MB-231 breast adenocarcinoma with dox-inducible WWOX, MCF-7, primary MEFs | 🥇 **THE NEGATIVE CONTROL. §4.2** |
| **`DVL2`** | 736 aa | 🔴 **WW-scaffold-dependent** (`DL-MECH-008`: *"la funzione anti-Wnt di WWOX è WW-scaffold (sequestro DVL2), non enzimatica"*), multi-source on direction | 🟡 Tractable | 🟡 Direction multi-source `DATO`; **residue-level domain mapping not held here at locator depth** | 🔴 **Oncological** (Bouteille/Li/Celebi, cancer context; `DL-MECH-008` flags the neuronal transfer as unconfirmed) | 🟡 **SECOND-CHOICE NEGATIVE CONTROL.** Better size than BRCA1, weaker mapping. Use if the BRCA1 fusion fails its pilot |
| **`ERBB4` / `p73` (PPxY ligands)** | large | 🔴 WW1/PPxY class ⇒ negative-control class by construction | 🟡 | 🔴 **Not held at locator depth in this repository** — thin mentions only, no read receipt | Oncological | 🔴 **DO NOT USE** without a reading. Named by Scientist D as an alternative WW1 control; **criterion (c) is unmet and I will not substitute it for BRCA1 on that basis** |
| **`Zfra`** | 31 aa peptide | 🔴 Not a domain-mapped partner; **accelerates WWOX degradation** — i.e. it perturbs the denominator | 🔴 A ligand that changes WWOX abundance is disqualified from an abundance-denominator assay by construction | 🟡 `partial_fulltext_read`; belief **basso-medio**; `DL-MOL-006` records incoherent reporting and peptide not detected in brain | Mixed (3×Tg-AD mouse; cancer) | 🔴 **REJECT.** Wrong instrument for this question |
| **`p53` / p-WWOX·p-p53 hetero-dimers** | — | 🔴 Not SDR-mapped. 🔴 **And this is the row that must not be misread:** `PMID 39894307` is the repository's **one** dimerisation record and it is **p-WWOX/p-p53 HETERO-dimers.** 🔴 **`WWOX homodimerises via the SDR` remains `PREMISE: UNVERIFIED`** — asserted uncited, no published source found by a query census. **Nothing below is built on it** | — | — | Oncological | 🔴 **EXCLUDED, and named here only to keep it excluded** |
| **A WWOX catalytic/substrate readout** | — | 🔴 No substrate; `oxidoreductase` appears **once** in the whole `41124647` body and `dehydrogenase` **zero** times | 🔴 No denominator | 🔴 `PMID 21476439` `PREMISE: UNREAD_PRIMARY` | — | 🔴 **CLOSED**, as Scientist D closed it. I add nothing and subtract nothing |

### 3.1 🔴 The finding that reorders the table: `POLE4` and `GSK3β` are strong on OPPOSITE criteria

|  | `POLE4` | `GSK3β` |
|---|---|---|
| **(a) SDR-span dependence** | 🟡 one substitution, span membership by **external arithmetic**; the source **never names the domain**; site unmapped | ✅ **residue-resolved, 388–407/`L404`, five orthogonal assays, two negatives — and the SDR attribution is the AUTHORS' own** |
| **C6 — abundance-independent failure demonstrated** | ✅ **`P282A`: engagement lost, no measured stability defect. The ONLY instance in the WWOX literature** | 🔴 **NONE.** `L404A`'s abundance was never reported; it is a designed interface substitution, not a disease allele |
| **(c) read depth + label integrity** | ✅ partial read, labels **now verified** | ✅ **complete read**, labels intact, nine locators |
| **Material of origin** | 🔴 thyroid carcinoma | 🟢 **neuroblastoma + endogenous mouse brain** |
| **Acceptor tractability** | ✅ **117 aa** | ✅ 420 aa |
| **Stress dependence of the measurement** | 🔴 **UV-only; no unstressed measurement exists** | 🟢 **measured in unstressed differentiating cells and in resting brain** |
| **Any WWOX-DEE allele ever tested** | 🔴 no | 🔴 no |

> 🔵 **Read across the row, the conclusion is forced and it is not the one either census reached:
> neither partner satisfies (a), (b) and (c) alone, and the two together do.** Running `POLE4`
> alone — Scientist D's §3.3 — leaves criterion (a) resting on one substitution in a paper that never
> names the domain. Running `GSK3β` alone leaves C6 — the design's own go/no-go gate — with no
> demonstrated instance at all. **The correct move is not to choose; it is to run both as
> co-primaries on one plate, which the design's own architecture already permits at no extra
> instrument and no extra read.**

---

## 4 · The recommendation

### 4.1 🥇 Numerator: `POLE4` **and** `GSK3β`, co-primary, same plate, same construct architecture

**`POLE4` earns its place for exactly one reason, and it is a reason nothing else has:** it is the
only WWOX readout in the literature reported to fail in a missense protein with **no measured
stability defect** — and after §2 that statement is **label-verified**, including on the panel
legend. That is criterion **C6**, the design's go/no-go gate, and without `POLE4` the plate has no
positive control for the dissociation it exists to detect.

**`GSK3β` earns co-primacy for three reasons `POLE4` cannot supply:**

1. ✅ **It is the only WWOX interaction mapped to residue level in a fully-read body** — 388–407,
   `L404A` abolishes, `L311A` does not, Δ286 and Δ389 do not bind. Criterion (a), met properly.
2. 🟢 **It brings a control set that needs no new reagents and no new science:**
   **`L404A`** = engineered loss-of-binding positive; **`L311A`** = in-plane negative;
   **`G372R`** = a **natural WWOX-DEE allele with a MILD phenotype** sitting **16 residues upstream**
   of the motif, which therefore serves simultaneously as a **disease-allele comparator** and a
   **proximity control** (`DL-MECH-019` upgrade; `CLAIM 030`); **`Q230P`** = the question.
3. 🟢 **It is the only non-oncological material of origin in the inventory**, and the only engagement
   measured between **endogenous proteins in brain**. Every other row is cancer.

⚠️ **And one constraint on `GSK3β` that must travel with it, because it cuts against my own
recommendation.** `Q230` is **174 residues** from `L404`. `DL-MECH-019`'s upgrade already states the
consequence and I adopt it unchanged: a loss of `GSK3β` binding in `Q230P` would report **global
collapse of the SDR fold**, not a local interface lesion. 🔴 **The converse is the risk nobody has
stated: 388–407 is a linear docking motif at the extreme C-terminal end of the span, and whether its
presentation requires the SDR core fold has NEVER been measured. A partially-unfolded WWOX could
still present it.** ⇒ **a NORMAL `GSK3β` curve for `Q230P` would be weak evidence of an intact fold**,
and must not be read as one. `PREMISE: UNVERIFIED` on motif-presentation-requires-core-fold.

🔴 **Neither partner meets the `PMID 28540421` standard, and applying that standard as instructed is
the honest bottom line of this section.** To call a cellular readout SDR-dependent, ENV9 required an
**active-site mutant AND a cofactor-site mutant** each to abolish it, *in vitro* and *in vivo*. For
WWOX the nearest equivalent — `S281A`/`Y293F`/`K297A` → perinuclear localisation — is **"Aldaz
laboratory unpublished observations", no data shown, readout = localisation**, standing against a
**published** WW1-routed alternative. **So for both `POLE4` and `GSK3β`, "SDR-dependent" today means
"an SDR-span substitution breaks it", which is a weaker claim, and the file says so rather than
rounding up.**

### 4.2 🥇 Negative control: `BRCA1` (WW1-dependent)

**`BRCA1` is the correct negative control and it is not close.** It is the only WWOX interaction for
which the WW1 requirement is (i) established by a **point mutant** (`W44F/P47A` abolishes binding,
lane 4), (ii) accompanied on the **same figure** by the matched exclusion (*"a GST-fused SDR fragment
did not bind HA-Brca1 (**lane 6**)"*), and (iii) cross-checked by a **functional** dissociation in the
same paper in which an **SDR catalytic substitution `Y293F` RETAINS** the WWOX-dependent output while
**WW1 `W44F/P47A` ABOLISHES** it. **That is precisely the shape criterion C4 demands: an output an
SDR lesion must leave normal, with published evidence that an SDR substitution does leave it
normal.** Body read, labels intact.

🔴 **One engineering problem, stated plainly: 1863 aa is a poor BRET acceptor, and no WW1 control in
BRET format has ever been built for WWOX.** Two honest options, and I will not pretend either is
free: tag a **BRCA1 fragment** containing the mapped interaction region, or keep the WW1 control in
its **published co-IP format on the same lysates** and accept that the domain control is then
semi-quantitative while the numerators are fitted. ⚠️ **The second is the safer first pass**, because
a fragment that fails to bind is indistinguishable from a control that works.

**Second-choice negative control: `DVL2`** (736 aa, WW-scaffold, `DL-MECH-008`, multi-source
direction) — better size, weaker mapping. 🔴 **`ERBB4`/`p73` are NOT available as substitutes**:
Scientist D names them, but this repository holds **no read body** for either, so criterion (c) is
unmet and swapping them in would trade a verified control for an unread one.

### 4.3 🥉 The addition I am contributing to the design: `HSC70` as a third, inverse-sign channel

🔵 **`HSC70` is the only reagent in this inventory whose figure already contains BOTH poles of the
`P252A`/`P282A` dissociation, measured side by side** — Figure 4I: *"an interaction between HSC70 and
`WWOX^P252A^` mutant protein, **but not wild-type WWOX protein and `WWOX^P282A^` mutant protein**."*

It is **not a numerator** — it reports misfolding-surface exposure and degradation targeting, in the
**opposite direction** to function. But added as a third channel on the same plate it does something
none of the design's existing controls do: it **discriminates, on the plate, between the two
mechanisms that a flat engagement curve cannot tell apart.**

| Reading on the plate | `HSC70` channel | Interpretation |
|---|---|---|
| `Q230P` engagement flat, `HSC70` channel **POSITIVE** | 🔴 | Protein present but presenting a degron surface ⇒ **misfolded-and-being-cleared**, and the denominator is counting protein en route to the lysosome |
| `Q230P` engagement flat, `HSC70` channel **NEGATIVE** | 🟢 | **The `P282A` outcome at this allele: stable, not clearance-targeted, and inert** — the one result that falsifies the abundance-raising axis on its own merits |
| `Q230P` engagement normal, `HSC70` **NEGATIVE** | 🟢 | Abundance-only lesion, the only result that licenses the boost axis |

🔴 **Bounds on it, all already on the repository's books:** the `KFERQ`-like motif (`LRSVQ` 187–191)
is **identified by sequence inspection and never mutated**; `LAMP2A` is neither manipulated nor
mentioned; `bafilomycin` and `LAMP2` occur **zero** times. ⇒ **record the route as
lysosome-dependent, proteasome-independent, macroautophagy-independent with an HSC70 co-IP and a
PREDICTED motif — NOT as chaperone-mediated autophagy.** The authors' own word is *"we speculated"*.

### 4.4 What would displace each — falsifiers, stated as observations

| # | Observation | Consequence |
|---|---|---|
| **D-1** ⭐ | **Figure S9 (Supporting Information) is obtained and shows the `P252A` POLE4 co-IP at a matched WWOX input** | If `P252A` loses `POLE4` binding *at matched abundance*, the confound the authors invoke dissolves and `POLE4` gains a **second** abundance-independent instance ⇒ `POLE4` becomes sole primary. If `P252A` retains it at matched input, the loss is `P282A`-specific ⇒ `POLE4` strengthens as a *residue* reporter. **Either way this is the single highest-value unopened item, and it is a supplement, not a programme** |
| **D-2** ⭐ | **A ±UV comparison shows WWOX–`POLE4` engagement is UV-INDUCED, not constitutive** | 🔴 `POLE4` is **demoted out of co-primacy**: a titration curve would then be measuring a stress-dependent assembly while the plate simultaneously runs CQ and 30 °C abundance arms that perturb the same stress pathways. `GSK3β` becomes sole primary |
| **D-3** | **A fragment or deletion series shows `POLE4` binds WWOX OUTSIDE the SDR span** (e.g. a WW-domain or C-tail site) | 🔴 **`POLE4` is disqualified as an SDR numerator entirely** and becomes a *second* negative control. `P282A`'s effect would then be allosteric or fold-mediated — still interesting, no longer domain-resolving |
| **D-4** | **`L404A`'s protein abundance is measured and found REDUCED** | 🔴 `GSK3β`'s loss-of-binding positive control is itself abundance-confounded ⇒ the control set loses its anchor and must be rebuilt |
| **D-5** | **A core SDR lesion is shown to RETAIN `GSK3β` binding** (e.g. `Q230P`, or a designed core substitution) | ⚠️ Confirms my stated risk: 388–407 presentation does not require the core fold ⇒ `GSK3β` is a poor reporter of a `Q230P`-class lesion and drops to a specificity control |
| **D-6** | **The `tau`-binding question is settled by a body with a Tau blot** (`FT-024`, `PMID 15126504`, Sze 2004 — **no PMCID, unobtainable from this checkout by any route**) | `tau` re-enters the inventory as a candidate rather than a rejection. **Until then it stays struck** |
| **D-7** | **An independent laboratory replicates TRAPPC6AΔ–WWOX SDR binding** | `TRAPPC6AΔ` rises to co-primary on the strength of its existing FRET format and its mapped region actually containing residue 230 |
| **D-8** | **A published experiment meets the `PMID 28540421` standard for any WWOX cellular readout** (active-site AND cofactor-site mutants both abolishing) | 🔴 **That readout outranks every engagement partner in this table**, because it would be a demonstrated **function** rather than a proxy. Scientist D's falsifier #6, and I endorse it unchanged |
| **D-9** | **The BRCA1 fusion fails its tag pilot** (no wild-type binding, or mislocalisation) | Switch the negative control to `DVL2`; if that also fails, keep the WW1 control in co-IP format and **declare the domain control semi-quantitative in the report** |

---

## 5 · Does the sibling's assay recommendation survive?

> ## 🟢 **IT SURVIVES — with one substitution INSIDE the partner slot, three new blocking constraints, and one addition. The instrument, the architecture and the logic are untouched.**

### 5.1 What survives without amendment

✅ The **donor-saturation NanoBRET architecture** with the NanoLuc donor channel as the abundance
denominator. ✅ The **fitted `BRET_max` / `BRET_50`** comparison instead of single wells — the
argument that a raw BRET ratio is *not* automatically expression-independent is correct and is the
reason the design works. ✅ **BRET over split-complementation**, and the stated reason (intrinsic
tag affinity in NanoBiT can rescue a weakened interaction and stabilise the tagged protein). ✅ The
**WWOX-depleted host**. ✅ **`P282A` as the go/no-go positive control** — and after §2 this is
**stronger** than when it was written, because both its label and its stability pole are now verified.
✅ The **paired WW1 domain control**. ✅ The **30 °C and chloroquine** abundance-raising arms.
✅ The **soluble/insoluble split** as prerequisite, and its placement as C8's enabler. ✅ The
**two-terminus tag pilot** as mandatory, on the strength of `T-1` and `T-5`. ✅ The **closure of the
enzymology route**, and the preservation of `E1`. ✅ The **`PNPLA3` `T-11` caution** — a normal curve
proves only that *this* engagement is intact. ✅ **No new research programme; no MAVE; no activity
sensor.** ✅ The `HUMAN_REQUIRED` parking of all four external actions.

### 5.2 🔴 What must change — five amendments

| # | Amendment | Basis |
|---|---|---|
| **A-1** | 🟢 **Falsifier #1 is RESOLVED and should be struck as an open gate.** The label is `P282A`. Do **not** demote the design a confidence step; do **not** switch the primary partner on label grounds | §2 — panel legend, Results, Discussion, abstract, docking, on two renderings |
| **A-2** | 🥇 **Promote `GSK3β` from "secondary/confirmatory" to CO-PRIMARY.** Not because `POLE4` failed, but because `POLE4`'s criterion-(a) evidence is one substitution in a paper that **never names the domain**, and `GSK3β` is residue-mapped at five-assay depth in a fully-read body with a free control set and the only non-oncological material of origin | §3, §3.1, §4.1 |
| **A-3** | 🔴 **STRIKE `tau` from the fallback.** Scientist D's §3.3 and falsifier #1 both read *"tau or GSK3β"*. `tau`'s SDR arc is **`INDETERMINATO`**: yeast two-hybrid on one side, and on the other a text denial whose **Supplementary Figure contains no Tau blot** (`DIS-010`, `D-14`). The fallback is **`GSK3β` alone**. ⚠️ `tau` retains a legitimate but different role — the **downstream pTau S396/S404 effector readout** of the GSK3β arc, where the epistasis places it | §3, `DL-MECH-019` upgrade |
| **A-4** | 🔴 **ADD a ±UV arm, and declare the collision.** **Every** WWOX–`POLE4` measurement in existence was made after UV; `without UV` / `no UV` / `untreated` / `mock` = **0** in the body (roman-type, informative). Whether the engagement exists in unstressed cells is `PREMISE: NOBODY_LOOKED`. ⚠️ **And UV perturbs abundance and autophagic-lysosomal flux — the very axes the CQ and 30 °C arms manipulate. This is a real design conflict, not a checkbox**, and it is a reason `POLE4` should not carry the plate alone | §1.2, §3 |
| **A-5** | 🥉 **ADD the `HSC70` channel** as a third, inverse-sign reporter — the only reagent whose own figure carries both poles of the `P252A`/`P282A` dissociation side by side (4I). It converts an otherwise-ambiguous flat curve into a two-way discrimination | §4.3 |

### 5.3 The revised partner line, in one sentence

> **Primary numerators: `POLE4` (117 aa; the only demonstrated abundance-independent engagement
> failure in the WWOX literature, label-verified, but domain-unmapped and UV-only) and `GSK3β`
> (420 aa; residue-mapped to 388–407/`L404` across five orthogonal assays in a fully-read body, with
> `L404A`/`L311A`/`G372R` as a free control set and the only brain-derived material in the
> inventory), run co-primary on one plate. Negative control: `BRCA1` (WW1, `W44F/P47A`-resolved, with
> the matched SDR-fragment exclusion at lane 6 and the `Y293F` functional dissociation), with `DVL2`
> as the size-tractable second choice. Third channel, inverse sign: `HSC70`. `tau` struck; `Zfra`,
> `p53` and any catalytic readout excluded.**

---

## 6 · What I could not establish

1. 🔴 **What the Figure 5F blot SHOWS.** I verified the panel's **legend text** — which is what the
   gate asked — and did **not** inspect the image. Per `D-14` the band is not adjudicated. The
   `P282A` → loss-of-`POLE4` result remains the authors' reported result at
   `partial_fulltext_read` depth, bounded by their own *"appeared to lose"*.
2. 🔴 **Figure S9, Supporting Information — the `P252A` `POLE4` co-IP.** Not retrieved by any route
   here. It is `D-1`, **the highest-value unopened item in this node**, and it is a supplement, not a
   programme. Also unseen: **S10** (CASTp pocket analysis) and **S11** (the docking), so the two
   docking sentences that survived the extraction are read **only as prose**, never as data.
3. 🔴 **Where `POLE4` binds on WWOX.** No fragment mapping, no deletion series, no WW control, no
   triad control exists. `PREMISE: NOBODY_LOOKED`. So `P282A`'s "SDR-span" membership is **external
   arithmetic** — the paper's own body contains `SDR` **0**, `short-chain` **0**, `dehydrogenase`
   **0** (verified case-sensitively after the `cadherin`/`ADH` false positive).
4. 🔴 **Whether presentation of the `GSK3β` 388–407 motif requires the SDR CORE fold.** Never
   measured, in any system, for any protein in this family. `PREMISE: UNVERIFIED`. ⇒ **a normal
   `GSK3β` curve for `Q230P` would be weak evidence of an intact fold**, and this is the single
   largest unquantified weakness in my own recommendation.
5. 🔴 **`P282A`'s half-life, and therefore what "no stability defect" numerically means.** No
   half-life value appears anywhere in the body for any allele; the CHX chase is
   densitometry-normalised to GAPDH at n = 3 with a Student's t-test. `PREMISE: DETECTION_FLOOR` on
   the **negative**. Criterion **C7 remains unmet for `P282A` as well as for `Q230P`** — which
   Scientist D's §8 item 4 stated for `Q230P` only.
6. 🔴 **`L404A`'s protein abundance.** Not reported in `PMID 22193544`'s held locators. So the
   `GSK3β` arc's loss-of-binding positive control **has no abundance credential of its own** —
   falsifier `D-4`.
7. 🔴 **Whether WWOX–`POLE4` engagement exists in unstressed cells.** UV-only, with informative
   zeros on every no-UV word. `PREMISE: NOBODY_LOOKED`.
8. 🔴 **Whether any of these engagements is SDR-dependent to the `PMID 28540421` standard.** None is.
   The nearest WWOX evidence is one **unpublished** observation with localisation as its readout and
   no data shown, against a **published** WW1-routed alternative. Unchanged from Scientist D's §8
   item 3, and now stated per partner.
9. 🔴 **Whether a NanoLuc or HaloTag fusion is tolerated by WWOX, at either terminus.** Unknown for
   this protein; `T-1` shows tag topology can flip the answer and `T-5` shows a tag can silently
   change one protein's biology and not its relatives'. Not assessable without the pilot.
10. ⚠️ **Whether an independent laboratory has ever replicated the TRAPPC6AΔ–WWOX SDR binding.** The
    repository records the biology as *"quasi esclusiva di questo gruppo, non replicata
    indipendentemente"*; I did not run a fresh census to test whether that is still true.
11. ⚠️ **`FT-024` (`PMID 15126504`, Sze 2004)** — the one body that could settle the `tau` question
    and the pY216-vs-pS9 ambiguity in `CLAIM 035`. **No PMCID; unobtainable from this checkout by any
    route** (independently established in `chang_ncku_wave2_node_independence_20260920.md`). Parked
    as an acquisition task, **not** escalated.
12. 🔴 **Everything downstream of engagement.** Whether engagement competence predicts anything about
    neurons, myelination, the developmental window, seizures or clinical course. `neuron` **0** and
    `seizure` **0** in `41124647`; **WOREE appears 7 times and every one is background prose with no
    data attached.** 🔴 **The paper's own most consequential sentence for this disease model points
    the other way and must travel with any use of it:** *"In this study, the cancer patient harboring
    germline homozygous WWOX P252A and P282A variants **did not suffer from WWOX-related nervous
    system disease** … However, WWOX^P252A^ and WWOX^P282A^ mutants **may have some residual protein
    function** to maintain the development of the neurological system."* **Cancer-assay-dead is not
    neurologically null**, and `P282A` — the design's positive control for "stable and dead" — is
    dead *in thyroid carcinoma assays* and, in the one human who carries it homozygously,
    **neurologically unaffected.**

---

## 7 · `HUMAN_REQUIRED` — parked, not pursued

🔴 **No `HUMAN_REQUIRED` decision packet replaces this adjudication.** The brief's condition for that
substitution — that only a materially new research programme would do — **is not met**: the label was
resolvable from published text, and the partner adjudication is a ranking of existing reagents.
Scientist D's `H-1` … `H-5` stand unchanged and I add nothing to them except the two below, both of
which are **external actions I am forbidden to take** and neither of which blocks the design.

| # | Action | Why `HUMAN_REQUIRED` | What it would change |
|---|---|---|---|
| **H-6** ⭐ | **Obtain `advs.202507602` Supporting Information** — Figures **S9** (`P252A` `POLE4` co-IP), **S10** (CASTp), **S11** (docking) | Not retrievable from this checkout: every publisher, PMC, Europe PMC and NCBI host returns an egress refusal, with `example.com` as the confirming control | 🔴 **It is falsifier `D-1`, the highest-value unopened item in this node**, and it decides whether `POLE4` holds one abundance-independent instance or two |
| **H-7** | **Obtain `PMID 15126504` (Sze 2004, `FT-024`)** | No PMCID; all routes refused. Author contact / WWOX Foundation / ILL are all external | Settles the `tau` arc (falsifier `D-6`) and the pY216-vs-pS9 ambiguity that `CLAIM 035` warns produces a false negative |

**No external human action was taken in this act:** no laboratory contacted, no author emailed, no
material requested, no institution approached.

---

## 8 · Declared limits of this file

- **No body was read end-to-end by me in this act.** I **searched** one body (`PMC12767083`) on two
  independent renderings for a specific textual fact and recovered it, and I read four figure legends
  and eleven passages of it. **That is a targeted verification, not a reading, and no
  `FULLTEXT_READ_RECEIPT` is claimed or recorded.** Everything else is another actor's attestation at
  the depth §0 declares.
- **No claim is created. No score is assigned to any expected assay result.** `FLAG FIRST` is
  honoured: the plate's outcome is not predicted and the therapeutic sign is not moved by one step.
  The boost axis stands exactly where Scientist B left it — **NOT-DANGEROUS-ON-THIS-EVIDENCE and
  STILL UNDETERMINED**, `IPOTESI`.
- **`PREMISE: NOBODY_LOOKED` / `UNREAD_PRIMARY` / `UNVERIFIED` are used with their distinct
  meanings** and are not interchanged: *nobody looked* where no experiment addresses the question
  (POLE4's binding site; ±UV; `L404A` abundance), *unread primary* where a body exists and is owed a
  reading (`PMID 21476439`; `FT-024`; the Supporting Information), *unverified* where a stated
  premise has no checked source (SDR homodimerisation; motif-presentation-requires-core-fold).
- **Abundance, stability, solubility and function are held apart throughout** — four lesions, four
  interventions. **No cross-variant generalisation.**
- 🔴 **`WWOX homodimerises via the SDR` is `PREMISE: UNVERIFIED`** and **nothing above is built on
  it.** The one dimerisation record is p-WWOX/p-p53 **hetero**-dimers, `PMID 39894307`.
- 🔴 **The `Q230P` namespace trap is not walked into:** the two records at a bare `"Q230P"` are
  **`GTPBP3`**, a different gene, at an identical `c.689A>C` (`PMID 41957021`, `38515655`). Neither
  appears anywhere above as evidence.
- **No prediction is used as a measurement.** The paper's PyMOL/CASTp/docking outputs are cited
  **only** as evidence of the authors' own variant attribution, never as evidence that the
  attribution is correct.
- **No new research programme is proposed.** No MAVE, no activity-sensor campaign, no
  deorphanisation. Those remain the Operator's decision and this file holds that line.
- 🔴 **I did not grep a tree containing my own output to verify any count.** Repository counts were
  taken with `git grep … HEAD`; body counts were taken with a case-sensitive word-boundary search of
  the fetched artefact in the scratchpad, reported alongside the naive count wherever the two differ.
- **No git command was run. No registry, queue, ledger, receipt, canonical file or state manifest was
  read-modified-written. No `BATCH_COMMIT`.** One output file was written: this one.
- **Nothing here is medical advice**, and no therapeutic recommendation for any person appears.

---

## 9 · Attribution

**According to PubMed**, the record adjudicated here is Zhang X, Qi J, Wang J, Wang Z, Wang Y, Hu Z,
Xu A, Hong B, Wang H (2025), *"Genetic and Functional Evidence Links Germline Biallelic Inactivating
Variants in WWOX to Histological Mixed-Type Thyroid Cancer"*, **Advanced Science** 13(1):e07602,
PMID 41124647, PMCID PMC12767083 — [DOI](https://doi.org/10.1002/advs.202507602). Supporting records
cited by PMID above, each with its DOI where the PubMed record carries one:
`PMID 22193544` — Wang H-Y *et al.* (2011), *Cell Death Differ* 19(6):1049–59,
[DOI](https://doi.org/10.1038/cdd.2011.188) ·
`PMID 27869163` — Schrock MS *et al.* (2016), *Oncogene* 36(16):2215–27,
[DOI](https://doi.org/10.1038/onc.2016.389) ·
`PMID 28540421` — Siddiqah IM *et al.* (2017), *Curr Genet* 63(6):1053–72,
[DOI](https://doi.org/10.1007/s00294-017-0702-y) ·
`PMID 21476439` — Sałuda-Gorgul A *et al.* (2011), *Z Naturforsch C* 66(1–2):73–82, which carries
**no DOI in its PubMed record**; none is asserted here.

⚠️ **Self-correction recorded rather than silently fixed.** In the first pass of this file I wrote
DOIs for `PMID 22193544` and `PMID 27869163` **from memory**, and both were wrong — one named the
wrong journal entirely, the other was off by one digit. I then queried the PubMed records and
replaced them with the returned values. **A remembered identifier is not a retrieved identifier**,
and the two are indistinguishable once written down, which is the whole reason this note is here.

**Licence note, carried from the repository's own receipt:** `41124647` is
*"© 2025 The Author(s), Advanced Science published by Wiley-VCH GmbH"*, with no machine-readable
licence recorded — **quote, do not redistribute.** All quotation above is verbatim excerpt for
verification purposes.

Scholar Gateway · *Which WWOX missense mutant protein loses its interaction with POLE4 …* · 12
passages · 1 article · 2025-10-22–2025-10-22
Scholar Gateway · *… which mutant is degraded rapidly via chaperone-mediated autophagy …* · 8
passages · 1 article · 2025-10-22–2025-10-22

---

Results retrieved by Scholar Gateway · Summary generated by AI — verify claims against source
documents · Last corpus update: September 2026 ·
[Content coverage details](https://support.scholargateway.ai/s/article/Available-Content)

---

**END OF FILE — complete run.** Nine sections, all written. Non-canonical research-layer file.
