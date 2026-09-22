# The existing-asset ceiling on the Purkinje question — a channel and metadata audit

**Actor:** Scientist B · **Date:** 2026-09-22 · **Axis:** what the *files that already exist* can be
made to say — not what a new experiment could say

**Scope and posture.** This is a constructive continuation of a programme that built, for its own
purposes, almost every asset this question needs. Nothing below is a criticism of the original work:
the 2021 study is an imaging and physiology study and the 2026 study is a dose-and-delivery study,
and neither was designed to answer a Purkinje question that nobody had yet asked. The contribution
here is narrow and deliberately unglamorous: **an asset-by-asset audit of channels and acquisition
metadata**, separating what is *in principle* resolvable from what is *actually* resolvable with the
files as the repository records them.

**PREMISE: `NOBODY_LOOKED` — carried intact.** Nothing in this file asserts, implies or scores that
Purkinje cells are poorly transduced, poorly reached or WWOX-low. Every statement of the form "this
is unknown" is a statement about the *measurement record*, not about the cell. The only claim made
here is that **no instrument yet applied could have seen a Purkinje cell**, and that this is a
property of reagents and channels, not of biology.

**Not medical advice.** No molecule, dose, route or clinical recommendation appears in this file.
Public edition: the reference genotype class only; no alleles or models are pooled — the `Wwox`-null
(Aqeilan-line) material, the `Wwox^P47T/P47T` knock-in material and the human tissue material are
kept in separate rows throughout, and no number crosses between them.

**Read-only.** No registry, `*_current.md`, ledger, receipt, state manifest or queue was read for
writing or modified. No external contact, no fetch, no git operation, no `BATCH_COMMIT`.

---

## 0 · Established at source before building — verification log

Six facts were handed to me as established. I verified each at the cited location before using it;
all six hold, and two of them turned out to be sharper than the summary I was given.

| # | Fact as handed over | Verified at | Verdict |
|---|---|---|---|
| 1 | The cerebellar transduced-fraction reagent is `MAB377` = clone A60, which excludes Purkinje cells from numerator **and** denominator | [`cerebellum_layer_localisation_20260922.md:573`](cerebellum_layer_localisation_20260922.md) §6.2; reagent text at `:280` | 🟢 **HOLDS.** Methods verbatim *"mouse anti-NeuN, (**MAB377**), Milipore, 1:500"*; A60's Purkinje-negativity attested at abstract depth from `PMID 17291468` |
| 2 | The blindness is **programme-wide**: three channels only, so WWOX's identity partners have only ever been NeuN and βIII-tubulin | [`purkinje_existing_material_experiment_20260922.md:239`](purkinje_existing_material_experiment_20260922.md) §2.3, secondaries at `:244` | 🟢 **HOLDS, and it is a secondary-antibody fact, not a filter choice.** Exactly two secondaries exist — *"goat anti-rabbit Alexa flour 647"*, *"goat anti-mouse Alexa flour 488"* — plus *"Hoechst 33258"*. Four rabbit primaries compete for one channel |
| 3 | The ≈61% figure excludes Purkinje **and** basket cells — it is a granule-cell measurement | [`cerebellar_discrimination_experiments_20260922.md:637`](cerebellar_discrimination_experiments_20260922.md) §13.2 | 🟢 **HOLDS, and is stronger than "an A60 property."** Weyer & Schilling 2003 (first-hand) puts NeuN at granule cells only; Aldaz & Hussain 2020 puts the highest-WWOX cerebellar subtypes at basket **and** granule cells. The measurement excludes one of its own two top candidates |
| 4 | Bulk vDNA is arithmetically mute on Purkinje (≤0.4% vs 8.75–12.05×) | [`purkinje_cheapest_path_and_community_followup_20260922.md:275`](purkinje_cheapest_path_and_community_followup_20260922.md) §2.5b | 🟢 **HOLDS for DNA, with the bound the source itself imposes.** Rat 274 granule per Purkinje ⇒ 0.36%; human ≈0.026%; **no mouse value retrieved**; and the arithmetic is clean *only* for the nucleus-denominated DNA assay — protein and RNA dilution are `UNMEASURED` (`RC-6`, `:415`) |
| 5 | The 2021 archive has in-vivo reporter material and **no** lysates; therapeutic vector is `mWwox-IRES-EGFP` | [`purkinje_cheapest_path_and_community_followup_20260922.md:197`](purkinje_cheapest_path_and_community_followup_20260922.md), `:217`, `:240` | 🟢 **HOLDS.** Complete 2021 Methods heading list contains no immunoblot and no tissue extraction; `AAV9-hSynI-EGFP` injected ICV in vivo at P0; therapeutic construct named `AAV9-hSynI-mWwox-IRES-EGFP` twice |
| 6 | 2026 scans are `BLOCKED — HOLDER-ONLY` | [`purkinje_existing_material_experiment_20260922.md:291`](purkinje_existing_material_experiment_20260922.md) §2.6; first-hand at [`tx007_animal_flow_survival_validity_20260922.md:81`](tx007_animal_flow_survival_validity_20260922.md) | 🟢 **HOLDS.** *"Data and code availability: Not relevant."* — read first-hand by another actor. There is no repository to query |

🔴 **Attestation discipline.** I read no primary article in this act. Every verbatim string quoted
below is reproduced from a repository file and is tagged **SIBLING-ATTESTED** with `file:line`. Where
a sibling itself marked a string FIRST-HAND, I say so, but I do not inherit its first-handedness.

