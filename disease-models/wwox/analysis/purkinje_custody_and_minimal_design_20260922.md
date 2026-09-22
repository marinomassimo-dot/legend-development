# The Purkinje question reduces to a custody read — the exact questions, the µm/pixel threshold, and the smallest stored-section design

**Actor:** Scientist B · **Date:** 2026-09-22 · **Axis:** converting *"we think existing images might work"*
into either an answerable custody question or the smallest stored-section experiment.

**Posture.** This file assumes **nothing** about whether the retained image files suffice. The prior wave
converged on a sentence — *"a panoramic scanner digitises the entire section at objective resolution"*
— which is an **inference from instrument class stated as a property of the files**
(SIBLING-ATTESTED, [`cerebellar_discrimination_experiments_20260922.md:381`](cerebellar_discrimination_experiments_20260922.md)).
That sentence is the thing this file replaces with a question a holder can answer in minutes.

**`PREMISE: NOBODY_LOOKED` — carried intact.** Nothing below asserts, implies or scores that Purkinje cells
**are** or **are not** transduced, reached, or WWOX-expressing. Every "unknown" here is a statement about the
**measurement record**, never about the cell.

🔴 **The rule this file obeys at every line.** *Absence of a specification in this repository is a fact about
our records, not about the files.* A missing NA is not a low NA. A missing pixel size is not a coarse pixel
size. A missing channel list is not a missing channel. Where the repository is silent, the correct entry is
`UNKNOWN — HOLDER-ONLY`, and the correct act is to ask, not to infer.

**Not medical advice.** No molecule, dose, route or clinical recommendation appears here. Public edition:
the reference genotype class only. 🔴 **No alleles or models are pooled** — the `Wwox`-null (Aqeilan-line)
material, the `Wwox^P47T/P47T` knock-in material, the rat `lde/lde` material and human tissue are kept in
separate rows throughout and no number crosses between them. The 2021 and 2026 archives are never merged.

**Read-only.** No registry, `*_current.md`, ledger, receipt chain, state manifest or queue was modified. No
git command. No `BATCH_COMMIT`. No external contact of any kind — nobody was written to, and every question
in § 1 is a **row in a file**, not a message. This file is the only artefact produced.

**Attestation discipline.** I read **no primary article** in this act. Every verbatim string below is
reproduced from a repository file and tagged **SIBLING-ATTESTED** with `file:line`. Where a sibling marked a
string FIRST-HAND I say so, but I do **not** inherit its first-handedness.

---

## 0 · Established at source before building — verification log

| # | Fact as handed over | Verified at | Verdict |
|---|---|---|---|
| 1 | The cerebellar transduced-fraction reagent is `MAB377` = NeuN clone **A60**, excluding Purkinje from numerator **and** denominator; ≈61% is a **granule-cell** measurement | [`cerebellum_layer_localisation_20260922.md:573`](cerebellum_layer_localisation_20260922.md) § 6.2 (reagent verbatim at `:280`); synthesis at [`cerebellar_discrimination_experiments_20260922.md:637`](cerebellar_discrimination_experiments_20260922.md) § 13.2 | 🟢 **HOLDS, and is stronger than handed over.** Weyer & Schilling 2003 (sibling-verified first-hand) puts NeuN at **granule neurons only** in murine cerebellum — *"not expressed by any other immunocytochemically identified cerebellar interneurons, which comprised basket and stellate cells, Golgi neurons, unipolar brush cells, and Lugaro cells"*; and its Discussion generalises Purkinje NeuN-negativity to the **antigen**, not the clone. Aldaz & Hussain put **basket** and **granule** cells at the highest cerebellar WWOX ⇒ the ≈61% excludes one of its own two top candidates |
| 2 | The archive is **3-channel**; WWOX's only identity partners have ever been NeuN and βIII-tubulin | [`purkinje_existing_material_experiment_20260922.md:239`](purkinje_existing_material_experiment_20260922.md) § 2.3; secondaries at `:244`; re-verified at `:597` | 🟢 **HOLDS, and it is a secondary-antibody fact, not a filter choice.** Exactly two secondaries exist — *"goat anti-rabbit Alexa flour 647"*, *"goat anti-mouse Alexa flour 488"* — plus *"Hoechst 33258 (1:1000)"*. **Four rabbit primaries compete for one channel; two mouse primaries compete for the other** |
| 3 | 🔴 No objective, NA or pixel-size specification is attached to the 3DHISTECH scanner in **any** repository artefact | [`purkinje_existing_asset_ceiling_20260922.md:378`](purkinje_existing_asset_ceiling_20260922.md) V1, with the scope correction at `:396` V2 | 🟢 **HOLDS in its corrected form only.** `numerical aperture` 0, `pixel size` 0; but `objective` 12 and `20x|40x|63x` 15 **elsewhere in the corpus**, in dose-forensics and delivery files, **none attached to the scanner**. ⚠️ *"Zero tokens in the corpus"* is the overstated form and is **not** carried forward here |
| 4 | 2021 archive: **in-vivo** reporter material, **no lysates**, therapeutic vector `AAV9-hSynI-mWwox-IRES-EGFP` | [`purkinje_cheapest_path_and_community_followup_20260922.md:199`](purkinje_cheapest_path_and_community_followup_20260922.md) § 2.3, `:219` § 2.3b, `:248` § 2.4 | 🟢 **HOLDS.** *"As control, AAV9-hSynI-EGFP was used"*, ICV at P0, `2E10`/hemisphere, perfused, 12–14 µm sagittal. The **complete 2021 Methods heading list** contains no immunoblot and no tissue extraction ⇒ image archive only |
| 5 | 2026 scans are `BLOCKED — HOLDER-ONLY` | [`purkinje_existing_material_experiment_20260922.md:291`](purkinje_existing_material_experiment_20260922.md) § 2.6 | 🟢 **HOLDS.** *"Data and code availability: Not relevant."* — there is no deposited image and no repository to query |
| 6 | 2026 `AAV9-hSynI-EGFP` is used **in vitro only** (E13.5 DRG cultures, DIV6) | [`purkinje_existing_material_experiment_20260922.md:266`](purkinje_existing_material_experiment_20260922.md) § 2.4 | 🟢 **HOLDS**, and § 4.4 below turns it into the hard bound on the arrival channel at therapeutic dose |
| 7 | The 2021 IF Methods name **no DAPI and no Hoechst** — they end at *"mounting with mounting medium"* | [`purkinje_cheapest_path_and_community_followup_20260922.md:188`](purkinje_cheapest_path_and_community_followup_20260922.md), `RC-1` at `:410` | 🟢 **HOLDS.** ⚠️ And it is `NOT STATED`, **not** a demonstrated absence — the Appendix Table S1 (`FT-152`) is unretrieved |

---

# 1 · THE PRECISE CUSTODY QUESTION

## 1.1 What this section is, and what it is not

Twelve questions. Each is answerable by **opening one file header and reading one field**, or by looking at a
folder listing — minutes of work for whoever holds the material, and **impossible from outside it**, because
none of these fields is in either paper. That is the distinction between *unretrieved* and *unrecorded*
([`purkinje_existing_asset_ceiling_20260922.md:120`](purkinje_existing_asset_ceiling_20260922.md)): better
retrieval clears the first and cannot touch the second.

🔴 **Nothing was sent.** These are rows in a file. The framing rule of the prior wave applies unchanged:
*their existing work creates a natural next question*, never *the authors were wrong*. No Methods section in
any field states its scanner channel profile or its scan objective; the absence is a **convention of
publishing**, not a defect of this programme.

🔴 **And each row obeys the prohibition.** The "kill" column below says what would make the **marker-free
route** unavailable. It never says, and must never be read as saying, anything about Purkinje biology. A scan
at 4 µm/pixel would kill the marker-free route and would leave `PREMISE: NOBODY_LOOKED` exactly where it is.

## 1.2 The twelve questions

**Group A — can the file resolve a soma at all?**

