# A third lab on WWOX localisation — `PMID 33565365` (Mahmud *et al.* 2021, rat testis)

> **Research layer — non-canonical. READ-ONLY toward every registry, ledger and `*_current.md`.**
> No BATCH_COMMIT, no commit candidate, no receipt, no registry edit was made by this session.
> Actor: SCIENTIST A · Date: 2026-09-21 · Disease model: WOREE / WWOX-DEE (public edition).
> **Not medical advice.**

⚪ **DEPTH DECLARATION — READ THIS BEFORE ANY SENTENCE BELOW.**
**This is an ABSTRACT-LEVEL note, not a read.** The PMC deposit returned a **measured body of 0
bytes**. There is no Methods section, no Results section, no figure legend, no antibody catalogue
number and no fractionation protocol in LEGEND's possession. Under
[`gold_is_in_the_details.md`](../../../framework/master/gold_is_in_the_details.md) **an abstract is
not a read**, and nothing here may be promoted, cited as a locator for a canonical claim, or used
to move the working model.

---

## 1 · ARTEFACT MANIFEST

| Artefact | Path | Bytes | Chars | sha256 |
|---|---|---|---|---|
| **PMC body (MCP), verbatim** | `files/fulltext/PMID33565365_PMC_MCPtext.txt` | **0** | **0** | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| Abstract fallback (persisted) | `files/fulltext/PMID33565365_abstract_PubMedMCP.txt` | 5083 | 5077 | `e6b91e762e955db182f8ebe7b6492e04a9186418c13b945c003442bdc39933af` |

`e3b0c442…852b855` is the sha256 of the empty byte string. **The measured body length is zero.**
The file was written from the `full_text` field of
`mcp__PubMed__get_full_text_article(pmc_ids=["PMC8013998"])`, which returned `"full_text": ""`
alongside a populated `abstract` field — i.e. the deposit resolved, the record exists, and the body
is absent, not the request malformed.

### 1.1 Retrievability was established by fetching, on four independent routes — and the zero is real *for this deployment*

| # | Route | Result |
|---|---|---|
| 1 | `mcp__PubMed__get_full_text_article(["PMC8013998"])` | **200, `full_text: ""`** — 0 bytes, abstract populated |
| 2 | Europe PMC `…/PMC8013998/fullTextXML` (curl) | **blocked** — `connect_rejected`, gateway 403 to CONNECT, `www.ebi.ac.uk:443` |
| 3 | NCBI `efetch.fcgi?db=pmc&id=8013998` (curl) | **blocked** — `connect_rejected`, gateway 403, `eutils.ncbi.nlm.nih.gov:443` |
| 4 | `WebFetch` on `pmc.ncbi.nlm.nih.gov/articles/PMC8013998/` | **blocked** — `EGRESS_BLOCKED` |

🔴 **The honest reading of this zero.** Routes 2–4 are **not** evidence about the paper. They are
evidence about *this container*: `__agentproxy/status` reports `selective: false` and shows this
deployment's gateway already answering **403 to CONNECT** for `eutils.ncbi.nlm.nih.gov`,
`www.ncbi.nlm.nih.gov`, `api.unpaywall.org` and `api.openalex.org` at 17:33 today — i.e. **another
actor already ran the `find-fulltext` cascade this session and every tier was denied at the
gateway, not by any publisher.** Running `find-fulltext` again would re-walk a cascade whose tiers
are all pre-denied, so it was not run (→ DEFAULTS_TAKEN).
**Therefore: `PMID 33565365` is UNREAD, and it is NOT established as unreadable.** A deployment
with literature egress, or a manual PDF, may well deliver the body. It should stay at the top of
the unread queue, **not** be retired as "not retrievable".

### 1.2 Calibration note on `get_copyright_status` — the flag was consistent this time, and that changes little

`get_copyright_status("33565365")` returns `license.type: null`, `license.url: null`,
**`is_open_access: false`**, `copyright.statement: "© The Author(s) 2021"`. This time the flag and
the fetch agree. That does **not** rehabilitate the flag: the repository's record now stands at
**three false negatives** (the most recent delivering 46,589 characters) against **one occasion
where the fetch also returned nothing** — and even that one occasion is confounded, because the
body could not be cross-checked on any independent route. 🔴 **The rule is unchanged and was
followed: fetch first, always. A flag never closes a paper.**