---

# 1 · CHANNEL AND METADATA AUDIT — the core question

## 1.1 The audit table

Six imaging assets exist or are claimed to exist. For each, the repository is interrogated for seven
metadata fields. `NOT STATED` means the source says nothing; **`UNKNOWN`** means the repository
cannot establish it even by inference and no actor has recorded it; `NOT RECORDED HERE` means the
field was never sought by any prior node.

| | **A1 · 2026 whole-slide scans** | **A2 · 2021 confocal images** | **A3 · 2021 whole-slide scans** | **A4 · 2021 in-vivo reporter sections** | **A5 · 2021 published panels** | **A6 · 2026 published panels** |
|---|---|---|---|---|---|---|
| **What it is** | Sagittal 14 µm, WT/KO/KO-injected, P10–P180 | Same programme, Nikon A1R+ or Olympus FV1000 | *"panoramic digital slide scanner … CaseViewer"* | `AAV9-hSynI-EGFP` control arm + `mWwox-IRES-EGFP` therapeutic arm, ICV P0, perfused | Fig 2F (cerebellum, P19), Fig 4A (whole-brain sagittal), Fig 1E/2G | S3C, S3E/F, S5J/K, S6D |
| **Channels present** | 🟡 **3 maximum, by secondary-antibody construction**: Hoechst 33258 · one *rabbit* @647 · one *mouse* @488 | same 3-channel ceiling | same 3-channel ceiling | 🔴 **2 named**, WWOX + NeuN; **native EGFP is a third green emitter competing with the anti-mouse 488 secondary** | 🔴 **2**: WWOX magenta, NeuN green | ⚪ **UNKNOWN** — captions `NOT READABLE` |
| **Hoechst / DAPI present?** | 🟡 **in the STAINING protocol — yes**. **In the SCANNED FILE — `NOT STATED`** (`RJ-7`) | ⚪ **UNKNOWN**; not separately attested | ⚪ **UNKNOWN** | 🔴 **NO.** 2021 IF Methods end at *"mounting with mounting medium"*; no DAPI, no Hoechst named (`RC-1`) | 🔴 **NO** — legend names only WWOX and NeuN | ⚪ **UNKNOWN** |
| **Magnification / objective / NA** | 🔴 **NOT STATED — zero tokens** for `objective`, `numerical aperture`, `pixel size` anywhere in the two deepest audits of this archive | 🔴 **NOT STATED** — instrument named, configuration not | 🔴 **NOT STATED** | 🔴 **NOT STATED** | 🟡 **inferable only from scale bars**: Fig 2F **50 µm**; Fig 4A **2 mm** | ⚪ **UNKNOWN** |
| **Effective resolution** | ⚪ **UNKNOWN.** Prior nodes' phrase *"at objective resolution"* is an **INFERENCE from the word *panoramic***, not a recorded number | ⚪ **UNKNOWN**, but confocal by class | ⚪ **UNKNOWN** | ⚪ **UNKNOWN** | 🔴 **compressed, contrast-adjusted reproduction**; effective ppi must be measured on the file, not assumed | ⚪ **UNKNOWN** |
| **Optics** | 🔴 **WIDEFIELD** (`confocal` = 0 on that surface) ⇒ anisotropic out-of-focus bleed from the granular layer onto the granular-facing side of the Purkinje row | 🟢 **CONFOCAL** — the optically best material in the problem | 🔴 widefield | 🟡 mixed; which sections went to which instrument `NOT STATED` | n/a | ⚪ **UNKNOWN** |
| **Mediolateral / sagittal level** | 🔴 **NOT STATED**, explicitly: *"at whatever mediolateral levels were cut"* | 🔴 **NOT STATED** | 🔴 **NOT STATED** | 🔴 **NOT STATED** | 🟡 Fig 4A is a **whole-brain sagittal with cerebellum demonstrably in frame** — the only positive frame evidence anywhere | ⚪ **UNKNOWN** |
| **Would the Purkinje layer be in frame?** | 🟡 **Probably, for the section** — a whole-slide scanner digitises the whole section. 🔴 **But whether cerebellum is covered in the `1.23E11` and `2.63E11` arms is `NOT STATED`** (`R4`); the one cerebellar transduced-fraction figure sits in the **`4E10` +WPRE** arm | ⚪ **UNKNOWN** — a confocal image is a chosen field, not a section | ⚪ **UNKNOWN** (`RC-4`) | ⚪ **UNKNOWN** — no cerebellar reporter panel is published; Fig 1F legend says *"brain tissue (**cortex**)"* | 🟢 **Fig 2F is a dedicated cerebellum field at P19** — but whether the **monolayer** is in frame is `A-f1`, **specified and never climbed** | ⚪ **UNKNOWN** |
| **Retention of material/files** | 🔴 `NOT STATED` (`A-f4`) | 🔴 `NOT STATED` | 🔴 `NOT STATED` (`RC-4`) | 🟡 FFPE blocks effectively indefinite; OCT `NOT STATED` (`RC-3`) | 🟢 published, permanent | 🟢 published |
| **Reachable by whom** | 🔴 **HOLDER-ONLY** — *"Data and code availability: Not relevant."* | 🔴 HOLDER-ONLY | 🔴 HOLDER-ONLY | 🔴 HOLDER-ONLY | 🟢 **anyone with a browser**; 🔴 blocked in this deployment (egress; `files/` absent) | 🔴 supplement retrieval untested on any available route (`C-6`) |