| # | Question, as a holder would answer it | 🟢 Answer that makes the marker-free route **viable** | 🔴 Answer that **kills** it (for that file) |
|---|---|---|---|
| **Q1** | **Which objective was the scan profile run at** — not the instrument's maximum, the setting actually used for these slides? (In a 3DHISTECH `Slidedat.ini` this is the objective / magnification entry; in an exported OME-TIFF it is in the acquisition metadata) | **20× or 40×.** At 20× the route is viable for soma-level work; at 40× it is comfortable | **10× or lower** (survey/overview profile). A whole-slide scanner run at low power digitises the entire section and still cannot separate a Purkinje soma from the granular-layer boundary |
| **Q2** | **What is the pixel size in µm per pixel**, as recorded in the file header (`MICROMETER_PER_PIXEL_X` / `_Y`, or the OME `PhysicalSizeX`)? 🎯 **This single number answers more than Q1**, because it is what the file actually contains, whatever objective was nominally selected | **≤ 0.5 µm/px** — working requirement; **≤ 0.25 µm/px** — comfortable, supports chromatin-texture and nucleolus criteria (§ 2) | **> 1.0 µm/px** — below the floor derived in § 2.4. Between **0.5 and 1.0** the route is `MARGINAL`: layer segmentation survives, per-soma discrimination from Bergmann glia does not |
| **Q3** | **What is the numerical aperture** of that objective? | **NA ≥ 0.3** is already sufficient for *lateral* separation of the relevant objects (§ 2.5) | 🎯 **No realistic answer kills the route on lateral resolution.** NA is the **wrong question to lead with** — it decides light collection and depth of field, not whether two 8 µm somata are separable. Recorded here to be **retired**, not to be waited on |
| **Q4** | **Single focal plane, or z-stack / extended-focus?** And if single, where in the 14 µm was it placed? | **Extended focus or a z-stack** — the truncation and out-of-focus traps both shrink | **Single plane, position unrecorded.** Does not kill the route, but it fixes the mean-not-integrated rule and the molecular-facing half-mask rule as **mandatory**, not advisory (§ 4.6) |

**Group B — is the information still in the file, or was it thrown away on save?**

| # | Question | 🟢 Viable | 🔴 Kills |
|---|---|---|---|
| **Q5** | 🎯 **Are the saved files the ORIGINAL scanner format** — `.mrxs` with its `Slidedat.ini` and `Data*.dat` sidecars, or the vendor equivalent — **or EXPORTED derivatives** (`.tif`, `.jpg`, `.png`, a CaseViewer annotation export, a figure crop)? | **Original format retained.** Header fields Q1/Q2/Q4/Q6 all become readable from the file itself, with no recollection required | **Only exports survive.** An export is a **decision already taken** about zoom level, bit depth and channel merge, and it is usually irreversible. ⚠️ This does **not** kill the route outright — it makes Q2 and Q6 apply to *the export*, and the honest answer becomes *"the original is gone; what is left is what it is"* |
| **Q6** | If exported: **at which zoom level / downsample factor**, and was the export a **channel merge** (one RGB image) or **separate channels**? | **Level 0 (full resolution), channels separate** | **A merged RGB at ≥2× downsample.** A merge destroys per-channel intensity; a 2–4× downsample turns a 0.25 µm/px scan into a 0.5–1.0 µm/px one and can cross the floor by itself |
| **Q7** | **Bit depth, and was brightness/contrast adjusted before saving?** The 2021 paper states its processing *"included the global changes of brightness and contrast"* (SIBLING-ATTESTED, [`purkinje_cheapest_path_and_community_followup_20260922.md:148`](purkinje_cheapest_path_and_community_followup_20260922.md)) | **16-bit, unadjusted raw retained** | **8-bit after contrast adjustment.** 🎯 **This kills QUANTIFICATION without killing LOCALISATION.** A contrast-adjusted 8-bit file can still show *where* the Purkinje row is; it cannot carry a per-cell intensity distribution, which is the entire output of the § 4 design |

**Group C — is the nuclear channel actually in the file?**

| # | Question | 🟢 Viable | 🔴 Kills |
|---|---|---|---|
| **Q8** | 🎯 **How many channels were ACQUIRED in the scan profile** — not how many were stained — and **which filter sets**? A whole-slide fluorescence scanner is routinely run on a subset of the filters a slide carries | **3 channels acquired**, including a DAPI/Hoechst filter | **2 channels** (the two Alexa fluorophores, nuclear filter omitted). This is `RJ-7` ([`purkinje_existing_material_experiment_20260922.md:550`](purkinje_existing_material_experiment_20260922.md)) and it is the **single most load-bearing unknown**: without a DNA channel the marker-free morphology route of § 3.1 of that file collapses entirely |
| **Q9** | **Does a nuclear counterstain channel exist in the saved 2021 files?** (Distinct from Q8: the 2021 IF Methods name no DAPI and no Hoechst at all — SIBLING-ATTESTED, `RC-1`) | **Yes, a DNA channel is present** — the strongest possible answer, because 2021 is the **confocal** archive | **No counterstain was ever applied.** ⚠️ **Not fatal, and the workaround is already on the slide:** NeuN is granule-restricted in murine cerebellum, so the **NeuN-bright granular band and NeuN-dark molecular band bracket the Purkinje monolayer** ([`purkinje_cheapest_path_and_community_followup_20260922.md:190`](purkinje_cheapest_path_and_community_followup_20260922.md)). 🔴 That workaround is `INFERENZA` from an attested antigen property plus cytoarchitecture (`PREMISE: DEFAULT_FROM_TEXTBOOK`), **not a measurement**, and it gives a **landmark**, never a soma mask |
| **Q10** | **Which fluorophore is on which channel, per slide series** — and does **any** archived slide carry **native EGFP**? | A slide set where EGFP is **uncontested** by the anti-mouse AF488 secondary — i.e. the **2021 `AAV9-hSynI-EGFP` control arm, which needs no antibody at all** | **EGFP and AF488-NeuN on one channel** in the `mWwox-IRES-EGFP` arm. This is `RC-2` ([`purkinje_cheapest_path_and_community_followup_20260922.md:411`](purkinje_cheapest_path_and_community_followup_20260922.md)), pending Appendix Table S1 (`FT-152`). If they are not separable, the therapeutic-arm reporter read costs a re-stain and only the control arm stays free |

**Group D — is the cerebellum, in the arm of interest, actually in the scanned region?**

| # | Question | 🟢 Viable | 🔴 Kills |
|---|---|---|---|
| **Q11** | **What sagittal / mediolateral level was cut**, per section series — vermis or hemisphere — and is there a block-orientation or coordinate record? | **Any recorded level.** Vermis is the preferred answer for this question, because the published `Wwox^P47T/P47T` Purkinje counts are **vermis** counts ([`cerebellar_functional_readout_census_20260922.md` R17](cerebellar_functional_readout_census_20260922.md)) 🔴 **and that is a comparability note only — the two alleles are never pooled** | **No level record at all.** Does not kill the Purkinje read; it kills **vermis-vs-hemisphere resolution** and any lobule-level statement, and it means each section's level must be reconstructed from its own foliation pattern |
| **Q12** | 🎯 **For which ARMS and AGES do cerebellum-containing scans exist** — specifically `1.23E11` (LD) and `2.63E11` (HD), and at which of P10–P180? | **Cerebellar scans exist in LD and HD.** Then the whole ladder of § 5 is live at the therapeutic dose | **Cerebellar scans exist only in the `4E10` +WPRE comparison arm.** This is `R4` ([`cerebellar_discrimination_experiments_20260922.md:551`](cerebellar_discrimination_experiments_20260922.md)), narrowed but not closed: cerebellar IHC is **first-hand established for the WPRE comparison arm** and **strongly implied for the HD arm at ~3 months**, **unassigned at P240/P300**, and **silent for LD** ([`purkinje_existing_material_experiment_20260922.md:228`](purkinje_existing_material_experiment_20260922.md) § 2.2). ⇒ An existing-image answer would then be an answer **at `4E10` +WPRE**, and would transfer to no other dose |

**Group E — is there anything left to cut?** *(one question, because it decides whether § 4 exists at all)*