---

## 2 · VERDICT on Q6 — bearing on the Aldaz/Chang dispute

### 🔴 **CANNOT ARBITRATE.**

**The deciding fact: this paper reports no mitochondrial measurement of any kind.** No
mitochondrial marker, no mitochondrial fraction and no mitochondrial compartment appears anywhere
in the retrievable record (`mitochondri*` = 0, `TOM20` = 0, `COX IV` = 0, `VDAC` = 0 over the
artefact). A study that positively locates a protein in compartment A, without ever assaying
compartment B, **cannot exclude B** — and Chang's claim is precisely about B. Secondarily, the
Golgi assignment itself rests on an antibody whose specificity controls are in the unretrievable
Methods, so LEGEND cannot even confirm that the positive limb is sound.
**The dispute stays open. It was kept open deliberately; nothing here closes it.**

---

## 3 · What was actually measured, and how

Everything in this section is **abstract- and metadata-depth**. Where a methodological fact is
unavailable it is written **`NOT RETRIEVABLE`**, never inferred.

| Dimension | What the record supports |
|---|---|
| **Species** | 🔴 **Rat** — `"…in Rats."` (title), MeSH `Rats`, `Animals`, `Male`. **Not mouse, not human.** LEGEND's prior abstract-level note in [`lectin_readout_domain_dependence_20260921.md`](lectin_readout_domain_dependence_20260921.md) § 4.1 carries the species in the title string but never states it in the reasoning — see § 6.2, where it turns out to matter a great deal |
| **Tissue** | Testis — *"normal testes"*. Normal, non-transformed, non-stressed |
| **Age / stage** | *"during postnatal days 0-70"* — a developmental series, i.e. the whole first wave of spermatogenesis |
| **Endogenous or construct?** | **Endogenous.** MeSH carries `Immunohistochemistry` and no transfection/GFP/recombinant term; `transfect` = 0, `GFP` = 0, `construct` = 0, `overexpress` = 0 over the artefact. ⚠️ These are **abstract-level zeros** (§ 5.2) — but the design (normal rat tissue, postnatal series, IHC + Western) admits no construct, and the MeSH indexing of the two disputants' foundational papers *does* carry `Green Fluorescent Proteins`, `Recombinant Fusion Proteins`, `Transfection`. The contrast is real |
| **Methods named** | *"using Western blotting and immunohistochemistry"*; plus a **subcellular fractionation** arm (*"isolated Golgi-enriched fractions"*) and a **dissociated-cell** arm (*"confirmed in single-cell suspension"*) |
| **Antibody + validation** | 🔴 **NOT RETRIEVABLE.** See § 4 — this is the decisive gap |
| **Fixation** | **NOT RETRIEVABLE** (`fixation` = 0, `paraformaldehyde` = 0 — abstract-level zeros, uninformative) |
| **Fractionation protocol + marker controls** | **NOT RETRIEVABLE.** The abstract names the fraction (*"Golgi-enriched"*) and **no marker at all** — not the Golgi markers used to certify enrichment, not any counter-marker |
| **Imaging modality / resolution** | **NOT RETRIEVABLE** (`confocal` = 0, `resolution` = 0, `electron microscopy` = 0 — abstract-level zeros) |
| **Quantification of colocalisation** | **NOT RETRIEVABLE** — `Pearson` = 0, `Mander` = 0 over the artefact. The abstract's own hedge is *"partially"*, which is a qualitative term |

### 3.1 The cell-type map, which is the paper's real content

> *"Immunohistochemistry showed that fetal-type and adult-type Leydig cells, immature and mature Sertoli cells, and germ cells (from gonocytes to step 17 spermatids) expressed Wwox except peritubular myoid cells, step 18-19 spermatids, and mature sperm."*

This is a **positive-and-negative** map across cell types within one tissue, at defined stages. It
is the most auditable thing in the abstract, because it contains **internal negative controls of a
sort**: peritubular myoid cells sit adjacent to Sertoli cells in the same section and are reported
**negative**, and the germ-cell signal **disappears at a defined differentiation step** (17 → 18).
A non-specific antibody does not usually produce a stage-resolved, cell-type-resolved pattern with
sharp internal negatives. ⚠️ **That is an argument for specificity; it is not a validation.** It
does not exclude cross-reaction with a genuinely cell-type-patterned off-target, and it is exactly
the kind of argument a genotype-null control exists to replace.