**Locators for the table, in order of appearance.** A1 channels and Hoechst:
[`purkinje_existing_material_experiment_20260922.md:239`](purkinje_existing_material_experiment_20260922.md) §2.3 and `:244`;
A1 `RJ-7`: `:540`, restated as load-bearing at `:550`. A1 optics: `:148`, `:383`.
A1 Methods verbatim: [`cerebellum_layer_localisation_20260922.md:280`](cerebellum_layer_localisation_20260922.md) §3.5.
A1 arm coverage `R4`: [`cerebellar_discrimination_experiments_20260922.md:551`](cerebellar_discrimination_experiments_20260922.md).
A1 mediolateral level: [`tx007_purkinje_frontier_20260922.md:287`](tx007_purkinje_frontier_20260922.md) P2 bound.
A2/A3 acquisition verbatim: [`purkinje_cheapest_path_and_community_followup_20260922.md:143`](purkinje_cheapest_path_and_community_followup_20260922.md) §2.1b; `RC-4` at `:413`.
A4 reporter: `:197`, `:202`, `:217`; the green-on-green conflict `RC-2` at `:411`.
A4/A5 counterstain absence: `:188`, `C-2` refutation at `:383`, `RC-1` at `:410`.
A5 scale bars and frame: `:68`, `:172`, `:334`; `A-f1` never climbed: [`tx007_purkinje_frontier_20260922.md:143`](tx007_purkinje_frontier_20260922.md).
A6: [`cerebellum_layer_localisation_20260922.md:945`](cerebellum_layer_localisation_20260922.md); `C-6` untestable at
[`purkinje_cheapest_path_and_community_followup_20260922.md:388`](purkinje_cheapest_path_and_community_followup_20260922.md).

## 1.2 🆕 The finding this audit exists to make

Prior nodes converge on one sentence — *"a panoramic scanner digitises the entire section at
objective resolution, so the Purkinje row is already inside the file"*
([`cerebellar_discrimination_experiments_20260922.md:381`](cerebellar_discrimination_experiments_20260922.md) §3 #5;
[`:523`](cerebellar_discrimination_experiments_20260922.md) `F3`;
[`purkinje_existing_material_experiment_20260922.md:524`](purkinje_existing_material_experiment_20260922.md) `J2`).
That sentence is **correct about the instrument class and underdetermined about the file**, and the
gap between those two has never been written down as such.

🔴 **Three things are asserted by that sentence and none is recorded anywhere in this repository:**

1. **That the scan carries the Hoechst channel.** One node flagged this as `RJ-7` and correctly
   called it load-bearing ([`purkinje_existing_material_experiment_20260922.md:550`](purkinje_existing_material_experiment_20260922.md)).
   Hoechst is in the *staining* protocol; the scanner's *channel configuration* is not described. A
   whole-slide fluorescence scanner is routinely run on a subset of the filters a slide carries, and
   nothing in the record excludes a two-channel or one-channel acquisition. ⇒ **`UNKNOWN`.**
2. **That the scan resolves a soma.** *"Objective resolution"* is an inference from the word
   *panoramic*. **No objective, no NA, no pixel size and no magnification is recorded for any 2026
   asset anywhere in the analysis corpus** — the token counts are zero in both files that audited
   this archive most deeply. A slide scanner run at a low-power survey setting digitises the whole
   section and still cannot separate a Purkinje soma from the granular-layer boundary. ⇒ **`UNKNOWN`.**
3. **That the scan covers cerebellum in the arms of interest.** `R4`: `NOT STATED`, and the only
   cerebellar transduced-fraction figure sits in the `4E10` +WPRE comparison arm, not in `1.23E11`
   or `2.63E11`.

🎯 **Stated as the deliverable asks.** *In principle*, the Purkinje question is resolvable from
existing images: the sections were cut, the cerebellum is in the block, WWOX is in a channel, and a
whole-slide scanner exists. *Actually*, with these files as the repository records them, **it is not
established that any existing image file has (i) a nuclear channel, (ii) sufficient resolution and
(iii) cerebellar coverage in a therapeutic-dose arm simultaneously** — and all three are required at
once for the marker-free route. The three unknowns are **not independent failure modes to be checked
serially**: any one of them being false collapses the whole marker-free route, and none can be
checked from outside the holding laboratory.

⚠️ **And this is not a reading debt that better retrieval would clear.** Items 1 and 2 are not in the
papers at all — no Methods section states its scanner channel configuration or its scan objective.
They are answerable only by **opening a file**, which requires the holder. This is the distinction
between *unretrieved* and *unrecorded*, and it changes the recommendation in §3.

## 1.3 The reporter asset carries a channel collision that is worse than recorded

The 2021 in-vivo reporter material is the single largest cost movement anyone has found on this
question, and it deserves its own channel line rather than a shared row.

🔴 **In the therapeutic (`mWwox-IRES-EGFP`) arm, three signals contend for two usable channels.**
Native EGFP is green; the NeuN secondary is *"goat anti-mouse Alexa flour 488"*, also green
([`purkinje_existing_material_experiment_20260922.md:244`](purkinje_existing_material_experiment_20260922.md));
and the 2021 Fig 1D legend itself says *"Neurons are labeled with anti-NeuN antibody (green)"*
([`purkinje_cheapest_path_and_community_followup_20260922.md:217`](purkinje_cheapest_path_and_community_followup_20260922.md) §2.3b).
Whether they are separable is `RC-2`, pending **Appendix Table S1** (`FT-152`), unretrieved.

