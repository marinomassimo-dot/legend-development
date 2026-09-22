# COMMIT CANDIDATE — CC-20260922-POSTNATAL-SVZ-01

**Source:** Scientist K (`postdiagnosis` follow-on, `wwox_postnatal_svz_expression_20260922.md`),
**verified by the Orchestrator in two retrieved bodies** — `PMC10901738` (Nascimento 2023) and
`PMC7727818` (Aldaz & Hussain 2020). Debt declared by the delegate as `FT-133`, **no PMIDs stripped**.
**Change class:** **MINOR**. One delegate contradiction is **downgraded** on verification; three
findings the delegate did not flag are added from the same bodies.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2**, except §4 which touches an allelic-series datum (**R3**).
**Proposes:** `D-32` — *"a resource that never sampled the compartment cannot report absence in it."*

---

## 1 · 🔴 The answer is NO — and the gap is now precisely located

**No accessible source reports WWOX, transcript or protein, in the human postnatal SVZ, RMS, MMS or
any postnatal human germinal compartment.** In any resource, at any age, at any depth.

Per-resource, and this is the discipline the task turned on — **`D-32`**:

| resource | reports WWOX? | sampled a postnatal germinal zone? | readable as absence? |
|---|---|---|---|
| Human Brain Transcriptome | 🟢 yes, human, conception→adult | 🔴 **no** — NCX/HIP/AMY/STR/MD/CBC, all parenchymal | ⛔ **no** |
| BrainSpan / Allen developmental | 🟡 one record, **8–37 pcw = prenatal** | 🔴 no | ⛔ no |
| GTEx (**already local**) | 🟢 yes | 🔴 **no — adult only** | ⛔ no |
| Human Protein Atlas | ⚠️ unverified (host 403) | 🔴 no — adult, 10 major regions | ⛔ no |
| Allen **Mouse** ISH | 🟢 yes (medial EC L2, BLA, isocortex L5, cerebellum) | 🔴 no — **mouse, adult**, and the mouse has no MMS | ⛔ no |
| BrainRNAseq mouse P7 | 🟢 yes, **postnatal**, highest in **progenitor** oligodendrocytes | 🟡 no SVZ, but a real progenitor-vs-mature contrast | ⛔ no |
| DropViz (mouse adult) | 🟢 yes; ⚠️ ependymal + choroid plexus **"data not shown"** | 🔴 no | ⛔ no |

🔵 **Local-first check paid off:** `analysis/data/WWOX_tissue_expression_GTEx.csv` cross-validates
against published GTEx medians exactly (Cerebellar_Hemisphere 12.1278 vs 12.1; Frontal_Cortex_BA9
6.8204 vs 6.9) — **and has no germinal-zone row, because GTEx has none.**

---

## 2 · 🎯 The prize: a two-week-old human dataset exists, and WWOX was never asked