---

## 4 · 🔴 The decisive methodological question: antibody validation

### **Answer: NO genotype-null or knockdown control is retrievable — and therefore none can be credited.**

`knockout` = 0 · `knock-out` = 0 · `knockdown` = 0 · `siRNA` = 0 · `shRNA` = 0 · `Wwox-/-` = 0 ·
`preabsorb` = 0 · `blocking peptide` = 0 · `validat` = 0 · `antibod` = 0 over the artefact.
⚠️ **Every one of these is an ABSTRACT-LEVEL zero and therefore INADMISSIBLE as a negative about
the paper.** Abstracts do not list antibody validation; a `Wwox`-null control could sit in the
Methods of this very paper and produce exactly these counts. **LEGEND does not know.** The
`null` = 2 hits in the artefact are `license.type: null` / `license.url: null` — a **false positive
of the search string, not a null control.**

### **Is this paper BETTER evidence, or merely DIFFERENT evidence? — Say it plainly.**

🔴 **It is a better-designed experiment of unknown validity. On present evidence LEGEND must treat
it as DIFFERENT evidence, not yet BETTER evidence.**

- **Why the design is better.** Aldaz's and Chang's foundational compartment claims rest on
  **overexpressed, tagged constructs in transformed cell lines** — a 46 kDa protein carrying a
  ~27 kDa GFP, expressed far above endogenous level, in cells with deranged membrane traffic.
  Mahmud measures **endogenous protein, in normal non-transformed tissue, in vivo, across a
  developmental series, with an orthogonal biochemical arm (fractionation) and a third arm
  (dissociated single cells) checking the same assignment.** That is a strictly stronger design
  on every axis the contradiction packet criticises.
- **Why it is not yet better evidence.** Both disputants' weakness is *specificity of the reporter*.
  Replacing a tag artefact with an **antibody artefact** does not fix specificity — it relocates it.
  🔴 And LEGEND holds a directly relevant warning: the preprint read today records that
  *"Commercial anti-WWOX antibodies did not show any specific signal for IF"*. An
  immunohistochemical WWOX result therefore carries a **positive burden to justify its antibody**,
  and that justification sits in a Methods section LEGEND cannot open.
- **The asymmetry that decides the wording.** Aldaz's one endogenous IF result (`15064722`) has the
  same defect — antibody, no null. Mahmud does not out-rank it; **it matches it on reagent risk
  while beating it on every other axis** (in vivo, normal tissue, orthogonal arms, developmental
  series, and an independent lab). **The upgrade from "different" to "better" is one retrievable
  Methods section away.** That is the single highest-value next action on this paper.

---

## 5 · VERBATIM LOCATORS

All quotes are from the persisted artefact `files/fulltext/PMID33565365_abstract_PubMedMCP.txt`
(sha256 `e6b91e76…39933af`), which holds the abstract **twice** — once as returned by
`get_full_text_article` and once by `get_article_metadata`. **Counts of 2 mean the quote matched in
both independent renderings**; counts of 1 are title/metadata fields present once.

### 🔴 **RE-MATCH COUNT: 13 / 13 locators matched exactly (100%), verified programmatically.**