🎯 **But the collision has a clean structural consequence that has not been drawn: the two reporter
arms are not equally blind, and they are blind in opposite ways.**

| arm | green channel | far-red channel | nuclear channel | what it can say about the Purkinje row |
|---|---|---|---|---|
| **`AAV9-hSynI-EGFP` control** | 🟢 **native EGFP, uncontested** — needs no antibody | 🟢 **free**, and the anti-WWOX rabbit channel could occupy it | 🔴 absent | 🎯 **Vector reach**, cleanly — but NeuN cannot be added without taking the green slot back |
| **`mWwox-IRES-EGFP` therapeutic** | 🔴 **contested** — EGFP + anti-mouse 488 | 🟡 anti-WWOX | 🔴 absent | 🟡 *"transduced"* and *"expressing"* in the same soma — **if** `RC-2` resolves favourably |

⚠️ **Two bounds carried from the source and not weakened.** An **IRES** second cistron is not
expressed at the first cistron's level, so EGFP intensity is **not** a proxy for WWOX amount — it is
a presence channel only. And the reporter dose is `2E10`/hemisphere; it answers at that dose and
transfers to no other
([`purkinje_cheapest_path_and_community_followup_20260922.md:224`](purkinje_cheapest_path_and_community_followup_20260922.md)).

🎯 **Adding a third bound, new here.** The control arm's advantage — *no antibody needed* — is also
its ceiling: **an EGFP-only section has no cell-identity channel at all.** Its green signal in the
Purkinje row is `hSynI` promoter activity in *something* at that position. The control arm answers
*"did vector reach the layer"* and is structurally incapable of answering *"did it reach a Purkinje
cell"*. That is a real answer to a real sub-question, and it should be claimed as that and not more.

---

# 2 · WHAT EXISTING IMAGES CAN AND CANNOT ANSWER

The question is whether **position + morphology**, with no Purkinje marker, is enough. Purkinje cells
are the most positionally stereotyped neurons in the brain: a monolayer at the molecular/granular
boundary, with somata far larger than anything around them. That is a genuine asset and it has been
correctly identified by a sibling node, which also retrieved the published precedent for **label-free
automated Purkinje-cell-layer localisation**
([`purkinje_existing_material_experiment_20260922.md:181`](purkinje_existing_material_experiment_20260922.md) `PJ2`).
I do not re-derive that. I assess the four capabilities the brief names, and state the residual
confound for each.

| | capability | verdict **if** a nuclear or landmark channel exists at soma resolution | verdict **on the files as actually recorded** | residual confound |
|---|---|---|---|---|
| **(a)** | **Layer segmentation** | 🟢 **YES, robustly.** Granular = extreme nuclear density; molecular = sparse; the PCL is the single row between them. Label-free automated PCL detection is published | 🟡 **CONDITIONAL.** Needs (i) the DNA channel to have been captured (`RJ-7`) *or* (ii) the NeuN-bright/NeuN-dark workaround, which exists only where NeuN was stained and imaged | 🔴 The NeuN workaround is `INFERENZA` from an attested antigen property + cytoarchitecture (`PREMISE: DEFAULT_FROM_TEXTBOOK`), not a measurement |
| **(b)** | **Reporter / EGFP presence in the Purkinje layer** | 🟢 **YES** — and in a `Wwox`-null host under a neuron-restricted promoter, a positive is transgene-derived and cannot be glial-autofluorescent background | 🔴 **NOT ON ANY PUBLISHED SURFACE.** The only published EGFP panel is *"brain tissue (**cortex**)"*; no cerebellar reporter panel exists in print. Holder-only | 🎯 **The asymmetry, carried from the frontier file:** a **positive** reading is informative; a **negative** is not, because absence at one field, one arm, one dose is not absence |
| **(c)** | **WWOX signal in the Purkinje layer** | 🟡 **PARTIALLY** — layer-resolved WWOX intensity is obtainable | 🟡 **CONDITIONAL** on the same three unknowns | 🔴 **The load-bearing confound. Signal AT the layer is not signal IN a Purkinje cell.** The PCL is interdigitated with **Bergmann glia somata** and invested with **basket-cell pericellular terminals** — and basket cells are, per Aldaz & Hussain, among the *highest*-WWOX cerebellar subtypes. A marker-free layer read therefore measures a mixture whose WWOX-brightest member may be the one that is not a Purkinje cell |
| **(d)** | **Re-quantification** | 🟡 **Layer-resolved distributions, yes. Cell-type-resolved, no** | 🔴 **NO, on the files as recorded** | 🔴 Three compounding traps, all of which must be honoured and one of which is fatal without a marker: **segment on the nuclear/landmark channel, never on WWOX** (segmenting on the signal under test makes an untransduced cell invisible by construction); **mean intensity inside the mask, never integrated** (a 12–14 µm cut is thinner than a Purkinje soma, so integrated signal penalises exactly the cell type of interest and would **manufacture a spurious deficit**); and **widefield bleed is anisotropic** on the granular-facing side |