| # | Question | 🟢 Viable | 🔴 Kills |
|---|---|---|---|
| **Q13** | **Are raw scan files retained, or only figure exports? And are the FFPE blocks, the OCT blocks and the unstained serial neighbours retained?** | **FFPE blocks retained** — 🎯 the strongest single answer in the whole set, because FFPE is effectively an indefinite archive and is **re-cuttable without limit**, so § 4 survives even if every image answer above goes the wrong way | **Nothing retained but published figures.** Then every rung above L0 is dead and the question becomes a new-animal question — which is the one outcome this whole line of work exists to avoid |

## 1.3 🎯 The dependency structure — why these are not thirteen serial checks

**Q2, Q8 and Q12 must be true SIMULTANEOUSLY** for the marker-free route, and any one of them being false
collapses it on its own: a file with soma-level pixels but no DNA channel has no WWOX-independent mask; a
file with a DNA channel at 2 µm/px cannot separate a Purkinje nucleus from a Bergmann-glia nucleus; a file
with both, covering only the `4E10` arm, answers at a dose nobody asked about
([`purkinje_existing_asset_ceiling_20260922.md:111`](purkinje_existing_asset_ceiling_20260922.md)).

**Q13 is orthogonal and strictly more important.** If FFPE blocks survive, § 4 is executable whatever Q1–Q12
return — and § 4 answers a question the images cannot answer at all (cell identity). ⇒ **Ask Q13 first.**

**Q3 should be asked and then set aside** (§ 2.5). Naming it here is deliberate: it has been the reflexive
first question on this axis, and § 2 shows it is not the binding one.

## 1.4 🔴 What a non-answer means

If the holder answers *"I don't know, I'd have to look"* — that is the **expected and correct** answer to
Q1, Q2, Q4, Q7, Q8 and Q10, because these are fields nobody records in a lab notebook. **They are read off
a file header, not recalled.** If the answer is *"the originals are gone"*, the honest record is
`FILES NOT RETAINED` — which is a fact about custody and, again, **not a fact about Purkinje cells**.

---

# 2 · RESOLUTION REALITY CHECK

## 2.1 The objects that have to be told apart

Four cell types occupy or border the Purkinje cell layer, and the marker-free route has to separate them on
shape and position alone.

🔴 **Provenance of every dimension below.** Only the first row is repository-attested. The rest are
`PREMISE: DEFAULT_FROM_TEXTBOOK` — standard cerebellar morphometry, **not retrieved in this act**, and
recorded as approximate ranges so a later reader can sharpen or overturn them rather than inherit them.
`RJ-5` and `RJ-6` ([`purkinje_existing_material_experiment_20260922.md:527`](purkinje_existing_material_experiment_20260922.md))
already stand open on exactly these two gaps — mouse granule nuclear dimensions and Bergmann glial nuclear
morphometry — and this section does **not** close them; it shows what follows from the ranges.

| Cell | Soma diameter (approx.) | Nuclear diameter (approx.) | Provenance | Why it is in this table |
|---|---|---|---|---|
| **Purkinje** | ≈ **18–25 µm** | ≈ **10–12 µm**, euchromatic and pale, prominent nucleolus | 🟡 Nuclear side **repository-attested**: guinea-pig Purkinje nuclear volume **470.9 µm³** ⇒ equivalent sphere ≈ **9.7 µm** ([`purkinje_existing_material_experiment_20260922.md:180`](purkinje_existing_material_experiment_20260922.md), sibling-retrieved). Soma side `DEFAULT_FROM_TEXTBOOK` | The target |
| **Bergmann glia** | ≈ **8–10 µm** | ≈ **6–8 µm**, denser chromatin | 🔴 `DEFAULT_FROM_TEXTBOOK`; `RJ-6` records this as **UNMEASURED** in the repository | 🎯 **Interposed in the same monolayer.** The confound that decides the negative direction |
| **Basket cell** | ≈ **10–14 µm** | ≈ **7–9 µm** | 🔴 `DEFAULT_FROM_TEXTBOOK` | Somata sit in the **lower molecular layer**, and their **pericellular terminals invest the Purkinje soma**. And per Aldaz & Hussain they are among the **highest-WWOX** cerebellar subtypes (§ 0 row 1) ⇒ a marker-free layer read measures a mixture whose **WWOX-brightest member may be the one that is not a Purkinje cell** |
| **Granule** | ≈ **5–7 µm** | ≈ **5–6 µm**, intensely heterochromatic | 🔴 `DEFAULT_FROM_TEXTBOOK`; `RJ-5` open | The internal comparator, in the same field, in the same section |

## 2.2 The discrimination each pixel size has to support

Three different tasks, three different requirements. Collapsing them is how *"is it enough?"* stays a guess.

| Task | What must be resolved | Sampling rule applied | ⇒ Requirement |
|---|---|---|---|
| **T1 · Layer segmentation** — find the Purkinje row as the single row between a nuclear-dense band and a nuclear-sparse band | A **texture contrast** between bands, not individual nuclei | ≈ 2–3 px across the smallest nucleus (≈5 µm) suffices to make the granular layer read as dense | **≤ ~2 µm/px** |
| **T2 · Soma masking** — draw a WWOX-independent boundary around one candidate soma and measure mean intensity inside it | A **≈10 µm nucleus** (or ≈20 µm soma) with a boundary accurate enough that the mask is not dominated by edge pixels | ≥ 8–10 px across the object being masked; at 10 µm that is 1.0–1.25 µm/px, and mask-edge error at that sampling is already ≈10% of the radius | **≤ ~1.0 µm/px**, and **≤0.5 µm/px** before the mask is trustworthy |
| **T3 · Identity discrimination** — separate a Purkinje nucleus (≈10–12 µm, pale) from a Bergmann-glia nucleus (≈6–8 µm, dense) **at the same position** | A **~1.5× diameter ratio** and a **chromatin-texture difference** — two anti-correlated features whose conjunction is strictly stronger than either | A 1.5× area-based separation needs the *smaller* object sampled well enough that its area estimate is not quantisation-limited: ≥ 12–15 px across ≈7 µm. Texture needs sub-nuclear structure: ≥ 3–4 px across a nucleolus or chromatin clump (≈1–2 µm) | **≤ ~0.5 µm/px** for size; **≤ ~0.25–0.3 µm/px** before texture contributes anything |

## 2.3 What whole-slide scanners actually deliver

`PREMISE: DEFAULT_FROM_TEXTBOOK` — instrument-class typicals, **not** a specification of any file in this
programme, and explicitly **not** attributed to the 3DHISTECH scanner, for which the repository holds no
specification at all (§ 0 row 3).

| Scan profile | Typical pixel size | Typical NA | T1 layer | T2 soma mask | T3 identity |
|---|---|---|---|---|---|
| **40×** | ≈ **0.25 µm/px** | ≈ 0.95 | 🟢 | 🟢 | 🟢 |
| **20×** | ≈ **0.5 µm/px** (0.45–0.50) | ≈ 0.75–0.80 | 🟢 | 🟢 | 🟡 **size yes, texture marginal** |
| **10× survey** | ≈ **1.0 µm/px** | ≈ 0.3–0.45 | 🟢 | 🟡 **marginal** | 🔴 **no** |
| **5× / overview** | ≈ **2 µm/px** | ≈ 0.15 | 🟡 | 🔴 | 🔴 |
| **Thumbnail / slide-label overview** | **4–15 µm/px** | — | 🔴 | 🔴 | 🔴 |
| **20× scan exported at 2× downsample** | ≈ **1.0 µm/px** | (as scanned) | 🟢 | 🟡 | 🔴 |
| **20× scan exported at 4× downsample** | ≈ **2 µm/px** | (as scanned) | 🟡 | 🔴 | 🔴 |

🎯 **The last two rows are why Q5 and Q6 are in Group B rather than as a footnote.** A scan acquired at a
sufficient pixel size and saved as a downsampled export has **already lost** the thing being asked about, and
the loss is invisible unless someone reads the header.

## 2.4 🎯 THE THRESHOLD, in one number the holder can check against one field

> ## **≤ 0.5 µm per pixel.**
>
> **≤ 1.0 µm/px** is the absolute floor — below it the layer is findable and a Purkinje soma is **not
> separable from a Bergmann-glia soma**, so the marker-free route returns *"signal at the layer"*, which is
> exactly the limitation that already bounds the field's only human Purkinje-layer observation.
> **≤ 0.5 µm/px** (≈20×) is the working requirement: size-based T3 discrimination becomes available.
> **≤ 0.25 µm/px** (≈40×) is comfortable: chromatin texture and the nucleolus become usable, and the two
> anti-correlated features (large **and** pale) can be conjoined.