| # | Quote (verbatim) | Matches | Proposition it supports — and its limit |
|---|---|---|---|
| L1 | *"Cellular Expression and Subcellular Localization of Wwox Protein During Testicular Development and Spermatogenesis in Rats."* | 1 | Species = **rat**; system = testis. Nothing about neurons |
| L2 | *"we investigated the cellular and subcellular localization of Wwox in normal testes during postnatal days 0-70 using Western blotting and immunohistochemistry"* | 1 | Normal tissue; two named methods. **Mood: "investigated"** — no claim yet |
| L3 | *"Wwox is expressed in testes at all ages"* | 2 | Expression, by Western. Expression ≠ localisation |
| L4 | *"fetal-type and adult-type Leydig cells, immature and mature Sertoli cells, and germ cells (from gonocytes to step 17 spermatids) expressed Wwox except peritubular myoid cells, step 18-19 spermatids, and mature sperm"* | 1 | Cell-type map **with internal negatives** (§ 3.1) |
| L5 | *"Wwox localized diffusely in the cytoplasm with focal intense signals in all testicular cells"* | 2 | 🔴 The **primary** pattern is **diffuse cytoplasmic**. The Golgi signal is a *focal intensification on top of a diffuse pool* — **not** an exclusive Golgi assignment |
| L6 | *"These signals gradually condensed in germ cells with their differentiation and colocalized with giantin for cis-Golgi marker and partially with golgin-97 for trans-Golgi marker"* | 2 | The Golgi claim. **Mood: "colocalized"**, and for *trans*-Golgi only **"partially"**. No coefficient, no resolution |
| L7 | *"Biochemically, Wwox was detected in isolated Golgi-enriched fractions"* | 2 | 🔴 **Mood: "was detected in", not "is localized to"; "Golgi-ENRICHED", not "Golgi".** See § 5.1 |
| L8 | *"But Wwox was undetectable in the nucleus"* | 2 | **A reported NEGATIVE** — the only admissible negative in the record. See § 7 |
| L9 | *"This subcellular localization pattern of Wwox was also confirmed in single-cell suspension"* | 2 | A third, independent-preparation arm agreeing with the first two |
| L10 | *"might locate into Golgi apparatus via interaction with Golgi proteins"* | 2 | 🔴 **The authors' own conclusion is hedged to "might".** LEGEND must not harden it |
| L11 | *"These unique localizations might be related to the function of Wwox in testicular development and spermatogenesis"* | 2 | Function is **speculative in the authors' own words**. No function was measured |
| L12 | *"Animals; Immunohistochemistry; Male; Rats; Spermatogenesis; Testis; Tumor Suppressor Proteins; WW Domain-Containing Oxidoreductase"* | 1 | MeSH: **no** transfection / GFP / fusion-protein term; **no** mitochondria term |
| L13 | *"license.is_open_access: false"* | 1 | The flag state at fetch time (§ 1.2) |

### 5.1 A fraction is not a compartment — and here it is bare

L7 says *"detected in isolated Golgi-enriched fractions"*. Three things are missing and all three
are load-bearing: **(i)** which markers certified the fraction as Golgi; **(ii)** what the purity
was; **(iii)** 🔴 **whether mitochondrial markers were blotted on the same fraction.** Golgi
preparations by differential/density centrifugation routinely carry ER and mitochondrial
contamination. Without a counter-marker lane, *enrichment is not residence* and a Wwox band in a
Golgi-enriched fraction is compatible with a Wwox pool on a contaminating membrane. **Because
mitochondria were not assayed — or at least are not shown to have been — this fraction result
cannot be turned against Chang. That is stated here as an explicit limit, per the task's own
instruction.**

### 5.2 Zero-class ruling — which zeros are admissible

| Class | Tokens | Ruling |
|---|---|---|
| **Extractor-elision-prone** (italic gene/species tokens, superscripts, exponents, citation numerals) | — | **N/A.** There is **no body**. The elision hazard does not arise, because nothing was extracted |
| **Roman-class method words** — `giantin`, `golgin`, `Pearson`, `Mander`, `knockout`, `siRNA`, `mitochondri*`, `TOM20`, `COX IV` | see § 3–4 | 🔴 **These would be admissible zeros over a BODY. Over an ABSTRACT they are NOT.** An abstract omits Methods by construction. Every zero above is therefore **uninformative about the paper** and is reported only to document what LEGEND does and does not hold |
| **Non-zero roman hits** | `giantin` 2, `golgin` 2, `Golgi` 14, `colocaliz` 2, `nucle` 2, `fraction` 2 | Admissible **as presence**, at abstract depth |
| **Search false positive** | `null` 2 | Both are `license.type: null` / `license.url: null`. **Not a null control** |

**The one exception, and it is important:** L8 is a **stated** negative, not an absence of a token.
*"But Wwox was undetectable in the nucleus"* is the authors asserting a negative result in their
own abstract. **That is an admissible negative claim** (at abstract depth), unlike every zero above.

---

## 6 · Q4 · Q5 — mitochondria, and transfer to neurons

### 6.1 Q4 — Does it report ANY mitochondrial signal? **No — and it reports no mitochondrial *assay*.**