🔴 **The honest summary of §2, and it is the file's second result.** Position and morphology alone
are sufficient to find **where a Purkinje cell must be** and insufficient to establish **that a given
bright object is one**. A marker-free re-quantification of existing scans would reproduce, at mouse
resolution and with better statistics, exactly the limitation that already bounds the field's only
human Purkinje-layer observation (`PMID 16941225`) — an observation the repository records as
`SOURCE_BLOCKED` by licence, third confirmation
([`purkinje_cerebellar_celltype_wwox_census_20260922.md:718`](purkinje_cerebellar_celltype_wwox_census_20260922.md)).
🎯 **Spending the cheapest rung to re-derive the known limit of the only existing datum is a poor
trade**, and naming that trade is the main practical output of this audit.

⚠️ **One thing a marker-free read *would* deliver that a marker adds nothing to.** The **spatial
pattern** — parasagittal banding versus a smooth pial-inward gradient — is a whole-field geometry
question that needs no cell identity at all, and it discriminates a circuit-topographic cause from a
delivery-gradient cause. That is already on the record as `C8` / `F3`
([`cerebellar_discrimination_experiments_20260922.md:419`](cerebellar_discrimination_experiments_20260922.md),
[`:523`](cerebellar_discrimination_experiments_20260922.md)) and I do not re-propose it; I note only
that it is the **one** existing-image question that survives every unknown in §1 except resolution.

---

# 3 · THE SMALLEST EXISTING-SECTION EXPERIMENT

🔁 **Already on the record and NOT re-proposed.** The compressed three-channel stain — **Hoechst
33258 · mouse anti-calbindin-D28k → anti-mouse AF488 · the laboratory's existing rabbit anti-WWOX
1:5,000 → anti-rabbit AF647** — is fully specified by a sibling node, with its segmentation bar, its
mean-not-integrated rule and its per-layer reporting
([`purkinje_existing_material_experiment_20260922.md:392`](purkinje_existing_material_experiment_20260922.md) §4,
channel justification at `:404`, asset list `J1` at `:523`; carried as `P4` at
[`tx007_purkinje_frontier_20260922.md:330`](tx007_purkinje_frontier_20260922.md), and as `F2` at
[`cerebellar_discrimination_experiments_20260922.md:522`](cerebellar_discrimination_experiments_20260922.md)).
**That design is correct, it is the right experiment, and this section does not compete with it.**

What this section adds is the thing the brief asks for and that the existing specification does not
carry: **a channel-by-channel justification against the three outcomes, and an explicit statement of
the blind spot created by the channel that has to be cut.**

## 3.1 The three outcomes, and the 3-channel constraint as a design constraint

| | outcome | what it means for the programme |
|---|---|---|
| **A** | **Vector absent** from Purkinje cells | Capsid, route or tropism problem — the lever is delivery |
| **B** | **Vector present, WWOX output poor** | Promoter, transcript or stability problem — the lever is the cassette |
| **C** | **Vector present, WWOX present** | Delivery and expression are solved for this cell type; any residual phenotype is function, timing or cell-autonomy — the lever is elsewhere entirely |

🔴 **The constraint is not a preference; it is built into the reagents.** Exactly two secondaries
exist in the entire programme — one anti-rabbit at 647 and one anti-mouse at 488 — plus the Hoechst
DNA channel. **Three channels is the hard ceiling**, and any fourth signal requires a new secondary,
a directly-conjugated primary or a species change, none of which are existing-asset moves.

## 3.2 Channel-by-channel justification: which outcome pair does each one separate?

| channel | separates | is it separable by anything cheaper? | verdict |
|---|---|---|---|
| **Nuclear / landmark** (Hoechst, or the NeuN-bright/NeuN-dark bands where Hoechst is absent) | 🎯 **A from "nothing here"** — it supplies the **WWOX-independent soma mask**, hence an honest **denominator**, hence the ability to observe an *untransduced* cell at all; and the section-plane control that makes mean intensity comparable between a truncated large soma and an intact small one | 🔴 **No.** Without it, segmentation must fall back to the signal under test, and outcome **A becomes unobservable by construction** — an untransduced Purkinje cell is simply not in the dataset | 🟢 **KEEP. Non-negotiable** |
| **Purkinje identity** (mouse anti-calbindin-D28k, taking the mouse slot `MAB377` occupies) | 🎯 **The Purkinje cell from everything else at the same position** — the Bergmann-glia and basket-terminal confound of §2(c). It is what converts *"signal at the layer"* into *"signal in the cell"* | 🔴 **No.** Morphology gets to the row and stops there (§2). And it is a **free co-product generator**: calbindin⁺ counts per arm come out of the same image with no extra step | 🟢 **KEEP. This is the channel the entire question is about** |
| **WWOX** (existing rabbit anti-WWOX @647) | 🎯 **B from C** — poor output from adequate output, as a per-cell **distribution** and a positive **fraction**, reported separately | 🔴 **No.** Nothing else in the programme measures WWOX protein at cellular resolution | 🟢 **KEEP** |
| ✂️ **Vector / reporter** (EGFP or anti-capsid) | Would separate **A from B** *directly* rather than by inference | 🟡 **Partly, and only in the 2021 archive.** The `mWwox-IRES-EGFP` construct puts a reporter in the same cells as the therapeutic protein — but that is a **different archive, a different dose (`2E10`/hemisphere) and a different construct**, and in this stain it would contend with the 488 secondary (`RC-2`) | 🔴 **CUT.** It owns no pair that the other three cannot reach, **at the price stated below** |