**Read Q2's answer against that number and the question is decided.** Not *"is a panoramic scan enough?"* —
**"is `MICROMETER_PER_PIXEL_X` ≤ 0.5?"**

⚠️ **And the threshold is necessary, not sufficient.** A file at 0.25 µm/px with **no DNA channel** (Q8) is
still unusable for this route, because segmentation would have to fall back on the WWOX channel — the
circularity bar, which makes an untransduced cell **invisible by construction**
([`purkinje_existing_material_experiment_20260922.md:371`](purkinje_existing_material_experiment_20260922.md)).

## 2.5 🎯 Why NA is the wrong question to lead with — and it inverts the intuition

Diffraction-limited lateral resolution is ≈ `0.61 λ / NA`. At λ ≈ 520 nm:

| NA | Lateral resolution | Enough to separate two ≈7 µm nuclei? |
|---|---|---|
| 0.30 | ≈ 1.06 µm | 🟢 yes, by a factor of ~7 |
| 0.75 | ≈ 0.42 µm | 🟢 yes, by a factor of ~17 |
| 0.95 | ≈ 0.33 µm | 🟢 yes |

⇒ **Every realistic whole-slide NA resolves these objects laterally with an order of magnitude to spare.
The binding constraint is PIXEL SAMPLING, not optics.** A scanner can carry an NA that resolves a 0.4 µm
feature and save a file at 2 µm/px, and the file is then limited by the save, not by the lens.

🔴 **Where NA *does* bite, and it runs the opposite way to the reflex.** Higher NA ⇒ **shallower** depth of
field. In a **widefield** whole-slide scan of a **14 µm** section, a high-NA objective has a DOF of ~1 µm and
collects out-of-focus light from the remaining ~13 µm; a low-NA objective has a DOF approaching the section
thickness and integrates through it. Neither is "correct" — they are **different biases**, and which one
applies changes how the mean-intensity rule must be applied. That is why **Q4 (single plane vs z-stack)**
matters more than Q3, and why the 2021 **confocal** material is optically the better archive for this
question even though 2026 is better for age range and dose
([`purkinje_cheapest_path_and_community_followup_20260922.md:156`](purkinje_cheapest_path_and_community_followup_20260922.md)).

## 2.6 🔴 The trap the threshold does not remove

Even at 0.25 µm/px with a DNA channel and confocal optics, **resolution buys LOCATION and does not buy
IDENTITY.** Jurk *et al.* use exactly the three morphological criteria this section quantifies — *"their
specific location next to the granular layer in the cerebellum, their large size, low nuclear DNA density"*
— and then add **"and positivity for calbindin"** as a **fourth, concurrent** criterion (SIBLING-ATTESTED,
[`purkinje_existing_material_experiment_20260922.md:183`](purkinje_existing_material_experiment_20260922.md)).
🎯 **Every retrieved study that names Purkinje cells in fluorescence adds a marker. None substitutes
morphology for one.** The µm/pixel threshold decides whether the images can be *asked* the question; § 4
decides what the answer can mean.

---

# 3 · THE THREE THINGS THAT MUST NOT COLLAPSE

## 3.1 The separation, stated before any design

| | Question | What it means | Assay that answers it | Assay that does **not** |
|---|---|---|---|---|
| **① VECTOR ARRIVAL** | Did the vector **genome or reporter** reach this cell? | A physical-delivery fact about **this soma**. In a cell type that is post-mitotic before birth it is also a **stable** fact, because there is no mitotic dilution after P0 | **Native reporter** in the same cell (EGFP), or **vector-genome ISH** against the human transcript / `WPRE` / `bGH` elements, or single-nucleus vDNA after capture | 🔴 **A WWOX stain.** Absence of protein is compatible with arrival. 🔴 **Bulk vDNA** — arithmetically mute: Purkinje cells are **0.36% (rat) to 0.026% (human)** of cerebellar cortical neurons, so their total absence moves a whole-cerebellum number by **≲0.4%**, against a measured **8.75–12.05×** deficit ([`purkinje_cheapest_path_and_community_followup_20260922.md:290`](purkinje_cheapest_path_and_community_followup_20260922.md)). ⚠️ Clean **for the nucleus-denominated DNA assay only**; for protein and RNA the dilution is `UNMEASURED` (`RC-6`) and no number is stated here |
| **② WWOX EXPRESSION** | Is WWOX **protein present** in this cell, and how much? | Collapses **arrival × transcription × translation × stability** into one steady-state per-cell number | **Per-cell WWOX immunofluorescence intensity**, inside a WWOX-independent mask, reported as a **distribution** and a **positive fraction**, **separately** | 🔴 **A reporter.** An **IRES** second cistron is not expressed at the first cistron's level, so EGFP intensity is a **presence** channel, **never** a proxy for WWOX amount ([`purkinje_cheapest_path_and_community_followup_20260922.md:236`](purkinje_cheapest_path_and_community_followup_20260922.md)). 🔴 **A homogenate** — granule-cell-dominated by construction |
| **③ FUNCTION** | Does this cell **work** — fire correctly, receive climbing-fibre input correctly, support motor coordination? | An entirely separate measurement class | Purkinje-resolved physiology (PF-PC EPSC, complex-spike waveform, CF mono-innervation, PC intrinsic excitability), or a **cerebellum-localising** behavioural readout (interlimb kinematics, delay eyeblink conditioning) | 🔴 **Everything in ① and ②.** A stain establishing expression does not establish functional rescue |

## 3.2 🔴 The two implications, stated because the temptation is structural

**A reporter showing arrival does not establish expression.** ① → ② is not entailment: a genome can arrive,
integrate episomally and transcribe poorly, or transcribe and not translate, or translate and be degraded.
The repository records **TRANSLATION** and **PROTEIN STABILITY** as `NOT ASSAYED by anyone, anywhere, in any
WWOX paper`, and **not separable from each other**, because a steady-state per-cell amount is their
**product** ([`cerebellum_layer_localisation_20260922.md:82`](cerebellum_layer_localisation_20260922.md) layers 4–5).

**A stain establishing expression does not establish functional rescue.** ② → ③ is not entailment, and in
**this gene** the repository holds the sharpest available warning against assuming it: in
`Wwox^P47T/P47T`, **total protein is normal and Purkinje cells are lost anyway**
([`cerebellar_discrimination_experiments_20260922.md` § 4.0](cerebellar_discrimination_experiments_20260922.md)).
🔴 **That statement is carried in its one permitted form and is not widened** — *for at least one WWOX missense
model, normal total protein abundance is insufficient to preserve Purkinje cells* — with its four firewalls
intact: **allele** (`P47T` ≠ null), **mechanism**, **species/system**, and **number versus function**. It is
**not** evidence that abundance rescue never works, and nothing about the null is inferred from it.

🎯 **The named failure mode.** If the § 4 design returns *vector present, WWOX present*, the correct
conclusion is **"delivery and expression are not the limiting variable for this cell type."** The incorrect
conclusion — the one an expression assay invites precisely because this outcome looks like good news — is
*"Purkinje cells are rescued."* And the converse trap, which protects the premise: **a WWOX-negative Purkinje
cell is not a functional deficit either.** It is an expression observation whose functional consequence is
unmeasured in every WWOX system.

## 3.3 🔴 THE CEREBELLAR FUNCTIONAL VOID — named explicitly, because the repository records it

The repository's functional census makes this a **documented absence**, not a gap I am asserting. Every row
is SIBLING-ATTESTED from [`cerebellar_functional_readout_census_20260922.md`](cerebellar_functional_readout_census_20260922.md),
which keeps each model in its own row and pools none of them.