`mitochondri*` = 0 over the artefact. There is nothing to quote. 🔴 **The distinction that matters:
this is not a mitochondrial negative. It is a mitochondrial SILENCE.** Had the paper blotted TOM20
on the Golgi-enriched fraction and found Wwox absent from a mitochondrial fraction, that would be a
result bearing directly on Chang. Nothing of the sort is in LEGEND's possession. The dichotomy is
therefore **not dissolved** — it is simply **not addressed**. (Whether the full paper addresses it
is unknown and is the second-highest-value question for whoever retrieves the body.)

### 6.2 🔴 The sharpest thing this paper does — and it is a *tension*, not a resolution

LEGEND already holds **one other endogenous, in-vivo, no-construct localisation dataset**:
`15664696` (Chang lineage, 2005), immuno-EM on **rat/mouse retina**, which reports
*"a large number of immunogold particles of WOX1 and p-WOX1 … in the damaged mitochondria and
condensed nuclei"* and — decisively for this comparison — *"**little or no WOX1-positive particles
were found in the Golgi apparatus**"* (as quoted in
[`chang_aldaz_contradiction_packet_20260920.md`](chang_aldaz_contradiction_packet_20260920.md)
row 1b, at abstract depth).

**So LEGEND now holds two in-vivo, endogenous, construct-free localisation datasets — plausibly in
the same species (rat) — that disagree about the Golgi:**

| | `15664696` (Chang lineage) | `33565365` (third lab, this note) |
|---|---|---|
| Preparation | Rat/mouse retina, **in vivo**, endogenous | Rat testis, **in vivo**, endogenous |
| Method | Immunogold **electron microscopy** (~10 nm particle assignment) | **IHC / IF** (diffraction-limited, ~200–250 nm) + fractionation |
| State | **Stressed / degenerating** (light damage, `rd`) | **Normal, unstressed** |
| Golgi | *"little or no"* particles | *"colocalized with giantin"*, *"partially"* with golgin-97 |
| Nucleus | *"condensed nuclei"* — positive | 🔴 *"undetectable in the nucleus"* — negative |
| Mitochondria | Positive | **Not assayed** |

🔴 **Two confounds separate these rows simultaneously — tissue (retina vs testis) AND state
(stressed vs normal) — so the comparison is uninterpretable as it stands.** It does not favour
either lab. What it does is make **tissue-specific and state-specific localisation a live, evidenced
possibility** rather than a rhetorical escape hatch: two construct-free in-vivo datasets, and they
do not agree. **That is the finding of this note, and it is a finding about the shape of the
question, not about its answer.** ⚠️ On resolution, note that the *method* asymmetry runs against
Mahmud: immunogold EM resolves an organelle; diffraction-limited colocalisation does not.

### 6.3 Q5 — Transfer to neurons: what transfers and what does not

🔴 **What does NOT transfer — the compartment assignment itself. Almost nothing here is evidence
about a neuron.**

1. **Cell type is a disqualifier, not a caveat.** This paper's *own* data show localisation and even
   expression varying **between adjacent cell types of one tissue** (L4: Sertoli positive,
   peritubular myoid **negative**) and **between stages of one lineage** (germ cells positive to
   step 17, **negative** at step 18–19). 🔴 **A paper that demonstrates cell-type- and
   stage-specific Wwox handling within a single tissue is, by its own result, the weakest possible
   licence to export that handling to a different cell type in a different organ.** The paper
   argues against its own transferability.
2. **The Golgi of a differentiating spermatid is not a generic Golgi.** 🔵 *(INFERENZA — my
   mechanistic background, NOT from this paper, which never uses the word:* `acrosome` = 0 *over the
   artefact.)* In spermiogenesis the Golgi is a hypertrophied, specialised organelle that
   manufactures the acrosome, and it is largely shed with the residual body late in spermiogenesis.
   The abstract's two most striking observations — that signals *"gradually condensed in germ cells
   with their differentiation"* and that signal is lost at *"step 18-19 spermatids"* — **track
   acrosome biogenesis and Golgi disposal.** Two readings remain open and the artefact cannot
   separate them: **(a)** genuine Golgi residence, elegantly traced through the one cell type where
   the Golgi is most conspicuous; **(b)** a bulk-secretory-compartment or cytoplasmic-volume effect
   in the cell with the largest Golgi in the body, vanishing when that cytoplasm is discarded.
   Neurons have no acrosome and no residual body. **Reading (a) would transfer weakly; reading (b)
   would not transfer at all.**