## 3.3 🔴 THE BLIND SPOT THE CUT CREATES — stated, not buried

**Cutting the vector channel makes A and B distinguishable only by inference, not by observation.**

In a `Wwox`-null host the inference is unusually strong — any WWOX signal is necessarily
transgene-derived, so **WWOX-positive ⇒ vector reached that cell**, and outcome **C is directly
observed**. The blind spot is entirely on the negative side: **a WWOX-negative Purkinje cell is
uninterpretable between A and B.** It is either a cell the vector never reached, or a cell the vector
reached whose cassette produced protein below the detection floor. Those are opposite therapeutic
conclusions — change the capsid, or change the promoter — and this three-channel design cannot tell
them apart.

🎯 **Three honest mitigations, and none of them is a substitute for the fourth channel.**

1. **The 2021 `AAV9-hSynI-EGFP` control arm answers the A-side question separately**, in different
   material, at `2E10`/hemisphere, with no antibody required — and therefore with no channel
   contention at all. That is a **two-archive answer, not a one-section answer**, and the dose bound
   must travel with it.
2. **The distribution, not the mean, carries the information.** A bimodal per-cell WWOX distribution
   in the Purkinje population argues for a reached/not-reached mixture (A-flavoured); a unimodal
   low-shifted distribution argues for uniform poor output (B-flavoured). 🔴 **This is suggestive
   geometry, not a discriminator**, and it must not be reported as one.
3. **`hWWOX` species-specific detection**, where the human construct was used, can in principle
   distinguish transgene from host product — recorded by a sibling at
   [`purkinje_existing_material_experiment_20260922.md:73`](purkinje_existing_material_experiment_20260922.md) §4.4 —
   but in a null host there is no host product to distinguish it from, so it buys nothing here.

⇒ 🎯 **The blind spot is accepted deliberately, on the argument that outcome C — the outcome that
would redirect the entire programme away from delivery — is the one this design observes *directly*,
and A-versus-B is a second-round question that a reporter arm in a second archive can take up.**
That reasoning is stated here so a later reader can overturn it rather than inherit it.

## 3.4 What this design still cannot do

- 🔴 It measures **protein per cell in arbitrary units**, not molecules. The bridge to an absolute
  quantity does not exist ([`purkinje_existing_material_experiment_20260922.md:613`](purkinje_existing_material_experiment_20260922.md)).
- 🔴 It is **one mediolateral level per section**, and which level is `NOT STATED` for every archive
  (§1.1). Vermis-versus-hemisphere is therefore not addressable without the block.
- 🔴 In the 2026 archive the optics are **widefield**; the granular-facing half of every Purkinje mask
  is contaminated anisotropically, and the molecular-facing half-mask must be reported separately.
  🎯 The 2021 archive is **confocal** and does not carry this trap — which makes it the *optically*
  better material even though the 2026 archive is better for age range and dose.

---

# 4 · EXPRESSION IS NOT FUNCTION

🔴 **Stated plainly, because the temptation is structural.** Everything in §§1–3 is an
**expression and delivery** question: *is the vector genome there, and is WWOX protein there.* A
Purkinje cell that is transduced and WWOX-positive by immunofluorescence has been shown to **contain
the protein**, and nothing whatever has been shown about whether it **fires correctly, receives
climbing-fibre input correctly, or supports motor coordination**.

**Purkinje functional rescue is a separate question requiring a separate readout**, and the
repository already records that the existing functional instruments cannot supply it: the 2021
cell-attached recordings are at *"1.6–2 mm posterior to the bregma and 4 mm lateral to the midline"*,
depth 300 µm, with the legend naming *"spontaneous **neocortical** activity"* — **no cerebellar
physiology exists in the paper**; and the video-EEG electrodes are *"implanted bilaterally into the
subdural space over frontal and parietal cortex"* — **no cerebellar electrode**
([`cerebellar_functional_readout_census_20260922.md:74`](cerebellar_functional_readout_census_20260922.md) `R7`,
[`:83`](cerebellar_functional_readout_census_20260922.md) `R16`). The motor endpoints that do exist —
hindlimb clasping, ataxia score, rotarod — are **coarse and not cerebellum-specific**, and the same
census names the high-resolution alternatives (interlimb kinematics, eyeblink conditioning) as the
discriminating readouts ([`:274`](cerebellar_functional_readout_census_20260922.md)).

⚠️ **The named failure mode.** If the stain in §3 returns outcome **C** — vector present, WWOX
present — the correct conclusion is *"delivery and expression are not the limiting variable for this
cell type"*, and the **incorrect** conclusion, which an expression assay invites, is *"Purkinje cells
are rescued."* 🎯 **An expression assay must not be allowed to masquerade as a functional one**, and
outcome C is precisely the result that would make that masquerade tempting, because it is the result
that looks like good news.

🔴 And the converse trap, which protects `PREMISE: NOBODY_LOOKED`: **a WWOX-negative Purkinje cell is
not a functional deficit either.** It is an expression observation, and the functional consequence of
it is unmeasured in every WWOX system.

---

# 5 · EXISTING-ASSET LADDER

Cost classes as the brief defines them. **L0** reanalysis of existing data · **L1** new analysis on
stored material · **L2** new stain on existing material · **L3** new animal.