| Instrument that exists | What it records | Why it cannot see the cerebellum |
|---|---|---|
| 2021 **cell-attached recordings** (`R7`) | *"1.6–2 mm posterior to the bregma and 4 mm lateral to the midline"*, depth 300 µm; legend *"spontaneous **neocortical** activity"* | 🔴 **Neocortex by stated coordinates.** No cerebellar physiology exists in the paper |
| 2026 **ECoG** (`R12`) | Single channel, *"the recording electrode was positioned above the **right dorsal cortex**"* | 🔴 **No cerebellar electrode** |
| `Wwox^P47T/P47T` **video-EEG** (`R16`) | Silver wires *"implanted bilaterally into the subdural space over **frontal and parietal cortex**"* | 🔴 **No cerebellar electrode.** 🔴 Different allele — listed, never pooled |
| **Synapsin-Cre × `Wwox^fl/fl` acute slice** (`R6`) — the corpus's only slice electrophysiology | Neocortex L2/3 and L5, hippocampus CA1/CA3 | 🔴 **Mechanically excluded:** *"The cerebellum and olfactory bulbs were removed"*. Cerebellum is `NOT TESTED, BY PROTOCOL` |
| 2026 **"ataxia score"** (`R10`) | LD partial, HD *"near-complete rescue"* | 🔴 **The label is cerebellar; the instrument is a hindlimb clasping test**, routinely positive in corticospinal, basal-ganglia and diffuse neurodegenerative models ([`cerebellum_layer_localisation_20260922.md:300`](cerebellum_layer_localisation_20260922.md) § 3.6) |
| 2026 **rotarod at 3 months** (`R11`) | HD only, comparator WT+RI | ⚠️ Reads ***supra*-WT** — *"significantly higher motor coordination and learning compared with WT mice"* — an uninterpretable comparator that cannot bear weight in either direction |
| **SCAR12 / WOREE human** (`H3`, `H9`) | — | 🔴 **SARA · ICARS · BARS · posturography · quantitative oculomotor · eyeblink conditioning: zero, all six, both cohorts.** In WOREE, *"None achieved independent walking"* (13/13), which the census records as **structurally untestable**, not merely untested |

> 🎯 ⇒ **No cerebellum-localising functional endpoint exists anywhere in this corpus, in any model, in any
> species.** ③ is therefore not merely a separate question from ① and ② — **it is a question no existing
> instrument in this programme can ask**, and nothing below L3 reaches it.

---

# 4 · THE SMALLEST STORED-SECTION EXPERIMENT

## 4.1 🔁 What is already specified, and is credited rather than re-proposed

The compressed three-channel stain — **Hoechst 33258 · mouse anti-calbindin-D28k → goat anti-mouse AF488 ·
the laboratory's existing rabbit anti-WWOX 1:5,000 → goat anti-rabbit AF647** — is **fully specified by a
sibling**, with its reagent attestations (`CB-955`, `McAb 300`, Sigma `C9848` on deparaffinised FFPE
alongside Hoechst 33258), its circularity bar, its mean-not-integrated rule, its widefield half-mask rule and
its per-layer reporting
([`purkinje_existing_material_experiment_20260922.md:392`](purkinje_existing_material_experiment_20260922.md) § 4,
reagents at `:415`, traps at `:369`; carried as `F2` at
[`cerebellar_discrimination_experiments_20260922.md:522`](cerebellar_discrimination_experiments_20260922.md),
as `C4` at [`purkinje_cheapest_path_and_community_followup_20260922.md:335`](purkinje_cheapest_path_and_community_followup_20260922.md),
and as `P4` at [`tx007_purkinje_frontier_20260922.md:330`](tx007_purkinje_frontier_20260922.md)).

🟢 **That design is correct, it is the right experiment, and this section does not compete with it.** I call
it **SECTION A** and add only what is missing.

Also already held and not re-derived: the **host-discipline constraint** (a *rabbit* anti-calbindin such as
`AB1778` would collide with anti-WWOX and must not be ordered for that stain —
[`purkinje_existing_material_experiment_20260922.md:434`](purkinje_existing_material_experiment_20260922.md));
the **NeuN/calbindin mouse-slot collision**, which means Section A **cannot cross-calibrate against the ≈61%
NeuN-gated figure on the same section** and the bridge is a **third measurement** to be planned rather than
discovered at the bench ([`purkinje_existing_material_experiment_20260922.md:601`](purkinje_existing_material_experiment_20260922.md) V2);
and the **ISH second pass** (`J3`) as the one thing that fully separates arrival from a sub-threshold
expression, on the same section, with zero endogenous background because the transgene is human in a mouse
host.

## 4.2 🆕 The channel arithmetic that has not been written down — and it forces the design

Under the hard 3-channel ceiling, with **exactly two secondaries** (one anti-rabbit @647, one anti-mouse @488)
plus a DNA channel, write out what each of the four signals costs:

| Signal | Host / nature | Channel it must occupy |
|---|---|---|
| **Nuclear mask** | Hoechst / DAPI | the DNA channel |
| **Purkinje identity** (calbindin-D28k) | mouse monoclonal → AF488 **or** rabbit polyclonal → AF647 | **either** green **or** far-red, depending on host chosen |
| **WWOX expression** | rabbit polyclonal (the laboratory's own) → AF647 | **far-red only** |
| **Vector arrival** (native EGFP) | not an antibody at all | **green only** |

> ## 🔴 **THE RESULT: arrival, expression and identity CANNOT coexist on one three-channel section. Ever, under this reagent set.**
>
> WWOX is locked to far-red. EGFP is locked to green. Identity is the only signal with a free choice of
> host — and whichever slot it takes, it **evicts** one of the other two. Three signals, two non-nuclear
> channels. **The design is not a preference among good options; it is a forced choice between two pairs.**

This is why the sibling's cut of the vector channel was correct and is **not** a shortcoming to be repaired
by better channel bookkeeping. It is arithmetic.

## 4.3 🆕 The minimal design: TWO serial sections, each three channels

> ### 🥇 **SECTION A — IDENTITY × EXPRESSION** *(the sibling's design, credited, unchanged)*
> **Hoechst 33258 · mouse anti-calbindin-D28k → goat anti-mouse AF488 · rabbit anti-WWOX 1:5,000 → goat
> anti-rabbit AF647.** Segment on Hoechst. Report, per cerebellar layer, the per-cell WWOX **mean**-intensity
> **distribution** and the positive **fraction** as two separate quantities, plus calbindin⁺ Purkinje
> **counts** per genotype and arm.
> **Cost:** one new primary, **no new secondary**, no new animal.

> ### 🆕 **SECTION B — IDENTITY × ARRIVAL** *(new here: the reagent Section A forbids is the reagent Section B requires)*
> On a **serial neighbour** from the **2021 `AAV9-hSynI-EGFP` control arm**:
> **nuclear counterstain · native EGFP (green, uncontested — no antibody) · rabbit anti-calbindin-D28k
> (e.g. `AB1778`) → goat anti-rabbit AF647.**
> **Cost:** one new primary, **no new secondary** (the anti-rabbit AF647 already exists), no new animal.
>
> 🎯 **The point.** On Section A the far-red slot is WWOX, so calbindin must be **mouse** and a rabbit
> calbindin is **prohibited**. On Section B there is no anti-WWOX antibody at all, the far-red slot is free,
> and **the prohibited reagent becomes the mandatory one** — because the green slot must be left empty for
> native EGFP. 🟢 The control arm is the one material in the whole problem with **no channel contention of any
> kind**: it needs no antibody for its arrival signal ([`purkinje_cheapest_path_and_community_followup_20260922.md:234`](purkinje_cheapest_path_and_community_followup_20260922.md)).

## 4.4 🔴 The bounds Section B carries, and they are severe

1. **Dose.** The 2021 reporter is `2E10`/hemisphere. **It answers at that dose and transfers to no other.**
   TX-007 is `1.23E11`/`2.63E11` — 5–13× higher.
2. **Archive.** 2021 and 2026 are **different studies, different vectors, different injection technique**
   (free-hand ~1 µL 33G vs stereotactic 2.0 µL 32G). 🔴 **No 2021↔2026 transfer in either direction**, and no
   number is differenced across them.
3. **Fluorophore persistence.** Whether native EGFP survived in a years-old archive is `NOT ATTESTED`.
   2% PFA is a mild fixative and therefore favourable, and the reporter was imaged successfully at the time
   ([`purkinje_cheapest_path_and_community_followup_20260922.md:428`](purkinje_cheapest_path_and_community_followup_20260922.md)).
4. **2026 has no reporter section at all** — its `AAV9-hSynI-EGFP` is used **in vitro only**, in dissociated
   E13.5 DRG cultures.

> 🔴 ⇒ **At the therapeutic dose, VECTOR ARRIVAL is unreachable on existing material by ANY channel
> arrangement.** Not because a channel is missing — because **no reporter animal at that dose was ever
> sectioned**. Section B answers ① at `2E10`; nothing existing answers ① at `1.23E11` or `2.63E11`. That is
> an honest hard stop, and it is the strongest argument for the `J3` ISH second pass, which reads arrival
> **on the therapeutic sections themselves** through the vector's own human-transcript / `WPRE` / `bGH`
> elements.

## 4.5 Channel-by-channel justification — which outcome pair does each one own?

Outcomes, as the prior wave defines them: **A** vector absent from Purkinje cells · **B** vector present,
WWOX output poor · **C** vector present, WWOX present. Plus the structural null: **"this object is not a
Purkinje cell."**

| Channel | Section | 🎯 Pair it separates | Is that pair reachable more cheaply? | Verdict |
|---|---|---|---|---|
| **Nuclear / landmark** (Hoechst; or the NeuN-bright/NeuN-dark bands where no counterstain exists) | A and B | 🎯 **A from "nothing here."** It supplies the **WWOX-independent soma mask**, hence an honest **denominator**, hence the ability to observe an *untransduced* cell at all; and the section-plane control that makes mean intensity comparable between a truncated large soma and an intact small one | 🔴 **No.** Without it segmentation falls back on the signal under test and **outcome A becomes unobservable by construction** | 🟢 **KEEP. Non-negotiable** |
| **Purkinje identity** (calbindin-D28k — mouse on A, rabbit on B) | A and B | 🎯 **The Purkinje cell from everything else at the same position** — the Bergmann-glia and basket confound of § 2.1. It converts *"signal at the layer"* into *"signal in the cell"*, and it is what § 2.6 shows morphology alone never delivers | 🔴 **No.** Morphology reaches the row and stops there, even at 0.25 µm/px. 🎯 And it is a **free co-product generator**: calbindin⁺ Purkinje counts per arm fall out of the same image | 🟢 **KEEP. This is the channel the whole question is about** |
| **WWOX** (rabbit → AF647) | A | 🎯 **B from C** — poor output from adequate output, as a per-cell **distribution** and a **positive fraction**, reported separately | 🔴 **No.** Nothing else in the programme measures WWOX protein at cellular resolution | 🟢 **KEEP** |
| **Vector arrival** (native EGFP) | B | 🎯 **A from B** *directly*, by observation rather than inference | 🟡 **Partly, and only in the 2021 archive at `2E10`** (§ 4.4). 🔴 **Not at all at LD/HD** | 🟢 **KEEP — but on its own section, at its own dose, claimed as exactly that.** 🔴 **Cut from Section A**, where it would evict either identity or expression |
| ✂️ **NeuN (`MAB377`)** | — | Nothing this design needs | Occupies the mouse slot calbindin requires, and in murine cerebellum labels **essentially granule neurons only** — the population we are trying to look past | 🔴 **CUT** |
| ✂️ **βIII-tubulin** | — | Nothing | Pan-neuronal; in cerebellar cortex it separates nothing. Also mouse, so it is not an escape route from the slot collision | 🔴 **CUT** |
| ✂️ **Glial marker (GFAP / Iba1 / MBP)** | — | Would address the non-cell-autonomous class (`C5`) | 🔴 All three are **rabbit** ⇒ they collide with anti-WWOX. A WWOX section can carry **no** glial or myelin marker, by construction | 🔴 **CUT**, and the cut is a reagent fact, not a choice |

## 4.6 🔴 THE BLIND SPOTS THE CUTS CREATE — stated, not buried

**① On Section A alone, A and B are distinguishable only by inference.** In a `Wwox`-null host any WWOX
signal is necessarily transgene-derived, so **WWOX-positive ⇒ vector reached that cell**, and **outcome C is
directly observed**. The blind spot is entirely on the negative side: **a WWOX-negative Purkinje cell is
uninterpretable between A and B** — a cell the vector never reached, or a cell the vector reached whose
cassette produced protein below the detection floor. Those are **opposite therapeutic conclusions** — change
the capsid, or change the cassette — and Section A cannot tell them apart.

**② The two sections do not co-register at the cell level.** Serial 14 µm neighbours are ~14 µm apart; a
Purkinje soma is ≈18–25 µm, so a given soma *may* appear in both and **cannot be relied on to**. ⇒ **The A/B
pairing is valid at the POPULATION level, per layer, per arm — never as "this same soma was reached and
expresses."** Claiming otherwise would be the single easiest error to make with this design.

**③ Section B's answer is at `2E10` and Section A's is at LD/HD.** 🔴 **The two are on different doses and
different archives, and the pairing must therefore be reported as two results, not one.** Anyone tempted to
difference them is doing the 2021↔2026 transfer that every file in this wave forbids.

**④ Translation is not separable from protein stability.** A steady-state per-cell amount is their product,
and no single-section design factors a product.

**⑤ The intensity axis is relative, never absolute.** The anti-WWOX polyclonal has **no vendor, no catalogue
number and no clone**. The design is deliberately built to need only a **within-field** Purkinje-vs-granule
contrast — same section, same animal, same antibody lot, same exposure, same threshold — which is a design
choice, not a solution.

🎯 **Three honest mitigations for ①, none of which is a substitute for a fourth channel.**
(i) **The distribution, not the mean, carries the information** — a bimodal per-cell WWOX distribution in the
Purkinje population argues for a reached/not-reached mixture (A-flavoured); a unimodal low-shifted
distribution argues for uniform poor output (B-flavoured). 🔴 **This is suggestive geometry, not a
discriminator, and must not be reported as one.**
(ii) **Section B answers the A-side question separately**, in different material, at a different dose.
(iii) **The `J3` ISH pass** is the only thing that closes ① on the therapeutic sections themselves — and the
first pass must therefore be designed **not to consume the section that would carry it**.

⇒ 🎯 **The blind spots are accepted deliberately**, on the argument that **outcome C — the outcome that would
redirect the whole programme away from delivery — is the one Section A observes *directly***, and that
A-versus-B at therapeutic dose is a second-round question requiring either the ISH pass or a new cohort.
**That reasoning is stated so a later reader can overturn it rather than inherit it.**

## 4.7 The rules that travel with any execution, carried unchanged

1. 🔴 **Segment on the nuclear/landmark channel, never on WWOX.**
2. 🔴 **Mean intensity inside the mask, never integrated** — 14 µm is thinner than a Purkinje soma, so
   integrated signal penalises exactly the cell type of interest and would **manufacture a spurious deficit**.
3. 🔴 **Where the optics are widefield, report the molecular-facing half-mask, or both halves separately** —
   out-of-focus bleed from the dense granular layer is **anisotropic**. The 2021 confocal material does not
   carry this trap.
4. 🔴 **Positive fraction and intensity distribution are reported SEPARATELY, never collapsed.** `V ≈ F × C`:
   positivity is a threshold measure, load is a quantity.
5. 🔴 **`NOT ASSAYED` is neither `NORMAL` nor `ABSENT`.** A dark Purkinje soma is a **detection-floor**
   statement, and the floor's height is set by a segmentation threshold the papers never state.

---

# 5 · THE LADDER

**L0** reanalysis / metadata · **L1** stored-material analysis · **L2** new stain on existing material ·
**L3** new animal. Every rung from L0 to L2 is **NEW ANIMALS: NO**.

| # | Rung | Level | New animals? | Information gain | Status |
|---|---|---|---|---|---|
| **α** | 🆕 **The custody read of § 1** — thirteen header and folder questions | **L0**, and **below every rung anyone has costed**: it is a *metadata* read, not an analysis | 🟢 NO | 🎯 **It answers no biological question at all. It decides whether L0-reanalysis and L1 exist as routes.** Cheapest act in the problem and **strictly prior** to α′ and δ | 🆕 **NEW HERE.** 🔴 `HOLDER-ONLY` — these fields are in no paper, so no retrieval substitutes |
| **α′** | **Inspect the published 2021 panels** — Fig 2F (cerebellum, P19, 50 µm bar) and Fig 4A (whole-brain sagittal) at measured effective ppi | **L0** | 🟢 NO | The only rung executable by a reader **holding nothing**; decides whether the Purkinje monolayer is in frame at all | 🔁 **CARRIED** — `C3`/`P3`, specified and **never climbed** (egress-blocked in this deployment). **Not re-proposed** |
| **γ** | **Spatial-pattern read** of existing scans — parasagittal banding vs pial-inward gradient | **L0/L1** | 🟢 NO | Discriminates a circuit-topographic cause from a delivery-gradient cause, and 🎯 **needs no cell identity**, so it survives every § 1 unknown **except pixel size** | 🔁 **CARRIED** — `C8`/`F3`. Noted, not re-proposed |
| **δ** | Marker-free **layer-resolved** WWOX re-quantification of existing scans | **L1** | 🟢 NO | 🟡 **Downgraded.** Conditional on Q2 **and** Q8 **and** Q12 simultaneously; and even on success it reproduces the known Bergmann/basket confound (§ 2.6) — i.e. it re-derives, at mouse resolution, the known limit of the field's only existing Purkinje-layer datum | 🔁 **CARRIED** — `J2`/`F3`/`C7`. 🔴 **α before δ** is the one ordering this file insists on |
| **δ′** | 🆕 **Read the DNA-yield-per-mg-of-tissue record, by region**, off the laboratory's own extraction sheets | **L0** | 🟢 NO | Not the Purkinje question — but it is the **only cheap handle** on the differential-nuclear-recovery composition bias that a host-reference amplicon is **structurally blind to** | 🔁 Substance carried at [`cerebellar_discrimination_experiments_20260922.md` § 2.4](cerebellar_discrimination_experiments_20260922.md); listed here only to keep the ladder complete |
| **ε** | **SECTION B** — 2021 `AAV9-hSynI-EGFP` control-arm cerebellar fields: nuclear · native EGFP · **rabbit** anti-calbindin → AF647 | **L1** if suitable scans exist; **L2** if a re-cut and one new primary are needed | 🟢 NO | 🎯 Answers **① VECTOR ARRIVAL with cell identity**, baseline-free (GFP has no endogenous counterpart), at `2E10`. 🔴 Transfers to no other dose | 🆕 **The channel pairing and the rabbit-calbindin inversion are new here.** The reporter asset itself is a sibling's finding and is **credited, not re-claimed** |
| **ζ** | **SECTION A** — Hoechst · mouse calbindin · WWOX; per-layer distributions + positive fraction + calbindin⁺ counts | **L2** — one new primary, inheriting the existing anti-mouse secondary | 🟢 NO | 🎯 **The highest-information act available without a new animal**, and the only one whose outcome is unpredicted in several directions. **Observes C directly; blind between A and B on the negative side** | 🔁 **CARRIED — `J1`/`F2`/`C4`/`P4`, not claimed here.** This file adds the § 4.5 pair-justification and the § 4.6 blind-spot statement |
| **η** | **WWOX channel added to the `Wwox^P47T/P47T` laboratory's existing calbindin vermis sections** (80 d / 250 d, published `ns` basket-cell control) | **L2** | 🟢 NO | Converts a **cell count** into a **protein measurement** in the exact cell type, in the one model carrying an internal interneuron specificity control | 🔁 **CARRIED** — `F6`. 🔴 **Different allele, different model — never pooled with null-line material** |
| **θ** | **ISH second pass** — human-transcript / `WPRE` / `bGH` probe combined with calbindin + WWOX IF on the **same** therapeutic section | **L2**, different chemistry | 🟢 NO | 🎯 **The only thing that separates A from a sub-threshold B at the therapeutic dose**, with zero endogenous background because the transgene is human in a mouse host | 🔁 **CARRIED** — `J3`. Named here because § 4.4 makes it the **named successor** to the blind spot, not an optional extra |
| **ι** | **Reporter cohort at `1.23E11` / `2.63E11`**, injected, perfused, sectioned | **L3** | 🔴 **YES** | The only route to ① at the therapeutic dose if θ is unavailable. ⚠️ And the mouse secondary must move to AF568/594, because EGFP collides with the existing AF488 — **stated up front, not discovered at the bench** | 🔁 **CARRIED** — `J4`, narrowed by `C1` |
| **κ** | **Purkinje-restricted conditional** (`Pcp2`/`L7`-Cre × `Wwox^fl/fl`) | **L3** | 🔴 YES | The only design that tests **necessity** rather than presence; the floxed allele exists and its own makers named this cross in print | 🔁 **CARRIED** — `F7` |
| **λ** | **Cerebellum-localising FUNCTIONAL readout** (§ 3.3) | **L3** | 🔴 YES | 🎯 **The only route to ③.** Nothing below L3 reaches it — the census shows every existing instrument is cortical, composite or mechanically cerebellum-excluding | 🔁 Carried by the functional census. **Correctly out of scope for a stored-section design** |

## 5.1 🎯 Where a lower rung is preferred, and where it is NOT

**Prefer lower:** **α before everything** — it costs minutes and decides whether γ and δ are routes at all;
**α′ before δ**, because a published panel is outside the holding laboratory by construction and δ is not;
**γ before δ**, because γ survives the Q8 unknown that δ does not.

🔴 **Do NOT prefer lower here:** **δ must not delay ζ.** δ is cheaper, but its information gain is **not
comparable** — on success it returns a layer-resolved distribution over a **mixture** (Purkinje + Bergmann
glia + basket terminals), which is the exact limitation that already bounds the only existing human
Purkinje-layer observation. Spending the cheapest rung to re-derive a known limit is a poor trade. ζ answers
a question no measurement in any species has answered.

🔴 **And ε must not be mistaken for a cheaper ζ.** It answers a **different one of the three things** (① not
②), in a **different archive**, at a **different dose**.

## 5.2 The ladder's structural lesson, restated

**The binding constraint on this question is not animals and not money — it is custody.** α, γ, δ, δ′, ε, ζ
and θ are all `HOLDER-ONLY`, because *"Data and code availability: Not relevant."* means there is no
deposited file and no repository to query. **α′ is the only rung outside the holding laboratory by
construction, and it is the one that was specified and never climbed.**

---

# 6 · THE HONEST OUTCOME

> ## 🎯 **For everything that depends on the existing IMAGES, this reduces to one custody read and nothing else can be done here.**
>
> Three metadata facts are required **simultaneously** — a nuclear channel actually acquired (Q8), a pixel
> size ≤ 0.5 µm/px surviving into the saved file (Q2, Q5, Q6), and cerebellar coverage in an arm of interest
> (Q12) — **none is in either paper**, and none is answerable by any amount of better retrieval. They are
> answerable by opening a file header, which requires the holder.
>
> 🟢 **But the reduction is not total, and that is the second result.** One thing does **not** depend on the
> images: **§ 4's stored-section design**, which is gated by **Q13 (block retention)** alone. If the FFPE
> blocks survive, Section A is executable whatever Q1–Q12 return — and it answers the question the images
> cannot answer **at any pixel size**, because resolution buys location and only a marker buys identity.

## 6.1 What I could NOT establish, and what would reopen it

| # | Recorded state | What would reopen it |
|---|---|---|
| **B-1** | 🔴 **Whether any whole-slide scan captured a nuclear channel** — `NOT STATED` (`RJ-7`); one of **three** simultaneous requirements | A scanner channel-profile statement, or any cerebellar panel showing a DNA channel |
| **B-2** | 🔴 **The objective, NA, magnification and pixel size of every image asset in the programme** — no specification is attached to the 3DHISTECH scanner in any repository artefact | Any acquisition-settings statement; or one image file's own header |
| **B-3** | 🆕 🔴 **Whether the saved files are original scanner format or exported derivatives, and at what downsample and bit depth** — never asked by any prior node, and it can cross the § 2.4 threshold **by itself** | A folder listing, or one file's extension and sidecar set |
| **B-4** | 🔴 **The mediolateral/sagittal level of every section series** — `NOT STATED` in both archives | Any sectioning-plane statement or block-orientation figure |
| **B-5** | 🔴 **Whether scans cover cerebellum in the `1.23E11` and `2.63E11` arms** — `R4`, narrowed to `PARTIALLY STATED`, silent for LD | Any per-panel arm assignment for S3, S5 or S8 |
| **B-6** | 🔴 **Whether native EGFP is separable from the anti-mouse AF488 secondary in the `mWwox-IRES-EGFP` arm** — `RC-2` | Appendix Table S1 (`FT-152`) |
| **B-7** | 🔴 **Whether native EGFP survived in the years-old 2021 archive** | Any re-imaging of a stored 2021 reporter slide |
| **B-8** | 🔴 **Mouse granule-cell nuclear dimensions** (`RJ-5`) and **Bergmann glial nuclear morphometry** (`RJ-6`) | Any stereological or morphometric source. 🎯 **These calibrate the § 2 threshold**: the T3 requirement is derived from ranges, and a measured Bergmann/Purkinje nuclear ratio would sharpen or loosen the 0.5 µm/px number |
| **B-9** | 🔴 **Purkinje share of cerebellar protein and RNA** — `UNMEASURED` (`RC-6`). The bulk-muteness argument is proven for **DNA only** and is not extended | Any measurement of Purkinje protein or RNA as a fraction of cerebellar total |
| **B-10** | ⚪ **The 2026 supplementary figure surface** — untestable on any route available in this deployment (egress-blocked, `files/` absent). **No external action was attempted** | A human with a browser, or a deployment with egress |

## 6.2 🔴 The premise, restated at the end exactly as at the start

**`PREMISE: NOBODY_LOOKED` stands unchanged.** Nobody has measured whether Purkinje cells are reached by the
vector, whether they express WWOX, or whether they function. **This file asserts nothing about any of the
three.** Every `UNKNOWN` above is a statement about a file header, a channel profile, a retention policy or
an instrument — never about a cell.

---

## Operating-mode record

**`DEFAULTS_TAKEN`** — cerebellar cell dimensions other than the repository-attested Purkinje nuclear volume
are `PREMISE: DEFAULT_FROM_TEXTBOOK`, stated as ranges, with `RJ-5`/`RJ-6` left open rather than closed by
assertion. Whole-slide scanner typicals in § 2.3 are instrument-class background, **explicitly not attributed
to the 3DHISTECH scanner**. No primary article was read in this act; every verbatim string is
**SIBLING-ATTESTED** with `file:line`.

**`DECISIONS_TAKEN`** — (i) Stated the threshold as **one number** (≤0.5 µm/px) with a floor (≤1.0) and a
comfort level (≤0.25), rather than a hedge, so a holder can check it against one header field; reversible if
B-8 closes. (ii) **Retired NA as the leading question** and said why, rather than listing it neutrally.
(iii) Built **two** sections rather than proposing a fourth channel, because § 4.2 shows a fourth channel is
not available under this reagent set. (iv) **Refused to pair Sections A and B at the cell level** or across
doses, though the pairing would have read more strongly.

**`STOP_LOG`** — class 1: 0 · class 2: 0 · class 3: 0. **No git command of any kind was run.** No registry,
`*_current.md`, queue, ledger, receipt or state-manifest file was read for modification or touched. No
`BATCH_COMMIT`. 🔴 **No email, no contact, no material request, no external action of any kind.** Exactly one
file was written: this one.

**Nothing here is medical advice.**

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

## V1 · 🎯 The channel arithmetic is CONFIRMED, and it converts a design choice into a constraint

Verified at source: exactly **two** secondaries exist programme-wide — *"goat anti-rabbit Alexa
fluor 647"*, *"goat anti-mouse Alexa fluor 488"* — plus *"Hoechst 33258"*
(`purkinje_existing_asset_ceiling_20260922.md:38`, tracing `purkinje_existing_material_experiment:244`).
And the anti-WWOX primary is **rabbit** (`HPA050992`, `wwox_antibody_epitope_census:399`).

So the slots are forced:

```
Hoechst        nuclear        free
AF488 (mouse)  one slot   ←── native EGFP also lands here (green)
AF647 (rabbit) one slot   ←── WWOX is rabbit, so it owns this
```

🔴 **Identity is the only signal with a free choice of host, and whichever slot calbindin takes it
evicts one of the other two. Therefore arrival, expression and identity cannot coexist on one
3-channel section — ever, under this reagent set.**

🎯 **This retro-justifies the earlier cut of the reporter channel as arithmetic, not oversight.** A
sibling cut that channel and stated its blind spot; this shows the cut was **forced**, not chosen.

**And the resolution is genuinely elegant:** *the reagent Section A forbids is the reagent Section B
requires.* Section A uses **mouse** anti-calbindin (AF488) beside rabbit-WWOX (AF647). Section B
drops the antibody entirely on the green side — **native EGFP, uncontested** — which frees the mouse
slot and lets calbindin move to **rabbit** (AF647). Two sections, no new secondary.

## V2 · 🟢 NA is the wrong question — the binding constraint is pixel sampling

Worth carrying beyond this file. At 520 nm, `0.61λ/NA` gives ≈1.06 µm even at NA 0.30, so **every
realistic whole-slide objective resolves these objects laterally with an order of magnitude to
spare.** The limit is how finely the image was **sampled**, not how well it was **resolved**.

| Task | Requirement |
|---|---|
| layer segmentation | ≤ 2 µm/px |
| soma masking | ≤ 1.0 (trustworthy ≤ 0.5) |
| Purkinje vs Bergmann identity | ≤ 0.5 for size; ≤ 0.25–0.3 before chromatin texture helps |

🔴 **The dangerous case, and the reason `Q2` is the decisive question:** a 20× scan exported at 2–4×
downsample lands at **1–2 µm/px and crosses the floor invisibly** — the file still looks like a 20×
scan. This is why the custody list asks for `MICROMETER_PER_PIXEL_X` **from the header**, not for
the objective from memory.

Consequence: `Q4` (single plane vs z-stack/extended focus) matters **more** than `Q3` (NA), because
NA bites only on depth of field in a 14 µm widefield section. The file asks Q3 *in order to retire
it*, which is the right use of a question.

## V3 · The hard stop is a MATERIAL limit, not a channel limit — and the distinction is load-bearing

🔴 At the **therapeutic** dose, vector arrival is unreachable on existing material by **any** channel
arrangement — not for want of a channel, but because **no reporter animal at that dose was ever
sectioned.** Section B answers at `2E10` and **does not transfer** to `1.23E11`/`2.63E11`.

That is a different class of limit from everything else in this file, and collapsing the two would
be the error. No amount of cleverness with three channels reaches it; only the named `J3` ISH pass
on the therapeutic sections does, and it is credited rather than re-proposed.

## V4 · The functional void, stated plainly

🔴 **No cerebellum-localising functional endpoint exists anywhere in this corpus.** Recordings
neocortical by stated coordinates; ECoG over right dorsal cortex; video-EEG frontal/parietal; the
one slice study removed the cerebellum outright; the "ataxia score" is a hindlimb clasping test;
rotarod reads supra-WT; and SARA/ICARS/BARS/posturography/oculomotor/eyeblink are **zero** in both
human cohorts.

**So `VECTOR ARRIVAL` / `WWOX EXPRESSION` / `FUNCTION` are not merely conceptually separate here —
the third has no instrument at all in this programme.** A stain that establishes expression could
not become a functional claim even if someone wished it to.

## V5 · Status

`Q2 ∧ Q8 ∧ Q12` must hold **simultaneously**; any one false collapses the marker-free route.
**`Q13` (raw files / blocks / unstained serial neighbours retained) is orthogonal and should be
asked first**, because it gates the stored-section design regardless of every image answer — and
that design answers, at any pixel size, the question the images cannot answer at all.

Absence of a specification in this repository is recorded throughout as a fact about **our records**,
never as a scientific negative. `PREMISE: NOBODY_LOOKED` intact at both ends.
LINT `PASS`, growth anchors `PASS`, `unread_premises 0`.