3. **Post-mitotic neurons are the tissue where the rival lab's best evidence sits.** The one
   construct-free dataset in **neurons** (`15664696`) reports the Golgi **negative**. Exporting a
   testis Golgi pool into neurons would mean overriding a neuronal measurement with a
   non-neuronal one.

🟢 **What DOES transfer — three things, all methodological rather than substantive:**

1. **An existence proof for the assay.** Endogenous Wwox **can** be localised in normal tissue
   in vivo, with no construct, and cross-checked by fractionation and by dissociated cells. That is
   the experimental template the contradiction packet's § "what would settle it" asks for — run in
   the wrong tissue, without the genotype control.
2. **A diffuse cytoplasmic pool as the baseline (L5).** *"localized diffusely in the cytoplasm with
   focal intense signals"* — whatever the focal compartment turns out to be, the **majority** pool
   is cytosolic. Any single-compartment model of WWOX, Aldaz's or Chang's, is arguing about a
   **minority** pool. This is the most genuinely transferable statement in the paper and it belongs
   in the dispute's framing.
3. **A nuclear negative at steady state (L8)** — see § 7.

---

## 7 · NEGATIVE RESULTS — explicit

| # | Negative | Class | Weight |
|---|---|---|---|
| **N1** | *"But Wwox was undetectable in the nucleus"* (L8) | **Reported negative** (authors' own claim, abstract depth) | ⚠️ **Genuine but weak, and its bearing is narrow.** It runs against the **nucleus limb** of Chang's position — but Chang's nuclear claim (`15664696`) is **stress-induced translocation in degenerating neurons**, and this is **normal unstressed testis**; the two are not the same measurement, so N1 does not touch it. It is also *"undetectable"* — a detection-limit statement made with an unvalidated antibody, i.e. the weakest form of a negative. It does **not** conflict with Aldaz, whose nuclear WWOX is the **SDR-deleted mutant** isoform, not wild type |
| **N2** | *"except peritubular myoid cells, step 18-19 spermatids, and mature sperm"* (L4) | **Reported negative** | 🟢 Useful twice: as an internal specificity argument (§ 3.1) and as this note's strongest evidence **against** cross-tissue transfer (§ 6.3) |
| **N3** | No mitochondrial assay in the record | 🔴 **SILENCE, not a negative** | **Zero evidential weight in either direction.** This is the fact that decides § 2 |
| **N4** | No Pearson/Mander coefficient, no stated resolution, no Golgi-fraction purity, no counter-marker, no antibody validation | 🔴 **NOT RETRIEVABLE — inadmissible as negatives** | These are artefacts of holding an abstract. They are gaps in LEGEND's possession, **not** defects demonstrated in the paper. **Do not cite this note as evidence that the paper lacks them** |
| **N5** | This note's own prior | **Method negative** | The activity-sensor census and the Golgi-readout census both failed to surface this paper as a localisation datum until § 4.1 of the lectin note found it by hand. **A census that misses the one independent in-vivo dataset on the exact compartment in dispute is a census defect** |

---

## 8 · Q7 — Bearing on the lectin readout, proportionate

**Direction: marginally MORE credible. Magnitude: small — a prior nudge, not a step change. It does
not convert the lectin readout into a WWOX-activity readout.**

**What it adds (honestly stated).** Before today, every claim that WWOX sits at the Golgi came from
**one lab, on tagged constructs, in transformed lines**, with a single endogenous IF result in one
cancer line. LEGEND now has an **independent lab, in a second and non-transformed system, in vivo,
on endogenous protein, with an orthogonal biochemical arm**, reporting a Golgi-associated pool. The
Aldaz Golgi assignment is therefore **no longer single-lab and no longer construct-only**. That is a
real, non-trivial increment to the *premise* the lectin readout depends on.

**Why the increment is small, in four steps — each of which independently caps it:**

1. 🔴 **Residence is not function, and the lectin readout needs function.** The readout's logic is:
   *WWOX lesion → Golgi glycosylation machinery impaired → altered surface glycans → increased
   lectin binding*. This paper speaks only to **where a protein is**. It measures **no**
   glycosylation, **no** secretory flux, **no** Golgi morphology, and **no** consequence of
   removing Wwox. Even if the Golgi pool is completely real, a protein can sit on a membrane
   without its loss perturbing that membrane's enzymology. **The paper supports the readout's
   premise and is silent on the readout's mechanism.**
2. **It is abstract depth.** By LEGEND's own rule this is not a read. The increment is provisional
   and reverses on retrieval if the Methods disappoint.
3. **The antibody is unvalidated as far as LEGEND can check** (§ 4), against a standing warning that
   commercial anti-WWOX antibodies failed to give specific IF.
4. 🔴 **It does not touch the upstream question the lectin note identified.** The lectin note's
   finding was that the Aldaz/Chang dispute is **prior to** the sensor question. This paper does
   not arbitrate that dispute (§ 2), so **the upstream blocker stands exactly where it was.** The
   readout's status is unchanged: coherent on Aldaz, an indirect downstream proxy on Chang.

**Net, in one sentence:** the Golgi premise moves from *one lab, constructs only* to *two labs, one
of them construct-free in vivo* — a strengthening of a **premise**, not a validation of a
**readout**, and the readout's decisive weakness (an SDR lesion might produce a mitochondrial, not
a glycosylation, defect) is untouched.