| # | proposal | level | new animals? | information gain | status |
|---|---|---|---|---|---|
| **α** | 🆕 **Establish the three unknowns of §1.2** — does any existing scan carry a nuclear channel; at what objective/pixel size; does it cover cerebellum in `1.23E11` / `2.63E11`? | **L0** — a *metadata* read, below every rung anyone has costed | 🟢 **NO** | 🎯 **It does not answer the biological question at all. It decides whether L0/L1 exist as routes.** Cheapest act in the problem and the only one that is strictly prior to the others | 🆕 **NEW HERE.** 🔴 **HOLDER-ONLY** — these fields are not in either paper, so no retrieval can substitute |
| **β** | Inspect **2021 Fig 2F** (cerebellum, P19, 50 µm bar) and **Fig 4A** at measured effective ppi | **L0** | 🟢 NO | The only rung executable by a reader holding nothing; decides `A-f1` | 🔁 **CARRIED** — `P3` / `C3`, specified and never climbed (egress-blocked here). **Not re-proposed** |
| **γ** | **Spatial-pattern** read of existing scans — parasagittal banding vs pial-inward gradient | **L0/L1** | 🟢 NO | Discriminates circuit-topographic from delivery-gradient causes; **needs no cell identity**, so it survives every §1 unknown but resolution | 🔁 **CARRIED** — `C8` / `F3`. Noted, not re-proposed |
| **δ** | Marker-free **layer-resolved** WWOX re-quantification of existing scans | **L1** | 🟢 NO | 🟡 **Downgraded by this audit.** Conditional on all three §1.2 unknowns simultaneously, and even on success it reproduces the known Bergmann/basket confound (§2) | 🔁 **CARRIED** — `J2` / `F3` / `P2`. 🔴 **This file recommends α before δ**, which is the one ordering change it proposes |
| **ε** | 🆕 **2021 `AAV9-hSynI-EGFP` control-arm cerebellar fields** — vector reach at the Purkinje layer, native reporter, **no antibody, no channel contention** | **L1** if scans exist; **L2** if re-cut FFPE is needed | 🟢 **NO** | 🎯 Answers *"did vector reach the layer"* cleanly and is **structurally incapable** of answering *"did it reach a Purkinje cell"* (§1.3). Claimed as exactly that | 🆕 **The channel analysis is new here**; the reporter asset itself is a sibling's finding and is credited, not re-claimed |
| **ζ** | **Hoechst · calbindin · WWOX** compressed stain, per-layer distributions + positive fraction + calbindin⁺ counts | **L2** — one new primary, inheriting the existing anti-mouse secondary | 🟢 **NO** | 🎯 **The highest-information act available without a new animal**, and the only one whose outcome is unpredicted in several directions. **Directly observes C; A-vs-B blind (§3.3)** | 🔁 **CARRIED — `J1` / `F2` / `P4`, not claimed here.** This file contributes the §3.2 pair-justification and the §3.3 blind-spot statement |
| **η** | **WWOX channel added to the `Wwox^P47T/P47T` laboratory's existing calbindin vermis sections** (80 d / 250 d, published `ns` basket-cell control) | **L2** | 🟢 NO | Converts a **cell count** into a **protein measurement** in the exact cell type, in the one model with an internal interneuron specificity control | 🔁 **CARRIED** — `F6`. 🔴 **Different allele and different model — results must never be pooled with the null-line material above** |
| **θ** | Cerebellum-specific **functional** readout (§4) | **L3** | 🔴 **YES** | The only route to function; nothing below L3 reaches it | 🔁 Carried by the functional census. **Out of scope here and correctly so** |

🎯 **The ladder's one structural lesson.** Every rung from **α** to **ζ** is `NEW ANIMALS: NO`. The
binding constraint on this question is **not animals and not money — it is custody**: rungs α, γ, δ,
ε and ζ are all `HOLDER-ONLY`, because *"Data and code availability: Not relevant."* means there is
no deposited file and no repository to query. **β is the only rung outside the holding laboratory by
construction, and it is the one that was specified and never climbed.**

---

# 6 · What I could NOT establish, and what would reopen it

| # | recorded state | what would reopen it |
|---|---|---|
| **B-1** | 🔴 **Whether any 2026 whole-slide scan captured the Hoechst channel** — `NOT STATED`; inherits `RJ-7` and, per this audit, is one of **three** simultaneous requirements rather than one | A scanner-configuration statement, or any cerebellar panel showing a DNA channel |
| **B-2** | 🆕 🔴 **The objective, NA, magnification and pixel size of every image asset in the programme** — `NOT STATED`, **zero tokens in the corpus**. *"At objective resolution"* is an inference from the word *panoramic* and should stop being repeated as a property of the files | Any acquisition-settings statement; or an image file's own metadata |
| **B-3** | 🔴 **The mediolateral/sagittal level of every section series** — `NOT STATED` in both archives. Decides vermis-vs-hemisphere and, for the sibling `P2` proposal, whether hypothalamus is in frame at all | Any sectioning-plane statement or a block-orientation figure |
| **B-4** | 🔴 **Whether whole-slide scans cover cerebellum in the `1.23E11` and `2.63E11` arms** — `R4`, unchanged | Any image-availability or supplementary-figure statement |
| **B-5** | 🔴 **Whether native EGFP is separable from the anti-mouse 488 secondary in the `mWwox-IRES-EGFP` arm** — `RC-2`, pending Appendix Table S1 (`FT-152`) | That table |
| **B-6** | 🔴 **Whether any 2021 cerebellar field was scanned whole-slide rather than photographed confocally** — `RC-4` | Any scanner-configuration statement |
| **B-7** | ⚪ **The 2026 supplementary figure surface** — untestable on any route available here (`C-6`); egress-blocked, `files/` absent. **No external action was attempted** | A human with a browser, or a deployment with egress |
| **B-8** | 🔴 **Purkinje share of cerebellar protein and RNA** — `UNMEASURED` (`RC-6`). The bulk-muteness argument is proven for **DNA only** and must not be extended silently | Any measurement of Purkinje protein or RNA as a fraction of cerebellar total |