**PMID 38122823** — Nascimento *et al.* 2023, *Nature*
([DOI](https://doi.org/10.1038/s41586-023-06981-x), `PMC10901738`). **Body retrieved and searched by
the Orchestrator.** Verbatim:

> *"To characterize the identity of the migrating neurons in the EC stream, **we microdissected this
> region from a two-week-old sample and performed single-nucleus RNA sequencing (snRNA-seq)**."*

> *"Notably, **our snRNA-seq of the stream captured a cluster that expressed RG markers**…, distinct
> from a cluster of differentiated astrocytes."*

🔴 **And `WWOX` occurs ZERO times in the served full text** — confirmed by direct count, not taken
from the hand-back.

**So: right species, right compartment, a radial-glia cluster captured, and an age of two weeks —
inside the WOREE presentation window (median 5 weeks). The gene was simply never queried.**

⚠️ **Bounds, all of which must travel:** `n = 1` postnatal donor; the study's dedicated
*germinal-zone* samples are **gestational** (only the stream and the EC are postnatal); the body was
served **without figures or supplements**, so a WWOX row in a supplement would not have been seen.
🔴 **And the decisive caveat:** a **per-nucleus zero at ~6 TPM bulk is uninterpretable without a
matched-abundance dropout control.** snRNA-seq dropout would make a naive *"WWOX absent"* reading
meaningless. Any reanalysis must carry that control or it produces nothing.

⛔ **No GEO or dbGaP accession is in the body as served** — the data-availability statement is
deferred to the publisher DOI, behind the 403. **The delegate named no accession and reconstructed
none; neither do I.** Obtaining it is the single artefact that converts a tissue request into a desk
reanalysis.

> **The headline correction to yesterday's framing: this gap was named as needing banked human
> tissue. It does not — at least not first.**

---

## 3 · 🔴 The delegate's contradiction C-1 is DOWNGRADED — I read the source and it says both

Scientist K reported that the repository records the HBT human readout as **FLAT** while Aldaz 2020
describes a **U-shape**, and called it *"two secondary descriptions of one database disagreeing about
its shape."*

**Verified in `PMC7727818`, and the quoted clause is accurate but incomplete.** The full sentence
begins one clause earlier:

> *"mRNA expression is **quite uniform from conception to adulthood in all depicted brain regions**…
> All regions show relatively higher expression levels in early embryonal life **slowly** decreasing
> during fetal development until birth to **slightly** increase again … in postnatal life and early
> childhood up to adolescence…, **remaining quite stable thereafter**."*

🔵 **So Aldaz 2020 says both.** *"Quite uniform"* is the authors' own headline; the dip and rise are
described as **slow** and **slight** modulations *within* that uniformity. **The repository's `FLAT`
record is therefore not wrong** — it captured the headline. What it lacks is the modulation.

**Proposed:** add the modulation to `wwox_developmental_timing_audit_20260920.md` as a refinement,
**not** as the resolution of a disagreement. ⚠️ **And neither description is a measurement by its
author** — both are secondary readings of one array database, and mRNA ≠ protein for this gene.

---

## 4 · Three things in those bodies that nobody flagged

**(a) 🎯 The cerebellar exception is a real directional postnatal finding**, verbatim:

> *"expression in cerebellar cortex (red line) **clearly behaves differently showing a more
> significant increase in early postnatal life** and remaining higher (compared to other tissues) up
> to adolescence."*

🔵 **This is the one region where the human data point the favourable way for a post-diagnosis
window** — and it is the **same region** that carries `TX-007`'s under-expression/biodistribution
signal. **Two independent reasons to keep the cerebellar axis separate**, now pointing in opposite
directions: expression rises postnatally there, and vector coverage is reported weakest there.
Worth recording; **not** worth a therapeutic inference.

**(b) 🔴 A THIRD transmission of the mouse audiogenic claim, first-person, from the lab itself:**

> *"In the study of Mallaret et al. … **we described that [Wwox-null] mice display spontaneous and
> audiogenic tonic-clonic seizures at a very early age** as well as ataxic gait and decreased
> mobility, matching observations in [lde] rats."*

So the claim has now been transmitted **three times** — Mallaret's abstract, a *Brain* commentary,
and this 2020 review — **twice in the first person by its own authors, and a method has never been
published anywhere.** This strengthens, and does not disturb, the note landed on `CLAIM 037` today:
*documented* rat-specific, *asserted* for the mouse at abstract depth, with no `n`, no strain, no
stimulus protocol and no control readable. **The `REVIVAL_TRIGGER` stands.**

**(c) 🔴 Two sources disagree about `G372R` protein level — and the allelic series uses one of them.**
Aldaz 2020, verbatim:

> *"Analysis from patient fibroblasts showed that **both described missense mutations do not alter
> WWOX protein expression** and instead result in the production of a defective, partially functional
> WWOX protein (i.e., **hypomorphic mutations**)."*

That is `P47T` **and `G372R`** with **unaltered** protein. But `DL-MECH-033`/`DL-MECH-037`'s allelic
series records `G372R` as ***"barely any signal"*** (Steinberg, **IF in organoids**). ⚠️ **Different
matrices and different methods** — patient fibroblast Western versus organoid immunofluorescence,
which the ledger already declares *"non confrontabili quantitativamente"*. **Flagged, not resolved,
and it matters:** `G372R` is the *"superficial residue, nearly absent protein, mild phenotype"*
data point that `DL-MECH-037`'s burial argument leans on. **If its protein is in fact normal, that
row changes, and the argument that burial discriminates gets simpler rather than weaker** — P47T and
G372R would both be surface, both protein-normal, both mild, against buried Q230P with absent
protein. **Not asserted. Queued.**

---

## 5 · Query census, and why its zeros are usable

All zeros carry **correctly expanded** `query_translation` (the `wwox protein human` Supplementary
Concept fired; `subventricular zone` → `"lateral ventricles"[MeSH]`): `WWOX AND subventricular
zone` **0** · `rostral migratory stream` **0** · `germinal zone` **0** · `"postnatal neurogenesis"`
**0** · `(ganglionic eminence OR doublecortin OR olfactory bulb OR neuroblast OR interneuron
migration)` **0**.

🔵 **One query was discarded as uninformative rather than counted:** `WWOX AND ventricular zone`
expands to **`"heart ventricles"[MeSH]`** — a wrong expansion, so not evidence. **That is the
`query_translation` rule being used correctly rather than recited.** Positive controls:
`postnatal neurogenesis AND subventricular zone` **580** · `WWOX AND neurogenesis` **5** ·
`WWOX AND infant brain` **17**.

⚠️ **Standing limit, correctly stated by the delegate:** `[All Fields]` does not index Methods or
supplements, so these zeros mean *"nobody framed a paper around it"*, **never** *"the datum does not
exist"* — which is exactly what §2 then demonstrates, in the strongest possible way: the dataset
exists and no query could have found WWOX in it.

---

## 6 · What would close the gap, cheapest first

**Desk:** **D1** read WWOX out of the Nascimento snRNA-seq object — hours, and it would be the
**first WWOX measurement in a human postnatal periventricular compartment** — 🔴 **requires the
matched-abundance dropout control and the accession, neither of which we have yet.** **D2** arbitrate
§3's modulation from the Aldaz figure this repository has already inspected — **~1 hour, zero
external access.** **D3** HPA brain/single-cell plus its manifest (403 today). **D4** Allen prenatal
germinal-zone series — prenatal, valuable only as proof WWOX is detectable in a germinal-zone
dissection at all.

**Tissue:** **T1** WWOX IHC on the **already-banked** Paredes postnatal SVZ/Arc series (birth, 1,
1.5, 3, 5, 7 months, 2 y, 6 y, 15 y), co-stained with DCX/PSA-NCAM — **one added antibody on
existing slides.** ⛔ **T3 (new prospective collection) should not be proposed while T1 is
unattempted.**

**BLOCK-1 observed throughout: no molecule, no dose, no route, no safety claim. Nothing here is
medical advice.**