---

## 9 · STEP 0 — ledger check: what each method found

🔴 **`NO RECORD MATCHED` ≠ `NOT HELD`. Both methods were run and they returned different things.**

| Method | Result |
|---|---|
| `registry_records.py get --pmid 33565365` | **`hits: 2 identity`** — **not** a miss. (a) `paper_registry_current.md:2177` → `## CORPUS-STUB-153`, `**Status:** not_processed`, `**Registry role:** corpus placeholder only`, `**Claim links:** none`. (b) `literature_tracking_log_current.md:5011` → `## LIT-0170`, `**Status:** discovered`, `Authors: not yet extracted`, `Year: unknown`, `clinical relevance: LOW`, `Claim links: none` |
| `grep -rn "33565365" --include=*.md disease-models/` | **7 hits in 5 files** — the two registry records above, **plus** `batch_queue.md:347` (status `screened`), **plus** `analysis/next_scientist_scout_20260921.md` (×3, listed as *"Genuinely unread"*), **plus** `analysis/lectin_readout_domain_dependence_20260921.md` (×6, including the § 4.1 abstract quote) |

🔴 **The two methods disagree and the disagreement IS the finding.** The tool reads **committed
canonical state only** and excludes `analysis/` and the hypotheses ledger — so it missed **the
richest holding LEGEND has on this paper**, the § 4.1 assessment written today, which already
carries the abstract quote and the judgement *"the highest-value unread item bearing on this
question"*. **An actor who had run only the tool would have concluded LEGEND held a bare stub and
would have duplicated § 4.1 wholesale.** This is the fifth occurrence of that error class today.
⚠️ The tool also emitted: `WORKING TREE DIRTY: disease-models/wwox/research/full_text_queue_current.md`
— another actor has an uncommitted edit in flight; this session touched nothing.

**Registry status is therefore: HELD at stub depth, SCREENED, NOT PROCESSED, NOT READ — and now
assessed at abstract depth twice.** No registry, ledger, receipt or queue was modified by this
session.

---

## 10 · INFORMATION GAIN

| Item | Gain | One line |
|---|---|---|
| **Mechanistic graph** | **NO** | No mechanism, no interaction, no pathway is added; a third lab's compartment *association* is not a mechanistic edge, and the paper measures no consequence of Wwox loss |
| **Therapeutic hypothesis** | **NO** | Nothing druggable, no target, no lever; rat testis at steady state generates no therapeutic move for WWOX-DEE |
| **Experimental roadmap** | 🟢 **YES** | Two concrete additions: **(i)** retrieve this Methods section — it is the single cheapest experiment in the programme, and it decides whether "different evidence" becomes "better evidence"; **(ii)** the contradiction packet's row-1a experiment should now be specified **across ≥2 tissues**, because § 6.2 shows two construct-free in-vivo datasets disagreeing, so a single-system fractionation could settle the wrong question |
| **Genotype stratification** | **NO** | No genotype, no allele, no variant anywhere in the record; wild-type rat only |
| **Intervention ranking** | **NO** | No intervention is ranked or re-ranked; the lectin readout's standing is nudged but it is a **readout**, not an intervention |
| **Uncertainty** | 🟢 **YES — the main gain, and it moves in two directions** | **Reduced:** the Golgi premise is no longer single-lab/construct-only. **Increased and better-shaped:** the competing localisations are now shown to have **tissue and state confounds running together** (§ 6.2), the mitochondrial limb is shown to be **unaddressed rather than refuted** (§ 6.1), and the retrievability zero is shown to be a **deployment limit, not a property of the paper** (§ 1.1) — so a paper LEGEND had begun to treat as closed is re-opened |