---

# 7 · Verdict, in four lines

1. 🔴 **The existing images cannot be shown to answer the question.** Not because the instruments are
   wrong — a whole-slide scanner over a sagittal section is the right instrument — but because
   **three metadata facts required simultaneously (nuclear channel, soma-level resolution, cerebellar
   coverage in a therapeutic arm) are each `UNKNOWN`, and none of them is in either paper.**
   *In principle* resolvable; *actually* resolvable is undetermined, and determinable only by the holder.
2. 🟡 **Position and morphology get to the Purkinje row and stop there.** A signal **at** the layer is
   not a signal **in** a Purkinje cell — Bergmann glia somata and basket-cell terminals share that
   position, and basket cells are among the highest-WWOX cerebellar subtypes.
3. 🟢 **The minimal existing-section experiment is the three-channel stain already specified by a
   sibling**, which this file does not re-propose. Its channels are justified here by outcome pair;
   the vector channel is cut for want of a pair it alone owns, and the resulting blind spot — **A and
   B indistinguishable on the negative side** — is stated rather than absorbed.
4. 🔴 **All of it is expression, none of it is function**, and `PREMISE: NOBODY_LOOKED` stands
   unchanged: **nobody has measured whether Purkinje cells are reached or express WWOX.** This file
   asserts nothing about the answer.

---

# ORCHESTRATOR VERIFICATION — 2026-09-22

Load-bearing claims re-retrieved at source rather than accepted from the hand-back.

## V1 · 🟢 The core finding is CONFIRMED, and it is the file's real result

**No magnification, numerical aperture, or pixel size is attached to the 3DHISTECH scanner
anywhere in the repository.** Every co-occurrence of the scanner with a resolution word is
**inferential**, not a stated specification. The premise is visible in the corpus in this exact
form:

> *"A panoramic scanner digitises the **entire** section at objective resolution"*
> — `cerebellar_discrimination_experiments_20260922.md:381`

🎯 **That sentence is an inference from the instrument's class, stated as a property of the
files.** It then propagates to `purkinje_existing_material_experiment_20260922.md:524` (`J2`) and
`purkinje_cheapest_path_and_community_followup_20260922.md:338` (`C7`), where a re-analysis is
called *"unanalysed data, not an unrun experiment"* — a claim that holds **only if** soma-level
resolution actually survived into the saved file. Nothing on record establishes that it did.

**This is the same defect class as the uncited SDR-homodimer premise**: an unsourced assertion
sitting inside an otherwise careful argument, load-bearing for a cost estimate, and inherited
forward by siblings without re-examination.

## V2 · 🔴 CORRECTION — one scope claim is overstated, and the looser form must not propagate

The hand-back states *"`NOT STATED`, **zero tokens** for `objective` / `numerical aperture` /
`pixel size` across the corpus."* Measured:

| Token | Files |
|---|---|
| `numerical aperture` | **0** 🟢 |
| `pixel size` | **0** 🟢 |
| `20x\|40x\|63x` | **15** 🔴 |
| `objective` | **12** 🔴 |

The 15 magnification hits sit in dose-unit forensics and delivery-reconstruction files
(`tx007_dose_unit_forensics`, `tx007_dose_challenge`, `tx007_per_arm_delivery_reconstruction`) and
in a partial-locator dossier — **none attached to the scanner**. So the *conclusion* survives
intact while the *stated scope* does not.

**Corrected form, which is what may be carried forward:**

> *No objective, numerical aperture or pixel-size specification is attached to the 3DHISTECH
> panoramic scanner in any repository artefact (`FILE TYPE` Markdown + JSONL · `SOURCE SCOPE`
> repository only, **not** the publications themselves · `SOURCE DEPTH` sibling-attested Methods
> quotations, no first-hand body read this act). Magnification tokens do occur elsewhere in the
> corpus, in unrelated dose and delivery contexts.*

🔴 **"Zero tokens in the corpus" and "no spec attached to this instrument" are different claims
with different evidence**, and only the second is supported. The first would have been repeated by
the next reader as a stronger fact than it is — which is precisely how the `panoramic ⇒ objective
resolution` premise it is criticising came to propagate.

## V3 · What this does NOT establish

It does **not** show the scans lack soma-level resolution. A 3DHISTECH panoramic scanner may well
digitise at a resolution that resolves a Purkinje soma. The finding is that **the repository cannot
tell**, and therefore that `J2`/`C7`/item-5 rest on an assumption rather than a record. `HOLDER-ONLY`
is the correct classification, and the α metadata read proposed in this file — **check the file
header before designing anything on top of it** — is endorsed as the correct first rung.

`PREMISE: NOBODY_LOOKED` is unchanged. Nothing here asserts anything about whether Purkinje cells
are reached.