---

## 11 · DEFAULTS_TAKEN

1. **Wrote a second artefact file.** The brief authorised one analysis file plus the STEP 1 artefact.
   Because the STEP 1 artefact is **empty**, no quote could be re-matched against anything, and the
   discipline *"re-match every quote programmatically against the artefact"* would have been
   unsatisfiable. I persisted the abstract fallback as
   `files/fulltext/PMID33565365_abstract_PubMedMCP.txt` so that all 13 locators are machine-checkable
   against a fixed, hashed file. It is a research-layer artefact; no canonical file, ledger, receipt
   or registry was touched.
2. **Did not re-run `find-fulltext`.** `__agentproxy/status` shows this deployment's gateway already
   answered **403 to CONNECT** today for `eutils.ncbi.nlm.nih.gov`, `www.ncbi.nlm.nih.gov`,
   `api.unpaywall.org` and `api.openalex.org` — i.e. tiers 1–4 of that cascade are pre-denied, with
   `selective: false`. I verified three domains myself (§ 1.1). Re-running the cascade would consume
   the session to re-derive the same 403s. **Consequence: the paper is recorded as UNREAD, explicitly
   NOT as unreadable** (§ 1.1) — the opposite default from retiring it.
3. **Used `get_article_metadata` as a second abstract source.** Not requested. Done to obtain the
   species (**rat** — absent from the brief and from the § 4.1 reasoning), the MeSH indexing (which
   is what licenses the "endogenous, no construct" reading), the affiliations (which confirm the
   third-lab independence claim), and a **second independent rendering of the abstract** so that
   locator matches at `n=2` are cross-source rather than single-source.
4. **Flagged one abstract-rendering discrepancy rather than silently normalising it.** The
   `get_full_text_article` rendering terminates *"…spermatogenesis**:**"* (colon) where the
   `get_article_metadata` rendering terminates *"…spermatogenesis**.**"* (period), and the former
   uses en-dashes where the latter uses hyphens. **Substance is identical**; this is a deposit
   punctuation artefact. Locators were matched against the ASCII-hyphen rendering; both renderings
   are preserved verbatim in the artefact.
5. **Marked the acrosome/residual-body reasoning (§ 6.3 ¶2) as `INFERENZA` from my own background
   knowledge, not from the paper.** `acrosome` = 0 over the artefact. It is offered as a confound to
   be tested against the real Methods and figures, **not** as a finding, and it is not used to
   support the § 2 verdict.
6. **Did not resolve the dispute, and did not let the nuclear negative (N1) drift into a verdict.**
   L8 is the one datum in this paper that cuts against a Chang limb, and the temptation is to
   promote it. It is confined to § 7 with its three limits stated. **The verdict is CANNOT ARBITRATE
   and it rests on § 6.1 alone.**
7. **No wikilinks were created to registry records**, to avoid generating LINT-visible edges from a
   research-layer note into canonical state.

---

## 12 · Attribution

Per PubMed tool terms: bibliographic data and the abstract quoted throughout were retrieved from
**PubMed / PubMed Central**. Mahmud MAA, Noguchi M, Domon A, Tochigi Y, Katayama K, Suzuki H.
*Cellular Expression and Subcellular Localization of Wwox Protein During Testicular Development and
Spermatogenesis in Rats.* J Histochem Cytochem. 2021;69(4):257–270.
PMID 33565365 · PMC8013998 · [DOI: 10.1369/0022155421991629](https://doi.org/10.1369/0022155421991629).
Comparator papers cited at abstract depth from LEGEND's existing notes: `15664696`
[DOI: 10.1016/j.neuroscience.2004.07.054](https://doi.org/10.1016/j.neuroscience.2004.07.054),
`15064722`, `11058590`, `14526170`, `11719429`, `24932569`.
